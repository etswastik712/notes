"""PA04 - counting infinities: the anti-diagonal walk through N x N, Cantor's diagonal, and the bijection (0,1) -> R."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.2), gridspec_kw=dict(width_ratios=[1, 1.05, 1]))
a = axes[0]
pair = lambda m, n: (m + n - 2) * (m + n - 1) // 2 + m
for m in range(1, 7):
    for n in range(1, 7):
        if m + n <= 7:
            a.text(n, -m, str(pair(m, n)), ha="center", va="center", fontsize=9, color=INK,
                   bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=BLUE if (m + n) % 2 else ORANGE, lw=1.1))
for s in range(3, 8):
    a.plot([1, s - 1], [-(s - 1), -1], color=MUTED, lw=0.7, ls=":", zorder=0)
a.set_xlim(0.4, 6.6); a.set_ylim(-7.3, -0.4); a.set_xticks(range(1, 7)); a.set_yticks([-m for m in range(1, 7)]); a.set_yticklabels(range(1, 7))
a.set_xlabel("n (column)"); a.set_ylabel("m (row)"); a.set_title("A  N × N is countable: walk the anti-diagonals", fontsize=10)
a.text(3.5, -7.0, "position of (m,n) is (m+n−2)(m+n−1)/2 + m", ha="center", fontsize=8.4)
b = axes[1]
rows = ["f(1) = 0 . 3 1 4 1 5 9 …", "f(2) = 0 . 5 0 0 0 0 0 …", "f(3) = 0 . 7 1 8 2 8 1 …", "f(4) = 0 . 3 3 3 3 3 3 …", "f(5) = 0 . 1 4 1 4 2 1 …", "f(6) = 0 . 2 7 1 8 2 8 …"]
digs = [[3, 1, 4, 1, 5, 9], [5, 0, 0, 0, 0, 0], [7, 1, 8, 2, 8, 1], [3, 3, 3, 3, 3, 3], [1, 4, 1, 4, 2, 1], [2, 7, 1, 8, 2, 8]]
for i, r in enumerate(digs):
    b.text(0.0, -i, f"f({i + 1}) = 0.", ha="left", va="center", fontsize=9.5, family="monospace")
    for j, d in enumerate(r):
        on = i == j
        b.text(2.2 + 0.55 * j, -i, str(d), ha="center", va="center", fontsize=10, family="monospace", color="white" if on else INK,
               bbox=dict(boxstyle="round,pad=0.2", fc=ORANGE if on else "white", ec=MUTED, lw=0.6))
new = [3 if digs[k][k] != 3 else 7 for k in range(6)]
b.text(0.0, -7.2, "b = 0.", ha="left", va="center", fontsize=9.5, family="monospace")
for j, d in enumerate(new): b.text(2.2 + 0.55 * j, -7.2, str(d), ha="center", va="center", fontsize=10, family="monospace", color="white", bbox=dict(boxstyle="round,pad=0.2", fc=BLUE, ec=MUTED, lw=0.6))
b.text(2.2 + 0.55 * 6, -7.2, "…", fontsize=12, va="center")
b.text(3.0, -8.4, "b_k = 3 unless the k-th diagonal digit is 3 (then 7):\nb differs from every f(k) in place k and never uses 9", ha="center", fontsize=8.4)
b.set_xlim(-0.2, 6.2); b.set_ylim(-9.4, 0.8); b.axis("off"); b.set_title("B  Cantor's diagonal argument", fontsize=10)
c = axes[2]
x1 = np.linspace(0.005, 0.5, 300); x2 = np.linspace(0.5, 0.995, 300)
f1 = 1 - 1 / (2 * x1); f2 = 1 / (2 * (1 - x2)) - 1
c.plot(x1, f1, color=BLUE, lw=2); c.plot(x2, f2, color=BLUE, lw=2)
c.axhline(0, color=INK, lw=0.6); c.scatter([0.5], [0], color=ORANGE, zorder=3, s=40)
c.set_xlim(0, 1); c.set_ylim(-8, 8); c.set_xlabel("x in (0,1)"); c.set_ylabel("f(x)")
c.text(0.27, -6.6, r"$f(x)=1-\frac{1}{2x}$ on $(0,\frac{1}{2}]$", fontsize=8.6); c.text(0.06, 5.6, r"$f(x)=\frac{1}{2(1-x)}-1$ on $[\frac{1}{2},1)$", fontsize=8.6)
c.set_title("C  (0,1) and R have the same size", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.02, "A: bijection N → N × N; B: any list of reals in (0,1) misses a number, so (0,1) is uncountable; C: lecture 20 bijection f with inverse g (g∘f = id checked on 96 rationals).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa04_cardinality")
