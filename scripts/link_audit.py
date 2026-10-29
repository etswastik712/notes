"""Strict (Obsidian-faithful) link audit and repair.

    .venv/bin/python -W ignore scripts/link_audit.py            # report
    .venv/bin/python -W ignore scripts/link_audit.py --fix      # rewrite alias-only links as [[File|alias]]

Why: `check_links.py` counts a frontmatter *alias* as a valid link target.  Obsidian does not: `[[alias]]` is resolved by FILE NAME
or PATH only (aliases feed autocomplete and "unlinked mentions", nothing else).  An alias-only link is therefore an *unresolved*
link, and `graph.json` has `hideUnresolved: true`, so the edge silently disappears from the graph.  This script resolves links
the way Obsidian does:  `[[name]]` -> any note whose file name (without .md) equals `name` (case-insensitive); `[[a/b/name]]` -> a
note whose path ends with `a/b/name.md`; non-markdown targets by full file name.  Ambiguity (several notes with the same name) is
reported: Obsidian then picks the closest one in the folder tree, which may not be the one intended.

--fix rewrites an alias-only link `[[alias]]` / `[[alias#h]]` as `[[File|alias]]` / `[[File#h|alias]]` (display text is unchanged);
it touches only the vault's own folders (00-Home, 0x-*, 1x-*), never the other tool's source folders.
"""
import argparse
import collections
import os
import re

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SKIP = {".git", ".obsidian", ".venv", "node_modules", "build", "__pycache__"}
OWN = re.compile(r"^(00-Home|\d\d-[A-Za-z-]+)$")
LINK = re.compile(r"(!?)\[\[([^\]\n]+?)\]\]")
NON_MD = (".pdf", ".png", ".jpg", ".jpeg", ".svg", ".canvas", ".gif", ".docx", ".mp4", ".pptx", ".csv", ".json", ".tex", ".excalidraw", ".md")


def index():
    by_name = collections.defaultdict(list)      # lower file name without .md -> [relpaths]
    by_file = collections.defaultdict(list)      # lower full file name -> [relpaths]
    aliases = collections.defaultdict(list)      # lower alias -> [relpaths]
    texts = {}
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in SKIP]
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), ROOT)
            by_file[f.lower()].append(rel)
            if f.endswith(".md"):
                by_name[f[:-3].lower()].append(rel)
                t = open(os.path.join(dp, f), encoding="utf-8", errors="ignore").read()
                texts[rel] = t
                m = re.match(r"---\n(.*?)\n---", t, re.S)
                if m:
                    try:
                        fm = yaml.safe_load(m.group(1)) or {}
                    except Exception:
                        fm = {}
                    al = fm.get("aliases") or []
                    if isinstance(al, str):
                        al = [al]
                    for a in al:
                        aliases[str(a).lower()].append(rel)
    return by_name, by_file, aliases, texts


def strip_code(text):
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return re.sub(r"`[^`\n]*`", lambda m: " " * len(m.group(0)), text)


def resolve(target, by_name, by_file):
    """Return (status, paths) for a link target as Obsidian would resolve it."""
    t = target.strip()
    if not t:
        return "self", []
    low = t.lower().replace("\\", "/")
    ext = os.path.splitext(low)[1]
    if ext in NON_MD and ext != ".md" or low.endswith(".excalidraw.md"):
        hits = by_file.get(os.path.basename(low), [])
        return ("ok" if hits else "missing"), hits
    if low.endswith(".md"):
        low = low[:-3]
    if "/" in low:
        hits = [p for p in by_name.get(os.path.basename(low), []) if p[:-3].lower().endswith(low)]
    else:
        hits = by_name.get(low, [])
    if not hits:
        return "missing", []
    return ("ok" if len(hits) == 1 else "ambiguous"), hits


def audit(fix=False):
    by_name, by_file, aliases, texts = index()
    stats = collections.Counter()
    alias_only = collections.defaultdict(list)
    missing = collections.defaultdict(list)
    ambiguous = collections.defaultdict(list)
    rewrites = {}
    for rel, text in texts.items():
        own = bool(OWN.match(rel.split(os.sep)[0]))
        clean = strip_code(text)
        for m in LINK.finditer(clean):
            if m.group(1) == "!":
                continue
            raw = m.group(2).replace("\\|", "|")
            target, _, disp = raw.partition("|")
            base, _, frag = target.partition("#")
            if not base.strip():
                continue
            st, hits = resolve(base, by_name, by_file)
            stats[("own" if own else "src", st)] += 1
            if st == "missing":
                al = aliases.get(base.strip().lower().replace(".md", ""), [])
                if al and not os.path.splitext(base)[1]:
                    alias_only[(base.strip(), al[0])].append(rel)
                    if fix and own:
                        rewrites.setdefault(rel, []).append((m.group(0), base.strip(), frag, disp, al[0]))
                else:
                    missing[base.strip()].append(rel)
            elif st == "ambiguous":
                ambiguous[base.strip()].append((rel, hits))
    return stats, alias_only, missing, ambiguous, rewrites, texts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix", action="store_true")
    a = ap.parse_args()
    stats, alias_only, missing, ambiguous, rewrites, texts = audit(a.fix)
    print("link resolution (Obsidian rules), counted per link occurrence:")
    for (scope, st), n in sorted(stats.items()):
        print(f"   {scope:4s} {st:10s} {n:6d}")
    n_alias = sum(len(v) for v in alias_only.values())
    print(f"\nALIAS-ONLY links (resolve in my old checker, UNRESOLVED in Obsidian): {n_alias} occurrences, {len(alias_only)} distinct")
    for (al, f), srcs in sorted(alias_only.items(), key=lambda kv: -len(kv[1]))[:25]:
        own = sum(1 for s in srcs if OWN.match(s.split(os.sep)[0]))
        print(f"   {len(srcs):4d} ({own} in vault)  [[{al}]]  ->  {os.path.basename(f)}")
    print(f"\ntruly missing targets: {sum(len(v) for v in missing.values())} occurrences, {len(missing)} distinct")
    for k, v in sorted(missing.items(), key=lambda kv: -len(kv[1]))[:15]:
        print(f"   {len(v):4d}  [[{k}]]  e.g. {v[0]}")
    print(f"\nambiguous targets (same file name in several folders): {len(ambiguous)} distinct")
    for k, v in sorted(ambiguous.items(), key=lambda kv: -len(kv[1]))[:10]:
        print(f"   {len(v):4d}  [[{k}]] -> {[h for h in v[0][1]]}")
    if a.fix:
        changed = 0
        for rel, items in rewrites.items():
            t = texts[rel]
            for full, base, frag, disp, f in items:
                fname = os.path.basename(f)[:-3]
                new = "[[" + fname + ("#" + frag if frag else "") + "|" + (disp or base) + "]]"
                if full in t:
                    t = t.replace(full, new)
                    changed += 1
            open(os.path.join(ROOT, rel), "w", encoding="utf-8").write(t)
        print(f"\nrewrote {changed} link occurrences in {len(rewrites)} vault notes")


if __name__ == "__main__":
    main()
