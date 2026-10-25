"""EE03 - stability map of the Hassell model N_{t+1} = lam N (1 + a N)^-beta.
Fixed point: 1 + aN* = lam^(1/beta);  f'(N*) = 1 - beta (1 - lam^(-1/beta)).
monotone damping: 0 <= f' < 1  <=>  beta(1 - lam^(-1/beta)) <= 1 ;  unstable: f' <= -1  <=>  beta(1 - lam^(-1/beta)) >= 2."""
from figlib import *

lam = np.logspace(0.0, 2.0, 400)
beta = np.linspace(0.2, 8, 400)
L, B = np.meshgrid(lam, beta)
Q = B * (1 - L ** (-1 / B))
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.contourf(L, B, Q, levels=[0, 1, 2, 100], colors=["#cfe6d9", "#f8e0b0", "#f4c3bf"], alpha=0.95)
ax.contour(L, B, Q, levels=[1, 2], colors=[MUTED, INK], linewidths=1.2)
ax.set_xscale("log")
ax.set_xlabel(r"growth parameter  $\lambda$ (log scale)")
ax.set_ylabel(r"density-dependence exponent  $\beta$")
ax.text(1.2, 0.45, "monotone damping\n(0 ≤ f′ < 1)", fontsize=9, color=INK)
ax.text(3.7, 4.3, "oscillatory damping\n(−1 < f′ < 0)", fontsize=9, color=INK)
ax.text(14, 6.4, "unstable: cycles,\nchaos (f′ ≤ −1)", fontsize=9, color=INK)
ax.text(16, 0.55, "β ≤ 1: always monotone", fontsize=8, color=MUTED)
ax.set_title("Where does a real population sit on the Hassell map?", fontsize=10.5)
ax.set_xlim(1, 100)
save(fig, "fig_ee03_hassell_map")
