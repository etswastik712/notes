"""CL11 diagram: the angular-momentum cycle of the atmosphere (SVG + Excalidraw), built with scripts/diagrams.py."""
from diagrams import excalidraw, svg

SPEC = dict(
    size=(860, 520),
    nodes={
        "earth": dict(x=430, y=450, w=640, h=60, text="Solid Earth: a huge reservoir of angular momentum (AM)", color="grey"),
        "trop":  dict(x=160, y=300, w=300, h=96, text="Tropical surface: easterlies\nground runs east faster than air\n→ air gains westerly AM", color="blue"),
        "had":   dict(x=255, y=125, w=240, h=80, text="Hadley cell, upper branch\nmean flow carries AM\nupward and poleward", color="orange"),
        "jet":   dict(x=610, y=70, w=240, h=70, text="Subtropical jet\nlargest westerlies\n(AM turned to the right)", color="aqua"),
        "eddy":  dict(x=700, y=195, w=250, h=76, text="Mid-latitude eddies carry\nAM poleward and downward", color="orange"),
        "mid":   dict(x=690, y=330, w=310, h=96, text="Mid-latitude surface: westerlies\nair runs east faster than ground\n→ air loses AM to the Earth", color="blue"),
    },
    arrows=[("earth", "trop", "+AM"), ("trop", "had", "ascent"), ("had", "jet", ""), ("jet", "eddy", ""), ("eddy", "mid", ""), ("mid", "earth", "−AM")],
    title="Angular-momentum cycle: picked up in the tropics, dropped in the mid-latitudes",
    footer="In steady state the net torque of the Earth on the atmosphere is zero (otherwise the length of the day would drift)",
)

if __name__ == "__main__":
    svg("CL11 Angular Momentum Cycle", SPEC)
    excalidraw("CL11 Angular Momentum Cycle", SPEC)
