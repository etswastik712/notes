"""Organise books from Downloads into the repo's  <subject>/<topic>/books/  scheme (physics/quantum-mechanics/books, math/probability/books, ...).

    .venv/bin/python -W ignore scripts/organise_books.py --plan          # dry run: destinations, duplicates, collisions (writes scripts/_work/books_plan.csv)
    .venv/bin/python -W ignore scripts/organise_books.py --apply         # move (rename) the unique files, write Assets/data/books-manifest.csv

Inputs: the staged zips (~/Downloads/_unzipped/<zip>/<zip>/...) and the loose books in ~/Downloads (LOOSE below).
Rules:
  * the user's own folder names are the topic names (Mathematics/<Level>/<Topic>/..., Physics/<Topic>/...); the Elementary/Intermediate/
    Advanced level is merged into one topic folder and kept only in the manifest;
  * topics that already exist as vault subjects use those folders (group-theory, probability, proofs-analysis-topology,
    quantum-mechanics, thermodynamics-stat-mech, waves);
  * flat or author-named zips are classified per file (PER_FILE below);
  * identical files (sha256) are filed once, the parent zips (Mathematics, Physics) winning; files already in the repo are not duplicated;
  * a book's companion material (solution manuals, Mathematica notebooks, resources) keeps its sub-folder under the topic's books/;
  * course notes (not books) go to <topic>/lecture-notes-slides/;  nothing is ever overwritten (a name clash gets a numeric suffix).
New books land in folders that .gitignore keeps out of git (the vault is auto-pushed to GitHub), see .gitignore.
"""
import argparse
import collections
import csv
import hashlib
import os
import re
import shutil
import sys

HOME = os.path.expanduser("~")
STAGE = os.path.join(HOME, "Downloads", "_unzipped")
DL = os.path.join(HOME, "Downloads")
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
BOOK_EXT = {".pdf", ".djvu", ".epub"}

