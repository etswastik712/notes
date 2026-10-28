---
title: LS01 Landscapes as Physical Systems
aliases: [LS01, Landscapes as Physical Systems]
subject: landscapes
type: chapter
chapter: 1
part: I
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS01 · Landscapes as Physical Systems

◀ [[Landscapes and Geomorphology - Course Map|Course Map]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS02 Mechanics and Mathematics Toolkit]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 1–24 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 6 sections, 1 derivation boxes, 1 redrawn figures and 9 slide images.

> [!key] After this chapter you can
> - state the programme *map, measure, model* and the kinematic bookkeeping $\partial_tz=U-E$,
> - list the processes that shape landscapes and give their spatial and temporal scales,
> - read the Google-Earth tour of slides 10–18 and answer its exercises.

> [!intuition] The one-sentence story
> A landscape is a surface $z(x,y,t)$ that changes by uplift, weathering, erosion and deposition; mapping it, measuring the forces and fluxes on it, and modelling how it evolves are three views of one physical problem.

```mermaid
flowchart LR
  A["map: patterns, scales"] --> B["measure: forces, fluxes"]
  B --> C["model: mass, force, steady state"]
  C --> D["processes: uplift, weathering, erosion"]
  D --> E["scales in space and time"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 1–9, 19–24]*


## The programme: map, measure, model

The first lecture (slide 7) states the method of the whole course. For *any* interesting piece of landscape one should


1. **map** surface and subsurface structures — patterns, spatial scales, orientations;
2. **measure** forces and fluxes — which processes act and how fast mass moves;
3. **model** formation and evolution — time scales, rates, and how the form will change.


Slide 8 adds the *language* of the model: mass conservation, force balance, steady states and feedbacks. Everything quantitative in this text is an application of only these four ideas to different materials (water, ice, air, rock, regolith).


![[ls_fig01.png]]
*Figure LS01.1. The map–measure–model cycle of slide 7.*


## Landscapes are dynamic: the kinematic bookkeeping

Slide 8 lists what changes a landscape: *uplift, exhumation and subsidence* (vertical mass flux caused by force imbalance), *weathering* (physical and chemical), and *erosion and deposition* (“horizontal” mass transport by viscous flow of mantle/ice/water/air, by deformation and fracture of solids in earthquakes, and by gravity-driven flow of solids in landslides). To use these words rigorously we need precise definitions.


> [!key] Definition: Uplift, exhumation, denudation
> Let $z_s(x,y,t)$ be the surface elevation above the geoid and let a particle of rock initially at the surface have elevation $z_r(t)$.
> *Rock uplift* is $U=\mathrm{d} z_r/\mathrm{d} t$ (motion of rock relative to the geoid). *Denudation* is $\mathcal{E}$, the rate at which the surface is lowered relative to the rock beneath it (physical removal + chemical loss). *Exhumation* is the rock's motion toward the surface, i.e. $\mathcal{E}$ measured following the rock. *Surface uplift* is $\partial_tz_s$.


> [!derivation] 🔵 Extra (not derived in the slides): Surface uplift $=$ rock uplift $-$ denudation
> Consider a column of rock. In a time $\mathrm{d} t$ the rock at the top rises by $U \mathrm{d} t$ (relative to the geoid); at the same time a layer of thickness $\mathcal{E} \mathrm{d} t$ is removed from the top. The surface therefore moves by $(U-\mathcal{E})\mathrm{d} t$:
>
>
> $$
> \dfrac{\partial z_s}{\partial t}=U-\mathcal{E}. \tag{1}
> $$
>
>
> **Steady state** of the surface elevation ($\partial_tz_s=0$) requires $U=\mathcal{E}$: uplift is exactly balanced by denudation. Then material still passes through the landscape (the rock is exhumed at rate $\mathcal{E}=U$) although the form does not change. This distinction between *form* being steady and *mass* being in transit is used repeatedly (hillslope steady state, glacier steady state, ocean-floor depth).


> [!example] 🧮 Worked example: Is a mountain range near steady state?
> Take $U=2\times10^{-3} \mathrm{m yr^{-1}}$ ($2$ mm/yr, typical of active orogens). To exhume a crustal thickness of $35$ km requires $35 000/0.002=1.75\times10^7$ yr. Yet the Himalaya has been rising for $\sim5\times10^7$ yr, so it can be near steady state or dynamically adjusting – a question that the time scales of Chapters 9–10 will let us answer quantitatively.


## The processes at a glance


| Process | Driving force | Carrier / material | Where developed |
|---|---|---|---|
| Rock uplift, subsidence | buoyancy, tectonic stress, elastic forces | rock (crust, mantle) | Ch. 7–10 |
| Weathering | chemical disequilibrium, thermal and frost stress | water, air, ice, biota | Ch. 11 |
| Hillslope creep, rain-splash | gravity (slope-dependent) | regolith | Ch. 12 |
| Landslides | gravity exceeding strength | rock, soil, water | Ch. 13 |
| Ice flow | gravity on a viscous, power-law fluid | glacier ice | Ch. 14–15 |
| River flow | gravity on water; shear on bed | water, sediment | Ch. 16 |
| Wind transport | drag of air on grains | air, sand | Ch. 17 |
| Earthquakes | elastic strain release, friction | rock | Ch. 9 |

*Landscape-forming processes (slide 8) and the chapters in which each is treated quantitatively.*


**Earth-system feedbacks** (slide 8, “an earth-system approach is necessary”). A landscape is affected by, *and feeds back on*, the atmosphere (precipitation, temperature), hydrosphere (rivers, ocean), cryosphere (ice), biosphere (vegetation, burrowing), lithosphere (tectonics, isostasy) and human activity. A closed feedback loop that the deck develops is: uplift $\to$ orography $\to$ rain and glaciers $\to$ erosion $\to$ unloading $\to$ isostatic uplift $\to$ more relief; and: tectonic uplift $\to$ enhanced silicate weathering $\to$ lower CO$_2$ $\to$ cooling (Chapter 10).


## Scales in space and time

Every chapter below quotes a length and a time; their orders of magnitude organise the subject.


| Phenomenon (slide) | Horizontal scale | Time scale |
|---|---|---|
| Earthquake rupture (Gorkha 2015, S93) | $10^{5}$ m | $10^{1}$ s; recurrence $10^{2}$–$10^{3}$ yr |
| Glacier surge / retreat (S138–140) | $10^{3}$–$10^{5}$ m | $10^{0}$–$10^{3}$ yr |
| Hillslope evolution (S121) | $10^{2}$ m | $10^{3}$–$10^{5}$ yr |
| Landslide (S123–137) | $10^{1}$–$10^{4}$ m | seconds to minutes |
| Isostatic rebound after ice (S148) | $10^{6}$ m | $10^{3}$–$10^{4}$ yr |
| Recent Himalayan uplift, terraces (S92) | $10^{4}$ m | $10^{3}$–$10^{4}$ yr |
| Ocean-floor cooling (S62) | $10^{6}$ m | $10^{8}$ yr |
| Building the Himalaya, Western Ghats (S77, S91) | $10^{6}$ m | $10^{7}$–$10^{8}$ yr |
| Folds (S80) | $10^{-1}$ to $10^{5}$ m | $10^{3}$–$10^{7}$ yr |

*Orders of magnitude of the scales on the slides.*


## The Google-Earth tour (slides 10–18) and exercises


Slide 9 says “let's explore interesting landscapes on Earth (and Mars)”. Slides 10–18 are Google-Earth views; from the coordinates printed on the images and the features visible, each illustrates a process studied later.


![[pre_010.jpg|300]] ![[pre_011.jpg|300]] ![[pre_012.jpg|300]] ![[pre_013.jpg|300]]


> [!example] 🖼 Reading the diagram: Slides 10–18 read one by one
> | Slide | What the view shows | Process and chapter |
> |---|---|---|
> | 10 | The Pacific basin from high altitude: island/seamount chains, ridges and the trench system around the rim | Plate tectonics, ocean-floor age and depth (Ch. 7, 8) |
> | 11 | South Georgia and the South Sandwich Islands: a curved island arc on the seafloor with a trench on its outer side (scale bar 420 km) | Subduction, island arcs, volcanoes (Ch. 8) |
> | 12 | Central Andes/Atacama: trench offshore, a high plateau with white salt flats | Subduction-driven orogen, isostasy (Ch. 7, 8) |
> | 13 | Fold belt with salt domes (image at $27^\circ$N, $54.8^\circ$E; Zagros, Iran; scale 28 km) | Folding, wavelength selection (Ch. 10) |
> | 14 | Himalayan glaciers near Mt. Everest (scale 5.9 km, $28^\circ$N, $86.8^\circ$E) | Glaciers, moraines, lakes (Ch. 14–15) |
> | 15 | Rivers leaving hills onto a plain, one wide braided river (Nepal–Bihar border) | Fluvial fans and braiding (Ch. 16) |
> | 16 | Sundarbans tidal-channel delta ($21.8^\circ$N, $89.2^\circ$E) | Fluvial-tidal deposition (Ch. 16) |
> | 17 | Dune field (Iranian desert by the coordinates) with wind-aligned linear and star dunes | Aeolian transport (Ch. 17) |
> | 18 | Lonar crater, Maharashtra ($19.98^\circ$N, $76.5^\circ$E): circular crater with lake in Deccan basalt | Impact landform; weathering of basalt (Ch. 11) |


> [!example] ❓ Question on the slides: Exercises ex1, ex2 (slide 19): how to do a quantitative “Google-Earth story”
> Slide 19 asks for (ex1) exploring the features above and (ex2) a story on a *dynamic* landscape of the Indian subcontinent using measurement tools and historical imagery. A rigorous version answers the following, each reducible to a formula:
>
>
> - **Scales**: horizontal scale $L$ from the ruler tool; vertical scale $H$ from the elevation profile; the *aspect ratio* $H/L$ tells whether the form is a thin layer ($H/L\ll1$) or a steep body. Note that Google Earth applies a vertical exaggeration factor (default 1, adjustable); always check it before reading slopes.
> - **Rates**: from two imagery dates $t_1,t_2$ the displacement $\Delta\ell$ of a feature (glacier terminus, river bank, dune crest) gives velocity $v=\Delta\ell/(t_2-t_1)$. Example: a terminus retreat of $500$ m in $20$ yr is $25 \mathrm{m yr^{-1}}$.
> - **Fluxes**: volume flux of a flowing body $=$ width $\times$ mean thickness $\times$ mean speed, e.g. $Q=W\bar H\bar u$; mass flux multiplies by density. Compare with supply (snowfall, rainfall, source area).
> - **Steady or evolving?** Compare $\partial_tz$ from imagery/DEM differencing with the uplift rate of (1).
> - **Forces and feedbacks**: what balances gravity (friction, viscosity, buoyancy)? Human imprints? Analogues on Mars or the Moon (slide 117 compares Mars, Moon and Munnar hillslopes)?
>
>
> Finally “check recent papers on the chosen landform. Do we know enough?”: the criterion is whether a model built from mass conservation and force balance reproduces the measured rates.


## Course structure and the local landscape (slides 20–24)

> [!figure]- 🖼 Slides 20–24: open to see the slides this section explains
> ![[pre_020.jpg|300]] ![[pre_021.jpg|300]] ![[pre_022.jpg|300]] ![[pre_023.jpg|300]] ![[pre_024.jpg|300]]

The syllabus (slide 20) has eight blocks: (1) Google-Earth tour, DEMs, contour maps, spatial/temporal scales, force balance and mass conservation; (2) planetary-scale landforms (oblateness, maximum topography, hypsometry, isostasy, plate boundaries, folds, faults, earthquakes); (3) erosional processes (physical and chemical weathering, climate–erosion–uplift linkage); (5) hillslope processes and landslides; (6) fluvial landscapes; (7) glacial landscapes; (8) aeolian landscapes. The slides cover 1, 2, 3, 5 and part of 7; Part IX of these notes covers 6 and 8. Assessment is open-notes, relatively graded.

Slides 21–24 show the landscape around the campus: the Deccan Traps of the Sahyadri, with the mapped dyke swarms (Narmada–Tapi, Pune–Nashik and the Western coastal swarm) and the Western Ghat escarpment; spheroidal (onion-skin) weathering of basalt; and a hillshade of the region. They anticipate Chapters 3 and 11.

## Further slides explained one by one
<span class="scope-taught">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*

![[pre_001.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 1: Ganglas, Leh: stories behind landscapes
> Two photographs open the course. *Left:* a wide view from the Ganglas pass down to the Leh valley, the flat floor of the Indus valley with fields and the town, and behind it the snow-capped Stok–Zanskar range: a high-altitude, arid mountain landscape. *Right:* a group photograph of the LIGSS 2026 field party on the ridge. The caption sets the tone of the whole course: every landscape has a story (uplift, glaciation, rivers) that classical mechanics can read.

![[pre_002.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 2: Ladakh strata and the India–Eurasia collision
> A desert ridge of tilted, light-coloured sedimentary strata dips steeply to the right: bedding rotated by collision-related folding and thrusting. The inset (Martin et al., PNAS 2020) is a tectonic map of the India–Eurasia collision zone: pink = Eurasian-affinity units, blue = Indian-affinity units, the dark line between them the Indus–Yarlung suture where the Tethys ocean closed. It links what you see in the photograph (rock tilted and folded) with the plate-scale cause (§LS08–LS10).

![[pre_003.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 3: Irshalwadi landslide
> A rocky basalt hillside in the Western Ghats (Raigad, Maharashtra) with a scar left by the July 2023 Irshalwadi landslide: bare brown rubble above, tree cover at the sides. It is the first of several landslide examples; the mechanics is in [[LS13 Landslides]] and the case studies at the end of that chapter.

![[pre_014.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 14: Google-Earth tour: Himalayan glaciers
> A Google-Earth view at about 5,300 m (lat 27.97° N, lon 86.8° E, Khumbu region; the label 'Mt Everest' is cut off at the right edge): several debris-covered glacier tongues flow from the snow-covered peaks, with turquoise supraglacial and proglacial lakes. The debris cover (grey-brown) is rock that has fallen onto and out of the ice ([[LS15 Glacial Deposits Rebound and Sea Level]]). Part of the exercise set of slides 10–20.

![[pre_015.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 15: Google-Earth tour: a braided river leaving the mountains
> A braided gravel-bed river (light bars separated by channels) leaves forested foothills (lat 26.69° N, lon 86.94° E, scale bar 8 km) and spreads on its fan; an abandoned meander loop (circular scar at the centre) shows channel migration. It illustrates fluxes of water and sediment and the lateral mobility of alluvial rivers ([[LS16 Fluvial Landscapes]]).

![[pre_016.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 16: Google-Earth tour: the Sundarbans delta
> A tidal delta in the Bay of Bengal (lat 21.85° N, lon 89.2° E, scale 26 km): dense mangrove islands separated by branching tidal channels that widen seaward. Landscape evolving at sea level: sediment supply, tides and subsidence control its shape.

![[pre_017.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 17: Google-Earth tour: a dune field
> A desert dune field: sinuous ridges with slip faces facing one direction and lighter interdune flats. The shape records the wind direction and sand supply ([[LS17 Aeolian Landscapes]]). (The coordinates on the slide are too small to read: location `[verify]`.)

![[pre_018.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 18: Google-Earth tour: Lonar crater
> A near-circular impact crater with a raised rim in Deccan basalt and a green saline lake on its floor (lat 19.98° N, lon 76.51° E), with the town of Lonar at the right. An example of a landscape made by a single instantaneous event and then modified slowly (see slide 120 on impacts and the Deccan chapter).

![[pre_019.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 19: Google-Earth exercise 2: write a story about a dynamic landscape
> Text slide. Exercise: use Google Earth to tell the story of a *dynamic* landscape in the Indian subcontinent using its tools (distance and area, elevation profile, historical imagery); discuss vertical and horizontal scales, formation and history, whether it is evolving, going up or down or shifting horizontally, the fluxes of wind, water, ice, sediment, rock, human imprint, Earth-system feedbacks and analogues on Mars or the Moon; check recent papers; Sentinel Hub is an alternative tool.


## Map of this chapter
> [!connection] How LS01 connects
> **Previous:** [[Landscapes and Geomorphology - Course Map|Course Map]] · **Next:** [[LS02 Mechanics and Mathematics Toolkit]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 1–24 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].
