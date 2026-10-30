"""PA12 - the one-point compactification, local finiteness, and an exhaustion by compact sets."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.2), gridspec_kw=dict(width_ratios=[1.1, 1.15, 1]))

# A: stereographic projection, side view --------------------------------------------------------------------------
a = axes[0]
t = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(t), np.sin(t), color=MUTED, lw=1.4)
a.plot([-1.4, 4.8], [0, 0], color=INK, lw=1.2)
a.scatter([0], [1], color=RED, s=46, zorder=4)
a.text(0.1, 1.1, "N = ∞", color=RED, fontsize=10)
cols = [BLUE, ORANGE, AQUA, VIOLET]
for w, c in zip((0.7, 1.6, 3.2, 4.4), cols):
    r2 = w * w
    p = np.array([2 * w, r2 - 1]) / (r2 + 1)                      # sigma^{-1}(w) in the (x, z) plane, 2-D slice
    a.plot([0, w], [1, 0], color=c, lw=1.2, alpha=0.9)
    a.scatter([w], [0], color=c, s=26, zorder=3)
    a.scatter([p[0]], [p[1]], color=c, s=26, zorder=3)
a.text(3.3, -0.16, "plane R² (side view)", fontsize=8.6, color=MUTED)
a.text(-1.4, -1.35, "points far out in the plane map to\npoints close to N:  |σ⁻¹(w) − N| = 2/√(1+|w|²)\n(|w| = 1000:  2.0×10⁻³)", fontsize=8.6, color=INK, va="top")
a.set_aspect("equal"); a.set_xlim(-1.5, 4.9); a.set_ylim(-2.7, 1.45); a.axis("off")
a.set_title("A  R² ∪ {∞} ≅ S²", fontsize=10)

# B: local finiteness depends on the ambient space ---------------------------------------------------------------
b = axes[1]
for n in range(1, 16):
    lo, hi = 1 / (n + 2), 1 / n
    b.plot([lo, hi], [n, n], color=BLUE, lw=3.2, solid_capstyle="butt")
b.axvline(0.0, color=RED, lw=1.6)
b.text(0.012, 15.7, "0 ∉ (0,1)", color=RED, fontsize=9)
b.axvspan(0.04, 0.06, color=ORANGE, alpha=0.18)
b.text(0.3, 13.6, "a small ball around 0.05 meets 10\nmembers: finitely many near every x > 0", fontsize=8.4, color=INK)
b.text(0.3, 10.0, "a ball of radius r around 0 would meet\nevery member with n ≥ 1/r: not locally\nfinite in [0,1)", fontsize=8.4, color=RED)
b.set_xlim(-0.03, 0.72); b.set_ylim(0, 17); b.set_xlabel("x"); b.set_ylabel("member n:  (1/(n+2), 1/n)")
b.set_title("B  locally finite in (0,1), not in [0,1)", fontsize=10)

# C: an exhaustion of the plane by compact discs and the induced locally finite annuli --------------------------------
c = axes[2]
for j in range(4, 0, -1):
    c.add_patch(plt.Circle((0, 0), j, facecolor=[BLUE, AQUA, ORANGE, VIOLET][j - 1], alpha=0.16, edgecolor=MUTED, lw=1))
    c.text(0.0, j - 0.35, f"K{j}", ha="center", fontsize=9, color=INK)
c.text(0, -4.55, "K_j ⊂ int K_{j+1},   ∪ K_j = R²", ha="center", fontsize=8.8, color=INK)
c.set_aspect("equal"); c.set_xlim(-4.4, 4.4); c.set_ylim(-4.9, 4.4); c.axis("off")
c.set_title("C  exhaustion by compact discs", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: stereographic projection (pa12_numbers.py). B: the family (1/(n+2), 1/n), n ≥ 1, counted by pa12_numbers.py. "
         "C: the compact sets of a compact exhaustion; the annuli K_{j+1} ∖ int K_{j−1} give a locally finite refinement of any open cover.",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_pa12_compact")
