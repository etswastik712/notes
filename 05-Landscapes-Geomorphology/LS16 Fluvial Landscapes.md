---
title: LS16 Fluvial Landscapes
aliases: [LS16, Fluvial Landscapes]
subject: landscapes
type: chapter
chapter: 16
part: IX
scope: [taught, extra-book, extra-beyond]
by: [slides, ai-notes, book]
status: draft
tags: [subject/landscapes, type/chapter, taught, extra/book, extra/beyond, src/slides, src/ai-notes, src/book, status/draft]
---
# LS16 · Fluvial Landscapes

◀ [[LS15 Glacial Deposits Rebound and Sea Level]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[LS17 Aeolian Landscapes]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught**: slides (post-midsem; not in the pre-midsem slides) of [[pre_ms_landscape_26.pdf|the EC2123 pre-midsem deck]] (Argha Banerjee, IISER Pune; 153 slides). Boxes marked 🟢 **In the slides** derive what the slides derive; boxes marked 🖼 **Reading the diagram** explain each slide figure panel by panel and sit directly under the slide image.
> 🔵 **Extra · beyond**: boxes marked 🔵 **Extra** complete derivations the slides only quote (from Anderson and Anderson, *Geomorphology: the Mechanics and Chemistry of Landscapes*, and Turcotte and Schubert, *Geodynamics*); 🛠 **Tool** boxes derive a mathematical tool from 12th-grade material; 🧮 **Worked example** boxes calibrate orders of magnitude.
> This chapter has 5 sections, 6 derivation boxes, 1 redrawn figures and 0 slide images.

> [!key] After this chapter you can
> - write the stream-power incision law and its steady-state profile,
> - explain knickpoint migration,
> - describe alluvial channel geometry and braiding,
> - define base level and grade.

> [!intuition] The one-sentence story
> Rivers incise bedrock at a rate set by drainage area and slope (stream power), reach a graded form in alluvium, and respond to base-level change by migrating knickpoints.

```mermaid
flowchart LR
  A["networks, discharge"] --> B["stream power: E = K A^m S^n"]
  B --> C["knickpoints, transients"]
  C --> D["alluvial channels, braiding"]
  D --> E["base level, grade"]
```
*Concept map: every box is a section of this chapter.*

## River networks and discharge


> [!key] Definition: Drainage basin, discharge, drainage density
> A *drainage basin* is the area draining to a point (Chapter 3, §3.4). *Discharge* $Q$ (m$^3$s$^{-1}$) is the volume of water crossing a channel cross-section per time. In a basin of area $A$ receiving precipitation $P$ (m yr$^{-1}$) with a fraction $r$ (runoff ratio) reaching the channel (the rest evaporating or infiltrating to deep groundwater), at steady state
>
>
> $$
> Q=rPA .
> $$
>
>
> *Drainage density* $D_d=$ total channel length / basin area (km$^{-1}$): high where rock is impermeable or rainfall intense (badlands, $D_d\sim10$–$100$ km$^{-1}$), low on permeable or vegetated terrain ($D_d\sim1$ km$^{-1}$).


> [!derivation] 🔵 Extra (not derived in the slides): Hack's law and basin geometry (EXTRA, empirical)
> Channel length $L$ and drainage area $A$ satisfy the empirical relation $L=cA^{h}$ with $h\approx0.6$ (quoted, Hack 1957). Since $A\sim L\times(\text{basin width})$, this implies basin width grows as $L^{1/h-1}=L^{0.67}$: basins are not self-similar but become relatively narrower as they lengthen.


## Stream power and bedrock incision


> [!derivation] 🟢 In the slides: DERIVATION (SYLLABUS): the stream-power incision law
> A channel of width $W$ carries discharge $Q$ at depth-averaged velocity $\bar u$ and slope $S=-\partial_xz$. The rate of loss of potential energy per unit channel length per time (the power available to do work on the bed and banks) is the weight flux times the drop in height per length:
>
>
> $$
> \Omega=\rho_wgQS\qquad[\mathrm{W m^{-1}}],\qquad\omega=\Omega/W=\rho_wgqS  [\mathrm{W m^{-2}}] (q=Q/W:\text{ discharge per width}).
> $$
>
>
> $\omega$ is the *stream power per unit bed area*. Bedrock incision (by plucking, abrasion with bedload tools, cavitation) is assumed proportional to the excess of $\omega$, or more commonly of shear stress, above a threshold; the simplest, most used closure (“stream-power law”, quoted, Howard and Kohl 1983) is
>
>
> $$
> \mathcal{E}=K\,A^{m}S^{n} \tag{30}
> $$
>
>
> using $Q\propto A$ (via $Q=rPA$) in place of $\omega$, with $K$ an erodibility coefficient (depends on rock strength, climate, sediment tools) and $m,n$ related to the basic physical exponents (for $\omega\propto Q S$ and $Q\propto A$: $m/n\approx0.5$ is commonly found and used, consistent with $Q\propto A^{1}$, hydraulic geometry $W\propto Q^{0.5}$, and $\omega\propto Q S/W\propto A^{0.5}S$).


> [!derivation] 🔵 Extra (not derived in the slides): Steady-state (equilibrium) river long-profile and channel concavity
> In steady state with uniform rock uplift $U$, erosion balances uplift, $\mathcal{E}=U$, so by (30), $KA^mS^n=U$, giving
>
>
> $$
> S=\Big(\frac UK\Big)^{1/n}A^{-m/n}\equiv k_sA^{-\theta},\qquad\theta=\frac mn\ \ (\text{the channel \emph{concavity} index}). \tag{31}
> $$
>
>
> This is the empirically ubiquitous “slope–area” scaling of bedrock rivers (log–log plots of channel slope against drainage area fall on straight lines of slope $-\theta$, $\theta\approx0.4$–$0.6$ typically). Since $-\mathrm{d} z/\mathrm{d} x=S=k_sA^{-\theta}$, and treating $A(x)$ as known from the network (often approximated as $A\propto x^{h}$, $h\approx1.5$–$2$ for a simple basin), the river profile is obtained by direct integration:
>
>
> $$
> z(x)=z(L)+\int_x^Lk_sA(x')^{-\theta} \mathrm{d} x' .
> $$
>
>
> For $A\propto x^{h}$: $z(x)-z(L)=\dfrac{k_s'}{1-h\theta}\big[L^{1-h\theta}-x^{1-h\theta}\big]$ (for $h\theta\ne1$): a concave-up profile (steep near the source where $A$ is small, gentle near the mouth where $A$ is large), matching the familiar shape of real rivers, steeper for larger $\theta$.


![[ls_fig32.png]]
*Figure LS16.1. Steady-state river long profiles from (31) with $A\propto x^{2}$: larger concavity $\theta$ gives a more strongly curved profile.*


> [!intuition] Reading the stream-power law
> Larger drainage area (more water) or steeper slope both erode bedrock faster; the balance $\mathcal{E}=U$ says a river channel steepens (locally) wherever uplift is faster or drainage area is smaller, exactly enough to supply the erosive power needed to keep up. This is the fluvial analogue of the hillslope diffusion balance $\kappa_hz”=-\mathcal E$ of Chapter 12: there, curvature balances erosion; here, slope (to a power) and area balance erosion.


<!-- ls-depth:LS16:1 -->
> [!intuition] Context: why the exponent ratio $m/n$ is the number to know
> A&A (ch. 13, [[geomorphology-the-mechanics-and-chemistry-of-landscapes-9780521519786-0521519780_compress.pdf#page=455|PDF p.455]]) call $\theta=m/n$ the **concavity index** "as it dictates the rapidity with which the slope changes as area increases". The *absolute* values of $m$ and $n$ matter for transient behaviour, but the steady-state slope–area relation involves only the ratio. Observed values $\theta\approx0.4$–$0.6$ are remarkably uniform across climates and rock types, which is why $\theta\approx0.5$ is the default.

> [!derivation] 🔵 Extra (computed): numbers for a bedrock river, and its response time
> Take $m=0.5$, $n=1$ (so $\theta=0.5$), uplift $U=0.5$ mm/yr and erodibility $K=5\times10^{-6}\ \mathrm{yr^{-1}}$ (with $A$ in m²). The steady-state slope $S=(U/K)A^{-\theta}=100\,A^{-0.5}$ gives
> | drainage area | $S$ | knickpoint celerity $c=KA^m$ |
> |---|---|---|
> | 1 km² | 0.100 | 5 km/Myr |
> | 100 km² | 0.010 | 50 km/Myr |
> | $10^4$ km² | 0.001 | 500 km/Myr |
> (`scripts/ls_depth_numbers.py`.) For $n=1$ the stream-power law is a **kinematic wave equation** $\partial_tz+KA^m\partial_xz=U$: a perturbation (a knickpoint) is carried upstream at speed $c=KA^m$, which grows with area, so *the lower, larger reaches adjust first and a signal takes longest to reach the headwaters*. With $c=0.05$ m/yr (100 km²) a knickpoint needs $L/c=30\ \mathrm{km}/0.05\ \mathrm{m\,yr^{-1}}=0.6$ Myr to travel 30 km. **This is the response time $\tau$ of a bedrock river: $10^5$–$10^6$ yr**, orders of magnitude slower than an alluvial channel. Hence bedrock rivers integrate tectonic and climatic forcing over $\gtrsim10^5$ yr and filter out ice-age cycles ($\omega\tau\gg1$, [[LS01 Landscapes as Physical Systems]]); this is why river profiles are good archives of *uplift history* but poor recorders of climate cycles.


## Knickpoints and transient response


> [!derivation] 🔵 Extra (not derived in the slides): DERIVATION (SYLLABUS): knickpoint migration as a kinematic wave
> Take $n=1$ in (30): $\mathcal{E}=KA^m (-\partial_xz)$. The elevation equation (with uplift $U$) is
>
>
> $$
> \partial_tz=U-KA^m (-\partial_xz)=U+KA(x)^m \partial_xz .
> $$
>
>
> This is a first-order wave equation (unlike hillslope diffusion, which is second order): a perturbation propagates *upstream* (toward decreasing $x$ if $x$ increases downstream, but the disturbance in $z$ moves up the channel, i.e. towards the source, since information travels against the flow direction along the channel network) at the local *celerity*
>
>
> $$
> c(x)=K A(x)^m .
> $$
>
>
> A sudden change in base level (a fault offset, a sea-level fall, a change in $K$ or $U$) launches a **knickpoint** — a step or slope break in the profile — that migrates upstream at speed $c(x)$, *without diffusing*: it stays sharp (advection, not diffusion, in contrast to the hillslope case). Since $c\propto A^m$ and $A$ typically decreases upstream, the knickpoint slows as it migrates into smaller tributaries, and can stall or split at tributary junctions. Travel time from the mouth to a point $x_0$: $t=\int_0^{x_0}\mathrm{d} x/c(x)$.


> [!example] 🧮 Worked example: Time for a knickpoint to cross a basin
> $A(x)=A_0(x/L)^{2}$ (headwater at $x=0$), $A_0=10^3$ km$^2$, $L=50$ km, $K=10^{-5} \mathrm{yr^{-1}}(\mathrm{km^2})^{-m}$, $m=0.5$: $c(x)=K A_0^{0.5}(x/L)$, so $t=\int_0^{x_0}\mathrm{d} x/[KA_0^{0.5}x/L]$ diverges logarithmically at $x=0$ (the knickpoint slows indefinitely approaching the divide) but the time to cross most of the basin, from $x=L$ to $x=0.1L$, is $t=\dfrac{L}{KA_0^{0.5}}\ln10\approx\dfrac{50}{10^{-5}\times31.6}\times2.3\approx3.6\times10^5$ yr: knickpoint retreat across a $50$ km basin takes hundreds of thousands of years for these parameters, setting the response time of bedrock landscapes to a base-level change (contrast with the diffusive hillslope response time $L^2/\kappa_h$ of Chapter 12, which grows as $L^2$ rather than $L$).


> [!example] 🖼 Reading the diagram: What a knickpoint looks like in the field
> A sharp convexity or waterfall in an otherwise smooth concave-up profile; upstream of it the channel is graded to an *old*, higher base level (relict landscape), downstream it is graded to the new, lower one. Their presence is the clearest field evidence that a landscape has not yet reached steady state.


## Alluvial rivers: bed and banks in equilibrium


> [!key] Definition: Bedrock versus alluvial channels
> A *bedrock* channel flows directly on rock (Ch. 16, §1–§4 above). An *alluvial* channel flows over its own sediment (alluvium); its slope and geometry adjust so that the channel can just transport the sediment supplied to it (“grade”), rather than being set by rock erodibility.


> [!derivation] 🔵 Extra (not derived in the slides): DERIVATION (SYLLABUS): threshold of sediment motion (Shields criterion)
> A grain of diameter $D$ and density $\rho_s$ resting on the bed is dislodged when the fluid drag exceeds a fraction of its submerged weight. Drag force $\sim C_d \rho_wu_*^2 D^2$ ($u_*=\sqrt{\tau_b/\rho_w}$, the shear velocity, with $\tau_b$ the bed shear stress); submerged weight $\sim(\rho_s-\rho_w)g D^3$. Motion begins when these are comparable:
>
>
> $$
> \tau_b\sim(\rho_s-\rho_w)gD\quad\Longrightarrow\quad\boxed{ \tau_*\equiv\frac{\tau_b}{(\rho_s-\rho_w)gD}\sim\tau_{*c} }
> $$
>
>
> the dimensionless *Shields number*; experiments give $\tau_{*c}\approx0.03$–$0.06$ for coarse, turbulent-flow conditions (quoted). With $\tau_b=\rho_wghS$ (depth $h$, slope $S$, wide-channel hydrostatic approximation), the critical condition becomes $\rho_wghS=\tau_{*c}(\rho_s-\rho_w)gD$, i.e. the depth (or discharge) needed to move a given grain size increases with $D$ and decreases with $S$: steep mountain streams move coarse gravel; low-gradient rivers carry only sand and finer.


| Channel pattern | Typical setting | Mechanism (qualitative) |
|---|---|---|
| Straight | confined, low sediment supply, cohesive banks | rare; banks resist migration |
| Meandering | single thread, moderate slope, cohesive banks, suspended-load dominated | helical secondary flow erodes the outer (cut) bank and deposits a point bar on the inner bank; the bend migrates and grows until cut off (oxbow) |
| Braided | steep, high sediment supply, erodible banks, variable discharge | repeated bar deposition and channel splitting; banks too weak to confine flow to one thread |
| Anastomosing | very low slope, stable vegetated banks | multiple stable interconnected channels around vegetated islands |

*River channel patterns (syllabus item 6: floodplains, meandering, braiding).*


> [!intuition] Why meanders migrate outward
> In a curved channel, water at the surface is flung outward by inertia (like a car on a curved road) and returns along the bed toward the inner bank: a helical (secondary) flow. This flow carries the fast surface water, and its erosive power, to the outer bank, and drops sediment carried along the bed at the inner bank (point bar). The bend erodes outward and migrates downstream, which is why meander belts widen over time and abandoned meanders (oxbow lakes) are left behind when a bend is cut off.


<!-- ls-depth:LS16:2 -->
> [!derivation] 🔵 Extra (computed): the Shields threshold in real units
> With $\tau_c=\tau_{*c}(\rho_s-\rho)gD$, $\tau_{*c}=0.045$, $\rho_s=2650$ (`scripts/ls_depth_numbers.py`):
> | grain size | $\tau_c$ | flow depth needed at $S=0.01$ | at $S=0.001$ |
> |---|---|---|---|
> | 2 mm (granule) | 1.5 Pa | 1.5 cm | 15 cm |
> | 20 mm (gravel) | 15 Pa | 15 cm | 1.5 m |
> | **50 mm** | 36 Pa | **37 cm** | 3.7 m |
> | 200 mm (cobble) | 146 Pa | 1.5 m | 15 m |
> The depth follows from $\tau=\rho_wghS=\tau_c$. *Reading it:* a mountain gravel stream (slope $0.01$) moves 50 mm cobbles once the flow is deeper than $\sim0.4$ m, which happens in a flood; a lowland river ($S=0.001$) needs $\sim4$ m, so large grains stay put except in extreme floods. The threshold is what makes the *effective* (formative) flow a moderately rare flood (the effective-discharge argument of [[LS01 Landscapes as Physical Systems]]).

> [!question] Check yourself (answers below)
> 1. With $m=0.5,n=1$, how does the steady-state slope change when the uplift rate quadruples?
> 2. A knickpoint is created at the outlet of a basin with $A=100$ km² and $c=0.05$ m/yr; when does it reach 15 km upstream?
> 3. At what depth does a 20 mm gravel start to move on a slope of 0.005?
> 4. Why does a bedrock river filter out 41 kyr cycles but an alluvial one does not?
> *Answers.* (1) $S\propto U^{1/n}$: quadruples (for $n=1$). (2) $15\ \mathrm{km}/0.05\ \mathrm{m\,yr^{-1}}=3\times10^5$ yr (the celerity increases downstream, so this is an upper bound for a uniform $c$). (3) $h=14.6/(9810\times0.005)=0.30$ m. (4) $\tau$ of $\sim10^6$ yr versus $10^3$ yr: with the transfer function $1/(1+i\omega\tau)$ the 41 kyr signal is attenuated by $\sim0.007$ for the bedrock river but passes unattenuated for the alluvial one.

> [!connection] Where else this appears
> - **Kinematic waves and characteristics** are first-order transport equations, solved by $x-ct$; in [[Fourier and Laplace Transforms]] §6.2 they are the non-dispersive limit $\omega=ck$.
> - **Power laws, Hack's law and drainage density:** [[LS03 Digital Elevation Models and Terrain Analysis]] (depth layer).
> - **Fluvial extra chapters (research papers):** [[Further Research - Landscapes Papers]] (braided-river modelling, secondary currents, flow at a river bend, building the Himalaya).


## Base level, knickpoints and long-term grade


> [!derivation] 🟢 In the slides: DERIVATION (SYLLABUS): equilibrium (graded) longitudinal profile of an alluvial river
> An alluvial channel adjusts its slope to transport, without net aggradation or degradation, the sediment load $Q_s$ supplied from upstream, given the water discharge $Q$. A minimal transport law (analogous to the stream-power incision law, but for *transport capacity* rather than *detachment)* is $Q_c=K_tQ^{m'}S^{n'}$ (transport capacity). Steady state (grade) requires $Q_s=Q_c$ everywhere: given $Q_s(x)$ and $Q(x)$ (both usually increasing downstream as tributaries join), the required slope is
>
>
> $$
> S(x)=\Big(\frac{Q_s(x)}{K_tQ(x)^{m'}}\Big)^{1/n'} .
> $$
>
>
> If $Q_s$ is roughly constant (no tributary sediment input) while $Q$ grows downstream (more tributaries), $S$ decreases downstream even without any change in $K_t$: this is the basic reason alluvial rivers, like bedrock ones, have concave-up long profiles. A change in $Q_s/Q$ (e.g. damming removes sediment supply downstream, or land-use change increases it) shifts the graded slope and drives a new phase of incision or aggradation until grade is re-established – the alluvial analogue of the knickpoint response above.

## Map of this chapter
> [!connection] How LS16 connects
> **Previous:** [[LS15 Glacial Deposits Rebound and Sea Level]] · **Next:** [[LS17 Aeolian Landscapes]].
> **Other subjects:** [[Climate - Course Map]] (weathering and the carbon cycle, glaciation, orographic rainfall), [[Thermodynamics and Statistical Mechanics - Course Map]] (heat conduction and diffusion), [[Evolution of Earth and Life - Course Map]] (plate tectonics and landscapes through geological time), [[Waves - Course Map]] (diffusion and wave equations).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | slide content, figures read panel by panel | [[pre_ms_landscape_26.pdf]] slides (post-midsem; not in the pre-midsem slides) (images embedded from the PDF, auto-cropped, `scripts/render_slides.py`) | taught |
> | derivations, worked examples, tool boxes, TikZ figures | the AI-written derivation-level notes [[Landscapes_and_Their_Evolution_notes.pdf]] (EC2123 notes; LaTeX source in `landscape-notes-tex-source.tar.gz`), converted with `scripts/tex2vault_ls.py`; cross-checked against Anderson and Anderson and Turcotte and Schubert as cited there | secondary + extra/book |
>
> **Notes.** (1) The text of this chapter is the AI-written reference notes' text, converted to the vault's callout style and equation numbering (chapter-local, so some cross-references read as "(label)"). (2) The slide images were checked against the notes' slide numbers for a sample of slides (e.g. 1–12, 109–120 match). Figure descriptions are the notes', and should be compared with the images beside them. (3) The `[!verify]` items of the notes' last front-matter section ("Two places where the slides need care") are in [[Landscapes Notation and Glossary]].

<!-- ls-depth:LS16:3 -->
> [!provenance]- Depth-layer sources (added 2026-10-28)
> | Topic | Source | Priority |
> |---|---|---|
> | concavity index $m/n$ | A&A PDF p.455 (found by search; the sentence read) | b · primary book |
> | slope–area numbers, kinematic-wave celerity, response time, Shields depths | my computation (`scripts/ls_depth_numbers.py`, `LS16`); $K$, $U$, $\tau_{*c}$ are illustrative values | extra · beyond |

## Continued in the vault (added 2026-10-29)
- Continued in [[LS21 River Hydraulics and Hydraulic Geometry]] (law of the wall, hydraulic geometry), [[LS22 Floods Planform and River Profiles]] (floods, braiding, meanders, alluvial profiles), [[LS23 Bedrock Channels and River Incision]] (the full stream-power treatment, the $\chi$ transform, the width problem) and [[LS24 Sediment Transport Mechanics]] (Shields, saltation, Rouse). Concept notes: [[Stream Power Law]], [[Knickpoint]], [[Base Level]], [[Shields Criterion]], [[Effective Discharge]].