# ---- the user's own topic folders -> repo folder (area/topic)
MATH_TOPIC = {
    "Algebraic Geometry": "math/algebraic-geometry", "Algebraic Topology": "math/algebraic-topology",
    "Combinatorics and Discrete Mathematics": "math/combinatorics-discrete-math", "Combinatorics and Discrete Math": "math/combinatorics-discrete-math",
    "Commutative and Homological Algebra": "math/commutative-homological-algebra", "Complex Analysis": "math/complex-analysis",
    "Differential Equations": "math/differential-equations", "Differential Geometry": "math/differential-geometry",
    "Differential Topology": "math/differential-topology", "Foundations": "math/proofs-analysis-topology",
    "Functional Analysis": "math/functional-analysis", "General Abstract Algebra": "math/general-abstract-algebra",
    "Geometric Measure Theory": "math/geometric-measure-theory", "Group Theory and Representation": "math/group-theory",
    "Harmonic Analysis": "math/harmonic-analysis", "Measure Theory": "math/measure-theory", "Number Theory": "math/number-theory",
    "Probability": "math/probability", "Problem Solving": "math/problem-solving", "Ring Theory": "math/ring-theory",
    "Algebra": "math/algebra", "Bridge reading": "math/proofs-analysis-topology", "Calculus": "math/calculus",
    "Geometry": "math/geometry", "Classical Geometry": "math/geometry", "Linear Algebra": "math/linear-algebra",
    "Multivariate Calculus": "math/calculus", "Point Set Topology": "math/proofs-analysis-topology", "Real Analysis": "math/proofs-analysis-topology",
}
PHYS_TOPIC = {
    "Electrodynamics": "physics/electromagnetism", "General Relativity and Cosmology": "physics/relativity",
    "Mathematical Methods": "physics/mathematical-physics", "Mathematical Physics": "physics/mathematical-physics",
    "Mechanics": "physics/classical-mechanics", "Particle Physics": "physics/particle-physics",
    "Quantum Field Theory": "physics/quantum-field-theory", "Quantum Mechanics": "physics/quantum-mechanics",
    "Statistical and Thermal Physics": "physics/thermodynamics-stat-mech", "String Theory": "physics/string-theory",
}
# ---- topic zips (everything in them goes to one topic unless PER_FILE says otherwise)
ZIP_TOPIC = {
    "Differential Equations": "math/differential-equations", "Differential Geometry": "math/differential-geometry",
    "Foundation": "math/proofs-analysis-topology", "Fourier Analysis": "math/harmonic-analysis", "Galois Theory": "math/galois-theory",
    "Geometry": "math/geometry", "Maths for Physicists": "physics/mathematical-physics", "Mechanics": "physics/classical-mechanics",
    "Nonlinear Dynamics": "physics/nonlinear-dynamics", "Particle Physics": "physics/particle-physics",
    "Quantum Field Theory": "physics/quantum-field-theory", "Relativity": "physics/relativity",
    "Statistical Mechanics and Thermodynamics": "physics/thermodynamics-stat-mech", "Feynman Lectures": "physics/general-physics",
}
# ---- per-file overrides / classification of flat and author zips: (zip, regex on the file or folder name) -> topic.  First match wins.
PER_FILE = [
    ("Mechanics", r"Vibrations and Waves", "physics/waves"),
    ("Algebra", r"Concrete Introduction to Higher Algebra", "math/general-abstract-algebra"),
    ("Algebra", r".", "math/group-theory"),                                   # Lie groups/algebras, representations, reflection groups
    ("Analysis", r"Browder|Pugh|Roussos|Tao - Analysis", "math/proofs-analysis-topology"),
    ("Analysis", r"Bressoud|Carter, B\. van Brunt|Axler|Bogachev|Royden", "math/measure-theory"),
    ("Analysis", r"Limaye|Conway|Bhatia|Kesavan|Rudin - Functional", "math/functional-analysis"),
    ("Analysis", r"Saff|Stein, Rami|Brown, Ruel|Schaum", "math/complex-analysis"),
    ("Analysis", r"Logarithmic Integral", "math/harmonic-analysis"),
    ("Topology", r"Algebraic Topology", "math/algebraic-topology"),
    ("Topology", r".", "math/proofs-analysis-topology"),
    ("Landau and Lifshitz", r"Vol\. 1 ", "physics/classical-mechanics"),
    ("Landau and Lifshitz", r"Vol\. 2 ", "physics/electromagnetism"),         # Classical Theory of Fields: special relativity + electrodynamics + GR
    ("Landau and Lifshitz", r"Vol\. 3 ", "physics/quantum-mechanics"),
    ("Landau and Lifshitz", r"Vol\. 4 |Course of theoretical physics\. 4", "physics/quantum-field-theory"),
    ("Landau and Lifshitz", r"Vol\. (5|9|10) ", "physics/thermodynamics-stat-mech"),
    ("Landau and Lifshitz", r"Vol\. (6|7) ", "physics/continuum-mechanics"),
    ("Landau and Lifshitz", r"Vol\. 8 ", "physics/electromagnetism"),
    ("Jakob Schwichtenberg", r"Classical Mechanics", "physics/classical-mechanics"),
    ("Jakob Schwichtenberg", r"Electrodynamics", "physics/electromagnetism"),
    ("Jakob Schwichtenberg", r"Quantum Field Theory", "physics/quantum-field-theory"),
    ("Jakob Schwichtenberg", r"Quantum Mechanics", "physics/quantum-mechanics"),
    ("Jakob Schwichtenberg", r"Physics from Finance|Physics from Symmetry", "physics/mathematical-physics"),
    ("Jakob Schwichtenberg", r"Teach Yourself Physics", "physics/general-physics"),
]
# ---- loose files in ~/Downloads: (file name, destination dir relative to repo, kind)
LOOSE = [
    ("Bruce van Brunt - The Calculus of Variations (2004).pdf", "math/calculus-of-variations/books", "book"),
    ("Foundations of Classical Electrodynamics - Charge, Flux, and -- Friedrich W. Hehl, Yuri N. Obukhov (auth.) -- ( WeLib.org ).pdf", "physics/electromagnetism/books", "book"),
    ("From calculus to cohomology - de Rham cohomology and -- Ib Madsen, Jorgen Tornehave -- ( WeLib.org ).pdf", "math/differential-topology/books", "book"),
    ("Mathematical Methods of Classical Mechanic - John.pdf", "physics/classical-mechanics/books", "book"),
    ("Peskin, An Introduction to Quantum Field Theory (1).pdf", "physics/quantum-field-theory/books", "book"),
    ("Robert Wald - Advanced Classical Electromagnetism (2022).pdf", "physics/electromagnetism/books", "book"),
    ("Zangwill A. - Modern Electrodynamics (2013).pdf", "physics/electromagnetism/books", "book"),
    ("Zangwill A. - Modern Electrodynamics solutions manual (2012).pdf", "physics/electromagnetism/books", "book"),
    ("b97450.pdf", "math/differential-geometry/books", "book"),                  # = Serge Lang, Introduction to Differentiable Manifolds, 2nd ed.
    ("Classical_Mechanics.pdf", "physics/classical-mechanics/lecture-notes-slides", "notes"),     # 17 pp. student notes (M. Alam, 2026)
    ("fourier-series.pdf", "math/harmonic-analysis/lecture-notes-slides", "notes"),               # 23 pp. course notes
    ("s11269-018-1930-8.pdf", "earth-and-climate/landscapes-geomorphology/books", "paper"),      # Yang et al. 2018, avulsions in a braided river (LS22)
]
RENAME = {"b97450.pdf": "Serge Lang - Introduction to Differentiable Manifolds, 2nd ed. (2002).pdf",
          "Mathematical Methods of Classical Mechanic - John.pdf": "V. I. Arnold - Mathematical Methods of Classical Mechanics (pdf scan).pdf",
          "Classical_Mechanics.pdf": "Mahfooz Alam - Classical Mechanics (student notes, 2026).pdf",
          "s11269-018-1930-8.pdf": "Yang, Lin, Zhou - Avulsions in a Simulated Large Lowland Braided River (2018).pdf"}
