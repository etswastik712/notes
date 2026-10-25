"""EE01 - levels of biological organisation and the domain of BI2113 (slides 13-14)."""
from figlib import *
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

levels = ["Biomolecules", "Cell", "Tissue", "Organ", "Organ system", "Individual",
          "Population", "Community", "Ecosystem", "Biome", "Biosphere"]
dom = {"Individual", "Population", "Community", "Ecosystem", "Biome", "Biosphere"}
fig, ax = plt.subplots(figsize=(6.6, 6.6))
ax.set_xlim(0, 10); ax.set_ylim(-0.7, 11.4); ax.axis("off"); ax.grid(False)
for i, name in enumerate(levels):
    inside = name in dom
    fc = "#dbe8f9" if inside else "#eeeeea"
    ec = BLUE if inside else MUTED
    ax.add_patch(FancyBboxPatch((0.9, i + 0.12), 3.2, 0.76, boxstyle="round,pad=0.02,rounding_size=0.12",
                                fc=fc, ec=ec, lw=1.4 if inside else 0.9))
    ax.text(2.5, i + 0.5, name, ha="center", va="center", fontsize=10, color=INK if inside else MUTED)
    if i < len(levels) - 1:
        ax.add_patch(FancyArrowPatch((2.5, i + 0.9), (2.5, i + 1.1), arrowstyle="-|>", mutation_scale=7,
                                     color=MUTED, lw=0.9))
# structural axis
ax.text(0.45, 5.4, "structural organisation (bigger and more inclusive)", rotation=90, ha="center",
        va="center", fontsize=8.5, color=MUTED)
# BI2113 domain bracket
ax.plot([4.35, 4.55, 4.55, 4.35], [5.05, 5.05, 10.95, 10.95], color=BLUE, lw=1.6)
ax.text(4.75, 7.6, "domain of BI2113\n(individual and up)", color=BLUE, fontsize=9.5, va="center", ha="left",
        fontweight="semibold")
ax.text(4.75, 0.55, "sub-organismal: not studied\nin this course (slide 14)", color=MUTED, fontsize=9, va="center", ha="left")
ax.add_patch(FancyArrowPatch((4.15, 5.5), (4.15, 1.5), connectionstyle="arc3,rad=-0.55", arrowstyle="-|>", mutation_scale=9,
                             color=AQUA, lw=1.3, ls="--"))
ax.text(5.55, 2.35, "life-cycle loop:\nreduction division and\ngene re-arrangement -> gamete\n-> fertilisation -> cell", fontsize=8.5, color=INK, va="center")
# time axis: evolutionary route
def arrow(p0, p1, color=ORANGE):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=11, color=color, lw=1.6))
arrow((4.2, 6.5), (6.3, 6.5))
ax.text(6.4, 6.5, "changed trait values:\nmicroevolution", va="center", fontsize=9, color=INK)
arrow((7.9, 6.0), (7.9, 4.6))
ax.text(8.05, 5.3, "speciation", va="center", fontsize=9, color=INK)
ax.text(7.2, 4.0, "macroevolution", va="center", ha="center", fontsize=10, color=ORANGE, fontweight="semibold")
ax.text(5.1, 9.6, "population up to biosphere:\nthese levels are 'CHANGING'\non ecological time scales", va="center", fontsize=9, color=INK)
ax.set_title("Levels of biological organisation (slides 13-14)", fontsize=11)
fig.tight_layout(); save(fig, "fig_ee01_levels")
