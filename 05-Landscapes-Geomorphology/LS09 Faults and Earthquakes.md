---
title: LS09 Faults and Earthquakes
aliases: [LS09, Faults and Earthquakes]
subject: landscapes
type: chapter
chapter: 9
part: V
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS09 · Faults and Earthquakes

◀ [[LS08 Plate Tectonics Strain Stress and Convection]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS10 Folds Flexure and Mountain Building]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides 85–94 of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 5 sections, 5 derivation boxes, 4 redrawn figures and 6 slide images.

> [!key] After this chapter you can
> - classify normal, reverse and strike-slip faults by principal stresses (Anderson),
> - describe the earthquake cycle as stick–slip,
> - read InSAR and fault-topography figures,
> - tell the story of the Himalaya over four time scales.

> [!intuition] The one-sentence story
> Anderson's theory turns the stress state into a fault type; earthquakes are the stick–slip release of stored elastic strain, and the Himalaya records that cycle on four time scales.

```mermaid
flowchart LR
  A["principal stresses"] --> B["fault types (Anderson)"]
  B --> C["stick-slip: earthquake cycle"]
  C --> D["finite faults, InSAR"]
  D --> E["Himalaya: 4 time scales"]
```
*Concept map: every box is a section of this chapter.*

*[Slides 85–94]*


## Fault types and Anderson's theory (slide 85)


![[ls_fig18.png]]
*Figure LS09.1. Slide 85: the three fault types. Red: fault plane; blue: motion of the hanging wall (normal, reverse) or of each side (strike-slip, right-lateral).*


