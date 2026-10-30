"""PA13 - contraction iteration, the inverse function theorem for z -> z^2, and the implicit function theorem on the circle."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.3))

# A: cobweb for cos x = x -----------------------------------------------------------------------------------------------
a = axes[0]
xs = np.linspace(0, 1.05, 200)
a.plot(xs, np.cos(xs), color=BLUE, lw=2, label="y = cos x")
a.plot(xs, xs, color=MUTED, lw=1.2, label="y = x")
x = 1.0
for _ in range(9):
    y = np.cos(x)
    a.plot([x, x], [x, y], color=ORANGE, lw=1.1)
    a.plot([x, y], [y, y], color=ORANGE, lw=1.1)
    x = y
xstar = 0.7390851332151607
a.scatter([xstar], [xstar], color=RED, zorder=4, s=40)
a.annotate("fixed point\n0.739085…", (xstar, xstar), xytext=(0.18, 0.88), fontsize=8.8, color=RED, arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
a.text(0.02, 0.1, "contraction, L = sin 1 = 0.841:\n67 steps to 10⁻¹²\n(a-priori bound 166)", fontsize=8.6, color=INK)
a.set_xlim(0, 1.05); a.set_ylim(0, 1.05); a.set_aspect("equal"); a.legend(loc="lower right", fontsize=8.4)
a.set_title("A  Banach iteration", fontsize=10)

# B: z -> z^2 near (1, 0) ------------------------------------------------------------------------------------------------------
b = axes[1]
F = lambda x_, y_: (x_ ** 2 - y_ ** 2, 2 * x_ * y_)
us = np.linspace(0.6, 1.4, 9)
vs = np.linspace(-0.5, 0.5, 11)
tt = np.linspace(0, 1, 100)
for u in us:
    X, Y = F(np.full_like(tt, u), vs[0] + (vs[-1] - vs[0]) * tt)
    b.plot(X, Y, color=BLUE, lw=1.1, alpha=0.9)
for v in vs:
    X, Y = F(us[0] + (us[-1] - us[0]) * tt, np.full_like(tt, v))
    b.plot(X, Y, color=ORANGE, lw=1.1, alpha=0.9)
z = np.sqrt(complex(1.1, 0.2))
b.scatter([1.1], [0.2], color=RED, s=44, zorder=5)
b.annotate("F(p) = (1.1, 0.2)", (1.1, 0.2), xytext=(1.45, 0.62), fontsize=8.6, color=RED, arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
b.scatter([1.0], [0.0], color=INK, s=24, zorder=5)
b.text(1.03, -0.12, "F(a)", fontsize=8.6)
b.text(-0.15, -1.38, "image of a grid around a = (1, 0) under F(x,y) = (x²−y², 2xy);\nDF(a) = 2·I is invertible, so F is a diffeomorphism near a\np = (1.05310, 0.09496), found by 8 contraction steps (error 10⁻⁹)", fontsize=8.2, color=INK, va="top")
b.set_aspect("equal"); b.set_xlim(-0.2, 2.2); b.set_ylim(-2.1, 1.3)
b.set_title("B  inverse function theorem", fontsize=10)

# C: implicit function theorem on the circle ------------------------------------------------------------------------------------
c = axes[2]
t = np.linspace(0, 2 * np.pi, 400)
c.plot(np.cos(t), np.sin(t), color=MUTED, lw=1.4)
xs = np.linspace(-0.8, 0.8, 100)
c.plot(xs, np.sqrt(1 - xs ** 2), color=BLUE, lw=3.2)
c.scatter([0], [1], color=BLUE, s=40, zorder=4)
c.text(-0.5, 1.12, "y = g(x) = √(1−x²) near (0,1)", fontsize=8.6, color=BLUE)
c.scatter([1], [0], color=RED, s=44, zorder=4)
c.plot([1, 1], [-0.45, 0.45], color=RED, lw=1.6, ls="--")
c.text(-1.35, -1.2, "∂F/∂y = 2y = 0 at (1, 0): vertical tangent,\nso the circle is not a graph y = g(x) there", fontsize=8.4, color=RED, va="top")
c.set_aspect("equal"); c.set_xlim(-1.4, 1.5); c.set_ylim(-1.95, 1.45)
c.set_title("C  implicit function theorem", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: iterates of x ↦ cos x. B: coordinate grid and its image. C: F(x, y) = x² + y² − 1; the theorem gives a graph exactly where ∂F/∂y ≠ 0. Numbers: pa13_numbers.py.",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_pa13_ift")
