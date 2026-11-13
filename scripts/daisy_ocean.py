"""Daisyworld with an Ocean (Joy's tutorial 2): bare-planet slab model (land, mixed layer, deep ocean) + daisies + grazers,
integrated from the equations on the app's 'How it works' page.

  C_L dT_L/dt = Q(1-A_L) - (a + b T_L) - k (T_L - T_m) + w
  C_m dT_m/dt = Q(1-A_o) - (a + b T_m) + k (1-f_o)/f_o (T_L - T_m) - gam_o (T_m - T_d) + w
  C_d dT_d/dt = gam_o (T_m - T_d)
  daisies:  da_i/dt = a_i (r beta(T_i) g - gamma) - G_i ;  grazers  dZ/dt = e (G_w + G_b) - m Z

  .venv/bin/python -I scripts/daisy_ocean.py bare     (Part-1 runs: bars, brightening)
  .venv/bin/python -I scripts/daisy_ocean.py life     (Part-2 runs: boom-bust cycle, ocean removed, depth)
"""
import math
import sys

import numpy as np
from scipy.signal import lfilter

DAY = 86400.0
YR = 365.25 * DAY
Q0 = 342.0
A_, B_ = 203.3, 2.09
CL, RHOC, CD = 1.0e7, 4.2e6, 4.2e9
K_EX, GAM_O, FO = 15.0, 0.7, 0.7
AW, AB, AG, AO = 0.50, 0.15, 0.32, 0.28


# ---------------------------------------------------------------- linear bare planet driven by AR(1) weather
def bare_matrix(H=75.0, deep=True, f_o=FO):
    Cm = RHOC * H
    go = GAM_O if deep else 0.0
    if f_o == 0:      # all land: no exchange, the ocean rows are inert
        return np.diag([-B_ / CL, -B_ / Cm, -1.0 / CD]), np.array([1.0 / CL, 0.0, 0.0])
    A = np.array([[-(B_ + K_EX) / CL, K_EX / CL, 0.0],
                  [K_EX * (1 - f_o) / f_o / Cm, -(B_ + K_EX * (1 - f_o) / f_o + go) / Cm, go / Cm],
                  [0.0, go / CD, -go / CD]])
    Bv = np.array([1.0 / CL, 1.0 / Cm, 0.0])
    return A, Bv


