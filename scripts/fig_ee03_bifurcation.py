"""EE03 - bifurcation diagram of the Ricker map (K=100) with the Lyapunov exponent below it."""
from figlib import *

K = 100.0
rs = np.linspace(1.5, 3.8, 1800)
f = lambda n, r: n * np.exp(r * (1 - n / K))
pts_r, pts_n, lam = [], [], []
for r in rs:
    x = 20.0
    for _ in range(600):
        x = f(x, r)
    s, acc = [], 0.0
    for _ in range(300):
        x = f(x, r)
        s.append(x)
        acc += np.log(abs(np.exp(r * (1 - x / K)) * (1 - r * x / K)) + 1e-300)
    pts_r += [r] * len(s[-60:]); pts_n += s[-60:]
    lam.append(acc / 300)
fig, (a, b) = plt.subplots(2, 1, figsize=(8.6, 6.2), sharex=True, gridspec_kw={"height_ratios": [2.2, 1]})
a.plot(pts_r, pts_n, ",", color=INK, alpha=0.5)
a.plot(pts_r, pts_n, ".", color=INK, ms=0.4, alpha=0.5)
for x0 in (2.0, 2.5265, 2.6564, 2.6924):
    a.axvline(x0, color=ORANGE, lw=0.8, ls=":")
a.text(1.99, 352, "r = 2.000: 1 → 2", rotation=90, ha="right", va="top", fontsize=8, color=MUTED)
a.text(2.5165, 352, "2.527: 2 → 4", rotation=90, ha="right", va="top", fontsize=8, color=MUTED)
a.text(2.6464, 352, "2.656: 4 → 8", rotation=90, ha="right", va="top", fontsize=8, color=MUTED)
a.text(2.7024, 352, "2.692: chaos begins", rotation=90, ha="left", va="top", fontsize=8, color=MUTED)
a.set_ylim(0, 360)
a.set_ylabel(r"long-run $N_t$")
a.set_title("Period doubling to chaos in the Ricker model (K = 100)", fontsize=10.5)
b.plot(rs, lam, color=BLUE, lw=0.8)
b.axhline(0, color=MUTED, lw=1)
b.fill_between(rs, lam, 0, where=np.array(lam) > 0, color=RED, alpha=0.25, lw=0)
b.annotate("λ > 0: sensitive dependence (chaos)", (3.0, 0.62), fontsize=8.5)
b.annotate("λ < 0: stable point or cycle", (1.6, -1.5), fontsize=8.5)
b.set_ylim(-2.6, 1.0)
b.set_ylabel("Lyapunov exponent λ")
b.set_xlabel("growth parameter r")
fig.tight_layout(); save(fig, "fig_ee03_bifurcation")
