"""Climate vault, Neena lectures (2025) + Joy readings (2026): numbers quoted in CL16-CL21 and in the tutorial Practice items, recomputed.
    .venv/bin/python -W ignore scripts/cl_neena_numbers.py [tut|cl16|cl17|cl18|cl19|cl20|cl21]
"""
import sys

import numpy as np
from scipy.integrate import solve_ivp

sigma = 5.670374419e-8
S0 = 1361.0
OMEGA = 7.2921e-5


def head(t):
    print("\n== " + t)


def tut():
    head("Neena Tutorial 1 (planetary energy balance)")
    h, c, k = 6.62607015e-34, 2.99792458e8, 1.380649e-23
    lam, T = 0.53e-6, 3000.0
    B = 2 * np.pi * h * c ** 2 / lam ** 5 / (np.exp(h * c / (lam * k * T)) - 1)  # W m^-2 m^-1 (hemispheric flux = pi * radiance)
    print("  Q1: Planck flux density pi B_lam(0.53 um, 3000 K) = %.3e W m^-2 um^-1  (sheet: 1.04e6)" % (B * 1e-6))
    print("  Q2: Wien lambda_max = 2898 um K / T: Sun 5780 K: %.3f um; Earth 290 K: %.2f um" % (2897.77 / 5780, 2897.77 / 290))
    Te = (S0 * 0.7 / (4 * sigma)) ** 0.25
    Td = (S0 * 0.7 / (2 * sigma)) ** 0.25
    print("  Q3: sphere Te = %.1f K; thin disc radiating from both sides, absorbing on one: T = (S(1-a)/(2 sigma))^(1/4) = %.1f K (sheet 303), +%.1f K" % (Te, Td, Td - Te))
    Tm = (9121 * 0.9 / (4 * sigma)) ** 0.25
    print("  Q4: Mercury Te = %.2f K (sheet 436.77); greenhouse = 440 - Te = %.2f K (sheet 4 K)" % (Tm, 440 - Tm))
    print("  Q5: 25%% weaker Sun: Te = 255 (0.75)^(1/4) = %.1f K (sheet 237); from S=1361 a=0.3: %.1f K" % (255 * 0.75 ** 0.25, ((0.75 * S0 * 0.7) / (4 * sigma)) ** 0.25))
    Te2 = 255 * ((1 - 0.47) / (1 - 0.30)) ** 0.25
    print("  Q6: albedo 0.47: Te = 255 ((1-0.47)/(1-0.30))^(1/4) = %.2f K, change %.2f K (sheet -17.22); greenhouse after = 281 - Te = %.1f K (sheet 43)" % (Te2, Te2 - 255, 281 - Te2))
    SJ = S0 / 5.19 ** 2
    TJ = (SJ * 0.55 / (4 * sigma)) ** 0.25
    print("  Q7: Jupiter S = %.1f W m^-2, Te(absorbed only) = %.1f K; with observed 130 K: internal flux = sigma(130^4 - Te^4) = %.2f W m^-2 (sheet '9.3 W', per m^2)" % (SJ, TJ, sigma * (130 ** 4 - TJ ** 4)))

    head("Neena Tutorial 2 (one-layer model, Venus and Earth)")
    for name, S, a, Tobs in (("Venus", 2642.3, 0.75, 735.0), ("Earth", 1369.77, 0.3, 288.0)):
        Te_ = (S * (1 - a) / (4 * sigma)) ** 0.25
        print("  %s: Te = %.1f K, one-layer Ts = 2^(1/4) Te = %.1f K, observed %.0f K, greenhouse (obs - Te) = %.0f K, one-layer greenhouse %.0f K" % (name, Te_, 2 ** 0.25 * Te_, Tobs, Tobs - Te_, (2 ** 0.25 - 1) * Te_))
    Se, ae, Te_ = 1369.77, 0.3, (1369.77 * 0.7 / (4 * sigma)) ** 0.25
    eps = 2 * (1 - (S0 * 0.7 / 4) / (sigma * 288 ** 4))
    print("  leaky layer (Lecture 4): eps for Ts = 288 K: eps = 2 [1 - S(1-a)/(4 sigma Ts^4)] = %.3f (slide 0.77)" % eps)
    print("  Mars (Lecture 4 slide: 590 W m^-2, albedo 0.25): Te = %.1f K" % ((590 * 0.75 / (4 * sigma)) ** 0.25))

    head("Neena Tutorial 5 (daily and seasonal variation)")
    print("  Q1: 1 deg of longitude = 4 min; 8 deg W of the noon meridian: local time 11:28 (32 min before noon)")
    print("  Q2: noon at 40W; 55E is 95 deg east: +%.2f h = 18:20; 80W is 40 deg west: -2.67 h = 09:20; 25S 40W: same longitude: 12:00" % (95 / 15))
    R = 6378.0
    print("  Q3: radius of the latitude circle: 30N %.0f km, 60N %.0f km (R cos lat)" % (R * np.cos(np.radians(30)), R * np.cos(np.radians(60))))
    print("  Q4: 1 deg of longitude: equator %.2f km, 30N %.2f km, 60N %.2f km" % (R * np.pi / 180, R * np.pi / 180 * np.cos(np.radians(30)), R * np.pi / 180 * np.cos(np.radians(60))))
    dec = 23.44
    for lat in (15, -25):
        alt = 90 - abs(lat - dec)
        print("  Q5: summer solstice, lat %+d: noon solar altitude = 90 - |lat - delta| = %.2f deg; S sin(alt) = %.1f W m^-2 (S0 = 1361)" % (lat, alt, S0 * np.sin(np.radians(alt))))
    print("  Q6: equinox noon: equator %.0f, 60N %.1f W m^-2; winter solstice noon: equator %.1f, 60N %.1f (altitude 6.56 deg)" % (S0, S0 * np.cos(np.radians(60)), S0 * np.sin(np.radians(90 - dec)), S0 * np.sin(np.radians(90 - 60 - dec))))
    I = S0 * np.cos(np.radians(60)) * 0.5
    print("  Q7: 60N equinox noon, atmosphere removes 50%%: surface flux %.1f W m^-2; absorbed: forest (a = 0.15) %.1f, ice (a = 0.90) %.1f W m^-2" % (I, I * 0.85, I * 0.10))

    head("Neena Tutorial 6 (apparent forces)")
    TJ = 9 * 3600 + 50 * 60
    wJ = 2 * np.pi / TJ
    RJ = 11.194173 * 6378e3
    print("  Q1: Jupiter: Omega = 2 pi / (9 h 50 min) = %.3e s^-1 (sheet 17.75e-5); equatorial speed %.0f m/s (sheet 12677)" % (wJ, wJ * RJ))
    Re = 6378e3
    Om = 7.29e-5
    v_in = Om * Re - 20.0
    print("  Q2: parcel moving west at 20 m/s on the equator: inertial-frame speed Omega R - 20 = %.2f m/s; (a) centripetal acceleration v^2/R = %.4f m/s^2 (sheet 0.0308)" % (v_in, v_in ** 2 / Re))
    print("      (b) rotating-frame acceleration u^2/R = %.3e m/s^2 (sheet 0.627e-4); (c) vertical Coriolis 2 Omega u = %.3e m/s^2, directed DOWNWARD (toward the ground) for westward motion on the equator (sheet -29.1e-4: the minus sign)" % (20.0 ** 2 / Re, 2 * Om * 20.0))
    f65 = 2 * Om * np.sin(np.radians(65))
    v = 100 / 3.6
    print("  Q3: 1300 kg at 65N, 100 km/h = %.2f m/s: f = %.4e s^-1; a = f v = %.5f m/s^2; F = %.3f N (sheet 0.00366, 4.758 N)" % (v, f65, f65 * v, 1300 * f65 * v))
    f30 = 2 * Om * np.sin(np.radians(30))
    print("  Q4: 100 m in 4 s at 30N: v = 25 m/s, deflection = (1/2) f v t^2 = %.4f m (sheet 0.0146)" % (0.5 * f30 * 25 * 16))


