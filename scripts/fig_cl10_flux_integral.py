"""CL10 - from net radiation to the poleward energy flux.

(a) R_TOA against latitude: the negative (polar) area *looks* bigger than the positive (tropical) one.
(b) R_TOA cos(phi): belts are weighted by their circumference; the two areas are equal (global-mean net radiation = 0).
(c) F(phi) = 2 pi a^2 Int_{-pi/2}^{phi} R cos(phi') dphi': northward flux, zero at both poles, maximal where R changes sign.
    The atmosphere/ocean split is a schematic curve through the values quoted by Hartmann (2.0 PW each at 20 deg N), not data.
Profile idealised (cl10lib.toa_profiles): see fig_cl10_toa_budget.py.
"""
from cl10lib import *
from figlib import *

lat = np.linspace(-90, 90, 1801)
phi = np.radians(lat)
Q, ASR, OLR, R = toa_profiles(phi)
F = poleward_flux(phi, R) / 1e15
O = ocean_flux(lat)
A = F - O
dphi = phi[1] - phi[0]
pos_plain = np.sum(np.clip(R, 0, None)) * dphi
neg_plain = np.sum(np.clip(-R, 0, None)) * dphi
pos_w = np.sum(np.clip(R, 0, None) * np.cos(phi)) * dphi
neg_w = np.sum(np.clip(-R, 0, None) * np.cos(phi)) * dphi
print(f"unweighted areas (W m-2 rad): + {pos_plain:.1f}, - {neg_plain:.1f}, ratio {neg_plain / pos_plain:.2f}")
print(f"cos-weighted areas:            + {pos_w:.2f}, - {neg_w:.2f}, ratio {neg_w / pos_w:.4f}")
i = F.argmax()
print(f"peak flux {F.max():.2f} PW at {lat[i]:.1f} N; F(-90)={F[0]:.3f}, F(90)={F[-1]:.3f} PW; F(20N)={F[np.argmin(abs(lat - 20))]:.2f} PW")
print(f"ocean at 20N {np.interp(20, lat, O):.2f}, atmosphere at 20N {np.interp(20, lat, A):.2f}; atmosphere max {A.max():.2f} at {lat[A.argmax()]:.0f}")
print(f"cap check: F(40N) from south = {np.interp(40, lat, F):.2f}; minus cap north of 40 = {-2*np.pi*A_EARTH**2*np.sum((R*np.cos(phi))[lat >= 40])*dphi/1e15:.2f}")

fig, (a, b, c) = plt.subplots(1, 3, figsize=(12.4, 3.9))
for ax, y, lab in ((a, R, "$R_{TOA}$ (W m$^{-2}$)"), (b, R * np.cos(phi), "$R_{TOA}\\cos\\varphi$ (W m$^{-2}$)")):
    ax.axhline(0, color=MUTED, lw=0.8)
    ax.plot(lat, y, color=INK, lw=2.0)
    ax.fill_between(lat, y, 0, where=y > 0, color=ORANGE, alpha=0.30, lw=0)
    ax.fill_between(lat, y, 0, where=y < 0, color=BLUE, alpha=0.30, lw=0)
    ax.set_xlim(-90, 90)
    ax.set_xticks(range(-90, 91, 30))
    ax.set_xlabel("latitude (°)")
    ax.set_ylabel(lab)
a.set_title("(a) plotted against φ: deficit looks bigger", fontsize=10)
a.annotate("tropical surplus", (0, 38), ha="center", fontsize=8.5)
a.annotate("polar deficit", (-72, -35), ha="center", fontsize=8.5)
a.annotate("polar deficit", (72, -35), ha="center", fontsize=8.5)
b.set_title("(b) weighted by circumference: areas equal", fontsize=10)
b.annotate(f"+{pos_w:.2f} = −{neg_w:.2f}", (0, -28), ha="center", fontsize=9)

c.axhline(0, color=MUTED, lw=0.8)
c.plot(lat, F, color=INK, lw=2.4, label="total")
c.plot(lat, A, color=ORANGE, lw=1.8, label="atmosphere (schematic)")
c.plot(lat, O, color=BLUE, lw=1.8, label="ocean (schematic)")
c.plot([lat[i]], [F[i]], "o", color=INK, ms=5)
c.annotate(f"peak {F[i]:.1f} PW\nat {lat[i]:.0f}°", (lat[i], F[i]), xytext=(10, -2), textcoords="offset points", fontsize=8.5)
c.legend(loc="lower right", fontsize=8)
c.set_xlim(-90, 90)
c.set_xticks(range(-90, 91, 30))
c.set_ylim(-7, 7)
c.set_xlabel("latitude (°)")
c.set_ylabel("northward energy flux (PW)")
c.set_title("(c) running total = poleward transport", fontsize=10)
fig.tight_layout()
save(fig, "fig_cl10_flux_integral")
