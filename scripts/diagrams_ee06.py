"""EE06 - causal-loop diagram of the shallow-lake feedback (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_ee06.py"""
from diagrams import excalidraw, svg

SPECS = {
    "EE06 Shallow Lake Feedback Loop": dict(
        size=(900, 520),
        nodes={
            "t": dict(x=450, y=95, w=290, h=84, text="Turbidity T\n(algae, suspended matter)", color="orange"),
            "l": dict(x=745, y=255, w=270, h=84, text="Light at the lake bed L", color="grey"),
            "v": dict(x=450, y=410, w=290, h=84, text="Submerged vegetation V", color="aqua"),
            "r": dict(x=155, y=255, w=270, h=84, text="Sediment resuspension R\n(waves, fish stirring)", color="grey"),
            "c": dict(x=450, y=255, w=190, h=84, text="Loop sign\n(-)(+)(-)(+) = +\nreinforcing", color="blue"),
        },
        arrows=[("t", "l", "-"), ("l", "v", "+"), ("v", "r", "-"), ("r", "t", "+")],
        title="Why a shallow lake keeps its state: vegetation and turbidity harm each other",
        footer="More turbidity gives less light (-); more light gives more vegetation (+); vegetation reduces resuspension (-); resuspension raises turbidity (+)",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
