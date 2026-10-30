"""PA15 - the covering R -> S^1, winding numbers, and the double cover SU(2) -> SO(3)."""
from figlib import *

fig = plt.figure(figsize=(13.4, 4.4))

# A: the helix covering the circle -----------------------------------------------------------------------------------------------
a = fig.add_subplot(1, 3, 1, projection="3d")
t = np.linspace(0, 3, 600)
a.plot(np.cos(2 * np.pi * t), np.sin(2 * np.pi * t), t, color=BLUE, lw=2.2)
th = np.linspace(0, 2 * np.pi, 200)
a.plot(np.cos(th), np.sin(th), np.zeros_like(th), color=INK, lw=1.6)
for k in range(0, 4):
    a.plot([1, 1], [0, 0], [0, k], color=MUTED, lw=0.7, ls=":")
    a.scatter([1], [0], [k], color=ORANGE, s=26)
a.text(1.15, 0, 3.05, "fibre over 1 = Z", fontsize=8.6, color=ORANGE)
a.text(1.1, -1.1, 0, "S¹", fontsize=10)
a.set_xticks([]); a.set_yticks([]); a.set_zticks([0, 1, 2, 3]); a.view_init(elev=18, azim=-62)
a.set_title("A  the covering p(t) = e^{2πit}", fontsize=10)

# B: winding numbers -------------------------------------------------------------------------------------------------------------
b = fig.add_subplot(1, 3, 2)
s = np.linspace(0, 1, 800)
for (cx, r, col, lab, dy) in ((0.5, 1.0, BLUE, "centre 0.5, r = 1:  winding 1", 0.0), (0.5, 0.3, AQUA, "centre 0.5, r = 0.3:  winding 0", 0.0)):
    b.plot(cx + r * np.cos(2 * np.pi * s), r * np.sin(2 * np.pi * s), color=col, lw=2, label=lab)
ang = 2 * np.pi * 3 * s
rad = 0.62 + 0.14 * np.sin(2 * np.pi * s)                      # closed curve winding 3 times around 0 (three nested turns)
b.plot(-2.1 + rad * np.cos(ang) * 1.0, rad * np.sin(ang), color=ORANGE, lw=1.5, label="loop winding 3 times around its centre (-2.1, 0): winding 3")
b.scatter([-2.1], [0], color=RED, zorder=5, s=28)
b.scatter([0], [0], color=RED, zorder=5, s=36)
b.text(0.05, 0.06, "0", color=RED, fontsize=9)
b.set_aspect("equal"); b.set_xlim(-3.0, 1.8); b.set_ylim(-1.3, 1.5)
b.legend(fontsize=7.4, loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=1)
b.set_title("B  class in π₁(S¹) = Z = winding number", fontsize=10)

# C: SU(2) -> SO(3): half a great circle upstairs is a full loop downstairs --------------------------------------------------------
c = fig.add_subplot(1, 3, 3)
u = np.linspace(0, 1, 300)
c.plot(np.cos(2 * np.pi * u), np.sin(2 * np.pi * u), color=MUTED, lw=1, ls=":")
c.plot(np.cos(np.pi * u), np.sin(np.pi * u), color=BLUE, lw=3, label="q(t) = (cos πt, 0, 0, sin πt) ∈ S³,  t∈[0,1]:  from 1 to −1")
c.scatter([1], [0], color=INK, zorder=5, s=34); c.scatter([-1], [0], color=RED, zorder=5, s=34)
c.text(1.08, 0.1, "q = 1", fontsize=9); c.text(-1.75, 0.1, "q = −1", fontsize=9, color=RED)
c.annotate("", xy=(0.0, -1.6), xytext=(0.0, -0.1), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.2))
c.text(0.1, -0.85, "R(q): rotation by 2πt", fontsize=8.6, color=INK)
phi = np.linspace(0, 2 * np.pi, 300)
c.plot(0.5 * np.cos(phi), -2.1 + 0.5 * np.sin(phi), color=AQUA, lw=3)
c.scatter([0.5], [-2.1], color=INK, zorder=5, s=34)
c.text(-1.75, -2.8, "a closed loop in SO(3), whose lift ends at −1:\nnot null-homotopic. Twice around lifts to a\nclosed loop in S³: π₁(SO(3)) = Z/2.", fontsize=8.2, color=INK)
c.set_aspect("equal"); c.set_xlim(-1.9, 1.7); c.set_ylim(-3.9, 1.4); c.axis("off")
c.legend(fontsize=7.4, loc="upper center", bbox_to_anchor=(0.5, 1.02))
c.set_title("C  SU(2) → SO(3) is a 2-sheeted cover", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.02, "A: the lifts of the base point are the integers. B: winding numbers computed by lifting (pa15_numbers.py). "
         "C: the quaternion loop from 1 to −1 maps to a rotation by 2π (checked numerically).", ha="center", fontsize=8, color=MUTED)
save(fig, "fig_pa15_cover")
