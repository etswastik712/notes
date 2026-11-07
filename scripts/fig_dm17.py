"""DM17 - leaves of linear foliations of the torus, the figure-eight (weak embeddedness), and the foliation of R^3 minus 0 by the level sets of x^2+y^2-z^2."""
from figlib import *

fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.7))

# A: the unrolled torus: one leaf of slope 3/5 (closed after 5 turns) and of slope sqrt2 (N = 12 and N = 60 turns) -----------------------------------
a = ax[0]
def leaf(th, N, col, lw):
    # leaf t -> (t mod 1, th t mod 1), drawn in the unit square: cut at each wrap
    t = np.linspace(0, N, 4000 * N // 5 + 1)
    X = t % 1.0
    Y = (th * t) % 1.0
    brk = np.where((np.abs(np.diff(X)) > 0.5) | (np.abs(np.diff(Y)) > 0.5))[0]
    seg_start = 0
    for bidx in list(brk) + [len(t) - 1]:
        a.plot(X[seg_start:bidx + 1], Y[seg_start:bidx + 1], color=col, lw=lw)
        seg_start = bidx + 1
leaf(np.sqrt(2.0), 60, GRID, 0.7)
leaf(np.sqrt(2.0), 8, BLUE, 1.4)
leaf(0.6, 5, ORANGE, 2.0)
a.axvline(0.5, color=INK, lw=1.0, ls=":")
a.text(0.505, 1.02, "transversal x = ½", fontsize=8, color=INK)
a.set_xlim(0, 1); a.set_ylim(0, 1.06); a.set_aspect("equal")
a.set_xlabel("angle 1"); a.set_ylabel("angle 2")
a.set_title("A  leaves of slope 3/5 (closed) and √2 (dense)", fontsize=9.8)
a.text(0.02, 0.1, "orange: 3/5 closes after 5 turns\nblue: √2, 8 turns;  grey: 60 turns\nin a flat chart each leaf is a\ncountable union of slices", fontsize=7.8, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.85))

# B: the figure-eight S = image of beta on (-pi/2, 3pi/2) and G(t) = (sin 2t, sin t) for t beyond the interval -------------------------------------------
b = ax[1]
tt = np.linspace(-np.pi / 2, 1.5 * np.pi, 800)
bx, by = np.sin(2 * tt), np.sin(tt)
b.plot(bx, by, color=BLUE, lw=2.4, label="β on (−π/2, 3π/2)")
t2 = np.linspace(1.5 * np.pi, 1.5 * np.pi + 0.9, 80)
b.plot(np.sin(2 * t2), np.sin(t2), color=ORANGE, lw=3.2, label="G(t) for t just past 3π/2")
b.scatter([0], [-1], color=RED, s=48, zorder=5)
b.annotate("β⁻¹∘G jumps by 2π here:\nG leaves the end of the interval\nand re-enters at the other end", xy=(0, -1), xytext=(0.30, -0.92), fontsize=7.8, color=RED, arrowprops=dict(arrowstyle="->", color=RED))
b.set_aspect("equal"); b.set_xlim(-1.15, 1.15); b.set_ylim(-1.3, 1.5)
b.legend(fontsize=7.8, loc="upper right", frameon=False)
b.set_title("B  figure-eight: G: ℝ → S not continuous", fontsize=9.8)

# C: the foliation of R^3 minus 0 by the connected components of the level sets of F = x^2 + y^2 - z^2 ----------------------------------------------------
c = ax[2]
rr = np.linspace(0, 2.2, 400)
for k in (0.25, 0.75, 1.5):
    zz = np.sqrt(rr ** 2 - (-k)) if False else None
for cval, col in ((-1.0, ORANGE), (-0.25, ORANGE), (0.25, BLUE), (1.0, BLUE), (2.0, BLUE)):
    # r^2 - z^2 = cval
    zz = np.sqrt(np.maximum(rr ** 2 - cval, 0))
    ok = rr ** 2 - cval >= 0
    if cval < 0:
        c.plot(rr[ok], zz[ok], color=col, lw=1.6)
        c.plot(rr[ok], -zz[ok], color=col, lw=1.6)
    else:
        c.plot(rr[ok], zz[ok], color=col, lw=1.6)
        c.plot(rr[ok], -zz[ok], color=col, lw=1.6)
c.plot(rr, rr, color=INK, lw=2.4); c.plot(rr, -rr, color=INK, lw=2.4)
c.set_xlim(0, 2.2); c.set_ylim(-2.2, 2.2); c.set_aspect("equal")
c.set_xlabel("r = √(x² + y²)"); c.set_ylabel("z")
c.text(1.7, 0.2, "F > 0: one sheet", color=BLUE, fontsize=8); c.text(0.05, 1.95, "F < 0: two sheets", color=ORANGE, fontsize=8)
c.text(1.05, 1.0, "F = 0: two\ncone halves", color=INK, fontsize=8, bbox=dict(fc=SURFACE, ec="none", alpha=0.9))
c.set_title("C  components of the level sets of F = x²+y²−z²", fontsize=9.8)

fig.tight_layout()
fig.text(0.5, -0.04, "A: the linear flow on T² = ℝ²/ℤ²: rational slope gives closed leaves, irrational slope dense leaves (Lee Ex. 19.18(e)); the three distinct gaps of the crossings of the transversal "
         "are listed in dm_numbers2.py (DM17).  B: Lee Ex. 5.28; the interval (−π/2, 3π/2) is my choice (its endpoints are illegible in the text layer).  "
         "C: HW10 Q5 (= Lee Problem 19-8) for the submersion F on ℝ³∖{0}: the components of the level sets are the leaves, the orbits of SO(2,1)⁰.",
         ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_dm17_foliations")
