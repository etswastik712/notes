"""EE01 - Hopcraft et al. (2015): sizes of the migratory and resident wildebeest populations (numbers quoted in the chapter)."""
from figlib import *

names = ["Serengeti migratory", "Maasai Mara (semi-migratory)", "Ngorongoro Crater", "Western Corridor (Kirawira)", "Loliondo"]
nums = [1.2e6, 40e3, 10e3, 7e3, 5e3]
dens = ["~52 per km2", "~22 per km2", "~40 per km2", "~6 per km2", "~8 per km2"]
fig, ax = plt.subplots(figsize=(7.4, 3.5))
y = np.arange(len(names))[::-1]
cols = [BLUE] + [ORANGE] * 4
ax.barh(y, nums, color=cols, height=0.62)
ax.set_xscale("log"); ax.set_xlim(1e3, 6e6)
ax.set_yticks(y); ax.set_yticklabels(names, fontsize=9)
for yi, n, d in zip(y, nums, dens):
    lab = (f"{n/1e6:.1f} million" if n >= 1e6 else (f"up to {n:,.0f}" if n in (7e3, 5e3) else f"about {n:,.0f}")) + f"   ({d.replace('km2', 'km$^2$')})"
    ax.text(n * 1.18, yi, lab, va="center", fontsize=8.5)
ax.set_xlabel("number of animals (log scale)")
ax.grid(axis="y", visible=False)
ax.set_title("One migratory herd outnumbers all four resident herds by a factor of 30 or more", fontsize=10)
fig.tight_layout(); save(fig, "fig_ee01_abundance")
