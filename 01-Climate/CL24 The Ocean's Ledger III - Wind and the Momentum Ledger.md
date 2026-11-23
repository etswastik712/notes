---
title: CL24 The Ocean's Ledger III - Wind and the Momentum Ledger
aliases: [CL24, momentum ledger, wind stress, Nansen, Ekman transport, Ekman spiral, Ekman pumping, coastal upwelling, equatorial upwelling, geostrophic flow, hills of water, gyres, garbage patch, Navier-Stokes in words, Joy O3, Joy O4]
subject: climate
type: chapter
chapter: 24
part: VI
scope: [taught, extra-book, extra-beyond]
by: [joy, book]
status: draft
prereq: ["[[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]]", "[[CL12 Rotating Frames and the Coriolis Force]]", "[[CL13 Horizontal Motion - Geostrophic Balance and Friction]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/joy, src/book, status/draft]
---
# CL24 · The Ocean's Ledger III: Wind and the Momentum Ledger

◀ [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] · [[Climate - Course Map|Course Map]] · ▶ CL25 (planned: the salt ledger)

<span class="scope-taught">taught · in syllabus (2026 Joy, O3 second half and O4)</span> <span class="scope-extra-book">extra · book (Stewart 2008, Hartmann 2016: passages read)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> **Primary source: Joy's slides**: the Week 2 deck frames 41–70 (O3, "The ponderous ocean: wind closes the momentum ledger") and the **O4 deck** ("Nansen's answer", 34 frames); PDFs with speaker notes are in `earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf/`. Then **readings read in this pass**: Stewart 2008 §9.2 (pp. 135–142) and §9.3–9.4 (pp. 143–147), and Hartmann 2016 §7.5.1 (pp. 216–219, OCR with garbled equations: only its words are used). Then the **O3 and O4 handouts**. Not read in this pass (cited only as Joy cites them): Stewart pp. 108–110 and 115–119 (momentum equation, viscosity, turbulence), Hartmann §7.4 (pp. 206–216), Stewart pp. 155–158 and 183–190, Hartmann pp. 219–221. Neena's 2025 treatment is [[CL19 Wind-Driven Ocean Circulation]]; CL24 adds Joy's **integration** argument for Ekman transport, Ekman pumping with its map and numbers, the force-balance logic for geostrophy, and the closing of the momentum ledger. 🔵 marks my recomputations (`scripts/fig_cl24.py`).

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 the heat-budget puzzle and the momentum ledger; §2 wind stress and the **ponderous** ocean; §3 **Nansen's question** and the free-body diagram; §4 the **equations of motion in words** (stress, turbulence, which terms matter); §5 **Ekman transport** by integrating over the layer; §6 the **spiral** and why Nansen saw 20–40°; §7 **Ekman pumping**, **coastal and equatorial upwelling**; §8 **hills of water** and **geostrophy**, gyres, boundary currents; §9 where the momentum finally goes; §10 the take-home question (the Arabian Sea)
>
> 🟡 **Extra · book** (passages actually read)
> - Stewart's measured Ekman transport (Chereskin and Roemmich), the six assumptions behind Ekman's theory, the Ralph–Niiler observations, San Francisco versus Norfolk, Drake Passage transport
>
> 🔵 **Extra · beyond** (my own)
> - recomputation of every Ekman, pumping, geostrophic and Reynolds-number figure; the numerical check that the spiral sums to exactly 90°; the idealised-wind pumping profile

> [!key] After this chapter you can
> - explain why a wind-driven layer moves **90° to the right of the wind** (northern hemisphere) by integrating the force balance over the stirred layer, and why the answer does **not** depend on the eddy viscosity,
> - compute **Ekman transport** $\tau/\rho f$ and **pumping** $w=\mathrm{curl}(\tau/\rho f)$ and their sizes (≈ 1 m² s⁻¹; ≈ 20 m per year),
> - say why cold water arrives at **coasts** and the **equator**, resolving the heat-budget puzzle of [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]],
> - explain why a **hill of water stays up** (geostrophy), why currents go **round** it, and why the fast flow hugs the **west** side,
> - say where the wind's momentum finally goes.

