#!/usr/bin/env python3
"""Sync Google Classroom (+ Drive) into the vault's SOURCE folders.

Sources land in  <area>/<topic>/<subdir>/   (default subdir: lecture-notes-slides)
and every topic folder gets  <area>/<topic>/classroom-sources.json  recording, for each
file and each post, which Classroom course / post it came from.

Nothing in the numbered vault folders and nothing in Kurooto's course folders
(introduction-to-climate-science/, ph2113/, ...) is read or written.

Usage (always with the vault venv):
  .venv/bin/python scripts/classroom_sync.py auth          # one-time browser login
  .venv/bin/python scripts/classroom_sync.py courses       # list courses + current mapping
  .venv/bin/python scripts/classroom_sync.py fetch [--dry-run] [--since YYYY-MM-DD] [--course ID]
  .venv/bin/python scripts/classroom_sync.py drive-ls [FOLDER_ID]   # browse Drive to pick book folders

Duplicate rule ("whatever is already in the vault is skipped"):
  1. a Drive file id already recorded in classroom-sources.json  -> skip
  2. a local file under the topic folder (any subfolder, books included) with the same
     size + md5 as the Drive file                                -> skip, recorded as already-present
  3. a local file with the same normalised name                  -> skip, recorded as already-present (name)
     (Google-native Docs/Slides have no md5, so name is the only test for them)
Secrets live in ~/.config/vault-sync/ (client_secret.json, token.json), never in the repo,
because the repo is auto-pushed to GitHub.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import io
import json
import os
import re
import sys
import unicodedata
from pathlib import Path

os.environ.setdefault("OAUTHLIB_RELAX_TOKEN_SCOPE", "1")  # Google renames scope aliases
ROOT = Path(__file__).resolve().parent.parent
CFG_PATH = ROOT / "scripts" / "classroom_sync_config.json"
SECRET_DIR = Path.home() / ".config" / "vault-sync"
CLIENT_SECRET = SECRET_DIR / "client_secret.json"
TOKEN = SECRET_DIR / "token.json"
REPORT_DIR = ROOT / "scripts" / "_work" / "classroom"
META_NAME = "classroom-sources.json"
GIT_LIMIT = 95 * 1024 * 1024  # files above this are added to .gitignore (GitHub hard limit is 100 MB)

SCOPES = [
    "https://www.googleapis.com/auth/classroom.courses.readonly",
    "https://www.googleapis.com/auth/classroom.announcements.readonly",
    "https://www.googleapis.com/auth/classroom.student-submissions.me.readonly",  # = coursework.me.readonly
    "https://www.googleapis.com/auth/classroom.courseworkmaterials.readonly",
    "https://www.googleapis.com/auth/classroom.topics.readonly",
    "https://www.googleapis.com/auth/drive.readonly",
]
EXPORT = {  # Google-native files -> downloadable format
    "application/vnd.google-apps.document": ("application/pdf", ".pdf"),
    "application/vnd.google-apps.presentation": ("application/pdf", ".pdf"),
    "application/vnd.google-apps.spreadsheet": (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".xlsx"),
    "application/vnd.google-apps.drawing": ("application/pdf", ".pdf"),
}
SKIP_DIRS = {".git", ".obsidian", ".venv", "__pycache__"}


# ---------------------------------------------------------------- auth / services
def credentials(interactive: bool = False):
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials

    creds = None
    if TOKEN.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if creds and creds.valid:
        return creds
    if creds and creds.expired and creds.refresh_token:
        try:
            creds.refresh(Request())
            TOKEN.write_text(creds.to_json())
            TOKEN.chmod(0o600)
            return creds
        except Exception as e:  # revoked / expired refresh token
            print(f"token refresh failed ({e}); re-authorising", file=sys.stderr)
    if not interactive:
        sys.exit("No valid token. Run:  .venv/bin/python scripts/classroom_sync.py auth")
    from google_auth_oauthlib.flow import InstalledAppFlow

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT_SECRET), SCOPES)
    creds = flow.run_local_server(
        port=0, open_browser=True,
        authorization_prompt_message="Open this URL in your browser to authorise:\n{url}\n",
        success_message="Vault sync authorised; you can close this tab.")
    TOKEN.write_text(creds.to_json())
    TOKEN.chmod(0o600)
    return creds


def services():
    from googleapiclient.discovery import build

    c = credentials()
    return (build("classroom", "v1", credentials=c, cache_discovery=False),
            build("drive", "v3", credentials=c, cache_discovery=False))


def paged(method, key, **kw):
    token = None
    while True:
        resp = method(pageToken=token, **kw).execute()
        yield from resp.get(key, [])
        token = resp.get("nextPageToken")
        if not token:
            return


# ---------------------------------------------------------------- config / metadata
def load_cfg() -> dict:
    if CFG_PATH.exists():
        return json.loads(CFG_PATH.read_text())
    return {"first_run_since": "2026-11-05", "last_sync": None, "courses": {}, "drive_folders": []}


def save_cfg(cfg: dict) -> None:
    CFG_PATH.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n")


def load_meta(topic_dir: Path) -> dict:
    p = topic_dir / META_NAME
    if p.exists():
        meta = json.loads(p.read_text())
        meta.setdefault("resources", [])
        return meta
    return {"_about": "Written by scripts/classroom_sync.py: which Classroom course/post (or Drive folder) "
                      "each source file in this topic folder came from, every post's text, and every "
                      "resource a post POINTS to (website, Dropbox, sheet, book pages) with its status. "
                      "Edit statuses with `classroom_sync.py mark`.",
            "files": [], "posts": [], "resources": []}


def save_meta(topic_dir: Path, meta: dict) -> None:
    meta["files"].sort(key=lambda r: (r.get("posted") or "", r.get("file") or ""))
    meta["posts"].sort(key=lambda r: r.get("posted") or "")
    meta.setdefault("resources", []).sort(key=lambda r: r.get("posted") or "")
    (topic_dir / META_NAME).write_text(json.dumps(meta, indent=2, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- local index
def norm_name(name: str) -> str:
    stem = Path(name).stem
    stem = unicodedata.normalize("NFKC", stem).lower()
    stem = re.sub(r"\s*\(\d+\)$", "", stem)          # "file (1)"
    stem = re.sub(r"[\s_\-.]+", "", stem)
    return stem


class LocalIndex:
    """Files already present under a topic folder (all subfolders, books included)."""

    def __init__(self, topic_dir: Path):
        self.by_size: dict[int, list[Path]] = {}
        self.by_name: dict[str, Path] = {}
        self._md5: dict[Path, str] = {}
        if topic_dir.exists():
            for p in topic_dir.rglob("*"):
                if p.is_file() and not (set(p.relative_to(topic_dir).parts) & SKIP_DIRS) and p.name != META_NAME:
                    self.add(p)

    def add(self, p: Path):
        self.by_size.setdefault(p.stat().st_size, []).append(p)
        self.by_name.setdefault(norm_name(p.name), p)

    def md5(self, p: Path) -> str:
        if p not in self._md5:
            h = hashlib.md5()
            with p.open("rb") as f:
                for chunk in iter(lambda: f.read(1 << 20), b""):
                    h.update(chunk)
            self._md5[p] = h.hexdigest()
        return self._md5[p]

    def match(self, size: int | None, md5: str | None, name: str) -> tuple[Path | None, str]:
        if size is not None and md5:
            for p in self.by_size.get(size, []):
                if self.md5(p) == md5:
                    return p, "md5"
        p = self.by_name.get(norm_name(name))
        if p is not None and not md5:      # Google-native file: name is the only test
            return p, "name"
        if p is not None:                  # same name, different bytes: keep both, flag it
            return None, f"name-clash:{p.name}"
        return None, ""


# ---------------------------------------------------------------- classroom fetch
def ts(s: str | None) -> dt.datetime | None:
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


def post_title(kind: str, item: dict) -> str:
    if item.get("title"):
        return item["title"]
    text = (item.get("text") or "").strip().splitlines()
    return (text[0][:90] if text else f"{kind} {item.get('id')}")


DRIVE_LINK = re.compile(r"(?:drive|docs)\.google\.com/(?:file/d/|open\?id=|document/d/|presentation/d/|spreadsheets/d/)([\w-]{20,})")


def materials_of(item: dict) -> tuple[list[dict], list[dict]]:
    """-> (drive files [{id,title}], other links [{type,url,title}])"""
    drive, links = [], []
    for m in item.get("materials", []) or []:
        if "driveFile" in m:
            f = m["driveFile"].get("driveFile", m["driveFile"])
            drive.append({"id": f["id"], "title": f.get("title", f["id"])})
        elif "link" in m:
            url = m["link"].get("url", "")
            mm = DRIVE_LINK.search(url)
            if mm:
                drive.append({"id": mm.group(1), "title": m["link"].get("title") or mm.group(1)})
            else:
                links.append({"type": "link", "url": url, "title": m["link"].get("title", "")})
        elif "youtubeVideo" in m:
            v = m["youtubeVideo"]
            links.append({"type": "youtube", "url": v.get("alternateLink", ""), "title": v.get("title", "")})
        elif "form" in m:
            f = m["form"]
            links.append({"type": "form", "url": f.get("formUrl", ""), "title": f.get("title", "")})
    # Drive links pasted in the post text
    for mm in DRIVE_LINK.finditer(item.get("text", "") or item.get("description", "") or ""):
        if mm.group(1) not in {d["id"] for d in drive}:
            drive.append({"id": mm.group(1), "title": None})
    return drive, links


URL_RE = re.compile(r"https?://[^\s<>()\"']+")
BOOK_RE = re.compile(
    r"[^.\n]*(?:\bbook\b|\bedition\b|\btext ?books?\b|\bchapter\b|\bch\.\s*\d|\bsection\b|§)[^.\n]*"
    r"(?:\bpages?\b|\bpp?\.?\s*\d|\bchapter\s*\d|\bsection\s*\d|§\s*\d)[^\n]*", re.I)


def classify_url(u: str) -> str:
    u2 = u.lower()
    if "dropbox.com" in u2: return "dropbox"
    if "github.io" in u2 or "github.com" in u2: return "website"
    if "docs.google.com/spreadsheets" in u2: return "google-sheet"
    if "docs.google.com/forms" in u2 or "forms.gle" in u2: return "form"
    if DRIVE_LINK.search(u): return "drive"
    if "youtu" in u2: return "youtube"
    if u2.endswith(".pdf"): return "pdf-link"
    return "website"


def resource_refs(post: dict) -> list[dict]:
    """Everything a post points to that is not an attached Drive file."""
    refs, text = [], post.get("text") or ""
    for l in post.get("links", []):
        refs.append({"kind": l["type"] if l["type"] != "link" else classify_url(l["url"]),
                     "target": l["url"], "label": l.get("title") or ""})
    for u in URL_RE.findall(text):
        u = u.rstrip(".,;:")
        if classify_url(u) == "drive":
            continue
        if u not in {r["target"] for r in refs}:
            refs.append({"kind": classify_url(u), "target": u, "label": ""})
    for m in BOOK_RE.finditer(text):
        refs.append({"kind": "book-pages", "target": m.group(0).strip(), "label": ""})
    return refs


def merge_resources(meta: dict, post: dict, course: str) -> int:
    have = {(r["kind"], r["target"]) for r in meta["resources"]}
    n = 0
    for r in resource_refs(post):
        if (r["kind"], r["target"]) in have:
            continue
        rid = hashlib.sha1(f"{r['kind']}|{r['target']}".encode()).hexdigest()[:8]
        meta["resources"].append({"id": rid, **r, "course": course, "post_id": post["post_id"],
                                  "post_title": post["title"], "posted": post["posted"],
                                  "status": "pending", "local": None, "note": None})
        have.add((r["kind"], r["target"]))
        n += 1
    return n


def course_posts(cls, course_id: str, since: dt.datetime) -> list[dict]:
    topics = {}
    try:
        topics = {t["topicId"]: t["name"] for t in paged(cls.courses().topics().list, "topic", courseId=course_id)}
    except Exception:
        pass
    out = []
    feeds = [
        ("announcement", cls.courses().announcements().list, "announcements"),
        ("coursework", cls.courses().courseWork().list, "courseWork"),
        ("material", cls.courses().courseWorkMaterials().list, "courseWorkMaterial"),
    ]
    for kind, method, key in feeds:
        try:
            items = list(paged(method, key, courseId=course_id))
        except Exception as e:
            print(f"  ! {kind}: {e}", file=sys.stderr)
            continue
        for it in items:
            created, updated = ts(it.get("creationTime")), ts(it.get("updateTime"))
            when = max(t for t in (created, updated) if t)
            if when < since:
                continue
            drive, links = materials_of(it)
            out.append({
                "post_id": it["id"], "post_type": kind, "title": post_title(kind, it),
                "text": (it.get("text") or it.get("description") or "").strip(),
                "posted": (created or updated).isoformat(), "updated": (updated or created).isoformat(),
                "topic": topics.get(it.get("topicId")), "url": it.get("alternateLink"),
                "due": it.get("dueDate"), "work_type": it.get("workType"),
                "drive": drive, "links": links,
            })
    out.sort(key=lambda p: p["posted"])
    return out


# ---------------------------------------------------------------- drive
def drive_meta(drv, file_id: str) -> dict | None:
    try:
        return drv.files().get(fileId=file_id, supportsAllDrives=True,
                               fields="id,name,mimeType,size,md5Checksum,modifiedTime,shortcutDetails").execute()
    except Exception as e:
        print(f"    ! cannot read Drive file {file_id}: {e}", file=sys.stderr)
        return None


def safe_name(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|\x00-\x1f]', "_", name).strip().strip(".")
    return name or "untitled"


def target_name(meta: dict) -> str:
    name = meta["name"]
    if meta["mimeType"] in EXPORT:
        ext = EXPORT[meta["mimeType"]][1]
        if not name.lower().endswith(ext):
            name += ext
    return safe_name(name)


def download(drv, meta: dict, dest: Path) -> None:
    from googleapiclient.http import MediaIoBaseDownload

    if meta["mimeType"] in EXPORT:
        req = drv.files().export_media(fileId=meta["id"], mimeType=EXPORT[meta["mimeType"]][0])
    else:
        req = drv.files().get_media(fileId=meta["id"], supportsAllDrives=True)
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".part")
    with tmp.open("wb") as fh:
        dl = MediaIoBaseDownload(fh, req, chunksize=16 << 20)
        done = False
        while not done:
            _, done = dl.next_chunk()
    tmp.rename(dest)


def unique_path(p: Path) -> Path:
    if not p.exists():
        return p
    i = 2
    while True:
        q = p.with_name(f"{p.stem} ({i}){p.suffix}")
        if not q.exists():
            return q
        i += 1


def gitignore_large(paths: list[Path]) -> None:
    big = [p for p in paths if p.exists() and p.stat().st_size > GIT_LIMIT]
    if not big:
        return
    gi = ROOT / ".gitignore"
    have = gi.read_text().splitlines()
    new = [str(p.relative_to(ROOT)) for p in big if str(p.relative_to(ROOT)) not in have]
    if new:
        gi.write_text(gi.read_text().rstrip("\n") + "\n# >95 MB, added by classroom_sync.py\n" + "\n".join(new) + "\n")


def handle_drive_file(drv, fid, title_hint, topic_dir, subdir, index, meta, provenance, dry, log, fetched):
    known = {r.get("drive_id") for r in meta["files"]}
    if fid in known:
        log.append(f"    = {title_hint or fid}: already synced")
        return
    dm = drive_meta(drv, fid)
    if dm is None:
        log.append(f"    ! {title_hint or fid}: not readable from Drive (permissions?)")
        return
    if dm["mimeType"] == "application/vnd.google-apps.shortcut":
        dm = drive_meta(drv, dm["shortcutDetails"]["targetId"]) or dm
    if dm["mimeType"] == "application/vnd.google-apps.folder":
        log.append(f"    > folder {dm['name']}: walking")
        for child in paged(drv.files().list, "files", q=f"'{dm['id']}' in parents and trashed=false",
                           fields="nextPageToken,files(id,name)", supportsAllDrives=True,
                           includeItemsFromAllDrives=True):
            handle_drive_file(drv, child["id"], child["name"], topic_dir, subdir, index, meta,
                              provenance, dry, log, fetched)
        return
    if dm["mimeType"].startswith("application/vnd.google-apps.") and dm["mimeType"] not in EXPORT:
        log.append(f"    ! {dm['name']}: Google {dm['mimeType'].rsplit('.', 1)[-1]} cannot be exported; link recorded")
    name = target_name(dm)
    size = int(dm["size"]) if dm.get("size") else None
    hit, how = index.match(size, dm.get("md5Checksum"), name)
    rec = {"drive_id": dm["id"], "drive_name": dm["name"], "drive_modified": dm.get("modifiedTime"),
           "md5": dm.get("md5Checksum"), **provenance}
    if hit is not None:
        rec.update(file=str(hit.relative_to(topic_dir)), status=f"already-present ({how})")
        log.append(f"    = {name}: already in vault as {hit.relative_to(topic_dir)} ({how})")
    else:
        dest = unique_path(topic_dir / subdir / name)
        rec.update(file=str(dest.relative_to(topic_dir)), status="downloaded")
        if how.startswith("name-clash"):
            rec["note"] = f"same name as existing {how.split(':', 1)[1]} but different content"
            log.append(f"    ! {name}: same name as an existing file, different content; kept both")
        if dry:
            log.append(f"    + {name}  -> {dest.relative_to(ROOT)}  [dry run]")
        else:
            download(drv, dm, dest)
            index.add(dest)
            fetched.append(dest)
            log.append(f"    + {name}  -> {dest.relative_to(ROOT)}")
    meta["files"].append(rec)


# ---------------------------------------------------------------- commands
def cmd_auth(_):
    if not CLIENT_SECRET.exists():
        sys.exit(f"Put the OAuth client JSON at {CLIENT_SECRET}")
    credentials(interactive=True)
    print(f"OK: token saved to {TOKEN}")


def cmd_courses(_):
    cls, _drv = services()
    cfg = load_cfg()
    for c in paged(cls.courses().list, "courses", studentId="me", pageSize=100):
        m = cfg["courses"].get(c["id"], {})
        print(f"{c['id']}\t{c.get('courseState')}\t{c['name']} | {c.get('section', '')}\t-> {m.get('topic', '(unmapped)')}")


def cmd_drive_ls(args):
    _cls, drv = services()
    parent = args.folder or "root"
    q = f"'{parent}' in parents and trashed=false"
    for f in paged(drv.files().list, "files", q=q, orderBy="folder,name",
                   fields="nextPageToken,files(id,name,mimeType,size)", supportsAllDrives=True,
                   includeItemsFromAllDrives=True, pageSize=200):
        kind = "DIR " if f["mimeType"].endswith("folder") else "    "
        print(f"{kind}{f['id']}\t{f['name']}\t{f.get('size', '')}")


def cmd_fetch(args):
    cfg = load_cfg()
    since_s = args.since or (cfg.get("last_sync") or cfg["first_run_since"])
    since = ts(since_s if "T" in since_s else since_s + "T00:00:00+00:00")
    if cfg.get("last_sync") and not args.since:
        since -= dt.timedelta(days=1)  # overlap; dedupe makes it free
    started = dt.datetime.now(dt.timezone.utc)
    cls, drv = services()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    log, fetched, report = [f"# Classroom sync {started:%Y-%m-%d %H:%M} UTC (since {since:%Y-%m-%d})", ""], [], []

    for cid, cm in cfg["courses"].items():
        if args.course and cid != args.course:
            continue
        if not cm.get("topic"):
            continue
        topic_dir = ROOT / cm["topic"]
        subdir = cm.get("subdir", "lecture-notes-slides")
        meta, index = load_meta(topic_dir), LocalIndex(topic_dir)
        seen_posts = {p["post_id"] for p in meta["posts"]}
        log.append(f"## {cm['name']}  ->  {cm['topic']}/{subdir}")
        posts = course_posts(cls, cid, since)
        new_posts = 0
        for p in posts:
            log.append(f"- [{p['posted'][:10]}] {p['post_type']}: {p['title']}" + (f"  (topic: {p['topic']})" if p['topic'] else ""))
            prov = {"course": cm["name"], "course_id": cid, "post_id": p["post_id"], "post_type": p["post_type"],
                    "post_title": p["title"], "posted": p["posted"], "classroom_topic": p["topic"]}
            for d in p["drive"]:
                handle_drive_file(drv, d["id"], d["title"], topic_dir, subdir, index, meta, prov,
                                  args.dry_run, log, fetched)
            for l in p["links"]:
                log.append(f"    ~ {l['type']}: {l['title']} {l['url']}")
            if merge_resources(meta, p, cm["name"]):
                for r in meta["resources"]:
                    if r["post_id"] == p["post_id"] and r["status"] == "pending":
                        log.append(f"    ? RESOURCE [{r['id']}] {r['kind']}: {r['target'][:140]}")
            if p["post_id"] not in seen_posts:
                new_posts += 1
                meta["posts"].append({k: p[k] for k in ("post_id", "post_type", "title", "text", "posted", "updated",
                                                       "topic", "url", "due", "work_type", "links")}
                                     | {"course": cm["name"], "course_id": cid,
                                        "drive_ids": [d["id"] for d in p["drive"]]})
                report.append({"course": cm["name"], "topic_dir": cm["topic"], **p})
        log.append(f"  ({len(posts)} posts since cutoff, {new_posts} not seen before)\n")
        if not args.dry_run:
            save_meta(topic_dir, meta)

    # optional Drive folders (books / resource dumps) mapped to topic folders
    for df in cfg.get("drive_folders", []):
        topic_dir = ROOT / df["topic"]
        meta, index = load_meta(topic_dir), LocalIndex(topic_dir)
        log.append(f"## Drive folder {df.get('name', df['id'])}  ->  {df['topic']}/{df.get('subdir', 'books')}")
        prov = {"course": df.get("course"), "drive_folder": df["id"], "posted": None, "post_type": "drive-folder"}
        handle_drive_file(drv, df["id"], df.get("name"), topic_dir, df.get("subdir", "books"), index, meta, prov,
                          args.dry_run, log, fetched)
        if not args.dry_run:
            save_meta(topic_dir, meta)

    if not args.dry_run:
        gitignore_large(fetched)
        if not args.course and not args.since:
            cfg["last_sync"] = started.isoformat()
            save_cfg(cfg)
    stamp = f"{started:%Y-%m-%d-%H%M}" + ("-dry" if args.dry_run else "")
    (REPORT_DIR / f"sync-{stamp}.md").write_text("\n".join(log) + "\n")
    (REPORT_DIR / f"sync-{stamp}.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print("\n".join(log))
    print(f"\n{len(fetched)} files downloaded; report: {REPORT_DIR.relative_to(ROOT)}/sync-{stamp}.md/.json")


def topic_dirs(cfg):
    seen = set()
    for cm in list(cfg["courses"].values()) + cfg.get("drive_folders", []):
        if cm.get("topic") and cm["topic"] not in seen:
            seen.add(cm["topic"]); yield ROOT / cm["topic"]


def cmd_pending(_):
    for td in topic_dirs(load_cfg()):
        meta = load_meta(td)
        for r in meta["resources"]:
            if r["status"] == "pending":
                print(f"{td.relative_to(ROOT)}\t[{r['id']}] {r['kind']}\t{r['posted'][:10]}\t{r['target'][:160]}")


def cmd_add(args):
    """Record a resource a post mentions without a URL (e.g. 'the course website is updated')."""
    td = ROOT / args.topic
    meta = load_meta(td)
    post = next((p for p in meta["posts"] if p["post_id"] == args.post_id), None)
    if post is None:
        sys.exit(f"no post {args.post_id} in {td}")
    fake = {"post_id": post["post_id"], "title": post["title"], "posted": post["posted"],
            "links": [{"type": args.kind, "url": args.target, "title": args.label or ""}], "text": ""}
    merge_resources(meta, fake, post["course"])
    save_meta(td, meta)
    print("ok")


def cmd_ingest(args):
    """Copy (or --move) local files into <topic>/<dest>, md5-deduped against the whole topic folder,
    and record each in classroom-sources.json (origin = where it came from)."""
    import shutil
    td = ROOT / args.topic
    meta, index = load_meta(td), LocalIndex(td)
    src = Path(args.src).expanduser()
    files = [src] if src.is_file() else sorted(p for p in src.rglob("*") if p.is_file())
    added = skipped = 0
    for f in files:
        size = f.stat().st_size
        h = hashlib.md5(f.read_bytes()).hexdigest() if size < (2 << 30) else None
        hit, how = index.match(size, h, f.name)
        rel = f.relative_to(src) if (args.keep_tree and src.is_dir()) else Path(f.name)
        rec = {"origin": args.origin or str(f), "md5": h, "resource_id": args.resource,
               "course": args.course, "posted": args.date, "post_type": "ingest"}
        if hit is not None:
            skipped += 1
            print(f"= {rel}: already present as {hit.relative_to(td)} ({how})")
            if not any(r.get("file") == str(hit.relative_to(td)) for r in meta["files"]):
                meta["files"].append({**rec, "file": str(hit.relative_to(td)), "status": f"already-present ({how})"})
            if args.move and how == "md5":
                f.unlink()  # identical copy already in the vault
            continue
        dest = unique_path(td / args.dest / rel)
        dest.parent.mkdir(parents=True, exist_ok=True)
        (shutil.move if args.move else shutil.copy2)(str(f), str(dest))
        index.add(dest)
        meta["files"].append({**rec, "file": str(dest.relative_to(td)), "status": "moved" if args.move else "copied"})
        added += 1
        print(f"+ {rel} -> {dest.relative_to(ROOT)}")
    save_meta(td, meta)
    gitignore_large([td / r["file"] for r in meta["files"] if (td / r["file"]).exists()])
    print(f"{added} added, {skipped} already present")


def render_site_pages(site, repo, dest):
    """Offline copy of a Jekyll/GitHub-Pages site: for every Markdown page in the repo (front matter with a layout), save the
    live rendered HTML as index.html next to it, with site-absolute links made relative and directory links pointed at
    index.html, so the pages open from disk. Keeps the previous copy if the live site is gone."""
    import urllib.request, urllib.parse, posixpath
    base = site["url"].rstrip("/") + "/"
    basepath = urllib.parse.urlparse(base).path            # e.g. /intro_climate_science/
    done = []
    for md in sorted(repo.rglob("*.md")):
        rel = md.relative_to(repo)
        if ".git" in rel.parts or rel.name.upper() == "README.MD" or not md.read_text(errors="ignore").startswith("---"):
            continue
        page_dir = rel.parent.as_posix()
        page_dir = "" if page_dir == "." else page_dir + "/"
        url = base + page_dir if rel.name == "index.md" else base + rel.with_suffix(".html").as_posix()
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "vault-offline-mirror"})
            html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")
        except Exception as e:
            print(f"    ! could not fetch {url}: {e} (keeping any previous copy)")
            continue
        here = "/" + page_dir                                  # page location relative to site root
        def fix(m):
            attr, q, link = m.group(1), m.group(2), m.group(3)
            if link.startswith(basepath):
                target = "/" + link[len(basepath):]
            elif link.startswith(base):
                target = "/" + link[len(base):]
            elif re.match(r"^[a-z]+:|^#|^//", link):
                return m.group(0)
            else:
                target = posixpath.normpath(posixpath.join(here, link)) + ("/" if link.endswith("/") else "")
            path, _, frag = target.partition("#")
            if path.endswith("/") or path == "":
                path = path + "index.html"
            relpath = posixpath.relpath(path, here.rstrip("/") or "/")
            return f'{attr}={q}{relpath}{"#" + frag if frag else ""}{q}'
        html = re.sub(r'(href|src)=(["\'])([^"\']+)\2', fix, html)
        out = dest / (page_dir + ("index.html" if rel.name == "index.md" else rel.with_suffix(".html").name))
        out.parent.mkdir(parents=True, exist_ok=True)
        if not out.exists() or out.read_text(errors="ignore") != html:
            out.write_text(html)
            done.append(str(out.relative_to(dest)))
    return [f"(rendered) {d}" for d in done]


def cmd_sites(args):
    """git clone/pull each course website repo and copy new/changed files into the source mirror
    (rsync without --delete: nothing already in the vault is removed). Changed files are logged."""
    import subprocess
    cfg = load_cfg()
    cache = REPORT_DIR.parent / "sites"
    cache.mkdir(parents=True, exist_ok=True)
    for site in cfg.get("sites", []):
        repo = cache / site["name"]
        if (repo / ".git").exists():
            subprocess.run(["git", "-C", str(repo), "pull", "-q", "--ff-only"], check=True)
        else:
            subprocess.run(["git", "clone", "-q", "--depth", "1", site["repo"], str(repo)], check=True)
        head = subprocess.run(["git", "-C", str(repo), "log", "-1", "--format=%h %cI %s"],
                              capture_output=True, text=True).stdout.strip()
        td = ROOT / site["topic"]
        dest = td / site["dest"]
        cmd = ["rsync", "-rtc", "--itemize-changes"] + [f"--exclude={e}" for e in site.get("exclude", [])]
        if args.dry_run:
            cmd.append("-n")
        out = subprocess.run(cmd + [f"{repo}/", f"{dest}/"], capture_output=True, text=True, check=True).stdout
        changed = [l.split(" ", 1)[1] for l in out.splitlines() if l[:2] in (">f", "cd") and not l.endswith("/")]
        if site.get("render") and not args.dry_run:
            changed += render_site_pages(site, repo, dest)
        print(f"## site {site['name']} @ {head}: {len(changed)} new/changed files")
        for c in changed:
            print("   ", c)
        if not args.dry_run and changed:
            meta = load_meta(td)
            meta.setdefault("site_syncs", []).append({"site": site["url"], "repo_head": head,
                "synced": dt.datetime.now(dt.timezone.utc).isoformat(), "changed": changed})
            save_meta(td, meta)


def cmd_mark(args):
    td = ROOT / args.topic
    meta = load_meta(td)
    for r in meta["resources"]:
        if r["id"] == args.id:
            r["status"] = args.status
            if args.local: r["local"] = args.local
            if args.note: r["note"] = args.note
            save_meta(td, meta)
            print("ok", r)
            return
    sys.exit(f"no resource {args.id} in {td}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("auth").set_defaults(fn=cmd_auth)
    sub.add_parser("courses").set_defaults(fn=cmd_courses)
    d = sub.add_parser("drive-ls"); d.add_argument("folder", nargs="?"); d.set_defaults(fn=cmd_drive_ls)
    sub.add_parser("pending", help="list resources still to fetch/read").set_defaults(fn=cmd_pending)
    mk = sub.add_parser("mark", help="set a resource's status: fetched | read | skipped | admin")
    mk.add_argument("topic"); mk.add_argument("id"); mk.add_argument("status")
    mk.add_argument("--local"); mk.add_argument("--note"); mk.set_defaults(fn=cmd_mark)
    ad = sub.add_parser("add", help="record a resource a post points to without a link")
    ad.add_argument("topic"); ad.add_argument("post_id"); ad.add_argument("kind"); ad.add_argument("target")
    ad.add_argument("--label"); ad.set_defaults(fn=cmd_add)
    ig = sub.add_parser("ingest", help="copy/move local files into a topic folder with dedupe + metadata")
    ig.add_argument("topic"); ig.add_argument("src"); ig.add_argument("--dest", default="lecture-notes-slides")
    ig.add_argument("--keep-tree", action="store_true"); ig.add_argument("--move", action="store_true")
    ig.add_argument("--origin"); ig.add_argument("--resource"); ig.add_argument("--course"); ig.add_argument("--date")
    ig.set_defaults(fn=cmd_ingest)
    st = sub.add_parser("sites", help="pull course-website repos into their source mirrors")
    st.add_argument("--dry-run", action="store_true"); st.set_defaults(fn=cmd_sites)
    f = sub.add_parser("fetch")
    f.add_argument("--dry-run", action="store_true")
    f.add_argument("--since", help="YYYY-MM-DD; default: last_sync (or first_run_since on the first run)")
    f.add_argument("--course", help="only this course id")
    f.set_defaults(fn=cmd_fetch)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
