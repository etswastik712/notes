"""EE03 - the numbers quoted in the chapter (Ricker bifurcations, Feigenbaum ratio, Lyapunov exponents,
Hassell stability boundary, integerised Ricker cycle lengths, delayed-density-dependence regression).

    .venv/bin/python scripts/ee03_numbers.py
"""
import numpy as np
from scipy.optimize import brentq

K = 100.0


def ricker(n, r):
    return n * np.exp(r * (1 - n / K))


def logistic(x, a):
    return a * x * (1 - x)


def iterate(f, x0, par, n):
    x = x0
    for _ in range(n):
        x = f(x, par)
    return x


def attractor(f, x0, par, burn=3000, keep=64):
    x = x0
    for _ in range(burn):
        x = f(x, par)
    out = []
    for _ in range(keep):
        x = f(x, par)
        out.append(x)
    return np.array(out)


def period_of(orbit, tol=1e-6):
    for p in range(1, 33):
        if np.allclose(orbit[p:], orbit[:-p], rtol=tol, atol=tol * max(1, abs(orbit).max())):
            return p
    return None


# ---- periods of the Ricker map at the slide's r values
print("Ricker attractor periods (K=100, N0=10):")
for r in (1.3, 2.3, 2.5, 2.6, 2.7, 3.3):
    print(f"  r={r}: period {period_of(attractor(ricker, 10.0, r))}")

# ---- exact period-doubling thresholds: solve cycle conditions with the multiplier = -1
from scipy.optimize import fsolve


def cycle_conditions(z, p):
    xs, r = z[:p], z[p]
    eqs = [ricker(xs[i], r) - xs[(i + 1) % p] for i in range(p)]
    d = np.exp(r * (1 - xs / K)) * (1 - r * xs / K)
    eqs.append(np.prod(d) + 1.0)
    return eqs


bif = [2.0]
for p, r0 in [(2, 2.45), (4, 2.62), (8, 2.665)]:
    orb = attractor(ricker, 10.0, r0, burn=60000, keep=p)
    sol, info, ier, msg = fsolve(cycle_conditions, np.append(orb, r0), args=(p,), full_output=True, xtol=1e-12)
    bif.append(sol[p] if ier == 1 else float("nan"))
print("Ricker period-doubling thresholds r (1->2, 2->4, 4->8, 8->16):", np.round(bif, 4))
print("  spacing ratios:", np.round([(bif[1] - bif[0]) / (bif[2] - bif[1]), (bif[2] - bif[1]) / (bif[3] - bif[2])], 3))

# ---- superstable parameters and Feigenbaum ratio (universal), vectorised
def iter_vec(f, x, par, p):
    for _ in range(p):
        x = f(x, par)
    return x


