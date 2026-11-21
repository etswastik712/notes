#!/usr/bin/env python3
"""Independent re-implementation of BEAM (Glotter et al. 2014), the model behind Joy's "Three Boxes of Carbon" app (O7).
Constants as the app lists them (Glotter Table 3); emissions (carbon that went into air + sea, GtC/yr, 1750-2024) are read
as JSON data from the mirrored app page (untrusted data: parsed, never executed).  Solver: scipy solve_ivp (LSODA), not the
app's RK4, so agreement is a real check.  Run: .venv/bin/python -I scripts/cl_carbon_boxes.py   (added 2026-11-21, CL29/CL30)
"""
import json, re
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/carbon-boxes/index.html"
DATA = json.loads(re.search(r"const DATA = (\{.*?\});", PAGE.read_text(), re.S).group(1))
E_HIST, Y0, RATE = np.array(DATA["emis"]), DATA["y0"], DATA["rate"]

DELTA, KH, K1, K2, AM, OM, ALK = 50, 1.23e3, 8.00e-7, 4.53e-10, 1.77e20, 7.8e22, 767.0
A = KH * AM / (OM / (DELTA + 1))
GPP, PPM0 = 2.124, 280.0


def h_of(m):  # [H+] from upper-ocean carbon at fixed alkalinity (Glotter eq. 13 as a quadratic in x = 1/[H+])
    r = m / ALK; a = (2 * r - 1) * K1 * K2; b = (r - 1) * K1
    return 1 / ((-b + np.sqrt(b * b + 4 * a)) / (2 * a))


B_of = lambda h: 1 / (1 + K1 / h + K1 * K2 / h**2)
MAT0 = PPM0 * GPP
MUP0 = brentq(lambda m: A * B_of(h_of(m)) * m - MAT0, 300, 3000)
MLO0 = DELTA * MUP0
B0 = B_of(h_of(MUP0))
AB = lambda m, chem=True: A * (B_of(h_of(m)) if chem else B0)
ph = lambda m: -np.log10(h_of(m))


def settle(added, chem=True):
    tot = MAT0 + MUP0 + MLO0 + added
    m = brentq(lambda m: AB(m, chem) * m + m * (1 + DELTA) - tot, MUP0 * 0.5, MUP0 * 4)
    return AB(m, chem) * m


def emis_hist(stop):
    def e(t):
        if t >= stop: return 0.0
        i = int(np.floor(t - Y0))
        return E_HIST[i] if i < len(E_HIST) else RATE
    return e


def run(mode="history", stop=2025, turn=1000.0, katime=5.0, chem=True, pulse=0.0, t_end=None):
    ka, kd = 1 / katime, DELTA / turn
    if mode == "history":
        t0 = Y0; e = emis_hist(stop); y0 = [MAT0, MUP0, MLO0]; t_end = t_end or 2100
    else:
        t0 = 0.0; e = lambda t: 0.0; y0 = [MAT0 + pulse, MUP0, MLO0]; t_end = t_end or 10000
    def f(t, s):
        fa = ka * (s[0] - AB(s[1], chem) * s[1]); fd = kd * (s[1] - s[2] / DELTA)
        return [e(t) - fa, fa - fd, fd]
    # integrate piecewise across yearly emission steps for accuracy in the history
    if mode == "history":
        knots = list(np.arange(t0, min(stop, t_end), 1.0)) + [min(stop, t_end), t_end]
    else:
        knots = [0.0, 1.0, 10.0, 100.0, 1000.0, t_end]
    knots = sorted(set(k for k in knots if t0 <= k <= t_end))
    T, Y = [], []
    y = np.array(y0, float)
    for a, b in zip(knots[:-1], knots[1:]):
        sol = solve_ivp(f, (a, b), y, method="LSODA", rtol=1e-9, atol=1e-6, dense_output=False, t_eval=np.linspace(a, b, max(2, int(b - a) + 1) if mode == "history" else 50))
        T.extend(sol.t[:-1]); Y.extend(sol.y.T[:-1]); y = sol.y[:, -1]
    T.append(knots[-1]); Y.append(y)
    T, Y = np.array(T), np.array(Y)
    if mode == "history":
        added = sum(E_HIST[i] * min(1, stop - (Y0 + i)) for i in range(len(E_HIST)) if Y0 + i < stop) + max(0, stop - (Y0 + len(E_HIST))) * RATE
    else:
        added = pulse
    return T, Y, added


