"""Numbers and checks for LS21-LS24 (rivers, bedrock channels, sediment transport; Anderson and Anderson Ch. 12-14).

    .venv/bin/python -W ignore scripts/ls_rivers_numbers.py            # all sections
    .venv/bin/python -W ignore scripts/ls_rivers_numbers.py 21 23      # chosen chapters

Every number quoted in the chapters comes from here.  Each derived identity is checked by a second route (numerical
quadrature, a finite-difference solution, or an exact special case) and asserted, so a wrong formula fails loudly.
"""
import math
import sys

import numpy as np
from scipy import integrate, optimize, special, stats

G = 9.81
RHO, RHO_S = 1000.0, 2650.0
S_REL = RHO_S / RHO                   # specific gravity of quartz
NU = 1.0e-6                           # kinematic viscosity of water, m2/s (about 20 C)
KAPPA = 0.4                           # von Karman constant
YR = 365.25 * 86400.0


def head(s):
    print("\n" + "=" * 100 + f"\n{s}\n" + "=" * 100)


def ok(name, cond):
    print(("  ok   " if cond else "  FAIL ") + name)
    assert cond, name


# ============================================================================================================ LS21
def ls21():
    head("LS21  River hydraulics: turbulent open-channel flow and hydraulic geometry")
    # ---- laminar sheet flow vs a river
    H, S = 1e-3, 0.01
    U = G * S * H ** 2 / (3 * NU)
    print(f"laminar sheet flow H=1 mm, S=0.01: <u> = g S H^2/(3 nu) = {U*100:.2f} cm/s, Re = H<u>/nu = {H*U/NU:.0f}")
    H, S = 2.0, 1e-3
    Ulam = G * S * H ** 2 / (3 * NU)
    ustar = math.sqrt(G * H * S)
    print(f"river H=2 m, S=1e-3: laminar formula would give {Ulam:.0f} m/s (absurd); u* = sqrt(gHS) = {ustar:.3f} m/s")
    D = 0.030
    z0 = D / 30
    lnr = math.log(H / z0)
    Ub = ustar / KAPPA * (lnr - 1)
    nut = KAPPA * ustar * H / 6
    print(f"gravel bed D=30 mm -> z0=D/30={z0*1e3:.1f} mm, H/z0={H/z0:.0f}, <U> = u*/k [ln(H/z0)-1] = {Ub:.2f} m/s")
    print(f"depth-mean eddy viscosity k u* H/6 = {nut:.4f} m2/s = {nut/NU:.2e} x molecular; Re = {H*Ub/NU:.2e}")
    # ---- six-tenths rule: numerical check
    for ratio in (1e2, 1e3, 1e4):
        zz0 = 1.0
        Hh = ratio
        f = lambda z: math.log(z / zz0)
        mean = integrate.quad(f, zz0, Hh)[0] / (Hh - zz0)
        zm = optimize.brentq(lambda z: f(z) - mean, zz0 * 1.0001, Hh)
        print(f"  H/z0={ratio:7.0f}: mean at z_m/H = {zm/Hh:.4f}   (1/e = {1/math.e:.4f});  U_surface/<U> = {f(Hh)/mean:.3f}")
    ok("six-tenths rule: z_m/H -> 1/e", abs(zm / Hh - 1 / math.e) < 2e-3)
    # ---- friction relations
    def relations(H, D, S=1e-3):
        z0 = D / 30
        us = math.sqrt(G * H * S)
        r = math.log(H / z0)
        Um = us / KAPPA * (r - 1)
        f = 8 * (us / Um) ** 2
        C = math.sqrt(8 * G / f)
        n = H ** (1 / 6) / (C)           # n = R^{1/6}/C with R=H (wide channel)
        n_str = D ** (1 / 6) / 21.1       # Strickler, D in m
        return z0, us, Um, f, C, n, n_str
    print("relative roughness -> friction (wide channel, z0 = D/30):")
    for H_, D_ in ((1.0, 0.027), (1.0, 0.1), (3.0, 0.1), (0.3, 0.1)):
        z0, us, Um, f, C, n, n_str = relations(H_, D_)
        print(f"  H={H_:3.1f} m D={D_*1e3:5.0f} mm H/z0={H_/z0:6.0f}: f={f:.4f}  Chezy C={C:5.1f}  Manning n={n:.4f}  Strickler n={n_str:.4f}  U={Um:.2f} m/s")
    z0, us, Um, f, C, n, n_str = relations(1.0, 0.027)
    ok("Manning n from the log law within 25% of Strickler for H/z0 ~ 1100", abs(n - n_str) / n_str < 0.25)
    # local exponent of U with H at fixed S
    H1 = z0 * math.exp(7)
    e = 0.5 + 1 / (math.log(H1 / z0) - 1)
    print(f"d ln U/d ln H at fixed S = 1/2 + 1/(ln(H/z0)-1) = {e:.4f} at H/z0 = e^7 = {H1/z0:.0f}   (Manning: 2/3)")
    ok("Manning's 2/3 reproduced by the log law at H/z0 = e^7", abs(e - 2 / 3) < 1e-9)
    # ---- Froude and hydraulic jump
    def froude(H, D, S):
        z0 = D / 30
        us = math.sqrt(G * H * S)
        Um = us / KAPPA * (math.log(H / z0) - 1)
        return Um, Um / math.sqrt(G * H)
    Ur, Fr_r = froude(2.0, 0.030, 1e-3)
    Um_, Fr_m = froude(0.5, 0.3, 0.05)
    print(f"lowland river H=2 m S=1e-3 D=30 mm: U={Ur:.2f} m/s Fr={Fr_r:.2f};  mountain step-pool H=0.5 S=0.05 D=0.3 m: U={Um_:.2f} Fr={Fr_m:.2f}")
    for Fr1 in (Fr_m, 2.0, 3.0, 5.0):
        r = (math.sqrt(1 + 8 * Fr1 ** 2) - 1) / 2
        H1_ = 1.0
        H2 = r * H1_
        dE = (H2 - H1_) ** 3 / (4 * H1_ * H2)
        print(f"  jump Fr1={Fr1:.2f}: H2/H1={r:.2f}, energy loss/H1 = {dE:.3f} (= {dE/(H1_+Fr1**2*H1_/2)*100:.0f}% of the upstream head)")
    # momentum conservation check of the sequent-depth formula
    Fr1 = 3.0
    r = (math.sqrt(1 + 8 * Fr1 ** 2) - 1) / 2
    u1 = Fr1 * math.sqrt(G * 1.0); u2 = u1 / r
    M1 = 0.5 * G * 1.0 ** 2 + u1 ** 2 * 1.0
    M2 = 0.5 * G * r ** 2 + u2 ** 2 * r
    ok("sequent depth: momentum flux conserved", abs(M1 - M2) / M1 < 1e-12)
    # backwater
    for nm, H_, S_ in (("lower Mississippi", 15.0, 9.5e-5), ("Amazon", 40.0, 2e-5), ("gravel stream", 1.0, 5e-3)):
        print(f"  backwater length ~ H/S ({nm}: H={H_} m, S={S_:g}) = {H_/S_/1e3:.1f} km")
    # ---- discharge measurement
    M, Qt, sig = 1.0, 1.5, 60.0
    dC_peak = M / (Qt * sig * math.sqrt(2 * math.pi))
    t = np.linspace(-600, 600, 20001)
    dC = dC_peak * np.exp(-t ** 2 / (2 * sig ** 2))
    Qrec = M / np.trapezoid(dC, t)
    print(f"salt dilution: M=1 kg, Q={Qt} m3/s, pulse sigma=60 s: peak rise {dC_peak*1e3:.2f} mg/L (about {dC_peak/0.5*1e3:.1f} uS/cm at 0.5 (g/L)/(mS/cm)); recovered Q = {Qrec:.3f}")
    ok("salt dilution recovers Q", abs(Qrec - Qt) < 1e-3)
    # rating curve and satellite-width method for a braided gravel river
    D50, S = 0.030, 0.005
    taustar = 0.045
    Hb = taustar * (S_REL - 1) * D50 / S
    us = math.sqrt(G * Hb * S)
    Ub = us / KAPPA * (math.log(Hb / (D50 / 30)) - 1)
    print(f"braided gravel river D50=30 mm S=0.005: threshold depth H = tau*_c (s-1) D/S = {Hb:.3f} m, U = {Ub:.2f} m/s, Fr = {Ub/math.sqrt(G*Hb):.2f}, q = {Hb*Ub:.2f} m2/s")
    for Wact in (100, 250, 500):
        print(f"   active width {Wact} m -> Q = {Hb*Ub*Wact:.0f} m3/s")
    # ---- hydraulic geometry
    for nm, (b, f_, m_) in (("downstream (Leopold-Maddock)", (0.5, 0.4, 0.1)), ("at a station", (0.26, 0.40, 0.34))):
        ok(f"{nm}: b+f+m = 1", abs(b + f_ + m_ - 1) < 1e-9)
        print(f"  {nm}: Q x10 -> W x{10**b:.2f}, H x{10**f_:.2f}, U x{10**m_:.2f}")
    print(f"  at-a-station velocity exponent expected from Manning (U ~ H^(2/3), H ~ Q^0.40): m = {0.4*2/3:.2f} (observed 0.34)")
    for r in (1e2, 1e3, 1e4):
        print(f"    log law at H/z0 = {r:.0e}: U ~ H^{0.5+1/(math.log(r)-1):.3f}  ->  m = f x that = {0.4*(0.5+1/(math.log(r)-1)):.3f}")
    # ---- worked example for the chapter: a cobble-bed reach
    D, S, H, W = 0.100, 0.002, 1.8, 60.0
    z0 = D / 30; us = math.sqrt(G * H * S); r = math.log(H / z0)
    U = us / KAPPA * (r - 1); f = 8 * (us / U) ** 2; C = math.sqrt(8 * G / f)
    n = H ** (1 / 6) / C; Q = W * H * U; Fr = U / math.sqrt(G * H)
    tau_b = RHO * G * H * S; tau_c = 0.045 * (RHO_S - RHO) * G * D; Hc = tau_c / (RHO * G * S)
    print(f"worked example (D=100 mm, S=0.002, H=1.8 m, W=60 m): z0={z0*1e3:.2f} mm, H/z0={H/z0:.0f}, u*={us:.4f} m/s, U={U:.3f} m/s, f={f:.4f}, C={C:.2f}, n={n:.4f}, Q={Q:.0f} m3/s, Fr={Fr:.3f}")
    print(f"   tau_b = {tau_b:.1f} Pa, tau_c(0.045) = {tau_c:.1f} Pa -> tau_b/tau_c = {tau_b/tau_c:.2f}; bed moves when H >= {Hc:.2f} m")
    # practice-problem values
    us2 = math.sqrt(G * 1.5 * 2e-3); U2 = us2 / KAPPA * (math.log(1.5 / 1e-3) - 1)
    print(f"practice: H=1.5, S=2e-3, z0=1 mm: u*={us2:.4f}, U={U2:.3f} m/s, q={1.5*U2:.2f} m2/s")
    Um = (1 / 0.035) * 2 ** (2 / 3) * 0.001 ** 0.5
    print(f"practice: Manning n=0.035, R=2 m, S=1e-3: U={Um:.3f} m/s; with A=100 m2: Q={Um*100:.0f} m3/s")
    Fr1 = 3.0 / math.sqrt(G * 0.4); r2 = (math.sqrt(1 + 8 * Fr1 ** 2) - 1) / 2
    print(f"practice: U=3 m/s, H=0.4 m: Fr={Fr1:.3f}, H2={r2*0.4:.3f} m, dE={(r2*0.4-0.4)**3/(4*0.4*r2*0.4):.4f} m")
    Hb2 = 0.045 * 1.65 * 0.05 / 0.01; us3 = math.sqrt(G * Hb2 * 0.01); U3 = us3 / KAPPA * (math.log(Hb2 / (0.05 / 30)) - 1)
    print(f"practice: braided D=50 mm, S=0.01: H={Hb2:.3f} m, u*={us3:.3f}, U={U3:.2f} m/s, Fr={U3/math.sqrt(G*Hb2):.2f}, q={Hb2*U3:.2f}; Q for 400 m of active width = {Hb2*U3*400:.0f} m3/s")
    print(f"  Amazon mean discharge = 6300 km3/yr / 1 yr = {6300e9/YR:.3e} m3/s; runoff depth = {6300/6.15e6*1e3:.2f} m/yr over 6.15e6 km2")


