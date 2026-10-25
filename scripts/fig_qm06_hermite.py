"""QM06 - Hermite functions: normalised polynomials, why only K = 2n+1 survive (shooting), Fourier invariance.  Units hbar = m = omega = 1."""
from figlib import *
from math import factorial
from scipy.integrate import solve_ivp
from scipy.special import eval_hermite, gammaln

hermfun = lambda n, z: np.pi ** -0.25 * np.exp(-z ** 2 / 2 - 0.5 * (n * np.log(2) + gammaln(n + 1))) * eval_hermite(n, z)

fig, axes = plt.subplots(1, 3, figsize=(12.4, 4.1), gridspec_kw=dict(width_ratios=[1, 1.1, 1]))

# A: normalised Hermite polynomials
a = axes[0]
z = np.linspace(-3.2, 3.2, 800)
cols = (BLUE, ORANGE, AQUA, VIOLET, RED, MUTED)
for n, c in zip(range(6), cols):
    a.plot(z, eval_hermite(n, z) / np.sqrt(2.0 ** n * factorial(n)), color=c, lw=1.8, label=f"$n={n}$")
a.set_ylim(-4.5, 4.5); a.set_xlim(-3.2, 3.2)
a.set_xlabel(r"$\xi=\sqrt{m\omega/\hbar}\,x$"); a.set_ylabel(r"$H_n(\xi)/\sqrt{2^n n!}$")
a.legend(ncol=3, fontsize=8, loc="upper center")
a.set_title("A  polynomials: $n$ real zeros, parity $(-1)^n$", fontsize=10)

# B: shooting - psi(xi = 6) against K = 2E/hbar omega for even and odd starts
b = axes[1]
def shoot(K, par, xe=6.0):
    f = lambda t, y: [y[1], (t ** 2 - K) * y[0]]
    y0 = [1.0, 0.0] if par == 0 else [0.0, 1.0]
    return solve_ivp(f, [0, xe], y0, rtol=1e-9, atol=1e-12).y[0, -1]
Ks = np.linspace(0.2, 10.4, 700)
for par, c, lab in ((0, BLUE, "even start"), (1, ORANGE, "odd start")):
    b.plot(Ks, [shoot(K, par) for K in Ks], color=c, label=lab)
b.set_yscale("symlog", linthresh=1e2)
b.axhline(0, color=MUTED, lw=0.8)
for K in (1, 3, 5, 7, 9):
    b.axvline(K, color=GRID, lw=1.0, zorder=0)
    b.text(K, b.get_ylim()[1] * 0.0 + 4e9, f"{K}", ha="center", fontsize=8, color=MUTED)
b.set_xlabel(r"trial $K=2E/\hbar\omega$"); b.set_ylabel(r"$\psi(\xi=6)$ (symlog)")
b.set_ylim(-1e10, 1e10)
b.legend(fontsize=8, loc="lower right")
b.set_title(r"B  only $K=2n+1$ do not blow up", fontsize=10)

# C: Fourier invariance for n = 3
c_ = axes[2]
x = np.linspace(-6, 6, 1201); dx = x[1] - x[0]
p = np.linspace(-6, 6, 241)
psi3 = hermfun(3, x)
ft = (np.exp(-1j * np.outer(p, x)) @ psi3) * dx / np.sqrt(2 * np.pi)
c_.plot(x, psi3, color=BLUE, lw=2.2, label=r"$\psi_3(x)$")
c_.plot(p, ft.imag, color=ORANGE, lw=1.6, ls="--", label=r"$\mathrm{Im}\,\tilde\psi_3(p)$")
c_.plot(p, ft.real, color=MUTED, lw=1.0, ls=":", label=r"$\mathrm{Re}\,\tilde\psi_3(p)$ (zero)")
c_.set_xlim(-5.2, 5.2); c_.set_xlabel(r"$x/\sqrt{\hbar/m\omega}$  or  $p/\sqrt{m\hbar\omega}$")
c_.legend(fontsize=8, loc="lower right")
c_.set_title(r"C  $\tilde\psi_n(p)=(-i)^n\psi_n(p)$", fontsize=10)
print("max |Re ft| =", float(np.abs(ft.real).max()), " max |Im ft - psi3(p)| =", float(np.abs(ft.imag - hermfun(3, p)).max()))

fig.tight_layout()
fig.text(0.5, -0.03, "B: integrating $\\psi''=(\\xi^2-K)\\psi$ outwards from $\\xi=0$, the value at $\\xi=6$ changes sign at $K=1,5,9$ (even) and $K=3,7$ (odd): "
         "$E=K/2=\\frac{1}{2},\\frac{3}{2},\\frac{5}{2},\\dots$. C: numerical Fourier transform, $n=3$, $(-i)^3=i$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm06_hermite")
