"""Concept maps (SVG + Excalidraw) for chapters that had only a one-sentence story.   .venv/bin/python scripts/diagrams_maps.py [name-substring]
Each chapter gets one 'Map' diagram: the dependency of ideas, drawn with scripts/diagrams.py."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "QM07 Finite Well Map": dict(
        size=(1000, 600),
        nodes={
            "w": dict(x=170, y=100, w=280, h=100, text="The well\nV = 0 for |x| < a, V0 outside\nenergy from the floor, 0 < E < V0", color="blue"),
            "m": dict(x=500, y=100, w=280, h=100, text="Match psi and psi' at x = a\nparity: even cos, odd sin\noutside: exp(-kappa|x|)", color="orange"),
            "q": dict(x=830, y=100, w=290, h=100, text="Quantisation\nkappa/k0 = tan(k0 a)  (even)\nkappa/k0 = -cot(k0 a)  (odd)", color="aqua"),
            "g": dict(x=170, y=290, w=280, h=110, text="Graph (Tutorial IV)\nkappa/k0 = sqrt(z0^2/z^2 - 1)\nintersect tan / -cot branches\nN = ceil(2 z0/pi)", color="aqua"),
            "l": dict(x=500, y=290, w=290, h=110, text="Limits\ndeep: box, E (1 - 2/z0)\nshallow: always one state\ndelta: kappa = m alpha/hbar^2", color="grey"),
            "p": dict(x=830, y=290, w=290, h=110, text="Penetration\nd = 1/kappa, P_out > 0\nwider effective box,\nlevels below the box levels", color="blue"),
            "s": dict(x=330, y=480, w=330, h=110, text="E > V0: scattering\nA e^{ikx} + B e^{-ikx} ... F e^{ikx}\nT = 1/(1 + V0^2 sin^2(2 k0 a)/4E(E-V0))", color="orange"),
            "r": dict(x=700, y=480, w=330, h=110, text="Resonances\nT = 1 at 2 k0 a = n pi\n(box energies); T -> 0 at E = V0\nT + R = 1", color="red"),
        },
        arrows=[("w", "m", ""), ("m", "q", ""), ("q", "g", ""), ("g", "l", ""), ("q", "p", ""), ("w", "s", ""), ("s", "r", ""), ("p", "l", "")],
        title="QM07: the finite square well in one page",
        footer="Finite_well.pdf pp.2-13 (instructor), Tutorial IV; Griffiths 2.6, Sakurai 2.5 for the extras",
    ),
    "QM08 Tunnelling Map": dict(
        size=(1000, 600),
        nodes={
            "st": dict(x=170, y=100, w=280, h=100, text="Step potential\nE > V0: R = ((k1-k2)/(k1+k2))^2\nE < V0: total reflection,\nevanescent tail", color="blue"),
            "ba": dict(x=500, y=100, w=290, h=100, text="Rectangular barrier\nE < V0: T = 1/(1 + V0^2 sinh^2(kappa L)/4E(V0-E))\ntunnelling", color="orange"),
            "tl": dict(x=830, y=100, w=290, h=100, text="Thick barrier\nT ~ 16 (E/V0)(1-E/V0) e^(-2 kappa L)\nexponentially small", color="red"),
            "cu": dict(x=170, y=290, w=280, h=110, text="Probability current\nj = (hbar/m) Im(psi* psi')\nR + T = 1 from conservation", color="aqua"),
            "wk": dict(x=500, y=290, w=290, h=110, text="WKB / Gamow\nT ~ exp(-2 int kappa(x) dx)\nsmooth barriers", color="aqua"),
            "ap": dict(x=830, y=290, w=290, h=110, text="Applications\nalpha decay, STM,\ntunnel diode, fusion in stars", color="grey"),
            "de": dict(x=330, y=480, w=300, h=100, text="Delta barrier / well\nT = 1/(1 + m alpha^2/(2 hbar^2 E))\nbound state kappa = m alpha/hbar^2", color="blue"),
            "tm": dict(x=700, y=480, w=320, h=100, text="Transfer matrix and bands\nperiodic wells: Kronig-Penney\ncos(qL) = cos(kL) + (m alpha/hbar^2 k) sin(kL)", color="orange"),
        },
        arrows=[("st", "ba", ""), ("ba", "tl", ""), ("st", "cu", ""), ("ba", "wk", ""), ("tl", "ap", ""), ("wk", "ap", ""), ("cu", "de", ""), ("de", "tm", "")],
        title="QM08: scattering and tunnelling in one page",
        footer="QM07 solved the well; here the particle comes from outside: step, barrier, delta, WKB, bands",
    ),
    "Dirac Algebra Map": dict(
        size=(1000, 600),
        nodes={
            "k": dict(x=170, y=100, w=270, h=100, text="Kets |alpha>\nabstract state space\nsuperposition, null ket", color="blue"),
            "b": dict(x=500, y=100, w=290, h=100, text="Bras <alpha|, inner product\n<a|b> = <b|a>*\nSchwarz inequality", color="orange"),
            "o": dict(x=830, y=100, w=290, h=100, text="Operators\nX|alpha>, |b><a| outer product\ncommutator [A,B]", color="aqua"),
            "h": dict(x=170, y=290, w=280, h=110, text="Adjoint, Hermitian\nreal eigenvalues\northogonal eigenkets", color="aqua"),
            "c": dict(x=500, y=290, w=290, h=110, text="Completeness\nsum |a><a| = 1\nmatrix elements, change of basis", color="grey"),
            "r": dict(x=830, y=290, w=290, h=110, text="x and p representations\npsi(x) = <x|alpha>\np = -i hbar d/dx, plane waves", color="blue"),
            "u": dict(x=330, y=480, w=300, h=110, text="Unitary operators\ntranslation T = e^(-i p l/hbar)\n[x,p] = i hbar", color="orange"),
            "m": dict(x=700, y=480, w=330, h=110, text="Measurement + dynamics\nP = |<a|alpha>|^2, Robertson DA DB >= |<[A,B]>|/2\nU = e^(-iHt/hbar), Heisenberg picture", color="red"),
        },
        arrows=[("k", "b", ""), ("b", "o", ""), ("b", "h", ""), ("o", "c", ""), ("h", "c", ""), ("c", "r", ""), ("c", "u", ""), ("u", "m", ""), ("r", "m", "")],
        title="Dirac algebra: from kets to measurement and time evolution",
        footer="Sakurai Ch.1 and 2.1: the same state in energy, position and momentum language",
    ),
}

if __name__ == "__main__":
    pat = sys.argv[1] if len(sys.argv) > 1 else ""
    for nm, sp in SPECS.items():
        if pat in nm:
            svg(nm, sp)
            excalidraw(nm, sp)
            print("built", nm)
