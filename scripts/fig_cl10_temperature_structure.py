"""CL10 - idealised annual-mean zonal-mean temperature T and potential temperature theta (latitude-height).

Model atmosphere (NOT observations; Figs. 5.7-5.8 of Marshall & Plumb are not in the excerpt): surface temperature
T_s = 300 - 40 sin^2(phi); tropospheric lapse rate 6.5 K/km up to a tropopause z_T = 8 + 8 cos^2(phi) km, then +1 K/km;
p(z) by hydrostatic integration; theta = T (1000 hPa / p)^(R/cp).  Chosen to reproduce the quoted statements:
T falls upward and poleward, surface T < 0 C poleward of ~60 deg, max ~27 C at the equator, ~40 K pole-equator
difference through the troposphere, tropopause higher in the tropics, isentropes slope upward toward the pole, theta increases with height.
"""
from figlib import *

KAPPA = 0.2857
Rd, g = 287.0, 9.81
lat = np.linspace(-90, 90, 181)
phi = np.radians(lat)
z = np.linspace(0, 24, 241)              # km
Ts = 300 - 40 * np.sin(phi) ** 2
zT = 8 + 8 * np.cos(phi) ** 2
T = np.zeros((len(z), len(lat)))
for j in range(len(lat)):
    tropo = Ts[j] - 6.5 * z
    TT = Ts[j] - 6.5 * zT[j]
    T[:, j] = np.where(z <= zT[j], tropo, TT + 1.0 * (z - zT[j]))
dz = (z[1] - z[0]) * 1000
lnp = np.zeros_like(T)
lnp[0] = np.log(1000.0)
for k in range(1, len(z)):
    Tm = 0.5 * (T[k] + T[k - 1])
    lnp[k] = lnp[k - 1] - g * dz / (Rd * Tm)
p = np.exp(lnp)
theta = T * (1000.0 / p) ** KAPPA

j0, j90, j60 = 90, 180, 150
k5 = np.argmin(abs(z - 5))
print(f"T_s equator {Ts[j0]-273.15:.0f} C; 60 deg {Ts[j60]-273.15:.0f} C; pole {Ts[j90]-273.15:.0f} C")
print(f"troposphere equator-pole difference at 5 km: {T[k5, j0]-T[k5, j90]:.0f} K")
print(f"tropopause: equator {zT[j0]:.0f} km (T={T[np.argmin(abs(z-zT[j0])), j0]:.0f} K), pole {zT[j90]:.0f} km (T={T[np.argmin(abs(z-zT[j90])), j90]:.0f} K)")
for lev in (300, 320, 340):
    zz = [z[np.argmin(abs(theta[:, j] - lev))] for j in (j0, j60, j90)]
    print(f"height of theta={lev} K surface: eq {zz[0]:.1f} km, 60 deg {zz[1]:.1f} km, pole {zz[2]:.1f} km")
print(f"theta at 8 km: equator {theta[np.argmin(abs(z-8)), j0]:.0f} K, pole {theta[np.argmin(abs(z-8)), j90]:.0f} K;  d(theta)/dz > 0 everywhere: {bool((np.diff(theta, axis=0) > 0).all())}")

fig, (a, b) = plt.subplots(1, 2, figsize=(10.6, 4.3), sharey=True)
cs = a.contourf(lat, z, T, levels=np.arange(190, 305, 10), cmap="YlOrRd", extend="both")
cl = a.contour(lat, z, T, levels=np.arange(190, 305, 10), colors=INK, linewidths=0.5)
a.clabel(cl, fmt="%d", fontsize=7)
a.plot(lat, zT, color=INK, lw=2.0, ls="--")
a.annotate("tropopause", (-78, 15.3), fontsize=9, color=INK)
a.set_title("Temperature T (K): falls upward and poleward")
fig.colorbar(cs, ax=a, pad=0.02, fraction=0.05, label="K")
levels = list(range(280, 340, 10)) + list(range(340, 520, 20))
cs2 = b.contour(lat, z, theta, levels=levels, colors=[BLUE], linewidths=1.1)
b.clabel(cs2, fmt="%d", fontsize=7)
b.plot(lat, zT, color=INK, lw=2.0, ls="--")
box = dict(fc=SURFACE, ec="none", alpha=0.9, pad=1.5)
b.annotate("isentropes rise\ntoward the pole", (36, 3.2), fontsize=8.5, color=INK, ha="left", bbox=box)
b.annotate("closely spaced\n(stratosphere)", (-84, 20.5), fontsize=8.5, color=INK, bbox=box)
b.annotate("widely spaced\n(troposphere)", (-84, 1.2), fontsize=8.5, color=INK, bbox=box)
b.set_title("Potential temperature θ (K): always increases with height")
for ax in (a, b):
    ax.set_xticks(range(-90, 91, 30))
    ax.set_xlabel("latitude (°)")
    ax.grid(False)
a.set_ylabel("height (km)")
fig.tight_layout()
save(fig, "fig_cl10_temperature_structure")
