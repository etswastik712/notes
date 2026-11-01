"""SM05 - grand canonical ensemble: Poisson numbers, Langmuir isotherm, Saha ionisation, one-mode FD/BE/MB occupations."""
from figlib import *
from math import pi, sqrt, exp, log
from scipy import stats

kB = 1.380649e-23; h = 6.62607015e-34; u = 1.66053906660e-27; me = 9.1093837015e-31; eV = 1.602176634e-19
fig, axes = plt.subplots(2, 2, figsize=(10.6, 7.6))

a = axes[0, 0]
for Nm, col in ((3, ORANGE), (10, BLUE), (30, AQUA)):
    k = np.arange(0, 60)
    a.plot(k, stats.poisson.pmf(k, Nm), "o", color=col, ms=3.8, label=fr"$\langle N\rangle={Nm}$")
    kk = np.linspace(0, 60, 400)
    a.plot(kk, stats.norm.pdf(kk, Nm, sqrt(Nm)), color=col, lw=1.0, ls="--")
a.set_xlabel("number of molecules $N$ in the open region"); a.set_ylabel("$P(N)$"); a.legend(fontsize=8.6)
a.set_title("A  ideal gas, grand canonical: Poisson (dashed: Gaussian)", fontsize=10)

b = axes[0, 1]
lam = lambda m, T: h / sqrt(2 * pi * m * kB * T)
m = 28.0134 * u
Pp = np.logspace(-3, 9, 400)
for T, col in ((300, BLUE), (400, AQUA), (600, ORANGE)):
    P0 = kB * T / lam(m, T) ** 3 * exp(-0.5 * eV / (kB * T))
    b.semilogx(Pp, Pp / (Pp + P0), color=col, label=f"$T={T}$ K, $P_0={P0:.1e}$ Pa")
b.axvline(1e5, color=MUTED, ls=":", lw=1); b.text(1.3e5, 0.05, "1 bar", fontsize=8.2, color=MUTED)
b.set_xlabel("gas pressure $P$ (Pa)"); b.set_ylabel(r"coverage $\theta=P/(P+P_0)$"); b.legend(fontsize=8.0, loc="center left")
b.set_title("B  Langmuir isotherm, binding 0.5 eV", fontsize=10)

c = axes[1, 0]
def K(T): return (2 * pi * me * kB * T / h ** 2) ** 1.5 * np.exp(-13.605693 * eV / (kB * T))
def frac(T, n): return 2 / (1 + np.sqrt(1 + 4 * n / K(T)))
T = np.linspace(2500, 20000, 600)
for n, col, lab in ((1e23, BLUE, r"$n=10^{23}$ m$^{-3}$"), (1e20, AQUA, r"$n=10^{20}$"), (1e10, ORANGE, r"$n=10^{10}$")):
    c.plot(T, frac(T, n), color=col, label=lab)
eta = 6.1e-10; zeta3 = 1.2020569; hb = 1.054571817e-34; cc = 2.99792458e8
Tc = np.linspace(2800, 4800, 300)
ng = 2 * zeta3 / pi ** 2 * (kB * Tc / (hb * cc)) ** 3
c.plot(Tc, frac(Tc, eta * ng), color=VIOLET, ls="--", label="early Universe, $n=\\eta n_\\gamma(T)$")
c.axvline(5800, color=MUTED, ls=":", lw=1); c.text(5900, 0.55, "solar\nphotosphere\n5800 K", fontsize=8.0, color=MUTED)
c.set_xlabel("temperature (K)"); c.set_ylabel("ionised fraction of hydrogen"); c.legend(fontsize=8.0, loc="lower right")
c.set_title("C  Saha: half-ionised at $kT\\approx0.03$–$0.09\\,I$", fontsize=10)

d = axes[1, 1]
x = np.linspace(-1.5, 6, 500)
xs = x[x > 0.05]
d.plot(x, 1 / (np.exp(x) + 1), color=BLUE, label="Fermi–Dirac $1/(e^x+1)$")
d.plot(xs, 1 / (np.exp(xs) - 1), color=ORANGE, label="Bose–Einstein $1/(e^x-1)$")
d.plot(x, np.exp(-x), color=INK, ls="--", lw=1.2, label="Boltzmann $e^{-x}$")
d.set_ylim(0, 2.2); d.set_xlabel(r"$x=(\varepsilon-\mu)/k_BT$"); d.set_ylabel(r"mean occupation $\langle n\rangle$"); d.legend(fontsize=8.2, loc="upper right")
d.set_title("D  one mode in the grand canonical ensemble", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm05_numbers.py: Saha prefactor $1.07\\times10^{27}$ m$^{-3}$ and $e^{-I/kT}=1.5\\times10^{-12}$ at 5800 K; half-ionised at 9000 K ($n=10^{20}$); Saha half-recombination of the Universe at 3760 K ($z\\approx1380$).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm05_grandcanonical")
