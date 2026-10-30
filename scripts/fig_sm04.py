"""SM04 - kinetic theory: Kac ring (exact recurrence), Kac collision model (H-theorem), conductivity from viscosity, the time-scale ladder."""
from figlib import *
import sm04_sims as sims
from math import pi, sqrt, exp, log

fig, axes = plt.subplots(2, 3, figsize=(13.4, 7.6))

# A  Kac ring, large N: decay as (1-2mu)^t
a = axes[0, 0]
N, k = 10000, 1000
m = sims.kac_ring(N, k, 40, seed=3)
t = np.arange(41)
a.semilogy(t, np.abs(m), "o", color=BLUE, ms=3.6, label=r"$|m_t|$, $N=10^4$, $k=10^3$")
a.semilogy(t, 0.8 ** t, color=ORANGE, lw=1.8, label=r"molecular chaos: $(1-2\mu)^t$")
a.axhline(1 / sqrt(N), color=MUTED, ls=":", lw=1); a.text(3, 1.25 / sqrt(N), r"noise $1/\sqrt{N}$", ha="left", fontsize=8.2, color=MUTED)
a.set_ylim(3e-4, 1.5); a.set_xlabel("time step $t$"); a.set_ylabel("colour imbalance $|m_t|$"); a.legend(fontsize=8.2, loc="lower left")
a.set_title("A  Kac ring: fast, exponential relaxation", fontsize=10)

# B  Kac ring, small N: exact recurrence
b = axes[0, 1]
N, k = 400, 80
m = sims.kac_ring(N, k, 820, seed=3)
b.plot(np.arange(821), m, color=AQUA, lw=0.9)
b.axhline(0, color=MUTED, lw=0.6)
for tt in (400, 800):
    b.plot([tt], [1], "o", color=ORANGE, ms=6)
