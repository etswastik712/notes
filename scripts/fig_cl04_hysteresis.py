"""CL04 - hysteresis of the ramp-albedo model: equilibrium T versus the solar constant S (emissivity 0.6 as on slide 47).

For each S solve  S/4 (1-alpha(T)) = 0.6 sigma T^4.  Stable branches solid, the unstable middle branch dashed.
Prints the two fold (saddle-node) values of S, which are the tipping points.
"""
from scipy.optimize import brentq

from figlib import *

EPS = 0.6


def alpha(T):
    T = np.asarray(T, float)
    return np.where(T < 253, 0.7, np.where(T <= 293, 0.7 - 0.5 * (T - 253) / 40.0, 0.2))


def net(T, S):
    return S / 4 * (1 - alpha(T)) - EPS * SIGMA * np.asarray(T, float) ** 4


Tgrid = np.linspace(180, 340, 3201)


def states(S):
    n = net(Tgrid, S)
    out = []
    for i in range(len(Tgrid) - 1):
        if n[i] * n[i + 1] < 0:
            r = brentq(lambda x: float(net(x, S)), Tgrid[i], Tgrid[i + 1])
            sl = (float(net(r + 0.01, S)) - float(net(r - 0.01, S))) / 0.02
            out.append((r, sl < 0))
    return out


Ss = np.linspace(900, 1900, 1001)
cold, mid, warm = [], [], []
for S in Ss:
    st = states(S)
    for r, stab in st:
        (warm if (stab and r > 270) else cold if stab else mid).append((S, r))
cold, mid, warm = (np.array(x) for x in (cold, mid, warm))
S_warm_lost = warm[:, 0].min()          # lowest S at which the ice-free branch still exists
S_cold_lost = cold[:, 0].max()          # highest S at which the snowball branch still exists
print(f"ice-free branch exists for S >= {S_warm_lost:.0f} W/m2 ({S_warm_lost/S0:.3f} S0);"
      f" snowball branch exists for S <= {S_cold_lost:.0f} W/m2 ({S_cold_lost/S0:.3f} S0)")

fig, ax = plt.subplots(figsize=(7.2, 4.4))
ax.plot(warm[:, 0] / S0, warm[:, 1], color=ORANGE, label="ice-free (stable)")
ax.plot(cold[:, 0] / S0, cold[:, 1], color=BLUE, label="snowball (stable)")
ax.plot(mid[:, 0] / S0, mid[:, 1], color=MUTED, ls="--", label="unstable")
ax.axvline(1.0, color=GRID, lw=1.2)
ax.annotate("today", (1.0, 212), ha="center", fontsize=8.5, color=MUTED)
ax.annotate("tipping point:\nice-free state vanishes\nas S decreases", (S_warm_lost / S0, warm[warm[:, 0].argmin(), 1]),
            xytext=(-12, -50), textcoords="offset points", ha="right", fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.annotate("tipping point:\nsnowball state vanishes\nas S increases", (S_cold_lost / S0, cold[cold[:, 0].argmax(), 1]),
            xytext=(12, 30), textcoords="offset points", ha="left", fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.set_xlabel(r"solar constant  $S/S_0$   ($S_0=1361$ W m$^{-2}$)")
ax.set_ylabel("steady global-mean temperature (K)")
ax.set_title("Hysteresis: the same Sun can hold two different climates")
ax.set_xlim(0.66, 1.4)
ax.set_ylim(190, 340)
ax.legend(loc="upper left", fontsize=8.5)
save(fig, "fig_cl04_hysteresis")
