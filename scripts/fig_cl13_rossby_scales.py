"""CL13 - Rossby number Ro = U/(f L) for atmospheric and oceanic motions (f at 45 deg, 1.03e-4 s-1).
Lines of constant U; labelled points are order-of-magnitude (U, L) pairs (Holton-type scale table in Suhas pre-midsem notes p.14).
"""
from figlib import *

f = 2 * OMEGA * np.sin(np.radians(45))
L = np.logspace(1, 7.5, 200)
fig, ax = plt.subplots(figsize=(7.8, 4.7))
for U, c, ls in [(0.1, AQUA, "-"), (1, BLUE, "-"), (10, ORANGE, "-"), (50, VIOLET, "-")]:
    ax.plot(L, U / (f * L), color=c, label=f"U = {U:g} m/s", ls=ls)
ax.axhline(1, color=INK, lw=1.2, ls="--")
ax.text(12, 1.25, "Ro = 1: rotation and advection equal", fontsize=8.5)
ax.fill_between(L, 1e-4, 1, color=BLUE, alpha=0.06, lw=0)
pts = [("tornado", 50, 1e2), ("thunderstorm", 10, 1e4), ("hurricane", 50, 1e5), ("synoptic cyclone", 10, 1e6),
       ("planetary wave", 20, 1e7), ("ocean gyre", 0.1, 1e6)]
for name, U, Lc in pts:
    ro = U / (f * Lc)
    ax.plot([Lc], [ro], "o", color=INK, ms=5, zorder=5)
    print(f"{name}: U={U} m/s, L={Lc:g} m, Ro={ro:.3g}")
    dy = 8 if name not in ("ocean gyre",) else -14
    ax.annotate(f"{name}\nRo≈{ro:.2g}", (Lc, ro), xytext=(6, dy), textcoords="offset points", fontsize=8, ha="left")
ax.set_xscale("log"); ax.set_yscale("log")
ax.set_xlim(10, 3e7); ax.set_ylim(1e-4, 1e5)
ax.set_xlabel("horizontal scale L (m)")
ax.set_ylabel("Rossby number  Ro = U/(fL)")
ax.set_title("Rotation controls only the large, slow motions (shaded: Ro < 1)", fontsize=10.5)
ax.legend(loc="upper right", fontsize=8.5)
save(fig, "fig_cl13_rossby_scales")
