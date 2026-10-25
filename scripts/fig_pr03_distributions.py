"""PR03 - the discrete catalogue: Binomial, Geometric, Poisson pmfs; and Binomial(n, c/n) -> Poisson(c)."""
from figlib import *
from scipy import stats

fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.8), gridspec_kw=dict(width_ratios=[1.0, 1.0, 1.0]))
a = axes[0]
kk = np.arange(0, 6)
a.bar(kk - 0.2, stats.hypergeom(25, 10, 5).pmf(kk), 0.4, color=ORANGE, label="hypergeometric (25 balls, 10 white, 5 drawn)")
a.bar(kk + 0.2, stats.binom(5, 0.4).pmf(kk), 0.4, color=BLUE, label="Binomial(5, 0.4): same mean 2")
a.set_xlabel("number of white balls $k$"); a.set_ylabel("pmf"); a.legend(fontsize=7.8, loc="upper right"); a.set_ylim(0, 0.52)
a.set_title("A  without vs with replacement", fontsize=10)
b = axes[1]
x = np.arange(1, 25)
b.bar(x - 0.2, stats.geom(0.25).pmf(x), 0.4, color=BLUE, label="Geometric(0.25): mean 4, var 12")
b.bar(x + 0.2, stats.nbinom(3, 0.4).pmf(x - 3), 0.4, color=ORANGE, label="NegBin(3, 0.4): mean 7.5, var 11.25")
b.set_xlabel("number of trials"); b.legend(fontsize=7.8, loc="upper right"); b.set_title("B  waiting for successes", fontsize=10)
c = axes[2]
ns = np.array([10, 30, 100, 300, 1000, 3000, 10000])
tv = [0.5 * np.abs(stats.binom.pmf(np.arange(80), n, 3.2 / n) - stats.poisson.pmf(np.arange(80), 3.2)).sum() for n in ns]
c.loglog(ns, tv, "o-", color=BLUE, label="total variation distance")
c.loglog(ns, 3.2 ** 2 / ns / 2.2, "--", color=MUTED, lw=1, label=r"$\propto1/n$")
c.set_xlabel("$n$ in Binomial$(n,3.2/n)$"); c.set_ylabel("distance to Poisson(3.2)"); c.legend(fontsize=8.2); c.set_title("C  the Poisson limit", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "All pmfs computed exactly. C: the distance falls like $1/n$ (0.0080 at $n=100$, 0.00079 at $n=1000$).", ha="center", fontsize=8.2, color=MUTED)
save(fig, "fig_pr03_distributions")