![[pre_085.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 85
> Top: a block on an inclined plane, the “fight between strength of rock (friction) and tectonic stress”: the weight component along the plane (magenta arrow, downhill) versus friction and applied stress (black arrow); the block slips when the driving shear exceeds the frictional resistance. Bottom: block diagrams of normal, reverse (thrust) and strike-slip faulting (Fig. above).


> [!derivation] 🔵 Extra (not derived in the slides): Coulomb failure and Anderson's fault angles
> Failure on a plane occurs when $\tau=C+f\sigma_n$ (slide 52). Using the Mohr circle of (16), at failure the circle of radius $\tfrac12(\sigma_1-\sigma_3)$ touches the straight line $\tau=C+\sigma_n\tan\phi$ ($f=\tan\phi$) at a single point; the radius from the centre to the tangent point is perpendicular to the line, so it makes angle $90^\circ+\phi$ with the $\sigma_n$ axis. That angle equals $2\theta$ in (16), hence the plane whose normal makes $\theta=45^\circ+\phi/2$ with $\sigma_1$ fails first; the plane itself makes
>
>
> $$
> \beta=\frac\pi2-\theta=45^\circ-\frac\phi2\quad\text{with }\sigma_1 .
> $$
>
>
> For $f=0.6$ ($\phi=31^\circ$): $\beta\approx30^\circ$. From the geometry of the circle, $\sin\phi=\dfrac{\tfrac12(\sigma_1-\sigma_3)}{\tfrac12(\sigma_1+\sigma_3)+C\cot\phi}$; for $C=0$: $\sigma_1/\sigma_3=(1+\sin\phi)/(1-\sin\phi)=3.1$ ($f=0.6$) or $4.7$ ($f=0.85$, Byerlee): the maximum stress ratio a fractured crust can sustain. **Anderson's theory**: the earth's surface is free, so it carries no shear traction and the vertical direction is a principal axis. Three cases: (i) $\sigma_1$ vertical $\Rightarrow$ the fault plane is $30^\circ$ from vertical, dip $60^\circ$: *normal fault*; (ii) $\sigma_3$ vertical $\Rightarrow$ plane $30^\circ$ from horizontal: *thrust* (low angle); (iii) $\sigma_2$ vertical $\Rightarrow$ vertical plane: *strike-slip*. Thrusts are thus low-angle, normal faults steep — as on slide 85 and the World Stress Map regimes of slide 70.


![[ls_fig19.png]]
*Figure LS09.2. Mohr circle touching the Coulomb envelope. Here $C=0.3$, $f=0.6$ (arbitrary stress units).*


## The earthquake cycle: stick–slip (slide 86)

> [!figure]- 🖼 Slide 86: open to see the slides this section explains
> ![[pre_086.jpg|300]]


![[ls_fig20.png]]
*Figure LS09.3. Slide 86 (T&S Fig. 8-18): slider-block model. A driver plate moves at constant speed $u_0$, stretching a spring $k$ attached to a block of mass $m$ on a frictional surface.*


> [!derivation] 🟢 In the slides: Slide 86: block–spring model of an earthquake cycle
> The driver moves at $u_0$; the spring force on the block is $F_k=k(u_0t-x)$. *Stick*: the block is at rest as long as $F_k<F_s$ (static friction). *Slip*: when $F_k=F_s$ at $t=t_s$ the block starts to move against the smaller dynamic friction $F_d<F_s$ (the essence: friction weakens once slip begins). Take the driver's advance during the rapid slip as negligible. Then $m\ddot x=k(u_0t_s-x)-F_d$. Let $x_e=u_0t_s-F_d/k$ be the position where spring and dynamic friction balance and $\xi=x-x_e$: $m\ddot\xi=-k\xi$. At the start $\xi(0)=x_s-x_e=-(F_s-F_d)/k$ (from $F_k=F_s$) and $\dot\xi(0)=0$, so
>
>
> $$
> \xi(t')=-\frac{F_s-F_d}{k}\cos(\omega t'),\qquad\omega=\sqrt{k/m}.
> $$
>
>
> The block stops (velocity zero) after half a period $\pi\sqrt{m/k}$ when $\xi=+(F_s-F_d)/k$. **Slip per event and stress drop**:
>
>
> $$
> \Delta=\frac{2(F_s-F_d)}k,\qquad\Delta F=k\Delta=2(F_s-F_d).
> $$
>
>
> After the slip the spring force is $F_s-2(F_s-F_d)=2F_d-F_s$. Then the driver recharges the spring at the constant rate $ku_0$ until $F_s$ is reached again, taking
>
>
> $$
> T=\frac\Delta{u_0}=\frac{2(F_s-F_d)}{ku_0}.
> $$
>
>
> The force history is a sawtooth (figure): slow linear loading (years to millennia) and sudden drops (seconds). *Long-term average slip rate* $=\Delta/T=u_0$: the driver speed — the plate velocity — however the details of $F_s,F_d,k$.


![[ls_fig21.png]]
*Figure LS09.4. Sawtooth force history of the slider block for $F_d=0.6F_s$.*


> [!example] 🧮 Worked example: San Andreas Fault (slides 87)
> Slide 87 (A&A Fig. 4.9): a stream channel crossing the fault has been offset right-laterally; an older, abandoned segment allows the long-term rate to be found: offset $D_1$ accumulated in time $T_1$ gives the slip rate $D_1/T_1$; at Wallace Creek $D_1=130$ m and $T_1=3800$ yr give $34 \mathrm{mm yr^{-1}}$. Slide 87 (Fig. 4.11): the palaeoseismic record at Pallett Creek, dated by well-preserved organic layers, shows $\sim12$ events (black bars: age ranges) in $\sim2000$ years, with the last being the 1857 Fort Tejon earthquake and an average recurrence interval of $145\pm8$ yr. Slip per event, from the model above ($\Delta=u_0T$): $34 \mathrm{mm yr^{-1}}\times145 \mathrm{yr}=4.9$ m, in line with the offsets of a few metres seen in large strike-slip earthquakes.


> [!derivation] 🔵 Extra (not derived in the slides): Seismic moment and moment magnitude
> The size of an earthquake is the *seismic moment* $M_0=\mu_r A \Delta$ (rigidity $\mu_r\approx3\times10^{10}$ Pa, ruptured area $A$, mean slip $\Delta$; units N m), a torque-like measure of the force couple. The moment magnitude is (Hanks and Kanamori's definition, quoted) $M_w=\tfrac23(\log_{10}M_0-9.1)$ with $M_0$ in N m: each unit of $M_w$ is a factor $10^{1.5}\approx32$ in $M_0$. Example: 1857 Fort Tejon: rupture $360$ km $\times$ $15$ km, $\Delta=4.9$ m: $M_0=3\times10^{10}\times5.4\times10^{9}\times4.9=7.9\times10^{20}$ N m, $M_w=7.9$ (the accepted value).


<!-- ls-depth:LS09:1 -->
> [!derivation] 🔵 Extra (computed): why the biggest earthquakes dominate everything (Gutenberg–Richter, moment, and the event-size argument of [[LS01 Landscapes as Physical Systems]])
> The seismic moment $M_0=\mu_rA\bar D$ and the moment magnitude are related by $M_w=\tfrac23(\log_{10}M_0-9.1)$ ($M_0$ in N m; i.e. $M_0=10^{1.5M_w+9.1}$): **each unit of magnitude is a factor $10^{1.5}=31.6$ in moment**, and a factor $\approx10^{1.5/2}$ in rupture length. The **Gutenberg–Richter law** says the *number* of earthquakes falls by a factor $10^b\approx10$ per unit magnitude ($b\approx1$). Combine:
> $$P(M_0>m)\propto m^{-2b/3}\qquad(\text{a power law with exponent }\alpha=2b/3\approx0.67<1),$$
> so the moment released per magnitude bin grows as $10^{(1.5-b)M_w}=10^{0.5M_w}$ for $b=1$: **most of the seismic moment is released by the largest events**, up to the cutoff set by the size of the fault (the finite thickness of the seismogenic layer, $\sim15$–$40$ km). In the language of LS01: the "transport law" $W\propto q^1$ has $b_{LS01}=1>\alpha=0.67$, so the work integral is dominated by the upper end. *Numbers* (`scripts/ls_depth_numbers.py`): an $M_w8$ earthquake ($M_0=1.3\times10^{21}$ N m) releases $1000\times$ the moment of an $M_w6$ one; with $b=1$ there are $100$ times as many $M_w6$ as $M_w8$ events, so the $M_w8$ class still releases about $1000/100=10$ times the *total* moment of the $M_w6$ class. A Gorkha-type event ($M_w7.8$: $M_0=6.3\times10^{20}$ N m) over a $150\times100$ km rupture with $\mu_r=3\times10^{10}$ Pa implies a mean slip of $1.4$ m (the actual average slip was larger because the rupture was smaller; the point is the order of magnitude).
> **Consequence for landscapes:** deformation of the surface (uplift of terraces, landslide triggering, [[LS13 Landslides]]) is controlled by rare great earthquakes, exactly the "neo-catastrophist" point of A&A ch. 1.

> [!question] Check yourself (answers below)
> 1. What is $M_0$ for $M_w=7$? By what factor does the energy/moment increase from $M_w6$ to $M_w8$?
> 2. A fault $100$ km long and $15$ km deep slips $2$ m with $\mu_r=3\times10^{10}$ Pa. What is $M_w$?
> 3. In the Gutenberg–Richter law with $b=1$, how many $M_w5$ events happen for each $M_w7$?
> 4. Why does stress on a plane resolved from principal stresses obey the same Mohr circle used for landslides?
> *Answers.* (1) $M_0=10^{1.5\times7+9.1}=3.98\times10^{19}$ N m; two units: $31.6^2=1000$. (2) $M_0=3\times10^{10}\times(10^5\times1.5\times10^4)\times2=9\times10^{19}$; $M_w=\tfrac23(\log_{10}9\times10^{19}-9.1)=\tfrac23(19.95-9.1)=7.23$. (3) $10^{2}=100$. (4) Both are Coulomb failure of a plane under $\sigma_n,\tau$ ([[LS02 Mechanics and Mathematics Toolkit]]).

> [!connection] Where else this appears
> - **Power laws and heavy tails:** [[Pareto]] and [[Gumbel]] in [[Probability - Course Map]]; the Poisson process of earthquake occurrence is [[Poisson Distribution]].
> - **Periodic loading and the elastic cycle:** the stick-slip oscillation of a spring-block model is a relaxation oscillator: [[Fourier and Laplace Transforms]] §7.5; [[LS02 Mechanics and Mathematics Toolkit]] (Maxwell time and post-seismic relaxation).
> - **Symmetry of the stress tensor** (torque balance) is why only 6 of its 9 components are independent: [[GT10 Symmetry Representations and Characters]] (rank-2 tensors under rotations).


## Finite faults, topography and InSAR (slides 87–88)


![[pre_088.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 88: vertical displacement patterns of finite faults (A&A Figs. 4.2, 4.8)
> Top: for a dip-slip fault (normal fault dipping $60^\circ$) the surface is uplifted on the footwall side and down-dropped on the hanging-wall side (profile with a sign change at the fault trace, amplitude cm); centre: the map of the vertical displacement field, a pair of lobes (red up, blue down) closing at the two ends of the fault where slip tapers to zero. The two lobed diagrams on the right plot further components of the displacement field around the fault (see the A&A figure caption), again alternating in sign. The message written on the slide: *faults are finite in size, so a transform fault can create topography*: the quadrants around the tips are alternately uplifted and depressed, so repeated events build ridges and depressions even though the average slip is horizontal.


> [!derivation] 🔵 Extra (not derived in the slides): InSAR: why one colour cycle is $\lambda/2$
> A radar satellite measures the phase of the reflected wave: a path of length $2r$ (there and back) gives phase $\varphi=4\pi r/\lambda$ (radians). Between two passes, ground motion towards the satellite by $\Delta r$ (along the line of sight) changes the phase by $\Delta\varphi=4\pi\Delta r/\lambda$. The interferogram shows $\Delta\varphi$ modulo $2\pi$ as colour cycles (“fringes”); one full cycle corresponds to $\Delta r=\lambda/2$. For C-band radar $\lambda=5.6$ cm, so one fringe is $28$ mm (the scale on slide 88, “28 mm”). Counting the fringes from the far field to the fault gives the surface displacement in the line of sight, e.g. $\sim35$ fringes = $\sim1$ m. The slide's fringe map (coordinates $34^\circ$–$35.5^\circ$N, $242.5^\circ$–$243.5^\circ$E; the Mojave region of California) shows concentric bands ending at the ruptured faults.


## Normal faults and rifts; thrust faults (slides 89, 91)


![[pre_089.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 89: the East African Rift and normal-fault growth
> Left: Google-Earth view of the Horn of Africa (Red Sea, Gulf of Aden, Afar, East African Rift). Middle: block diagram: normal faulting, extension, hanging wall drops relative to footwall, forming a scarp and a basin (lake). Right (A&A Fig. 4.5, after Cowie 1998): (a) many small fault segments each with an elliptical slip profile; (b) growth enhances slip in overlap zones; (c) linkage: a few large faults take all the slip and abandon the others. An observed empirical result (quoted): the maximum slip $d$ scales with fault length $L$ as $d\approx\gamma L$, $\gamma\sim10^{-2}$–$10^{-1}$.


**Thrust faults** (slide 91): compression makes the hanging wall move *up* relative to the footwall (a low-angle reverse fault, Fig. above). The Himalaya is the largest example, treated next.


## The Himalaya over four time scales (slides 91–94)


![[pre_091.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 91: map and section
> The map (Wikipedia) divides the Himalaya into E–W belts: **Lesser Himalaya** (yellow), the **High Himalayan Crystalline Sequence** (orange), the **Tethys Himalaya** (blue), the Indus–Yarlung **suture zone**/ophiolites (green), the **Trans-Himalaya** batholith (red), and **leucogranites** (black), with the **Main Central Thrust (MCT)** and **Main Boundary Thrust (MBT)**. The cross-section (A&A) at the bottom shows India (dark arrow) underthrusting beneath Tibet along the **Main Himalayan Thrust**; a stack of thrusts developed in sequence, each step towards the south (foreland): **MCT** $\sim23$–$12$ Ma, **MBT** $\sim11$–$5$ Ma, **Main Frontal Thrust (MFT)** $\sim2$ Ma to present. Depth axis: $0$ to $-100$ km (Moho at $\sim70$ km beneath Himalaya).


> [!derivation] 🔵 Extra (not derived in the slides): From terrace ages to uplift and fault slip
> Slide 92 shows the recent Himalayan uplift ($10^{3}$–$10^{4}$ yr) recorded by river terraces of the Sutlej (labels T1, T2, T3, T4, T6; ages $2.2$, $6.1$, $9.1$ ka on the plot). A river cuts a strath, is then lifted and incises a new one: the height $H_t$ of a terrace above the modern riverbed divided by its age $t$ is the rock-uplift rate if the river's own incision keeps pace with uplift: $u=H_t/t$. Example: $H_t=22$ m at $2.2$ ka: $u=10 \mathrm{mm yr^{-1}}$, the peak of the uplift-rate profile (panel b, $\sim10$ mm yr$^{-1}$ at $\sim5$–$10$ km north of the MFT). Panel (c): a rigid hanging wall moving up a ramp of dip $\theta$ at slip rate $d$ rises at $u=d\sin\theta$ and shifts horizontally at $d\cos\theta$. With $d=21.5$ mm yr$^{-1}$ (convergence absorbed by the MFT, slide) and $u=10$ mm yr$^{-1}$: $\sin\theta=0.47$, $\theta=28^\circ$, just the dip predicted by Anderson theory for a thrust.


![[pre_093.jpg|460]]


> [!example] 🖼 Reading the diagram: Slide 93: the seismic cycle in the Himalaya (Gorkha 2015, $10^{0}$–$10^{2}$ yr)
> The upper panel of (a) tabulates behaviours along the section from the Gangetic plain (S) to Tibet (N); (b) plots against distance from the MFT (km): the topography (grey), long-term net structural uplift rate (blue steps), interseismic uplift rate from InSAR (thin blue), denudation rate (purple: high at the front), co-seismic (red: Gorkha, slip $\sim$ metres, uplift over the rupture and subsidence to the north) and post-seismic movement, and the “interseismic locking line” at $\sim100$ km. Between the locking line and the MFT the fault is locked and stores strain (surface goes up slowly, like the block–spring model between events); north of it the fault creeps continuously. In the earthquake the locked patch slips, uplifting the region above it. Over many cycles the net uplift is $\sum$ interseismic $+\sum$ coseismic movements, which must equal the long-term uplift pattern.


> [!example] ❓ Question on the slides: Slide 94: pending mega-earthquakes? “aseismic creep”?
> Great earthquakes recur where strain has accumulated. If plate convergence $V_c\approx20$ mm yr$^{-1}$ is accommodated on a fault segment that has not ruptured for $T_\mathrm{elapsed}$ years, the slip deficit is $D_\mathrm{def}=\chi V_cT_\mathrm{elapsed}$ where $\chi\le1$ is the fraction of convergence stored elastically (seismic coupling). A&A Fig. 4.21 shows for the Himalayan arc, coloured yellow, the “slip potential” (m) of segments from Kabul to Bhutan with the maximum magnitude ($7.6$–$8.6$) each could produce, together with historical events (1505, 1555, 1803, 1833, 1905, 1934, 1950) and the population centres at risk. Example: a segment $200\times100$ km unbroken for $500$ yr at $\chi=1$: $D_\mathrm{def}=0.02\times500=10$ m, $M_0=3\times10^{10}\times2\times10^{10}\times10=6\times10^{21}$ N m, $M_w=8.4$. If part of the convergence is taken up by *aseismic creep* or by many small earthquakes, $\chi<1$ and the potential is smaller ($\chi=0.5$ gives $M_w=8.2$); geodetic data show the Himalayan front is largely locked ($\chi\approx1$) up-dip of the locking line, creeping below — the “(?)” on the slide is the question of how much is in fact unlocked.

## Further slides explained one by one
<span class="scope-taught">taught</span> *the slides of this chapter's range that carry no derivation of their own; each image is followed by what it shows*

![[pre_087.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 87: Strike-slip faults and the San Andreas record (Anderson & Anderson)
> *Left:* a block diagram of a right-lateral strike-slip (transform) fault with the National Park Service explanation; centre-top a hillshade of a fault trace with offset streams; *centre:* Fig. 4.11 (Wallace Creek): a stream channel is offset by successive earthquakes, so the total offset divided by the age of the channel gives the long-term slip rate $D/T_1$; *right:* the palaeoseismic record of the San Andreas fault (dates of past earthquakes against number of earthquakes before the 1857 Fort Tejon event) with an average recurrence interval of order 150 years.

![[pre_092.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 92: Uplift in the Himalaya over $10^2$–$10^4$ years
> *Left:* river terraces (labelled T2–T6) along a Himalayan river, each a former river bed abandoned as the river incised into rising ground; *right:* (a) terrace elevation against distance from the Main Frontal Thrust (MFT), (b) the inferred uplift rate in mm/yr against distance, peaking where the active fold crests, (c) the cross-section of the frontal fold above the thrust ramp with a convergence rate of about 21.5 mm/yr taken up by the thrust (A&A Fig. 4.26).

![[pre_094.jpg|520]]

> [!example] 🖼 Reading the diagram: Slide 94: Himalayan great earthquakes and 'aseismic creep'
> A map of the Himalayan arc (A&A Fig. 4.21) with the rupture segments of historical great earthquakes drawn as yellow strips with magnitudes (8.0–8.6) and years (1505, 1803, 1833, 1897, 1905, 1934, 1950...), cities as circles scaled by population (Kabul, Islamabad, Delhi, Dhaka, Kolkata, Bhuj). The title question asks whether the gaps between ruptures are 'aseismic creep' or locked segments that will break (a seismic hazard for tens of millions of people).


## Map of this chapter
> [!connection] How LS09 connects
> **Previous:** [[LS08 Plate Tectonics Strain Stress and Convection]] · **Next:** [[LS10 Folds Flexure and Mountain Building]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides 85–94 (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS09:2 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | moment magnitude relation, Gutenberg–Richter, moment per magnitude, power-law exponent $2b/3$, Gorkha-type slip estimate | standard seismology (formulas recalled, not read from a page in the repository); arithmetic in `scripts/ls_depth_numbers.py` (`LS09`) | extra · beyond, `[verify]` constants |
> | event size and frequency argument | A&A ch. 1 (PDF p.25), via [[LS01 Landscapes as Physical Systems]] | b · primary book |

## Continued in the vault (added 2026-10-29)
- Fault scarps and bedrock rivers as recorders of slip: [[LS23 Bedrock Channels and River Incision]] (steepness $k_s\propto U^{1/n}$), and cosmogenic scarp dating: [[LSX1 Clocks in Rocks]].
