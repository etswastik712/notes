"""Convert the AI-written EC2123 LaTeX notes (landscape-notes-tex-source.tar.gz) into vault chapters.

usage: python3 scripts/tex2vault_ls.py <dir-with-extracted-tex> <outdir-for-md> [--figs]
Writes one markdown file per (part, chapter) pair listed in CHAPTERS. TikZ figures are compiled to PNG
(Assets/figures/ls_figNN.png) when --figs is given (needs pdflatex + pdftoppm).
Boxes: gbox derivation in slides, rbox extra, tbox tool, qbox question on slide, ibox intuition, dbox reading the diagram,
xbox worked example, kbox definition.
"""
import os
import re
import subprocess
import sys

SRC = sys.argv[1]
OUT = sys.argv[2]
DO_FIGS = "--figs" in sys.argv
FIGDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "Assets", "figures")
os.makedirs(OUT, exist_ok=True)

# vault chapter table: (file, chapter index within file (1-based), code, title, slide-deck prefix, short aliases)
CHAPTERS = [
    ("p1_foundations.tex", 1, "LS01", "Landscapes as Physical Systems"),
    ("p1_foundations.tex", 2, "LS02", "Mechanics and Mathematics Toolkit"),
    ("p2_mapping.tex", 1, "LS03", "Digital Elevation Models and Terrain Analysis"),
    ("p2_mapping.tex", 2, "LS04", "Map Projections and Reference Surfaces"),
    ("p3_planet.tex", 1, "LS05", "Shape of Planets"),
    ("p3_planet.tex", 2, "LS06", "Maximum Topography"),
    ("p4_isostasy.tex", 1, "LS07", "Isostasy"),
    ("p5_tectonics.tex", 1, "LS08", "Plate Tectonics Strain Stress and Convection"),
    ("p5_tectonics.tex", 2, "LS09", "Faults and Earthquakes"),
    ("p5_tectonics.tex", 3, "LS10", "Folds Flexure and Mountain Building"),
    ("p6_weathering.tex", 1, "LS11", "Weathering and Regolith"),
    ("p7_hillslope.tex", 1, "LS12", "Hillslope Transport and the Diffusion Equation"),
    ("p7_hillslope.tex", 2, "LS13", "Landslides"),
    ("p8_glacier.tex", 1, "LS14", "Glaciers Mass Balance and Ice Flow"),
    ("p8_glacier.tex", 2, "LS15", "Glacial Deposits Rebound and Sea Level"),
    ("p9_postms.tex", 1, "LS16", "Fluvial Landscapes"),
    ("p9_postms.tex", 2, "LS17", "Aeolian Landscapes"),
    ("p10_problems.tex", 0, "LS99", "Landscapes Practice Problems"),
]

MACROS = {
    r"\dd": r"\mathrm{d}", r"\ee": r"\mathrm{e}", r"\ii": r"\mathrm{i}",
    r"\Pa": r"\,\mathrm{Pa}", r"\MPa": r"\,\mathrm{MPa}", r"\GPa": r"\,\mathrm{GPa}", r"\kmu": r"\,\mathrm{km}",
    r"\mm": r"\,\mathrm{m}", r"\ms": r"\,\mathrm{m\,s^{-1}}", r"\Pas": r"\,\mathrm{Pa\,s}", r"\yr": r"\,\mathrm{yr}",
    r"\kyr": r"\,\mathrm{kyr}", r"\Myr": r"\,\mathrm{Myr}", r"\kgm": r"\,\mathrm{kg\,m^{-3}}", r"\sgn": r"\operatorname{sgn}",
    r"\bm": r"\boldsymbol",
}
ARG_MACROS = {
    "pd": (2, r"\dfrac{\partial #1}{\partial #2}"), "pdd": (2, r"\dfrac{\partial^2 #1}{\partial #2^2}"),
    "dv": (2, r"\dfrac{\mathrm{d} #1}{\mathrm{d} #2}"), "vect": (1, r"\boldsymbol{#1}"), "Ord": (1, r"\mathcal{O}\!\left(#1\right)"),
}


def brace_group(s, i):
    """Return (content, end_index) of balanced {..} starting at s[i]=='{'."""
    assert s[i] == "{"
    depth = 0
    for j in range(i, len(s)):
        if s[j] == "{" and s[j - 1] != "\\":
            depth += 1
        elif s[j] == "}" and s[j - 1] != "\\":
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
    return s[i + 1:], len(s)


