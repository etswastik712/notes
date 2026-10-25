"""EE04 - conceptual diagram (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_ee04.py"""
from diagrams import excalidraw, svg

SPECS = {
    "EE04 Exclusion or Coexistence": dict(
        size=(920, 520),
        nodes={
            "t": dict(x=460, y=85, w=420, h=70, text="Two species depend on the same limiting resource", color="grey"),
            "l": dict(x=155, y=225, w=270, h=100, text="Same niche, one resource:\nthe lower R* wins\n(Gause; Tilman)", color="orange"),
            "m": dict(x=460, y=225, w=270, h=100, text="Lotka-Volterra: coexist only if\neach limits itself more than\nthe other (a12 a21 < 1)", color="blue"),
            "r": dict(x=765, y=225, w=270, h=100, text="Invader with no enemies:\na super-competitor drives\nnatives out", color="orange"),
            "p": dict(x=250, y=385, w=330, h=100, text="Niche partitioning lowers a:\nspace, time, body size\n(barnacles, spiny mice, finches)", color="aqua"),
            "c": dict(x=670, y=385, w=330, h=100, text="Conditional outcomes:\ntemperature and humidity flip\nthe winner (Park's Tribolium)", color="aqua"),
        },
        arrows=[("t", "l", ""), ("t", "m", ""), ("t", "r", ""), ("l", "p", ""), ("m", "p", ""), ("m", "c", "")],
        title="When do competitors exclude each other, and when do they coexist?",
        footer="Slides 7-30: exclusion in 3 of 4 L-V regions, yet in nature similar species often coexist: partitioning and conditions explain how",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
