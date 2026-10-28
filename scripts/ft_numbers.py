"""Checks and numbers for 09-Foundations/Fourier and Laplace Transforms.md.   .venv/bin/python -W ignore scripts/ft_numbers.py
Convention (same as the QM notes): F(k) = (1/sqrt(2 pi)) int f(x) e^{-ikx} dx,  f(x) = (1/sqrt(2 pi)) int F(k) e^{ikx} dk."""
import math
import numpy as np
from scipy import integrate, signal, special
import sympy as sp

def FT(f, k, lim=60):
    re = integrate.quad(lambda x: f(x) * math.cos(k * x), -lim, lim, limit=400)[0]
    im = -integrate.quad(lambda x: f(x) * math.sin(k * x), -lim, lim, limit=400)[0]
    return (re + 1j * im) / math.sqrt(2 * math.pi)

if __name__ == "__main__":
    print("== 1. Fourier series: square wave +-1, b_n = 4/(n pi) for odd n ==")
    x = np.linspace(0, math.pi, 200001)
    for N in (1, 3, 10, 50, 200):          # N odd harmonics 1,3,...,2N-1
        S = sum(4 / (math.pi * n) * np.sin(n * x) for n in range(1, 2 * N, 2))
        print(f"  N={N:3d} terms: max = {S.max():.5f} at x/pi = {x[S.argmax()]/math.pi:.5f} (pi/2N = {1/(2*N):.5f}); overshoot of the full jump 2: {100*(S.max()-1)/2:.3f} %")
    print("  limit (2/pi) Si(pi) =", 2 / math.pi * special.sici(math.pi)[0], " -> overshoot", 100 * (2 / math.pi * special.sici(math.pi)[0] - 1) / 2, "% of the jump")
    print("== 2. Parseval and Basel ==")
    print("  square wave: mean square = 1;  sum b_n^2/2 =", sum((4/(math.pi*n))**2/2 for n in range(1, 200001, 2)))
    print("  sawtooth f=x on (-pi,pi): b_n = 2(-1)^(n+1)/n; (1/pi)int f^2 = 2pi^2/3 =", 2*math.pi**2/3, " sum b_n^2 =", sum((2/n)**2 for n in range(1, 400001)), "; zeta(2) =", math.pi**2/6, "partial", sum(1/n**2 for n in range(1, 400001)))
    print("== 3. transform pairs (unitary convention), numerical vs closed form at k=0.7, 1.9 ==")
    a = 1.3; s = 0.8
    pairs = {
      "gauss exp(-x^2/2s^2) -> s exp(-s^2k^2/2)": (lambda x: math.exp(-x*x/(2*s*s)), lambda k: s*math.exp(-s*s*k*k/2)),
      "rect |x|<a -> sqrt(2/pi) sin(ka)/k": (lambda x: 1.0 if abs(x) < a else 0.0, lambda k: math.sqrt(2/math.pi)*math.sin(k*a)/k),
      "exp(-a|x|) -> sqrt(2/pi) a/(a^2+k^2)": (lambda x: math.exp(-a*abs(x)), lambda k: math.sqrt(2/math.pi)*a/(a*a+k*k)),
      "1/(x^2+a^2) -> sqrt(pi/2) exp(-a|k|)/a": (lambda x: 1/(x*x+a*a), lambda k: math.sqrt(math.pi/2)*math.exp(-a*abs(k))/a),
      "triangle (1-|x|/a)_+ -> a/sqrt(2pi) sinc^2(ka/2)": (lambda x: max(0.0, 1-abs(x)/a), lambda k: a/math.sqrt(2*math.pi)*(math.sin(k*a/2)/(k*a/2))**2),
    }
    for nm, (f, F) in pairs.items():
        lim = 400 if "1/(x^2" in nm else 40
        for k in (0.7, 1.9):
            n = FT(f, k, lim); print(f"  {nm:55s} k={k}: numeric {n.real:+.6f}{n.imag:+.1e}j  closed {F(k):+.6f}")
    print("== 4. uncertainty: Delta x Delta k (standard deviations of |f|^2 and |F|^2) ==")
    def prod(f, F, Lx=60, Lk=60):
        q = lambda g, L: integrate.quad(g, -L, L, limit=2000, points=[0])[0]
        n1 = q(lambda x: abs(f(x))**2, Lx); v1 = q(lambda x: x*x*abs(f(x))**2, Lx)/n1
        n2 = q(lambda k: abs(F(k))**2, Lk); v2 = q(lambda k: k*k*abs(F(k))**2, Lk)/n2
        return round(math.sqrt(v1), 5), round(math.sqrt(v2), 5), round(math.sqrt(v1*v2), 5)
    print("  gaussian s=0.8:", prod(lambda x: math.exp(-x*x/(2*.64)), lambda k: .8*math.exp(-.64*k*k/2)))
    print("  exp(-|x|):", prod(lambda x: math.exp(-abs(x)), lambda k: math.sqrt(2/math.pi)/(1+k*k), 40, 20000), " analytic 1/sqrt2 =", 1/math.sqrt(2))
    sinc = lambda u: math.sin(u)/u if u else 1.0
    print("  triangle a=1:", prod(lambda x: max(0, 1-abs(x)), lambda k: sinc(k/2)**2/math.sqrt(2*math.pi), 1.5, 3000))
    print("  sech(x):", prod(lambda x: 1/math.cosh(x), lambda k: math.sqrt(math.pi/2)/math.cosh(math.pi*k/2), 40, 40))
    print("== 5. aliasing and DEM ==")
    fs = 10.0; t = np.arange(0, 2, 1/fs); y = np.sin(2*math.pi*9*t); Y = np.abs(np.fft.rfft(y)); fr = np.fft.rfftfreq(len(t), 1/fs)
    print("  9 Hz sampled at 10 Hz: spectral peak at", fr[Y.argmax()], "Hz")
    print("  DEM 30 m: wavelength 40 m appears as 1/(1/30-1/40) =", 1/(1/30-1/40), "m; Nyquist wavelength 2*Delta = 60 m")
    print("== 6. DFT / FFT ==")
    N = 8; n = np.arange(N); Fm = np.exp(-2j*np.pi*np.outer(n, n)/N)
    v = np.random.default_rng(1).normal(size=N); print("  DFT matrix vs FFT max diff:", np.abs(Fm@v - np.fft.fft(v)).max(), "; F F^dagger = N I:", np.allclose(Fm@Fm.conj().T, N*np.eye(N)))
    u = np.random.default_rng(2).normal(size=N); cyc = np.array([sum(v[j]*u[(m-j) % N] for j in range(N)) for m in range(N)])
    print("  cyclic convolution = IFFT(FFT*FFT):", np.allclose(cyc, np.fft.ifft(np.fft.fft(v)*np.fft.fft(u)).real))
    for NN in (2**10, 2**20):
        print(f"  N={NN}: N^2 = {NN**2:.2e}, N log2 N = {NN*math.log2(NN):.2e}, speed-up {NN**2/(NN*math.log2(NN)):.0f}")
    M = 4096; k = np.arange(M)
    for nm, w in (("rectangular", np.ones(M)), ("Hann", np.hanning(M))):
        W = np.abs(np.fft.rfft(w, 64*M)); W /= W.max(); dB = 20*np.log10(W+1e-16)
        i = np.argmax(dB < -3); first_null = np.argmax(np.diff(dB) > 0); side = dB[first_null:first_null+4000].max()
        print(f"  {nm}: highest sidelobe {side:.1f} dB")
    print("== 7. diffusion by Fourier modes ==")
    D = 0.01; lam = 100.0; kk = 2*math.pi/lam
    print(f"  sinusoid wavelength {lam} m, D={D} m2/yr: decay time 1/(D k^2) = {1/(D*kk**2):.0f} yr")
    for lam in (10, 50, 100, 1000): print(f"    lambda={lam}: tau = {lam**2/(4*math.pi**2*D):.3g} yr")
    Lg = 2000; xg = np.linspace(-Lg/2, Lg/2, 4096, endpoint=False); dx = xg[1]-xg[0]; s0 = 5.0; t = 1e4
    f0 = np.exp(-xg**2/(2*s0**2)); kx = 2*np.pi*np.fft.fftfreq(len(xg), dx); ft = np.fft.ifft(np.fft.fft(f0)*np.exp(-D*kx**2*t)).real
    s_t = math.sqrt(s0**2 + 2*D*t); an = s0/s_t*np.exp(-xg**2/(2*s_t**2)); print(f"  Gaussian s0=5 m, t=1e4 yr: width {s_t:.2f} m; spectral vs analytic max diff {np.abs(ft-an).max():.2e}")
    print("== 8. dispersion ==")
    g = 9.81
    for lam in (1, 10, 100): kq = 2*math.pi/lam; print(f"  deep-water wave lambda={lam} m: c = {math.sqrt(g/kq):.2f} m/s, c_g = {math.sqrt(g/kq)/2:.2f} m/s, period {2*math.pi/math.sqrt(g*kq):.2f} s")
    hbar = 1.054571817e-34; me = 9.1093837e-31; s0 = 1e-9
    tau_s = 2*me*s0**2/hbar; print(f"  free electron packet sigma0=1 nm: spreading time 2 m s0^2/hbar = {tau_s:.2e} s; width doubles at t = {math.sqrt(3)*tau_s:.2e} s")
    print("== 9. Poisson summation / theta function: sum exp(-pi n^2 t) = t^-1/2 sum exp(-pi n^2/t) ==")
    th = lambda t: sum(math.exp(-math.pi*n*n*t) for n in range(-60, 61)); t0 = 0.7
    print(" ", th(t0), t0**-0.5*th(1/t0))
    print("== 10. Laplace: sympy table check ==")
    t_, s_ = sp.symbols("t s", positive=True); a_, w_ = sp.symbols("a omega", positive=True)
    for nm, f in [("1", sp.Integer(1)), ("t", t_), ("t^3", t_**3), ("exp(-a t)", sp.exp(-a_*t_)), ("sin(w t)", sp.sin(w_*t_)), ("cos(w t)", sp.cos(w_*t_)),
                  ("exp(-a t) sin(w t)", sp.exp(-a_*t_)*sp.sin(w_*t_)), ("t exp(-a t)", t_*sp.exp(-a_*t_)), ("sinh(w t)", sp.sinh(w_*t_))]:
        print(f"  L[{nm}] = {sp.simplify(sp.laplace_transform(f, t_, s_, noconds=True))}")
    print("  L[1/sqrt(pi t)] =", sp.laplace_transform(1/sp.sqrt(sp.pi*t_), t_, s_, noconds=True))
    print("== 11. second-order system x'' + 2 zeta w0 x' + w0^2 x = w0^2 u(t): overshoot exp(-pi zeta/sqrt(1-zeta^2)) ==")
    for z in (0.1, 0.2, 0.5, 0.707, 1.0, 2.0):
        sys = signal.TransferFunction([1], [1, 2*z, 1]); tt, yy = signal.step(sys, T=np.linspace(0, 40, 20001))
        th_ = math.exp(-math.pi*z/math.sqrt(1-z*z)) if z < 1 else 0
        print(f"  zeta={z}: max step response {yy.max():.4f}  (theory {1+th_:.4f}); poles {np.round(np.roots([1, 2*z, 1]), 3)}")
    print("== 12. relaxation filter H(s) = 1/(1+tau s) at s = i w: |H| = 1/sqrt(1+w^2 tau^2) (LS01) ==")
    tau, T = 1e6, 4.1e4; w = 2*math.pi/T; print(f"  tau=1e6 yr, T=41 kyr: |H| = {1/math.sqrt(1+(w*tau)**2):.4f}, phase lag = {math.degrees(math.atan(w*tau)):.1f} deg")
    print("== 13. MGF = two-sided Laplace transform at -t: exponential(lambda): lambda/(lambda - t); Laplace lambda/(lambda + s) ==")
    lam = 2.0; ss = 1.3; print(" ", integrate.quad(lambda x: lam*math.exp(-lam*x)*math.exp(-ss*x), 0, 80)[0], lam/(lam+ss))
    print("== 14. numerical Bromwich inversion (mpmath, talbot) of F(s)=1/(s^2+s+1) at t=2 ==")
    import mpmath as mp
    F = lambda s: 1/(s*s+s+1); tt = 2.0
    print("  numeric:", mp.invertlaplace(F, tt, method="talbot"), " exact:", 2/mp.sqrt(3)*mp.e**(-tt/2)*mp.sin(mp.sqrt(3)/2*tt))
    print("== 15. CLT via characteristic functions: X uniform with variance 1 (phi = sin(sqrt3 t)/(sqrt3 t)), n=10, t=1 ==")
    n = 10; t = 1.0; phi = lambda u: math.sin(math.sqrt(3)*u)/(math.sqrt(3)*u)
    print(f"  phi(t/sqrt n)^n = {phi(t/math.sqrt(n))**n:.5f}, exp(-t^2/2) = {math.exp(-t*t/2):.5f}")
    print("== 16. sum of two U(0,1): density is the convolution = triangle; FT is sinc^2 product ==")
    d = 0.001; u = np.ones(int(1/d)); c = np.convolve(u, u)*d; print("  max of convolution (should be 1):", c.max(), " integral:", c.sum()*d)
    print("== 17. Heaviside / final value: L[x'']... example: F(s)=1/(s(s+2)) f(inf)=1/2 ==", sp.limit(s_*(1/(s_*(s_+2))), s_, 0))
    print("== 18. flexure as a low-pass filter: w~(k) = q~(k)/(D k^4 + drho g); response = 1/(1 + D k^4/(drho g)) ==")
    Dflex = 1e23; drg = 3300 * 9.81
    kc = (drg / Dflex) ** 0.25; print(f"  D=1e23 N m, drho g = {drg:.3g}: k_c = {kc:.3e} 1/m, half-compensation wavelength 2 pi/k_c = {2*math.pi/kc/1e3:.0f} km; alpha=(4D/drho g)^(1/4) = {(4*Dflex/drg)**0.25/1e3:.1f} km")
    for lam in (50, 100, 200, 470, 1000, 3000):
        k = 2*math.pi/(lam*1e3); print(f"    wavelength {lam} km: response {1/(1+Dflex*k**4/drg):.3f}")
    print("== 19. upward continuation: anomaly of wavelength lam from depth z is attenuated by exp(-2 pi z/lam) ==")
    for lam, z in [(10, 2), (10, 5), (100, 2), (1, 2)]: print(f"  lam={lam} km, z={z} km: {math.exp(-2*math.pi*z/lam):.4f}")
    print("== 20. critical slowing down: pole s = -(1 - r) -> relaxation time 1/(1-r) ==")
    for r in (0.0, 0.5, 0.9, 0.99): print(f"  distance to bifurcation 1-r={1-r:.2f}: tau = {1/(1-r):.1f} (units of the intrinsic time)")
