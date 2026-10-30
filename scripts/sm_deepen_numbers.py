"""SM01-SM03 deepening: extra numbers (Edgeworth, Chernoff, MaxEnt dice, AEP, cat map, hypersphere marginal, Brillouin, Einstein solid).

    .venv/bin/python -W ignore scripts/sm_deepen_numbers.py
"""
import numpy as np
from math import comb, exp, factorial, lgamma, log, pi, sqrt
from scipy import stats, optimize, special

P = print
def sec(t): P("\n#####", t)
kB = 1.380649e-23; muB = 9.2740100783e-24; NA = 6.02214076e23; R = 8.314462618

sec("SM01: moment-cumulant (partition) formula and Gamma/exponential")
P("exponential(1): kappa_n = (n-1)! ; m4 = k4 + 4 k3 k1 + 3 k2^2 + 6 k2 k1^2 + k1^4 =", 6 + 4 * 2 * 1 + 3 * 1 + 6 * 1 + 1, " vs 4! =", factorial(4))
P("Gaussian check m4 = 3 s^4: k4=0, k2=s^2, k1=0 -> 3 ; m6 = 15 s^6 (15 pair partitions)")

sec("SM01: Edgeworth correction for the Poisson CDF, lambda = 10")
lam = 10.0; mu = lam; s = sqrt(lam); g1 = 1 / sqrt(lam)       # skewness
print("k   exact    Gaussian(cc)   Edgeworth(skew)   err_G    err_E")
for k in (3, 5, 7, 10, 13, 15, 18):
    ex = stats.poisson.cdf(k, lam)
    z = (k + 0.5 - mu) / s
    G = stats.norm.cdf(z)
    E = G - g1 / 6 * (z ** 2 - 1) * stats.norm.pdf(z)
    print(f"{k:2d} {ex:8.5f} {G:10.5f} {E:14.5f} {G - ex:+9.5f} {E - ex:+9.5f}")
P("Berry-Esseen: sup|F_N - Phi| <= C rho/(sigma^3 sqrt N), C < 0.48 ; for N=100 fair coins rho/sigma^3 = 1 -> bound", 0.48 / 10, " ; actual sup ~", 0.5 * stats.binom.pmf(50, 100, .5) * 1.0)

sec("SM01: Chernoff bound P(mean >= 0.6) <= exp(-N I(0.6)) is rigorous for every N")
def I(m): return log(2) + m * log(m) + (1 - m) * log(1 - m)
for N in (10, 20, 50, 100, 1000):
    k0 = int(np.ceil(0.6 * N - 1e-9))
    ex = stats.binom.sf(k0 - 1, N, .5); bd = exp(-N * I(0.6))
    P(f"N={N:5d}: exact {ex:.4e}  Chernoff {bd:.4e}  ratio bound/exact = {bd / ex:.2f}")
k = 20
P("Poisson(10) P(X>=20): exact", stats.poisson.sf(19, 10.0), " Chernoff exp(-lam)(e lam/k)^k =", exp(-10) * (np.e * 10 / k) ** k)
q = np.array([.6, .4]); p0 = np.array([.5, .5])
P("Sanov: D(q||p) for q=(0.6,0.4), p=(1/2,1/2) =", (q * np.log(q / p0)).sum(), " = I(0.6) =", I(0.6))

sec("SM01: Jaynes' dice (mean 4.5) by maximum entropy")
faces = np.arange(1, 7)
def mean_for(l): w = np.exp(-l * faces); return (faces * w).sum() / w.sum()
l = optimize.brentq(lambda l: mean_for(l) - 4.5, -3, 3)
w = np.exp(-l * faces); pj = w / w.sum()
P("lambda =", l, " p =", np.round(pj, 4), " check mean =", (faces * pj).sum(), " entropy =", -(pj * np.log(pj)).sum(), " (uniform ln6 =", log(6), ") ; ln Z =", log(w.sum()), "S = ln Z + lambda<F> =", log(w.sum()) + l * 4.5)
P("mean 3.5 -> lambda = 0 (uniform); mean 5.5 -> lambda =", optimize.brentq(lambda l: mean_for(l) - 5.5, -5, 3))

sec("SM01: mutual information of a binary symmetric channel, eps = 0.1")
eps = 0.1
Hb = lambda p_: -(p_ * log(p_) + (1 - p_) * log(1 - p_))
P("I(X;Y) = ln2 - H(0.1) =", log(2) - Hb(eps), "nats =", (log(2) - Hb(eps)) / log(2), "bits ; capacity of the channel = 1 - H2(0.1) =", 1 - Hb(eps) / log(2))

sec("SM01: typical set (AEP) for p = 0.1, N = 1000")
Nn = 1000; pp = 0.1
Hn = Hb(pp)
lo, hi = Nn * (Hn - 0.05), Nn * (Hn + 0.05)
ks = np.arange(Nn + 1)
logp_seq = ks * log(pp) + (Nn - ks) * log(1 - pp)
typ = (-logp_seq >= lo) & (-logp_seq <= hi)
P("H =", Hn, " nats ; typical set (|-ln p(x)/N - H| < 0.05) contains k in", ks[typ].min(), "..", ks[typ].max(),
  " probability =", stats.binom.pmf(ks[typ], Nn, pp).sum(), " ; size ln|T| =", log(sum(comb(Nn, int(kk)) for kk in ks[typ])), " vs N H =", Nn * Hn, " vs N ln2 =", Nn * log(2))