# ============================================================================================================ LS22
def ls22():
    head("LS22  Floods, floodplains, channel planform and river profiles")
    # ---- Gumbel: the mean annual flood has recurrence 2.33 yr
    F_mean = math.exp(-math.exp(-0.5772156649))
    print(f"Gumbel annual maxima: P(Q <= mean) = exp(-exp(-gamma)) = {F_mean:.4f} -> recurrence of the mean annual flood T = {1/(1-F_mean):.3f} yr")
    ok("mean annual flood is the 2.33-yr event", abs(1 / (1 - F_mean) - 2.33) < 0.01)
    for T in (1.5, 2, 2.33, 5, 10, 50, 100):
        y = -math.log(-math.log(1 - 1 / T))
        print(f"   T={T:6.2f} yr: Gumbel reduced variate y={y:6.3f}  Q_T = mu + beta y (in units of mu=1, beta=0.35: {1+0.35*y:.2f})")
    # ---- effective discharge (Wolman-Miller): lognormal daily flows x Q^j
    sig = 1.0
    for j in (1.5, 2.0, 2.5, 3.0):
        x = np.linspace(-6, 10, 160001)               # x = ln(Q/Qmed)
        p = stats.norm.pdf(x, 0, sig)
        integrand = np.exp(j * x) * p
        xe = x[np.argmax(integrand)]
        analytic = j * sig ** 2
        exceed = 1 - stats.norm.cdf(xe / sig)
        print(f"  j={j}: effective discharge Qe/Qmed = {math.exp(xe):6.2f} (analytic exp(j sigma^2) = {math.exp(analytic):6.2f}), exceeded {exceed*100:5.2f}% of days = {exceed*365.25:4.1f} d/yr")
        ok(f"j={j}: peak of Q^j p(Q) at ln(Q/Qmed) = j sigma^2", abs(xe - analytic) < 1e-3)
    # with a threshold (no transport below Qc = 3 Qmed)
    j = 2.5
    xc = math.log(3)
    x = np.linspace(xc, 10, 160001)
    integrand = (np.exp(x) - 3) ** j * stats.norm.pdf(x, 0, sig)
    xe = x[np.argmax(integrand)]
    print(f"  with a threshold Qc = 3 Qmed: Qe/Qmed = {math.exp(xe):.2f} -> exceeded {(1-stats.norm.cdf(xe/sig))*365.25:.1f} d/yr")
    print(f"  share of the long-term load carried by flows above the 99th daily percentile (j=2.5, no threshold): "
          f"{1 - stats.norm.cdf((stats.norm.ppf(0.99) - j * sig) / sig):.3f}")
    print(f"  sediment rating Qs ~ Q^j: doubling Q multiplies the load by 2^j = {2**2:.0f} (j=2) to {2**3:.0f} (j=3)")
    # ---- meander geometry
    U, W, R = 1.5, 100.0, 300.0
    dh = U ** 2 * W / (G * R)
    print(f"super-elevation across a bend: dh = U^2 W/(g R) = {dh*100:.1f} cm for U=1.5 m/s, W=100 m, R=300 m;  wavelength 11 W = {11*W:.0f} m")
    print("sine-generated curve theta = omega sin(2 pi s/lambda): sinuosity = 1/J0(omega)")
    for deg in (30, 60, 70, 90, 110):
        w = math.radians(deg)
        s_num = integrate.quad(lambda s: math.cos(w * math.sin(2 * math.pi * s)), 0, 1)[0]
        print(f"   omega={deg:3d} deg: J0={special.j0(w):.4f}  valley/channel length = {s_num:.4f}  sinuosity = {1/s_num:.3f}")
        ok(f"valley length per channel length = J0({deg} deg)", abs(s_num - special.j0(w)) < 1e-9)
    # ---- long profiles
    L, SL = 100e3, 50.0
    x = 1e3
    print(f"Hack stream-gradient index SL = {SL} m: z(x)-z(L) = SL ln(L/x) -> {SL*math.log(L/x):.0f} m between x=1 km and L=100 km")
    xs = 300e3 / math.log(100)
    print(f"Sternberg fining D = D0 exp(-x/x*): 100 mm -> 1 mm over 300 km gives x* = {xs/1e3:.0f} km;"
          f" with S ~ D, S(x) = S0 exp(-x/x*): relief = S0 x* (1 - e^(-x/x*)) = {1e-3*xs*(1-0.01):.0f} m for S0 = 1e-3")
    # capacity argument: S ~ A^(n-m)
    for n, m in ((1.0, 1.0), (0.8, 1.0), (0.5, 1.0)):
        print(f"  capacity argument  Qs ~ A^{n}, Q ~ A^{m}: S ~ A^{n-m:+.2f}")
    # ---- alluvial baselevel fall: diffusion
    kap, h = 1e5, 20.0
    for t_ in (1e3, 1e4, 1e5):
        d = math.sqrt(kap * t_)
        xr = 2 * d * special.erfcinv(0.1)
        print(f"  baselevel drop h=20 m, kappa=1e5 m2/yr, t={t_:8.0f} yr: sqrt(kappa t)={d/1e3:6.1f} km, drop felt (>10% of h) out to x = {xr/1e3:6.1f} km")
    # numerical check of z = -h erfc(x/(2 sqrt(kappa t))) by an explicit finite-difference scheme
    dx, nx = 500.0, 1200
    xg = np.arange(nx) * dx
    z = np.zeros(nx); z[0] = -h
    dt = 0.2 * dx ** 2 / kap
    tt = 0.0; tend = 2e4
    while tt < tend:
        z[1:-1] += kap * dt / dx ** 2 * (z[2:] - 2 * z[1:-1] + z[:-2])
        z[0] = -h; tt += dt
    zex = -h * special.erfc(xg / (2 * math.sqrt(kap * tt)))
    print(f"  finite-difference vs erfc solution at t={tt:.0f} yr: max |diff| = {np.abs(z-zex).max():.4f} m")
    ok("diffusive baselevel response = erfc", np.abs(z - zex).max() < 0.05)
    # ---- Amazon budget
    inp = {"Amazon at Sao Paulo de Olivenca": 616, "Madeira": 715, "smaller tributaries": 117}
    tot_in = sum(inp.values())
    out = 1239
    print(f"Amazon sediment budget (Mt/yr): inputs {inp} = {tot_in}; output at Obidos = {out}; storage = {tot_in-out} Mt/yr = {(tot_in-out)/tot_in*100:.1f}% of the input")
    ok("Amazon storage 209 Mt/yr", tot_in - out == 209)
    print(f"  1200 Mt/yr at 1700 kg/m3 = {1200e9/1700/1e9:.2f} km3/yr; Mississippi mean slope {95/1000e3:.2e} (95 m over 1000 km); Amazon 2 cm/km = {2e-2/1e3:.1e}")
    print(f"  the Mississippi drops 95 m in 1000 km: a head of {95:.0f} m over {1000:.0f} km; at slope 9.5e-5 and H = 15 m the shear stress rho g H S = {RHO*G*15*9.5e-5:.1f} Pa")


