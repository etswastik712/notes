"""CL09 - saturated (moist) adiabatic lapse rate and a tropical parcel.

Gamma_s = g (1 + L r_s/(R_d T)) / (c_p + L^2 r_s eps/(R_d T^2)),  r_s = eps e_s/(p - e_s),  e_s from Bolton (1980);
(derivation: W&H Exercise 3.50 / CL09 callout).  Right: a saturated parcel lifted from 1000 hPa, 300 K,
vs the dry adiabat and the observed-mean 6.5 K/km.
"""
from scipy.integrate import solve_ivp

from figlib import *

g, cp, Rd, eps = 9.81, 1004.0, 287.0, 0.622


def Lv(T):
    return 2.501e6 - 2370.0 * (T - 273.15)


def es(T):                                       # Pa (Bolton 1980)
    return 611.2 * np.exp(17.67 * (T - 273.15) / (T - 29.65))


def Gam_s(T, p):                                 # K/m
    rs = eps * es(T) / (p - es(T))
    L = Lv(T)
    return g * (1 + L * rs / (Rd * T)) / (cp + L**2 * rs * eps / (Rd * T**2))


for Tc, p in ((20, 1000e2), (0, 800e2), (-20, 500e2), (-40, 300e2)):
    print(f"Gamma_s({Tc:+d} C, {p/100:.0f} hPa) = {Gam_s(Tc+273.15, p)*1e3:.2f} K/km")


def rhs(z, y):
    T, p = y
    return [-Gam_s(T, p), -p * g / (Rd * T)]


sol = solve_ivp(rhs, (0, 16000), [300.0, 1.0e5], max_step=50, dense_output=True)
zz = np.linspace(0, 16000, 400)
Tm, pm = sol.sol(zz)
zT220 = np.interp(-220, -Tm, zz)
print(f"moist adiabat from 300 K: T = 220 K at z = {zT220/1e3:.1f} km (p = {np.interp(zT220, zz, pm)/100:.0f} hPa);"
      f" T(10 km) = {np.interp(10e3, zz, Tm):.1f} K; T(16 km) = {Tm[-1]:.1f} K; mean lapse 0-10 km = {(300-np.interp(10e3, zz, Tm))/10:.2f} K/km")
print(f"dry adiabat from 300 K: T(10 km) = {300-9.8*10:.0f} K ; reaches 220 K at {80/9.8:.1f} km")

fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 4.5))
T = np.linspace(223, 305, 200)
for p, c in ((1000e2, BLUE), (700e2, AQUA), (500e2, VIOLET), (300e2, ORANGE)):
    a.plot(T - 273.15, Gam_s(T, p) * 1e3, color=c, label=f"{p/100:.0f} hPa")
a.axhline(9.8, color=MUTED, ls=":", lw=1.2)
a.annotate(r"dry value $\Gamma_d$ = 9.8", (-48, 9.8), xytext=(0, 5), textcoords="offset points", fontsize=8.5, color=MUTED)
a.set_xlabel("temperature (°C)")
a.set_ylabel(r"saturated adiabatic lapse rate $\Gamma_s$ (K km$^{-1}$)")
a.set_title("Latent heat shrinks the lapse rate", fontsize=10.5)
a.set_ylim(2, 11)
a.legend(title="pressure", fontsize=8.2, loc="lower left", title_fontsize=8.2)

b.plot(Tm, zz / 1e3, color=BLUE, lw=2.2, label="moist adiabat (saturated parcel)")
b.plot(300 - 9.8 * zz / 1e3, zz / 1e3, color=ORANGE, lw=2.0, label="dry adiabat")
b.plot(300 - 6.5 * zz / 1e3, zz / 1e3, color=MUTED, lw=1.4, ls="--", label="6.5 K km$^{-1}$ (observed mean)")
b.axvline(220, color=MUTED, lw=0.8, ls=":")
b.plot([220], [zT220 / 1e3], "o", color=BLUE, ms=6, label=f"{220} K (deep cloud top) at {zT220/1e3:.1f} km")
b.set_xlim(190, 305)
b.set_ylim(0, 16)
b.set_xlabel("temperature (K)")
b.set_ylabel("height (km)")
b.set_title("A tropical parcel from 300 K", fontsize=10.5)
b.legend(fontsize=8.2, loc="upper right")
fig.tight_layout()
save(fig, "fig_cl09_moist_adiabat")