def cl16():
    head("CL16: atmospheric evolution (Neena Lecture 4) and greenhouse gases / carbon cycle (Lecture 6)")
    kB, u = 1.380649e-23, 1.66053907e-27
    gases = {"H2": 2.016, "He": 4.003, "H2O": 18.015, "N2": 28.014, "CO2": 44.01}
    planets = {"Earth": 11.186e3, "Mars": 5.027e3, "Venus": 10.36e3}
    T = 1000.0
    print("  mean thermal speed sqrt(8 k T / (pi m)) at T = %.0f K (an assumed exospheric temperature) and 1/6 of the escape speed:" % T)
    for g, M in gases.items():
        vm = np.sqrt(8 * kB * T / (np.pi * M * u))
        print("    %-4s %.0f m/s" % (g, vm))
    for p, ve in planets.items():
        print("    %-5s v_esc = %.2f km/s, v_esc/6 = %.0f m/s -> loses: %s" % (p, ve / 1e3, ve / 6, ", ".join(g for g, M in gases.items() if np.sqrt(8 * kB * T / (np.pi * M * u)) > ve / 6) or "none"))
    print("  mass fraction below height z for p ~ exp(-z/H): H = 7 km: below 32 km %.4f, below 80 km %.6f; H = 7.5 km: %.4f, %.6f" % (1 - np.exp(-32 / 7), 1 - np.exp(-80 / 7), 1 - np.exp(-32 / 7.5), 1 - np.exp(-80 / 7.5)))
    print("  mass of the atmosphere implied by 1013 hPa at sea level: m = p 4 pi R^2 / g = %.3e kg" % (101300 * 4 * np.pi * 6.371e6 ** 2 / 9.81))
    print("  Venus: observed 462 C = %.0f K (Lecture 6) and Tutorial 2 '735 K'; Earth 288 K = 15 C" % (462 + 273.15))
    print("  lifetimes (Lecture 6): fraction remaining after t = exp(-t/tau): CH4 (12 yr) after 12/36/60 yr: %.3f / %.3f / %.4f; N2O (114 yr) after 114 yr: %.3f; water vapour (10 d) after 30 d: %.3f" % (np.exp(-1), np.exp(-3), np.exp(-5), np.exp(-1), np.exp(-3)))
    print("  Venus atmosphere '90 times as thick': surface pressure ~ 90 bar means 91 x Earth's 1.013 bar = %.0f bar" % (90 * 1.013))
    print("  water vapour: saturation pressure at the triple point = 6.11 hPa (Lecture 6), at 273.16 K")
    print("  Clausius-Clapeyron e_s(T) = 6.11 exp[(L/Rv)(1/273.16 - 1/T)], L = 2.5e6 J/kg, Rv = 461.5: e_s(288 K) = %.2f hPa, e_s(298 K) = %.2f hPa, ratio per 10 K = %.2f (about 7%%/K: %.1f%% per K)" % (
        6.11 * np.exp(2.5e6 / 461.5 * (1 / 273.16 - 1 / 288)), 6.11 * np.exp(2.5e6 / 461.5 * (1 / 273.16 - 1 / 298)),
        np.exp(2.5e6 / 461.5 * (1 / 288 - 1 / 298)), 100 * (np.exp(2.5e6 / 461.5 * 1 / (293.0 ** 2)) - 1)))


