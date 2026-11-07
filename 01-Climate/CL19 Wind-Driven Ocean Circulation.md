---
title: CL19 Wind-Driven Ocean Circulation
aliases: [CL19, Ekman spiral, Ekman transport, Ekman pumping, upwelling, subtropical gyre, western boundary current, Gulf Stream, eastern boundary current, wind-driven circulation, Neena Lecture 21, Neena Lecture 22, Joy O3]
subject: climate
type: chapter
chapter: 19
part: V
scope: [taught, extra-book, extra-beyond]
by: [neena, joy, book]
status: draft
prereq: ["[[CL18 The Ocean as the Climate System's Heat Reservoir]]", "[[CL12 Rotating Frames and the Coriolis Force]]", "[[CL13 Horizontal Motion - Geostrophic Balance and Friction]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/neena, src/joy, src/book, status/draft]
---
# CL19 · Wind-Driven Ocean Circulation

◀ [[CL18 The Ocean as the Climate System's Heat Reservoir]] · [[Climate - Course Map|Course Map]] · ▶ [[CL20 ENSO and the Walker Circulation]]

<span class="scope-taught">taught · in syllabus (2025 Neena L21–22)</span> <span class="scope-extra-book">extra · book (Joy "NotCoveredInClass" readings)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-07)
> **Neena Lectures 21 and 22** (2025: scales of ocean motion, Ekman theory, Ekman transport, upwelling, gyres, boundary currents) and two of **Joy's readings that the reading list marks "NotCoveredInClass"** (this year): **Stewart 2008 pp. 143–147** (*Ekman mass transport, applications, Ekman pumping, Langmuir circulation*; clean text) and **Hartmann 2016 pp. 206–216** (*the wind-driven circulation*; OCR text, figures and equations garbled; the file ends in the middle of the Ekman derivation on p. 216). So the Ekman material is 🟢 taught in 2025 and 🟡 extra · book this year. Overlap with the atmosphere is deliberate: the Ekman layer is the oceanic cousin of the atmospheric boundary-layer balance in [[CL13 Horizontal Motion - Geostrophic Balance and Friction]], and the geostrophic gyre interior is [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] again with sea-surface height in place of pressure.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught (2025: L21–L22)**
> - §1 the two circulations (wind-driven vs thermohaline); §2 **Ekman's theory** (spiral, transport 90° to the right/left, Ekman depth), equatorial and coastal **upwelling**, nutrients and productivity; §3 **gyres** (subtropical anticyclonic gyre from equatorial, western and eastern boundary currents; Ekman convergence → sea-surface hump → geostrophic flow; what shapes the gyre; downwelling and the "ocean deserts"), **western and eastern boundary currents**, the Gulf Stream and the climate of western Europe
>
> 🟡 **Extra · book** (Joy's NotCoveredInClass readings)
> - §2 Ekman **mass transport** (9.24–9.27), the Sverdrup, the Atlantic 11°N section, **Ekman pumping** (9.28–9.29), Langmuir cells, inertial currents; §3 the current maps, the Indian-Ocean monsoon reversal, the vertical structure of the Gulf Stream, meanders and rings, eastern boundary currents and cold SST
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 the spiral derived for constant eddy viscosity (45°, $D_E$, $\pi D_E$, transport $\tau/f$), checked numerically; §3 geostrophic speed from the sea-surface hump; heat-flux check; the `[!verify]` on the lecture's Ekman depth

> [!key] After this chapter you can
> - separate **wind-driven** from **thermohaline** circulation by speed, depth, area and time scale,
> - state and **derive** the Ekman balance, the spiral and the transport $M_E=\tau/f$ **perpendicular to the wind**, in either hemisphere,
> - say where and why **upwelling** occurs (equator, coasts, wind-stress curl) and what it does to SST, weather and fisheries,
> - build a **subtropical gyre** from Ekman convergence and geostrophy and say why its western boundary current is narrow and fast,
> - explain why **Europe is warmer than eastern Canada** and why eastern boundary currents are cold.

> [!intuition] The one-sentence story
> Wind pushes the sea surface, but the Earth's rotation turns the water so that the **net** motion of the surface layer is **sideways** to the wind. Sideways transport piles water up in the middle of an ocean basin and drains it from the equator and the coasts; the pile is a hill, the hill drives a **geostrophic** flow (the same balance as the atmosphere's pressure highs), and the whole thing closes into a **gyre** with a narrow fast current on the western edge.

![[fig_cl19_ekman.png]]
*A: the Ekman spiral for $A_z=0.1$ m² s⁻¹, $f=10^{-4}$ s⁻¹ ($D_E=44.7$ m): current vectors from the surface (45° to the right of the stress) to $z=-\pi D_E$ where it is reversed (§2). B: Ekman volume transport $\tau/(\rho f)$ against latitude (Stewart 9.26). C: coastal upwelling, schematic (Stewart Fig. 9.8). Numbers: `scripts/cl_neena_numbers.py` (cl19).*

> [!tip] 🔬 Interactive: the Ekman spiral
> Open [▶ cl_ekman_spiral.html](../Assets/interactive/cl_ekman_spiral.html) (self-contained, works offline). Choose hemisphere, latitude, wind stress and eddy viscosity: the hodograph shows the current at each depth, the right panel its speed and rotation, and the violet arrow the **transport**, which stays exactly perpendicular to the stress and equal to $\tau/f$ **whatever $A_z$ is**.

## 1. Two circulations
<span class="scope-taught">taught</span> *Neena L21 pp. 2–7: [[Lecture21 Ocean_wind driven circulation-1_251119_141638 (1).pdf#page=3|p. 3]], [[Lecture21 Ocean_wind driven circulation-1_251119_141638 (1).pdf#page=6|p. 6]]*

The oceans carry **more heat than the atmosphere at low latitudes**, transport nutrients and organisms, exchange gases, shape fisheries, weather and climate (L21 p. 2; [[CL18 The Ocean as the Climate System's Heat Reservoir]] §7). The currents are the oceanic equivalent of winds (Benjamin Franklin mapped the Gulf Stream in the 18th century). Two energy sources define two circulations:

| | wind-driven | thermohaline |
|---|---|---|
| forcing | wind stress on the surface (momentum) | density changes from heat and fresh-water exchange (buoyancy) |
| speeds | fast, ~50 cm/s to 4 m/s | very slow, <1 cm/s |
| depth | surface layer, 50–200 m | deep, ~1000–4500 m |
| volume | ~10 % of the ocean | ~90 % |
| time scale | daily to seasonal | ~1000 yr |

Lateral temperature and density differences are **too small to drive the surface currents directly**; the chain is: SST differences → atmospheric pressure gradients → **winds** → frictional drag → surface currents. The thermohaline half is [[CL21 Thermohaline Circulation Water Masses and Sea Ice]].

## 2. Ekman theory
<span class="scope-taught">taught</span> *Neena L21 pp. 8–15* · <span class="scope-extra-book">extra · book</span> *Stewart §9.3–9.5: [[03_NotCoveredInClass_Stewart2008_Ekman-Transport-and-Upwelling_pp143-147.pdf#page=1|pp. 143–147]]; Hartmann p. 216: [[04_NotCoveredInClass_Hartmann2016_Wind-Driven-Circulation_pp206-216.pdf#page=11|p. 216]]* · <span class="scope-extra-beyond">extra · beyond</span> *derivation and numbers*

**History** (L21 p. 9): Nansen (1898) saw Arctic icebergs drift to the **right of the wind**; Ekman (1905) quantified the effect of wind and the Earth's rotation on the upper ocean. A water column is a stack of thin coupled layers: each layer drives the one below, which Coriolis then deflects, so with depth the current **weakens and turns** away from the wind in a **spiral**. Surface currents flow at **20°–45° to the wind** (L21); the kinetic energy of the wind is passed down. **Transport:** the net transport in the spiral is **90° to the right (left) of the wind in the northern (southern) hemisphere**.

**Derivation** 🔵 (constant eddy viscosity $A_z$; steady; no pressure gradient; northern hemisphere, $f>0$): $-fv=A_zu_{zz}$, $fu=A_zv_{zz}$. With $w=u+iv$: $w_{zz}=(if/A_z)w$, so $w=W\exp[(1+i)z/D_E]$ with $D_E=\sqrt{2A_z/f}$; the stress boundary condition $\rho A_zw_z(0)=\tau$ (stress along $+x$) fixes $W=\tau/[\rho A_z(1+i)/D_E]$. Hence
$$u+iv=\frac{\sqrt2\,\tau}{\rho fD_E}\,e^{z/D_E}\,e^{i(z/D_E-\pi/4)}.$$
Checked numerically ($A_z=0.1$, $f=10^{-4}$, $\tau=0.1$): $D_E=44.7$ m; the surface current is $3.09$ cm/s at $-45^\circ$ (**45° to the right** of the stress); the speed is $1/e$ of the surface value at $z=-D_E$ (the current has rotated $57.3^\circ$); at $z=-\pi D_E$ the current is **exactly opposite** to the surface current with $e^{-\pi}=4.3\,\%$ of its speed. **Integrated transport:** $M=\rho\!\int u\,dz=(0,-1000.1\,\mathrm i)$ kg m⁻¹ s⁻¹, i.e. $\tau/f$ (1000.0) **at $-90^\circ$ from the stress**, independent of $A_z$.

> [!verify] The lecture's "Ekman depth"
> L21 pp. 10–11 says that at "some depth the flow becomes opposite to the surface flow with the speed reducing to $1/e$ of the surface speed. This depth is called the Ekman depth", and gives about $100$ m in the open ocean for the depth where the current is opposite. In the constant-viscosity solution these are **two different depths**: the speed is $1/e$ at $D_E$ (rotated 57°) and the flow is opposite at $\pi D_E$ (speed $4.3\,\%$). Stewart (9.23) gives the scalings $A_z\sim U_{10}^2/N$ and $D_E\sim U_{10}/\sqrt{Nf}$ for a stratified ocean ($N$ the stability frequency, Chapter 8; the printed coefficient is not legible); the depth depends on **stratification, wind speed and latitude**. The surface-angle "20–45°" of the slide vs the exact $45^\circ$ of the constant-$A_z$ model: drifter data give less than 45° (Stewart Fig. 9.6).

> [!key] Ekman mass transport (Stewart 9.24–9.27)
> Integrating the balance over the layer (the stress vanishes a few hundred metres down): $$fM_{Ey}=-\tau_{xz}(0),\qquad fM_{Ex}=\tau_{yz}(0),$$ i.e. $\mathbf M_E=\hat{\mathbf z}\times\boldsymbol\tau/f$: **perpendicular to the wind**, to the **right** in the northern hemisphere ($f>0$). A south wind ($\tau_y>0$) gives eastward transport. This holds because friction is confined to a thin boundary layer, zero in the interior, and the current is in equilibrium with the wind. It is far more **robust** than the velocities: it needs neither the eddy viscosity nor the profile. **Volume transport** $Q=M\,(\text{width})/\rho$ in m³ s⁻¹; the unit $10^6$ m³ s⁻¹ is the **Sverdrup (Sv)**.
> *Numbers* 🔵: $\tau=0.1$ N m⁻² gives $M/\rho=1.34$ m² s⁻¹ at 30° ($1.34$ Sv across 1000 km), $3.51$ at 11°, $0.95$ at 45°, $0.77$ at 60° (figure B; the $1/\sin\varphi$ growth towards the equator shows where the theory stops working). **Observation** (Chereskin and Roemmich 1991, Atlantic 11°N, acoustic Doppler profiler): $12.0\pm5.5$ Sv northward measured directly, $8.8\pm1.9$ Sv from the measured winds, $13.5\pm0.3$ Sv from mean climatological winds. (A transport of $8.8$ Sv at $f=2.78\times10^{-5}$ s⁻¹ means $\tau L=Q\rho f=2.5\times10^5$ N m⁻¹: over an assumed $4000$ km, a mean stress of $0.063$ N m⁻², a reasonable trade-wind value.)
> **Inertial currents** (Stewart 9.6): a sudden change of stress excites oscillations of period $2\pi/f$ ($23.9$ h at 30°, $62.7$ h at 11°, $16.9$ h at 45°).

**Upwelling** (L21 pp. 12–15; Stewart §9.4, Fig. 9.8):
- **Equatorial:** the surface winds are easterlies; Ekman transport is to the right (poleward) north of the equator and to the left (poleward) south of it: **divergence** of surface water, **upwelling from below**.
- **Coastal:** wind blowing *along* the shore: Ekman transport **away from the coast** → coastal upwelling; towards the coast → downwelling. North winds on a west coast in the northern hemisphere (California) push water offshore; it is replaced from 100–300 m depth by **cold, nutrient-rich** water.
- **Nutrients and life:** photosynthesis depletes nitrate and phosphate in the euphotic zone; decaying organic matter releases them as it sinks, with a **nutrient maximum near 1 km**; where upwelling brings thermocline water to the surface, **primary productivity is high** (limited by nutrients elsewhere). The great fisheries (Peru, California, Somalia, Morocco, Namibia) are upwelling regions (Stewart).
- **Weather:** cold upwelled water cools the air above it; onshore air forms fog and low stratus, with stable stratification, little convection and little rain: Stewart's answer to why San Francisco differs from Norfolk, Virginia (also the thin eastern mixed layer and equatorward cold currents on the eastern side; all reversed off east coasts).
- **Ekman pumping** (Stewart 9.28–9.29): horizontal variations of the wind change the Ekman transport and, by continuity, produce **vertical velocity**: $\nabla_H\!\cdot\mathbf M_E=-\rho w_E(0)$, $w_E(0)=-\mathrm{curl}_z(\boldsymbol\tau/\rho f)$ (Stewart's sign convention is for the **top** of the layer, where $w_E$ is balanced by a geostrophic $w_G$; the physical rule is: **divergence of $\mathbf M_E$ → upwelling from below, convergence → downwelling**). 🔵 A wind-stress curl of $-10^{-7}$ N m⁻³ at 30°N (anticyclonic, as over a subtropical gyre) corresponds to Ekman convergence pumping water down at $1.3\times10^{-6}$ m s⁻¹ $\approx42$ m yr⁻¹.
- **Langmuir circulation** (Stewart §9.5): wind also makes cells with axes parallel to the wind; at 14 m/s Weller et al. saw cells spaced $20$ m, $15^\circ$ to the right of the wind, with downward jets to $-0.18$ m/s at $23$ m, not penetrating the seasonal thermocline at 50 m.

## 3. Gyres and boundary currents
<span class="scope-taught">taught</span> *Neena L21 pp. 16–17, L22 pp. 2–16: [[Lecture22_Ocean_wind driven circulation-2_251113_133827 (1).pdf#page=4|p. 4]], [[Lecture22_Ocean_wind driven circulation-2_251113_133827 (1).pdf#page=8|p. 8]], [[Lecture22_Ocean_wind driven circulation-2_251113_133827 (1).pdf#page=12|p. 12]]* · <span class="scope-extra-book">extra · book</span> *Hartmann pp. 206–216*

**The subtropical gyres are anticyclonic** (clockwise in the NH) and are made of three parts (L21 p. 16): **westward currents along the equator**, **poleward currents on the western boundaries** of the basins, **equatorward currents on the eastern boundaries**. **How the wind makes them** (L22 pp. 4–5): the Ekman transport is $90^\circ$ to the right of the wind, i.e. **towards the centre of the gyre**; it **piles up water** in the centre, so sea level is higher there than at the edges; gravity makes the water flow outward ("downhill"), the Coriolis force deflects it; away from the boundary the flow is **geostrophic** (pressure-gradient force balancing Coriolis; "recall geostrophy in the atmosphere", [[CL13 Horizontal Motion - Geostrophic Balance and Friction]]) and moves clockwise around the hill. The observed gyre is thus the sum of the **wind-driven surface currents and the geostrophic currents** of the sea-surface-height variations created by Ekman transport; since the winds vary, the geostrophic part keeps the circulation steady when the wind drops. 🔵 *Scale:* a $1$ m hump over a gyre of half-width $2500$ km at 30°N: $v=g\,\Delta\eta/(fL)=9.81\times1/(7.29\times10^{-5}\times2.5\times10^6)=0.054$ m s⁻¹, a few cm/s in the broad interior (the "much more gradual return flow across the centre of each basin" of Hartmann). **The shape of a gyre** depends on (L22 p. 8) the **shape of the ocean basin**, the **spatial variation of the wind**, and the **variation of the Coriolis parameter with latitude**. Cyclonic **subpolar** gyres form at high latitudes (less clear because of the land–ocean geometry). **Convergence** in the middle of the subtropical gyres causes **downwelling**: surface water sinks, no nutrients are brought up, **productivity is low**: "deserts on land and deserts in the ocean".

| western boundary currents (warm, poleward) | eastern boundary currents (cold, equatorward) |
|---|---|
| Gulf Stream (N Atlantic), Kuroshio (N Pacific), Brazil (S Atlantic), East Australian (S Pacific), Agulhas (Indian) | Canary (N Atlantic), California (N Pacific), Benguela (S Atlantic), Peru/Humboldt (S Pacific) |

- **Western boundary currents** (Hartmann): narrow, strong poleward currents very close to the continents, speeds that may exceed $1$ m s⁻¹, "the closest oceanographic analogs to the jet streams" though flowing poleward; the Gulf Stream follows the coast of South America, through the Strait of Florida and up the US east coast, leaves it at Cape Hatteras and turns east along the SST gradient; **its strength is nearly the same in summer and winter** (unlike the atmospheric jets); the eastward current at 65°W is $>0.5$ m s⁻¹ in the monthly mean, extends to $\sim1000$ m, and is geostrophically balanced by the sloping thermocline; it breaks into **meanders and rings** whose size is about **100 times smaller** than the atmosphere's corresponding eddies (the baroclinic Rossby radius is smaller in the ocean). L22: they carry warm water poleward, **$\sim10^{15}$ W** (checked, [[CL18 The Ocean as the Climate System's Heat Reservoir]] §7: $1.2\times10^{15}$ W for $30$ Sv and $10$ K), and the **mild winters of western Europe** (about **5 °C** warmer than parts of Canada at the same latitude) owe to it; Hartmann adds that the Atlantic SST asymmetry is *one* contribution, the other being the **cold continental air advected over North America** by stationary waves; a weakening Gulf Stream could bring colder winters (L22).
- **Eastern boundary currents** (Hartmann): **cold, shallow, broad**; the wind-driven flow along the coast towards the equator then turns west; associated with **cold SST** (deviation from the zonal mean, Fig. 7.14), persistent **stratocumulus and fog** (the California current, L22) and the surface highs of the subtropics; best developed in summer in the northern hemisphere, year-round in the southern; **upwelling** (alongshore or offshore winds) produces the cold coastal water; the Ekman transport "plays a critical role in determining relatively cold surface temperatures in the eastern boundary current regions and along the equator, and in driving the subtropical gyres that feed the western boundary currents".
- **Indian Ocean** (Hartmann p. 207–210): the currents reverse with the monsoon (westward north of the equator in January, eastward in July); along the African and Arabian coasts the southerly summer winds drive a northward current and **offshore upwelling**, so the SST is **warmer in January than July**. **Southern Ocean:** the **Antarctic Circumpolar Current** flows eastward at ~60°S through the Drake Passage because no continents block it. Near the equator in the Pacific the current is westward, with the **North Equatorial Countercurrent** eastward north of the equator, strongest in northern summer.

> [!example] Why the western boundary is the narrow one (not on the slides) 🔵
> The slides name western boundary currents but do not say why *western*. The standard answer (Stommel 1948; Munk) is that the **variation of $f$ with latitude** makes the interior flow of a wind-driven gyre equatorward (the **Sverdrup balance** $\beta v=\mathrm{curl}_z\tau/\rho$), so mass conservation demands a return flow in a thin boundary layer, which must lie on the **west** for $\beta>0$. This is **recalled, not read**, and it is outside the lecture's set of ideas; it is consistent with the lecture's "change of Coriolis parameter with latitude" among the shape controls and with the observation that the Gulf Stream is narrow and the return flow broad.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: The Ekman spiral and Ekman transport
> A steady wind stress τ drags the surface water; friction (constant eddy viscosity A_z) and the Coriolis force turn the current with depth: the Ekman spiral.
>
> ![[cl_ekman_spiral.png|720]]
>
> **Try:** A_z = 0.1 m² s⁻¹ at f = 10⁻⁴ s⁻¹ (about 43° latitude): D_E = 44.7 m and the surface current is 3.1 cm/s for τ = 0.1 N m⁻². Change A_z: D_E and the surface speed change but the transport arrow does not. Move to the southern hemisphere: everything mirrors. Latitude 11°, τ = 0.063 N m⁻² gives the 8.8 Sv-type transport of the Chereskin–Roemmich section over ~4000 km.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_ekman_spiral.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_ekman_spiral.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL19 connects
> **Builds on:** [[CL18 The Ocean as the Climate System's Heat Reservoir]] (mixed layer, heat transport), [[CL12 Rotating Frames and the Coriolis Force]] and [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (Coriolis, geostrophy, boundary-layer friction), [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (trades and westerlies as the wind stress).
> **Leads to:** [[CL20 ENSO and the Walker Circulation]] (equatorial upwelling and the thermocline), [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] (what the gyres feed).
> **Concepts:** [[Ekman Spiral]] · [[Ekman Transport]] · [[Ekman Pumping]] · [[Upwelling]] · [[Subtropical Gyre]] · [[Western Boundary Current]] · [[Eastern Boundary Current]] · [[Inertial Oscillation]]
> **Other subjects:** [[Waves - Course Map]] (inertial oscillations, Kelvin waves), [[Quantum Mechanics - Course Map]] (analogy only: the complex form $w=u+iv$ and $e^{i\theta}$ rotation), [[Landscapes and Geomorphology - Course Map]] ([[LS26 Sea Level and Ocean Waves]], [[LS27 Coasts Beaches Deltas and Rocky Shores]]: coastal currents and sediment), [[Ecology and Evolution - Course Map]] (primary productivity and nutrient limitation: [[EE06 Eutrophication and Alternative Stable States]]), [[Classical Mechanics - Course Map]] (rotating frames, Coriolis: [[CM01 Variational Calculus and Hamilton's Principle]] background).

## Summary
> [!summary] Cheat-sheet
> - **Wind-driven:** 50 cm/s–4 m/s, 50–200 m, 10 % of the ocean, days–seasons; **thermohaline:** <1 cm/s, 1–4.5 km, 90 %, ~1000 yr.
> - **Ekman:** $-fv=A_zu_{zz}$, $fu=A_zv_{zz}$; spiral $e^{z/D_E}$, $D_E=\sqrt{2A_z/|f|}$; surface current 45° right (NH) of the wind (observed 20–45°), reversed at $\pi D_E$ ($4.3\,\%$); **transport $\mathbf M=\hat z\times\tau/f$, 90° right (NH), independent of $A_z$**; $1\ \text{Sv}=10^6$ m³ s⁻¹; Atlantic 11°N: 8.8–13.5 Sv.
> - **Upwelling:** equator (divergence), coasts (alongshore wind, offshore transport), wind-stress curl; cold, nutrient-rich, productive, foggy, fisheries.
> - **Gyres:** Ekman convergence → hill → geostrophic clockwise flow; equatorial westward, western boundary poleward (warm, narrow, fast, ~$10^{15}$ W, steady all year), eastern boundary equatorward (cold, broad); centre downwelling = ocean desert; Gulf Stream + continental air → mild western Europe.

## Practice
1. **Ekman transport.** $\tau=0.1$ N m⁻² (eastward wind) at 30°N and at 11°N: find $M$, $M/\rho$ and the transport across 1000 km and its direction. Repeat at 30°S.
2. **Spiral.** With $A_z=0.05$ m² s⁻¹ and $f=10^{-4}$ s⁻¹ find $D_E$, the depth where the current is opposite, and the speed there relative to the surface.
3. **Independence.** Show that the integrated transport does not depend on $A_z$ (integrate the momentum equations directly).
4. **Atlantic section.** 8.8 Sv at 11°N over an assumed width of 4000 km: find the mean stress.
5. **Upwelling.** North wind of 0.1 N m⁻² on a west coast at 36°N: find the Ekman transport per km of coast and the vertical velocity if the upwelling zone is 50 km wide.
6. **Gyre.** A subtropical gyre with a 1 m sea-surface height difference over $L=2500$ km at 30°N: geostrophic speed. What is the sign of the sea-level slope at its edge?
7. **Heat.** A boundary current of 30 Sv with a 10 K contrast: heat transport. The total at 35° is 6 PW: what fraction?
8. **Concept.** Why is the Gulf Stream almost the same in summer and winter whereas the jet stream is not? Why are eastern boundary currents cold?

> [!example]- Solutions
> 1. $f(30^\circ)=7.29\times10^{-5}$: $M=1371$ kg m⁻¹ s⁻¹, $M/\rho=1.34$ m² s⁻¹, $1.34$ Sv across 1000 km, directed **south** (right of an eastward wind); at 11°: $f=2.78\times10^{-5}$, $M=3594$, $3.5$ m² s⁻¹, $3.5$ Sv; at 30°S $f<0$: transport to the **north** (left of the wind), same magnitude.
> 2. $D_E=\sqrt{2\cdot0.05/10^{-4}}=31.6$ m; opposite at $\pi D_E=99$ m (the lecture's "about 100 m"), speed $e^{-\pi}=4.3\,\%$.
> 3. Integrate $A_zu_{zz}=-fv$ from $-\infty$ to $0$: $A_zu_z(0)=-fV$ and $A_zv_z(0)=fU$ with $\rho A_zu_z(0)=\tau_x$: $V=-\tau_x/(\rho f)$, $U=\tau_y/(\rho f)$: no $A_z$.
> 4. $Q\rho f/L=8.8\times10^6\times1025\times2.78\times10^{-5}/4\times10^6=0.063$ N m⁻².
> 5. $M=\tau/f=0.1/8.57\times10^{-5}=1167$ kg m⁻¹ s⁻¹ ($f=2\Omega\sin36^\circ=8.57\times10^{-5}$), so per km $1.14\times10^3$ m³ s⁻¹; spread over a $50$ km wide zone the upwelling is $w=1.14/(50\times10^3)=2.3\times10^{-5}$ m s⁻¹ $=2$ m day⁻¹.
> 6. $0.054$ m s⁻¹; sea level falls from the centre to the edges, so the slope is outward.
> 7. $1.2\times10^{15}$ W $=1.2$ PW $=20\,\%$ of 6 PW.
> 8. The ocean's thermal and mechanical inertia and the steadiness of the trade/westerly stress make the gyre persistent; the jet depends on the seasonal meridional temperature gradient of the air ([[CL14 Observed Winds - Jets, Trades and the ITCZ]]). Eastern boundary: equatorward flow brings water from high latitudes, and offshore Ekman transport brings deep cold water up.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (3): the other tool's concept notes from the lectures, unreviewed
> [[zettel/ocean-surface-currents|Ocean Surface Currents]] · [[zettel/oceanic-gyres-and-surface-currents|Oceanic Gyres and Surface Currents]] · [[zettel/oxygen-isotope-ratio|Oxygen Isotope Ratio]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | scales and the two circulations, Ekman's theory, Ekman depth, upwelling, nutrients | [[Lecture21 Ocean_wind driven circulation-1_251119_141638 (1).pdf]] pp. 2–15 | taught (2025) |
> | gyres, Ekman convergence, geostrophy, shape, downwelling, boundary currents, Gulf Stream and Europe | [[Lecture22_Ocean_wind driven circulation-2_251113_133827 (1).pdf]] pp. 2–16 | taught (2025) |
> | Ekman mass transport, Sverdrup, 11°N section, coastal upwelling, climate of San Francisco, Ekman pumping, Langmuir cells, inertial currents | [[03_NotCoveredInClass_Stewart2008_Ekman-Transport-and-Upwelling_pp143-147.pdf]] (read) | extra/book (2026, "not covered in class") |
> | wind stress, surface current maps, western/eastern boundary currents, Gulf Stream structure, Indian Ocean monsoon reversal, cold eastern SST | [[04_NotCoveredInClass_Hartmann2016_Wind-Driven-Circulation_pp206-216.pdf]] (OCR; read to p. 216, figures not seen) | extra/book (2026) |
> | spiral derivation, numbers, geostrophic scale, Ekman pumping rate | `scripts/cl_neena_numbers.py` (cl19), `scripts/fig_cl16_21.py`, tool `cl_ekman_spiral` | extra/beyond |
>
> **Notes.** [!verify] The lecture's Ekman depth (§2). The Hartmann Ekman derivation (pp. 216 ff.) is cut off in the excerpt; the spiral is derived here independently. The Sverdrup/Stommel explanation of the western intensification is **recalled, not read**. Stewart's printed (9.23) coefficient is illegible; only the scalings are quoted.
