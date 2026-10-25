"""CL07 - Beer-Lambert law: transmission vs optical depth, and the effect of a slant path (air mass)."""
from figlib import *

fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.9))

# (a) transmission vs tau
tau = np.linspace(0, 5, 300)
a.plot(tau, np.exp(-tau), color=BLUE, label=r"transmitted  $e^{-\tau}$")
a.plot(tau, 1 - np.exp(-tau), color=ORANGE, label=r"absorbed  $1-e^{-\tau}$")
a.plot(tau, np.clip(1 - tau, 0, 1), color=MUTED, lw=1, ls=":", label=r"thin-layer limit  $1-\tau$")
for t in (0.1, 1, 3):
    a.plot([t], [np.exp(-t)], "o", color=BLUE, ms=5)
    a.annotate(f"τ={t:g}: {np.exp(-t)*100:.1f} %", (t, np.exp(-t)), xytext=(8, 8), textcoords="offset points", fontsize=8.5)
a.set_xlabel(r"optical depth $\tau$")
a.set_ylabel("fraction of the beam")
a.set_title("Every step removes the same fraction")
a.set_xlim(0, 5)
a.set_ylim(0, 1.05)
a.legend(loc="center right", fontsize=8.5)

# (b) slant path: transmission vs air mass for different vertical tau0
m = np.linspace(1, 10, 200)
for tau0, c in [(0.1, BLUE), (0.3, ORANGE), (1.0, AQUA)]:
    b.plot(m, np.exp(-tau0 * m), color=c, label=rf"$\tau_0={tau0:g}$")
    b.plot([1, 2], [np.exp(-tau0), np.exp(-2 * tau0)], "o", color=c, ms=5)
b.axvline(2, color=MUTED, lw=0.9, ls="--")
b.annotate("60° from zenith\n(air mass 2)", (2, 0.04), xytext=(5, 0), textcoords="offset points", fontsize=8.5, color=MUTED)
b.set_xlabel(r"air mass  $m=\sec\theta$  (1 = overhead)")
b.set_ylabel(r"transmitted  $e^{-\tau_0 m}$")
b.set_title("A slant path multiplies the optical depth")
b.set_xlim(1, 10)
b.set_ylim(0, 1.05)
b.legend(loc="upper right", fontsize=8.5)
fig.tight_layout()
save(fig, "fig_cl07_beer_lambert")
