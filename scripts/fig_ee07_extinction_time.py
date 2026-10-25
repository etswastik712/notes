"""EE07: stochastic extinction of a small population (birth-death process).
Left : extinction probability vs initial size N0 (linear birth-death, b>d): theory (d/b)^N0 vs Gillespie/jump-chain simulation.
Right: mean time to extinction vs carrying capacity K (birth rate capped at K): exact closed form vs simulation.
Illustrative model: per-capita rates b, d are chosen for teaching, not fitted to any species.
"""
from figlib import *

rng = np.random.default_rng(7)


def sim_pext(n0, b, d, ntr=40000, cap=300):
    """Embedded jump chain: +1 with prob b/(b+d), -1 otherwise; absorbed at 0 (extinct) or cap (escaped)."""
    p = b / (b + d)
    n = np.full(ntr, n0)
    active = np.arange(ntr)
    ext = 0
    while active.size:
        step = np.where(rng.random(active.size) < p, 1, -1)
        n[active] += step
        hit0 = n[active] == 0
        ext += hit0.sum()
        active = active[~hit0 & (n[active] < cap)]
    return ext / ntr


def T_exact(K, b, d):
    """Mean extinction time from N=K when births stop at K (lambda_n=b n for n<K, 0 at K; mu_n=d n)."""
    rho = b / d
    k = np.arange(1, K + 1)
    return np.sum((rho ** k - 1) / k) / (b - d)


def T_recursion(K, lam, mu):
    """Same quantity from tau_n = 1/mu_n + (lam_n/mu_n) tau_{n+1}, T_K = sum_{n=1..K} tau_n; lam, mu arrays on 1..Nmax."""
    nmax = len(lam)
    tau = np.zeros(nmax + 2)
    tau[nmax] = 1.0 / mu[nmax - 1]
    for n in range(nmax - 1, 0, -1):
        tau[n] = 1.0 / mu[n - 1] + lam[n - 1] / mu[n - 1] * tau[n + 1]
    return tau[1:K + 1].sum()


def sim_T(K, b, d, ntr=1000):
    n = np.full(ntr, K)
    t = np.zeros(ntr)
    alive = np.arange(ntr)
    while alive.size:
        nn = n[alive]
        up = np.where(nn < K, b * nn, 0.0)
        dn = d * nn
        tot = up + dn
        t[alive] += rng.exponential(1.0 / tot)
        n[alive] = nn + np.where(rng.random(alive.size) < up / tot, 1, -1)
        alive = alive[n[alive] > 0]
    return t.mean(), t.std() / np.sqrt(ntr), t.std()


fig, ax = plt.subplots(1, 2, figsize=(11, 4.1))

# ---- panel A
a = ax[0]
N0 = np.arange(1, 41)
for (b, d, col, nmax) in [(1.1, 1.0, BLUE, 30), (1.5, 1.0, ORANGE, 12)]:
    a.plot(N0, (d / b) ** N0, color=col, lw=1.8)
    pts = np.arange(1, nmax + 1, 1 if nmax <= 12 else 2)
    sims = np.array([sim_pext(int(k), b, d) for k in pts])
    a.plot(pts, sims, "o", color=col, ms=4.5, mfc="white", mew=1.5)
    print(f"b={b} d={d}: d/b={d/b:.4f}; P_ext(1)={d/b:.4f} sim {sims[0]:.4f}; "
          f"P_ext(10)={(d/b)**10:.4f} sim {sim_pext(10, b, d):.4f}; P_ext(50)={(d/b)**50:.5f}")
a.set_yscale("log")
a.set_ylim(3e-4, 1.5)
a.set_xlim(0, 41)
a.set_xlabel("initial number of individuals $N_0$")
a.set_ylabel("probability of eventual extinction")
a.set_title("Growing populations still go extinct")
a.text(31, 0.045, "$b=1.1,\\ d=1.0$\n$r=b-d=0.1$", color=INK, fontsize=9, va="center")
a.text(14.2, 0.0035, "$b=1.5,\\ d=1.0$", color=INK, fontsize=9, va="center")
a.plot([29], [0.045], "o", color=BLUE, ms=5)
a.plot([12.5], [0.0035], "o", color=ORANGE, ms=5)
a.text(1.5, 5e-4, "line = $(d/b)^{N_0}$; circles = simulation (40 000 runs each)", color=MUTED, fontsize=8)

# ---- panel B
b_, d_ = 1.2, 1.0
rho = b_ / d_
Ks = np.arange(2, 101)
Tex = np.array([T_exact(int(K), b_, d_) for K in Ks])
# logistic-type death rate: mu_n = d n + (b-d) n^2/K, lambda_n = b n, truncated at 4K
Tlog = []
for K in Ks:
    nm = 4 * int(K)
    nn = np.arange(1, nm + 1)
    Tlog.append(T_recursion(int(K), b_ * nn, d_ * nn + (b_ - d_) * nn ** 2 / K))
Tlog = np.array(Tlog)
# consistency of closed form with the recursion for the ceiling model
for K in (5, 20, 60):
    nn = np.arange(1, K + 1)
    lam = b_ * nn.astype(float)
    lam[-1] = 0.0
    assert abs(T_recursion(K, lam, d_ * nn) / T_exact(K, b_, d_) - 1) < 1e-9
b = ax[1]
b.plot(Ks, Tex, color=BLUE, lw=1.8)
b.plot(Ks, Tlog, color=VIOLET, lw=1.6, ls="--")
Ksim = [5, 10, 15, 20, 25, 30, 35, 40]
for K in Ksim:
    m, se, sd = sim_T(K, b_, d_)
    b.errorbar([K], [m], yerr=[2 * se], fmt="o", color=BLUE, ms=4.5, mfc="white", mew=1.5, capsize=2)
    print(f"K={K}: exact {T_exact(K, b_, d_):.2f}, sim {m:.2f} +- {se:.2f} (SD/mean={sd/m:.2f}), logistic exact {Tlog[K-2]:.2f}")
for K in (10, 20, 30, 50, 100):
    print(f"T_exact(K={K}) = {T_exact(K, b_, d_):.4g}   logistic: {Tlog[K-2]:.4g}")
lead = lambda K: d_ * rho ** (K + 1) / (K * (b_ - d_) ** 2)
print("leading-order d rho^(K+1)/(K (b-d)^2) at K=50:", f"{lead(50):.4g}", " exact:", f"{T_exact(50, b_, d_):.4g}")
b.set_yscale("log")
b.set_xlim(0, 101)
b.set_xlabel("carrying capacity $K$ (start at $N=K$)")
b.set_ylabel("mean time to extinction (years)")
b.set_title("Persistence time grows exponentially with $K$")
b.text(56, 2e1, "solid: closed form, ceiling model\ndashed: logistic death rate (exact)\ncircles: simulation $\\pm2$ SE", fontsize=8.5, color=INK, va="center")
b.text(4, 3e5, "$\\ln T\\approx K\\ln(b/d)$,\nslope $\\ln1.2=0.18$ per individual", fontsize=9, color=INK, va="center")
b.axhline(100, color=GRID, lw=1)
b.text(1, 125, "100 yr", color=MUTED, fontsize=8)
b.axhline(1000, color=GRID, lw=1)
b.text(1, 1250, "1000 yr", color=MUTED, fontsize=8)
fig.tight_layout()
save(fig, "fig_ee07_extinction_time")
