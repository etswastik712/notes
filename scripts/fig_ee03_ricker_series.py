"""EE03 - Ricker time series for four values of r (K = 100, N0 = 20)."""
from figlib import *

K = 100.0
f = lambda n, r: n * np.exp(r * (1 - n / K))
fig, axs = plt.subplots(2, 2, figsize=(9.6, 5.6), sharex=True)
cases = [(1.3, "stable point (1 value)", BLUE), (2.3, "2-point cycle", ORANGE), (2.6, "4-point cycle", AQUA), (3.3, "chaos (no repeat)", RED)]
for ax, (r, lab, c) in zip(axs.ravel(), cases):
    x = [20.0]
    for _ in range(40):
        x.append(f(x[-1], r))
    ax.plot(range(41), x, "-o", color=c, ms=3.2, lw=1.2)
    ax.axhline(K, color=MUTED, ls=":", lw=1)
    ax.set_title(f"r = {r}: {lab}", fontsize=10)
    ax.set_ylim(0, 320)
for ax in axs[:, 0]:
    ax.set_ylabel(r"$N_t$")
for ax in axs[1]:
    ax.set_xlabel("generation t")
fig.suptitle("Only r changes (K and N₀ fixed): the qualitative behaviour changes completely", fontsize=11, fontweight="semibold", y=1.0)
fig.tight_layout(); save(fig, "fig_ee03_ricker_series")
