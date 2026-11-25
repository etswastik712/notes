"""QM13 numbers: probability current and Ehrenfest's theorem (hbar = m = 1 unless stated).
Run: python scripts/qm13_numbers.py
"""
import numpy as np

# ---------- 1. Box superposition (psi1 + psi2)/sqrt2: rho, j, <x>, continuity ----------
L = 1.0
E = lambda n: n**2 * np.pi**2 / (2 * L**2)          # hbar = m = 1
w21 = E(2) - E(1)
x = np.linspace(0, L, 20001)
psi = lambda n, x, t: np.sqrt(2 / L) * np.sin(n * np.pi * x / L) * np.exp(-1j * E(n) * t)
Psi = lambda x, t: (psi(1, x, t) + psi(2, x, t)) / np.sqrt(2)

def j_num(x, t, h=1e-6):
    P = Psi(x, t)
    dP = (Psi(x + h, t) - Psi(x - h, t)) / (2 * h)
    return np.imag(np.conj(P) * dP)                  # j = (hbar/m) Im(psi* psi')

def j_formula(x, t):
    return (w21 / np.pi) * np.sin(w21 * t) * (np.sin(np.pi * x / L) - np.sin(3 * np.pi * x / L) / 3)

t = 0.37
xs = np.linspace(0.05, 0.95, 7)
print("1. box (1+2)/sqrt2, t=%.2f" % t)
print("   max |j_num - j_formula| on interior:", np.max(np.abs(j_num(xs, t) - j_formula(xs, t))))
print("   j at the walls (formula): x=0 ->", j_formula(0.0, t), " x=L ->", j_formula(L, t))
rho = lambda x, t: np.abs(Psi(x, t))**2
h = 1e-5
drho = (rho(xs, t + h) - rho(xs, t - h)) / (2 * h)
dj = (j_formula(xs + 1e-5, t) - j_formula(xs - 1e-5, t)) / 2e-5
print("   continuity residual max |d_t rho + d_x j|:", np.max(np.abs(drho + dj)))
xm = lambda t: np.trapezoid(x * rho(x, t), x)
print("   <x>(t) numeric = %.6f ; formula L/2-16L/(9pi^2)cos(w21 t) = %.6f" %
      (xm(t), L / 2 - 16 * L / (9 * np.pi**2) * np.cos(w21 * t)))
print("   16/(9 pi^2) = %.6f ; w21 = 3 pi^2/2 = %.5f" % (16 / (9 * np.pi**2), w21))
dxm = (xm(t + 1e-4) - xm(t - 1e-4)) / 2e-4
print("   d<x>/dt = %.6f ; int j dx = %.6f ; <p>/m: see below" % (dxm, np.trapezoid(j_formula(x, t), x)))
pm = np.trapezoid(np.real(np.conj(Psi(x, t)) * (-1j) * (Psi(x + 1e-6, t) - Psi(x - 1e-6, t)) / 2e-6), x)
print("   <p> = %.6f" % pm)

# ---------- 2. Gaussian packet with momentum k0: j = (hbar k0/m) rho ----------
k0, s0 = 3.0, 0.7
g = lambda x: (2 * np.pi * s0**2) ** -0.25 * np.exp(-x**2 / (4 * s0**2) + 1j * k0 * x)
xx = np.linspace(-8, 8, 40001)
gp = (g(xx + 1e-6) - g(xx - 1e-6)) / 2e-6
jj = np.imag(np.conj(g(xx)) * gp)
print("\n2. Gaussian packet, k0=3: max |j - k0 rho| =", np.max(np.abs(jj - k0 * np.abs(g(xx))**2)),
      "; int j dx =", np.trapezoid(jj, xx))

