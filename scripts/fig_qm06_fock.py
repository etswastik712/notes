"""QM06 - number basis, coherent states, photon statistics, thermal oscillator.  Units hbar = m = omega = 1."""
from figlib import *
from math import factorial
from scipy import stats

fig, axes = plt.subplots(2, 2, figsize=(11.0, 8.2))

# A: |<m|x|n>| in the number basis
a = axes[0, 0]
N = 9
M = np.zeros((N, N))
for n in range(N - 1):
    M[n, n + 1] = M[n + 1, n] = np.sqrt((n + 1) / 2)
im = a.imshow(M, cmap="Blues", vmin=0, vmax=2.2, origin="upper")
for i in range(N):
    for j in range(N):
        if M[i, j] > 0:
            a.text(j, i, f"{M[i, j]:.2f}", ha="center", va="center", fontsize=7.4, color=INK if M[i, j] < 1.3 else "white")
a.set_xticks(range(N)); a.set_yticks(range(N)); a.grid(False)
a.set_xlabel("$n$"); a.set_ylabel("$m$")
a.set_title(r"A  $\langle m|\hat x|n\rangle/\sqrt{\hbar/m\omega}$: only $|m-n|=1$", fontsize=10)

# B: phase space - coherent state vs Fock state
b = axes[0, 1]
al = 2.0 * np.exp(1j * 0.4)
th = np.linspace(0, 2 * np.pi, 400)
b.plot(np.sqrt(2) * np.abs(al) * np.cos(th), np.sqrt(2) * np.abs(al) * np.sin(th), color=MUTED, lw=1.0, ls=":", label="classical orbit")
for k, (t, c) in enumerate(zip((0, np.pi / 2, np.pi, 3 * np.pi / 2), (BLUE, ORANGE, AQUA, VIOLET))):
    z = al * np.exp(-1j * t)
    cx, cy = np.sqrt(2) * z.real, np.sqrt(2) * z.imag
    b.add_patch(plt.Circle((cx, cy), 1 / np.sqrt(2), color=c, alpha=0.35))
    b.plot([cx], [cy], "o", color=c, ms=3.5)
    b.text(cx * 1.28, cy * 1.28, rf"$\omega t={['0','\\pi/2','\\pi','3\\pi/2'][k]}$", fontsize=7.8, ha="center", va="center")
r10 = np.sqrt(2 * 10 + 1)
b.plot(r10 * np.cos(th), r10 * np.sin(th), color=RED, lw=1.2, label=r"Fock $n=10$: radius $\sqrt{2n+1}$")
b.set_aspect("equal"); b.set_xlim(-5.4, 5.4); b.set_ylim(-5.4, 5.4)
b.set_xlabel(r"$\langle x\rangle/\sqrt{\hbar/m\omega}$"); b.set_ylabel(r"$\langle p\rangle/\sqrt{m\hbar\omega}$")
b.legend(fontsize=7.6, loc="lower left")
b.set_title(r"B  coherent state: a fixed blob ($\Delta x\Delta p=\hbar/2$) riding the orbit", fontsize=9.5)

# C: photon-number statistics
c = axes[1, 0]
n = np.arange(0, 15)
mean = 4.0
pth = (1 / (1 + mean)) * (mean / (1 + mean)) ** n            # geometric (failures), mean 4
c.bar(n - 0.27, stats.poisson.pmf(n, mean), width=0.27, color=BLUE, label=r"coherent: Poisson, $Q=0$")
c.bar(n, pth, width=0.27, color=ORANGE, label=r"thermal: geometric, $Q=\langle n\rangle$")
c.bar(n + 0.27, (n == 4).astype(float), width=0.27, color=AQUA, label="Fock $n=4$: sharp")
c.set_xlabel("photon (quantum) number $n$"); c.set_ylabel(r"$P(n)$"); c.set_ylim(0, 0.34)
c.legend(fontsize=7.8, loc="upper right")
c.set_title(r"C  same mean $\langle n\rangle=4$, three different statistics", fontsize=10)

# D: Einstein heat capacity
d = axes[1, 1]
T = np.logspace(-1.3, 1.3, 400)
Cv = (1 / T) ** 2 * np.exp(1 / T) / np.expm1(1 / T) ** 2
d.semilogx(T, Cv, color=BLUE)
for nm, nu, col, off in (("CO stretch", 2143.0, ORANGE, (18, 34)), ("CO$_2$ bend", 667.0, AQUA, (22, -38))):
    theta = 1.438777 * nu
    t = 288.0 / theta
    cv = (1 / t) ** 2 * np.exp(1 / t) / np.expm1(1 / t) ** 2
    d.plot([t], [cv], "o", color=col, ms=6)
    d.annotate(f"{nm}\n$\\theta_v={theta:.0f}$ K, 288 K: $C/k={cv:.3f}$", (t, cv), xytext=off, textcoords="offset points", fontsize=8, color=INK, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
d.axhline(1, color=MUTED, lw=0.8, ls=":")
d.set_xlabel(r"$T/\theta_v$, $\theta_v=\hbar\omega/k_B$"); d.set_ylabel(r"$C/k_B$ per oscillator")
d.set_title("D  Einstein heat capacity: frozen below $\\theta_v$, $k_B$ above", fontsize=10)
d.set_ylim(-0.03, 1.12)

fig.tight_layout()
fig.text(0.5, -0.012, "A: $\\sqrt{(n+1)/2}$ from $\\hat x=\\sqrt{\\hbar/2m\\omega}(\\hat a_++\\hat a_-)$. B: coherent state $\\alpha=2e^{0.4i}$. C: Mandel $Q=\\mathrm{Var}\\,n/\\langle n\\rangle-1$. "
         "D: $C/k=x^2e^x/(e^x-1)^2$, $x=\\theta_v/T$ (numbers from scripts/qm_numbers.py).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_qm06_fock")
