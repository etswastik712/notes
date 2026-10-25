"""CL11 - how the mass stream function is built from the zonal-mean meridional wind at one latitude.

psi(phi, p) = (2 pi a cos(phi) / g) * integral_0^p [v] dp'      (Suhas 8 Oct slide 8; slide 7 Oct p20)

Illustrative profile (NOT data): poleward aloft, equatorward below, zero net mass flux:  [v](p) = V cos(pi p / p_s).
"""
from figlib import *

ps = 1.0e5            # Pa
V = 1.5               # m/s, illustrative amplitude
phi = np.radians(15)
p = np.linspace(0, ps, 400)
v = V * np.cos(np.pi * p / ps)
psi = (2 * np.pi * R_EARTH * np.cos(phi) / G0) * V * (ps / np.pi) * np.sin(np.pi * p / ps)
print(f"psi_max at 15 deg for V={V} m/s: {psi.max():.3e} kg/s = {psi.max()/1e9:.0f} x 1e9 kg/s at p={p[psi.argmax()]/100:.0f} hPa")

fig, (a, b) = plt.subplots(1, 2, figsize=(8.6, 4.6), sharey=True)
ph = p / 100
a.fill_betweenx(ph, 0, v, where=v >= 0, color=BLUE, alpha=0.25, lw=0)
a.fill_betweenx(ph, 0, v, where=v <= 0, color=ORANGE, alpha=0.25, lw=0)
a.plot(v, ph, color=INK)
a.axvline(0, color=MUTED, lw=0.8)
a.annotate("poleward aloft\n($[v]>0$)", (-1.0, 190), ha="center", fontsize=9, color=INK)
a.annotate("equatorward\nbelow ($[v]<0$)", (1.0, 790), ha="center", fontsize=9, color=INK)
a.annotate("$[v]=0$ at 500 hPa", (0.0, 500), xytext=(0.3, 440), fontsize=8.5, color=MUTED, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.7))
a.set_xlabel("zonal-mean meridional wind $[v]$ (m s$^{-1}$)")
a.set_ylabel("pressure (hPa)")
a.set_xlim(-2, 2)
a.set_ylim(1000, 0)
a.set_title("(a) the input: $[v](p)$ at 15°")

b.plot(psi / 1e9, ph, color=BLUE)
b.fill_betweenx(ph, 0, psi / 1e9, color=BLUE, alpha=0.15, lw=0)
b.axvline(0, color=MUTED, lw=0.8)
b.plot([psi.max() / 1e9], [500], "o", color=BLUE, ms=6)
b.annotate(f"max {psi.max()/1e9:.0f}×10$^9$ kg s$^{{-1}}$\nwhere $[v]=0$", (psi.max() / 1e9, 500), xytext=(10, -4), textcoords="offset points", ha="left", fontsize=9)
b.annotate("$\\psi=0$ at the top ($p=0$)", (-28, 25), fontsize=8.5, color=MUTED)
b.annotate("$\\psi=0$ at the ground\n(no net mass flux)", (-28, 960), fontsize=8.5, color=MUTED, va="bottom")
b.set_xlabel("mass stream function $\\psi$ ($10^9$ kg s$^{-1}$)")
b.set_title("(b) the output: $\\psi(p)$, the running total", fontsize=10.5)
b.set_xlim(-30, 290)
fig.tight_layout()
save(fig, "fig_cl11_streamfunction_build")
