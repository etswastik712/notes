---
title: CL20 ENSO and the Walker Circulation
aliases: [CL20, ENSO, El Nino, La Nina, Southern Oscillation, Walker circulation, Bjerknes feedback, Nino index, SOI, teleconnections, Neena Lecture 23]
subject: climate
type: chapter
chapter: 20
part: V
scope: [taught, extra-beyond]
by: [neena]
status: draft
prereq: ["[[CL19 Wind-Driven Ocean Circulation]]", "[[CL18 The Ocean as the Climate System's Heat Reservoir]]", "[[CL14 Observed Winds - Jets, Trades and the ITCZ]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/neena, status/draft]
---
# CL20 · ENSO and the Walker Circulation

◀ [[CL19 Wind-Driven Ocean Circulation]] · [[Climate - Course Map|Course Map]] · ▶ [[CL21 Thermohaline Circulation Water Masses and Sea Ice]]

<span class="scope-taught">taught · in syllabus (2025 Neena L23)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-07)
> **Neena Lecture 23** (2025, *El Niño Southern Oscillation*; 24 slides, mostly figures, animations and short captions: **text only was read**, the SST maps, the 1997–98 and 1995–96 animations and the teleconnection map were not seen). No 2026 source (Joy's readings mention El Niño only in passing: Stewart §5.6 and Hartmann Fig. 4.19 say that heat fluxes change substantially from year to year, "especially in the tropics, especially due to El Niño"). The chapter is therefore **short**, and its extras are labelled: a force balance for the zonal slope and the reduced-gravity relation are **my illustrations** with assumed values, not course content. The mechanism of the *oscillation* (what turns El Niño into La Niña) is **not on the slides** and is not invented here.

> [!note] Joy-primary update (2026-11-13)
> Joy has no ENSO lecture yet (O7 is not on the site); his material touches it in **[[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]]** §7 (equatorial upwelling and the cold tongue; weaker trades ⇒ weaker upwelling) and in **[[CL28 Tutorials II - Earth's Energy Budget from Space (CERES)]]** Exercises 7–8 (the El Niño OLR dipole, why the global net radiation barely changes, the 6-month lag), recomputed from CERES data.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught (2025: L23)**
> - §1 the **mean state** of the equatorial Pacific (upwelling, sea level, SST, mixed layer and thermocline depth, the east–west pressure gradient), the **Walker circulation** and the **Bjerknes feedback**; §2 **El Niño** (anomaly, weakened trades, eastward surge of warm water, shift of convection, 1997–98), the **Southern Oscillation** (Walker 1920; Tahiti and Darwin), **La Niña**; §3 the **Niño index**, the **Southern Oscillation Index**, the definition of **ENSO**, teleconnections and observing system
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §1 the pressure-force/wind-stress balance for the 0.5 m slope; the reduced-gravity conversion to thermocline depth; a Kelvin-wave crossing time

> [!key] After this chapter you can
> - describe the **mean state** of the tropical Pacific (west warm and deep, east cold and shallow) and the atmospheric circulation that goes with it,
> - explain the **Bjerknes feedback** as a **positive feedback** between SST gradient and trade winds,
> - describe an **El Niño** and a **La Niña** in SST, wind, thermocline, sea level, pressure and rainfall, and define the **Niño** and **Southern Oscillation** indices,
> - say what ENSO is in one sentence, and what is *not* explained by the lecture.

> [!intuition] The one-sentence story
> The trade winds pile warm water up in the west of the Pacific; the warm pool heats the air above it, the air rises, the circulation closes with easterlies at the surface, and those easterlies are what **keep** the warm water piled up: a **loop that feeds itself**. If the loop weakens, the pile slumps eastward, the convection follows it, and the winds weaken further. That is El Niño; the same loop running **stronger** than normal is La Niña.

![[fig_cl20_enso.png]]
*A, B: cartoon cross-sections of the equatorial Pacific as described by Lecture 23 (not data): thermocline tilt, SST, convection and surface winds in the mean state and in El Niño. C: the balance between the pressure force of a sea-level slope and the wind stress on a layer of thickness $H$ (§1, my illustration). Numbers: `scripts/cl_neena_numbers.py` (cl20).*

## 1. The mean state and the Walker circulation
<span class="scope-taught">taught</span> *Neena L23 pp. 2–8, 15–16: [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=2|p. 2]], [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=4|p. 4]], [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=5|p. 5]]* · <span class="scope-extra-beyond">extra · beyond</span> *numbers*

