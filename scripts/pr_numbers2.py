"""PR07 + PR05 quiz - numbers quoted in the HW4 chapter and the MT2213 quiz of 16 Sep, recomputed.

    .venv/bin/python -W ignore scripts/pr_numbers2.py
"""
import numpy as np
from scipy import stats, integrate, special

rng = np.random.default_rng(2113)
P = print


def sec(t): P("\n=====", t)


sec("Quiz 1 (16/09/2026)")
P("Q1 E[X] for f=x e^-x:", integrate.quad(lambda x: x * x * np.exp(-x), 0, np.inf)[0], "(Gamma(2,1): mean 2); normalisation", integrate.quad(lambda x: x * np.exp(-x), 0, np.inf)[0])
P("Q2 P(4<X<16), N(10,36):", stats.norm.cdf(1) - stats.norm.cdf(-1), "= 2Phi(1)-1 =", 2 * stats.norm.cdf(1) - 1)
for b in (0.5, 1.0, 2.0):
    a = 4 * b ** 1.5 / np.sqrt(np.pi)
    P(f"Q3 b={b}: a=4b^(3/2)/sqrt(pi)={a:.6f}; integral of a x^2 e^(-b x^2) over [0,inf) =", integrate.quad(lambda x: a * x * x * np.exp(-b * x * x), 0, np.inf)[0])
P("   E[V] = a/(2 b^2) at b=1 =", 4 * 1 / np.sqrt(np.pi) / 2, "vs numeric", integrate.quad(lambda x: 4 / np.sqrt(np.pi) * x ** 3 * np.exp(-x * x), 0, np.inf)[0], "(b=1; formula 2/sqrt(pi) b^(-1/2))", 2 / np.sqrt(np.pi))

sec("HW4 Q1 convolution of two normals")
m1, s1, m2, s2 = 1.0, 2.0, -0.5, 1.5
for z in (-2.0, 0.3, 1.7, 4.0):
    conv = integrate.quad(lambda x: stats.norm.pdf(x, m1, s1) * stats.norm.pdf(z - x, m2, s2), -np.inf, np.inf)[0]
    P(f"  z={z}: convolution {conv:.8f}  N(mu1+mu2, s1^2+s2^2) density {stats.norm.pdf(z, m1 + m2, np.hypot(s1, s2)):.8f}")

sec("HW4 Q2 reflection and E|X-Y|")
P("  -Y ~ N(-mu,s^2): mean and sd of -Y for Y~N(2,9) by Monte Carlo:", (-rng.normal(2, 3, 10**6)).mean(), (-rng.normal(2, 3, 10**6)).std())
x, y = rng.standard_normal(10**7), rng.standard_normal(10**7)
P("  E|X-Y| Monte Carlo", np.abs(x - y).mean(), "  2/sqrt(pi) =", 2 / np.sqrt(np.pi), "  sqrt(2)*sqrt(2/pi) =", np.sqrt(2) * np.sqrt(2 / np.pi))
P("  half-normal mean sqrt(2/pi) =", np.sqrt(2 / np.pi), " E|N(0,s^2)| = s*sqrt(2/pi); s=sqrt2 ->", np.sqrt(2) * np.sqrt(2 / np.pi))
P("  Var|X-Y| = 2 - 4/pi =", 2 - 4 / np.pi, "MC", np.abs(x - y).var())

sec("HW4 Q3 covariance matrix and correlation")
n = 4
c = np.array([2.0, -1.0, 0.5, 3.0])
cov = np.cov(rng.multivariate_normal(np.zeros(n), np.array([[2, .5, 0, .3], [.5, 1, .2, 0], [0, .2, 3, -.4], [.3, 0, -.4, 1.5]]), 10**6).T)
S = np.array([[2, .5, 0, .3], [.5, 1, .2, 0], [0, .2, 3, -.4], [.3, 0, -.4, 1.5]])
P("  c^T A c =", c @ S @ c, "; sum c_i^2 Var + 2 sum_{i<j} c_i c_j Cov =", sum(c[i] ** 2 * S[i, i] for i in range(n)) + 2 * sum(c[i] * c[j] * S[i, j] for i in range(n) for j in range(i + 1, n)))
w = rng.multivariate_normal(np.zeros(n), S, 10**6) @ c
P("  Monte Carlo Var(sum c_i X_i) =", w.var())
P("  eigenvalues of A (all >= 0):", np.linalg.eigvalsh(S))
# discriminant argument: Var(X+tY) = Var X + 2t Cov + t^2 Var Y >= 0
vx, vy, cxy = 2.0, 3.0, 1.2
t = np.linspace(-3, 3, 7)
P("  Var(X+tY) at t=-3..3:", vx + 2 * t * cxy + t * t * vy, "  min at t*=-Cov/VarY =", -cxy / vy, " min value =", vx - cxy ** 2 / vy, "(>=0 iff rho^2<=1; rho =", cxy / np.sqrt(vx * vy), ")")
u = rng.standard_normal(10**6)
for a_, b_ in ((2.0, 1.0), (-3.0, 0.0), (0.0, 5.0)):
    P(f"  Y={a_}*X+{b_}: corr(X,Y) =", np.corrcoef(u, a_ * u + b_)[0, 1])
