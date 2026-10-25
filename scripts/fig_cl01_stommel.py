"""CL01 - a Stommel-type diagram: processes of the climate system on a time-scale vs length-scale plane (schematic).

Boxes are order-of-magnitude placements (Stommel 1963 style), NOT data.  Colour = which sphere the process lives in.
"""
from matplotlib.patches import Rectangle

from figlib import *

# name, t_lo, t_hi (s), L_lo, L_hi (m), sphere
P = [
    ("turbulent eddies", 1e0, 1e2, 1e-2, 1e1, "A"),
    ("cumulus / thunderstorm", 1e3, 1e4, 1e3, 1e4, "A"),
    ("mesoscale systems", 1e4, 1e5, 1e4, 1e5, "A"),
    ("fronts, cyclones", 1e5, 1e6, 1e5, 2e6, "A"),
    ("planetary waves, jets", 1e6, 3e6, 3e6, 2e7, "A"),
    ("seasonal cycle, monsoon", 5e6, 4e7, 1e6, 2e7, "A"),
    ("ocean eddies", 1e6, 1e7, 1e4, 3e5, "O"),
    ("ENSO", 5e7, 2e8, 5e6, 2e7, "O"),
    ("gyres, decadal variability", 3e8, 3e9, 1e6, 1.5e7, "O"),
    ("overturning circulation", 1e10, 1e11, 1e6, 2e7, "O"),
    ("glacial cycles", 1e12, 1e13, 1e6, 2e7, "I"),
    ("continental drift, orogeny", 3e14, 1e16, 1e5, 2e7, "S"),
]
COL = {"A": BLUE, "O": ORANGE, "I": AQUA, "S": MUTED}
NAME = {"A": "atmosphere", "O": "ocean", "I": "cryosphere (ice sheets)", "S": "solid Earth"}

fig, ax = plt.subplots(figsize=(8.4, 5.4))
for i, (nm, t0, t1, l0, l1, s) in enumerate(P, 1):
    ax.add_patch(Rectangle((t0, l0), t1 - t0, l1 - l0, fc=COL[s], ec=COL[s], alpha=0.22, lw=1.4))
    ax.add_patch(Rectangle((t0, l0), t1 - t0, l1 - l0, fc="none", ec=COL[s], lw=1.4))
    ax.annotate(str(i), (np.sqrt(t0 * t1), np.sqrt(l0 * l1)), ha="center", va="center", fontsize=9, fontweight="bold", color=INK)
key = "\n".join(f"{i:>2}  {p[0]}" for i, p in enumerate(P, 1))
ax.text(0.985, 0.03, key, transform=ax.transAxes, ha="right", va="bottom", fontsize=7.6, color=INK, family="DejaVu Sans Mono",
        bbox=dict(boxstyle="round,pad=0.4", fc=SURFACE, ec=GRID))
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.5, 1e17)
ax.set_ylim(3e-3, 3e8)
marks = [(60, "1 min"), (3600, "1 h"), (86400, "1 day"), (3.156e7, "1 yr"), (3.156e10, "1 kyr"), (3.156e13, "1 Myr")]
for x, lab in marks:
    ax.axvline(x, color=GRID, lw=0.8, zorder=0)
    ax.annotate(lab, (x, 4e-3), ha="center", va="bottom", fontsize=7.5, color=MUTED, rotation=90)
for y, lab in [(1, "1 m"), (1e3, "1 km"), (6.4e6, "Earth radius")]:
    ax.axhline(y, color=GRID, lw=0.8, zorder=0)
    ax.annotate(lab, (0.6, y), ha="left", va="bottom", fontsize=7.5, color=MUTED)
ax.set_xlabel("time scale (s)")
ax.set_ylabel("length scale (m)")
ax.set_title("Climate-system processes span 17 decades of time and 10 of length\n(schematic order-of-magnitude placement, not data)", fontsize=10.5)
for i, (k, v) in enumerate(NAME.items()):
    ax.add_patch(Rectangle((0, 0), 0, 0, fc=COL[k], ec=COL[k], alpha=0.5, label=v))
ax.legend(loc="upper left", fontsize=8, ncol=1)
save(fig, "fig_cl01_stommel")
