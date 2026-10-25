"""EE07 - conceptual diagram (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_ee07.py"""
from diagrams import excalidraw, svg

SPECS = {
    "EE07 From Why to What To Do": dict(
        size=(920, 560),
        nodes={
            "w": dict(x=460, y=85, w=360, h=70, text="WHY conserve?\nthree ethics: preserve, use wisely, land community", color="grey"),
            "r": dict(x=200, y=215, w=300, h=90, text="WHO is at risk?\nrarity: range x tolerance x\nlocal population size", color="blue"),
            "s": dict(x=720, y=215, w=300, h=90, text="HOW FAST?\nsmall populations: demographic,\ngenetic, environmental chance", color="orange"),
            "c": dict(x=200, y=355, w=300, h=90, text="CASE 1: passenger pigeon\nsix causes; Allee effect\nin a flock species", color="aqua"),
            "m": dict(x=720, y=355, w=300, h=90, text="HOW MANY? survey with\ncapture-recapture, N = C/p,\ncamera traps", color="aqua"),
            "a": dict(x=460, y=490, w=480, h=80, text="WHAT to do: reserves (core, buffer, corridors), policy,\nlaw: Project Tiger (science + common sense + economics + politics)", color="grey"),
        },
        arrows=[("w", "r", ""), ("w", "s", ""), ("r", "c", ""), ("s", "m", ""), ("c", "a", ""), ("m", "a", "")],
        title="Conservation biology in one chain: why, who, how fast, how many, what to do",
        footer="Slides 1-31: ethics -> rarity -> stochasticity and MVP -> pigeon and tiger case studies -> reserves and policy",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
