---
title: LS17 Aeolian Landscapes
aliases: [LS17, Aeolian Landscapes]
subject: landscapes
type: chapter
chapter: 17
part: IX
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS17 · Aeolian Landscapes

◀ [[LS16 Fluvial Landscapes]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS99 Landscapes Practice Problems]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides (post-midsem; see also l_glacial_aolian.pdf) of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 2 sections, 4 derivation boxes, 0 redrawn figures and 0 slide images.

> [!key] After this chapter you can
> - derive the threshold for saltation and the sand flux,
> - classify dune morphologies by wind regime,
> - compute dune migration rate.

> [!intuition] The one-sentence story
> Wind moves sand in hops (saltation) above a threshold shear velocity, and the resulting dunes migrate with a speed inversely proportional to their height.

```mermaid
flowchart LR
  A["threshold shear velocity"] --> B["saltation, sand flux"]
  B --> C["dune morphology"]
  C --> D["dune migration"]
```
*Concept map: every box is a section of this chapter.*

## Saltation: how wind moves sand


> [!key] Definition: Modes of aeolian transport
> *Suspension*: very fine particles (dust, $\lesssim60 \mu$m) kept aloft by turbulence, travel far. *Saltation*: sand grains ($\sim0.1$–$1$ mm) bounce in short hops, the dominant mode for sand. *Creep (surface creep)*: coarser grains rolled and pushed along the surface by saltation impacts, too heavy to hop.


> [!derivation] 🔵 Extra (not derived in the slides): DERIVATION (SYLLABUS): threshold wind shear velocity for saltation (Bagnold)
> As for water (Shields, above), a grain on the bed is lifted/dragged into motion when the wind shear stress $\tau=\rho_au_*^2$ ($\rho_a$: air density, $u_*$: friction velocity) exceeds a threshold set by its submerged (here, simply its) weight and the aerodynamic lift/drag coefficients:
>
>
> $$
> \tau_{tc}\sim(\rho_s-\rho_a)gD \Longrightarrow u_{*t}=A_B\sqrt{\frac{(\rho_s-\rho_a)gD}{\rho_a}}
> $$
>
>
> with $A_B\approx0.1$–$0.12$ an empirical coefficient (Bagnold, quoted). For quartz sand ($\rho_s=2650$, $D=250 \mu$m) in air ($\rho_a=1.2$): $u_{*t}=0.1\sqrt{2649\times9.8\times2.5\times10^{-4}/1.2}=0.1\sqrt{5.4}=0.23 \mathrm{m s^{-1}}$, corresponding (via the logarithmic wind profile) to a $10$-m wind speed of order $5$–$6$ m s$^{-1}$: a stiff breeze. $u_{*t}\propto\sqrt D$: coarser sand needs a stronger wind, exactly as for water, but the density ratio $(\rho_s-\rho_a)/\rho_a\approx2200$ is far larger than $(\rho_s-\rho_w)/\rho_w\approx1.65$ for water, so wind needs much higher shear velocities than water to move the same grain.


> [!derivation] 🔵 Extra (not derived in the slides): The saltation trajectory and the “splash” feedback (EXTRA)
> A grain lifted from the bed accelerates in the wind (drag $\propto u_*^2$) along a low, flat trajectory (typical hop length $\sim10$–$100\times$ hop height, hop height of order cm, length of order tens of cm at threshold winds, growing with $u_*$), then strikes the bed and splashes several new grains into motion (a chain reaction analogous to the rain-splash cascade of Chapter 12, but here amplified by the wind rather than damped): once saltation starts it is sustained at winds *below* the threshold needed to *initiate* it (a lower “impact threshold” than the “fluid threshold” above), giving aeolian transport hysteresis.