**Ocean:** upwelling along the equator and along the eastern margins; sea level about **half a metre higher over the West Pacific** than the East; **warmer SST in the west, cooler in the east** (the "warm pool" and "cold tongue"); a **deep mixed layer (to ~200 m) in the west and a shallow one in the east**, with the thermocline at a larger depth in the west. **Atmosphere:** the SST contrast sets an **east–west pressure gradient**; air **ascends over the warm west**, **subsides over the cooler east**, and the loop closes with **upper-tropospheric westerlies** and **surface easterlies**: the **Walker circulation** (Bjerknes 1960), which **reinforces the surface easterlies** of the trades ([[CL14 Observed Winds - Jets, Trades and the ITCZ]], [[CL11 Mean Meridional Circulation and Angular Momentum]] for the north–south analogue).

> [!key] The Bjerknes feedback (L23 pp. 5, 16)
> Surface easterlies drive easterly surface currents and upwelling → warm SST and low pressure in the west, cool SST and high pressure in the east → atmospheric **convection over the West Pacific** → **latent-heat release** heats the atmospheric column → lower surface pressure → **stronger easterlies**: a **positive feedback**. The coupled system: **west** = warm SST, low pressure, convection, cloud and rain, converging surface water, higher sea level, **deep** mixed layer, downwelling, **deep thermocline**; **east** = cool SST, high pressure, subsidence, no cloud or rain, **diverging** surface water, upwelling, **shallow** mixed layer and thermocline. Along the South American coast upwelling brings nutrient-rich cold water and rich fisheries ([[CL19 Wind-Driven Ocean Circulation]] §2).

> [!example] Is half a metre consistent with the trades? 🔵
> The wind must hold the pile of water against its own pressure force. Balancing the zonal pressure force on a layer of thickness $H$ and density $\rho$ with the stress $\tau$: $\tau=\rho gH\,\Delta\eta/L$. With the slide's $\Delta\eta=0.5$ m, an assumed width $L=15{,}000$ km and $H=150$ m: $\tau=1025\times9.81\times150\times0.5/1.5\times10^7=\mathbf{0.050}$ N m⁻² ($0.034$ for $H=100$ m, $0.067$ for $200$ m). The bulk formula of [[CL18 The Ocean as the Climate System's Heat Reservoir]] §4 ($\tau=\rho_aC_DU_{10}^2$, $C_D=(0.50+0.071U_{10})\times10^{-3}$) gives $0.043$ N m⁻² for a $6$ m s⁻¹ trade wind: the two agree within the uncertainty of $H$ and $L$. A **reduced-gravity** step (assumed $g'=g\,\Delta\rho/\rho=0.03$ m s⁻², i.e. $\Delta\rho/\rho=0.3\,\%$ across the thermocline) converts a surface slope into an opposite thermocline slope $\Delta h=g\,\Delta\eta/g'\approx160$ m: the **thermocline tilt is hundreds of times larger than the sea-surface tilt**, which is why the thermocline depth is the better indicator of the heat stored in the west. A first-baroclinic **Kelvin wave** with $c=\sqrt{g'H}\approx2.1$ m s⁻¹ would cross $15{,}000$ km in $\sim82$ days: an indication why the ocean adjusts over months. All three are illustrations with assumed parameters; none is on the slides.

## 2. El Niño, La Niña and the Southern Oscillation
<span class="scope-taught">taught</span> *Neena L23 pp. 8–21: [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=10|p. 10]], [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=13|p. 13]], [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=18|p. 18]]*