P("  X,X^2 for X~N(0,1): corr =", np.corrcoef(u, u * u)[0, 1], "(uncorrelated, not independent)")

sec("HW4 Q4 two dice MGF (= HW3 Q4)")
t0 = 0.3
M = (np.exp(t0 * np.arange(1, 7)).mean()) ** 2
cs = np.array([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])
P("  M(0.3) =", M, " via convolution c_s:", (cs * np.exp(t0 * np.arange(2, 13))).sum() / 36)
pmf = np.convolve(np.ones(6) / 6, np.ones(6) / 6)
P("  convolution of pmfs:", np.round(pmf * 36).astype(int))

sec("extra: sums of independent variables, discrete and continuous")
P("  Expo(1)+Expo(1) = Gamma(2,1): conv at z=1.5", integrate.quad(lambda x: np.exp(-x) * np.exp(-(1.5 - x)), 0, 1.5)[0], " Gamma pdf", stats.gamma.pdf(1.5, 2), " (=z e^-z)", 1.5 * np.exp(-1.5))
P("  U(0,1)+U(0,1) triangular: f(0.5)=", integrate.quad(lambda x: 1.0, 0, 0.5)[0], " f(1)=", 1.0, " f(1.5)=", integrate.quad(lambda x: 1.0, 0.5, 1)[0])
P("  Poisson(2)+Poisson(3)=Poisson(5): P[S=4]", sum(stats.poisson.pmf(k, 2) * stats.poisson.pmf(4 - k, 3) for k in range(5)), stats.poisson.pmf(4, 5))
P("  Cauchy + Cauchy: density at 0 of (X+Y)/2 :", stats.cauchy.pdf(0), "convolution of two Cauchy at z=0:", integrate.quad(lambda x: stats.cauchy.pdf(x) * stats.cauchy.pdf(-x), -np.inf, np.inf)[0], " = 2*Cauchy(0,2) density", 1 / (2 * np.pi), "?  Cauchy(0,2) pdf(0) =", stats.cauchy.pdf(0, scale=2))

sec("PR07 completing the square (symbolic)")
import sympy as sp
u, w, s1_, s2_ = sp.symbols("u w sigma1 sigma2", positive=True)
S2 = s1_ ** 2 + s2_ ** 2
tau2 = s1_ ** 2 * s2_ ** 2 / S2
m = w * s1_ ** 2 / S2
lhs = -u ** 2 / (2 * s1_ ** 2) - (w - u) ** 2 / (2 * s2_ ** 2)
rhs = -(u - m) ** 2 / (2 * tau2) - w ** 2 / (2 * S2)
P("  exponent identity holds:", sp.simplify(lhs - rhs) == 0, "; tau/(sigma1 sigma2) = 1/sqrt(sigma1^2+sigma2^2):", sp.simplify(sp.sqrt(tau2) / (s1_ * s2_) - 1 / sp.sqrt(S2)) == 0)

