"""EE06 - numbers quoted in the chapter: Scheffer et al. (2001) Box 1 model, its folds and hysteresis; Vollenweider; P-classes.

    .venv/bin/python -W ignore scripts/ee06_numbers.py
"""
import numpy as np
from scipy.optimize import brentq

b, r, h, p = 1.0, 1.4, 1.0, 8
f = lambda x: x ** p / (x ** p + h ** p)
fp = lambda x: p * x ** (p - 1) * h ** p / (x ** p + h ** p) ** 2
a_of_x = lambda x: b * x - r * f(x)               # equilibrium: a - b x + r f(x) = 0
print("== Box 1 model dx/dt = a - b x + r x^p/(x^p+h^p); b=1, r=1.4, h=1, p=8")
print("max r f'(x) =", round(max(r * fp(x) for x in np.linspace(0.01, 3, 5000)), 3), "> b =", b, " -> multiple equilibria possible")
xs = np.linspace(0.001, 4, 400000)
da = b - r * fp(xs)                               # da/dx = 0 at the folds
roots = xs[np.where(np.diff(np.sign(da)))[0]]
x1, x2 = roots
print("fold x-values:", np.round(roots, 4), " a at folds F1 (lower a):", round(a_of_x(x1), 4), " F2:", round(a_of_x(x2), 4))
# F: forward switch (clear->turbid) happens at the larger a ; backward switch at the smaller a
alo, ahi = sorted([a_of_x(x1), a_of_x(x2)])
print(f"bistable for a in ({alo:.3f}, {ahi:.3f}); width {ahi - alo:.3f}")
for a in (0.02, 0.2, 0.4, 0.7, 1.0):
    g = lambda x: a - b * x + r * f(x)
    xx = np.linspace(0.0, 4, 40001); s = np.sign(g(xx)); idx = np.where(np.diff(s) != 0)[0]
    eq = [round(float(brentq(g, xx[i], xx[i + 1])), 3) for i in idx]
    print(f"  a={a}: equilibria x = {eq}")
# jump size at the forward switch: x just below fold to the other branch
def eq_branch(a, start):
    from scipy.integrate import solve_ivp
    s = solve_ivp(lambda t, x: a - b * x + r * f(x), (0, 400), [start], rtol=1e-10)
    return s.y[0][-1]
print("jump at forward fold (a slightly above the upper fold): x goes from", round(float(x2 if a_of_x(x2) > a_of_x(x1) else x1), 3), "to", round(eq_branch(ahi + 0.01, x2), 3))
print("jump at backward fold (a slightly below the lower fold): x goes from", round(float(x1 if a_of_x(x1) < a_of_x(x2) else x2), 3), "to", round(eq_branch(alo - 0.01, x1), 3))
print("\n== Vollenweider / OECD relation (Lampert & Sommer): P_L = 1.55 [P_in/(1+sqrt(tau))]^0.82")
for tau in (0.5, 1, 4, 10, 100):
    for Pin in (50.0,):
        print(f"  tau_w={tau:6} yr, P_in={Pin} ug/L -> P_L = {1.55 * (Pin / (1 + np.sqrt(tau))) ** 0.82:.1f} ug/L")
print("\n== trophic classes by P_tot (ug/L at spring circulation, Lampert & Sommer): <5 ultra-oligo; 5-10 oligo; 10-30 meso; 30-100 eu; >100 hypereutrophic")
for P in (6, 10, 20, 87, 100):
    cls = "ultra-oligotrophic" if P < 5 else "oligotrophic" if P < 10 else "mesotrophic" if P < 30 else "eutrophic" if P < 100 else "hypereutrophic"
    print(f"  Lake Constance-style P_tot = {P}: {cls}")
print("\n== Lake Washington (Lampert & Sommer, Fig. 8.14 text): sewage diversion finished 1968; transparency 1 m (1960s) -> 3-4 m until 1975 -> up to 10 m after Daphnia returned in 1976 (x2-3)")
print("== global P loading (slide 21): 1.5 Tg/yr; China 30%, India 8%, USA 7%, Spain 6%, Brazil 6%:", 0.30 * 1.5, "Tg China ;", round(0.08 * 1.5, 3), "Tg India")
print("   N:P in domestic sewage ~4:1 (Lampert & Sommer) vs Redfield 16:1 -> shift towards N limitation")
