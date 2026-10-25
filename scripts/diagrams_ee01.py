"""EE01 - conceptual diagrams (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_ee01.py"""
from diagrams import excalidraw, svg

SPECS = {
    "EE01 How and Why of the Migration": dict(
        size=(860, 540),
        nodes={
            "h1":  dict(x=145, y=95,  w=270, h=104, text="HOW (mechanism)\nmuscles 62.6 % efficient;\nmovement tracks green-grass intake\nand plant nitrogen (Holdo 2009)", color="blue"),
            "h2":  dict(x=145, y=250, w=270, h=104, text="HOW (reproduction)\ncalves stand in ~6 min;\nrut and calving are synchronous", color="blue"),
            "obs": dict(x=430, y=250, w=190, h=104, text="OBSERVED\n~1.2 million animals\nwalk ~1,500 km a year", color="orange"),
            "w1":  dict(x=715, y=95,  w=270, h=104, text="WHY (benefit)\nrainfall and soil fertility\nrun in opposite directions:\n>3,500 km² of rich grass", color="aqua"),
            "w2":  dict(x=715, y=250, w=270, h=104, text="WHY (benefit)\nsynchronous calving swamps\npredators; migration escapes\nlocal food limits", color="aqua"),
            "eff": dict(x=430, y=415, w=470, h=84, text="CONSEQUENCES FOR THE ECOSYSTEM\nmass drownings feed the Mara River (death);\ngrazing changes fuel and fire", color="grey"),
        },
        arrows=[("h1", "obs", ""), ("h2", "obs", ""), ("w1", "obs", ""), ("w2", "obs", ""), ("obs", "eff", "")],
        title="Two kinds of question about one behaviour: proximate (how) and ultimate (why)",
        footer="Mayr's distinction: proximate = how the machinery works now; ultimate = why selection built it that way",
    ),
    "EE01 Why Biology Resists Laws": dict(
        size=(860, 560),
        nodes={
            "d": dict(x=110, y=70, w=190, h=70, text="Diversity and\ninterconnectedness", color="blue"),
            "s": dict(x=315, y=70, w=190, h=70, text="Stochasticity\n'chancy world'", color="blue"),
            "h": dict(x=520, y=70, w=190, h=70, text="Historicity", color="blue"),
            "e": dict(x=725, y=70, w=190, h=70, text="Emergence:\nreductionism fails", color="blue"),
            "m": dict(x=420, y=205, w=540, h=76, text="Result: mathematical formulation is hard; links to reality\nare statistical and conditional, not exact laws", color="orange"),
            "a1": dict(x=225, y=345, w=330, h=76, text="1. Describe what is there\n(natural history, classification)", color="grey"),
            "a2": dict(x=615, y=345, w=330, h=76, text="2. Build simplified models\n(with caveats; limited prediction)", color="grey"),
            "b": dict(x=420, y=470, w=640, h=84, text="Approach of BI2113: oversimplified mathematical models,\nconcepts, historical narrative, examining the pedagogy.\nBreadth over depth.", color="aqua"),
        },
        arrows=[("d", "m", ""), ("s", "m", ""), ("h", "m", ""), ("e", "m", ""), ("m", "a1", ""), ("m", "a2", ""), ("a1", "b", ""), ("a2", "b", "")],
        title="Why biology feels different from physics, and what the course does about it",
        footer="Slides 15-17: features to be observed -> result -> two approaches -> the approach of BI2113",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
