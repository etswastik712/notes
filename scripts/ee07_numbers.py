"""EE07 - numbers quoted in the chapter: stochastic extinction, Allee harvest fold, mark-recapture, genetic drift, tiger trend.

    .venv/bin/python -W ignore scripts/ee07_numbers.py
(The extinction-time and Allee figures print their own check values: fig_ee07_extinction_time.py, fig_ee07_allee.py.)
"""
import numpy as np

print("== 1. Extinction of a linear birth-death population (b>d): P_ext(N0) = (d/b)^N0")
for b, d in ((1.1, 1.0), (1.5, 1.0)):
    print(f"  b={b}, d={d}: ", {n: round((d / b) ** n, 4) for n in (1, 5, 10, 20, 50)})
print("  environmental noise does not fade like this; demographic noise relative to the mean scales as 1/sqrt(N):", {n: round(1 / np.sqrt(n), 3) for n in (10, 100, 1000)})

print("\n== 2. Allee effect with constant harvest: f(N)=r N (N/A-1)(1-N/K), r=0.5, A=20, K=100")
r, A, K = 0.5, 20.0, 100.0
f = lambda N: r * N * (N / A - 1) * (1 - N / K)
Nm = ((A + K) + np.sqrt((A + K) ** 2 - 3 * A * K)) / 3
print(f"  max growth f={f(Nm):.2f} at N={Nm:.1f} (logistic rK/4={r * K / 4}); harvest H=20 -> equilibria 52.05 (unstable) and 85.85 (stable)")
print("  per-capita growth at N=5:", round(f(5) / 5, 3), "(negative) vs logistic r(1-N/K) =", round(r * (1 - 5 / K), 3))

print("\n== 3. Mark-recapture (Lincoln-Petersen and Chapman): M marked, n caught later, m recaptured")
for M, n, m in ((50, 40, 8), (50, 40, 20), (50, 40, 3)):
    LP = M * n / m
    ch = (M + 1) * (n + 1) / (m + 1) - 1
    var = (M + 1) * (n + 1) * (M - m) * (n - m) / ((m + 1) ** 2 * (m + 2))
    print(f"  M={M}, n={n}, m={m}: LP={LP:.0f}, Chapman={ch:.1f}, SE={np.sqrt(var):.1f}, approx 95% CI {ch - 1.96 * np.sqrt(var):.0f}-{ch + 1.96 * np.sqrt(var):.0f}")
print("  N = C/p: counted C=30 tigers, capture probability p=0.6 ->", 30 / 0.6)
p, k = 0.1, 10
print(f"  camera trap: per-occasion capture p={p}, K={k} occasions -> overall p*=1-(1-p)^K = {1 - (1 - p) ** k:.3f}; C=30 counted -> N_hat = {30 / (1 - (1 - p) ** k):.1f}")

print("\n== 4. Genetic drift: H_t/H_0 = (1 - 1/(2 Ne))^t")
for Ne in (10, 50, 500):
    print(f"  Ne={Ne}: after 10, 50, 100 generations: {[round((1 - 1 / (2 * Ne)) ** t, 3) for t in (10, 50, 100)]}")
print("  generations to lose half the heterozygosity ~ 1.39 Ne:", {Ne: round(np.log(2) / -np.log(1 - 1 / (2 * Ne)), 1) for Ne in (10, 50, 500)})

print("\n== 5. Project Tiger numbers (slide 22-25)")
print("  1972 -> '>4000 in 11 years' (disputed): implied growth", round(np.log(4000 / 1827) / 11, 4), "per yr (x", round(4000 / 1827, 2), ")")
print("  2008 1411 -> 2011 1706: x", round(1706 / 1411, 3), ", growth", round(np.log(1706 / 1411) / 3, 4), "per yr")
print("  2011 1706 -> 2018 2967: x", round(2967 / 1706, 3), ", growth", round(np.log(2967 / 1706) / 7, 4), "per yr; 2018 CI 2603-3346 = -", round(100 * (1 - 2603 / 2967), 1), "% / +", round(100 * (3346 / 2967 - 1), 1), "%")
print("  reserves: 9 reserves 13,017 km2 (1973) -> >40 reserves 37,761 km2 (2007): area x", round(37761 / 13017, 2))
print("  early 20th c. 40-45 thousand -> 1972 1827: fall to", round(100 * 1827 / 42500, 1), "% (mid-point 42,500); 2018 is", round(100 * 2967 / 42500, 1), "% of that")
print("  illustrative background extinction ~1 E/MSY: for 1e6 species that is 1 per yr; 100-1000x -> 100-1000 per yr")
