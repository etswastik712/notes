"""CL07 - vibration modes of CO2 (linear) and H2O (bent) and whether they change the dipole moment (IR-active)."""
from matplotlib.patches import Circle, FancyArrowPatch

from figlib import *

OXY, CAR, HYD = "#e34948", "#52514e", "#c9c8c3"
fig, axs = plt.subplots(2, 3, figsize=(9.6, 5.6))


def atom(ax, xy, kind, r=None):
    col = {"O": OXY, "C": CAR, "H": HYD}[kind]
    r = r or {"O": 0.34, "C": 0.28, "H": 0.2}[kind]
    ax.add_patch(Circle(xy, r, fc=col, ec=INK, lw=1.2, zorder=3))
    ax.text(xy[0], xy[1], kind, ha="center", va="center", fontsize=9, color="white" if kind != "H" else INK, zorder=4, fontweight="bold")


def arrow(ax, xy, d, color=BLUE, lw=2.4):
    ax.add_patch(FancyArrowPatch(xy, (xy[0] + d[0], xy[1] + d[1]), arrowstyle="-|>", mutation_scale=14, color=color, lw=lw, zorder=5))


def finish(ax, title, sub, active):
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-1.7, 1.7)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(title, fontsize=9.5, fontweight="semibold")
    ax.text(0, -1.45, sub, ha="center", va="center", fontsize=8.6, color=(AQUA if active else RED))


# --- CO2 (linear): O=C=O
base = [(-1.3, 0.0), (0.0, 0.0), (1.3, 0.0)]
for ax in (axs[0, 0], axs[0, 2]):
    ax.plot([-1.3, 1.3], [0, 0], color=MUTED, lw=2, zorder=1)
ax = axs[0, 0]
atom(ax, base[0], "O"); atom(ax, base[1], "C"); atom(ax, base[2], "O")
arrow(ax, (-1.6, 0.0), (-0.55, 0)); arrow(ax, (1.6, 0.0), (0.55, 0))
finish(ax, "CO₂  symmetric stretch  ν₁\n(≈ 7.2 µm)", "dipole stays 0:  IR-inactive", False)
ax = axs[0, 1]
atom(ax, (-1.3, 0.25), "O"); atom(ax, (0.0, -0.4), "C"); atom(ax, (1.3, 0.25), "O")
ax.plot([-1.3, 0, 1.3], [0.25, -0.4, 0.25], color=MUTED, lw=2, zorder=1)
arrow(ax, (-1.3, 0.62), (0, 0.55)); arrow(ax, (1.3, 0.62), (0, 0.55)); arrow(ax, (0.0, -0.78), (0, -0.55))
finish(ax, "CO₂  bend  ν₂  (two-fold degenerate)\n(15.0 µm)", "dipole oscillates perpendicular to the axis:  IR-active", True)
ax = axs[0, 2]
atom(ax, (-1.3, 0), "O"); atom(ax, (0.0, 0), "C"); atom(ax, (1.3, 0), "O")
arrow(ax, (-1.3, 0.55), (0.6, 0)); arrow(ax, (1.3, 0.55), (0.6, 0)); arrow(ax, (0.0, -0.5), (-0.7, 0))
finish(ax, "CO₂  asymmetric stretch  ν₃\n(4.26 µm)", "dipole oscillates along the axis:  IR-active", True)

# --- H2O (bent): H-O-H, 104.5 deg
hx, hy = 0.95, -0.75
for ax in axs[1]:
    ax.plot([-hx, 0, hx], [hy, 0.35, hy], color=MUTED, lw=2, zorder=1)
ax = axs[1, 0]
atom(ax, (0, 0.35), "O"); atom(ax, (-hx, hy), "H"); atom(ax, (hx, hy), "H")
arrow(ax, (-hx - 0.1, hy - 0.1), (-0.35, -0.3)); arrow(ax, (hx + 0.1, hy - 0.1), (0.35, -0.3)); arrow(ax, (0, 0.75), (0, 0.4))
finish(ax, "H₂O  symmetric stretch  ν₁\n(2.73 µm)", "dipole oscillates along the axis:  IR-active", True)
ax = axs[1, 1]
atom(ax, (0, 0.35), "O"); atom(ax, (-hx, hy), "H"); atom(ax, (hx, hy), "H")
arrow(ax, (-hx, hy + 0.35), (0.45, 0.1)); arrow(ax, (hx, hy + 0.35), (-0.45, 0.1)); arrow(ax, (0, 0.75), (0, -0.0))
finish(ax, "H₂O  bend  ν₂\n(6.27 µm)", "dipole oscillates along the axis:  IR-active", True)
ax = axs[1, 2]
atom(ax, (0, 0.35), "O"); atom(ax, (-hx, hy), "H"); atom(ax, (hx, hy), "H")
arrow(ax, (-hx - 0.1, hy - 0.1), (-0.35, -0.3)); arrow(ax, (hx + 0.1, hy + 0.15), (-0.3, 0.2)); arrow(ax, (0, 0.75), (-0.3, 0.1))
finish(ax, "H₂O  asymmetric stretch  ν₃\n(2.66 µm)", "dipole oscillates across the axis:  IR-active", True)
fig.suptitle("A vibration absorbs infrared only if it makes the dipole moment oscillate", fontsize=11, fontweight="semibold", y=1.0)
fig.tight_layout()
save(fig, "fig_cl07_molecule_modes")
