"""CL08 - a CO2 forcing in the one-layer model: OLR(T_s) for eps = 0.779 and eps = 0.798 (delta eps = 0.019 <-> F = 3.7 W/m2)."""
from cl08_layers import te
from figlib import *

Te = te()
Q = SIGMA * Te**4
e0 = 2 * (1 - (Te / 288.0) ** 4)
e1 = e0 + 2 * 3.7 / (SIGMA * 288.0**4)
T = np.linspace(280, 296, 200)


def olr(T, e):
    return SIGMA * T**4 * (1 - e / 2)


T1 = (Q / (SIGMA * (1 - e1 / 2))) ** 0.25
print(f"eps0={e0:.4f} eps1={e1:.4f}  new Ts={T1:.2f} K  (dT={T1-288:.2f})  forcing at 288 K = {olr(288,e0)-olr(288,e1):.2f}")
fig, ax = plt.subplots(figsize=(6.6, 4.2))
ax.plot(T, olr(T, e0), color=BLUE, label=f"OLR, ε = {e0:.3f} (today)")
ax.plot(T, olr(T, e1), color=ORANGE, label=f"OLR, ε = {e1:.3f} (CO₂ doubled)")
ax.axhline(Q, color=INK, lw=1)
ax.annotate("absorbed sunlight 238 W m⁻²", (285.15, Q), xytext=(0, 5), textcoords="offset points", fontsize=8.5)
ax.annotate("", xy=(288, olr(288, e1)), xytext=(288, olr(288, e0)), arrowprops=dict(arrowstyle="<->", color=RED, lw=1.6))
ax.annotate("forcing 3.7 W m⁻²", (288, 0.5 * (olr(288, e0) + olr(288, e1))), xytext=(-12, -22), textcoords="offset points", ha="right", va="center", fontsize=8.5, color=RED, arrowprops=dict(arrowstyle="-", color=RED, lw=0.8))
ax.annotate("", xy=(T1, Q), xytext=(288, Q), arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.4))
ax.annotate(f"+{T1-288:.1f} K\n(no feedback)", (0.5 * (T1 + 288), Q), xytext=(18, -34), textcoords="offset points", ha="center", fontsize=8.5)
ax.plot([288, T1], [Q, Q], "o", color=INK, ms=5, zorder=5)
ax.plot([290.2], [Q], "s", color=AQUA, ms=6, zorder=5)
ax.annotate("+2.2 K with water-vapour\nfeedback (f ≈ 0.5)", (290.2, Q), xytext=(14, 26), textcoords="offset points", fontsize=8.5, color=AQUA,
            arrowprops=dict(arrowstyle="-", color=AQUA, lw=0.8))
ax.set_xlabel("surface temperature $T_s$ (K)")
ax.set_ylabel("outgoing longwave radiation (W m$^{-2}$)")
ax.set_title("Doubling CO₂ cuts the OLR; the surface warms until it is restored", fontsize=10.5)
ax.set_xlim(285, 292.5)
ax.set_ylim(228, 250)
ax.legend(loc="upper left", fontsize=8.5)
save(fig, "fig_cl08_forcing")
