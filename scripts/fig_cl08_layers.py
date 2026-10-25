"""CL08 - N-layer greenhouse: T_s vs N (exact linear-system solution) and the layer temperatures for N = 5 opaque layers."""
from cl08_layers import solve, te
from figlib import *

Te = te()
Ns = np.arange(0, 11)
fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 4.0))
for eps, c, lab in [(1.0, BLUE, "ε = 1 (opaque layers)"), (0.78, ORANGE, "ε = 0.78 per layer"), (0.5, AQUA, "ε = 0.5 per layer")]:
    ts = [Te] + [solve(n, eps)[0] for n in Ns[1:]]
    a.plot(Ns, ts, "o-", color=c, ms=4, label=lab)
a.plot(Ns, Te * (Ns + 1) ** 0.25, color=MUTED, lw=1, ls=":", label=r"$(N+1)^{1/4}T_e$")
a.axhline(288, color=RED, lw=1, ls="--")
a.annotate("Earth, 288 K", (10, 288), xytext=(0, 5), textcoords="offset points", ha="right", fontsize=8.5, color=RED)
a.set_xlabel("number of layers N")
a.set_ylabel("surface temperature $T_s$ (K)")
a.set_title("More layers, hotter surface", fontsize=10.5)
a.legend(loc="upper left", fontsize=8.5)

Ts, T, olr = solve(5, 1.0)
levels = [0] + list(range(1, 6))
temps = [Ts] + T                         # ground, then layer 1 (lowest) ... layer 5 (top)
for k, (z, t) in enumerate(zip(levels, temps)):
    b.plot([t], [z], "o", color=INK if z else ORANGE, ms=7, zorder=3)
    b.annotate(f"{t:.0f} K", (t, z), xytext=(8, -3), textcoords="offset points", fontsize=8.5)
b.plot(temps, levels, color=BLUE, lw=1.6)
b.annotate("", xy=(T[0], 0.5), xytext=(Ts, 0.5), arrowprops=dict(arrowstyle="<->", color=RED, lw=1.2))
b.annotate(f"ground is {Ts - T[0]:.0f} K hotter\nthan the air above it", (0.5 * (Ts + T[0]), 0.5), xytext=(-8, -30), textcoords="offset points", ha="right", fontsize=8.5, color=RED)
b.set_yticks(levels)
b.set_yticklabels(["ground"] + [f"layer {i}" for i in range(1, 6)])
b.set_xlabel("temperature (K)")
b.set_title("Five opaque layers: $T_k^4=(6-k)\\,T_e^4$ (k counted from the ground)", fontsize=10)
b.set_xlim(240, 440)
b.grid(axis="y", visible=False)
fig.tight_layout()
save(fig, "fig_cl08_layers")
