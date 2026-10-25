"""EE05 - Lotka-Volterra predator-prey (slides 5-8): A phase portrait of the basic model (closed orbits), B the time series
(prey peak first, predator peak later), C with logistic prey: a spiral into a stable point.  r=1, p=0.02, a=0.5, m=0.5 (illustrative).
"""
from scipy.integrate import solve_ivp

from figlib import *

r, p, a, m, K = 1.0, 0.02, 0.5, 0.5, 200.0
Hs, Ps = m / (a * p), r / p
f = lambda t, y: [r * y[0] - p * y[0] * y[1], a * p * y[0] * y[1] - m * y[1]]
Hs2, Ps2 = m / (a * p), (r / p) * (1 - m / (a * p) / K)
g = lambda t, y: [r * y[0] * (1 - y[0] / K) - p * y[0] * y[1], a * p * y[0] * y[1] - m * y[1]]

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.0))
a1 = axes[0]
for H0 in (60, 70, 80, 100, 120):
    s = solve_ivp(f, (0, 30), [H0, Ps], rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.05)
    a1.plot(s.y[0], s.y[1], color=BLUE, lw=1.2)
a1.axvline(Hs, color=ORANGE, lw=1.8); a1.axhline(Ps, color=BLUE, lw=1.8, ls="--")
a1.plot([Hs], [Ps], "o", color=INK, ms=6, zorder=5)
a1.text(Hs + 2, 6, "predator isocline\n$H^*=m/(ap)=50$", color=ORANGE, fontsize=8.2)
a1.text(125, Ps + 3, "prey isocline $P^*=r/p=50$", color=BLUE, fontsize=8.2, va="bottom")
a1.set_xlim(0, 160); a1.set_ylim(0, 110)
a1.set_xlabel("prey  $H$"); a1.set_ylabel("predators  $P$")
a1.set_title("A  closed orbits around the equilibrium", fontsize=10)

b = axes[1]
s = solve_ivp(f, (0, 30), [Hs * 0.6, Ps], rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.05)
tt = np.linspace(0, 30, 800); H, P = s.sol(tt)
b.plot(tt, H, color=ORANGE, label="prey $H$"); b.plot(tt, P, color=BLUE, label="predators $P$")
b.axhline(Hs, color=ORANGE, lw=0.8, ls=":"); b.axhline(Ps, color=BLUE, lw=0.8, ls=":")
b.set_xlabel("time"); b.set_ylabel("numbers")
b.legend(loc="upper right", fontsize=8.6)
b.set_title("B  neutral cycles: predators lag the prey", fontsize=10)

c = axes[2]
for start in ((30, 30), (150, 20), (60, 90)):
    s2 = solve_ivp(g, (0, 90), start, rtol=1e-10, atol=1e-12, dense_output=True, max_step=0.05)
    c.plot(s2.y[0], s2.y[1], color=BLUE, lw=1.1)
    c.plot([start[0]], [start[1]], "o", color=MUTED, ms=4)
Hg = np.linspace(0, K, 50)
c.plot(Hg, (r / p) * (1 - Hg / K), color=BLUE, lw=1.8, ls="--")
c.axvline(Hs2, color=ORANGE, lw=1.8)
c.plot([Hs2], [Ps2], "o", color=INK, ms=6, zorder=5)
c.text(105, 80, "stable spiral at\n$(50,\\ 37.5)$", fontsize=8.4)
c.set_xlim(0, 210); c.set_ylim(0, 110)
c.set_xlabel("prey  $H$"); c.set_ylabel("predators  $P$")
c.set_title("C  logistic prey ($K=200$): spiral in", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.04, "Illustrative parameters r = 1, p = 0.02, a = 0.5, m = 0.5 (my construction). A, B: dH/dt = rH - pHP, dP/dt = apHP - mP. C: the same with logistic prey growth rH(1 - H/K).",
         ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_ee05_lv")
