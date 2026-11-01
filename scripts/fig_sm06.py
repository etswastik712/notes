"""SM06 - Szilard engine, Landauer bound against technology, the Earth's radiative entropy budget, and the Page curve of entanglement entropy."""
from figlib import *
from math import log, pi, sqrt
from scipy.special import zeta

kB = 1.380649e-23; sigma = 5.670374419e-8
fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.6))

a = axes[0, 0]
V = np.linspace(0.5, 1.0, 200)
a.plot(V, 1 / V, color=BLUE, lw=2)
a.fill_between(V, 0, 1 / V, color=BLUE, alpha=0.18)
a.set_xlim(0.4, 1.1); a.set_ylim(0, 2.3); a.set_xlabel("volume available to the molecule $V/V_0$"); a.set_ylabel(r"$P=k_BT/V$ (in units of $k_BT/V_0$)")
a.text(0.74, 0.55, r"area $=\int P\,\mathrm{d}V=k_BT\ln2$" + "\n" + r"$=2.87\times10^{-21}$ J at 300 K", fontsize=9, ha="center")
a.axvline(0.5, color=MUTED, lw=0.8, ls=":"); a.axvline(1.0, color=MUTED, lw=0.8, ls=":")
a.text(0.5, 2.15, "partition inserted:\nmolecule on one side\n(1 bit known)", fontsize=8.0, ha="center", va="top", color=MUTED)
a.text(1.0, 2.15, "expanded to the full\nbox: work $k_BT\\ln2$\nextracted", fontsize=8.0, ha="right", va="top", color=MUTED)
a.set_title("A  the Szilard engine: one bit buys $k_BT\\ln2$", fontsize=10)

b = axes[0, 1]
LB = kB * 300 * log(2)
vals = [LB, 1e-17, 1e-15]; labs = ["Landauer bound\n$k_BT\\ln2$ (300 K)", "gate switch today\n(order of magnitude)", "older logic / long wire\n(order of magnitude)"]
cols = [AQUA, BLUE, ORANGE]
b.bar(range(3), vals, color=cols, width=0.55)
b.set_yscale("log"); b.set_xticks(range(3)); b.set_xticklabels(labs, fontsize=8.0); b.set_ylabel("energy per bit operation (J)")
for i, v in enumerate(vals):
    b.text(i, v * 1.6, f"{v:.1e} J\n({v / LB:.0e}$\\times$)" if i else f"{v:.2e} J", ha="center", fontsize=8.2)
b.set_ylim(1e-22, 1e-13)
b.set_title("B  erasing a bit costs $\\geq k_BT\\ln2$", fontsize=10)

c = axes[1, 0]
J = 0.7 * 1361 / 4; Ts = 5772.0; Te = (J / sigma) ** 0.25
s_in, s_out = 4 / 3 * J / Ts, 4 / 3 * J / Te
c.bar([0, 1], [s_in, s_out], color=[ORANGE, BLUE], width=0.5)
c.set_xticks([0, 1]); c.set_xticklabels([f"in: absorbed sunlight\n(source $T_\\odot=5772$ K)", f"out: infrared\n($T_e={Te:.0f}$ K)"], fontsize=8.4)
c.set_ylabel(r"entropy flux (W m$^{-2}$ K$^{-1}$)")
c.text(0, s_in + 0.03, f"{s_in:.3f}", ha="center", fontsize=9); c.text(1, s_out + 0.03, f"{s_out:.3f}", ha="center", fontsize=9)
c.annotate("", xy=(1, 0.95), xytext=(0, 0.95), arrowprops=dict(arrowstyle="->", color=MUTED))
c.text(0.5, 1.0, f"$\\times{Ts / Te:.1f}$ (= photons out per photon in)", ha="center", fontsize=8.6, color=MUTED)
c.set_ylim(0, 1.5); c.text(0.5, 0.45, f"entropy produced\n{s_out - s_in:.2f} W m$^{{-2}}$K$^{{-1}}$\n$=6.1\\times10^{{14}}$ W K$^{{-1}}$", ha="center", fontsize=8.8)
c.set_title("C  the Earth exports entropy as infrared", fontsize=10)

d = axes[1, 1]
rng = np.random.default_rng(4)
nq = 12
ms = np.arange(1, nq)
sim = []
for mA in ms:
    dA, dB = 2 ** mA, 2 ** (nq - mA); out = []
    for _ in range(40):
        psi = rng.standard_normal((dA, dB)) + 1j * rng.standard_normal((dA, dB)); psi /= np.linalg.norm(psi)
        s2 = np.linalg.svd(psi, compute_uv=False) ** 2; s2 = s2[s2 > 1e-14]; out.append(-(s2 * np.log(s2)).sum())
    sim.append(np.mean(out))
page = [log(min(2 ** m, 2 ** (nq - m))) - min(2 ** m, 2 ** (nq - m)) / (2 * max(2 ** m, 2 ** (nq - m))) for m in ms]
mx = [min(m, nq - m) * log(2) for m in ms]
d.plot(ms, mx, color=MUTED, ls="--", lw=1.2, label="maximum $\\min(m,N-m)\\ln2$")
d.plot(ms, page, color=BLUE, lw=1.8, label=r"Page: $\ln d_A-d_A/2d_B$")
d.plot(ms, sim, "o", color=ORANGE, ms=4.5, label="random pure states (40 each)")
d.set_xlabel(r"number of qubits $m$ in subsystem A ($N=12$ in total)"); d.set_ylabel(r"entanglement entropy $\langle S_A\rangle$ (nats)"); d.legend(fontsize=8.2, loc="lower center")
d.set_title("D  a typical pure state is almost maximally entangled", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm06_numbers.py: $k_BT\\ln2=2.87\\times10^{-21}$ J (300 K); $J=238.2$ W m$^{-2}$, $T_e=254.6$ K; entropy flux in 0.055, out 1.247 W m$^{-2}$K$^{-1}$; Page: $N=12,\\ m=6$: simulated 3.659, formula 3.659. CMOS energies are order-of-magnitude recalled values.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm06_entropy")
