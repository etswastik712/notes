"""Reproduce the numbers of Joy's CERES-explorer handout (Exercises 1-8) from the mirrored data.
   .venv/bin/python -I scripts/joy_ceres_numbers.py   (prints a report; figures in scripts/fig_cl28_ceres.py)
Data: tutorials/ceres-energy-budget/assets/data  (CERES EBAF Ed4.2.1, 2-degree monthly 2010-01..2025-01, Nino-3.4)
"""
import gzip
import json
import os
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
D = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/ceres-energy-budget/assets/data")
R = 6.371e6
meta = json.load(open(f"{D}/meta.json"))
lat = np.array(meta["lat"]); lon = np.array(meta["lon"])
times = meta["times"]
glob = json.load(open(f"{D}/series/global.json"))
nino = json.load(open(f"{D}/nino34.json"))
w = np.cos(np.deg2rad(lat))


def load(group, b, chunk):
    raw = gzip.decompress(open(f"{D}/ceres.zarr/{group}/{b}/c/{chunk}", "rb").read())
    a = np.frombuffer(raw, dtype="<i2").reshape(-1, 90, 180).astype(float)
    a[a == -32768] = np.nan
    return a * 0.1


def clim(b):
    return load("clim", b, "0/0/0")


def gm(x):  # area-weighted global mean of a (..,90,180) field
    x = np.asarray(x)
    ww = w[:, None] * np.ones(180)[None, :]
    return np.nansum(x * ww, axis=(-2, -1)) / np.nansum(np.where(np.isnan(x), 0, ww), axis=(-2, -1))


def zm(x):
    return np.nanmean(x, axis=-1)


def ij(la, lo):
    return int(round((la + 89) / 2)), int(round(((lo % 360) - 1) / 2))


C = {b: clim(b) for b in json.load(open(f"{D}/fields.json"))["base"]}
net, swr, lwr = C["toa_net_all"], C["toa_sw_all"], C["toa_lw_all"]
solar = net + swr + lwr
asr = net + lwr
ann = lambda x: np.nanmean(x, axis=0)
out = {}
print("=== Ex.1  TOA pattern (annual mean of 12 climatological months)")
print("global mean net/ASR/OLR:", [round(float(gm(ann(x))), 2) for x in (net, asr, lwr)])
zn, za, zo = zm(ann(net)), zm(ann(asr)), zm(ann(lwr))
k = np.argmax(zn)
print("max zonal gain %.1f at %d; poles: 89N %.1f, 89S %.1f" % (zn[k], lat[k], zn[-1], zn[0]))
d = za - zo
cross = [(lat[i] + (lat[i + 1] - lat[i]) * d[i] / (d[i] - d[i + 1])) for i in range(len(d) - 1) if d[i] * d[i + 1] < 0]
print("ASR-OLR zero crossings (deg):", np.round(cross, 1))
print("ASR eq vs 89N: %.0f vs %.0f; OLR eq vs 89N: %.0f vs %.0f" % (za[44:46].mean(), za[-1], zo[44:46].mean(), zo[-1]))
for name, la, lo in [("Sahara", 23, 11), ("warm pool", 1, 151)]:
    i, j = ij(la, lo)
    a_, o_, s_ = ann(asr)[i, j], ann(lwr)[i, j], ann(solar)[i, j]
    print(f"{name} ({la},{lo}) net {ann(net)[i,j]:.0f} ASR {a_:.0f} OLR {o_:.0f} albedo {1-a_/s_:.2f}")
# implied northward transport F(phi) = 2 pi R^2 int_{-90}^{phi} net cos
dphi = np.deg2rad(2.0)
cum = 2 * np.pi * R ** 2 * np.cumsum(zn * np.cos(np.deg2rad(lat)) * dphi)  # W, at upper edge of each band
for tgt in (-36, 36):
    i = int(np.argmin(abs(lat - tgt)))
    print("transport northward across %d : %.2f PW" % (tgt, cum[i] / 1e15))
print("peak |F|:", round(float(np.nanmax(abs(cum))) / 1e15, 2), "PW at", lat[int(np.argmax(abs(cum)))])

print("=== Ex.2  seasons")
for m, nm in [(0, "Jan"), (6, "Jul")]:
    z = zm(net[m]); zz = zm(asr[m]) - zm(lwr[m])
    pos = lat[zz > 0]
    print(nm, "gain from", pos.min(), "to", pos.max(), "; polar net 89N %.0f 89S %.0f" % (z[-1], z[0]))
