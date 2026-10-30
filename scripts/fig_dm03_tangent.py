"""DM03 - two coordinate bases of one tangent plane, the change of basis by the Jacobian, and the velocity of a curve on S^2."""
from figlib import *
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

fig = plt.figure(figsize=(13.4, 4.5))

# A: S^1, tangent line at p with the basis vectors of two charts ---------------------------------------------------------------
a = fig.add_subplot(1, 3, 1)
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color=INK, lw=1.4)
ang = np.radians(55)
p = np.array([np.cos(ang), np.sin(ang)])
tang = np.array([-np.sin(ang), np.cos(ang)])
a.plot(*np.array([p - 1.2 * tang, p + 1.2 * tang]).T, color=MUTED, lw=1, ls="--")
# graph chart x: d/dx = (1, dy/dx) with y = sqrt(1-x^2): (1, -x/y)
dx = np.array([1.0, -p[0] / p[1]]); dx = dx / np.linalg.norm(dx) * 0.9
# stereographic chart w = x/(1-y): d/dw = d(x,y)/dw
def sinv(w):
    return np.array([2 * w, w * w - 1]) / (w * w + 1)
w0 = p[0] / (1 - p[1])
dw = (sinv(w0 + 1e-6) - sinv(w0 - 1e-6)) / 2e-6
a.annotate("", xy=p + dx, xytext=p, arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2))
a.annotate("", xy=p + 6 * dw, xytext=p, arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2))
a.scatter(*p, color=RED, s=40, zorder=5)
a.text(p[0] + 0.35, p[1] - 0.75, "∂/∂x|_p  (graph chart)", color=BLUE, fontsize=8.8)
a.text(-1.6, 1.55, "∂/∂w|_p (stereographic chart),\ndrawn 6× longer; it points the opposite way", color=ORANGE, fontsize=8.6)
lam = 2 * (1 - w0 ** 2) / (1 + w0 ** 2) ** 2                 # dx/dw with x(w) = 2w/(1+w^2)
a.text(-1.65, -1.55, f"∂/∂w|_p = (dx/dw) ∂/∂x|_p,  dx/dw = {lam:.3f} at w = {w0:.3f}:\nthe same tangent line, two bases related by the Jacobian", fontsize=8.2, color=INK)
a.set_aspect("equal"); a.set_xlim(-1.7, 2.2); a.set_ylim(-1.75, 2.1); a.axis("off")
a.set_title("A  one tangent line, two coordinate bases (S¹)", fontsize=10)

# B: HW2 Q3: X = (1,2) in the phi-plane and J X in the psi-plane ---------------------------------------------------------------------
b = fig.add_subplot(1, 3, 2)
u = np.array([np.sqrt(3) / 2, 0.5]); X = np.array([1.0, 2.0])
J = np.array([[-0.5, -np.sqrt(3) / 2], [-np.sqrt(3) / 2, 0.5]])
Xt = J @ X
tt = np.linspace(0, 2 * np.pi, 300)
b.plot(np.cos(tt), np.sin(tt), color=MUTED, lw=0.8, ls=":")
b.scatter(*u, color=RED, s=36, zorder=5)
b.annotate("", xy=u + 0.6 * X, xytext=u, arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2))
b.text(u[0] + 0.35, u[1] + 1.25, "X = (1, 2) in the φ-basis\nX f = 5 for f = u¹ + 2(u²)²", fontsize=8.6, color=BLUE)
b.annotate("", xy=u + 0.6 * Xt, xytext=u, arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2))
b.text(-1.55, 0.65, "same vector in the ψ-basis:\nJX = (−2.232, 0.134)", fontsize=8.6, color=ORANGE)
b.text(-1.55, -1.65, "p = (√3/2, ½, 0) lies on the unit circle of the chart plane, where the\ninversion w ↦ w/|w|² fixes the point and J = I − 2ûûᵀ is a reflection", fontsize=8.0, color=INK)
b.set_aspect("equal"); b.set_xlim(-1.7, 2.1); b.set_ylim(-1.9, 2.8)
b.set_title("B  change of basis by the Jacobian (HW2 Q3)", fontsize=10)

# C: velocity of a curve on S^2 -----------------------------------------------------------------------------------------------------------
c = fig.add_subplot(1, 3, 3, projection="3d")
uu, vv = np.meshgrid(np.linspace(0, 2 * np.pi, 40), np.linspace(0, np.pi, 20))
c.plot_wireframe(np.cos(uu) * np.sin(vv), np.sin(uu) * np.sin(vv), np.cos(vv), color=GRID, lw=0.4)
t = np.linspace(-0.44, 0.44, 200)
al = np.stack([t, 2 * t, np.sqrt(1 - 5 * t * t)])
c.plot(*al, color=BLUE, lw=2.4)
t0 = 0.25
p3 = np.array([t0, 2 * t0, np.sqrt(1 - 5 * t0 ** 2)])
v3 = np.array([1, 2, -5 * t0 / np.sqrt(1 - 5 * t0 ** 2)])
c.scatter(*p3, color=RED, s=36)
c.quiver(*p3, *(0.45 * v3), color=ORANGE, lw=2.2, arrow_length_ratio=0.25)
c.text2D(0.02, 0.02, "α(t) = (t, 2t, √(1−5t²)),  α′(¼) = (1, 2, −5/√11)\nin φ₃⁺: (1, 2);  in φ₂⁺: (1, −5/√11) = (1, −1.5076)", transform=c.transAxes, fontsize=8.0)
c.view_init(elev=22, azim=35); c.set_xticks([]); c.set_yticks([]); c.set_zticks([])
c.set_title("C  velocity of a curve (HW3 Q1)", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.02, "A: tangent line to S¹ with the basis vectors of two charts. B: the Jacobian of the transition map converts components (numbers verified by pushing curves, dm_numbers.py DM03). "
         "C: the velocity of a curve on S² is a vector in R³ tangent to the sphere.", ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm03_tangent")