def cl17():
    head("CL17: orbital forcing (Neena Lectures 9-10); exact insolation through cl10lib")
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cl10lib import daily_insolation, annual_mean
    for e in (0.0167, 0.0607, 0.05, 0.005):
        print("  e = %.4f: (r_aphelion/r_perihelion)^2 = ((1+e)/(1-e))^2 = %.4f -> perihelion flux is %.1f%% above aphelion" % (e, ((1 + e) / (1 - e)) ** 2, 100 * (((1 + e) / (1 - e)) ** 2 - 1)))
    print("  eccentricity at which the ratio is 1.23 (Lecture 9: '23%% more'): e = %.4f (the lecture's maximum is 0.0607)" % (np.sqrt(1.23) - 1) / (np.sqrt(1.23) + 1)) if False else None
    r = np.sqrt(1.23)
    print("  eccentricity at which the ratio is 1.23 (Lecture 10: 'as large as 23%%'): e = (sqrt(1.23)-1)/(sqrt(1.23)+1) = %.4f" % ((r - 1) / (r + 1)))
    print("  annual-mean insolation scales as (1-e^2)^(-1/2): e = 0.0607 vs 0.005: %.3f %% (Lecture 10: 'about 0.2 %%')" % (100 * ((1 - 0.0607 ** 2) ** -0.5 / (1 - 0.005 ** 2) ** -0.5 - 1)))
    print("  Lecture 9: 3%% distance difference -> 6.8%% flux difference: (1.0167/0.9833)^2 - 1 = %.2f %%" % (100 * ((1.0167 / 0.9833) ** 2 - 1)))
    print("  Earth equatorial bulge: 21 km (Lecture 9) = 6378 - 6357 = %.0f km" % (6378.137 - 6356.752))
    phi = np.radians(65)
    lam = np.pi / 2
    cases = [("present (23.44, e 0.0167, perihelion Jan)", dict(obl=np.radians(23.44), ecc=0.0167, varpi=np.radians(282.9))),
             ("circular orbit, 23.44", dict(obl=np.radians(23.44), ecc=0.0, varpi=0.0)),
             ("cool NH summer: 22.1, e 0.05, aphelion at solstice", dict(obl=np.radians(22.1), ecc=0.05, varpi=np.radians(270))),
             ("warm NH summer: 24.5, e 0.05, perihelion at solstice", dict(obl=np.radians(24.5), ecc=0.05, varpi=np.radians(90)))]
    vals = []
    for nm, kw in cases:
        q = float(daily_insolation(phi, lam, **kw))
        vals.append(q)
        print("  Q(65N, 21 June) %-55s = %.1f W m^-2" % (nm, q))
    print("  warm - cool = %.1f W m^-2 = %.1f %% of the present value; Lecture 10: 'obliquity and precession can change seasonal insolation by 10-12 %%'" % (vals[3] - vals[2], 100 * (vals[3] - vals[2]) / vals[0]))
    for ob in (22.1, 23.44, 24.5):
        q0 = vals[0]
    qo1 = float(daily_insolation(phi, lam, obl=np.radians(22.1), ecc=0.0167, varpi=np.radians(282.9)))
    qo2 = float(daily_insolation(phi, lam, obl=np.radians(24.5), ecc=0.0167, varpi=np.radians(282.9)))
    print("  obliquity alone (present orbit): Q(65N, June solstice) = %.1f (22.1 deg), %.1f (23.44), %.1f (24.5): range %.1f W m^-2 = %.1f %% of the present value" % (qo1, q0, qo2, qo2 - qo1, 100 * (qo2 - qo1) / q0))
    qp = [float(daily_insolation(phi, lam, obl=np.radians(23.44), ecc=0.0167, varpi=np.radians(v))) for v in (90, 270)]
    print("  precession alone (e = 0.0167, obliquity 23.44): perihelion at the June solstice %.1f vs at the December solstice %.1f: range %.1f W m^-2 = %.1f %%" % (qp[0], qp[1], qp[0] - qp[1], 100 * (qp[0] - qp[1]) / q0))
    print("  annual mean at the pole, obliquity %.2f: %.1f W m^-2; at 65N: %.1f; at the equator: %.1f" % (ob, float(annual_mean(np.pi / 2, obl=np.radians(ob))), float(annual_mean(phi, obl=np.radians(ob))), float(annual_mean(0.0, obl=np.radians(ob)))))
    print("  precession at fixed e = 0.05, obliquity 23.44: Q(65N, June solstice) for perihelion longitude varpi (solar longitude of perihelion):")
    for vp in (0, 90, 180, 270):
        print("    varpi = %3d deg: %.1f W m^-2" % (vp, float(daily_insolation(phi, lam, obl=np.radians(23.44), ecc=0.05, varpi=np.radians(vp)))))
    print("  precession of the equinoxes 25,700 yr (Lecture 9): 360 deg / 25700 yr = %.4f deg/yr; half a cycle = %.0f yr; the lecture's 13,000 yr ago = half a cycle" % (360 / 25700, 25700 / 2))
    print("  apsidal precession 112,000 yr; combined climatic precession period 1/(1/25700 + 1/112000) = %.0f yr (the usual ~21-23 kyr)" % (1 / (1 / 25700 + 1 / 112000)))
    print("  glacier mass balance: LGM ice covered 32%% of land: land area 1.49e8 km^2 -> %.2e km^2" % (0.32 * 1.489e8))


