"""Daisyworld, land and ocean (Joy's tutorial 1): the model of the handout 'The model in full', integrated numerically.

    A = f(a_w A_w + a_b A_b + x A_g) + (1-f) A_o ;  C dT/dt = S L (1-A) - sigma T^4 ;  C = f C_land + (1-f) rho c h
    T_w = T + q'(A-A_w), T_b = T + q'(A-A_b) ;  beta(T) = 1 - 0.003265 (22.5-T)^2 (0 outside 5..40 C)
    da_i/dt = a_i [x beta(T_i) - gamma], x = 1 - a_w - a_b ;  daisy cover floor 1 % of the land (seeds)

Run:  .venv/bin/python -I scripts/daisy_land_ocean.py       (prints the handout's quoted numbers next to the model's)
"""
import math

SIG = 5.670374e-8
S0 = 917.0
AW, AB, AG, AO = 0.75, 0.25, 0.5, 0.10
GAM, QP = 0.3, 20.0
CLAND, RHOC = 1.0e7, 4.1e6
YR = 365.25 * 86400.0


def beta(t):
    if t < 5.0 or t > 40.0:
        return 0.0
    return 1.0 - 0.003265 * (22.5 - t) ** 2


def heatcap(f, h):
    return f * CLAND + (1 - f) * RHOC * h


def albedo(f, aw, ab, ao=AO):
    x = 1.0 - aw - ab
    return f * (aw * AW + ab * AB + x * AG) + (1 - f) * ao


def tbal(L, A):  # equilibrium temperature (C) of the bare/ daisy-free balance
    return (S0 * L * (1 - A) / SIG) ** 0.25 - 273.15


def step(T, aw, ab, L, f, C, dt, daisies=True, ao=AO):
    """one explicit-Euler step of length dt (seconds). T in C. returns T, aw, ab, A"""
    A = albedo(f, aw, ab, ao) if daisies else f * AG + (1 - f) * ao
    Tk = T + 273.15
    dT = (S0 * L * (1 - A) - SIG * Tk ** 4) / C
    if daisies and f > 0:
        x = 1.0 - aw - ab
        tw, tb = T + QP * (A - AW), T + QP * (A - AB)
        dy = dt / YR
        aw = max(0.01, aw + dy * aw * (x * beta(tw) - GAM))
        ab = max(0.01, ab + dy * ab * (x * beta(tb) - GAM))
    return T + dT * dt, aw, ab, A


def sweep(f=1.0, h=50.0, ao=AO, L0=0.4, L1=1.8, years=600.0, dt_days=0.5, daisies=True, down=False):
    """slow brightening (and optionally dimming back). returns list of (L, T_daisy, T_bare, aw, ab)"""
    C = heatcap(f, h)
    dt = dt_days * 86400.0
    n_up = int(years * 365.25 / dt_days)
    T = tbal(L0, f * AG + (1 - f) * ao)
    Tb = T
    aw = ab = 0.01
    out = []
    n_tot = n_up * (2 if down else 1)
    for k in range(n_tot):
        frac = k / n_up if k < n_up else 2 - k / n_up
        L = L0 + (L1 - L0) * frac
        T, aw, ab, A = step(T, aw, ab, L, f, C, dt, True, ao)
        Tb, _, _, _ = step(Tb, 0, 0, L, f, C, dt, False, ao)
        if k % int(30 / dt_days) == 0:
            out.append((L, T, Tb, aw, ab, k < n_up))
    return out


def settle(L, f=1.0, h=50.0, ao=AO, years=300, dt_days=0.5, state=None, daisies=True):
    C = heatcap(f, h)
    dt = dt_days * 86400.0
    T = 20.0 if state is None else state[0]
    aw, ab = (0.01, 0.01) if state is None else state[1:3]
    for _ in range(int(years * 365.25 / dt_days)):
        T, aw, ab, A = step(T, aw, ab, L, f, C, dt, daisies, ao)
    return T, aw, ab


