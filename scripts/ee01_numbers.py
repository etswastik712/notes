"""EE01 - the numbers quoted in the chapter (arithmetic on the slides, Hopcraft et al. 2015 and Holdo et al. 2009).

    .venv/bin/python scripts/ee01_numbers.py
"""
import numpy as np

print("== 1. distance check (Hopcraft 2015: 4.25 km/day on average, ~1550 km/yr)")
print(f"4.25 km/day x 365 = {4.25 * 365:.0f} km per year")

print("\n== 2. muscle efficiency (slide 5): metabolic energy needed per unit of mechanical work = 1/eta")
eta = {"wildebeest": 0.626, "cow": 0.418, "mouse": 0.34}
for k, e in eta.items():
    print(f"{k:10s} eta={e:.3f}  fuel per unit work={1/e:.3f}  heat per unit work={1/e - 1:.3f}")
print(f"cow fuel / wildebeest fuel   = {(1/eta['cow'])/(1/eta['wildebeest']):.2f}")
print(f"mouse fuel / wildebeest fuel = {(1/eta['mouse'])/(1/eta['wildebeest']):.2f}")
print(f"cow heat / wildebeest heat   = {(1/eta['cow']-1)/(1/eta['wildebeest']-1):.2f}")
print(f"mouse heat / wildebeest heat = {(1/eta['mouse']-1)/(1/eta['wildebeest']-1):.2f}")

print("\n== 3. calving synchrony (Hopcraft 2015: >250,000 calves in 3 weeks = ~80% of the year's calves)")
N, w = 250_000, 21
print(f"per day = {N / w:,.0f}   per hour = {N / (w * 24):,.0f}   year total = {N / 0.8:,.0f}")

print("\n== 4. migratory herd vs resident herds (Hopcraft 2015)")
mig = 1.2e6
for name, n in [("Maasai Mara", 40e3), ("Ngorongoro", 10e3), ("Kirawira", 7e3), ("Loliondo", 5e3)]:
    print(f"{name:12s} {n:>9,.0f}   ratio {mig / n:6.0f}")
print(f"area implied by 52 per km2: {mig / 52:,.0f} km2   (Holdo's ecosystem area: 30,700 km2)")

print("\n== 5. swamping upper bound  f_max = min(1, K*w/N)  for N=250,000 calves born over a window of w days")
for K in (500, 1000, 2000):
    row = []
    for ww in (21, 90, 365):
        row.append(f"w={ww:3d}: {min(1, K * ww / N):6.1%}")
    print(f"K={K:5d}/day  " + "   ".join(row) + f"   threshold w*=N/K={N / K:.0f} d")

print("\n== 6. Akaike weights from Holdo Table 1  w_i = exp(-d_i/2) / sum_j exp(-d_j/2)")
models = ["G", "G,T", "G,N", "G,T,N", "I", "I,T", "I,N", "I,T,N", "I,T,Na", "I,T,N,Na", "I,T,N,F", "I,T,N,R", "I,N,F", "I,F"]
ols25 = [226.8, 123.9, 55.3, 44.3, 103.1, 72.4, 25.8, 21.9, 78.0, 26.6, 0.0, 12.2, 2.6, 56.6]
ols10 = [638.6, 548.5, 232.2, 107.5, 283.0, 162.8, 143.9, 0.0, 107.5, 42.7, 0.4, 4.1, 135.4, 144.5]
for name, d in (("10 km OLS", ols10), ("25 km OLS", ols25)):
    d = np.array(d)
    wts = np.exp(-d / 2)
    wts /= wts.sum()
    print(name)
    for i in np.argsort(-wts)[:4]:
        print(f"   {models[i]:10s} delta={d[i]:6.1f}  weight={wts[i]:.3f}")
    wn = sum(wts[i] for i, m in enumerate(models) if "N" in m.split(","))
    print(f"   total weight of the models that contain plant N: {wn:.4f}")
    wg = sum(wts[i] for i, m in enumerate(models) if m.split(",")[0] == "G")
    print(f"   total weight of the models driven by green biomass G: {wg:.2e}")

print("\n== 7. Bayes update (illustrative priors and likelihoods, NOT from the paper)")
hyp = ["forage biomass", "intake + protein", "surface water", "predator escape"]
prior = np.array([0.35, 0.25, 0.20, 0.20])
like = np.array([0.05, 0.60, 0.10, 0.15])
num = prior * like
post = num / num.sum()
for h, p, l, n, q in zip(hyp, prior, like, num, post):
    print(f"{h:18s} prior={p:.2f} like={l:.2f} prior*like={n:.4f} posterior={q:.3f}")
print(f"P(D) = {num.sum():.4f}")
