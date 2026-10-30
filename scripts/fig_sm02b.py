"""SM02 (deepening) - cat-map coarse graining and the Maxwell marginal of the hypersphere."""
from figlib import *
from math import log, sqrt, exp, pi
from scipy import special

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.1))
rng = np.random.default_rng(5)
pts = 0.30 + 0.05 * rng.random((200000, 2)); x = pts.copy()
M = 40
def cell_entropy(p, M):
    ix = np.minimum((p[:, 0] * M).astype(int), M - 1); iy = np.minimum((p[:, 1] * M).astype(int), M - 1)
    c = np.bincount(ix * M + iy, minlength=M * M) / len(p); c = c[c > 0]; return -(c * np.log(c)).sum()
snaps = {}; S = []
for t in range(0, 11):
    S.append(cell_entropy(x, M))
    if t in (0, 2, 4, 7): snaps[t] = x[::40].copy()
    x = np.c_[(2 * x[:, 0] + x[:, 1]) % 1.0, (x[:, 0] + x[:, 1]) % 1.0]
a = axes[0]
for (t, p), col in zip(snaps.items(), (BLUE, AQUA, ORANGE, VIOLET)):
    a.plot(p[:, 0], p[:, 1], ".", ms=1.3, color=col, alpha=0.6, label=f"$t={t}$")
a.set_xlim(0, 1); a.set_ylim(0, 1); a.set_aspect("equal"); a.set_xlabel("$x$"); a.set_ylabel("$y$"); a.legend(fontsize=8.0, markerscale=6, loc="upper right")
a.set_title("A  cat map: a square becomes a filament", fontsize=10)
b = axes[1]
t = np.arange(11); lam = log((3 + sqrt(5)) / 2)
b.plot(t, S, "o-", color=BLUE, ms=4, label="coarse-grained $S$ (40×40 cells)")
b.plot(t, np.minimum(log(4) + lam * t, log(1600)), color=ORANGE, lw=1.4, ls="--", label=r"$\ln4+\lambda t$, $\lambda=\ln\frac{3+\sqrt{5}}{2}$")
b.axhline(log(1600), color=MUTED, lw=0.9, ls=":"); b.text(0.2, log(1600) + 0.12, r"$\ln1600$ (all cells)", fontsize=8.2, color=MUTED)
b.axhline(log(4), color=INK, lw=0.7); b.text(10, log(4) - 0.55, "fine-grained entropy: constant", ha="right", fontsize=8.2)
b.set_xlabel("time step"); b.set_ylabel("entropy (nats)"); b.set_ylim(0, 8.3); b.legend(fontsize=8.0, loc="center right")
b.set_title("B  coarse-grained S grows at rate $\lambda$", fontsize=10)
c = axes[2]
z = np.linspace(0, 9, 600)
def ratio(N, z):
    n = 3 * N; out = np.zeros_like(z); ok = z * z < n
    lf = (n - 3) / 2 * np.log(1 - z[ok] ** 2 / n) + special.gammaln(n / 2) - 0.5 * log(pi * n) - special.gammaln((n - 1) / 2)
    out[ok] = np.exp(lf) / (np.exp(-z[ok] ** 2 / 2) / sqrt(2 * pi)); return out
for N, col in ((10, ORANGE), (100, BLUE), (1000, AQUA)):
    c.semilogy(z, np.maximum(ratio(N, z), 1e-4), color=col, label=f"$N={N}$")
c.axhline(1, color=INK, lw=0.8); c.set_ylim(1e-3, 3); c.set_xlabel(r"$z=p_x/\sqrt{mk_BT}$"); c.set_ylabel("exact marginal / Gaussian"); c.legend(fontsize=8.2, loc="lower left")
c.set_title("C  one momentum is Maxwellian", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Computed in scripts/sm_deepen_numbers.py: $S_{\\rm coarse}=1.386, 2.186, 2.963, 3.885, 4.838, 5.799, 6.753, 7.337$ for $t=0\\ldots7$; $N=100$: exact/Gaussian $=0.9975$ (z=0), $1.0042$ (z=2), $0.9746$ (z=3), $0.655$ (z=5).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm02b_ergodic")
