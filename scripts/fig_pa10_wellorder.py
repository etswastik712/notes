"""PA10 - lexicographic order on N x N, Ackermann call counts, Euclid's descent."""
from figlib import *
import math

fig, axes = plt.subplots(1, 3, figsize=(12.4, 3.9))
a = axes[0]
N = 5
pts = [(i, j) for i in range(1, N + 1) for j in range(1, N + 1)]
for (i, j) in pts:
    a.scatter(j, i, s=26, color=BLUE, zorder=3)
for i in range(1, N + 1):
    a.plot([1, N], [i, i], color=BLUE, lw=1.0, alpha=0.8)
    if i < N:
        a.annotate("", xy=(1, i + 1), xytext=(N, i), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=0.9, connectionstyle="arc3,rad=-0.25"))
a.scatter([1], [2], s=120, facecolor="none", edgecolor=RED, lw=1.8, zorder=4)
a.text(1.15, 2.42, "(2,1): infinitely many\npredecessors in N x N", fontsize=8.0, color=RED)
a.set_xlabel("second coordinate $b$"); a.set_ylabel("first coordinate $a$")
a.set_xlim(0.5, N + 0.8); a.set_ylim(0.5, N + 0.7)
a.set_title("A  $(a,b)<(c,d)$ if $a<c$, or $a=c$, $b<d$", fontsize=10)

b = axes[1]
def calls(m, n):
    cnt = [0]
    def A(m, n):
        cnt[0] += 1
        if m == 0: return n + 1
        if n == 0: return A(m - 1, 1)
        return A(m - 1, A(m, n - 1))
    A(m, n); return cnt[0]
n = np.arange(0, 6)
for m, c in ((1, BLUE), (2, AQUA), (3, ORANGE)):
    b.semilogy(n, [calls(m, int(x)) for x in n], color=c, lw=1.8, marker="o", ms=4, label=f"$A({m},n)$")
b.set_xlabel("$n$"); b.set_ylabel("number of recursive calls"); b.legend(fontsize=8.4, loc="lower right")
b.text(0.04, 0.80, "each call lowers $(m,n)$\nlexicographically, so the\nrecursion must stop", transform=b.transAxes, fontsize=8.0, color=MUTED)
b.set_title("B  Ackermann terminates", fontsize=10)

c = axes[2]
def euclid(a, b):
    seq = [a]
    while b: a, b = b, a % b; seq.append(a)
    return seq + [0]
for (x, y, col) in ((1071, 462, BLUE), (987, 610, ORANGE), (1000, 7, AQUA), (832, 520, RED)):
    s = euclid(x, y)
    c.plot(range(len(s)), s, marker="o", ms=4, lw=1.4, color=col, label=f"$(a,b)=({x},{y})$")
c.set_yscale("symlog", linthresh=1); c.xaxis.set_major_locator(plt.MaxNLocator(integer=True)); c.set_xlabel("step $k$"); c.set_ylabel("first entry $a_k$")
c.legend(fontsize=7.8, loc="upper right")
c.set_title("C  Euclid: a decreasing sequence stops", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "B: call counts counted by running the recursion (scripts/pa_numbers2.py). C: the pair (a,b) goes to (b, a mod b), whose first entry is smaller than a.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa10_wellorder")
