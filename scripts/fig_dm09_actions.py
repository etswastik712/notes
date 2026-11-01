"""DM09 - orbit-stabiliser dimensions, the Euclidean group as a semidirect product, and the affine group of the line."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.4), gridspec_kw=dict(width_ratios=[1.15, 1.0, 1.0]))

# A: dim G = dim stabiliser + dim orbit ------------------------------------------------------------------------------------------------------------------
a = axes[0]
names = ["SO(3)\non S²", "O(4)\non S³", "U(2)\non S³", "SU(2)\non S²", "GL(3,ℝ) on\nSym(3)", "GL(2,ℂ) on\nHerm(2)"]
dG = np.array([3, 6, 4, 3, 9, 8]); dH = np.array([1, 3, 1, 1, 3, 4]); dO = dG - dH
x = np.arange(len(names))
a.bar(x - 0.27, dG, 0.27, color=GRID, edgecolor=MUTED, label="dim G")
a.bar(x, dH, 0.27, color=ORANGE, label="dim stabiliser G_p")
a.bar(x + 0.27, dO, 0.27, color=BLUE, label="dim orbit = dim G − dim G_p")
for xi in x:
    a.text(xi - 0.27, dG[xi] + 0.2, str(dG[xi]), ha="center", fontsize=8); a.text(xi, dH[xi] + 0.2, str(dH[xi]), ha="center", fontsize=8); a.text(xi + 0.27, dO[xi] + 0.2, str(dO[xi]), ha="center", fontsize=8)
a.set_xticks(x); a.set_xticklabels(names, fontsize=7.2); a.set_ylim(0, 10.5); a.legend(fontsize=7.8, loc="upper left")
a.set_title("A  orbit–stabiliser: the dimensions add up", fontsize=10)

# B: E(2) = R^2 x| SO(2): (t1, R1)(t2, R2) = (t1 + R1 t2, R1 R2) ------------------------------------------------------------------------------------------
b = axes[1]
def R(t):
    return np.array([[np.cos(t), -np.sin(t)], [np.sin(t), np.cos(t)]])
tri = np.array([[0, 0], [1, 0], [0.3, 0.7], [0, 0]]).T
th1, t1, th2, t2 = 0.8, np.array([1.2, 0.6]), -0.3, np.array([-0.4, 0.5])
b.plot(*tri, color=MUTED, lw=1.6, label="x")
g2 = R(th2) @ tri + t2[:, None]
b.plot(*g2, color=BLUE, lw=1.6, label="g₂ x")
g12 = R(th1) @ g2 + t1[:, None]
b.plot(*g12, color=ORANGE, lw=2.4, label="g₁ g₂ x")
prod_t = t1 + R(th1) @ t2
chk = R(th1 + th2) @ tri + prod_t[:, None]
b.plot(*chk, color=RED, lw=1.0, ls="--", label="(t₁ + R₁t₂, R₁R₂) x (identical)")
b.legend(fontsize=7.6, loc="upper left"); b.set_aspect("equal"); b.set_xlim(-1.3, 3.0); b.set_ylim(-0.8, 3.0)
b.text(-1.2, -0.7, "semidirect law (t₁,R₁)(t₂,R₂) = (t₁ + R₁t₂, R₁R₂);\nmatrix product agrees to 1×10⁻¹⁶", fontsize=7.8, color=INK)
b.set_title("B  E(2) = ℝ² ⋊ SO(2)", fontsize=10)

# C: Aff(1) = R x| R^x: composition of x -> a x + b ------------------------------------------------------------------------------------------------------------
c = axes[2]
xs = np.linspace(-1, 2, 100)
b1, a1, b2, a2 = 0.7, 1.9, -1.3, 0.4
c.plot(xs, a2 * xs + b2, color=BLUE, lw=1.8, label="f₂(x) = 0.4x − 1.3")
c.plot(xs, a1 * xs + b1, color=ORANGE, lw=1.8, label="f₁(x) = 1.9x + 0.7")
c.plot(xs, a1 * (a2 * xs + b2) + b1, color=RED, lw=2.4, label="f₁∘f₂ = (b₁ + a₁b₂, a₁a₂)")
c.plot(xs, xs, color=GRID, lw=1)
c.scatter([0.55], [a1 * (a2 * 0.55 + b2) + b1], color=INK, zorder=5, s=26)
c.text(-0.1, -2.9, "at x = 0.55:  (f₁∘f₂)(x) = −1.352\n= (0.76)(0.55) − 1.77", fontsize=8.0, color=INK, va="bottom")
c.legend(fontsize=7.8, loc="upper left"); c.set_xlim(-1, 2); c.set_ylim(-3, 3.2)
c.set_title("C  Aff(1) = ℝ ⋊ ℝ^×  (the ax + b group)", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: stabilisers are embedded Lie subgroups, orbits have dimension dim G − dim G_p (§1–§2). B, C: semidirect products checked numerically (§3). Numbers: dm_numbers.py (DM09).",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm09_actions")
