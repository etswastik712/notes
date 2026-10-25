"""CL14 - IDEALISED zonal-mean zonal wind built from thermal-wind balance (NOT data).

Idea: prescribe a smooth equator-to-pole temperature contrast in the troposphere (reversed in the stratosphere),
integrate the thermal-wind relation upward from a weak surface wind:

    u(phi, z) = u_s(phi) exp(-z/3 km)  -  integral_0^z  [ g / (f T0) ] (1/a) dT/dphi  A(z') dz'

with f = 2 Omega sin(phi) (regularised near the equator), T0 = 250 K, and A(z) = +1 in the troposphere, falling to a
reversed (negative) contrast above the tropopause.  Two parameters per hemisphere: contrast dT (tropics minus pole) and
the latitude phi_c of the steepest temperature gradient.  Annual: 12 K at 40 deg; winter hemisphere: 14.5 K at 33 deg; summer hemisphere: 8.5 K at 46 deg (the pattern M&P describe: ~30 m/s subtropical jet at ~30 deg in
winter, a weaker jet near 45 deg in summer).  The panels mimic the layout of Suhas's slides (annual / DJF / JJA).
"""
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm

from figlib import *

a = R_EARTH
phi_deg = np.linspace(-90, 90, 721)
phi = np.radians(phi_deg)
z = np.linspace(0, 16e3, 321)          # m
T0 = 250.0


def dTdphi(dT, phic_deg, w_deg=9.0):
    """d/dphi of T(phi) = -(dT/2)[1 + tanh((|phi|-phic)/w)] applied per hemisphere (tropics warm, pole cold)."""
    ap = np.abs(phi_deg)
    dT_dabs = -(dT / 2) / np.cosh((ap - phic_deg) / w_deg) ** 2 / np.radians(w_deg)   # per radian of |phi|
    return np.sign(phi_deg) * dT_dabs


def A_of_z(zz):
    # +1 in the troposphere, reversed (stratospheric) contrast above ~12 km
    return 0.5 * (1 - np.tanh((zz - 11.5e3) / 1.3e3)) - 0.45 * 0.5 * (1 + np.tanh((zz - 12.5e3) / 1.5e3))


def ubar(dT_nh, pc_nh, dT_sh, pc_sh):
    f = 2 * OMEGA * np.where(phi_deg >= 0, 1.0, -1.0) * np.maximum(np.abs(np.sin(phi)), np.sin(np.radians(7)))
    g_nh = dTdphi(dT_nh, pc_nh)
    g_sh = dTdphi(dT_sh, pc_sh)
    grad = np.where(phi_deg >= 0, g_nh, g_sh) / a                 # dT/dy in K/m
    shear = -(G0 / (f * T0))[:, None] * grad[:, None] * A_of_z(z)[None, :]      # du/dz  (phi x z)
    u_int = np.cumsum(shear, axis=1) * (z[1] - z[0])
    # weak 'background' wind: tropical easterlies (persist through the troposphere: the tropical temperature
    # gradient is ~0, so there is almost no shear) + shallow surface westerlies in mid-latitudes (friction layer)
    trop = -5.0 * np.exp(-(phi_deg / 22.0) ** 2)
    trop_z = 0.5 * (1 - np.tanh((z - 14e3) / 1.5e3))
    mid = 4.0 * np.exp(-((np.abs(phi_deg) - 50.0) / 12.0) ** 2)
    return trop[:, None] * trop_z[None, :] + mid[:, None] * np.exp(-z / 3e3)[None, :] + u_int


cases = [("Annual mean (idealised)", (12, 40, 12, 40)),
         ("DJF: NH winter (idealised)", (14.5, 33, 8.5, 46)),
         ("JJA: SH winter (idealised)", (8.5, 46, 14.5, 33))]
cmap = LinearSegmentedColormap.from_list("wind", ["#b45f06", "#e8b87a", "#f4f3ef", "#9ed3b6", "#1b8a5a", "#0b4f33"])
levels = np.arange(-12.5, 47.6, 5)
norm = TwoSlopeNorm(vmin=-12.5, vcenter=0, vmax=47.5)

fig, axs = plt.subplots(3, 1, figsize=(7.2, 9.6), sharex=True)
for ax, (title, p) in zip(axs, cases):
    U = ubar(*p)
    cs = ax.contourf(phi_deg, z / 1e3, U.T, levels=levels, cmap=cmap, norm=norm, extend="both")
    ax.contour(phi_deg, z / 1e3, U.T, levels=levels, colors="k", linewidths=0.35)
    ax.contour(phi_deg, z / 1e3, U.T, levels=[-0.01], colors="k", linewidths=1.0, linestyles="--")
    i, j = np.unravel_index(np.argmax(U), U.shape)
    ax.plot([phi_deg[i]], [z[j] / 1e3], "o", mfc="white", mec="k", ms=6)
    ax.annotate(f"max {U.max():.0f} m/s", (phi_deg[i], z[j] / 1e3), xytext=(6, 8), textcoords="offset points", fontsize=8.5)
    # the other hemisphere's maximum
    U2 = U.copy()
    if phi_deg[i] > 0:
        U2[phi_deg > 0] = -99
    else:
        U2[phi_deg < 0] = -99
    i2, j2 = np.unravel_index(np.argmax(U2), U2.shape)
    ax.plot([phi_deg[i2]], [z[j2] / 1e3], "o", mfc="white", mec="k", ms=6)
    ax.annotate(f"max {U2.max():.0f} m/s", (phi_deg[i2], z[j2] / 1e3), xytext=(6, 8), textcoords="offset points", fontsize=8.5)
    ax.axhline(11.8, color=MUTED, lw=0.8, ls=":")
    ax.annotate("≈ 200 hPa", (-88, 12.1), fontsize=8, color=MUTED)
    ax.set_title(title, fontsize=10)
    ax.set_ylabel("height (km)")
    ax.grid(False)
    print(title, "max NH %.1f SH %.1f" % (U[phi_deg > 0].max(), U[phi_deg < 0].max()),
          "lat of NH max %.0f" % phi_deg[np.unravel_index(np.argmax(np.where(phi_deg[:, None] > 0, U, -99)), U.shape)[0]],
          "| surface tropics %.1f" % U[360, 0])
axs[-1].set_xlabel("latitude (°)  (S ← → N)")
axs[-1].set_xticks(np.arange(-90, 91, 30))
cb = fig.colorbar(cs, ax=axs, orientation="horizontal", fraction=0.03, pad=0.07, ticks=np.arange(-10, 46, 10))
cb.set_label("zonal-mean zonal wind  $\\bar u$ (m s$^{-1}$)   green = westerly, brown = easterly")
fig.suptitle("Thermal-wind jets from a prescribed temperature contrast (idealised, not data)", fontsize=11, fontweight="semibold", y=0.995)
save(fig, "fig_cl14_idealised_ubar")
