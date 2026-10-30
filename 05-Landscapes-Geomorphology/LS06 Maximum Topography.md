---
title: LS06 Maximum Topography
aliases: [LS06, Maximum Topography]
subject: landscapes
type: chapter
chapter: 6
part: III
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS06 · Maximum Topography

◀ [[LS05 Shape of Planets]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS07 Isostasy]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 52–55 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 3 sections, 3 derivation boxes, 1 redrawn figures and 3 slide images.

> [!key] After this chapter you can
> - state the strength of rock and its yield criterion,
> - derive an upper bound on mountain height,
> - explain friction-limited relief on small bodies.

> [!intuition] The one-sentence story
> A column of rock can only stand as tall as its strength allows; comparing strength with the weight of the column gives an upper bound on relief on Earth, Mars and small bodies.

```mermaid
flowchart LR
  A["rock strength"] --> B["weight of a column"]
  B --> C["upper bound on relief"]
  C --> D["small bodies: friction limit"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 52–55]*


## Strength of rock (slide 52)


> [!key] 🛠 Tool: Stress on an inclined plane; Mohr's circle
> Let a solid be loaded by principal (compressive) stresses $\sigma_1\ge\sigma_3$ along perpendicular axes $1,3$. Consider a plane whose normal makes angle $\theta$ with axis $1$: $\hat{\vect n}=(\cos\theta,\sin\theta)$ in the $(1,3)$ frame. The traction on it is $\vect t=(\sigma_1\cos\theta, \sigma_3\sin\theta)$ (each principal stress acts on the projected area). Its components along $\hat{\vect n}$ and along the plane, $\hat{\vect s}=(-\sin\theta,\cos\theta)$, are
>
>
> $$
> \sigma_n=\sigma_1\cos^2\theta+\sigma_3\sin^2\theta=\tfrac12(\sigma_1+\sigma_3)+\tfrac12(\sigma_1-\sigma_3)\cos2\theta,\qquad\tau=\tfrac12(\sigma_1-\sigma_3)\sin2\theta . \tag{16}
> $$
>
>
> Eliminating $2\theta$ gives the **Mohr circle**: $\big(\sigma_n-\tfrac12(\sigma_1+\sigma_3)\big)^2+\tau^2=\big(\tfrac12(\sigma_1-\sigma_3)\big)^2$, a circle of radius $\tfrac12(\sigma_1-\sigma_3)$ centred on the mean stress. The largest shear stress, at $\theta=45^\circ$, is $\tau_\mathrm{max}=\tfrac12(\sigma_1-\sigma_3)$.


> [!derivation] 🔵 Extra (not derived in the slides): Friction and cohesion: the strength law $\tau=fN+C$ (slide 52) and Byerlee's law
> *Friction*. Put a block on a plane and press it with normal force $N$. Amontons' law (empirical): the tangential force needed to start sliding is $F=fN$, with $f$ independent of area and of $N$; per unit area, $\tau=f\sigma_n$ ($f=\tan\phi$, $\phi$ the friction angle). *Cohesion* $C$ is the shear strength that remains at zero normal stress (bonded grains, cement). Together: $\tau=C+f\sigma_n$ (Coulomb). Slide 52's diagram: a block (blue) on a base (brown) with applied shear $\tau$ (arrow right), friction resistance $f\sigma$ (arrow left) and normal load $\sigma$ downward; sliding occurs when $\tau$ reaches $\tau_\mathrm{max}\approx0.85\sigma$. The plot (T&S Fig. 8.7, data of Byerlee 1977) shows the maximum shear stress at which many rock types (limestone, sandstones, granite, gabbro, quartz, \dots) slide, against normal stress up to $\sim100$ MPa: all points fall near one straight line of slope $\approx0.85$ — *Byerlee's law*, remarkable because the rock types differ. (At normal stress above $\sim200$ MPa the fit is $\tau\approx50+0.6 \sigma_n$ MPa; quoted.) Friction on *pre-existing fractures* therefore limits crustal stress; *intact* rock is stronger, with cohesion of order $10^8$ Pa.


![[pre_053.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 53 (left): Melosh Fig. 3.3 — stresses beneath a load
> A triangular ridge load (top, mountain shape) rests on an elastic half-space (grey). The nested closed curves are contours of the second invariant $\Sigma_2=\sqrt{\tfrac16[(\sigma_1-\sigma_2)^2+(\sigma_2-\sigma_3)^2+(\sigma_3-\sigma_1)^2]}$, a measure of how far the stress state is from hydrostatic (pure shear strength). They are concentric around a point *beneath the centre of the load at a depth comparable to its half-width*: failure starts there, not at the surface. Peak $\Sigma_2$ is a fraction $<0.5$ of the peak load pressure $\rho gh$, so taking $\tau_\mathrm{max}=\rho gh/2$ (below) is a conservative simplification.


<!-- ls-depth:LS06:1 -->
> [!intuition] Context: three different answers to "how high can a mountain be?"
> Everest stands 8.85 km above sea level; the Andes and Tibet hover near 4–6 km; the Moon's maximum relief is 8.7 km but Olympus Mons is 21 km. Different mechanisms cap relief in different places, and it is the *smallest* cap that wins:
> | Cap | Mechanism | Size | Where developed |
> |---|---|---|---|
> | **material strength** | the rock at the base of a tall block yields | $\Delta h\lesssim2\times10^8/\rho_cg$: Earth $7.6$ km, Venus $8.4$, Mars $18.6$, Moon $44$ | this chapter (slides 52–55) |
> | **isostasy** (not a cap but a *carrier*) | buoyancy of the crustal root carries most of the weight, so strength only has to support the topography *above the compensated level* | roots of $\sim5\times$ the elevation | [[LS07 Isostasy]] |
> | **glacial buzzsaw** | glaciers erode everything above the snowline | topography rarely exceeds snowline $+\,1.5$ km | [[LS19 Glacial and Aeolian Landforms]] slides 30–36 |
> | **plate-boundary shear force** | the stress that the subducting plate can transmit limits the supportable elevation | within $\pm10$–$20$ MPa of observed maximum elevations | [[LS19 Glacial and Aeolian Landforms]] slides 37–38 (Dielforder et al. 2020) |
> The slide-37/38 "open problem" ("reconcile the two approaches to global mountain height") is exactly this table: strength, climate and tectonic stress are three bounds on the same quantity, and the observed range of $\sim5$–$9$ km on Earth sits where several of them overlap.

> [!derivation] 🔵 Extra (computed): where does the slides' "$\sigma_y=2\times10^8$ Pa" come from? Byerlee friction at $\sim5.7$ km depth
> The Coulomb law with friction $\mu_s=0.6$ and hydrostatic pore pressure gives, at depth $z$ in a *compressional* (thrust) regime, a differential stress at failure $\sigma_1'-\sigma_3'=(R-1)\sigma_v'$ with $R=\sigma_1'/\sigma_3'=3.12$ and $\sigma_v'=(\rho-\rho_w)gz$ (derived in [[LS02 Mechanics and Mathematics Toolkit]]). Numbers from `scripts/ls_depth_numbers.py`:
> | depth | $\sigma_v'$ | compressional strength $(R-1)\sigma_v'$ | extensional strength $(1-1/R)\sigma_v'$ |
> |---|---|---|---|
> | 3 km | 50 MPa | 106 MPa | 34 MPa |
> | 5 km | 83 MPa | 177 MPa | 57 MPa |
> | 10 km | 167 MPa | 353 MPa | 113 MPa |
> | 15 km | 250 MPa | 530 MPa | 170 MPa |
> The compressional strength equals the slides' $2\times10^8$ Pa at **$z=5.7$ km**, a perfectly reasonable depth for the base of an upper-crustal block, which justifies the constant $\tau_y=10^8$ Pa (differential stress $2\tau_y$) as a *representative* upper-crustal value. **Two consequences:** (i) strength is not constant but *increases with depth* (confinement), so the bound (17) is a rough, order-one estimate; (ii) the **extensional strength at the same depth is only $64$ MPa, three times smaller**, so *extensional* regimes cannot support elevations as high as compressional ones. This is the mechanical reason why high plateaus such as Tibet start to extend (normal faulting) once their elevation reaches $\sim5$ km, and why mountain belts are generally in compression.


## Upper bound on relief (slide 53)


> [!derivation] 🟢 In the slides: Slide 53: $\Delta h_\mathrm{max}=\dfrac{3\times10^8}{\rho_cG(2\pi\bar\rho)}\dfrac1R$
> Consider an isolated block of height $\Delta h$ with crust density $\rho_c$ supported by rock below. At its base the vertical stress is $\sigma_1=\rho_cg \Delta h$ (weight per unit area), while the horizontal stress, since the flanks are free, is $\sigma_3\approx0$. By (16) the maximum shear stress is $\tau_\mathrm{max}=\tfrac12\sigma_1=\tfrac12\rho_cg \Delta h$. The rock can carry a shear stress at most $\tau_y\approx100$ MPa (the slide: “balancing rock strength and shear”). So $100 \mathrm{MPa}\approx\rho_cg \Delta h_\mathrm{max}/2$, i.e.
>
>
> $$
> \Delta h_\mathrm{max}=\frac{2\times10^{8}}{\rho_cg}=\frac{2\times10^8R^2}{\rho_cGM},\qquad g=\frac{GM}{R^2}.
> $$
>
>
> With $M=\tfrac43\pi\bar\rho R^3$, $g=\tfrac43\pi G\bar\rho R$, so
>
>
> $$
> \Delta h_\mathrm{max}=\frac{3\times10^8}{2\pi\,\rho_cG\bar\rho}\,\frac1R=\frac{3\tau_y}{2\pi G\rho_c\bar\rho\,R}. \tag{17}
> $$
>
>
> Bigger planets support *lower* mountains ($\Delta h_\mathrm{max}\propto1/g\propto1/R$ at fixed density) because gravity loads the rock more. The footnote on the slide: ambient (confining) pressure is about $100$ MPa at $3$ km depth ($\rho gz=2800\times9.8\times3000=82$ MPa) and the frictional term $f\sigma_n$ is ignored, i.e. the strength is taken as one number of order $10^8$ Pa; this simplification is the main source of $\mathcal{O}\!\left(1\right)$ errors.


> [!example] ❓ Question on the slides: Slide 53: $\Delta h_\mathrm{max}$ for the Earth?
> $\Delta h_\mathrm{max}=2\times10^8/(\rho_cg)$; with $\rho_c=2800$: $7.3$ km; with $2500$: $8.1$ km. Observed extremes relative to sea level: Everest $+8.85$ km, Challenger Deep $-10.9$ km. Same order of magnitude; the mismatch is the usual $\mathcal{O}\!\left(1\right)$ factor (isostatic compensation and roots reduce the load carried elastically; dynamic support by mantle flow; fluids weaken the crust).


| Body | $R$ (km) | $\bar\rho$ (kg m$^{-3}$) | my (17) ($\rho_c=2500$) | slide “estimated” | slide “observed” (km) |
|---|---|---|---|---|---|
| Mars | 3390 | 3933 | 21.5 | 21 | 21 |
| Venus | 6052 | 5243 | 9.0 | 8.9 | 9.7 |
| Mercury | 2440 | 5427 | 21.6 | 3.0 | 3.2 |
| Moon | 1737 | 3344 | 49.3 | 49 | 8.7 |

*Slide 54, with an independent recomputation using (17) and $\tau_y=10^8$ Pa. Mars, Venus and the Moon are reproduced; the Mercury estimate on the slide (3.0 km) is not (with Mercury's surface gravity about that of Mars the formula must give a value close to Mars's). Treat that entry with caution.*


![[pre_054.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 54: the table and Olympus Mons
> The table compares the largest topographic relief above/below the datum with the estimate (17). The two images show Olympus Mons (Mars) as a colour-coded elevation map and a shaded-relief view with a 500 km scale bar: the shield volcano rises $\sim21$ km above the datum, and has a scarp along its base — the fact that Mars's biggest mountain reaches the strength limit is why the estimate works. The **Moon is the orange outlier**: the estimate is $\sim5\times$ the observed value. The estimate is an *upper bound*, not a prediction: relief only reaches the bound if a process (volcanic construction on Mars; mountain building on Earth) can pile up rock until the strength is exhausted. Plausible reasons (the slide only flags the discrepancy): the Moon is geologically inactive, so nothing has piled up relief to the bound, and its crust is pervasively fractured by impacts, so its effective strength is frictional rather than that of intact rock.


## Small bodies: friction-limited relief (slide 55)


> [!derivation] 🟢 In the slides: Slide 55: $\Delta h/R\sim f$ for small bodies
> For small $R$ the bound (17) grows so large ($\Delta h_\mathrm{max}>R$ when $R\lesssim280$ km, from $R_\mathrm{crit}$ of §5.1 with $\sigma_y=10^8$) that bulk rock strength no longer limits anything (“for smaller bodies ($R\le10$ km) bulk rock strength is too high to matter”). The relief is then limited by *friction*: material simply slides down slopes steeper than the friction angle. Slide 55: with gravity $g$ small, $\Delta h\sim R$ and the load is borne by the body's centre, where the pressure is $\sim\rho gR$ and the frictional strength there is $\sim f\times\rho gR$. The load of a mountain of height $\Delta h$ is $\rho g \Delta h$. Setting load $\sim$ strength,
>
>
> $$
> \rho g \Delta h\sim f \rho gR\quad\Longrightarrow\quad\boxed{ \frac{\Delta h}{R}\sim f }
> $$
>
>
> independent of $g$, $\rho$ and size. With $f=\tan30^\circ=0.58$ (line $\phi=30^\circ$ in the figure), small bodies can have relief of order their radius (potato shapes). For large bodies, (17) gives $\Delta h/R=3\tau_y/(2\pi G\rho_c\bar\rho R^2)\propto1/R^2$ (the slide's “$\sim1/R^2$”). The two branches meet at $R_*=\sqrt{3\tau_y/(2\pi G\rho_c\bar\rho f)}\approx370$ km for $\tau_y=10^8$ Pa, $\rho_c=2500$, $\bar\rho=3500$ (the transition radius is larger for stronger rock).


![[ls_fig13.png]]
*Figure LS06.1. Schematic of Melosh §3.4.2 (slide 55) computed from (17) with $\rho_c=3000$, $\bar\rho=3000$, $f=0.58$: relief is capped by friction for small bodies and falls as $1/R^2$ for large ones. Observed relief of planets and moons follows such a curve with $\tau_y\sim10^{8}$ Pa.*


![[pre_055.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 55: the observed maximum-relief plot
> Vertical axis: (maximum $-$ minimum elevation)/mean radius, from $10^{-3}$ to $10$; horizontal axis: mean radius from $1$ to $10^{4}$ km. Filled and open circles are icy and rocky bodies. Small bodies ($R\lesssim20$ km) lie near $0.1$–$1$: friction-limited. Beyond a few hundred km the points fall as $1/R^{2}$, following the diagonal strength lines labelled $0.1$ MPa to $1$ GPa (the line labels are strengths); ice and rock bodies straddle different lines because ice is weaker. The nearly horizontal line at the top, labelled $\phi=30^\circ$, is the friction bound. The plot thus contains *both* regimes of the argument above in one figure.

<!-- ls-depth:LS06:2 -->
> [!example] 🔵 Extra (computed): bound (17) for the planets with the real surface gravity
> $\Delta h_{max}=2\times10^8/(\rho_cg)$ with $g$ the surface gravity: Earth ($9.81$, $\rho_c=2700$): **7.6 km**; Venus ($8.87$): **8.4 km**; Mars ($3.71$, $2900$): **18.6 km**; Mercury ($3.70$): **20 km**; Moon ($1.62$, $2800$): **44 km** (observed Mars $21$ km: the bound is reached; observed Moon $8.7$ km: it is *not*, because the Moon's large mountains are old, heavily degraded impact structures, not strength-limited volcanoes). **Lesson:** the bound is a *ceiling*, not a prediction: a body reaches it only if enough construction (volcanism, tectonics) has occurred and not too much degradation (erosion, impacts, viscous relaxation). Earth, with an active climate system, sits below the ceiling because of the **glacial and fluvial caps** of the table above.

> [!question] Check yourself (answers below)
> 1. Why does $\Delta h_{max}\propto1/R$ for a fixed mean density? What changes for a body twice as large?
> 2. At what depth does compressional frictional strength reach $3\times10^8$ Pa (take the numbers above)?
> 3. Why can a mountain be much higher than $\Delta h_{max}$ *if* it is supported isostatically, and what does the strength limit then apply to?
> 4. Why would a plateau at 5 km elevation tend to collapse by normal faulting?
> *Answers.* (1) $g\propto\bar\rho R$ so the load $\rho_cg\Delta h$ grows with $R$; a body twice as large has half the maximum relief. (2) $z=3\times10^8/[(R-1)(\rho-\rho_w)g]=3\times10^8/(2.119\times1700\times9.81)=8.5$ km. (3) Buoyancy of a root carries the weight; strength must support only the part of the topography that is not compensated (the load of a block relative to its isostatic position), so high-standing, thick-crust plateaus are possible. (4) At the depth where the load is carried, extensional strength is $\sim\tfrac13$ of compressional, so the same gravitational stress that the crust can resist in compression exceeds the extensional strength.

> [!connection] Where else these ideas appear
> - **Mohr–Coulomb failure and pore pressure** are derived in [[LS02 Mechanics and Mathematics Toolkit]]; the same $R=3.12$ sets Anderson's fault regimes in [[LS09 Faults and Earthquakes]] and the stability of slopes in [[LS13 Landslides]].
> - **Scaling $\Delta h\propto1/g$** is a dimensional argument (stress / weight per volume): [[LS02 Mechanics and Mathematics Toolkit]] (Buckingham Π).
> - **Gravitational potential energy and plate forces** also appear in [[Climate - Course Map]] only indirectly (the Himalaya and the monsoon, [[LS10 Folds Flexure and Mountain Building]]).


## Further slides explained one by one
<span class="scope-taught">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*

![[pre_052.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 52: Friction and cohesion: the strength of rock
> *Left:* a block of weight (normal stress $\sigma$) sliding on a surface under shear stress $\tau$; the resistance is friction $\mu\sigma$ plus cohesion $C$: $\tau=\mu N+C$. *Right:* Turcotte & Schubert Fig. 6.7 (Byerlee 1977): the maximum shear stress to start sliding against normal stress, for many rock types and pressures (log–log scatter): all points follow one line, $\tau_{\max}\approx0.85\,\sigma$: **Byerlee's law**, a universal friction coefficient $\mu\approx0.85$ (with a cohesion offset at high stress). It is the strength used for the maximum-topography estimate of this chapter.


## Map of this chapter
> [!connection] How LS06 connects
> **Previous:** [[LS05 Shape of Planets]] · **Next:** [[LS07 Isostasy]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics and Statistical Mechanics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 52–55 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS06:3 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | slide 37–38 (Dielforder et al. 2020) and buzzsaw numbers | [[LS19 Glacial and Aeolian Landforms]] (read from the slide images) | a · slides |
> | Coulomb strength with depth, $R=3.12$, planetary $\Delta h_{max}$ with real $g$, depth of $2\times10^8$ Pa | my own computation: `scripts/ls_depth_numbers.py` (`LS06`); $\mu_s=0.6$, hydrostatic pore pressure and $\rho_c=2700$ are assumed round values | extra · beyond |
> | surface gravities of Mars, Venus, Moon, Mercury | standard values recalled, not read from a page | not checked (`[verify]`) |
> | the Tibet/extension remark | general geology (England and Houseman style); not checked against a page | not checked (`[verify]`) |
