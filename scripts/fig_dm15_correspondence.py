"""DM15 - why exp(U) meets a closed subgroup in exp(U cap h) only for small U, the Lie correspondence, and a non-involutive distribution."""
from figlib import *
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

fig = plt.figure(figsize=(13.8, 4.7))

# A: G = T^2, H = closed circle {(2t, 3t)}: lifts of H to the Lie algebra R^2 are the strands 3x - 2y = k ---------------------------------------------------
a = fig.add_subplot(1, 3, 1)
xs = np.linspace(-1.3, 1.3, 10)
for k in range(-7, 8):
    ys = (3 * xs - k) / 2
    a.plot(xs, ys, color=BLUE if k == 0 else GRID, lw=2.4 if k == 0 else 1.0)
gx, gy = np.meshgrid(np.arange(-1, 2), np.arange(-1, 2))
a.scatter(gx.ravel(), gy.ravel(), color=INK, s=14, zorder=4)
th = np.linspace(0, 2 * np.pi, 200)
a.plot(0.12 * np.cos(th), 0.12 * np.sin(th), color=AQUA, lw=2.2)
a.plot(0.4 * np.cos(th), 0.4 * np.sin(th), color=RED, lw=1.6, ls="--")
a.text(0.14, -0.22, "small U", color=AQUA, fontsize=8.6)
a.text(0.43, 0.22, "large U", color=RED, fontsize=8.6)
a.text(-1.25, 1.12, "h = span(2,3) (blue); the other strands\n3x−2y = k are lifts of the same circle H;\nspacing 1/√13 = 0.277", fontsize=8.2, color=INK, va="top")
a.set_xlim(-1.3, 1.3); a.set_ylim(-1.3, 1.3); a.set_aspect("equal")
a.set_title("A  exp(U) ∩ H = exp(U ∩ h) needs U small", fontsize=9.8)

# B: the Lie correspondence ---------------------------------------------------------------------------------------------------------------------------------
b = fig.add_subplot(1, 3, 2)
b.set_xlim(0, 10); b.set_ylim(0, 10); b.axis("off")
def box(x, y, w, h, txt, col, fs=8.4):
    b.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.15", fc=col, ec=MUTED, alpha=0.25))
    b.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=fs, color=INK)
box(0.2, 7.6, 3.9, 1.7, "simply connected\nLie groups  G", BLUE)
box(5.9, 7.6, 3.9, 1.7, "finite-dim. real\nLie algebras  g", ORANGE)
b.add_patch(FancyArrowPatch((4.15, 8.8), (5.85, 8.8), arrowstyle="-|>", mutation_scale=14, color=INK, lw=1.4))
b.add_patch(FancyArrowPatch((5.85, 8.2), (4.15, 8.2), arrowstyle="-|>", mutation_scale=14, color=INK, lw=1.4))
b.text(5.0, 9.15, "Lie(G)", fontsize=8.4, ha="center"); b.text(5.0, 7.8, "Lie III", fontsize=8.4, ha="center")
b.text(0.2, 6.9, "injective: Homomorphism Thm (Lee 20.19, Cor 20.20)", fontsize=7.8, color=INK)
b.text(0.2, 6.4, "surjective: Ado + Lie subgroup of GL(n) + universal cover", fontsize=7.8, color=INK)
rows = [("ℝⁿ", "ℝⁿ, [ , ] = 0"), ("SU(2) = S³", "su(2) ≅ so(3) ≅ (ℝ³, ×)"), ("Aff(1)⁺ = {a > 0} ≅ ℝ²", "aff(1): [f₁,f₂] = f₂")]
for i, (g, l) in enumerate(rows):
    y = 4.8 - 1.2 * i
    box(0.2, y, 4.5, 0.9, g, BLUE, 8.2); box(5.2, y, 4.6, 0.9, l, ORANGE, 8.2)
    b.text(4.95, y + 0.45, "↔", ha="center", va="center", fontsize=11)
b.text(0.2, 1.05, "other connected groups with the same Lie algebra: G̃/Γ, Γ discrete central", fontsize=7.8)
b.text(0.2, 0.5, "Tⁿ = ℝⁿ/ℤⁿ,   SO(3) = SU(2)/{±1}", fontsize=8.6, color=RED)
b.set_title("B  the Lie correspondence", fontsize=9.8)

# C: a non-involutive distribution D = span{d_x, d_y + x d_z}: the commutator quadrilateral climbs in z ----------------------------------------------------
c = fig.add_subplot(1, 3, 3, projection="3d")
e = 0.5
P = np.array([[0, 0, 0], [e, 0, 0], [e, e, e * e], [0, e, e * e], [0, 0, e * e]])
c.plot(P[:4, 0], P[:4, 1], P[:4, 2], color=BLUE, lw=2.4)
c.plot(P[3:, 0], P[3:, 1], P[3:, 2], color=BLUE, lw=2.4)
c.scatter(P[:, 0], P[:, 1], P[:, 2], color=INK, s=22)
c.plot([0, 0], [0, 0], [0, e * e], color=RED, lw=3.0)
c.text(0.02, 0.0, e * e / 2, "gap = ε² ∂_z\n∉ D", color=RED, fontsize=8.6)
c.text(P[1, 0] + 0.02, P[1, 1], P[1, 2], "X₁", color=BLUE, fontsize=8.6)
c.text(P[2, 0], P[2, 1] + 0.02, P[2, 2], "X₂", color=BLUE, fontsize=8.6)
c.set_xlim(0, 0.6); c.set_ylim(0, 0.6); c.set_zlim(0, 0.3)
c.view_init(elev=22, azim=-55)
c.set_xlabel("x", fontsize=8); c.set_ylabel("y", fontsize=8); c.set_zlabel("z", fontsize=8)
c.set_title("C  D = span{∂ₓ, ∂ᵧ + x∂_z}: not involutive", fontsize=9.8)

fig.tight_layout()
fig.text(0.5, -0.02, "A: T² = ℝ²/ℤ² ⊃ H = {(2t,3t)}: the preimage of H in ℝ² is the union of the strands 3x − 2y = k (§1). B: §2. "
         "C: tracing integral curves of X₁, X₂, −X₁, −X₂ (ε = 0.5) ends at (0,0,ε²): [X₁,X₂] = ∂_z ∉ D, so no integral surface (§3). Numbers: dm_numbers.py (DM15).",
         ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_dm15_correspondence")