def sudden(f=1.0, h=50.0, ao=AO, L0=0.78, L1=0.86, years=40.0, dt_days=0.25):
    """settle at L0 (daisies+twin), jump to L1; return time series (t_yr, T_daisy, T_bare, aw, ab)"""
    C = heatcap(f, h)
    dt = dt_days * 86400.0
    st = settle(L0, f, h, ao, years=max(400, 8 * C / 5.4 / YR * 20), dt_days=max(dt_days, 0.5))
    bare = settle(L0, f, h, ao, years=max(100, 40 * C / 5.4 / YR), dt_days=max(dt_days, 0.5), daisies=False)
    T, aw, ab = st
    Tb = bare[0]
    ser = [(0.0, T, Tb, aw, ab)]
    n = int(years * 365.25 / dt_days)
    for k in range(1, n + 1):
        T, aw, ab, A = step(T, aw, ab, L1, f, C, dt, True, ao)
        Tb, _, _, _ = step(Tb, 0, 0, L1, f, C, dt, False, ao)
        if k % 4 == 0:
            ser.append((k * dt_days / 365.25, T, Tb, aw, ab))
    return (st, bare), ser


def window(out, lo=17.5, hi=27.5, col=1, up_only=True):
    ls = [r[0] for r in out if (r[5] or not up_only) and lo <= r[col] <= hi]
    return (min(ls), max(ls)) if ls else (None, None)


def survive(out):
    ls = [r[0] for r in out if r[5] and r[3] + r[4] > 0.0201]  # above the 1 % floors
    return (min(ls), max(ls)) if ls else (None, None)


if __name__ == "__main__":
    import sys
    print("Run 1: all land, slow brightening (handout: daisies 0.75-1.59, planet within 5 C 0.76-1.52, bare 0.88-1.01)")
    o = sweep(1.0)
    print("  daisies survive", survive(o), "planet within5C", window(o), "bare within5C", window(o, col=2))
    for L0 in (0.95, 1.33):
        r = min(o, key=lambda r: abs(r[0] - L0)); print("  L=%.2f daisy T %.1f bare %.1f" % (r[0], r[1], r[2]))
    r = min(o, key=lambda r: abs(r[0] - 1.47)); print("  L=1.47: white %.0f%% of land, T %.1f, bare planet %.1f (handout 69 %%, 24.3, 56.8)" % (100 * r[3], r[1], r[2]))
    sys.stdout.flush()
    print("Run 2/3: ocean planets (handout daisies survive 30%: .63-1.15 70%: .52-.89; planet within5C 30%: .64-1.01, 70%: .55-.61)")
    for f in (0.7, 0.3):
        o = sweep(f)
        print("  ocean %.0f%%: survive %s window %s bare %s" % (100 * (1 - f), survive(o), window(o), window(o, col=2)))
    sys.stdout.flush()
    print("Run 3: bright ocean A_o=0.5 (handout survive 30%: .75-1.44, 70%: .75-1.30; window .77-1.32 / .80-1.13)")
    for f in (0.7, 0.3):
        o = sweep(f, ao=0.5)
        print("  ocean %.0f%%: survive %s window %s" % (100 * (1 - f), survive(o), window(o)))
    sys.stdout.flush()
    print("Run 5: brighten then dim, 300 yr up/300 down (handout dies/returns: all land 1.63/1.17; 30% 1.18/0.97; 70% 0.91/0.80)")
    for f in (1.0, 0.7, 0.3):
        o = sweep(f, years=300, down=True)
        up = [r for r in o if r[5]]; dn = [r for r in o if not r[5]]
        # die point: first L (going up) after peak where daisies < 0.0201 ; return: first L going down where daisies > 0.05
        pk = max(range(len(up)), key=lambda i: up[i][3] + up[i][4])
        die = next((up[i][0] for i in range(pk, len(up)) if up[i][3] + up[i][4] < 0.0201), None)
        back = next((r[0] for r in dn if r[3] + r[4] > 0.05 and r[0] < up[pk][0]), None)
        print("  ocean %.0f%%: dies %s returns %s" % (100 * (1 - f), die and round(die, 2), back and round(back, 2)))
    sys.stdout.flush()


def hysteresis_points(f, years_up):
    """die / return points defined by the daisy planet leaving / rejoining the bare line (|dT| > 0.5 C)."""
    o = sweep(f, years=years_up, down=True)
    up = [r for r in o if r[5]]; dn = [r for r in o if not r[5]]
    pk = max(range(len(up)), key=lambda i: up[i][3] + up[i][4])
    die = next((up[i][0] for i in range(pk, len(up)) if up[i][1] - up[i][2] < 0.5), None)
    ret = next((r[0] for r in dn if r[1] - r[2] < -0.5 and r[0] < up[pk][0]), None)
    return die, ret, o