def cl18():
    head("CL18: ocean as the climate system's heat reservoir (Neena Lecture 20; Hartmann Ch. 4, 7; Stewart Ch. 5, 6)")
    n = 1.33
    print("  Fresnel reflectivity at normal incidence (n-1)^2/(n+1)^2 = %.4f (Stewart: 0.02); speed of light in water c/n = %.3e m/s (Stewart: 2.25e8)" % ((n - 1) ** 2 / (n + 1) ** 2, 2.998e8 / n))
    c = np.log(10) / 90
    print("  Jerlov type I water: 10%% of 465 nm light at 90 m -> c = ln10/90 = %.4f m^-1; 1%% level at %.0f m (the euphotic zone of Lecture 20: ~200 m); e-folding depth %.0f m" % (c, np.log(100) / c, 1 / c))
    print("  Hartmann: solar flux halves within ~1 m under average conditions: effective c = ln2/1 m = %.2f m^-1 (total solar, dominated by the red and infrared)" % np.log(2))
    Cp, g = 1004.0, 9.81
    Ca = Cp * 1.013e5 / g
    Cw = 1000 * 4218.0
    print("  heat capacity of the atmosphere C_a = c_p p_s / g = %.3e J m^-2 K^-1 = %.2f m of water (c_w rho = %.3e per m): Hartmann 'a little over 2 m'" % (Ca, Ca / Cw, Cw))
    print("  top 70 m of ocean: %.3e J m^-2 K^-1 = %.1f x the atmosphere (Hartmann: 'about 30')" % (70 * Cw, 70 * Cw / Ca))
    print("  Stewart seasonal storage: ocean 100 m, dT = 10 K: %.1e J/m^2; land 1 m of rock (3000 kg/m^3, 800 J/kg/K), dT = 20 K: %.1e J/m^2; ratio %.0f (Stewart writes 100; the arithmetic gives 83)" % (4000 * 1e5 * 10, 800 * 3000 * 20, 4000 * 1e5 * 10 / (800 * 3000 * 20)))
    print("  heat needed to warm the top 100 m by 5 K in 3 months (Hartmann Ex. 4.1): %.1f W m^-2; for the atmosphere warming 20 K: %.1f W m^-2" % (100 * Cw * 5 / (0.25 * 3.156e7), Ca * 20 / (0.25 * 3.156e7)))
    D = 5e-7
    print("  soil: thermal diffusivity %.0e m^2/s: sqrt(D tau/(2 pi)) for 1 day / 1 yr / 1e4 yr = %.3f / %.2f / %.0f m  (Hartmann quotes 10 cm, 1.5 m, 150 m; the printed (4.10) lost a factor: sqrt(D tau) would be %.2f / %.1f / %.0f m)" % (
        D, np.sqrt(D * 86400 / (2 * np.pi)), np.sqrt(D * 3.156e7 / (2 * np.pi)), np.sqrt(D * 3.156e11 / (2 * np.pi)), np.sqrt(D * 86400), np.sqrt(D * 3.156e7), np.sqrt(D * 3.156e11)))
    print("  Stewart Fig. 5.6 closure: TOA 342 = 107 + 235: %d; surface 168 + 324 = %d vs 390 + 78 + 24 = %d; atmosphere 67 + 78 + 24 + 350 = %d vs 165 + 30 + 324 = %d; OLR 235 = 165 + 30 + 40: %d" % (107 + 235, 168 + 324, 390 + 78 + 24, 67 + 78 + 24 + 350, 165 + 30 + 324, 165 + 30 + 40))
    # bulk formulae (Stewart 5.10): Q_S = rho_a c_p C_S U (ts - ta); Q_L = rho_a L_E C_L U (qs - qa)
    rho_a, cpa, CS, CL, LE = 1.3, 1030.0, 1.0e-3, 1.2e-3, 2.5e6
    def qsat(Tc, p=1013.0):
        e = 6.112 * np.exp(17.67 * Tc / (Tc + 243.5))
        return 0.622 * e / (p - 0.378 * e)
    for (U, ts, ta, RH, lab) in ((8.0, 27.0, 25.0, 0.80, "tropical trade-wind ocean"), (10.0, 20.0, 10.0, 0.70, "Gulf Stream under cool continental air (winter)"), (5.0, 15.0, 15.0, 0.80, "calm, neutral")):
        qs, qa = qsat(ts), RH * qsat(ta)
        QS_, QL_ = rho_a * cpa * CS * U * (ts - ta), rho_a * LE * CL * U * (qs - qa)
        print("  bulk formulae, %s: U = %.0f m/s, ts = %.0f C, ta = %.0f C, RH = %.0f %%: qs = %.4f, qa = %.4f; Q_S = %.1f, Q_L = %.1f W m^-2 (upward)" % (lab, U, ts, ta, 100 * RH, qs, qa, QS_, QL_))
    print("  Stewart's annual-mean ranges: Q_SW 30-260, Q_LW -60 to -30, Q_L -130 to -10, Q_S -42 to -2 W m^-2")
    print("  wind stress tau = rho_a C_D U10^2 with C_D = (0.50 + 0.071 U10) 1e-3: U10 = 6 m/s: %.4f N m^-2; 10 m/s: %.4f; 15 m/s: %.4f" % tuple(rho_a * (0.5 + 0.071 * U) * 1e-3 * U ** 2 for U in (6.0, 10.0, 15.0)))
    print("  Stewart: a +-15 W m^-2 flux error warms/cools a 100 m column by %.2f K in a year" % (15 * 3.156e7 / (100 * Cw)))
    print("  ocean 20%% of heat at 35N: total transport 6 PW -> NH ocean %.2f PW, SH (8%%) %.2f PW" % (0.22 * 6, 0.08 * 6))
    print("  slab ocean seasonal cycle, mixed layer depth h: dT/dt = (Q_net)/(rho c h): amplitude A = Q_amp / (omega rho c h): Q_amp = 100 W m^-2, h = 50 m: %.1f K; h = 25 m: %.1f K; h = 100 m: %.1f K (omega = 2 pi / 1 yr; no damping)" % tuple(100 / (2 * np.pi / 3.156e7 * Cw * h) for h in (50, 25, 100)))
    print("  mixed layer with Newtonian damping: tau = rho c h / lambda, lambda = 20 W m^-2 K^-1, h = 50 m: tau = %.2f yr" % (Cw * 50 / 20 / 3.156e7))


