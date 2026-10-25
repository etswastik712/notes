"""EE03 - the lattice effect: integer-valued Ricker dynamics (K=100, r=3.0) are periodic; cycle lengths grow with K."""
from figlib import *

def ricker(n, r, K):
    return n * np.exp(r * (1 - n / K))

def integer(n, r, K):
    return int(round(ricker(n, r, K))) if n > 0 else 0

K, r = 100, 3.0
x, y = [30.0], [30]
for _ in range(60):
    x.append(ricker(x[-1], r, K)); y.append(integer(y[-1], r, K))
fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.7))
axs[0].plot(range(61), x, "-o", color=RED, ms=2.8, lw=1)
axs[0].set_title("continuous Ricker (r=3.0): never repeats", fontsize=10)
axs[1].plot(range(61), y, "-o", color=BLUE, ms=2.8, lw=1)
axs[1].set_title("integer-valued: locks onto a 10-cycle", fontsize=10)
for ax in axs[:2]:
    ax.set_xlabel("generation t"); ax.set_ylim(0, 260)
axs[0].set_ylabel(r"$N_t$")
Ks = [100, 1000, 10000]
l28 = [14, 36, 82]
l30 = [10, 25, 155]
w = 0.36
xx = np.arange(3)
axs[2].bar(xx - w / 2, l28, w, color=ORANGE, label="r = 2.8")
axs[2].bar(xx + w / 2, l30, w, color=AQUA, label="r = 3.0")
for i in range(3):
    axs[2].annotate(str(l28[i]), (xx[i] - w / 2, l28[i]), ha="center", va="bottom", fontsize=8.5)
    axs[2].annotate(str(l30[i]), (xx[i] + w / 2, l30[i]), ha="center", va="bottom", fontsize=8.5)
axs[2].set_xticks(xx); axs[2].set_xticklabels([f"K={k:,}" for k in Ks])
axs[2].set_ylabel("cycle length reached (generations)")
axs[2].set_title("bigger populations: longer cycles", fontsize=10)
axs[2].legend(fontsize=8.5, loc="upper left"); axs[2].grid(axis="x", visible=False)
fig.tight_layout(); save(fig, "fig_ee03_lattice")
