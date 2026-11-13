"""CL27 figure: Daisyworld tutorials (my simulations of Joy's models).   .venv/bin/python -I scripts/fig_cl27.py"""
import os, sys, importlib.util
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
here = os.path.dirname(os.path.abspath(__file__))
def load(n):
    sp = importlib.util.spec_from_file_location(n, os.path.join(here, n + ".py")); m = importlib.util.module_from_spec(sp); sys.argv = ["x"]; sp.loader.exec_module(m); return m
dl, do = load("daisy_land_ocean"), load("daisy_ocean")
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.5))
a = ax[0]
for f, col, lab in ((1.0, ORANGE, "all land"), (0.7, AQUA, "30 % ocean"), (0.3, BLUE, "70 % ocean")):
    o = dl.sweep(f)
    L = [r[0] for r in o]; a.plot(L, [r[1] for r in o], color=col, lw=2, label=lab); a.plot(L, [r[2] for r in o], color=col, lw=1, ls="--")
a.axhspan(17.5, 27.5, color="#bbb", alpha=0.25); a.text(1.62, 22.5, "22.5 ± 5 °C", fontsize=7.5, color="#666", va="center")
a.set_xlim(0.4, 1.8); a.set_ylim(-5, 80); a.set_xlabel("sun brightness L"); a.set_ylabel("planet temperature (°C)")
a.legend(fontsize=8, frameon=False, loc="upper left"); a.set_title("A  daisy planet (solid) vs bare planet (dashed)", fontsize=9.8)
b = ax[1]
for lab, f, h, col in (("all land", 1.0, 50, ORANGE), ("30 % ocean, 50 m", 0.7, 50, AQUA), ("30 % ocean, 500 m", 0.7, 500, BLUE)):
    _, ser = dl.sudden(f, h, years=30.0)
    t = np.array([r[0] for r in ser]); T0 = ser[0][1]; b.semilogx(np.maximum(t, 1e-3) , [r[1] - T0 for r in ser], color=col, lw=2, label=lab + " (daisies)")
    b.semilogx(np.maximum(t, 1e-3), [r[2] - ser[0][2] for r in ser], color=col, lw=1, ls="--")
b.axhline(0, color="#888", lw=.6); b.set_xlim(1e-2, 30); b.set_xlabel("years after the sun jumps from L = 0.78 to 0.86"); b.set_ylabel("temperature change (°C)")
b.legend(fontsize=7.6, frameon=False, loc="upper right"); b.set_title("B  sudden change (dashed: bare planet)", fontsize=9.8)
c = ax[2]
m = do.Life(sigma=0.0); m.run(1500, 30, noise=False); r = m.run(40, 7, noise=False)
t = r[:, 0]
c.semilogy(t, r[:, 6], color=INK, lw=2, label="grazers (log, left)")
c.set_ylabel("grazers"); c.set_xlabel("years"); c.set_ylim(5e-3, 1)
c2 = c.twinx(); c2.plot(t, r[:, 1], color=ORANGE, lw=1.6, label="land T"); c2.plot(t, r[:, 2], color=BLUE, lw=1.6, label="mixed-layer T"); c2.set_ylabel("temperature (°C)")
h1, l1 = c.get_legend_handles_labels(); h2, l2 = c2.get_legend_handles_labels(); c.legend(h1 + h2, l1 + l2, fontsize=7.6, frameon=False, loc="lower left")
c.set_title("C  grazers + daisies + ocean delay: an 8-yr cycle", fontsize=9.8)
fig.subplots_adjust(wspace=0.4)
save(fig, "fig_cl27_daisyworld")