def cl19():
    head("CL19: wind-driven circulation (Neena Lectures 21-22; Stewart Ch. 9; Hartmann Ch. 7)")
    for lat in (11, 30, 45, 60):
        f = 2 * OMEGA * np.sin(np.radians(lat))
        print("  lat %2d: f = %.3e s^-1; inertial period 2 pi/f = %.1f h; Ekman mass transport M = tau/f for tau = 0.1 N/m^2: %.0f kg/(m s) -> %.2f m^2/s" % (lat, f, 2 * np.pi / f / 3600, 0.1 / f, 0.1 / f / 1025))
    f30 = 2 * OMEGA * np.sin(np.radians(30))
    print("  volume transport across a 1000 km wide section at 30N, tau = 0.1: %.2f Sv (1 Sv = 1e6 m^3/s)" % (0.1 / f30 / 1025 * 1e6 / 1e6))
    f11 = 2 * OMEGA * np.sin(np.radians(11))
    print("  Chereskin and Roemmich at 11N: Q = 8.8 Sv from winds: tau L = Q rho f = %.0f N/m; over an assumed 4000 km the implied mean stress is %.3f N/m^2" % (8.8e6 * 1025 * f11, 8.8e6 * 1025 * f11 / 4e6))
    # Ekman spiral with constant eddy viscosity (my derivation); north hemisphere, wind stress tau in +y direction (south wind)
    print("  Ekman spiral (constant eddy viscosity Az, depth z <= 0), D_E = sqrt(2 Az/|f|): u + i v = (sqrt(2) tau/(rho |f| D_E)) exp(z/D_E) exp(i (z/D_E - pi/4)) for stress along +x ... check numerically:")
    Az, f, rho, tau = 0.1, 1e-4, 1025.0, 0.1
    DE = np.sqrt(2 * Az / f)

    def rhs(z, y):  # y = [u, v, u', v']; Az u'' = -f v ... momentum: f v = -Az u''?  (steady, no pressure gradient): -f v = Az u_zz ; f u = Az v_zz  (NH, f>0)
        u, v, du, dv = y
        return [du, dv, -f * v / Az, f * u / Az]
    # boundary: stress at z=0: rho Az du/dz = tau (x-direction), dv/dz = 0 ; decay at depth: use analytic solution
    a = np.sqrt(f / (2 * Az))  # = 1/DE
    # analytic: w = u + i v ; i f w = Az w_zz ... for NH: w_zz = (i f/Az) w -> w = W exp((1+i) a z) ; tau/(rho Az) = w_z(0) = (1+i) a W
    W = tau / (rho * Az) / ((1 + 1j) * a)
    z = np.linspace(0, -3 * np.pi * DE, 2001)
    w = W * np.exp((1 + 1j) * a * z)
    ang = np.degrees(np.angle(w[0]))
    print("    D_E = sqrt(2 Az/f) = %.1f m (Az = %.1f m^2/s, f = %.0e); surface current speed %.4f m/s directed %.1f deg from the +x stress (clockwise = to the right in the NH: %.1f)" % (DE, Az, f, abs(w[0]), ang, ang))
    print("    speed ratio at z = -D_E: %.4f (= 1/e = %.4f), rotation there %.1f deg; at z = -pi D_E: ratio %.4f (= e^-pi = %.4f), direction relative to the surface current %.0f deg (opposite)" % (abs(np.interp(-DE, z[::-1], np.abs(w)[::-1])) / abs(w[0]), np.exp(-1), np.degrees(np.angle(np.interp(-DE, z[::-1], w.real[::-1]) + 1j * np.interp(-DE, z[::-1], w.imag[::-1]))) - ang, abs(np.interp(-np.pi * DE, z[::-1], np.abs(w)[::-1])) / abs(w[0]), np.exp(-np.pi), abs(np.degrees(np.angle(w[np.argmin(abs(z + np.pi * DE))]) - np.angle(w[0])))))
    M = np.trapezoid(w, z) * rho  # integral from 0 downwards: z decreasing -> sign
    M = -M
    print("    transport M = rho Int u dz = (%.1f %+.1fj) kg/(m s) (a perpendicular to the stress: %.1f deg), |M| = %.1f vs tau/f = %.1f" % (M.real, M.imag, np.degrees(np.angle(M)), abs(M), tau / f))
    # Ekman pumping: w_E = curl(tau/(rho f))
    print("  Ekman pumping: w_E = curl_z(tau)/(rho f): a wind-stress curl of -1e-7 N/m^3 at 30N gives %.2e m/s = %.1f m/yr (downwelling for negative curl in the NH)" % (-1e-7 / (rho * f30), -1e-7 / (rho * f30) * 3.156e7))
    print("  Lecture 22: sea-level hump of ~1 m in the centre of a subtropical gyre of half-width L = 2500 km at 30N: geostrophic speed g d_eta / (f L) = %.3f m/s" % (9.81 * 1.0 / (f30 * 2.5e6)))
    print("  Gulf Stream transport 1e15 W: Q = rho c_p dT V: dT = 10 K, V = 30 Sv: %.2e W (Lecture 22: ~1e15 J/s)" % (1025 * 3990 * 10 * 30e6))


