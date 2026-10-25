"""Grey-gas radiative(-convective) equilibrium column model used by the CL09 figures (not a figure script itself).

Physics (all standard; see CL09 sections 1 and 3):
  * all absorbed sunlight F_s = S(1-alpha)/4 is absorbed AT THE SURFACE (atmosphere transparent to shortwave);
  * longwave: grey absorber, two-stream with diffusivity factor D = 1.66, optical depth tau(p) = tau_s [f p* + (1-f) p*^4],
    p* = p/p_s (a well-mixed part plus a water-vapour-like part concentrated near the ground; Frierson et al. 2006 form);
  * layers equal in pressure, time-stepped to equilibrium; the ground has heat capacity C_g;
  * optional convective adjustment (Manabe-style): any pair of adjacent layers steeper than a critical lapse rate G_c is
    mixed to exactly G_c conserving enthalpy (the ground takes part as a thin 'layer' of enthalpy-mass C_g g / c_p).
"""
import numpy as np

G, CP, RD = 9.81, 1004.0, 287.0
SIG = 5.670374e-8
PS = 1.0e5
D = 1.66


def column(N=100, tau_s=2.5, f=0.2):
    p_if = np.linspace(0.0, PS, N + 1)                 # interfaces, top -> bottom
    dp = np.diff(p_if)
    ps_ = p_if / PS
    tau_if = tau_s * (f * ps_ + (1 - f) * ps_**4)
    return p_if, dp, tau_if


def fluxes(T, Tg, tau_if):
    """Upward/downward LW flux at the N+1 interfaces (vectorised cumulative solution of the two-stream recurrences)."""
    dtau = np.diff(tau_if)
    t = np.exp(-D * dtau)
    src = SIG * T**4 * (1 - t)
    N = len(T)
    P = np.cumprod(t)                                   # P[n] = prod_{i<=n} t_i
    Fd = np.zeros(N + 1)
    Fd[1:] = P * np.cumsum(src / P)                    # F_d[n+1] = sum_{j<=n} src_j prod_{i=j+1..n} t_i
    tr = t[::-1]                                        # work from the bottom upward
    src_r = src[::-1]
    Pr = np.cumprod(tr)
    Fu = np.zeros(N + 1)
    Fu[N] = SIG * Tg**4
    Fu[:N] = (Pr * Fu[N] + Pr * np.cumsum(src_r / Pr))[::-1]
    return Fu, Fd


def adjust(T, Tg, p_if, dp, Gc, Cg):
    """Convective adjustment sweep(s) to critical lapse rate Gc (K/m); modifies T, Tg in place; returns Tg."""
    xi = RD * Gc / G
    pm = 0.5 * (p_if[:-1] + p_if[1:])
    N = len(T)
    dpg = Cg * G / CP                                  # enthalpy-mass of the ground slab [Pa]
    for _ in range(200):
        changed = False
        for k in range(N - 1):                         # upper k, lower k+1
            r = (pm[k + 1] / pm[k]) ** xi
            if T[k + 1] > r * T[k] * (1 + 1e-12):
                Tk = (dp[k] * T[k] + dp[k + 1] * T[k + 1]) / (dp[k] + dp[k + 1] * r)
                T[k], T[k + 1] = Tk, r * Tk
                changed = True
        r = (PS / pm[-1]) ** xi                        # ground vs lowest layer
        if Tg > r * T[-1] * (1 + 1e-12):
            Tl = (dp[-1] * T[-1] + dpg * Tg) / (dp[-1] + dpg * r)
            T[-1], Tg = Tl, r * Tl
            changed = True
        if not changed:
            break
    return Tg


def run(Fs=238.2, tau_s=2.5, f=0.2, N=80, Gc=None, Cg=1.0e6, dt=14400.0, nmax=6000, tol=1e-5, T0=250.0, verbose=False):
    p_if, dp, tau_if = column(N, tau_s, f)
    T = np.full(N, T0)
    Tg = T0 + 10
    for n in range(nmax):
        Fu, Fd = fluxes(T, Tg, tau_if)
        Fn = Fu - Fd
        dT = (G / CP) * (Fn[1:] - Fn[:-1]) / dp * dt
        dTg = (Fs - Fn[-1]) / Cg * dt
        T = T + dT
        Tg = Tg + dTg
        if Gc is not None:
            Tg = adjust(T, Tg, p_if, dp, Gc, Cg)
        if max(np.max(np.abs(dT)), abs(dTg)) < tol and n > 500:
            break
    Fu, Fd = fluxes(T, Tg, tau_if)
    # heights by integrating the hypsometric equation upward from the ground
    z_mid = np.zeros(N)
    z = 0.0
    p_below = PS
    for k in range(N - 1, -1, -1):
        dz = RD * T[k] / G * np.log(p_below / p_if[k]) if False else RD * T[k] / G * np.log(p_if[k + 1] / p_if[k])
        z_mid[k] = z + 0.5 * dz
        z += dz
    pm = 0.5 * (p_if[:-1] + p_if[1:])
    return dict(T=T, Tg=Tg, z=z_mid, p=pm, p_if=p_if, Fu=Fu, Fd=Fd, steps=n, tau_if=tau_if)


def lapse(res):
    T, z = res["T"], res["z"]
    return -np.gradient(T, z)          # K/m, top->bottom ordering (z decreasing): gradient handles it


if __name__ == "__main__":
    Fs = 238.2
    Te = (Fs / SIG) ** 0.25
    print(f"Te={Te:.2f} K  skin T = Te/2^(1/4) = {Te/2**0.25:.1f} K")
    for tau_s in (1.0, 2.5):
        re = run(Fs, tau_s=tau_s)
        Tair = re["T"][-1]
        analytic = Te * (1 + D * tau_s / 2) ** 0.25
        print(f"tau_s={tau_s}: RE  Tg={re['Tg']:.1f} K (analytic {analytic:.1f}) lowest-layer T={Tair:.1f} jump={re['Tg']-Tair:.1f} K"
              f"  sigma(Tg^4-Ta^4)={SIG*(re['Tg']**4-Tair**4):.1f} (F/2={Fs/2:.1f}) steps={re['steps']}")
        for Gc in (9.8e-3, 6.5e-3):
            rc = run(Fs, tau_s=tau_s, Gc=Gc)
            L = lapse(rc)
            conv = rc["p"][L > 0.97 * Gc * 1.0 - 1e-9]
            print(f"   RCE Gc={Gc*1e3:.1f}: Tg={rc['Tg']:.1f}  T(lowest)={rc['T'][-1]:.1f} steps={rc['steps']}  OLR={rc['Fu'][0]:.1f}")


def run_cached(name, **kw):
    """run() with an on-disk cache in scripts/__pycache__ (git-ignored) so figure scripts re-run quickly."""
    import hashlib
    import os
    key = hashlib.md5(repr(sorted(kw.items())).encode()).hexdigest()[:10]
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "__pycache__", f"cl09_{name}_{key}.npz")
    if os.path.exists(path):
        d = np.load(path, allow_pickle=True)
        return {k: (d[k].item() if d[k].shape == () else d[k]) for k in d.files}
    res = run(**kw)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    np.savez(path, **res)
    return res
