"""CM01 figure: brachistochrone paths; second variation of the oscillator action. .venv/bin/python -W ignore scripts/fig_cm01.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad
g = 9.81; X, Y = 1.0, 0.5
t1 = brentq(lambda t: (1 - np.cos(t)) / (t - np.sin(t)) - Y / X, 0.1, 6.2); a = X / (t1 - np.sin(t1))
fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.4))
A = ax[0]
t = np.linspace(0, t1, 300)
A.plot(a * (t - np.sin(t)), a * (1 - np.cos(t)), color=BLUE, label="cycloid  $T=0.570$ s")
A.plot([0, X], [0, Y], color=ORANGE, label="straight line  $T=0.714$ s")
xs = np.linspace(0, X, 300)
A.plot(xs, Y * np.sqrt(xs / X), color=AQUA, label="parabola $y\\propto\\sqrt{x}$  $T=0.583$ s")
A.plot(xs, Y * (xs / X) ** 0.7, color=VIOLET, label="$y\\propto x^{0.7}$  $T=0.607$ s")
A.invert_yaxis(); A.set_aspect("equal"); A.set_xlabel("$x$ (m)"); A.set_ylabel("depth $y$ (m)")
A.legend(fontsize=8, loc="upper right"); A.set_title("A  Brachistochrone: fastest of four paths")
B = ax[1]
w = 2.0
Ts = np.linspace(0.2, 3.0, 400)
for n, col in ((1, BLUE), (2, ORANGE), (3, AQUA)):
    B.plot(Ts, Ts / 4 * ((n * np.pi / Ts) ** 2 - w ** 2), color=col, label=f"mode $n={n}$")
B.axhline(0, color=MUTED); B.axvline(np.pi / w, color=RED, ls=":"); B.text(np.pi / w + 0.03, -1.8, "$\\omega T=\\pi$", color=RED)
B.set_ylim(-2.5, 6); B.set_xlabel("duration $T$"); B.set_ylabel("$(S-S_0)/\\epsilon^2$  ($m=1,\\omega=2$)")
B.legend(fontsize=8); B.set_title("B  Second variation: minimum until $\\omega T=\\pi$")
C = ax[2]
T = 1.4; tt = np.linspace(0, T, 400)
x0 = np.sin(w * tt) / np.sin(w * T)
C.plot(tt, x0, color=INK, lw=2.2, label="true path (stationary)")
for eps, col in ((0.3, BLUE), (-0.3, ORANGE)):
    C.plot(tt, x0 + eps * np.sin(np.pi * tt / T), color=col, ls="--", label=f"varied, $\\epsilon={eps}$")
C.set_xlabel("$t$"); C.set_ylabel("$x$"); C.legend(fontsize=8); C.set_title("C  Varied paths share endpoints ($\\delta q=0$ at both ends)")
fig.tight_layout(); save(fig, "fig_cm01_variational")

# ---- soap film figure
from scipy.integrate import quad as _quad
from scipy.optimize import brentq as _bq
from scipy.special import ellipk
fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.4))
cs = np.linspace(0.12, 1.0, 400)
A = ax[0]
A.plot(cs, cs * np.arccosh(1 / cs), color=BLUE)
hmax = (cs * np.arccosh(1 / cs)).max(); cm = cs[np.argmax(cs * np.arccosh(1 / cs))]
A.axhline(0.5, color=ORANGE, ls="--"); A.plot([0.2351, 0.8483], [0.5, 0.5], "o", color=ORANGE)
A.axhline(hmax, color=RED, ls=":"); A.text(0.62, hmax + 0.012, f"$h_{{max}}={hmax:.4f}$", color=RED)
A.set_xlabel("waist parameter $c/R$"); A.set_ylabel("half-separation $h/R=c\\,\\mathrm{arccosh}(R/c)$")
A.set_title("A  Two catenaries for $h<h_{max}$ (dots: $h=0.5$)")
B = ax[1]
def area(c, h): return _quad(lambda z: 2 * np.pi * c * np.cosh(z / c) ** 2, -h, h)[0]
hs = np.linspace(0.05, hmax - 1e-4, 300)
big, small = [], []
for h in hs:
    f = lambda c: c * np.cosh(h / c) - 1
    big.append(area(_bq(f, cm, 1.0), h)); small.append(area(_bq(f, h/600, cm), h))
B.plot(hs, big, color=BLUE, label="wide catenoid (minimum)"); B.plot(hs, small, color=ORANGE, label="narrow catenoid (saddle)")
B.axhline(2 * np.pi, color=MUTED, ls="--", label="two discs $2\\pi$"); B.axvline(0.5277, color=AQUA, ls=":"); B.text(0.535, 1.0, "$h=0.5277$", color=AQUA)
B.set_ylim(0, 9.5); B.set_xlabel("$h/R$"); B.set_ylabel("area / $R^2$"); B.legend(fontsize=8); B.set_title("B  Area: discs win beyond $h=0.5277$")
C = ax[2]
th = np.linspace(0.01, 3.1, 300)
C.plot(th, 2 / np.pi * ellipk(np.sin(th / 2) ** 2), color=BLUE, label="exact $T/T_0=\\frac{2}{\\pi}K$")
C.plot(th, 1 + th ** 2 / 16, color=ORANGE, ls="--", label="$1+\\theta_0^2/16$")
C.set_ylim(0.9, 4); C.set_xlabel("amplitude $\\theta_0$ (rad)"); C.set_ylabel("$T/T_0$"); C.legend(fontsize=8); C.set_title("C  Pendulum period grows without bound as $\\theta_0\\to\\pi$")
fig.tight_layout(); save(fig, "fig_cm01_soapfilm")