def expand_args(s):
    for name, (n, tmpl) in ARG_MACROS.items():
        pat = "\\" + name
        out = []
        i = 0
        while True:
            k = s.find(pat, i)
            if k < 0:
                out.append(s[i:])
                break
            end = k + len(pat)
            if end < len(s) and s[end].isalpha():
                out.append(s[i:end]); i = end; continue
            out.append(s[i:k])
            j = end
            args = []
            ok = True
            for _ in range(n):
                while j < len(s) and s[j] == " ":
                    j += 1
                if j < len(s) and s[j] == "{":
                    a, j = brace_group(s, j)
                    args.append(a)
                else:
                    ok = False; break
            if ok:
                t = tmpl
                for q, a in enumerate(args, 1):
                    t = t.replace("#%d" % q, a)
                out.append(t)
            else:
                out.append(pat)
            i = j if ok else end
        s = "".join(out)
    return s


def fix_math(m):
    m = expand_args(m)
    for k in sorted(MACROS, key=len, reverse=True):
        m = re.sub(re.escape(k) + r"(?![A-Za-z])", lambda _m, v=MACROS[k]: v, m)
    m = m.replace(r"\label", r"\label")
    m = re.sub(r"\\label\{[^}]*\}", "", m)
    m = m.replace("\\,\\,", "\\,")
    m = re.sub(r"\\(?:footnotesize|small)\b", "", m)
    return m


def strip_comments(s):
    out = []
    for line in s.split("\n"):
        i = 0
        cut = None
        while i < len(line):
            if line[i] == "%" and (i == 0 or line[i - 1] != "\\"):
                cut = i; break
            i += 1
        out.append(line if cut is None else line[:cut])
    return "\n".join(out)


# ------------------------------------------------------------------ parsing into nodes
ENV = re.compile(r"\\(begin|end)\{([A-Za-z*]+)\}")


def parse(s):
    """Return list of nodes: str | (name, arg_or_None, children)."""
    s = re.sub(r"(\\begin\{(?:table|figure)\*?\})\[[a-zA-Z!]*\]", r"\1", s)
    root = []
    stack = [("root", None, root)]
    pos = 0
    for m in ENV.finditer(s):
        if m.start() > pos:
            stack[-1][2].append(s[pos:m.start()])
        pos = m.end()
        kind, name = m.group(1), m.group(2)
        if kind == "begin":
            arg = None
            if name in ("dbox", "rbox", "xbox", "gbox", "qbox", "kbox", "ibox", "tbox"):
                j = pos
                while s[j] in " \n":
                    j += 1
                arg, pos = brace_group(s, j)
            elif name in ("tabularx", "tabular"):
                j = pos
                if name == "tabularx":
                    _, j = brace_group(s, pos)          # width
                cols, j = brace_group(s, j)
                arg, pos = cols, j
            elif name in ("axis", "loglogaxis", "minipage"):
                # raw: consume to matching end (kept verbatim for figures)
                pass
            node = (name, arg, [])
            stack[-1][2].append(node)
            stack.append(node)
        else:
            if len(stack) > 1 and stack[-1][0] == name:
                stack.pop()
    if pos < len(s):
        stack[-1][2].append(s[pos:])
    return root


def raw_of(node):
    """Re-serialise a node (for figure compilation)."""
    if isinstance(node, str):
        return node
    name, arg, ch = node
    a = ""
    inner = "".join(raw_of(c) for c in ch)
    return "\\begin{%s}%s%s\\end{%s}" % (name, ("{%s}" % arg) if arg is not None and name in ("tabular",) else "", inner, name)


# ------------------------------------------------------------------ text conversion
SLIDE_RE = re.compile(r"[Ss]lides?\s*~?\s*(\d+)(?:\s*(?:--|–|-|,|and)\s*(\d+))?")