# ---------- 3. TDSE split-step: Ehrenfest in V = x^4/4, x^2/2, and uniform force ----------
def run(V, x0=1.5, sig=0.5, T=2.0, dt=5e-4, N=4096, Lx=40.0):
    xg = np.linspace(-Lx / 2, Lx / 2, N, endpoint=False)
    dx = xg[1] - xg[0]
    k = 2 * np.pi * np.fft.fftfreq(N, dx)
    psi = (2 * np.pi * sig**2) ** -0.25 * np.exp(-(xg - x0)**2 / (4 * sig**2)).astype(complex)
    Vx = V(xg)
    expV = np.exp(-0.5j * Vx * dt)
    expK = np.exp(-0.5j * k**2 * dt)
    out = []
    nsteps = int(round(T / dt))
    for n in range(nsteps + 1):
        rho = np.abs(psi)**2
        pk = np.fft.fft(psi)
        p_psi = np.fft.ifft(k * pk)
        xm = np.sum(xg * rho) * dx
        pm = np.real(np.sum(np.conj(psi) * p_psi) * dx)
        out.append((n * dt, xm, pm, xg, rho))
        psi = expV * np.fft.ifft(expK * np.fft.fft(expV * psi))
    return out

def check(V, dV, label, **kw):
    out = run(V, **kw)
    ts = np.array([o[0] for o in out]); xm = np.array([o[1] for o in out]); pm = np.array([o[2] for o in out])
    force = np.array([-np.sum(dV(o[3]) * o[4]) * (o[3][1] - o[3][0]) for o in out])
    dxdt = np.gradient(xm, ts); dpdt = np.gradient(pm, ts)
    sl = slice(5, -5)
    print("   %s: max|d<x>/dt - <p>| = %.2e ; max|d<p>/dt + <V'>| = %.2e ; <V'>(0) = %.4f ; V'(<x>)(0) = %.4f ; d<p>/dt(0)~%.4f"
          % (label, np.max(np.abs(dxdt - pm)[sl]), np.max(np.abs(dpdt - force)[sl]),
             -force[0], dV(np.array([xm[0]]))[0], np.gradient(pm, ts)[5]))
    return ts, xm, pm

print("\n3. TDSE checks (hbar = m = 1, Gaussian x0=1.5, sigma=0.5, p0=0, T=2)")
ts, xm, pm = check(lambda x: x**4 / 4, lambda x: x**3, "V=x^4/4")
ts, xm2, pm2 = check(lambda x: x**2 / 2, lambda x: x, "V=x^2/2")
print("   oscillator: max |<x>(t) - x0 cos t| = %.2e" % np.max(np.abs(xm2 - 1.5 * np.cos(ts))))
F = 0.8
ts, xm3, pm3 = check(lambda x: -F * x, lambda x: -F * np.ones_like(x), "V=-Fx (F=0.8)")
print("   uniform force: max |<x>(t) - (x0 + F t^2/2)| = %.2e (packet spreads, mean does not care)" %
      np.max(np.abs(xm3 - (1.5 + F * ts**2 / 2))))

# ---------- 4. Moment algebra for a Gaussian ----------
x0, s = 1.5, 0.5
print("\n4. Gaussian moments: <x^3> = x0^3 + 3 x0 s^2 = %.4f ; V'(<x>) = x0^3 = %.4f ; correction (1/2)V'''(x0)s^2 = %.4f"
      % (x0**3 + 3 * x0 * s**2, x0**3, 0.5 * 6 * x0 * s**2))
# V = cos x : <V'> = -<sin x> = -sin(x0) exp(-s^2/2) vs V'(x0) = -sin(x0)
print("   V=cos x: <V'> = -sin(x0) e^{-s^2/2} = %.5f vs V'(<x>) = -sin(x0) = %.5f" %
      (-np.sin(x0) * np.exp(-s**2 / 2), -np.sin(x0)))
# Virial from Ehrenfest: d<xp>/dt = 2<T> - <x V'> (hbar=m=1) for the oscillator ground state
xg = np.linspace(-10, 10, 40001); psi0 = np.pi ** -0.25 * np.exp(-xg**2 / 2)
T_ = 0.5 * np.trapezoid(np.gradient(psi0, xg)**2, xg); xV = np.trapezoid(xg * xg * psi0**2, xg)
print("   ground state HO: 2<T> = %.5f, <x V'> = <x^2> = %.5f  (equal => d<xp>/dt = 0)" % (2 * T_, xV))
