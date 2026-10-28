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
