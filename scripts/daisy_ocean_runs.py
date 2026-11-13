"""Part-2 (life) runs of Joy's Daisyworld-with-an-Ocean tutorial.  .venv/bin/python -I scripts/daisy_ocean_runs.py"""
import importlib.util, os, sys
import numpy as np
here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("do", os.path.join(here, "daisy_ocean.py")); do = importlib.util.module_from_spec(spec); sys.argv = ["x"]; spec.loader.exec_module(do)
Life, peaks = do.Life, do.peaks


def cycle(mdl_kw, years=150, hidden=1500):
    m = Life(sigma=0.0, **mdl_kw); m.run(hidden, rec_every_days=30, noise=False); r = m.run(years, rec_every_days=7, noise=False)
    t, Z = r[:, 0], r[:, 6]; pk = peaks(t, Z, 0.5)
    per = np.diff(t[pk]); return r, per, (Z.max() / Z.min())


print("Run 1 (daisies, no grazers, no weather, 70% ocean): sun table (handout bare 12.4/18.2/23.9/29.7/35.5; daisies 19.0/24.9/22.0/21.6/27.1; cover white/black 0/69, 1/68, 43/26, 70/0, 69/0)")
for L in (0.95, 1.00, 1.05, 1.10, 1.15):
    m = Life(sigma=0.0, grazers=False, L=L); m.run(1500, 30, noise=False); r = m.run(20, 30, noise=False)[-1]
    b = Life(sigma=0.0, daisies=False, grazers=False, L=L); b.run(1500, 30, noise=False); rb = b.run(5, 30, noise=False)[-1]
    print("  L=%.2f bare land %.1f  daisy land %.1f  white/black %.0f/%.0f %%" % (L, rb[1], r[1], 100 * r[4], 100 * r[5]))
print("Run 3 (preset 6 with no ocean: handout settles, grazers 0.19, white 29%, black 26%, land 18.3 C; 30% ocean: cycle ~3 yr)")
m = Life(sigma=0.0, f_o=0.0); m.run(300, 30, noise=False); r = m.run(40, 30, noise=False)[-1]
print("  0%% ocean: grazers %.2f white %.0f%% black %.0f%% land %.1f" % (r[6], 100 * r[4], 100 * r[5], r[1]))
for fo in (0.3,):
    _, per, ratio = cycle(dict(f_o=fo), 100, 1500)
    print("  %.0f%% ocean: mean cycle %.1f yr (intervals %s)" % (100 * fo, per.mean(), np.round(per[:6], 1)))
print("Run 5 clockwork cycle (best 26 C, tolerance 5 K, no weather; handout turn length 25/50/75/150 m = 6.7/7.7/8.4/10.7 yr)")
for H in (25, 50, 75, 150):
    _, per, _ = cycle(dict(H=H, Tg=26.0, wg=5.0), 200, 1500)
    print("  H=%d m: mean turn %.1f yr (range %.1f-%.1f)" % (H, per.mean(), per.min(), per.max()))
print("Run 6 grazer variants on preset 6 (handout best 22 C -> ~1.1 yr; 28 C -> 8.4; 30 C -> die out; tol 4 -> 7.8; tol 8 -> 1.3; taste .5 -> 1.2; taste 1 -> 4)")
for lab, kw in [("best 22", dict(Tg=22.0)), ("best 28", dict(Tg=28.0)), ("best 30", dict(Tg=30.0)), ("tol 4", dict(wg=4.0)), ("tol 8", dict(wg=8.0)), ("taste .5", dict(p=0.5)), ("taste 1", dict(p=1.0))]:
    r, per, ratio = cycle(kw, 100, 1000)
    print("  %-9s turn %s yr ; grazer swing x%.0f ; land %.0f-%.0f C" % (lab, (np.round(per.mean(), 1) if len(per) else None), ratio, r[:, 1].min(), r[:, 1].max()))
