"""Build the JSON-Canvas files and the Subject Map note from one relation table.

    .venv/bin/python scripts/build_canvases.py
Writes  00-Home/Subject Map.canvas, 00-Home/Subject Map.md, 01-Climate/Climate - Course Map.canvas.
Edit SUBJECTS / RELATIONS below to change the maps.  Canvas colours: 1 red, 2 orange, 3 yellow, 4 green, 5 cyan, 6 purple.
"""
import json
import math
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# key: (label, moc note title, phase colour, one-line status)
SUBJECTS = {
    "climate":    ("Climate", "Climate - Course Map", "4", "Phase 1 · pilot drafted"),
    "eco":        ("Ecology and Evolution", "Ecology and Evolution - Course Map", "4", "Phase 1 · next"),
    "thermo":     ("Thermodynamics and Stat. Mech.", "Thermodynamics and Statistical Mechanics - Course Map", "4", "Phase 1 · parallel track"),
    "earthevo":   ("Evolution of Earth and Life", "Evolution of Earth and Life - Course Map", "5", "Phase 2"),
    "landscapes": ("Landscapes and Geomorphology", "Landscapes and Geomorphology - Course Map", "5", "Phase 2"),
    "waves":      ("Waves", "Waves - Course Map", "5", "Phase 2"),
    "prob":       ("Probability", "Probability - Course Map", "5", "Phase 2"),
    "qm":         ("Quantum Mechanics", "Quantum Mechanics - Course Map", "6", "Phase 3"),
    "group":      ("Group Theory", "Group Theory - Course Map", "6", "Phase 3"),
    "chem":       ("Inorganic Chemistry", "Inorganic Chemistry - Course Map", "6", "Phase 3"),
    "analysis":   ("Proofs, Analysis and Topology", "Proofs, Analysis and Topology - Course Map", "6", "Phase 3"),
    "neuro":      ("Neuroscience", "Neuroscience - Course Map", "2", "Phase 4 · least connected"),
    "found":      ("Foundations (shared tools)", "Bistability and Tipping Points", "3", "grows with every subject"),
}

# (a, b, strength 1-3, reason)
RELATIONS = [
    ("climate", "thermo", 3, "radiation laws, gas law, adiabats, latent heat, entropy"),
    ("climate", "earthevo", 3, "paleoclimate, snowball Earth, faint young Sun, carbon cycle"),
    ("climate", "waves", 2, "Rossby, gravity and Kelvin waves; Fourier methods"),
    ("climate", "landscapes", 2, "weathering and CO2, glaciation, precipitation as a driver"),
    ("climate", "eco", 2, "biosphere feedbacks, Daisyworld, regime shifts"),
    ("climate", "chem", 2, "atmospheric chemistry, ozone, carbonate system"),
    ("climate", "qm", 2, "Planck law; molecular absorption spectra"),
    ("climate", "group", 1, "IR selection rules via molecular symmetry"),
    ("climate", "prob", 2, "sampling, autocorrelation, extremes in observations"),
    ("climate", "found", 3, "stability, linearisation, rotating frames, Jensen"),
    ("thermo", "qm", 3, "photon statistics, Planck law, quantised energy levels"),
    ("thermo", "prob", 3, "statistical mechanics is probability: ensembles, entropy"),
    ("thermo", "chem", 2, "chemical equilibrium, redox potentials, free energy"),
    ("thermo", "waves", 1, "mode counting in cavities, sound"),
    ("eco", "prob", 3, "stochastic population models, demography, Markov chains"),
    ("eco", "earthevo", 3, "macroevolution, extinctions, conservation"),
    ("eco", "analysis", 2, "chaos and bifurcations in discrete maps (May 1976)"),
    ("eco", "found", 3, "fixed points, stage-structured matrices, bistable lakes"),
    ("eco", "landscapes", 1, "habitat and landscape ecology"),
    ("eco", "neuro", 1, "behaviour (weak)"),
    ("qm", "group", 3, "symmetry, angular momentum, representations"),
    ("qm", "waves", 3, "wave mechanics, superposition, Schrodinger equation"),
    ("qm", "chem", 3, "atomic and molecular orbitals"),
    ("group", "chem", 3, "MO theory, vibrational selection rules, crystal field"),
    ("group", "analysis", 2, "abstract algebra and proof technique"),
    ("prob", "analysis", 3, "measure, convergence, limit theorems"),
    ("waves", "analysis", 1, "Fourier analysis"),
    ("earthevo", "landscapes", 2, "geology: tectonics, sedimentary record"),
    ("landscapes", "prob", 1, "statistics of floods and erosion"),
    ("neuro", "prob", 2, "neural coding, signal detection"),
    ("neuro", "waves", 1, "oscillations (EEG, rhythms)"),
    ("neuro", "found", 1, "bistable and critical dynamics"),
    ("neuro", "thermo", 1, "energy and information (weak)"),
    ("found", "analysis", 2, "rigour behind calculus and dynamical systems"),
]


