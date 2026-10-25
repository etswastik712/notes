"""CL09 diagrams (SVG for embedding + editable Excalidraw twin).   .venv/bin/python scripts/diagrams_cl09.py"""
from diagrams import excalidraw, svg

SPECS = {
    "Tropical OLR Contrast": dict(
        size=(760, 470),
        nodes={
            "sp":  dict(x=380, y=60,  w=640, h=56, text="Space: what a satellite sees\nOLR = outgoing longwave radiation", color="grey"),
            "gl":  dict(x=170, y=330, w=250, h=70, text="Clear, dry region (desert)\nground T_s ≈ 300 K: σT_s⁴ = 459", color="orange"),
            "ct":  dict(x=590, y=190, w=270, h=70, text="Deep convective cloud top\nT_c ≈ 220 K: σT_c⁴ = 133 W/m²", color="blue"),
            "gr":  dict(x=590, y=360, w=270, h=70, text="Warm moist ground below\nT_s ≈ 300 K (hidden)", color="orange"),
        },
        arrows=[("gl", "sp", "459 W/m²"), ("ct", "sp", "133"), ("gr", "ct", "")],
        title="OLR contrast: the colder the emitter, the dimmer the planet",
        footer="(300/220)⁴ ≈ 3.5: deep convection = LOW OLR, clear dry air = HIGH OLR",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
