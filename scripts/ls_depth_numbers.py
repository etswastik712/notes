"""Numbers behind the Landscapes depth layer (one function per chapter).   .venv/bin/python -W ignore scripts/ls_depth_numbers.py [LS01 ...]"""
import math, sys
import numpy as np

def LS01():
    print("== LS01: low-pass filter response of dz/dt = -(z - z_eq(t))/tau, z_eq = A sin(wt) ==")
    for tau, T in [(1e6, 4.1e4), (1e6, 1e5), (1e4, 1e5), (1e3, 1e5), (2e6, 1e5)]:
        w = 2 * math.pi / T; amp = 1 / math.sqrt(1 + (w * tau) ** 2); lag = math.degrees(math.atan(w * tau))
        print(f"tau={tau:.0e} yr, period={T:.1e} yr: amplitude ratio {amp:.4f}, phase lag {lag:.1f} deg, lag time {lag/360*T:.0f} yr")
    print("hillslope response time L^2/D: L=100 m, D=0.01 m2/yr ->", 100**2 / 0.01, "yr; L=50 m, D=0.002 ->", 50**2 / 0.002, "yr")
    print("== magnitude-frequency: lognormal discharge, transport ~ (q - qc)^b for q > qc ==")
    q = np.logspace(-2, 2, 4000); s = 1.0
    f = np.exp(-(np.log(q)) ** 2 / (2 * s * s)) / (q * s * math.sqrt(2 * math.pi))   # pdf of q, median 1
    for qc, b in [(0.0, 1.0), (0.0, 2.0), (0.0, 3.0), (1.0, 2.0)]:
        w = np.where(q > qc, (q - qc) ** b, 0.0) * f * q          # per unit ln q
        k = int(np.argmax(w)); print(f"qc={qc}, b={b}: effective discharge (peak of work) q* = {q[k]:.2f} x median; fraction of total work from q > 10 x median = {w[q>10].sum()/w.sum():.3f}")
    print("== uplift / denudation time: 35 km at 2 mm/yr ==", 35000 / 0.002 / 1e6, "Myr")
    print("== Gutenberg-style magnitude-frequency: P(Q>q) = (q/q0)^-a, work integral converges only if b < a ==")

def LS02():
    yr = 3.156e7
    print("== LS02: Reynolds numbers Re = rho U L / eta ==")
    for nm, rho, U, L, eta in [("glacier (30 m/yr, 100 m, eta 1e13)", 900, 30/yr, 100, 1e13), ("mantle (3 cm/yr, 1000 km, 1e21)", 3300, 0.03/yr, 1e6, 1e21),
                               ("river (2 m/s, 2 m)", 1000, 2, 2, 1e-3), ("wind over dune (10 m/s, 1 m)", 1.2, 10, 1, 1.8e-5),
                               ("basalt lava (1 m/s, 1 m, 100 Pa s)", 2700, 1, 1, 100), ("honey-like film (0.1 m/s, 5 mm, 10 Pa s)", 1400, .1, .005, 10)]:
        print(f"  {nm}: Re = {rho*U*L/eta:.2e}")
    print("== Maxwell time eta/G ==")
    for nm, eta, G in [("mantle (1e21, 70 GPa)", 1e21, 7e10), ("asthenosphere (1e19, 70 GPa)", 1e19, 7e10), ("ice (1e13, 3.5 GPa)", 1e13, 3.5e9), ("warm basalt lava (1e2, 20 GPa)", 1e2, 2e10), ("lower crust (1e20, 40 GPa)", 1e20, 4e10)]:
        t = eta / G; print(f"  {nm}: tau_M = {t:.2e} s = {t/yr:.3g} yr")
    print("== Deborah number De = tau_M / T ==")
    for nm, tau, T in [("mantle, 2 s earthquake wave", 1.4e10, 2), ("mantle, ice age 1e4 yr", 1.4e10, 1e4*yr), ("mantle, orogeny 1e7 yr", 1.4e10, 1e7*yr), ("ice, 1 yr seasonal", 2.9e3, yr)]:
        print(f"  {nm}: De = {tau/T:.2e}")
    print("== lithostatic stress ==  sigma_v = rho g z; K = nu/(1-nu) for nu=0.25:", 0.25/0.75, " at 5 km:", 2700*9.81*5e3/1e6, "MPa")
    print("== Stokes drag from dimensional analysis: F = C mu a U, C = 6 pi =", 6*math.pi)
    mu = 0.6; phi = math.atan(mu); R = (1 + math.sin(phi)) / (1 - math.sin(phi))
    print(f"== Coulomb (cohesionless, mu=0.6): phi={math.degrees(phi):.2f} deg; failure plane angle to sigma1 = 45-phi/2 = {45-math.degrees(phi)/2:.1f} deg; sigma1'/sigma3' = {R:.3f}")
    z = 5e3; sv = 2700*9.81*z/1e6; pp = 1000*9.81*z/1e6; svp = sv - pp
    print(f"  at 5 km: sigma_v = {sv:.1f} MPa, hydrostatic p = {pp:.1f} MPa, effective sigma_v' = {svp:.1f}")
    print(f"  thrust: sigma_H' = {R*svp:.0f} MPa -> differential sigma_H - sigma_v = {R*svp - svp:.0f} MPa; normal: sigma_h' = {svp/R:.1f} -> sigma_v - sigma_h = {svp - svp/R:.1f} MPa; ratio {(R*svp-svp)/(svp-svp/R):.2f}")

