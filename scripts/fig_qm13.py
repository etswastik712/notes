#!/usr/bin/env python3
"""QM13 figures: probability current and Ehrenfest's theorem (hbar = m = 1).
Run from anywhere:  .venv/bin/python scripts/fig_qm13.py
Writes Assets/figures/fig_qm13_current.png and Assets/figures/fig_qm13_ehrenfest.png
Every number quoted in the captions is printed at the end so it can be checked against scripts/qm13_numbers.py.
"""
import os
import numpy as np, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "Assets", "figures"); os.makedirs(OUT, exist_ok=True)
BL, RD, GR, VI, OR, GY = "#1f4e79", "#c0392b", "#117a65", "#7d3c98", "#d35400", "0.45"
trap = getattr(np, "trapezoid", None) or np.trapz

# =====================================================================================
# Figure 1: the probability current
# =====================================================================================
L = 1.0
E = lambda n: n**2 * np.pi**2 / (2 * L**2)
w21 = E(2) - E(1)
x = np.linspace(0, L, 4001)
f = lambda n, x: np.sqrt(2 / L) * np.sin(n * np.pi * x / L)
rho = lambda x, wt: 0.5 * (f(1, x)**2 + f(2, x)**2) + f(1, x) * f(2, x) * np.cos(wt)
jj = lambda x, wt: (w21 / np.pi) * np.sin(wt) * (np.sin(np.pi * x / L) - np.sin(3 * np.pi * x / L) / 3)

fig, axs = plt.subplots(1, 3, figsize=(13.0, 4.1))

# A. density sloshes, current carries it
ax = axs[0]
for wt, c, lab in [(0, BL, r"$\omega t=0$"), (np.pi / 2, GR, r"$\omega t=\pi/2$"), (np.pi, RD, r"$\omega t=\pi$")]:
    ax.plot(x, rho(x, wt), color=c, lw=2, label=r"$\rho$, " + lab)
ax.plot(x, jj(x, np.pi / 2), color=VI, lw=2, ls="--", label=r"$j$ at $\omega t=\pi/2$")
ax.fill_between(x, 0, jj(x, np.pi / 2), color=VI, alpha=0.12)
for xa in np.linspace(0.1, 0.9, 5):
    ax.annotate("", xy=(xa + 0.07, -0.22), xytext=(xa - 0.07, -0.22), arrowprops=dict(arrowstyle="-|>", color=VI, lw=1.6))
ax.text(0.5, -0.62, "flow at $\\omega t=\\pi/2$: everything moves right", ha="center", fontsize=8, color=VI)
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlim(0, 1); ax.set_ylim(-0.8, 7.0); ax.set_xlabel("x / L"); ax.legend(frameon=False, fontsize=8, loc="upper right")
ax.set_title("A. box state $(\\psi_1+\\psi_2)/\\sqrt{2}$: density moves, $j\\neq0$", fontsize=10)

# B. <x>(t) and the total current
ax = axs[1]
wts = np.linspace(0, 2 * np.pi, 400)
xm = lambda wt: trap(x * rho(x, wt), x)
xm_num = np.array([xm(a) for a in wts])
xm_formula = L / 2 - 16 * L / (9 * np.pi**2) * np.cos(wts)
ax.plot(wts / np.pi, xm_num, color=BL, lw=2.2, label=r"$\langle x\rangle=\int x\rho\,dx$")
ax.set_ylabel(r"$\langle x\rangle/L$", color=BL); ax.set_xlabel(r"$\omega t/\pi$"); ax.set_ylim(0.1, 0.9)
ax2 = ax.twinx()
h = 1e-4
vnum = np.array([(xm(a + h) - xm(a - h)) / (2 * h / w21) for a in wts])      # d<x>/dt by finite difference of the integral
wd = np.linspace(0.15, 2 * np.pi - 0.15, 14)
jint = np.array([trap(jj(x, a), x) for a in wd])
ax2.plot(wts / np.pi, vnum, color=GY, lw=1.4, label=r"$d\langle x\rangle/dt$ (finite difference)")
ax2.plot(wd / np.pi, jint, "o", color=VI, ms=5, label=r"$\int j\,dx$")
ax2.set_ylabel(r"velocity ($\hbar/mL$ units)", color=VI)
h1, l1 = ax.get_legend_handles_labels(); h2, l2 = ax2.get_legend_handles_labels()
ax.legend(h1 + h2, l1 + l2, frameon=False, fontsize=8, loc="upper right")
ax.set_title("B. the total current is the speed of the centre", fontsize=10)

