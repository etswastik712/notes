"""CL03 - diurnal cycle of an airless slab at the sub-solar latitude (Argha L6 slides 69-71).

   rho V C dT/dt = (1-alpha) S max(sin w t, 0) sin... -> here the incoming flux is S(1-alpha) max(sin(wt), 0)
   with t measured from sunrise, minus sigma T^4.   (The deck writes Theta(sin) * sin; same thing.)
   Parameters from the slide:  S = 1361, alpha = 0.31, rho V C = 1500*0.20*2500 = 7.5e5 J m-2 K-1.
"""
from scipy.integrate import solve_ivp

from figlib import *

ALPHA, C = 0.31, 7.5e5
W = 2 * np.pi / 86400.0


def rhs(t, T):
    sw = S0 * (1 - ALPHA) * max(np.sin(W * t), 0.0)
    return (sw - SIGMA * T**4) / C


def run(T0=255.0, days=12):
    t = np.linspace(0, days * 86400, days * 288 + 1)
    sol = solve_ivp(rhs, (0, t[-1]), [T0], t_eval=t, max_step=300, rtol=1e-7)
    return sol.t, sol.y[0]


t, T = run()
last = t >= t[-1] - 86400
tl = (t[last] - t[last][0]) / 3600
Tl = T[last]
sw = S0 * (1 - ALPHA) * np.maximum(np.sin(W * t[last]), 0)
Tmax, tmax = Tl.max(), tl[Tl.argmax()]
print(f"Tmax={Tmax:.1f} K at {tmax:.1f} h after sunrise; Tmin={Tl.min():.1f} K; mean T={Tl.mean():.1f} K")

fig, (a, b) = plt.subplots(2, 1, figsize=(7, 5.2), sharex=True, gridspec_kw={"height_ratios": [1, 1.15]})
a.plot(tl, sw, color=ORANGE, label="absorbed shortwave")
a.plot(tl, SIGMA * Tl**4, color=BLUE, label=r"emitted $\sigma T^4$")
a.set_ylabel("flux (W m$^{-2}$)")
a.legend(loc="upper right", fontsize=8.5)
a.set_title("Airless slab, equator, equinox: the temperature peak lags the Sun")
b.plot(tl, Tl, color=INK)
b.axvline(tmax, color=MUTED, ls=":", lw=1)
b.annotate(f"peak {Tmax:.0f} K at {tmax:.1f} h (local noon = 6 h)", (11.2, 261.3), ha="left", fontsize=8.5)
b.axvline(6, color=ORANGE, ls=":", lw=1)
b.set_ylabel("surface temperature (K)")
b.set_ylim(259, 281)
b.set_xlabel("hours after sunrise")
b.set_xlim(0, 24)
save(fig, "fig_cl03_diurnal")
