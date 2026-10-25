"""N-layer grey greenhouse model: solve the radiative balance exactly (linear system), compare with closed forms.

Set-up (planar, shortwave transparent, N isothermal layers each with longwave absorptivity = emissivity eps, numbered 1 = lowest ... N = highest):
  Q = S(1-alpha)/4 absorbed at the ground;  surface emits Es = sigma Ts^4;
  upward flux just above layer k :  U_k = (1-eps) U_{k-1} + eps E_k      (U_0 = Es)
  downward flux just below layer k: D_{k-1} = (1-eps) D_k + eps E_k      (D_N = 0)
  layer equilibrium (absorbed = emitted):   eps (U_{k-1} + D_k) = 2 eps E_k   with E_k = sigma T_k^4
  surface: Es = Q + D_0.            (TOA: U_N = Q follows from energy conservation.)
Closed forms checked below:
  N = 1:   Ts = Te (2/(2-eps))^(1/4)      N layers, eps = 1:   Ts = Te (N+1)^(1/4),   T_k = Te (N-k+1)^(1/4)... (counted from the top).
    usage:  .venv/bin/python scripts/cl08_layers.py
"""
import numpy as np

SIGMA = 5.670374419e-8


def te(S=1361.0, alpha=0.30):
    return (S * (1 - alpha) / (4 * SIGMA)) ** 0.25


def solve(N, eps, S=1361.0, alpha=0.30):
    """Return (Ts, [T_1..T_N], OLR).  Layer 1 is the lowest."""
    Q = S * (1 - alpha) / 4
    n = 3 * N + 1
    # unknown index map: Es:0 ; E_k:1..N ; U_k:N+1..2N (k=1..N) ; D_k:2N+1..3N (k=0..N-1)
    iE = lambda k: k                        # k = 0 is the surface Es
    iU = lambda k: N + k                    # k = 1..N
    iD = lambda k: 2 * N + 1 + k            # k = 0..N-1
    A = np.zeros((n, n))
    b = np.zeros(n)
    r = 0
    for k in range(1, N + 1):
        Uprev = (iE(0) if k == 1 else iU(k - 1))
        # U_k - (1-eps) U_{k-1} - eps E_k = 0
        A[r, iU(k)] = 1; A[r, Uprev] -= (1 - eps); A[r, iE(k)] -= eps; r += 1
        # D_{k-1} - (1-eps) D_k - eps E_k = 0   (D_N = 0)
        A[r, iD(k - 1)] = 1; A[r, iE(k)] -= eps
        if k < N:
            A[r, iD(k)] -= (1 - eps)
        r += 1
        # E_k = (U_{k-1} + D_k)/2
        A[r, iE(k)] = 1; A[r, Uprev] -= 0.5
        if k < N:
            A[r, iD(k)] -= 0.5
        r += 1
    # surface: Es - D_0 = Q
    A[r, iE(0)] = 1; A[r, iD(0)] = -1; b[r] = Q
    x = np.linalg.solve(A, b)
    Ts = (x[0] / SIGMA) ** 0.25
    T = [(x[k] / SIGMA) ** 0.25 for k in range(1, N + 1)]
    return Ts, T, x[iU(N)]


if __name__ == "__main__":
    T_e = te()
    print(f"Te = {T_e:.2f} K")
    print("N, eps=1:  Ts numeric / formula (N+1)^(1/4) Te ; top-layer T ; bottom-layer T")
    for N in (1, 2, 3, 5, 10, 20):
        Ts, T, olr = solve(N, 1.0)
        print(f"  N={N:2d}  Ts={Ts:7.2f}  formula={T_e*(N+1)**0.25:7.2f}  T_top={T[-1]:6.2f}  T_bot={T[0]:6.2f}  OLR={olr:6.1f}")
    print("N=1, various eps: Ts numeric / formula Te (2/(2-eps))^(1/4); Ta; formula Ts/2^(1/4)")
    for eps in (0.0, 0.15, 0.5, 0.78, 0.8, 1.0):
        Ts, T, olr = solve(1, eps)
        print(f"  eps={eps:4.2f}  Ts={Ts:7.2f}  formula={T_e*(2/(2-eps))**0.25:7.2f}  Ta={T[0]:6.2f} (Ts/2^.25={Ts/2**0.25:6.2f})  OLR={olr:6.1f}")
    print("N grey layers, eps each:")
    for eps in (0.5, 0.78):
        for N in (1, 2, 3, 5, 10):
            Ts, T, olr = solve(N, eps)
            print(f"  eps={eps}  N={N:2d}  Ts={Ts:7.2f}  T_bot={T[0]:6.2f} T_top={T[-1]:6.2f}")
    # eps needed for Ts = 288 and for Mars
    eps288 = 2 * (1 - (T_e / 288.0) ** 4)
    print(f"eps for Ts=288 K: {eps288:.3f};  Ta={288/2**0.25:.1f} K")
    for name, Tm, Tem in (("Mars", 214.0, 209.8), ("Venus", 737.0, 226.6)):
        print(f"  {name}: eps needed = {2*(1-(Tem/Tm)**4):.3f}  (Ts/Te)^4={(Tm/Tem)**4:.1f}")
    # greenhouse flux and forcing numbers
    Ts = 288.0
    G = SIGMA * Ts**4 - 238.2
    print(f"sigma Ts^4 = {SIGMA*Ts**4:.1f}, G = {G:.1f} W/m2 (sigma Ts^4 eps/2 with eps={eps288:.3f}: {SIGMA*Ts**4*eps288/2:.1f})")
    d_eps = 2 * 3.7 / (SIGMA * Ts**4)
    print(f"Delta eps for F=3.7 W/m2: {d_eps:.4f};  no-feedback dTs = {3.7/(4*SIGMA*Ts**3*(1-eps288/2)):.2f} K ; A_down = {eps288*SIGMA*(Ts/2**0.25)**4:.1f} W/m2")
    # dTs/deps
    print(f"dTs/deps = {Ts/(8*(1-eps288/2)):.1f} K per unit eps")
    # water vapour feedback illustration: tau_total = -ln(1-eps), WV share 50%, 7 %/K
    tau = -np.log(1 - eps288)
    for share in (0.3, 0.5):
        dtau_dT = 0.07 * share * tau
        deps_dT = (1 - eps288) * dtau_dT
        f = Ts / (8 * (1 - eps288 / 2)) * deps_dT
        print(f"  WV share {share}: tau={tau:.3f}, dtau/dT={dtau_dT:.4f}/K, deps/dT={deps_dT:.4f}/K, f_WV={f:.2f}")
