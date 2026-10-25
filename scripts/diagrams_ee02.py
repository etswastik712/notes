"""EE02 - conceptual diagram (SVG + Excalidraw).   .venv/bin/python scripts/diagrams_ee02.py"""
from diagrams import excalidraw, svg

SPECS = {
    "EE02 From Life Table to Management": dict(
        size=(920, 520),
        nodes={
            "t": dict(x=200, y=95, w=290, h=84, text="Cohort life table\nl_x (survival), m_x (fecundity)\nR0 = sum of l_x m_x", color="blue"),
            "s": dict(x=590, y=95, w=290, h=84, text="Survivorship curve\nlog l_x against age:\nType I, II or III", color="blue"),
            "m": dict(x=200, y=250, w=290, h=84, text="Projection matrix\nn(t+1) = A n(t)\nLeslie (age) or Lefkovitch (stage)", color="orange"),
            "e": dict(x=590, y=250, w=250, h=104, text="Eigen-analysis of A\nlambda: long-run growth\nw: stable distribution\nv: reproductive value", color="aqua"),
            "h": dict(x=830, y=250, w=150, h=84, text="Age pyramids\nbase width\nfollows lambda", color="grey"),
            "p": dict(x=590, y=400, w=290, h=84, text="Perturbation analysis\nelasticity of lambda:\nwhich rate matters most?", color="aqua"),
            "a": dict(x=200, y=400, w=290, h=84, text="Management\nprotect large juveniles\n(turtle excluder devices)", color="grey"),
        },
        arrows=[("t", "m", ""), ("s", "m", ""), ("m", "e", ""), ("e", "h", ""), ("e", "p", ""), ("p", "a", "")],
        title="Structured populations in one pass: from a life table to a conservation decision",
        footer="Slides 9-29: Phlox table -> survivorship -> Leslie matrix -> stable age distribution -> loggerhead stage matrix -> sensitivity -> TEDs; humans: pyramids",
    ),
}

if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
