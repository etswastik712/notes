"""TH08 figure: dG(T), van 't Hoff, Clausius-Clapeyron, G(xi)."""
from figlib import *
from scipy import optimize
R = 8.314462618
fig, axes = plt.subplots(2, 2, figsize=(10.4, 7.8))

# A dG(T) water-gas
a = axes[0, 0]
dH, dS, dCp = 131.29e3, 133.78, 15.85
T = np.linspace(298.15, 1300, 300)
g0 = dH - T * dS
g1 = dH + dCp * (T - 298.15) - T * (dS + dCp * np.log(T / 298.15))
a.plot(T, g0 / 1000, color=MUTED, label="constant $\\Delta H^\\circ$, $\\Delta S^\\circ$")
a.plot(T, g1 / 1000, color=BLUE, label="with $\\Delta C_p=+15.85$ J K$^{-1}$")
a.axhline(0, color=INK, lw=0.8)
a.axvline(981.4, color=MUTED, ls=":", lw=1); a.axvline(930.8, color=BLUE, ls=":", lw=1)
a.text(985, 60, "981 K", color=MUTED, fontsize=8.5); a.text(870, 60, "931 K", color=BLUE, fontsize=8.5, ha="right")
a.fill_between(T, -60, 0, where=T > 930.8, color=BLUE, alpha=0.07)
a.set_ylim(-45, 100); a.set_xlabel("$T$ / K"); a.set_ylabel(r"$\Delta_rG^\circ$ / kJ mol$^{-1}$"); a.legend(fontsize=8.5, loc="upper right")
a.set_title("A  C + H$_2$O(g) $\\to$ CO + H$_2$: where $\\Delta G^\\circ$ changes sign", fontsize=10)

# B van 't Hoff
b = axes[0, 1]
Tinv = np.linspace(1 / 900, 1 / 280, 200)
dHn, dGn, T0 = -92.22e3, -32.90e3, 298.15
lnK0 = -dGn / (R * T0)
lnK = lnK0 - dHn / R * (Tinv - 1 / T0)
dCpn = -5.48
Tn = 1 / Tinv
dHT = dHn + dCpn * (Tn - T0); dST = (dHn - dGn) / T0 + dCpn * np.log(Tn / T0)
lnKc = -(dHT - Tn * dST) / (R * Tn)
b.plot(1000 * Tinv, lnK, color=BLUE, label="constant $\\Delta H^\\circ$ (straight line)")
b.plot(1000 * Tinv, lnKc, color=ORANGE, ls="--", label="with $\\Delta C_p=-5.48$ J K$^{-1}$")
for TT, lab in ((298.15, "298 K: $K=5.8\\times10^5$"), (773.15, "773 K: $K=6.9\\times10^{-5}$")):
    y = lnK0 - dHn / R * (1 / TT - 1 / T0); b.plot([1000 / TT], [y], "o", color=INK); b.annotate(lab, (1000 / TT, y), ((2.15 if TT < 500 else 1.45), (y - 3.0 if TT < 500 else -13.5)), fontsize=8.5, ha="left" if TT > 500 else "left")
b.set_ylim(-16, 18); b.set_xlabel("$1000/T$ / K$^{-1}$"); b.set_ylabel("$\\ln K$"); b.legend(fontsize=8.5, loc="upper left")
b.set_title("B  van 't Hoff: slope $=-\\Delta H^\\circ/R$ (N$_2$+3H$_2\\to$2NH$_3$)", fontsize=10)

# C Clausius-Clapeyron
c = axes[1, 0]
def Pcc(T, Tref, Pref, L): return Pref * np.exp(-L / R * (1 / T - 1 / Tref))
Tt = np.linspace(330, 400, 200)
c.plot(Tt - 273.15, Pcc(Tt, 353.15, 1.0, 40e3), color=BLUE, label="unknown liquid: $L=40$ kJ mol$^{-1}$, $T_b=80$ °C")
c.plot(Tt - 273.15, Pcc(Tt, 373.15, 1.0, 40.66e3), color=ORANGE, label="water: $L=40.66$ kJ mol$^{-1}$")
c.plot([80, 85.88], [1.0, 1.25], "o", color=BLUE); c.annotate("", xy=(85.88, 1.25), xytext=(80, 1.0), arrowprops=dict(arrowstyle="->", color=INK))
c.text(82.2, 1.33, "+25 % pressure\n$\\Rightarrow$ boiling point +5.88 K", fontsize=8.5)
Tev = 1 / (1 / 373.15 - R / 40.66e3 * np.log(33.7 / 101.325)); c.plot([Tev - 273.15], [33.7 / 101.325], "s", color=ORANGE); c.annotate("water, 33.7 kPa: %.1f °C" % (Tev - 273.15), (Tev - 273.15, 33.7 / 101.325), (62, 0.55), fontsize=8.5, arrowprops=dict(arrowstyle="-", color=MUTED))
c.axhline(1.0, color=MUTED, lw=0.8, ls=":")
c.set_xlabel("temperature / °C"); c.set_ylabel("vapour pressure / atm"); c.set_ylim(0.1, 2.3); c.legend(fontsize=8.2, loc="upper left")
c.set_title("C  Clausius–Clapeyron: the boiling point moves with pressure", fontsize=10)

# D G(xi)
d = axes[1, 1]
x = np.linspace(1e-4, 1 - 1e-4, 400)
for K, col in ((0.1, AQUA), (1.0, BLUE), (10.0, ORANGE)):
    dG0 = -np.log(K)
    G = x * np.log(x) + (1 - x) * np.log(1 - x) + x * dG0
    d.plot(x, G, color=col, label=f"$K={K:g}$")
    xe = K / (1 + K); Ge = xe * np.log(xe) + (1 - xe) * np.log(1 - xe) + xe * dG0
    d.plot([xe], [Ge], "o", color=col)
d.set_xlabel(r"extent $\xi$ of A $\to$ B (fraction converted)"); d.set_ylabel("$(G-G_A^\\circ)/RT$ (ideal-gas mixture)"); d.legend(fontsize=8.5, loc="upper center")
d.set_title("D  Equilibrium is the minimum of $G(\\xi)$; slope $=\\Delta G$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.012, "Computed in scripts/th_tutorial_numbers.py. Water-gas data and NH$_3$ data: Schroeder pp. 404-405. Everest pressure 33.7 kPa and $L_{water}=40.66$ kJ mol$^{-1}$ are recalled.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th08_gibbs_equilibrium")
