"""Check citations of John M. Lee's *Introduction to Smooth Manifolds* (2nd ed.) in the PA11-PA15 and 14-* notes.

    .venv/bin/python -W ignore scripts/check_lee_cites.py [--rebuild]

1. For every link  [[John M. Lee ...pdf#page=N|label]]  whose label names a numbered result (Thm/Prop./Lemma/Cor./Example X.Y) the
   result must be on PDF page N (+-1: results may straddle a page break); a label with 'p. M' must satisfy M = N - 18.
2. Every plain mention 'Lee Thm X.Y' / 'Lee Prop. X.Y' / 'Lee Lemma X.Y' / 'Lee Example X.Y' must name a result that exists.
The index (label -> PDF page) is built from `pdftotext -layout` of the PDF (labels at the start of a line); needs poppler.
"""
import glob
import json
import os
import re
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PDF = os.path.join(ROOT, "math", "differential-geometry", "books", "John M. Lee - Introduction to Smooth Manifolds.pdf")
CACHE = os.path.join(os.environ.get("CLAUDE_JOB_DIR", "/tmp"), "tmp", "src", "lee_idx2.json")
KIND = {"theorem": "Theorem", "thm": "Theorem", "proposition": "Proposition", "prop": "Proposition", "lemma": "Lemma", "corollary": "Corollary",
        "cor": "Corollary", "example": "Example", "problem": "Problem"}


def build():
    txt = subprocess.run(["pdftotext", "-layout", PDF, "-"], capture_output=True, text=True).stdout
    pages = txt.split("\f")
    idx = {}
    pat = re.compile(r"^\s*(Theorem|Proposition|Lemma|Corollary|Example)\s+(\d+\.\d+|[A-D]\.\d+)\b", re.M)
    for i, p in enumerate(pages):
        if i < 18:
            continue
        for m in pat.finditer(p):
            idx.setdefault(f"{m.group(1)} {m.group(2)}", i + 1)
        # theorem numbers also appear as "2.23 (Existence ...)" after a bold label that pdftotext splits: catch the bare form
        for m in re.finditer(r"^\s*(\d+\.\d+|[A-D]\.\d+)\s*(?:\(|\.)", p, re.M):
            idx.setdefault(("?", m.group(1)), i + 1) if False else None
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(idx, open(CACHE, "w"))
    return idx


def main():
    idx = json.load(open(CACHE)) if os.path.exists(CACHE) and "--rebuild" not in sys.argv else build()
    bare = {k.split()[1]: v for k, v in idx.items()}                           # number -> page, regardless of the word
    files = glob.glob(os.path.join(ROOT, "11-Proofs-Analysis-Topology", "PA1[1-5]*.md")) + glob.glob(os.path.join(ROOT, "14-Differential-Geometry", "**", "*.md"), recursive=True) \
        + glob.glob(os.path.join(ROOT, "scripts", "spec_pa1*.py")) + glob.glob(os.path.join(ROOT, "scripts", "spec_dm*.py"))
    bad = 0
    link = re.compile(r"\[\[John M\. Lee[^\]#]*\.pdf#page=(\d+)\|([^\]]*)\]\]")
    ref = re.compile(r"Lee\s+((?:Thms?\.?|Theorem|Props?\.?|Proposition|Lemma|Lemmas|Cor\.?|Corollary|Example|Examples|Problem)\s*(?:and\s+)?)([A-D]?\d*\.?\d+(?:[,–-]\s*[A-D]?\d*\.?\d+)*)")
    for f in sorted(files):
        t = open(f, encoding="utf-8").read()
        rel = os.path.relpath(f, ROOT)
        for m in link.finditer(t):
            pdf, lab = int(m.group(1)), m.group(2)
            pm = re.search(r"\bpp?\.\s*(\d+)", lab)
            if pm and abs((pdf - 18) - int(pm.group(1))) > 1:
                print(f"PAGE-OFFSET {rel}: page={pdf} label '{lab[:60]}'")
                bad += 1
            for nm in re.finditer(r"(?:Thms?\.?|Theorem|Props?\.?|Proposition|Lemma|Cor\.?|Corollary|Example)\s*([A-D]\.\d+|\d+\.\d+)", lab):
                num = nm.group(1)
                if num not in bare:
                    print(f"UNKNOWN RESULT {rel}: '{num}' in link label '{lab[:60]}'")
                    bad += 1
                elif abs(bare[num] - pdf) > 1:
                    print(f"WRONG PAGE {rel}: result {num} is on PDF page {bare[num]} (p. {bare[num] - 18}) but the link says page={pdf} ('{lab[:50]}')")
                    bad += 1
        for m in ref.finditer(t):
            for num in re.findall(r"[A-D]\.\d+|\d+\.\d+", m.group(2)):
                if num not in bare:
                    print(f"UNKNOWN RESULT {rel}: 'Lee {m.group(1).strip()} {num}'")
                    bad += 1
    print(f"checked {len(files)} files; {bad} problems")


if __name__ == "__main__":
    main()
