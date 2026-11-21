#!/usr/bin/env python3
"""CH11 figure: (A) sigma-only MO diagram of an octahedral ML6; (B) pi donor / sigma only / pi acceptor and Delta_O."""
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
fig, (a, b) = plt.subplots(1, 2, figsize=(12, 6.2), gridspec_kw={"width_ratios": [1.25, 1]})
def lev(ax, x, y, n, lab, col="k", w=0.42, labside="right"):
    g = 0.06; tot = n * w / 1.6 + (n - 1) * g; x0 = x - tot / 2
    for i in range(n): ax.plot([x0 + i * (w / 1.6 + g), x0 + i * (w / 1.6 + g) + w / 1.6], [y, y], color=col, lw=2.2)
    ax.text(x + tot / 2 + 0.06 if labside == "right" else x - tot / 2 - 0.06, y, lab, va="center", ha="left" if labside == "right" else "right", fontsize=9, color=col)
# metal
lev(a, 0, 6.0, 3, "4p", "#1f4e79", labside="left"); lev(a, 0, 4.6, 1, "4s", "#1f4e79", labside="left"); lev(a, 0, 3.0, 5, "3d", "#1f4e79", labside="left")
# ligands
lev(a, 4, 1.0, 6, "6 σ (ligand lone pairs)", "#c0392b")
# complex
L = {"t1u*": 7.6, "a1g*": 6.9, "eg*": 4.3, "t2g": 3.0, "eg": 0.3, "t1u": -0.3, "a1g": -0.9}
N = {"t1u*": 3, "a1g*": 1, "eg*": 2, "t2g": 3, "eg": 2, "t1u": 3, "a1g": 1}
for k, y in L.items(): lev(a, 2, y, N[k], k, "#117a65" if k != "t2g" else "k")
for k in ("eg*", "eg"): a.plot([0.55, 1.6], [3.0, L[k]], ":", color="0.5", lw=0.8); a.plot([2.45, 3.3], [L[k], 1.0], ":", color="0.5", lw=0.8)
a.plot([0.55, 1.6], [3.0, 3.0], ":", color="0.5", lw=0.8)
a.annotate("", (2.0 + 0.55, 4.3), (2.0 + 0.55, 3.0), arrowprops=dict(arrowstyle="<->", color="#7d3c98", lw=1.6)); a.text(2.62, 3.65, "Δ$_O$", color="#7d3c98", fontsize=12)
a.add_patch(plt.Rectangle((1.25, 2.6), 1.5, 2.1, fill=False, ls="--", ec="#7d3c98", lw=1))
a.text(2.0, 2.35, "frontier orbitals (the CFT pair)", ha="center", fontsize=8.5, color="#7d3c98")
a.text(2.0, -1.55, "12 ligand electrons fill a1g, t1u, eg (mostly ligand);\nthe metal's n d electrons go into t2g (nonbonding) and eg* (antibonding)", ha="center", fontsize=8.5)
a.set_xlim(-1.2, 5.6); a.set_ylim(-2, 8.3); a.axis("off"); a.set_title("A. σ-only octahedral ML$_6$ (after S&A Fig. 20.16, Huheey Fig. 11.20)", fontsize=10)
for i, (lab, dy, col) in enumerate([("π donor\n(F⁻, Cl⁻, OH⁻, H₂O)", +0.6, "#c0392b"), ("σ only\n(NH₃, CH₃⁻, H⁻)", 0.0, "k"), ("π acceptor\n(CO, CN⁻, PR₃)", -0.6, "#1f4e79")]):
    x = i * 1.6; eg, t2 = 4.0, 2.0 + dy
    b.plot([x - 0.4, x + 0.4], [eg, eg], color="k", lw=2.2); b.plot([x - 0.4, x + 0.4], [t2, t2], color=col, lw=2.2)
    b.annotate("", (x + 0.5, eg), (x + 0.5, t2), arrowprops=dict(arrowstyle="<->", color="#7d3c98")); b.text(x + 0.55, (eg + t2) / 2, f"Δ$_O$", color="#7d3c98", fontsize=10, va="center")
    b.text(x - 0.42, eg + 0.15, "eg*", fontsize=8.5); b.text(x - 0.42, t2 - 0.35, "t2g" + ("*" if dy > 0 else "" if dy == 0 else " (bonding)"), fontsize=8.5, color=col)
    b.text(x, 0.6, lab, ha="center", fontsize=9, color=col)
b.text(0, 5.0, "filled ligand π below d:\nt2g pushed UP → Δ$_O$ smaller", ha="center", fontsize=8.5, color="#c0392b")
b.text(3.2, 5.0, "empty ligand π* above d:\nt2g pulled DOWN → Δ$_O$ larger", ha="center", fontsize=8.5, color="#1f4e79")
b.set_xlim(-0.9, 4.2); b.set_ylim(0, 5.8); b.axis("off"); b.set_title("B. π bonding and Δ$_O$ (S&A §20.2b; Huheey 11.26–11.27)", fontsize=10)
fig.tight_layout(); fig.savefig("Assets/figures/fig_ch11_ligand_field.png", dpi=140); print("ok")
