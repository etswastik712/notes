"""PR06 - the central limit theorem for sums of Exp(1): standardised densities and the 1/sqrt(n) distance."""
from figlib import *
from scipy import stats
import math

fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.9))
a = axes[0]
z = np.linspace(-3.5, 3.5, 600)
a.plot(z, stats.norm.pdf(z), color=INK, lw=2.2, label="$N(0,1)$")
for n, c in ((1, ORANGE), (3, VIOLET), (10, AQUA), (30, BLUE)):
    # S_n ~ Gamma(n,1), standardised (S_n - n)/sqrt(n)
    a.plot(z, stats.gamma.pdf(n + z * math.sqrt(n), a=n) * math.sqrt(n), color=c, lw=1.4, label=f"$n={n}$")
a.set_xlim(-3.5, 3.5); a.set_ylim(0, 0.75); a.set_xlabel("standardised sum $(S_n-n)/\\sqrt{n}$"); a.set_ylabel("density"); a.legend(fontsize=8.2, loc="upper right")
a.set_title("A  sums of Exp(1) become normal", fontsize=10)
b = axes[1]
ns = np.array([1, 2, 3, 5, 10, 20, 30, 50, 100, 300, 1000])
xs = np.linspace(-6, 6, 4001)
d = [np.max(np.abs(stats.gamma.cdf(n + xs * math.sqrt(n), a=n) - stats.norm.cdf(xs))) for n in ns]
b.loglog(ns, d, "o-", color=BLUE, label=r"$\sup_x|F_n(x)-\Phi(x)|$ (exact)")
b.loglog(ns, 2 / (6 * np.sqrt(2 * np.pi * ns)), "--", color=ORANGE, label=r"$\frac{\gamma_1}{6\sqrt{2\pi n}}$, $\gamma_1=2$")
b.set_xlabel("number of terms $n$"); b.set_ylabel("largest cdf gap"); b.legend(fontsize=8.4); b.set_title(r"B  the error falls like $1/\sqrt{n}$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Exp(1) has skewness 2; the gap at $n=100$ is 0.0133 and at $n=1000$ it is 0.0042 (scripts/pr_numbers.py).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr06_clt")
