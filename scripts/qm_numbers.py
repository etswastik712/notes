"""QM (PH2113) - numbers quoted in chapters QM01-QM05, all recomputed.

    .venv/bin/python -W ignore scripts/qm_numbers.py
"""
import numpy as np
import sympy as sp
from scipy.integrate import quad
from scipy.optimize import minimize_scalar

hb = 1.054571817e-34; h = 6.62607015e-34; me = 9.1093837015e-31; e = 1.602176634e-19
c = 2.99792458e8; eps0 = 8.8541878128e-12; eV = e
k_e = 1 / (4 * np.pi * eps0)
np.set_printoptions(precision=5, suppress=True)
P = print


def sec(t): P("\n=====", t)


sec("QM01 Gaussian packet: Dx, Dk, Dx*Dp")
sig = 1.7
psi = lambda x: (2 * np.pi * sig ** 2) ** -0.25 * np.exp(-x ** 2 / (4 * sig ** 2))
norm = quad(lambda x: psi(x) ** 2, -np.inf, np.inf)[0]
x2 = quad(lambda x: x ** 2 * psi(x) ** 2, -np.inf, np.inf)[0]
# momentum-space amplitude by numerical Fourier transform
ks = np.linspace(-6, 6, 2401)
phi = np.array([quad(lambda x: psi(x) * np.cos(k * x), -40, 40)[0] for k in ks]) / np.sqrt(2 * np.pi)
dk = ks[1] - ks[0]
pk = phi ** 2; pk /= pk.sum() * dk
k2 = (ks ** 2 * pk).sum() * dk
P(f"norm={norm:.6f}  <x^2>={x2:.5f} (sigma^2={sig ** 2:.5f})  <k^2>={k2:.6f}  1/(4 sigma^2)={1 / (4 * sig ** 2):.6f}  Dx*Dk={np.sqrt(x2 * k2):.5f}")
P("analytic transform: phi(k) = (2 sigma^2/pi)^(1/4) exp(-sigma^2 k^2); check at k=0.3:", round((2 * sig ** 2 / np.pi) ** 0.25 * np.exp(-sig ** 2 * 0.09), 6), "numeric", round(phi[np.argmin(abs(ks - 0.3))], 6))

sec("QM01 band-limited packet sin(Kx)/(pi x): first zero and product")
for K in (1.0, 2.0, 4.0):
    P(f"  K={K}: height K/pi={K / np.pi:.4f}; first zero pi/K={np.pi / K:.4f}; Dx*Dk ~ pi (first-zero width x band half-width)")

sec("QM01 hydrogen estimate")
a0 = 4 * np.pi * eps0 * hb ** 2 / (me * e ** 2)
E0 = -hb ** 2 / (2 * me * a0 ** 2)
P(f"a0={a0:.5e} m = {a0 * 1e10:.4f} A ; E_min={E0:.4e} J = {E0 / eV:.3f} eV")
Ef = lambda r, f: f * hb ** 2 / (2 * me * r ** 2) - k_e * e ** 2 / r
for f, nm in ((1, "Dp=hbar/r"), (0.25, "Dp=hbar/(2r)")):
    res = minimize_scalar(lambda r: Ef(r, f), bounds=(1e-12, 1e-9), method="bounded", options=dict(xatol=1e-16))
    P(f"  {nm}: r_min={res.x:.4e} m = {res.x / a0:.3f} a0 ; E={res.fun / eV:.2f} eV")
P("  a0 from scratch:", hb ** 2 / (me * k_e * e ** 2))
P(f"  tennis ball 57 g, dx=1 mm: dv >= {hb / (2 * 0.057 * 1e-3):.2e} m/s ;  electron dx=a0: dv >= {hb / (2 * me * a0):.3e} m/s")

sec("QM01 Compton and de Broglie")
lamC = h / (me * c); redC = hb / (me * c)
P(f"Compton wavelength h/mc={lamC * 1e12:.4f} pm ; reduced hbar/mc={redC:.4e} m ({redC * 1e12:.4f} pm)")
for th in (0, 60, 90, 120, 180):
    P(f"  theta={th:3d} deg: shift = {lamC * (1 - np.cos(np.radians(th))) * 1e12:.4f} pm")
P("  Compton shift for lambda=71.1 pm (Mo K-alpha) at 90 deg: new lambda =", round(71.1 + lamC * 1e12, 3), "pm  (fractional change", round(lamC * 1e12 / 71.1 * 100, 2), "%)")
for V in (54.0, 100.0, 150.0):
    lam = h / np.sqrt(2 * me * e * V); P(f"  electron accelerated through {V} V: lambda = {lam * 1e9:.4f} nm")
P("  mc^2 =", round(me * c ** 2 / eV / 1e3, 2), "keV")
P("  single slit: first minimum sin(theta)=lambda/a ; dx*dp ~ h =", h)

sec("QM01 phase vs group velocity")
P("omega=hbar k^2/2m: v_phase = hbar k/2m = v/2 ; v_group = hbar k/m = v ; for v=1e6 m/s electron: p =", me * 1e6, " lambda=", h / (me * 1e6))

sec("QM01 Gaussian packet spreading (extra)")
# sigma(t)^2 = sigma0^2 (1 + (hbar t/(2 m sigma0^2))^2)
s0 = 1e-10
t_s = 2 * me * s0 ** 2 / hb
P(f"electron, sigma0=1 A: spreading time 2 m s0^2/hbar = {t_s:.3e} s ; after t=1 ns width ratio = {np.sqrt(1 + (1e-9 / t_s) ** 2):.1f}")
P(f"tennis ball 57 g, sigma0=1 mm: 2 m s0^2/hbar = {2 * 0.057 * 1e-6 / hb:.2e} s")

sec("QM02 ring: benzene-size and cm-size")
L = 0.83e-9
E1 = 2 * np.pi ** 2 * hb ** 2 / (me * L ** 2)
P(f"L={L}: p1={h / L:.3e} kg m/s ; v1={h / L / me:.3e} m/s ; E1={E1:.3e} J = {E1 / eV:.3f} eV ; E2={4 * E1 / eV:.3f} eV ; gap E2-E1 = {3 * E1 / eV:.3f} eV ; E(n) = n^2 * {E1 / eV:.3f}")
Lc = 1e-2
E1c = 2 * np.pi ** 2 * hb ** 2 / (me * Lc ** 2)
P(f"L=1 cm: E1={E1c:.3e} J = {E1c / eV:.3e} eV; kT(300K)={1.380649e-23 * 300 / eV:.4f} eV ; ratio gap/kT ~ {3 * E1c / (1.380649e-23 * 300):.2e}")
P("  de Broglie wavelength of the n=1 state = L ; electron with E=2.18 eV has lambda =", round(h / np.sqrt(2 * me * 2.18 * eV) * 1e9, 3), "nm")

