"""PR09 Change of Variables, the Multivariate Normal and Products of Uniforms (MT2113 Weeks 4-5 summaries and Homework 6): every number quoted, recomputed.
    .venv/bin/python -W ignore scripts/pr09_numbers.py
"""
import math

import numpy as np
from scipy import integrate, special, stats

rng = np.random.default_rng(2026)


def section(t):
    print("\n== " + t)


section("Week 4: marginal of the uniform distribution on a disc of radius R (the semicircle law)")
R = 2.0
fx = lambda x: 2 * np.sqrt(R * R - x * x) / (math.pi * R * R)
print("  R = 2: integral of f_X1 over [-2,2] = %.6f (must be 1)" % integrate.quad(fx, -R, R)[0])
P = integrate.quad(fx, -R / 2, R / 2)[0]
exact = (1 / math.pi) * (math.sqrt(3) / 2 + math.pi / 6) * 1.0       # P(|X|<R/2) = (2/pi)(x sqrt(1-x^2)/2 + asin(x)/2) at x=1/2, doubled
N = 2_000_000
ang = rng.uniform(0, 2 * math.pi, N); rad = R * np.sqrt(rng.uniform(0, 1, N))
X1, X2 = rad * np.cos(ang), rad * np.sin(ang)
print("  P(|X1| < R/2) = %.6f by the marginal; closed form sqrt(3)/(2 pi) + 1/3 = %.6f; simulation %.6f" % (P, math.sqrt(3) / (2 * math.pi) + 1 / 3, np.mean(np.abs(X1) < R / 2)))
print("  conditional X2 | X1 = 1 is uniform on +-sqrt(R^2-1) = +-%.5f: f = 1/(2 sqrt(R^2-1)) = %.5f; simulation (|X1 - 1| < 0.01): range [%.3f, %.3f], mean %.4f" % (
    math.sqrt(R * R - 1), 1 / (2 * math.sqrt(R * R - 1)), X2[np.abs(X1 - 1) < 0.01].min(), X2[np.abs(X1 - 1) < 0.01].max(), X2[np.abs(X1 - 1) < 0.01].mean()))
print("  Bayes check at (x, y) = (1, 0.5): f(y|x) f(x) / f(y) = %.6f vs f(x|y) = 1/(2 sqrt(R^2 - y^2)) = %.6f" % (
    (1 / (2 * math.sqrt(R * R - 1))) * fx(1.0) / fx(0.5), 1 / (2 * math.sqrt(R * R - 0.25))))

section("Week 4, Example 2: P(X1 < X2) -- the sheet says Poisson but integrates exponential densities")
l1, l2 = 2.0, 3.0
E1, E2 = rng.exponential(1 / l1, N), rng.exponential(1 / l2, N)
print("  Expo(%g), Expo(%g): lambda1/(lambda1+lambda2) = %.5f, simulation %.5f" % (l1, l2, l1 / (l1 + l2), np.mean(E1 < E2)))
ks = np.arange(0, 80)
pois = lambda lam: stats.poisson.pmf(ks, lam)
def p_lt(a, b):
    return sum(pois(a)[k] * (1 - stats.poisson.cdf(k, b)) for k in ks)
print("  Poisson(%g), Poisson(%g): P(X1 < X2) = %.5f (not %.5f); P(X1 = X2) = %.5f; simulation %.5f" % (
    l1, l2, p_lt(l1, l2), l1 / (l1 + l2), sum(pois(l1) * pois(l2)), np.mean(rng.poisson(l1, N) < rng.poisson(l2, N))))
print("  Poisson(2), Poisson(2): P(X1<X2) = %.5f = (1 - e^-4 I0(4))/2 = %.5f" % (p_lt(2, 2), (1 - math.exp(-4) * special.i0(4)) / 2))
t = 0.3
print("  mgf of a sum: Expo(1)+Expo(2) at t = %.1f: M_X M_Y = %.5f, simulation of E[e^{t(X+Y)}] %.5f" % (t, (1 / (1 - t)) * (2 / (2 - t)), np.mean(np.exp(t * (rng.exponential(1, N) + rng.exponential(0.5, N))))))

