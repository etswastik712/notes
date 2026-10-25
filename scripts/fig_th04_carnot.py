"""TH04 - the Carnot cycle of a monatomic ideal gas in PV and TS."""
from figlib import *

R = 8.314462618; g = 5 / 3
TH, TC = 500.0, 300.0; n = 1.0
V1, V2 = 1.0e-3, 2.0e-3
V3 = V2 * (TH / TC) ** (1 / (g - 1)); V4 = V1 * (TH / TC) ** (1 / (g - 1))
def iso(Va, Vb, T): V = np.linspace(Va, Vb, 200); return V, n * R * T / V
def adi(Va, Vb, Ta): V = np.linspace(Va, Vb, 200); return V, n * R * Ta * (Va / V) ** g * V ** (g - 1) / V ** (g - 1) / V * (V / V) if False else n * R * Ta / V * (Va / V) ** (g - 1)
fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.0))
a = axes[0]
Vv, Pv = iso(V1, V2, TH); a.plot(Vv * 1e3, Pv / 1e3, color=ORANGE, lw=2.2)
Vv, Pv = iso(V4, V3, TC); a.plot(Vv * 1e3, Pv / 1e3, color=BLUE, lw=2.2)
Vv, Pv = V2 * np.ones(1), None
Va = np.linspace(V2, V3, 200); a.plot(Va * 1e3, n * R * TH / Va * (V2 / Va) ** (g - 1) / 1e3, color=INK, lw=1.6)
Vb = np.linspace(V1, V4, 200); a.plot(Vb * 1e3, n * R * TH / Vb * (V1 / Vb) ** (g - 1) / 1e3, color=INK, lw=1.6)
for lab, V, T in (("1", V1, TH), ("2", V2, TH), ("3", V3, TC), ("4", V4, TC)):
    a.plot([V * 1e3], [n * R * T / V / 1e3], "o", color=INK, ms=6); a.text(V * 1e3 + 0.07, n * R * T / V / 1e3 + 80, lab, fontsize=10)
a.text(1.45, 3300, r"$Q_H=2882$ J in at $T_H$", fontsize=8.6, color=ORANGE); a.text(2.6, 180, r"$Q_C=1729$ J out at $T_C$", fontsize=8.6, color=BLUE)
a.text(2.35, 1550, r"$W=1153$ J", fontsize=9)
a.set_xlabel("$V$ (L)"); a.set_ylabel("$P$ (kPa)"); a.set_title("A  Carnot cycle, PV plane", fontsize=10); a.set_xlim(0.6, 5.0); a.set_ylim(0, 4400)
b = axes[1]
dS = n * R * np.log(V2 / V1)
b.plot([0, dS], [TH, TH], color=ORANGE, lw=2.2); b.plot([dS, 0], [TC, TC], color=BLUE, lw=2.2)
b.plot([dS, dS], [TH, TC], color=INK, lw=1.6); b.plot([0, 0], [TC, TH], color=INK, lw=1.6)
b.fill_between([0, dS], [TC, TC], [TH, TH], color=AQUA, alpha=0.16); b.fill_between([0, dS], [0, 0], [TC, TC], color=BLUE, alpha=0.10)
b.text(dS / 2, (TH + TC) / 2, "work $W$\n$=(T_H-T_C)\\Delta S$", ha="center", fontsize=9)
b.text(dS / 2, TC / 2, r"$Q_C=T_C\Delta S$", ha="center", fontsize=9); b.text(dS / 2, TH + 12, r"$Q_H=T_H\Delta S$", ha="center", fontsize=9)
b.set_xlabel(r"$S-S_1$ (J/K), $\Delta S=R\ln2=5.76$"); b.set_ylabel("$T$ (K)"); b.set_ylim(0, 570); b.set_xlim(-0.8, dS + 0.8)
b.set_title(r"B  a rectangle in $TS$: $\eta=1-T_C/T_H=0.40$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "Monatomic ideal gas, 1 mol, $T_H=500$ K, $T_C=300$ K, $V_1=1$ L, $V_2=2$ L: $V_3=4.30$ L, $V_4=2.15$ L (computed). Adiabats $TV^{\\gamma-1}$ = const.", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th04_carnot")
