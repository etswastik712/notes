"""DM07 - critical values of a cubic, secant directions of a space curve, and transversality of a parabola to an axis."""
from figlib import *
from dm_numbers import trefoil

fig, axes = plt.subplots(1, 3, figsize=(13.4, 4.3))

# A: Sard in dimension 1 -----------------------------------------------------------------------------------------------------------------------
a = axes[0]
x = np.linspace(-2.2, 2.2, 400)
f = x ** 3 - 3 * x
a.plot(x, f, color=BLUE, lw=2.2)
for xc in (-1, 1):
    a.scatter([xc], [xc ** 3 - 3 * xc], color=RED, s=44, zorder=5)
    a.axhline(xc ** 3 - 3 * xc, color=RED, lw=0.8, ls=":")
a.text(-2.1, 2.2, "critical values ±2 (red): the only\nlevels where the level set is not\na manifold. A finite set: measure zero.", fontsize=8.4, color=RED)
for c in (-1.0, 0.5, 1.2):
    a.axhline(c, color=GRID, lw=1)
a.text(-2.1, -5.0, "every other level c has 1 or 3 points,\nwith f′ ≠ 0 there (Monte Carlo: all 5000\nrandom c were regular values)", fontsize=8.2, color=INK)
a.set_xlim(-2.3, 2.3); a.set_ylim(-5.6, 5.6)
a.set_title("A  Sard: f = x³ − 3x", fontsize=10)

# B: secant directions of the trefoil on the sphere ----------------------------------------------------------------------------------------------------
b = axes[1]
T = np.linspace(0, 2 * np.pi, 700, endpoint=False)
P = trefoil(T)
i, j = np.triu_indices(len(T), 1)
keep = (np.abs(i - j) > 3) & (np.abs(i - j) < len(T) - 3)
d = P[j[keep]] - P[i[keep]]
d /= np.linalg.norm(d, axis=1)[:, None]
sel = np.random.default_rng(0).choice(len(d), 60000, replace=False)
d = d[sel]
b.scatter(np.degrees(np.arctan2(d[:, 1], d[:, 0])), d[:, 2], s=0.6, color=BLUE, alpha=0.5)
b.text(-175, -0.55, "secant directions of a trefoil knot fill S² (100% of 648 equal-area bins):\nno direction gives an injective projection to a plane,\nconsistent with Whitney: n = 1 needs 2n + 1 = 3 dimensions", fontsize=8.0, color=INK, bbox=dict(boxstyle="round", fc="white", ec=GRID))
b.set_xlabel("longitude (degrees)"); b.set_ylabel("sin(latitude)"); b.set_xlim(-180, 180); b.set_ylim(-1, 1)
b.set_title("B  Whitney: counting directions", fontsize=10)

# C: transversality ----------------------------------------------------------------------------------------------------------------------------------------
c = axes[2]
x = np.linspace(-1.4, 1.4, 300)
for cc, col, lab in ((0.25, BLUE, "c = 0.25: crosses at ±45°: transverse"), (0.0, RED, "c = 0: tangent at 0: not transverse"), (-0.25, AQUA, "c = −0.25: no intersection")):
    c.plot(x, x ** 2 - cc, color=col, lw=2, label=lab)
c.axhline(0, color=INK, lw=1.4)
c.scatter([-0.5, 0.5, 0], [0, 0, 0], color=INK, s=24, zorder=5)
c.set_ylim(-0.6, 1.2); c.legend(fontsize=8, loc="upper center")
c.text(-1.35, -0.5, "f_c(x) = x² − c transverse to the x-axis ⇔ c ≠ 0;\nsmall perturbations of c = 0 make it transverse (genericity)", fontsize=8.2, color=INK)
c.set_title("C  transversality to the x-axis", fontsize=10)

fig.tight_layout()
fig.text(0.5, -0.03, "A: critical values are rare. B: why 2n+1 dimensions are needed (secant directions of a space curve fill S²). C: transversality is the generic situation. Numbers: dm_numbers.py (DM07).",
         ha="center", fontsize=8, color=MUTED)
save(fig, "fig_dm07_sard")
