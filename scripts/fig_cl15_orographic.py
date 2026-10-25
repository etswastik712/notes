"""CL15 - orographic rain from a moist onshore flow: lift a saturated-by-lifting parcel (dry adiabat, then pseudo-adiabat).

Parcel: T = 27 C, p = 1000 hPa, RH = 85 % (typical monsoon boundary layer).  Condensate = initial mixing ratio - parcel mixing
ratio after lifting by h.  Rainfall on the windward slope:   P = rho U D dq / L
   (air layer of depth D = 1500 m moving at U = 10 m/s over a windward slope of length L = 50 km, all condensate falling out).
Illustrative, order-of-magnitude numbers (no precipitation efficiency or evaporation).
"""
from figlib import *

g, cp, Rd, Lv, eps = G0, 1004.0, 287.0, 2.5e6, 0.622


def es(T):                                   # hPa, Bolton (1980)
    return 6.112 * np.exp(17.67 * (T - 273.15) / (T - 29.65))


def ws(T, p):
    e = es(T)
    return eps * e / (p - e)


T0, p0, RH = 300.15, 1000.0, 0.85
q0 = RH * ws(T0, p0)
dz = 5.0
z = np.arange(0, 3000 + dz, dz)
T = np.empty_like(z); p = np.empty_like(z); q = np.empty_like(z); sat = np.zeros_like(z, bool)
T[0], p[0], q[0] = T0, p0, q0
for i in range(1, len(z)):
    Tm, pm = T[i - 1], p[i - 1]
    if q[i - 1] < ws(Tm, pm) * 0.9999 and not sat[i - 1]:
        dT = -g / cp * dz
        T[i] = Tm + dT
        p[i] = pm * np.exp(-g * dz / (Rd * 0.5 * (Tm + T[i])))
        q[i] = q[i - 1]
        if q[i] >= ws(T[i], p[i]):
            sat[i] = True
            q[i] = ws(T[i], p[i])
    else:
        w_ = ws(Tm, pm)
        gam = g * (1 + Lv * w_ / (Rd * Tm)) / (cp + Lv**2 * w_ * eps / (Rd * Tm**2))
        T[i] = Tm - gam * dz
        p[i] = pm * np.exp(-g * dz / (Rd * 0.5 * (Tm + T[i])))
        q[i] = ws(T[i], p[i])
        sat[i] = True
lcl = z[np.argmax(sat)]
print(f"q0 = {q0*1e3:.1f} g/kg ; LCL = {lcl:.0f} m (rule of thumb 125 m/K x (T-Td) check below)")
Td = 243.5 * np.log(RH * es(T0) / 6.112) / (17.67 - np.log(RH * es(T0) / 6.112))
print(f"Td = {Td:.1f} C ; 125*(T-Td) = {125*(T0-273.15-Td):.0f} m")
cond = (q0 - q) * 1e3                           # g/kg
rho, U, D, L = 1.1, 10.0, 1500.0, 50e3
P = rho * U * D * (q0 - q) / L * 86400          # mm/day  (kg m-2 s-1 -> mm/day)
for h in (500, 1000, 1500, 2000):
    i = np.argmin(abs(z - h))
    print(f"lift {h} m: T={T[i]-273.15:.1f} C  condensate={cond[i]:.2f} g/kg  P={P[i]:.0f} mm/day")

fig, (a, b, a2) = plt.subplots(1, 3, figsize=(11.2, 3.9))
Tdry = T0 - g / cp * z
a.plot(T - 273.15, z / 1e3, color=INK, label="parcel (dry, then moist adiabat)")
a.plot(Tdry - 273.15, z / 1e3, color=MUTED, ls=":", label="dry adiabat continued")
a.axhline(lcl / 1e3, color=ORANGE, lw=1)
a.annotate(f"condensation level {lcl:.0f} m", (3, lcl / 1e3 + 0.06), fontsize=8.5, color=ORANGE)
a.set_xlabel("parcel temperature (°C)")
a.set_ylabel("height lifted (km)")
a.set_title("Rising air cools; at the\ncondensation level a cloud forms", fontsize=10)
a.legend(loc="upper right", fontsize=7.8)
b.plot(q * 1e3, z / 1e3, color=BLUE)
b.axhline(lcl / 1e3, color=ORANGE, lw=1)
b.set_xlabel("water vapour mixing ratio (g/kg)")
b.set_title("Vapour is conserved below the\nlevel, squeezed out above it", fontsize=10)
a2.plot(P, z / 1e3, color=AQUA)
for h in (1000, 1500, 2000):
    i = np.argmin(abs(z - h))
    a2.plot([P[i]], [h / 1e3], "o", color=AQUA, ms=5)
    a2.annotate(f"{P[i]:.0f} mm/day", (P[i], h / 1e3), xytext=(-6, 3), textcoords="offset points", ha="right", fontsize=8.5)
a2.set_xlabel("windward-slope rainfall (mm/day)")
a2.set_title("Rain rate if a 1.5 km deep layer is lifted\nover a 50 km slope at 10 m/s", fontsize=10)
fig.tight_layout()
save(fig, "fig_cl15_orographic")