def LS03():
    print("== LS03: finite-difference attenuation (wave z = sin kx, lambda = n*Delta) ==")
    for n in (4, 6, 10, 20, 26, 50):
        kd = 2 * math.pi / n; sl = math.sin(kd) / kd; cu = 2 * (1 - math.cos(kd)) / kd ** 2
        print(f"  lambda = {n:3d} Delta: slope (central diff) factor {sl:.4f} (error {100*(1-sl):.2f} %), curvature factor {cu:.4f} (error {100*(1-cu):.2f} %)")
    print("  cells per wavelength for 1% slope error:", 2 * math.pi / math.sqrt(0.06), " for 1% curvature error:", 2 * math.pi / math.sqrt(0.12))
    print("== D8 path length factor f(theta) = cos th + (sqrt2-1) sin th, 0<th<45 ==")
    for th in (0, 10, 22.5, 35, 45):
        t = math.radians(th); print(f"  theta={th}: {math.cos(t) + (math.sqrt(2)-1)*math.sin(t):.4f}")
    print("== drainage density: mean hillslope length ~ 1/(2 Dd) ==")
    for Dd in (0.5, 2, 10, 30): print(f"  Dd = {Dd} /km -> {1000/(2*Dd):.0f} m")
    print("== Hack's law L = 1.4 A^0.6 (km) ==", [round(1.4 * A ** 0.6, 1) for A in (1, 10, 100, 1000, 1e4)])
    print("== Earth hypsometry two-box mean: 29% at +0.84 km, 71% at -3.8 km ==", 0.29 * 0.84 - 0.71 * 3.8)

def LS04():
    print("== LS04: Mercator / TM scale factors ==")
    for ph in (0, 30, 45, 60, 70, 80):
        k = 1 / math.cos(math.radians(ph)); print(f"  lat {ph}: linear scale sec(phi) = {k:.3f}, area scale = {k*k:.3f}")
    print("  Greenland 2.166e6 km2 at ~72N: appears", 2.166e6 / math.cos(math.radians(72)) ** 2 / 1e6, "x1e6 km2 (mean sec^2 at 72 ~ 10.5); Africa 30.37e6 at ~0-> 30.4")
    print("== UTM: k = 0.9996 (1 + (dlam cos phi)^2 / 2) ==")
    for dl in (0, 1, 2, 3):
        for ph in (0, 18.5, 45):
            print(f"  dlam={dl} deg, lat {ph}: k = {0.9996*(1+0.5*(math.radians(dl)*math.cos(math.radians(ph)))**2):.6f}")
    print("== ellipsoid parameters ==")
    a = 6378137.0; f = 1/298.257223563; b = a*(1-f); e2 = f*(2-f)
    print(f"  WGS84 a={a} b={b:.3f} e2={e2:.8f}; a-b = {a-b:.0f} m")
    for ph in (0, 18.5, 45, 90):
        p_ = math.radians(ph); N = a/math.sqrt(1-e2*math.sin(p_)**2); M = a*(1-e2)/(1-e2*math.sin(p_)**2)**1.5
        print(f"  phi={ph}: prime-vertical radius N={N/1e3:.3f} km, meridian radius M={M/1e3:.3f} km; length of 1 deg lat = {math.radians(1)*M/1e3:.3f} km, of 1 deg lon = {math.radians(1)*N*math.cos(p_)/1e3:.3f} km")