def cl20():
    head("CL20: ENSO (Neena Lecture 23)")
    g = 9.81
    rho = 1025.0
    for H, L, deta in ((150.0, 1.5e7, 0.5), (100.0, 1.5e7, 0.5), (200.0, 1.5e7, 0.5), (150.0, 1.2e7, 0.5)):
        print("  zonal pressure gradient balanced by wind stress: tau = rho g H deta/L with H = %.0f m, L = %.0f km, deta = %.1f m: tau = %.4f N/m^2" % (H, L / 1e3, deta, rho * g * H * deta / L))
    print("  bulk stress for U10 = 6 m/s (Stewart): %.4f N/m^2" % (1.3 * (0.5 + 0.071 * 6) * 1e-3 * 36))
    print("  Walker circulation: 0.5 m sea-level difference corresponds to a thermocline depth change of delta_h = (rho/(drho)) delta_eta: for a reduced gravity g' = g drho/rho = 0.03 m/s^2: delta_h = g delta_eta / g' = %.0f m (the 'reduced gravity' step is my addition, drho/rho = 0.003 assumed)" % (g * 0.5 / 0.03))
    print("  El Nino: 1983 anomaly, Nino index, SOI = standardised SLP(Tahiti) - SLP(Darwin): negative during El Nino (Lecture 23: Tahiti pressure lower, Darwin higher)")
    print("  teleconnection speed: an eastward-propagating Kelvin wave with c = sqrt(g' H1) = sqrt(0.03 x 150) = %.1f m/s crosses 15,000 km in %.0f days (my illustration; reduced gravity assumed)" % (np.sqrt(0.03 * 150), 1.5e7 / np.sqrt(0.03 * 150) / 86400))
    # toy Bjerknes feedback: dT/dt = a T - b T^3  (symmetric), plus noise-free: not claimed physical: skip numerics


