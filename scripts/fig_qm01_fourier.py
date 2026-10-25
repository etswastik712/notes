"""QM01 - Fourier synthesis: narrow in k <=> broad in x. A: sin(Kx)/(pi x); B: Gaussian pairs with Dx*Dk = 1/2."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(11.6, 3.7), gridspec_kw=dict(width_ratios=[1.15, 1, 1]))
a = axes[0]
x = np.linspace(-8, 8, 4001)
for K, c in ((1, BLUE), (2, AQUA), (4, ORANGE)):
    a.plot(x, np.sin(K * x) / (np.pi * x), color=c, lw=1.6, label=f"$K={K}$")
a.axhline(0, color=MUTED, lw=0.6)
a.set_xlabel("$x$"); a.set_ylabel(r"$\psi(x)=\sin(Kx)\,/\,\pi x$")
a.legend(fontsize=8.6, loc="upper right"); a.set_title("A  wider band of $k$, narrower peak", fontsize=10)
a.set_ylim(-0.25, 1.35)
x = np.linspace(-9, 9, 2001); k = np.linspace(-4, 4, 2001)
for j, (sig, c) in enumerate(((0.7, BLUE), (1.6, ORANGE))):
    psi2 = np.exp(-x ** 2 / (2 * sig ** 2)) / np.sqrt(2 * np.pi * sig ** 2)
    axes[1].plot(x, psi2, color=c, label=f"$\\sigma={sig}$: $\\Delta x={sig}$")
    phi2 = np.exp(-2 * sig ** 2 * k ** 2); phi2 /= np.trapezoid(phi2, k)
    axes[2].plot(k, phi2, color=c, label=f"$\\Delta k=1/2\\sigma={1 / (2 * sig):.2f}$")
axes[1].set_xlabel("$x$"); axes[1].set_ylabel(r"$|\psi(x)|^2$"); axes[1].legend(fontsize=8.4)
axes[1].set_title(r"B  position: $\Delta x=\sigma$", fontsize=10)
axes[2].set_xlabel("$k$  ($p=\\hbar k$)"); axes[2].set_ylabel(r"$|\tilde\psi(k)|^2$"); axes[2].legend(fontsize=8.4)
axes[2].set_title(r"C  momentum: $\Delta x\,\Delta k=\frac{1}{2}$ for both", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: first zeros at $\\pm\\pi/K$, so $\\Delta x\\,\\Delta k\\approx\\pi$ whatever $K$. B, C: the Gaussian saturates $\\Delta x\\,\\Delta k=1/2$ (checked by numerical integration in scripts/qm_numbers.py).",
         ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm01_fourier")