# C. step: |psi|^2 jumps, j does not
ax = axs[2]
k1, k2 = 1.0, 0.5
r = (k1 - k2) / (k1 + k2); tt = 2 * k1 / (k1 + k2)
xl = np.linspace(-9, 0, 800); xr = np.linspace(0, 9, 800)
dens = lambda xx: np.where(xx < 0, 1 + r**2 + 2 * r * np.cos(2 * k1 * xx), tt**2 + 0 * xx)
cur = lambda xx: np.where(xx < 0, k1 * (1 - r**2), k2 * tt**2)
xx = np.concatenate([xl, xr])
ax.plot(xx, dens(xx), color=BL, lw=2, label=r"$|\psi|^2$")
ax.plot(xx, cur(xx), color=VI, lw=2.4, label=r"$j=k_1(1-R)=k_2|F/A|^2=0.89$ (same on both sides)")
ax.axvline(0, color=OR, lw=1.2, ls=":"); ax.text(0.2, 2.3, "step", color=OR, fontsize=8)
ax.text(1.5, tt**2 + 0.1, f"$|F/A|^2={tt**2:.2f}>1$", color=BL, fontsize=8.5)
ax.set_xlim(-9, 9); ax.set_ylim(0, 2.5); ax.set_xlabel("x"); ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title("C. step, $k_2=k_1/2$: $|\\psi|^2$ jumps, $j$ does not", fontsize=10)

fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_qm13_current.png"), dpi=140); plt.close(fig)
print("fig 1 ok")
print("  max |d<x>/dt (finite diff) - int j dx| at sample points: %.2e" %
      max(abs(jint[i] - np.interp(wd[i], wts, vnum)) for i in range(len(wd))))
print("  max |<x> numeric - formula|: %.2e" % np.max(np.abs(xm_num - xm_formula)))
print("  step: R=%.4f T=k2/k1|F/A|^2=%.4f R+T=%.4f ; j_I=%.4f j_II=%.4f ; |F/A|^2=%.4f" %
      (r**2, k2 / k1 * tt**2, r**2 + k2 / k1 * tt**2, k1 * (1 - r**2), k2 * tt**2, tt**2))

# =====================================================================================
# Figure 2: Ehrenfest — exact for the means, classical only for a linear force
# =====================================================================================
def run(V, dV, **kw):
    """returns t, <x>, <p>, <V'> using the same split-step; <p> = -i hbar int psi* psi' dx."""
    x0 = kw.get("x0", 1.5); sig = kw.get("sig", 0.5); p0 = kw.get("p0", 0.0)
    T = kw.get("T", 6.0); dt = kw.get("dt", 1e-3); N = kw.get("N", 2048); Lx = kw.get("Lx", 40.0); every = kw.get("every", 10)
    xg = np.linspace(-Lx / 2, Lx / 2, N, endpoint=False); dx = xg[1] - xg[0]
    k = 2 * np.pi * np.fft.fftfreq(N, dx)
    psi = ((2 * np.pi * sig**2) ** -0.25 * np.exp(-(xg - x0)**2 / (4 * sig**2) + 1j * p0 * xg)).astype(complex)
    eV = np.exp(-0.5j * V(xg) * dt); eK = np.exp(-0.5j * k**2 * dt)
    ts, xs, ps, fs = [], [], [], []
    for n in range(int(round(T / dt)) + 1):
        if n % every == 0:
            rho_ = np.abs(psi)**2
            ts.append(n * dt); xs.append(np.sum(xg * rho_) * dx)
            ps.append(np.real(np.sum(np.conj(psi) * np.fft.ifft(k * np.fft.fft(psi))) * dx))   # <p> = int psi* (-i d/dx) psi
            fs.append(np.sum(dV(xg) * rho_) * dx)
        psi = eV * np.fft.ifft(eK * np.fft.fft(eV * psi))
    return np.array(ts), np.array(xs), np.array(ps), np.array(fs)

def classical(dV, x0, p0, T, dt=1e-3, every=10):
    y = np.array([x0, p0]); out = []
    f_ = lambda y: np.array([y[1], -dV(y[0])])
    for n in range(int(round(T / dt)) + 1):
        if n % every == 0: out.append(y.copy())
        k1 = f_(y); k2 = f_(y + 0.5 * dt * k1); k3 = f_(y + 0.5 * dt * k2); k4 = f_(y + dt * k3)
        y = y + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return np.array(out)

T = 6.0
tq, xq, pq, fq = run(lambda x: x**4 / 4, lambda x: x**3, T=T)
th, xh, ph, fh = run(lambda x: x**2 / 2, lambda x: x, T=T)
cq = classical(lambda x: x**3, 1.5, 0.0, T); ch = classical(lambda x: x, 1.5, 0.0, T)

