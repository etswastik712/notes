"""EE03 - Rosen's modelling relation (slide 6-7): natural system N, formal system F, encoding, decoding, causal and inferential entailment."""
from figlib import *
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(8.6, 4.0))
ax.set_xlim(0, 10); ax.set_ylim(0, 5); ax.axis("off"); ax.grid(False)

def box(x, y, w, h, title, sub, col):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.12", fc="#ffffff", ec=col, lw=2))
    ax.text(x + w / 2, y + h * 0.66, title, ha="center", va="center", fontsize=11.5, fontweight="semibold", color=INK)
    ax.text(x + w / 2, y + h * 0.28, sub, ha="center", va="center", fontsize=8.8, color=MUTED)

box(0.7, 1.7, 2.7, 1.6, "Natural system N", "a real population:\ncounts, births, deaths", BLUE)
box(6.6, 1.7, 2.7, 1.6, "Formal system F", "an equation:\n$N_{t+1}=f(N_t)$", ORANGE)

def arrow(p0, p1, rad, col, text, tx, ty, **kw):
    ax.add_patch(FancyArrowPatch(p0, p1, connectionstyle=f"arc3,rad={rad}", arrowstyle="-|>", mutation_scale=16, lw=1.8, color=col))
    ax.text(tx, ty, text, ha="center", va="center", fontsize=9.2, color=INK, **kw)

arrow((3.5, 2.25), (6.5, 2.25), -0.35, VIOLET, "encoding  ε\n(measure, abstract, choose variables)", 5.0, 1.15)
arrow((6.5, 2.75), (3.5, 2.75), -0.35, AQUA, "decoding  δ\n(predict, compare with data)", 5.0, 3.95)
ax.add_patch(FancyArrowPatch((1.0, 3.4), (3.1, 3.4), connectionstyle="arc3,rad=-1.2", arrowstyle="-|>", mutation_scale=14, lw=1.6, color=BLUE))
ax.text(2.05, 4.75, "causal entailment  c\n(what the world does)", ha="center", va="center", fontsize=9, color=INK)
ax.add_patch(FancyArrowPatch((6.9, 3.4), (9.0, 3.4), connectionstyle="arc3,rad=-1.2", arrowstyle="-|>", mutation_scale=14, lw=1.6, color=ORANGE))
ax.text(7.95, 4.75, "inferential entailment  i\n(what the algebra implies)", ha="center", va="center", fontsize=9, color=INK)
ax.text(5.0, 0.35, "A model is good when going round the loop  ε → i → δ  agrees with going along  c.", ha="center", fontsize=9.3, color=INK, style="italic")
save(fig, "fig_ee03_rosen")