section("Week 5: change of variables, one dimension")
X = rng.normal(0, 1, N)
Y = np.exp(X)
ys = np.array([0.5, 1.0, 2.0])
fY = stats.norm.pdf(np.log(ys)) / ys
h = 0.01
print("  Y = e^X, X ~ N(0,1) (log-normal): f_Y(y) = f_X(ln y)/y at y = 0.5,1,2: %s; histogram %s" % (np.round(fY, 4), np.round([np.mean(np.abs(Y - y) < h) / (2 * h) for y in ys], 4)))
Z = X * X
zs = np.array([0.25, 1.0, 4.0])
fZ = (stats.norm.pdf(np.sqrt(zs)) * 2) / (2 * np.sqrt(zs))             # two preimages +-sqrt(z), each with |dx/dz| = 1/(2 sqrt z)
print("  Y = X^2 (two preimages): f_Y(y) = e^{-y/2}/sqrt(2 pi y) at y = 0.25, 1, 4: %s; chi-square(1) pdf %s; histogram %s" % (
    np.round(fZ, 4), np.round(stats.chi2.pdf(zs, 1), 4), np.round([np.mean(np.abs(Z - z) < h / 2) / h for z in zs], 4)))
a, b = -3.0, 5.0
W = a * X + b
print("  Y = aX + b with a = -3, b = 5: f_Y(y) = f_X((y-b)/a)/|a| is N(5, 9): simulation mean %.4f, sd %.4f; KS distance to N(5,3) = %.5f" % (W.mean(), W.std(), stats.kstest(W[:200000], stats.norm(5, 3).cdf).statistic))

section("Week 5: change of variables, n dimensions (Jacobian)")
A = np.array([[2.0, 1.0], [0.0, 3.0]])
print("  Y = A X, X uniform on the unit square, A = [[2,1],[0,3]]: det A = %.1f, so f_Y = 1/|det A| = %.5f on a parallelogram of area %.1f" % (np.linalg.det(A), 1 / abs(np.linalg.det(A)), abs(np.linalg.det(A))))
U = rng.uniform(0, 1, (N, 2)); V = U @ A.T
print("  simulation: P(Y in the box [0,2]x[0,3]) = %.5f; by f_Y: (area of parallelogram inside the box)/6 = %.5f" % (
    np.mean((V[:, 0] >= 0) & (V[:, 0] <= 2) & (V[:, 1] >= 0) & (V[:, 1] <= 3)), integrate.dblquad(lambda y1, y2: 1.0 if (0 <= y1 - y2 / 3 <= 2) else 0.0, 0, 3, 0, 2)[0] / 6))
rr = np.sqrt(-2 * np.log(rng.uniform(size=N))); th = 2 * math.pi * rng.uniform(size=N)
g1, g2 = rr * np.cos(th), rr * np.sin(th)
print("  polar coordinates (Jacobian r) and Box-Muller: R = sqrt(-2 ln U1) has density r e^{-r^2/2} (Rayleigh); Theta = 2 pi U2; X = R cos Theta, Y = R sin Theta: mean %.4f / %.4f, var %.4f / %.4f, corr %.4f, KS(X vs N(0,1)) %.5f, E[R^2] = %.4f (= 2)" % (
    g1.mean(), g2.mean(), g1.var(), g2.var(), np.corrcoef(g1, g2)[0, 1], stats.kstest(g1[:200000], stats.norm.cdf).statistic, np.mean(rr ** 2)))
print("  P(R < 1) = 1 - e^{-1/2} = %.5f, simulation %.5f" % (1 - math.exp(-0.5), np.mean(rr < 1)))

