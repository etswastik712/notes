"""EE06 - alternative stable states and hysteresis in the minimal model of Scheffer et al. (2001), Box 1:
dx/dt = a - b x + r x^p/(x^p + h^p),  b = 1, r = 1.4, h = 1, p = 8  (illustrative values).
x = the unwanted property (e.g. algal turbidity), a = the environmental driver (e.g. nutrient loading).
A: equilibria against a (solid = stable, dashed = unstable) and a slow ramp of a up, then down;  B: dx/dt against x at three values of a.
"""
from scipy.integrate import solve_ivp

from figlib import *

b, r, h, p = 1.0, 1.4, 1.0, 8
f = lambda x: x ** p / (x ** p + h ** p)
fp = lambda x: p * x ** (p - 1) * h ** p / (x ** p + h ** p) ** 2
x = np.linspace(0.0, 2.6, 4000)
a_eq = b * x - r * f(x)
stable = (b - r * fp(x)) > 0                       # da/dx > 0  <=>  d(rhs)/dx < 0
idx = np.where(np.diff(np.sign(b - r * fp(x))))[0]
xf = x[idx]; af = a_eq[idx]
lo_a, hi_a = af.min(), af.max()

fig, axes = plt.subplots(1, 2, figsize=(11.4, 4.2), gridspec_kw=dict(width_ratios=[1.25, 1]))
A = axes[0]
for seg, st in ((stable, True), (~stable, False)):
    xx = np.where(seg, x, np.nan)
    A.plot(a_eq, xx, color=(BLUE if st else MUTED), ls=("-" if st else "--"), lw=(2.4 if st else 1.6))
# ramp simulation
def ramp(a0, a1, T=2000.0, x0=0.0):
    sol = solve_ivp(lambda t, y: [(a0 + (a1 - a0) * t / T) - b * y[0] + r * f(y[0])], (0, T), [x0], rtol=1e-9, atol=1e-11, dense_output=True, max_step=2.0)
    t = np.linspace(0, T, 800); return a0 + (a1 - a0) * t / T, sol.sol(t)[0]
a_up, x_up = ramp(-0.1, 1.0, x0=0.0)
a_dn, x_dn = ramp(1.0, -0.1, x0=x_up[-1])
A.plot(a_up, x_up, color=ORANGE, lw=1.2, alpha=0.95); A.plot(a_dn, x_dn, color=AQUA, lw=1.2, alpha=0.95)
for aa, xx_, col in ((a_up, x_up, ORANGE), (a_dn, x_dn, AQUA)):
    k = len(aa) // 2 if col == ORANGE else len(aa) // 2
A.annotate("", xy=(0.80, 1.7), xytext=(0.62, 1.7), arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.6))
A.annotate("", xy=(0.12, 0.35), xytext=(0.30, 0.35), arrowprops=dict(arrowstyle="->", color=AQUA, lw=1.6))
A.axvline(hi_a, color=INK, lw=0.7, ls=":"); A.axvline(lo_a, color=INK, lw=0.7, ls=":")
A.text(hi_a + 0.015, 0.12, f"forward switch\n(a = {hi_a:.2f})", fontsize=8.3, va="bottom")
A.text(lo_a - 0.015, 2.3, f"backward switch\n(a = {lo_a:.2f})", fontsize=8.3, va="top", ha="right")
A.text(0.40, 0.66, "unstable states\n(the threshold)", fontsize=8.2, color=MUTED, ha="center", va="center")
A.text(0.40, 0.04, "clear-water state", color=BLUE, fontsize=8.6, va="bottom", ha="center")
A.text(0.40, 2.25, "turbid state", color=BLUE, fontsize=8.6, ha="center")
A.set_xlim(-0.1, 1.0); A.set_ylim(0, 2.6)
A.set_xlabel("environmental driver a (e.g. nutrient loading)"); A.set_ylabel("ecosystem state x (e.g. turbidity)")
A.set_title("A  two stable states for the same loading", fontsize=10)
B = axes[1]
xx = np.linspace(0, 2.6, 400)
for a_, col in ((0.0, AQUA), (0.35, BLUE), (0.8, ORANGE)):
    B.plot(xx, a_ - b * xx + r * f(xx), color=col, label=f"a = {a_}")
B.axhline(0, color=INK, lw=0.9)
B.set_xlabel("state x"); B.set_ylabel("rate of change dx/dt"); B.set_ylim(-1.2, 1.0)
B.legend(loc="upper right", fontsize=8.6)
B.set_title("B  zero crossings = equilibria (1, 3 or 1)", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.04, "Minimal model of Scheffer et al. (2001), Box 1, with illustrative parameters (b = 1, r = 1.4, h = 1, p = 8). Orange: a ramped up slowly; green: ramped back down. "
         "The jump up happens at the right-hand fold, the jump back at the left-hand fold: hysteresis.", ha="center", fontsize=7.9, color=MUTED)
save(fig, "fig_ee06_hysteresis")
print("folds: x", np.round(xf, 3), "a", np.round(af, 3))
