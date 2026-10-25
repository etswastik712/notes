"""CL10 (extra, beyond) - how much can orbital changes alter summer insolation at 65 N?  Daily-mean TOA flux on the June solstice.

Scenarios use the exact insolation formula of cl10lib.  Ranges quoted: obliquity ~22.1-24.5 deg, eccentricity 0-~0.058,
precession moves perihelion around the year (period ~19-23 kyr).  Hays, Imbrie & Shackleton (1976, Science 194, 1121).
"""
from cl10lib import *
from figlib import *

phi = np.radians(65)
lam = np.pi / 2                                   # NH summer solstice
cases = [
    ("present\n(ε 23.4°, e 0.017,\nperihelion in Jan)", dict(obl=np.radians(23.44), ecc=0.0167, varpi=np.radians(282.9))),
    ("circular orbit\n(ε 23.4°, e 0)", dict(obl=np.radians(23.44), ecc=0.0, varpi=0.0)),
    ("cool NH summer\n(ε 22.1°, e 0.05,\naphelion at solstice)", dict(obl=np.radians(22.1), ecc=0.05, varpi=np.radians(270))),
    ("warm NH summer\n(ε 24.5°, e 0.05,\nperihelion at solstice)", dict(obl=np.radians(24.5), ecc=0.05, varpi=np.radians(90))),
]
vals = []
for name, kw in cases:
    q = float(daily_insolation(phi, lam, **kw))
    vals.append(q)
    print(f"{name.splitlines()[0]:<18s} Q(65N, 21 Jun) = {q:.0f} W m-2")
print(f"range warm - cool = {vals[3]-vals[2]:.0f} W m-2 ({(vals[3]-vals[2])/vals[0]*100:.0f}% of present)")
for nm, ob in (("22.1", 22.1), ("23.44", 23.44), ("24.5", 24.5)):
    print(f"annual mean at 65N, obliquity {nm}: {float(annual_mean(phi, obl=np.radians(ob))):.1f} W m-2; at pole {float(annual_mean(np.pi/2, obl=np.radians(ob))):.1f}")

fig, ax = plt.subplots(figsize=(7.2, 3.9))
cols = [MUTED, MUTED, BLUE, ORANGE]
ax.bar(range(4), vals, color=cols, width=0.62)
for i, v in enumerate(vals):
    ax.annotate(f"{v:.0f}", (i, v), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
ax.set_xticks(range(4))
ax.set_xticklabels([c[0] for c in cases], fontsize=8)
ax.set_ylim(0, 640)
ax.set_ylabel("daily-mean insolation, 65°N, 21 June (W m$^{-2}$)")
ax.set_title("Orbital changes swing 65°N summer insolation by ~140 W m$^{-2}$")
ax.grid(axis="x", visible=False)
save(fig, "fig_cl10_milankovitch")
