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

if __name__ == "__main__":
    for c in (sys.argv[1:] or ["LS01"]): globals()[c]()