def superstable_list(f, xc_of, lo, hi, nmax):
    roots = []
    prev = lo
    for n in range(0, nmax + 1):
        p = 2 ** n
        grid = np.linspace(prev + 1e-5, hi, 400001)
        v = iter_vec(f, xc_of(grid), grid, p) - xc_of(grid)
        idx = np.where(v[:-1] * v[1:] < 0)[0]
        root = None
        for i in idx:
            g = lambda a: iter_vec(f, xc_of(a), a, p) - xc_of(a)
            a0 = brentq(g, grid[i], grid[i + 1], xtol=1e-14)
            if n == 0 or abs(iter_vec(f, xc_of(a0), a0, p // 2) - xc_of(a0)) > 1e-5:
                root = a0
                break
        if root is None:
            break
        roots.append(root)
        prev = root
    return np.array(roots)


Rlog = superstable_list(logistic, lambda a: 0.5 + 0 * a, 1.5, 3.5699, 7)
print("logistic superstable a_n:", np.round(Rlog, 6))
print("  Feigenbaum ratios:", np.round((Rlog[1:-1] - Rlog[:-2]) / (Rlog[2:] - Rlog[1:-1]), 4), "(limit 4.6692)")
Rric = superstable_list(ricker, lambda r: K / r, 1.0 - 1e-4, 2.6924, 7)
print("Ricker superstable r_n:", np.round(Rric, 6))
print("  Feigenbaum ratios:", np.round((Rric[1:-1] - Rric[:-2]) / (Rric[2:] - Rric[1:-1]), 4))
# accumulation point estimate by geometric extrapolation
d = 4.6692
r_inf = Rric[-1] + (Rric[-1] - Rric[-2]) / (d - 1)
print("Ricker accumulation (chaos onset) estimate:", round(r_inf, 4), "(May's table: 2.6924)")

# ---- Lyapunov exponents
def lyap(f, df, x0, par, burn=2000, n=20000):
    x = x0
    for _ in range(burn):
        x = f(x, par)
    s = 0.0
    for _ in range(n):
        s += np.log(abs(df(x, par)) + 1e-300)
        x = f(x, par)
    return s / n


dric = lambda n, r: np.exp(r * (1 - n / K)) * (1 - r * n / K)
print("Lyapunov (Ricker): " + ", ".join(f"r={r}: {lyap(ricker, dric, 10.0, r):+.3f}" for r in (1.3, 2.3, 2.6, 3.0, 3.3, 3.6)))
dlog = lambda x, a: a * (1 - 2 * x)
print("Lyapunov (logistic a=4):", round(lyap(logistic, dlog, 0.3, 4.0), 4), "(exact ln2 = 0.6931)")

# ---- integerised Ricker: eventual periodicity (K, r grid), random starts
def int_ricker(n, r, Kc):
    return int(round(n * np.exp(r * (1 - n / Kc)))) if n > 0 else 0


print("Integerised Ricker: cycle length reached (300 random starts per case)")
rng0 = np.random.default_rng(3)
for Kc in (100, 1000, 10000):
    for r in (2.8, 3.0):
        nmax = int(Kc / r * np.exp(r - 1))
        lens, ext = [], 0
        for n0 in rng0.integers(1, nmax, 300):
            x, seen, t = int(n0), {}, 0
            while x not in seen and t < 400000:
                seen[x] = t
                x = int_ricker(x, r, Kc)
                t += 1
            if x == 0:
                ext += 1
            else:
                lens.append(t - seen[x])
        print(f"  K={Kc}, r={r}: max state {nmax}; extinct {ext}/300; cycle length median {int(np.median(lens))}, max {max(lens)}")

# ---- Hassell model: stability boundary
print("Hassell N_{t+1}=lam N (1+aN)^-beta: f'(N*)=1-beta*(1-lam^(-1/beta))")
for lam, beta in [(2, 1), (10, 1), (10, 3), (10, 6), (3, 6), (30, 2)]:
    d = 1 - beta * (1 - lam ** (-1 / beta))
    kind = "monotone damping" if 0 <= d < 1 else ("oscillatory damping" if -1 < d < 0 else "unstable (cycles/chaos)")
    print(f"  lam={lam}, beta={beta}: f'={d:+.3f} -> {kind}")

# ---- delayed density dependence: fit a first-order Ricker to a second-order system
rng = np.random.default_rng(1)
def sim2(r, b, steps=400, n0=(40.0, 60.0)):
    x = list(n0)
    for _ in range(steps):
        x.append(x[-1] * np.exp(r * (1 - (x[-1] + b * x[-2]) / (K * (1 + b)))))
    return np.array(x)


for r, b in [(1.6, 3.0), (1.2, 4.0)]:
    x = sim2(r, b)
    tail = x[-100:]
    print(f"2-lag model r={r}, b={b}: range of last 100 steps {tail.min():.1f}-{tail.max():.1f}, period {period_of(x[-64:], 1e-3)}")
    y = np.log(x[1:] / x[:-1])
    A = np.vstack([np.ones(len(x) - 1), x[:-1]]).T
    coef, res, *_ = np.linalg.lstsq(A[-300:], y[-300:], rcond=None)
    pred = A[-300:] @ coef
    r2 = 1 - np.sum((y[-300:] - pred) ** 2) / np.sum((y[-300:] - y[-300:].mean()) ** 2)
    rhat = coef[0]
    print(f"   fitted 1-lag Ricker: r_hat={rhat:.3f}, slope={coef[1]:.4f}, R^2={r2:.3f}; implied f'(K)=1-r_hat={1-rhat:+.3f}")


# ================================================================== chapter worked examples and practice sums (added with the EE03 chapter)
print("\n== chapter examples / practice sums")
r_h = np.log(2) / 50
print(f"Q1 r = ln2/50 = {r_h:.5f}; Q2 N(2000) = 5.4e9 exp(7 r) = {5.4e9 * np.exp(7 * r_h):.4e}")
print(f"Q3 r = ln1.12 = {np.log(1.12):.5f}; doubling time {np.log(2) / np.log(1.12):.2f} yr")
b_, d_ = 400 / 3000, 150 / 3000
print(f"Q4 r = b - d = {b_ - d_:.4f} per month; continuous N(6) = {3000 * np.exp((b_ - d_) * 6):.0f}; discrete 3000*(1+R)^6 = {3000 * (1 + b_ - d_) ** 6:.0f}; ln(1+R) = {np.log(1 + b_ - d_):.5f}")
print(f"Q5 r = ln5/10 = {np.log(5) / 10:.5f} per day; Q6 N = {500000 * np.exp(np.log(5)):.0f} (the docx rounds r to 0.16 and gets 2.47e6)")
K_, r_l, N0_ = 100, 0.6, 2
print(f"logistic K=100 r=0.6 N0=2: t at K/2 = {np.log((K_ - N0_) / N0_) / r_l:.3f}; N(10) = {K_ / (1 + (K_ - N0_) / N0_ * np.exp(-r_l * 10)):.2f}; max dN/dt = rK/4 = {r_l * K_ / 4}")
for r_ in (1.3, 2.3, 2.6):
    x = 20.0
    for _ in range(400):
        x = ricker(x, r_)
    att = []
    for _ in range(4):
        x = ricker(x, r_); att.append(round(float(x), 2))
    print(f"Ricker K=100 r={r_}: attractor {att}")
print("discrete logistic N+ = N[1+r(1-N/K)] is the logistic map with a = 1 + r: thresholds in r (= a - 1):", np.round(np.array([3, 3.4495, 3.5441, 3.5644, 3.5699]) - 1, 4))
for beta_ in (3, 6, 10):
    l0 = brentq(lambda l: beta_ * (1 - l ** (-1 / beta_)) - 1, 1.0001, 1e8)
    l1 = brentq(lambda l: beta_ * (1 - l ** (-1 / beta_)) - 2, 1.0001, 1e8)
    print(f"Hassell beta={beta_}: monotone -> oscillatory damping at lambda={l0:.3f}; stable -> unstable at lambda={l1:.3f}")
print("forecast horizon for a 1e-6 error to reach 100 at Lyapunov 0.39:", round(np.log(100 / 1e-6) / 0.39, 1), "generations")
