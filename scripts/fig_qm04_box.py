"""QM04 - particle in a box: levels and wavefunctions, probability densities vs the classical uniform one, Dx*Dp vs n."""
from figlib import *

L = 1.0
x = np.linspace(0, L, 801)
phi = lambda n: np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.0), gridspec_kw=dict(width_ratios=[1.15, 1, 1]))
a = axes[0]
cols = [BLUE, ORANGE, AQUA, VIOLET]
for n, c in zip(range(1, 5), cols):
    En = n ** 2
    a.plot([0, L], [En, En], color=c, lw=0.9, ls=":")
    a.plot(x, En + 1.5 * phi(n) / np.sqrt(2 / L) * 1.0, color=c, lw=2.0)
    a.text(1.04, En, f"$n={n}$: $E={En}E_1$", va="center", fontsize=8.6)
a.plot([0, 0], [0, 19.5], color=INK, lw=2.2); a.plot([L, L], [0, 19.5], color=INK, lw=2.2)
a.set_xlim(-0.05, 1.5); a.set_ylim(0, 19.5); a.set_xticks([0, 0.5, 1]); a.set_xticklabels(["0", "$a/2$", "$a$"])
a.set_ylabel("$E/E_1$,  $E_1=\\pi^2\\hbar^2/2ma^2$"); a.set_title("A  levels and $\\psi_n$ (drawn on the levels)", fontsize=10)
b = axes[1]
for n, c in zip((1, 2, 5), (BLUE, ORANGE, VIOLET)):
    b.plot(x, phi(n) ** 2, color=c, label=f"$n={n}$")
b.axhline(1 / L, color=INK, lw=1.0, ls="--", label="classical, uniform $1/a$")
b.set_xlabel("$x/a$"); b.set_ylabel(r"$a\,|\psi_n|^2$"); b.legend(fontsize=8.0, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.0))
b.set_ylim(0, 2.35); b.set_title("B  zeros are allowed; average tends to uniform", fontsize=10)
c = axes[2]
n = np.arange(1, 11)
dx = np.sqrt(1 / 12 - 1 / (2 * n ** 2 * np.pi ** 2)); dp = n * np.pi
c.plot(n, dx * dp, "o-", color=BLUE, ms=5, label=r"$\Delta x\,\Delta p/\hbar$")
c.axhline(0.5, color=INK, lw=1.0, ls="--"); c.text(10, 0.62, r"bound $\hbar/2$", ha="right", fontsize=8.4)
c.annotate(f"$n=1$: {dx[0] * dp[0]:.3f}", (1, dx[0] * dp[0]), xytext=(2.3, 1.6), fontsize=8.6, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
c.set_xlabel("$n$"); c.set_ylabel(r"$\Delta x\,\Delta p/\hbar$"); c.set_title("C  the bound is never reached", fontsize=10); c.set_xticks(n)
c.legend(fontsize=8.4, loc="upper left")
fig.tight_layout()
fig.text(0.5, -0.03, "$\\psi_n=\\sqrt{2/a}\\,\\sin(n\\pi x/a)$, $E_n=n^2\\pi^2\\hbar^2/2ma^2$; $\\Delta x=a\\sqrt{1/12-1/2n^2\\pi^2}$, $\\Delta p=n\\pi\\hbar/a$ (exact; scripts/qm_numbers.py).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm04_box")
