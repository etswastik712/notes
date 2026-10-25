"""CL02 - isotopic thermometer: a Rayleigh-distillation model of delta-18O of precipitation versus temperature.

An air parcel leaves the ocean at T0 = 20 C and cools; vapour is removed as rain/snow as soon as it condenses (Rayleigh).
  * equilibrium fractionation (Majoube): liquid-vapour  ln a = 1137/T^2 - 0.4156/T - 0.0020667     (T > 0 C)
                                          ice-vapour     ln a = 11.839/T - 0.028244                 (T < 0 C)
  * fraction of vapour left F = e_s(T)/e_s(T0) with the Magnus saturation vapour pressure (constant relative humidity)
  * d ln R_v / d ln F = a - 1  ,  precipitation  R_p = a R_v ,  delta = (R/R_std - 1) 1000
Idealised (no kinetic effects, no mixing, no temperature-dependent source); compare with the empirical spatial relation of
Dansgaard (1964): delta18O = 0.695 T_annual - 13.6 permil.
Prints the model slope.
"""
from figlib import *


def alpha(T):                                      # T in kelvin
    la_l = 1137.0 / T**2 - 0.4156 / T - 0.0020667
    la_i = 11.839 / T - 0.028244
    return np.where(T > 273.15, np.exp(la_l), np.exp(la_i))


def es(Tc):                                        # Magnus, hPa
    return np.where(Tc > 0, 6.112 * np.exp(17.62 * Tc / (243.12 + Tc)), 6.112 * np.exp(22.46 * Tc / (272.62 + Tc)))


T0 = 20.0
Tc = np.linspace(T0, -45, 1301)
F = es(Tc) / es(T0)
a = alpha(Tc + 273.15)
a0 = alpha(np.array(T0 + 273.15))
d0 = (1 / a0 - 1) * 1000                           # first vapour: in equilibrium with 0 permil ocean
R = np.empty_like(Tc)
R[0] = 1 + d0 / 1000
for i in range(1, len(Tc)):
    R[i] = R[i - 1] * np.exp((a[i] - 1) * (np.log(F[i]) - np.log(F[i - 1])))
d_p = (a * R - 1) * 1000
k = (Tc <= -5) & (Tc >= -40)
slope = np.polyfit(Tc[k], d_p[k], 1)[0]
print(f"initial vapour delta = {d0:.1f} permil; precipitation delta at 0 C {np.interp(0, Tc[::-1], d_p[::-1]):.1f}, -20 C {np.interp(-20, Tc[::-1], d_p[::-1]):.1f}, -40 C {np.interp(-40, Tc[::-1], d_p[::-1]):.1f}")
print(f"model slope (-5..-40 C): {slope:.2f} permil per C;  fractionation (a-1)*1000 at 20 C {(a0-1)*1000:.1f}, at -20 C {(alpha(np.array(253.15))-1)*1000:.1f}")

fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.9))
ax = axs[0]
ax.plot(Tc, d_p, color=BLUE, lw=2, label="Rayleigh model (idealised)")
tt = np.array([-45, 0.0])
ax.plot(tt, 0.695 * tt - 13.6, color=ORANGE, lw=1.8, ls="--", label="Dansgaard (1964): 0.695 T − 13.6")
ax.set_xlabel("condensation temperature T (°C)")
ax.set_ylabel("δ¹⁸O of precipitation (‰)")
ax.set_title("Colder ⇒ isotopically lighter", fontsize=10)
ax.legend(loc="lower right", fontsize=8)
ax.invert_xaxis()
ax.annotate(f"model slope ≈ {slope:.2f} ‰ per °C", (-10, -45), fontsize=8.5, ha="right")
ax = axs[1]
Tk = np.linspace(-50, 30, 200) + 273.15
ax.plot(Tk - 273.15, (alpha(Tk) - 1) * 1000, color=INK, lw=2)
ax.axvline(0, color=GRID, lw=1)
ax.annotate("liquid–vapour", (15, 10.3), fontsize=8.5, ha="center", xytext=(0, 8), textcoords="offset points")
ax.annotate("ice–vapour", (-30, 21.5), fontsize=8.5, ha="center", xytext=(0, 8), textcoords="offset points")
ax.set_xlabel("T (°C)")
ax.set_ylabel("fractionation (α − 1) × 1000  (‰)")
ax.set_title("The heavy isotope condenses preferentially, more so when cold", fontsize=10)
fig.tight_layout()
save(fig, "fig_cl02_d18o")
