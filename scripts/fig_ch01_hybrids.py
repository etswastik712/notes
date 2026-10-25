"""CH01 - Coulson's theorem, the shape of s-p hybrid lobes, and the angle trend CH4 > NH3 > H2O."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(12.6, 4.2), gridspec_kw=dict(width_ratios=[1.15, 1, 1]))

# A: cos(theta) = S/(S-1): bond angle against s character
a = axes[0]
S = np.linspace(0.0, 0.5, 500)
theta = np.degrees(np.arccos(S / (S - 1)))
a.plot(100 * S, theta, color=INK, lw=2.0)
arrow = dict(arrowstyle="-", color=MUTED, lw=0.7)
for lab, s_, txt in (("p", 0.0, (7, 86.5)), ("sp3", 0.25, (27, 99)), ("sp2", 1 / 3, (38, 111)), ("sp", 0.5, (40, 170))):
    th_ = np.degrees(np.arccos(s_ / (s_ - 1)))
    a.plot([100 * s_], [th_], "o", color=BLUE, ms=6)
    nm = {"p": "p$^2$ (pure p)", "sp3": "sp$^3$", "sp2": "sp$^2$", "sp": "sp"}[lab]
    a.annotate(f"{nm}  {th_:.1f}°", (100 * s_, th_), xytext=txt, textcoords="data", fontsize=8, arrowprops=arrow)
Sb = np.cos(np.radians(104.5)) / (np.cos(np.radians(104.5)) - 1)
Sl = (1 - 2 * Sb) / 2
for lab, s_, c, txt in (("H$_2$O bonds", Sb, ORANGE, (2, 119)), ("H$_2$O lone pairs", Sl, AQUA, (3, 140))):
    th_ = np.degrees(np.arccos(s_ / (s_ - 1)))
    a.plot([100 * s_], [th_], "s", color=c, ms=6.5)
    a.annotate(f"{lab}\n{100 * s_:.1f}% s, {th_:.2f}°", (100 * s_, th_), xytext=txt, textcoords="data", fontsize=8, arrowprops=arrow)
a.set_xlabel("s character $S$ of two equivalent hybrids (%)"); a.set_ylabel(r"angle between them $\theta$ (°)")
a.set_xlim(-2, 52); a.set_ylim(85, 190)
a.set_title(r"A  Coulson: $\cos\theta=S/(S-1)$", fontsize=10)

# B: polar plot of the hybrid lobes
b = fig.add_subplot(1, 3, 2, projection="polar")
axes[1].remove()
th = np.linspace(0, 2 * np.pi, 800)
for S_, c, lab in ((0.5, BLUE, "sp ($S$=1/2)"), (1 / 3, ORANGE, "sp$^2$ (1/3)"), (0.25, AQUA, "sp$^3$ (1/4)"), (0.0, VIOLET, "p")):
    amp = np.sqrt(S_) / np.sqrt(4 * np.pi) + np.sqrt(1 - S_) * np.sqrt(3 / (4 * np.pi)) * np.cos(th)
    b.plot(th, np.abs(amp) ** 2 * 4 * np.pi, color=c, lw=1.8, label=lab)
b.set_yticklabels([]); b.set_xticklabels([]); b.set_title("B  lobe shape $|h(\\vartheta)|^2$", fontsize=10, pad=14)
b.legend(fontsize=7.2, loc="upper center", bbox_to_anchor=(0.5, -0.03), ncol=4, frameon=False, columnspacing=0.9, handlelength=1.4)

# C: bond angle against number of lone pairs for the tetrahedral family
c_ = axes[2]
mols = ["CH$_4$", "NH$_3$", "H$_2$O"]
ang = [109.47, 107.0, 104.5]
lp = [0, 1, 2]
c_.bar(lp, ang, color=[BLUE, ORANGE, AQUA], width=0.55)
c_.axhline(109.47, color=MUTED, lw=1.0, ls="--")
c_.axhline(90, color=GRID, lw=0.8)
for x, y, m in zip(lp, ang, mols):
    c_.text(x, y + 0.5, f"{y:.1f}°", ha="center", fontsize=9)
    c_.text(x, 87.5, m, ha="center", fontsize=9, color=INK)
Sbs = [0.25, np.cos(np.radians(107.0)) / (np.cos(np.radians(107.0)) - 1), Sb]
for x, s in zip(lp, Sbs):
    c_.text(x, 96, f"{100 * s:.1f}% s", ha="center", fontsize=8.5, color="white", fontweight="bold")
c_.set_ylim(85, 114); c_.set_xticks(lp); c_.set_xlabel("lone pairs on the central atom"); c_.set_ylabel("H–X–H angle (°)")
c_.set_title("C  lone pairs squeeze the bond angle", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.075, "A: for two equivalent s–p hybrids, orthogonality gives $S+(1-S)\\cos\\theta=0$. The H$_2$O bonds (104.5°) need only 20.0% s, which leaves 30.0% s for each lone-pair hybrid (115.35°); "
         "NH$_3$ (107°): bonds 22.6% s, lone pair 32.1% s. B: $h=\\sqrt{S}\\,s+\\sqrt{1-S}\\,p$: less s character, smaller back lobe. C: slide angles (NH$_3$ 107°).",
         ha="center", fontsize=7.8, color=MUTED, wrap=True)
save(fig, "fig_ch01_hybrids")
