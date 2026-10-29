"""Figures for LS21-LS24 (rivers, bedrock channels, sediment transport).  Numbers: scripts/ls_rivers_numbers.py.
    .venv/bin/python -W ignore scripts/fig_ls_rivers.py
Writes Assets/figures/fig_ls21_flow.png, fig_ls21_hydgeo.png, fig_ls22_floods.png, fig_ls22_profiles.png,
fig_ls23_incision.png, fig_ls23_transient.png, fig_ls24_threshold.png, fig_ls24_suspension.png.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
from scipy import special, stats  # noqa

G, RHO, RHO_S, NU, KAPPA = 9.81, 1000.0, 2650.0, 1e-6, 0.4
S_REL = RHO_S / RHO
YR = 365.25 * 86400


def brownlie(Rep):
    return 0.22 * Rep ** -0.6 + 0.06 * np.exp(-17.77 * Rep ** -0.6)


def settling(D, C1=18.0, C2=1.0):
    return (S_REL - 1) * G * D ** 2 / (C1 * NU + np.sqrt(0.75 * C2 * (S_REL - 1) * G * D ** 3))


# =============================================================================================== LS21 flow
def fig_ls21_flow():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    # (a) laminar parabola vs log law at the same mean velocity
    z = np.linspace(0.0005, 1, 800)
    lam = 1.5 * (z - z ** 2 / 2) / 1.0 * 1.0
    lam = lam / 1.0                                   # <u> of (z - z^2/2) on [0,1] is 1/3 ; normalise below
    lam = (z - z ** 2 / 2) / (1 / 3)
    ax[0].plot(lam, z, color=BLUE, label="laminar (parabola)")
    for r, col in ((1e2, ORANGE), (1e4, AQUA)):
        z0 = 1.0 / r
        zz = np.linspace(z0, 1, 800)
        U = np.log(zz / z0)
        mean = np.trapezoid(U, zz) / (1 - z0)
        ax[0].plot(U / mean, zz, color=col, label=rf"turbulent, $H/z_0={r:.0e}$".replace("e+0", r"\times10^{")+"}$" if False else rf"turbulent $H/z_0$ = {r:.0f}")
    ax[0].axhline(1 / math.e, color=MUTED, ls="--", lw=1)
    ax[0].text(2.0, 0.40, "$z_m=H/e\\approx0.37H$\n(mean velocity: 'six-tenths down')", fontsize=8.5, color=INK, va="bottom", ha="right")
    ax[0].set_xlim(0, 2.1); ax[0].set_ylim(0, 1.0)
    ax[0].set_xlabel(r"$U/\langle U\rangle$"); ax[0].set_ylabel("$z/H$")
    ax[0].set_title("A  Same mean, different shape")
    ax[0].legend(loc="upper left", fontsize=8)
    # (b) semi-log: straight line with slope u*/kappa, intercept z0
    zl = np.logspace(-3.2, 0, 200)
    for z0, ustar, col, lab in ((1e-3, 0.14, BLUE, "$z_0=1$ mm, $u_*=0.14$"), (1e-3, 0.28, ORANGE, "$z_0=1$ mm, $u_*=0.28$"),
                                (1e-2, 0.14, AQUA, "$z_0=10$ mm, $u_*=0.14$")):
        zz = 2.0 * zl
        U = np.maximum(ustar / KAPPA * np.log(zz / z0), 0)
        ax[1].plot(U, zz, color=col, label=lab)
        ax[1].plot([0], [z0], "o", color=col, ms=5)
    ax[1].set_yscale("log"); ax[1].set_ylim(5e-4, 2.2)
    ax[1].set_xlabel("$U$ (m/s)"); ax[1].set_ylabel("height above bed $z$ (m), $H=2$ m")
    ax[1].set_title("B  Law of the wall: slope $u_*/\\kappa$, intercept $z_0$")
    ax[1].legend(loc="lower right", fontsize=8)
    ax[1].text(0.2, 0.0011, "dot = $U=0$ at $z=z_0$", fontsize=8, color=MUTED)
    # (c) friction factor and Manning n vs H/z0
    r = np.logspace(1.5, 4.5, 200)
    f = 8 * KAPPA ** 2 / (np.log(r) - 1) ** 2
    a1 = ax[2]
    a1.plot(r, f, color=BLUE)
    a1.set_xscale("log"); a1.set_xlabel("relative depth $H/z_0$"); a1.set_ylabel("Darcy-Weisbach $f$", color=BLUE)
    a2 = a1.twinx()
    a2.spines["right"].set_visible(True)
    H = 1.0
    n = H ** (1 / 6) / (math.sqrt(8 * G) / np.sqrt(f))
    a2.plot(r, n, color=ORANGE)
    a2.set_ylabel("Manning $n$ for $H=1$ m", color=ORANGE); a2.grid(False)
    a1.set_title("C  Friction falls as the flow deepens over its roughness")
    a1.annotate("Manning's $H^{1/6}$ law\nholds where $\\ln(H/z_0)-1\\approx6$\n($H/z_0=e^{7}\\approx1100$)", (1097, 0.035), (60, 0.085), fontsize=8.5,
                arrowprops=dict(arrowstyle="->", color=MUTED))
    save(fig, "fig_ls21_flow")


def fig_ls21_hydgeo():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    Q = np.logspace(0, 4, 100)
    for k, (b, f, m, ttl, ls) in enumerate(((0.5, 0.4, 0.1, "downstream", "-"), (0.26, 0.40, 0.34, "at a station", "--"))):
        for val, nm, col in ((b, "width $W$", BLUE), (f, "depth $H$", ORANGE), (m, "velocity $U$", AQUA)):
            pref = {"width $W$": 3.0, "depth $H$": 0.25, "velocity $U$": 1.0}[nm]
            ax[0].plot(Q, pref * Q ** val, color=col, ls=ls, label=f"{nm} ({ttl}: {val})" if True else None)
    ax[0].set_xscale("log"); ax[0].set_yscale("log")
    ax[0].set_xlabel("discharge $Q$ (m$^3$/s)"); ax[0].set_ylabel("$W$ (m), $H$ (m), $U$ (m/s)")
    ax[0].set_title("A  $W=aQ^b,\\ H=cQ^f,\\ U=kQ^m$")
    ax[0].legend(fontsize=7, ncol=1, loc="upper left")
    # exponent triangle
    a = ax[1]
    pts = {"downstream": (0.5, 0.4, 0.1), "at a station": (0.26, 0.40, 0.34), "braided\n(depth pinned)": (0.85, 0.05, 0.10),
           "laminar sheet\n$U\\sim H^2$": (0.0, 1 / 3, 2 / 3)}
    def xy(b, f, m):
        # barycentric: vertices W (0,0), H (1,0), U (0.5, 0.866)
        return f + 0.5 * m, 0.866 * m
    tri = np.array([[0, 0], [1, 0], [0.5, 0.866], [0, 0]])
    a.plot(tri[:, 0], tri[:, 1], color=MUTED, lw=1)
    a.text(-0.04, -0.04, "all width\n$b=1$", ha="right", va="top", fontsize=8.5)
    a.text(1.04, -0.04, "all depth\n$f=1$", ha="left", va="top", fontsize=8.5)
    a.text(0.5, 0.90, "all velocity $m=1$", ha="center", fontsize=8.5)
    cols = (BLUE, ORANGE, AQUA, VIOLET)
    for (nm, (b, f, m)), c in zip(pts.items(), cols):
        x, y = xy(b, f, m)
        a.plot([x], [y], "o", color=c, ms=8)
        a.annotate(nm, (x, y), (8, 6), textcoords="offset points", fontsize=8.5)
    a.set_aspect("equal"); a.axis("off"); a.set_title("B  Where a river puts extra discharge ($b+f+m=1$)")
    # hydraulic jump
    Fr = np.linspace(1.0, 6, 200)
    r = (np.sqrt(1 + 8 * Fr ** 2) - 1) / 2
    ax[2].plot(Fr, r, color=BLUE, label="$H_2/H_1$")
    dE = (r - 1) ** 3 / (4 * r) / (1 + Fr ** 2 / 2)
    ax[2].plot(Fr, 10 * dE, color=ORANGE, label="energy loss (% of head)/10")
    ax[2].axvline(1, color=MUTED, ls="--", lw=1)
    for nm, fr_, col in (("lowland river", 0.52, AQUA), ("step-pool", 1.63, RED)):
        if fr_ >= 1:
            ax[2].plot([fr_], [(math.sqrt(1 + 8 * fr_ ** 2) - 1) / 2], "o", color=col)
            ax[2].annotate(nm, (fr_, (math.sqrt(1 + 8 * fr_ ** 2) - 1) / 2), (6, -12), textcoords="offset points", fontsize=8.5)
    ax[2].set_xlabel("upstream Froude number $Fr_1=U_1/\\sqrt{gH_1}$"); ax[2].set_ylabel("sequent-depth ratio")
    ax[2].set_title("C  Supercritical flow jumps to subcritical")
    ax[2].legend(loc="upper left", fontsize=8.5)
    save(fig, "fig_ls21_hydgeo")


# =============================================================================================== LS22
def fig_ls22_floods():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    x = np.linspace(-4, 6, 800)       # ln(Q/Qmed)
    p = stats.norm.pdf(x)
    Qr = np.exp(x)
    ax[0].plot(Qr, p / p.max(), color=BLUE, label="frequency of daily flows (lognormal, $\\sigma=1$)")
    for j, col in ((1.5, AQUA), (2.5, ORANGE)):
        w = np.exp(j * x) * p
        ax[0].plot(Qr, w / w.max(), color=col, label=f"load carried $Q^j p(Q)$, $j={j}$")
        ax[0].axvline(math.exp(j), color=col, ls=":", lw=1)
    ax[0].set_xscale("log"); ax[0].set_xlim(0.05, 150)
    ax[0].set_xlabel("daily discharge $Q/Q_{med}$"); ax[0].set_ylabel("normalised")
    ax[0].set_title("A  Load peaks at $Q_e=Q_{med}e^{j\\sigma^2}$")
    ax[0].set_ylim(0, 1.5)
    ax[0].legend(fontsize=7.5, loc="upper left")
    # Gumbel recurrence
    T = np.logspace(0.05, 2, 200)
    y = -np.log(-np.log(1 - 1 / T))
    ax[1].plot(T, 1 + 0.35 * y, color=BLUE)
    ax[1].axvline(2.33, color=ORANGE, ls="--"); ax[1].text(2.5, 0.8, "mean annual flood\n$T=2.33$ yr", fontsize=8.5, color=INK)
    ax[1].axvspan(1.5, 2.5, color=AQUA, alpha=0.15); ax[1].text(3.2, 2.25, "shaded: bankfull\nrecurrence 1.5-2.5 yr", fontsize=8.5, color=INK)
    ax[1].set_xscale("log"); ax[1].set_xlabel("recurrence interval $T$ (yr)"); ax[1].set_ylabel("annual flood $Q_T/\\mu$ (Gumbel, $\\beta=0.35\\mu$)")
    ax[1].set_title("B  Gumbel annual maxima")
    # sinuosity
    w = np.radians(np.linspace(0, 125, 300))
    ax[2].plot(np.degrees(w), 1 / special.j0(w), color=BLUE)
    ax[2].set_ylim(1, 6); ax[2].set_xlabel("maximum deflection angle $\\omega$ (deg)"); ax[2].set_ylabel("sinuosity $=1/J_0(\\omega)$")
    ax[2].set_title("C  Sine-generated meander")
    ax2 = ax[2].inset_axes([0.07, 0.52, 0.5, 0.4])
    for om, col in ((0.5, AQUA), (1.15, ORANGE)):
        s = np.linspace(0, 2, 400)
        th = om * np.sin(2 * np.pi * s)
        X = np.cumsum(np.cos(th)) * (s[1] - s[0]); Y = np.cumsum(np.sin(th)) * (s[1] - s[0])
        ax2.plot(X, Y, color=col, lw=1.5)
    ax2.set_aspect("equal"); ax2.axis("off")
    ax2.text(0.0, -0.45, "green $\\omega=29^\\circ$ (1.06); orange $\\omega=66^\\circ$ (1.5)", fontsize=7.5, transform=ax2.transData)
    save(fig, "fig_ls22_floods")


def fig_ls22_profiles():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    x = np.linspace(0, 100, 400)                      # km downstream from the head
    # three concave forms
    L = 100.0
    xd = np.linspace(1, 100, 400)
    zh = 50 * np.log(L / xd)
    ax[0].plot(xd, zh / zh.max(), color=BLUE, label="Hack: $z=SL\\ln(L/x)$")
    xs = 65.0
    ze = (1 - np.exp(-(L - xd) / xs)) * 0 + (np.exp(-xd / xs) - np.exp(-L / xs))
    ax[0].plot(xd, ze / ze.max(), color=ORANGE, label="Sternberg fining: $S=S_0e^{-x/x_*}$, $x_*=65$ km")
    for n_m, col, lab in ((-0.5, AQUA, "capacity: $S\\propto A^{-0.5}$, $A\\propto x^{1.67}$"),):
        A = xd ** 1.67
        S = A ** n_m
        zz = np.cumsum((S * (xd[1] - xd[0]))[::-1])[::-1]
        ax[0].plot(xd, zz / zz.max(), color=col, label=lab)
    ax[0].set_xlabel("distance from the divide $x$ (km)"); ax[0].set_ylabel("elevation above base level (normalised)")
    ax[0].set_title("A  Three arguments, one shape: concave up")
    ax[0].legend(fontsize=7.5)
    # baselevel diffusion
    xx = np.linspace(0, 150, 300)
    for t, col in ((1e3, AQUA), (1e4, BLUE), (1e5, ORANGE)):
        kap = 1e5
        ax[1].plot(xx, -20 * special.erfc(xx * 1e3 / (2 * math.sqrt(kap * t))), color=col, label=f"{t:.0e} yr".replace("e+0", "e"))
    ax[1].set_xlabel("distance upstream of the mouth (km)"); ax[1].set_ylabel("elevation change (m), base level drops 20 m")
    ax[1].set_title("B  Base-level fall: diffusive response")
    ax[1].legend(title="$\\kappa=10^5$ m$^2$/yr", fontsize=8.5)
    # Amazon budget
    names = ["Amazon\n(upper)", "Madeira", "small\ntributaries", "stored on\nfloodplain", "output at\nObidos"]
    vals = [616, 715, 117, -209, 1239]
    cols = [BLUE, BLUE, BLUE, ORANGE, AQUA]
    bars = ax[2].bar(range(5), [abs(v) for v in vals], color=cols, width=0.62)
    for i, v in enumerate(vals):
        ax[2].text(i, abs(v) + 25, f"{abs(v)}", ha="center", fontsize=9)
    ax[2].set_xticks(range(5)); ax[2].set_xticklabels(names, fontsize=8.5)
    ax[2].set_ylabel("sediment (Mt/yr)")
    ax[2].set_title("C  Amazon: 1448 in = 1239 out + 209 stored")
    save(fig, "fig_ls22_profiles")


# =============================================================================================== LS23
def fig_ls23_incision():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    qs = np.linspace(0, 1.2, 400)
    E = np.where(qs <= 1, qs * (1 - qs), 0)
    ax[0].plot(qs, E / 0.25, color=BLUE, label="$\\sigma_T$ = reference")
    ax[0].plot(qs, E / 0.25 / 4, color=ORANGE, label="rock twice as strong ($\\sigma_T^{-2}$)")
    ax[0].axvline(0.5, color=MUTED, ls="--", lw=1)
    ax[0].text(0.52, 0.93, "optimum $q_s=q_c/2$", fontsize=8.5)
    ax[0].text(0.05, 0.12, "tools-limited", fontsize=8.5, color=MUTED)
    ax[0].text(0.78, 0.12, "cover-limited", fontsize=8.5, color=MUTED)
    ax[0].set_xlabel("sediment supply / transport capacity, $q_s/q_c$"); ax[0].set_ylabel("incision rate / maximum")
    ax[0].set_title("A  Tools and cover")
    ax[0].legend(fontsize=8.5, loc="center right")
    A = np.logspace(5.5, 11, 100)       # m2
    for U, col in ((0.25e-3, AQUA), (1e-3, BLUE), (4e-3, ORANGE)):
        S = (U / 5e-6) * A ** -0.5
        ax[1].plot(A / 1e6, S, color=col, label=f"$U={U*1e3:g}$ mm/yr")
    ax[1].set_xscale("log"); ax[1].set_yscale("log")
    ax[1].set_xlabel("drainage area $A$ (km$^2$)"); ax[1].set_ylabel("steady channel slope $S$")
    ax[1].set_title("B  Slope-area: $S=(U/K)A^{-1/2}$ ($n=1$, $m=\\frac{1}{2}$)")
    ax[1].legend(fontsize=8.5, loc="lower left")
    # response time vs basin length for m = 1 and m = 1/2
    h = 1 / 0.6
    xh = 1.4e3 * 0.5 ** 0.6
    Ls = np.logspace(math.log10(3e3), math.log10(4e5), 80)
    for m, K, col, lab in ((1.0, 5e-10, BLUE, "$m=1$, $K=5\\times10^{-10}$ (converges)"), (0.5, 5e-6, ORANGE, "$m=\\frac{1}{2}$, $K=5\\times10^{-6}$ (grows as $L^{1/6}$)")):
        ex = 1 - m * h
        T = (1.4e3) ** (m * h) / (K * 1e6 ** m) * (Ls ** ex - xh ** ex) / ex
        ax[2].plot((Ls / 1.4e3) ** h, T / 1e6, color=col, label=lab)
    ax[2].set_xscale("log"); ax[2].set_xlabel("basin area (km$^2$)"); ax[2].set_ylabel("response time $T=\\int dx/C$ (Myr)")
    ax[2].set_ylim(0, 6.5)
    ax[2].set_title("C  Headwaters set the response time")
    ax[2].legend(fontsize=8.5, loc="lower right")
    save(fig, "fig_ls23_incision")

def simulate_step(U0=0.2e-3, U1=0.8e-3, tend=1.0e6, K=5e-6, m=0.5, Ltot=40e3, ds=200.0):
    s = np.arange(0, Ltot + ds, ds)
    x_div = Ltot - s
    A = np.maximum((np.maximum(x_div, 1.0) / 1e3 / 1.4) ** (1 / 0.6) * 1e6, 5e5)
    z = np.concatenate([[0.0], np.cumsum(0.5 * (U0 / (K * A[1:] ** m) + U0 / (K * A[:-1] ** m)) * ds)])
    chi = np.concatenate([[0.0], np.cumsum(0.5 * ((1e6 / A[1:]) ** m + (1e6 / A[:-1]) ** m) * ds)])
    snaps = {0.0: z.copy()}
    t = 0.0
    dtmax = 0.4 * ds / (K * A.max() ** m)
    marks = [0.25e6, 0.5e6, 1.0e6]
    while t < tend:
        dt = min(dtmax, tend - t)
        z[1:] += dt * (U1 - K * A[1:] ** m * np.diff(z) / ds)
        z[0] = 0.0
        t += dt
        for mk in marks:
            if mk not in snaps and t >= mk:
                snaps[mk] = z.copy()
    return s, chi, A, snaps

def fig_ls23_transient():
    s, chi, A, snaps = simulate_step()
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    cols = {0.0: MUTED, 0.25e6: AQUA, 0.5e6: BLUE, 1.0e6: ORANGE}
    for t, z in snaps.items():
        ax[0].plot(s / 1e3, z, color=cols[t], label="initial steady state" if t == 0 else f"{t/1e6:.2f} Myr after uplift x4")
        ax[1].plot(chi / 1e3, z, color=cols[t])
    ax[0].set_xlabel("distance upstream of the outlet $s$ (km)"); ax[0].set_ylabel("elevation (m)")
    ax[0].set_title("A  Step in uplift: a knickpoint climbs")
    ax[0].legend(fontsize=8, loc="upper left")
    v = 5e-6 * 1e6 ** 0.5
    ax[1].set_xlabel("$\\chi=\\int(A_0/A)^{m}ds$ (km)"); ax[1].set_ylabel("elevation (m)")
    for t in (0.25e6, 0.5e6, 1.0e6):
        ax[1].axvline(v * t / 1e3, color=cols[t], ls=":", lw=1)
    ax[1].set_title("B  In $\\chi$: two straight lines, break at $vt$")
    t = 350e3
    Aa = np.logspace(5.5, 9, 50)
    ax[2].plot(Aa / 1e6, 5e-10 * Aa * t / 1e3, color=BLUE, label="$m=1,\\ K=5\\times10^{-10}$ ($s_k\\propto A$)")
    ax[2].plot(Aa / 1e6, 5e-6 * Aa ** 0.5 * t / 1e3, color=ORANGE, label="$m=\\frac{1}{2},\\ K=5\\times10^{-6}$ ($s_k\\propto A^{1/2}$)")
    ax[2].set_xscale("log"); ax[2].set_yscale("log")
    ax[2].set_xlabel("tributary drainage area $A$ (km$^2$)"); ax[2].set_ylabel("knickpoint distance from the trunk (km)")
    ax[2].set_title("C  $s_k=KA^mt$ after 350 kyr")
    ax[2].legend(fontsize=8.5, loc="upper left")
    save(fig, "fig_ls23_transient")

# =============================================================================================== LS24
def fig_ls24_threshold():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    Rep = np.logspace(-0.5, 5.2, 400)
    ax[0].plot(Rep, brownlie(Rep), color=BLUE)
    ax[0].set_xscale("log"); ax[0].set_ylim(0, 0.2)
    for D, lab in ((0.1e-3, "0.1 mm"), (1e-3, "1 mm"), (20e-3, "20 mm"), (200e-3, "200 mm")):
        r = math.sqrt((S_REL - 1) * G * D ** 3) / NU
        ax[0].plot([r], [brownlie(r)], "o", color=ORANGE)
        ax[0].annotate(lab, (r, brownlie(r)), (-6, 8), textcoords="offset points", fontsize=8.5, ha="right" if lab=="200 mm" else "left")
    ax[0].set_xlabel("particle Reynolds number $Re_p=\\sqrt{(s-1)gD^3}/\\nu$"); ax[0].set_ylabel("critical Shields number $\\tau_{*c}$")
    ax[0].set_title("A  Shields curve (Brownlie fit)")
    ax[0].text(300, 0.14, "minimum 0.03 at\n$u_*D/\\nu\\approx10$", fontsize=8.5)
    D = np.logspace(-4, -0.5, 200)
    Rp = np.sqrt((S_REL - 1) * G * D ** 3) / NU
    tauc = brownlie(Rp) * (RHO_S - RHO) * G * D
    ax[1].plot(D * 1e3, np.sqrt(tauc / RHO), color=BLUE, label="water: $u_{*c}=\\sqrt{\\tau_c/\\rho}$")
    for nm, rf, g_, col in (("air, Earth", 1.2, 9.81, ORANGE), ("air, Mars", 0.02, 3.71, AQUA)):
        ax[1].plot(D * 1e3, 0.1 * np.sqrt((RHO_S - rf) / rf * g_ * D), color=col, label=f"{nm}: $0.1\\sqrt{{(\\rho_s/\\rho)gD}}$")
    ax[1].set_xscale("log"); ax[1].set_yscale("log")
    ax[1].set_xlabel("grain diameter $D$ (mm)"); ax[1].set_ylabel("threshold shear velocity $u_{*t}$ (m/s)")
    ax[1].set_title("B  Air needs 15-20x the shear velocity")
    ax[1].legend(fontsize=8.5)
    w = settling(D)
    ax[2].plot(D * 1e3, w, color=BLUE, label="Ferguson-Church")
    ax[2].plot(D * 1e3, (S_REL - 1) * G * D ** 2 / (18 * NU), color=ORANGE, ls="--", label="Stokes $\\propto D^2$")
    ax[2].plot(D * 1e3, np.sqrt(3.3 * (S_REL - 1) * G * D), color=AQUA, ls=":", label="turbulent $\\propto D^{1/2}$")
    ax[2].set_xscale("log"); ax[2].set_yscale("log"); ax[2].set_ylim(1e-3, 3)
    ax[2].set_xlabel("grain diameter $D$ (mm)"); ax[2].set_ylabel("settling velocity $w_s$ (m/s)")
    ax[2].set_title("C  Settling: Stokes to Newton drag")
    ax[2].legend(fontsize=8.5)
    save(fig, "fig_ls24_threshold")


def fig_ls24_suspension():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    H = 3.0; a = 0.05 * H
    z = np.linspace(a, 0.98 * H, 300)
    for P, col in ((0.1, BLUE), (0.5, AQUA), (1.0, ORANGE), (2.5, RED), (5.0, VIOLET)):
        C = ((H - z) / z * a / (H - a)) ** P
        ax[0].plot(C, z / H, color=col, label=f"$P={P}$")
    ax[0].set_xscale("log"); ax[0].set_xlim(1e-4, 1.5)
    ax[0].set_xlabel("$C/C_a$"); ax[0].set_ylabel("$z/H$")
    ax[0].set_title("A  Rouse profiles, $P=w_s/\\kappa u_*$")
    ax[0].legend(fontsize=8.5)
    D = np.logspace(-4.3, -1.3, 150)
    us = np.logspace(-2, 0, 150)
    DD, UU = np.meshgrid(D, us)
    P = settling(DD) / (KAPPA * UU)
    cs = ax[1].contourf(DD * 1e3, UU, np.digitize(P, [0.8, 2.5]), levels=[-0.5, 0.5, 1.5, 2.5], colors=[AQUA, ORANGE, BLUE], alpha=0.35)
    Rp = np.sqrt((S_REL - 1) * G * D ** 3) / NU
    uc = np.sqrt(brownlie(Rp) * (S_REL - 1) * G * D)
    ax[1].plot(D * 1e3, uc, color=INK, lw=2)
    ax[1].text(6, 0.022, "no motion", fontsize=9, color=INK)
    ax[1].text(6, 0.2, "bedload\n$P>2.5$", fontsize=9, color=INK)
    ax[1].text(0.45, 0.12, "mixed", fontsize=9, color=INK)
    ax[1].text(0.07, 0.45, "full suspension\n$P<0.8$", fontsize=9, color=INK)
    ax[1].set_xscale("log"); ax[1].set_yscale("log")
    ax[1].set_xlabel("grain diameter $D$ (mm)"); ax[1].set_ylabel("shear velocity $u_*$ (m/s)")
    ax[1].set_title("B  Transport mode map (black line = threshold)")
    tau = np.linspace(0.047, 0.5, 100)
    ax[2].plot(tau / 0.047, 8 * (tau - 0.047) ** 1.5, color=BLUE, label="bedload (Meyer-Peter and Muller)")
    ax[2].plot(tau / 0.047, 8 * (tau - 0.047) ** 1.5 * 0 + 8 * (tau - 0.047) * 0.2, color=ORANGE, ls="--", label="linear in the excess (same start)")
    ax[2].set_xlabel("$\\tau_*/\\tau_{*c}$"); ax[2].set_ylabel("dimensionless bedload $q_{b*}$")
    ax[2].set_title("C  Thresholded, then nonlinear")
    ax[2].legend(fontsize=8.5)
    save(fig, "fig_ls24_suspension")


if __name__ == "__main__":
    for f in (fig_ls21_flow, fig_ls21_hydgeo, fig_ls22_floods, fig_ls22_profiles, fig_ls23_incision, fig_ls23_transient,
              fig_ls24_threshold, fig_ls24_suspension):
        f()
