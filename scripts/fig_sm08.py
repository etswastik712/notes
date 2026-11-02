"""SM08 - quantum statistics of identical particles: pair correlation, counting, ideal-gas pressure, two particles in a well."""
from figlib import *
from math import comb, factorial, pi
from scipy import integrate, special

fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.6))
a = axes[0, 0]
r = np.linspace(0, 2, 400)
e = np.exp(-2 * pi * r ** 2)
a.plot(r, 1 + e, color=ORANGE, label="bosons $1+e^{-2\\pi r^2/\\lambda^2}$")
a.plot(r, 1 - e, color=BLUE, label="fermions (same spin) $1-e^{-2\\pi r^2/\\lambda^2}$")
a.axhline(1, color=INK, ls="--", lw=1, label="distinguishable / classical")
a.set_xlabel(r"separation $r/\lambda$"); a.set_ylabel("pair correlation $g(r)$"); a.legend(fontsize=8.2, loc="upper right")
a.set_title("A  exchange hole and bunching in the ideal gas", fontsize=10)

b = axes[0, 1]
gs = np.unique(np.logspace(1, 3.5, 40).astype(int))
for N, col in ((3, AQUA), (10, BLUE)):
    gg = gs[gs >= N]
    cl = np.array([float(g) ** N / factorial(N) for g in gg])
    bos = np.array([float(comb(N + g - 1, N)) for g in gg]) / cl
    fer = np.array([float(comb(g, N)) for g in gg]) / cl
    b.semilogx(gg, bos, color=col, label=f"bosons, $N={N}$"); b.semilogx(gg, fer, color=col, ls="--", label=f"fermions, $N={N}$")
    b.semilogx(gg, 1 + N * (N - 1) / (2 * gg), color=MUTED, ls=":", lw=0.9)
b.axhline(1, color=INK, lw=0.8)
b.set_ylim(0.4, 2.4); b.set_xlabel("number of single-particle states $g$"); b.set_ylabel(r"states / $(g^N/N!)$"); b.legend(fontsize=7.8, loc="upper right", ncol=2)
b.set_title("B  counting: the classical $N!$ is the limit $g\\gg N^2$", fontsize=10)

c = axes[1, 0]
def f(nu, z, sign):
    return integrate.quad(lambda t: t ** (nu - 1) / (np.exp(t) / z + sign), 0, 100, limit=300)[0] / special.gamma(nu)
zs = np.concatenate([np.linspace(0.005, 0.98, 120)])
nfd = np.array([f(1.5, z, 1) for z in zs]); pfd = np.array([f(2.5, z, 1) for z in zs]) / nfd
zb = np.linspace(0.005, 0.985, 120)
nbe = np.array([f(1.5, z, -1) for z in zb]); pbe = np.array([f(2.5, z, -1) for z in zb]) / nbe
c.plot(nfd, pfd, color=BLUE, label="Fermi–Dirac")
c.plot(nbe, pbe, color=ORANGE, label="Bose–Einstein (up to $z=0.985$)")
xx = np.linspace(0, 1.0, 50)
c.plot(xx, 1 + xx / 2 ** 2.5, color=BLUE, ls=":", lw=1); c.plot(xx, 1 - xx / 2 ** 2.5, color=ORANGE, ls=":", lw=1)
c.axhline(1, color=INK, ls="--", lw=1, label="classical")
c.set_xlim(0, 1.0); c.set_ylim(0.75, 1.25); c.set_xlabel(r"$n\lambda^3/g$"); c.set_ylabel(r"$P/nk_BT$"); c.legend(fontsize=8.2, loc="upper left")
c.set_title("C  statistical pressure: Pauli up, Bose down", fontsize=10)

d = axes[1, 1]
vals = [0.0384, 0.1033, 0.1682]
d.bar([0, 1, 2], vals, color=[ORANGE, MUTED, BLUE], width=0.55)
d.set_xticks([0, 1, 2]); d.set_xticklabels(["symmetric\n(bosons)", "distinguishable", "antisymmetric\n(fermions)"], fontsize=8.6)
for i, v in enumerate(vals): d.text(i, v + 0.004, f"{v:.3f}", ha="center", fontsize=9)
d.set_ylabel(r"$\langle(x_1-x_2)^2\rangle/L^2$"); d.set_ylim(0, 0.2)
d.set_title("D  two particles in a box (levels 1 and 2)", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm08_numbers.py: $g(\\lambda/2)=1\\pm0.208$; $N=10$, $g=1000$: bosons/classical 1.0459, fermions 0.9559; $P/nkT=1\\pm n\\lambda^3/(g\\,2^{5/2})$; box: $0.038$, $0.103$, $0.168$ (ratio 4.4).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm08_identical")
