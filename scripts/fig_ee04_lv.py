"""EE04 - Lotka-Volterra competition: the four outcomes in the (N1, N2) plane (slides 10-12).
dN_i/dt = r_i N_i (K_i - N_i - a_ij N_j)/K_i ; K1 = 100, K2 = 80, r1 = r2 = 0.5.  Isoclines are straight lines;
trajectories are numerical solutions from several starting points.  (My construction; the parameter values are illustrative.)
"""
from scipy.integrate import solve_ivp

from figlib import *

K1, K2, r1, r2 = 100.0, 80.0, 0.5, 0.5
cases = [("A  species 1 wins", 0.5, 1.5), ("B  species 2 wins", 1.5, 0.5),
         ("C  stable coexistence", 0.5, 0.6), ("D  unstable equilibrium: the start decides", 1.5, 1.5)]


def rhs(t, y, a12, a21):
    n1, n2 = y
    return [r1 * n1 * (K1 - n1 - a12 * n2) / K1, r2 * n2 * (K2 - n2 - a21 * n1) / K2]


fig, axes = plt.subplots(1, 4, figsize=(13.4, 3.9), sharex=True, sharey=True)
for ax, (title, a12, a21) in zip(axes, cases):
    x = np.linspace(0, 210, 2)
    ax.plot(x, (K1 - x) / a12, color=BLUE, lw=2)               # dN1/dt = 0 : N2 = (K1 - N1)/a12
    ax.plot(x, K2 - a21 * x, color=ORANGE, lw=2)               # dN2/dt = 0 : N2 = K2 - a21 N1
    starts = [(5, 5), (150, 10), (10, 120), (120, 90), (60, 40), (30, 70), (80, 20), (20, 25)]
    for s in starts:
        sol = solve_ivp(rhs, (0, 120), s, args=(a12, a21), dense_output=True, rtol=1e-8)
        ax.plot(sol.y[0], sol.y[1], color=MUTED, lw=0.9, alpha=0.8)
        ax.annotate("", xy=(sol.y[0][len(sol.t) // 6], sol.y[1][len(sol.t) // 6]), xytext=(sol.y[0][len(sol.t) // 6 - 1], sol.y[1][len(sol.t) // 6 - 1]),
                    arrowprops=dict(arrowstyle="->", color=MUTED, lw=0.9))
    d = 1 - a12 * a21
    n1s, n2s = (K1 - a12 * K2) / d, (K2 - a21 * K1) / d
    if n1s > 0 and n2s > 0:
        ax.plot([n1s], [n2s], "o", ms=7, mfc=("white" if a12 * a21 > 1 else INK), mec=INK, zorder=6)
        ax.text(n1s + 4, n2s + 5, f"({n1s:.0f}, {n2s:.0f})", fontsize=8.2)
    for pt in [(K1, 0), (0, K2)]:
        stable = (title.startswith("A") and pt == (K1, 0)) or (title.startswith("B") and pt == (0, K2)) or title.startswith("D")
        ax.plot(*pt, "o", ms=7, mfc=(INK if stable else "white"), mec=INK, zorder=6)
    ax.set_title(title, fontsize=9.2)
    ax.set_xlim(0, 200); ax.set_ylim(0, 160)
    ax.set_xlabel("$N_1$")
    ax.text(196, 150, rf"$\alpha_{{12}}={a12}$, $\alpha_{{21}}={a21}$", ha="right", fontsize=8.5)
axes[0].set_ylabel("$N_2$")
axes[0].text(8, 2.5 * 0 + 118, "blue: $dN_1/dt=0$\norange: $dN_2/dt=0$", fontsize=8.0, color=INK, va="top")
fig.tight_layout()
fig.text(0.5, -0.04, "Filled dots: stable equilibria; open dots: unstable. K1 = 100, K2 = 80 (illustrative). Panel C coexists because each species limits itself more than the other (α12 α21 < 1 and "
         "α12 < K1/K2, α21 < K2/K1); in D the interior point is a saddle.", ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_ee04_lv")
