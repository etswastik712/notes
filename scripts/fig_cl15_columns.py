"""CL15 - why a warm land column makes high pressure aloft, and when the upper-level gradient reverses.

Hydrostatic + ideal gas (Webster & Fasullo 2003, Eqs. 4-6):   d ln p / dz = -g / (R T)
For two isothermal-mean columns (cold ocean Tc, warm land Tw = Tc + dT) with the same SURFACE pressure
    d ln p(z1) = (g z1 / R) (1/Tc - 1/Tw)            -> warm column has HIGHER pressure at every height above 0.
If the warm column has a surface LOW, d ln p(0) < 0, the upper-level gradient reverses only above
    z* = - R d ln p(0) / [ g (1/Tc - 1/Tw) ].
Panels: (a) pressure profiles; (b) pressure difference with height for several dT; (c) reversal height z* vs dT.
"""
from figlib import *

R = 287.0
Tc = 265.0                      # mean temperature of the cold (ocean) column, K
z = np.linspace(0, 16e3, 400)


def p(zz, T, p0=1000.0):
    return p0 * np.exp(-G0 * zz / (R * T))


fig, (a, b, c) = plt.subplots(1, 3, figsize=(11.2, 3.9))

# (a) profiles for dT = 10 K, equal surface pressure
Tw = Tc + 10
a.plot(p(z, Tc), z / 1e3, color=BLUE, label=f"cold ocean column, {Tc:.0f} K")
a.plot(p(z, Tw), z / 1e3, color=ORANGE, label=f"warm land column, {Tw:.0f} K")
a.fill_betweenx(z / 1e3, p(z, Tc), p(z, Tw), color=ORANGE, alpha=0.18, lw=0)
a.set_xlabel("pressure (hPa)")
a.set_ylabel("height (km)")
a.set_title("Same surface pressure: the warm column\nis 'puffed up' aloft", fontsize=10)
a.legend(loc="lower left", fontsize=8)
a.annotate("warm column has the\nhigher pressure at\nany given height", (p(8e3, Tw), 8), xytext=(520, 11.5), fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
d10 = p(10e3, Tw) - p(10e3, Tc)
print(f"dT=10 K, equal surface pressure: p(10 km) cold={p(10e3,Tc):.1f} hPa, warm={p(10e3,Tw):.1f} hPa, diff={d10:.1f} hPa")

# (b) pressure difference vs height for several dT
for dT, col in [(3, VIOLET), (6, AQUA), (10, ORANGE)]:
    Tw_ = Tc + dT
    dp = p(z, Tw_) - p(z, Tc)
    b.plot(dp, z / 1e3, color=col, label=f"ΔT = {dT} K")
    print(f"dT={dT}: max dp = {dp.max():.1f} hPa at {z[dp.argmax()]/1e3:.1f} km")
b.axvline(0, color=MUTED, lw=0.8)
b.set_xlabel("p(warm) − p(cold)  (hPa)")
b.set_title("Pressure difference grows with height\n(equal surface pressure)", fontsize=10)
b.legend(loc="center right", fontsize=8.5)

# (c) reversal height vs dT for a surface low in the warm column
dTs = np.linspace(1, 20, 200)
for dp0, col in [(2, VIOLET), (5, AQUA), (10, ORANGE)]:
    dln0 = np.log((1000 - dp0) / 1000.0)             # d ln p(0) < 0 : surface low over land
    zstar = -R * dln0 / (G0 * (1 / Tc - 1 / (Tc + dTs)))
    c.plot(dTs, zstar / 1e3, color=col, label=f"surface low {dp0} hPa")
    i = np.argmin(abs(dTs - 10))
    print(f"surface low {dp0} hPa, dT=10 K: z* = {zstar[i]/1e3:.2f} km")
c.axhline(5.5, color=MUTED, lw=0.8, ls=":")
c.annotate("mid-troposphere", (19.5, 5.7), ha="right", fontsize=8, color=MUTED)
c.set_ylim(0, 12)
c.set_xlabel("column temperature contrast ΔT (K)")
c.set_ylabel("height above which the gradient is reversed (km)")
c.set_title("A deeper surface low needs a bigger ΔT\nbefore the flow aloft reverses", fontsize=10)
c.legend(loc="upper right", fontsize=8.5)
fig.tight_layout()
save(fig, "fig_cl15_columns")
