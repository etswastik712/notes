"""CL10 - zonal-mean top-of-atmosphere budget: insolation, absorbed solar, OLR and net radiation (annual mean).

IDEALISED profile calibrated to numbers in the course sources (global albedo 0.29; absorbed ~320 W m-2 in the tropics vs ~60 at the
poles; OLR dip at the equator; net radiation +75 W m-2 at the equator, ~-115 at the poles, changing sign near 35-37 deg;
peak poleward flux ~5.8 PW).  It reproduces the shape of Hartmann Fig. 2.12 / Marshall & Plumb Fig. 5.5 / 7 Oct slide 10;
it is NOT satellite data.
"""
from cl10lib import *
from figlib import *

lat = np.linspace(-90, 90, 721)
phi = np.radians(lat)
Q, ASR, OLR, R = toa_profiles(phi)
zc = lat[(lat > 0) & (np.sign(R) != np.sign(np.roll(R, 1)))][0]
x = np.linspace(-1, 1, 4001)
Qx, ASRx, OLRx, Rx = toa_profiles(np.arcsin(x))
print(f"global albedo = {1 - ASRx.mean() / Qx.mean():.3f}; mean ASR = {ASRx.mean():.1f}; mean OLR = {OLRx.mean():.1f}; mean net = {Rx.mean():.3f}")
print(f"ASR eq {ASR[360]:.0f}, pole {ASR[-1]:.0f} (ratio {ASR[360] / ASR[-1]:.1f}); OLR eq {OLR[360]:.0f}, 25N {OLR[np.argmin(abs(lat - 25))]:.0f}, pole {OLR[-1]:.0f}")
print(f"net: eq {R[360]:.0f}, pole {R[-1]:.0f}; zero crossing {zc:.1f} deg;  albedo eq {1 - ASR[360] / Q[360]:.2f}, 60 deg {1 - ASR[np.argmin(abs(lat - 60))] / Q[np.argmin(abs(lat - 60))]:.2f}, pole {1 - ASR[-1] / Q[-1]:.2f}")

fig, (a, b) = plt.subplots(2, 1, figsize=(7.4, 7.0), sharex=True, gridspec_kw={"height_ratios": [1.25, 1]})
a.plot(lat, Q, color=MUTED, ls="--", lw=1.4)
a.plot(lat, ASR, color=ORANGE)
a.plot(lat, OLR, color=BLUE)
a.fill_between(lat, ASR, Q, color=ORANGE, alpha=0.10, lw=0)
arrow = dict(arrowstyle="-", color=MUTED, lw=0.8)
a.annotate("insolation Q (annual mean)", (-50, float(np.interp(-50, lat, Q))), xytext=(-88, 430), fontsize=8.5, color=INK, arrowprops=arrow)
a.annotate("absorbed solar $Q(1-\\alpha)$", (-25, float(np.interp(-25, lat, ASR))), xytext=(-62, 118), fontsize=9, color=INK, arrowprops=arrow)
a.annotate("outgoing longwave (OLR)", (58, float(np.interp(58, lat, OLR))), xytext=(34, 425), fontsize=9, color=INK, arrowprops=arrow)
a.annotate("reflected: the albedo\nrises poleward", (-90, 118), xytext=(-86, 20), fontsize=8, color=MUTED, ha="left")
a.annotate("OLR dip: cold tops of\ndeep tropical clouds", (0, OLR[360]), xytext=(14, -62), textcoords="offset points", fontsize=8, color=INK,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_ylim(0, 460)
a.set_ylabel("flux (W m$^{-2}$)")
a.set_title("Idealised zonal-mean TOA budget (calibrated to the quoted numbers, not data)")

b.axhline(0, color=MUTED, lw=0.8)
b.plot(lat, R, color=INK, lw=2.2)
b.fill_between(lat, R, 0, where=R > 0, color=ORANGE, alpha=0.25, lw=0)
b.fill_between(lat, R, 0, where=R < 0, color=BLUE, alpha=0.25, lw=0)
b.annotate("surplus", (0, 20), ha="center", fontsize=9)
b.annotate("deficit:\nnet loss", (-70, -60), ha="center", fontsize=9)
b.annotate("deficit", (70, -60), ha="center", fontsize=9)
for s in (-1, 1):
    b.plot([s * zc], [0], "o", color=INK, ms=5, zorder=5)
b.annotate(f"net = 0 at ±{zc:.0f}°", (zc, 0), xytext=(8, 14), textcoords="offset points", fontsize=8.5)
b.set_ylim(-140, 100)
b.set_xlim(-90, 90)
b.set_xticks(range(-90, 91, 30))
b.set_xlabel("latitude (°)")
b.set_ylabel("net radiation $R_{TOA}$ (W m$^{-2}$)")
fig.tight_layout()
save(fig, "fig_cl10_toa_budget")
