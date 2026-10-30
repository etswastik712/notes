"""PA08 - why a pattern is not a proof: Moser's circle, sum of 1/k^2 and the strengthened hypothesis, n^2+n+41."""
from figlib import *
import math
import sympy as sp

fig, axes = plt.subplots(1, 3, figsize=(12.4, 3.8))
a = axes[0]
n = np.arange(1, 11)
reg = np.array([math.comb(m, 4) + math.comb(m, 2) + 1 for m in n])
a.plot(n, 2.0 ** (n - 1), color=ORANGE, lw=1.6, marker="o", ms=4, label=r"$2^{n-1}$ (the pattern)")
a.plot(n, reg, color=BLUE, lw=1.6, marker="s", ms=4, label=r"regions: $C(n,4)+C(n,2)+1$")
a.annotate("1, 2, 4, 8, 16, then 31", (6, 31), (2.2, 190), fontsize=8.4, arrowprops=dict(arrowstyle="->", color=MUTED))
a.set_yscale("log"); a.set_xlabel("number of points $n$ on the circle"); a.set_ylabel("regions"); a.legend(fontsize=8.2, loc="lower right")
a.set_title("A  five terms do not make a theorem", fontsize=10)

b = axes[1]
m = np.arange(1, 31)
s = np.cumsum(1.0 / m ** 2)
b.plot(m, s, color=BLUE, lw=1.8, label=r"$s_n=\sum_{k\leq n}1/k^2$")
b.plot(m, 2 - 1.0 / m, color=AQUA, lw=1.6, ls="--", label=r"$2-1/n$: provable by induction")
b.axhline(2, color=ORANGE, lw=1.4, label=r"$2$: true, but the step cannot reach it")
b.axhline(math.pi ** 2 / 6, color=MUTED, lw=0.9, ls=":"); b.text(15, math.pi ** 2 / 6 + 0.02, r"limit $\pi^2/6=1.645$", fontsize=8.0, color=MUTED)
b.set_ylim(0.9, 2.15); b.set_xlabel("$n$"); b.legend(fontsize=7.9, loc="lower right")
b.set_title("B  strengthen the hypothesis", fontsize=10)

c = axes[2]
k = np.arange(0, 61)
isp = np.array([sp.isprime(int(x * x + x + 41)) for x in k])
c.scatter(k[isp], np.ones(isp.sum()), s=18, color=BLUE, label="$n^2+n+41$ is prime")
c.scatter(k[~isp], np.ones((~isp).sum()), s=44, color=RED, marker="x", label="composite")
c.annotate("$n=40$: $1681=41^2$", (40, 1), (16, 1.35), fontsize=8.6, arrowprops=dict(arrowstyle="->", color=MUTED))
c.set_ylim(0.6, 1.7); c.set_yticks([]); c.set_xlabel("$n$"); c.legend(fontsize=8.2, loc="upper right")
c.set_title("C  40 good cases, then a failure", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Numbers in scripts/pa_numbers2.py. A: the sequence is 1, 2, 4, 8, 16, 31, 57, 99, ... B: $s_n\\leq2-1/n$ for all $n$ (proved by induction in PA08 §5).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa08_induction2")