sec("QM02 admissibility examples (Lecture 8): integral of |psi|^2")
cases = {
    "Gaussian exp(-a x^2)": lambda x: np.exp(-2 * x ** 2),
    "exp(-a|x|)": lambda x: np.exp(-2 * abs(x)),
    "A/(1+|x|)^(1/2) -> |psi|^2 = 1/(1+|x|)": lambda x: 1 / (1 + abs(x)),
    "A/(1+|x|) -> |psi|^2 = 1/(1+|x|)^2": lambda x: 1 / (1 + abs(x)) ** 2,
}
for nm, f in cases.items():
    for Rr in (1e2, 1e4, 1e6):
        pass
    vals = [2 * quad(f, 0, Rr, limit=400)[0] for Rr in (1e2, 1e4, 1e6)]
    P(f"  {nm}: integral to |x|<R for R=1e2,1e4,1e6: {np.round(vals, 4)}")
P("  tutorial P1(b): psi = A/(1+x^2)^(1/4): |psi|^2 = 1/sqrt(1+x^2) ~ 1/|x| -> diverges (log)")
vals = [2 * quad(lambda x: 1 / np.sqrt(1 + x ** 2), 0, Rr, limit=400)[0] for Rr in (1e2, 1e4, 1e6)]
P("   ", np.round(vals, 3), "(grows like 2 ln R)")
P("  tutorial P1(g): ring, psi=exp(i phi/2): psi(phi+2 pi) = -psi(phi): not single-valued -> not allowed")

sec("QM02 delta potential: cusp from matching condition")
P("  psi = sqrt(kappa) exp(-kappa|x|) has psi'(0+)-psi'(0-) = -2 kappa^(3/2) ; condition = 2 m lambda/hbar^2 * psi(0) -> kappa = -m lambda/hbar^2 (needs lambda<0): E = -hbar^2 kappa^2/2m")
lam_d = -1.0; m_ = 1.0; hb_ = 1.0
kap = -m_ * lam_d / hb_ ** 2
P(f"  natural units (hbar=m=1, lambda=-1): kappa={kap}, E={-hb_ ** 2 * kap ** 2 / (2 * m_)}")

sec("QM03 two-level system: X,Y,Z")
X = sp.Matrix([[0, 1], [1, 0]]); Y = sp.Matrix([[0, -sp.I], [sp.I, 0]]); Z = sp.Matrix([[1, 0], [0, -1]])
P("[X,Y]=2iZ:", (X * Y - Y * X) == 2 * sp.I * Z, " [Y,Z]=2iX:", (Y * Z - Z * Y) == 2 * sp.I * X, " [Z,X]=2iY:", (Z * X - X * Z) == 2 * sp.I * Y)
xp = sp.Matrix([1, 1]) / sp.sqrt(2); yp = sp.Matrix([1, sp.I]) / sp.sqrt(2); ym = sp.Matrix([1, -sp.I]) / sp.sqrt(2)
c1 = (yp.H * xp)[0]; c2 = (ym.H * xp)[0]
P("|+x> in the Y basis: coefficients", sp.simplify(c1), sp.simplify(c2), "-> |c|^2:", sp.simplify(abs(c1) ** 2), sp.simplify(abs(c2) ** 2))
P("X|+y> =", sp.simplify(X * yp), " = i|-y>?", sp.simplify(X * yp - sp.I * ym) == sp.zeros(2, 1), "; X|-y> = -i|+y>?", sp.simplify(X * ym + sp.I * yp) == sp.zeros(2, 1))
zp = sp.Matrix([1, 0])
ex = lambda A, v: sp.simplify((v.H * A * v)[0])
P("|+z>: <X>,<Y>,<Z> =", ex(X, zp), ex(Y, zp), ex(Z, zp), "; DX,DY =", sp.sqrt(ex(X * X, zp) - ex(X, zp) ** 2), sp.sqrt(ex(Y * Y, zp) - ex(Y, zp) ** 2), "; (1/2)|<[X,Y]>| =", sp.Rational(1, 2) * abs(ex(X * Y - Y * X, zp)))
v = sp.Matrix([sp.sqrt(3) / 2, sp.Rational(1, 2)])
P("psi=(sqrt3/2, 1/2): <Z>=", ex(Z, v), " DZ=", sp.simplify(sp.sqrt(1 - ex(Z, v) ** 2)), " <X>=", ex(X, v), " DX=", sp.simplify(sp.sqrt(1 - ex(X, v) ** 2)), " DZ*DX=", sp.simplify(sp.sqrt(1 - ex(Z, v) ** 2) * sp.sqrt(1 - ex(X, v) ** 2)), " (1/2)|<[Z,X]>| =", sp.simplify(sp.Rational(1, 2) * abs(ex(2 * sp.I * Y, v))))

sec("QM03 ring superposition a psi_n + b psi_-n: Dp = 2|a||b||p_n|")
for P_a in (0, 0.25, 0.5, 0.75, 1):
    P(f"  |a|^2={P_a}: <p>/p_n = {2 * P_a - 1:+.2f}, Dp/p_n = {2 * np.sqrt(P_a * (1 - P_a)):.4f}")

sec("QM03/QM04 box: moments, Dx*Dp, numbers")
n = sp.symbols("n", positive=True, integer=True); x, Lb = sp.symbols("x L", positive=True)
phi_n = sp.sqrt(2 / Lb) * sp.sin(n * sp.pi * x / Lb)
mx = sp.simplify(sp.integrate(x * phi_n ** 2, (x, 0, Lb)))
mx2 = sp.simplify(sp.integrate(x ** 2 * phi_n ** 2, (x, 0, Lb)))
P("<x> =", sp.simplify(mx.subs(n, 1)), sp.simplify(mx.subs(n, 2)), " <x^2> n=1,2,3:", [sp.simplify(mx2.subs(n, k)) for k in (1, 2, 3)])
P("general <x^2>/L^2 = 1/3 - 1/(2 n^2 pi^2):", [float(sp.simplify(mx2.subs({n: k, Lb: 1}))) for k in (1, 2, 3)], [round(1 / 3 - 1 / (2 * k ** 2 * np.pi ** 2), 6) for k in (1, 2, 3)])
for k in (1, 2, 3, 5, 10):
    dx = np.sqrt(1 / 12 - 1 / (2 * k ** 2 * np.pi ** 2)); dp = k * np.pi
    P(f"  n={k}: Dx/L={dx:.5f}  Dp*L/hbar={dp:.4f}  Dx*Dp/hbar={dx * dp:.5f}  (> 0.5: {dx * dp > 0.5})")
P("  <p^2> = (n pi hbar/L)^2 ; <p> =", sp.simplify(sp.integrate(phi_n * (-sp.I) * sp.diff(phi_n, x), (x, 0, Lb))))
Lq = 1e-9
E1b = np.pi ** 2 * hb ** 2 / (2 * me * Lq ** 2)
dxq = Lq * np.sqrt(1 / 12 - 1 / (2 * np.pi ** 2)); dpq = np.pi * hb / Lq
P(f"electron, L=1 nm: E1={E1b:.3e} J = {E1b / eV:.4f} eV; E2={4 * E1b / eV:.3f}; E3={9 * E1b / eV:.3f} ; Dx={dxq:.3e} Dp={dpq:.3e} Dx*Dp={dxq * dpq:.3e} (hbar/2={hb / 2:.3e}) ratio {dxq * dpq / hb:.4f}")
P("  transition 1->2:", round(3 * E1b / eV, 3), "eV -> lambda =", round(h * c / (3 * E1b) * 1e9, 1), "nm")
P("  macroscopic: marble m=1 g, L=10 cm, E1 =", f"{np.pi ** 2 * hb ** 2 / (2 * 1e-3 * 0.01):.2e} J; marble at 1 cm/s: KE = {0.5 * 1e-3 * 1e-4:.2e} J; n ~ {0.5 * 1e-3 * 1e-4 / (np.pi ** 2 * hb ** 2 / (2 * 1e-3 * 0.01)):.2e}")

