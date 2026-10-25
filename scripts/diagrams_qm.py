"""QM - conceptual diagrams (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_qm.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "QM03 From State to Measurement": dict(
        size=(940, 520),
        nodes={
            "s": dict(x=170, y=110, w=270, h=96, text="State\npsi(x), or |psi>\nnormalised: sum |c|^2 = 1", color="blue"),
            "o": dict(x=170, y=300, w=270, h=96, text="Observable A\nrepresented by an\nHermitian operator A-hat", color="orange"),
            "e": dict(x=490, y=205, w=290, h=110, text="Eigenproblem\nA-hat phi_a = a phi_a\neigenvalues a: possible results\neigenstates phi_a: a basis", color="aqua"),
            "c": dict(x=800, y=110, w=240, h=96, text="Expansion\npsi = sum c_a phi_a\nc_a = <phi_a|psi>", color="blue"),
            "p": dict(x=800, y=300, w=240, h=110, text="Outcomes\nP(a) = |c_a|^2\n<A> = sum |c_a|^2 a\n(DA)^2 = <A^2> - <A>^2", color="grey"),
            "k": dict(x=490, y=430, w=520, h=84, text="[A,B] = 0: shared eigenstates, both sharp\n[A,B] != 0: DA DB >= |<[A,B]>|/2   (x,p: hbar/2)", color="red"),
        },
        arrows=[("s", "c", ""), ("o", "e", ""), ("e", "c", ""), ("c", "p", ""), ("o", "k", "")],
        title="Quantum mechanics in one pass: state, operator, eigenbasis, probabilities",
        footer="PH2113 States, Operators, Measurements: Sections 2-8 and 11; the commutator decides which observables can be sharp together",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
