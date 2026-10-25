"""CL06 - is the atmosphere hydrostatic?  Order-of-magnitude accelerations (m s-2) in the vertical momentum balance.

Vertical:  Dw/Dt = -(1/rho) dp/dz - g.  The two big terms cancel to ~1 part in 10^3-10^7; the leftover (the vertical acceleration)
is tiny for large-scale flow and only comparable with the departure from balance in deep convection.
Scale estimates (not measurements):
  g = 9.8;  (1/rho) dp/dz = g (hydrostatic);  horizontal PGF: 10 hPa / 1000 km at rho = 1.2;
  Coriolis f U = 1e-4 * 10;  convective Dw/Dt ~ W^2/L = (10 m/s)^2 / 10 km;  synoptic Dw/Dt ~ W U / L = 0.01 * 10 / 1e6.
"""
from figlib import *

items = [
    ("gravity  g", 9.8, INK),
    ("vertical pressure-gradient force  $\\rho^{-1}\\partial p/\\partial z$", 9.8, INK),
    ("deep convection: $Dw/Dt\\sim W^2/L$", 1e-2, ORANGE),
    ("Coriolis  $fU$ (synoptic)", 1e-3, BLUE),
    ("horizontal PGF (10 hPa per 1000 km)", 8.3e-4, BLUE),
    ("synoptic-scale $Dw/Dt\\sim WU/L$", 1e-7, AQUA),
]
items = items[::-1]
fig, ax = plt.subplots(figsize=(8.6, 4.2))
y = np.arange(len(items))
ax.barh(y, [v for _, v, _ in items], color=[c for _, _, c in items], height=0.6)
for yi, (n, v, c) in zip(y, items):
    ax.annotate(f"{v:.1e}", (v, yi), xytext=(5, 0), textcoords="offset points", va="center", fontsize=8.5)
ax.set_yticks(y)
ax.set_yticklabels([n for n, _, _ in items], fontsize=8.5)
ax.set_xscale("log")
ax.set_xlim(1e-8, 1e3)
ax.set_xlabel("magnitude of the term (m s$^{-2}$), log scale")
ax.set_title("Vertically, gravity and the pressure force are 10$^3$–10$^8$ times bigger than any vertical acceleration", fontsize=10)
ax.grid(axis="y", visible=False)
fig.tight_layout()
save(fig, "fig_cl06_hydrostatic_check")
print("vertical PGF / horizontal PGF = %.1e" % (1.225 * 9.80665 / 1000 * 1e6 / 1.0 / (1.225)))
