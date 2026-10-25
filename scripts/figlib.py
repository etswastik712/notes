"""Shared matplotlib style for the vault.  Every fig_*.py does `from figlib import *`.

Palette = first slots of the dataviz reference palette (fixed order, never cycled):
  BLUE, ORANGE, AQUA, plus INK/MUTED/GRID neutrals.  Figures are drawn on a light surface and saved as
  PNG (dpi 200) so they read the same in Obsidian light and dark themes (the CSS snippet puts a white
  backing behind raster images).
"""
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "Assets", "figures")
os.makedirs(OUT, exist_ok=True)

SURFACE = "#fcfcfb"
INK = "#0b0b0b"
MUTED = "#52514e"
GRID = "#e4e3df"
BLUE = "#2a78d6"
ORANGE = "#eb6834"
AQUA = "#1baf7a"
RED = "#e34948"
VIOLET = "#6250d6"

plt.rcParams.update({
    "figure.facecolor": SURFACE,
    "axes.facecolor": SURFACE,
    "savefig.facecolor": SURFACE,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": INK,
    "axes.titlecolor": INK,
    "axes.titlesize": 11,
    "axes.titleweight": "semibold",
    "axes.labelsize": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.6,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "text.color": INK,
    "font.size": 9.5,
    "font.family": "DejaVu Sans",
    "lines.linewidth": 2.0,
    "legend.frameon": False,
    "mathtext.fontset": "cm",
})

# physical constants (CODATA / SI)
SIGMA = 5.670374e-8      # W m-2 K-4
H_PL = 6.62607015e-34    # J s
C_LT = 2.99792458e8      # m s-1
K_B = 1.380649e-23       # J K-1
OMEGA = 7.2921159e-5     # rad s-1 (sidereal)
R_EARTH = 6.371e6        # m
G0 = 9.80665             # m s-2
S0 = 1361.0              # W m-2 total solar irradiance (Kopp & Lean 2011; TSIS-1)


def save(fig, name):
    """Save <name>.png into Assets/figures and print the path."""
    path = os.path.join(OUT, name + ".png")
    fig.savefig(path, dpi=200, bbox_inches="tight")
    plt.close(fig)
    print(os.path.normpath(path))


def label_line(ax, x, y, text, color, dx=0, dy=0, ha="left", va="center", **kw):
    """Direct label next to a line (text in ink, a coloured dot marks identity)."""
    ax.plot([x], [y], "o", color=color, ms=5, zorder=5)
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va,
                color=INK, fontsize=9, **kw)
