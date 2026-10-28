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

if __name__ == "__main__":
    for c in (sys.argv[1:] or ["LS01"]): globals()[c]()