def LS05():
    print("== LS05: Darwin-Radau and Clairaut ==")
    G = 6.674e-11; M = 5.972e24; a = 6378137.0; w = 7.2921159e-5
    q = w*w*a**3/(G*M); print("  q = w^2 a^3/GM =", q)
    print("  homogeneous f = 5q/4 =", 1.25*q, "= 1/", 1/(1.25*q))
    f_obs = 1/298.257223563; c_obs = 0.3307
    print("  observed f = 1/298.257 =", f_obs)
    for c in (0.4, 0.3307, 0.3):
        f = 2.5*q/(1 + 6.25*(1 - 1.5*c)**2); print(f"  Darwin-Radau f for C/MR^2={c}: {f:.6f} = 1/{1/f:.1f}")
    c_from_f = (2/3)*(1 - 0.4*math.sqrt(2.5*q/f_obs - 1)); print("  C/MR^2 inferred from observed f and q:", c_from_f)
    print("  equatorial bulge a-c = f a =", f_obs*a/1e3, "km; homogeneous would give", 1.25*q*a/1e3, "km")
    J2 = 1.08263e-3; print("  J2 =", J2, " f ~ (3/2) J2 + q/2 =", 1.5*J2 + 0.5*q)
    print("  geoid undulation range ~ +-100 m vs bulge 21.4 km -> ratio", 100/21385)

def LS06():
    mu = 0.6; phi = math.atan(mu); R = (1 + math.sin(phi)) / (1 - math.sin(phi)); g = 9.81
    print(f"== LS06: R = sigma1'/sigma3' = {R:.3f}")
    for z in (3e3, 5e3, 10e3, 15e3):
        svp = (2700 - 1000) * g * z / 1e6
        print(f"  z={z/1e3:.0f} km: sigma_v' = {svp:.0f} MPa; thrust strength (R-1)sigma_v' = {(R-1)*svp:.0f} MPa; normal strength (1-1/R)sigma_v' = {(1-1/R)*svp:.0f} MPa")
    zc = 2e8 / ((R - 1) * 1700 * g); print(f"  depth at which compressional frictional strength = 2e8 Pa: {zc/1e3:.2f} km; extensional strength there = {(1-1/R)*1700*g*zc/1e6:.0f} MPa")
    for nm, gg, rho in [("Earth", 9.81, 2700), ("Mars", 3.71, 2900), ("Venus", 8.87, 2700), ("Moon", 1.62, 2800), ("Mercury", 3.70, 2700)]:
        print(f"  {nm}: dh_max = 2e8/(rho g) = {2e8/(rho*gg)/1e3:.1f} km")

def LS07():
    G = 7e10; rho = 3300; g = 9.81; mu = 1e21
    print("== LS07: viscous half-space relaxation tau_r = 4 pi mu / (rho g lambda) vs Maxwell time ==")
    for lam in (100e3, 300e3, 1000e3, 3000e3):
        tr = 4 * math.pi * mu / (rho * g * lam); print(f"  lambda={lam/1e3:.0f} km: tau_r = {tr:.3g} s = {tr/3.156e7:.3g} yr; tau_r/tau_M = {tr/(mu/G):.1f}")
    print("  crossover wavelength tau_r = tau_M: 4 pi G/(rho g) =", 4 * math.pi * G / (rho * g) / 1e3, "km")
    print("== Bonneville: deflection 50 m under a lake load of depth ~300 m ==", "water load", 1000 * g * 300 / 1e6, "MPa; Airy-like rebound if fully compensated: w = (rho_w/rho_m) h =", 1000 / 3300 * 300, "m")