sec("QM04 tutorial I states")
E = np.array([1, 4, 9])
P("(psi1+psi2+psi3)/sqrt3: outcomes E1,4E1,9E1 each 1/3; <E> =", E.mean(), "E1 = 14/3 =", 14 / 3, "; <E^2>=", (E ** 2).mean(), " DE =", round(np.sqrt((E ** 2).mean() - E.mean() ** 2), 5), "E1")
P("(psi1+psi2)/sqrt2: <E> = 5/2 E1, DE = 3/2 E1; |Psi|^2 = (psi1^2+psi2^2)/2 + psi1 psi2 cos(3E1 t/hbar); period 2 pi hbar/(3 E1)")
P("times: t=0 -> cross term +; t=pi hbar/(2E1): cos(3pi/2)=0; t=pi hbar/E1: cos 3pi = -1; t=2 pi hbar/E1: cos 6 pi = +1")
xs = np.linspace(0, 1, 100001)
p1 = np.sqrt(2) * np.sin(np.pi * xs); p2 = np.sqrt(2) * np.sin(2 * np.pi * xs)
for nm, ph in (("t=0", 0), ("t=pi hbar/(2E1)", 3 * np.pi / 2), ("t=pi hbar/E1", 3 * np.pi), ("t=2 pi hbar/E1", 6 * np.pi)):
    dens = 0.5 * (p1 ** 2 + p2 ** 2) + p1 * p2 * np.cos(ph)
    P(f"  {nm}: <x>/L = {np.trapezoid(xs * dens, xs):.4f}")
P("analytic <x>(t) = L/2 + (1/2)*2*<1|x|2> cos(3E1 t/hbar) with <1|x|2> = -16 L/(9 pi^2) =", round(-16 / (9 * np.pi ** 2), 5), " -> <x> = L/2 -", round(16 / (9 * np.pi ** 2), 5), "L cos(...)")

sec("QM05 harmonic oscillator via sympy")
xx, m, w, hbs = sp.symbols("x m omega hbar", positive=True)
psi0 = (m * w / (sp.pi * hbs)) ** sp.Rational(1, 4) * sp.exp(-m * w * xx ** 2 / (2 * hbs))
ap = lambda f: (m * w * xx * f - hbs * sp.diff(f, xx)) / sp.sqrt(2 * hbs * m * w)
am = lambda f: (m * w * xx * f + hbs * sp.diff(f, xx)) / sp.sqrt(2 * hbs * m * w)
psi1 = sp.simplify(ap(psi0)); psi2 = sp.simplify(ap(psi1) / sp.sqrt(2)); psi3 = sp.simplify(ap(psi2) / sp.sqrt(3))
P("psi1 =", psi1); P("psi2 =", sp.simplify(psi2))
Hh = lambda f: -hbs ** 2 / (2 * m) * sp.diff(f, xx, 2) + m * w ** 2 * xx ** 2 / 2 * f
for k, f in enumerate((psi0, psi1, psi2, psi3)):
    P(f"  H psi{k} / psi{k} =", sp.simplify(Hh(f) / f), " norm =", sp.simplify(sp.integrate(f ** 2, (xx, -sp.oo, sp.oo))))
P("a- psi0 = 0:", sp.simplify(am(psi0)) == 0, "; a- psi1 / psi0 =", sp.simplify(am(psi1) / psi0), "; a+ psi0/psi1 =", sp.simplify(ap(psi0) / psi1), "; a+ psi1 /psi2 =", sp.simplify(ap(psi1) / psi2), "(sqrt2)")
P("[a-,a+] psi0 =", sp.simplify(am(ap(psi0)) - ap(am(psi0)) - psi0) == 0)
P("<0|x|1> =", sp.simplify(sp.integrate(psi0 * xx * psi1, (xx, -sp.oo, sp.oo))), " (sqrt(hbar/2 m w) expected)")
P("<x^2> in psi_n:", [sp.simplify(sp.integrate(f * xx ** 2 * f, (xx, -sp.oo, sp.oo))) for f in (psi0, psi1, psi2)], " <p^2>:",
  [sp.simplify(sp.integrate(f * (-hbs ** 2) * sp.diff(f, xx, 2), (xx, -sp.oo, sp.oo))) for f in (psi0, psi1, psi2)])
dxs = [sp.sqrt(sp.simplify(sp.integrate(f * xx ** 2 * f, (xx, -sp.oo, sp.oo)))) for f in (psi0, psi1, psi2)]
dps = [sp.sqrt(sp.simplify(sp.integrate(f * (-hbs ** 2) * sp.diff(f, xx, 2), (xx, -sp.oo, sp.oo)))) for f in (psi0, psi1, psi2)]
P("Dx*Dp / hbar for n=0,1,2:", [sp.simplify(a * b / hbs) for a, b in zip(dxs, dps)])
P("classical turning points x_t = sqrt((2n+1) hbar/(m w)): n=0:", 1, "units sqrt(hbar/m w); nodes of psi1:", 0, " psi2:", "x = +-1/sqrt(2) units sqrt(hbar/(m w))")
# nodes
P("nodes psi2:", sp.solve(sp.simplify(psi2 / psi0), xx))
# time-dependent <x> for (psi0+psi1)/sqrt2
P("(psi0+psi1)/sqrt2: <x>(t) = sqrt(hbar/2 m w) cos(w t); amplitude for electron in w=1e15 rad/s:", round(np.sqrt(hb / (2 * me * 1e15)) * 1e10, 3), "Angstrom")
# CO2 bend
nu_cm = 667.0
Ehw = h * c * 100 * nu_cm
P(f"CO2 bending 667 cm^-1: hbar*omega = h c nu~ = {Ehw / eV:.4f} eV ; lambda = {1e4 / nu_cm:.2f} um ; omega = {2 * np.pi * c * 100 * nu_cm:.3e} rad/s")
P("zero-point energy hbar w/2 =", round(Ehw / 2 / eV, 4), "eV; thermal kT(288K) =", round(1.380649e-23 * 288 / eV, 4), "eV; Boltzmann factor for n=1 relative to n=0:", round(np.exp(-Ehw / (1.380649e-23 * 288)), 4))

sec("QM05 Gaussian integrals / Fourier")
a_, b_ = sp.symbols("a b", positive=True)
P("int exp(-a x^2) =", sp.integrate(sp.exp(-a_ * xx ** 2), (xx, -sp.oo, sp.oo)))
P("int exp(-a x^2 + b x) =", sp.simplify(sp.integrate(sp.exp(-a_ * xx ** 2 + b_ * xx), (xx, -sp.oo, sp.oo))))
k = sp.symbols("k", real=True); s = sp.symbols("sigma", positive=True)
FT = sp.simplify(sp.integrate(sp.exp(-xx ** 2 / (2 * s ** 2)) * sp.exp(-sp.I * k * xx), (xx, -sp.oo, sp.oo)) / sp.sqrt(2 * sp.pi))
P("FT of exp(-x^2/2s^2) =", FT, "  -> width in k is 1/sigma (for |f|: exp(-k^2 sigma^2) has std 1/(sqrt2 sigma))")

