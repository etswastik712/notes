"""CL25: salt ledger numbers + figure (Joy O5).  Equation of state: UNESCO EOS-80 (Millero & Poisson 1981) at p = 0, RECALLED, not read;
validated below against Joy's TEOS-10 numbers.   .venv/bin/python -I scripts/fig_cl25.py"""
import os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa


def rho(S, T):
    rw = 999.842594 + 6.793952e-2 * T - 9.095290e-3 * T ** 2 + 1.001685e-4 * T ** 3 - 1.120083e-6 * T ** 4 + 6.536332e-9 * T ** 5
    A = 8.24493e-1 - 4.0899e-3 * T + 7.6438e-5 * T ** 2 - 8.2467e-7 * T ** 3 + 5.3875e-9 * T ** 4
    B = -5.72466e-3 + 1.0227e-4 * T - 1.6546e-6 * T ** 2
    return rw + A * S + B * S ** 1.5 + 4.8314e-4 * S ** 2


def tfreeze(S):
    return -0.0575 * S + 1.710523e-3 * S ** 1.5 - 2.154996e-4 * S ** 2


print("pure water: rho(4C)=%.4f rho(0)=%.4f rho(25)=%.4f ; seawater S=35: rho(0)=%.3f rho(10)=%.3f rho(25)=%.3f" % (rho(0, 4), rho(0, 0), rho(0, 25), rho(35, 0), rho(35, 10), rho(35, 25)))
print("freezing point S=35: %.2f C (Joy TEOS-10: -1.92)" % tfreeze(35))
def ab(S, T, h=1e-3):
    r = rho(S, T)
    return (-(rho(S, T + h) - rho(S, T - h)) / (2 * h), (rho(S + h, T) - rho(S - h, T)) / (2 * h))
for T in (25, 0):
    a, b = ab(35, T); print("T=%2d C S=35: rho*alpha = %.3f kg/m3 per K ; rho*beta = %.3f per g/kg  -> 1 g/kg worth %.2f K ; +1 kg/m3 = %.1f K cooling or %.2f g/kg   (Joy: 25C 0.30/0.74, 3.3 K or 1.4 g/kg; 0C 0.054/0.80, 18 K or 1.2 g/kg)" % (T, a, b, b / a, 1 / a, 1 / b))
print("sigma Arabian Sea surface (S=36.2,T=27.5): %.1f ; Bay of Bengal (32.9, 28.3): %.1f  (Joy 23.4 / 20.7)" % (rho(36.2, 27.5) - 1000, rho(32.9, 28.3) - 1000))
print("N Pacific surface (32.8, 8.4) cooled to freezing: sigma %.1f at %.2f C (Joy 26.4 at -1.8) ; N Atlantic (35.1,10.3) cooled to 4C: %.1f (Joy 27.8 below ~4C)" % (rho(32.8, tfreeze(32.8)) - 1000, tfreeze(32.8), rho(35.1, 4.0) - 1000))
print("N Atlantic cooled to 4C sigma %.2f ; to 2C %.2f ; to -1.8C %.2f" % (rho(35.1, 4) - 1000, rho(35.1, 2) - 1000, rho(35.1, -1.8) - 1000))
print("accountant: 50 m layer, S=35, loses 1 m/yr -> dS = %.2f g/kg per yr" % (35 * 1 / 50))
print("E-P 2.7 mm/day = %.2f m/yr" % (2.7e-3 * 365.25))
wm = {"NADW": (4.0, 35.0), "AAIW": (3.3, 34.15), "AABW": (0.4, 34.67)}
for k, (T, S) in wm.items(): print("%s T=%.1f S=%.2f sigma=%.2f" % (k, T, S, rho(S, T) - 1000))
# cabbeling: 50/50 mix of AAIW and NADW (linear in T,S) vs mean of densities
T1, S1 = wm["AAIW"]; T2, S2 = wm["NADW"]
print("50/50 AAIW+NADW: sigma(mix) %.4f vs mean of sigmas %.4f -> excess %.4f kg/m3" % (rho((S1 + S2) / 2, (T1 + T2) / 2) - 1000, ((rho(S1, T1) + rho(S2, T2)) / 2) - 1000, rho((S1 + S2) / 2, (T1 + T2) / 2) - (rho(S1, T1) + rho(S2, T2)) / 2))
T1, S1, T2, S2 = 0.0, 34.0, 20.0, 36.0  # strongly different: equal-density-ish? find S2 giving same sigma at T=20
from math import isclose
tgt = rho(34.0, 0.0)
S2 = next(s for s in np.arange(30, 40, 0.001) if rho(s, 20.0) >= tgt)
print("two waters of equal sigma %.2f: (0C, 34.0) and (20C, %.2f); 50/50 mix is denser by %.3f kg/m3" % (tgt - 1000, S2, rho((34.0 + S2) / 2, 10.0) - tgt))
print("Atlantic 35.6 vs Pacific 34.6 (WOCE 30S-60N, Joy); Broecker 0.32 Sv: over 1000 yr a 1 g/L change ; Amazon ~0.2 Sv (Stewart: 'a little more than')")
print("fraction of volume with sigma>27.4: 75% (Hartmann p.225 via Joy), WOCE 78%; of surface: 4% (Hartmann), 1.4% annual (Joy)")

