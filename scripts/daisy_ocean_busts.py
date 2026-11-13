"""Run 4 of the life tutorial: weather + ocean memory -> busts of every size.  .venv/bin/python -I scripts/daisy_ocean_busts.py"""
import importlib.util, os, sys
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("do", os.path.join(here, "daisy_ocean.py")); do = importlib.util.module_from_spec(spec); sys.argv = ["x"]; spec.loader.exec_module(do)
Life, peaks, bars = do.Life, do.peaks, do.bars


def planet_monthly(r):
    tp = 0.3 * r[:, 1] + 0.7 * r[:, 2]          # recorded weekly -> average to ~months of 4 records
    n = (len(tp) // 52) * 52
    return tp[:n].reshape(-1, 52 // 12 if False else 1).mean(1)


def century_bar(r):
    tp = 0.3 * r[:, 1] + 0.7 * r[:, 2]
    per_year = 52  # weekly records ~ 365/7
    n = (len(tp) // (per_year * 100)) * per_year * 100
    return tp[:n].reshape(-1, per_year * 100).mean(1).std()


res = {}
for seed in (1, 2, 3):
    out = {}
    for lab, kw in [("bare", dict(daisies=False, grazers=False)), ("daisies", dict(grazers=False)), ("life", dict())]:
        m = Life(sigma=30.0, seed=seed, **kw); m.run(1500, 30)
        r = m.run(2000, 7)
        out[lab] = (century_bar(r), r)
    print("seed %d century bars (K): bare %.3f  daisies-only %.3f  daisies+grazers %.3f   (handout: .05-.08 / .013-.023 / .11-.28)" % (seed, out["bare"][0], out["daisies"][0], out["life"][0]))
    r = out["life"][1]
    t, Z, Tm = r[:, 0], r[:, 6], r[:, 2]
    # smooth grazers with 0.25-yr window to find booms
    k = 13
    Zs = np.convolve(Z, np.ones(k) / k, mode="same")
    pk = peaks(t, Zs, 1.5)
    drops, anomm = [], []
    for a, b in zip(pk[:-1], pk[1:]):
        drops.append(Zs[a] / Zs[a:b].min())
        i0, i1 = np.searchsorted(t, t[a] - 3.0), np.searchsorted(t, t[a] - 1.0)
        if i0 > 0:
            anomm.append(Tm[i0:i1].mean() - Tm.mean())
        else:
            anomm.append(np.nan)
    drops = np.array(drops); anomm = np.array(anomm)
    ok = ~np.isnan(anomm)
    print("   busts %d ; median drop x%.0f ; 10th pct x%.1f ; 90th pct x%.0f ; corr(log drop, ocean anomaly 3 yr before) = %.2f" % (
        len(drops), np.median(drops), np.percentile(drops, 10), np.percentile(drops, 90), np.corrcoef(np.log10(drops[ok]), anomm[ok])[0, 1]))
