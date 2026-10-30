"""DM08 - a left-invariant field on S^1, the two components of O(2), and ranks of Lie group homomorphisms."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.3), gridspec_kw=dict(width_ratios=[1.0, 1.05, 1.0]))

# A: S^1 = U(1): left translation L_g is a rotation; it carries the unit tangent at e to the unit tangent at g -----------------------------------------
a = axes[0]
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color=INK, lw=1.4)
for k, ang in enumerate(np.linspace(0, 2 * np.pi, 9)[:-1]):
    p = np.array([np.cos(ang), np.sin(ang)]); v = np.array([-np.sin(ang), np.cos(ang)]) * 0.45
    a.annotate("", xy=p + v, xytext=p, arrowprops=dict(arrowstyle="-|>", color=BLUE if k else RED, lw=2.0))
a.scatter([1], [0], color=RED, s=40, zorder=5)
a.text(1.08, -0.18, "e = 1", color=RED, fontsize=9)
a.text(-1.7, -1.65, "L_g(h) = gh is a diffeomorphism (rotation by arg g);\nd(L_g)_e carries the vector at e to the one at g:\nthe left-invariant field, a global frame (S¹ is parallelizable)", fontsize=8.2, color=INK)
a.set_aspect("equal"); a.set_xlim(-1.8, 1.9); a.set_ylim(-1.9, 1.7); a.axis("off")
a.set_title("A  S¹: translations and a left-invariant field", fontsize=10)

# B: O(2) = two circles ----------------------------------------------------------------------------------------------------------------------------------------
b = axes[1]
for cx, col, lab in ((-1.5, BLUE, "SO(2): det = +1\n[cos θ  −sin θ; sin θ  cos θ]\n(identity component)"), (1.5, ORANGE, "det = −1 (reflections)\n[cos θ   sin θ; sin θ  −cos θ]")):
    b.plot(cx + np.cos(th), np.sin(th), color=col, lw=2.6)
    b.text(cx - 1.0, -1.75, lab, fontsize=8.2, color=col)
b.scatter([-0.5], [0], color=RED, s=40, zorder=5); b.text(-0.55, 0.15, "I", color=RED, fontsize=9)
b.text(-2.5, 1.55, "O(2) is a 1-dimensional embedded submanifold of GL(2,R)\nwith two components, n(n−1)/2 = 1", fontsize=8.4, color=INK)
b.set_aspect("equal"); b.set_xlim(-3, 3); b.set_ylim(-2.4, 2.0); b.axis("off")
b.set_title("B  components: O(2) = SO(2) ⊔ (reflections)", fontsize=10)

# C: constant rank of homomorphisms ----------------------------------------------------------------------------------------------------------------------------
c = axes[2]
names = ["det:\nGL(3)→R×", "R→T²\n(dense)", "SU(2)→\nSO(3)", "exp:\nR→R×"]
dimG = np.array([9, 1, 3, 1]); rk = np.array([1, 1, 3, 1]); ker = dimG - rk
x = np.arange(4)
c.bar(x - 0.27, dimG, 0.27, color=GRID, edgecolor=MUTED, label="dim G")
c.bar(x, rk, 0.27, color=BLUE, label="rank dF (same at every point)")
c.bar(x + 0.27, ker, 0.27, color=ORANGE, label="dim ker F = dim G − rank")
for xi, (d_, r_, k_) in enumerate(zip(dimG, rk, ker)):
    c.text(xi - 0.27, d_ + 0.15, str(d_), ha="center", fontsize=8.4); c.text(xi, r_ + 0.15, str(r_), ha="center", fontsize=8.4); c.text(xi + 0.27, k_ + 0.15, str(k_), ha="center", fontsize=8.4)
c.set_xticks(x); c.set_xticklabels(names, fontsize=8.4); c.set_ylim(0, 11.5); c.legend(fontsize=7.6, loc="upper right")
c.set_title("C  homomorphisms have constant rank", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: translations and invariant fields (§1). B: components (§3). C: ranks computed numerically at 20–40 random points each (dm_numbers.py, DM08): F∘L_g = L_{F(g)}∘F forces constant rank (§2).",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm08_liegroup")
