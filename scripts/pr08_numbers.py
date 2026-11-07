"""PR08 Order Statistics and the Multinomial Distribution (MT2113 Homework 5): every number quoted, recomputed.
    .venv/bin/python -W ignore scripts/pr08_numbers.py
"""
import itertools
import math

import numpy as np
from scipy import integrate, stats

rng = np.random.default_rng(2026)


def section(t):
    print("\n== " + t)


section("Q1: the joint cdf of (min, max) of two iid variables, F(y1,y2) = 2F(y1)F(y2) - F(y1)^2 for y1 < y2")
N = 2_000_000
X = rng.exponential(1.0, size=(N, 2))
Y1, Y2 = X.min(1), X.max(1)
y1, y2 = 0.5, 1.2
F = lambda t: 1 - np.exp(-t)
print("  Expo(1), y1 = %.1f, y2 = %.1f: formula 2F(y1)F(y2) - F(y1)^2 = %.5f, simulation %.5f" % (y1, y2, 2 * F(y1) * F(y2) - F(y1) ** 2, np.mean((Y1 <= y1) & (Y2 <= y2))))
# density: mixed partial of the cdf = 2 f(y1) f(y2); check by a finite-difference of the formula
f = lambda t: np.exp(-t)
h = 1e-4
G = lambda a, b: 2 * F(a) * F(b) - F(a) ** 2
mixed = (G(y1 + h, y2 + h) - G(y1 + h, y2 - h) - G(y1 - h, y2 + h) + G(y1 - h, y2 - h)) / (4 * h * h)
print("  mixed second difference of the cdf at (0.5, 1.2) = %.6f, 2 f(y1) f(y2) = %.6f" % (mixed, 2 * f(y1) * f(y2)))
# total mass of 2 f f on y1 < y2 is 1:
mass, _ = integrate.dblquad(lambda b, a: 2 * np.exp(-a) * np.exp(-b), 0, 60, lambda a: a, lambda a: 60)
print("  integral of 2 f(y1) f(y2) over y1 < y2 (Expo(1)) = %.6f" % mass)

section("n variables: joint density n! prod f(y_i); marginal of Y_(k): n!/((k-1)!(n-k)!) F^(k-1) (1-F)^(n-k) f")
n, k = 5, 2
U = np.sort(rng.random((1_000_000, n)), axis=1)
print("  Uniform(0,1), n = 5: E[Y_(k)] = k/(n+1): " + ", ".join("k=%d: %.4f (sim %.4f)" % (kk, kk / (n + 1), U[:, kk - 1].mean()) for kk in range(1, n + 1)))
print("  Y_(2) ~ Beta(2, 4): P(Y_(2) <= 0.3) exact %.5f, simulation %.5f" % (stats.beta.cdf(0.3, 2, 4), np.mean(U[:, 1] <= 0.3)))
c = math.factorial(n) / (math.factorial(k - 1) * math.factorial(n - k))
pdf_k = lambda t: c * t ** (k - 1) * (1 - t) ** (n - k)
print("  the formula n!/((k-1)!(n-k)!) t^(k-1) (1-t)^(n-k) with n = 5, k = 2 has constant %.0f and integrates to %.6f over (0,1)" % (c, integrate.quad(pdf_k, 0, 1)[0]))
print("  the density n! on the ordered simplex: volume of {y1 < ... < y5} in [0,1]^5 = 1/5! = %.6f, so the total mass is 5! * (1/5!) = 1" % (1 / math.factorial(5)))

