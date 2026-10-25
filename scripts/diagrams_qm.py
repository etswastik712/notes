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
    "QM06 The Oscillator Toolbox": dict(
        size=(1000, 600),
        nodes={
            "h": dict(x=170, y=100, w=270, h=96, text="Hamiltonian\nH = hbar w (a+ a- + 1/2)\n(factorised sum of squares)", color="blue"),
            "l": dict(x=500, y=100, w=290, h=110, text="Ladder algebra\n[a-, a+] = 1\na- |n> = sqrt(n) |n-1>\na+ |n> = sqrt(n+1) |n+1>", color="orange"),
            "f": dict(x=830, y=100, w=290, h=110, text="Number basis |n>\nE_n = (n + 1/2) hbar w\npsi_n = (a+)^n psi_0 / sqrt(n!)", color="aqua"),
            "x": dict(x=170, y=290, w=290, h=118, text="x, p = a+ +- a-\ntridiagonal matrices\n<x^2> = (2n+1) hbar/2mw\nselection rule dn = +-1", color="blue"),
            "q": dict(x=500, y=290, w=290, h=118, text="Hermite functions\npsi_n ~ H_n(xi) e^(-xi^2/2)\nRodrigues, recurrence, generating fn\nnorm sqrt(pi) 2^n n!", color="aqua"),
            "m": dict(x=830, y=290, w=290, h=96, text="Momentum space\npsi~_n(p) = (-i)^n psi_n(p)\nx and p play the same role", color="grey"),
            "c": dict(x=170, y=490, w=290, h=110, text="Coherent states\na |alpha> = alpha |alpha>\nPoisson in n, Dx Dp = hbar/2\nmoves on the classical orbit", color="orange"),
            "t": dict(x=500, y=490, w=290, h=110, text="Thermal oscillator\nP(n) geometric, <n> = 1/(e^x - 1)\nPlanck mean energy\nEinstein heat capacity", color="red"),
            "e": dict(x=830, y=490, w=290, h=110, text="Dynamics\nEhrenfest: <x>, <p> classical\nHeisenberg: a(t) = a e^(-iwt)\nvirial: <T> = <V> = E/2", color="grey"),
        },
        arrows=[("h", "l", ""), ("l", "f", ""), ("l", "x", ""), ("f", "q", ""), ("q", "m", ""), ("x", "e", ""), ("l", "c", ""), ("f", "t", "")],
        title="The oscillator toolbox: one algebra, many representations",
        footer="QM05-QM06: every result follows from [a-, a+] = 1 and the ground-state condition a- psi_0 = 0",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
