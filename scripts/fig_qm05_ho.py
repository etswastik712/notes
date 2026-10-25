"""QM05 - harmonic oscillator: levels and psi_n; correspondence at n=10; <x>(t) of (psi0+psi1)/sqrt2.  Units hbar=m=omega=1."""
from figlib import *
from math import factorial

def hermite(n, x):
    H = [np.ones_like(x), 2 * x]
    for k in range(1, n):
        H.append(2 * x * H[k] - 2 * k * H[k - 1])
    return H[n]
psi = lambda n, x: (np.pi ** -0.25) / np.sqrt(2.0 ** n * factorial(n)) * hermite(n, x) * np.exp(-x ** 2 / 2)

x = np.linspace(-6.2, 6.2, 1500)
fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.0), gridspec_kw=dict(width_ratios=[1.15, 1, 1]))
a = axes[0]
a.plot(x, 0.5 * x ** 2, color=INK, lw=1.8)
for n, c in zip(range(4), (BLUE, ORANGE, AQUA, VIOLET)):
    E = n + 0.5
    xt = np.sqrt(2 * E)
    m = abs(x) <= xt + 0.9
    a.plot([-xt, xt], [E, E], color=c, lw=0.8, ls=":")
    a.plot(x[m], E + 0.8 * psi(n, x[m]), color=c, lw=2.0)
    a.text(4.35, E, f"$n={n}$: $E={E:g}\\hbar\\omega$", fontsize=8.4, va="center")
a.set_xlim(-4.3, 6.9); a.set_ylim(0, 5.0); a.set_xlabel(r"$x/\sqrt{\hbar/m\omega}$"); a.set_ylabel(r"$E/\hbar\omega$")
a.set_title(r"A  $E_n=(n+\frac{1}{2})\hbar\omega$, equally spaced", fontsize=10)
b = axes[1]
n = 10; xt = np.sqrt(2 * (n + 0.5)); xc = np.linspace(-xt + 1e-3, xt - 1e-3, 800)
b.plot(x, psi(n, x) ** 2, color=BLUE, label=r"$|\psi_{10}|^2$")
b.plot(xc, 1 / (np.pi * np.sqrt(xt ** 2 - xc ** 2)), color=ORANGE, lw=1.6, label="classical $1/\\pi\\sqrt{x_t^2-x^2}$")
b.set_ylim(0, 0.45); b.set_xlim(-6.2, 6.2); b.set_xlabel(r"$x/\sqrt{\hbar/m\omega}$"); b.legend(fontsize=8.4, loc="upper center")
b.set_title("B  $n=10$ looks classical on average", fontsize=10)
c = axes[2]
for tt, col, ls, lab in ((0, BLUE, "-", r"$\omega t=0$"), (np.pi / 2, MUTED, "--", r"$\omega t=\pi/2$ or $3\pi/2$"), (np.pi, ORANGE, "-", r"$\omega t=\pi$")):
    Psi = (psi(0, x) + psi(1, x) * np.exp(-1j * tt)) / np.sqrt(2)           # relative phase e^{-i w t}
    c.plot(x, np.abs(Psi) ** 2, color=col, ls=ls, lw=1.9, label=lab)
c.set_xlim(-4.5, 4.5); c.set_xlabel(r"$x/\sqrt{\hbar/m\omega}$"); c.set_ylim(0, 0.95)
c.legend(fontsize=8.0, ncol=1, loc="upper center", bbox_to_anchor=(0.5, 1.0))
c.set_title(r"C  $(\psi_0+\psi_1)/\sqrt{2}$ sloshes at $\omega$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "$\\psi_n=(\\pi)^{-1/4}(2^nn!)^{-1/2}H_n(x)e^{-x^2/2}$ in units $\\hbar=m=\\omega=1$ (checked against the ladder construction in scripts/qm_numbers.py). "
         "C: $\\langle x\\rangle=\\sqrt{\\hbar/2m\\omega}\\cos\\omega t$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm05_ho")
