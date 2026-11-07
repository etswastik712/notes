"""PR08 - order statistics of two variables (two preimages), exponential order statistics (Y1, Y2 - Y1 independent), the multinomial covariance."""
from figlib import *
import itertools, math
from matplotlib.patches import Ellipse, Rectangle

fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.7))

# A: the map (x1,x2) -> (min, max): the point (y1,y2) with y1<y2 has two preimages ----------------------------------------------------------------------
a = ax[0]
g = np.linspace(0, 3, 300)
X1, X2 = np.meshgrid(g, g)
dens = np.exp(-X1) * np.exp(-X2)
a.contourf(X1, X2, dens, levels=12, cmap="Blues", alpha=0.55)
a.plot([0, 3], [0, 3], color=INK, lw=1.6)
y1, y2 = 0.7, 1.9
for (u, v, col) in ((y1, y2, BLUE), (y2, y1, ORANGE)):
    a.add_patch(Rectangle((u - 0.07, v - 0.07), 0.14, 0.14, fc=col, ec=INK, lw=1.2))
a.annotate("(y₁, y₂): x₁ = min, x₂ = max", xy=(y1, y2), xytext=(0.05, 2.55), fontsize=8.2, color=BLUE, arrowprops=dict(arrowstyle="->", color=BLUE))
a.annotate("(y₂, y₁): x₁ = max, x₂ = min", xy=(y2, y1), xytext=(1.55, 0.35), fontsize=8.2, color=ORANGE, arrowprops=dict(arrowstyle="->", color=ORANGE))
a.text(0.35, 0.12, "y₁ < y₂ region of the (y₁,y₂)-plane\nis hit twice ⇒ factor 2", fontsize=8.2, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.85))
a.set_xlim(0, 3); a.set_ylim(0, 3); a.set_aspect("equal"); a.set_xlabel("x₁"); a.set_ylabel("x₂")
a.set_title("A  two preimages ⇒  f(y₁,y₂) = 2 f(y₁) f(y₂)", fontsize=9.8)

# B: Expo(lambda = 2): (Y1, G = Y2 - Y1) are independent; contours of the product density ----------------------------------------------------------
b = ax[1]
rng = np.random.default_rng(4)
lam = 2.0
S = rng.exponential(1 / lam, size=(2500, 2))
Y1, Y2 = S.min(1), S.max(1)
Gp = Y2 - Y1
b.scatter(Y1, Gp, s=4, color=BLUE, alpha=0.35)
yy, gg = np.meshgrid(np.linspace(0, 1.6, 200), np.linspace(0, 2.4, 200))
dd = (2 * lam * np.exp(-2 * lam * yy)) * (lam * np.exp(-lam * gg))
b.contour(yy, gg, dd, levels=[0.1, 0.4, 1.0, 2.0, 4.0], colors=ORANGE, linewidths=1.3)
b.set_xlim(0, 1.6); b.set_ylim(0, 2.4)
b.set_xlabel("Y₁ = min  ~ Expo(2λ)"); b.set_ylabel("Y₂ − Y₁  ~ Expo(λ)")
b.text(0.62, 1.9, "orange: the product density\n(2λe^{−2λy₁})(λe^{−λg}), λ = 2\nsample correlation %.3f" % np.corrcoef(Y1, Gp)[0, 1], fontsize=8, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.85))
b.set_title("B  Y₁ and Y₂ − Y₁ are independent", fontsize=9.8)

# C: the multinomial n = 10, p = (0.2, 0.3, 0.5): joint pmf of (X1, X2) and the covariance ellipse ----------------------------------------------------
c = ax[2]
n = 10
p = np.array([0.2, 0.3, 0.5])
pts = [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]
pm = [math.factorial(n) / (math.factorial(i) * math.factorial(j) * math.factorial(n - i - j)) * p[0] ** i * p[1] ** j * p[2] ** (n - i - j) for (i, j) in pts]
c.scatter([q[0] for q in pts], [q[1] for q in pts], s=[900 * m for m in pm], color=BLUE, alpha=0.55, ec=INK, lw=0.4)
cov = n * (np.diag(p[:2]) - np.outer(p[:2], p[:2]))
w, V = np.linalg.eigh(cov)
ang = np.degrees(np.arctan2(V[1, 1], V[0, 1]))
c.add_patch(Ellipse((n * p[0], n * p[1]), 2 * 2 * np.sqrt(w[1]), 2 * 2 * np.sqrt(w[0]), angle=ang, fc="none", ec=ORANGE, lw=2))
c.plot([0, n], [n, 0], color=MUTED, lw=1.2, ls="--")
c.text(5.4, 5.2, "X₁ + X₂ ≤ n", fontsize=8, color=MUTED, rotation=-45)
c.set_xlim(-0.5, 8); c.set_ylim(-0.5, 9); c.set_xlabel("X₁ (outcome 1)"); c.set_ylabel("X₂ (outcome 2)")
c.text(3.9, 0.3, "bubble area ∝ pmf; ellipse = 2σ of\nn(diag p − ppᵀ) = [[1.6, −0.6],[−0.6, 2.1]]\nCorr(X₁,X₂) = −0.327", fontsize=7.8, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.85))
c.set_title("C  Mult₃(10, p): negative covariance", fontsize=9.8)

fig.tight_layout()
fig.text(0.5, -0.03, "A: the joint density of (min, max) is 2f(y₁)f(y₂) on y₁ < y₂ (§1; instructor's route by the joint cdf 2F(y₁)F(y₂) − F(y₁)², then ∂²/∂y₁∂y₂).  "
         "B: for exponentials the min and the gap are independent with rates 2λ and λ (§3; 2500 samples).  "
         "C: the multinomial counts are negatively correlated because they must add up to n (§4).  Numbers: pr08_numbers.py.",
         ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_pr08_order_multinomial")
