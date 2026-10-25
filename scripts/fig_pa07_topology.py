"""PA07 - unit balls, counts of finite topologies and an open cover with no finite subcover."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.0), gridspec_kw=dict(width_ratios=[1, 1, 1.1]))
a = axes[0]
t = np.linspace(0, 2 * np.pi, 400)
a.fill([1, 0, -1, 0, 1], [0, 1, 0, -1, 0], color=AQUA, alpha=0.25, label=r"$\ell_1$ (area 2)")
a.plot(np.cos(t), np.sin(t), color=BLUE, lw=2, label=r"$\ell_2$ (area $\pi$)")
a.plot([-1, 1, 1, -1, -1], [-1, -1, 1, 1, -1], color=ORANGE, lw=2, label=r"$\ell_\infty$ (area 4)")
a.set_aspect("equal"); a.set_xlim(-1.4, 1.4); a.set_ylim(-1.4, 1.4); a.legend(fontsize=8, loc="lower right"); a.set_title("A  unit balls of three metrics on R²", fontsize=10)
b = axes[1]
ns = np.array([1, 2, 3, 4]); lab = [1, 4, 29, 355]; hom = [1, 3, 9, 33]
b.bar(ns - 0.2, lab, 0.4, color=BLUE, label="labelled"); b.bar(ns + 0.2, hom, 0.4, color=ORANGE, label="up to homeomorphism")
for x_, v in zip(ns - 0.2, lab): b.text(x_, v + 8, str(v), ha="center", fontsize=8.6)
for x_, v in zip(ns + 0.2, hom): b.text(x_, v + 8, str(v), ha="center", fontsize=8.6)
b.set_xticks(ns); b.set_xlabel("number of points n"); b.set_ylabel("topologies on an n-point set"); b.legend(fontsize=8.4, loc="upper left"); b.set_title("B  finite topologies = preorders", fontsize=10)
c = axes[2]
for k, n in enumerate(range(2, 9)):
    c.plot([1 / n, 1], [k, k], color=BLUE, lw=5, solid_capstyle="butt"); c.text(1.02, k, f"(1/{n}, 1)", va="center", fontsize=8.2)
c.scatter([1 / 20], [3], marker="x", color=RED, s=60, zorder=3); c.annotate("a point near 0 is\nnever covered by a\nfinite subfamily", (1 / 20, 3), xytext=(0.02, 0.2), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED))
c.set_xlim(0, 1.25); c.set_ylim(7.3, -0.8); c.set_yticks([]); c.set_xlabel("x"); c.set_title("C  (0,1) is not compact", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "B: topologies on 3 points: 29 (9 up to homeomorphism), on 4 points: 355 (33), the same numbers as preorders (computed by brute force). C: {(1/n, 1)} covers (0,1) but any finite subfamily is contained in (1/N, 1).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa07_topology")
