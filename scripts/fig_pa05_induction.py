"""PA05 - induction needs its base: 2^n vs n^2; the integers as differences of naturals."""
from figlib import *

fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.1))
a = axes[0]
n = np.arange(1, 9)
a.plot(n, 2.0 ** n, "o-", color=BLUE, label="$2^n$"); a.plot(n, n ** 2.0, "s-", color=ORANGE, label="$n^2$")
for k in (2, 3, 4): a.scatter([k], [2 ** k], s=140, facecolor="none", edgecolor=RED, linewidth=1.6, zorder=3)
a.axvline(4.5, color=INK, lw=0.9, ls="--"); a.text(4.65, 6, "true for every\nn ≥ 5", fontsize=8.8); a.text(1.15, 55, "2 > 1 ✓   4 = 4 ✗\n8 < 9 ✗   16 = 16 ✗", fontsize=8.6, color=RED)
a.set_yscale("log"); a.set_xlabel("n"); a.legend(fontsize=9, loc="lower right"); a.set_title("A  2ⁿ > n² starts at n = 5 (base case n = 5)", fontsize=10)
b = axes[1]
for p in range(0, 6):
    for q in range(0, 6):
        d = p - q
        b.scatter([q], [p], s=170, color=plt.cm.coolwarm((d + 5) / 10), edgecolor=INK, linewidth=0.6, zorder=2)
        b.text(q, p, f"{d}", ha="center", va="center", fontsize=7.8, zorder=3)
b.plot([-0.4, 5.4], [-0.4, 5.4], color=INK, lw=0.9, ls="--")
b.set_xlabel("b"); b.set_ylabel("a"); b.set_title("B  Z from pairs: (a,b) ~ (c,d) iff a + d = c + b", fontsize=10); b.set_aspect("equal")
b.text(2.5, -1.25, "each diagonal a − b = const is one integer (11 classes here)", ha="center", fontsize=8.6)
b.set_xlim(-0.6, 5.6); b.set_ylim(-1.8, 5.6); b.set_yticks(range(6)); b.set_xticks(range(6))
fig.tight_layout()
fig.text(0.5, -0.03, "A: the 'n = n+1' paradox of Assignment 8 has a valid inductive step but no base; here the base is n = 5. B: the diagonals of N × N are the integers (computed in scripts/pa_numbers.py).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa05_induction")
