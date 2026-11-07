"""CL16-CL21 figures (Neena lectures 2025 + Joy readings 2026). One figure per chapter; numbers come from cl_neena_numbers.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *
from cl10lib import daily_insolation, annual_mean
from matplotlib.patches import FancyArrowPatch, Rectangle, Polygon

sigma = 5.670374419e-8
S0 = 1361.0
OMEGA = 7.2921e-5

# ============================================================================================================== CL16
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.6))
kB, u = 1.380649e-23, 1.66053907e-27
gases = [("H₂", 2.016), ("He", 4.003), ("H₂O", 18.015), ("N₂", 28.014), ("CO₂", 44.01)]
vm = [np.sqrt(8 * kB * 1000 / (np.pi * M * u)) for _, M in gases]
a = ax[0]
a.bar([g for g, _ in gases], vm, color=[BLUE if v > 1864 else (ORANGE if v > 838 else AQUA) for v in vm], width=0.62)
for y, lab, col in ((1864, "Earth  v_esc/6 = 1864 m/s", INK), (838, "Mars  v_esc/6 = 838 m/s", RED)):
    a.axhline(y, color=col, lw=1.6, ls="--")
    a.text(4.45, y + 40, lab, ha="right", fontsize=8.2, color=col)
a.set_ylabel("mean thermal speed at 1000 K  (m/s)"); a.set_ylim(0, 3500)
a.set_title("A  who escapes? (speed > ⅙ v_esc)", fontsize=9.8)
a.text(-0.4, 3250, "blue: lost by Earth and Mars;  orange: lost by Mars only;\ngreen: held by both (T = 1000 K assumed)", fontsize=7.8, color=INK, va="top")

b = ax[1]
t = np.logspace(-2.5, 3, 300)
for tau, nm, col in ((10 / 365.25, "water vapour 10 d", AQUA), (12, "CH₄ 12 yr", ORANGE), (114, "N₂O 114 yr", BLUE)):
    b.plot(t, np.exp(-t / tau), color=col, lw=2.2, label=nm)
b.axvspan(10, 100, color=GRID, alpha=0.8)
b.text(10.8, 0.9, "CO₂: 'at least a decade'\n(10–100 yr, Lecture 6)", fontsize=7.8, color=INK)
b.set_xscale("log"); b.set_xlabel("time since emission (yr)"); b.set_ylabel("fraction of a pulse remaining  exp(−t/τ)")
b.legend(fontsize=8, frameon=False, loc="lower left")
b.set_title("B  atmospheric lifetimes (Lecture 6)", fontsize=9.8)

c = ax[2]
names = ["Mars", "Earth", "Venus"]
S = {"Mars": (590.0, 0.25), "Earth": (1369.77, 0.30), "Venus": (2642.3, 0.75)}
Te = [((S[n][0] * (1 - S[n][1])) / (4 * sigma)) ** 0.25 for n in names]
Ts1 = [2 ** 0.25 * x for x in Te]
obs = [np.nan, 288, 735]
x = np.arange(3)
c.bar(x - 0.27, Te, 0.26, color=MUTED, label="T_e (no atmosphere effect)")
c.bar(x, Ts1, 0.26, color=BLUE, label="one-layer model  2^{1/4} T_e")
c.bar(x + 0.27, obs, 0.26, color=ORANGE, label="observed surface")
for i, v in enumerate(Te): c.text(i - 0.27, v + 12, "%.0f" % v, ha="center", fontsize=7.6)
for i, v in enumerate(Ts1): c.text(i, v + 12, "%.0f" % v, ha="center", fontsize=7.6)
for i, v in enumerate(obs):
    if not np.isnan(v): c.text(i + 0.27, v + 12, "%.0f" % v, ha="center", fontsize=7.6)
c.set_xticks(x); c.set_xticklabels(names); c.set_ylabel("temperature (K)"); c.set_ylim(0, 860)
c.legend(fontsize=7.8, frameon=False, loc="upper left")
c.set_title("C  the one-layer model fails for Venus", fontsize=9.8)
fig.tight_layout()
fig.text(0.5, -0.03, "A: mean thermal speeds √(8kT/πm) at an assumed 1000 K against one sixth of the escape speed (Lecture 4's criterion): Earth keeps H₂O and N₂ and loses H₂ and He; Mars loses H₂O (and, marginally, N₂) but keeps CO₂ (694 vs 838 m/s).  "
         "B: exponential decay with the lifetimes of Lecture 6.  C: Tutorial 2 / Lecture 4 numbers (Mars: 590 W m⁻², albedo 0.25).  Numbers: cl_neena_numbers.py (cl16).", ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_cl16_atmosphere")

# ============================================================================================================== CL17
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.6))
a = ax[0]
e = np.linspace(0, 0.07, 200)
a.plot(e, 100 * (((1 + e) / (1 - e)) ** 2 - 1), color=BLUE, lw=2.4)
for ee, lab in ((0.0167, "today 0.0167\n6.9 %"), (0.0517, "Lecture 10's '23 %'\ne = 0.052"), (0.0607, "max of Lecture 9\n0.0607: 27.5 %")):
    yv = 100 * (((1 + ee) / (1 - ee)) ** 2 - 1)
    a.plot([ee], [yv], "o", color=ORANGE, ms=6)
    a.annotate(lab, (ee, yv), xytext=(ee - 0.035 if ee > 0.05 else ee + 0.004, yv + (4 if ee > 0.05 else 5)), fontsize=7.8, color=INK)
a.set_xlabel("eccentricity  e"); a.set_ylabel("perihelion flux above aphelion flux  (%)")
a.set_title("A  ((1+e)/(1−e))² − 1", fontsize=9.8)

b = ax[1]
vp = np.linspace(0, 360, 361)
phi = np.radians(65)
for ecc, col, lab in ((0.0, MUTED, "e = 0"), (0.0167, BLUE, "e = 0.0167 (today)"), (0.05, ORANGE, "e = 0.05")):
    q = [float(daily_insolation(phi, np.pi / 2, obl=np.radians(23.44), ecc=ecc, varpi=np.radians(v))) for v in vp]
    b.plot(vp, q, color=col, lw=2.2, label=lab)
b.axvline(282.9, color=GRID, lw=1.4)
b.text(287, 528, "perihelion\ntoday ≈ 283°", fontsize=7.6, color=MUTED)
b.set_xlabel("solar longitude of perihelion ϖ  (deg; 90° = perihelion at the June solstice)"); b.set_ylabel("daily insolation, 65°N, 21 June  (W m⁻²)")
b.legend(fontsize=8, frameon=False, loc="lower left")
b.set_title("B  precession is modulated by eccentricity", fontsize=9.8)

c = ax[2]
lat = np.linspace(0, 90, 91)
d_ann = [float(annual_mean(np.radians(l), obl=np.radians(24.5))) - float(annual_mean(np.radians(l), obl=np.radians(22.1))) for l in lat]
d_jun = [float(daily_insolation(np.radians(l), np.pi / 2, obl=np.radians(24.5))) - float(daily_insolation(np.radians(l), np.pi / 2, obl=np.radians(22.1))) for l in lat]
c.plot(lat, d_ann, color=BLUE, lw=2.4, label="annual mean")
c.plot(lat, d_jun, color=ORANGE, lw=2.4, label="21 June daily mean")
c.axhline(0, color=MUTED, lw=1)
c.set_xlabel("latitude (deg N)"); c.set_ylabel("insolation(24.5°) − insolation(22.1°)  (W m⁻²)")
c.legend(fontsize=8, frameon=False, loc="upper left")
c.set_title("C  obliquity: high latitudes, not the tropics", fontsize=9.8)
fig.tight_layout()
fig.text(0.5, -0.03, "A: Lecture 9's 6.8 % and Lecture 10's 23 % checked: with the maximum eccentricity of the same lecture (0.0607) the ratio is 27.5 %; 23 % corresponds to e = 0.052.  "
         "B: exact daily-mean insolation (cl10lib, Kepler weighting) at 65°N on 21 June for obliquity 23.44°: with e = 0.05 the precession swing is 447.7–547.0 W m⁻² (20 %).  "
         "C: tilt 24.5° vs 22.1°: at the equator the annual mean *falls* by 3.5 W m⁻², at the pole it rises by 16.7.  Numbers: cl_neena_numbers.py (cl17).", ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_cl17_orbit")

# ============================================================================================================== CL18
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.6))
a = ax[0]
z = np.linspace(0, 250, 400)
for c_, col, lab in ((np.log(10) / 90, BLUE, "Jerlov type I, 465 nm (10 % at 90 m): c = 0.0256 m⁻¹"), (0.1, AQUA, "turbid midlatitude water (illustrative c = 0.1)"), (0.5, ORANGE, "coastal water (illustrative c = 0.5)"), (np.log(2), MUTED, "total solar flux, 'half in the first metre' (c = 0.69)")):
    a.plot(100 * np.exp(-c_ * z), z, color=col, lw=2.1, label=lab)
a.set_ylim(250, 0); a.set_xlim(0, 100); a.set_xscale("linear")
a.axhline(180, color=GRID, lw=1.2); a.text(60, 176, "1 % level, type I: 180 m", fontsize=7.8, color=BLUE, va="bottom")
a.set_xlabel("irradiance remaining  (%)"); a.set_ylabel("depth (m)")
a.legend(fontsize=7.2, frameon=False, loc="lower right")
a.set_title("A  Beer–Lambert: I = I₀ exp(−c z)", fontsize=9.8)

b = ax[1]
Cw = 4.218e6
vals = [("1 m of rock\n(seasonal land layer)", 2.4e6, MUTED), ("atmosphere\nc_p p_s/g", 1004 * 1.013e5 / 9.81, AQUA), ("mixed layer\n70 m", 70 * Cw, BLUE), ("whole ocean\n3730 m", 3730 * Cw, ORANGE)]
for i, (n, v, col) in enumerate(vals):
    b.bar(i, v, color=col, width=0.6)
    b.text(i, v * 1.25, "%.1e" % v, ha="center", fontsize=8)
b.set_yscale("log"); b.set_ylim(1e6, 1e12)
b.set_xticks(range(4)); b.set_xticklabels([v[0] for v in vals], fontsize=7.8)
b.set_ylabel("heat capacity per m² of surface  (J m⁻² K⁻¹)")
b.set_title("B  the ocean is the heat reservoir", fontsize=9.8)

c = ax[2]
inn = [("absorbed solar", 168, BLUE), ("back radiation", 324, AQUA)]
out = [("IR emitted", 390, ORANGE), ("latent heat", 78, RED), ("sensible heat", 24, VIOLET)]
bot = 0
for n, v, col in inn:
    c.bar(0, v, bottom=bot, color=col, width=0.55); c.text(0, bot + v / 2, "%s\n%d" % (n, v), ha="center", va="center", fontsize=8, color="white")
    bot += v
bot = 0
for n, v, col in out:
    c.bar(1, v, bottom=bot, color=col, width=0.55); c.text(1, bot + v / 2, "%s %d" % (n, v), ha="center", va="center", fontsize=8, color="white")
    bot += v
c.set_xticks([0, 1]); c.set_xticklabels(["gains\n492", "losses\n492"]); c.set_ylabel("W m⁻²"); c.set_ylim(0, 540)
c.set_title("C  surface budget (Stewart Fig. 5.6)", fontsize=9.8)
fig.tight_layout()
fig.text(0.5, -0.03, "A: Stewart (2008) p. 97–99: type I water passes 10 % of 465 nm light to 90 m (c = ln 10/90); the other curves are illustrative.  B: Hartmann §4.3 (atmosphere 2.46 m of water, top 70 m of ocean ≈ 28.5×) with 1 m of rock for Stewart's seasonal land layer.  "
         "C: the global mean surface budget of Stewart Fig. 5.6 (342 W m⁻² incoming; 168 solar + 324 back radiation = 390 + 78 + 24).  Numbers: cl_neena_numbers.py (cl18).", ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_cl18_ocean_heat")

# ============================================================================================================== CL19
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.7))
Az, f, rho, tau = 0.1, 1e-4, 1025.0, 0.1
DE = np.sqrt(2 * Az / f)
aa = 1 / DE
W = tau / (rho * Az) / ((1 + 1j) * aa)
zz = np.linspace(0, -3 * np.pi * DE, 600)
w = W * np.exp((1 + 1j) * aa * zz)
a = ax[0]
a.plot(w.real * 100, w.imag * 100, color=BLUE, lw=2.2)
labs = {0: ("z = 0", (0.08, 0.1), "left"), -DE: ("z = −D_E", (0.1, -0.05), "left"), -np.pi * DE / 2: ("z = −πD_E/2", (-0.06, -0.1), "right"), -np.pi * DE: ("z = −πD_E", (0.05, 0.12), "left")}
for zk, (txt, off, ha) in labs.items():
    i = np.argmin(abs(zz - zk))
    a.annotate("", xy=(w[i].real * 100, w[i].imag * 100), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=ORANGE if zk == 0 else MUTED, lw=1.8 if zk == 0 else 1.1))
    a.text(w[i].real * 100 + off[0], w[i].imag * 100 + off[1], txt, fontsize=7.8, color=INK, ha=ha)
a.annotate("wind stress", xy=(1.1, 0.35), xytext=(0.15, 0.35), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.0), fontsize=8, color=RED, va="center")
a.set_aspect("equal"); a.set_xlabel("u (cm/s)"); a.set_ylabel("v (cm/s)"); a.set_xlim(-1.5, 2.6); a.set_ylim(-2.6, 0.7)
a.set_title("A  Ekman spiral (northern hemisphere)", fontsize=9.8)

b = ax[1]
lat = np.linspace(8, 80, 200)
fv = 2 * OMEGA * np.sin(np.radians(lat))
for tt, col in ((0.05, AQUA), (0.1, BLUE), (0.2, ORANGE)):
    b.plot(lat, tt / fv / rho, color=col, lw=2.2, label="τ = %.2f N m⁻²" % tt)
b.set_xlabel("latitude (deg)"); b.set_ylabel("Ekman volume transport per metre  M/ρ = τ/(ρ f)  (m² s⁻¹)")
b.legend(fontsize=8, frameon=False)
b.text(35, 5.0, "perpendicular to the wind (to the right\nin the NH); grows towards the equator\n(the theory breaks down there)", fontsize=7.8, color=INK)
b.set_title("B  Ekman transport = τ/(ρ f)", fontsize=9.8)

c = ax[2]
c.set_xlim(0, 10); c.set_ylim(-4.2, 2.2); c.axis("off")
c.fill_between([2.2, 10], -4.1, 0, color="#cfe3f7", alpha=0.7)
c.fill_between([0, 2.2], -4.1, 1.2, color="#d9c9a3", alpha=0.9)
c.plot([2.2, 10], [0, 0], color=BLUE, lw=1.6)
c.plot([2.2, 10], [-0.9, -0.9], color=MUTED, lw=1.0, ls="--")
c.text(9.9, -0.75, "base of the mixed/Ekman layer", fontsize=7.6, ha="right", color=MUTED)
c.annotate("", xy=(8.8, -0.45), xytext=(3.2, -0.45), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.4))
c.text(6.0, -0.2, "Ekman transport away from the coast", fontsize=8.2, ha="center", color=RED)
c.annotate("", xy=(2.9, -0.7), xytext=(2.9, -3.3), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.4))
c.text(3.15, -2.4, "upwelling\n(cold, nutrient-rich)", fontsize=8, color=BLUE)
c.text(0.4, 0.2, "coast", fontsize=8.5, color=INK)
c.text(6.0, 1.6, "alongshore wind (equatorward on a west coast in the NH)\n⊗ / ⊙ into / out of the page", fontsize=8, ha="center", color=INK)
c.set_title("C  coastal upwelling (cross-section, schematic)", fontsize=9.8)
fig.tight_layout()
fig.text(0.5, -0.03, "A: constant eddy viscosity: the current rotates clockwise with depth, decays as e^{z/D_E}, is 1/e of the surface speed at z = −D_E (rotated 57.3°) and opposite to it at z = −πD_E where it is e^{−π} = 4.3 % of the surface speed (Lecture 21 attributes 1/e to the depth of reversal: `[!verify]`).  "
         "B: Stewart (9.26): M = τ/f.  C: Lecture 21 / Stewart Fig. 9.8.  Numbers: cl_neena_numbers.py (cl19).", ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_cl19_ekman")

# ============================================================================================================== CL20
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.6))
def section(a, el_nino):
    a.set_xlim(0, 10); a.set_ylim(-3.2, 2.6); a.axis("off")
    x = np.linspace(0, 10, 200)
    th = (-0.9 - 1.2 * (1 - x / 10) ** 1.0 * 0 + (-1.5 + 1.2 * x / 10)) if not el_nino else (-1.75 + 0.15 * x / 10)
    # surface warm pool: SST colour band
    a.fill_between(x, th, 0, color="#cfe3f7", alpha=0.65)
    a.fill_between(x, -3.2, th, color="#9bb9d6", alpha=0.65)
    a.plot(x, th, color=BLUE, lw=2.4)
    a.text(8.7, th[-1] - 0.35 if not el_nino else th[-1] - 0.35, "thermocline", fontsize=8, color=BLUE, ha="right")
    wp = 2.6 if not el_nino else 5.8
    a.add_patch(Polygon([[wp - 1.8, 0.7], [wp + 1.8, 0.7], [wp + 1.1, 1.6], [wp - 1.1, 1.6]], fc="#e8e8e8", ec=MUTED, alpha=0.9))
    a.text(wp, 1.15, "deep convection", fontsize=7.8, ha="center")
    for xs_, ys_, dx, dy in ((wp, 0.7, 0, -0.55), ):
        pass
    a.annotate("", xy=(1.1 if not el_nino else 3.3, 0.1), xytext=(9.0 if not el_nino else 8.4, 0.1), arrowprops=dict(arrowstyle="-|>", color=RED, lw=2.8 if not el_nino else 1.2))
    a.text(5.0, 0.3, "surface easterlies" + (" (strong)" if not el_nino else " (weak)"), fontsize=8, ha="center", color=RED)
    a.text(0.2, -3.0, "west", fontsize=8); a.text(9.8, -3.0, "east", fontsize=8, ha="right")
    a.text(1.2 if not el_nino else 1.0, -0.55, "warm SST\ndeep mixed layer" if not el_nino else "cooler SST", fontsize=7.8, color=INK)
    a.text(8.3 if not el_nino else 8.3, -0.55, "cold tongue\nupwelling" if not el_nino else "warm SST\n(no cold tongue)", fontsize=7.8, color=INK, ha="center")
a = ax[0]; section(a, False); a.set_title("A  mean state: Walker circulation (schematic)", fontsize=9.8)
b = ax[1]; section(b, True); b.set_title("B  El Niño: weaker trades, flatter thermocline", fontsize=9.8)
c = ax[2]
H = np.linspace(50, 250, 100)
L = 1.5e7
for deta, col in ((0.25, AQUA), (0.5, BLUE), (0.75, ORANGE)):
    c.plot(H, 1025 * 9.81 * H * deta / L, color=col, lw=2.2, label="Δη = %.2f m" % deta)
c.axhspan(1.3 * (0.5 + 0.071 * 5) * 1e-3 * 25, 1.3 * (0.5 + 0.071 * 7) * 1e-3 * 49, color=GRID, alpha=0.9)
c.text(52, 0.047, "bulk stress ρ_a C_D U² for U = 5–7 m/s", fontsize=7.8, color=INK)
c.axvline(150, color=MUTED, lw=1, ls=":")
c.set_xlabel("layer thickness H pushed by the wind  (m)"); c.set_ylabel("balancing wind stress  ρ g H Δη/L  (N m⁻²)")
c.legend(fontsize=8, frameon=False, loc="upper left")
c.set_title("C  a 0.5 m slope needs ≈ 0.05 N m⁻²", fontsize=9.8)
fig.tight_layout()
fig.text(0.5, -0.03, "A, B: cartoon cross-sections of the equatorial Pacific as described on Lecture 23's slides (not data).  C: balance of the zonal pressure force of the slide's 0.5 m sea-level difference over an assumed 15,000 km against the wind stress on a layer H "
         "(my illustration); the grey band is Stewart's bulk formula τ = ρ_a C_D U₁₀² with C_D = (0.50 + 0.071 U₁₀)×10⁻³ for 5–7 m/s.  Numbers: cl_neena_numbers.py (cl20).", ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_cl20_enso")

# ============================================================================================================== CL21
fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.7))
a = ax[0]
Tg, Sg = np.meshgrid(np.linspace(-3, 30, 200), np.linspace(33, 37.5, 200))
rho_ = 1027 * (1 - 2e-4 * (Tg - 10) + 7.6e-4 * (Sg - 35))
cs = a.contour(Sg, Tg, rho_, levels=np.arange(1022, 1031, 1.0), colors=MUTED, linewidths=0.9)
a.clabel(cs, fmt="%.0f", fontsize=7)
for nm, T, S, col in (("tropical\nsurface", 27, 35.5, ORANGE), ("subtropical\nsalty surface", 25, 37.0, ORANGE), ("subpolar\nsurface", 5, 33.5, AQUA), ("N. Atlantic\nwinter", 2, 35.1, BLUE), ("Weddell\nshelf brine", -1.8, 34.8, VIOLET)):
    a.plot([S], [T], "o", color=col, ms=7)
    a.text(S + 0.06, T + 0.6, nm, fontsize=7.4, color=INK)
a.axhline(-1.8, color=GRID, lw=1.2)
a.set_xlabel("salinity (psu)"); a.set_ylabel("temperature (°C)"); a.set_xlim(33, 37.5); a.set_ylim(-3, 30)
a.set_title("A  T–S diagram, density contours (teaching EOS)", fontsize=9.8)

b = ax[1]
fr = np.linspace(0, 0.3, 100)
for Si, col in ((0, BLUE), (5, ORANGE)):
    b.plot(100 * fr, (35 - fr * Si) / (1 - fr), color=col, lw=2.3, label="ice salinity %d" % Si)
b.set_xlabel("fraction of seawater frozen (%)"); b.set_ylabel("salinity of the remaining water (psu)")
b.legend(fontsize=8, frameon=False, loc="upper left")
b.text(1, 42, "S = (35 − f·S_ice)/(1 − f)\n10 % frozen: +3.3 to +3.9 psu", fontsize=8, color=INK)
b.set_title("B  brine rejection (mass balance)", fontsize=9.8)

c = ax[2]
c.set_xlim(0, 10); c.set_ylim(-4.2, 1.6); c.axis("off")
c.fill_between([0, 10], -4.1, 0, color="#cfe3f7", alpha=0.6)
c.fill_between([0, 1.1], -1.5, 0, color="white"); c.fill_between([8.9, 10], -1.0, 0, color="white")
c.text(0.0, 1.0, "Antarctica", fontsize=8.2); c.text(9.9, 1.0, "Greenland", fontsize=8.2, ha="right")
c.annotate("", xy=(1.3, -3.7), xytext=(1.3, -0.4), arrowprops=dict(arrowstyle="-|>", color=VIOLET, lw=2.6))
c.text(1.5, -2.0, "AABW\n(Weddell,\nbrine)", fontsize=7.8, color=VIOLET)
c.annotate("", xy=(8.5, -2.4), xytext=(8.5, -0.4), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.6))
c.annotate("", xy=(2.6, -2.0), xytext=(8.3, -2.0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.0))
c.text(8.3, -1.3, "NADW", fontsize=8, color=BLUE, ha="right")
c.text(5.4, -1.8, "southward at ~2–4 km", fontsize=7.8, color=BLUE, ha="center")
c.annotate("", xy=(9.0, -0.2), xytext=(4.0, -0.2), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.8))
c.text(5.5, 0.25, "warm surface flow north", fontsize=7.8, color=ORANGE, ha="center")
c.annotate("", xy=(4.0, -0.5), xytext=(4.0, -3.5), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.6, ls="--"))
c.text(4.1, -3.4, "return/upwelling\n(Southern Ocean)", fontsize=7.6, color=MUTED)
c.set_title("C  the deep overturning, schematic", fontsize=9.8)
fig.tight_layout()
fig.text(0.5, -0.03, "A: a linearised teaching equation of state ρ = 1027[1 − 2×10⁻⁴(T−10) + 7.6×10⁻⁴(S−35)] (coefficients assumed; the real one is nonlinear, Lecture 24); the T and S of the five water types are illustrative, not data.  "
         "B: freezing a fraction f of 35 psu seawater into ice of salinity S_ice leaves water of salinity (35 − f S_ice)/(1 − f).  C: after Lecture 24's NADW/AABW slide (cartoon).  Numbers: cl_neena_numbers.py (cl21).", ha="center", fontsize=7.6, color=MUTED, wrap=True)
save(fig, "fig_cl21_thermohaline")
print("done")
