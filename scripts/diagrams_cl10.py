"""CL10 diagram: energy budget of one latitude belt (SVG + editable Excalidraw).   .venv/bin/python scripts/diagrams_cl10.py"""
from diagrams import excalidraw, svg

SPEC = dict(
    size=(760, 400),
    nodes={
        "sp":  dict(x=380, y=60,  w=380, h=70, text="Space\nabsorbed sunlight in  ·  OLR out", color="orange"),
        "col": dict(x=380, y=235, w=260, h=120, text="Atmosphere–ocean column\nenergy content E\ndE/dt = R_TOA − ΔF", color="aqua"),
        "in":  dict(x=100, y=235, w=170, h=84, text="Flux in\nF(φ−)\nfrom the equator side", color="blue"),
        "out": dict(x=660, y=235, w=170, h=84, text="Flux out\nF(φ+)\ntowards the pole", color="blue"),
    },
    arrows=[("sp", "col", "R_TOA"), ("in", "col", "+"), ("col", "out", "−")],
    title="Energy budget of one latitude belt",
    footer="Annual mean: dE/dt ≈ 0, so R_TOA = ΔF = F(φ+) − F(φ−): the belt exports its net radiative surplus poleward",
)

if __name__ == "__main__":
    svg("Column Energy Budget", SPEC)
    excalidraw("Column Energy Budget", SPEC)
