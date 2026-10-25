"""QM03 - the same state in three bases, and the spread of a +p/-p superposition on the ring."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(11.6, 3.7), gridspec_kw=dict(width_ratios=[1.0, 1.0, 1.0]))
a = axes[0]
Pa = np.linspace(0, 1, 201)
a.plot(Pa, 2 * np.sqrt(Pa * (1 - Pa)), color=BLUE, label=r"$\Delta p/|p_n|=2|a||b|$")
a.plot(Pa, 2 * Pa - 1, color=ORANGE, label=r"$\langle p\rangle/|p_n|=|a|^2-|b|^2$")
a.axhline(0, color=MUTED, lw=0.6)
a.set_xlabel(r"probability of $+p_n$, $|a|^2$"); a.legend(fontsize=8.4, loc="lower center", bbox_to_anchor=(0.5, 0.0))
a.set_title(r"A  $\Psi=a\psi_n+b\psi_{-n}$ on the ring", fontsize=10)
# two-level state psi = (sqrt3/2, 1/2)
psi = np.array([np.sqrt(3) / 2, 0.5])
bases = {"Z": (np.array([1, 0]), np.array([0, 1])),
         "X": (np.array([1, 1]) / np.sqrt(2), np.array([1, -1]) / np.sqrt(2)),
         "Y": (np.array([1, 1j]) / np.sqrt(2), np.array([1, -1j]) / np.sqrt(2))}
b = axes[1]
for j, (nm, (up, dn)) in enumerate(bases.items()):
    pu = abs(np.vdot(up, psi)) ** 2; pd = abs(np.vdot(dn, psi)) ** 2
    b.bar(j - 0.19, pu, 0.36, color=BLUE, label="outcome $+1$" if j == 0 else None)
    b.bar(j + 0.19, pd, 0.36, color=ORANGE, label="outcome $-1$" if j == 0 else None)
    b.text(j - 0.19, pu + 0.02, f"{pu:.3f}", ha="center", fontsize=8.2); b.text(j + 0.19, pd + 0.02, f"{pd:.3f}", ha="center", fontsize=8.2)
b.set_xticks([0, 1, 2]); b.set_xticklabels(["measure $Z$", "measure $X$", "measure $Y$"]); b.set_ylim(0, 1.12)
b.set_ylabel("probability"); b.legend(fontsize=8.4, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.0)); b.grid(axis="x", visible=False)
b.set_title(r"B  $|\psi\rangle=(\sqrt{3}/2,\ 1/2)$ in three bases", fontsize=10)
c = axes[2]
th = np.linspace(0, np.pi, 400)
c.plot(th / np.pi, np.abs(np.cos(th)) * 1.0, color=BLUE, lw=2.4, label=r"$\Delta X\,\Delta Y$")
c.plot(th / np.pi, np.abs(np.cos(th)), color=INK, lw=1.0, ls="--", label=r"bound $\frac{1}{2}|\langle[X,Y]\rangle|=|\langle Z\rangle|$")
c.plot(th / np.pi, np.abs(np.sin(th) * np.cos(th)), color=ORANGE, lw=2.0, label=r"$\Delta Z\,\Delta X$ (bound $=|\langle Y\rangle|=0$)")
c.set_xlabel(r"mixing angle $\theta/\pi$")
c.set_title(r"C  state $\cos\frac{\theta}{2}|{+z}\rangle+\sin\frac{\theta}{2}|{-z}\rangle$", fontsize=10)
c.set_ylabel("product of spreads"); c.legend(fontsize=8.0, loc="upper center", bbox_to_anchor=(0.5, 1.0)); c.set_ylim(0, 1.45)
fig.tight_layout()
fig.text(0.5, -0.05, "A: $\\Delta p^2=\\langle p^2\\rangle-\\langle p\\rangle^2=4|a|^2|b|^2p_n^2$. B: probabilities from $|\\langle\\text{basis}|\\psi\\rangle|^2$ (scripts/qm_numbers.py, two-level block). "
         "C: for these real states $\\Delta Y=1$ and $\\Delta X=|\\cos\\theta|=|\\langle Z\\rangle|$, so $X,Y$ saturate the bound at every $\\theta$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm03_measurement")