def LS08():
    rho, g, al, dT, b, kap, eta = 3300, 9.81, 3e-5, 3000, 2.9e6, 1e-6, 1e21
    Ra = rho*g*al*dT*b**3/(eta*kap); print(f"== LS08: Ra = {Ra:.2e}")
    for Rac in (657.5, 1000, 1708):
        d = b*(Rac/Ra)**(1/3); u = kap/b*(Ra/Rac)**(2/3)
        print(f"  Ra_c = {Rac}: boundary-layer thickness b (Ra_c/Ra)^(1/3) = {d/1e3:.0f} km; velocity scale (kappa/b)(Ra/Ra_c)^(2/3) = {u:.2e} m/s = {u*3.156e7*100:.2f} cm/yr")
    print("  thermal diffusion time across 100 km lithosphere L^2/kappa =", (1e5)**2/kap/3.156e7/1e6, "Myr")
    print("  Peclet number u L/kappa for u=5 cm/yr, L=2900 km:", 0.05/3.156e7*2.9e6/kap)

def LS09():
    print("== LS09: moment magnitude and Gutenberg-Richter ==")
    for Mw in (5, 6, 7, 7.8, 8, 9, 9.5):
        M0 = 10**(1.5*Mw + 9.1); print(f"  Mw={Mw}: M0 = {M0:.2e} N m; ratio to Mw-1 = {10**1.5:.1f}")
    M0 = 10**(1.5*7.8+9.1); A = 150e3*100e3; print(f"  Gorkha-like M0={M0:.2e}: mean slip over 150x100 km with mu=3e10: {M0/(3e10*A):.2f} m")
    for b in (0.8, 1.0, 1.2):
        a = 2*b/3; print(f"  b={b}: P(M0>m) ~ m^-{a:.2f}; moment per magnitude unit grows as 10^({1.5-b:.1f} M) -> largest events dominate: {a<1}")
    print("  number ratio per unit magnitude (b=1):", 10, "; moment ratio:", 10**1.5)
    print("  moment release of one M8 = ", 10**(1.5*8)/10**(1.5*6), "x M6 events;  number of M6 events with the same total moment per M8 (b=1):", 10**(1.5*2)/10**2, "events of M6 per M6-..." )

def LS10():
    E, nu, D = 7e10, 0.25, 1e23
    Te = (12*(1-nu**2)*D/E)**(1/3); print(f"== LS10: D = E Te^3/12(1-nu^2): D=1e23 -> Te = {Te/1e3:.1f} km")
    for nm, drho in [("no infill (air), drho=3300", 3300), ("water infill, drho=2300", 2300), ("sediment infill, drho=900", 900)]:
        a = (4*D/(drho*9.81))**0.25; print(f"  {nm}: alpha = (4D/drho g)^(1/4) = {a/1e3:.1f} km; flexural wavelength 2 pi alpha = {2*math.pi*a/1e3:.0f} km")
    for Te_ in (10e3, 25e3, 50e3, 100e3): print(f"  Te = {Te_/1e3:.0f} km -> D = {E*Te_**3/(12*(1-nu**2)):.2e} N m")

def LS11():
    R = 8.314
    print("== LS11: Arrhenius sensitivity exp[(Ea/R)(1/T0 - 1/T1)] ==")
    for Ea in (30e3, 60e3, 90e3):
        for T0, T1 in [(288, 298), (288, 293), (278, 283)]:
            print(f"  Ea={Ea/1e3:.0f} kJ/mol, {T0}->{T1} K: rate x{math.exp(Ea/R*(1/T0-1/T1)):.3f}")
    print("  CO2 removed per unit mass of CaSiO3 weathered (net 1 CO2 per Ca):", 44.01/116.16, "t/t")
    print("  Ca2+ + 2HCO3- -> CaCO3 + CO2 + H2O: of the 2 CO2 consumed in weathering, 1 is returned at precipitation")

