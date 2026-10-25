"""EE03 - cobweb diagrams for the Ricker map N_{t+1} = N_t exp(r(1 - N_t/K)), K = 100."""
from figlib import *

K = 100.0
f = lambda n, r: n * np.exp(r * (1 - n / K))
fig, axs = plt.subplots(1, 3, figsize=(10.8, 3.8))
for ax, r, title, n0 in zip(axs, (1.3, 2.3, 3.0), ("r = 1.3: spiral into K", "r = 2.3: a 2-cycle", "r = 3.0: chaos"), (20.0, 20.0, 20.0)):
    n = np.linspace(0, 300, 600)
    ax.plot(n, f(n, r), color=BLUE, lw=2)
    ax.plot(n, n, color=MUTED, lw=1, ls="--")
    x = n0
    xs, ys = [x], [0.0]
    for _ in range(40):
        y = f(x, r)
        xs += [x, y]; ys += [y, y]
        x = y
    ax.plot(xs[:60 if r < 3 else 70], ys[:60 if r < 3 else 70], color=ORANGE, lw=1.0, alpha=0.9)
    ax.set_xlim(0, 300); ax.set_ylim(0, 300 if r > 2 else 160 + 0)
    ax.set_xlabel(r"$N_t$"); ax.set_title(title, fontsize=10)
    ax.plot([K], [K], "o", mfc=SURFACE, mec=INK, ms=7, zorder=5)
axs[0].set_ylabel(r"$N_{t+1}$")
axs[0].set_ylim(0, 160)
axs[0].text(150, 20, "slope at K: 1−r = −0.3\n(|slope|<1: stable)", fontsize=8.2)
axs[1].text(165, 235, "slope at K: 1−r = −1.3\n(|slope|>1: unstable)", fontsize=8.2)
fig.tight_layout(); save(fig, "fig_ee03_cobweb")
