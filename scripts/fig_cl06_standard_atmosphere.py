"""CL06 - the US Standard Atmosphere 1976: temperature profile with its layers, base pressures and lapse rates (computed by integrating
hydrostatic balance + ideal gas law layer by layer; see cl06lib.py).  Prints the table used in the chapter."""
from cl06lib import *
from figlib import *

z = np.linspace(0, 84.852, 900)
T, p = std_atm(z)
fig, ax = plt.subplots(figsize=(7.6, 6.2))
bands = [(0, 11, "troposphere", "#dbe8f9"), (11, 47, "stratosphere", "#d3f1e6"), (47, 51, "", "#eeeeea"), (51, 84.852, "mesosphere", "#fbe0d4")]
for lo, hi, n, c in bands:
    ax.axhspan(lo, hi, color=c, lw=0)
    if n:
        ax.annotate(n, (173, (lo + hi) / 2), ha="left", va="center", fontsize=10, color=MUTED, fontweight="semibold")
ax.plot(T, z, color=INK, lw=2.4)
names = {1: "tropopause", 4: "stratopause"}
for i, zb in enumerate(HB[:-1]):
    ax.axhline(zb, color=GRID, lw=0.8)
    pb = PB[i]
    ax.annotate(f"{zb:g} km: {pb:.4g} hPa", (312, zb), ha="left", va="center", fontsize=8.5)
    print(f"base {zb:7.3f} km  T={TB[i]:7.2f} K  p={pb:9.4f} hPa")
for lo, hi, L, txt in ((0, 11, -6.5, "−6.5 K/km"), (20, 32, 1.0, "+1 K/km"), (32, 47, 2.8, "+2.8 K/km"), (51, 71, -2.8, "−2.8 K/km")):
    zm = (lo + hi) / 2
    Tm = float(std_atm(zm)[0][0])
    ax.annotate(txt, (Tm, zm), xytext=(-14 if L < 0 else 14, 0), textcoords="offset points", ha="right" if L < 0 else "left", va="center", fontsize=8.5, color=ORANGE)
ax.set_xlim(170, 375)
ax.set_ylim(0, 85)
ax.set_xlabel("temperature (K)")
ax.set_ylabel("geopotential height (km)")
ax.set_title("Standard-atmosphere temperature: pressure at each layer base", fontsize=10.5)
save(fig, "fig_cl06_standard_atmosphere")