def at(T, Y, year, k=0):
    return float(np.interp(year, T, Y[:, k]))


if __name__ == "__main__":
    print(f"A = {A:.4f}; MUP0 = {MUP0:.1f} GtC (app: 714); pH0 = {ph(MUP0):.3f} (app 8.29); 1/B0 = {1/B0:.1f} (handout ~170); AB0 = {A*B0:.3f} (handout 0.83)")
    print(f"total carbon / air = {(MAT0+MUP0+MLO0)/MAT0:.1f} (handout 'about 60 times')")
    eps = 1.0
    dAB = (AB(MUP0 + eps) * (MUP0 + eps) - AB(MUP0) * MUP0) / eps
    print(f"d(AB*MUP)/dMUP at start = {dAB:.2f} (handout: ~13 GtC in air per GtC in top) -> top catches up in 1/(ka*(1+{dAB:.1f})) = {5/(1+dAB)*12:.1f} months")

    print("=== handout Run 1/2 and the turnover table (history, emissions stop 2025)")
    print(" turnover  CO2_2024  uptake_2015-24  settles   air/up/deep share 2024")
    for turn in (1000, 500, 300, 200, 100):
        T, Y, added = run(stop=2025, turn=turn, t_end=2100)
        co2 = at(T, Y, 2024.5) / GPP
        upt = np.mean([ (at(T, Y, yr + 1, 1) + at(T, Y, yr + 1, 2)) - (at(T, Y, yr, 1) + at(T, Y, yr, 2)) for yr in range(2015, 2025)])
        tot = sum((at(T, Y, 2025, k) - [MAT0, MUP0, MLO0][k]) for k in range(3))
        sh = [ (at(T, Y, 2025, k) - [MAT0, MUP0, MLO0][k]) / tot for k in range(3)]
        print(f"  {turn:5d}   {co2:6.0f}    {upt:5.2f}          {settle(added)/GPP:5.0f}     {sh[0]:.0%}/{sh[1]:.0%}/{sh[2]:.0%}   (added {added:.0f} GtC)")
    T, Y, added = run(stop=2025, turn=200, t_end=2025)
    print("  turnover 200: CO2 1959/1994/2024 =", [round(at(T, Y, y + 0.5) / GPP) for y in (1959, 1994, 2024)], "(handout 313, 359, 422; Mauna Loa 316, 359, 425)")
    for turn in (1000, 200):
        T, Y, _ = run(stop=2025, turn=turn, t_end=2025)
        yr = next(y for y in range(1900, 2026) if at(T, Y, y + 0.5) / GPP >= 380)
        print(f"  turnover {turn}: first annual mean >= 380 ppm in {yr} (handout 1989 / 2006)")
    print(f"  settled share of the 522 GtC left in air = {(settle(added) - MAT0)/added:.0%} (handout 22%)")

    print("=== handout Run 3 (air-sea time, turnover 200)")
    for kt in (1, 5, 20):
        T, Y, _ = run(stop=2025, turn=200, katime=kt, t_end=2025)
        upt = np.mean([(at(T, Y, yr + 1, 1) + at(T, Y, yr + 1, 2)) - (at(T, Y, yr, 1) + at(T, Y, yr, 2)) for yr in range(2015, 2025)])
        print(f"  ka time {kt:2d} yr: CO2 2024 = {at(T, Y, 2024.5)/GPP:.0f} ppm, uptake {upt:.2f} GtC/yr (handout 420..431, 3.4..3.1)")

    print("=== handout Run 4 (stop later, turnover 200)")
    for stop in (2025, 2050, 2075, 2100, 2150):
        T, Y, added = run(stop=stop, turn=200, t_end=3000)
        peak = Y[:, 0].max() / GPP; s = settle(added) / GPP
        print(f"  stop {stop}: added {added:6.0f} GtC, peak {peak:4.0f} ppm, pH at stop {ph(at(T, Y, stop, 1)):.2f}, settles {s:4.0f} ppm, share {(settle(added)-MAT0)/added:.0%}")
    T, Y, added = run(stop=2025, turn=200, t_end=3000)
    s = settle(added); c25 = at(T, Y, 2025)
    half = next(y for y in range(2025, 3001) if at(T, Y, y) <= s + 0.5 * (c25 - s)); nine = next(y for y in range(2025, 3001) if at(T, Y, y) <= s + 0.1 * (c25 - s))
    T2, Y2, _ = run(stop=2025, turn=1000, t_end=4000); c25b = at(T2, Y2, 2025)
    half2 = next(y for y in range(2025, 4001) if at(T2, Y2, y) <= s + 0.5 * (c25b - s)); nine2 = next(y for y in range(2025, 4001) if at(T2, Y2, y) <= s + 0.1 * (c25b - s))
    print(f"  after stopping in 2025: halfway to settled by {half} / nine-tenths by {nine} (200 yr; handout 2066/2156); 1000 yr: {half2}/{nine2} (handout 2229/2667)")

    print("=== handout Run 5/6 (pulses, turnover 1000) and exercise Q7")
    for P in (100, 1000, 5000):
        for chem in (True, False):
            T, Y, _ = run(mode="pulse", pulse=P, turn=1000, chem=chem, t_end=10000)
            sh = [(at(T, Y, t) - MAT0) / P for t in (10, 100, 1000)]
            print(f"  {P:5d} GtC chem={'on ' if chem else 'off'}: in air after 10/100/1000 yr = {sh[0]:.0%}/{sh[1]:.0%}/{sh[2]:.0%}; settled {(settle(P, chem)-MAT0)/P:.1%}; min pH {ph(Y[:,1].max()):.2f}")
    print(f"  no-chemistry pencil check: AB0/(AB0+1+delta) = {A*B0/(A*B0+1+DELTA):.2%}")

    print("=== exercise Q1 (turnover 200, 2024 shares) and GCB comparison")
    gcb_air, gcb_ocean = 0.41 * 752, 0.28 * 752
    print(f"  GCB: air share of (air + ocean) = {gcb_air/(gcb_air+gcb_ocean):.0%}  (= {gcb_air:.0f}/({gcb_air:.0f}+{gcb_ocean:.0f}))")
    print("=== exercise Q2 pencil check")
    print(f"  334 ppm - 280 = 54 ppm = {54*GPP:.0f} GtC; share of 522 = {54*GPP/522:.0%}")
    print("=== exercise Q3 (peaks)")
    for kt, turn in ((5, 200), (10, 200), (5, 400)):
        T, Y, added = run(stop=2025, turn=turn, katime=kt, t_end=2100)
        print(f"  ka time {kt}, turnover {turn}: peak {Y[:,0].max()/GPP:.1f} ppm, settles {settle(added)/GPP:.0f}")
    print("=== exercise Q4 (2050 stop vs pulses, turnover 200)")
    T, Y, added = run(stop=2050, turn=200, t_end=3000)
    print(f"  stop 2050: added {added:.0f} GtC, peak {Y[:,0].max()/GPP:.0f}, settles {settle(added)/GPP:.1f}")
    for P in (700, 800):
        T, Y, _ = run(mode="pulse", pulse=P, turn=200, t_end=10000)
        print(f"  pulse {P}: peak {Y[:,0].max()/GPP:.0f} ppm, settles {settle(P)/GPP:.1f}")
    print("=== exercise Q5 (stop 2050; CO2 in 2100 and 3000)")
    for turn in (200, 1000):
        T, Y, added = run(stop=2050, turn=turn, t_end=3000)
        print(f"  turnover {turn}: 2100 {at(T, Y, 2100)/GPP:.0f} ppm, 3000 {at(T, Y, 3000)/GPP:.0f} ppm, settles {settle(added)/GPP:.0f}")
    print("=== exercise Q6 (pH at stop, H+ ratio)")
    for stop in (2025, 2075, 2150):
        T, Y, _ = run(stop=stop, turn=200, t_end=stop + 1)
        p = ph(at(T, Y, stop, 1)); print(f"  stop {stop}: pH {p:.2f}, [H+] x {10**(8.29-p):.2f} of pre-industrial")