def tau_two_thirds(ser, col=2):
    """time (days) for the bare-planet series to cover 2/3 of its total change"""
    T0, T1 = ser[0][col], ser[-1][col]
    for r in ser:
        if (r[col] - T0) >= 2.0 / 3.0 * (T1 - T0):
            return r[0] * 365.25
    return None


def run_sudden(label, f, h=50.0, L0=0.78, L1=0.86, years=40.0, ao=AO):
    (st, bare), ser = sudden(f, h, ao, L0, L1, years)
    T0d, T0b = ser[0][1], ser[0][2]
    pk = max(ser, key=lambda r: r[1])
    print("%-34s before: daisy %.1f bare %.1f (black %.0f%%, white %.0f%%) | bare +%.1f C, 2/3 in %.0f d | daisy peak +%.1f C at %.2f yr, end %+.1f C"
          % (label, T0d, T0b, 100 * st[2], 100 * st[1], ser[-1][2] - T0b, tau_two_thirds(ser), pk[1] - T0d, pk[0], ser[-1][1] - T0d))
    return ser


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "part2":
    print("Run 5 (refined): handout dies/returns all land 1.63/1.17; 30% 1.18/0.97; 70% 0.91/0.80")
    for f in (1.0, 0.7, 0.3):
        d, r, _ = hysteresis_points(f, 300)
        print("  ocean %.0f%%: dies %s returns %s" % (100 * (1 - f), d and round(d, 2), r and round(r, 2)))
    print("Run 6-9 (handout: all land bare +7.0, 22 d; daisy peak +7, end -1.4 after ~18 y | 30%%/50 m: bare +7.3, 127 d; peak +6.5 at ~1 y, end -1.3 | 70%%: bare +7.8, ~8 mo; end +12.9 to 49.6)")
    for lab, f, h in [("all land", 1.0, 50), ("30% ocean 50 m", 0.7, 50), ("30% ocean 200 m", 0.7, 200), ("30% ocean 500 m", 0.7, 500)]:
        run_sudden(lab, f, h)
    run_sudden("70% ocean 50 m", 0.3, 50)
    run_sudden("70% ocean 200 m", 0.3, 200)
    print("   gentle change 0.58 -> 0.62, 70% ocean (handout: daisy +4.8 = bare +4.9)")
    run_sudden("70% ocean, 0.58->0.62", 0.3, 50, 0.58, 0.62)
    print("heat store / tau table (handout: x1.0 21 d; 1.9 41 d; 6.8 146 d; 25 1.5 y; 62 3.6 y; 15 0.85 y; 58 3.4 y)")
    lam = 4 * SIG * (273.15 + 20) ** 3
    print("  lambda=4 sigma T^3 at 20 C = %.2f" % lam)
    for lab, f, h in [("all land", 1.0, 50), ("30%, 10 m", .7, 10), ("30%, 50 m", .7, 50), ("30%, 200 m", .7, 200), ("30%, 500 m", .7, 500), ("70%, 50 m", .3, 50), ("70%, 200 m", .3, 200)]:
        C = heatcap(f, h)
        print("  %-12s C/Cland %.1f tau %.2f d = %.2f yr" % (lab, C / CLAND, C / lam / 86400, C / lam / YR))
    print("Run 10: fast brighten+dim over 30 yr (15 up/15 down) (handout lag up to: land 1.3 C; 30%/50 m 6.2; 30%/300 m 21; daisies alive up: .95-1.44, .86-1.16, 1.02-1.28; return .96/.75/.63)")
    for lab, f, h in [("all land", 1.0, 50), ("30% 50 m", .7, 50), ("30% 300 m", .7, 300)]:
        o = sweep(f, h, years=15, down=True, dt_days=0.25)
        up = [r for r in o if r[5]]; dn = [r for r in o if not r[5]]
        # bare lag = bare T vs its balance temperature at that L
        C = heatcap(f, h)
        lag = max(abs(r[2] - tbal(r[0], f * AG + (1 - f) * AO)) for r in o)
        d, r_, _ = (None, None, None)
        pk = max(range(len(up)), key=lambda i: up[i][3] + up[i][4])
        alive_lo = next((r[0] for r in up if r[3] + r[4] > 0.0201), None)
        print("  %-9s bare lag max %.1f C ; daisies first >2%% at L=%s ; peak daisies at L=%.2f" % (lab, lag, alive_lo and round(alive_lo, 2), up[pk][0]))