def LS12():
    print("== LS12: diffusive scarp degradation: slope profile = h * Gaussian(sigma^2 = 2 D t); max slope = h/sqrt(4 pi D t) ==")
    h = 10.0; D = 0.01
    for t in (1e3, 1e4, 1e5, 1e6):
        sm = h/math.sqrt(4*math.pi*D*t); print(f"  t={t:.0e} yr: D t = {D*t:.3g} m2; max slope {sm:.3f} = {math.degrees(math.atan(sm)):.1f} deg; scarp width ~ 4 sqrt(D t) = {4*math.sqrt(D*t):.0f} m")
    print("  decay time of a sinusoid lambda=100 m, D=0.01:", 100**2/(4*math.pi**2*0.01), "yr")
    print("  frost creep flux ~ f z_bar^2 : doubling the frost depth multiplies D by 4")

def LS13():
    g = 9.81
    print("== LS13: saturated cohesionless slope critical angle: tan(theta_c) = (1 - rho_w/rho) tan(phi) ==")
    for phi in (20, 30, 35, 40):
        t = (1 - 1000/2000) * math.tan(math.radians(phi)); print(f"  phi={phi}: dry {phi} deg; saturated (rho=2000) {math.degrees(math.atan(t)):.1f} deg")
    print("== critical depth of a cohesive slope z_c = c / (rho g cos^2 th (tan th - tan phi)), rho=1800, phi=30 ==")
    for c in (2e3, 5e3, 10e3):
        for th in (35, 40, 45):
            zc = c/(1800*g*math.cos(math.radians(th))**2*(math.tan(math.radians(th))-math.tan(math.radians(30)))); print(f"  c={c/1e3:.0f} kPa, theta={th}: z_c = {zc:.2f} m")
    print("== size distribution: noncumulative density ~ A^-2.4 (recalled); moment of order q diverges at the large end if q > 1.4 ==")
    for q in (1.0, 1.5): print(f"  q={q}: integral exponent {q-2.4+1:+.1f}; ratio of contributions A_max/A_min = 1e4 ->", 1e4**(q-1.4) if q != 1.4 else 'log')

def LS14():
    rho, g = 917.0, 9.81; A = 2.4e-24; yr = 3.156e7
    print("== LS14: Glen surface speed U_s = (A/2) (rho g sin a)^3 H^4 (n=3) ==")
    for H, al in [(50, 5), (100, 5), (200, 5), (400, 5), (100, 2), (100, 10)]:
        tau = rho*g*H*math.sin(math.radians(al)); U = A/2*(rho*g*math.sin(math.radians(al)))**3*H**4
        print(f"  H={H} m, slope {al} deg: tau_b = {tau/1e3:.0f} kPa, U_s = {U*yr:.2f} m/yr")
    print("  doubling H multiplies U by", 2**4, "(at fixed slope)")
    print("== Nye plastic profile: H^2 = 2 tau0 x /(rho g) ==")
    for tau0 in (5e4, 1e5): 
        for x in (100e3, 500e3, 800e3): print(f"  tau0={tau0/1e3:.0f} kPa, x={x/1e3:.0f} km: H = {math.sqrt(2*tau0*x/(rho*g))/1e3:.2f} km")
    print("  volume response time ~ H / |b_t|: H=100 m, b_t=-3 m/yr ->", 100/3, "yr")

def LS15():
    A_oc = 3.61e14; rho_i, rho_w = 917, 1000
    print("== LS15: sea-level equivalent dz = (rho_i/rho_w) V_ice / A_ocean ==")
    for nm, V in [("Greenland 2.9e6 km3", 2.9e6), ("Antarctica 26.5e6 km3", 26.5e6), ("LGM extra ~47e6 km3", 47e6)]:
        print(f"  {nm}: {rho_i/rho_w*V*1e9/A_oc:.1f} m of sea level")
    print("  ice volume for 120 m:", 120*A_oc*rho_w/rho_i/1e9/1e6, "million km3")
    print("  Airy depression under 3 km of ice:", rho_i/3300*3000, "m;  shelf exposure 29% -> 36% land for -120 m (A&A)")
    print("  a +- 5 m coral depth range (Acropora palmata) -> sea-level uncertainty +-5 m, i.e. 4 % of the 120 m glacial amplitude:", 5/120)

if __name__ == "__main__":
    for c in (sys.argv[1:] or ["LS01"]): globals()[c]()
