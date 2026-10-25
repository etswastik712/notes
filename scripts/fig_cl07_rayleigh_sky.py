"""CL07 - Rayleigh scattering: optical depth tau_R(lambda) = 0.097 (0.55/lambda)^4 and what survives at air mass 1, 5, 38."""
from matplotlib.colors import to_rgb

from figlib import *

TAU550 = 0.0973          # Rayleigh optical depth of the whole atmosphere at 0.55 um, sea level (Bodhaine et al. 1999)
lam = np.linspace(0.38, 0.78, 400)
tauR = TAU550 * (0.55 / lam) ** 4


def wl_to_rgb(w):
    """Approximate visible colour of wavelength w (um); for the decorative strip only."""
    w = w * 1000
    if w < 440: r, g, b = -(w - 440) / 60, 0, 1
    elif w < 490: r, g, b = 0, (w - 440) / 50, 1
    elif w < 510: r, g, b = 0, 1, -(w - 510) / 20
    elif w < 580: r, g, b = (w - 510) / 70, 1, 0
    elif w < 645: r, g, b = 1, -(w - 645) / 65, 0
    else: r, g, b = 1, 0, 0
    f = 0.3 + 0.7 * min(1, (w - 380) / 40, (780 - w) / 100) if w < 420 or w > 700 else 1
    return (r * f, g * f, b * f)


fig, (a, b) = plt.subplots(1, 2, figsize=(9.4, 3.9))
a.plot(lam, tauR, color=BLUE)
for l0 in (0.45, 0.55, 0.70):
    y = TAU550 * (0.55 / l0) ** 4
    a.plot([l0], [y], "o", color=BLUE, ms=5)
    a.annotate(f"{l0:.2f} µm: τ={y:.3f}", (l0, y), xytext=(6, 6), textcoords="offset points", fontsize=8.5)
a.set_xlabel("wavelength λ (µm)")
a.set_ylabel(r"Rayleigh optical depth $\tau_R$ (vertical)")
a.set_title(r"$\tau_R\propto\lambda^{-4}$: blue is scattered most")
a.set_xlim(0.38, 0.78)
a.set_ylim(0, 0.5)

for m, c, name in [(1, BLUE, "overhead (m = 1)"), (5, ORANGE, "m = 5"), (38, AQUA, "horizon (m = 38)")]:
    b.plot(lam, np.exp(-m * tauR), color=c, label=name)
b.set_xlabel("wavelength λ (µm)")
b.set_ylabel("fraction of direct sunlight that survives")
b.set_title("Why sunsets are red")
b.set_xlim(0.38, 0.78)
b.set_ylim(-0.04, 1.02)
b.legend(loc="upper left", fontsize=8.5)
# colour strip along the bottom of the right panel
for l0 in np.linspace(0.38, 0.78, 200):
    b.axvspan(l0, l0 + 0.002, ymin=0, ymax=0.035, color=wl_to_rgb(l0), lw=0)
b.annotate("0.03 % blue at the horizon", (0.45, 0.0003 + 0.0), xytext=(0.49, 0.27), fontsize=8.5,
           arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
fig.tight_layout()
save(fig, "fig_cl07_rayleigh_sky")
for l0 in (0.40, 0.45, 0.55, 0.70):
    t = TAU550 * (0.55 / l0) ** 4
    print(f"lambda={l0}: tau_R={t:.3f}  T(m=1)={np.exp(-t):.3f}  T(m=5)={np.exp(-5*t):.3f}  T(m=38)={np.exp(-38*t):.2e}")