# ============================================================================================================ LS23
def ls23():
    head("LS23  Bedrock channels and river incision")
    # ---- stream power, bond-energy closure
    Q, W, S = 100.0, 10.0, 0.01
    q = Q / W
    omega = RHO * G * q * S
    print(f"unit stream power omega = rho g q S = {omega:.0f} W/m2 for q = {q:.0f} m2/s, S = {S}")
    Wf = 100.0     # J/m2, work of fracture of rock (illustrative)
    d = 0.1        # slab thickness (m)
    E_target = 1e-3 / YR
    alpha = E_target * Wf / (d * omega)
    print(f"E = alpha d omega / W_f: with W_f = {Wf:.0f} J/m2, d = {d} m, the observed E = 1 mm/yr needs alpha = {alpha:.1e} (a tiny efficiency)")
    print(f"  k = alpha d / W_f = {alpha*d/Wf:.1e} m3/J   (A&A: units L T^2/M)")
    # ---- tools and cover (saltation-abrasion): E ~ q_s (1 - q_s/q_c)
    qs = np.linspace(0, 1, 1001)
    E = qs * (1 - qs)
    print(f"tools-and-cover: E(qs) ~ qs (1 - qs/qc) peaks at qs/qc = {qs[np.argmax(E)]:.2f}, E_max = qc/4 (here {E.max():.3f} qc)")
    ok("optimum sediment supply = qc/2", abs(qs[np.argmax(E)] - 0.5) < 1e-3)
    print(f"  E ~ sigma_T^-2: doubling the tensile strength cuts the abrasion rate by x{1/4:.2f}")
    print(f"  kinetic-energy flux  q_ke ~ C m_p U^3: doubling U -> x{2**3}; if C ~ U^2 (wind) -> x{2**5}")
    # ---- dissolution (Palmer)
    Qc, p, L, dC = 0.01, 1.0, 1000.0, 0.05      # m3/s, m, m, kg/m3 CaCO3
    mass = Qc * dC * YR
    retreat = mass / (2700.0 * p * L)
    print(f"cave dissolution: Q={Qc} m3/s removing {dC*1e3:.0f} mg/L over a reach of {L:.0f} m, wetted perimeter {p} m -> {mass/1e3:.1f} t/yr -> wall retreat {retreat*1e3:.1f} mm/yr")
    # ---- knickpoint lowering E = C H / l
    print(f"knickpoint lowering E = C H / l: C=1 m/yr, H=0.2 m, l=20 m -> {1*0.2/20*1e3:.0f} mm/yr")
    # ---- cosmogenic: averaging time and water shielding
    zs, zsw = 0.6, 1.6
    print(f"cosmogenic channel-floor sampling: T = z*/E = {zs/1e-3:.0f} yr at E = 1 mm/yr; z*_rock = Lambda/rho = 160/2.7 = {1.6/2.7:.2f} m, z*_water = {1.6:.1f} m")
    for hw in (1, 3, 5, 10):
        print(f"   {hw:2d} m of water: production reduced to {math.exp(-hw/zsw)*100:6.2f}%")
    # burial dating pair
    tAl = 0.705 / math.log(2); tBe = 1.387 / math.log(2)
    tau = 1 / (1 / tAl - 1 / tBe)
    print(f"26Al/10Be burial dating: tau_Al = {tAl:.3f} Myr, tau_Be = {tBe:.3f} Myr, ratio decays with tau = 1/(1/tau_Al - 1/tau_Be) = {tau:.2f} Myr (A&A: 2.07 Ma)")
    ok("burial-dating characteristic time 2.07 Myr", abs(tau - 2.07) < 0.02)
    print(f"   dating range ~ 2.5 tau = {2.5*tau:.1f} Myr (the ratio is then {6.75*math.exp(-2.5):.2f} of ~6.75)")
    # ---- chi transform, kinematic wave check (n = 1, m = 1/2: theta = 1/2, C = K A^m = 0.05 m/yr at 100 km2, as in LS16)
    m_exp, A0, K = 0.5, 1.0e6, 5e-6
    h_ = 1 / 0.6                          # Hack: L(km) = 1.4 A(km2)^0.6  ->  A(km2) = (L/1.4)^(1/0.6)

    def A_of_x(x):
        return (x / 1e3 / 1.4) ** h_ * 1e6
    Ltot, ds = 40e3, 200.0
    s = np.arange(0, Ltot + ds, ds)
    A = np.maximum(A_of_x(np.maximum(Ltot - s, 1.0)), 5e5)   # channel head at A_c = 0.5 km2; s = distance upstream of the outlet
    U0, U1 = 0.2e-3, 0.8e-3
    v = K * A0 ** m_exp
    chi = np.concatenate([[0.0], np.cumsum(0.5 * ((A0 / A[1:]) ** m_exp + (A0 / A[:-1]) ** m_exp) * ds)])
    z = np.concatenate([[0.0], np.cumsum(0.5 * (U0 / (K * A[1:] ** m_exp) + U0 / (K * A[:-1] ** m_exp)) * ds)])
    t, tend = 0.0, 1.0e6
    dtmax = 0.4 * ds / (K * A.max() ** m_exp)
    while t < tend:
        dt_ = min(dtmax, tend - t)
        z[1:] += dt_ * (U1 - K * A[1:] ** m_exp * np.diff(z) / ds)
        z[0] = 0.0
        t += dt_
    S_num = np.diff(z) / ds
    S_new = U1 / (K * A[1:] ** m_exp); S_old = U0 / (K * A[1:] ** m_exp)
    frac = (S_num - S_old) / (S_new - S_old)
    idx = int(np.argmax(frac < 0.5)) if np.any(frac < 0.5) else len(frac) - 1
    chi_pred, chi_num = v * tend, chi[1:][idx]
    print(f"kinematic wave n=1, m=1/2, step U {U0*1e3:.1f}->{U1*1e3:.1f} mm/yr after {tend:.0e} yr: knickpoint at chi = {chi_num:.0f} m "
          f"(prediction v t = {chi_pred:.0f} m, v = K A0^m = {v*1e3:.1f} mm/yr); in s: {s[1:][idx]/1e3:.1f} km upstream")
    ok("knickpoint travels at constant speed in chi-space", abs(chi_num - chi_pred) / chi_pred < 0.05)
    print(f"  in real space the speed C = K A^m changes by x{(A.max()/A.min())**m_exp:.0f} along the channel while v in chi-space is constant")
    S_ratio = S_new[0] / S_old[0]
    print(f"  new/old steady slope = U1/U0 = {S_ratio:.1f} (n=1: slope proportional to U)")
    # response time vs basin size, general m
    print("response time T = integral dx/(K A^m) from the channel head x_h (A_c = 0.5 km2) to the basin length L:")
    xh = 1.4e3 * 0.5 ** 0.6
    for m_, K_ in ((1.0, 5e-10), (0.5, 5e-6)):
        Ts = {}
        for Lb in (10e3, 30e3, 90e3, 300e3):
            Ts[Lb] = integrate.quad(lambda x: 1.0 / (K_ * A_of_x(x) ** m_), xh, Lb, limit=400)[0]
        txt = "  ".join(f"L={Lb/1e3:.0f} km (A={A_of_x(Lb)/1e6:.0f} km2): {T/1e6:.2f} Myr" for Lb, T in Ts.items())
        print(f"   m = {m_}, K = {K_:g}:  {txt}")
        print(f"      basin area x{A_of_x(300e3)/A_of_x(10e3):.0f} (L 10 -> 300 km): T x{Ts[300e3]/Ts[10e3]:.2f};  exponent of T ~ L^(1-m h) = L^{1-m_*h_:.3f}" if m_ * h_ != 1 else "")
        if m_ == 1.0:
            Tlim = xh / (K_ * 5e5 * (h_ - 1))
            print(f"      limit L -> infinity: T = x_h/(K A_c (h-1)) = {Tlim/1e6:.2f} Myr (x_h = {xh:.0f} m)")
            ok("m = 1: response time nearly independent of basin size (T(30 km) within 10% of the limit, T(300 km) within 3%)",
               abs(Ts[30e3] / Tlim - 1) < 0.10 and abs(Ts[300e3] / Tlim - 1) < 0.03)
        else:
            ex = 1 - m_ * h_
            Tan = (1.4e3) ** (m_ * h_) / (K_ * 1e6 ** m_) * (300e3 ** ex - xh ** ex) / ex
            print(f"      analytic T = (1.4 km)^(mh)/(K A_1^m) [L^(1-mh) - x_h^(1-mh)]/(1-mh) at L=300 km: {Tan/1e6:.3f} Myr")
            ok("m = 1/2: T = const x [L^(1/6) - x_h^(1/6)] (the integral done analytically)", abs(Tan / Ts[300e3] - 1) < 1e-6)
    print(f"   celerity C = K A^m (m=1/2, K=5e-6): A = 0.5 km2 -> {5e-6*5e5**0.5*1e3:.1f} mm/yr; 100 km2 -> {5e-6*1e8**0.5:.3f} m/yr; 1e5 km2 -> {5e-6*1e11**0.5:.1f} m/yr")
    print(f"   (m=1, K=5e-10: 100 km2 -> {5e-10*1e8:.3f} m/yr).  Parachute Creek: 350 ka at 0.050 m/yr -> {350e3*0.05/1e3:.1f} km of retreat in a 100 km2 tributary")
    print(f"   tributary knickpoints after 350 kyr, s_k = K A^m t:  A = 1, 10, 100 km2 -> "
          + ", ".join(f"{5e-10*a*1e6*350e3/1e3:.2f} km" for a in (1, 10, 100)) + " (m=1, K=5e-10)")
    # ---- Niagara
    print(f"Niagara: 1 km/1 ka = 1 m/yr; 1 km/5 ka = 0.2 m/yr: ratio 5 for a discharge ratio 7 -> exponent a in R ~ Q^a: {math.log(5)/math.log(7):.2f}")
    # ---- width
    print(f"Finnegan width law W ~ Q^(3/8) S^(-3/16): unit stream power Q S/W ~ Q^{1-3/8:.3f} S^{1+3/16:.4f} -> m = 5/8, n = 19/16, theta = m/n = {(5/8)/(19/16):.3f}")
    print(f"  for W ~ Q^(1/2): Q S/W ~ Q^(1/2) S -> theta = 1/2;  empirical W ~ Q^0.4 S^-0.2 -> Q^0.6 S^1.2 -> theta = {0.6/1.2:.2f}")
    print(f"  Wobus et al. self-organised cross section: W/H = 2.9 (steady state)")


