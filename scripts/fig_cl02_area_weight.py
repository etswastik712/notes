"""CL02 - why the global mean must be area-weighted.

Toy zonal-mean field T(phi) = 255 + 45 cos^2(phi) K (equator 300 K, poles 255 K).
(a) the area of an equal lat-lon cell shrinks as cos(phi);  (b) arithmetic mean over latitude bands overweights the cold poles:
the exact area-weighted mean is 255 + 45*(2/3) = 285 K, the naive band mean is 255 + 45/2 = 277.5 K.
Also prints the discrete sums for a 5-degree grid and for a coarse 3-band grid used in the chapter's worked example.
"""
from figlib import *

dphi = 5.0
phi_c = np.arange(-90 + dphi / 2, 90, dphi)              # cell centres
w = np.cos(np.radians(phi_c))
T = 255 + 45 * np.cos(np.radians(phi_c)) ** 2
naive = T.mean()
aw = (T * w).sum() / w.sum()
print(f"5-degree grid: naive mean {naive:.2f} K; area-weighted {aw:.2f} K; exact 285.00 K; bias {naive-aw:+.2f} K")
# 3-band toy for the worked example: bands 0-30, 30-60, 60-90 (each hemisphere same), centre T from the same field
edges = np.radians([0, 30, 60, 90])
area = np.sin(edges[1:]) - np.sin(edges[:-1])
Tc = 255 + 45 * np.cos(np.radians([15, 45, 75])) ** 2
print("3 bands: areas (fraction of hemisphere)", np.round(area, 3), " T", np.round(Tc, 1),
      f" arithmetic {Tc.mean():.1f}  area-weighted {(Tc*area).sum()/area.sum():.1f}")

fig, axs = plt.subplots(1, 2, figsize=(9.6, 3.7))
ax = axs[0]
ax.barh(phi_c, w * 100, height=dphi * 0.9, color=BLUE, alpha=0.6)
ax.set_xlabel("relative area of a 5° × 5° cell (%)")
ax.set_ylabel("latitude (°)")
ax.set_title("Equal grid cells are not equal in area", fontsize=10)
ax.annotate("area ∝ cos φ", (80, 55), fontsize=9)
ax.set_ylim(-90, 90)
ax = axs[1]
ax.plot(phi_c, T, color=INK, lw=2)
ax.axhline(aw, color=ORANGE, lw=1.8)
ax.axhline(naive, color=BLUE, lw=1.8, ls="--")
ax.annotate(f"area-weighted mean {aw:.1f} K", (-88, aw), xytext=(0, 5), textcoords="offset points", fontsize=8.5)
ax.annotate(f"naive mean over latitude {naive:.1f} K  (bias {naive-aw:+.1f} K)", (-88, naive), xytext=(0, -13), textcoords="offset points", fontsize=8.5)
ax.set_xlabel("latitude (°)")
ax.set_ylabel("T (K)")
ax.set_title("Toy field: the naive mean is too cold", fontsize=10)
ax.set_xlim(-90, 90)
fig.tight_layout()
save(fig, "fig_cl02_area_weight")