sec("QM04 symmetric V and E >= Vmin check numerically (finite well)")
# finite square well depth V0, width 2a: lowest energy > 0 = Vmin
from scipy.linalg import eigh_tridiagonal
N = 4000; xg = np.linspace(-10, 10, N); dxg = xg[1] - xg[0]
V = np.where(abs(xg) < 1, 0.0, 20.0)
d = 1 / dxg ** 2 + V; o = -0.5 / dxg ** 2 * np.ones(N - 1) * 2 / 2
w_, vv = eigh_tridiagonal(1.0 / dxg ** 2 * 0.5 * 2 + V - 0, -0.5 / dxg ** 2 * np.ones(N - 1))
P("finite well V=0 (|x|<1), 20 outside (hbar=m=1): lowest 4 energies", np.round(w_[:4], 4), "(all > Vmin=0; infinite well would give", np.round([(np.pi * j / 2) ** 2 / 2 for j in range(1, 5)], 4), ")")
for j in range(3):
    f = vv[:, j]; par = np.sign(f[N // 2 + 5] * f[N // 2 - 6] + 0.0)
    P(f"   state {j}: parity {'even' if par > 0 else 'odd'} (f(x)f(-x)>0 -> even)")


sec("QM01 practice-problem numbers")
# P3: single slit for electrons at 100 V through a 1 um slit
lam100 = h / np.sqrt(2 * me * e * 100.0)
P(f"100 V electrons: lambda={lam100 * 1e9:.4f} nm ; slit a=1 um: first minimum sin(theta)=lambda/a -> theta={lam100 / 1e-6:.3e} rad ; dp ~ h/a = {h / 1e-6:.3e} kg m/s")
# P4: sinc packet K=2e10 m^-1
K = 2e10
P(f"K=2e10 m^-1: first zeros at +-pi/K = {np.pi / K * 1e9:.4f} nm ; momentum band +-hbar K = +-{hb * K:.3e} kg m/s ; kinetic energy at edge hbar^2K^2/2m = {hb ** 2 * K ** 2 / (2 * me) / eV:.3f} eV")
# P5: Gaussian sigma=0.1 nm
s = 0.1e-9
dp = hb / (2 * s)
P(f"sigma=0.1 nm: dp={dp:.3e} kg m/s ; dp^2/2m={dp ** 2 / (2 * me) / eV:.3f} eV ; dv={dp / me:.3e} m/s")
# P6: proton in a nucleus
hbc = 197.3269804  # MeV fm
mp = 938.272
for dx in (5.0,):
    for f, nm in ((0.5, "hbar/2dx"), (1.0, "hbar/dx")):
        pc = f * hbc / dx
        P(f"proton dx={dx} fm: pc >= {nm} = {pc:.2f} MeV ; KE ~ (pc)^2/2mc^2 = {pc ** 2 / (2 * mp):.3f} MeV ; v/c = {pc / mp:.3f}")
# P7: hydrogen-like ions
for Z, nm in ((1, "H"), (2, "He+"), (3, "Li2+")):
    P(f"{nm}: r_min = a0/Z = {a0 / Z * 1e10:.4f} A ; E = -Z^2 * 13.606 = {-Z ** 2 * 13.6057:.2f} eV")
# P9: Compton for Mo K-alpha X-rays at 90 deg
lam0 = 71.1e-12
lam1 = lam0 + lamC
E0x = h * c / lam0 / eV; E1x = h * c / lam1 / eV
P(f"Mo K-alpha {lam0 * 1e12} pm: photon {E0x / 1e3:.3f} keV -> {E1x / 1e3:.3f} keV at 90 deg ; electron kinetic energy = {(E0x - E1x):.1f} eV")
# gamma-ray
lam_g = 2.0e-12
P(f"2 pm photon (620 keV): shift at 180 deg = {2 * lamC * 1e12:.3f} pm -> {(lam_g + 2 * lamC) * 1e12:.3f} pm ; fractional {2 * lamC / lam_g * 100:.0f} %")
# P10 de Broglie
for nm, m_, v in (("baseball 0.145 kg at 40 m/s", 0.145, 40.0), ("electron 1e6 m/s", me, 1e6), ("thermal neutron 2200 m/s", 1.67492749804e-27, 2200.0)):
    P(f"  {nm}: lambda = {h / (m_ * v):.3e} m")
# P11 time scale
P(f"hbar/(m c^2) = {hb / (me * c ** 2):.3e} s ; it is hbar/mc over c: {redC / c:.3e} s")


sec("QM05 extra checks")
from scipy.special import erfc
psi0_ = (m * w / (sp.pi * hbs)) ** sp.Rational(1, 4) * sp.exp(-m * w * xx ** 2 / (2 * hbs))
psi2_ = psi2
cross = sp.simplify(sp.integrate(psi0_ * xx ** 2 * psi2_, (xx, -sp.oo, sp.oo)))
P("<0|x^2|2> =", cross, " (expected sqrt(2) hbar/(2 m w))")
P("<0|x|1> =", sp.simplify(sp.integrate(psi0_ * xx * psi1, (xx, -sp.oo, sp.oo))), "; <1|x|2> =", sp.simplify(sp.integrate(psi1 * xx * psi2_, (xx, -sp.oo, sp.oo))), " (sqrt(2)*sqrt(hbar/2mw) expected)")
P("<V>=<T>=E/2 for n=0..2:", [sp.simplify(sp.integrate(f * (m * w ** 2 * xx ** 2 / 2) * f, (xx, -sp.oo, sp.oo)) / (hbs * w)) for f in (psi0_, psi1, psi2_)], "(in units of hbar w: 1/4, 3/4, 5/4)")
P(f"P(|x| > x_t) in the ground state = erfc(1) = {erfc(1):.4f} ; n=1: ", end=""); 
from scipy.integrate import quad as _q
H1 = lambda z: 2 * z; psi_n = lambda n, z: np.pi ** -0.25 / np.sqrt(2.0 ** n * float(sp.factorial(n))) * float(sp.hermite(n, z)) * np.exp(-z ** 2 / 2)
for nn in (0, 1, 2, 5):
    xt = np.sqrt(2 * nn + 1)
    pr = 2 * _q(lambda z: psi_n(nn, z) ** 2, xt, 12)[0]
    P(f"  n={nn}: turning point {xt:.3f}; P(forbidden) = {pr:.4f}")
# CO vibration
kf = 1857.0; mu = (12.0 * 15.9949 / (12.0 + 15.9949)) * 1.66053906660e-27
om = np.sqrt(kf / mu)
P(f"CO: k={kf} N/m, mu={mu:.4e} kg -> omega={om:.4e} rad/s, hbar omega={hb * om / eV:.4f} eV, nu~={om / (2 * np.pi * c * 100):.0f} cm^-1, lambda={2 * np.pi * c / om * 1e6:.2f} um; amplitude of zero-point motion sqrt(hbar/2 mu omega)={np.sqrt(hb / (2 * mu * om)) * 1e10:.4f} A")
P(f"  population ratio n=1/n=0 at 300 K: {np.exp(-hb * om / (1.380649e-23 * 300)):.2e}")
# Fourier transform of psi0: momentum-space width
P("psi0 in momentum space ~ exp(-p^2/(2 m w hbar)): Dp = sqrt(m w hbar/2) ; Dx = sqrt(hbar/(2 m w)) ; product hbar/2")
# N operator eigen: a+ a- psi_n = n psi_n
for k_, f in enumerate((psi0_, psi1, psi2_, psi3)):
    P(f"  a+ a- psi{k_} / psi{k_} =", sp.simplify(ap(am(f)) / f))
P("[H,a-]/hbar w = -a- :", sp.simplify((Hh(am(psi2_)) - am(Hh(psi2_))) / (hbs * w) + am(psi2_)) == 0, " ; [H,a+] = +hbar w a+:", sp.simplify((Hh(ap(psi2_)) - ap(Hh(psi2_))) / (hbs * w) - ap(psi2_)) == 0)


sec("QM05 update: oscillator lecture (Harmonic_oscillator.pdf) and Tutorial III")
psis = [psi0]
for n_ in range(1, 7):
    psis.append(sp.simplify(ap(psis[-1]) / sp.sqrt(n_)))
Int = lambda f: sp.simplify(sp.integrate(f, (xx, -sp.oo, sp.oo)))
# lecture pp.10-11: a+ psi_n = sqrt(n+1) psi_{n+1}, a- psi_n = sqrt(n) psi_{n-1}
P("a+ psi_n / psi_{n+1}, n=0..5:", [sp.simplify(ap(psis[n_]) / psis[n_ + 1]) for n_ in range(6)], "(sqrt(n+1))")
P("a- psi_n / psi_{n-1}, n=1..6:", [sp.simplify(am(psis[n_]) / psis[n_ - 1]) for n_ in range(1, 7)], "(sqrt(n))")
P("H psi_n / psi_n (units hbar w), n=0..6:", [sp.simplify(Hh(f) / f / (hbs * w)) for f in psis], "(n + 1/2)")
# lecture p.9 identity: int f (a+ g) dx = int (a- f) g dx (real functions, adjoint relation)
ok = all(sp.simplify(Int(psis[n_] * ap(psis[m_])) - Int(am(psis[n_]) * psis[m_])) == 0 for n_ in range(5) for m_ in range(5))
P("lecture identity  int f a+ g = int (a- f) g   for n,m <= 4:", ok)
# the page-9 line writes a+ = hbar d/dx + m w x (sign of a-): with it, the identity fails for psi_0, psi_1
ap_wrong = lambda f: (m * w * xx * f + hbs * sp.diff(f, xx)) / sp.sqrt(2 * hbs * m * w)
P("with the page-9 sign (hbar d/dx + m w x): int psi0 (a'psi1) - int (a- psi0) psi1 =", sp.simplify(Int(psis[0] * ap_wrong(psis[1])) - Int(am(psis[0]) * psis[1])), "(not 0: slip)")
# lecture p.12-13 and Tutorial III Q1
P("<x>_n, n=0..4:", [Int(f * xx * f) for f in psis[:5]])
P("<p>_n, n=0..4:", [Int(f * (-sp.I * hbs) * sp.diff(f, xx)) for f in psis[:5]])
P("<x^2>_n / (hbar/(2 m w)), n=0..5:", [sp.simplify(Int(f * xx ** 2 * f) / (hbs / (2 * m * w))) for f in psis[:6]], "(2n+1)")
P("<p^2>_n / (hbar m w / 2), n=0..5:", [sp.simplify(Int(f * (-hbs ** 2) * sp.diff(f, xx, 2)) / (hbs * m * w / 2)) for f in psis[:6]], "(2n+1)")
# Tutorial III Q1 by the ladder formula: <p^2> = -(m hbar w / 2) <(a+ - a-)^2> = (m hbar w / 2)(2n+1)
# Tutorial III Q2: Gaussian integrals for the ground state
a_ = sp.symbols("a", positive=True)
P("int x^2 e^{-a x^2} dx =", sp.simplify(sp.integrate(xx ** 2 * sp.exp(-a_ * xx ** 2), (xx, -sp.oo, sp.oo))), " (= sqrt(pi)/(2 a^{3/2}) = -d/da sqrt(pi/a))")
P("-d/da sqrt(pi/a) =", sp.simplify(-sp.diff(sp.sqrt(sp.pi / a_), a_)))
P("<x^2>_0 = ", sp.simplify(sp.sqrt(m * w / (sp.pi * hbs)) * sp.sqrt(sp.pi) / (2 * (m * w / hbs) ** sp.Rational(3, 2))), "= hbar/(2 m w)")
# Tutorial III Q3: orthogonality
P("<psi_m|psi_n>, 0<=m<n<=6 (all zero?):", all(Int(psis[m_] * psis[n_]) == 0 for n_ in range(7) for m_ in range(n_)))
P("<psi_n|psi_n> =", [Int(f * f) for f in psis[:7]])
# the classical question on lecture p.2: time spent near x for x = A cos(w t)
rng_q = np.random.default_rng(5)
tt = rng_q.uniform(0, 2 * np.pi, 2_000_000); xc = np.cos(tt)
P("classical x = A cos(wt): P(|x| < A/2) simulated", round(float((np.abs(xc) < 0.5).mean()), 4), " exact (2/pi) arcsin(1/2) = 1/3 =", round(2 / np.pi * np.arcsin(0.5), 4))
P("  P(|x| > 0.9 A) simulated", round(float((np.abs(xc) > 0.9).mean()), 4), " exact 1-(2/pi) arcsin(0.9) =", round(1 - 2 / np.pi * np.arcsin(0.9), 4))
P("  normalisation of 1/(pi sqrt(A^2-x^2)) over [-A,A]:", quad(lambda x: 1 / (np.pi * np.sqrt(1 - x ** 2)), -1, 1)[0])
# quantum density of n=20 vs classical time-average, averaged over a window near the centre
from scipy.special import eval_hermite, gammaln
def psin_num(n, z):
    return np.pi ** -0.25 * np.exp(-z ** 2 / 2 - 0.5 * (n * np.log(2) + gammaln(n + 1))) * eval_hermite(n, z)
n_hi = 20; xt_hi = np.sqrt(2 * n_hi + 1)
Pq = quad(lambda z: psin_num(n_hi, z) ** 2, -xt_hi / 2, xt_hi / 2, limit=400)[0]
P(f"n=20: quantum P(|x| < x_t/2) = {Pq:.4f} vs classical 1/3 (correspondence)")


sec("QM06 oscillator toolbox: Hermite polynomials")
from math import factorial as fac
from scipy.special import eval_hermite, gammaln
from scipy.linalg import expm
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
xi_, t_ = sp.symbols("xi t", real=True)
Hn = [sp.hermite(n, xi_) for n in range(9)]
for n_ in range(7):
    P(f"  H_{n_} =", sp.expand(Hn[n_]))
P("Rodrigues H_n = (-1)^n e^{xi^2} d^n/dxi^n e^{-xi^2}, n<=7:", all(sp.simplify((-1) ** n_ * sp.exp(xi_ ** 2) * sp.diff(sp.exp(-xi_ ** 2), xi_, n_) - Hn[n_]) == 0 for n_ in range(8)))
P("recurrence H_{n+1} = 2 xi H_n - 2 n H_{n-1}, n=1..7:", all(sp.expand(Hn[n_ + 1] - (2 * xi_ * Hn[n_] - 2 * n_ * Hn[n_ - 1])) == 0 for n_ in range(1, 8)))
P("H_n' = 2 n H_{n-1}, n=1..8:", all(sp.expand(sp.diff(Hn[n_], xi_) - 2 * n_ * Hn[n_ - 1]) == 0 for n_ in range(1, 9)))
P("H_{n+1} = 2 xi H_n - H_n' (the ladder identity), n=0..7:", all(sp.expand(Hn[n_ + 1] - (2 * xi_ * Hn[n_] - sp.diff(Hn[n_], xi_))) == 0 for n_ in range(8)))
P("Hermite ODE h'' - 2 xi h' + 2 n h = 0, n=0..8:", all(sp.expand(sp.diff(Hn[n_], xi_, 2) - 2 * xi_ * sp.diff(Hn[n_], xi_) + 2 * n_ * Hn[n_]) == 0 for n_ in range(9)))
gf = sp.series(sp.exp(2 * xi_ * t_ - t_ ** 2), t_, 0, 9).removeO()
P("generating function e^{2 xi t - t^2} = sum H_n t^n/n!, n<=8:", all(sp.expand(sp.Poly(gf, t_).coeff_monomial(t_ ** n_) * fac(n_) - Hn[n_]) == 0 for n_ in range(9)))
P("H_n(0), n=0..8:", [Hn[n_].subs(xi_, 0) for n_ in range(9)], " (even n=2k: (-1)^k (2k)!/k! =", [(-1) ** k * fac(2 * k) // fac(k) for k in range(5)], ")")
P("leading coefficient of H_n = 2^n:", [sp.Poly(Hn[n_], xi_).LC() for n_ in range(8)])
orth = [[sp.integrate(Hn[m_] * Hn[n_] * sp.exp(-xi_ ** 2), (xi_, -sp.oo, sp.oo)) for n_ in range(5)] for m_ in range(5)]
P("int H_m H_n e^{-xi^2} (m,n<=4):", [[sp.simplify(v) for v in row] for row in orth])
P("  sqrt(pi) 2^n n! =", [sp.simplify(sp.sqrt(sp.pi) * 2 ** n_ * fac(n_)) for n_ in range(5)])
from numpy.polynomial.hermite import hermroots
for n_ in range(1, 8):
    r = np.sort(hermroots([0] * n_ + [1]))
    P(f"  zeros of H_{n_} (positive): {r[r > 1e-12]}")
# probabilists' Hermite
Hep = [sp.expand(sp.hermite_prob(n_, xi_)) for n_ in range(7)]
P("  He_n(x) = 2^{-n/2} H_n(x/sqrt2), n<=6:", all(sp.simplify(Hep[n_] - 2 ** (-sp.Rational(n_, 2)) * Hn[n_].subs(xi_, xi_ / sp.sqrt(2))) == 0 for n_ in range(7)))
for n_ in range(5):
    P(f"  He_{n_} =", Hep[n_])
phi_ = sp.exp(-xi_ ** 2 / 2) / sp.sqrt(2 * sp.pi)
P("  E[He_m(Z) He_n(Z)] (m,n<=4) =", [[sp.simplify(sp.integrate(Hep[m_] * Hep[n_] * phi_, (xi_, -sp.oo, sp.oo))) for n_ in range(5)] for m_ in range(5)], "(n! on the diagonal)")
P("  E[Z^{2k}] =", [sp.integrate(xi_ ** (2 * k) * phi_, (xi_, -sp.oo, sp.oo)) for k in range(5)], " (2k-1)!! =", [int(np.prod(range(1, 2 * k, 2))) if k else 1 for k in range(5)])
P("  generating function of He_n: e^{x t - t^2/2}; the MGF of N(0,1) is e^{t^2/2}, so e^{x t - t^2/2} = e^{x t} / M_Z(t)")

sec("QM06 normalisation of psi_n three ways (units hbar = m = omega = 1)")
hermfun = lambda n, z: np.pi ** -0.25 * np.exp(-z ** 2 / 2 - 0.5 * (n * np.log(2) + gammaln(n + 1))) * eval_hermite(n, z)
P("int psi_n^2 dx, n=0..10:", [round(quad(lambda z: hermfun(n_, z) ** 2, -14, 14, limit=300)[0], 10) for n_ in range(11)])
for n_ in (5, 10):
    P(f"  int H_{n_}^2 e^(-xi^2) = {quad(lambda z: eval_hermite(n_, z) ** 2 * np.exp(-z ** 2), -14, 14, limit=300)[0]:.6e} ; sqrt(pi) 2^n n! = {np.sqrt(np.pi) * 2 ** n_ * fac(n_):.6e}")
P("  ladder constant recursion N_{n+1} = N_n / sqrt(2(n+1)):", all(abs(np.pi ** -0.25 / np.sqrt(2.0 ** (n_ + 1) * fac(n_ + 1)) - np.pi ** -0.25 / np.sqrt(2.0 ** n_ * fac(n_)) / np.sqrt(2 * (n_ + 1))) < 1e-15 for n_ in range(12)))

sec("QM06 series solution and the shooting method")
def series_coeffs(K, J=61, par=0):
    a = np.zeros(J + 1); a[par] = 1.0
    for j in range(par, J - 1, 2):
        a[j + 2] = (2 * j + 1 - K) / ((j + 1) * (j + 2)) * a[j]
    return a
P("K = 5 (n=2), even series:", series_coeffs(5.0)[:7], " -> 1 - 2 xi^2 = -H_2/2")
P("K = 3 (n=1), odd series:", series_coeffs(3.0, par=1)[:6], " -> xi (H_1/2)")
P("K = 9 (n=4), even series:", series_coeffs(9.0)[:9], " -> 1 - 4 xi^2 + (4/3) xi^4 = H_4/12")
a2 = series_coeffs(2.0, J=121)
for j in (20, 40, 80):
    P(f"  K=2 (not allowed): a_(j+2)/a_j at j={j}: {a2[j + 2] / a2[j]:.5f} vs 2/(j+2) = {2 / (j + 2):.5f} (the coefficient ratio of e^(xi^2))")
def shoot(K, par, xe=6.0):
    f = lambda z, y: [y[1], (z ** 2 - K) * y[0]]
    y0 = [1.0, 0.0] if par == 0 else [0.0, 1.0]
    return solve_ivp(f, [0, xe], y0, rtol=1e-10, atol=1e-12).y[0, -1]
for par in (0, 1):
    Ks = np.linspace(0.2, 10.5, 2000); vals = [shoot(K_, par) for K_ in Ks]
    roots = [brentq(lambda K_: shoot(K_, par), Ks[i], Ks[i + 1]) for i in range(len(Ks) - 1) if vals[i] * vals[i + 1] < 0]
    P(f"  {'even' if par == 0 else 'odd'} solutions: psi(6) changes sign at K = {np.round(roots, 4)} -> E = K/2 = {np.round(np.array(roots) / 2, 4)}")

sec("QM06 number basis (Fock) matrices, units hbar = m = omega = 1")
NN = 200
a_f = np.diag(np.sqrt(np.arange(1, NN)), 1); ad_f = a_f.T
x_f = (a_f + ad_f) / np.sqrt(2); p_f = 1j * (ad_f - a_f) / np.sqrt(2)
nn_ = 8
P("a (top-left 5x5):\n", a_f[:5, :5].round(4))
P("x (top-left 5x5):\n", x_f[:5, :5].round(4))
P("p (top-left 5x5, imaginary part):\n", p_f[:5, :5].imag.round(4))
cm = a_f @ ad_f - ad_f @ a_f
P("[a, a+] diagonal: first 4:", np.diag(cm)[:4], " last:", np.diag(cm)[-1], "(truncation artefact: [a,a+]=1 cannot hold in a finite matrix, its trace is 0)")
X2 = x_f @ x_f; X3 = X2 @ x_f; X4 = X2 @ X2; P2 = p_f @ p_f; P4 = P2 @ P2
n_arr = np.arange(10)
P("<n|x^2|n> / (1/2):", np.diag(X2)[:10].real * 2, " = 2n+1")
P("<n|x^4|n> / (1/2)^2 vs 6n^2+6n+3:", np.round(np.diag(X4)[:10].real * 4, 8), (6 * n_arr ** 2 + 6 * n_arr + 3))
P("<n|p^4|n> / (1/2)^2:", np.round(np.diag(P4)[:10].real * 4, 8))
P("<n|x^3|n> (all zero):", np.abs(np.diag(X3)[:10]).max())
P("<n|x^2|n+2> / (1/2) vs sqrt((n+1)(n+2)):", np.round(np.diag(X2, 2)[:6] * 2, 6), np.round(np.sqrt((n_arr[:6] + 1) * (n_arr[:6] + 2)), 6))
m_ = 3
P(f"completeness: sum_n |<{m_}|x|n>|^2 = {np.sum(np.abs(x_f[m_, :]) ** 2):.6f} = <{m_}|x^2|{m_}> = {X2[m_, m_].real:.6f}")
En_ = np.arange(NN) + 0.5
P(f"Thomas-Reiche-Kuhn sum rule: sum_n (E_n - E_{m_}) |x_nm|^2 = {np.sum((En_ - En_[m_]) * np.abs(x_f[:, m_]) ** 2):.6f} = hbar^2/2m = 0.5")
Ht = (X2 + P2).real / 2
w_ = np.linalg.eigvalsh(Ht[:60, :60])
P("(x^2+p^2)/2 in a 60x60 truncation, lowest 5:", np.round(w_[:5], 6), " top 2:", np.round(w_[-2:], 3), " (the top rows are corrupted by truncation: use n << N)")
selection = np.argwhere(np.abs(x_f[:12, :12]) > 1e-12)
P("nonzero <m|x|n> for m,n<12 occur only for |m-n| =", sorted({abs(int(i) - int(j)) for i, j in selection}))

sec("QM06 Fourier invariance of the Hermite functions (momentum space)")
for n_ in range(5):
    for p0 in (0.4, 1.3):
        re = quad(lambda z: hermfun(n_, z) * np.cos(p0 * z), -14, 14, limit=300)[0] / np.sqrt(2 * np.pi)
        im = -quad(lambda z: hermfun(n_, z) * np.sin(p0 * z), -14, 14, limit=300)[0] / np.sqrt(2 * np.pi)
        P(f"  n={n_}, p={p0}: psi~_n(p)/psi_n(p) = {(re + 1j * im) / hermfun(n_, p0):.5f} ; (-i)^n = {(-1j) ** n_}")

sec("QM06 uncertainty-principle estimate of the zero-point energy")
f_ = lambda s: 1 / (8 * s) + s / 2
r_ = minimize_scalar(f_, bounds=(0.01, 5), method="bounded", options=dict(xatol=1e-10))
P(f"E(s) = 1/(8 s) + s/2 with s = (Dx)^2: minimum E = {r_.fun:.6f} at s = {r_.x:.6f} (exact: 1/2 at s = 1/2) -> hbar omega/2, sharp because the ground state is a Gaussian")

sec("QM06 virial theorem beyond the oscillator (finite-difference ground states, hbar = m = 1)")
from scipy.linalg import eigh_tridiagonal
def gs(V, L=7.0, Ng=6001):
    xg = np.linspace(-L, L, Ng); dxg = xg[1] - xg[0]
    d = 1 / dxg ** 2 + V(xg); e = -0.5 / dxg ** 2 * np.ones(Ng - 1)
    w, v = eigh_tridiagonal(d, e, select="i", select_range=(0, 0))
    f = v[:, 0] / np.sqrt(np.sum(v[:, 0] ** 2) * dxg)
    T = 0.5 * np.sum(np.gradient(f, dxg) ** 2) * dxg; Vv = np.sum(V(xg) * f ** 2) * dxg
    return w[0], T, Vv
for nm, V, s in (("x^2/2", lambda z: 0.5 * z ** 2, 2), ("x^4", lambda z: z ** 4, 4), ("|x|", lambda z: np.abs(z), 1)):
    E0, T0, V0 = gs(V)
    P(f"  V = {nm}: E0 = {E0:.5f}, <T> = {T0:.5f}, <V> = {V0:.5f}, 2<T>/<V> = {2 * T0 / V0:.4f} (virial: s = {s})")

sec("QM06 Ehrenfest and Heisenberg (units hbar = m = omega = 1)")
x_s = sp.symbols("x", real=True)
ps0 = sp.pi ** sp.Rational(-1, 4) * sp.exp(-x_s ** 2 / 2); ps1 = sp.sqrt(2) * x_s * ps0
Psi = (ps0 * sp.exp(-sp.I * t_ / 2) + ps1 * sp.exp(-3 * sp.I * t_ / 2)) / sp.sqrt(2)
Psic = (ps0 * sp.exp(sp.I * t_ / 2) + ps1 * sp.exp(3 * sp.I * t_ / 2)) / sp.sqrt(2)
ex = sp.simplify(sp.integrate(Psic * x_s * Psi, (x_s, -sp.oo, sp.oo)))
ep = sp.simplify(sp.integrate(Psic * (-sp.I) * sp.diff(Psi, x_s), (x_s, -sp.oo, sp.oo)))
P("<x>(t) =", ex, " ; <p>(t) =", ep)
P("Ehrenfest d<x>/dt - <p> =", sp.simplify(sp.diff(ex, t_) - ep), " ; d<p>/dt + <x> =", sp.simplify(sp.diff(ep, t_) + ex))
Nh = 40; Hd = np.diag(np.arange(Nh) + 0.5); a_h = np.diag(np.sqrt(np.arange(1, Nh)), 1); tt0 = 0.83
U = expm(1j * Hd * tt0); a_t = U @ a_h @ U.conj().T
P(f"Heisenberg a(t) = a e^(-i w t): max error {np.abs(a_t - a_h * np.exp(-1j * tt0)).max():.2e}")
x_h = (a_h + a_h.T) / np.sqrt(2); p_h = 1j * (a_h.T - a_h) / np.sqrt(2)
x_t = U @ x_h @ U.conj().T
P(f"Heisenberg x(t) = x cos wt + p sin wt (m = w = 1): max error {np.abs(x_t - (x_h * np.cos(tt0) + p_h * np.sin(tt0))).max():.2e}")
P("[H, x] = -i p and [H, p] = i x (units): errors", np.abs((Hd @ x_h - x_h @ Hd)[:30, :30] + 1j * p_h[:30, :30]).max(), np.abs((Hd @ p_h - p_h @ Hd)[:30, :30] - 1j * x_h[:30, :30]).max())

sec("QM06 coherent states (units hbar = m = omega = 1)")
from scipy import stats
Nc = 90; nn = np.arange(Nc)
a_c = np.diag(np.sqrt(np.arange(1, Nc)), 1); ad_c = a_c.T
def coh(al): return np.exp(-abs(al) ** 2 / 2) * np.array([al ** k / np.sqrt(float(fac(k))) for k in range(Nc)])
al1, al2 = 2.0 + 0j, 1.2 + 0.9j
for al in (al1, al2):
    c = coh(al)
    x_m = c.conj() @ ((a_c + ad_c) / np.sqrt(2)) @ c; p_m = c.conj() @ (1j * (ad_c - a_c) / np.sqrt(2)) @ c
    x2m = c.conj() @ (((a_c + ad_c) / np.sqrt(2)) @ ((a_c + ad_c) / np.sqrt(2))) @ c
    p2m = c.conj() @ ((1j * (ad_c - a_c) / np.sqrt(2)) @ (1j * (ad_c - a_c) / np.sqrt(2))) @ c
    nmean = (np.abs(c) ** 2 * nn).sum(); nvar = (np.abs(c) ** 2 * nn ** 2).sum() - nmean ** 2
    P(f"  alpha = {al}: norm {np.vdot(c, c).real:.8f}; |a c - alpha c| = {np.linalg.norm(a_c @ c - al * c):.2e}; <n> = {nmean:.5f} (|alpha|^2 = {abs(al) ** 2:.5f}); Var n = {nvar:.5f}")
    P(f"     <x> = {x_m.real:.5f} (sqrt2 Re a = {np.sqrt(2) * al.real:.5f}); <p> = {p_m.real:.5f} (sqrt2 Im a = {np.sqrt(2) * al.imag:.5f}); Dx = {np.sqrt(x2m.real - x_m.real ** 2):.5f}; Dp = {np.sqrt(p2m.real - p_m.real ** 2):.5f}; Dx Dp = {np.sqrt((x2m.real - x_m.real ** 2) * (p2m.real - p_m.real ** 2)):.5f}")
    P(f"     max | |c_n|^2 - Poisson(|alpha|^2) | = {np.abs(np.abs(c) ** 2 - stats.poisson.pmf(nn, abs(al) ** 2)).max():.2e}")
c = coh(al2)
for tt1 in (0.0, 0.7, 2.0):
    ct = c * np.exp(-1j * (nn + 0.5) * tt1)
    P(f"  t = {tt1}: <x> = {(ct.conj() @ ((a_c + ad_c) / np.sqrt(2)) @ ct).real:.5f} vs sqrt2 Re(alpha e^(-it)) = {np.sqrt(2) * (al2 * np.exp(-1j * tt1)).real:.5f}")
be = 0.3 - 0.5j
P(f"  |<alpha|beta>| = {abs(np.vdot(coh(al2), coh(be))):.6f} vs exp(-|alpha-beta|^2/2) = {np.exp(-abs(al2 - be) ** 2 / 2):.6f}")
Dd = expm(al2 * ad_c - np.conj(al2) * a_c)
P(f"  D(alpha)|0> vs |alpha>: max difference {np.abs(Dd[:, 0] - coh(al2)).max():.2e}")
xg = np.array([-2.0, -0.5, 0.3, 1.7]); x0, p0 = np.sqrt(2) * al2.real, np.sqrt(2) * al2.imag
psi_sum = sum(coh(al2)[k] * hermfun(k, xg) for k in range(Nc))
psi_gauss = np.pi ** -0.25 * np.exp(-(xg - x0) ** 2 / 2 + 1j * p0 * xg - 1j * x0 * p0 / 2)
P("  psi_alpha(x) from the Fock sum / Gaussian formula (should be 1):", np.round(psi_sum / psi_gauss, 6))

sec("QM06 thermal oscillator")
c2 = 1.438777   # second radiation constant, K per cm^-1
for nm, nu in (("CO stretch 2143 cm^-1", 2143.0), ("CO2 bend 667 cm^-1", 667.0)):
    th = c2 * nu
    for T in (288.0, 300.0):
        x = th / T
        P(f"  {nm}: theta_v = {th:.0f} K ; T = {T:.0f} K: x = {x:.3f}, <n> = {1 / np.expm1(x):.5f}, P(n>=1) = {np.exp(-x):.5f}, C/k = {x ** 2 * np.exp(x) / np.expm1(x) ** 2:.5f}")
for x in (0.1, 1.0, 3.0, 10.0):
    P(f"  Einstein function x = {x}: C/k = {x ** 2 * np.exp(x) / np.expm1(x) ** 2:.5f} (1 - x^2/12 = {1 - x ** 2 / 12:.5f})")
x = 1.7; pq = (1 - np.exp(-x)) * np.exp(-x * nn)
P(f"  p_n = (1 - e^-x) e^(-n x), x = {x}: sum = {pq.sum():.8f}; mean n = {(pq * nn).sum():.6f} vs 1/(e^x - 1) = {1 / np.expm1(x):.6f}; geometric (failures) mean q/p = {np.exp(-x) / (1 - np.exp(-x)):.6f}; Var = {((pq * nn ** 2).sum() - (pq * nn).sum() ** 2):.5f} vs q/p^2 = {np.exp(-x) / (1 - np.exp(-x)) ** 2:.5f}")
P("  thermal Mandel Q = Var/<n> - 1 = <n> (super-Poissonian); coherent Q = 0")

sec("QM06 degeneracy of isotropic oscillators")
from itertools import product
for N in range(7):
    d2 = sum(1 for t in product(range(N + 1), repeat=2) if sum(t) == N)
    d3 = sum(1 for t in product(range(N + 1), repeat=3) if sum(t) == N)
    P(f"  N = {N}: 2D degeneracy {d2} (N+1 = {N + 1}); 3D degeneracy {d3} ((N+1)(N+2)/2 = {(N + 1) * (N + 2) // 2})")

sec("QM06 anharmonic shift: H = (p^2 + x^2)/2 + lambda x^4")
Nb = 260; ab = np.diag(np.sqrt(np.arange(1, Nb)), 1); xb = (ab + ab.T) / np.sqrt(2); x4 = np.linalg.matrix_power(xb, 4)[:140, :140]
Hb0 = np.diag(np.arange(140) + 0.5)
for lam in (0.001, 0.002):
    Ev = np.linalg.eigvalsh(Hb0 + lam * x4)[:3]
    P(f"  lambda = {lam}: E_0 - 1/2 = {Ev[0] - 0.5:.8f} ; first order 3 lambda/4 = {0.75 * lam:.8f} ; with -21 lambda^2/8: {0.75 * lam - 21 / 8 * lam ** 2:.8f} ; E_1 - 3/2 = {Ev[1] - 1.5:.8f} vs 15 lambda/4 = {15 * lam / 4:.8f}")
