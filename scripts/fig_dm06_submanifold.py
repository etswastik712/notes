"""DM06 - a slice chart straightens the circle, regular and critical levels of x^2 - y^2, and the tangent plane of S^2 as ker dF."""
from figlib import *
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

fig = plt.figure(figsize=(13.4, 4.5))

# A: slice chart phi(x,y) = (x, y - sqrt(1-x^2)) near (0,1) ---------------------------------------------------------------------------------
a = fig.add_subplot(1, 3, 1)
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color=INK, lw=1.4, label="S¹ ⊂ R²")
xx, yy = np.meshgrid(np.linspace(-0.9, 0.9, 13), np.linspace(0.3, 1.5, 13))
a.scatter(xx, yy, color=GRID, s=6)
for c in (-0.15, 0.0, 0.15):
    x = np.linspace(-0.85, 0.85, 200)
    a.plot(x, c + np.sqrt(1 - x ** 2), color=BLUE if c == 0 else AQUA, lw=2.2 if c == 0 else 1.0, alpha=1 if c == 0 else 0.7)
a.text(-0.35, 1.52, "level lines  y − √(1−x²) = c", fontsize=8.4, color=AQUA)
a.text(-1.55, -1.5, "slice chart φ(x, y) = (x, y − √(1−x²)) near (0, 1):\nS¹ ∩ U = {second coordinate = 0}  (|·| ≤ 2×10⁻¹⁶ on the arc)", fontsize=8.2, color=INK)
a.set_aspect("equal"); a.set_xlim(-1.6, 1.6); a.set_ylim(-1.7, 1.8); a.axis("off")
a.set_title("A  a slice chart straightens the circle", fontsize=10)

# B: level sets of F = x^2 - y^2 ------------------------------------------------------------------------------------------------------------------
b = fig.add_subplot(1, 3, 2)
X, Y = np.meshgrid(np.linspace(-2.2, 2.2, 500), np.linspace(-2.2, 2.2, 500))
Fv = X ** 2 - Y ** 2
b.contour(X, Y, Fv, levels=[-1, -0.25, 0.25, 1], colors=[BLUE], linewidths=1.6)
b.contour(X, Y, Fv, levels=[0], colors=[RED], linewidths=2.2)
b.scatter([0], [0], color=RED, s=44, zorder=5)
b.text(0.08, 0.12, "critical point,\nlevel 0 = cross", color=RED, fontsize=8.6)
b.text(-2.15, -2.45, "regular values c ≠ 0: hyperbolas, smallest |∇F| = 2 (c=1), 1 (c=¼)\ncritical value c = 0: |∇F| = 0 at the origin, the level set is a cross", fontsize=8.0, color=INK)
b.set_aspect("equal"); b.set_xlim(-2.3, 2.3); b.set_ylim(-2.6, 2.3)
b.set_title("B  regular levels are submanifolds; the critical one is not", fontsize=9.8)

# C: tangent plane of S^2 = kernel of dF_p, F = |x|^2 ------------------------------------------------------------------------------------------------
c = fig.add_subplot(1, 3, 3, projection="3d")
uu, vv = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 20))
c.plot_wireframe(np.cos(uu) * np.sin(vv), np.sin(uu) * np.sin(vv), np.cos(vv), color=GRID, lw=0.4)
p = np.array([0.25, 0.5, np.sqrt(11) / 4])
n = p / np.linalg.norm(p)
e1 = np.cross(n, [0, 0, 1]); e1 /= np.linalg.norm(e1); e2 = np.cross(n, e1)
g1, g2 = np.meshgrid(np.linspace(-0.7, 0.7, 6), np.linspace(-0.7, 0.7, 6))
c.plot_surface(p[0] + g1 * e1[0] + g2 * e2[0], p[1] + g1 * e1[1] + g2 * e2[1], p[2] + g1 * e1[2] + g2 * e2[2], color=ORANGE, alpha=0.25)
c.quiver(*p, *(0.7 * n), color=RED, lw=2.0, arrow_length_ratio=0.2)
v = np.array([1, 2, -5 / np.sqrt(11)]); v = v / np.linalg.norm(v)
c.quiver(*p, *(0.7 * v), color=BLUE, lw=2.2, arrow_length_ratio=0.2)
c.scatter(*p, color=INK, s=24)
c.text2D(0.02, 0.0, "red: ∇F = 2p (normal), orange: T_pS² = ker dF_p,\nblue: α′(¼) = (1, 2, −5/√11) ⊥ p  (dF_p α′ = 0)", transform=c.transAxes, fontsize=8.0)
c.view_init(elev=24, azim=-40); c.set_xticks([]); c.set_yticks([]); c.set_zticks([])
c.set_title("C  T_pS² = ker dF_p", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: slice chart; B: regular value theorem (HW4 Q1); C: tangent space of a regular level set. Numbers: dm_numbers.py (DM06).", ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm06_submanifold")
