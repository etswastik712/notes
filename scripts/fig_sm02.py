"""SM02 - Liouville flow of a phase-space blob (pendulum), two Einstein solids exchanging energy, two-level S(E) and temperature."""
from figlib import *
from math import log, pi, sqrt
from scipy.special import gammaln
from scipy.integrate import solve_ivp

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.1))

# A  pendulum blob
a = axes[0]
def rhs(t, y): return [y[1], -np.sin(y[0])]
th = np.linspace(0, 2 * pi, 500, endpoint=False)
blob0 = np.c_[1.6 + 0.35 * np.cos(th), 0.35 * np.sin(th)]
def area(poly): x, y = poly[:, 0], poly[:, 1]; return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))
cols = {0: BLUE, 5: AQUA, 12: ORANGE, 30: VIOLET}
for tf, col in cols.items():
    pts = np.array([solve_ivp(rhs, [0, tf], b, rtol=1e-11, atol=1e-12).y[:, -1] if tf else b for b in blob0])
    a.fill(pts[:, 0], pts[:, 1], color=col, alpha=0.55, lw=0.6, label=f"$t={tf}$,  area {area(pts):.4f}")
# separatrix
x = np.linspace(-pi, pi, 400); a.plot(x, 2 * np.cos(x / 2), color=MUTED, lw=0.8, ls=":"); a.plot(x, -2 * np.cos(x / 2), color=MUTED, lw=0.8, ls=":")
a.set_xlim(-pi, pi); a.set_ylim(-2.3, 2.3); a.set_xlabel(r"angle $q$"); a.set_ylabel(r"momentum $p$"); a.legend(fontsize=7.6, loc="lower left")
a.set_title("A  Liouville: the blob stretches, its area does not", fontsize=10)

# B  two Einstein solids
b = axes[1]
NA_, NB_, q = 300, 200, 100
def lnW(Nn, qq): return gammaln(qq + Nn) - gammaln(qq + 1) - gammaln(Nn)
qa = np.arange(0, q + 1)
lw = np.array([lnW(NA_, k) + lnW(NB_, q - k) for k in qa]); p = np.exp(lw - lw.max()); p /= p.sum()
b.bar(qa, p, color=BLUE, width=0.85, alpha=0.9)
s = sqrt(28.8); b.plot(qa, np.exp(-(qa - 60) ** 2 / (2 * 28.8)) / sqrt(2 * pi * 28.8), color=ORANGE, lw=1.6, label=r"Gaussian, $\sigma=5.37$")
b.set_xlabel(r"energy quanta in solid A, $q_A$"); b.set_ylabel(r"probability $P(q_A)$"); b.legend(fontsize=8.4)
b.annotate("most probable $q_A=60$\n$=q\\,N_A/(N_A+N_B)$", (60, p.max()), xytext=(68, 0.058), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.annotate(r"$P(q_A=0)=3\times10^{-35}$", (1, 0.0003), xytext=(4, 0.012), fontsize=8.2, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_title("B  two Einstein solids, $N_A=300$, $N_B=200$, $q=100$", fontsize=10)

# C  two-level system
c = axes[2]
x = np.linspace(0.005, 0.995, 600)
S = -(x * np.log(x) + (1 - x) * np.log(1 - x))
beta = np.log((1 - x) / x)
c.plot(x, S, color=BLUE, label=r"$S/Nk_B$")
c2 = c.twinx(); c2.spines["right"].set_visible(True); c2.grid(False)
c2.plot(x, np.clip(beta, -4, 4), color=ORANGE, label=r"$\beta\varepsilon=\varepsilon/k_BT$")
c2.axhline(0, color=MUTED, lw=0.7)
c.set_xlabel(r"$E/N\varepsilon$ (fraction in the upper level)"); c.set_ylabel(r"$S/Nk_B$", color=BLUE); c2.set_ylabel(r"$\beta\varepsilon$", color=ORANGE); c2.set_ylim(-4, 4)
c.annotate("$T=+\\infty$ then $-\\infty$\nat the entropy maximum", (0.5, np.log(2)), xytext=(0.08, 0.12), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
c.text(0.86, 0.50, "$T<0$: hotter\nthan $T=+\\infty$", fontsize=8.4, color=ORANGE, ha="center")
c.set_title("C  $S(E)$ turns over: negative temperature", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "Computed in scripts/sm_numbers.py: pendulum blob area 0.3848 → 0.3848 over $t=0\\ldots32$; Einstein solids: $\\langle q_A\\rangle=60$, $\\sigma=5.36$; $x=0.25$: $S/Nk_B=0.5623$, $k_BT/\\varepsilon=0.910$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm02_phasespace")
