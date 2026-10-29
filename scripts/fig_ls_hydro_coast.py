"""Figures for LS25-LS27 (water in the landscape, sea level and waves, coasts).  Numbers: scripts/ls_hydro_coast_numbers.py.
    .venv/bin/python -W ignore scripts/fig_ls_hydro_coast.py
Writes Assets/figures/fig_ls25_basins.png, fig_ls25_soil.png, fig_ls25_runoff.png, fig_ls26_sealevel.png, fig_ls26_waves.png,
fig_ls27_littoral.png, fig_ls27_delta.png.
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
from scipy import optimize, stats  # noqa
import ls_hydro_coast_numbers as N  # noqa

G, RHO, RHO_S, RHO_SEA = 9.81, 1000.0, 2650.0, 1025.0
YR = 365.25 * 86400


# ================================================================================================= LS25
def fig_ls25_basins():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    rng = np.random.default_rng(3)
    tot, nrep = {}, 40
    for _ in range(nrep):
        for k, v in N.strahler_counts(4096, rng).items():
            tot[k] = tot.get(k, 0) + v
    od = sorted(tot)
    avg = np.array([tot[k] / nrep for k in od])
    ax[0].semilogy(od, avg, "o", color=BLUE, label="simulated random-topology networks (4096 sources)")
    j = np.arange(1, 9)
    ax[0].semilogy(j, 4096 * 4.0 ** -(j - 1), color=ORANGE, label="$N_j=N_1R_b^{-(j-1)}$, $R_b=4$")
    ax[0].set_xlabel("Strahler order $j$"); ax[0].set_ylabel("number of streams $N_j$")
    ax[0].set_title("A  Horton's law of stream numbers")
    ax[0].legend(fontsize=8.5)
    ax[0].text(4.6, 1000, "$R_b=3.99$ from the fit", fontsize=9)
    # B: distance to nearest channel
    w = 200.0
    x = rng.uniform(0, w, 200000)
    d = np.minimum(x, w - x)
    ax[1].hist(d, bins=40, density=True, color=AQUA, alpha=0.8)
    ax[1].axvline(w / 4, color=ORANGE, lw=2); ax[1].text(w / 4 + 2, 0.0113, "mean $=w/4=1/(4D_d)$", fontsize=9)
    ax[1].axvline(w / 2, color=MUTED, ls="--"); ax[1].text(w / 2 - 3, 0.0085, "divide:\n$w/2=1/(2D_d)$", fontsize=9, ha="right")
    ax[1].set_xlabel("distance to the nearest channel (m)"); ax[1].set_ylabel("probability density")
    ax[1].set_title("B  Channels 200 m apart ($D_d=5$ km/km$^2$)")
    ax[1].set_ylim(0, 0.0135)
    # C: lag times
    names = ["overland flow\n($U=0.05$ m/s)", "subsurface storm flow\n($K=10^{-4}$ m/s)", "groundwater\n($K=10^{-5}$ m/s)"]
    t = [100 / 0.05, 100 / (1e-4 * 0.3 / 0.4), 100 / (1e-5 * 0.05 / 0.3)]
    ax[2].bar(range(3), np.array(t) / 3600, color=[ORANGE, BLUE, AQUA], width=0.6)
    ax[2].set_yscale("log"); ax[2].set_xticks(range(3)); ax[2].set_xticklabels(names, fontsize=8.5)
    for i, tt in enumerate(t):
        ax[2].text(i, tt / 3600 * 1.3, f"{tt/3600:.1f} h" if tt < 3 * 86400 else f"{tt/86400:.0f} d", ha="center", fontsize=9.5)
    ax[2].set_ylabel("travel time over 100 m (h)"); ax[2].set_ylim(0.1, 3e5)
    ax[2].set_title("C  Why short hillslopes make flashy basins")
    save(fig, "fig_ls25_basins")


def fig_ls25_soil():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    r = np.logspace(-7.3, -3.7, 200)
    h = 2 * 0.072 / (RHO * G * r)
    ax[0].loglog(r * 1e6, h, color=BLUE)
    ax[0].axhline(3.4, color=AQUA, ls="--"); ax[0].text(0.06, 3.9, "field capacity ($-33$ kPa)", fontsize=9)
    ax[0].axhline(153, color=ORANGE, ls="--"); ax[0].text(0.06, 175, "wilting point ($-1.5$ MPa)", fontsize=9)
    ax[0].set_xlabel("pore radius ($\\mu$m)"); ax[0].set_ylabel("suction head $2\\gamma/\\rho g r$ (m)")
    ax[0].set_title("A  Small pores hold water harder")
    ax[0].set_ylim(0.04, 600)
    # B: Green-Ampt
    Ks, psi, dth = 1e-6, 0.20, 0.30
    R = 20e-3 / 3600
    sd = psi * dth
    Fp = sd * Ks / (R - Ks); tp = Fp / R
    t = np.linspace(tp, 6 * 3600, 400)
    Ts = (Fp - sd * math.log(1 + Fp / sd)) / Ks
    F = np.array([optimize.brentq(lambda F_: F_ - sd * math.log(1 + F_ / sd) - Ks * (tt - tp + Ts), 1e-12, 10) for tt in t])
    fcap = Ks * (1 + sd / F)
    th = np.linspace(0, 6, 2)
    ax[1].plot([0, tp / 3600], [R * 3.6e6] * 2, color=MUTED); ax[1].plot(t / 3600, fcap * 3.6e6, color=BLUE, label="infiltration capacity $f$")
    ax[1].axhline(R * 3.6e6, color=ORANGE, ls="--", label="rain 20 mm/h")
    ax[1].axhline(Ks * 3.6e6, color=AQUA, ls=":", label="$K_s=3.6$ mm/h")
    ax[1].axvline(tp / 3600, color=MUTED, lw=1); ax[1].text(tp / 3600 + 0.05, 17, "ponding\n$t_p=39$ min", fontsize=9)
    ax[1].fill_between(t / 3600, fcap * 3.6e6, R * 3.6e6, where=fcap * 3.6e6 < R * 3.6e6, color=ORANGE, alpha=0.2)
    ax[1].text(2.4, 16.2, "shaded: runoff", fontsize=9.5, color=INK)
    ax[1].set_xlabel("time (h)"); ax[1].set_ylabel("rate (mm/h)"); ax[1].set_ylim(0, 24)
    ax[1].set_title("B  Green-Ampt: capacity falls toward $K_s$")
    ax[1].legend(fontsize=8.5, loc="lower right", bbox_to_anchor=(1.0, 0.18))
    # C: Dupuit
    L = 500.0
    x = np.linspace(0, L, 300)
    K = 1e-5
    for IK, col in ((0.0, MUTED), (1e-3, AQUA), (2e-3, BLUE), (4e-3, ORANGE)):
        H = np.sqrt(15 ** 2 + (5 ** 2 - 15 ** 2) * x / L + IK * x * (L - x))
        ax[2].plot(x, H, color=col, label=f"$I/K={IK:g}$")
    ax[2].fill_between(x, 0, 5, color=BLUE, alpha=0.08)
    ax[2].set_xlabel("distance between two channels (m)"); ax[2].set_ylabel("water-table height $H$ (m)")
    ax[2].set_title("C  Dupuit water table: an ellipse (stages 15 m, 5 m)")
    ax[2].legend(fontsize=8.5, loc="lower left")
    save(fig, "fig_ls25_soil")


def fig_ls25_runoff():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    S, f = 0.004, 0.5
    Rr, Ii = 5e-3 / 3600, 2e-3 / 3600
    x = np.linspace(1, 500, 500)
    q = (Rr - Ii) * x
    h = (q * math.sqrt(f / (8 * G * S))) ** (2 / 3)
    tau = RHO * G * h * S
    ax[0].plot(x, h * 1e3, color=BLUE); ax[0].set_ylabel("flow thickness $h$ (mm)")
    ax[0].set_xlabel("distance from the divide $x$ (m)")
    sec = ax[0].secondary_yaxis("right", functions=(lambda hh: RHO * G * S * hh / 1e3, lambda tt: tt * 1e3 / (RHO * G * S)))
    sec.set_ylabel("bed shear stress $\\tau_b=\\rho gSh$ (Pa)")
    ax[0].axhline(0.17 / (RHO * G * S) * 1e3, color=MUTED, ls="--"); ax[0].text(20, 4.5, "$\\tau_c=0.17$ Pa (0.2 mm sand)", fontsize=9)
    ax[0].axvline(271, color=AQUA, lw=2); ax[0].text(278, 1.0, "$X_c=271$ m\nbelt of no erosion", fontsize=9)
    ax[0].set_title("A  Horton's sheetwash: $h\\propto x^{2/3}$")
    # B: Xc vs excess rain
    Rex = np.logspace(0.3, 2.3, 100) * 1e-3 / 3600
    for Sx, col in ((0.004, BLUE), (0.02, AQUA), (0.1, ORANGE)):
        hc = 0.17 / (RHO * G * Sx); Uc = math.sqrt(8 * 0.17 / (RHO * f))
        ax[1].loglog(Rex * 3.6e6, hc * Uc / Rex, color=col, label=f"$S={Sx}$")
    ax[1].set_xlabel("excess rainfall $R-I$ (mm/h)"); ax[1].set_ylabel("belt of no erosion $X_c$ (m)")
    ax[1].set_title("B  $X_c\\propto1/[S(R-I)]$")
    ax[1].legend(fontsize=8.5)
    # C: saturation threshold
    Kk = np.logspace(-7, -2.5, 100)
    qr = 20e-3 / 86400
    ax[2].loglog(Kk, Kk * 0.7 / qr, color=BLUE)
    ax[2].axhline(89, color=ORANGE, ls="--"); ax[2].text(2e-7, 105, "CB-1 hollow: $a/S\\approx89$ m", fontsize=9)
    for nm, k, yy in (("till", 1e-6, 3.3), ("loam", 1e-4, 330), ("CB-1 soil", 1e-3, 3300)):
        ax[2].plot([k], [k * 0.7 / qr], "o", color=INK, ms=5); ax[2].annotate(nm, (k, k * 0.7 / qr), (6, -12), textcoords="offset points", fontsize=9)
    ax[2].text(3e-7, 6e3, "above the line: soil saturates from above\n(saturation overland flow)", fontsize=9, color=INK)
    ax[2].set_xlabel("saturated conductivity $K_s$ (m/s), soil 0.7 m thick"); ax[2].set_ylabel("critical $a/S=T/q_r$ (m), $q_r=20$ mm/d")
    ax[2].set_title("C  Where a hillslope saturates")
    fig.subplots_adjust(wspace=0.38)
    save(fig, "fig_ls25_runoff")


# ================================================================================================= LS26
def fig_ls26_sealevel():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    names = ["present", "Holocene\n(6 m in\n10 kyr)", "deglaciation\n(120 m in\n16 kyr)", "melt-water\npulse 1A\n(25 m in\n500 yr)"]
    vals = [2.9, 0.6, 7.5, 50.0]
    ax[0].bar(range(4), vals, color=[AQUA, BLUE, BLUE, ORANGE], width=0.6)
    for i, v in enumerate(vals):
        ax[0].text(i, v * 1.12, f"{v:g} mm/yr", ha="center", fontsize=9.5)
    ax[0].set_yscale("log"); ax[0].set_ylim(0.3, 120); ax[0].set_xticks(range(4)); ax[0].set_xticklabels(names, fontsize=8.5)
    ax[0].set_ylabel("rate of sea-level rise (mm/yr)"); ax[0].set_title("A  Rates of sea-level rise")
    # B: terrace elevation
    U = np.linspace(0, 4, 50)
    ax[1].plot(U, U * 125 + 6, color=BLUE, label="125 ka terrace (sea level $+6$ m)")
    ax[1].plot(U, U * 6 + 0, color=ORANGE, label="6 ka terrace (sea level $\\approx0$)")
    ax[1].axvspan(1, 3, color=AQUA, alpha=0.15); ax[1].text(1.05, 330, "Huon Peninsula\n1-3 mm/yr", fontsize=9)
    ax[1].set_xlabel("uplift rate $U$ (mm/yr)"); ax[1].set_ylabel("terrace elevation $z=UT+z_{sl}$ (m)")
    ax[1].set_title("B  A raised shoreline is an uplift gauge"); ax[1].legend(fontsize=8.5, loc="upper left")
    # C: swell arrival period
    t = np.linspace(1.5, 8, 200)
    for D, col in ((2000, AQUA), (4000, BLUE), (8000, ORANGE)):
        ax[2].plot(t, 4 * math.pi * D * 1e3 / (G * t * 86400), color=col, label=f"storm {D/1000:.0f} Mm away")
    ax[2].set_ylim(5, 40)
    ax[2].set_xlabel("time since the storm (days)"); ax[2].set_ylabel("period of the arriving swell $T=4\\pi D/gt$ (s)")
    ax[2].set_title("C  Dispersion sorts a storm's waves"); ax[2].legend(fontsize=8.5)
    save(fig, "fig_ls26_sealevel")


def fig_ls26_waves():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    h = np.logspace(0, 3.7, 300)
    for T, col in ((6, AQUA), (10, BLUE), (14, ORANGE), (20, VIOLET)):
        C = np.array([N.wave_props(T, hh)[1] for hh in h])
        ax[0].semilogx(h, C, color=col, label=f"$T={T}$ s")
    ax[0].semilogx(h, np.sqrt(G * h), color=MUTED, ls="--", label="$\\sqrt{gh}$")
    ax[0].set_ylim(0, 35); ax[0].set_xlabel("water depth $h$ (m)"); ax[0].set_ylabel("phase speed $C$ (m/s)")
    ax[0].set_title("A  Dispersion: deep waves $gT/2\\pi$, shallow $\\sqrt{gh}$"); ax[0].legend(fontsize=8.5, loc="upper left")
    # B: shoaling
    T, H0, a0 = 12.0, 2.0, math.radians(30)
    k0, C0, Cg0, _ = N.wave_props(T, 5000)
    hh = np.linspace(40, 1.2, 200)
    Hs, an = [], []
    for hv in hh:
        k, C, Cg, n = N.wave_props(T, hv)
        sa = math.sin(a0) * C / C0
        Hs.append(H0 * math.sqrt(Cg0 / Cg) * math.sqrt(math.cos(a0) / math.sqrt(1 - sa ** 2))); an.append(math.degrees(math.asin(sa)))
    Hs = np.array(Hs)
    ax[1].plot(hh, Hs, color=BLUE, label="wave height $H$"); ax[1].plot(hh, 0.78 * hh, color=ORANGE, ls="--", label="breaking limit $0.78\\,h$")
    ax[1].set_xlim(40, 0); ax[1].set_ylim(0, 4); ax[1].set_xlabel("water depth $h$ (m), shoreward $\\to$"); ax[1].set_ylabel("height $H$ (m)")
    a2 = ax[1].twinx(); a2.spines["right"].set_visible(True); a2.grid(False); a2.plot(hh, an, color=AQUA); a2.set_ylabel("wave angle to shore (deg)", color=AQUA); a2.set_ylim(0, 35)
    ax[1].plot([3.18], [2.48], "o", color=INK); ax[1].annotate("breaks: $h_b=3.2$ m,\n$H_b=2.5$ m, $\\alpha_b=8.5^\\circ$", (3.18, 2.48), (14, 0.4), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax[1].set_title("B  Shoaling and refraction ($T=12$ s, 2 m, $30^\\circ$)"); ax[1].legend(fontsize=8.5, loc="upper left")
    # C: Rayleigh energy
    q = np.linspace(0.001, 1, 500)
    ax[2].plot(q * 100, q * (1 + np.log(1 / q)) * 100, color=BLUE)
    ax[2].plot([10], [33], "o", color=ORANGE); ax[2].annotate("largest 10% of waves\ncarry 33% of the energy", (10, 33), (25, 18), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax[2].plot([0, 100], [0, 100], color=MUTED, ls=":")
    ax[2].set_xlabel("share of waves, largest first (%)"); ax[2].set_ylabel("share of energy (%)")
    ax[2].set_title("C  Rayleigh sea: big waves do the work")
    fig.subplots_adjust(wspace=0.42)
    save(fig, "fig_ls26_waves")


# ================================================================================================= LS27
def littoral(Hb, ab, K=0.39, gam=0.78, p=0.4):
    P = RHO_SEA * G / 8 * Hb ** 2 * math.sqrt(G * Hb / gam) * math.sin(math.radians(ab)) * math.cos(math.radians(ab))
    return K * P / ((RHO_S - RHO_SEA) * G * (1 - p))


def fig_ls27_littoral():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    ang = np.linspace(0, 90, 300)
    for Hb, col in ((1.0, AQUA), (2.0, BLUE)):
        ax[0].plot(ang, [littoral(Hb, a) * YR / 1e6 for a in ang], color=col, label=f"$H_b={Hb:g}$ m")
    ax[0].axvline(45, color=MUTED, ls="--"); ax[0].text(46, 1.0, "maximum drift\nat $45^\\circ$", fontsize=9)
    ax[0].set_xlabel("breaker angle to the shore $\\alpha_b$ (deg)"); ax[0].set_ylabel("longshore transport (million m$^3$/yr)")
    ax[0].set_title("A  $Q\\propto H_b^{5/2}\\sin2\\alpha_b$"); ax[0].legend(fontsize=8.5)
    # B: diffusivity sign and shoreline evolution
    a0 = np.linspace(0, 90, 300)
    kap = 2e6 * np.cos(np.radians(2 * a0)) / 10 / 1e5
    ax[1].plot(a0, kap, color=BLUE); ax[1].axhline(0, color=MUTED)
    ax[1].fill_between(a0, 0, kap, where=kap > 0, color=AQUA, alpha=0.25); ax[1].fill_between(a0, 0, kap, where=kap < 0, color=ORANGE, alpha=0.25)
    ax[1].text(8, 0.6, "smoothing\n(diffusion)", fontsize=9.5); ax[1].text(55, -1.5, "growth: capes,\nspits (anti-diffusion)", fontsize=9.5)
    ax[1].set_xlabel("deep-water wave angle $\\alpha_0$ (deg)"); ax[1].set_ylabel("shoreline diffusivity $\\kappa$ ($10^5$ m$^2$/yr)")
    ax[1].set_title("B  $\\kappa=2Q_0\\cos2\\alpha_0/D$ changes sign at $45^\\circ$")
    # C: net vs gross
    classes = [(0.6, 1.2, +10, "60%: 1.2 m, +10$^\\circ$"), (0.3, 0.8, -15, "30%: 0.8 m, $-15^\\circ$"), (0.1, 2.5, -8, "10%: 2.5 m, $-8^\\circ$")]
    vals = [f * littoral(Hb, abs(a)) * YR / 1e6 * math.copysign(1, a) for f, Hb, a, _ in classes]
    ax[2].bar(range(3), vals, color=[BLUE, AQUA, ORANGE], width=0.6)
    for i, v in enumerate(vals):
        ax[2].text(i, v + (0.06 if v > 0 else -0.14), f"{v:+.2f}", ha="center", fontsize=9.5)
    ax[2].bar([3], [sum(vals)], color=MUTED, width=0.6); ax[2].text(3, sum(vals) - 0.14, f"net {sum(vals):+.2f}", ha="center", fontsize=9.5)
    ax[2].axhline(0, color=INK, lw=0.8)
    ax[2].set_xticks(range(4)); ax[2].set_xticklabels([c[3] for c in classes] + ["net drift"], fontsize=8)
    ax[2].set_ylabel("drift (million m$^3$/yr, + = one way)"); ax[2].set_title("C  Net drift: a small difference of big numbers")
    save(fig, "fig_ls27_littoral")


def fig_ls27_delta():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    x = np.linspace(0, 30, 300)
    for nm, K, col in (("Fraser ($K=2.4\\times10^{4}$)", 2.4e4, AQUA), ("Mississippi ($K=5.6\\times10^{5}$)", 5.6e5, BLUE)):
        ax[0].plot(x, np.exp(-x * 1e3 * 50 / K), color=col, label=nm)
        ax[0].axvline(K / 50 / 1e3, color=col, ls=":")
    ax[0].set_xlabel("distance seaward of the delta lip (km), $u_0=50$ m/yr"); ax[0].set_ylabel("height above the basin floor / delta thickness")
    ax[0].set_title("A  Delta front: $z=z_0e^{-u_0x/K}$, scale $K/u_0$"); ax[0].legend(fontsize=8.5)
    # B: plume diving
    drho = np.linspace(0, 30, 100)
    ax[1].plot(drho, drho / (1 - RHO / RHO_S), color=BLUE)
    ax[1].plot([25], [40.15], "o", color=ORANGE); ax[1].annotate("river into the sea:\n$C>40$ kg/m$^3$", (25, 40.15), (3, 36), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax[1].plot([10], [16.06], "o", color=AQUA); ax[1].annotate("brackish estuary:\n16 kg/m$^3$", (10, 16.06), (16, 8), fontsize=9, arrowprops=dict(arrowstyle="->", color=MUTED))
    ax[1].text(1, 9, "below: hypopycnal plume\n(spreads over the water)", fontsize=9); ax[1].text(14, 34, "above: hyperpycnal\n(plunges, turbidity current)", fontsize=9)
    ax[1].set_xlabel("ambient minus river-water density (kg/m$^3$)"); ax[1].set_ylabel("critical sediment concentration $C$ (kg/m$^3$)")
    ax[1].set_title("B  When does a river plunge?")
    # C: delta budget
    names = ["Mississippi-size\n3e4 km$^2$, 10 mm/yr", "Ganges-Brahmaputra\n1e5 km$^2$, 5 mm/yr", "small delta\n1e3 km$^2$, 8 mm/yr"]
    need = [390, 650, 10]
    ax[2].bar(range(3), need, color=[BLUE, AQUA, ORANGE], width=0.6)
    for i, v in enumerate(need):
        ax[2].text(i, v + 15, f"{v} Mt/yr", ha="center", fontsize=9.5)
    ax[2].set_xticks(range(3)); ax[2].set_xticklabels(names, fontsize=8.5); ax[2].set_ylabel("sediment needed to keep pace (Mt/yr)")
    ax[2].set_title("C  The delta budget: $A\\cdot\\mathrm{RSLR}\\cdot\\rho_b$")
    save(fig, "fig_ls27_delta")


if __name__ == "__main__":
    for f in (fig_ls25_basins, fig_ls25_soil, fig_ls25_runoff, fig_ls26_sealevel, fig_ls26_waves, fig_ls27_littoral, fig_ls27_delta):
        f()
