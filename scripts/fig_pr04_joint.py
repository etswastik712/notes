"""PR04 - the joint pmf of (sum, max) of two dice with its marginals, and the coupon collector."""
from figlib import *
import itertools, math

fig, axes = plt.subplots(1, 3, figsize=(11.8, 4.0), gridspec_kw=dict(width_ratios=[1.25, 0.9, 1.0]))
a = axes[0]
H = np.zeros((6, 11))
for d1, d2 in itertools.product(range(1, 7), repeat=2): H[max(d1, d2) - 1, d1 + d2 - 2] += 1
H /= 36
im = a.imshow(H, origin="lower", cmap="Blues", aspect="auto", extent=(1.5, 12.5, 0.5, 6.5))
for m in range(6):
    for s in range(11):
        if H[m, s] > 0: a.text(s + 2, m + 1, f"{int(round(H[m, s] * 36))}", ha="center", va="center", fontsize=8.2, color=INK if H[m, s] < 0.045 else "white")
a.set_xlabel("sum $X_1$"); a.set_ylabel("maximum $X_2$"); a.set_xticks(range(2, 13)); a.set_yticks(range(1, 7)); a.grid(False)
a.set_title("A  joint pmf of (sum, max), in 36ths", fontsize=10)
b = axes[1]
x = np.arange(2, 13); psum = np.array([6 - abs(s - 7) for s in x]) / 36
b.bar(x, psum, color=BLUE); b.set_xlabel("sum"); b.set_ylabel("marginal pmf of the sum"); b.set_xticks(x)
b.text(12.3, 0.145, "mean 7\nvar 35/6", ha="right", fontsize=8.6)
b.set_title("B  marginal; $E[X_1+X_1']=7$", fontsize=10)
c = axes[2]
Ns = np.arange(2, 61)
c.plot(Ns, [N * sum(1 / i for i in range(1, N + 1)) for N in Ns], color=BLUE, label=r"$E[T]=N\,H_N$")
c.plot(Ns, Ns * (np.log(Ns) + 0.5772), "--", color=ORANGE, lw=1.2, label=r"$N(\ln N+\gamma)$")
for N in (6, 50):
    v = N * sum(1 / i for i in range(1, N + 1)); c.plot([N], [v], "o", color=INK, ms=5); c.text(N + 1, v - 15 if N == 50 else v + 12, f"N={N}: {v:.1f}", fontsize=8.4)
c.set_xlabel("number of coupon types $N$"); c.set_ylabel("expected draws to collect all"); c.legend(fontsize=8.4, loc="upper left")
c.set_title("C  coupon collector, by linearity", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "A: $X_1$ and $X_2$ are not independent ($\\mathrm{Cov}=2.917$); $P(X_1=7,X_2=5)=2/36=1/18$. C: $T=\\sum T_i$ with $T_i\\sim$ Geometric$((N-i+1)/N)$.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_pr04_joint")