fig, ax = plt.subplots(1, 3, figsize=(14.2, 4.6))
a = ax[0]
S = np.linspace(32.4, 37.2, 60); T = np.linspace(-2.5, 30, 120)
SS, TT = np.meshgrid(S, T); sg = rho(SS, TT) - 1000
cs = a.contour(SS, TT, sg, levels=np.arange(21, 29), colors="#4b55a8", linewidths=1.0); a.clabel(cs, fmt="%d", fontsize=7)
a.plot(S, tfreeze(S), color="#888", lw=1.2); a.text(32.5, -2.3, "freezing", fontsize=7.5, color="#666")
pts = {"warm subtropics": (25, 36.0), "NADW": wm["NADW"], "AAIW": wm["AAIW"], "AABW": wm["AABW"], "N Pacific surface": (8.4, 32.8), "N Atlantic surface": (10.3, 35.1)}
cols = {"warm subtropics": ORANGE, "NADW": ORANGE, "AAIW": BLUE, "AABW": INK, "N Pacific surface": AQUA, "N Atlantic surface": ORANGE}
for k, (Tk, Sk) in pts.items():
    a.plot(Sk, Tk, "o", color=cols[k], ms=5.5); a.text(Sk + 0.06, Tk + 0.5, k, fontsize=7.6, color=cols[k])
a.plot([wm["AAIW"][1], wm["NADW"][1]], [wm["AAIW"][0], wm["NADW"][0]], color="#999", lw=1, ls="--")
a.set_xlabel("salinity (g/kg)"); a.set_ylabel("temperature (°C)"); a.set_xlim(32.4, 37.2); a.set_ylim(-2.5, 30)
a.set_title("A  T–S diagram, σ = ρ − 1000 (EOS-80, p = 0)", fontsize=9.8)
b = ax[1]
Ts = np.linspace(-1.9, 30, 100)
al = np.array([ab(35, t)[0] for t in Ts]); be = np.array([ab(35, t)[1] for t in Ts])
b.plot(Ts, al, color=ORANGE, lw=2, label="ρα  (kg m⁻³ per K of cooling)"); b.plot(Ts, be, color=BLUE, lw=2, label="ρβ  (kg m⁻³ per g/kg)")
b.set_xlabel("temperature (°C), S = 35"); b.set_ylabel("density sensitivity"); b.legend(fontsize=8, frameon=False, loc="center right")
b.text(1, 0.62, "cold: salt decides", fontsize=8.5); b.text(15, 0.12, "warm: temperature\ndoes most of the work", fontsize=8.5)
b.set_title("B  what controls density", fontsize=9.8)
c = ax[2]
boxes = [("N Atl subtropics", 2.8, 37.2), ("S Pac subtropics", 3.3, 36.2), ("E Pac rain band", -3.9, 33.8), ("W Pac warm pool", -3.6, 34.5), ("Arabian Sea", 2.5, 36.2), ("Bay of Bengal", -1.1, 32.9)]
for nm, ep, sl in boxes:
    c.plot(ep, sl, "o", color=BLUE, ms=6)
    c.text(ep - 0.15 if nm == "Arabian Sea" else ep + 0.15, sl - 0.05 + (0.12 if nm == "S Pac subtropics" else 0), nm, fontsize=7.6, ha="right" if nm == "Arabian Sea" else "left")
c.set_xlabel("E − P  (mm/day, 2010–2020 box mean)"); c.set_ylabel("surface salinity (g/kg, WOCE)"); c.set_xlim(-5, 5.8)
c.set_title("C  salinity records E − P (Joy's box means)", fontsize=9.8)
fig.subplots_adjust(wspace=0.3)
save(fig, "fig_cl25_salt")
