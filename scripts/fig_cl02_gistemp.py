"""CL02 - real data: NASA GISS Surface Temperature Analysis (GISTEMP v4), global land-ocean annual mean (J-D) anomaly
relative to 1951-1980.  File fetched 2026-10-23 from data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.txt and saved
as Assets/data/GISTEMP_GLB_Ts_dSST.txt; set GISTEMP_FILE to another path to re-run.

Prints the numbers quoted in the chapter: trends, residual scatter, lag-1 autocorrelation, effective sample size.
"""
import os
import re

from figlib import *

PATH = os.environ.get("GISTEMP_FILE", os.path.join(HERE, "..", "Assets", "data", "GISTEMP_GLB_Ts_dSST.txt"))
yrs, jd = [], []
for line in open(PATH):
    m = re.match(r"^(\d{4})\s+(.*)$", line)
    if not m:
        continue
    cols = m.group(2).split()
    if len(cols) < 13:
        continue
    v = cols[12]                       # J-D column
    if "*" in v:
        continue
    yrs.append(int(m.group(1)))
    jd.append(int(v) / 100.0)
yrs, jd = np.array(yrs), np.array(jd)
print("years", yrs[0], "-", yrs[-1], "n =", len(yrs))
for y in (1880, 1940, 1976, 1998, 2016, 2023, 2024, yrs[-1]):
    print(f"  {y}: {jd[yrs == y][0]:+.2f}")


def trend(y0, y1):
    k = (yrs >= y0) & (yrs <= y1)
    p = np.polyfit(yrs[k], jd[k], 1)
    res = jd[k] - np.polyval(p, yrs[k])
    n = k.sum()
    s = res.std(ddof=2)
    se = s / np.sqrt(((yrs[k] - yrs[k].mean()) ** 2).sum())
    r1 = np.corrcoef(res[:-1], res[1:])[0, 1]
    neff = n * (1 - r1) / (1 + r1)
    se_eff = se * np.sqrt(n / neff)
    return p[0] * 10, se * 10, se_eff * 10, s, r1, neff, n


for a, b in [(1975, yrs[-1]), (1880, yrs[-1]), (1951, 1980), (1985, yrs[-1])]:
    sl, se, se2, s, r1, ne, n = trend(a, b)
    print(f"trend {a}-{b}: {sl:.3f} K/decade  (naive se {se:.3f}; with AR(1) n_eff={ne:.0f}/{n}: se {se2:.3f}); resid sd {s:.3f} K, lag-1 r {r1:.2f}")

sl, *_ = trend(1975, yrs[-1])
p = np.polyfit(yrs[yrs >= 1975], jd[yrs >= 1975], 1)
rm = np.convolve(jd, np.ones(5) / 5, mode="valid")
fig, ax = plt.subplots(figsize=(7.6, 4.1))
ax.bar(yrs, jd, color=np.where(jd >= 0, ORANGE, BLUE), width=0.85, alpha=0.55)
ax.plot(yrs[2:-2], rm, color=INK, lw=1.8, label="5-year running mean")
xx = np.array([1975, yrs[-1]])
ax.plot(xx, np.polyval(p, xx), color=RED, lw=1.8, ls="--", label=f"linear trend since 1975: {sl:.2f} K per decade")
ax.axhline(0, color=MUTED, lw=0.8)
ax.axvspan(1951, 1980, color="#eda100", alpha=0.12, lw=0)
ax.annotate("baseline\n1951–1980", (1965.5, -0.52), ha="center", fontsize=8, color=MUTED)
ax.set_ylabel("global-mean anomaly (K)")
ax.set_xlim(1878, yrs[-1] + 2)
ax.set_title("Global mean surface temperature anomaly, 1880–" + str(yrs[-1]) + " (NASA GISTEMP v4)")
ax.legend(loc="upper left", fontsize=8.5)
ax.grid(axis="x", visible=False)
fig.text(0.01, -0.01, "Data: NASA GISS GISTEMP v4, land-ocean index, annual J–D, base 1951–1980; fetched 2026-10-23.", fontsize=7.3, color=MUTED)
save(fig, "fig_cl02_gistemp")