fig, axs = plt.subplots(1, 3, figsize=(13.0, 4.1))
ax = axs[0]
ax.plot(tq, xq, color=OR, lw=2.2, label=r"quartic $\frac{1}{4}x^4$: TDSE $\langle x\rangle$")
ax.plot(tq, cq[:, 0], color=RD, lw=1.8, ls="--", label=r"quartic: classical orbit from $(x_0,0)$")
ax.plot(th, xh, color=BL, lw=2.2, label=r"oscillator $\frac{1}{2}x^2$: TDSE $\langle x\rangle$")
ax.plot(th, ch[:, 0], color=GR, lw=1.4, ls=":", label=r"oscillator: $x_0\cos t$")
ax.set_xlabel("t"); ax.set_ylabel(r"$\langle x\rangle$"); ax.set_ylim(-3.4, 2.0); ax.legend(frameon=False, fontsize=7.5, loc="lower left")
ax.set_title("A. means: exactly classical only for a linear force", fontsize=10)

ax = axs[1]
ax.plot(tq, -fq, color=OR, lw=2.2, label=r"quartic: $-\langle V'\rangle$ (what Ehrenfest says)")
ax.plot(tq, -xq**3, color=RD, lw=1.8, ls="--", label=r"quartic: $-V'(\langle x\rangle)$ (classical force at centre)")
ax.plot(th, -fh, color=BL, lw=2.2, label=r"oscillator: $-\langle V'\rangle$")
ax.plot(th, -xh, color=GR, lw=1.4, ls=":", label=r"oscillator: $-V'(\langle x\rangle)$ (identical)")
ax.axhline(0, color="0.6", lw=0.8)
ax.set_xlabel("t"); ax.set_ylabel("force on the mean"); ax.legend(frameon=False, fontsize=7.5, loc="lower right")
ax.set_title("B. the force that enters is the cloud-averaged one", fontsize=10)

ax = axs[2]
sg = np.linspace(0.0, 0.9, 200); x0 = 1.5
ax.plot(sg, 1 + 3 * sg**2 / x0**2, color=OR, lw=2.2, label=r"$V=\frac{1}{4}x^4$: $\langle V'\rangle/V'(x_0)=1+3\sigma^2/x_0^2$")
ax.plot(sg, np.exp(-sg**2 / 2), color=VI, lw=2.2, label=r"$V=\cos x$: $\langle V'\rangle/V'(x_0)=e^{-\sigma^2/2}$")
ax.axhline(1, color=GY, lw=1.2, ls="--"); ax.text(0.58, 1.03, "classical: ratio 1", color=GY, fontsize=8)
xg_ = np.linspace(-12, 12, 80001)
for s_ in (0.2, 0.35, 0.5, 0.7):
    rho_ = np.exp(-(xg_ - x0)**2 / (2 * s_**2)) / np.sqrt(2 * np.pi * s_**2)
    ax.plot(s_, trap(xg_**3 * rho_, xg_) / x0**3, "o", color=OR, ms=5)
    ax.plot(s_, trap(-np.sin(xg_) * rho_, xg_) / (-np.sin(x0)), "o", color=VI, ms=5)
ax.plot([0.5], [1.3333], "s", mfc="none", mec="k", ms=9); ax.text(0.53, 1.26, "$\\sigma=0.5$: 4.5 vs 3.375", fontsize=8)
ax.set_xlabel(r"packet width $\sigma$"); ax.set_ylabel(r"$\langle V'\rangle\,/\,V'(\langle x\rangle)$"); ax.set_xlim(0, 0.9); ax.set_ylim(0.6, 1.9)
ax.legend(frameon=False, fontsize=7.5, loc="upper left")
ax.set_title(r"C. classical limit: the gap is $\propto\sigma^2$ and vanishes as $\sigma\to0$", fontsize=10)

fig.tight_layout(); fig.savefig(os.path.join(OUT, "fig_qm13_ehrenfest.png"), dpi=140); plt.close(fig)
print("fig 2 ok")
print("  quartic: <V'>(0)=%.4f  V'(<x>)(0)=%.4f" % (fq[0], xq[0]**3))
print("  oscillator: max|<x>-1.5 cos t|=%.2e ; max|<V'>-V'(<x>)|=%.2e" % (np.max(np.abs(xh - 1.5 * np.cos(th))), np.max(np.abs(fh - xh))))
tm = int(np.argmax(np.abs(xq - cq[:, 0]) > 0.3)); print("  quartic: |TDSE <x> - classical| first exceeds 0.3 at t=%.2f ; max over 0<t<6: %.3f" % (tq[tm], np.max(np.abs(xq - cq[:, 0]))))
dxdt = np.gradient(xq, tq); dpdt = np.gradient(pq, tq)
print("  quartic: max|d<x>/dt-<p>|=%.2e ; max|d<p>/dt+<V'>|=%.2e" % (np.max(np.abs(dxdt - pq)[5:-5]), np.max(np.abs(dpdt + fq)[5:-5])))
