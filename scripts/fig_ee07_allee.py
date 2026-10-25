"""EE07: Allee effect. Left: per-capita growth rate g(N) with and without an Allee effect. Right: growth f(N) of a
strong-Allee population with a constant harvest H: fixed points move together and annihilate at H = max f (fold).
Illustrative parameters (r=0.5, A=20, K=100); not fitted to data.
"""
from figlib import *

r, A, K = 0.5, 20.0, 100.0
f = lambda N: r * N * (N / A - 1.0) * (1.0 - N / K)
N = np.linspace(0, 115, 600)

Nm = ((A + K) + np.sqrt((A + K) ** 2 - 3 * A * K)) / 3
Nl = ((A + K) - np.sqrt((A + K) ** 2 - 3 * A * K)) / 3
print(f"f'(N)=0 at N={Nm:.2f} (max, f={f(Nm):.2f}) and N={Nl:.2f} (min, f={f(Nl):.2f}); logistic rK/4={r*K/4:.1f}")
for Nn, nm in [(0, "0"), (A, "A"), (K, "K")]:
    h = 1e-6
    print(f"f'({nm}) = {(f(Nn+h)-f(Nn-h))/(2*h):.3f}")
H = 20.0
roots = np.roots([-r / (A * K), r * (A + K) / (A * K), -r, -H])
roots = np.sort(roots[np.isreal(roots)].real)
print(f"H={H}: roots of f(N)=H:", np.round(roots, 2), "; slopes:",
      [round((f(x + 1e-6) - f(x - 1e-6)) / 2e-6, 3) for x in roots])
H2 = f(Nm) + 0.5
print(f"max sustainable constant harvest H*={f(Nm):.2f} at N={Nm:.1f}; H*/(rK/4 logistic)={f(Nm)/(r*K/4):.2f}")

fig, ax = plt.subplots(1, 2, figsize=(11, 4.1))
a = ax[0]
Np = np.linspace(0.01, 115, 600)
a.axhline(0, color=MUTED, lw=0.8)
a.plot(Np, r * (1 - Np / K), color=BLUE, lw=1.9)
a.plot(Np, r * (1 - Np / K) * Np / (Np + 10.0), color=AQUA, lw=1.9)
a.plot(Np, r * (Np / A - 1) * (1 - Np / K), color=ORANGE, lw=1.9)
a.set_xlim(0, 115)
a.set_ylim(-0.6, 0.62)
a.set_xlabel("population size $N$")
a.set_ylabel("per-capita growth rate $\\dot N/N$ (yr$^{-1}$)")
a.set_title("Per-capita growth: highest at low $N$ or not?")
label_line(a, 5, 0.475, "no Allee effect (logistic)", BLUE, dx=8, dy=3)
label_line(a, 60, 0.157, "weak Allee effect", AQUA, dx=-6, dy=14, ha="right")
label_line(a, 80, 0.5 * (80 / A - 1) * (1 - 80 / K) , "strong Allee effect", ORANGE, dx=6, dy=18, ha="left")
a.plot([A], [0], "o", ms=7, mfc="white", mec=INK, mew=1.5, zorder=6)
a.annotate("Allee threshold $A$", (A, 0), xytext=(24, -0.40), arrowprops=dict(arrowstyle="-", color=MUTED), fontsize=9)
a.plot([K], [0], "o", ms=7, color=INK, zorder=6)
a.text(K - 1, -0.1, "$K$", ha="right", fontsize=9)

b = ax[1]
b.axhline(0, color=MUTED, lw=0.8)
b.plot(N, f(N), color=ORANGE, lw=2.0)
b.axhline(H, color=VIOLET, lw=1.3, ls="--")
b.text(2, H + 1.2, f"harvest $H={H:.0f}$ per yr (constant quota)", color=VIOLET, fontsize=9)
b.axhline(f(Nm), color=RED, lw=1.0, ls=":")
b.text(2, f(Nm) + 1.1, f"fold: $H^*=\\max f={f(Nm):.1f}$", color=RED, fontsize=9)
# fixed points at H=0 (on axis) and at H (on the dashed line)
for x, stable in [(0, True), (A, False), (K, True)]:
    b.plot([x], [0], "o", ms=7, color=INK if stable else "white", mec=INK, mew=1.5, zorder=6)
for x in roots:
    slope = (f(x + 1e-6) - f(x - 1e-6)) / 2e-6
    b.plot([x], [H], "o", ms=7, color=VIOLET if slope < 0 else "white", mec=VIOLET, mew=1.5, zorder=6)
b.annotate("", xy=(roots[0] - 3, H - 4.5), xytext=(roots[0] + 3, H - 4.5), arrowprops=dict(arrowstyle="->", color=VIOLET))
b.text(roots[1], H - 7.5, "below: drifts to 0", ha="center", fontsize=8.5, color=VIOLET)
b.set_xlim(0, 115)
b.set_ylim(-14, 33)
b.set_xlabel("population size $N$")
b.set_ylabel("growth $f(N)$ (individuals yr$^{-1}$)")
b.set_title("A quota that is 'safe' can still tip a population over")
b.text(60, -11.5, "filled = stable, open = unstable", fontsize=8.5, color=MUTED)
fig.tight_layout()
save(fig, "fig_ee07_allee")