print("June 89N net %.0f, Jul %.0f; Dec 89S %.0f" % (zm(net[5])[-1], zm(net[6])[-1], zm(net[11])[0]))
print("June solar 89N %.0f eq %.0f ; Dec solar 89S %.0f eq %.0f" % (zm(solar[5])[-1], zm(solar[5])[44:46].mean(), zm(solar[11])[0], zm(solar[11])[44:46].mean()))
print("June albedo 89N %.2f, ASR %.0f" % (1 - zm(asr[5])[-1] / zm(solar[5])[-1], zm(asr[5])[-1]))

print("=== Ex.3  imbalance (global series)")
g = {k: np.array(v, dtype=float) for k, v in glob.items()}
gn = g["toa_net"]
print("mean net %.2f ; ASR %.2f OLR %.2f" % (gn[:180].mean(), g["asr"][:180].mean(), g["olr"][:180].mean()))
yrs = np.array([int(t[:4]) for t in times]); mon = np.array([int(t[5:7]) for t in times])
mask = yrs <= 2024
print("2010-14 mean %.2f ; 2020-24 mean %.2f" % (gn[(yrs >= 2010) & (yrs <= 2014)].mean(), gn[(yrs >= 2020) & (yrs <= 2024)].mean()))
ym = {y: gn[yrs == y].mean() for y in range(2010, 2025)}
print("min year", min(ym, key=ym.get), round(min(ym.values()), 2), "max year", max(ym, key=ym.get), round(max(ym.values()), 2))
# trend with calendar-month means removed
anom = gn.copy()
for m in range(1, 13):
    sel = (mon == m) & mask
    anom[mon == m] -= gn[sel].mean()
t = np.arange(len(gn)) / 120.0
sl = np.polyfit(t[mask], anom[mask], 1)[0]
print("trend per decade (2010-2024, month-mean removed): %.2f" % sl, "; incl. Jan 2025: %.2f" % np.polyfit(t, anom, 1)[0])
print("monthly clim range: min %.1f max %.1f" % (min(gn[(mon == m) & mask].mean() for m in range(1, 13)), max(gn[(mon == m) & mask].mean() for m in range(1, 13))))
Eyr = gn[:180].mean() * 5.1e14 * 3.156e7
print("energy per year %.2e J" % Eyr)

print("=== Ex.4  clouds")
for k_ in ("toa_cre_net", "toa_cre_sw", "toa_cre_lw"):
    print(k_, round(g[k_][:180].mean(), 2))
print("clear-sky net", round(g["toa_net_clr"][:180].mean(), 2))
swc, lwc = C["toa_sw_clr"], C["toa_lw_clr"]
cre_sw = ann((swr - swc))  # reflected SW: all minus clr (positive = more reflected) -> CRE_SW = -(that)
cre_sw = -(swr - swc); cre_lw = -(lwr - lwc)
for name, la, lo in [("Peru", -19, -81), ("Namibia", -17, 7), ("California", 27, -125), ("warm pool", 1, 151)]:
    i, j = ij(la, lo)
    print(name, "net %.0f SW %.0f LW %.0f cloud %.0f%% top %.0fK" % (ann(cre_sw + cre_lw)[i, j], ann(cre_sw)[i, j], ann(cre_lw)[i, j], ann(C["cld_frac"])[i, j], ann(C["cld_temp"])[i, j]))
nm = ann(cre_sw + cre_lw)
print("max net CRE %.0f at" % np.nanmax(nm), lat[np.unravel_index(np.nanargmax(nm), nm.shape)[0]], lon[np.unravel_index(np.nanargmax(nm), nm.shape)[1]])

print("=== Ex.5  OLR all vs clear")
for name, la, lo in [("warm pool", 1, 151), ("Sahara", 23, 11)]:
    i, j = ij(la, lo)
    print(name, "OLR all %.0f clr %.0f diff %.0f ; cloud %.0f%% top %.0f K ; sigmaT^4(239K)=%.0f" % (ann(lwr)[i, j], ann(lwc)[i, j], ann(lwc - lwr)[i, j], ann(C["cld_frac"])[i, j], ann(C["cld_temp"])[i, j], 5.670374e-8 * 239 ** 4))

