"""SM01 - binomial -> Gaussian, Stirling, Cauchy vs Gaussian running means, and the large-deviation rate function."""
from figlib import *
from math import comb, log, pi, sqrt
from scipy.special import gammaln
from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.4))

# A  binomial -> Gaussian (standardised)
a = axes[0, 0]
z = np.linspace(-4, 4, 400)
a.plot(z, np.exp(-z ** 2 / 2) / sqrt(2 * pi), color=INK, lw=1.2, label="Gaussian")
for N, c, w in ((10, ORANGE, 0.55), (100, BLUE, 0.18)):
    n = np.arange(0, N + 1); sd = sqrt(N) / 2
    p = stats.binom.pmf(n, N, 0.5) * sd
    a.bar((n - N / 2) / sd, p, width=w, color=c, alpha=0.85, label=f"$N={N}$ spins")
a.set_xlim(-4, 4); a.set_xlabel(r"$(n_\uparrow-N/2)/\sigma$, $\sigma=\sqrt{N}/2$"); a.set_ylabel(r"$\sigma\,P(n_\uparrow)$")
a.legend(fontsize=8.5); a.set_title("A  sums of independent variables become Gaussian", fontsize=10)

# B  Stirling
b = axes[0, 1]
N = np.unique(np.logspace(0, 3, 60).astype(int))
ex = gammaln(N + 1)
crude = N * np.log(N) - N
ref = crude + 0.5 * np.log(2 * pi * N)
b.loglog(N, np.abs(ex - crude) / ex, color=ORANGE, label=r"$N\ln N-N$")
b.loglog(N, np.abs(ex - ref) / ex, color=BLUE, label=r"$+\frac{1}{2}\ln 2\pi N$")
for nn in (10, 100):
    e = gammaln(nn + 1); b.plot([nn], [abs(e - (nn * log(nn) - nn)) / e], "o", color=ORANGE, ms=4.5)
b.annotate("$N=100$: 0.89 %", (100, 3.2224 / 363.739), xytext=(150, 0.03), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_xlabel("$N$"); b.set_ylabel(r"relative error of $\ln N!$"); b.legend(fontsize=8.6, loc="lower left")
b.set_title("B  Stirling: the error of $\\ln N!$ per particle vanishes", fontsize=10)

# C  Cauchy vs Gaussian running means
c = axes[1, 0]
rng = np.random.default_rng(3)
M = 3000
for dist, col, lab in ((rng.standard_normal(M), AQUA, "Gaussian samples"), (rng.standard_cauchy(M), ORANGE, "Cauchy samples")):
    c.plot(np.arange(1, M + 1), np.cumsum(dist) / np.arange(1, M + 1), color=col, lw=1.3, label=lab)
c.set_xscale("log"); c.set_ylim(-3, 3); c.axhline(0, color=MUTED, lw=0.7)
c.set_xlabel("number of samples $N$"); c.set_ylabel(r"running mean $\bar x_N$"); c.legend(fontsize=8.6, loc="upper right")
c.set_title("C  no finite variance, no central limit theorem", fontsize=10)

# D  rate function
d = axes[1, 1]
m = np.linspace(0.02, 0.98, 400)
I = np.log(2) + m * np.log(m) + (1 - m) * np.log(1 - m)
d.plot(m, I, color=INK, lw=1.6, label=r"$I(m)=\ln2+m\ln m+(1-m)\ln(1-m)$")
d.plot(m, 2 * (m - 0.5) ** 2, color=MUTED, ls="--", lw=1.2, label=r"Gaussian: $2(m-\frac{1}{2})^2$")
for N, col in ((20, ORANGE), (100, BLUE), (1000, AQUA)):
    k = np.arange(1, N)
    mm = k / N
    d.plot(mm, -stats.binom.logpmf(k, N, 0.5) / N, ".", color=col, ms=4, label=f"$-\\frac{{1}}{{N}}\\ln P$, $N={N}$")
d.set_xlabel(r"fraction of heads $m$"); d.set_ylabel("rate"); d.set_ylim(0, 0.8); d.legend(fontsize=8.0, loc="upper center")
d.set_title("D  large deviations: $P\\sim e^{-NI(m)}$", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm_numbers.py: $P(n=50)=0.07959$ (Gaussian 0.07979); $\\ln100!=363.739$; $P(\\geq60\\%$ of 100)$=0.0284$, of 1000: $1.36\\times10^{-10}$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm01_limits")
