"""CL14 diagram: why the ITCZ is a band of convergence, a self-reinforcing loop (SVG + Excalidraw), via scripts/diagrams.py."""
from diagrams import excalidraw, svg

SPEC = dict(
    size=(860, 520),
    nodes={
        "sst":  dict(x=430, y=60,  w=300, h=70, text="Warm tropical surface\n(sunlight, warm ocean)", color="orange"),
        "low":  dict(x=700, y=190, w=290, h=76, text="Surface air warms and rises:\nlow pressure near the equator", color="blue"),
        "conv": dict(x=700, y=360, w=290, h=76, text="Trades blow in from both\nhemispheres: convergence", color="aqua"),
        "asc":  dict(x=430, y=450, w=300, h=70, text="Moist air ascends:\ndeep clouds and heavy rain", color="grey"),
        "lat":  dict(x=160, y=360, w=290, h=76, text="Condensation releases latent\nheat: column warms further", color="orange"),
        "out":  dict(x=160, y=190, w=290, h=76, text="Upper-level outflow towards\nboth poles: Hadley cells", color="blue"),
    },
    arrows=[("sst", "low", ""), ("low", "conv", "+"), ("conv", "asc", "+"), ("asc", "lat", "+"), ("lat", "out", ""), ("out", "sst", "")],
    title="The ITCZ: trade-wind convergence feeds ascent, and ascent deepens the low (a positive loop)",
    footer="Surface convergence at the equator ⇒ ascent ⇒ upper outflow: the ascending branch of the Hadley circulation (CL11)",
)

if __name__ == "__main__":
    svg("CL14 ITCZ Convergence Loop", SPEC)
    excalidraw("CL14 ITCZ Convergence Loop", SPEC)