section("Q2: exponential order statistics, lambda = 2")
lam = 2.0
X = rng.exponential(1 / lam, size=(2_000_000, 2))
Y1, Y2 = X.min(1), X.max(1)
Gp = Y2 - Y1
print("  Y1: mean %.5f (1/2lam = %.5f), var %.5f (1/4lam^2 = %.5f);  P(Y1 > 0.3): %.5f vs exp(-2 lam 0.3) = %.5f" % (Y1.mean(), 1 / (2 * lam), Y1.var(), 1 / (4 * lam ** 2), np.mean(Y1 > 0.3), np.exp(-2 * lam * 0.3)))
print("  G = Y2 - Y1: mean %.5f (1/lam = %.5f), var %.5f (1/lam^2 = %.5f);  P(G > 0.3): %.5f vs exp(-lam 0.3) = %.5f" % (Gp.mean(), 1 / lam, Gp.var(), 1 / lam ** 2, np.mean(Gp > 0.3), np.exp(-lam * 0.3)))
print("  independence of Y1 and G: sample correlation %.5f; P(Y1 > 0.2, G > 0.3) = %.5f vs product %.5f" % (np.corrcoef(Y1, Gp)[0, 1], np.mean((Y1 > 0.2) & (Gp > 0.3)), np.mean(Y1 > 0.2) * np.mean(Gp > 0.3)))
print("  Y2: mean %.5f (3/2lam = %.5f), var %.5f (5/4lam^2 = %.5f)  <- the sheet's 5/(4 lam^2) is Var(Y2), not Var(Y1)" % (Y2.mean(), 3 / (2 * lam), Y2.var(), 5 / (4 * lam ** 2)))
print("  Cov(Y1,Y2) = %.5f (= Var(Y1) = %.5f);  Corr(Y1,Y2) = %.5f vs 1/sqrt5 = %.5f" % (np.cov(Y1, Y2)[0, 1], 1 / (4 * lam ** 2), np.corrcoef(Y1, Y2)[0, 1], 1 / np.sqrt(5)))
print("  joint density of (Y1, G): 2 lam^2 exp(-lam(2 y1 + g)) = (2 lam e^{-2 lam y1})(lam e^{-lam g}); at (0.1, 0.2): %.6f" % (2 * lam ** 2 * np.exp(-lam * (2 * 0.1 + 0.2))))
print("  two components in parallel, lam = 0.1 per hour: E[first failure] = %.1f h, E[system failure] = %.1f h, P(second fails > 10 h after the first) = exp(-1) = %.4f" % (1 / (2 * 0.1), 3 / (2 * 0.1), np.exp(-1)))

section("n exponentials: gaps Y_(k) - Y_(k-1) ~ Expo((n-k+1) lam) independent (Renyi); n = 5, lam = 1")
n, lam = 5, 1.0
Xs = np.sort(rng.exponential(1 / lam, size=(1_000_000, n)), axis=1)
gaps = np.diff(np.concatenate([np.zeros((Xs.shape[0], 1)), Xs], axis=1), axis=1)
for kk in range(1, n + 1):
    print("  gap %d: mean %.4f vs 1/((n-k+1) lam) = %.4f" % (kk, gaps[:, kk - 1].mean(), 1 / ((n - kk + 1) * lam)))
Hn = sum(1 / j for j in range(1, n + 1))
print("  E[max] = H_5 / lam = %.4f, simulation %.4f; max gap pair correlations (largest |corr| among distinct gaps) = %.4f" % (Hn / lam, Xs[:, -1].mean(), np.abs(np.corrcoef(gaps.T) - np.eye(n)).max()))

