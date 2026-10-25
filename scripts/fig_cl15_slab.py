"""CL15 - land vs ocean seasonal temperature response in a slab model (Webster & Fasullo 2003, Eqs. 1-3).

C dT/dt = F0 cos(w (t - t_s)) - lam T      (T = departure from the annual mean)
Periodic steady state: amplitude F0 / sqrt(lam^2 + (C w)^2), lag phi = arctan(C w / lam).
C = rho c dz :  dry land (1500 kg/m3, 1300 J/kg/K, active depth 1 m) ; ocean e-folding depth 10 m ;
a deeper 'active' ocean layer of 50 m.  lam = 4 eps sigma T^3 (eps = 0.6, T = 289 K) = 3.3 W m-2 K-1.
F0 = 50 W m-2 is an ILLUSTRATIVE seasonal forcing amplitude, not a measurement; only the RATIOS matter.
"""
from figlib import *

lam = 4 * 0.6 * SIGMA * 289.0**3
w = 2 * np.pi / (365.25 * 86400)
F0 = 50.0
layers = [("dry land, 1 m active layer", 1500 * 1300 * 1.0, ORANGE),
          ("ocean, 10 m (Webster's e-folding depth)", 1025 * 4218 * 10.0, AQUA),
          ("ocean, 50 m active layer", 1025 * 4218 * 50.0, BLUE)]
t = np.linspace(0, 365, 731)                       # days
ts = 172.0                                         # June solstice
fig, (a, b) = plt.subplots(1, 2, figsize=(10.4, 3.9), gridspec_kw={"width_ratios": [1.6, 1]})
a.plot(t, F0 * np.cos(w * 86400 * (t - ts)) / 5, color=MUTED, lw=1.2, ls="--", label="forcing (÷5, W m$^{-2}$)")
for name, C, col in layers:
    amp = F0 / np.hypot(lam, C * w)
    phi = np.arctan2(C * w, lam)
    lag = phi / w / 86400
    a.plot(t, amp * np.cos(w * 86400 * (t - ts) - phi), color=col, label=f"{name}: ±{amp:.1f} K, lag {lag:.0f} d")
    print(f"{name}: C={C:.2e}  tau=C/lam={C/lam/86400:.1f} d  amplitude={amp:.2f} K  lag={lag:.0f} d")
a.axhline(0, color=GRID, lw=0.8)
a.set_xlim(0, 365)
a.set_xticks([0, 91, 182, 273, 365])
a.set_xticklabels(["1 Jan", "1 Apr", "1 Jul", "1 Oct", "1 Jan"])
a.set_ylabel("temperature departure (K) / scaled forcing")
a.set_title("Land follows the Sun within weeks, the ocean lags by a quarter year", fontsize=10)
a.legend(loc="lower left", fontsize=7.8)

names = ["land", "ocean 10 m", "ocean 50 m"]
amps = [F0 / np.hypot(lam, C * w) for _, C, _ in layers]
b.bar(names, amps, color=[c for _, _, c in layers], width=0.55)
for i, v in enumerate(amps):
    b.annotate(f"{v:.1f} K", (i, v), xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)
b.set_ylabel("amplitude of the annual cycle (K)")
b.set_title("Same forcing, very different swing", fontsize=10)
b.grid(axis="x", visible=False)
fig.tight_layout()
save(fig, "fig_cl15_slab")
