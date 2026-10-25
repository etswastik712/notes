"""Report unresolved [[wikilinks]], missing embeds/PDF files and canvas link problems for the NEW vault content.

    .venv/bin/python scripts/check_links.py [--all]
By default only the vault's own folders (00-Home, 0x-*, 1x-*, Assets) are scanned for links; the whole repo is indexed
so links into the source PDFs resolve.  Heading anchors (#Heading) are checked for notes; #page=N is checked for PDFs.
"""
import json
import os
import re
import sys

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP_DIRS = {".git", ".obsidian", ".venv", "node_modules", "build", "__pycache__"}
OWN = re.compile(r"^(00-Home|\d\d-[A-Za-z-]+|Assets)$")

files = {}      # lower-case basename -> [paths]
notes = {}      # lower-case note name or alias -> path
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    for f in fn:
        p = os.path.join(dp, f)
        files.setdefault(f.lower(), []).append(p)
        if f.endswith(".md"):
            name = f[:-3].lower()
            notes[name] = p
            if f.endswith(".excalidraw.md"):
                notes[f[:-3].lower()] = p
            try:
                txt = open(p, encoding="utf-8").read(4000)
                m = re.match(r"---\n(.*?)\n---", txt, re.S)
                if m:
                    fm = yaml.safe_load(m.group(1)) or {}
                    al = fm.get("aliases") or []
                    if isinstance(al, str):
                        al = [al]
                    for a in al:
                        notes.setdefault(str(a).lower(), p)
            except Exception:
                pass

LINK = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")


def strip_code(text):
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def headings(path):
    out = set()
    for line in open(path, encoding="utf-8"):
        m = re.match(r"#+\s+(.*)", line)
        if m:
            out.add(re.sub(r"[\s]+", " ", m.group(1).strip().lower()))
    return out


def check_target(raw, src, line, errs):
    raw = raw.replace("\\|", "|")
    target = raw.split("|")[0].strip()
    if not target:
        return
    base, _, frag = target.partition("#")
    base = base.strip()
    if not base:                      # same-note heading link
        return
    low = base.lower()
    ext = os.path.splitext(low)[1]
    if ext in (".pdf", ".png", ".jpg", ".jpeg", ".svg", ".canvas", ".gif", ".docx", ".mp4"):
        hits = files.get(os.path.basename(low))
        if not hits:
            errs.append((src, line, f"missing file: {base}"))
        elif ext == ".pdf" and frag.startswith("page="):
            n = int(re.match(r"page=(\d+)", frag).group(1))
            try:
                import fitz
                with fitz.open(hits[0]) as d:
                    if n > len(d):
                        errs.append((src, line, f"page {n} > {len(d)} in {base}"))
            except Exception:
                pass
        return
    p = notes.get(low) or notes.get(low.replace(".md", ""))
    if not p:
        errs.append((src, line, f"unresolved note: {base}"))
    elif frag and not frag.startswith(("page=", "^")) and p.endswith(".md"):
        if re.sub(r"[\s]+", " ", frag.strip().lower()) not in headings(p):
            errs.append((src, line, f"heading not found: {base}#{frag}"))


errs = []
scan_all = "--all" in sys.argv
count = 0
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d not in SKIP_DIRS]
    rel = os.path.relpath(dp, ROOT)
    top = rel.split(os.sep)[0]
    if not scan_all and not OWN.match(top):
        continue
    if rel.startswith(os.path.join("00-Home", "Templates")):
        continue
    for f in fn:
        p = os.path.join(dp, f)
        if f.endswith(".md") and not f.endswith(".excalidraw.md"):
            count += 1
            text = strip_code(open(p, encoding="utf-8").read())
            for i, line in enumerate(text.split("\n"), 1):
                for m in LINK.finditer(line):
                    check_target(m.group(2), os.path.relpath(p, ROOT), i, errs)
        elif f.endswith(".canvas"):
            count += 1
            try:
                d = json.load(open(p, encoding="utf-8"))
            except Exception as e:
                errs.append((os.path.relpath(p, ROOT), 0, f"invalid JSON: {e}"))
                continue
            ids = {n["id"] for n in d.get("nodes", [])}
            for n in d.get("nodes", []):
                for m in LINK.finditer(n.get("text", "") or ""):
                    check_target(m.group(2), os.path.relpath(p, ROOT), 0, errs)
                if n.get("type") == "file" and not os.path.exists(os.path.join(ROOT, n["file"])):
                    errs.append((os.path.relpath(p, ROOT), 0, f"missing canvas file {n['file']}"))
            for e in d.get("edges", []):
                if e["fromNode"] not in ids or e["toNode"] not in ids:
                    errs.append((os.path.relpath(p, ROOT), 0, f"edge {e['id']} points to a missing node"))

seen = set()
for s, l, m in sorted(errs):
    if (s, m) in seen:
        continue
    seen.add((s, m))
    print(f"{s}:{l}: {m}")
print(f"\nchecked {count} files, {len(seen)} distinct problems")
