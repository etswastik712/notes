"""CL01 - residence times of water in Earth-system reservoirs (log scale).

Data: average residence times as tabulated on Wikipedia 'Water cycle' (accessed 2026-10-23); ranges are drawn as bars.
Ocean volume 1.338e9 km3 (97 %), ice 2.4e7 km3 (1.7 %) from the same page.
"""
from figlib import *

D = 1 / 365.25
M = 1 / 12
# name, lo, hi (years), sphere
R = [
    ("atmosphere", 9 * D, 9 * D, "A"),
    ("soil moisture", 1 * M, 2 * M, "L"),
    ("rivers", 2 * M, 6 * M, "L"),
    ("seasonal snow", 2 * M, 6 * M, "I"),
    ("glaciers", 20, 100, "I"),
    ("lakes", 50, 100, "L"),
    ("shallow groundwater", 100, 200, "L"),
    ("oceans", 3200, 3200, "O"),
    ("deep groundwater", 10000, 10000, "L"),
    ("Antarctic ice", 20000, 20000, "I"),
]
COL = {"A": BLUE, "O": ORANGE, "I": AQUA, "L": MUTED}
LAB = {"atmosphere": "9 days", "soil moisture": "1–2 months", "rivers": "2–6 months", "seasonal snow": "2–6 months",
       "glaciers": "20–100 yr", "lakes": "50–100 yr", "shallow groundwater": "100–200 yr", "oceans": "3,200 yr",
       "deep groundwater": "10,000 yr", "Antarctic ice": "20,000 yr"}
R = sorted(R, key=lambda r: np.sqrt(r[1] * r[2]))
fig, ax = plt.subplots(figsize=(7.2, 4.0))
for i, (nm, lo, hi, s) in enumerate(R):
    if hi > lo:
        ax.plot([lo, hi], [i, i], color=COL[s], lw=7, solid_capstyle="butt")
    ax.plot([np.sqrt(lo * hi)], [i], "o", color=COL[s], ms=8 if hi == lo else 0, mec=INK, mew=0.8)
    lab = LAB[nm]
    ax.annotate(lab, (hi * 1.35, i), va="center", fontsize=8, color=MUTED)
ax.set_yticks(range(len(R)))
ax.set_yticklabels([r[0] for r in R])
ax.set_xscale("log")
ax.set_xlim(1e-2, 3e5)
ax.set_xlabel("average residence time of water (years, log scale)")
ax.set_title("From 9 days to 20,000 years: a hierarchy of memory")
ax.grid(axis="y", visible=False)
ax.annotate("blue: air · orange: ocean · aqua: ice · grey: land water", (1.2e-2, -0.9), fontsize=7.8, color=MUTED)
ax.set_ylim(-1.2, len(R) - 0.4)
save(fig, "fig_cl01_reservoirs")
