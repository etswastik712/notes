"""One-off restructuring of 10-Group-Theory (2026-10-28): renumber, strip taught/extra scope tags (the subject has no lectures).
   Idempotent: running twice does nothing more. Nothing but scope labels is removed; old names stay as aliases."""
import glob, os, re
V = "/home/swastik/Documents/notes/"
G = V + "10-Group-Theory/"
RENAMES = [("GT03 Actions Conjugation and Sylow Theorems", "GT05 Actions Conjugation and Sylow Theorems", "GT03", "GT05", 5),
           ("GT04 Symmetry Representations and Characters", "GT10 Symmetry Representations and Characters", "GT04", "GT10", 10)]
SRC = {"GT01": "Follows Kurzweil and Stellmacher, *The Theory of Finite Groups* (K–S), §1.1 ([[Kurzweil-Stellmacher_Theory of finite groups.pdf#page=14|PDF p.14 ff.]]; PDF page = printed page + 13). Cayley table, subgroup lattices and all counts are my own computations (`scripts/gt_numbers.py`).",
       "GT02": "Follows K–S §1.2–1.3 ([[Kurzweil-Stellmacher_Theory of finite groups.pdf#page=23|PDF p.23 ff.]]). The explicit quotient $S_4\\to S_3$, the commutator subgroup $S_4'=A_4$ and the index-2 argument are my own computations (`scripts/gt_numbers.py`, `scripts/fig_gt.py`).",
       "GT05": "Follows K–S §3.1–3.2 and §4.3 ([[Kurzweil-Stellmacher_Theory of finite groups.pdf#page=68|PDF p.68 ff.]]). Burnside's lemma, the McKay proof of Cauchy, the proof of Sylow's theorems, the class lists and the simplicity of $A_5$ are my own write-ups and computations (`scripts/gt_numbers.py`).",
       "GT10": "No source in the repository (K–S excludes representation theory); a bridge to the places where groups are used in this vault. All tables and reductions are computed in `scripts/gt_numbers.py`."}

def all_md():
    for root, dirs, files in os.walk(V):
        dirs[:] = [d for d in dirs if d not in (".git", ".venv", "node_modules", ".obsidian", "Assets")]
        for f in files:
            if f.endswith(".md"): yield os.path.join(root, f)

# 1) rename files
for old, new, oc, nc, n in RENAMES:
    o = G + old + ".md"; w = G + new + ".md"
    if os.path.exists(o) and not os.path.exists(w): os.rename(o, w); print("renamed", old, "->", new)
# 2) update references everywhere
for p in all_md():
    s = open(p).read(); t = s
    for old, new, oc, nc, n in RENAMES:
        t = t.replace("[[" + old, "[[" + new)
        t = t.replace(old + ".md", new + ".md")
    # chapter header nav lines mentioning short codes
    if t != s: open(p, "w").write(t)
# 3) strip scope labels in group theory notes
def strip(p):
    s = open(p).read(); o = s
    s = re.sub(r"^scope:.*\n", "", s, count=1, flags=re.M)
    s = re.sub(r"(tags: \[.*?)\b(extra/book|extra/beyond|taught), ?", r"\1", s)
    s = re.sub(r"(tags: \[.*?)(, (extra/book|extra/beyond|taught))+(\])", lambda m: m.group(1) + m.group(4), s)
    s = re.sub(r'<span class="scope-[^"]*">[^<]*</span>\s*', "", s)
    # a line that became empty after removing spans: drop it
    s = re.sub(r"\n[ \t]+\n", "\n\n", s)
    # chapter: syllabus callout -> source callout
    code = re.match(r"(GT\d+)", os.path.basename(p))
    def repl_chapter(m):
        c = code.group(1) if code else ""
        txt = SRC.get(c, "")
        return ("> [!info] Source and approach\n> " + txt + "\n") if txt else m.group(0)
    if code and not re.search(r"\[!info\] Source and approach", s):
        s = re.sub(r"> \[!syllabus\][^\n]*\n(?:>[^\n]*\n)*", repl_chapter, s, count=1)
    # concept notes
    s = s.replace("> [!syllabus] In the syllabus vs extra", "> [!info] Source")
    s = s.replace("🟡 **Extra · book:** ", "").replace("🔵 **Extra · beyond:** ", "")
    # provenance scope column
    s = s.replace("| Topic | Source | Scope |", "| Topic | Source | Origin |")
    s = s.replace("| extra · book |", "| book |").replace("| extra · beyond |", "| mine |").replace("| extra · book + beyond |", "| book + mine |")
    s = re.sub(r"extra · book \+ beyond", "book + mine", s)
    if s != o: open(p, "w").write(s)
for p in glob.glob(G + "**/*.md", recursive=True): strip(p)
# 4) frontmatter of renamed chapters
for old, new, oc, nc, n in RENAMES:
    p = G + new + ".md"; s = open(p).read()
    s = re.sub(r"^title: .*$", "title: " + new, s, count=1, flags=re.M)
    s = re.sub(r"^chapter: .*$", "chapter: %d" % n, s, count=1, flags=re.M)
    if oc not in s.split("---")[1]:
        s = re.sub(r"^aliases: \[", "aliases: [" + oc + " (old number), ", s, count=1, flags=re.M)
    open(p, "w").write(s)
print("done")
