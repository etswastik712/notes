"""CL01 - why weather is unpredictable but climate statistics are not: two Lorenz-63 runs that start 1e-8 apart.

dx/dt = s(y-x),  dy/dt = x(r-z)-y,  dz/dt = xy - b z   with s=10, r=28, b=8/3 (Lorenz 1963).
Left: x(t) of the two runs; middle: log10 of their separation (slope = largest Lyapunov exponent ~0.9 per unit time);
right: running means of z converge to the same value (the 'climate').
"""
from scipy.integrate import solve_ivp

from figlib import *


def rhs(t, u, s=10.0, r=28.0, b=8.0 / 3.0):
    x, y, z = u
    return [s * (y - x), x * (r - z) - y, x * y - b * z]


T = 60.0
t = np.linspace(0, T, 6001)
u0 = np.array([1.0, 1.0, 1.0])
a = solve_ivp(rhs, (0, T), u0, t_eval=t, rtol=1e-12, atol=1e-12, method="DOP853")
b = solve_ivp(rhs, (0, T), u0 + np.array([1e-8, 0, 0]), t_eval=t, rtol=1e-12, atol=1e-12, method="DOP853")
sep = np.linalg.norm(a.y - b.y, axis=0)
ok = (sep > 1e-7) & (sep < 1e-1)
lam = np.polyfit(t[ok], np.log(sep[ok]), 1)[0]
t_lose = t[np.argmax(sep > 1.0)]
print(f"lyapunov ~ {lam:.2f} per unit time; separation reaches 1 at t={t_lose:.1f}")
zm_a = np.cumsum(a.y[2]) / np.arange(1, len(t) + 1)
zm_b = np.cumsum(b.y[2]) / np.arange(1, len(t) + 1)
print(f"mean z at T: {zm_a[-1]:.2f} vs {zm_b[-1]:.2f};  |x| trajectories differ by {abs(a.y[0][-1]-b.y[0][-1]):.1f} at T")

fig, axs = plt.subplots(1, 3, figsize=(11.2, 3.4))
ax = axs[0]
ax.plot(t, a.y[0], color=BLUE, lw=1.3, label="run A")
ax.plot(t, b.y[0], color=ORANGE, lw=1.0, label="run B (initial $x$ differs by $10^{-8}$)")
ax.set_xlabel("time")
ax.set_ylabel("x")
ax.set_title("Weather: trajectories part ways", fontsize=10)
ax.legend(loc="lower left", fontsize=7.5)
ax = axs[1]
ax.semilogy(t, sep, color=INK, lw=1.4)
ax.axhline(1, color=MUTED, ls=":", lw=1)
ax.annotate(f"separation ≈ 1 at t ≈ {t_lose:.0f}\ngrowth ≈ {lam:.1f} e-folds per time unit", (t_lose, 1), xytext=(33, 3e-6), textcoords="data",
            ha="left", fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
ax.set_xlabel("time")
ax.set_ylabel("|A − B|")
ax.set_title("Error grows exponentially", fontsize=10)
ax = axs[2]
ax.plot(t, zm_a, color=BLUE, lw=1.6, label="run A")
ax.plot(t, zm_b, color=ORANGE, lw=1.2, ls="--", label="run B")
ax.set_xlabel("time")
ax.set_ylabel("running mean of z")
ax.set_title("Climate: the average is robust", fontsize=10)
ax.legend(loc="lower right", fontsize=8)
fig.tight_layout()
save(fig, "fig_cl01_lorenz")
