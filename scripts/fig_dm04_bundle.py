"""DM04 - TS^1 as a cylinder, the vector field with one zero on S^2 (HW3 Q3), and the rank theorem for a rank-1 map."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.4), gridspec_kw=dict(width_ratios=[1.0, 1.05, 1.1]))

# A: TS^1 = S^1 x R with the two bundle charts ----------------------------------------------------------------------------------
a = axes[0]
th = np.linspace(0, 2 * np.pi, 300)
for v in (-1, -0.5, 0, 0.5, 1):
    a.plot(th, np.full_like(th, v), color=GRID if v else INK, lw=1.3 if v == 0 else 0.9)
for ang in np.linspace(0.3, 6.0, 9):
    a.plot([ang, ang], [-1.1, 1.1], color=BLUE, lw=0.8, alpha=0.6)
a.annotate("", xy=(1.0, 0.9), xytext=(1.0, 0.0), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2))
a.text(1.08, 0.45, "a tangent vector v at p\nlies in the fibre T_pS¹ ≅ R", fontsize=8.6, color=ORANGE)
a.text(0.1, -1.55, "chart on TS¹:  (p, v) ↦ (w(p), v)  where v = v ∂/∂w\ntransition: (w, v) ↦ (1/w, −v/w²)   [check: (1.70, 0.90) ↦ (0.5882, −0.3114)]", fontsize=8.0, color=INK)
a.set_xlim(0, 2 * np.pi); a.set_ylim(-1.8, 1.4); a.set_xlabel("position on S¹ (angle)"); a.set_yticks([])
a.set_title("A  TS¹ = S¹ × R (trivial bundle)", fontsize=10)

# B: the vector field (u2^2 - u1^2, -2 u1 u2) in the psi-plane ---------------------------------------------------------------------------
b = axes[1]
x = np.linspace(-2.2, 2.2, 28)
X, Y = np.meshgrid(x, x)
U = Y ** 2 - X ** 2
V = -2 * X * Y
mag = np.sqrt(U ** 2 + V ** 2)
b.streamplot(X, Y, U, V, color=BLUE, density=1.5, linewidth=0.9, arrowsize=0.9)
b.scatter([0], [0], color=RED, s=48, zorder=5)
b.text(0.12, 0.14, "N", color=RED, fontsize=10)
b.text(-2.15, -2.3, "Y = (φ⁻¹)_*(∂/∂u¹) in the ψ-chart: (u₂² − u₁², −2u₁u₂),  |Y| = |u|²\nvanishes at exactly one point, the north pole", fontsize=8.2, color=INK)
b.set_aspect("equal"); b.set_xlim(-2.3, 2.3); b.set_ylim(-2.4, 2.3)
b.set_title("B  a vector field on S² with one zero (HW3 Q3)", fontsize=10)

# C: the rank theorem: F(u,v) = (u+v, (u+v)^2) ------------------------------------------------------------------------------------------------
c = axes[2]
cs = np.linspace(-1.5, 1.5, 11)
cmap = plt.get_cmap("viridis")
uu = np.linspace(-1.8, 1.8, 50)
for k, cc in enumerate(cs):
    col = cmap(k / (len(cs) - 1))
    c.plot(uu, cc - uu, color=col, lw=1.4)                                       # fibre u + v = cc  in the domain (u horizontal, v vertical)
ins = c.inset_axes([0.58, 0.05, 0.4, 0.42])
s_ = np.linspace(-1.6, 1.6, 200)
ins.plot(s_, s_ ** 2, color=MUTED, lw=1)
for k, cc in enumerate(cs):
    ins.scatter([cc], [cc ** 2], color=cmap(k / (len(cs) - 1)), s=18, zorder=5)
ins.set_title("image: the parabola b = a²", fontsize=7.8); ins.tick_params(labelsize=6.5)
c.text(-1.75, 2.3, "F(u,v) = (u+v, (u+v)²) has rank 1 everywhere.", fontsize=8.6, color=INK)
c.text(-1.75, 1.95, "It collapses each line u+v = c to one point c, c².", fontsize=8.6, color=INK)
c.text(-1.75, -2.35, "In the charts φ(u,v) = (u+v, v), ψ(a,b) = (a, b−a²):\nψ∘F∘φ⁻¹(s,t) = (s, 0)  (error 9×10⁻¹⁶ numerically)", fontsize=8.2, color=INK)
c.set_xlim(-1.9, 1.9); c.set_ylim(-2.5, 2.6); c.set_aspect("equal"); c.set_xlabel("u"); c.set_ylabel("v")
c.set_title("C  constant rank: fibres are 1-dimensional", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: the tangent bundle of the circle is a cylinder (Chart Lemma, §1). B: the HW3 Q3 field in the south-pole chart (§1). C: a constant-rank-1 map and its normal form (§3). Numbers: dm_numbers.py (DM04).",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm04_bundle")
