"""Turn Joy Monteiro's mirrored slide decks (JSON presentations) and lecture-handout HTML into plain-text transcripts.
   Reads  earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/  and writes transcripts/ next to it.
   python3 -I scripts/joy_extract.py
"""
import html, json, os, re
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "earth-and-climate", "climate", "lecture-notes-slides", "joy_intro_climate_science"))
OUT = os.path.join(ROOT, "transcripts")
os.makedirs(OUT, exist_ok=True)
def strip(h):
    h = re.sub(r"<br\s*/?>", " / ", h)
    h = re.sub(r"</(div|p|li|h\d)>", "\n", h)
    h = re.sub(r"<sup>(.*?)</sup>", r"^(\1)", h)
    h = re.sub(r"<sub>(.*?)</sub>", r"_(\1)", h)
    h = re.sub(r"<[^>]+>", "", h)
    h = html.unescape(h)
    return re.sub(r"[ \t]+", " ", h).strip()
DECKS = {"ocean-ledger": "Week 1 (O1)", "ocean-ledger-w2": "Week 2 (O2, O3)", "ocean-ledger-o4": "O4", "ocean-ledger-o5": "O5", "ocean-ledger-o6": "O6"}
for d, label in DECKS.items():
    src = open(os.path.join(ROOT, "lectures", d, "index.html"), encoding="utf-8").read()
    m = re.search(r"window\.__PRES__=(\{.*?\});?\s*</script>", src, re.S)
    P = json.loads(m.group(1))
    frames = P["frames"]
    idx = {f["id"]: i for i, f in enumerate(frames)}
    els = P["elements"]
    lines = ["# %s: %s" % (label, P["title"]), "", "(%d frames, %d elements; deck file lectures/%s/index.html)" % (len(frames), len(els), d), ""]
    for i, f in enumerate(frames):
        lines.append("## Frame %d: %s  [%s]" % (i + 1, f["title"], f["id"]))
        if f.get("notes"):
            lines.append("NOTES: " + f["notes"].strip())
        shown_t, shown_s = [], []
        for e in els:
            lc = e.get("lifecycle", {}) or {}
            en = lc.get("enterAt")
            if en is None or en not in idx:
                continue            # persistent backgrounds (ocean, land) are skipped
            start = idx[en]
            ex = lc.get("exitAt")
            leave = lc.get("onExit") == "leave"
            end = idx[ex] if (ex in idx) else (start if leave else len(frames) - 1)
            if start <= i <= end:
                if e["type"] == "text":
                    t = strip(e.get("content", ""))
                    if t:
                        shown_t.append((e.get("y", 0), e.get("x", 0), t))
                elif e["type"] == "svg":
                    shown_s.append(os.path.basename(e.get("content", "")))
        for y, x, t in sorted(shown_t):
            lines.append("  TEXT: " + t.replace("\n", " | "))
        if shown_s:
            lines.append("  FIGURES: " + ", ".join(shown_s))
        lines.append("")
    open(os.path.join(OUT, d + ".md"), "w", encoding="utf-8").write("\n".join(lines))
    print(d, len(frames), "frames ->", len("\n".join(lines)), "chars")
# lecture handouts
for o in ("o1", "o2", "o3", "o4", "o5"):
    h = open(os.path.join(ROOT, "lectures", "notes", o, "index.html"), encoding="utf-8").read()
    body = re.search(r"<main[^>]*>(.*?)</main>", h, re.S)
    b = body.group(1) if body else h
    b = re.sub(r"<script.*?</script>|<style.*?</style>", "", b, flags=re.S)
    b = re.sub(r"<h([1-4])[^>]*>(.*?)</h\1>", lambda m: "\n" + "#" * int(m.group(1)) + " " + strip(m.group(2)) + "\n", b, flags=re.S)
    b = re.sub(r"<li[^>]*>", "\n- ", b)
    b = re.sub(r"<(p|div|tr|table|ul|ol|blockquote|figure|figcaption)[^>]*>", "\n", b)
    b = re.sub(r"</t[dh]>", " | ", b)
    t = strip(b)
    t = re.sub(r"\n{3,}", "\n\n", t)
    open(os.path.join(OUT, "handout_" + o + ".md"), "w", encoding="utf-8").write(t)
    print("handout", o, len(t), "chars")
for tdir in ("daisyworld-land-ocean", "daisyworld-ocean", "ceres-energy-budget"):
    p = os.path.join(ROOT, "tutorials", tdir, "index.html")
    h = open(p, encoding="utf-8").read()
    h = re.sub(r"<script.*?</script>|<style.*?</style>", "", h, flags=re.S)
    t = strip(re.sub(r"<(h[1-6]|p|li|div|tr|section)[^>]*>", "\n", h))
    t = re.sub(r"\n{3,}", "\n\n", t)
    open(os.path.join(OUT, "tutorial_" + tdir + ".md"), "w", encoding="utf-8").write(t)
    print("tutorial", tdir, len(t))
