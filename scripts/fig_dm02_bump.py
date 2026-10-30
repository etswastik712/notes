"""DM02 - the flat function e^{-1/t}, bump functions, and partitions of unity on R and on S^1."""
from figlib import *
from dm_numbers import f_bump, h_step

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.2), gridspec_kw=dict(width_ratios=[1.05, 1.05, 0.9]))

# A: f, step, bump ---------------------------------------------------------------------------------------------------------
a = axes[0]
t = np.linspace(-0.3, 1.3, 800)
a.plot(t, f_bump(t), color=ORANGE, lw=1.8, label="f(t) = e^{-1/t}  (t > 0)")
a.plot(t, h_step(t), color=BLUE, lw=2.2, label="step h = f(t)/(f(t)+f(1−t))")
x = np.linspace(-2.6, 2.6, 1000)
a.set_ylim(-0.2, 1.15); a.legend(fontsize=8, loc="upper left")
a.text(-0.28, 0.5, "f is flat at 0:\nf(t)/t²⁰ = 3.7×10⁻⁴ at t = 0.01", fontsize=8.2, color=ORANGE)
a.axhline(0, color=MUTED, lw=0.6)
ins = a.inset_axes([0.45, 0.07, 0.52, 0.34])
ins.plot(x, h_step(2 - np.abs(x)), color=AQUA, lw=2)
ins.set_title("bump b(x) = h(2 − |x|)", fontsize=8); ins.set_xticks([-2, -1, 0, 1, 2]); ins.tick_params(labelsize=7)
a.set_title("A  a smooth step and a bump", fontsize=10)

# B: partition of unity on R -------------------------------------------------------------------------------------------------
b = axes[1]
x = np.linspace(-0.6, 1.6, 900)
p2 = h_step(3 * x - 1)
b.plot(x, 1 - p2, color=BLUE, lw=2.2, label="ψ₁ = 1 − ψ₂   (supp ⊂ U₁ = (−∞, 1))")
b.plot(x, p2, color=ORANGE, lw=2.2, label="ψ₂ = h(3x − 1)   (supp = [1/3, ∞) ⊂ U₂ = (0, ∞))")
b.plot(x, np.ones_like(x), color=INK, lw=0.8, ls=":")
b.fill_between([-0.6, 1.0], -0.2, -0.12, color=BLUE, alpha=0.25); b.text(-0.55, -0.19, "U₁", fontsize=8.5, color=BLUE)
b.fill_between([0.0, 1.6], -0.1, -0.02, color=ORANGE, alpha=0.25); b.text(1.5, -0.09, "U₂", fontsize=8.5, color=ORANGE)
b.scatter([0.4, 0.5, 0.6], [1 - h_step(0.2), 0.5, 1 - h_step(0.8)], color=INK, zorder=5, s=18)
b.text(0.62, 0.65, "ψ₂(0.4) = 0.023\nψ₂(0.5) = 0.5\nψ₂(0.6) = 0.977", fontsize=8.2, color=INK)
b.set_ylim(-0.25, 1.15); b.legend(fontsize=7.4, loc="upper left", bbox_to_anchor=(0.0, 0.99))
b.set_title("B  a partition of unity subordinate to {U₁, U₂}", fontsize=10)

# C: partition of unity on S^1 ------------------------------------------------------------------------------------------------
c = axes[2]
th = np.linspace(0, 2 * np.pi, 800)
xx, yy = np.cos(th), np.sin(th)
p1 = h_step(0.5 - yy)
sc = c.scatter(xx, yy, c=p1, cmap="viridis", s=12)
c.scatter([0], [1], color=RED, s=40, zorder=5); c.scatter([0], [-1], color=BLUE, s=40, zorder=5)
c.text(0.06, 1.1, "N: ψ₁ = 0, V₁ = S¹∖N", fontsize=8.4, color=RED)
c.text(0.06, -1.22, "S: ψ₁ = 1", fontsize=8.4, color=BLUE)
c.text(-1.3, 0.0, "ψ₁ = h(0.5 − y):\n0 where y ≥ 0.5\n1 where y ≤ −0.5", fontsize=8.2, color=INK)
fig.colorbar(sc, ax=c, fraction=0.04, pad=0.02, label="ψ₁")
c.set_aspect("equal"); c.set_xlim(-1.5, 1.5); c.set_ylim(-1.4, 1.35); c.axis("off")
c.set_title("C  on the circle (charts V₁, V₂)", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: f, h and b built from e^{-1/t}. B: ψ₁ + ψ₂ = 1, each supported in one set of the cover. C: ψ₁ on S¹ subordinate to the two stereographic domains. Numbers: dm_numbers.py (DM02).",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm02_bump")
