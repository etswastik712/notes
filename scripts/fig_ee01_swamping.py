"""EE01 - predator swamping: TOY upper bound on losses (my construction; the calving numbers are Hopcraft et al. 2015).

N = 250,000 calves are born over a window of w days (the real wildebeest value is w = 21 d, ~12,000 calves/day).
The whole predator guild can kill at most K calves per day (K = 500, 1000, 2000: ASSUMED, illustrative).
Then the most that can be lost is  f_max = min(1, K w / N).
"""
from figlib import *

N = 250_000
w = np.logspace(np.log10(5), np.log10(365), 300)
Ks = [(500, MUTED), (1000, BLUE), (2000, ORANGE)]

fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.9))
a = axes[0]
a.plot(w, N / w, color=INK)
for K, c in Ks:
    a.axhline(K, color=c, lw=1.4, ls="--")
    a.text(6, K * 1.08, f"K = {K:,} per day", color=c, fontsize=8.5, va="bottom")
a.plot([21], [N / 21], "o", color=RED, ms=6, zorder=5)
a.annotate("wildebeest: 3 weeks,\n~12,000 calves per day", (21, N / 21), xytext=(30, 22000), fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xscale("log"); a.set_yscale("log")
a.set_xlim(5, 365); a.set_ylim(300, 60000)
a.set_xlabel("calving window w (days; log scale)")
a.set_ylabel("calves born per day, N / w")
a.set_title("A  births outrun the predators' kill capacity", fontsize=10)
a.grid(which="minor", visible=False)

b = axes[1]
for K, c in Ks:
    fmax = np.minimum(1.0, K * w / N)
    b.plot(w, 100 * fmax, color=c, label=f"K = {K:,} per day")
    wstar = N / K
    if wstar < 365:
        b.plot([wstar], [100], "o", color=c, ms=4.5)
    i = np.argmin(abs(w - 21))
    b.plot([21], [100 * min(1, K * 21 / N)], "o", color=c, ms=4.5, mfc="white", zorder=5)
b.axvline(21, color=RED, lw=1.0, ls=":")
b.text(23, 92, "real window\n(21 d)", color=RED, fontsize=8.5, va="top")
b.legend(loc="center left", bbox_to_anchor=(0.02, 0.48), fontsize=8.5)
b.set_xscale("log"); b.set_xlim(5, 365); b.set_ylim(0, 105)
b.set_xlabel("calving window w (days; log scale)")
b.set_ylabel("most that predators can take (%)")
b.set_title("B  a short window caps the loss", fontsize=10)
b.grid(which="minor", visible=False)
fig.tight_layout()
fig.text(0.5, -0.04, "Toy bound (my construction): N = 250,000 calves, kill capacity K per day is an assumed illustration. "
         "Open circles: w = 21 d. Filled circles: the window beyond which no cap remains (w* = N/K).",
         ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_ee01_swamping")
for K, _ in Ks:
    print(f"K={K}: cap at 21 d = {100*min(1,K*21/N):.1f}%, at 90 d = {100*min(1,K*90/N):.1f}%, w* = {N/K:.0f} d")
