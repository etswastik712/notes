"""TH - conceptual diagrams (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_th.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "TH05 The Potentials by Legendre Transform": dict(
        size=(940, 500),
        nodes={
            "E": dict(x=170, y=130, w=270, h=96, text="Energy E(S, x, N)\ndE = T dS + J dx + mu dN\nisolated: S is maximal", color="blue"),
            "H": dict(x=470, y=130, w=270, h=96, text="Enthalpy H = E - J x\nH(S, J, N): dH = T dS - x dJ\nconst S, J: H is minimal", color="orange"),
            "F": dict(x=170, y=330, w=270, h=96, text="Helmholtz F = E - T S\nF(T, x, N): dF = -S dT + J dx\nconst T, no work: F is minimal", color="aqua"),
            "G": dict(x=470, y=330, w=270, h=96, text="Gibbs G = E - T S - J x\nG(T, J, N): dG = -S dT - x dJ\nconst T, J: G is minimal", color="aqua"),
            "O": dict(x=790, y=330, w=240, h=110, text="Grand potential\nG-tilde = E - T S - mu N\nd = -S dT - J dx - N dmu\nconst T, mu: minimal", color="grey"),
            "M": dict(x=790, y=130, w=240, h=96, text="Maxwell relations\nmixed second derivatives\nof any potential agree", color="red"),
        },
        arrows=[("E", "H", "-Jx"), ("E", "F", "-TS"), ("H", "G", "-TS"), ("F", "G", "-Jx"), ("F", "O", "-mu N"), ("G", "M", ""), ("O", "M", "")],
        title="Each constraint has its own potential: swap a variable for its conjugate",
        footer="Kardar I.G-I.H (MIT 8.333 Lectures 3): potentials are Legendre transforms; the inequalities of Table 2 pick the equilibrium state",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