sec("SM02: Arnold cat map and coarse-graining")
rng = np.random.default_rng(5)
lam_cat = log((3 + sqrt(5)) / 2)
M = 40
pts = 0.30 + 0.05 * rng.random((200000, 2))
def cell_entropy(pts, M):
    ix = np.minimum((pts[:, 0] * M).astype(int), M - 1); iy = np.minimum((pts[:, 1] * M).astype(int), M - 1)
    c = np.bincount(ix * M + iy, minlength=M * M) / len(pts)
    c = c[c > 0]; return -(c * np.log(c)).sum()
x = pts.copy()
P("Lyapunov exponent ln((3+sqrt5)/2) =", lam_cat, " ; det of the map = 1 (area preserving)")
for t in range(0, 11):
    if t in (0, 1, 2, 3, 4, 5, 6, 7, 8, 10):
        P(f"t={t:2d}  S_coarse = {cell_entropy(x, M):.4f}   (max ln(M^2) = {log(M * M):.4f}; initial ln(cells) = {log((0.05 * M + 1) ** 2):.3f}; theory S0 + lam t = {log(0.05 * M * 0.05 * M) + lam_cat * t:.3f})")
    x = np.c_[(2 * x[:, 0] + x[:, 1]) % 1.0, (x[:, 0] + x[:, 1]) % 1.0]

sec("SM02: marginal of one momentum component from the uniform measure on the 3N-sphere")
def ratio(N, z):
    n = 3 * N                                  # radius R^2 = 2mE = n m kT => R = sqrt(n) sigma
    if z * z >= n: return 0.0
    lf = (n - 3) / 2 * log(1 - z ** 2 / n) + special.gammaln(n / 2) - 0.5 * log(pi * n) - special.gammaln((n - 1) / 2)
    return exp(lf) / (exp(-z ** 2 / 2) / sqrt(2 * pi))
for N in (10, 100, 1000):
    P(f"N={N:5d} (n=3N={3 * N}): exact/Gaussian at z=0: {ratio(N, 0.0):.4f}; z=1: {ratio(N, 1.0):.4f}; z=2: {ratio(N, 2.0):.4f}; z=3: {ratio(N, 3.0):.4f}; z=5: {ratio(N, 5.0):.4f}; z=7: {ratio(N, 7.0):.4f}")
P("(normalisation check N=10: integral of exact density =", __import__('scipy.integrate', fromlist=['quad']).quad(lambda z: (1 - z ** 2 / 30) ** 13.5 * special.gamma(15) / (sqrt(pi * 30) * special.gamma(14.5)), -sqrt(30), sqrt(30))[0], ")")
for n_ in (30, 300):
    for e in (0.01, 0.1):
        P(f"fraction of the volume of a {n_}-dim ball within the outer shell of relative thickness {e}: {1 - (1 - e) ** n_:.4f}")
P("ice residual entropy (Pauling): R ln(3/2) =", R * log(1.5), "J/(mol K) (measured ~3.4 +- 0.2, recalled)")

sec("SM03: Brillouin, Langevin, spin-1/2")
def brillouin(J, y): a = (2 * J + 1) / (2 * J); b = 1 / (2 * J); return a / np.tanh(a * y) - b / np.tanh(b * y)
def langevin(x): return 1 / np.tanh(x) - 1 / x
B, T = 5.0, 2.0
x = muB * B / (kB * T); J = 3.5; g = 2.0; y = g * J * x
P(f"Gd3+ (J=7/2, g=2) at B={B} T, T={T} K: x = muB B/kT = {x:.4f}, y = g J x = {y:.3f} ; M/Msat Brillouin = {brillouin(J, y):.4f} ; Langevin with the same saturation moment = {langevin(y):.4f} ; spin-1/2 with x: tanh(x) = {np.tanh(x):.4f}")
P("Curie constants ~ g^2 J(J+1): spin-1/2 (g=2):", 4 * 0.75, " ; J=7/2:", 4 * 3.5 * 4.5, " ; ratio", 4 * 3.5 * 4.5 / (4 * 0.75), " ; Langevin (classical, moment mu): mu^2 ->", "g^2 J^2 for J->inf")
for J in (0.5, 1.0, 3.5):
    for yy in (0.1, 1.0, 5.0):
        P(f"B_J: J={J}, y={yy}: {brillouin(J, yy):.4f}   small-y slope (J+1)/(3J) y = {(J + 1) / (3 * J) * yy:.4f}")
P("Langevin small x: L(x) = x/3 - x^3/45 ; at x=0.3 :", langevin(0.3), " vs ", 0.3 / 3 - 0.3 ** 3 / 45)
x0 = 0.5
P("static response: d(tanh x)/dx = sech^2 x =", 1 / np.cosh(x0) ** 2, " ; beta Var(M)/(N mu) with Var = sech^2 x ->", 1 / np.cosh(x0) ** 2)

sec("SM03: Einstein solid, Dulong-Petit")
def cE(x): return x ** 2 * np.exp(x) / (np.exp(x) - 1) ** 2
for t_ in (0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0, 5.0):
    P(f"T/theta_E = {t_:5.2f}: C/3Nk = {cE(1 / t_):.5f}")
P("Dulong-Petit 3R =", 3 * R, "J/(mol K); Cu 24.4, Al 24.2, Pb 26.4, Au 25.4, diamond 6.1 (recalled, 298 K)")
thE = 1300.0
P("diamond with theta_E ~ 1300 K (fitted, not predicted): C =", 3 * R * cE(thE / 298.15), "J/(mol K)")
for x_ in (0.1, 1.0, 3.0):
    zq = 1 / (2 * np.sinh(x_ / 2)); zc = 1 / x_
    P(f"oscillator x = {x_}: quantum z = {zq:.4f}, classical 1/x = {zc:.4f}, ratio {zq / zc:.4f} (= 1 - x^2/24 + ... : {1 - x_ ** 2 / 24:.4f})")