section("Week 5 / Homework 4 Q3: |corr| <= 1 from the eigenvalues of the 2x2 covariance matrix")
for (vx, vy, c) in [(4.0, 9.0, 3.0), (4.0, 9.0, 6.0), (4.0, 9.0, 7.0)]:
    disc = (vx + vy) ** 2 - 4 * (vx * vy - c * c)
    lam = ((vx + vy) - math.sqrt(disc)) / 2, ((vx + vy) + math.sqrt(disc)) / 2
    print("  Var X = %g, Var Y = %g, Cov = %g: corr = %.4f, eigenvalues %.4f, %.4f (numpy %s)" % (vx, vy, c, c / math.sqrt(vx * vy), lam[0], lam[1], np.round(np.linalg.eigvalsh(np.array([[vx, c], [c, vy]])), 4)))
print("  Cov = 6 gives corr = 1 and a zero eigenvalue (Y = 1.5 X exactly); Cov = 7 gives corr 1.1667 > 1 and a negative eigenvalue: not a covariance matrix")

section("Homework 6 Q1: the multivariate normal and orthogonal diagonalisation")
Sig = np.array([[2.0, 1.0], [1.0, 2.0]]); mu = np.array([1.0, -1.0])
O = np.array([[1.0, 1.0], [1.0, -1.0]]) / math.sqrt(2)   # rows = the eigenvectors (1,1)/sqrt2 and (1,-1)/sqrt2
w = np.diag(O @ Sig @ O.T)                         # eigenvalues 3 and 1, in this order
print("  Sigma = [[2,1],[1,2]]: eigenvalues %s (numpy: %s); O (rows = eigenvectors) = %s; O O^T = I: %s; O Sigma O^T = %s" % (np.round(w, 4), np.round(np.linalg.eigvalsh(Sig), 4), np.round(O, 4).tolist(), np.allclose(O @ O.T, np.eye(2)), np.round(O @ Sig @ O.T, 6).tolist()))
mup = O @ mu
print("  mu' = O mu = %s; det Sigma = %.4f = product of eigenvalues %.4f" % (np.round(mup, 4), np.linalg.det(Sig), np.prod(w)))
print("  note: the original variances are Sigma_ii = 2, 2; the variances of the Y_i are the EIGENVALUES %s (not the sigma_i^2 of the X_i)" % np.round(w, 4))
fX = lambda x: np.exp(-0.5 * (x - mu) @ np.linalg.inv(Sig) @ (x - mu)) / ((2 * math.pi) ** 1 * math.sqrt(np.linalg.det(Sig)))
fYprod = lambda y: np.prod([stats.norm.pdf(y[i], mup[i], math.sqrt(w[i])) for i in range(2)])
worst = 0
for _ in range(1000):
    x = rng.normal(0, 2, 2) + mu
    worst = max(worst, abs(fX(x) - fYprod(O @ x)))             # |det O| = 1
print("  max over 1000 random x of |f_X(x) - prod_i f_{Y_i}((Ox)_i)| = %.2e (the joint pdf factorises)" % worst)
Xs = rng.multivariate_normal(mu, Sig, N); Ys = Xs @ O.T
print("  simulation: sample cov of X = %s; sample cov of Y = %s (off-diagonal ~ 0); corr(Y1,Y2) = %.4f; Y means %s" % (np.round(np.cov(Xs.T), 3).tolist(), np.round(np.cov(Ys.T), 3).tolist(), np.corrcoef(Ys.T)[0, 1], np.round(Ys.mean(0), 3)))
print("  Y1 = (X1+X2)/sqrt2 has variance 3, Y2 = (X1-X2)/sqrt2 variance 1 (= the eigenvalues); KS Y1 vs N(%.3f, sqrt3) %.5f; KS Y2 vs N(%.3f, 1) %.5f" % (
    mup[0], stats.kstest(Ys[:200000, 0], stats.norm(mup[0], math.sqrt(w[0])).cdf).statistic, mup[1], stats.kstest(Ys[:200000, 1], stats.norm(mup[1], math.sqrt(w[1])).cdf).statistic))
S3 = np.array([[3.0, 1.0, 0.5], [1.0, 2.0, -0.7], [0.5, -0.7, 1.5]])
w3, Q3 = np.linalg.eigh(S3)
print("  3x3 example: Sigma has eigenvalues %s (all > 0: positive definite); O Sigma O^T diagonal: %s" % (np.round(w3, 4), np.allclose(Q3.T @ S3 @ Q3, np.diag(w3))))
print("  independent normals need not come from a covariance matrix with zero off-diagonals: the covariance of (Y1,Y2) is zero ONLY after the rotation; for the jointly normal pair uncorrelated <=> independent")