section("Q3: the multinomial distribution, n = 10, p = (0.2, 0.3, 0.5)")
n = 10
p = np.array([0.2, 0.3, 0.5])
k = len(p)
support = [x for x in itertools.product(range(n + 1), repeat=k) if sum(x) == n]
pmf = {x: math.factorial(n) / np.prod([math.factorial(v) for v in x]) * np.prod(p ** np.array(x)) for x in support}
tot = sum(pmf.values())
mean = np.array([sum(pmf[x] * x[i] for x in support) for i in range(k)])
cov = np.array([[sum(pmf[x] * x[i] * x[j] for x in support) - mean[i] * mean[j] for j in range(k)] for i in range(k)])
print("  support size %d, total mass %.12f" % (len(support), tot))
print("  mean (exact enumeration) = %s;  n p = %s" % (np.round(mean, 6), n * p))
print("  covariance (exact enumeration) =\n%s" % np.round(cov, 6))
print("  n (diag p - p p^T) =\n%s" % np.round(n * (np.diag(p) - np.outer(p, p)), 6))
w = np.linalg.eigvalsh(cov)
print("  eigenvalues of the covariance matrix: %s (one is 0: X1 + X2 + X3 = n is constant, the vector (1,1,1) is in the kernel)" % np.round(w, 6))
print("  Corr(X1,X2) = %.5f vs -sqrt(p1 p2 / ((1-p1)(1-p2))) = %.5f" % (cov[0, 1] / np.sqrt(cov[0, 0] * cov[1, 1]), -np.sqrt(p[0] * p[1] / ((1 - p[0]) * (1 - p[1])))))
# trial-level indicators: Cov(Y_ij, Y_kj)
print("  indicator level (one trial): Var(Y_1j) = p1(1-p1) = %.4f, Cov(Y_1j, Y_2j) = -p1 p2 = %.4f (Y_1j Y_2j = 0 always), Cov(Y_1j, Y_2j') = 0 for j != j'" % (p[0] * (1 - p[0]), -p[0] * p[1]))
# conditional distribution of X1 given X2 = 3: Bin(n - 3, p1/(1-p2))
x2 = 3
cond = {x: pmf[x] for x in support if x[1] == x2}
Z = sum(cond.values())
b = stats.binom(n - x2, p[0] / (1 - p[1]))
err = max(abs(cond[x] / Z - b.pmf(x[0])) for x in cond)
print("  X1 | X2 = 3 ~ Bin(7, 0.2/0.7): max pmf difference %.1e; E[X1 | X2=3] = %.5f = 7 * 2/7 = 2" % (err, sum(x[0] * cond[x] / Z for x in cond)))
# simulation
S = rng.multinomial(n, p, size=1_000_000)
print("  simulation (10^6 draws): mean %s;  cov(X1,X2) %.4f vs -n p1 p2 = %.4f" % (np.round(S.mean(0), 4), np.cov(S[:, 0], S[:, 1])[0, 1], -n * p[0] * p[1]))
# marginals are binomial
print("  X1 ~ Bin(10, 0.2): P(X1 = 2) = %.6f; from the pmf: %.6f" % (stats.binom(10, 0.2).pmf(2), sum(v for x, v in pmf.items() if x[0] == 2)))

section("fair die, 12 rolls: counts (X1..X6) ~ Mult_6(12, 1/6)")
n = 12
p6 = np.ones(6) / 6
print("  Var(X_i) = n p (1-p) = %.5f, Cov(X_i,X_k) = -n p^2 = %.5f, Corr = -1/5 = %.3f" % (n * p6[0] * (1 - p6[0]), -n * p6[0] ** 2, -1 / 5))
pall = math.factorial(12) / (math.factorial(2) ** 6) / 6 ** 12
print("  P(every face exactly twice) = 12!/(2!^6 6^12) = %.6f (= 1 in %.0f)" % (pall, 1 / pall))
print("  P(no face missing) via inclusion-exclusion: %.6f" % sum((-1) ** j * math.comb(6, j) * ((6 - j) / 6) ** 12 for j in range(7)))

section("Poissonisation: independent Poisson(mu p_i) counts conditioned on their sum n are multinomial (n = 4, mu = 3, p = (0.2, 0.3, 0.5))")
mu, n = 3.0, 4
p = np.array([0.2, 0.3, 0.5])
sup = [x for x in itertools.product(range(n + 1), repeat=3) if sum(x) == n]
joint = {x: np.prod([stats.poisson(mu * p[i]).pmf(x[i]) for i in range(3)]) for x in sup}
Z = sum(joint.values())
mult = {x: math.factorial(n) / np.prod([math.factorial(v) for v in x]) * np.prod(p ** np.array(x)) for x in sup}
print("  P(sum = 4) for Poisson(3) = %.6f (= total of the joint over the slice %.6f); max |conditional - multinomial| = %.1e" % (stats.poisson(mu).pmf(n), Z, max(abs(joint[x] / Z - mult[x]) for x in sup)))
