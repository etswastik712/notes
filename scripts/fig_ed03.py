"""ED03 figure: displacement current in a capacitor; refraction of field lines. .venv/bin/python -W ignore scripts/fig_ed03.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
mu0 = 4e-7 * np.pi; I = 2.0; R = 0.05
fig, ax = plt.subplots(1, 3, figsize=(15.5, 4.4))
A = ax[0]
r = np.linspace(0.002, 0.15, 400)
B = np.where(r <= R, mu0 * I * r / (2 * np.pi * R ** 2), mu0 * I / (2 * np.pi * r))
A.plot(r * 100, B * 1e6, color=BLUE, label="$B(r)$ with displacement current")
A.plot(r * 100, mu0 * I / (2 * np.pi * r) * 1e6, color=ORANGE, ls="--", label="$\\mu_0I/2\\pi r$ (no gap current)")
A.axvline(R * 100, color=MUTED, ls=":"); A.set_ylim(0, 25)
A.set_xlabel("$r$ (cm)"); A.set_ylabel("$B$ ($\\mu$T)"); A.legend(fontsize=8); A.set_title("A  Charging capacitor ($R=5$ cm, $I=2$ A)")
Bx = ax[1]
th1 = np.radians(np.linspace(0, 89, 300))
for eps, col in ((2, BLUE), (4, ORANGE), (80, AQUA)):
    Bx.plot(np.degrees(th1), np.degrees(np.arctan(np.tan(th1) * eps)), color=col, label=f"$\\epsilon_2/\\epsilon_1={eps}$")
Bx.plot([0, 89], [0, 89], color=MUTED, ls=":")
Bx.set_xlabel("$\\theta_1$ (deg from normal)"); Bx.set_ylabel("$\\theta_2$ (deg)"); Bx.legend(fontsize=8)
Bx.set_title("B  $\\tan\\theta_2/\\tan\\theta_1=\\epsilon_2/\\epsilon_1$")
C = ax[2]
C.set_xlim(-1, 1); C.set_ylim(-1, 1); C.axhspan(-1, 0, color=GRID, alpha=0.8); C.axhline(0, color=MUTED)
th1 = np.radians(60); th2 = np.arctan(np.tan(th1) * 4)
for xo in (-0.6, 0, 0.6):
    C.annotate("", xy=(xo + 0.0, 0), xytext=(xo - 0.5 * np.sin(th1) * 0.0 - 0.5 * np.sin(th1), 0.5 * np.cos(th1)), arrowprops=dict(arrowstyle="->", color=BLUE))
    C.annotate("", xy=(xo + 0.5 * np.sin(th2), -0.5 * np.cos(th2)), xytext=(xo, 0), arrowprops=dict(arrowstyle="->", color=ORANGE))
C.text(-0.95, 0.85, "$\\epsilon_1=1$", fontsize=9); C.text(-0.95, -0.9, "$\\epsilon_2=4$", fontsize=9)
C.text(0.1, 0.45, "$\\theta_1=60^\\circ$", color=BLUE); C.text(0.45, -0.5, "$\\theta_2=81.8^\\circ$", color=ORANGE)
C.set_aspect("equal"); C.grid(False); C.set_xticks([]); C.set_yticks([]); C.set_title("C  Lines bend away from the normal")
fig.tight_layout(); save(fig, "fig_ed03_maxwell")
