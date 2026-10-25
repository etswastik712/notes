"""CL08 - one-layer greenhouse: T_s/T_e vs absorptivity eps, and the greenhouse flux G = back-radiation vs eps.

  T_s = T_e (1 - eps/2)^(-1/4);   G = sigma T_s^4 - OLR = sigma T_e^4 eps/(2-eps);   back-radiation = eps sigma T_a^4 = G.
"""
from cl08_layers import te
from figlib import *

Te = te()
eps = np.linspace(0, 1, 300)
ratio = (1 - eps / 2) ** -0.25
Q = SIGMA * Te**4
G = Q * eps / (2 - eps)

fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 4.0))
a.plot(eps, ratio, color=BLUE)
a.axhline(2**0.25, color=MUTED, lw=0.9, ls=":")
a.annotate(r"opaque layer: $2^{1/4}=1.189$  (303 K)", (0.02, 2**0.25), xytext=(0, 6), textcoords="offset points", fontsize=8.5)
a.axhline(1, color=MUTED, lw=0.9, ls=":")
a.annotate("no atmosphere: $T_s=T_e$", (0.5, 1.0), xytext=(0, -13), textcoords="offset points", fontsize=8.5, ha="center")
e_earth = 2 * (1 - (Te / 288.0) ** 4)
a.plot([e_earth], [288 / Te], "o", color=ORANGE, ms=7)
a.annotate(f"Earth: ε = {e_earth:.2f}\n288 K", (e_earth, 288 / Te), xytext=(-12, 22), textcoords="offset points", ha="right", fontsize=8.5)
e_mars = 2 * (1 - (209.8 / 214.0) ** 4)
a.plot([e_mars], [214 / 209.8], "o", color=AQUA, ms=7)
a.annotate(f"Mars: ε = {e_mars:.2f}\n($T_s/T_e$ = 1.02)", (e_mars, 214 / 209.8), xytext=(10, 12), textcoords="offset points", fontsize=8.5)
a.annotate("Venus: $T_s/T_e=3.25$\nneeds ε = 1.98 > 1", (0.62, 1.185), xytext=(0.12, 1.15), fontsize=8.5, color=RED)
a.set_xlabel("longwave absorptivity of the layer, ε")
a.set_ylabel(r"$T_s/T_e$")
a.set_title("One leaky layer: the surface warms as ε grows", fontsize=10.5)
a.set_xlim(0, 1)
a.set_ylim(0.98, 1.22)

b.plot(eps, G, color=BLUE, label=r"$G=A_\downarrow=\sigma T_e^4\,\varepsilon/(2-\varepsilon)$")
b.axhline(Q, color=MUTED, lw=0.9, ls=":")
b.annotate("maximum (ε = 1): the absorbed sunlight, 238 W m⁻²", (0.02, Q), xytext=(0, 5), textcoords="offset points", fontsize=8.5)
b.axhline(340, color=RED, lw=1.2, ls="--")
b.annotate("observed downward longwave at the surface ≈ 340 W m⁻²\n(out of reach of a single isothermal layer)", (0.02, 340), xytext=(0, 5), textcoords="offset points", fontsize=8.5, color=RED)
b.plot([e_earth], [Q * e_earth / (2 - e_earth)], "o", color=ORANGE, ms=7)
b.annotate(f"Earth: {Q*e_earth/(2-e_earth):.0f} W m⁻²", (e_earth, Q * e_earth / (2 - e_earth)), xytext=(-8, 8), textcoords="offset points", ha="right", fontsize=8.5)
b.set_xlabel("longwave absorptivity of the layer, ε")
b.set_ylabel("flux (W m$^{-2}$)")
b.set_title("Greenhouse flux = back-radiation", fontsize=10.5)
b.set_xlim(0, 1)
b.set_ylim(0, 380)
b.legend(loc="lower right", fontsize=8.5)
fig.tight_layout()
save(fig, "fig_cl08_one_layer")
print(f"eps_earth={e_earth:.3f} eps_mars={e_mars:.3f} G_earth={Q*e_earth/(2-e_earth):.1f}")
