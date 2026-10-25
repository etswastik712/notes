"""CL09 - GFD Lab II: convection burrowing into a stably stratified tank heated from below (M&P Fig. 4.28, Eq. 4-31, Problem 3).

Model: rho cp dT/dt = H/h with a well-mixed layer of depth h that 'joins on' to the initial profile T = T0 + Tz z.
  rho cp Tz/2 d(h^2)/dt = H   =>   h = sqrt(2 H t / (rho cp Tz)),   T - T0 = Tz h.
Illustrative numbers: rho = 1000, cp = 4186, Tz = 50 K/m, H = 500 W/m^2.
"""
from figlib import *

rho, cp, Tz, H, T0 = 1000.0, 4186.0, 50.0, 500.0, 20.0


def h(t):
    return np.sqrt(2 * H * t / (rho * cp * Tz))


print(f"h(600 s) = {h(600)*100:.2f} cm, mixed-layer warming Tz*h = {Tz*h(600):.2f} K; h(2400 s) = {h(2400)*100:.1f} cm (x2 for 4x time)")
fig, (a, b) = plt.subplots(1, 2, figsize=(9.2, 4.2))
z = np.linspace(0, 0.30, 300)
a.plot(T0 + Tz * z, z * 100, color=MUTED, lw=1.6, ls="--", label="t = 0 (initial)")
for t, c in ((300, AQUA), (900, BLUE), (1800, ORANGE)):
    hh = h(t)
    Tp = np.where(z < hh, T0 + Tz * hh, T0 + Tz * z)
    a.plot(Tp, z * 100, color=c, lw=2, label=f"t = {t//60} min: h = {hh*100:.1f} cm")
a.set_xlabel("temperature (°C)")
a.set_ylabel("height above the heater (cm)")
a.set_title("A mixed layer burrows into the stratification", fontsize=10.5)
a.legend(fontsize=8.2, loc="upper left")
a.set_xlim(19.5, 36)

t = np.linspace(0, 3600, 300)
b.plot(np.sqrt(t), h(t) * 100, color=BLUE, lw=2, label="mixed-layer depth h (cm)")
b.plot(np.sqrt(t), Tz * h(t), color=ORANGE, lw=2, label=r"warming $T-T_0$ (K)")
b.set_xlabel(r"$\sqrt{t}$  (s$^{1/2}$)")
b.set_ylabel("h (cm)  or  warming (K)")
b.set_title(r"Both grow like $\sqrt{t}$ (straight lines)", fontsize=10.5)
b.legend(fontsize=8.4, loc="upper left")
fig.tight_layout()
save(fig, "fig_cl09_lab_convection")
