"""EE03 - delayed logistic (Hutchinson) dN/dt = rN(1 - N(t - tau)/K): thermostat-with-delay overshoot. Hopf threshold r*tau = pi/2."""
from figlib import *

def run(rtau, tau=1.0, K=1.0, T=45.0, dt=0.001):
    r = rtau / tau
    n = int(T / dt); lag = int(tau / dt)
    N = np.empty(n + lag + 1); N[: lag + 1] = 0.3
    for i in range(lag, n + lag):
        N[i + 1] = N[i] + dt * r * N[i] * (1 - N[i - lag] / K)
    t = (np.arange(n + 1)) * dt
    return t, N[lag: lag + n + 1]

fig, axs = plt.subplots(1, 3, figsize=(11.0, 3.4), sharey=True)
for ax, rtau, col, lab in zip(axs, (1.0, 1.5, 2.0), (BLUE, AQUA, RED), ("rτ = 1.0: damped overshoot", "rτ = 1.5: barely damped (threshold π/2 ≈ 1.571)", "rτ = 2.0: sustained cycle")):
    t, N = run(rtau)
    ax.plot(t, N, color=col, lw=1.4)
    ax.axhline(1.0, color=MUTED, ls=":", lw=1)
    ax.set_title(lab, fontsize=9)
    ax.set_xlabel("time (in units of the delay τ)")
axs[0].set_ylabel("N / K")
fig.tight_layout(); save(fig, "fig_ee03_delay")
t, N = run(2.0)
tail = N[t > 30]; tt = t[t > 30]
pk = tt[1:-1][(tail[1:-1] > tail[:-2]) & (tail[1:-1] > tail[2:])]
print("r*tau=2 peaks (tau=1):", np.round(pk, 2), "period ~", np.round(np.diff(pk), 2), "amplitude range", tail.min().round(3), tail.max().round(3))