b.annotate("exact return\n$t=N=400$", (400, 1), xytext=(430, 0.55), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.annotate("$t=0$: all white", (0, 1), xytext=(40, 0.82), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_ylim(-0.4, 1.12); b.set_xlabel("time step $t$"); b.set_ylabel("$m_t$ ($N=400$, $k=80$)")
b.set_title("B  the same dynamics is periodic (Zermelo)", fontsize=10)

# C  Kac model histograms
c = axes[0, 2]
res = sims.kac_model()
v = np.linspace(-4.5, 4.5, 400)
c.plot(v, np.exp(-v ** 2 / 2) / sqrt(2 * pi), color=INK, lw=1.3, label="Gaussian (equilibrium)")
cols = {0: ORANGE, 2: VIOLET, 6: AQUA, 15: BLUE}
for tt, col in cols.items():
    h, e = np.histogram(res["snap"][tt], bins=np.arange(-4.5, 4.51, 0.15), density=True)
    c.step(0.5 * (e[1:] + e[:-1]), h, where="mid", color=col, lw=1.3, label=f"$t={tt}$")
c.set_xlabel("velocity $v$ ($\\langle v^2\\rangle=1$)"); c.set_ylabel("$f(v)$"); c.legend(fontsize=8.0, loc="upper left")
c.set_title("C  Kac collision model: uniform to Gaussian", fontsize=10)

# D  H(t) and kurtosis
d = axes[1, 0]
t = np.array(res["t"]); H = np.array(res["H"]); K = np.array(res["kurt"])
d.plot(t, H, "o-", color=BLUE, ms=3.2, lw=1.2, label=r"$H(t)=\int f\ln f$")
d.axhline(-0.5 * log(2 * pi * np.e), color=INK, ls="--", lw=1.0); d.text(20.2, -0.5 * log(2 * pi * np.e) + 0.012, r"$-\frac{1}{2}\ln 2\pi e$", ha="right", fontsize=8.4)
d.set_xlabel("time $t$ (one collision per particle per unit)"); d.set_ylabel("$H$", color=BLUE)
d2 = d.twinx(); d2.spines["right"].set_visible(True); d2.grid(False)
d2.plot(t, K, "s", color=ORANGE, ms=3.4, label="excess kurtosis")
d2.plot(t, -1.2 * np.exp(-t / 4), color=ORANGE, lw=1.4, ls="--", label=r"$-1.2\,e^{-t/4}$")
d2.set_ylabel("excess kurtosis", color=ORANGE)
d.set_title("D  $H$ falls monotonically; the 4th moment decays as $e^{-t/4}$", fontsize=10)
l1, n1 = d.get_legend_handles_labels(); l2, n2 = d2.get_legend_handles_labels(); d.legend(l1 + l2, n1 + n2, fontsize=8.0, loc="center right")

# E  conductivity from viscosity (Eucken), noble gases
e = axes[1, 1]
gas = ["He", "Ne", "Ar", "Kr", "Xe"]
mass = np.array([4.0026, 20.180, 39.948, 83.798, 131.29]) * 1.66053906660e-27
eta = np.array([19.9, 31.8, 22.7, 25.6, 23.2]) * 1e-6
kap = np.array([0.1560, 0.0493, 0.01772, 0.00949, 0.00569])
pred = 15 / 4 * 1.380649e-23 / mass * eta
bgk = 5 / 2 * 1.380649e-23 / mass * eta
x = np.arange(5)
e.bar(x - 0.18, pred / kap, width=0.34, color=BLUE, label=r"$\frac{15}{4}\frac{k_B}{m}\eta$ (Chapman–Enskog)")
e.bar(x + 0.18, bgk / kap, width=0.34, color=ORANGE, label=r"$\frac{5}{2}\frac{k_B}{m}\eta$ (single-time)")
e.axhline(1, color=INK, lw=1.0)
e.set_xticks(x); e.set_xticklabels(gas); e.set_ylim(0, 1.15); e.set_ylabel(r"predicted $\kappa$ / measured $\kappa$")
e.legend(fontsize=8.0, loc="lower left")
e.set_title("E  $\\kappa$ from $\\eta$ at 300 K: 0.97–1.00 vs 0.67", fontsize=10)

# F  time-scale ladder
f = axes[1, 2]
items = [(7.8e-13, "collision $\\tau_c=d/\\bar v$"), (1.4e-10, "free flight $\\tau_\\times=\\lambda/\\bar v$"), (2.1e-6, "cross 1 mm, $\\tau_U$"),
         (2.1e-3, "cross 1 m"), (6.4, "shear diffuses 1 cm")]
for i, (tt, lab) in enumerate(items):
    f.plot([tt, tt], [0, 1], color=BLUE, lw=2.2); f.plot([tt], [1], "o", color=BLUE, ms=6)
    f.text(tt, 1.04 + 0.13 * (i % 2), lab, rotation=0, ha="center", fontsize=7.6, va="bottom")
f.set_xscale("log"); f.set_xlim(1e-13, 1e2); f.set_ylim(0, 1.6); f.set_yticks([]); f.grid(False, axis="y")
f.set_xlabel("time (s) for air at 300 K, 1 atm"); f.spines["left"].set_visible(False)
f.annotate("", xy=(1.4e-10, 0.5), xytext=(7.8e-13, 0.5), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.3))
f.text(1.2e-11, 0.31, r"$\tau_c/\tau_\times=5.5\times10^{-3}\approx nd^3$", ha="center", fontsize=8.0, color=ORANGE)
f.annotate("", xy=(2.1e-3, 0.22), xytext=(1.4e-10, 0.22), arrowprops=dict(arrowstyle="<->", color=AQUA, lw=1.3))
f.text(5e-7, 0.1, "hydrodynamics lives in this gap", ha="center", fontsize=8.0, color=AQUA)
f.set_title("F  the ladder of scales behind the Boltzmann equation", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/sm04_numbers.py and sm04_sims.py. Measured $\\eta,\\kappa$ are recalled CRC/NIST values at 300 K (inputs, good to ~1 %). Kac model: $N=10^5$ particles; histogram estimate of $H$ good to ~0.02.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_sm04_kinetic")
