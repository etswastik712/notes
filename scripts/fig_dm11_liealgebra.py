"""DM11 - left-invariant frame on Aff(1) (upper half-plane), dimensions of the matrix Lie algebras, and su(2) -> so(3) (the double cover seen along a one-parameter subgroup)."""
from figlib import *

fig, axes = plt.subplots(1, 3, figsize=(13.8, 4.5), gridspec_kw=dict(width_ratios=[1.15, 1.05, 1]))

# A: left-invariant fields X1 = a d_b, X2 = a d_a on Aff(1) = {(b, a): a > 0} -----------------------------------------------------------------------------
a = axes[0]
pts = [(0, 1), (1.2, 1), (2.4, 1), (0, 2), (1.2, 2), (2.4, 2), (0.6, 0.5), (1.8, 0.5)]
for (b, aa) in pts:
    a.annotate("", xy=(b + 0.45 * aa, aa), xytext=(b, aa), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.4))
    a.annotate("", xy=(b, aa + 0.45 * aa), xytext=(b, aa), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4))
    a.scatter([b], [aa], color=INK, s=14, zorder=4)
a.scatter([0], [1], color=RED, s=60, facecolors="none", linewidths=1.8, zorder=5)
a.text(0.05, 0.62, "e = (0, 1)", color=RED, fontsize=8.6)
from matplotlib.lines import Line2D
a.legend(handles=[Line2D([0], [0], color=BLUE, lw=2, label="X₁ = a ∂_b"), Line2D([0], [0], color=ORANGE, lw=2, label="X₂ = a ∂_a"), Line2D([0], [0], color="none", label="[X₁, X₂] = −X₁")], fontsize=8.4, loc="upper right", frameon=True)
a.set_xlim(-0.4, 3.3); a.set_ylim(0.2, 4.2); a.set_aspect("equal"); a.set_xlabel("b"); a.set_ylabel("a")
a.set_title("A  Lie(Aff(1)): left-invariant frame", fontsize=9.8)

# B: dimensions of the matrix Lie algebras (kernels of the differentials at I) -------------------------------------------------------------------------
b = axes[1]
ns = np.array([2, 3, 4])
dims = {"so(n)": ns * (ns - 1) // 2, "sl(n, ℝ)": ns ** 2 - 1, "su(n)": ns ** 2 - 1, "u(n)": ns ** 2}
cols = {"so(n)": VIOLET, "sl(n, ℝ)": BLUE, "su(n)": AQUA, "u(n)": ORANGE}
w = 0.2
for i, (k, v) in enumerate(dims.items()):
    xs = np.arange(3) + (i - 1.5) * w
    b.bar(xs, v, w, color=cols[k], label=k)
    for xi, vi in zip(xs, v):
        b.text(xi, vi + 0.25, str(vi), ha="center", fontsize=7.4)
b.set_xticks(range(3)); b.set_xticklabels(["n = 2", "n = 3", "n = 4"]); b.set_ylim(0, 18.5); b.set_ylabel("real dimension")
b.legend(fontsize=8, loc="upper left")
b.set_title("B  dim Lie(G) = dim G", fontsize=9.8)

# C: exp(t tau_3) in SU(2) has period 4 pi, its image in SO(3) has period 2 pi -------------------------------------------------------------------------
c = axes[2]
t = np.linspace(0, 4 * np.pi, 600)
c.plot(t, np.cos(t / 2), color=ORANGE, lw=2.4, label="SU(2):  Re U(t)₁₁ = cos(t/2)")
c.plot(t, np.cos(t), color=BLUE, lw=2.0, label="SO(3):  R(t)₁₁ = cos t")
c.axhline(0, color=GRID, lw=1)
for x in (0, 2 * np.pi, 4 * np.pi):
    c.axvline(x, color=GRID, lw=0.8, ls=":")
c.scatter([2 * np.pi], [np.cos(np.pi)], color=RED, s=44, zorder=5)
c.text(2 * np.pi + 0.25, -1.17, "t = 2π: R = I,\nbut U = −I", color=RED, fontsize=8.4, va="center")
c.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi]); c.set_xticklabels(["0", "π", "2π", "3π", "4π"])
c.set_ylim(-1.55, 1.5); c.set_xlabel("t")
c.legend(fontsize=7.8, loc="upper right")
c.set_title("C  su(2) ≅ so(3), but SU(2) → SO(3) is 2 : 1", fontsize=9.6)

fig.tight_layout()
fig.text(0.5, -0.03, "A: d(L_g)_e e_b = (a₁, 0), d(L_g)_e e_a = (0, a₁) at g = (b₁, a₁); bracket checked symbolically. B: dimensions as kernels of the differentials, computed by rank (§3). "
         "C: τ₃ = −iσ₃/2 and dR(τ_k) = E_k (error 1.7×10⁻¹³). Numbers: dm_numbers.py (DM11).", ha="center", fontsize=7.8, color=MUTED)
save(fig, "fig_dm11_liealgebra")
