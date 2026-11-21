"""Render Joy's HTML slide decks to PDF (slides only, and slides + speaker notes).

  .venv/bin/python -I scripts/joy_slides_pdf.py [deck ...]        (decks: ocean-ledger ocean-ledger-w2 ocean-ledger-o4 ocean-ledger-o5 ocean-ledger-o6 ocean-ledger-o7)

Method: each deck is a downloaded HTML page (untrusted data, only ever opened from a throw-away copy). For every frame n the copy is
opened in headless Firefox at  index.html#n  with prefers-reduced-motion forced on (no fades or camera moves) and the deck's progress
bar / hint hidden, then a 1920x1080 screenshot is taken. Screenshots are assembled into PDFs with PyMuPDF.
Output: earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf/
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor

import fitz  # PyMuPDF

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/lectures")
OUT = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf")
JOB = os.environ.get("CLAUDE_JOB_DIR", "/home/swastik/.claude/jobs/1eb128c0")
WORK = os.path.join(JOB, "tmp", "slides_work")
W, H = 1920, 1080

DECKS = {
    "ocean-ledger": "O1_Week1_The-ocean-ledger",
    "ocean-ledger-w2": "O2-O3_Week2_Where-does-it-go_and_The-ponderous-ocean",
    "ocean-ledger-o4": "O4_Nansens-answer",
    "ocean-ledger-o5": "O5_The-salt-ledger",
    "ocean-ledger-o6": "O6_The-overturning",
    "ocean-ledger-o7": "O7_Slow-swings-and-the-oceans-memory-for-carbon",
}
FONT = "/usr/share/fonts/liberation/LiberationSans-Regular.ttf"
FONTB = "/usr/share/fonts/liberation/LiberationSans-Bold.ttf"
SUP = dict(zip("⁻⁰¹²³⁴⁵⁶⁷⁸⁹", "-0123456789"))
SUBS = {"✓": "[ok]", "⚠": "[!]", "≪": "<<", "≫": ">>", "∇": "grad ", "∼": "~", "⁻": "^-"}


def fix_text(t):
    """replace glyphs missing from Liberation Sans: runs of superscript digits become ^(...)"""
    import re as _re
    t = _re.sub(r"[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+", lambda m: "^(" + "".join(SUP[c] for c in m.group(0)).replace("-", "\u2212") + ")" if len(m.group(0)) > 1 or m.group(0) in "⁻⁰" else m.group(0), t)
    t = t.replace("\\u2212", "\u2212")
    for a, b in SUBS.items():
        t = t.replace(a, b)
    return t


HIDE = "<style>#hint,#progress{display:none !important}</style>"


def load_pres(html):
    m = re.search(r"window\.__PRES__=(\{.*?\});\s*</script>", html, re.S)
    if not m:
        m = re.search(r"window\.__PRES__\s*=\s*(\{.*?\})\s*;?\s*</script>", html, re.S)
    return json.loads(m.group(1))


def make_copy(deck):
    d = os.path.join(WORK, deck)
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(d)
    html = open(os.path.join(SRC, deck, "index.html"), encoding="utf-8").read()
    pres = load_pres(html)
    html = html.replace("</head>", HIDE + "</head>", 1)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)
    assets = os.path.join(SRC, deck, "assets")
    if os.path.isdir(assets):
        os.symlink(assets, os.path.join(d, "assets"))
    return d, pres


def make_profile(i):
    p = os.path.join(WORK, f"prof{i}")
    shutil.rmtree(p, ignore_errors=True)
    os.makedirs(p)
    open(os.path.join(p, "user.js"), "w").write(
        'user_pref("ui.prefersReducedMotion", 1);\n'
        'user_pref("browser.shell.checkDefaultBrowser", false);\n'
        'user_pref("datareporting.policy.dataSubmissionEnabled", false);\n'
        'user_pref("toolkit.telemetry.enabled", false);\n'
        'user_pref("network.http.speculative-parallel-limit", 0);\n')
    return p


def shot(args):
    deck_dir, n, png, prof = args
    if os.path.exists(png) and os.path.getsize(png) > 5000:
        return png
    url = f"file://{deck_dir}/index.html#{n}"
    for attempt in range(3):
        subprocess.run(["firefox", "--headless", "--no-remote", "--profile", prof, "--screenshot", png,
                        f"--window-size={W},{H}", url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
        if os.path.exists(png) and os.path.getsize(png) > 5000:
            return png
    raise RuntimeError(f"screenshot failed: {url}")


def build(deck, workers=4):
    d, pres = make_copy(deck)
    frames = pres["frames"]
    n = len(frames)
    shots = os.path.join(WORK, deck + "_png")
    os.makedirs(shots, exist_ok=True)
    profs = [make_profile(f"{deck}_{i}") for i in range(workers)]
    jobs = [(d, k, os.path.join(shots, f"{k:03d}.png"), profs[(k - 1) % workers]) for k in range(1, n + 1)]
    # one profile per worker thread: group jobs by profile so two firefox never share a profile
    groups = [[j for j in jobs if j[3] == p] for p in profs]
    def run_group(g):
        return [shot(j) for j in g]
    with ThreadPoolExecutor(workers) as ex:
        list(ex.map(run_group, groups))
    os.makedirs(OUT, exist_ok=True)
    name = DECKS[deck]
    pngs = [os.path.join(shots, f"{k:03d}.png") for k in range(1, n + 1)]
    title = pres.get("title", deck)
    # 1) slides only: page = 16:9, 960x540 pt
    doc = fitz.open()
    for k, p in enumerate(pngs):
        page = doc.new_page(width=960, height=540)
        page.insert_image(page.rect, filename=p)
    doc.set_metadata({"title": title + " (slides)", "author": "Joy Monteiro, EC2113 ocean module (rendered from the course's HTML deck)"})
    # bookmarks: frame titles
    doc.set_toc([[1, f"{k + 1}. {frames[k].get('title') or ''}".strip(), k + 1] for k in range(n)])
    doc.save(os.path.join(OUT, name + ".pdf"), deflate=True, garbage=3)
    doc.close()
    # 2) slides + speaker notes: A4 landscape-ish? use portrait 612x792: slide on top, notes below
    doc = fitz.open()
    for k, p in enumerate(pngs):
        page = doc.new_page(width=612, height=792)
        r = fitz.Rect(36, 30, 576, 30 + 540 * 9 / 16)
        page.insert_image(r, filename=p)
        page.draw_rect(r, color=(0.6, 0.6, 0.6), width=0.5)
        notes = (frames[k].get("notes") or "").strip()
        head = f"{k + 1}/{n} · {frames[k].get('title') or ''}"
        page.insert_font(fontname="LS", fontfile=FONT)
        page.insert_font(fontname="LSB", fontfile=FONTB)
        page.insert_textbox(fitz.Rect(36, 30 + 540 * 9 / 16 + 6, 576, 30 + 540 * 9 / 16 + 24), fix_text(head), fontsize=9, fontname="LSB")
        tb = fitz.Rect(36, 30 + 540 * 9 / 16 + 28, 576, 770)
        text = fix_text(notes) if notes else "(no speaker notes for this frame)"
        drawn = False
        for fs in (8.5, 8.0, 7.5, 7.0, 6.5, 6.0, 5.5):
            if page.insert_textbox(tb, text, fontsize=fs, fontname="LS") >= 0:   # nothing is drawn when it does not fit
                drawn = True
                break
        if not drawn:
            page.insert_textbox(tb, text[:2200] + " ...", fontsize=5.5, fontname="LS")
    doc.set_metadata({"title": title + " (slides with speaker notes)", "author": "Joy Monteiro, EC2113 ocean module (rendered from the course's HTML deck)"})
    doc.set_toc([[1, f"{k + 1}. {frames[k].get('title') or ''}".strip(), k + 1] for k in range(n)])
    doc.save(os.path.join(OUT, name + "_with-notes.pdf"), deflate=True, garbage=3)
    doc.close()
    return n, name


if __name__ == "__main__":
    os.makedirs(WORK, exist_ok=True)
    todo = sys.argv[1:] or list(DECKS)
    for deck in todo:
        n, name = build(deck)
        print(f"{deck}: {n} frames -> {name}.pdf, {name}_with-notes.pdf", flush=True)
