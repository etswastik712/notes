"""QM09 figures: Stern-Gerlach apparatus and screen patterns, sequential SG on the Bloch sphere, spin dynamics,
Bell/CHSH and spin-j beams, and the cross-subject parallels.
.venv/bin/python -W ignore scripts/fig_qm09.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
from matplotlib.patches import Polygon, FancyArrowPatch  # noqa
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401
from mpl_toolkits.mplot3d.art3d import Line3D  # noqa: F401

import numpy as np

MU_B = 9.2740100783e-24
U_AMU = 1.66053906660e-27
MU_P = 1.41060679736e-26
M_AG = 107.8682 * U_AMU
T_OVEN = 1300.0
G_GRAD = 1000.0
L1, L2 = 0.035, 0.010


def sphere(ax, alpha=0.10):
    u = np.linspace(0, 2 * np.pi, 60)
    v = np.linspace(0, np.pi, 30)
    X = np.outer(np.cos(u), np.sin(v)); Y = np.outer(np.sin(u), np.sin(v)); Z = np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(X, Y, Z, color=BLUE, alpha=alpha, linewidth=0, shade=False)
    t = np.linspace(0, 2 * np.pi, 200)
    ax.plot(np.cos(t), np.sin(t), 0 * t, color=MUTED, lw=0.7, alpha=0.7)
    ax.plot(np.cos(t), 0 * t, np.sin(t), color=MUTED, lw=0.7, alpha=0.5)
    ax.plot(0 * t, np.cos(t), np.sin(t), color=MUTED, lw=0.7, alpha=0.5)
    for vec, lab in (((1.35, 0, 0), "$x$"), ((0, 1.35, 0), "$y$"), ((0, 0, 1.35), "$z$")):
        ax.plot([0, vec[0]], [0, vec[1]], [0, vec[2]], color=INK, lw=0.8)
        ax.text(vec[0] * 1.07, vec[1] * 1.07, vec[2] * 1.07, lab, ha="center", va="center", fontsize=10)
    ax.set_axis_off()
    ax.set_box_aspect((1, 1, 1))
    ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05); ax.set_zlim(-1.05, 1.05)


def arrow3(ax, v, color, lw=2.4, label=None, off=(0.08, 0.0, 0.08)):
    ax.plot([0, v[0]], [0, v[1]], [0, v[2]], color=color, lw=lw)
    ax.scatter([v[0]], [v[1]], [v[2]], color=color, s=28, depthshade=False)
    if label:
        ax.text(v[0] + off[0], v[1] + off[1], v[2] + off[2], label, color=INK, fontsize=9)


# ------------------------------------------------------------------ Figure 1: apparatus
def screen_pattern(z, classical, sigma_beam=3.0e-5, nv=400):
    """density of impacts (arbitrary units) on z grid (m) for an effusive silver beam"""
    v = np.linspace(150, 1800, nv)
    wv = v ** 3 * np.exp(-M_AG * v ** 2 / (2 * 1.380649e-23 * T_OVEN))
    wv /= wv.sum()
    a = MU_B * G_GRAD / M_AG
    zmax = 0.5 * a * (L1 / v) ** 2 + a * (L1 / v) * (L2 / v)           # m, for mu_z = +mu_B
    dens = np.zeros_like(z)
    if classical:
        ss = np.linspace(-1, 1, 201)
        for s in ss:
            for vi, w, zm in zip(v, wv, zmax):
                dens += w * np.exp(-0.5 * ((z - s * zm) / sigma_beam) ** 2)
    else:
        for s in (-1.0, 1.0):
            for vi, w, zm in zip(v, wv, zmax):
                dens += w * np.exp(-0.5 * ((z - s * zm) / sigma_beam) ** 2)
    return dens / dens.max()


def fig_apparatus():
    fig = plt.figure(figsize=(15.8, 4.9))
    # A: magnet cross-section with field lines (S pole with the knife edge on top, N below: B points up, dB_z/dz > 0)
    a = fig.add_subplot(1, 3, 1)
    a.add_patch(Polygon([[-1.6, 1.55], [1.6, 1.55], [1.6, 0.85], [0.18, 0.85], [0.0, 0.55], [-0.18, 0.85], [-1.6, 0.85]], closed=True, fc="#c4d5e8", ec=INK, lw=1.2))
    a.add_patch(Polygon([[-1.6, -1.55], [1.6, -1.55], [1.6, -0.85], [0.55, -0.85], [0.45, -0.55], [-0.45, -0.55], [-0.55, -0.85], [-1.6, -0.85]], closed=True, fc="#e5c9c4", ec=INK, lw=1.2))
    a.text(-1.45, 1.2, "S", fontsize=13, weight="bold"); a.text(-1.45, -1.2, "N", fontsize=13, weight="bold")
    X, Z = np.meshgrid(np.linspace(-1.3, 1.3, 40), np.linspace(-0.5, 0.5, 40))
    alpha, B0 = 0.7, 1.0
    Bx, Bz = -alpha * X, (B0 + alpha * Z)                # B_z grows toward the knife edge; div B = -alpha + alpha = 0
    a.streamplot(X, Z, Bx, Bz, color=MUTED, linewidth=0.9, density=0.8, arrowsize=0.9)
    a.plot([0], [0], "o", color=ORANGE, ms=7, zorder=5)
    a.annotate("", xy=(0, 0.46), xytext=(0, 0.04), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.4), zorder=6)
    a.text(0.1, 0.27, "$F_z$", fontsize=10, color=INK, va="center", bbox=dict(fc=SURFACE, ec="none", pad=1.5), zorder=7)
    a.text(0, -1.85, "atoms fly along $y$ (out of the page);  $F_z=\\mu_z\\,\\partial_zB_z$,\n$\\mu_z>0$ is pushed up, towards the knife edge", ha="center", va="top", fontsize=8.5, color=INK)
    a.set_xlim(-1.65, 1.65); a.set_ylim(-2.35, 1.65); a.set_aspect("equal"); a.set_axis_off()
    a.set_title("A  knife-edge and groove: $\\mathbf{B}=(-\\alpha x,\\,B_0+\\alpha z)$, $\\nabla\\cdot\\mathbf{B}=0$")
    # B: trajectories
    b = fig.add_subplot(1, 3, 2)
    v = math.sqrt(3 * 1.380649e-23 * T_OVEN / M_AG)
    acc = MU_B * G_GRAD / M_AG
    y = np.linspace(0, L1 + L2, 400)
    def zt(s, yy):
        t = yy / v
        inside = np.minimum(yy, L1) / v
        z = 0.5 * acc * s * inside ** 2 + np.where(yy > L1, acc * s * inside * (yy - L1) / v, 0.0)
        return z
    for s in np.linspace(-0.8, 0.8, 9):
        b.plot(y * 1e3, zt(s, y) * 1e3, color=GRID, lw=1.4, zorder=1)
    b.plot([], [], color=MUTED, lw=1.4, label="classical: any $\\mu_z$ in $[-\\mu,\\mu]$")
    b.plot(y * 1e3, zt(1.0, y) * 1e3, color=BLUE, lw=2.4, label="$\\mu_z=+\\mu_B$")
    b.plot(y * 1e3, zt(-1.0, y) * 1e3, color=ORANGE, lw=2.4, label="$\\mu_z=-\\mu_B$")
    b.axvspan(0, L1 * 1e3, color=GRID, alpha=0.5)
    b.axvline((L1 + L2) * 1e3, color=INK, lw=2.0)
    b.text(L1 * 500, 0.19, "magnet", ha="center", fontsize=9); b.text((L1 + L2) * 1e3 - 0.8, -0.19, "plate", ha="right", fontsize=9)
    b.set_xlabel("distance along the beam $y$ (mm)"); b.set_ylabel("deflection $z$ (mm)")
    b.set_ylim(-0.23, 0.23); b.legend(fontsize=8, loc="upper left", bbox_to_anchor=(0.0, 0.86))
    b.set_title("B  trajectories ($v=548$ m/s, $\\partial_zB_z=+10$ T/cm)")
    # C: screen pattern
    c = fig.add_subplot(1, 3, 3)
    zz = np.linspace(-0.6e-3, 0.6e-3, 600)
    cl = screen_pattern(zz, True)
    qm = screen_pattern(zz, False)
    c.fill_between(zz * 1e3, 0, cl, color=GRID, label="classical expectation")
    c.plot(zz * 1e3, cl, color=MUTED, lw=1.2)
    c.plot(zz * 1e3, qm, color=BLUE, lw=2.3, label="two spots: what is seen")
    c.set_xlabel("position on the plate $z$ (mm)"); c.set_ylabel("deposit density (rel.)")
    c.legend(fontsize=8.5, loc="upper right")
    c.set_title("C  plate: smear against two lips")
    fig.tight_layout()
    save(fig, "fig_qm09_apparatus")


# ------------------------------------------------------------------ Figure 2: sequential SG
def fig_sequential():
    fig = plt.figure(figsize=(15.8, 4.9))
    a = fig.add_subplot(1, 3, 1, projection="3d")
    sphere(a)
    arrow3(a, (0, 0, 1), BLUE, label="$|{+z}\\rangle$")
    arrow3(a, (1, 0, 0), ORANGE, label="$|{+x}\\rangle$ ($\\frac{1}{2}$)", off=(0.12, 0.0, 0.16))
    arrow3(a, (0, 0, -1), AQUA, label="$|{-z}\\rangle$ ($\\frac{1}{2}$)", off=(0.08, 0.0, -0.18))
    t = np.linspace(0, np.pi / 2, 40)
    a.plot(np.sin(t), 0 * t, np.cos(t), color=ORANGE, lw=1.6, ls="--")
    t2 = np.linspace(0, np.pi / 2, 40)
    a.plot(np.cos(t2), 0 * t2, -np.sin(t2), color=AQUA, lw=1.6, ls="--")
    a.view_init(elev=18, azim=-58)
    a.set_title("A  $z\\to x\\to z$ on the Bloch sphere")
    b = fig.add_subplot(1, 3, 2)
    th = np.linspace(0, np.pi, 400)
    b.plot(np.degrees(th), np.sin(th) ** 2 / 4, color=BLUE, lw=2.4, label="middle analyser measures: $\\sin^2\\theta/4$")
    b.plot([0, 180], [0, 0], color=ORANGE, lw=2.4, ls="--", label="middle beams recombined: 0")
    b.plot([90], [0.25], "o", color=BLUE, ms=7)
    b.annotate("$\\theta=90^\\circ$: $\\frac{1}{4}$\n(the $z$-$x$-$z$ experiment)", (90, 0.25), xytext=(122, 0.20), fontsize=9, arrowprops=dict(arrowstyle="-", color=MUTED))
    b.set_xlabel("angle $\\theta$ of the middle SG axis from $z$ (deg)"); b.set_ylabel("$P(S_z=-\\hbar/2)$ at the end")
    b.set_xlim(0, 180); b.set_ylim(-0.015, 0.29)
    b.legend(fontsize=8.2, loc="upper left")
    sec = b.secondary_xaxis("top", functions=(lambda d: d / 2, lambda d: d * 2))
    sec.set_xlabel("same curve for polarisers: angle $\\alpha=\\theta/2$ of the middle polariser (deg)", fontsize=8.5)
    b.set_title("B  sequential SG (and three polarisers)", pad=34)
    c = fig.add_subplot(1, 3, 3)
    Ns = np.arange(1, 41)
    P = np.cos(np.pi / (2 * Ns)) ** (2 * Ns)
    c.plot(Ns, P, "o-", color=BLUE, ms=4, label="$\\cos^{2N}(\\pi/2N)$")
    c.plot(Ns, 1 - np.pi ** 2 / (4 * Ns), color=ORANGE, ls="--", label="$1-\\pi^2/4N$")
    c.axhline(1, color=MUTED, lw=0.8)
    c.set_ylim(-0.05, 1.05); c.set_xlabel("number $N$ of intermediate SG analysers (axis turns by $\\pi/N$ each)")
    c.set_ylabel("fraction turned from $+z$ to $-z$")
    c.legend(fontsize=8.5, loc="lower right")
    c.set_title("C  many gentle filters turn the spin: $N\\to\\infty$ gives 1")
    fig.tight_layout()
    save(fig, "fig_qm09_sequential")


# ------------------------------------------------------------------ Figure 3: dynamics
def fig_dynamics():
    fig = plt.figure(figsize=(15.8, 4.9))
    a = fig.add_subplot(1, 3, 1, projection="3d")
    sphere(a)
    th0 = math.radians(60)
    ph = np.linspace(0, 2 * np.pi, 200)
    a.plot(np.sin(th0) * np.cos(ph), np.sin(th0) * np.sin(ph), np.cos(th0) + 0 * ph, color=BLUE, lw=2.2)
    arrow3(a, (math.sin(th0), 0, math.cos(th0)), BLUE, label="$\\langle\\mathbf{S}\\rangle$ precesses", off=(0.1, 0, 0.12))
    a.plot([0, 0], [0, 0], [0, 1.0], color=INK, lw=2.0, ls=":")
    a.text(0.05, 0.0, 1.12, "$\\mathbf{B}$", fontsize=10)
    tt = np.linspace(0, np.pi, 80)
    a.plot(0 * tt, np.sin(tt), np.cos(tt), color=ORANGE, lw=2.6)
    a.text(0.0, 0.62, -0.95, "resonant $\\pi$-pulse\n(rotating frame)", color=INK, fontsize=8.5)
    a.view_init(elev=16, azim=-50)
    a.set_title("A  Larmor precession and a Rabi flip")
    b = fig.add_subplot(1, 3, 2)
    x = np.linspace(0, 3, 600)
    for D, col in ((0, BLUE), (0.5, ORANGE), (1.0, AQUA), (2.0, VIOLET)):
        W = math.sqrt(1 + D ** 2)
        b.plot(x, (1 / W ** 2) * np.sin(W * 2 * np.pi * x / 2) ** 2, color=col, lw=2, label=f"$\\Delta/\\Omega={D:g}$: max $={1/(1+D**2):.2f}$")
    b.set_xlabel("$\\Omega t/2\\pi$"); b.set_ylabel("spin-flip probability $P(t)$")
    b.set_ylim(-0.02, 1.05); b.legend(fontsize=8.3, loc="upper right", ncol=1)
    b.set_title("B  Rabi: $P=\\frac{\\Omega^2}{\\Omega^2+\\Delta^2}\\sin^2\\frac{\\sqrt{\\Omega^2+\\Delta^2}\\,t}{2}$")
    c = fig.add_subplot(1, 3, 3)
    phi = np.linspace(0, 8 * np.pi, 800)
    c.plot(phi / np.pi, 1 + np.cos(phi / 2), color=BLUE, lw=2.4, label="spinor: $1+\\cos(\\varphi/2)$, period $4\\pi$")
    c.plot(phi / np.pi, 1 + np.cos(phi), color=MUTED, lw=1.6, ls="--", label="if $2\\pi$ returned the ket: period $2\\pi$")
    for k in (0, 4, 8):
        c.axvline(k, color=BLUE, lw=0.8, alpha=0.5)
    c.set_xlabel("spin rotation angle $\\varphi=|\\gamma|B\\ell/v$ in the field arm ($\\pi$ rad)")
    c.set_ylabel("interference intensity (rel.)")
    c.set_ylim(-0.05, 2.75); c.legend(fontsize=8.3, loc="upper center")
    c.set_title("C  neutron interferometer: maxima every $4\\pi$")
    fig.tight_layout()
    save(fig, "fig_qm09_dynamics")


# ------------------------------------------------------------------ Figure 4: Bell and spin j
def fig_bell_spinj():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    a = ax[0]
    th = np.linspace(0, np.pi, 400)
    a.plot(np.degrees(th), -np.cos(th), color=BLUE, lw=2.4, label="quantum: $E=-\\cos\\theta$")
    a.plot(np.degrees(th), -1 + 2 * th / np.pi, color=ORANGE, lw=2.2, ls="--", label="local model $\\mathrm{sgn}(\\mathbf{a}\\cdot\\lambda)$: $-1+2\\theta/\\pi$")
    a.fill_between(np.degrees(th), -np.cos(th), -1 + 2 * th / np.pi, color=BLUE, alpha=0.10)
    for d in (45, 135):
        a.plot([d], [-math.cos(math.radians(d))], "o", color=BLUE, ms=6)
    a.annotate("$\\theta=45^\\circ$: $-0.707$ vs $-0.5$", (45, -0.707), xytext=(60, -0.95), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
    a.set_xlabel("angle $\\theta$ between the two analyser axes (deg)"); a.set_ylabel("spin correlation $E(\\theta)$")
    a.legend(fontsize=8.5, loc="upper left"); a.set_xlim(0, 180)
    a.set_title("A  singlet correlation")
    b = ax[1]
    ph = np.linspace(0, 90, 400)
    S = np.abs(3 * np.cos(np.radians(ph)) - np.cos(3 * np.radians(ph)))
    b.plot(ph, S, color=BLUE, lw=2.4, label="quantum $|S|=|3\\cos\\varphi-\\cos3\\varphi|$")
    b.axhline(2, color=ORANGE, lw=1.8, ls="--"); b.text(2, 2.03, "local hidden variables: $|S|\\leq 2$", color=INK, fontsize=9, va="bottom")
    b.axhline(2 * math.sqrt(2), color=MUTED, lw=1.4, ls=":"); b.text(2, 2.86, "Tsirelson: $2\\sqrt{2}=2.828$", color=INK, fontsize=9, va="bottom")
    b.fill_between(ph, 2, S, where=S > 2, color=BLUE, alpha=0.12)
    b.plot([45], [2 * math.sqrt(2)], "o", color=BLUE, ms=7)
    b.set_xlabel("$\\varphi$ (deg): axes at $0,\\,\\varphi,\\,2\\varphi,\\,3\\varphi$"); b.set_ylabel("CHSH $|S|$")
    b.set_ylim(0, 3.2); b.set_xlim(0, 90)
    b.legend(fontsize=8.3, loc="lower center")
    b.set_title("B  CHSH: violated for $0<\\varphi<68.5^\\circ$")
    c = ax[2]
    w = 0.36
    ms = np.array([-1, 0, 1])
    p_from_plus = np.array([0.25, 0.5, 0.25])
    p_from_zero = np.array([0.5, 0.0, 0.5])
    c.bar(ms - w / 2, p_from_plus, w, color=BLUE, label="start $m_z=+1$")
    c.bar(ms + w / 2, p_from_zero, w, color=ORANGE, label="start $m_z=0$")
    for xx, yy in zip(ms - w / 2, p_from_plus):
        c.text(xx, yy + 0.012, f"{yy:.2f}", ha="center", fontsize=8.5)
    for xx, yy in zip(ms + w / 2, p_from_zero):
        c.text(xx, yy + 0.012, f"{yy:.2f}", ha="center", fontsize=8.5)
    c.set_xticks(ms); c.set_xticklabels(["$-1$", "$0$", "$+1$"])
    c.set_xlabel("outcome $m_x\\hbar$ of the SG$_x$ stage (three beams)"); c.set_ylabel("probability")
    c.set_ylim(0, 0.62); c.legend(fontsize=8.5, loc="upper center")
    c.set_title("C  spin 1: a $z$-beam sent through SG$_x$")
    fig.tight_layout()
    save(fig, "fig_qm09_bell_spinj")


# ------------------------------------------------------------------ Figure 5: parallels
def fig_parallels():
    fig, ax = plt.subplots(1, 3, figsize=(15.8, 4.7))
    a = ax[0]
    x = np.logspace(-6.5, 1.0, 400)
    a.semilogx(x, np.tanh(x), color=BLUE, lw=2.4, label="$P=\\tanh(\\mu B/kT)$")
    a.semilogx(x, x, color=MUTED, lw=1.2, ls="--", label="linear (Curie) regime $P\\approx\\mu B/kT$")
    pts = (("1", MU_P * 1.5 / (1.380649e-23 * 300)), ("2", MU_B * 1.0 / (1.380649e-23 * 300)),
           ("3", MU_B * 1.0 / (1.380649e-23 * 4)), ("4", MU_B * 10.0 / (1.380649e-23 * 2)))
    for lab, xv in pts:
        a.plot([xv], [math.tanh(xv)], "o", color=ORANGE, ms=8, zorder=5)
        if lab == "4":
            a.text(xv * 0.55, math.tanh(xv) - 0.02, lab, ha="center", va="center", fontsize=10, weight="bold")
        else:
            a.text(xv * 1.0, math.tanh(xv) + 0.07, lab, ha="center", fontsize=10, weight="bold")
    a.text(2e-7, 0.93, "1  proton, 1.5 T, 300 K: $5.1\\times10^{-6}$\n2  electron, 1 T, 300 K: $2.2\\times10^{-3}$\n3  electron, 1 T, 4 K: $0.17$\n4  electron, 10 T, 2 K: $0.998$",
           fontsize=8.8, va="top", ha="left", bbox=dict(fc=SURFACE, ec=GRID, pad=4))
    a.set_xlabel("$\\mu B/k_BT$"); a.set_ylabel("spin polarisation $P=p_\\uparrow-p_\\downarrow$"); a.set_ylim(-0.02, 1.05)
    a.legend(fontsize=8.3, loc="center left", bbox_to_anchor=(0.0, 0.36))
    a.set_title("A  a two-level paramagnet in equilibrium")
    b = ax[1]
    LE = np.linspace(0, 2000, 800)
    for s22, col, lab in ((1.0, BLUE, "$\\sin^22\\theta=1.0$"), (0.85, ORANGE, "$\\sin^22\\theta=0.85$")):
        b.plot(LE, s22 * np.sin(1.267 * 2.5e-3 * LE) ** 2, color=col, lw=2.2, label=lab)
    b.axvline(295 / 0.6, color=MUTED, lw=1.2, ls=":")
    b.text(520, 1.12, "long-baseline beam:\n295 km, 0.6 GeV $=$ 492 km/GeV", fontsize=8.5, va="center")
    b.set_xlabel("$L/E$ (km/GeV)"); b.set_ylabel("flavour-change probability")
    b.legend(fontsize=8.5, loc="upper right"); b.set_ylim(-0.02, 1.3)
    b.set_title("B  flavour oscillation $=$ Rabi flopping ($\\Delta m^2=2.5\\times10^{-3}$ eV$^2$)")
    c = ax[2]
    n = np.arange(1, 6)
    mu = np.sqrt(n * (n + 2))
    c.bar(n, mu, color=[GRID, BLUE, GRID, GRID, ORANGE], edgecolor=MUTED)
    for nn, mm in zip(n, mu):
        c.text(nn, mm + 0.08, f"{mm:.2f}", ha="center", fontsize=9)
    c.text(2, 1.2, "O$_2$\n(triplet)", ha="center", fontsize=8.5, color="white")
    c.text(5, 1.2, "Fe$^{3+}$, Mn$^{2+}$\nhigh-spin $d^5$", ha="center", fontsize=8.0, color="white")
    c.set_xlabel("number $n$ of unpaired electrons"); c.set_ylabel("spin-only moment $\\sqrt{n(n+2)}\\,\\mu_B$")
    c.set_ylim(0, 6.6); c.set_xticks(n); c.grid(axis="x", visible=False)
    c.set_title("C  chemistry: moments of transition-metal ions")
    fig.tight_layout()
    save(fig, "fig_qm09_parallels")


if __name__ == "__main__":
    fig_apparatus()
    fig_sequential()
    fig_dynamics()
    fig_bell_spinj()
    fig_parallels()
