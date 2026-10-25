"""PR06 - normal approximation to the binomial (continuity correction) and the failure of the law of large numbers for the Cauchy."""
from figlib import *
from scipy import stats

rng = np.random.default_rng(11)
fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.9))
a = axes[0]
k = np.arange(0, 31)
a.bar(k, stats.binom(30, 0.3).pmf(k), 0.8, color=BLUE, alpha=0.8, label="Binomial(30, 0.3)")
xx = np.linspace(0, 30, 400); a.plot(xx, stats.norm.pdf(xx, 9, np.sqrt(30 * 0.3 * 0.7)), color=ORANGE, lw=2, label=r"normal: mean 9, variance 6.3")
a.axvline(10.5, color=INK, lw=0.9, ls="--"); a.text(11.2, 0.105, r"$P(X\leq10)$:" + "\nexact 0.7304\ncontinuity-corrected 0.7250\nuncorrected 0.6548", fontsize=8.2)
a.set_xlim(0, 22); a.set_xlabel("$k$"); a.set_ylabel("pmf / density"); a.legend(fontsize=8.4, loc="upper left"); a.set_title("A  the normal approximation to a binomial", fontsize=10)
b = axes[1]
n = np.arange(1, 5001)
for s, c in ((1, BLUE), (2, AQUA)):
    b.plot(n, np.cumsum(rng.standard_normal(5000)) / n, color=c, lw=1.0, label="mean of normal draws" if s == 1 else None)
for s, c in ((1, ORANGE), (2, RED)):
    b.plot(n, np.cumsum(rng.standard_cauchy(5000)) / n, color=c, lw=1.0, label="mean of Cauchy draws" if s == 1 else None)
b.set_ylim(-6, 6); b.set_xlabel("sample size $n$"); b.set_ylabel("running mean"); b.legend(fontsize=8.4, loc="upper right")
b.set_title("B  the mean exists for the normal but not the Cauchy", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: exact and normal values computed in scripts/pr_numbers.py. B: random simulation (seeded); the Cauchy running mean never settles.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr06_limits")
