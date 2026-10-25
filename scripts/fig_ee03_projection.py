"""EE03 - Turchin & Taylor's point in miniature: a second-order (delayed density dependence) system that fluctuates
persistently looks 'stable' when analysed with a first-order Ricker regression.
True model (illustrative): N_{t+1} = N_t exp( r (1 - (N_t + b N_{t-1}) / (K (1+b))) ), r=1.6, b=3, K=100."""
from figlib import *

K, r, b = 100.0, 1.6, 3.0
x = [40.0, 60.0]
for _ in range(400):
    x.append(x[-1] * np.exp(r * (1 - (x[-1] + b * x[-2]) / (K * (1 + b)))))
x = np.array(x)
tail = x[-300:]
yy = np.log(tail[1:] / tail[:-1])
A = np.vstack([np.ones(299), tail[:-1]]).T
coef = np.linalg.lstsq(A, yy, rcond=None)[0]
r_hat = coef[0]; Khat = -coef[0] / coef[1]
fig, (a, b2, c) = plt.subplots(1, 3, figsize=(11.0, 3.7))
a.plot(range(80), tail[:80], "-o", color=RED, ms=2.8, lw=1)
a.axhline(K, color=MUTED, ls=":", lw=1)
a.set_title("true dynamics (two lags): persistent fluctuations", fontsize=10); a.set_xlabel("generation"); a.set_ylabel(r"$N_t$")
b2.plot(tail[:-1], yy, ".", color=RED, ms=4)
nn = np.linspace(tail.min(), tail.max(), 50)
b2.plot(nn, coef[0] + coef[1] * nn, color=BLUE, lw=2)
b2.set_title("one-lag Ricker regression of ln(N$_{t+1}$/N$_t$)", fontsize=10); b2.set_xlabel(r"$N_t$"); b2.set_ylabel(r"$\ln(N_{t+1}/N_t)$")
b2.text(15, 1.62, "points trace a loop; a straight\nline fits poorly (R² = 0.30)", fontsize=8.3); b2.set_ylim(-2.0, 2.05)
sim = [40.0]
for _ in range(79):
    sim.append(sim[-1] * np.exp(coef[0] + coef[1] * sim[-1]))
c.plot(range(80), sim, "-o", color=BLUE, ms=2.8, lw=1)
c.axhline(Khat, color=MUTED, ls=":", lw=1)
c.set_title("what the one-lag fit predicts: smooth damping", fontsize=10); c.set_xlabel("generation")
c.set_ylim(0, 250); a.set_ylim(0, 250)
fig.tight_layout(); save(fig, "fig_ee03_projection")
print("fit: r_hat=%.3f K_hat=%.1f  implied f'(K)=%.3f" % (r_hat, Khat, 1 - r_hat))
