"""PR09 - the disc marginal and conditional (Week 4), the rotation to independent normals (HW6 Q1), products of uniforms (HW6 Q2), the tangent line and Jensen (HW6 Q3)."""
from figlib import *
import math
from matplotlib.patches import Ellipse

rng = np.random.default_rng(9)
fig, ax = plt.subplots(2, 2, figsize=(11.6, 9.2))

# A: uniform on a disc: the semicircle marginal and the conditional slice -----------------------------------------------------------------------------
a = ax[0, 0]
R = 2.0
n = 6000
ang = rng.uniform(0, 2 * math.pi, n); rad = R * np.sqrt(rng.uniform(0, 1, n))
X, Y = rad * np.cos(ang), rad * np.sin(ang)
a.scatter(X, Y, s=3, color=BLUE, alpha=0.35)
t = np.linspace(0, 2 * math.pi, 300)
a.plot(R * np.cos(t), R * np.sin(t), color=INK, lw=1)
x0 = 1.0
h = math.sqrt(R * R - x0 * x0)
a.plot([x0, x0], [-h, h], color=ORANGE, lw=3)
a.annotate("slice x₁ = 1: X₂ | X₁ uniform on ±√(R²−1) = ±1.732\ndensity 1/(2√(R²−x₁²)) = 0.2887", xy=(x0, h * 0.55), xytext=(-2.0, 2.3), fontsize=8, color=ORANGE, arrowprops=dict(arrowstyle="->", color=ORANGE))
xs = np.linspace(-R, R, 200)
a.fill_between(xs, -3.4, -3.4 + 0.9 * np.sqrt(1 - (xs / R) ** 2), color=AQUA, alpha=0.5)
a.plot(xs, -3.4 + 0.9 * np.sqrt(1 - (xs / R) ** 2), color=AQUA, lw=1.5)
a.text(-1.9, -3.32, "marginal f(x₁) = (2/πR)√(1−(x₁/R)²)", fontsize=7.8, color=INK)
a.set_xlim(-2.6, 2.6); a.set_ylim(-3.5, 2.7); a.set_aspect("equal"); a.set_xlabel("x₁"); a.set_ylabel("x₂")
a.set_title("A  uniform on a disc: semicircle marginal, uniform conditional", fontsize=9.6)

# B: rotation to independent normals ----------------------------------------------------------------------------------------------------------------
b = ax[0, 1]
Sig = np.array([[2.0, 1.0], [1.0, 2.0]]); mu = np.array([1.0, -1.0])
S = rng.multivariate_normal(mu, Sig, 2500)
b.scatter(S[:, 0], S[:, 1], s=4, color=BLUE, alpha=0.35)
for k, col in ((1, ORANGE), (2, ORANGE)):
    b.add_patch(Ellipse(mu, 2 * k * math.sqrt(3), 2 * k * 1.0, angle=45, fill=False, ec=col, lw=1.4))
v1, v2 = np.array([1, 1]) / math.sqrt(2), np.array([1, -1]) / math.sqrt(2)
b.annotate("", xy=mu + 2.2 * math.sqrt(3) * v1, xytext=mu, arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
b.annotate("", xy=mu + 2.2 * 1.0 * v2, xytext=mu, arrowprops=dict(arrowstyle="->", color=INK, lw=1.8))
b.text(mu[0] + 2.35, mu[1] + 2.45, "e₁ = (1,1)/√2\nVar Y₁ = 3", fontsize=8, color=INK)
b.text(mu[0] + 1.5, mu[1] - 2.0, "e₂ = (1,−1)/√2\nVar Y₂ = 1", fontsize=8, color=INK)
b.set_xlim(-5, 6.5); b.set_ylim(-6, 5.5); b.set_aspect("equal"); b.set_xlabel("x₁"); b.set_ylabel("x₂")
b.text(-4.8, 4.0, "Σ = [[2,1],[1,2]], μ = (1,−1)\nY = OX with rows of O = e₁, e₂:\nY₁, Y₂ independent N(0,3), N(√2,1)\nellipses: 1σ and 2σ contours of f_X", fontsize=7.8, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.9))
b.set_title("B  O Σ Oᵀ = diag(3, 1): rotate to the axes of the ellipse", fontsize=9.6)

# C: product of n uniforms ---------------------------------------------------------------------------------------------------------------------------
c = ax[1, 0]
u = np.linspace(0.002, 1, 800)
cols = [BLUE, AQUA, VIOLET, ORANGE, RED]
for n_, col in zip(range(1, 6), cols):
    c.plot(u, (-np.log(u)) ** (n_ - 1) / math.factorial(n_ - 1), color=col, lw=2 if n_ in (2, 5) else 1.3, label="n = %d" % n_)
U5 = rng.uniform(size=(300000, 5)).prod(1)
hh, ee = np.histogram(U5, bins=np.linspace(0, 1, 201), density=True)
c.step(ee[:-1], hh, where="post", color=RED, lw=0.8, alpha=0.8)
c.set_ylim(0, 10); c.set_xlim(0, 0.6)
c.set_xlabel("u"); c.set_ylabel("density of U₁⋯Uₙ")
c.legend(frameon=False, fontsize=8, loc="upper right")
c.text(0.22, 5.3, "f(u) = (−ln u)ⁿ⁻¹/(n−1)!\nn = 5: E[U] = 2⁻⁵ = 0.03125,\nVar U = 3⁻⁵ − 4⁻⁵ = 0.00314\n(thin red steps: 3·10⁵ simulated n = 5)", fontsize=8, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.9))
c.set_title("C  −ln(U₁⋯Uₙ) ~ Gamma(n,1)  ⇒  density of the product", fontsize=9.6)

# D: tangent line lies below a convex function; Jensen ------------------------------------------------------------------------------------------------
d = ax[1, 1]
x = np.linspace(-1.2, 2.3, 400)
d.plot(x, np.exp(x), color=BLUE, lw=2.2, label="g(x) = eˣ  (g″ > 0)")
for a0, col in ((0.0, ORANGE), (1.0, AQUA)):
    d.plot(x, math.exp(a0) * (1 + x - a0), color=col, lw=1.3, label="tangent at a = %g" % a0)
    d.plot([a0], [math.exp(a0)], "o", color=col, ms=5)
# two-point distribution: X in {0, 1.6}, equal probability
pts = np.array([0.0, 1.6]); gp = np.exp(pts)
d.plot(pts, gp, "o", color=INK, ms=5)
d.plot(pts, gp, color=INK, lw=0.9, ls=":")
m = pts.mean()
d.plot([m], [gp.mean()], "s", color=RED, ms=7)
d.plot([m], [math.exp(m)], "s", color=VIOLET, ms=7)
d.annotate("E g(X) = %.3f" % gp.mean(), xy=(m, gp.mean()), xytext=(1.25, 1.35), fontsize=8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
d.annotate("g(E X) = %.3f" % math.exp(m), xy=(m, math.exp(m)), xytext=(-1.1, 3.9), fontsize=8, color=VIOLET, arrowprops=dict(arrowstyle="->", color=VIOLET))
d.set_xlim(-1.2, 2.3); d.set_ylim(-0.3, 7)
d.legend(frameon=False, fontsize=8, loc="upper left")
d.set_xlabel("x")
d.text(0.95, 0.0, "X ∈ {0, 1.6}, probability ½ each", fontsize=8, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.9))
d.set_title("D  tangent below the graph ⇒ Jensen", fontsize=9.6)

fig.tight_layout()
save(fig, "fig_pr09_change_of_variables")