> [!intuition] The one-sentence story
> The wind pushes the ocean, but a turning Earth bends the answer: the whole stirred layer slides **sideways, 90° to the right** of the wind. Where that sideways flow spreads apart water must come **up**; where it piles up water goes **down**, builds a **1 m hill** in the subtropics, and flows **round** it, not down it.

![[fig_cl24_momentum.png]]
*A: an idealised zonal stress (trades and westerlies, zero at 30°; not data), the Ekman transport and the pumping it implies (masked near the equator where f → 0). B: Ekman's spiral for a constant eddy viscosity (wind to the north, depth below): surface current 45° right of the wind, current turning right and fading; the transport integral is exactly 90° to the right (🔵 numerical check). C: surface geostrophic speed $(g/f)\times$slope. Script: `scripts/fig_cl24.py`.*

## 1. The puzzle, and a new ledger
<span class="scope-taught">taught</span> *O4 deck frames 1–3; O4 handout §1; Week 2 deck frames 40–45*

The heat budget of [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §9 ended with two apparent contradictions: the **eastern equatorial Pacific gains heat fastest and is cold**, the **western boundary currents lose it fastest and are warm**. A slab that only stores heat cannot do that for decades: something must keep bringing **cold water** to the first place and **warm water** to the second. Water only moves if it is pushed, so the physicist's answer to the *heat* budget opens a new ledger, **momentum**, with its own three hats (accountant: the wind's stress goes in, where does it go? data scientist: maps of stress, sea height, currents; physicist: Coriolis and geostrophy). The atmosphere hands momentum to the surface below it ([[CL22 The Ocean's Ledger I - Accounting for Energy]] §4), and **over 70 % of that surface is water**.

**Wind stress on the ocean** (slide frames, 2011 reanalysis annual mean): the **trades push the water west, the westerlies east**, the strongest push is in the **Southern Ocean** (largest near 50°S); eastward and westward pushes nearly cancel globally and over long times but not at any one place (O3 handout §8).

## 2. The ocean is ponderous
<span class="scope-taught">taught</span> *Week 2 deck frames 54–55; O3 handout "Read this part"*

| | Air | Water |
|---|---|---|
| density | 1.2 kg m⁻³ | 1,025 kg m⁻³ (≈ **850×**; 🔵 854) |
| typical speed | 10 m s⁻¹ | 0.1 m s⁻¹ (boundary currents 1–2 m s⁻¹) |
| heat carried per m² of cross-section per K ($\rho c\,v$) | 1.2×10⁴ W m⁻² K⁻¹ | 4×10⁵ W m⁻² K⁻¹: **≈ 34×** (🔵 34) |

(Per m³ per K water holds ≈ 3,400× more heat than air: 🔵.) A typical stress $\tau=0.1$ N m⁻² on a 50 m layer gives $\tau/(\rho H)\approx2\times10^{-6}$ m s⁻² (🔵 1.95×10⁻⁶): unopposed it would reach 0.1 m s⁻¹ in **half a day** (🔵 14 h) and the wind speed in about **two months** (🔵 59 days). **It never gets there**: the Earth is turning.

## 3. Nansen's question and a free-body diagram
<span class="scope-taught">taught</span> *O4 deck frames 4–7; Week 2 frames 56–57; O4 handout §2* · <span class="scope-extra-book">extra · book</span> *Stewart §9.2 pp. 135–137*

On the *Fram* (1893–96) Nansen saw Arctic ice drift **20–40° to the right of the wind**. His own first move (Stewart p. 136, read): three forces on the ice, **wind $W$**, **friction $F$** (opposite its motion, otherwise it would move as fast as the wind), **Coriolis $C$** (perpendicular to the velocity), steady motion $W+F+C=0$. Friction and Coriolis are at right angles to each other (one points straight back along the velocity, the other perpendicular to it), so they cannot cancel each other; the wind must balance their sum. In the north Coriolis is to the right of the motion, so that sum points backwards and to the right, and the wind must point forwards and to the *left* of the motion. Said the other way round: the ice drifts to the **right of the wind**. The diagram gets the side right, but the angle depends on how strong friction is compared with Coriolis, which the diagram cannot say.

**Why the analogy misleads (Joy's argument).** The friction comes from the water under the ice, and what that water does is the thing we do not know: the diagram hands the problem down to the water. And the object is the wrong size: a floe a few metres thick rides on tens of metres of stirred water over thousands of kilometres; most of the mass that feels Coriolis is water. So go to larger scales: treat the ice as a **passive tracer** (Brownian pollen) marking what the top of the layer does. (Caveat on the slide: ice is not strictly passive, the wind pushes it directly and sea-ice models keep a force balance; the turning comes from the water beneath.) **Does rotation matter?** It needs the motion to last long enough: $1/f\approx3$ h at mid-latitudes (🔵 2.8 h), so Nansen's weeks-long drift feels it fully; a thrown ball does not. It is the size and duration of the motion that count.

## 4. The equations of motion, in words
<span class="scope-taught">taught</span> *O4 handout §3* (Joy: "you won't be examined on the full equations; what you need is the idea of each term")

Newton for a parcel (Stewart eq. 7.10, as Joy cites it): $D\mathbf v/Dt=-\tfrac1\rho\nabla p-2\boldsymbol\Omega\times\mathbf v+\mathbf g+\mathbf F$: acceleration = pressure-gradient force + Coriolis + gravity + friction (with friction this is the **Navier–Stokes** equation). Coriolis for horizontal motion is $f\times$speed with $f=2\Omega\sin\varphi\approx10^{-4}$ s⁻¹ at mid-latitudes, positive in the north, zero at the equator. Gravity is balanced by the vertical pressure gradient, so set it aside for horizontal flow.

**Stress.** A force per unit area (N m⁻²); pressure pushes perpendicular, a **shear stress** drags along a surface; the wind stress is typically **0.1 N m⁻²**. Stack the layers like a deck of cards: each thin layer is dragged forward by the layer above (stress $\tau_{top}$) and held back by the one below ($\tau_{bottom}$); the net force is the *difference*, so the friction per unit mass is
$$F=\frac1\rho\frac{\partial\tau}{\partial z}\qquad(\text{units: N m}^{-3}/\text{kg m}^{-3}=\text{m s}^{-2}).$$
**Molecules or eddies?** Molecular viscosity carries momentum only a few millimetres (Stewart §8.1, as Joy cites it): it cannot explain how the wind reaches 50 m down. **Turbulence** does: the Reynolds number $Re=UL/\nu$ (ν = 10⁻⁶ m² s⁻¹) is ≈ **10¹¹** for U = 0.1 m s⁻¹, L = 1,000 km (🔵 1×10¹¹); eddies carry fast water down and slow water up, acting like a much stronger **turbulent (Reynolds) stress**, still written $\tau$. The Ekman argument never needs to know how.

**Which terms matter depends on the scale.** The acceleration against Coriolis is $U/(fL)$ (**Rossby number**): 0.1/(10⁻⁴ × 10⁶) = **10⁻³** (🔵): for large slow motions the acceleration is negligible. Make three assumptions: **steady**, **large and smooth** (drop advection), **flat sea surface** for now (no pressure gradient). Then each thin layer has only Coriolis and the stress difference:
$$-fv=\frac1\rho\frac{\partial\tau^x}{\partial z},\qquad fu=\frac1\rho\frac{\partial\tau^y}{\partial z}\qquad(x\text{ east},\,y\text{ north},\,z\text{ up}).$$

## 5. The whole layer moves at right angles to the wind
<span class="scope-taught">taught</span> *O4 deck frames 8–13; O4 handout §3–4* · <span class="scope-extra-book">extra · book</span> *Stewart (9.24)–(9.27), p. 143; Hartmann pp. 216–218 (words)*

Each layer hands its problem to the one below, like the cards. **Stack all layers into one block**, from the surface to below the stirred layer ([[Mixed Layer]]): the internal drags cancel in pairs (Newton's third law) and $\int\partial\tau/\partial z\,dz$ leaves only the two ends, $\tau(\text{top})-\tau(\text{bottom})$: at the top the **wind stress**, at the bottom of the stirred layer the turbulence has died, $\tau\approx0$. With the **transport** $M_x=\int u\,dz$, $M_y=\int v\,dz$ (m² s⁻¹, i.e. m³ s⁻¹ through a strip one metre wide):
$$\boxed{M_y=-\frac{\tau^x}{\rho f},\qquad M_x=\frac{\tau^y}{\rho f}}$$
(Stewart (9.26a,b) with mass transport $\rho M$; Hartmann §7.5.1 says it in words: transport is "90° to the right of [the wind stress] in the Northern Hemisphere and 90° to the left in the Southern".) An eastward wind ($\tau^x>0$, $f>0$) gives $M_y<0$: **south**. The same result as a force balance on the **block**: only the wind stress and Coriolis act, they cancel only if opposite, so Coriolis must point upwind, i.e. the block moves 90° to the right. *For the ice two forces were not enough because the water under it drags on its underside; the block has nothing dragging on its underside (the stress has died out at its base), so wind and Coriolis alone must balance.*

**Robust.** The answer needs only the stress at the top, the fact that it dies out below, and $f$. It does not depend on eddy viscosity, breaking waves or convection: that is why Stewart calls the transport "much more robust" than the velocities in the layer (p. 143, read: fewer assumptions, "does not depend on knowing the distribution of velocity in the Ekman layer or the eddy viscosity").

**Size.** $\tau=0.1$ N m⁻², ρ = 1025, $f=10^{-4}$ (≈ 43°): $M=\tau/\rho f=$ **0.98 m² s⁻¹** (🔵), about 2 cm s⁻¹ over 50 m: small, but across a basin it adds up to millions of m³ s⁻¹.

**Measured** (Stewart p. 144, read): across **11°N in the Atlantic** Chereskin and Roemmich (1991) found **12.0 ± 5.5 Sv** northward from direct current profiling, **8.8 ± 1.9 Sv** from the winds measured at the time with $\tau/\rho f$, and **13.5 ± 0.3 Sv** from long-term mean winds: agreement within the errors.

## 6. Inside the layer: Ekman's spiral and Nansen's 20–40°
<span class="scope-taught">taught</span> *O4 deck frames 14–16* · <span class="scope-extra-book">extra · book</span> *Stewart §9.2 pp. 137–142, read*

Ekman (1905) assumed the simplest turbulence, a **constant eddy viscosity** $A_z$ with $\tau=\rho A_z\,\partial u/\partial z$, steady, homogeneous, deep water, $f$-plane. For a wind to the north the solution is (Stewart (9.9), $z$ positive up)
$$u=V_0e^{az}\cos(\pi/4+az),\quad v=V_0e^{az}\sin(\pi/4+az),\quad a=\sqrt{f/2A_z}.$$
- At the surface the current has speed $V_0$ and is **45° to the right of the wind** (left in the south); going down it **weakens exponentially and turns further right**: a spiral (figure B).
- The **Ekman depth** (where the current is opposite the surface current) is $D_E=\pi/a=\sqrt{2\pi^2A_z/f}$ (Stewart (9.15)); there the speed is $e^{-\pi}\approx4$ % of the surface's (🔵 0.043). Stewart's empirical $D_E=7.6\,U_{10}/\sqrt{\sin|\varphi|}$ gives **45–300 m** (🔵 75/150/299 m at 15°, 45/90/181 m at 45° for 5/10/20 m s⁻¹; Table 9.3). Ekman number at $D_E$: $E_z=1/2\pi^2\approx0.05$ (🔵), so friction is much smaller than Coriolis there.
- **Add up the arrows** (the area under the spiral, as vectors): exactly **90° to the right**, whatever the viscosity. 🔵 Numerically (`fig_cl24.py`): net transport angle 90.0° to the right of the wind and magnitude $V_0/(a\sqrt2)$ (exact value 0.707; the cut at $D_E$ gives 0.738). *The spiral depends on the turbulence; the total doesn't.*
- **Why Nansen saw 20–40° and not 90°.** The ice marks the **very top** of the layer, so it shows the *surface* angle (≈ 45° in theory), not the total; real turbulence is not a constant viscosity and the ice is not quite passive. Observations (Stewart p. 142, read): the flow averaged over many inertial periods is **almost exactly** Ekman's; the transport is 90° to the right, agreeing well with theory; Ralph and Niiler (2000) find $D_E=7.12\,U_{10}/\sqrt{\sin|\varphi|}$, almost exactly Ekman's, but a surface current $V_0$ **half** his; the surface angle depends on latitude and is near 45° at mid-latitudes. Clean spirals are hard to see; the transport is easy to see.
- **Assumptions** (Stewart p. 141, read): no boundaries (valid away from coasts), deep water ($\gg200$ m), $f$-plane, steady (wind longer than a pendulum day), $A_z$ depends only on $U_{10}^2$ and not on depth (**not a good assumption**: mixing changes rapidly at the base of the mixed layer), homogeneous density. Joy's remark: the spiral's depth is set by an assumed viscosity and ignores stratification (the Arabian Sea's mixed layer went from 20 to 62 m); one more reason to trust the total, not the spiral.

## 7. Ekman pumping and upwelling
<span class="scope-taught">taught</span> *O4 deck frames 17–24; Week 2 frames 59–64; O3 handout "Upwelling solves the puzzle"; O4 handout §5* · <span class="scope-extra-book">extra · book</span> *Stewart §9.3–9.4 pp. 143–146; Hartmann p. 218*

If the wind is the same everywhere the transport is the same everywhere: water arrives as fast as it leaves. But the wind changes from place to place; where more leaves than arrives water must come **up from below the mixed layer**, where more arrives it is pushed **down** (mass conservation). Integrating continuity over the layer (Stewart (9.28)): $\nabla_H\!\cdot\mathbf M_E=-\rho w_E(0)$, and with (9.26)
$$w=\mathrm{curl}_z\!\left(\frac{\boldsymbol\tau}{\rho f}\right)\ \text{(upward, at the base of the Ekman layer; Hartmann p. 218, Joy O4)}.$$
(Stewart's (9.29) is written at the *top* of the layer and balanced by a geostrophic velocity; following Pedlosky he notes it differs from the traditional bottom-of-layer form and that for the ocean the distinction matters.)

**Size.** The stress changes by 0.1 N m⁻² over 1,500 km (trades to westerlies): $w\approx0.1/(1025\times10^{-4}\times1.5\times10^{6})=6.5\times10^{-7}$ m s⁻¹ ≈ **20 m per year** (🔵 20.5; slide "≈ 21"): tiny as a speed, but all year, every year, across whole basins. **Map** (2011 winds, box means ✓ by Joy; blank within 5° of the equator and next to coasts): subtropical gyres **pushed down** ≈ 35 (N Pacific), 30 (N Atlantic), 25 m yr⁻¹ (S Pacific); subpolar N Pacific **pulled up** ≈ 15; Southern Ocean 50–62°S **pulled up** ≈ 25 m yr⁻¹. 🔵 Idealised check (figure A): trades (−) and westerlies (+) meeting at 30° give convergence and downward pumping there, and upward pumping poleward of ≈ 45°.

**Coastal upwelling.** Wind along a coast with the land on its left (NH) gives transport to the right, **offshore**; the water cannot come out of the coast, so it rises from below: **cold and nutrient-rich**. Examples: Somalia and Oman in the summer monsoon, **California** (wind blowing south), **Peru** (SH, wind blowing north, transport to the left, still offshore); Stewart lists Peru, California, Somalia, Morocco and Namibia as the world's major fisheries (p. 146, read). Stewart's San Francisco-versus-Norfolk answer (p. 146, read): upwelling gives cold water close to shore, the onshore wind is cooled to a thin cool boundary layer with **fog**, and the warmer air aloft (Hadley subsidence) inhibits convection, so rain is rare; the east coast has the reverse. *This is a wall, not a curl: it is not on the pumping map.* Upwelled nutrients: plankton use them in the sunlit layer, below the light nothing uses them and they build up.

**Equatorial upwelling.** $f$ changes sign at the equator. Under the westward trades the transport is to the right (north) just north of the equator and to the left (south) just south: **away from the equator on both sides**, so cold water rises: the **cold tongue** (Hartmann p. 218 says the cold SST tongue of July "is caused largely by this wind-driven upwelling"). *This closes the puzzle: the ocean gains heat where it is cold because cold water keeps arriving from below.* This year's El Niño (Joy: CPC advisory of 8 Oct 2026, Niño-3.4 +2.1 °C, a strong event likely through early 2027; ⚠ not recomputed) is weakened trades, weakened upwelling, a warmer tongue.

**The slab gets a new term** (O4 frame 23): the slab of CL23 only stored heat, no water moved. At a coast or the equator cold water from below keeps entering the layer and the surface must warm it: the heat budget needs a term for **water moving through** the slab.

## 8. Hills of water and geostrophy
<span class="scope-taught">taught</span> *Week 2 frames 65–69; O4 frames 25–31; O4 handout §6 and "How fast does water go round the hill?"*

Under the trades water goes poleward, under the westerlies equatorward; they meet near 30°, water piles up and is pushed down: a **hill about 1 m high, thousands of kilometres across** (subtropical gyres ≈ 0.9 m above the subpolar ocean: N Pacific 0.93, N Atlantic 0.94, S Pacific 1.05 m, box means ✓ by Joy). A hill means higher pressure under it than beside it: a push **downhill**. Every instinct says the water runs down and the hill flattens. But the moment it moves **Coriolis turns it to the right**; it keeps turning until Coriolis exactly opposes the pressure force, which happens only when the water runs **along the height contours**, at 90° to the push, with the **high side on its right** (in the northern hemisphere; on its left in the southern). Pressure pushes out, Coriolis pushes in, they cancel, the water keeps going round: nothing runs downhill, so **the hill stays up** (to ≈ 1 part in 1,000 for flows larger than ≈ 50 km and longer than a few days, Stewart p. 152 as Joy cites it, not read). This is **geostrophic flow**, Suhas's wind round a high in water ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]]); same form as Ekman: motion at 90° to the push. $u=-\frac1{f\rho}\partial_yp$, $v=\frac1{f\rho}\partial_xp$ (Joy citing Stewart (10.7a)). Surface speed $u=(g/f)\times$slope (Stewart (10.10) as cited):

| Slope | Speed (🔵) |
|---|---|
| 1 m over 1,500 km | **6.5 cm s⁻¹** (slow drift in a gyre interior; slide "≈ 7") |
| 1 m over 100 km | **0.98 m s⁻¹** (Gulf Stream; Stewart's "typical of strong currents") |

Steep slopes ⇒ fast currents, which is why **the fast flow is narrow**. The surface currents circle the hills: **clockwise in the north, anticlockwise in the south**; the fast flow is on the **west side** of each basin (Gulf Stream, Kuroshio, Agulhas), which Stommel (1948) traced to the change of $f$ with latitude (Joy: one sentence, "beyond this course"; Stewart ch. 11 not read here). The Southern Ocean has no land to stop them: the flow goes all the way round. **Garbage patches** (O4 handout §6): floating plastic collects near the centre of the subtropical gyres because Ekman transport carries it in towards the hill centre and geostrophic currents carry it only *around*. **Where is the friction?** Mostly at the edges (coasts, sea floor); in the open ocean the flow hardly feels friction.

## 9. Where the momentum finally goes
<span class="scope-taught">taught</span> *Week 2 frame 70; O4 frame 32* · <span class="scope-extra-book">extra · book</span> *Stewart p. 229, read*

The wind keeps adding momentum, so something must take it out: **coasts and the sea floor**. In most oceans continents hold the flow up. At Drake Passage's latitudes **no continent blocks the way**, so the **Antarctic Circumpolar Current** runs all the way round Antarctica, **≈ 125 million m³ s⁻¹** (Stewart p. 229, read: mean transport through Drake Passage **125 ± 11 Sv**, range 95–158 Sv from 91 current meters on 24 moorings, maximum in late winter/early spring; typical speeds ≈ 10 cm s⁻¹, up to 50 cm s⁻¹ at fronts; slow but deep and wide; currents reach the bottom and are steered by ridges), and hands its momentum to the sea floor over undersea ridges. That closes the momentum ledger. The Southern Ocean was teal (pulled up) on the pumping map: under that current **deep water comes up**. *Why was it down there? Salt.* → CL25.

## 10. Take-home: why does the Arabian Sea cool in mid-summer?
<span class="scope-taught">taught</span> *O4 deck frames 33–34; O4 handout "The take-home question, answered"*

The surface of the Arabian Sea (10–20°N, 60–70°E) is **29.9 °C in May and 26.7 °C in August** (CERES; 🔵 recomputed monthly means 29.9 and 26.6 °C, [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §6) although August's sun is still strong. The pieces: **monsoon winds** (the strongest of the year), a **deeper mixed layer** (20 m in April to 62 m in July: cool water mixed up), **upwelling** (Ekman transport offshore of Somalia and Oman, and Ekman pumping offshore of the jet's axis), and **monsoon clouds** cutting the sunlight; in autumn the winds drop and it warms again before winter cools it. It is the mixed-layer slab's budget again: a deeper layer and cold water entering from below it.

## Map of this chapter
> [!connection] How CL24 connects
> **Builds on:** [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] (the heat map to be explained, the mixed layer), [[CL22 The Ocean's Ledger I - Accounting for Energy]] (momentum exchange with the ground), [[CL12 Rotating Frames and the Coriolis Force]], [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (Suhas), [[CL19 Wind-Driven Ocean Circulation]] (Neena's version: scales of motion, gyres, boundary currents), [[CL15 Monsoons]].
> **Leads to:** CL25 salt ledger (density, why deep water forms), CL26 mass ledger (the Southern Ocean return of deep water is driven by the same wind), [[CL20 ENSO and the Walker Circulation]] (weaker trades, weaker upwelling).
> **Concepts:** [[Ekman Transport]] · [[Ekman Pumping]] · [[Subtropical Gyre]] · [[Mixed Layer]] · see also the interactive Ekman-spiral tool in [[Interactive Tools]] · [[Wind Stress]] · [[Sea-Surface Height]] · [[Geostrophic Balance]] · [[Upwelling]]

## Summary
> [!summary] Cheat-sheet
> - Air vs water: ρ ×850; ρc v ×34; $\tau/\rho H=2\times10^{-6}$ m s⁻²; Coriolis stops the push. $f=2\Omega\sin\varphi$.
> - $F=\frac1\rho\partial_z\tau$; Re ≈ 10¹¹, Ro ≈ 10⁻³; steady + large + flat ⇒ $-fv=\frac1\rho\partial_z\tau^x$, $fu=\frac1\rho\partial_z\tau^y$.
> - **Integrate over the layer:** $M_y=-\tau^x/\rho f$, $M_x=\tau^y/\rho f$: **90° right (N), left (S)**; ≈ 1 m² s⁻¹, 2 cm s⁻¹ over 50 m; 11°N Atlantic 12.0 ± 5.5 vs 8.8 ± 1.9 vs 13.5 ± 0.3 Sv.
> - Spiral: surface 45°, $D_E=\sqrt{2\pi^2A_z/f}$ (45–300 m), 4 % at $D_E$, sum = 90°. Ice 20–40° = top of the layer.
> - **Pumping** $w=\mathrm{curl}(\tau/\rho f)\approx20$ m yr⁻¹; subtropics down 25–35, Southern Ocean up 25. Coastal and equatorial upwelling (walls, $f\to0$) not on the map. Cold tongue ⇒ heat gain.
> - Hills ≈ 1 m: geostrophic, $u=(g/f)\,$slope: 7 cm s⁻¹ (1 m/1,500 km), 1 m s⁻¹ (1 m/100 km); clockwise N, west intensification; garbage patches. ACC 125 ± 11 Sv.

## Practice
1. **Transport.** Compute the Ekman transport for $\tau=0.15$ N m⁻² at 30°N, and the speed it implies over a 60 m layer. Which way does it point for a westerly wind?
2. **Direction.** Winds blow from the south along the coast of a northern-hemisphere continent that lies to the east of the ocean. Upwelling or downwelling? Repeat for winds from the north along the coast of a southern-hemisphere continent east of the ocean. (Joy's questions.)
3. **Pumping.** The stress changes by 0.08 N m⁻² over 1,000 km at 35°N ($f=8.4\times10^{-5}$). Estimate $w$ in m per year and say whether it is up or down if the stress becomes more eastward to the north.
4. **Geostrophy.** A 0.6 m rise of the sea surface across 400 km at 30°N ($f=7.3\times10^{-5}$): surface speed? Which way does the water go around the high?
5. **Rossby.** Show that for U = 0.1 m s⁻¹ and L = 1,000 km the acceleration term is a thousandth of Coriolis. Near the equator which assumption of §4 fails first? (Joy's question.)
6. **Cancellation.** In §5 why did every stress between the top and the bottom cancel? What changes if the stirred layer reached the sea floor? (Joy's question.)
7. **Trades.** If the trade winds weakened, what happens to the cold tongue and to the ocean's heat uptake there? (Joy's question.)
8. **Ice.** Explain without equations why the whole layer moves at exactly 90° to the wind while Nansen's ice moved 20–40°.

> [!example]- Solutions
> 1. $f=2\times7.292\times10^{-5}\times0.5=7.29\times10^{-5}$: $M=0.15/(1025\times7.29\times10^{-5})=2.0$ m² s⁻¹; over 60 m: **3.3 cm s⁻¹**. A westerly wind (toward the east, $\tau^x>0$) gives $M_y<0$: **southward** (to the right).
> 2. NH, wind from the south ⇒ wind blows north; transport to its right = **east = toward the coast** ⇒ **downwelling**. SH, wind from the north ⇒ blows south; transport to its **left** = **east** = toward the coast ⇒ **downwelling**.
> 3. $w=0.08/(1025\times8.4\times10^{-5}\times10^{6})=9.3\times10^{-7}$ m s⁻¹ ≈ **29 m yr⁻¹**; a stress that becomes more eastward to the north means $\partial_y\tau^x>0$, so $w=-\partial_y(\tau^x/\rho f)<0$: **downward** (the trades-to-westerlies convergence at 30°).
> 4. Slope 0.6/4×10⁵ = 1.5×10⁻⁶; $u=(9.81/7.3\times10^{-5})\times1.5\times10^{-6}=\mathbf{0.20}$ m s⁻¹, **clockwise** around the high in the north (high pressure on the right).
> 5. $Ro=U/fL=0.1/(10^{-4}\times10^{6})=10^{-3}$. Near the equator $f\to0$ so $Ro\to\infty$ and the acceleration/advection terms are no longer small (and $\tau/\rho f$ diverges); the steady, geostrophic balance fails, which is why the pumping map is blank within 5° of the equator.
> 6. Each layer exerts on the one below exactly what that one exerts back (Newton's third law), so adding $\partial\tau/\partial z$ over the layers telescopes to $\tau(\text{top})-\tau(\text{bottom})$. If the layer reached the sea floor, $\tau(\text{bottom})$ would be the **bottom friction**, not zero: the transport would no longer be at 90° to the wind (a bottom Ekman layer).
> 7. Weaker trades ⇒ weaker divergence ⇒ **less upwelling** ⇒ less cold water arrives ⇒ the cold tongue warms and its heat uptake falls, more strongly in the east where the upwelled water is the coldest (El Niño).
> 8. The block has only wind stress and Coriolis, which cancel only if opposite, so Coriolis (⊥ to motion) forces the motion 90° to the wind. The ice rides on the top of the layer, where the water moves at ≈ 45° (the spiral), and feels the wind directly as well.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | wind stress, ponderous ocean, Nansen, force balance, integration, transport, spiral, pumping, upwelling, hills, geostrophy, gyres, momentum's end, take-home | Week 2 deck frames 41–70 ([[O2-O3_Week2_Where-does-it-go_and_The-ponderous-ocean.pdf]]) and O4 deck, 34 frames ([[O4_Nansens-answer.pdf]]; speaker notes in the `_with-notes` versions) | taught (2026) |
> | equations in words, stress, turbulence, Re, Ro, assumptions, garbage patches, questions | [[handout_o3.md]], [[handout_o4.md]] (read in full) | taught (2026) |
> | Nansen force balance, Ekman solution and depth, observations, assumptions; transport (9.24)–(9.27), Chereskin and Roemmich, upwelling, San Francisco, pumping (9.28)–(9.29); Drake Passage | Stewart 2008 pp. 135–147 and p. 229 (`transcripts/readings/O4__01…`, `O4__02…`, `O5__04…`; read) | extra/book (2026) |
> | Ekman layer, transport, equatorial and coastal upwelling, pumping | Hartmann 2016 pp. 216–219 (`O4__03…`, OCR: equations garbled, words used; read) | extra/book (2026) |
> | every 🔵 number; idealised pumping profile; spiral hodograph | `scripts/fig_cl24.py` | extra-beyond |
>
> **Notes.** The idealised wind in figure A is mine, not a measurement; the stress/pumping/SSH/current maps and the box-mean values are Joy's (2011 ocean reanalysis) and were not recomputed. Not read: Stewart pp. 108–110, 115–119, 155–158, 183–190; Hartmann pp. 206–216 and 219–221; Ekman (1905), Stommel (1948), Chereskin and Roemmich (1991) are cited as Stewart/Joy cite them. The El Niño figures are Joy's quotation of a 2026 CPC advisory and were not checked.
