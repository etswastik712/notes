"""EE01 - Holdo et al. (2009) Table 1: delta-AICc of the 14 candidate wildebeest movement models (real values)."""
from figlib import *

models = ["G", "G,T", "G,N", "G,T,N", "I", "I,T", "I,N", "I,T,N", "I,T,Na", "I,T,N,Na", "I,T,N,F", "I,T,N,R", "I,N,F", "I,F"]
ols25 = [226.8, 123.9, 55.3, 44.3, 103.1, 72.4, 25.8, 21.9, 78.0, 26.6, 0.0, 12.2, 2.6, 56.6]
ols10 = [638.6, 548.5, 232.2, 107.5, 283.0, 162.8, 143.9, 0.0, 107.5, 42.7, 0.4, 4.1, 135.4, 144.5]
order = np.argsort(ols25)[::-1]            # worst at top
fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.6), sharey=True)
for ax, vals, ttl in zip(axes, (ols25, ols10), ("25 km lattice (OLS)", "10 km lattice (OLS)")):
    v = np.array(vals)
    y = np.arange(len(models))
    cols = [AQUA if v[i] <= 1.0 else (BLUE if "N" in models[i].split(",") else MUTED) for i in order]
    ax.barh(y, v[order], color=cols, height=0.7)
    for yi, i in zip(y, order):
        if v[i] <= 1.0:
            ax.plot([0.0], [yi], "D", color=AQUA, ms=5, zorder=5)
    ax.set_yticks(y); ax.set_yticklabels([models[i] for i in order], fontsize=8.5)
    ax.set_xscale("symlog", linthresh=10); ax.set_xlim(0, 900)
    ax.set_xticks([0, 5, 10, 30, 100, 300, 800]); ax.set_xticklabels(["0", "5", "10", "30", "100", "300", "800"])
    for yi, i in zip(y, order):
        ax.text(v[i] * 1.12 + 0.5, yi, f"{v[i]:.1f}", va="center", fontsize=7.5, color=INK)
    ax.set_title(ttl, fontsize=10); ax.set_xlabel(r"$\Delta$AICc (symlog axis; 0 = best model)")
    ax.grid(axis="y", visible=False)
fig.suptitle("Holdo et al. 2009, Table 1: which cues explain where the wildebeest are?", fontsize=10.5, y=1.0)
fig.text(0.5, -0.03, "G green biomass, I green-grass intake, T tree cover, N plant nitrogen, Na plant sodium, F flow accumulation (water), R roughness.\n"
         "Green = best fit; blue = other models containing N; grey = models without N. Values copied from Table 1 (p.435).",
         ha="center", fontsize=7.8, color=MUTED)
fig.tight_layout(); save(fig, "fig_ee01_aicc")
