"""PA11 - gluing a square, the line with two origins, and an injective continuous map that is not an embedding."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.2, 4.2), gridspec_kw=dict(width_ratios=[1.35, 1, 1]))

# A: edge identifications of the square ----------------------------------------------------------------------------
a = axes[0]
a.set_aspect("equal"); a.axis("off")


def square(ax, x0, y0, edges, title):
    """edges: dict side -> (label, direction) with direction +1 along the walk bottom->right->top->left (anticlockwise)."""
    s = 1.0
    corners = {"bottom": ((x0, y0), (x0 + s, y0)), "right": ((x0 + s, y0), (x0 + s, y0 + s)),
               "top": ((x0 + s, y0 + s), (x0, y0 + s)), "left": ((x0, y0 + s), (x0, y0))}
    for side, (p, q) in corners.items():
        label, direction = edges[side]
        col = {"a": BLUE, "b": ORANGE}.get(label, MUTED)
        if direction < 0:
            p, q = q, p
        ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="-|>", color=col, lw=2, mutation_scale=14))
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        off = {"bottom": (0, -0.14), "top": (0, 0.1), "left": (-0.13, 0), "right": (0.1, 0)}[side]
        ax.text(mx + off[0], my + off[1], label, color=col, ha="center", va="center", fontsize=10, fontweight="semibold")
    ax.text(x0 + s / 2, y0 + s / 2, title, ha="center", va="center", fontsize=8.6, color=INK)


# the four standard words, read anticlockwise from the bottom-left corner
square(a, 0.0, 1.35, {"bottom": ("a", 1), "right": ("b", 1), "top": ("a", -1), "left": ("b", -1)}, "torus  a b a⁻¹ b⁻¹\nχ = 0")
square(a, 1.35, 1.35, {"bottom": ("a", 1), "right": ("b", 1), "top": ("a", -1), "left": ("b", 1)}, "Klein  a b a⁻¹ b\nχ = 0")
square(a, 0.0, 0.0, {"bottom": ("a", 1), "right": ("b", 1), "top": ("a", 1), "left": ("b", 1)}, "projective plane\n(a b a b)  χ = 1")
square(a, 1.35, 0.0, {"bottom": ("a", 1), "right": ("a", -1), "top": ("b", 1), "left": ("b", -1)}, "sphere\n(a a⁻¹ b b⁻¹)  χ = 2")
a.set_xlim(-0.3, 2.65); a.set_ylim(-0.3, 2.55)
a.set_title("A  one square, four gluings (χ = V − E + F, computed)", fontsize=10)

# B: the line with two origins --------------------------------------------------------------------------------------
b = axes[1]
xs = np.linspace(-1, 1, 200)
b.plot(xs, np.full_like(xs, 0.18), color=BLUE, lw=2.4)
b.plot(xs, np.full_like(xs, -0.18), color=ORANGE, lw=2.4)
for x_ in (-0.7, -0.35, 0.35, 0.7):
    b.plot([x_, x_], [-0.18, 0.18], color=MUTED, lw=1, ls=":")
b.scatter([0], [0.18], s=70, color=BLUE, zorder=3); b.scatter([0], [-0.18], s=70, color=ORANGE, zorder=3)
b.text(0.05, 0.3, "0₁", color=BLUE, fontsize=10); b.text(0.05, -0.43, "0₂", color=ORANGE, fontsize=10)
b.text(0, 0.78, "x₁ ~ x₂ for x ≠ 0", ha="center", fontsize=9, color=INK)
b.text(0, -0.82, "every neighbourhood of 0₁ meets\nevery neighbourhood of 0₂:\nnot Hausdorff", ha="center", va="top", fontsize=8.6, color=RED)
b.set_xlim(-1.1, 1.1); b.set_ylim(-1.35, 1.0); b.axis("off")
b.set_title("B  locally Euclidean, but not Hausdorff", fontsize=10)

# C: figure-eight --------------------------------------------------------------------------------------------------
c = axes[2]
t = np.linspace(-np.pi + 0.0005, np.pi - 0.0005, 3000)
c.plot(np.sin(2 * t), np.sin(t), color=BLUE, lw=2)
for d, m in ((0.5, "o"), (0.2, "s"), (0.05, "D")):
    tt = np.pi - d
    c.scatter([np.sin(2 * tt)], [np.sin(tt)], s=34, color=ORANGE, marker=m, zorder=3)
c.scatter([0], [0], s=60, facecolor="none", edgecolor=RED, linewidth=1.8, zorder=4)
c.text(0.08, 0.14, "β(0)", color=RED, fontsize=9)
c.text(-0.98, -0.95, "β(π−δ) → β(0) as δ → 0\nthough π−δ stays far from 0", fontsize=8.4, color=INK)
c.set_aspect("equal"); c.set_xlim(-1.15, 1.15); c.set_ylim(-1.2, 1.2); c.set_xticks([]); c.set_yticks([])
c.set_title("C  injective, continuous, not an embedding", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: the edge word read anticlockwise (an exponent −1 reverses the arrow); V, E, F counted by union-find in pa11_numbers.py. "
         "B: Lee's line with two origins. C: β(t) = (sin 2t, sin t), t ∈ (−π, π) (Lee Example 4.19): the image's subspace topology is not that of the interval.",
         ha="center", fontsize=8, color=MUTED, wrap=True)
save(fig, "fig_pa11_quotients")
