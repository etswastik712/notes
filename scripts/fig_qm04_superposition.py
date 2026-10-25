"""QM04 - Tutorial I: (psi1+psi2)/sqrt2 in a box sloshes with period 2 pi hbar/(3 E1): |Psi|^2 at the four requested times, and <x>(t)."""
from figlib import *

x = np.linspace(0, 1, 800)
p1 = np.sqrt(2) * np.sin(np.pi * x); p2 = np.sqrt(2) * np.sin(2 * np.pi * x)
dens = lambda ph: 0.5 * (p1 ** 2 + p2 ** 2) + p1 * p2 * np.cos(ph)         # ph = 3 E1 t / hbar
fig, axes = plt.subplots(1, 3, figsize=(11.8, 3.8), gridspec_kw=dict(width_ratios=[1.2, 1, 1]))
a = axes[0]
for (lab, ph, c, ls) in (("$t=0$", 0, BLUE, "-"), (r"$t=\pi\hbar/2E_1$", 3 * np.pi / 2, MUTED, "--"), (r"$t=\pi\hbar/E_1$", 3 * np.pi, ORANGE, "-"), (r"$t=2\pi\hbar/E_1$", 6 * np.pi, AQUA, ":")):
    a.plot(x, dens(ph), color=c, ls=ls, lw=2.0, label=lab)
a.set_xlabel("$x/a$"); a.set_ylabel(r"$a\,|\Psi(x,t)|^2$"); a.legend(fontsize=8.4, loc="upper center", ncol=2, bbox_to_anchor=(0.5, 1.02))
a.set_ylim(0, 4.1); a.set_title("A  the density at the four times of Tutorial I", fontsize=10)
b = axes[1]
t = np.linspace(0, 2 * np.pi, 400)                                         # t in units of hbar/E1
xm = 0.5 - 16 / (9 * np.pi ** 2) * np.cos(3 * t)
b.plot(t / np.pi, xm, color=BLUE)
for tt, c in ((0, BLUE), (0.5, MUTED), (1, ORANGE), (2, AQUA)):
    b.plot([tt], [0.5 - 16 / (9 * np.pi ** 2) * np.cos(3 * np.pi * tt)], "o", color=c, ms=7)
b.axhline(0.5, color=INK, lw=0.7, ls=":")
b.set_xlabel(r"$t\,E_1/\pi\hbar$"); b.set_ylabel(r"$\langle x\rangle/a$"); b.set_title(r"B  $\langle x\rangle=\frac{a}{2}-0.180\,a\cos(3E_1t/\hbar)$", fontsize=10)
c = axes[2]
E = np.array([1, 4, 9])
for Eo, pr, col in zip(E, [1 / 3] * 3, (BLUE, ORANGE, AQUA)):
    c.bar(Eo, pr, width=0.7, color=col)
c.axvline(14 / 3, color=INK, lw=1.2, ls="--"); c.text(4.8, 0.36, r"$\langle E\rangle=\frac{14}{3}E_1$", fontsize=9, va="bottom")
c.set_xlabel("$E/E_1$"); c.set_ylabel("probability"); c.set_ylim(0, 0.46); c.set_xticks([1, 4, 9])
c.set_title(r"C  energy outcomes of $(\psi_1+\psi_2+\psi_3)/\sqrt{3}$", fontsize=10); c.grid(axis="x", visible=False)
fig.tight_layout()
fig.text(0.5, -0.03, "$|\\Psi|^2=\\frac{1}{2}(\\psi_1^2+\\psi_2^2)+\\psi_1\\psi_2\\cos(3E_1t/\\hbar)$ (real $\\psi_n$): the only time dependence is the relative phase of the two energies.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm04_superposition")
