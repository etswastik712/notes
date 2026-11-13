"""TH10 - entropy and Gibbs energy of mixing; G(extent) of SO2 + 1/2 O2 <=> SO3 at three pressures; extent against pressure for Delta nu = -1/2, 0, +1."""
from figlib import *
import math
from scipy import optimize

R = 8.314462618
fig, ax = plt.subplots(1, 3, figsize=(14.6, 4.7))

# A: mixing ---------------------------------------------------------------------------------------------------------------------------------------------
a = ax[0]
x = np.linspace(0.0005, 0.9995, 600)
s = -R * (x * np.log(x) + (1 - x) * np.log(1 - x))
a.plot(x, s, color=BLUE, lw=2.4, label="ΔS_mix  (J mol⁻¹ K⁻¹)")
a.set_xlabel("mole fraction x of gas A"); a.set_ylabel("ΔS_mix  (J mol⁻¹ K⁻¹)", color=BLUE)
a.set_xlim(0, 1); a.set_ylim(0, 6.6)
a2 = a.twinx()
a2.spines["right"].set_visible(True); a2.grid(False)
a2.plot(x, -298.15 * s / 1000, color=ORANGE, lw=2.4)
a2.set_ylabel("ΔG_mix at 298.15 K  (kJ mol⁻¹)", color=ORANGE); a2.set_ylim(-1.97, 0.0)
xa = 0.79
sa = -R * (xa * math.log(xa) + (1 - xa) * math.log(1 - xa))
a.plot([xa], [sa], "o", color=INK, ms=6)
a.annotate("air-like (0.79 : 0.21)\nΔS = 4.27 J mol⁻¹K⁻¹\nΔG = −1.27 kJ mol⁻¹", xy=(xa, sa), xytext=(0.04, 2.2), fontsize=8.2, color=INK, arrowprops=dict(arrowstyle="->", color=INK))
a.plot([0.5], [R * math.log(2)], "s", color=INK, ms=6)
a.text(0.5, R * math.log(2) + 0.3, "R ln 2 = 5.76 (maximum)", ha="center", fontsize=8.2, color=INK)
a.set_title("A  ideal gases: mixing is entropic, ΔH = 0", fontsize=9.8)

# B: G(extent) at three pressures --------------------------------------------------------------------------------------------------------------
b = ax[1]
K = 10.0
def comp(e):
    n = np.array([1 - e, 0.5 - 0.5 * e, e]); return n, n.sum()
def G(e, P):
    n, N = comp(e); xx = n / N
    return -e * math.log(K) + float((n * np.log(xx * P)).sum())
def Kf(e, P):
    n, N = comp(e); xx = n / N
    return xx[2] / (xx[0] * math.sqrt(xx[1])) * P ** (-0.5)
es = np.linspace(0.0005, 0.9995, 800)
for P, col in ((0.1, VIOLET), (1.0, BLUE), (10.0, ORANGE)):
    g = np.array([G(e, P) for e in es]); g -= g[0]
    b.plot(es, g, color=col, lw=2.2, label="P = %g bar" % P)
    ee = optimize.brentq(lambda e: Kf(e, P) - K, 1e-9, 1 - 1e-9)
    b.plot([ee], [G(ee, P) - G(es[0], P)], "o", color=col, ms=6)
    b.text(ee, G(ee, P) - G(es[0], P) - 0.25, "%.3f" % ee, ha="center", fontsize=8.2, color=col)
b.set_xlabel("extent of reaction ε  (start: 1 SO₂ + ½ O₂)"); b.set_ylabel("[G(ε) − G(0)] / RT")
b.set_xlim(0, 1); b.set_ylim(-5.0, 4.5)
b.legend(frameon=False, fontsize=8.5, loc="upper right")
b.text(0.03, 3.4, "K = 10 (illustrative); the minimum sits where\nΣνᵢμᵢ = 0, i.e. Q = K; higher P moves it right\n(Σν = −½: fewer moles of gas)", fontsize=8.0, color=INK, bbox=dict(fc=SURFACE, ec="none", alpha=0.9))
b.set_title("B  G(ε) has an interior minimum (the mixing terms)", fontsize=9.8)

# C: extent vs pressure ---------------------------------------------------------------------------------------------------------------------------
c = ax[2]
Ps = np.logspace(-1.5, 3, 200)
def ext(Pv, kind):
    if kind == "so3":
        return optimize.brentq(lambda e: Kf(e, Pv) - 10.0, 1e-9, 1 - 1e-9)
    if kind == "hi":
        return math.sqrt(50.0) / (2 + math.sqrt(50.0))
    return math.sqrt(0.15 / (0.15 + 4 * Pv))
c.semilogx(Ps, [ext(p, "so3") for p in Ps], color=BLUE, lw=2.4, label="SO₂ + ½O₂ ⇌ SO₃   Σν = −½  (K = 10)")
c.semilogx(Ps, [ext(p, "hi") for p in Ps], color=AQUA, lw=2.4, label="H₂ + I₂ ⇌ 2HI   Σν = 0  (K = 50)")
c.semilogx(Ps, [ext(p, "n2o4") for p in Ps], color=ORANGE, lw=2.4, label="N₂O₄ ⇌ 2NO₂   Σν = +1  (K = 0.15)")
c.set_xlabel("total pressure P / bar"); c.set_ylabel("equilibrium extent ε_eq"); c.set_ylim(0, 1.02)
c.legend(frameon=False, fontsize=8.0, loc="center right")
c.set_title("C  pressure shifts the equilibrium only if Σν ≠ 0", fontsize=9.8)

fig.tight_layout()
save(fig, "fig_th10_mixing_reacting")
