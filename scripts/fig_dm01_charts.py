"""DM01 - stereographic charts (circle picture), the transition map w -> w/|w|^2 on lines, and the incompatible chart x^3."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.4), gridspec_kw=dict(width_ratios=[1.0, 1.05, 1.0]))

# A: stereographic charts of S^1 (the S^2 case adds one more coordinate) ---------------------------------------------------------
a = axes[0]
t = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(t), np.sin(t), color=INK, lw=1.6)
a.plot([-2.7, 2.7], [0, 0], color=MUTED, lw=1)
a.scatter([0], [1], color=BLUE, s=44, zorder=4); a.scatter([0], [-1], color=ORANGE, s=44, zorder=4)
a.text(0.08, 1.08, "N", color=BLUE, fontsize=10); a.text(0.08, -1.2, "S", color=ORANGE, fontsize=10)
for ang, col in ((0.55, AQUA), (2.4, VIOLET)):
    p = np.array([np.cos(ang), np.sin(ang)])
    wN = p[0] / (1 - p[1])                                 # chart from N
    wS = p[0] / (1 + p[1])                                 # chart from S
    a.plot([0, wN], [1, 0], color=BLUE, lw=1.1, alpha=0.9)
    a.plot([0, wS], [-1, 0], color=ORANGE, lw=1.1, alpha=0.9)
    a.scatter([p[0]], [p[1]], color=col, s=34, zorder=5)
    a.scatter([wN], [0], color=BLUE, s=16, zorder=5); a.scatter([wS], [0], color=ORANGE, s=16, zorder=5)
a.text(-2.7, 1.55, "chart ψ_N: blue dots on the axis\nchart ψ_S: orange dots on the axis", fontsize=8.2, color=INK, va="top")
a.text(-2.7, -1.55, "transition ψ_S∘ψ_N⁻¹(w) = 1/w  (w ≠ 0)", fontsize=9, color=INK)
a.set_aspect("equal"); a.set_xlim(-2.8, 2.8); a.set_ylim(-1.8, 1.6); a.axis("off")
a.set_title("A  two charts cover the circle", fontsize=10)

# B: the transition map of S^2 is the inversion w -> w/|w|^2; vertical lines go to circles through the origin ------------------------
b = axes[1]
y = np.linspace(-4, 4, 800)
for c, col in ((0.5, AQUA), (1.0, BLUE), (2.0, ORANGE), (-1.0, VIOLET)):
    w = np.stack([np.full_like(y, c), y])
    img = w / (w ** 2).sum(0)
    b.plot(w[0], w[1], color=col, lw=1.0, alpha=0.55)
    b.plot(img[0], img[1], color=col, lw=2.0, label=f"line x = {c:g}  →  circle through 0")
b.scatter([0], [0], color=RED, s=30, zorder=5)
b.set_aspect("equal"); b.set_xlim(-2.4, 2.4); b.set_ylim(-2.4, 2.4); b.legend(fontsize=7.4, loc="lower center", ncol=1, bbox_to_anchor=(0.5, -0.38))
b.text(-2.3, 2.05, "S²: ψ_S∘ψ_N⁻¹(w) = w/|w|²\nsmooth on R²∖0, det = −1/|w|⁴", fontsize=8.6, color=INK, va="top")
b.set_title("B  the transition map of S²", fontsize=10)

# C: the chart x^3 is NOT smoothly compatible with the identity chart ------------------------------------------------------------------
c = axes[2]
yy = np.linspace(-1, 1, 801)
c.plot(yy, np.cbrt(yy), color=BLUE, lw=2.2, label="y ↦ y^{1/3}  (transition id ∘ (x³)⁻¹)")
c.plot(yy, yy ** 3, color=ORANGE, lw=1.6, label="x ↦ x³  (transition (x³) ∘ id⁻¹: smooth)")
c.scatter([0], [0], color=RED, zorder=5, s=30)
c.text(0.08, -0.12, "slope (1/3)y^{-2/3}:\n33 at y = 10⁻³, 3333 at 10⁻⁶", fontsize=8.4, color=RED)
c.set_xlim(-1.05, 1.05); c.set_ylim(-1.1, 1.1); c.set_aspect("equal"); c.legend(fontsize=7.4, loc="upper left")
c.set_title("C  two charts on R, one smooth structure each", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.04, "A: stereographic charts of the circle; S² is identical with one more coordinate. B and C: transition maps decide whether two charts are smoothly compatible "
         "(numbers: dm_numbers.py, DM01).", ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm01_charts")
