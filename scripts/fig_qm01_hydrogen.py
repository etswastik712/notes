"""QM01 - the hydrogen scale from the uncertainty argument: E(r) = hbar^2/(2 m r^2) - e^2/(4 pi eps0 r), in atomic units."""
from figlib import *

r = np.linspace(0.12, 5.0, 1500)          # units of a0
HART = 27.2114                            # eV per hartree
E = lambda f: f * 0.5 / r ** 2 - 1 / r    # hartree
fig, axes = plt.subplots(1, 2, figsize=(10.6, 3.9))
a = axes[0]
a.plot(r, 0.5 / r ** 2 * HART, color=ORANGE, label=r"kinetic from confinement, $\hbar^2/2m r^2$")
a.plot(r, -1 / r * HART, color=BLUE, label=r"Coulomb, $-e^2/4\pi\varepsilon_0 r$")
a.plot(r, E(1) * HART, color=INK, lw=2.4, label=r"total, $\Delta p\sim\hbar/r$")
a.plot([1], [-0.5 * HART], "o", color=INK, ms=6)
a.annotate(r"$r=a_0=0.529$ Å" + "\n" + r"$E=-13.6$ eV", (1, -0.5 * HART), xytext=(1.7, -32), fontsize=9, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_ylim(-45, 30); a.set_xlim(0.12, 4); a.axhline(0, color=MUTED, lw=0.6)
a.set_xlabel(r"$r$ in units of $a_0$"); a.set_ylabel("energy (eV)")
a.legend(fontsize=8.2, loc="upper right"); a.set_title("A  squeezing costs kinetic energy as $1/r^2$", fontsize=10)
b = axes[1]
b.plot(r, E(1) * HART, color=INK, lw=2.2, label=r"$\Delta p=\hbar/r$: min $-13.6$ eV at $a_0$")
b.plot(r, E(0.25) * HART, color=VIOLET, lw=2.2, ls="--", label=r"$\Delta p=\hbar/2r$: min $-54.4$ eV at $a_0/4$")
b.plot([1, 0.25], [-13.6057, -54.4228], "o", color=INK, ms=5)
b.set_ylim(-70, 20); b.set_xlim(0.12, 3); b.axhline(0, color=MUTED, lw=0.6)
b.set_xlabel(r"$r$ in units of $a_0$"); b.set_ylabel("energy (eV)")
b.legend(fontsize=8.2, loc="lower right"); b.set_title("B  trust the scaling, not the prefactor", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Both curves minimise $A/r^2-B/r$; the minimum is $-B^2/4A$ at $2A/B$. Computed in scripts/qm_numbers.py (hydrogen block).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm01_hydrogen")
