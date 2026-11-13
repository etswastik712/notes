"""CL23 figure: reach of heat (conduction vs stirring), weather-kicked slab spectra, timescale ruler.  .venv/bin/python -I scripts/fig_cl23.py"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa

YR = 365.25 * 86400.0
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.4))
# A: reach d(period)
a = ax[0]
per = np.logspace(math.log10(86400.0), math.log10(1000 * YR), 200)
om = 2 * np.pi / per
for kap, lab, col, ls in ((0.5e-6, "soil  κ = 5×10⁻⁷", ORANGE, "-"), (1.4e-7, "still water  κ = 1.4×10⁻⁷", AQUA, "-"), (1e-5, "below mixed layer  K = 10⁻⁵", BLUE, "--"), (1e-4, "K = 10⁻⁴", BLUE, "-")):
    a.loglog(per / YR, np.sqrt(2 * kap / om), color=col, ls=ls, lw=2, label=lab)
a.axhspan(10, 100, xmin=0, xmax=1, color="#6d8bff", alpha=0.10)
a.text(2.5e-3, 45, "mixed layer: stirred, tens of m", fontsize=7.8, color=BLUE)
for x, t in ((1 / 365.25, "day"), (1, "year"), (100, "century")):
    a.axvline(x, color="#aaa", lw=0.7); a.text(x * 1.1, 0.012, t, fontsize=8, color="#555")
a.set_xlabel("period of the swing (yr)"); a.set_ylabel("reach  d = √(2κ/ω)  (m)"); a.set_ylim(0.01, 1000)
a.legend(fontsize=7.4, frameon=False, loc="upper left")
a.set_title("A  how deep does a swing reach?", fontsize=9.8)
# B: spectra
b_, CL, CM, CD, GAM, b = ax[1], 1e7, 4.2e6 * 75, 4.2e9, 0.7, 2.09
Zl = lambda w: 1j * w * CL + b
Zm = lambda w: 1j * w * CM + b
Zd = lambda w: 1j * w * CM + b + GAM * 1j * w * CD / (1j * w * CD + GAM)
P = np.logspace(-1.3, 3.2, 300) * YR; w = 2 * np.pi / P
for Z, lab, col in ((Zl, "land  (τ = 2 months)", ORANGE), (Zm, "mixed layer  (τ ≈ 5 yr)", BLUE), (Zd, "+ deep ocean  (τ ≈ 190 yr)", AQUA)):
    b_.loglog(P / YR, (1 / abs(Z(w)) ** 2) * b ** 2, color=col, lw=2, label=lab)
for tau, col in ((CL / b, ORANGE), (CM / b, BLUE)):
    b_.axvline(2 * np.pi * tau / YR, color=col, lw=0.8, ls=":")
b_.set_xlabel("period (yr)"); b_.set_ylabel("temperature power / slow-limit power of a land slab")
b_.legend(fontsize=7.6, frameon=False, loc="lower right", bbox_to_anchor=(1.0, 0.0)); b_.set_ylim(1e-4, 3)
b_.text(0.06, 2e-4, "fast: C sets it\n(power ∝ 1/C²)", fontsize=8); b_.text(25, 0.012, "slow: λ sets it,\nC drops out", fontsize=8)
b_.set_title("B  weather-kicked slabs (white push F′)", fontsize=9.8)
# C: ruler
c = ax[2]
rows = [("land (1 m)", 1.0), ("atmosphere (2.4 m)", 2.4), ("mixed layer (50 m)", 50.0), ("full ocean (4 km)", 4000.0)]
taus = [m * 4.2e6 / 3.8 / YR for _, m in rows]
c.barh(range(4), taus, color=[ORANGE, "#c9a227", BLUE, AQUA], height=0.55)
c.set_xscale("log"); c.set_yticks(range(4)); c.set_yticklabels([r for r, _ in rows], fontsize=8.2); c.invert_yaxis()
for i, t in enumerate(taus):
    c.text(t * 1.25, i, ("%.0f days" % (t * 365.25)) if t < 0.2 else ("%.1f yr" % t if t < 10 else "%.0f yr" % t), va="center", fontsize=8.5)
c.set_xlim(1e-2, 1e3); c.set_xlabel("τ = C/λ  (yr), λ = 3.8 W m⁻² K⁻¹")
c.set_title("C  the ruler: more water, slower", fontsize=9.8)
fig.subplots_adjust(wspace=0.42)
save(fig, "fig_cl23_inertia")