def weather_ar1(n_steps, dt_h, sigma_day=30.0, rng=None, seed=1):
    """hourly AR(1) push with retention 0.986/hour, scaled so that the *daily mean* has std sigma_day; sampled every dt_h hours.
    (built by simulating hourly and block-averaging over dt_h hours)"""
    rng = rng or np.random.default_rng(seed)
    phi = 0.986
    nh = n_steps * dt_h
    e = rng.standard_normal(nh)
    x = lfilter([1.0], [1.0, -phi], e)          # unit-innovation AR(1)
    # std of the 24-h mean of x (stationary): compute from the closed form by brute force on a long sample
    s24 = x[: (len(x) // 24) * 24].reshape(-1, 24).mean(1).std()
    x = x * (sigma_day / s24)
    return x.reshape(n_steps, dt_h).mean(1)       # W/m2 averaged over each step


def simulate_bare(years, H=75.0, deep=True, f_o=FO, dt_h=6, seed=1, sigma=30.0, extra_forcing=None):
    """returns monthly-mean temperature departures (K) for land, mixed layer, deep, planet; exact modal discretisation."""
    A, Bv = bare_matrix(H, deep, f_o)
    lam, V = np.linalg.eig(A)
    lam, V = lam.real, V.real
    Vi = np.linalg.inv(V)
    dt = dt_h * 3600.0
    n = int(years * YR / dt)
    w = weather_ar1(n, dt_h, sigma, seed=seed)
    if extra_forcing is not None:
        w = w + extra_forcing[:n]
    modes = []
    for k in range(3):
        bk = (Vi @ Bv)[k]
        if abs(lam[k]) < 1e-18:
            m = np.cumsum(w) * dt * bk
        else:
            e = math.exp(lam[k] * dt)
            m = lfilter([bk * (e - 1.0) / lam[k]], [1.0, -e], w)
        modes.append(m)
    X = V @ np.array(modes)
    TL, TM, TD = X
    per_month = int(round(YR / 12 / dt))
    nm = (len(TL) // per_month) * per_month
    mm = lambda x: x[:nm].reshape(-1, per_month).mean(1)
    TL, TM, TD = mm(TL), mm(TM), mm(TD)
    TP = TL if f_o == 0 else (1 - f_o) * TL + f_o * TM
    return TL, TM, TD, TP


def bars(x, blocks=(1, 12, 120, 1200)):
    out = []
    for b in blocks:
        m = (len(x) // b) * b
        out.append(x[:m].reshape(-1, b).mean(1).std())
    return out


def power_ratio(x1, x2, nseg=4):
    """crude spectra via Welch-like periodogram of monthly series; returns freq (cycles/yr), P1, P2"""
    n = (min(len(x1), len(x2)) // nseg) * nseg
    f = np.fft.rfftfreq(n // nseg, d=1.0 / 12.0)
    P1 = np.mean([abs(np.fft.rfft(s - s.mean())) ** 2 for s in x1[:n].reshape(nseg, -1)], 0)
    P2 = np.mean([abs(np.fft.rfft(s - s.mean())) ** 2 for s in x2[:n].reshape(nseg, -1)], 0)
    return f, P1, P2


def brighten(f_o=FO, H=75.0, deep=True, dL=0.05, L0=1.05, years=600, dt_h=24):
    """steady 5% brighter sun, no weather: share of final warming reached after 1, 10, 100, 500 yr (planet mean)"""
    A, Bv = bare_matrix(H, deep, f_o)
    dt = dt_h * 3600.0
    # forcing in each box: land gets Q dL (1-A_L) (A_L = bare .32), ocean gets Q dL (1-A_o)
    dFL = Q0 * dL * L0 / L0 * (1 - AG)   # d(Q L)(1-A)  with Q L0 = 342*1.05 -> change dL*342 ... see below
    dFL = Q0 * dL * (1 - AG) * 1.0
    dFm = Q0 * dL * (1 - AO) * 1.0
    # NOTE: 'the sun brightens by 5 %': Q -> 1.05 Q, i.e. dQ = 0.05 * Q0*L0 = 0.05*359.1
    dQ = dL * Q0   # 'the sun brightens by 5 %' = L from 1.05 to 1.10 (final warming 5.8 K as in the handout)
    f = np.array([dQ * (1 - AG) / CL, dQ * (1 - AO) / (RHOC * H), 0.0])
    lam, V = np.linalg.eig(A)
    Vi = np.linalg.inv(V)
    lam, V = lam.real, V.real
    out = {}
    tgrid = np.array([1, 10, 100, 500]) * YR
    # solution x(t) = V diag((e^{lam t}-1)/lam) Vi f   (x(0)=0)
    c = Vi @ f
    def xt(t):
        return V @ (np.where(abs(lam) > 1e-20, (np.exp(lam * t) - 1) / lam, t) * c)
    xinf = xt(1.0e5 * YR)
    Tp_inf = (1 - f_o) * xinf[0] + f_o * xinf[1]
    res = []
    for t in tgrid:
        x = xt(t)
        res.append(((1 - f_o) * x[0] + f_o * x[1]) / Tp_inf)
    return Tp_inf, res


# ---------------------------------------------------------------- nonlinear life model
class Life:
    def __init__(self, H=75.0, f_o=FO, deep=True, L=1.05, daisies=True, grazers=True, p=0.3, Tg=25.0, wg=6.0,
                 sigma=30.0, seed=1, T0=20.0):
        self.H, self.f_o, self.deep, self.L = H, f_o, deep, L
        self.daisies, self.grazers = daisies, grazers
        self.p, self.Tg, self.wg, self.sigma = p, Tg, wg, sigma
        self.rng = np.random.default_rng(seed)
        self.s = [T0, T0, T0, 0.3, 0.3, 0.05]   # TL, Tm, Td, aw, ab, Z

    def run(self, years, rec_every_days=7, dt_days=0.25, noise=True):
        H, f_o = self.H, self.f_o
        Cm = RHOC * H
        go = GAM_O if self.deep else 0.0
        has_ocean = f_o > 0
        Q = Q0 * self.L
        dt = dt_days * DAY
        n = int(years * 365.25 / dt_days)
        TL, Tm, Td, aw, ab, Z = self.s
        r, gam, q, Topt, wd = 0.1, 0.03, 20.0, 22.5, 17.5
        g0, K, e, m = 0.12, 0.08, 0.5, 0.015
        sw, sb = 2 * self.p, 2 * (1 - self.p)
        sig2 = 2 * self.sigma
        pushes = self.rng.standard_normal(n) * sig2 if (noise and self.sigma > 0) else np.zeros(n)
        rec = []
        every = int(rec_every_days / dt_days)
        floor_d, floor_z = 1e-4, 1e-5
        for i in range(n):
            gb = 1.0 - aw - ab
            AL = aw * AW + ab * AB + gb * AG if self.daisies else AG
            w = pushes[i]
            dTL = (Q * (1 - AL) - (A_ + B_ * TL) - (K_EX * (TL - Tm) if has_ocean else 0.0) + w) / CL
            if has_ocean:
                dTm = (Q * (1 - AO) - (A_ + B_ * Tm) + K_EX * (1 - f_o) / f_o * (TL - Tm) - go * (Tm - Td) + w) / Cm
                dTd = go * (Tm - Td) / CD
            if self.daisies:
                tw, tb = TL + q * (AL - AW), TL + q * (AL - AB)
                bw = 1 - ((tw - Topt) / wd) ** 2; bw = bw if bw > 0 else 0.0
                bb = 1 - ((tb - Topt) / wd) ** 2; bb = bb if bb > 0 else 0.0
                if self.grazers:
                    gmax = g0 * math.exp(-((TL - self.Tg) / self.wg) ** 2)
                    den = K + sw * aw + sb * ab
                    Gw, Gb = gmax * sw * aw * Z / den, gmax * sb * ab * Z / den
                else:
                    Gw = Gb = 0.0
                daw = aw * (r * bw * gb - gam) - Gw
                dab = ab * (r * bb * gb - gam) - Gb
                dZ = (e * (Gw + Gb) - m * Z) if self.grazers else 0.0
                aw = max(floor_d, aw + daw * dt_days); ab = max(floor_d, ab + dab * dt_days)
                if self.grazers:
                    Z = max(floor_z, Z + dZ * dt_days)
            TL += dTL * dt
            if has_ocean:
                Tm += dTm * dt; Td += dTd * dt
            if i % every == 0:
                rec.append((i * dt_days / 365.25, TL, Tm, Td, aw, ab, Z, AL))
        self.s = [TL, Tm, Td, aw, ab, Z]
        return np.array(rec)


def peaks(t, x, min_sep=2.0):
    idx = [i for i in range(1, len(x) - 1) if x[i] > x[i - 1] and x[i] >= x[i + 1]]
    out = []
    for i in idx:
        if out and t[i] - t[out[-1]] < min_sep:
            if x[i] > x[out[-1]]:
                out[-1] = i
        else:
            out.append(i)
    return out


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "bare"
    if mode == "bare":
        print("Part 1 spreads (K) of block means: 1 month / 1 yr / 10 yr / 100 yr  (handout: land 3.20-3.26 / 1.75-1.83 / .55-.67 / .14-.28; with mixed layer .74-.80 / .67-.74 / .45-.54 / .14-.26)")
        for seed in (1, 2, 3):
            TL, TM, TD, TP = simulate_bare(2000, seed=seed, f_o=0.0, deep=False)  # land only
            L1 = bars(TL)
            _, TM2, _, TP2 = simulate_bare(2000, seed=seed, f_o=FO, deep=False)
            print(" seed", seed, "land only", np.round(L1, 2), " planet w/ mixed layer", np.round(bars(TP2), 2))
        print("depth runs (planet bars 1yr/10yr/100yr; handout 25 m: 1.08-1.14/.51-.62/.14-.28; 75 m .67-.74/.45-.54/.14-.26; 150 m .48-.54/.37-.45/.13-.24)")
        for H in (25, 75, 150):
            b = np.mean([bars(simulate_bare(2000, H=H, seed=s, deep=False)[3])[1:] for s in (1, 2, 3, 4)], 0)
            print("  H=%d m" % H, np.round(b, 2))
        bd = np.mean([bars(simulate_bare(2000, H=75, seed=s, deep=True)[3])[1:] for s in (1, 2, 3, 4)], 0)
        bn = np.mean([bars(simulate_bare(2000, H=75, seed=s, deep=False)[3])[1:] for s in (1, 2, 3, 4)], 0)
        print("  with deep ocean", np.round(bd, 2), " without", np.round(bn, 2), "(handout: century bar 0.14-0.26 -> 0.12-0.22)")
        print("Run 6 brighten 5%% (handout with deep 35/80/87/98 %%; without 37/95/100/100 %%; final warming 5.8 K):")
        for deep in (True, False):
            Tinf, res = brighten(deep=deep)
            print("  deep", deep, "final planet warming %.2f K" % Tinf, np.round(100 * np.array(res)))
        TLs, TMs, _, _ = simulate_bare(5000, H=75, seed=1, deep=False)
        TLl, _, _, _ = simulate_bare(5000, H=75, seed=1, deep=False, f_o=0.0)
    if mode == "life":
        print("Preset 6: grazers, no weather (handout: ~8 yr cycle, grazers swing 24x (0.016..0.39), land 18-21 C)")
        mdl = Life(sigma=0.0)
        mdl.run(1500, rec_every_days=30, noise=False)     # hidden settle
        rec = mdl.run(120, rec_every_days=7, noise=False)
        t, TL, Tm, Z = rec[:, 0], rec[:, 1], rec[:, 2], rec[:, 6]
        pk = peaks(t, Z, 3.0)
        print("  grazer peaks (yr):", np.round(t[pk], 1)[:12], " intervals:", np.round(np.diff(t[pk]), 1)[:10])
        print("  grazers min %.3f max %.3f ratio %.0f ; land T range %.1f..%.1f" % (Z.min(), Z.max(), Z.max() / Z.min(), TL.min(), TL.max()))
        print("  white cover max %.2f ; black cover max %.2f" % (rec[:, 4].max(), rec[:, 5].max()))