def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT))


def subject_canvas():
    nodes, edges = [], []
    keys = list(SUBJECTS)
    R = 1000
    for i, k in enumerate(keys):
        ang = 2 * math.pi * i / len(keys) - math.pi / 2
        x, y = R * math.cos(ang), R * math.sin(ang)
        label, moc, col, status = SUBJECTS[k]
        link = f"[[{moc}|{label}]]"
        nodes.append(dict(id=k, type="text", x=int(x - 170), y=int(y - 70), width=340, height=140,
                          text=f"## {link}\n{status}", color=col))
    for j, (a, b, s, why) in enumerate(RELATIONS):
        if s < 2:
            continue
        edges.append(dict(id=f"e{j}", fromNode=a, toNode=b, fromEnd="none", toEnd="none",
                          color="4" if s == 3 else "5", label=why))
    save(os.path.join(ROOT, "00-Home", "Subject Map.canvas"), dict(nodes=nodes, edges=edges))


def subject_note():
    L = ["---", "title: Subject Map", "tags: [meta, type/moc]", "---", "# Subject Map",
         "",
         "How the subjects in this repository relate, and why. Interactive version: [[Subject Map.canvas|Subject Map (canvas)]]. "
         "Strength 3 = a topic cannot be understood without the other; 2 = regular exchange of tools or examples; 1 = occasional link.",
         "",
         "**Reading the map.** Climate, Thermodynamics and Ecology/Evolution form the first phase because they share the most tools (stability and feedback, radiation, probability); "
         "Quantum Mechanics, Group Theory and Inorganic Chemistry form a tight cluster; Neuroscience is the most isolated subject (a single paper so far) and is scheduled last.",
         "",
         "| Subject A | Subject B | Strength | Why they connect |", "|---|---|---|---|"]
    name = {k: f"[[{v[1]}\\|{v[0]}]]" for k, v in SUBJECTS.items()}
    for a, b, s, why in sorted(RELATIONS, key=lambda r: (-r[2], r[0], r[1])):
        L.append(f"| {name[a]} | {name[b]} | {s} | {why} |")
    L += ["", "## Degree of connection",
          "```dataview", 'TABLE length(rows) AS "Notes" FROM #type/moc OR #type/chapter GROUP BY subject', "```", ""]
    path = os.path.join(ROOT, "00-Home", "Subject Map.md")
    open(path, "w", encoding="utf-8").write("\n".join(L))
    print("wrote", os.path.relpath(path, ROOT))


