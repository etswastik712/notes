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


<!-- ls-depth:LS01:1 -->
> [!intuition] Why a *physics* course about landscapes? (context)
> Geomorphology began as description: **G. K. Gilbert** (1870s–90s, the Henry Mountains) already thought in terms of *rates, forces and equilibrium*, **W. M. Davis** (1899) replaced that by a *cycle* (youth, maturity, old age), and **J. T. Hack** (1960) returned to the idea that a landscape in *steady state* has all its slopes adjusted to each other. What changed after about 1985 is that we can finally **date** things (cosmogenic nuclides, thermochronology, OSL), so models must now get not only the *shape* but also the *rate* right (A&A §1.4). This course is the physics-first version: conservation laws, transport laws (rheology) and the size/frequency of events.
> *Where to read more:* Anderson and Anderson (A&A) ch. 1 ([[geomorphology-the-mechanics-and-chemistry-of-landscapes-9780521519786-0521519780_compress.pdf#page=23|PDF pp.23–26]]); Huggett, *Fundamentals of Geomorphology*, ch. 1 on system dynamics and equilibrium ([[Fundamentals of Geomorphology (Fundamentals of Physical Geography) - Second Edition (Richar Huggett) (z-library.sk, 1lib.sk, z-lib.sk).pdf#page=36|PDF p.36]]).

> [!key] 🟡 Extra · book: the three guiding principles of A&A (ch. 1)
> 1. **Conservation.** *"The rate of change of [quantity] within a definable volume equals the rate at which it is produced within that space, plus the rate at which it is transported in across the boundaries, minus the rate at which it is lost across the boundaries."* The quantity may be heat, regolith, ice, water, sediment, a radioactive isotope or momentum. A&A list thirteen uses (heat in the lithosphere, ice in a glacier, regolith on a hillslope, sediment in a bedform, water in a flood, momentum in the Navier–Stokes equation...). *Mathematically they all look the same:* rates of change are governed by spatial gradients in transport rates plus sources and sinks.
> 2. **Transport rules.** Material is moved by body forces (gravity) and surface tractions (stresses); *how fast* depends on the **rheology**, the relation between strain rate and stress. Different materials have different rheologies (see the table below).
> 3. **Event size and frequency.** A landscape feels many small events and a few huge ones; the question is which do the *work* (§ "Which events build the landscape?" below).

> [!derivation] 🔵 Extra (my derivation): the master equation behind principle 1
> Take a control volume with cross-section $A$ and length $\mathrm dx$ along $x$, containing a quantity of density $c$ (per unit volume). Let $q(x,t)$ be the flux (quantity per unit area per unit time) in $+x$ and $P$ the net production per unit volume per time (negative for decay). In $\mathrm dt$: change $=$ in $-$ out $+$ production, so
> $$\frac{\partial(cA\,\mathrm dx)}{\partial t}=A\big[q(x)-q(x+\mathrm dx)\big]+PA\,\mathrm dx\ \Longrightarrow\ \boxed{\frac{\partial c}{\partial t}=-\frac{\partial q}{\partial x}+P}\qquad\text{(in 3D: }\partial_tc=-\nabla\!\cdot\!\mathbf q+P).$$
> **Every equation of this course is this equation with a particular $c$, $\mathbf q$ and $P$:**
> | Chapter | $c$ | flux $q$ (the *transport rule*) | $P$ | result |
> |---|---|---|---|---|
> | [[LS01 Landscapes as Physical Systems\|LS01]] | surface height $z$ (mass per area $\rho z$) | none (kinematic: $U-\mathcal E$) | uplift $U$ | $\partial_tz=U-\mathcal E$ |
> | [[LS02 Mechanics and Mathematics Toolkit\|LS02]], [[LS08 Plate Tectonics Strain Stress and Convection\|LS08]] | temperature ($\rho c_pT$) | $-k\nabla T$ (Fourier) | radioactive heating | heat equation |
> | [[LS12 Hillslope Transport and the Diffusion Equation\|LS12]] | regolith height $h$ | $-D\,\partial_xz$ (creep) | soil production | hillslope diffusion |
> | [[LS14 Glaciers Mass Balance and Ice Flow\|LS14]] | ice thickness $H$ | $\bar uH$, $\bar u\propto H^{n+1}S^n$ (Glen) | mass balance $b$ | $\partial_tH=-\partial_xQ+b$ |
> | [[LS16 Fluvial Landscapes\|LS16]] | channel elevation $z$ | $-KA^mS^n$ (stream power: an *erosion* sink) | uplift $U$ | $\partial_tz=U-KA^mS^n$ |
> | [[LS17 Aeolian Landscapes\|LS17]], [[LS19 Glacial and Aeolian Landforms\|LS19]] | bed elevation | sand flux $q(u_*)$ | none | $\partial_tz=-\partial_xq/\rho_b$ |
> The **transport rule** is the only place where the *physics of the material* enters, and it is the only part that differs between chapters.

> [!example] 🟡 Extra · book: transport rules differ because rheologies differ
> | Material | How it responds to stress (rheology) | Consequence in this course |
> |---|---|---|
> | water | linear viscous (Newtonian), turbulent at geomorphic scales | shear stress $\tau=\rho ghS$, bedload $\propto(\tau-\tau_c)^{3/2}$ ([[LS16 Fluvial Landscapes]]) |
> | air | linear viscous, strongly turbulent | threshold for grain entrainment, $q\propto u_*^3$ ([[LS19 Glacial and Aeolian Landforms]]) |
> | ice | power-law viscous, $\dot\varepsilon\propto\tau^n$, $n\approx3$ (Glen's law) | $u\propto H^{n+1}$, thin ice flows slowly ([[LS14 Glaciers Mass Balance and Ice Flow]]) |
> | mantle | linear viscous at geological times, $\eta\sim10^{21}$ Pa s | isostatic rebound ([[LS07 Isostasy]], [[LS15 Glacial Deposits Rebound and Sea Level]]) |
> | cold lithosphere | elastic, then brittle (friction, Coulomb) | flexure, faults, earthquakes ([[LS09 Faults and Earthquakes]], [[LS10 Folds Flexure and Mountain Building]]) |
> | regolith on a slope | flux $\propto$ slope (creep) until a threshold, then plastic failure | diffusion, landslides ([[LS12 Hillslope Transport and the Diffusion Equation]], [[LS13 Landslides]]) |


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


<!-- ls-depth:LS01:2 -->
> [!derivation] 🔵 Extra (my derivation): how fast does a landscape forget? Response time and the low-pass filter
> A landscape that is pushed away from its equilibrium form $z_{eq}$ relaxes back at a rate proportional to the distance (this is exactly what diffusion, stream-power incision or ice flow do to a small perturbation; see the response times in LS12, LS14, LS16):
> $$\frac{\mathrm dz}{\mathrm dt}=-\frac{z-z_{eq}(t)}{\tau}.$$
> **Step forcing.** If $z_{eq}$ jumps by $\Delta$ at $t=0$ then $z-z_{eq}$ decays as $e^{-t/\tau}$: after $\tau$ the adjustment is $63\,\%$ complete, after $3\tau$ it is $95\,\%$. **Periodic forcing** $z_{eq}=A\sin\omega t$: the steady response is $z=\dfrac{A}{\sqrt{1+\omega^2\tau^2}}\sin(\omega t-\phi)$ with $\phi=\arctan\omega\tau$. (*Proof:* try $z=B\sin(\omega t-\phi)$; $\omega\tau B\cos(\omega t-\phi)+B\sin(\omega t-\phi)=A\sin\omega t$; write $\sin\omega t=\sin\big((\omega t-\phi)+\phi\big)$ and match the $\sin(\omega t-\phi)$ and $\cos(\omega t-\phi)$ parts: $B=A\cos\phi$ and $\omega\tau B=A\sin\phi$, so $\tan\phi=\omega\tau$ and $B=A\cos\phi=A/\sqrt{1+\omega^2\tau^2}$.)
> *Meaning:* if the forcing is **slow** compared with the response ($\omega\tau\ll1$) the landscape tracks it (amplitude 1, no lag: *quasi-equilibrium*); if it is **fast** ($\omega\tau\gg1$) the landscape **averages it out**, amplitude falls as $1/\omega\tau$, and it lags by a quarter period.
> **Numbers** (`scripts/ls_depth_numbers.py`): a 100 m hillslope with $D=0.01\ \mathrm{m^2\,yr^{-1}}$ has $\tau=L^2/D=10^6$ yr, so the 41 kyr obliquity cycle is attenuated to **0.65 %** of its amplitude (phase lag 90°, i.e. about 10 kyr): the *form* of such a hillslope records the long-term uplift, not the ice-age climate cycles. A fast system ($\tau=10$ kyr) follows a 100 kyr cycle with **85 %** of the amplitude and a 9 kyr lag; an *alluvial* channel that adjusts its slope and width by moving sediment ($\tau\sim10^2$–$10^3$ yr) follows it essentially perfectly, whereas a *bedrock* river must cut down through rock and has $\tau\sim10^5$–$10^6$ yr (a knickpoint needs $\sim0.6$ Myr to travel 30 km up a 100 km² basin; computed in [[LS16 Fluvial Landscapes]]).

![[fig_ls01_magfreq_filter.png]]
*Figure LS01.2. Right: the low-pass-filter response above; the two dots are the worked cases (slow hillslope versus 41-kyr forcing; fast system versus 100-kyr forcing). Left: see the next section.*

> [!intuition] Three timescales to keep apart
> (i) the **forcing time** $T$ (how long the climate or tectonic input stays roughly constant), (ii) the **response time** $\tau$ of the landscape, and (iii) the **age** of the landscape. $\tau\ll T$: the landscape is in quasi-steady state *with respect to that forcing*; $\tau\gg T$: it is a long-term average; $\tau\sim T$: it is out of equilibrium and carries a *transient* signal (knickpoints, perched valleys, terraces: [[LS16 Fluvial Landscapes]]). Whether a mountain is "in steady state" is therefore never yes/no: it depends on *which process* and *which forcing*.

> [!key] 🟡 Extra · book: kinds of equilibrium (Huggett, after Chorley and Kennedy 1971)
> *Static* (nothing changes), *stable* (returns after a small kick), *unstable* (a small kick sends it to a new state), *metastable* (stable until a **threshold** is crossed), *steady-state* (fluctuates about a fixed mean), *thermodynamic* (maximum entropy: a mountain reduced to a plain), *dynamic* (fluctuations about a mean that trends in one direction), *dynamic metastable* (trending mean that jumps when thresholds are crossed). "$\partial_tz_s=0$" of eq. (1) is the **steady-state** case; Hack's "dynamic equilibrium" is a steady state *of the form* with mass passing through. Huggett warns the early dynamic-equilibrium idea "was open to question and difficult to apply", which is why the finer classification exists.


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


<!-- ls-depth:LS01:3 -->
> [!derivation] 🔵 Extra (my illustration): which events build a landscape? Magnitude, frequency and work
> Let events of size $q$ (a flood discharge, a rainstorm, an earthquake) occur with probability density $f(q)$, and let one event of size $q$ do work $W(q)$. The **total work** done by events of size near $q$ is $W(q)f(q)\,\mathrm dq$; the **effective** (formative) event is where this product peaks. Take a log-normal $f$ (median 1, $\sigma_{\ln q}=1$, a reasonable model for river peaks) and a transport law $W\propto q^b$ (for sediment transport $b\sim2$–3; with a threshold $W\propto(q-q_c)^b$). Then $q^bf(q)\,q$ (per unit $\ln q$) is again a Gaussian in $\ln q$ centred at $\ln q^*=b\sigma^2$, so
> $$q^*=e^{b\sigma^2}\times\text{median}:\qquad b=1:\ 2.7;\quad b=2:\ 7.4;\quad b=3:\ 20\ \text{times the median}$$
> (computed numerically: `scripts/ls_depth_numbers.py` reproduces $2.72$, $7.39$, $20.1$). **The steeper the transport law, the larger and rarer the formative event:** with $b=3$ about **74 %** of the total work comes from events more than ten times the median, with $b=1$ only **10 %**. If instead event sizes follow a power law (heavy tail) $P(Q>q)\propto q^{-\alpha}$, the integral $\int q^bf\,\mathrm dq$ converges at large $q$ only if $b<\alpha$: for $b\ge\alpha$ the **largest events dominate without limit**, which is the mathematical content of A&A's "neo-catastrophist" remark that single huge floods, tsunamis or impacts can write a signature that thousands to millions of years cannot erase. (The classic study is Wolman and Miller 1960, quoted from memory; A&A discuss the idea on p. 7 = PDF p. 25.)
> *Link:* heavy-tailed laws are the Pareto distribution of [[Pareto Distribution|Pareto]] and the extreme-value (Gumbel) distribution of [[Gumbel Distribution|Gumbel]] in the probability notes ([[Probability - Course Map]]); landslide sizes ([[LS13 Landslides]]) and earthquakes ([[LS09 Faults and Earthquakes]]) are the clearest geomorphic power laws.


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


<!-- ls-depth:LS01:4 -->
> [!question] Check yourself (answers below)
> 1. A rock column is uplifted at $U=1$ mm/yr while its surface is lowered by denudation at $\mathcal E=0.4$ mm/yr. What is the surface uplift rate and how long to build 1 km of relief if $U,\mathcal E$ stay fixed?
> 2. A glacier valley responds to climate with $\tau=2\times10^{3}$ yr. Is it in quasi-steady state with respect to a 41 kyr cycle? With respect to a 100-year warm spell?
> 3. In the master equation $\partial_tc=-\partial_xq+P$, what must $q$ and $P$ be for (a) a decaying isotope in a closed box, (b) heat conduction with no sources?
> 4. Why does a steeper transport law (larger $b$) push the formative event to rarer, larger events?
> 5. Name one landscape variable for which "steady state" is a good approximation and one for which it is not, and say why (use $\tau$).
> *Answers.* (1) $\partial_tz_s=0.6$ mm/yr; $1000\,\mathrm m/0.6\times10^{-3}\ \mathrm{m\,yr^{-1}}\approx1.7$ Myr. (2) Yes for the 41 kyr cycle ($\omega\tau=2\pi\cdot2000/41000\approx0.31$, amplitude $0.96$); no for 100 yr ($\omega\tau\approx126$, amplitude $0.008$: it ignores the spell). (3) (a) $q=0$, $P=-\lambda c$; (b) $q=-k\,\partial_xT$ (with $c\propto T$), $P=0$. (4) $W\propto q^b$ weights large events more; the peak of $q^bf$ moves to $\ln q^*=b\sigma^2$. (5) The slope of an *alluvial* channel ($\tau\sim10^2$–$10^3$ yr) is close to steady with respect to ice-age forcing; a *bedrock* river ($\sim0.6$ Myr), a 100 m hillslope ($\sim10^6$ yr) and an orogen ($10^6$–$10^7$ yr) are not.

> [!connection] Where else these ideas turn up in the vault
> - The **master equation** is the continuity equation of [[Thermodynamics - Course Map]] (heat), [[Waves - Course Map]] (diffusion versus wave propagation) and [[Climate - Course Map]] (energy balance: $c\,\mathrm dT/\mathrm dt=$ in $-$ out, the same relaxation law as above with $\tau=c/\lambda$).
> - **Response time and forcing frequency** is the same filter as the ocean's thermal inertia in climate and the damped driven oscillator in [[QM06 The Oscillator Toolbox]] (resonance versus lag).
> - **Event size and frequency** is the probability toolbox of [[Probability - Course Map]] (log-normal, Pareto, extremes).


## Map of this chapter
> [!connection] How LS01 connects
> **Previous:** [[Landscapes and Geomorphology - Course Map|Course Map]] · **Next:** [[LS02 Mechanics and Mathematics Toolkit]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

> [!connection] Fourier and Laplace view
> The response-time filter of this chapter is the transfer function $1/(1+\tau s)$ with one pole at $-1/\tau$: [[Fourier and Laplace Transforms]] §1, §7.5.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 1–24 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS01:5 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | principles of conservation, transport rules, event size and frequency; timing; what drives surface processes | [[geomorphology-the-mechanics-and-chemistry-of-landscapes-9780521519786-0521519780_compress.pdf#page=23|A&A ch. 1, PDF pp.23–26]] (read) | b · primary book |
> | types of equilibrium, Hack's steady state | [[Fundamentals of Geomorphology (Fundamentals of Physical Geography) - Second Edition (Richar Huggett) (z-library.sk, 1lib.sk, z-lib.sk).pdf#page=36|Huggett PDF p.36]] (read) | b · primary book |
> | history (Gilbert, Davis, Hack), Wolman and Miller 1960 | my recollection; A&A name Gilbert, Powell, Penck, Davis (PDF p.25) | not checked against a source |
> | master equation, response time and low-pass filter, effective-event calculation | my own derivations; numbers in `scripts/ls_depth_numbers.py`, figure `scripts/fig_ls_depth.py` | extra · beyond |
