"""SM07 - N2 heat capacity (rotation + vibration), the quantum rotor overshoot, paramagnet isentropes, diamagnetism against paramagnetism."""
from figlib import *
from math import log, cosh, tanh

R = 8.314462618; kB = 1.380649e-23; muB = 9.2740100783e-24
fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.6))
cvib = lambda x: x ** 2 * np.exp(x) / (np.exp(x) - 1) ** 2
th = 3393.5
a = axes[0, 0]
T = np.linspace(100, 3200, 500)
a.plot(T, 3.5 * R + R * cvib(th / T), color=BLUE, label="rotation + harmonic vibration ($\\theta_v=3394$ K)")
a.axhline(3.5 * R, color=MUTED, ls=":", lw=1); a.text(3150, 3.5 * R + 0.35, "$\\frac{7}{2}R$: vibration frozen", ha="right", fontsize=8.2, color=MUTED)
a.axhline(4.5 * R, color=MUTED, ls=":", lw=1); a.text(3150, 4.5 * R + 0.35, "$\\frac{9}{2}R$: equipartition", ha="right", fontsize=8.2, color=MUTED)
jt = {298.15: 29.124, 500: 29.580, 1000: 32.697, 2000: 35.971}
a.plot(list(jt.keys()), list(jt.values()), "o", color=ORANGE, ms=6, label="N$_2$ (JANAF, recalled)")
a.set_xlabel("temperature (K)"); a.set_ylabel(r"$C_p$ (J mol$^{-1}$K$^{-1}$)"); a.legend(fontsize=8.2, loc="lower right"); a.set_ylim(26, 40)
a.set_title("A  N$_2$: equipartition reached only at the highest $T$", fontsize=10)

b = axes[0, 1]
def c_rot(t):
    J = np.arange(0, 200); E = J * (J + 1.0); g = 2 * J + 1
    w = g * np.exp(-E / t); Z = w.sum(); E1 = (w * E).sum() / Z; E2 = (w * E ** 2).sum() / Z
    return (E2 - E1 ** 2) / t ** 2
ts = np.linspace(0.15, 6, 500)
b.plot(ts, [c_rot(t) for t in ts], color=BLUE, label="rigid rotor $C_{\\rm rot}/k_B$")
b.axhline(1, color=INK, ls="--", lw=1); b.text(5.9, 1.015, "equipartition", ha="right", fontsize=8.2)
b.plot([0.8075], [1.0976], "o", color=ORANGE, ms=6); b.annotate("maximum $1.098\\,k_B$\nat $T=0.81\\,\\theta_r$", (0.8075, 1.0976), xytext=(1.6, 0.55), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_xlabel(r"$T/\theta_r$"); b.set_ylabel(r"$C_{\rm rot}/k_B$"); b.set_ylim(0, 1.25)
b.set_title("B  rotation freezes out, and overshoots on the way", fontsize=10)

c = axes[1, 0]
x = np.linspace(0.001, 5, 500)
S = np.log(2 * np.cosh(x)) - x * np.tanh(x)
c.plot(x, S, color=BLUE, lw=2, label=r"$S/Nk_B$ as a function of $x=\mu_BB/k_BT$")
x1 = muB * 1.0 / (kB * 1.0)
c.plot([x1], [log(2 * cosh(x1)) - x1 * tanh(x1)], "o", color=ORANGE, ms=7)
c.annotate("1 T, 1 K: $S/Nk_B=0.510$\n(isothermal magnetisation\nreleased 1.5 J/mol)", (x1, 0.51), xytext=(1.5, 0.62), fontsize=8.2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
c.annotate("adiabatic demagnetisation to 0.01 T:\n$S$ unchanged $\\Rightarrow B/T$ unchanged\n$\\Rightarrow T=0.01$ K", (x1, 0.51), xytext=(1.9, 0.28), fontsize=8.2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
c.set_xlabel(r"$x=\mu_BB/k_BT$ ($=0.672\,B[\mathrm{T}]/T[\mathrm{K}]$)"); c.set_ylabel(r"$S/Nk_B$"); c.set_ylim(0, 0.75); c.legend(fontsize=8.0, loc="lower left")
c.set_title("C  $S$ depends on $B/T$ only: cooling by demagnetisation", fontsize=10)

d = axes[1, 1]
names = ["spin-½ para-\nmagnet, 300 K", "He", "Ne", "Ar", "Kr", "Xe"]
vals = [1.25e-3, 1.9e-6, 7.2e-6, 15.4e-6, 28.0e-6, 43.0e-6]
cols = [ORANGE] + [BLUE] * 5
d.bar(range(6), vals, color=cols, width=0.6); d.set_yscale("log")
d.set_xticks(range(6)); d.set_xticklabels(names, fontsize=8.0); d.set_ylabel(r"$|\chi_{\rm mol}|$ (cm$^3$ mol$^{-1}$)")
d.text(0, vals[0] * 1.5, "+", ha="center", fontsize=12); [d.text(i, vals[i] * 1.5, "$-$", ha="center", fontsize=12) for i in range(1, 6)]
d.text(3.4, 3e-4, "classical orbits: $\\chi=0$\n(Bohr–van Leeuwen)", ha="center", fontsize=8.6, color=MUTED)
d.set_ylim(5e-7, 1e-2)
d.set_title("D  paramagnetism $\\gg$ diamagnetism; classical magnetism: zero", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm07_numbers.py: $C_p(\\mathrm{N_2})=29.11,\\ 29.53,\\ 32.54,\\ 35.68$ J mol$^{-1}$K$^{-1}$ at 298, 500, 1000, 2000 K (recalled JANAF 29.12, 29.58, 32.70, 35.97); $\\chi_{\\rm mol}(\\mathrm{He})=-1.89\\times10^{-6}$ cm$^3$/mol (measured $-1.9\\times10^{-6}$).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm07_equipartition")
