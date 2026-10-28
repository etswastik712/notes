"""Wrap converted EC2123 bodies (tex2vault_ls.py output *.md.body) into vault chapters in 05-Landscapes-Geomorphology/.
python3 scripts/assemble_ls.py <dir with *.md.body>"""
import os
import re
import sys

BODY = sys.argv[1]
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "05-Landscapes-Geomorphology")

CH = [
 # code, title, part, slides, story, abilities, mermaid, links
 ("LS01", "Landscapes as Physical Systems", "I", "1–24", "A landscape is a surface $z(x,y,t)$ that changes by uplift, weathering, erosion and deposition; mapping it, measuring the forces and fluxes on it, and modelling how it evolves are three views of one physical problem.",
  ["state the programme *map, measure, model* and the kinematic bookkeeping $\\partial_tz=U-E$", "list the processes that shape landscapes and give their spatial and temporal scales", "read the Google-Earth tour of slides 10–18 and answer its exercises"],
  'flowchart LR\n  A["map: patterns, scales"] --> B["measure: forces, fluxes"]\n  B --> C["model: mass, force, steady state"]\n  C --> D["processes: uplift, weathering, erosion"]\n  D --> E["scales in space and time"]'),
 ("LS02", "Mechanics and Mathematics Toolkit", "I", "35–38, 45–50", "Almost every landscape equation is one of four things: a Taylor expansion, mass conservation with a flux, a force balance with a stress, or a viscous flow; this chapter derives each once so the rest can use them.",
  ["expand a function in a Taylor series and use order-of-magnitude reasoning", "write mass conservation $\\partial_t\\rho+\\partial_xq=S$ and derive the diffusion equation", "balance forces on a slab and use stress, pressure and viscosity", "solve the Newtonian viscous flow down an incline"],
  'flowchart LR\n  A["orders of magnitude,<br/>dimensions"] --> B["Taylor series,<br/>Newton laws"]\n  B --> C["mass conservation,<br/>flux, diffusion"]\n  C --> D["force balance, stress"]\n  D --> E["viscous flow"]'),
 ("LS03", "Digital Elevation Models and Terrain Analysis", "II", "25, 28, 56–57", "A digital elevation model is a matrix of heights; slopes, curvature, flow directions, drainage basins and the hypsometric curve are just arithmetic on that matrix.",
  ["describe a DEM as a raster and say how elevation is measured (SRTM, LiDAR, photogrammetry)", "compute slope, aspect and curvature on a grid", "extract a river network and a drainage basin", "read and compute a hypsometric curve"],
  'flowchart LR\n  A["DEM = raster of z"] --> B["how z is measured"]\n  B --> C["slope, aspect, curvature"]\n  C --> D["flow routing,<br/>river network, basins"]\n  D --> E["hypsometry"]'),
 ("LS04", "Map Projections and Reference Surfaces", "II", "31–32, 42", "A sphere cannot be flattened without distortion; the Mercator projection preserves angles at the price of area, and the heights on every map are relative to a reference ellipsoid and a datum.",
  ["explain why every map projection distorts", "derive the Mercator projection from conformality", "describe transverse Mercator and UTM", "distinguish geoid, ellipsoid and datum"],
  'flowchart LR\n  A["sphere is not developable"] --> B["Mercator: conformal"]\n  B --> C["transverse Mercator, UTM"]\n  C --> D["ellipsoid and datum"]'),
 ("LS05", "Shape of Planets", "III", "33, 41–42, 51", "Planets are round because gravity beats rock strength, slightly flattened because they rotate, and the geoid is the equipotential surface sea level would follow.",
  ["show that large bodies are spherical (gravity vs strength)", "derive the flattening of a rotating planet", "define the geoid and its relation to the ellipsoid"],
  'flowchart LR\n  A["gravity vs strength:<br/>why round"] --> B["rotation: oblateness"]\n  B --> C["flattening ~ 1/300"]\n  C --> D["geoid vs ellipsoid"]'),
 ("LS06", "Maximum Topography", "III", "52–55", "A column of rock can only stand as tall as its strength allows; comparing strength with the weight of the column gives an upper bound on relief on Earth, Mars and small bodies.",
  ["state the strength of rock and its yield criterion", "derive an upper bound on mountain height", "explain friction-limited relief on small bodies"],
  'flowchart LR\n  A["rock strength"] --> B["weight of a column"]\n  B --> C["upper bound on relief"]\n  C --> D["small bodies: friction limit"]'),
 ("LS07", "Isostasy", "IV", "58–64", "Topography floats: mountains have roots like icebergs, the mantle flows to restore the balance, and an eroding mountain rises again.",
  ["state Airy and Pratt isostasy and compute a root", "explain why isostasy works (mantle flow)", "derive the thermal subsidence of the ocean floor", "compute the isostatic uplift caused by erosion"],
  'flowchart LR\n  A["gravity anomalies"] --> B["Airy isostasy: roots"]\n  B --> C["why it works:<br/>mantle flows"]\n  C --> D["oceans: thermal isostasy"]\n  D --> E["erosion -> rebound"]'),
 ("LS08", "Plate Tectonics Strain Stress and Convection", "V", "65–75", "Plates move because the mantle convects; stress and strain rate in the lithosphere tell where earthquakes and volcanoes occur and how fast the plates go.",
  ["map earthquakes and volcanoes onto plate boundaries", "define strain, strain rate and stress", "state the Rayleigh–Bénard criterion", "estimate a plate speed"],
  'flowchart LR\n  A["earthquakes, volcanoes"] --> B["strain rate"]\n  B --> C["stress in the lithosphere"]\n  C --> D["Rayleigh-Benard convection"]\n  D --> E["plate speed estimate"]'),
 ("LS09", "Faults and Earthquakes", "V", "85–94", "Anderson's theory turns the stress state into a fault type; earthquakes are the stick–slip release of stored elastic strain, and the Himalaya records that cycle on four time scales.",
  ["classify normal, reverse and strike-slip faults by principal stresses (Anderson)", "describe the earthquake cycle as stick–slip", "read InSAR and fault-topography figures", "tell the story of the Himalaya over four time scales"],
  'flowchart LR\n  A["principal stresses"] --> B["fault types (Anderson)"]\n  B --> C["stick-slip: earthquake cycle"]\n  C --> D["finite faults, InSAR"]\n  D --> E["Himalaya: 4 time scales"]'),
 ("LS10", "Folds Flexure and Mountain Building", "V", "76–84, 90, 95", "A plate bends elastically under a load (flexure), layers buckle into folds, a mountain belt is a critical wedge, and climate feeds back on tectonics.",
  ["derive the elastic flexure of a plate under a line load", "describe fold geometry and buckling", "explain critical taper (sandbox and Himalaya)", "state the climate–tectonics coupling"],
  'flowchart LR\n  A["mountain belts,<br/>passive margins"] --> B["elastic flexure"]\n  B --> C["folds, buckling"]\n  C --> D["critical taper: sandbox"]\n  D --> E["climate-tectonic coupling"]'),
 ("LS11", "Weathering and Regolith", "VI", "96–116", "Weathering turns rock into mobile regolith, chemically by dissolution and physically by cracking; regolith thickness is production balanced against removal.",
  ["define weathering and the two limiting regimes (supply- and transport-limited)", "derive regolith thickness from production against erosion", "describe chemical weathering (Arrhenius, Goldich series, rates)", "describe physical weathering (frost cracking, thermal stress, salts)"],
  'flowchart LR\n  A["weathering regimes"] --> B["regolith: production vs erosion"]\n  B --> C["chemical weathering"]\n  B --> D["physical weathering"]\n  C --> E["solute vs sediment load"]\n  D --> E'),
 ("LS12", "Hillslope Transport and the Diffusion Equation", "VII", "117–122", "Soil creeps downhill at a rate proportional to the slope, so the hillslope obeys the diffusion equation and hilltops are convex.",
  ["list slope-dependent transport processes (rain-splash, tree-throw, impacts)", "derive linear flux $q=-\\kappa_h\\partial_xz$", "write and solve the hillslope diffusion equation", "state the nonlinear flux near the angle of repose"],
  'flowchart LR\n  A["slow processes:<br/>flux proportional to slope"] --> B["rain-splash: q ~ S"]\n  A --> C["bioturbation, impacts"]\n  B --> D["mass conservation"]\n  C --> D\n  D --> E["diffusion equation,<br/>convex hilltops"]'),
 ("LS13", "Landslides", "VII", "123–137", "A slope fails when driving stress exceeds the friction and cohesion resisting it; pore pressure lowers the threshold, and runout and size distributions follow.",
  ["derive infinite-slope stability with pore pressure", "distinguish loose and dense initiation", "describe size distribution and runout", "read the case studies (Kedarnath, Kerala, Mars, Moon)"],
  'flowchart LR\n  A["infinite slope: driving vs resisting"] --> B["pore pressure"]\n  B --> C["initiation: loose vs dense"]\n  C --> D["size distribution, runout"]\n  D --> E["case studies"]'),
 ("LS14", "Glaciers Mass Balance and Ice Flow", "VIII", "138–144", "A glacier is a river of ice whose size is set by accumulation against ablation and whose speed comes from viscous deformation (Glen's law) plus sliding.",
  ["write the glacier mass balance and ice flux equation", "derive deformation velocity from Glen's flow law", "describe sliding and the role of water", "read the slide figures on glacier geometry"],
  'flowchart LR\n  A["open, non-equilibrium system"] --> B["mass balance b(z)"]\n  B --> C["ice flux Q"]\n  C --> D["Glen flow law (n = 3)"]\n  D --> E["sliding, water"]'),
 ("LS15", "Glacial Deposits Rebound and Sea Level", "VIII", "145–153", "Glaciers carry debris and leave moraines; their weight depresses the crust and removal makes it rebound, and ice volume sets sea level and coral reefs record it.",
  ["describe debris on a glacier and moraines", "explain the Last Glacial Maximum imprint and Gondwana glaciations", "derive glacial isostatic adjustment", "relate ice volume to sea level and coral terraces"],
  'flowchart LR\n  A["debris, moraines"] --> B["LGM imprint, Gondwana"]\n  B --> C["isostatic adjustment"]\n  C --> D["sea level, coral reefs"]'),
 ("LS16", "Fluvial Landscapes", "IX", "(post-midsem; not in the pre-midsem slides)", "Rivers incise bedrock at a rate set by drainage area and slope (stream power), reach a graded form in alluvium, and respond to base-level change by migrating knickpoints.",
  ["write the stream-power incision law and its steady-state profile", "explain knickpoint migration", "describe alluvial channel geometry and braiding", "define base level and grade"],
  'flowchart LR\n  A["networks, discharge"] --> B["stream power: E = K A^m S^n"]\n  B --> C["knickpoints, transients"]\n  C --> D["alluvial channels, braiding"]\n  D --> E["base level, grade"]'),
 ("LS17", "Aeolian Landscapes", "IX", "(post-midsem; see also l_glacial_aolian.pdf)", "Wind moves sand in hops (saltation) above a threshold shear velocity, and the resulting dunes migrate with a speed inversely proportional to their height.",
  ["derive the threshold for saltation and the sand flux", "classify dune morphologies by wind regime", "compute dune migration rate"],
  'flowchart LR\n  A["threshold shear velocity"] --> B["saltation, sand flux"]\n  B --> C["dune morphology"]\n  C --> D["dune migration"]'),
 ("LS99", "Landscapes Practice Problems", "X", "all", "Problems that turn each chapter's results into numbers: orders of magnitude for flexure, isostasy, diffusion, glaciers and rivers.", ["solve the problems in order of the chapters", "check each answer against the stated assumptions"], 'flowchart LR\n  A["foundations"] --> B["planet, isostasy"]\n  B --> C["tectonics"]\n  C --> D["surface processes"]\n  D --> E["glaciers, rivers"]'),
]
TITLES = {c[0]: c[1] for c in CH}


