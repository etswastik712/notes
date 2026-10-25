"""CL07 diagram: the four fates of a beam crossing a layer (SVG + Excalidraw), using the shared builder in diagrams.py."""
import diagrams

SPEC = dict(
    size=(760, 470),
    nodes={
        "beam": dict(x=130, y=240, w=210, h=70, text="Incoming beam\nI₀", color="orange"),
        "layer": dict(x=380, y=240, w=230, h=90, text="Layer of air\noptical depth τ", color="grey"),
        "trans": dict(x=635, y=240, w=210, h=70, text="Transmitted\nI₀ e^(−τ)", color="blue"),
        "abs": dict(x=380, y=405, w=250, h=70, text="Absorbed → heat\nthen re-emitted (Kirchhoff)", color="red"),
        "sca": dict(x=380, y=75, w=250, h=70, text="Scattered → redirected\nsome back to space (albedo)", color="aqua"),
    },
    arrows=[("beam", "layer", ""), ("layer", "trans", ""), ("layer", "abs", ""), ("layer", "sca", "")],
    title="Four fates of a beam crossing a layer",
    footer="Extinction = absorption + scattering; only absorption heats the air",
)

if __name__ == "__main__":
    diagrams.svg("CL07 Photon Fates", SPEC)
    diagrams.excalidraw("CL07 Photon Fates", SPEC)