# ============================================================================================================ LS24
def brownlie(Rep):
    return 0.22 * Rep ** -0.6 + 0.06 * math.exp(-17.77 * Rep ** -0.6)


def settling(D, s=S_REL, nu=NU, C1=18.0, C2=1.0):
    return (s - 1) * G * D ** 2 / (C1 * nu + math.sqrt(0.75 * C2 * (s - 1) * G * D ** 3))


def ls24():
    head("LS24  Sediment transport mechanics")
    print("Shields threshold (Brownlie fit): tau*_c(Rep), Rep = sqrt((s-1) g D^3)/nu")
    for D in (0.1e-3, 0.2e-3, 1e-3, 2e-3, 20e-3, 200e-3):
        Rep = math.sqrt((S_REL - 1) * G * D ** 3) / NU
        ts = brownlie(Rep)
        tauc = ts * (RHO_S - RHO) * G * D
        print(f"   D = {D*1e3:7.1f} mm: Rep = {Rep:9.1f}  tau*_c = {ts:.4f}  tau_c = {tauc:8.2f} Pa  u*_c = {math.sqrt(tauc/RHO)*100:6.2f} cm/s")
    Reps = np.logspace(-0.5, 4, 2000)
    ts = np.array([brownlie(r) for r in Reps])
    imin = int(np.argmin(ts))
    print(f"   minimum of the curve: tau*_c = {ts[imin]:.4f} at Rep = {Reps[imin]:.1f} (grain size ~ {(Reps[imin]*NU)**(2/3)/((S_REL-1)*G)**(1/3)*1e3:.2f} mm); large-grain limit {brownlie(1e4):.3f}")
    Rstar = Reps[imin] * math.sqrt(ts[imin])           # boundary Reynolds number u*_c D / nu  = Rep sqrt(tau*_c)
    print(f"   at the minimum the boundary Reynolds number R* = u*_c D/nu = Rep sqrt(tau*_c) = {Rstar:.1f}")
    ok("Shields curve minimum ~0.03 at boundary Reynolds number R* ~ 10", 0.025 < ts[imin] < 0.04 and 6 < Rstar < 16)
    # wind threshold
    for nm, rho_f, g_ in (("Earth (air)", 1.2, 9.81), ("Mars", 0.020, 3.71)):
        D = 0.2e-3
        ut = 0.1 * math.sqrt((RHO_S - rho_f) / rho_f * g_ * D)
        print(f"   {nm}: Bagnold threshold u*_t = A sqrt((rho_s-rho)/rho g D), A = 0.1, D = 0.2 mm -> {ut:.2f} m/s")
    # settling
    print("settling velocity (Ferguson-Church), Stokes limit check:")
    for D in (0.01e-3, 0.1e-3, 0.5e-3, 1e-3, 5e-3, 20e-3):
        w = settling(D)
        stokes = (S_REL - 1) * G * D ** 2 / (18 * NU)
        Re = w * D / NU
        print(f"   D = {D*1e3:6.3f} mm: w_s = {w*1e3:9.3f} mm/s (Stokes {stokes*1e3:10.3f}) Re_p = {Re:8.2f}")
    ok("Ferguson-Church -> Stokes at D = 10 um", abs(settling(1e-5) / ((S_REL - 1) * G * 1e-10 / (18 * NU)) - 1) < 0.02)
    # Rouse profile
    H, S = 3.0, 1e-3
    us = math.sqrt(G * H * S)
    print(f"Rouse profile: H = {H} m, S = {S}: u* = {us:.3f} m/s")
    a = 0.05 * H
    zs = np.linspace(a, 0.98 * H, 400)
    rows = []
    for D in (0.05e-3, 0.1e-3, 0.25e-3, 1e-3, 5e-3):
        w = settling(D)
        P = w / (KAPPA * us)
        C = ((H - zs) / zs * a / (H - a)) ** P
        c_half = float(np.interp(0.5 * H, zs, C))
        rows.append((D, w, P, c_half))
        print(f"   D={D*1e3:6.2f} mm: w_s={w*1e3:8.2f} mm/s, Rouse number P = w_s/(k u*) = {P:6.2f}, C(0.5H)/C(a) = {c_half:.4f}")
    # numerical check: the Rouse profile solves w C + eps dC/dz = 0 with eps = k u* z (1 - z/H)
    P = 0.8
    zz = np.linspace(a, 0.98 * H, 20001)
    Cn = ((H - zz) / zz * a / (H - a)) ** P
    eps = KAPPA * us * zz * (1 - zz / H)
    resid = np.gradient(Cn, zz) * eps + P * KAPPA * us * Cn
    ok("Rouse profile solves the diffusion-settling balance", np.abs(resid[100:-100]).max() < 5e-3 * (P * KAPPA * us))
    # suspended flux fraction via log law
    P = 0.5
    Cz = lambda z: ((H - z) / z * a / (H - a)) ** P
    Uz = lambda z: us / KAPPA * math.log(z / 1e-3)
    Qs = integrate.quad(lambda z: Cz(z) * Uz(z), a, H)[0]
    Qw = integrate.quad(Uz, 1e-3, H)[0]
    print(f"   suspended flux for P=0.5 (a=0.05H): flux-weighted mean concentration / reference = {Qs/Qw:.3f}")
    # bedload
    H, S, D = 1.0, 0.005, 0.01
    tstar = H * S / ((S_REL - 1) * D)
    qstar = 8 * (tstar - 0.047) ** 1.5
    qb = qstar * math.sqrt((S_REL - 1) * G * D) * D
    print(f"Meyer-Peter and Muller: H=1 m, S=0.005, D=10 mm: tau* = {tstar:.3f}, q*_b = 8 (tau*-0.047)^1.5 = {qstar:.3f}, q_b = {qb*1e3:.2f} L/m/s, mass flux {qb*RHO_S:.1f} kg/m/s")
    for ex in (1.0, 1.5):
        a1 = (2 * tstar - 0.047) ** ex / (tstar - 0.047) ** ex
        print(f"   doubling tau* multiplies the excess-power law by {a1:.2f} (exponent {ex})")
    # entrainment by torque balance (A&A sec. 14.2): theta = (4/3) cot(alpha) kappa^2 / (Cd beta ln^2(zbar/z0))
    kap, Cd, beta, alpha = 0.4, 0.4, 0.87, math.radians(60)
    def theta_c(zbar_over_D, alpha=alpha, z0_over_D=0.1):
        return (4 / 3) / math.tan(alpha) * kap ** 2 / (Cd * beta * math.log(zbar_over_D / z0_over_D) ** 2)
    zb = optimize.brentq(lambda z: theta_c(z) - 0.08, 0.2, 5)
    print(f"torque balance: tau_c = theta (rho_s-rho) g D; with kappa=0.4, alpha=60 deg, beta=0.87, Cd=0.4, z0=0.1 D, theta=0.08 needs the mean exposed velocity at z = {zb:.2f} D")
    for z_ in (0.5, 0.83, 1.0):
        print(f"   mean taken at {z_:.2f} D -> theta = {theta_c(z_):.3f}")
    for a_ in (45, 50, 60, 70):
        print(f"   pocket angle alpha = {a_} deg (z = 0.83 D): theta = {theta_c(zb, alpha=math.radians(a_)):.3f}")
    ok("torque balance gives theta = 0.08 for the quoted parameters", abs(theta_c(zb) - 0.08) < 1e-9)
    print(f"   observed 0.03-0.06 => the model overestimates by x{0.08/0.06:.1f} to x{0.08/0.03:.1f}")
    # dimensional threshold minimum
    Dd = np.logspace(-5, -2.5, 400)
    Rpp = np.sqrt((S_REL - 1) * G * Dd ** 3) / NU
    tauc_d = np.array([brownlie(r) for r in Rpp]) * (RHO_S - RHO) * G * Dd
    print("   dimensional tau_c (Brownlie, non-cohesive) is nearly flat below ~0.3 mm: "
          + ", ".join(f"{d_*1e3:.2f} mm: {np.interp(d_, Dd, tauc_d):.3f} Pa" for d_ in (0.02e-3, 0.05e-3, 0.1e-3, 0.2e-3, 0.5e-3))
          + "  (cohesion/viscous sublayer, absent from the fit, give the A&A trough at ~0.1 mm)")
    # hop-length scaling and flux
    print("saltation flux scaling: q = m N L with N ~ u*, L ~ u*^2 -> q ~ u*^3 (A&A): doubling u* multiplies q by 8")
    # annual transport by a distribution of wind (Kawamura form), threshold ut = 0.2 m/s, lognormal u*, sigma 0.5, median 0.15
    ut, med, sg = 0.20, 0.15, 0.5
    us_ = np.exp(np.linspace(math.log(0.02), math.log(3.0), 40001))
    pdf = stats.norm.pdf(np.log(us_), math.log(med), sg)           # density in ln u*
    flux = np.where(us_ > ut, (us_ - ut) * (us_ + ut) ** 2, 0.0)
    w = flux * pdf
    ue = us_[np.argmax(w)]
    tot = np.trapezoid(w, np.log(us_))
    act = 1 - stats.norm.cdf((math.log(ut) - math.log(med)) / sg)
    cum = np.cumsum(w) / w.sum()
    u90 = us_[np.searchsorted(cum, 0.9)]
    print(f"annual eolian transport with lognormal u* (median {med}, sigma {sg}) and threshold {ut} m/s: active {act*100:.1f}% of the time; "
          f"the load peaks at u* = {ue:.2f} m/s (= {ue/ut:.1f} x threshold, exceeded {(1-stats.norm.cdf((math.log(ue)-math.log(med))/sg))*100:.1f}% of time);"
          f" 90% of the transport happens below u* = {u90:.2f} m/s")
    # saltation
    v0, ang = 1.0, math.radians(40)
    print(f"ballistic hop v0 = 1 m/s at 40 deg: height {v0**2*math.sin(ang)**2/(2*G)*100:.1f} cm, length {v0**2*math.sin(2*ang)/G*100:.1f} cm")
    # eolian flux (Bagnold) and dune migration
    us_w, D = 0.4, 0.25e-3
    qw = 1.8 * math.sqrt(D / 0.25e-3) * (1.2 / G) * us_w ** 3
    yr_eff = qw * YR * 0.10
    print(f"Bagnold flux q = C (rho_a/g) u*^3: u* = 0.4 m/s, D = 0.25 mm -> {qw*1e3:.1f} g/m/s; at 10% active time {yr_eff:.2e} kg/m/yr")
    for h in (2.0, 10.0, 50.0):
        c = yr_eff / (1600.0 * h)
        print(f"   dune of height {h:4.0f} m migrates c = q/(rho_b h) = {c:6.2f} m/yr (dune speed ~ 1/h)")
    print(f"   doubling u*: flux x{2**3}; threshold u*_t = 0.2 m/s -> Owen/Kawamura (u*-u*_t)(u*+u*_t)^2 ratio u*=0.4 vs 0.8: "
          f"{((0.8-0.2)*(0.8+0.2)**2)/((0.4-0.2)*(0.4+0.2)**2):.1f}")


if __name__ == "__main__":
    want = {int(a) for a in sys.argv[1:]} or {21, 22, 23, 24}
    for k, f in ((21, ls21), (22, ls22), (23, ls23), (24, ls24)):
        if k in want:
            f()
    print("\nall checks passed")
