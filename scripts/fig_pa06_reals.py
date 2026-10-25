"""PA06 - completeness in action: Newton rationals for sqrt 2, nested bisection intervals, and a Cauchy vs non-Cauchy series."""
from figlib import *
from fractions import Fraction as Fr
import math

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.0))
a = axes[0]
x = Fr(1); err1 = []; u = Fr(1); err2 = []
for _ in range(7):
    err1.append(abs(float(x) - math.sqrt(2)) + 1e-17); x = (x + 2 / x) / 2
    err2.append(abs(float(u) - math.sqrt(2)) + 1e-17); u = (2 * u + 2) / (u + 2)
a.semilogy(range(7), err1, "o-", color=BLUE, label="Newton: x → (x + 2/x)/2"); a.semilogy(range(7), err2, "s-", color=ORANGE, label="u → (2u+2)/(u+2)")
a.set_xlabel("step"); a.set_ylabel("|x − √2|"); a.legend(fontsize=8.2, loc="lower left"); a.set_title("A  Cauchy sequences of rationals (limit not in Q)", fontsize=10)
b = axes[1]
lo, hi = 1.0, 2.0
for k in range(7):
    b.plot([lo, hi], [k, k], color=BLUE, lw=5, solid_capstyle="butt")
    mid = (lo + hi) / 2
    if mid * mid < 2: lo = mid
    else: hi = mid
b.axvline(math.sqrt(2), color=ORANGE, lw=1.4); b.text(math.sqrt(2) + 0.02, 6.4, "√2", color=ORANGE, fontsize=9)
b.set_ylim(6.7, -0.7); b.set_yticks(range(7)); b.set_xlabel("x"); b.set_ylabel("step n"); b.set_title("B  nested intervals [aₙ, bₙ], width 2⁻ⁿ", fontsize=10)
c = axes[2]
n = np.arange(1, 2001)
c.plot(n, np.cumsum(1 / n), color=ORANGE, label=r"$H_n=\sum 1/k$ (not Cauchy)"); c.plot(n, np.cumsum(1 / n ** 2), color=BLUE, label=r"$\sum 1/k^2$ (Cauchy)")
c.axhline(math.pi ** 2 / 6, color=BLUE, lw=0.8, ls="--"); c.text(1000, 1.72, r"$\pi^2/6$", fontsize=8.6)
c.set_xlabel("n"); c.legend(fontsize=8.2, loc="center right"); c.set_title("C  the Cauchy criterion", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: Newton's error squares each step (4.1e-1, 8.6e-2, 2.5e-3, 2.1e-6, 1.6e-12); the other map gains a constant factor. C: H_2n − H_n ≥ 1/2 for all n, so H_n is not Cauchy (H_2000 = 8.18).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pa06_reals")
