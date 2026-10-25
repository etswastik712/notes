"""EE02 - survivorship curves on a log axis: A idealised types I-III (schematic, my construction), B the Phlox drummondii
cohort of slide 10 (Leverich and Levin 1979), plotted at the start of each age class.
"""
from figlib import *

fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.0), gridspec_kw=dict(width_ratios=[1, 1.15]))

# ---- A: idealised
a = axes[0]
x = np.linspace(0, 1, 400)
t1 = np.maximum(1 - x ** 5, 1e-3)                     # low mortality until late
t2 = np.exp(-np.log(1000) * x)                        # constant per-capita mortality
t3 = np.exp(-2.2 * x) * (0.004 + 0.996 * np.exp(-26 * x))    # very high early mortality, then lower
for y, c, nm, xy in ((t1, BLUE, "Type I", (0.5, 0.95)), (t2, ORANGE, "Type II", (0.52, 0.04)), (t3, AQUA, "Type III", (0.12, 0.005))):
    a.plot(x, y, color=c)
a.text(0.27, 0.45, "Type I: mortality late", color=BLUE, fontsize=8.8, ha="left")
a.text(0.52, 0.058, "Type II: constant risk\n(straight line on log axis)", color=ORANGE, fontsize=8.8, va="top")
a.text(0.02, 0.0016, "Type III:\nmortality early", color=AQUA, fontsize=8.8, va="bottom")
a.set_yscale("log"); a.set_ylim(1e-3, 1.5); a.set_xlim(0, 1)
a.set_xlabel("age (fraction of maximum life span)"); a.set_ylabel("survivors, $l_x$ (log scale)")
a.set_title("A  three idealised types (schematic)", fontsize=10)
a.grid(which="minor", visible=False)

# ---- B: Phlox
b = axes[1]
start = np.array([0, 299, 306, 313, 320, 327, 334, 341, 348, 355])
l_x = np.array([1.0, .1586, .1546, .1516, .1476, .1365, .1054, .0743, .0221, 0.0])
b.plot(start[:2], l_x[:2], "--", color=BLUE, lw=1.3)          # no data inside class 1 (days 0-299)
b.plot(start[1:-1], l_x[1:-1], "-o", color=BLUE, ms=4.5)
b.plot([0], [1.0], "o", color=BLUE, ms=4.5)
b.annotate("", xy=(355, 0.0075), xytext=(348, 0.0221), arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.4))
b.text(357, 0.0075, "0 at day 355-362", color=BLUE, fontsize=8.3, va="center")
b.annotate("84 % die before day 299\n(dashed: no data inside class 1)", (150, 0.075), color=INK, fontsize=8.4, ha="center")
b.annotate("only 22 of 996 seeds (2 %)\nlost over the next four classes", (321, 0.145), xytext=(170, 0.034), fontsize=8.4, color=INK,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.annotate("final collapse:\nannual plant dies after seed set", (343, 0.08), xytext=(215, 0.0125), fontsize=8.4, color=INK,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_yscale("log"); b.set_ylim(0.005, 1.6); b.set_xlim(-10, 420)
b.set_xlabel("age, days (class starts)"); b.set_ylabel("$l_x$ (log scale)")
b.set_title("B  Phlox drummondii cohort, slide 10", fontsize=10)
b.grid(which="minor", visible=False)
fig.tight_layout()
fig.text(0.5, -0.045, "A is schematic. B is the slide-10 table (996 seeds): high early loss, then a plateau, then a steep final fall; "
         "Molles (Fig. 10.15) files it with the Type I pattern.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_ee02_survivorship")