**El Niño** means **warmer than normal SST in the eastern Pacific**. In 1983 the SST anomaly (departure from the climatological mean state) shows the warm tongue. El Niño events are departures from the mean state that result from a **weakening of the easterly trade winds**: weaker trades let the warm western water **surge eastward** and the sea level **flattens**; weaker easterlies **reduce upwelling** of cold water in the east; the warm water carries the **clouds and convection** with it, so it is **drier over the West Pacific** and **wetter over the central and eastern Pacific**: low pressure and convection move east, higher pressure and subsidence appear over the west; the **east–west gradients of SST, sea-surface height and thermocline depth all fall**; the **Walker circulation shifts**. The **Bjerknes feedback runs the other way**: weaker easterlies → weaker easterly currents and less upwelling → warmer east, cooler west → more convection over the east, less over the west → lower pressure in the east, higher in the west → weaker easterlies still. **La Niña** (1995–96 is the example): **cooler than normal SST in the eastern Pacific when the trade winds are stronger than normal**. The **1997–98 El Niño** is shown as an animation (January 1997–December 1998).

**The Southern Oscillation** (Sir Gilbert Walker, 1920): in the climatological mean the sea-level pressure is **higher over Tahiti than over Darwin**; the Southern Oscillation is the **oscillation of surface pressure between the eastern and western Pacific**. In El Niño the western Pacific has cooler SST, higher pressure, subsidence, no cloud or rain; the eastern Pacific warmer SST, **lower pressure**, more convection, cloud and rain (the table of L23 p. 14).

