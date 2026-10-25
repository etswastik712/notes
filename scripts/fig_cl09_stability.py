"""CL09 - the parcel method: a dry parcel displaced upward in environments with different lapse rates, and the
resulting buoyancy oscillation  d2z/dt2 = -N^2 z,  N^2 = (g/T)(Gamma_d - Gamma)   (Wallace & Hobbs Eqs. 3.73-3.75; M&P Problem 1).
"""
from figlib import *

G0_, CPD = 9.81, 1004.0
Gd = G0_ / CPD * 1e3                                    # K/km
T0 = 280.0
cases = [("stable", 4.0, BLUE), ("neutral", Gd, MUTED), ("unstable", 14.0, ORANGE)]

fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 4.4), gridspec_kw={"width_ratios": [1.0, 1.15]})
z = np.linspace(0, 3, 50)
z0, dz = 1.0, 0.5                                       # parcel starts in equilibrium at 1 km, is pushed up to 1.5 km
for nm, Gam, c in cases:
    Te = T0 - Gam * z
    a.plot(Te, z, color=c, lw=2, label=f"{nm}: environment {Gam:.1f} K/km")
    Tp1 = (T0 - Gam * z0) - Gd * dz                      # parcel temperature after lifting
    a.plot([Tp1], [z0 + dz], "o", color=c, ms=7, mfc="white", mew=2)
    a.plot([T0 - Gam * z0, Tp1], [z0, z0 + dz], color=c, lw=1.2, ls="--")
    buoy = (T0 - Gam * (z0 + dz)) - Tp1
    print(f"{nm}: Gamma={Gam:.1f}  parcel after +0.5 km is {-buoy:+.2f} K relative to its surroundings"
          f" (positive = warmer, accelerates up); N^2 = {G0_/T0*(Gd-Gam)*1e-3:.2e} s^-2")
a.set_xlim(253, 283)
a.set_ylim(0.6, 2.4)
a.set_xlabel("temperature (K)")
a.set_ylabel("height (km)")
a.set_title("Lift a parcel 0.5 km (dashed: dry adiabat)", fontsize=10.5)

t = np.linspace(0, 20, 600) * 60                          # seconds
d0 = 100.0                                               # initial displacement 100 m
for nm, Gam, c in cases:
    N2 = G0_ / T0 * (Gd - Gam) * 1e-3
    if N2 > 1e-12:
        N = np.sqrt(N2)
        y = d0 * np.cos(N * t)
        lab = f"stable (4 K/km): N = {N:.4f} s$^{{-1}}$, period {2*np.pi/N/60:.1f} min"
        print(f"stable: N={N:.5f} s^-1 period={2*np.pi/N:.0f} s")
    elif N2 < -1e-12:
        s = np.sqrt(-N2)
        y = d0 * np.cosh(s * t)
        lab = f"unstable (14 K/km): grows e-fold in {1/s:.0f} s"
        print(f"unstable: e-folding {1/s:.0f} s")
    else:
        y = d0 + 0 * t
        lab = "neutral (9.8 K/km): stays where pushed"
    b.plot(t / 60, y, color=c, lw=2, label=lab)
b.axhline(0, color=MUTED, lw=0.8)
b.set_ylim(-130, 600)
b.set_xlim(0, 20)
b.set_xlabel("time after release (min)")
b.set_ylabel("displacement from start level (m)")
b.set_title("What happens next", fontsize=10.5)
b.legend(loc="upper left", fontsize=8.2)
fig.tight_layout()
save(fig, "fig_cl09_stability")