section("Homework 6 Q2: -ln U is Expo(1); the product of n uniforms")
Uu = rng.uniform(size=(N, 5))
Xe = -np.log(Uu[:, 0])
print("  X = -ln U: P(X > 1) = %.5f (e^-1 = %.5f); mean %.4f (1), var %.4f (1); KS vs Expo(1) %.5f" % (np.mean(Xe > 1), math.exp(-1), Xe.mean(), Xe.var(), stats.kstest(Xe[:200000], stats.expon.cdf).statistic))
V5 = -np.log(Uu).sum(1)
print("  V = -ln(U1...U5) ~ Gamma(5,1): mean %.4f (5), var %.4f (5); KS vs Gamma(5) %.5f; mgf at t = 0.3: simulation %.5f, (1-t)^-5 = %.5f" % (V5.mean(), V5.var(), stats.kstest(V5[:200000], stats.gamma(5).cdf).statistic, np.mean(np.exp(0.3 * V5)), (1 - 0.3) ** -5))
Up = Uu.prod(1)
n = 5
dens = lambda u: (-math.log(u)) ** (n - 1) / math.factorial(n - 1)
print("  U = U1...U5 has density (-ln u)^4/4! on (0,1): integrates to %.6f; E[U] = 2^-5 = %.5f (numeric %.5f, simulation %.5f); E[U^2] = 3^-5 = %.6f (numeric %.6f)" % (
    integrate.quad(dens, 0, 1)[0], 2.0 ** -n, integrate.quad(lambda u: u * dens(u), 0, 1)[0], Up.mean(), 3.0 ** -n, integrate.quad(lambda u: u * u * dens(u), 0, 1)[0]))
print("  Var(U) = 3^-n - 4^-n = %.6f (simulation %.6f)" % (3.0 ** -n - 4.0 ** -n, Up.var()))
print("  n = 2: density -ln u; P(U1 U2 < 0.1) = 0.1 (1 - ln 0.1) = %.6f, simulation %.6f" % (0.1 * (1 - math.log(0.1)), np.mean(Uu[:, 0] * Uu[:, 1] < 0.1)))
print("  density at u = 0.01 (n = 5): %.4f; histogram %.4f" % (dens(0.01), np.mean(np.abs(Up - 0.01) < 0.0005) / 0.001))

section("Homework 6 Q3: the tangent line of a convex function lies below the graph; Jensen")
xs = np.linspace(-6, 6, 120001)
for name, g, dg, a in [("e^x at a = 0", np.exp, np.exp, 0.0), ("x^4 at a = 1", lambda x: x ** 4, lambda x: 4 * x ** 3, 1.0), ("x^2 at a = -2", lambda x: x ** 2, lambda x: 2 * x, -2.0)]:
    gap = g(xs) - (g(a) + dg(a) * (xs - a))
    print("  g = %-14s: min over [-6,6] of g(x) - tangent(x) = %.3e at x = %.4f (touches only at x = a)" % (name, gap.min(), xs[gap.argmin()]))
Xn = rng.normal(0, 1, N)
print("  Jensen, g = e^x, X ~ N(0,1): E g(X) = %.5f (exact e^{1/2} = %.5f) >= g(E X) = %.5f" % (np.exp(Xn).mean(), math.exp(0.5), 1.0))
Xu = rng.uniform(1, 3, N)
print("  g = 1/x on (1,3), X ~ U(1,3): E[1/X] = ln3/2 = %.5f (simulation %.5f) >= 1/E[X] = %.5f" % (math.log(3) / 2, np.mean(1 / Xu), 1 / 2))
Xq = rng.uniform(0, 1, N)
gap = np.exp(Xq).mean() - math.exp(0.5)
print("  quantitative form: g'' >= m gives E g(X) - g(E X) >= (m/2) Var X. g = e^x, X ~ U(0,1): m = 1 (g'' >= e^0), Var = 1/12: bound %.5f; actual gap (e-1) - e^{1/2} = %.5f (simulation %.5f)" % (1 / 24, (math.e - 1) - math.exp(0.5), gap))
print("  AM-GM from Jensen with g = -ln: for positive a_i, mean(-ln a_i) >= -ln mean(a_i) => geometric mean <= arithmetic mean; a = (1, 4, 16): GM %.4f <= AM %.4f" % ((1 * 4 * 16) ** (1 / 3), (1 + 4 + 16) / 3))

