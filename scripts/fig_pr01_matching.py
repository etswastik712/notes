"""PR01 - the matching (derangement) problem by inclusion-exclusion, and the coincidence probability for random slots."""
from figlib import *
import math

rng = np.random.default_rng(5)
fig, axes = plt.subplots(1, 2, figsize=(10.4, 3.9))
a = axes[0]
ns = np.arange(1, 13)
exact = np.array([sum((-1) ** i / math.factorial(i) for i in range(n + 1)) for n in ns])
a.plot(ns, exact, "o-", color=BLUE, label=r"$\sum_{i=0}^{n}(-1)^i/i!$ (exact)")
mc = [np.mean([(rng.permutation(n) != np.arange(n)).all() for _ in range(20000)]) for n in ns]
a.plot(ns, mc, "x", color=ORANGE, ms=7, label="simulation, 20,000 shuffles")
a.axhline(1 / math.e, color=INK, lw=0.9, ls="--"); a.text(12, 1 / math.e + 0.04, r"$1/e=0.3679$", ha="right", fontsize=8.6)
a.set_xlabel("number of people $n$"); a.set_ylabel("P(nobody gets their own coat)"); a.set_ylim(0, 1.05); a.legend(fontsize=8.2, loc="lower right")
a.set_title("A  inclusion-exclusion converges fast", fontsize=10)
b = axes[1]
k = np.arange(1, 60)
for N, c in ((10, BLUE), (365, ORANGE)):
    kk = np.arange(1, min(N, 60) + 1)
    p = 1 - np.array([math.perm(N, int(x)) / N ** int(x) for x in kk])
    b.plot(kk, p, color=c, label=f"$N={N}$ slots")
b.plot([3], [0.28], "o", color=BLUE, ms=7); b.annotate("3 courses, 10 slots:\n0.28", (3, 0.28), xytext=(10, 0.1), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.plot([23], [1 - math.perm(365, 23) / 365 ** 23], "o", color=ORANGE, ms=7); b.annotate("23 people, 365 days:\n0.507", (23, 0.507), xytext=(30, 0.3), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
b.set_xlabel("number of objects $k$"); b.set_ylabel("P(at least two share a slot)"); b.legend(fontsize=8.4, loc="lower right"); b.set_ylim(0, 1.03)
b.set_title("B  collisions come sooner than intuition says", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: $P=\\sum(-1)^i/i!$ from $P(\\cup A_i)$ with $P(A_{i_1}\\cap\\dots\\cap A_{i_k})=(n-k)!/n!$. B: $1-N!/((N-k)!N^k)$; the 10-slot case is the class example (3 courses, 0.28). All computed.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr01_matching")
