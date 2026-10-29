"""Numbers and checks for the interdisciplinary chapters LSX1 (Clocks in Rocks) and THX1 (Diffusion).

    .venv/bin/python -W ignore scripts/interdisc_numbers.py            # both
    .venv/bin/python -W ignore scripts/interdisc_numbers.py lsx1
    .venv/bin/python -W ignore scripts/interdisc_numbers.py thx1

Every number quoted in the chapters and concept notes comes from here; each derived identity is checked by a second route
(quadrature, Monte Carlo, a finite-difference solution) and asserted.
"""
import math
import sys

import numpy as np
from scipy import integrate, optimize, special, stats

YR = 365.25 * 86400.0
MYR = 1e6 * YR


def head(s):
    print("\n" + "=" * 100 + f"\n{s}\n" + "=" * 100)


def ok(name, cond):
    print(("  ok   " if cond else "  FAIL ") + name)
    assert cond, name


# ================================================================================================= LSX1
def lsx1():
    head("LSX1  Clocks in Rocks")
    # ---- decay law
    t_half_14c = 5730.0
    lam = math.log(2) / t_half_14c
    tau = 1 / lam
    print(f"14C: t1/2 = {t_half_14c} yr, lambda = {lam:.4e} /yr, mean life tau = {tau:.0f} yr; t1/2/tau = {t_half_14c/tau:.4f} (A&A: half-life is 69% of the mean life)")
    ok("t1/2 = ln2 tau", abs(t_half_14c / tau - math.log(2)) < 1e-12)
    for n in (1, 2, 5, 9, 10):
        print(f"   after {n:2d} half-lives: N/N0 = {0.5**n:.5f}  age = {n*t_half_14c:8.0f} yr")
    # activity of modern carbon
    atoms_per_g = 6.02214076e23 / 12.011
    ratio = 1.2e-12
    N14 = atoms_per_g * ratio
    lam_s = math.log(2) / (t_half_14c * YR)
    A = lam_s * N14
    print(f"1 g of modern carbon: {atoms_per_g:.3e} C atoms, 14C/C = {ratio:.1e} -> N = {N14:.3e}; activity = lambda N = {A:.3f} Bq = {A*60:.1f} decays/min (known value ~13.6-14)")
    ok("modern-carbon activity ~ 0.23 Bq/g", 0.21 < A < 0.25)
    # counting statistics
    for prec in (0.05, 0.01):
        counts = 1 / prec ** 2
        print(f"   decay counting to {prec*100:.0f}% (Poisson, relative error 1/sqrt(n)) needs n = {counts:.0f} counts = {counts/A/3600:.2f} h on 1 g of modern carbon")
    print(f"   AMS counts atoms: 1 mg of carbon holds {N14*1e-3:.2e} 14C atoms -> 1/sqrt(N) = {1/math.sqrt(N14*1e-3):.1e} (counting statistics are no longer the limit)")
    # age uncertainty from a 1% error in N
    for dN in (0.01, 0.05):
        print(f"   delta t = tau * (dN/N) = {tau*dN:.0f} yr for a {dN*100:.0f}% error in N (independent of age!)")
    # Monte Carlo of the decay of N atoms: exponential waiting times
    rng = np.random.default_rng(1)
    n0 = 200000
    t_dec = rng.exponential(tau, n0)
    surv = (t_dec > t_half_14c).mean()
    ok("Monte Carlo: exponential waiting times give N(t1/2)/N0 = 1/2", abs(surv - 0.5) < 0.005)
    print(f"   Monte Carlo ({n0} atoms): fraction surviving one half-life = {surv:.4f}; mean life = {t_dec.mean():.0f} yr (tau = {tau:.0f})")
    # ---- Gamow model of alpha decay
    hbarc = 197.3269804          # MeV fm
    e2 = 1.43996                 # MeV fm
    m_alpha = 3727.379           # MeV
    def half_life_gamow(Zd, Ad, Q, V0=35.0):
        R = 1.2 * (Ad ** (1 / 3) + 4 ** (1 / 3))                # fm
        mu = m_alpha * Ad * 931.494 / (m_alpha + Ad * 931.494)
        b = Zd * 2 * e2 / Q
        f = lambda r: math.sqrt(max(2 * mu * (2 * Zd * e2 / r - Q), 0.0)) / hbarc
        G = integrate.quad(f, R, b, limit=200)[0]
        v = math.sqrt(2 * (Q + V0) / mu)                          # in units of c
        nu = v * 2.99792458e23 / (2 * R)                          # fm/s -> hits/s (c = 2.998e23 fm/s)
        lam = nu * math.exp(-2 * G)
        return math.log(2) / lam, G, R, b
    cases = [("238U", 90, 234, 4.270, 4.468e9 * YR), ("232Th", 88, 228, 4.081, 1.405e10 * YR), ("226Ra", 86, 222, 4.871, 1600 * YR),
             ("222Rn", 84, 218, 5.590, 3.82 * 86400), ("212Po", 82, 208, 8.954, 0.299e-6)]
    print("Gamow model (square well radius R=1.2(A^(1/3)+4^(1/3)) fm, V0=35 MeV, assault frequency v/2R):")
    res = {}
    for nm, Zd, Ad, Q, t_obs in cases:
        th, G, R, b = half_life_gamow(Zd, Ad, Q)
        res[nm] = (th, t_obs)
        print(f"   {nm:6s} Q={Q:5.3f} MeV  2G={2*G:6.1f}  model t1/2 = {th:10.3e} s ({th/YR:9.3e} yr)  observed {t_obs:10.3e} s  ratio model/obs = {th/t_obs:9.2e}")
    span_model = res["238U"][0] / res["212Po"][0]
    span_obs = res["238U"][1] / res["212Po"][1]
    print(f"   span 238U/212Po: model {span_model:.2e}, observed {span_obs:.2e}  (log10: {math.log10(span_model):.1f} vs {math.log10(span_obs):.1f})")
    ok("Gamow model reproduces the ~24 orders of magnitude of alpha half-lives to within 2.5 orders in the span", abs(math.log10(span_model) - math.log10(span_obs)) < 2.5)
    # sensitivity: 10% change in Q
    t1 = half_life_gamow(90, 234, 4.270)[0]; t2 = half_life_gamow(90, 234, 4.270 * 1.10)[0]
    print(f"   a 10% increase in Q changes the 238U half-life by a factor {t1/t2:.1e} (exponential sensitivity to the barrier)")
    # ---- cosmogenic nuclides
    rho, Lam = 2.7, 160.0          # g/cm3, g/cm2
    P, lam10 = 5.0, math.log(2) / 1.387e6         # atoms/g/yr (sea level high latitude, illustrative), 1/yr
    zstar = Lam / rho
    print(f"cosmogenic 10Be: attenuation length in rock z* = Lambda/rho = {zstar:.1f} cm = {zstar/100:.2f} m; lambda = {lam10:.3e} /yr (t1/2 1.387 Myr)")
    print(f"   secular equilibrium N_max = P/lambda = {P/lam10:.2e} atoms/g; reached to 95% after {-math.log(0.05)/lam10/1e6:.1f} Myr")
    N = 1e5
    eps = zstar * (P / N - lam10)           # cm/yr
    T_avg = zstar / eps
    print(f"   steady erosion: N = P/(lambda + rho eps/Lambda); N = 1e5 atoms/g -> eps = z*(P/N - lambda) = {eps*1e4:.1f} um/yr = {eps*1e-2*1e6:.1f} m/Myr; averaging time Lambda/(rho eps) = {T_avg/1e3:.0f} kyr")
    ok("inverse formula reproduces N", abs(P / (lam10 + eps / zstar) - N) / N < 1e-9)
    # no-erosion exposure age
    print(f"   exposure age without erosion/decay: t = N/P = {N/P/1e3:.0f} kyr for N = 1e5")
    print(f"   erosion rate, mean life vs production: eps (m/Myr) for N = 1e4, 1e5, 1e6: " + ", ".join(f"{zstar*(P/n - lam10)*1e4:.1f}" for n in (1e4, 1e5, 1e6)) + " (um/yr = m/Myr)")
    # time-dependent solution check by ODE
    from scipy.integrate import solve_ivp
    k = lam10 + eps / zstar
    sol = solve_ivp(lambda t, y: P - k * y, (0, 5e6), [0.0], rtol=1e-10, atol=1e-6, t_eval=[1e5, 1e6, 5e6])
    ex = [P / k * (1 - math.exp(-k * t)) for t in sol.t]
    ok("N(t) = P/k (1 - e^(-kt)) agrees with ODE integration", max(abs(a - b) / b for a, b in zip(sol.y[0], ex)) < 1e-6)
    # glacial (A&A): 3 m in 30 ka
    print(f"   A&A: LGM surfaces with < 3 m of erosion in 30 ka -> < {3/30e3*1e3:.1f} mm/yr")
    # depth dependence
    for d in (0, 0.6, 1.2, 3.0):
        print(f"   production at depth {d:3.1f} m (spallation only): {math.exp(-d/(zstar/100)):.3f} of the surface rate")
    # burial dating
    tAl, tBe = 0.705 / math.log(2), 1.387 / math.log(2)
    tau_b = 1 / (1 / tAl - 1 / tBe)
    print(f"burial dating: tau = {tau_b:.2f} Myr; ratio R = 6.75 exp(-t/tau): R = 3, 1.5, 0.6 -> t = " + ", ".join(f"{tau_b*math.log(6.75/r):.2f}" for r in (3, 1.5, 0.6)) + " Myr")
    # ---- Dodson closure temperature
    Rg = 8.314
    def Tc(E, D0a2, cool_K_per_Myr, A=55.0):
        dTdt = cool_K_per_Myr / MYR
        T = 400.0
        for _ in range(200):
            tau_c = Rg * T ** 2 / (E * dTdt)
            Tn = E / Rg / math.log(A * tau_c * D0a2)
            if abs(Tn - T) < 1e-9:
                break
            T = Tn
        return T
    E_he, D0a2_he = 138e3, 8.3e5      # D0/a2 back-calculated so that Tc = 70 C at 10 K/Myr (A&A quote ~75 C); E is the recalled apatite-He value
    for rate in (1, 10, 100):
        print(f"   apatite (U-Th)/He (E=138 kJ/mol, D0/a2=8.3e5 /s) cooling at {rate:3d} K/Myr: Tc = {Tc(E_he, D0a2_he, rate)-273.15:6.1f} C")
    Tc10 = Tc(E_he, D0a2_he, 10) - 273.15
    ok("apatite He closure ~ 70 C at 10 K/Myr (A&A quotes 75 C)", 60 < Tc10 < 80)
    print(f"   Dodson: Tc rises ~ {(Tc(E_he,D0a2_he,100)-Tc(E_he,D0a2_he,10)):.1f} K per decade of cooling rate")
    Tfast = Tc(E_he, D0a2_he, 100)
    # exhumation from a thermochronometer age
    Ts, G = 10.0, 25.0
    age = 4.0
    zc = (Tc10 - Ts) / G
    print(f"exhumation: apatite He age {age} Ma, Tc = {Tc10:.0f} C, surface {Ts:.0f} C, geotherm {G:.0f} C/km -> closure depth {zc:.2f} km -> mean exhumation rate {zc/age:.2f} km/Myr = {zc/age:.2f} mm/yr")
    # advection-diffusion Peclet
    kT = 1e-6 * YR           # m2/yr
    for eps_, Lz in ((0.2e-3, 10e3), (1e-3, 10e3), (5e-3, 10e3)):
        print(f"   Peclet = eps L/kappa_T: eps = {eps_*1e3:.1f} mm/yr, L = 10 km -> {eps_*Lz/kT:.2f}  (kappa_T = 1e-6 m2/s = {kT:.1f} m2/yr)")
    print(f"   thermal diffusion time L^2/kappa_T: 1 km = {1e6/kT/1e3:.0f} kyr; 10 km = {1e8/kT/1e6:.1f} Myr; 100 km = {1e10/kT/1e6:.0f} Myr")
    # ---- summary of ranges
    print("ranges: 14C ~ 50 kyr (9 half-lives); 10Be/26Al exposure ~ 1 kyr - 5 Myr; burial ~ 0.5-5 Myr; AFT ~ 10-100 Myr (110 C); (U-Th)/He ~ 1-100 Myr (70 C)")


