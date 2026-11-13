"""CL28 figure: CERES explorer exercises 3, 7, 8 recomputed.   .venv/bin/python -I scripts/fig_cl28_ceres.py"""
import os, sys, gzip, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
D = os.path.join(ROOT, "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/ceres-energy-budget/assets/data")
meta = json.load(open(f"{D}/meta.json")); lat = np.array(meta["lat"]); lon = np.array(meta["lon"]); times = meta["times"]
g = {k: np.array(v, dtype=float) for k, v in json.load(open(f"{D}/series/global.json")).items()}
n34 = np.array([np.nan if v is None else v for v in json.load(open(f"{D}/nino34.json"))["anom"]], dtype=float)
yrs = np.array([int(t[:4]) for t in times]); mon = np.array([int(t[5:7]) for t in times]); mask = yrs <= 2024
def load(group, b, chunk):
    a = np.frombuffer(gzip.decompress(open(f"{D}/ceres.zarr/{group}/{b}/c/{chunk}", "rb").read()), dtype="<i2").reshape(-1, 90, 180).astype(float); a[a == -32768] = np.nan; return a * 0.1
def dj(y0): return np.concatenate([load("map", "toa_lw_all", f"{y0-2010}/0/0")[11:12], load("map", "toa_lw_all", f"{y0+1-2010}/0/0")[0:2]]).mean(0) - np.concatenate([load("clim", "toa_lw_all", "0/0/0")[11:12], load("clim", "toa_lw_all", "0/0/0")[0:2]]).mean(0)
fig, ax = plt.subplots(1, 3, figsize=(14.4, 4.4), gridspec_kw=dict(width_ratios=[1.15, 1.25, 1]))
a = ax[0]
t = 2010 + (np.arange(len(times))) / 12.0
net = g["toa_net"]
rm = np.convolve(net, np.ones(12) / 12, mode="valid")
a.plot(t, net, color="#bbb", lw=0.8, label="monthly"); a.plot(t[5:5 + len(rm)], rm, color=ORANGE, lw=2.2, label="12-month mean")
sl, ic = np.polyfit((t - 2010)[mask], (net - np.array([net[(mon == m) & mask].mean() for m in mon]))[mask], 1)[0], 0
sl2 = np.polyfit((t - 2010)[mask], net[mask], 1)
tm = (t - 2010)[mask].mean(); a.plot(t[mask], net[mask].mean() + sl * (t[mask] - 2010 - tm), color=INK, ls="--", lw=1.2, label="trend +%.2f W m⁻² per decade" % (sl * 10))
nn = n34
a.fill_between(t, 8, 9.5, where=nn >= 0.5, color=RED, alpha=0.5); a.fill_between(t, 8, 9.5, where=nn <= -0.5, color=BLUE, alpha=0.5)
a.set_xticks([2010, 2015, 2020, 2025]); a.set_ylim(-11, 10); a.axhline(0, color="#888", lw=.6); a.set_ylabel("global-mean net TOA (W m⁻²)"); a.set_xlabel("year")
a.legend(fontsize=7.6, frameon=False, loc="lower left"); a.set_title("A  the planet gains ≈ +1.26 W m⁻² (red/blue: El Niño/La Niña)", fontsize=9)
b = ax[1]
d = dj(2015) - dj(2010)
sel_lat = (lat >= -30) & (lat <= 30); sel_lon = (lon >= 100) & (lon <= 300)
im = b.imshow(d[np.ix_(sel_lat, sel_lon)][::-1], extent=[100, 300, -30, 30], cmap="RdBu_r", vmin=-110, vmax=110, aspect="auto")
b.set_xlabel("longitude (°E)"); b.set_ylabel("latitude"); b.set_title("B  OLR, DJF 2015–16 minus 2010–11 (W m⁻²)", fontsize=9.8)
plt.colorbar(im, ax=b, fraction=0.04, pad=0.02)
b.plot([199], [-1], "k+"); b.plot([119], [-1], "k+")
c = ax[2]
def anomser(x):
    q = x.copy()
    for m in range(1, 13): q[mon == m] -= q[(mon == m) & mask].mean()
    return q
lags = np.arange(-6, 13)
for key, col, lab in (("toa_net", INK, "net TOA"), ("olr", BLUE, "OLR"), ("asr", ORANGE, "ASR")):
    an = anomser(g[key]); cc = []
    for L in lags:
        if L >= 0: x, y = n34[: len(an) - L], an[L:]
        else: x, y = n34[-L:], an[: len(an) + L]
        ok = ~np.isnan(x) & ~np.isnan(y); cc.append(np.corrcoef(x[ok], y[ok])[0, 1])
    c.plot(lags, cc, color=col, lw=2, label=lab)
c.axhline(0, color="#888", lw=.6); c.axvline(0, color="#ccc", lw=.6); c.set_xlabel("months the global anomaly lags Niño-3.4"); c.set_ylabel("correlation")
c.legend(fontsize=8, frameon=False); c.set_title("C  El Niño and the global budget: weak, and late", fontsize=9.8)
fig.subplots_adjust(wspace=0.42)
save(fig, "fig_cl28_ceres")
print("trend per decade (month-mean removed) %.2f ; raw %.2f" % (sl * 10, sl2[0] * 10))