## 3. Indices, definition and impacts
<span class="scope-taught">taught</span> *Neena L23 pp. 19–24: [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=19|p. 19]], [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=20|p. 20]], [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf#page=22|p. 22]]*

- **Niño index:** SST anomalies **averaged over a box in the eastern equatorial Pacific**; it captures the variation of SST there (positive in El Niño, negative in La Niña).
- **Southern Oscillation Index (SOI):** the **sea-level-pressure difference between Tahiti and Darwin**; it measures the strength of the **Walker circulation**: a **large positive** SOI means a strong Walker circulation (La Niña conditions); **negative** during El Niño (the pressure difference collapses).
- **ENSO** "refers to the natural **interannual variability** over the Pacific that results from **unstable interactions between the ocean and atmosphere**" (L23 p. 20): the ocean and the atmosphere are **coupled** and the coupled system has its own variability that neither has alone.
- **Global impacts:** El Niño affects weather far from the Pacific through **teleconnections** (a map on L23 p. 22, not seen); there is a 3-D animation of the tropical Pacific cycling through El Niño and La Niña and a slide on the **ENSO observing system** (buoys, satellites; no text).

> [!verify] What the lecture does not say 🔵
> The slides describe the two states and the feedback that sustains **each**, not the process that makes the system **switch** (the recharge or delayed-oscillator mechanism) nor the **forecast** skill; nor how the heat flux of [[CL18 The Ocean as the Climate System's Heat Reservoir]] §3 changes (the upwelling regions are where the air *heats* the ocean: Hartmann p. 129), nor the link to the Indian monsoon ([[CL15 Monsoons]]). Those are recalled topics, **not read** and not stated here as course content.

## Map of this chapter
> [!connection] How CL20 connects
> **Builds on:** [[CL19 Wind-Driven Ocean Circulation]] (equatorial upwelling, thermocline), [[CL18 The Ocean as the Climate System's Heat Reservoir]] (mixed layer, heat flux, bulk stress), [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (trades, ITCZ), [[CL04 Feedback and Multiple Steady States]] (positive feedbacks).
> **Leads to:** [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] (the slow part of the ocean).
> **Concepts:** [[Walker Circulation]] · [[Bjerknes Feedback]] · [[El Nino and La Nina]] · [[Southern Oscillation Index]] · [[ENSO]]
> **Other subjects:** [[Ecology and Evolution - Course Map]] (El Niño and fisheries/population crashes; recalled), [[Probability - Course Map]] ([[PR08 Order Statistics and the Multinomial Distribution]]: ranking events; indices as standardised variables), [[Waves - Course Map]] (equatorial waves, recalled), [[Thermodynamics and Statistical Mechanics - Course Map]] (positive feedback and instability).

## Summary
> [!summary] Cheat-sheet
> - **Mean state:** warm, deep-mixed-layer, convective west; cold-tongue, shallow-thermocline, subsiding east; sea level ~0.5 m higher west; Walker circulation (surface easterlies, upper westerlies).
> - **Bjerknes feedback** (positive): stronger easterlies → stronger SST contrast → stronger convection/low pressure in the west → stronger easterlies.
> - **El Niño:** trades weaken, warm water surges east, thermocline/sea level flatten, upwelling falls, convection and rain move east, Walker cell weakens; **La Niña:** stronger trades, cooler east.
> - **Indices:** Niño = SST anomaly over an eastern-Pacific box; SOI = SLP(Tahiti) − SLP(Darwin), strength of the Walker circulation.
> - **ENSO** = natural interannual variability from unstable ocean–atmosphere interaction; teleconnections give global impacts.

## Practice
1. **Describe.** Contrast west and east of the equatorial Pacific in the mean state (SST, pressure, vertical motion, rain, mixed layer, thermocline).
2. **Feedback.** Write the Bjerknes feedback as a loop with signs and explain why it is a *positive* feedback in El Niño and La Niña alike.
3. **Slope.** Using $\tau=\rho gH\Delta\eta/L$ find the stress for $H=100$ m, $\Delta\eta=0.5$ m, $L=12{,}000$ km; compare with a $6$ m/s wind with $C_D=(0.5+0.071U)\times10^{-3}$.
4. **Thermocline.** With $g'=0.03$ m s⁻², what thermocline displacement accompanies a surface displacement of 0.3 m?
5. **SOI.** Why is the SOI negative in El Niño? What does it measure?
6. **Rain.** In El Niño which of Indonesia and the central Pacific gets more rain, and why?

> [!example]- Solutions
> 1. West: warm SST, low pressure, rising air, cloud and rain, deep mixed layer (~200 m), deep thermocline, higher sea level, convergence/downwelling; east: cool, high pressure, subsidence, dry, shallow mixed layer and thermocline, lower sea level, divergence/upwelling.
> 2. Easterlies ↑ → east–west SST contrast ↑ → convection in the west ↑ and pressure gradient ↑ → easterlies ↑ (loop product positive). In El Niño the same loop runs **backwards** (weaker easterlies → smaller contrast → weaker easterlies): a positive loop amplifies any departure, up or down.
> 3. $1025\times9.81\times100\times0.5/1.2\times10^7=0.042$ N m⁻²; $1.3\times(0.5+0.426)\times10^{-3}\times36=0.043$ N m⁻².
> 4. $\Delta h=g\Delta\eta/g'=9.81\times0.3/0.03=98$ m.
> 5. The Tahiti–Darwin pressure difference measures the east–west pressure gradient driving the Walker circulation; in El Niño pressure falls in the east and rises in the west, so the difference shrinks (SOI negative).
> 6. The central/eastern Pacific, because convection and the warm water move east; Indonesia gets drier (high pressure, subsidence).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | mean state, Walker circulation, Bjerknes feedback, El Niño, 1983 anomaly, Southern Oscillation, La Niña, Niño index, SOI, ENSO definition, teleconnections | [[Lecture23_El Nino Southern Oscillation_251113_133915 (1).pdf]] pp. 2–24 (text layer only; pictures and animations not seen) | taught (2025) |
> | force balance, reduced gravity, Kelvin crossing time | `scripts/cl_neena_numbers.py` (cl20), `scripts/fig_cl16_21.py` | extra/beyond |
> | bulk wind-stress formula | [[05_Optional_Stewart2008_Heat-Budget-Terms-and-Bulk-Formulas_pp53-61.pdf]] (Stewart Table 5.1, (5.10)) | extra/book |
>
> **Notes.** The 15,000 km width, the 150 m layer, the 0.3 % density contrast and the Kelvin-wave speed are **assumptions** of the illustration. The lecture's "El Niño refers to warmer than normal SST over the eastern Pacific" is quoted; the switching mechanism, the forecast and the Indian-monsoon link are not in the folder.