def conv_text(t):
    """Convert prose (may contain inline math)."""
    # protect inline math
    parts = re.split(r"(\$[^$]*\$)", t)
    out = []
    for p in parts:
        if p.startswith("$") and p.endswith("$") and len(p) >= 2:
            out.append("$" + fix_math(p[1:-1]) + "$")
            continue
        p = re.sub(r"\\\[(.*?)\\\]", lambda m: "\n\n$$\n" + fix_math(m.group(1)).strip() + "\n$$\n\n", p, flags=re.S)
        p = re.sub(r"\\(chapter|section|subsection|part)\*?\{", lambda m: "\x00" + m.group(1) + "{", p)
        out.append(p)
    t = "".join(out)
    return t


def inline_cleanup(t):
    t = re.sub(r"\\textbf\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", r"**\1**", t)
    t = re.sub(r"\\(?:emph|textit)\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}", r"*\1*", t)
    t = re.sub(r"\\texttt\{([^{}]*)\}", r"`\1`", t)
    t = re.sub(r"\\textsc\{([^{}]*)\}", r"\1", t)
    t = re.sub(r"\\slideref\{([^{}]*)\}", lambda m: "*[Slides " + m.group(1).replace("--", "–") + "]*", t)
    t = re.sub(r"\\url\{([^{}]*)\}", r"<\1>", t)
    t = re.sub(r"\\footnote\{([^{}]*)\}", r" (\1)", t)
    t = re.sub(r"\\(?:centering|noindent|small|footnotesize|normalsize|large|Large|hfill|medskip|smallskip|bigskip|clearpage|newpage|vspace\*?\{[^}]*\}|hspace\*?\{[^}]*\})\b", "", t)
    t = t.replace("\\&", "&").replace("\\%", "%").replace("\\#", "#").replace("\\_", "_").replace("\\$", "\\$")
    t = t.replace("``", "“").replace("''", "”").replace("---", "—").replace("--", "–")
    t = t.replace("\\S\\,", "§").replace("\\S ", "§ ").replace("\\S~", "§")
    t = t.replace("~", " ").replace("\\ ", " ").replace("\\,", " ")
    t = re.sub(r"\\label\{[^}]*\}", "", t)
    t = re.sub(r"\\(?:ref|eqref)\{([^}]*)\}", lambda m: EQREF.get(m.group(1), "(" + m.group(1).split(":")[-1] + ")"), t)
    return t


EQREF = {}
EQN = [0]


def render_math_env(name, node):
    body = "".join(raw_of(c) for c in node[2])
    lab = re.findall(r"\\label\{([^}]*)\}", body)
    EQN[0] += 1
    n = EQN[0]
    for l in lab:
        EQREF[l] = "(%d)" % n
    body = fix_math(body)
    if name == "align":
        body = "\\begin{aligned}" + body + "\\end{aligned}"
    return "\n\n$$\n" + body.strip() + " \\tag{%d}\n$$\n\n" % n


def split_tabular(body):
    body = body.replace("\\toprule", "").replace("\\midrule", "").replace("\\bottomrule", "").replace("\\hline", "")
    rows = [r.strip() for r in re.split(r"\\\\(?:\[[^\]]*\])?", body) if r.strip()]
    table = []
    for r in rows:
        cells = [c.strip() for c in r.split("&")]
        cells = [re.sub(r"\\multicolumn\{\d+\}\{[^}]*\}\{(.*)\}", r"\1", c) for c in cells]
        table.append(cells)
    return table


def render_table(node):
    name, arg, ch = node
    body = "".join(c if isinstance(c, str) else raw_of(c) for c in ch)
    table = split_tabular(body)
    if not table:
        return ""
    w = max(len(r) for r in table)
    rows = []
    for k, r in enumerate(table):
        r = r + [""] * (w - len(r))
        rows.append("| " + " | ".join(conv_inline_full(c).replace("|", "\\|").replace("\n", " ") for c in r) + " |")
        if k == 0:
            rows.append("|" + "|".join(["---"] * w) + "|")
    return "\n\n" + "\n".join(rows) + "\n\n"


def conv_inline_full(c):
    return inline_cleanup(conv_text(c))


BOX = {
    "gbox": ("derivation", "🟢 In the slides: "),
    "rbox": ("derivation", "🔵 Extra (not derived in the slides): "),
    "tbox": ("key", "🛠 Tool: "),
    "qbox": ("example", "❓ Question on the slides: "),
    "ibox": ("intuition", ""),
    "dbox": ("example", "🖼 Reading the diagram: "),
    "xbox": ("example", "🧮 Worked example: "),
    "kbox": ("key", "Definition: "),
}


