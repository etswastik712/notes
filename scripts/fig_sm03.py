"""SM03 - canonical energy distribution (Gamma), barometric formula against the standard atmosphere, spin-1/2 paramagnet, hydrogen partition-function divergence."""
from figlib import *
from math import pi, sqrt, exp
from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.4))
m_air = 28.9647 * 1.66053906660e-27; g = 9.80665

# A  energy distribution of N ideal-gas atoms in the canonical ensemble: Gamma(3N/2, kT)
a = axes[0, 0]
zz = np.linspace(-4.2, 5.2, 600)
a.plot(zz, stats.norm.pdf(zz), color=INK, lw=1.2, label="Gaussian")
for N, col in ((10, ORANGE), (100, BLUE)):
    k = 1.5 * N; sd = sqrt(k)
    E = k + zz * sd
    ok = E > 0
    a.plot(zz[ok], stats.gamma.pdf(E[ok], k) * sd, color=col, label=f"$N={N}$: Gamma$(3N/2)$")
a.set_xlabel(r"$(E-\langle E\rangle)/\Delta E$"); a.set_ylabel("probability density"); a.legend(fontsize=8.4)
a.set_title("A  canonical energy: skewed for small $N$, Gaussian for large", fontsize=10)

# B  barometric formula
b = axes[0, 1]
z = np.linspace(0, 20e3, 300)
p_std = 101.325 * (1 - 0.0065 * np.minimum(z, 11e3) / 288.15) ** 5.25588
p_std = np.where(z <= 11e3, p_std, 22.632 * np.exp(-(z - 11e3) / 6341.6))
for T, col, lab in ((288.15, BLUE, "isothermal 288 K"), (255.0, AQUA, "isothermal 255 K")):
    H = 1.380649e-23 * T / (m_air * g)
    b.semilogy(z / 1e3, 101.325 * np.exp(-z / H), color=col, label=f"{lab}, $H={H / 1e3:.2f}$ km")
b.semilogy(z / 1e3, p_std, color=ORANGE, label="standard atmosphere (6.5 K/km)")
b.set_xlabel("height (km)"); b.set_ylabel("pressure (kPa)"); b.legend(fontsize=8.2, loc="upper right"); b.set_ylim(4, 120)
b.set_title("B  the Boltzmann factor $e^{-mgz/k_BT}$ in the sky", fontsize=10)

# C  paramagnet
c = axes[1, 0]
x = np.linspace(0, 4, 300)
c.plot(x, np.tanh(x), color=BLUE, label=r"$\tanh x$")
c.plot(x, x, color=MUTED, ls="--", lw=1.1, label=r"Curie: $x$")
c.axhline(1, color=MUTED, lw=0.7, ls=":")
for B, T, pos in ((1, 300, (1.5, 0.08)), (1, 4.2, (1.5, 0.22)), (1, 1.0, (1.5, 0.36))):
    xx = 9.2740100783e-24 * B / (1.380649e-23 * T)
    c.plot([xx], [np.tanh(xx)], "o", color=ORANGE, ms=5)
    c.annotate(f"$B=1$ T, $T={T:g}$ K", (xx, np.tanh(xx)), xytext=pos, fontsize=8.2, va="center", arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
c.set_xlim(0, 4); c.set_ylim(0, 1.15); c.set_xlabel(r"$x=\mu_BB/k_BT$"); c.set_ylabel(r"$M/N\mu_B$"); c.legend(fontsize=8.4, loc="lower right")
c.set_title("C  spin-½ paramagnet: Curie law to saturation", fontsize=10)

# D  hydrogen partition function
d = axes[1, 1]
E1 = 13.605693 * 1.602176634e-19; kB = 1.380649e-23
nmax = np.unique(np.logspace(0, 6, 120).astype(int))
for T, col in ((5800, BLUE), (10000, ORANGE)):
    Zs = []
    n = np.arange(1, nmax[-1] + 1, dtype=float)
    terms = 2 * n ** 2 * np.exp(-(E1 - E1 / n ** 2) / (kB * T))
    cs = np.cumsum(terms)
    d.loglog(nmax, cs[nmax - 1], color=col, label=f"$T={T}$ K")
d.axvline(45, color=MUTED, lw=0.9, ls=":"); d.text(38, 3e3, "plasma at $10^{20}$ m$^{-3}$:\ncutoff $n_{\\max}\\approx45$", fontsize=8.2, color=MUTED, ha="right")
d.axhline(2, color=MUTED, lw=0.7); d.text(1.2, 2.4, "ground-state weight 2", fontsize=8.0, color=MUTED)
d.set_xlabel(r"upper limit $n_{\max}$ of the sum"); d.set_ylabel(r"partial sum $Z(n_{\max})$"); d.legend(fontsize=8.4, loc="upper left")
d.set_title("D  isolated atom: $Z\\to\\infty$ (grows like $n_{\\max}^3$)", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm_numbers.py: $H=k_BT/mg=8.43$ km (288 K), 7.46 km (255 K); $p(5.5\\,\\mathrm{km})/p_0=0.521$ isothermal vs 0.498 standard; $\\tanh x=0.586$ at $x=0.672$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm03_canonical")
