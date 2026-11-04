"""TH09 figure A: macrostates are sharp - binomial widths, two Einstein solids, entropy, ideal-gas fluctuations."""
from figlib import *
from math import lgamma, log, sqrt
from scipy import stats
def lnC(n, k): return lgamma(n + 1) - lgamma(k + 1) - lgamma(n - k + 1)
fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.8))

a = axes[0, 0]
for N, col in ((10, AQUA), (100, BLUE), (1000, ORANGE), (10000, VIOLET)):
    k = np.arange(N + 1); p = stats.binom.pmf(k, N, 0.5)
    a.plot(k / N, p / p.max(), color=col, label=f"$N={N}$", lw=1.8)
a.set_xlabel("fraction of heads (or spins up, or molecules in the left half)"); a.set_ylabel("macrostate probability / its maximum"); a.set_xlim(0.1, 0.9); a.legend(fontsize=8.5)
a.set_title("A  The macrostate sharpens as $1/\\sqrt{N}$", fontsize=10)

b = axes[0, 1]
NA_, NB_, q = 300, 200, 100
qa = np.arange(q + 1); lnOm = np.array([lnC(x + NA_ - 1, x) + lnC(q - x + NB_ - 1, q - x) for x in qa]); lnTot = lnC(q + NA_ + NB_ - 1, q)
p = np.exp(lnOm - lnTot)
b.bar(qa, p, color=BLUE, width=0.9)
g = np.exp(-(qa - 60) ** 2 / (2 * 5.361 ** 2)) / (5.361 * sqrt(2 * np.pi)); b.plot(qa, g, color=ORANGE, lw=1.4, label="Gaussian, $\\sigma=5.36$")
b.annotate("$P(q_A=100)=1.8\\times10^{-20}$\n(all quanta in A)", (100, 0.0002), (73, 0.035), fontsize=8.5, arrowprops=dict(arrowstyle="->", color=MUTED))
b.set_xlabel("$q_A$: quanta in solid A (300 oscillators; B has 200; $q=100$)"); b.set_ylabel("$P(q_A)$"); b.legend(fontsize=8.5, loc="upper left")
b.set_title("B  Two Einstein solids in contact", fontsize=10)

c = axes[1, 0]
c.plot(qa, lnOm, color=BLUE, lw=2)
c.plot([60], [lnOm[60]], "o", color=ORANGE); c.plot([100], [lnOm[100]], "o", color=MUTED); c.plot([80], [lnOm[80]], "o", color=AQUA)
c.annotate("equilibrium: $S/k=264.4$", (60, lnOm[60]), (8, 262.5), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
c.annotate("$q_A=80$: 256.9", (80, lnOm[80]), (82, 238), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
c.annotate("all in A: 221.6", (100, lnOm[100]), (75, 223), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
c.set_ylim(215, 270); c.set_xlabel("$q_A$"); c.set_ylabel("$S_{\\rm tot}/k_B=\\ln\\Omega_A\\Omega_B$")
c.set_title("C  Entropy of the macrostate: a peak, not a plateau", fontsize=10)

d = axes[1, 1]
from scipy.special import erf
Ns = np.logspace(1, 4.3, 200)
for tol, col in ((0.01, ORANGE), (0.05, BLUE)):
    d.semilogx(Ns, erf(tol * np.sqrt(2 * Ns)), color=col, label=f"within $\\pm{tol:g}$ of one half (Gaussian limit)")
    for N in (100, 1000, 10000):
        pr = stats.binom.cdf(int(np.floor((0.5 + tol) * N)), N, 0.5) - stats.binom.cdf(int(np.ceil((0.5 - tol) * N)) - 1, N, 0.5)
        d.plot([N], [pr], "o", color=col, ms=5)
d.axhline(1.0, color=MUTED, lw=0.8, ls=":")
d.set_xlabel("number of molecules $N$"); d.set_ylabel("probability of the macrostate"); d.legend(fontsize=8.2, loc="lower right")
d.text(11, 0.72, "dots: exact binomial. $N=100$: all in one half\nhas probability $2^{-N}=10^{-30}$; for 1 mol it\nis $10^{-1.8\\times10^{23}}$", fontsize=8.4)
d.set_title("D  A gas finds its equal-density macrostate", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/th09_numbers.py: $\\sigma_{q_A}=5.361$, $P_{\\max}=0.0741$; $N_A=N_B$, $q=2N$: $\\sigma/\\langle q_A\\rangle=0.309,\\ 0.0998,\\ 0.0316,\\ 0.0100$ for $N=10,\\ 10^2,\\ 10^3,\\ 10^4$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th09a_macrostates")