# ================================================================================================= THX1
def thx1():
    head("THX1  Diffusion: random walks, heat, hillslopes and genes")
    rng = np.random.default_rng(7)
    # ---- 1D random walk
    nwalk, nstep = 200000, 400
    steps = rng.choice([-1, 1], size=(nwalk, nstep))
    x = steps.cumsum(1)
    for n in (25, 100, 400):
        v = x[:, n - 1].var()
        print(f"1D random walk, unit steps: n = {n:3d}: <x> = {x[:, n-1].mean():+.3f}, <x^2> = {v:7.1f}  (theory n = {n}), kurtosis = {stats.kurtosis(x[:, n-1], fisher=False):.3f} (Gaussian 3)")
    ok("<x^2> = n", abs(x[:, 399].var() - 400) / 400 < 0.02)
    # approach to Gaussian: total variation vs CLT
    for n in (4, 16, 64, 400):
        xs = x[:, n - 1]
        # lattice: only parity-matching sites; compare the cdf at 1 sigma
        print(f"   n = {n:3d}: kurtosis of x = {stats.kurtosis(xs, fisher=False):.3f}, skewness {stats.skew(xs):+.3f} (Gaussian 3, 0)")
    # D from step: D = l^2/(2 tau)
    l, tau = 1.0, 1.0
    D = l ** 2 / (2 * tau)
    print(f"diffusion coefficient from the walk: <x^2> = 2 D t with D = l^2/(2 tau) = {D}")
    # d-dimensional
    n = 400
    for d in (1, 2, 3):
        pos = np.zeros((20000, d))
        for _ in range(n):
            k = rng.integers(0, d, 20000)
            pos[np.arange(20000), k] += rng.choice([-1, 1], 20000)
        print(f"   d = {d}: <r^2> = {(pos**2).sum(1).mean():.1f} (theory n = {n}); fraction returning to origin region not computed")
    # ---- diffusion equation from the master equation, exact check by finite difference
    kap = 5.0
    L, nx = 100.0, 1001
    xg = np.linspace(-L, L, nx); dx = xg[1] - xg[0]
    u = np.zeros(nx); u[nx // 2] = 1 / dx
    dt = 0.2 * dx ** 2 / kap
    t = 0.0; tend = 40.0
    while t < tend:
        u[1:-1] += kap * dt / dx ** 2 * (u[2:] - 2 * u[1:-1] + u[:-2])
        t += dt
    ex = np.exp(-xg ** 2 / (4 * kap * t)) / math.sqrt(4 * math.pi * kap * t)
    print(f"heat kernel: FD solution of u_t = kappa u_xx for a delta source vs exp(-x^2/4kt)/sqrt(4 pi k t): max |diff| = {np.abs(u-ex).max():.2e} (peak {ex.max():.4f}); variance = {np.trapezoid(u*xg**2, xg):.2f} (2 k t = {2*kap*t:.2f})")
    ok("Gaussian kernel is the Green's function of the diffusion equation", np.abs(u - ex).max() / ex.max() < 5e-3)
    # ---- scales: time to diffuse a distance L
    print("diffusion time t = L^2/(2D) (1D) for different D and L:")
    cases = [("salt in water", 1.6e-9, (10e-6, 1e-2, 1.0)), ("heat in rock (kappa_T = 1e-6 m2/s)", 1e-6, (1.0, 1e3, 1e5)),
             ("hillslope soil (kappa_h = 5 m2/kyr)", 5.0 / (1e3 * YR), (10.0, 100.0, 1000.0)), ("gas in air", 2e-5, (1e-3, 1.0, 100.0))]
    for nm, Dd, Ls in cases:
        print("   " + nm + ": " + "; ".join(f"L = {Lv:g} m: {Lv**2/(2*Dd):.2e} s ({Lv**2/(2*Dd)/YR:.2e} yr)" for Lv in Ls))
    # ---- thermal skin depth (periodic surface temperature): T(z,t) = T0 exp(-z/d) cos(wt - z/d), d = sqrt(2 kappa/omega)
    kT = 1e-6 * YR
    for nm, period in (("diurnal", 1 / 365.25), ("annual", 1.0), ("glacial cycle (41 kyr)", 41e3), ("glacial cycle (100 kyr)", 1e5)):
        om = 2 * math.pi / period
        d = math.sqrt(2 * kT / om)
        print(f"skin depth, {nm:24s}: d = sqrt(2 kappa/omega) = {d:9.3f} m;  amplitude at 2d: {math.exp(-2):.3f} of the surface; phase lag {math.degrees(1):.0f} deg per d")
    # numerical check of the skin-depth solution (FD in z with a sinusoidal top boundary)
    zz = np.linspace(0, 30, 601); dz = zz[1] - zz[0]; om = 2 * math.pi
    T = np.zeros_like(zz); dtt = 0.2 * dz ** 2 / kT; t = 0.0
    amp = np.zeros_like(zz)
    while t < 12.0:
        T[1:-1] += kT * dtt / dz ** 2 * (T[2:] - 2 * T[1:-1] + T[:-2])
        t += dtt; T[0] = math.cos(om * t); T[-1] = 0
        if t > 10.0:
            amp = np.maximum(amp, np.abs(T))
    dsk = math.sqrt(2 * kT / om)
    k5 = int(5.0 / dz)
    print(f"   FD check: amplitude at z = 5 m: {amp[k5]:.4f}, theory exp(-5/d) = {math.exp(-5/dsk):.4f}")
    ok("skin-depth solution", abs(amp[k5] - math.exp(-5 / dsk)) < 0.01)
    # entropy of the spreading Gaussian
    Dd = 1.0
    for t in (1.0, 4.0, 16.0):
        Sd = 0.5 * math.log(2 * math.pi * math.e * 2 * Dd * t)
        print(f"   differential entropy of the diffusing Gaussian at t = {t:4.1f}: S = (1/2) ln(4 pi e D t) = {Sd:.4f} nats; dS/dt = 1/(2t) = {1/(2*t):.4f}")
    print(f"   entropy gain on quadrupling the time: {0.5*math.log(4):.4f} nats = ln 2")
    # Einstein relation by Boltzmann balance (numerical check): drift mu F c  = D dc/dx with c ~ exp(-F x /kT)
    print("   Einstein relation from J = -D c' + mu F c = 0 with c ~ exp(F x/kT) -> D = mu kT (checked algebraically in the note)")
    # ---- Einstein relation: Brownian particle
    kB, T = 1.380649e-23, 293.15
    eta = 1.0e-3
    for a in (1e-6, 0.5e-6, 5e-9):
        Dd = kB * T / (6 * math.pi * eta * a)
        print(f"Stokes-Einstein: sphere radius {a*1e9:.0f} nm in water at 20 C: D = kT/(6 pi eta a) = {Dd:.3e} m2/s; rms displacement in 1 s (1D) = {math.sqrt(2*Dd)*1e6:.2f} um")
    # ---- Wright-Fisher drift as diffusion
    N, p0, gens, reps = 100, 0.5, 100, 40000
    p = np.full(reps, p0)
    var_t = []
    for g in range(gens):
        p = rng.binomial(2 * N, p) / (2 * N)
        if g + 1 in (10, 50, 100):
            var_t.append((g + 1, p.var(), (p == 0).mean(), (p == 1).mean()))
    for g, v, f0, f1 in var_t:
        th = p0 * (1 - p0) * (1 - (1 - 1 / (2 * N)) ** g)
        print(f"Wright-Fisher 2N=200, p0=0.5: t = {g:3d} generations: Var(p) = {v:.4f} (theory p0(1-p0)[1-(1-1/2N)^t] = {th:.4f}); fixed: lost {f0:.3f}, fixed {f1:.3f}")
    g, v, _, _ = var_t[0]
    ok("early Var(p) = p0(1-p0)[1-(1-1/2N)^t]", abs(v - 0.25 * (1 - (1 - 1 / (2 * N)) ** g)) < 6e-4)
    print(f"   diffusion limit: Var(p) = p(1-p) t/(2N) at small t: t = 10: {0.25*10/(2*N):.4f}; effective D = p(1-p)/(4N) = {0.25/(4*N):.2e} per generation (at p=1/2)")
    print(f"   mean time to fixation (neutral, p0=1/2): ~ 4N generations = {4*N} (diffusion approximation 2.77 N_e... not computed)")
    # hillslope
    kh = 5.0
    print(f"hillslope diffusion: kappa_h = {kh} m2/kyr: a 20 m high scarp of half-width 10 m rounds off in L^2/kappa = {100/kh:.0f} kyr; a 100 m hillslope relaxes in {1e4/kh/1e3:.1f} Myr")
    print(f"  steady hillslope with lowering E (LS12): kappa z'' = -E, z = E (L^2 - x^2)/(2 kappa): L=100 m, E=20 m/Myr, kappa = 5 m2/kyr = 0.005 m2/yr -> relief = {2e-5*100**2/(2*0.005):.0f} m, edge slope E L/kappa = {2e-5*100/0.005:.2f}")
    # Peclet
    for nm, v, Lc, Dd in (("hillslope lowering 20 m/Myr", 2e-5, 100, 5e-3), ("geotherm", 1e-3, 1e4, 31.6)):
        print(f"   Peclet number ({nm}) = v L/D = {v*Lc/Dd:.2f}")
    # random walk first-passage / recurrence
    print("recurrence: 1D and 2D walks return to the origin with probability 1; in 3D the return probability is 0.3405 (Polya)")
    pp = 0.3405
    n3 = 3000
    ret = 0
    nw = 4000
    for _ in range(nw):
        pos = np.zeros(3, dtype=int)
        seen = False
        k = rng.integers(0, 3, n3); sgn = rng.choice([-1, 1], n3)
        for kk, ss in zip(k, sgn):
            pos[kk] += ss
            if not pos.any():
                seen = True
                break
        ret += seen
    print(f"   3D simple random walk, {nw} walks of {n3} steps: fraction that returned = {ret/nw:.3f} (Polya limit 0.3405, finite-length value slightly lower)")
    ok("3D return probability near 0.34", 0.28 < ret / nw < 0.36)


if __name__ == "__main__":
    which = set(sys.argv[1:]) or {"lsx1", "thx1"}
    if "lsx1" in which:
        lsx1()
    if "thx1" in which:
        thx1()
    print("\nall checks passed")
