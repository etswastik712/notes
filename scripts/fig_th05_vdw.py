"""TH05 - stability: van der Waals isotherms of CO2, the unstable region where (dP/dV)_T > 0, and the critical point."""
from figlib import *

R = 8.314462618; a_, b_ = 0.364, 4.267e-5
Tc = 8 * a_ / (27 * R * b_); Pc = a_ / (27 * b_ ** 2); Vc = 3 * b_
P = lambda V, T: R * T / (V - b_) - a_ / V ** 2
dP = lambda V, T: -R * T / (V - b_) ** 2 + 2 * a_ / V ** 3
V = np.linspace(b_ * 1.2, 6.5e-4, 3000)
fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.1))
a = axes[0]
cols = {280: BLUE, 300: AQUA, Tc: INK, 330: ORANGE}
for T, c in cols.items():
    lab = f"$T_c={Tc:.0f}$ K (critical)" if T == Tc else f"{T:.0f} K"
    a.plot(V * 1e6, P(V, T) / 1e6, color=c, lw=2.0 if T != Tc else 2.4, label=lab)
    if T < Tc:
        m = dP(V, T) > 0
        a.plot(V[m] * 1e6, P(V, T)[m] / 1e6, color=RED, lw=4.0, alpha=0.5, solid_capstyle="butt")
a.plot([Vc * 1e6], [Pc / 1e6], "o", color=INK, ms=7)
a.annotate(f"critical point\n$P_c={Pc / 1e6:.2f}$ MPa\n$V_c={Vc * 1e6:.0f}$ cm$^3$/mol", (Vc * 1e6, Pc / 1e6), xytext=(215, 8.9), fontsize=8.4, arrowprops=dict(arrowstyle="-", color=MUTED, lw=0.8))
a.set_xlim(50, 650); a.set_ylim(0, 14); a.set_xlabel(r"molar volume (cm$^3$/mol)"); a.set_ylabel("$P$ (MPa)")
a.legend(fontsize=8.2, loc="upper right", title="isotherms", title_fontsize=8.2); a.set_title(r"A  red: $(\partial P/\partial V)_T>0$, forbidden by stability", fontsize=10)
b = axes[1]
Ts = np.linspace(250, Tc, 400)
lo, hi = [], []
for T in Ts:
    Vs = np.linspace(b_ * 1.02, 7e-4, 40000); d = dP(Vs, T)
    idx = np.where(np.diff(np.sign(d)))[0]
    if len(idx) >= 2: lo.append((Vs[idx[0]], T)); hi.append((Vs[idx[-1]], T))
lo = np.array(lo); hi = np.array(hi)
b.fill_betweenx(lo[:, 1], lo[:, 0] * 1e6, hi[:, 0] * 1e6, color=RED, alpha=0.25, label="unstable: $(\\partial P/\\partial V)_T>0$")
b.plot(lo[:, 0] * 1e6, lo[:, 1], color=RED); b.plot(hi[:, 0] * 1e6, hi[:, 1], color=RED)
b.plot([Vc * 1e6], [Tc], "o", color=INK, ms=7); b.text(Vc * 1e6 + 6, Tc - 6, "critical point", fontsize=8.6)
b.set_xlabel(r"molar volume (cm$^3$/mol)"); b.set_ylabel("$T$ (K)"); b.set_xlim(50, 400); b.set_ylim(250, 320); b.legend(fontsize=8.2, loc="lower right")
b.set_title("B  the spinodal region closes at $T_c$", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.03, "van der Waals CO$_2$ ($a=0.364$ Pa m$^6$ mol$^{-2}$, $b=4.267\\times10^{-5}$ m$^3$ mol$^{-1}$): $T_c=8a/27Rb=304.0$ K (real 304.1 K), $P_c=a/27b^2=7.40$ MPa (real 7.38).", ha="center", fontsize=8.0, color=MUTED)
save(fig, "fig_th05_vdw")
