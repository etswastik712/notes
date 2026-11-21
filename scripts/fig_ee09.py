#!/usr/bin/env python3
"""EE09 Figure 9.1: de Finetti diagram with the Hardy-Weinberg parabola and one generation of random mating."""
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
# barycentric -> cartesian: AA at (0,0), aa at (1,0), Aa at (0.5, sqrt3/2); x = q + Q... use x = R + Q/2 = q, y = Q*sqrt3/2
s3 = np.sqrt(3) / 2
def xy(P, Q, R): return R + Q / 2, Q * s3
fig, ax = plt.subplots(figsize=(6.2, 5.2))
ax.plot([0, 1, 0.5, 0], [0, 0, s3, 0], color="0.3", lw=1.2)
q = np.linspace(0, 1, 400); X, Y = xy((1 - q) ** 2, 2 * q * (1 - q), q * q)
ax.plot(X, Y, color="#c0392b", lw=2.2, label=r"Hardy–Weinberg: $Q^2=4PR$")
for P, Q, R, c in [(0.3, 0.6, 0.1, "#2471a3"), (0.2, 0.8, 0.0, "#2471a3"), (0.5, 0.0, 0.5, "#117a65"), (0.5, 0.2, 0.3, "#7d3c98")]:
    p = P + Q / 2; x0, y0 = xy(P, Q, R); x1, y1 = xy(p * p, 2 * p * (1 - p), (1 - p) ** 2)
    ax.plot(x0, y0, "o", color=c, ms=7); ax.annotate("", (x1, y1), (x0, y0), arrowprops=dict(arrowstyle="->", color=c, lw=1.6))
    ax.text(x0 + 0.02, y0 + (0.03 if Q > 0.3 else -0.05), f"{P}:{Q}:{R}", color=c, fontsize=9)
ax.plot(*xy(0.36, 0.48, 0.16), "s", color="k", ms=6)
ax.text(0.37, 0.40, "0.36 : 0.48 : 0.16\n(both blue starts, p = 0.6)", fontsize=8.5, ha="right")
for lab, (x, y) in {"AA": (-0.04, -0.04), "aa": (1.0, -0.04), "Aa": (0.5, s3 + 0.03)}.items(): ax.text(x, y, lab, fontsize=12, ha="center")
ax.set_xlabel("allele frequency q of a  (= R + Q/2)"); ax.set_yticks([]); ax.set_xlim(-0.08, 1.08); ax.set_ylim(-0.08, s3 + 0.1)
ax.set_title("One generation of random mating moves a population\nvertically onto the HW parabola (q unchanged)", fontsize=10.5)
ax.legend(loc="upper right", fontsize=9, frameon=False); ax.set_aspect("equal"); [ax.spines[k].set_visible(False) for k in ("top", "right", "left")]
fig.tight_layout(); fig.savefig("Assets/figures/fig_ee09_de_finetti.png", dpi=160); print("ok")
