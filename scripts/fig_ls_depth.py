"""Figures for the Landscapes depth layer.   .venv/bin/python -W ignore scripts/fig_ls_depth.py [LS01 ...]"""
import math, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *

def LS01():
    # (a) effective discharge: frequency x work
    q = np.logspace(-2, 2.2, 600); s = 1.0
    f = np.exp(-(np.log(q)) ** 2 / (2 * s * s)) / (s * math.sqrt(2 * math.pi))   # density per ln q
    fig, ax = plt.subplots(1, 2, figsize=(10.4, 3.9))
    a = ax[0]; a.grid(True)
    a.plot(q, f / f.max(), color=MUTED, lw=2, label="frequency of events")
    for b, c in [(1, BLUE), (2, ORANGE), (3, AQUA)]:
        w = q ** b * f; a.plot(q, w / w.max(), color=c, label=f"work, transport $\\propto q^{{{b}}}$")
        a.plot([math.exp(b)], [1], "o", color=c, ms=5)
    a.set_xscale("log"); a.set_xlabel("event size $q$ (median = 1)"); a.set_ylabel("relative (per $\\ln q$)")
    a.set_title("Which events do the work?"); a.legend(fontsize=8, loc="upper left")
    # (b) low-pass filter
    b_ = ax[1]
    wt = np.logspace(-2, 2, 400)
    b_.plot(wt, 1 / np.sqrt(1 + wt ** 2), color=BLUE, label="amplitude ratio")
    b_.plot(wt, np.degrees(np.arctan(wt)) / 90, color=ORANGE, label="phase lag / 90°")
    for lab, tau, T in [("tau=1 Myr,\n41-kyr tilt", 1e6, 4.1e4), ("tau=10 kyr,\n100-kyr cycle", 1e4, 1e5)]:
        x = 2 * math.pi * tau / T; b_.plot([x], [1 / math.sqrt(1 + x * x)], "o", color=INK, ms=5)
        b_.annotate(lab, (x, 1 / math.sqrt(1 + x * x)), xytext=(6, 8), textcoords="offset points", fontsize=8)
    b_.set_xscale("log"); b_.set_yscale("log"); b_.set_ylim(3e-3, 1.5); b_.set_xlabel("$\\omega\\tau$ (response time $\\times$ forcing frequency)")
    b_.set_title("A landscape is a low-pass filter"); b_.legend(fontsize=8, loc="lower left")
    save(fig, "fig_ls01_magfreq_filter")

def LS02():
    yr = 3.156e7
    fig, ax = plt.subplots(figsize=(10, 3.6)); ax.grid(True, axis="x")
    mats = [("ice ($\\eta=10^{13}$ Pa s)", 2.9e3, BLUE), ("lower crust ($10^{20}$)", 1e20/4e10, AQUA), ("mantle ($10^{21}$)", 1e21/7e10, VIOLET)]
    ys = [3, 2, 1]
    for (nm, t, c), y in zip(mats, ys):
        ax.plot([t, 1e16], [y, y], color=c, lw=6, alpha=.35, solid_capstyle="butt"); ax.plot([t], [y], "o", color=c, ms=8)
        ax.text(t * 1.4, y + .22, f"{nm}: $\\tau_M$ = {t/yr:.2g} yr" if t > yr else f"{nm}: $\\tau_M$ = {t:.2g} s", fontsize=8.5)
    for nm, t in [("earthquake wave\n(seconds)", 5), ("post-seismic\n(years)", 1 * yr), ("ice-age\nrebound (10 kyr)", 1e4 * yr), ("orogeny\n(10 Myr)", 1e7 * yr)]:
        ax.axvline(t, color=MUTED, ls="--", lw=1); ax.text(t * 1.2, 4.75, nm, fontsize=8, color=MUTED, va="top")
    ax.set_xscale("log"); ax.set_xlim(1e-6, 1e16); ax.set_ylim(.4, 5); ax.set_yticks([])
    ax.set_xlabel("time scale of the loading $T$ (s)")
    ax.set_title("Elastic to the left of a material's Maxwell time, viscous to the right (thick bars = viscous regime)")
    save(fig, "fig_ls02_maxwell")

def LS03():
    fig, ax = plt.subplots(1, 2, figsize=(10.2, 3.8))
    n = np.linspace(3, 60, 400); kd = 2 * np.pi / n
    ax[0].plot(n, np.sin(kd) / kd, color=BLUE, label="slope (central difference)")
    ax[0].plot(n, 2 * (1 - np.cos(kd)) / kd ** 2, color=ORANGE, label="curvature (second difference)")
    ax[0].axhline(.99, color=MUTED, ls=":", lw=1); ax[0].text(34, .985, "1% error", fontsize=8, color=MUTED, va="top")
    ax[0].set_xlabel("wavelength / cell size"); ax[0].set_ylabel("recovered fraction of the true value"); ax[0].set_ylim(0, 1.03); ax[0].legend(fontsize=8, loc="lower right")
    ax[0].set_title("What a DEM grid does to slope and curvature")
    th = np.linspace(0, 45, 200); t = np.radians(th)
    ax[1].plot(th, np.cos(t) + (math.sqrt(2) - 1) * np.sin(t), color=BLUE)
    ax[1].plot([22.5], [math.cos(math.radians(22.5)) + (math.sqrt(2) - 1) * math.sin(math.radians(22.5))], "o", color=ORANGE)
    ax[1].annotate("worst case +8.2 %\nat 22.5°", (22.5, 1.0824), xytext=(26, 1.02), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
    ax[1].set_xlabel("true flow direction from the grid axis (deg)"); ax[1].set_ylabel("D8 path length / straight length"); ax[1].set_ylim(.99, 1.1)
    ax[1].set_title("D8 routing lengthens every flow path")
    save(fig, "fig_ls03_grid_errors")

if __name__ == "__main__":
    for c in (sys.argv[1:] or ["LS01"]): globals()[c]()
