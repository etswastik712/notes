"""Run figure scripts.   usage (from the vault root):
    .venv/bin/python scripts/make_figures.py            # all fig_*.py
    .venv/bin/python scripts/make_figures.py cl04       # only scripts whose name contains 'cl04'
Outputs go to Assets/figures/ (PNG).  One script per figure, named fig_<chapter>_<slug>.py.
"""
import glob
import os
import subprocess
import sys

here = os.path.dirname(os.path.abspath(__file__))
pat = sys.argv[1] if len(sys.argv) > 1 else ""
for s in sorted(glob.glob(os.path.join(here, "fig_*.py"))):
    if pat in os.path.basename(s):
        print(f"--- {os.path.basename(s)}")
        r = subprocess.run([sys.executable, s], cwd=here, capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode:
            print(r.stderr.strip())