> [!example] 🧮 Worked example: Sand flux (Bagnold's formula, quoted)
> $$
> Q_s=C_B\sqrt{\frac{D}{D_{ref}}} \frac{\rho_a}{g} u_*^3
> $$
>
>
> ($C_B\approx1.5$–$2.8$ depending on sorting, $D_{ref}=250 \mu$m): flux grows as the *cube* of the shear velocity (cf. stream power $\propto u^3$-type scalings in Chapter 16 and rain-splash energy $\propto v^2$ in Chapter 12 — transport rates generically scale steeply with the driving agent's speed once a threshold is exceeded). Doubling the wind speed above threshold increases sand transport roughly eight-fold.


<!-- ls-depth:LS17:1 -->
> [!derivation] 🔵 Extra (computed): why sand saltates and dust floats, in one number (Stokes settling and the Rouse number)
> A grain falls through air at its **settling velocity** $w$; A&A give two limits (PDF pp.332–333): for low Reynolds number the drag coefficient is $24/Re$, giving Stokes' law
> $$w=\frac{(\rho_s-\rho)gD^2}{18\mu},\qquad Re=\frac{\rho wD}{\mu}\ll1.$$
> For quartz in air ($\mu=1.8\times10^{-5}$ Pa s): $D=5\ \mu$m: $w=2$ mm/s; **$20\ \mu$m: $3.2$ cm/s** ($Re=0.04$, Stokes valid); $63\ \mu$m: $0.32$ m/s ($Re=1.3$, Stokes beginning to fail); $100\ \mu$m: Stokes would give $0.80$ m/s ($Re=5$, so it overestimates; the true value is lower, recalled $\sim0.5$ m/s). Compare $w$ with the turbulent velocity scale, the **shear velocity** $u_*\sim0.3$ m/s in a strong wind: the **Rouse number** $P=w/(\kappa u_*)$ with $\kappa=0.41$ is $0.02$ for $5\ \mu$m, $0.26$ for $20\ \mu$m, $2.6$ for $63\ \mu$m and $6.5$ for $100\ \mu$m. **$P\ll1$: turbulence keeps the grain aloft (suspension, dust, travels thousands of km: the loess of A&A's introduction); $P\gg1$: gravity wins, the grain falls back after a hop (saltation, sand, dunes).** The size at which $P\sim1$ ($\sim50$ $\mu$m) is the observed boundary between loess/dust and sand deposits.
> *Link to LS19:* the entrainment threshold for $D\approx0.1$ mm is the minimum (the easiest grain to move) while $P>1$ already holds for it: the most mobile grains are the ones that saltate.


<!-- ls-depth:LS17:4 -->
> [!pitfall] ⚠ Cross-check against A&A: the transport-law constant (needs checking)
> A&A (ch. 14, [[geomorphology-the-mechanics-and-chemistry-of-landscapes-9780521519786-0521519780_compress.pdf#page=502|PDF p.484]], Eq. 14.18) write the eolian transport capacity as a **cubic law with a threshold**: $Q=C\,\dfrac{\rho_a}{g}\sqrt{\dfrac{D}{D_0}}\,(u_*-u_{*c})^3$, with $D_0=0.25$ mm and "a dimensional constant equal to **0.18** if all dimensions are in SI units" (the formula was read from a garbled text extraction: `[verify]` on the printed page). This vault (LS17 and [[LS19 Glacial and Aeolian Landforms]]) used **Bagnold's form** $q=C(\rho/g)\sqrt{d/D}\,u_*^3$ with the recalled constant $C=1.8$ and **no threshold subtracted**. For $u_*=0.5$ m/s and $u_{*c}\approx0.23$ m/s the A&A form gives $\approx4\times10^{-4}$ kg m⁻¹ s⁻¹, about **60 times smaller** than the $0.0275$ kg m⁻¹ s⁻¹ used for the dune speeds ($54$ m/yr for a 10 m dune would become $\sim1$ m/yr). **Both forms agree on the physics** (cubic, thresholded: "both effects enhance the importance of rare high fluid speeds", A&A) but they differ in the *prefactor*, and the dune speeds quoted in LS17/LS19 should be read as order-of-magnitude with the prefactor uncertain by $10$–$100\times$. Resolve by reading A&A p.466–468 (printed) and Bagnold (1941).
> **Other points from A&A worth knowing:** (i) **hysteresis** (PDF p.477): the shear velocity needed to *start* saltation is higher, by several tens of percent, than the one that *sustains* it (Bagnold's lower **impact threshold**); (ii) the saltation system takes **1–2 s** to reach steady transport after the wind rises and a *saltation cloud* needs **several metres** of fetch to reach full capacity (PDF p.484), so gusts of seconds matter; (iii) wind-tunnel laser measurements show **small grains (0.19 mm) are entrained at lower shear velocity than large (0.77 mm)** (Nickling 1988; PDF p.477), consistent with the $\sqrt{d}$ threshold of LS19.


## Dune morphology and migration


> [!example] 🖼 Reading the diagram: Dune types (EXTRA, standard classification)
> *Barchan*: crescentic, horns pointing downwind, isolated, unidirectional wind, limited sand supply. *Transverse*: long ridges perpendicular to a unidirectional wind, abundant sand (barchans coalescing). *Linear (seif)*: long straight ridges parallel to the resultant of two oblique wind directions. *Star*: pyramidal, multiple slip faces, multidirectional winds. *Parabolic*: U-shaped, arms pointing upwind, partly vegetated/anchored arms (opposite curvature to barchans).


> [!derivation] 🟢 In the slides: DERIVATION (SYLLABUS): dune migration speed from mass conservation
> Treat a 2-D dune of height $H$ and cross-sectional area $\Sigma\sim cH^2$ ($c\sim\mathcal{O}\!\left(1\right)$ shape factor: the dune's along-wind cross-section scales with $H^2$ because its length is proportional to its height for a given angle of repose). Sand is carried up the gentle windward face at the saturated flux $Q_s$ and avalanches down the steep (angle-of-repose) lee face; conservation of sand within the dune profile (identical structure to (3) applied to the whole dune, or directly: in time $\mathrm{d} t$ the dune advances by $\mathrm{d} x_d$ and this must accommodate the flux crossing the crest):
>
>
> $$
> Q_s \mathrm{d} t=H \mathrm{d} x_d\quad\Longrightarrow\quad\boxed{ \dfrac{\mathrm{d} x_d}{\mathrm{d} t}=\frac{Q_s}{H} }
> $$
>
>
> (the celebrated result, quoted from Bagnold 1941). **Smaller dunes migrate faster**: with $Q_s$ set by the wind alone (independent of dune size), $u_d\propto1/H$. *Numbers*: $Q_s=10 \mathrm{m^2 yr^{-1}}$ (per unit dune width; a modest sand flux), $H=5$ m: $u_d=2$ m yr$^{-1}$; a $H=0.5$ m ripple superimposed on the same dune migrates $20$ m yr$^{-1}$: small bedforms visibly move within a season, large dunes over years to decades – directly observable by comparing satellite images at different dates (cf. the Google-Earth exercises of Chapter 1).


> [!intuition] Why the migration law has this form
> The windward slope of a dune is far gentler than the lee slope, so essentially all the sand that saltates up and over the crest must be redeposited on the lee face; a dune migrates because, seen from a fixed point in space, the whole hill of sand is simply being disassembled from the windward side and reassembled, grain by grain, on the lee side, one hop's-width downwind at a time.


> [!derivation] 🔵 Extra (not derived in the slides): Exploring martian dunes (syllabus item 8, “exploring martian dunes”)
> Mars has an atmosphere $\sim1/100$th the density of Earth's ($\rho_a\approx0.02 \mathrm{kg m^{-3}}$), so the threshold formula above gives $u_{*t}\propto1/\sqrt{\rho_a}$: martian threshold shear velocities (and hence near-surface wind speeds) must be roughly an order of magnitude higher than on Earth to move similarly sized grains, which is why martian dunes were long thought inactive; repeat orbital imagery (e.g. HiRISE) has since shown many martian dunes *do* migrate measurably (metres per Earth year, generally slower than terrestrial dunes of the same size, consistent with rarer threshold-exceeding winds), directly testable with the same Google-Earth-type displacement measurement introduced in Chapter 1 (§1.7) applied to Mars orbital imagery instead.

<!-- ls-depth:LS17:2 -->
> [!example] Conservation of sand, Exner's equation, and the migration speed in numbers
> The sand mass balance $\rho_b\,\partial_tz=-\partial_xq$ (the master equation of [[LS01 Landscapes as Physical Systems]] with flux $q(u_*)$) gives, for a dune of height $H$ whose crest receives flux $q$ and advances by avalanching down the slip face, $c=q/(\rho_bH)$ ([[LS19 Glacial and Aeolian Landforms]] §6). With $\rho_b=1600$ kg/m³ and Bagnold's $q=0.0275\ \mathrm{kg\,m^{-1}s^{-1}}$ at $u_*=0.5$ m/s: $H=5$ m: **109 m/yr**; $10$ m: $54$ m/yr; $20$ m: $27$ m/yr (computed). *Small dunes outrun big ones; dunes of the same type can collide and merge.* The $q\propto u_*^3$ law means the **strongest few percent of winds move most of the sand**, so dune orientation records the *resultant* of strong-wind directions, not the mean wind.

> [!question] Check yourself (answers below)
> 1. Estimate the settling velocity of a 20 µm silt grain in air and its Rouse number at $u_*=0.5$ m/s.
> 2. Why does a dune of 40 m height advance slowly compared with a 4 m dune in the same wind?
> 3. Why do desert dunes have lee faces at about 30–34°?
> 4. Which grain sizes are lifted to altitude and carried across oceans?
> *Answers.* (1) $w=0.032$ m/s, $P=0.032/(0.41\times0.5)=0.16$: suspended. (2) $c\propto1/H$: ten times slower for the same flux. (3) That is the angle of repose of dry sand ($\tan34^\circ=0.67$), where avalanches occur. (4) Silt and clay, $\lesssim50$ µm, with $P\lesssim1$ (dust).

> [!connection] Where else this appears
> - **Stokes drag by dimensional analysis:** [[LS02 Mechanics and Mathematics Toolkit]] (Buckingham Π; Reynolds number).
> - **Dust and climate:** radiative effects of mineral aerosols and loess as a palaeoclimate archive: [[Climate - Course Map]].
> - **Ripples and bedform wavelengths** as a pattern-forming instability (a Fourier-mode growth problem): [[Fourier and Laplace Transforms]] (modes and dispersion).


## Map of this chapter
> [!connection] How LS17 connects
> **Previous:** [[LS16 Fluvial Landscapes]] · **Next:** [[LS99 Landscapes Practice Problems]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics and Statistical Mechanics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides (post-midsem; see also l_glacial_aolian.pdf) (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS17:3 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | low-$Re$ drag coefficient $24/Re$, settling velocities | A&A PDF pp.265, 332–333 (found by search) | b · primary book |
> | Stokes values, Rouse numbers, dune speeds | my computation (`scripts/ls_depth_numbers.py`, `LS17`); real settling velocity of 100 µm sand recalled, `[verify]` | extra · beyond |

## Continued in the vault (added 2026-10-29)
- The mechanics under the dunes (entrainment, saltation, the splash, $q\propto u_*^3$, dune speed $c=q/\rho_bh$) is in [[LS24 Sediment Transport Mechanics]] §4 and §7; [[Saltation]] and [[Shields Criterion]] are the concept notes.