def link(code):
    return "[[%s %s]]" % (code, TITLES[code])


# front matter note
fb = open(os.path.join(BODY, "LS00.md.body")).read().strip()
fb = re.sub(r"\n> \[!figure\]- [^\n]*\n> [^\n]*\n", "\n", fb)
open(os.path.join(OUT, "Landscapes Notation and Glossary.md"), "w").write("""---
title: Landscapes Notation and Glossary
aliases: [EC2123 notation, landscapes glossary, landscapes symbol table]
subject: landscapes
type: moc
scope: [taught, extra-beyond]
by: [ai-notes, slides]
status: draft
tags: [subject/landscapes, type/moc, taught, extra/beyond, src/ai-notes, status/draft]
---
# Landscapes: Notation, Symbols, Terminology and Slide Map

Front matter of the EC2123 derivation notes, converted to the vault: how the boxes are used, the conventions, the **symbol table**, the **terminology key**, the **map from slides to chapters** and the **two places where the slides need care** (flagged `[verify]`). Back to [[Landscapes and Geomorphology - Course Map]].

""" + fb + "\n")
print("LS00 written")

for i, (code, title, part, slides, story, abil, mer) in enumerate(CH):
    body = open(os.path.join(BODY, code + ".md.body")).read().strip()
    prev = link(CH[i - 1][0]) if i > 0 else "[[Landscapes and Geomorphology - Course Map|Course Map]]"
    nxt = link(CH[i + 1][0]) if i < len(CH) - 1 else "(end)"
    nsec = len(re.findall(r"^## ", body, re.M))
    nder = body.count("[!derivation]")
    nfig = len(re.findall(r"!\[\[ls_fig", body))
    nsl = len(set(re.findall(r"pre_(\d{3})\.jpg", body)))
    fm = f"""---
title: {code} {title}
aliases: [{code}, {title}]
subject: landscapes
type: chapter
chapter: {int(code[2:]) if code != 'LS99' else 99}
part: {part}
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# {code} · {title}

◀ {prev} · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: {nxt}

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides {slides} of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has {nsec} sections, {nder} derivation boxes, {nfig} redrawn figures and {nsl} slide images.

> [!key] After this chapter you can
{chr(10).join('> - ' + a + ',' for a in abil).rstrip(',')}.

> [!intuition] The one-sentence story
> {story}

```mermaid
{mer}
```
*Concept map: every box is a section of this chapter.*

"""
    tail = f"""

## Map of this chapter
> [!connection] How {code} connects
> **Previous:** {prev} · **Next:** {nxt}.
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides {slides} (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].
"""
    open(os.path.join(OUT, f"{code} {title}.md"), "w").write(fm + body + tail)
    print(code, title)