SKIP_NAMES = set()


def sha(path, cache={}):
    if path in cache:
        return cache[path]
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    cache[path] = h.hexdigest()
    return cache[path]


def staged_files():
    out = []
    for z in sorted(os.listdir(STAGE)):
        base = os.path.join(STAGE, z)
        if not os.path.isdir(base):
            continue
        for dp, dn, fn in os.walk(base):
            for f in fn:
                p = os.path.join(dp, f)
                rel = os.path.relpath(p, base).split(os.sep)
                if rel and rel[0] == z:                  # zips extract to <stem>/<top>/...; strip the repeated top folder
                    rel = rel[1:]
                out.append((z, rel, p))
    return out


def classify(zipname, inner):
    """-> (area/topic, subpath below the topic's books folder (list of dirs), level or '', kind)"""
    name = inner[-1]
    if zipname == "Mathematics":
        level, topic, rest = inner[0], inner[1], inner[2:]
        return MATH_TOPIC[topic], rest[:-1], level, "book"
    if zipname == "Physics":
        topic, rest = inner[0], inner[1:]
        return PHYS_TOPIC[topic], rest[:-1], "", "book"
    probe = " / ".join(inner)
    for z, rx, dest in PER_FILE:
        if z == zipname and re.search(rx, probe):
            return dest, inner[:-1] if len(inner) > 1 else [], "", "book"
    if zipname in ZIP_TOPIC:
        if zipname == "Nonlinear Dynamics" and inner[0] == "Santhanam Notes":
            return ZIP_TOPIC[zipname], ["Santhanam Notes"] + inner[1:-1], "", "notes"
        return ZIP_TOPIC[zipname], inner[:-1], "", "book"
    raise KeyError((zipname, inner))


def repo_books():
    """sha256 -> path of books already in the repo (small set: tracked books)."""
    idx = {}
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", ".venv", "node_modules", "_work")]
        if os.sep + "books" not in dp + os.sep and "lecture-notes-slides" not in dp:
            continue
        for f in fn:
            if os.path.splitext(f)[1].lower() in BOOK_EXT:
                idx.setdefault(os.path.getsize(os.path.join(dp, f)), []).append(os.path.join(dp, f))
    return idx


def build():
    items = []   # dict(src, dest_dir, name, zip, level, kind, size)
    for z, inner, p in staged_files():
        name = inner[-1]
        ext = os.path.splitext(name)[1].lower()
        if name in SKIP_NAMES or ext in (".rar",) or (ext == ".zip" and name.startswith("George Mark Bergman")):
            items.append(dict(src=p, zip=z, skip="nested archive already extracted" if ext in (".rar", ".zip") else "web page of a companion", name=name))
            continue
        top, sub, level, kind = classify(z, inner)
        folder = "lecture-notes-slides" if kind == "notes" else "books"
        d = os.path.join(top, folder, *sub)
        items.append(dict(src=p, dest_dir=d, name=name, zip=z, level=level, kind=kind, size=os.path.getsize(p), inner="/".join(inner)))
    for fn, d, kind in LOOSE:
        p = os.path.join(DL, fn)
        if os.path.exists(p):
            items.append(dict(src=p, dest_dir=d if "/books" in d or "/lecture" in d else d, name=RENAME.get(fn, fn), zip="(loose in Downloads)", level="", kind=kind, size=os.path.getsize(p), inner=fn))
    return items