sec("PR07 practice answers")
# 1 joint density c(x+y) on the unit square
x_, y_ = sp.symbols("x y")
c_ = 1 / sp.integrate(sp.integrate(x_ + y_, (y_, 0, 1)), (x_, 0, 1))
EX = sp.integrate(x_ * (x_ + y_), (x_, 0, 1), (y_, 0, 1)); EXY = sp.integrate(x_ * y_ * (x_ + y_), (x_, 0, 1), (y_, 0, 1)); EX2 = sp.integrate(x_ ** 2 * (x_ + y_), (x_, 0, 1), (y_, 0, 1))
cov = EXY - EX ** 2; var = EX2 - EX ** 2
P("  1. c =", c_, " f_X = x+1/2, E[X] =", EX, " E[XY] =", EXY, " Cov =", cov, " Var X =", var, " rho =", cov / var, "=", float(cov / var))
# 2 uniform on the disc
pts = rng.uniform(-1, 1, (4 * 10**6, 2)); pts = pts[(pts ** 2).sum(1) <= 1]
P("  2. disc: Cov (MC)", np.cov(pts.T)[0, 1], " P[|X|>0.8,|Y|>0.8] =", np.mean((np.abs(pts[:, 0]) > .8) & (np.abs(pts[:, 1]) > .8)), "(exactly 0: 0.64+0.64>1) vs P[|X|>.8]^2 =", np.mean(np.abs(pts[:, 0]) > .8) ** 2)
P("     rho(X^2,Y^2) =", np.corrcoef(pts[:, 0] ** 2, pts[:, 1] ** 2)[0, 1], " exact -1/3:", -1 / 3)
# 3 Expo(1)+Expo(2)
z = 1.3
P("  3. conv at 1.3:", integrate.quad(lambda x: np.exp(-x) * 2 * np.exp(-2 * (z - x)), 0, z)[0], " formula 2(e^-z - e^-2z) =", 2 * (np.exp(-z) - np.exp(-2 * z)), " mean", integrate.quad(lambda z: z * 2 * (np.exp(-z) - np.exp(-2 * z)), 0, np.inf)[0])
# 4 U+U
P("  4. P[X+Y>1.5] =", 1 / 8, " MC", np.mean(rng.random(10**6) + rng.random(10**6) > 1.5))
# 5 poisson
P("  5. P[S=4] =", stats.poisson.pmf(4, 5), "= 5^4 e^-5/24 =", 5 ** 4 * np.exp(-5) / 24)
# 6 X-Y > 6 for X~N(1,4), Y~N(-2,9)
P("  6. X-Y ~ N(3,13): P[X-Y>6] =", 1 - stats.norm.cdf((6 - 3) / np.sqrt(13)), " z =", 3 / np.sqrt(13), " MC", np.mean(rng.normal(1, 2, 10**7) - rng.normal(-2, 3, 10**7) > 6))
# 7 E|X-Y| iid N(5,4)
P("  7. E|X-Y| iid N(5,4):", 4 / np.sqrt(np.pi), " MC", np.abs(rng.normal(5, 2, 10**7) - rng.normal(5, 2, 10**7)).mean())
# 8 linear combination
A = np.array([[4, 3, -1], [3, 9, 0], [-1, 0, 1.]]); c = np.array([2, -3, 1.])
P("  8. c^T A c =", c @ A @ c, " eigenvalues", np.linalg.eigvalsh(A))
# 11 dice
d = np.arange(-5, 6); pd = (6 - np.abs(d)) / 36
P("  11. P[X-Y=d] =", (6 - np.abs(d)), "/36;  E|X-Y| =", (np.abs(d) * pd).sum(), "= 35/18 =", 35 / 18, " P[X+Y=7]=1/6, P[X-Y=0]=1/6; Var(X-Y)=", (d ** 2 * pd).sum(), "= 35/6 =", 35 / 6)
# 12 sample mean
n = np.ceil((1.959964 / 0.1) ** 2)
P("  12. n >= (1.96/0.1)^2 =", (1.959964 / 0.1) ** 2, "-> n =", n, " P[|Xbar-mu|<0.1 sigma] at n=385:", 2 * stats.norm.cdf(0.1 * np.sqrt(385)) - 1, " at 384:", 2 * stats.norm.cdf(0.1 * np.sqrt(384)) - 1)
# 9 correlation under affine maps
P("  9. corr(2X+1, -3Y+4) =", np.corrcoef(2 * x + 1, -3 * (0.5 * x + np.sqrt(0.75) * y) + 4)[0, 1], " vs -rho =", -0.5)
# cauchy-schwarz check
U_, V_ = rng.standard_normal(10**6), rng.standard_normal(10**6)
V_ = 0.7 * U_ + V_
P("  10. (E[UV])^2 =", np.mean(U_ * V_) ** 2, " <= E[U^2]E[V^2] =", np.mean(U_ ** 2) * np.mean(V_ ** 2))
sec("PR07 numbers for the text")
P("  uniform disc marginal f_X(x) = 2 sqrt(1-x^2)/pi at 0.9:", 2 * np.sqrt(1 - .81) / np.pi, " f_X(.9)f_Y(.9) =", (2 * np.sqrt(1 - .81) / np.pi) ** 2, " (joint density 0 at (0.9,0.9))")
P("  Var(X+tY): Var X=2, Var Y=3, Cov=1.2 -> discriminant/4 =", 1.2 ** 2 - 2 * 3, " (<0), rho =", 1.2 / np.sqrt(6))