print("=== Ex.6  column")
sfc = C["sfc_sw_dn_all"] - C["sfc_sw_up_all"] + C["sfc_lw_dn_all"] - C["sfc_lw_up_all"]
col = net - sfc
colsw = (solar - swr) - (C["sfc_sw_dn_all"] - C["sfc_sw_up_all"])
collw = -lwr - (C["sfc_lw_dn_all"] - C["sfc_lw_up_all"]) * 1 + 0  # placeholder check below
collw = col - colsw
print("global mean TOA %.2f  surface %.1f  column %.1f ; col SW %.1f LW %.1f" % (gm(ann(net)), gm(ann(sfc)), gm(ann(col)), gm(ann(colsw)), gm(ann(collw))))
cn = ann(col)
print("column loss everywhere? max(col)=%.1f ; min %.0f at" % (np.nanmax(cn), np.nanmin(cn)), lat[np.unravel_index(np.nanargmin(cn), cn.shape)[0]], lon[np.unravel_index(np.nanargmin(cn), cn.shape)[1]], "; max loss-least %.0f" % np.nanmax(cn), lat[np.unravel_index(np.nanargmax(cn), cn.shape)[0]], lon[np.unravel_index(np.nanargmax(cn), cn.shape)[1]])
for name, la, lo in [("warm pool", 1, 151), ("Peru", -19, -81), ("Sahara", 23, 11)]:
    i, j = ij(la, lo)
    print(name, "col %.0f  sfc %.0f" % (cn[i, j], ann(sfc)[i, j]))
print("column cooling rate if radiative only: %.2f K/day (atmos cp*M = 1.0e3*1e4 = 1e7 J/m2/K)" % (110.4 * 86400 / 1.0e7))
print("rain equivalent of 80 W/m2: %.2f mm/day (2.5e6 J/kg)" % (80 * 86400 / 2.5e6))

print("=== Ex.7  El Nino vs La Nina (OLR)")
def dj(b, y0):  # Dec y0, Jan,Feb y0+1 -> array(3,90,180)
    a = load("map", b, f"{y0-2010}/0/0")[11:12]; c = load("map", b, f"{y0+1-2010}/0/0")[0:2]
    return np.concatenate([a, c])
def djclim(b):
    return np.concatenate([clim(b)[11:12], clim(b)[0:2]])
def anomdjf(b, y0):
    return dj(b, y0).mean(0) - djclim(b).mean(0)
A, B = anomdjf("toa_lw_all", 2015), anomdjf("toa_lw_all", 2010)
d_ = A - B
for name, la, lo in [("1S 161W", -1, -161), ("1S 119E", -1, 119)]:
    i, j = ij(la, lo); print("OLR A-B at", name, round(float(d_[i, j]), 0))
sub = d_[(lat > -20) & (lat < 20)][:, :]
ii = np.unravel_index(np.nanargmin(sub), sub.shape)
print("strongest negative A-B in tropics: %.0f at lat %d lon %d" % (np.nanmin(sub), lat[(lat > -20) & (lat < 20)][ii[0]], lon[ii[1]]))
print("global-mean OLR anomaly A %.2f B %.2f ; net A %.2f B %.2f" % (gm(A), gm(B), gm(anomdjf("toa_net_all", 2015)), gm(anomdjf("toa_net_all", 2010))))
Asw = -(anomdjf("toa_sw_all", 2015) - anomdjf("toa_sw_clr", 2015)); Aswb = -(anomdjf("toa_sw_all", 2010) - anomdjf("toa_sw_clr", 2010))
i, j = ij(-1, -161)
print("net TOA A-B at 1S161W: %.0f" % (anomdjf("toa_net_all", 2015) - anomdjf("toa_net_all", 2010))[i, j])
A2, B2 = anomdjf("toa_lw_all", 2023), anomdjf("toa_lw_all", 2020)
print("2023-24 vs 2020-21 OLR: global A-B %.2f ; at 1S161W %.0f" % (gm(A2) - gm(B2), (A2 - B2)[i, j]))

print("=== Ex.8  Nino3.4 vs global anomalies (lags)")
n34 = np.array([np.nan if v is None else v for v in nino["anom"]], dtype=float)
def anomser(x):
    a = np.array(x, dtype=float).copy()
    for m in range(1, 13):
        a[mon == m] -= a[(mon == m) & mask].mean()
    return a
for nm_, key in [("net", "toa_net"), ("OLR", "olr"), ("ASR", "asr")]:
    a = anomser(g[key])
    cc = []
    for lag in range(0, 13):
        x, y = n34[: len(a) - lag], a[lag:]
        ok = ~np.isnan(x) & ~np.isnan(y)
        cc.append(np.corrcoef(x[ok], y[ok])[0, 1])
    cc = np.array(cc)
    # also negative-lag (global leads)
    print(nm_, "corr same month %.2f ; best lag %d -> %.2f ; std of global anom %.2f" % (cc[0], int(np.argmax(abs(cc))), cc[int(np.argmax(abs(cc)))], np.nanstd(a[mask])))
