"""PA03 - the three posets of Assignment 4: divisors of 24, subsets of {1,2,3,4}, Z x Z with the product order."""
from figlib import *
import itertools

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.4), gridspec_kw=dict(width_ratios=[1, 1.35, 1]))
# A: divisors of 24
a = axes[0]
pos = {1: (0.5, 0), 2: (0.2, 1), 3: (0.8, 1), 4: (0.0, 2), 6: (0.5, 2), 8: (0.0, 3), 12: (0.5, 3), 24: (0.5, 4)}
edges = [(1, 2), (1, 3), (2, 4), (2, 6), (3, 6), (4, 8), (4, 12), (6, 12), (8, 24), (12, 24)]
for u, v in edges: a.plot([pos[u][0], pos[v][0]], [pos[u][1], pos[v][1]], color=MUTED, lw=1.2, zorder=1)
S = {2, 3, 4, 6}
for n, (x, y) in pos.items():
    c = BLUE if n in S else (ORANGE if n in (1, 12, 24) else "white")
    a.scatter([x], [y], s=520, color=c, edgecolor=INK, zorder=2, linewidth=1.0)
    a.text(x, y, str(n), ha="center", va="center", fontsize=9.5, color="white" if n in S or n in (1, 12, 24) else INK, zorder=3)
a.text(0.5, -0.65, "S = {2,3,4,6} (blue)\nminimal 2, 3; maximal 4, 6; no min or max\nlower bound 1; upper bounds 12, 24\nglb = 1, lub = 12 (orange)", ha="center", va="top", fontsize=8.4)
a.set_xlim(-0.3, 1.1); a.set_ylim(-2.1, 4.4); a.axis("off"); a.set_title("A  divisors of 24 under divisibility", fontsize=10)
# B: power set of {1,2,3,4}
b = axes[1]
subs = [frozenset(c) for k in range(5) for c in itertools.combinations([1, 2, 3, 4], k)]
levels = {k: [s for s in subs if len(s) == k] for k in range(5)}
pos = {}
for k, ss in levels.items():
    for i, s in enumerate(sorted(ss, key=lambda s: sorted(s))): pos[s] = ((i - (len(ss) - 1) / 2) * 1.0, k)
for s in subs:
    for t in subs:
        if s < t and len(t) == len(s) + 1: b.plot([pos[s][0], pos[t][0]], [pos[s][1], pos[t][1]], color=MUTED, lw=0.8, zorder=1)
S = [frozenset(x) for x in ({1}, {2}, {1, 2}, {1, 3}, {2, 3})]
bounds = [frozenset(), frozenset({1, 2, 3}), frozenset({1, 2, 3, 4})]
for s in subs:
    x, y = pos[s]
    c = BLUE if s in S else (ORANGE if s in bounds else "white")
    b.scatter([x], [y], s=330, color=c, edgecolor=INK, zorder=2, linewidth=0.9)
    lab = "".join(map(str, sorted(s))) or "∅"
    b.text(x, y, lab, ha="center", va="center", fontsize=7.2, color="white" if s in S or s in bounds else INK, zorder=3)
b.text(0, -0.9, "S = {{1},{2},{1,2},{1,3},{2,3}}: minimal {1}, {2}; maximal {1,2}, {1,3}, {2,3}\nlower bound ∅ only, so glb = ∅; upper bounds {1,2,3}, {1,2,3,4}, so lub = {1,2,3}", ha="center", va="top", fontsize=8.2)
b.set_xlim(-3, 3); b.set_ylim(-1.9, 4.5); b.axis("off"); b.set_title("B  subsets of {1,2,3,4} under inclusion", fontsize=10)
# C: product order
c = axes[2]
pts = [(0, 1), (1, 0), (1, 2), (2, 1)]
c.fill_between([-4, 0], -4, 0, color=AQUA, alpha=0.18); c.fill_between([2, 5], 2, 5, color=VIOLET, alpha=0.15)
c.text(-1.9, -1.9, "lower bounds\na ≤ 0, b ≤ 0", ha="center", fontsize=8.4); c.text(3.5, 3.5, "upper bounds\na ≥ 2, b ≥ 2", ha="center", fontsize=8.4)
for x, y in itertools.product(range(-3, 5), repeat=2): c.scatter([x], [y], s=6, color=MUTED, alpha=0.5)
for x, y in pts: c.scatter([x], [y], s=110, color=BLUE, edgecolor=INK, zorder=3)
c.scatter([0], [0], s=150, marker="s", color=ORANGE, edgecolor=INK, zorder=3); c.scatter([2], [2], s=150, marker="s", color=ORANGE, edgecolor=INK, zorder=3)
c.annotate("glb (0,0)", (0, 0), xytext=(-3.4, 1.2), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED)); c.annotate("lub (2,2)", (2, 2), xytext=(2.9, 0.6), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED))
c.set_xlim(-3.5, 4.5); c.set_ylim(-3.5, 4.5); c.set_aspect("equal"); c.set_xlabel("a"); c.set_ylabel("b"); c.set_title("C  Z × Z with (a,b) ≤ (c,d) iff a ≤ c and b ≤ d", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.02, "Blue: the subset S. Orange: the greatest lower and least upper bounds that exist in each poset (S has no minimum or maximum in any of the three). All computed in scripts/pa_numbers.py.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa03_posets")
