"""PA - conceptual diagrams (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_pa.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from diagrams import excalidraw, svg

SPECS = {
    "PA01 Proof Strategies by Logical Form": dict(
        size=(960, 520),
        nodes={
            "G": dict(x=150, y=90, w=250, h=70, text="Goal has the form...", color="grey"),
            "I": dict(x=480, y=60, w=250, h=70, text="P => Q\nassume P, derive Q\n(or contrapositive, or contradiction)", color="blue"),
            "A": dict(x=480, y=150, w=250, h=60, text="for all x in A, P(x)\ntake arbitrary x, prove P(x)", color="blue"),
            "E": dict(x=480, y=240, w=250, h=60, text="there exists x, P(x)\nexhibit a witness (or non-constructive)", color="aqua"),
            "C": dict(x=480, y=330, w=250, h=60, text="P and Q\nprove each part", color="aqua"),
            "O": dict(x=480, y=420, w=250, h=60, text="P or Q\nassume not P, prove Q (or cases)", color="orange"),
            "N": dict(x=800, y=240, w=230, h=80, text="Disproving a for-all:\nONE counterexample\n(negation: there exists x, not P(x))", color="orange"),
        },
        arrows=[("G", "I", "conditional"), ("G", "A", "universal"), ("G", "E", "existential"), ("G", "C", "conjunction"), ("G", "O", "disjunction"), ("A", "N", "to refute"), ("E", "N", "negation is for-all")],
        title="Choosing a proof strategy from the logical form of the goal",
        footer="Assignments 1-2 and the tautology note; AI notes ch. 3 (methods of proof) used for the table of strategies",
    ),
    "PA05 The Number System Tower": dict(
        size=(980, 420),
        nodes={
            "N": dict(x=130, y=200, w=170, h=100, text="N\nvon Neumann sets\n0 = {}, n+1 = n u {n}", color="blue"),
            "Z": dict(x=370, y=200, w=170, h=100, text="Z\nclasses of pairs (a, b)\n(a,b) ~ (c,d) iff a+d = c+b", color="blue"),
            "Q": dict(x=610, y=200, w=170, h=100, text="Q\nclasses of pairs (a, b), b != 0\nad = bc", color="aqua"),
            "R": dict(x=850, y=200, w=170, h=100, text="R\nDedekind cuts of Q\nleast upper bound property", color="orange"),
        },
        arrows=[("N", "Z", "add negatives"), ("Z", "Q", "add quotients"), ("Q", "R", "fill the gaps")],
        title="Each system is built from the previous one by equivalence classes or cuts",
        footer="AI notes ch. 12-15 (extra, book level); Assignment 8 uses only the induction property of N",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