def dedupe(items):
    """mark exact duplicates (same sha256) of staged files and of books already in the repo."""
    repo = repo_books()
    by_size = collections.defaultdict(list)
    for it in items:
        if "skip" not in it:
            by_size[it["size"]].append(it)
    for size, group in by_size.items():
        cand_repo = repo.get(size, [])
        if len(group) == 1 and not cand_repo:
            continue
        groups = collections.defaultdict(list)
        for it in group:
            groups[sha(it["src"])].append(it)
        repo_h = {sha(p): p for p in cand_repo}
        for h, g in groups.items():
            if h in repo_h:
                for it in g:
                    it["dup_of"] = "repo:" + os.path.relpath(repo_h[h], ROOT)
                continue
            if len(g) > 1:
                # keep the copy from a parent zip, then the loose file, else the first
                g.sort(key=lambda it: (0 if it["zip"] in ("Mathematics", "Physics") else 1 if it["zip"].startswith("(") else 2, it["src"]))
                keep = g[0]
                for it in g[1:]:
                    it["dup_of"] = f"{keep['zip']}: {keep['inner']}"
    return items


def target_paths(items):
    """destination file paths with clash handling (no overwrite)."""
    used = set()
    for it in items:
        if "skip" in it or "dup_of" in it:
            continue
        base = os.path.join(ROOT, it["dest_dir"], it["name"])
        p, n = base, 1
        while p in used or os.path.exists(p):
            stem, ext = os.path.splitext(base)
            n += 1
            p = f"{stem} ({n}){ext}"
        used.add(p)
        it["dest"] = p
    return items


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()
    items = target_paths(dedupe(build()))
    moves = [i for i in items if "dest" in i]
    dups = [i for i in items if "dup_of" in i]
    skips = [i for i in items if "skip" in i]
    dest_count = collections.Counter(os.path.relpath(os.path.dirname(i["dest"]), ROOT).split("/books")[0].split("/lecture-notes")[0] for i in moves)
    print(f"files seen: {len(items)}   to move: {len(moves)} ({sum(i['size'] for i in moves)/2**30:.2f} GiB)   exact duplicates (not filed): {len(dups)} ({sum(i['size'] for i in dups)/2**30:.2f} GiB)   skipped: {len(skips)}")
    for k, v in sorted(dest_count.items()):
        print(f"   {v:4d}  {k}")
    clash = [i for i in moves if re.search(r" \(\d+\)\.\w+$", os.path.basename(i["dest"])) and not re.search(r"\(\d{4}\)\.\w+$", os.path.basename(i["dest"]))]
    print(f"name clashes resolved with a suffix: {len(clash)}")
    os.makedirs(os.path.join(ROOT, "scripts", "_work"), exist_ok=True)
    with open(os.path.join(ROOT, "scripts", "_work", "books_plan.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["status", "zip", "level", "kind", "source (inside zip / Downloads)", "destination", "note"])
        for i in items:
            st = "move" if "dest" in i else "duplicate" if "dup_of" in i else "skip"
            w.writerow([st, i["zip"], i.get("level", ""), i.get("kind", ""), i.get("inner", i.get("name", "")), os.path.relpath(i["dest"], ROOT) if "dest" in i else "", i.get("dup_of", i.get("skip", ""))])
    if not a.apply:
        return
    moved = 0
    for i in moves:
        os.makedirs(os.path.dirname(i["dest"]), exist_ok=True)
        shutil.move(i["src"], i["dest"])
        moved += 1
    man = os.path.join(ROOT, "Assets", "data", "books-manifest.csv")
    os.makedirs(os.path.dirname(man), exist_ok=True)
    with open(man, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file (relative to the repo)", "size_MB", "origin zip", "level in the origin library", "kind", "path inside the origin"])
        for i in sorted(moves, key=lambda i: i["dest"]):
            w.writerow([os.path.relpath(i["dest"], ROOT), f"{i['size']/2**20:.1f}", i["zip"], i.get("level", ""), i.get("kind", ""), i["inner"]])
    print(f"moved {moved} files; manifest -> {os.path.relpath(man, ROOT)}")


if __name__ == "__main__":
    main()