section("Practice items")
Xe1 = rng.exponential(1.0, N)
print("  P3: Y = sqrt(X), X ~ Expo(1): f_Y = 2y e^{-y^2}; E[Y] = sqrt(pi)/2 = %.5f (simulation %.5f); P(Y > 1) = e^-1 = %.5f (%.5f)" % (math.sqrt(math.pi) / 2, np.sqrt(Xe1).mean(), math.exp(-1), np.mean(np.sqrt(Xe1) > 1)))
Z1, Z2 = rng.normal(size=N), rng.normal(size=N)
print("  P4: Y1 = X1+X2, Y2 = X1-X2: |det A| = 2; Var Y1 = %.4f, Var Y2 = %.4f, Cov = %.4f (all expected 2, 2, 0)" % ((Z1 + Z2).var(), (Z1 - Z2).var(), np.cov(Z1 + Z2, Z1 - Z2)[0, 1]))
print("  P5: R^2 = X^2+Y^2: P(R^2 > 3) = e^{-3/2} = %.5f (simulation %.5f); E[R^2] = %.4f" % (math.exp(-1.5), np.mean(Z1 ** 2 + Z2 ** 2 > 3), np.mean(Z1 ** 2 + Z2 ** 2)))
S5 = np.array([[5.0, 3.0], [3.0, 5.0]])
print("  P6: Sigma = [[5,3],[3,5]]: eigenvalues %s, det = %.1f; Var(X1+X2) = 5+5+2*3 = %.1f = 2 * 8" % (np.round(np.linalg.eigvalsh(S5), 4), np.linalg.det(S5), np.ones(2) @ S5 @ np.ones(2)))
rho = 0.8
Sr = np.array([[1, rho], [rho, 1]])
print("  P7: Sigma = [[1,rho],[rho,1]], rho = 0.8: eigenvalues %s (= 1 +- rho), ratio of axis lengths sqrt(%.1f/%.1f) = %.4f" % (np.round(np.linalg.eigvalsh(Sr), 4), 1 + rho, 1 - rho, math.sqrt((1 + rho) / (1 - rho))))
print("  P8: X = -ln(U)/2 is Expo(2): mean %.4f (0.5), P(X > 1) = e^-2 = %.5f (simulation %.5f)" % ((-np.log(rng.uniform(size=N)) / 2).mean(), math.exp(-2), np.mean(-np.log(rng.uniform(size=N)) / 2 > 1)))
U3 = rng.uniform(size=(N, 3)).prod(1)
F3 = lambda u: 0.5 * u * (math.log(u) ** 2 - 2 * math.log(u) + 2)
print("  P9: U = U1 U2 U3 has density (ln u)^2/2: P(U < 1/8) = %.5f (numeric integral %.5f, simulation %.5f); E[U] = 1/8, simulation %.5f" % (F3(1 / 8), integrate.quad(lambda u: math.log(u) ** 2 / 2, 0, 1 / 8)[0], np.mean(U3 < 1 / 8), U3.mean()))
print("  P10: X in {1,3} equally likely: E[X^2] = %.1f >= (EX)^2 = %.1f; E[1/X] = %.4f >= 1/EX = %.4f" % (5.0, 4.0, (1 + 1 / 3) / 2, 0.5))
xs2 = np.linspace(-5, 5, 100001)
print("  P11: e^x - e x >= 0 with minimum %.2e at x = %.4f" % ((np.exp(xs2) - math.e * xs2).min(), xs2[(np.exp(xs2) - math.e * xs2).argmin()]))