def callout(kind, title, inner):
    inner = inner.strip("\n")
    lines = inner.split("\n")
    q = "\n".join(("> " + l if l.strip() else ">") for l in lines)
    return "\n\n> [!%s] %s\n%s\n\n" % (kind, title, q)


FIGS = []
SLIDE_DECK = "pre"


def slide_gallery(title, maxn=4):
    m = SLIDE_RE.search(title)
    if not m:
        return ""
    a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
    if b < a or b > 153:
        b = a
    nums = list(range(a, min(b, a + maxn - 1) + 1))
    imgs = " ".join("![[%s_%03d.jpg|%d]]" % (SLIDE_DECK, n, 460 if len(nums) < 3 else 300) for n in nums)
    return "\n\n" + imgs + "\n\n"


def render(nodes, ctx):
    out = []
    for n in nodes:
        if isinstance(n, str):
            out.append(inline_cleanup(conv_text(n)))
            continue
        name, arg, ch = n
        if name in BOX:
            kind, pre = BOX[name]
            inner = render(ch, ctx)
            title = inline_cleanup(conv_text(arg)).strip()
            gal = slide_gallery(arg) if name == "dbox" else ""
            out.append(gal + callout(kind, pre + title, inner))
        elif name in ("equation", "align", "equation*", "align*"):
            out.append(render_math_env(name.rstrip("*"), n))
        elif name == "itemize" or name == "enumerate":
            items = []
            body = "".join(c if isinstance(c, str) else "" for c in ch)
            parts = re.split(r"\\item\s*(?:\[[^\]]*\])?", body)
            for k, it in enumerate(parts[1:], 1):
                bullet = "- " if name == "itemize" else "%d. " % k
                items.append(bullet + inline_cleanup(conv_text(it.strip())).replace("\n", "\n  "))
            out.append("\n\n" + "\n".join(items) + "\n\n")
        elif name in ("tabularx", "tabular"):
            out.append(render_table(n))
        elif name == "table":
            body = "".join(raw_of(c) if not isinstance(c, str) else c for c in ch)
            cap = ""
            m = re.search(r"\\caption\{", body)
            if m:
                cap, _ = brace_group(body, m.end() - 1)
            tbl = "".join(render_table(c) for c in ch if not isinstance(c, str) and c[0] in ("tabular", "tabularx"))
            out.append(tbl + ("*%s*\n\n" % inline_cleanup(conv_text(cap)).strip() if cap else ""))
        elif name == "figure":
            out.append(render_figure(n, ctx))
        elif name in ("tikzpicture", "axis", "loglogaxis", "scope", "minipage", "center"):
            out.append(render(ch, ctx) if name in ("center", "minipage") else "")
        else:
            out.append(render(ch, ctx))
    return "".join(out)


FIGN = [0]


def render_figure(n, ctx):
    name, arg, ch = n
    FIGN[0] += 1
    k = FIGN[0]
    cap = ""
    body = ""
    for c in ch:
        s = raw_of(c)
        body += s
    m = re.search(r"\\caption\{", body)
    if m:
        cap, _ = brace_group(body, m.end() - 1)
        body = body[:m.start()] + body[brace_group(body, m.end() - 1)[1]:]
    capmd = inline_cleanup(conv_text(cap)).strip()
    fname = "ls_fig%02d" % k
    FIGS.append((fname, body))
    return "\n\n![[%s.png]]\n*Figure %s.%d. %s*\n\n" % (fname, ctx["code"], ctx["fig"].__next__(), capmd)