CH = {  # chapter -> (title, status)
    1: ("CL01 Earth as a System", "draft"), 2: ("CL02 Observing Global Temperature", "draft"),
    3: ("CL03 Radiation and Planetary Energy Balance", "draft"), 4: ("CL04 Feedback and Multiple Steady States", "draft"),
    5: ("CL05 Thermodynamic State of the Atmosphere", "draft"), 6: ("CL06 Hydrostatic Balance and Vertical Structure", "draft"),
    7: ("CL07 Optical Properties of the Atmosphere", "draft"), 8: ("CL08 Greenhouse Models", "draft"),
    9: ("CL09 Radiative-Convective Equilibrium", "draft"), 10: ("CL10 Global Energy Balance and Meridional Structure", "draft"),
    11: ("CL11 Mean Meridional Circulation and Angular Momentum", "draft"), 12: ("CL12 Rotating Frames and the Coriolis Force", "draft"),
    13: ("CL13 Horizontal Motion - Geostrophic Balance and Friction", "draft"), 14: ("CL14 Observed Winds - Jets, Trades and the ITCZ", "draft"),
    15: ("CL15 Monsoons", "draft"),
}
PARTS = [("Part I · Climate system and energy balance", [1, 2, 3, 4]), ("Part II · The atmosphere at rest", [5, 6]),
         ("Part III · Radiation, greenhouse, convection", [7, 8, 9]), ("Part IV · General circulation", [10, 11, 12, 13, 14, 15])]


def climate_canvas():
    nodes, edges = [], []
    W, H, GX, GY = 360, 120, 60, 140
    y0 = 0
    for pi, (label, chs) in enumerate(PARTS):
        gy = pi * 330
        nodes.append(dict(id=f"g{pi}", type="group", x=-40, y=gy - 60, width=len(chs) * (W + GX) + 20, height=250, label=label))
        for i, c in enumerate(chs):
            t, st = CH[c]
            nodes.append(dict(id=f"c{c}", type="text", x=i * (W + GX), y=gy, width=W, height=H,
                              text=f"### [[{t}]]\n*{st}*", color="4" if st == "draft" else "3"))
    for c in range(1, 15):
        a, b = c, c + 1
        same = any(a in chs and b in chs for _, chs in PARTS)
        edges.append(dict(id=f"n{c}", fromNode=f"c{a}", toNode=f"c{b}", fromSide="right" if same else "bottom",
                          toSide="left" if same else "top", toEnd="arrow"))
    # concept hubs (file notes would embed full previews; text nodes with links keep the canvas light)
    hubs = [("h1", "[[Blackbody Radiation]]\n[[Planck Law]] · [[Stefan-Boltzmann Law]]", [3], "1"),
            ("h2", "[[Fixed Points and Linear Stability]]\n[[Bistability and Tipping Points]]", [4], "5"),
            ("h3", "[[Ideal Gas Law]]", [5, 6], "1"),
            ("h4", "[[Rotating Reference Frames]]\n[[Coriolis Force]]", [12], "5"),
            ("h5", "[[Absolute Angular Momentum of Air]]", [11, 12], "5"),
            ("h6", "[[Quantum Mechanics - Course Map]] · [[Group Theory - Course Map]]\n(molecular absorption)", [7], "6"),
            ("h7", "[[Evolution of Earth and Life - Course Map]]\n(snowballs, faint young Sun)", [4], "6"),
            ("h8", "[[Ecology and Evolution - Course Map]]\n(regime shifts, Daisyworld)", [4], "6")]
    bx = 2200
    for i, (hid, text, chs, col) in enumerate(hubs):
        nodes.append(dict(id=hid, type="text", x=bx, y=i * 160 - 40, width=380, height=120, text=text, color=col))
        for c in chs:
            edges.append(dict(id=f"x{hid}{c}", fromNode=f"c{c}", toNode=hid, toEnd="arrow", color=col))
    nodes.append(dict(id="title", type="text", x=-40, y=-190, width=800, height=90,
                      text="# Climate: course map\nGreen = drafted · yellow = stub · right-hand column = concept and cross-subject hubs"))
    save(os.path.join(ROOT, "01-Climate", "Climate - Course Map.canvas"), dict(nodes=nodes, edges=edges))


if __name__ == "__main__":
    subject_canvas()
    subject_note()
    climate_canvas()
