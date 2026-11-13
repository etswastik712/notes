"""CL22 figure: Earth's TOA energy ledger from CERES EBAF (Joy's CERES tutorial data, 2010-2024) and the implied poleward transport.
   .venv/bin/python -I scripts/fig_cl22.py      (numbers: scripts/joy_ceres_numbers.py)"""
import gzip
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa: F401,F403

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
D = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/ceres-energy-budget/assets/data")
R = 6.371e6
lat = np.array(json.load(open(f"{D}/meta.json"))["lat"])


def clim(b):
    raw = gzip.decompress(open(f"{D}/ceres.zarr/clim/{b}/c/0/0/0", "rb").read())
    a = np.frombuffer(raw, dtype="<i2").reshape(12, 90, 180).astype(float)
    a[a == -32768] = np.nan
    return a * 0.1


net, lw = clim("toa_net_all"), clim("toa_lw_all")
asr = net + lw
zn, za, zo = [np.nanmean(x.mean(0), axis=-1) for x in (net, asr, lw)]
w = np.cos(np.deg2rad(lat))
gmean = (zn * w).sum() / w.sum()
band = lambda z: 2 * np.pi * R ** 2 * z * w * np.deg2rad(2.0)
F_raw = np.cumsum(band(zn)) / 1e15                      # from the south pole, imbalance kept
F_bal = np.cumsum(band(zn - gmean)) / 1e15             # global-mean imbalance removed uniformly (the handout's convention)

fig, ax = plt.subplots(1, 2, figsize=(11.6, 4.3))
a = ax[0]
a.plot(lat, za, color=ORANGE, lw=2); a.plot(lat, zo, color=BLUE, lw=2)
a.fill_between(lat, za, zo, where=za >= zo, color=ORANGE, alpha=0.18); a.fill_between(lat, za, zo, where=za < zo, color=BLUE, alpha=0.18)
a.plot(lat, zn, color=INK, lw=1.4, ls="--")
a.axhline(0, color="#888", lw=0.6)
a.set_xlim(-90, 90); a.set_xlabel("latitude (°)"); a.set_ylabel("W m⁻²")
a.text(28, 305, "absorbed sunlight", color=ORANGE, fontsize=9); a.text(-88, 236, "outgoing infrared", color=BLUE, fontsize=9)
a.text(30, 30, "net", color=INK, fontsize=9)
a.set_title("A  the zonal-mean TOA budget (CERES, 2010–2024)", fontsize=9.8)
b = ax[1]
b.plot(lat + 1, F_raw, color="#999", lw=1.6, ls=":", label="imbalance kept (+1.26 W m⁻²)")
b.plot(lat + 1, F_bal, color=INK, lw=2.2, label="imbalance removed uniformly")
b.axhline(0, color="#888", lw=0.6); b.set_xlim(-90, 90)
i35 = int(np.argmin(abs(lat - 35))); im36 = int(np.argmin(abs(lat + 37)))
b.annotate("%.1f PW" % F_bal[i35], (lat[i35] + 1, F_bal[i35]), (50, 5.3), arrowprops=dict(arrowstyle="-", color=INK), fontsize=9)
b.annotate("%.1f PW" % F_bal[im36], (lat[im36] + 1, F_bal[im36]), (-85, -3.6), arrowprops=dict(arrowstyle="-", color=INK), fontsize=9)
b.set_xlabel("latitude (°)"); b.set_ylabel("northward energy transport (PW)")
b.legend(fontsize=8, frameon=False, loc="upper left")
b.set_title("B  what the atmosphere + ocean must carry", fontsize=9.8)
save(fig, "fig_cl22_energy_ledger")
print("global mean net %.2f ; F_bal(36N) %.2f ; F_bal(36S) %.2f ; F_raw(36N) %.2f" % (gmean, F_bal[i35 + 0], F_bal[im36], F_raw[i35]))