def cl21():
    head("CL21: thermohaline circulation, water masses and sea ice (Neena Lecture 24)")
    V = 1.335e18
    yr = 3.156e7
    for tau in (600, 1000):
        print("  ocean volume 1.335e18 m^3 (recalled, not in the lectures) renewed in %d yr needs %.0f Sv" % (tau, V / (tau * yr) / 1e6))
    print("  brine rejection (my mass balance): freeze a fraction f of seawater of salinity 35 into ice of salinity S_i; the remaining water has S = (35 - f S_i)/(1 - f):")
    for f in (0.05, 0.10, 0.20):
        for Si in (0.0, 5.0):
            print("    f = %.2f, S_ice = %.0f: S_water = %.2f (+%.2f)" % (f, Si, (35 - f * Si) / (1 - f), (35 - f * Si) / (1 - f) - 35))
    print("  freezing point: Lecture 24 'about -1.8 C' for S ~ 35: depression %.3f K per unit of salinity" % (1.8 / 35))
    print("  Antarctic Circumpolar Current: using the lecture's maxima together (20 cm/s, width 2000 km, depth 3000 m) gives an upper bound of %.0f Sv; the mean speed over the section is far below the maximum" % (0.2 * 2e6 * 3000 / 1e6))
    print("  14C: radioactive decay with half-life 5730 yr (recalled): water ventilated 600 yr ago retains %.3f of its 14C relative to the surface; 1000 yr: %.3f" % (0.5 ** (600 / 5730), 0.5 ** (1000 / 5730)))
    print("  heat/CO2 storage: ocean heat capacity ratio vs atmosphere for the whole ocean (3700 m mean depth): %.0f x" % (3700 * 4.218e6 / (1004 * 1.013e5 / 9.81)))
    print("  linearised teaching equation of state rho = rho0 [1 - alpha (T - T0) + beta (S - S0)] with rho0 = 1027, T0 = 10, S0 = 35, alpha = 2e-4, beta = 7.6e-4:")
    for nm, T, S in (("tropical surface", 27.0, 35.5), ("subtropical salty surface", 25.0, 37.0), ("subpolar surface (fresh)", 5.0, 33.5), ("North Atlantic winter (cold, salty)", 2.0, 35.1), ("Weddell shelf brine", -1.8, 34.8)):
        print("    %-35s T = %5.1f, S = %5.2f: rho = %.2f" % (nm, T, S, 1027 * (1 - 2e-4 * (T - 10) + 7.6e-4 * (S - 35))))


if __name__ == "__main__":
    w = sys.argv[1:] or ["tut", "cl16", "cl17", "cl18", "cl19", "cl20", "cl21"]
    for k in w:
        globals()[k]()
