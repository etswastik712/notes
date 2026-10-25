"""CL15 - conceptual monsoon circulation loop (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_cl15.py"""
from diagrams import excalidraw, svg

SPEC = dict(
    size=(780, 520),
    nodes={
        "oc":  dict(x=130, y=250, w=240, h=92, text="Cold ocean column\nhigh surface pressure\nsinking air", color="blue"),
        "lo":  dict(x=390, y=420, w=290, h=70, text="Low-level flow towards the land\nmoist, spiralling across isobars", color="aqua"),
        "ld":  dict(x=650, y=250, w=240, h=92, text="Warm land: thermal low\nconvergence, ascent,\nlatent heating", color="orange"),
        "up":  dict(x=390, y=80,  w=290, h=70, text="Upper-level outflow towards the ocean\nreversed pressure gradient", color="grey"),
        "mid": dict(x=390, y=250, w=210, h=84, text="Rain over the land\n= solar energy collected\nover the ocean", color="red"),
    },
    arrows=[("oc", "lo", ""), ("lo", "ld", ""), ("ld", "up", ""), ("up", "oc", "")],
    title="The monsoon as a land–sea circulation loop",
    footer="Heating contrast → pressure contrast → flow; moisture imported at low levels returns as latent heat aloft",
)
if __name__ == "__main__":
    svg("Monsoon Circulation Loop", SPEC)
    excalidraw("Monsoon Circulation Loop", SPEC)
