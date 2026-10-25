"""CL04 - the 'ball in a valley' picture of the ramp-albedo model.

Net heating N(T) = S/4 (1-alpha(T)) - 0.6 sigma T^4  [W m-2] plays the role of a force:  C dT/dt = N(T) = -dU/dT.
U(T) = -integral N dT is a potential: stable states are valley bottoms, the unstable state is the hilltop between them.
Three panels: S = S0 (two valleys), 0.94 S0 (the warm valley is shallow), 0.90 S0 (it has vanished: tipping).
"""
from scipy.integrate import cumulative_trapezoid

from figlib import *

EPS = 0.6


def alpha(T):
    T = np.asarray(T, float)
    return np.where(T < 253, 0.7, np.where(T <= 293, 0.7 - 0.5 * (T - 253) / 40.0, 0.2))


T = np.linspace(190, 330, 2801)
fig, axs = plt.subplots(1, 3, figsize=(10.4, 3.7), sharey=True)
panels = [(1.00, "S = S₀ (today)"), (0.94, "S = 0.94 S₀"), (0.90, "S = 0.90 S₀")]
for ax, (f, title) in zip(axs, panels):
    N = f * S0 / 4 * (1 - alpha(T)) - EPS * SIGMA * T**4
    U = -cumulative_trapezoid(N, T, initial=0)
    U -= U.min()
    ax.plot(T, U, color=INK, lw=2)
    # equilibria: sign changes of N
    idx = np.where(np.sign(N[:-1]) != np.sign(N[1:]))[0]
    for i in idx:
        stable = N[i] > 0            # N goes + to - : valley
        ax.plot([T[i]], [U[i]], "o", ms=9, mfc=(BLUE if stable else SURFACE), mec=INK, mew=1.6, zorder=5)
    ax.set_title(title, fontsize=10)
    ax.set_xlabel("T (K)")
    ax.set_xlim(190, 330)
    ax.grid(axis="y", visible=False)
axs[0].set_ylabel("potential U(T)  (arbitrary zero, W m$^{-2}$ K)")
axs[0].set_ylim(-120, 1750)
axs[0].annotate("snowball\nvalley", (234, 0.0), xytext=(233, 400), textcoords="data", ha="center", fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
axs[0].annotate("hilltop\n(unstable)", (274, 720), xytext=(274, 960), textcoords="data", ha="center", fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
axs[0].annotate("ice-free\nvalley", (299, 430), xytext=(314, 900), textcoords="data", ha="center", fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
axs[1].annotate("warm valley\nis shallow", (294, 1070), xytext=(300, 1500), textcoords="data", ha="center", fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
axs[2].annotate("warm valley gone:\nonly the snowball\nvalley is left", (228, 0.0), xytext=(262, 120), textcoords="data", ha="left", fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
fig.suptitle("A ball (the planet's temperature) rolls downhill: the warm valley fills in as the Sun dims", fontsize=11, fontweight="semibold", y=1.03)
fig.tight_layout()
save(fig, "fig_cl04_potential")
