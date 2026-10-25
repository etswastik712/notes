"""CL08 diagram: the leaky one-layer greenhouse (SVG + Excalidraw)."""
import diagrams

SPEC = dict(
    size=(760, 480),
    nodes={
        "space": dict(x=380, y=70, w=230, h=64, text="Space", color="blue"),
        "atm": dict(x=150, y=235, w=250, h=96, text="Atmospheric layer\nT_a, absorptivity ε\nemits ε σT_a⁴ up and down", color="aqua"),
        "sfc": dict(x=380, y=400, w=240, h=64, text="Surface  T_s\nemits σT_s⁴", color="orange"),
        "sun": dict(x=640, y=235, w=190, h=76, text="Absorbed sunlight\n(1−α)S/4 = 238 W/m²", color="grey"),
    },
    arrows=[("sun", "sfc", ""), ("sfc", "atm", "absorbed εσT_s⁴"), ("atm", "space", "εσT_a⁴"), ("sfc", "space", "leaks (1−ε)σT_s⁴")],
    title="Leaky greenhouse: three balances",
    footer="TOA: Q = εσT_a⁴ + (1−ε)σT_s⁴;  surface: Q + εσT_a⁴ = σT_s⁴;  layer: 2εσT_a⁴ = εσT_s⁴",
)

if __name__ == "__main__":
    diagrams.svg("CL08 Leaky Greenhouse", SPEC)
    diagrams.excalidraw("CL08 Leaky Greenhouse", SPEC)
