"""DM10 - pushforward of a vector field (HW4 Q3), the commutator quadrilateral of [d_x, x d_y] = d_y, and the commuting pair E = r d_r, R = d_theta."""
from figlib import *

fig, axes = plt.subplots(1, 4, figsize=(14.2, 4.3), gridspec_kw=dict(width_ratios=[1, 1.35, 0.95, 1.05]))
cs = [0.4, 0.8, 1.4, 2.2]
cols = [BLUE, ORANGE, AQUA, VIOLET]
x0s = (0.5, 1.0, 1.5)

# A1: domain: the rays y = cx with X = x d_x + y d_y ---------------------------------------------------------------------------------------------------
a = axes[0]
for c, col in zip(cs, cols):
    xs = np.linspace(0.05, 2.2, 40)
    a.plot(xs, c * xs, color=col, lw=1.0, alpha=0.55)
    for x0 in x0s:
        a.annotate("", xy=(1.22 * x0, 1.22 * c * x0), xytext=(x0, c * x0), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3))
a.set_xlim(0, 2.3); a.set_ylim(0, 3.6); a.set_aspect("equal"); a.set_xlabel("x"); a.set_ylabel("y")
a.set_title("A  X = x∂ₓ + y∂ᵧ on the quadrant", fontsize=9.5)

# A2: codomain: the lines v = c with F_*X = 2u d_u ------------------------------------------------------------------------------------------------------
a2 = axes[1]
for c, col in zip(cs, cols):
    a2.plot([0, 5.8], [c, c], color=col, lw=1.0, alpha=0.55)
    for x0 in x0s:
        u0 = c * x0 ** 2
        a2.annotate("", xy=(u0 * 1.44, c), xytext=(u0, c), arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3))
a2.set_xlim(0, 6.0); a2.set_ylim(0, 3.6); a2.set_aspect("equal"); a2.set_xlabel("u"); a2.set_ylabel("v")
a2.set_title("F(x,y)=(xy, y/x):   F_*X = 2u ∂ᵤ", fontsize=9.5)

# B: the commutator quadrilateral for X = d_x, Y = x d_y: gap = eps^2 [X,Y] ----------------------------------------------------------------------------
b = axes[2]
xx, yy = np.meshgrid(np.linspace(-0.1, 0.7, 5), np.linspace(-0.05, 0.4, 4))
b.quiver(xx, yy, 0 * xx, xx, color=GRID, scale=6, width=0.005, pivot="tail")
e = 0.5
P = np.array([[0, 0], [e, 0], [e, e * e], [0, e * e]])
b.plot(P[:, 0], P[:, 1], color=BLUE, lw=2.2)
b.scatter(P[:, 0], P[:, 1], color=INK, s=22, zorder=4)
b.scatter([0], [e * e], color=RED, s=60, zorder=5, facecolors="none", linewidths=1.8)
b.annotate("", xy=(0.0, e * e), xytext=(0.0, 0.0), arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
b.text(0.04, 0.095, "gap\nε²∂ᵧ", fontsize=8.6, color=RED)
b.text(0.2, -0.045, "flow X", color=BLUE, fontsize=8.6, ha="center"); b.text(0.53, 0.1, "flow Y", color=BLUE, fontsize=8.6)
b.text(0.25, 0.27, "flow −X", color=BLUE, fontsize=8.6, ha="center")
b.set_xlim(-0.15, 0.8); b.set_ylim(-0.1, 0.45); b.set_aspect("equal")
b.set_xlabel("then −Y returns to the same point (Y = 0 on x = 0)", fontsize=7.6)
b.set_title("B  [∂ₓ, x∂ᵧ] = ∂ᵧ ≠ 0", fontsize=9.5)

# C: commuting pair E = r d_r, R = d_theta: the quadrilateral closes ------------------------------------------------------------------------------------
c = axes[3]
th = np.linspace(0, 1, 100)
eps = 0.5
p0 = np.array([1.0, 0.0])
rot = lambda ang: np.array([[np.cos(ang), -np.sin(ang)], [np.sin(ang), np.cos(ang)]])
s1 = np.exp(eps) * p0
arc1 = np.array([rot(eps * t) @ s1 for t in th])
s2 = rot(eps) @ s1
s3 = np.exp(-eps) * s2
arc2 = np.array([rot(-eps * t) @ s3 for t in th])
c.plot([p0[0], s1[0]], [p0[1], s1[1]], color=BLUE, lw=2.2)
c.plot(arc1[:, 0], arc1[:, 1], color=ORANGE, lw=2.2)
c.plot([s2[0], s3[0]], [s2[1], s3[1]], color=BLUE, lw=2.2)
c.plot(arc2[:, 0], arc2[:, 1], color=ORANGE, lw=2.2)
c.scatter([s1[0], s2[0], s3[0]], [s1[1], s2[1], s3[1]], color=INK, s=22, zorder=4)
c.scatter([p0[0]], [p0[1]], color=RED, s=60, zorder=5, facecolors="none", linewidths=1.8)
c.text(0.95, -0.2, "start = end", color=RED, fontsize=8.4, ha="center")
c.text(1.35, -0.14, "E", color=BLUE, fontsize=9); c.text(1.7, 0.4, "R", color=ORANGE, fontsize=9)
c.text(1.2, 0.8, "−E", color=BLUE, fontsize=9); c.text(0.68, 0.18, "−R", color=ORANGE, fontsize=9)
c.set_aspect("equal"); c.set_xlim(0.4, 2.0); c.set_ylim(-0.35, 1.0)
c.set_xlabel("E = x∂ₓ + y∂ᵧ,  R = x∂ᵧ − y∂ₓ:  [E, R] = 0", fontsize=7.8)
c.set_title("C  [r∂ᵣ, ∂_θ] = 0", fontsize=9.5)

fig.tight_layout()
fig.text(0.5, -0.03, "A: F is a diffeomorphism of the open quadrant (det DF = 2y/x, inverse (√(u/v), √(uv))); Y = dF(X)∘F⁻¹ checked at 200 random points (error 1.8×10⁻⁹). "
         "B, C: flow quadrilaterals, ε = 0.5 (exact flows); the gap is ε²[X,Y] to leading order (DM13). Numbers: dm_numbers.py (DM10).", ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_dm10_fields")
