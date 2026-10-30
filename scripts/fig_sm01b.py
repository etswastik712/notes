"""SM01 (deepening) - Edgeworth correction, Chernoff bound, maximum-entropy dice."""
from figlib import *
from math import log, sqrt, exp
from scipy import stats, optimize

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.0))
# A  Poisson CDF: Gaussian vs Edgeworth error
a = axes[0]
lam = 10.0; k = np.arange(0, 26)
ex = stats.poisson.cdf(k, lam); z = (k + 0.5 - lam) / sqrt(lam)
G = stats.norm.cdf(z); E = G - (1 / sqrt(lam)) / 6 * (z ** 2 - 1) * stats.norm.pdf(z)
a.plot(k, G - ex, "o-", color=ORANGE, ms=3.6, lw=1.2, label="Gaussian (continuity-corrected)")
a.plot(k, E - ex, "s-", color=BLUE, ms=3.6, lw=1.2, label="+ skewness term (Edgeworth)")
a.axhline(0, color=MUTED, lw=0.7); a.set_xlabel("$k$"); a.set_ylabel(r"approximation $-$ exact $P(X\leq k)$"); a.legend(fontsize=8.2, loc="lower right")
a.set_title("A  Poisson($\\lambda=10$): the skewness term removes 85 %", fontsize=10)

# B  Chernoff bound
b = axes[1]
def I(m): return log(2) + m * log(m) + (1 - m) * log(1 - m)
Ns = np.arange(5, 301, 5)
exact = np.array([stats.binom.sf(int(np.ceil(0.6 * N - 1e-9)) - 1, N, .5) for N in Ns])
b.semilogy(Ns, np.exp(-Ns * I(0.6)), color=BLUE, lw=1.8, label=r"Chernoff bound $e^{-NI(0.6)}$ (rigorous)")
b.semilogy(Ns, exact, "o", color=ORANGE, ms=3.6, label="exact $P(\\bar x\\geq0.6)$")
b.semilogy(Ns, stats.norm.sf((0.6 - 0.5) * np.sqrt(Ns) / 0.5), color=MUTED, ls="--", lw=1.2, label="Gaussian")
b.set_xlabel("$N$ coin flips"); b.set_ylabel("probability"); b.set_ylim(1e-9, 2); b.legend(fontsize=8.2, loc="lower left")
b.set_title("B  the exponent is an upper bound for every $N$", fontsize=10)

# C  Jaynes dice
c = axes[2]
faces = np.arange(1, 7)
def p_for(mean):
    f = lambda l: ((faces * np.exp(-l * faces)).sum() / np.exp(-l * faces).sum()) - mean
    l = optimize.brentq(f, -6, 6) if abs(mean - 3.5) > 1e-9 else 0.0
    w = np.exp(-l * faces); return w / w.sum(), l
w = 0.26
for off, mean, col in ((-w, 2.5, VIOLET), (0, 3.5, MUTED), (w, 4.5, ORANGE)):
    p, l = p_for(mean); S = -(p * np.log(p)).sum()
    c.bar(faces + off, p, width=w * 0.95, color=col, label=f"mean {mean}: $\\lambda={l:+.3f}$, $S={S:.3f}$")
c.axhline(1 / 6, color=INK, lw=0.7, ls=":")
c.set_xlabel("face $i$"); c.set_ylabel("$p_i\\propto e^{-\\lambda i}$"); c.legend(fontsize=8.0, loc="upper center"); c.set_ylim(0, 0.52)
c.set_title("C  maximum entropy for a die with known mean", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Computed in scripts/sm_deepen_numbers.py: Poisson CDF at $k=5$: exact 0.0671, Gaussian 0.0774, Edgeworth 0.0695; $P(\\bar x\\geq0.6)$, $N=100$: 0.0284 vs bound 0.134; mean 4.5: $\\lambda=-0.3710$, $S=1.6136$ vs $\\ln6=1.7918$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm01b_rigour")
