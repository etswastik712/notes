"""CL04 - feedback amplification  Lambda = Lambda_P / (1 - f)  and Planck sensitivity vs temperature."""
from figlib import *

fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 3.8), gridspec_kw={"width_ratios": [1.1, 1]})

# (a) gain curve
LP = 1 / (4 * SIGMA * 255.0**3)
f = np.linspace(-1.5, 0.93, 500)
a.plot(f, LP / (1 - f), color=BLUE)
a.axvline(1, color=RED, lw=1, ls="--")
a.annotate("f = 1: runaway\n(no steady state in\nthe linear model)", (1.0, 1.25), xytext=(-6, 0), textcoords="offset points",
           ha="right", fontsize=8.5)
a.axhline(LP, color=MUTED, lw=0.8, ls=":")
a.annotate(rf"no feedback: $\Lambda_P$ = {LP:.2f} K/(W m$^{{-2}}$)", (-1.45, LP), xytext=(0, 6), textcoords="offset points", fontsize=8.5)
for fv, txt, dy in [(0.5, "f = 0.5 doubles it", -4), (-1.0, "f = −1 halves it", -16)]:
    a.plot([fv], [LP / (1 - fv)], "o", color=BLUE, ms=5)
    if fv > 0:
        a.annotate(txt, (fv, LP / (1 - fv)), xytext=(-8, 6), textcoords="offset points", ha="right", fontsize=8.5)
    else:
        a.annotate(txt, (fv, LP / (1 - fv)), xytext=(-1.4, 0.75), textcoords="data", ha="left", fontsize=8.5,
                   arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xlim(-1.5, 1.2)
a.set_ylim(0, 2.0)
a.set_xlabel("total feedback factor  f = Σ f$_i$")
a.set_ylabel(r"sensitivity  $\Lambda$  (K per W m$^{-2}$)")
a.set_title("Positive feedback amplifies; f → 1 diverges", fontsize=10.5)

# (b) Planck sensitivity vs T
T = np.linspace(200, 330, 200)
b.plot(T, 1 / (4 * SIGMA * T**3), color=ORANGE)
for Tv, lab in [(255, "255 K (airless Earth)"), (288, "288 K (actual surface)")]:
    y = 1 / (4 * SIGMA * Tv**3)
    b.plot([Tv], [y], "o", color=ORANGE, ms=5)
    b.annotate(f"{lab}\n{y:.2f} K/(W m$^{{-2}}$)", (Tv, y), xytext=(8, 10), textcoords="offset points", fontsize=8.5)
b.set_xlabel("T (K)")
b.set_ylabel(r"$\Lambda_P=1/(4\sigma T^3)$  (K per W m$^{-2}$)")
b.set_title("Warmer planets are less sensitive")
b.set_ylim(0.1, 0.5)
fig.tight_layout()
save(fig, "fig_cl04_feedback_gain")
