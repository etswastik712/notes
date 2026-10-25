"""QM02 - the same equation, different boundary conditions: continuous E(k) on a line, discrete levels on a ring."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.9), gridspec_kw=dict(width_ratios=[1.1, 0.85, 1.15]))
a = axes[0]
k = np.linspace(-4.6, 4.6, 400)
a.plot(k, k ** 2, color=MUTED, lw=1.6, label=r"line: any $k$, $E\propto k^2$")
n = np.arange(-4, 5)
a.plot(n, n ** 2, "o", color=BLUE, ms=7, label=r"ring: $k_n=2\pi n/L$ only")
a.set_xlabel(r"$k\,L/2\pi$"); a.set_ylabel(r"$E$ in units of $E_1=2\pi^2\hbar^2/mL^2$")
a.legend(fontsize=8.4, loc="upper center"); a.set_title(r"A  $\psi(x+L)=\psi(x)$ selects points", fontsize=10)
a.set_xlim(-4.7, 4.7); a.set_ylim(-1, 24)
b = axes[1]
for m in range(0, 5):
    xs = [(-0.5, 0.5)] if m == 0 else [(-1.45, -0.55), (0.55, 1.45)]
    for x0, x1 in xs:
        b.plot([x0, x1], [m ** 2, m ** 2], color=BLUE, lw=3)
    b.text(1.55, m ** 2, f"$n=\\pm{m}$" if m else "$n=0$", va="center", fontsize=8.6)
b.set_xlim(-1.6, 2.5); b.set_xticks([]); b.set_ylabel("$E_n/E_1=n^2$"); b.grid(False)
b.set_title("B  levels, doubly degenerate", fontsize=10)
c = axes[2]
x = np.linspace(0, 1, 500)
c.plot(x, np.ones_like(x), color=BLUE, label=r"$\psi_n$: uniform, any $n$")
c.plot(x, 2 * np.cos(2 * np.pi * 2 * x) ** 2, color=ORANGE, label=r"$\sqrt{2/L}\cos k_2x$: 2 maxima")
c.plot(x, 2 * np.sin(2 * np.pi * 2 * x) ** 2, color=AQUA, label=r"$\sqrt{2/L}\sin k_2x$: shifted")
c.set_xlabel("$x/L$"); c.set_ylabel(r"$L\,|\psi|^2$"); c.legend(fontsize=8.0, loc="upper center", bbox_to_anchor=(0.5, 1.02), ncol=1)
c.set_ylim(0, 3.1); c.set_title("C  same energy, different states ($n=\\pm2$)", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "$E_n=\\hbar^2k_n^2/2m$ with $k_n=2\\pi n/L$; the equation is the free-particle equation throughout, only the condition on $\\psi$ changed.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm02_ring")
