"""DM05 - a dense line on the torus (injective immersion, not an embedding), its returns, and the cusp (not an immersion)."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.4), gridspec_kw=dict(width_ratios=[1.05, 1.0, 1.0]))
alpha = np.sqrt(2.0)

# A: the line t -> (t, alpha t) mod 2 pi on the flat torus ---------------------------------------------------------------------------
a = axes[0]
for T, col, lw in ((60, BLUE, 0.7), (6, ORANGE, 1.6)):
    t = np.linspace(0, T, 40000)
    x, y = t % (2 * np.pi), (alpha * t) % (2 * np.pi)
    jump = (np.abs(np.diff(x)) > 3) | (np.abs(np.diff(y)) > 3)
    x2, y2 = x.copy(), y.copy()
    x2[1:][jump] = np.nan
    a.plot(x2, y2, color=col, lw=lw)
a.scatter([0], [0], color=RED, s=40, zorder=5)
a.text(0.2, 0.25, "F(0)", color=RED, fontsize=9)
a.set_xlim(0, 2 * np.pi); a.set_ylim(0, 2 * np.pi); a.set_aspect("equal"); a.set_xticks([0, np.pi, 2 * np.pi]); a.set_xticklabels(["0", "π", "2π"]); a.set_yticks([0, np.pi, 2 * np.pi]); a.set_yticklabels(["0", "π", "2π"])
a.set_title("A  F(t) = (e^{it}, e^{i√2 t}): t ∈ [0, 6] and [0, 60]", fontsize=9.6)

# B: returns ---------------------------------------------------------------------------------------------------------------------------------
b = axes[1]
qs = np.array([1, 2, 5, 12, 29, 70, 169, 408, 985])
def tdist(t):
    aa = np.abs((t + np.pi) % (2 * np.pi) - np.pi)
    bb = np.abs((alpha * t + np.pi) % (2 * np.pi) - np.pi)
    return np.hypot(aa, bb)
d = tdist(2 * np.pi * qs)
b.loglog(2 * np.pi * qs, d, "o-", color=BLUE, lw=1.6)
b.loglog(2 * np.pi * qs, 2 * np.pi / (2 * np.sqrt(2) * qs), "--", color=MUTED, lw=1)
b.text(10, 0.003, "dashed: ≈ 2π/(2√2 q)", fontsize=8.4, color=MUTED)
b.text(8, 1.6, "|F(2πq) − F(0)| → 0 although 2πq → ∞", fontsize=8.8, color=RED)
b.set_xlabel("t = 2πq  (q: denominators of the continued fraction of √2)"); b.set_ylabel("distance of F(t) from F(0)")
b.set_title("B  the line returns arbitrarily close", fontsize=10)

# C: the cusp ---------------------------------------------------------------------------------------------------------------------------------------
c = axes[2]
t = np.linspace(-1.2, 1.2, 400)
c.plot(t ** 2, t ** 3, color=BLUE, lw=2.2)
for tt in (-1.0, -0.6, 0.6, 1.0):
    c.annotate("", xy=(tt ** 2 + 0.25 * 2 * tt, tt ** 3 + 0.25 * 3 * tt ** 2), xytext=(tt ** 2, tt ** 3), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8))
c.scatter([0], [0], color=RED, s=46, zorder=5)
c.text(0.08, 0.1, "t = 0: F′(0) = (0, 0)", color=RED, fontsize=9)
c.text(0.35, -1.55, "F(t) = (t², t³): injective, smooth,\nbut velocity vanishes at t = 0:\nnot an immersion, image is not a submanifold", fontsize=8.4, color=INK)
c.set_aspect("equal"); c.set_xlim(-0.2, 1.9); c.set_ylim(-1.9, 1.9)
c.set_title("C  a cusp: injective but not an immersion", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A, B: an injective immersion of R into T² whose image is dense, hence not an embedding (§1, numbers dm_numbers.py DM05). C: rank 0 at one point destroys the immersion property.",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm05_immersion")
