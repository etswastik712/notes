"""Apply the Landscapes 'depth layer' (additive, idempotent).   python3 scripts/ls_depth.py [LS01 LS02 ...]
Reads scripts/ls_depth/<code>.md with blocks:
   @@ AFTER <heading prefix>   -> inserted at the END of the '## ' section whose heading starts with the prefix
   @@ END                      -> inserted just before '## Map of this chapter'
   @@ TAIL                     -> appended at the end of the file (e.g. an extra provenance callout)
Each block is tagged <!-- ls-depth:<code>:<n> --> so re-running never duplicates; nothing existing is removed.
Also makes sure the frontmatter lists book as a source and extra-book as a scope."""
import glob, os, re, sys
V = "/home/swastik/Documents/notes/05-Landscapes-Geomorphology/"
D = "/home/swastik/Documents/notes/scripts/ls_depth/"
def chapter_file(code):
    g = glob.glob(V + code + " *.md"); return g[0] if g else None
def blocks(txt):
    out, cur = [], None
    for line in txt.split("\n"):
        if line.startswith("@@ "):
            cur = [line[3:].strip(), []]; out.append(cur)
        elif cur is not None: cur[1].append(line)
    return [(k, "\n".join(v).strip("\n")) for k, v in out]
def fm_add(s, key, val):
    m = re.search(r"^(%s:\s*\[)(.*?)(\])" % key, s, re.M)
    if m and val not in [x.strip() for x in m.group(2).split(",")]:
        s = s[:m.end(2)] + (", " if m.group(2).strip() else "") + val + s[m.end(2):]
    return s
def apply(code):
    f = chapter_file(code); spec = D + code + ".md"
    if not f or not os.path.exists(spec): print("skip", code); return
    s = open(f).read(); n = 0
    for i, (k, body) in enumerate(blocks(open(spec).read()), 1):
        mark = f"<!-- ls-depth:{code}:{i} -->"
        if mark in s: continue
        blk = mark + "\n" + body.strip("\n") + "\n\n"
        lines = s.split("\n")
        if k.startswith("AFTER"):
            pre = k[5:].strip()
            idx = next((j for j, l in enumerate(lines) if l.startswith("## ") and l[3:].startswith(pre.lstrip("# ").strip())), None)
            if idx is None: print("  !! heading not found:", code, pre); continue
            end = next((j for j in range(idx + 1, len(lines)) if lines[j].startswith("## ")), len(lines))
            lines[end:end] = blk.split("\n"); s = "\n".join(lines)
        elif k == "END":
            idx = next((j for j, l in enumerate(lines) if l.startswith("## Map of this chapter")), None)
            if idx is None: idx = len(lines)
            lines[idx:idx] = blk.split("\n"); s = "\n".join(lines)
        elif k == "TAIL":
            s = s.rstrip("\n") + "\n\n" + blk.rstrip("\n") + "\n"
        n += 1
    s = fm_add(s, "by", "book"); s = fm_add(s, "scope", "extra-book"); s = fm_add(s, "tags", "extra/book"); s = fm_add(s, "tags", "src/book")
    open(f, "w").write(s); print(code, "blocks added:", n)
if __name__ == "__main__":
    for c in (sys.argv[1:] or sorted(os.path.basename(x)[:-3] for x in glob.glob(D + "LS*.md"))): apply(c)