def compile_figs():
    pre = open(os.path.join(SRC, "preamble.tex")).read()
    lines = pre.split("\n")
    keep = [l for l in lines if l.startswith(r"\newcommand") or l.startswith(r"\definecolor") or l.startswith(r"\usetikzlibrary") or l.startswith(r"\tikzset")]
    i0 = next(i for i, l in enumerate(lines) if "every axis" in l)
    keep += lines[i0:i0 + 4]
    macros = "\n".join(keep).replace("\\newcommand{\\slideref}", "\\newcommand{\\slideref}")
    macros = macros.replace("0.78\\textwidth", "13cm").replace("0.42\\textwidth", "7cm")
    tmp = os.path.join(SRC, "_figs")
    os.makedirs(tmp, exist_ok=True)
    for fname, body in FIGS:
        tex = (r"\documentclass[border=6pt,varwidth=17cm]{standalone}" "\n"
               r"\usepackage[utf8]{inputenc}\usepackage{amsmath,amssymb,mathtools,bm}\usepackage[dvipsnames]{xcolor}\usepackage{tikz}\usepackage{pgfplots}\usepackage{booktabs,array}" "\n"
               + macros + "\n" r"\begin{document}" "\n" + body + "\n" r"\end{document}")
        path = os.path.join(tmp, fname + ".tex")
        open(path, "w").write(tex)
        r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", fname + ".tex"], cwd=tmp, capture_output=True, text=True, timeout=120)
        if r.returncode != 0:
            print("LATEX FAIL", fname, [l for l in r.stdout.split("\n") if l.startswith("!")][:2])
            continue
        subprocess.run(["pdftoppm", "-r", "140", "-png", "-singlefile", fname + ".pdf", os.path.join(FIGDIR, fname)], cwd=tmp)
    print("figures compiled:", len(FIGS))


def build():
    import itertools
    files = {}
    for fn, idx, code, title in CHAPTERS:
        if fn not in files:
            files[fn] = strip_comments(open(os.path.join(SRC, fn)).read())
    for fn, idx, code, title in CHAPTERS:
        s = files[fn]
        # split by \chapter
        chunks = re.split(r"(?=\\chapter\*?\{)", s)
        chunks = [c for c in chunks if c.strip().startswith("\\chapter")]
        if idx == 0:
            body = s
            body = re.sub(r"\\part\{[^}]*\}", "", body)
            body = re.sub(r"\\chapter\*?\{[^}]*\}", "", body)
        else:
            body = chunks[idx - 1]
            body = re.sub(r"\\chapter\*?\{[^}]*\}", "", body, count=1)
        ctx = {"code": code.replace("LS", "LS"), "fig": itertools.count(1)}
        nodes = parse(body)
        md = render(nodes, ctx)
        md = md.replace("\x00section{", "\n\n## ").replace("\x00subsection{", "\n\n### ").replace("\x00chapter{", "\n\n# ").replace("\x00part{", "\n\n# ")
        # close heading braces: heading text ends at first matching "}" on the line
        def fix_heading(m):
            hashes, rest = m.group(1), m.group(2)
            depth = 0; end = None
            for i, ch_ in enumerate(rest):
                if ch_ == "{":
                    depth += 1
                elif ch_ == "}":
                    if depth == 0:
                        end = i; break
                    depth -= 1
            if end is None:
                return hashes + rest
            head, tail = rest[:end], rest[end + 1:]
            return hashes + head + "\n" + SLIDEGAL(head) + tail
        md = re.sub(r"(\n\n#{1,3} )([^\n]*)", fix_heading, md)
        # drop galleries of sections that already show their slides inside a reading box
        secs = re.split(r"(?=\n\n## )", md)
        keep = []
        for sec in secs:
            if "Reading the diagram" in sec:
                sec = re.sub(r"\n> \[!figure\]- 🖼 [^\n]*\n> [^\n]*\n", "\n", sec, count=1)
            keep.append(sec)
        md = "".join(keep)
        md = re.sub(r"\n{4,}", "\n\n\n", md)
        open(os.path.join(OUT, code + ".md.body"), "w").write(md)
        print(code, len(md.split()), "words")
    if DO_FIGS:
        compile_figs()


def SLIDEGAL(head):
    m = SLIDE_RE.search(head)
    if not m:
        return ""
    a = int(m.group(1)); b = int(m.group(2)) if m.group(2) else a
    if b < a or b > 153:
        b = a
    nums = list(range(a, b + 1))
    if len(nums) > 8:
        nums = nums[:8]
    imgs = " ".join("![[%s_%03d.jpg|%d]]" % (SLIDE_DECK, n, 300) for n in nums)
    ttl = ("Slide %d" % a) if a == b else ("Slides %d–%d" % (a, b))
    return "\n> [!figure]- 🖼 %s: open to see the slides this section explains\n> %s\n" % (ttl, imgs) if nums else ""


if __name__ == "__main__":
    build()
