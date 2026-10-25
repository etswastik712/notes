"""EE01 - TOY model of opposing rainfall and nutrient gradients (my construction, NOT Holdo et al.'s model or data).

Transect x: 0 = south-east plains, 1 = north-west woodland / Lake Victoria side.
Rain R(x) rises 400 -> 1200 mm/yr (the range quoted by Holdo et al. 2009, p.433); growing season L(x) = 2 + 6x months
after the rains start; peak green biomass G(x) proportional to R; plant N falls 1 -> 0.5 (relative, assumed);
site attractiveness Z = G * N**b  (b = 3 as in Holdo's fitted exponent, 2.99 - 3.34).
"""
from figlib import *

x = np.linspace(0, 1, 201)
t = np.linspace(0, 8, 321)             # months after the rains start
R = 400 + 800 * x
L = 2 + 6 * x
Gmax = R / 1200.0
N = 1 - 0.5 * x

def Z(b):
    Zm = np.zeros((len(t), len(x)))
    for i, ti in enumerate(t):
        green = np.where(ti <= L, np.minimum(ti / 0.5, 1.0), 0.03)  # flush in 0.5 month, then dry grass
        Zm[i] = Gmax * green * N ** b
    return Zm

fig, axes = plt.subplots(1, 3, figsize=(10.6, 3.7), gridspec_kw={"width_ratios": [1, 1.25, 1.25]})
a = axes[0]
a.plot(x, R, color=BLUE, label="rainfall (mm/yr)")
a.set_ylabel("rainfall, mm per year", color=BLUE); a.set_xlabel("distance from SE plains (0) to NW woodland (1)")
a2 = a.twinx(); a2.plot(x, N, color=ORANGE); a2.set_ylabel("plant nitrogen (relative)", color=ORANGE)
a2.spines["right"].set_visible(True); a2.grid(False); a2.set_ylim(0, 1.1); a.set_ylim(0, 1300)
a.set_title("A  opposing gradients", fontsize=10)
a.annotate("rainfall rises", (0.5, 520), color=BLUE, fontsize=9); a.annotate("nitrogen falls", (0.05, 250), color=ORANGE, fontsize=9)
for ax, b, ttl in ((axes[1], 3.0, "B  cue = intake x N$^3$"), (axes[2], 0.0, "C  cue = intake only (b = 0)")):
    Zm = Z(b)
    Zn = Zm / Zm.max()
    im = ax.imshow(Zn.T, origin="lower", aspect="auto", extent=[t[0], t[-1], 0, 1], cmap="YlGn", vmin=0, vmax=1)
    path = x[np.argmax(Zm, axis=1)]
    ax.plot(t, path, color=INK, lw=2.0)
    ax.set_xlabel("months after the rains start"); ax.set_title(ttl, fontsize=10)
    ax.grid(False)
    ax.spines["top"].set_visible(True); ax.spines["right"].set_visible(True)
axes[1].set_ylabel("position on the transect")
axes[1].annotate("black line: best site\nat each moment", (3.6, 0.1), fontsize=8.5, color=INK)
axes[2].annotate("always the woodland:\nno migration", (1.6, 0.52), fontsize=8.5, color=INK)
fig.tight_layout()
fig.text(0.5, -0.04, "Toy model (my construction, illustrative numbers; not data). Shading = attractiveness Z of a site (relative to its maximum).",
         ha="center", fontsize=8.2, color=MUTED)
save(fig, "fig_ee01_gradients")
Zm = Z(3.0); pth = x[np.argmax(Zm, axis=1)]
Zm0 = Z(0.0); pth0 = x[np.argmax(Zm0, axis=1)]
for tt in (0.2, 1, 2, 3, 4, 6, 8):
    i = np.argmin(abs(t - tt)); print(f"t={tt}: best x (b=3) = {pth[i]:.2f}   (b=0) = {pth0[i]:.2f}")
