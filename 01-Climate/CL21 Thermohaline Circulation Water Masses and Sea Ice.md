---
title: CL21 Thermohaline Circulation Water Masses and Sea Ice
aliases: [CL21, thermohaline circulation, deep water formation, NADW, AABW, water masses, T-S diagram, sea ice, brine rejection, Antarctic Circumpolar Current, Southern Ocean, Neena Lecture 24]
subject: climate
type: chapter
chapter: 21
part: V
scope: [taught, extra-book, extra-beyond]
by: [neena, joy, book]
status: draft
prereq: ["[[CL19 Wind-Driven Ocean Circulation]]", "[[CL18 The Ocean as the Climate System's Heat Reservoir]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/neena, src/joy, src/book, status/draft]
---
# CL21 · Thermohaline Circulation, Water Masses and Sea Ice

◀ [[CL20 ENSO and the Walker Circulation]] · [[Climate - Course Map|Course Map]] · (last chapter of Part V)

<span class="scope-taught">taught · in syllabus (2025 Neena L24)</span> <span class="scope-extra-book">extra · book (Joy optional reading)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-07)
> **Neena Lecture 24** (2025: water masses, deep-water formation, sea ice, the Southern Ocean, the thermohaline circulation and its role; 24 slides, text layer only) and the **optional** reading **Hartmann 2016 pp. 227–231** (this year's list; OCR; the Southern Ocean, the Southern-Ocean/North-Atlantic link and the ocean's energy transport). The lecture's figures (SST and salinity maps, the T–S diagram, the conveyor, the sea-ice stages, the ACC map) were **not seen**. The T–S diagram and the density values below use a **linearised teaching equation of state with assumed coefficients** and **illustrative** $(T,S)$ points of mine: the real equation of state is nonlinear (L24 p. 5) and the lecture gives no table. The glacial-cycle role of the deep ocean is only touched here; see [[CL17 Orbital Forcing and Glacial Cycles]].

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught (2025: L24)**
> - §1 the **thermohaline circulation** (definition, speed, depth, time scale); §2 **water masses** (surface, intermediate, deep, bottom), density from $T$, $S$, $P$, **T–S** identification, ¹⁴C age; §3 **sea ice** (anomalous expansion, freezing point, **brine rejection**, stages, stratification), **sites of deep-water formation** (NADW off Greenland, AABW in the Weddell Sea and on the Antarctic shelf), the **Southern Ocean** and **ACC**, **600/1000-yr** time scales, the **climate roles** of the circulation
>
> 🟡 **Extra · book** (optional reading)
> - §4 the Southern Ocean as the **return path** of deep water, its eddies, the link between the North-Atlantic overturning and the Southern-Ocean upwelling, and the carbon cycle (Hartmann pp. 227–231)
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - the brine-rejection **mass balance**; overturning rates implied by the ventilation times; the ¹⁴C numbers; the linearised T–S density table

> [!key] After this chapter you can
> - state what drives the **thermohaline** circulation, its speed, depth and time scale and how it differs from the wind-driven one,
> - read the **T–S diagram** idea of a water mass, and list the four layers of the Atlantic,
> - explain **why sea water behaves differently from fresh water near freezing**, and how **brine rejection** produces dense bottom water,
> - locate the **deep-water formation** sites and say what the **ACC** and the Southern Ocean do,
> - list the **climate roles** of the circulation and why high-latitude **salinity** changes matter.

> [!intuition] The one-sentence story
> The wind stirs the top 200 m; **density** moves the rest. Where the surface becomes cold **and** salty (North Atlantic, the Antarctic shelves, helped by the salt left behind when sea ice forms) the water sinks to the bottom and spreads; elsewhere it must **rise** slowly (mostly in the Southern Ocean), so each parcel of deep water returns to the surface about once in **600 years**. That slow loop stores heat and carbon for centuries and links the two poles.

![[fig_cl21_thermohaline.png]]
*A: a T–S diagram with density contours from a linearised teaching equation of state, and five illustrative water types (§2). B: salinity of the water left after freezing a fraction $f$ of 35 psu seawater (§3). C: the deep overturning as a cartoon after L24's NADW/AABW slide. Numbers: `scripts/cl_neena_numbers.py` (cl21).*

## 1. Two circulations, again
<span class="scope-taught">taught</span> *Neena L24 pp. 2–3: [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=2|p. 2]]*

As in [[CL19 Wind-Driven Ocean Circulation]] §1: the **wind-driven** circulation (fast, ~50 cm/s–4 m/s, surface 50–200 m, ~10 % of the ocean, days to seasons) is forced by **momentum** exchange; the **thermohaline** circulation is driven by **density variations imposed at the sea surface by exchange of heat and fresh water with the atmosphere (buoyancy)**; it is very slow (<1 cm/s), deep (~1000–4500 m), global, covers **~90 %** of the ocean, and has a **time scale of ~1000 years**. The word *thermohaline* = temperature + salinity; "**overturning circulation**" is the modern synonym used in Hartmann's text.

## 2. Water masses
<span class="scope-taught">taught</span> *Neena L24 pp. 4–9: [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=4|p. 4]], [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=8|p. 8]]* · <span class="scope-extra-beyond">extra · beyond</span> *table*

- **Layers of the Atlantic** (L24 p. 4): **surface** water (0–200 m), **intermediate** water (thermocline depth to ~1500 m), **deep** water (to 4000 m), **bottom** water (>4000 m, near the floor).
- **Density** is a nonlinear function of temperature, salinity and pressure; for $-2$ to $30\,^\circ$C and salinity $30$–$37$ the **surface density is $1020$–$1030$ kg m⁻³**; low for **warm and fresh**, high for **cold and salty** water.
- A **water mass** is a body of water with a **common formation history**, identified by its **temperature–salinity** combination. Water masses form **at the sea surface** by air–sea interaction (heating, cooling, evaporation, rain, ice); below the surface layer $T$ and $S$ are **quasi-conservative** (they change only by mixing), so a water mass carries its birth signature through the ocean.
- **Tropical oceans:** density stratification controlled by **temperature** (warm surface over cold deep water). **High latitudes:** controlled by **salinity** (surface water almost as cold as the deep, **fresher** than the deep water).
- **Age:** the ratio **¹⁴C/¹²C** of deep water measures the time since it last touched the surface; **low ratios = "older"** water; **the youngest deep waters are near the Weddell Sea and the Norwegian/Barents Sea**. 🔵 With the half-life of ¹⁴C (5730 yr, recalled), water ventilated 600 yr ago retains $0.5^{600/5730}=0.93$ of the surface ratio, 1000 yr ago $0.89$ (a small signal; real ages come from comparing with other tracers).

> [!example] A T–S table with a teaching equation of state 🔵
> $\rho=1027\,[1-2\times10^{-4}(T-10)+7.6\times10^{-4}(S-35)]$ (coefficients assumed; accurate to a few tenths of a kg m⁻³ near $10\,^\circ$C, 35 psu; wrong near freezing and for large pressure): **tropical surface** ($27\,^\circ$C, 35.5) $1023.9$; **subtropical salty surface** ($25$, 37.0) $1025.5$; **subpolar surface** ($5$, 33.5) $1026.9$; **North Atlantic winter** ($2$, 35.1) $1028.7$; **Weddell shelf brine** ($-1.8$, 34.8) $\mathbf{1029.3}$ kg m⁻³. All fall in the lecture's range $1020$–$1030$; the ordering (warm & fresh lightest, cold & salty densest) is the lecture's.

## 3. Sea ice, brine and the formation of deep water
<span class="scope-taught">taught</span> *Neena L24 pp. 10–20: [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=11|p. 11]], [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=12|p. 12]], [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=15|p. 15]], [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=17|p. 17]], [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=19|p. 19]]*

**The subpolar ocean** (L24 pp. 9–11): low surface temperatures (much cooler SST in the upwelling regions of the cyclonic subpolar gyres); the subpolar front; high precipitation, riverine flux and glacier melt give **low surface salinity**, which keeps the polar ocean **stable**. The **wind-driven** circulation matters here: the northward **Gulf Stream continues as the North Atlantic Drift and the Norwegian Current**, bringing **cold-but-salty** water to the polar ocean (warm subtropical water has lost heat to the air, and in the warm subtropics evaporation exceeds precipitation, so it is salty): in winter the polar cooling then makes it dense enough to sink. (See [[CL19 Wind-Driven Ocean Circulation]] §3 and [[CL18 The Ocean as the Climate System's Heat Reservoir]] §6.)

**Fresh water vs sea water** (L24 pp. 12–14): pure water has its **maximum density ($1000$ kg m⁻³) at $4\,^\circ$C**; cooling from 4 to $0\,^\circ$C is an **anomalous expansion**, which is why lakes freeze from the surface and fish survive below. **Sea water** freezes too, at lower temperature: salinity depresses the freezing point to about **$-1.8\,^\circ$C** (for 35 psu; $0.05$ K per unit of salinity 🔵); at least **15 %** of the ocean is covered by sea ice for part of the year. The density **maximum of sea water lies below the freezing point**: the anomalous expansion is **offset by the salinity** increase when freezing starts.

> [!key] Brine rejection (L24 pp. 14–16)
> In the polar ocean density increases with **salinity** with depth; the stable (fresh) upper layer **restricts convective mixing to a shallow layer**. Once convection has cooled it to a uniform temperature, **freezing commences at the surface**; ice excludes salt: the **dissolved salts are rejected** into the water below ("**brine rejection**"), **raising its salinity and density**. Where sea ice forms, surface density increases and **plumes of dense water sink** to form the deep and bottom water masses.
> **Mass balance** 🔵: freezing a fraction $f$ of seawater of salinity $35$ into ice of salinity $S_i$ leaves water of salinity $S=(35-fS_i)/(1-f)$: $f=0.05$: $36.6$–$36.8$; $f=0.10$: $38.3$ ($S_i=5$) or $38.9$ ($S_i=0$) (**+3.3 to +3.9**); $f=0.20$: $42.5$–$43.8$ (figure B). Only a few per cent frozen already makes the residual water several salinity units saltier than its neighbours, which is why the *rate* of ice formation, not the ice, matters.

**Sites of deep-water formation** (L24 pp. 8, 17–19):
- **North Atlantic Deep Water (NADW)** forms **off the coast of Greenland**; it flows **southward** along the Atlantic basin (at depths of ~2–4 km in the cartoon, 🔵) and joins the AABW.
- **Antarctic Bottom Water (AABW)** forms in the shallow continental-shelf regions of the **Weddell Sea, the Ross Sea and the Adélie Coast**; **persistent winds sweep away the sea ice** (leaving open water that freezes again), favouring more ice formation and more brine. It circles Antarctica and flows north as the **coldest, deepest layer in all three basins** (Atlantic, Pacific, Indian) and **surfaces in upwelling zones**, joining the surface circulation.
- **More than half of the ocean's volume is filled by cold water from these two sources.**
- **The Southern Ocean and ACC** (L24 p. 19): the **southern-hemisphere westerlies** drive the **Antarctic Circumpolar Current**, the most important current of the Southern Ocean, flowing **west to east** at **less than 20 cm s⁻¹**, from the surface to **2000–4000 m**, up to **2000 km wide**; at ~40–60°S it separates the cold Southern Ocean from the Atlantic, Pacific and Indian oceans. 🔵 Using all three maxima together ($0.2$ m s⁻¹, $2000$ km, $3000$ m) gives an **upper bound** of $1200$ Sv; the real transport is an order of magnitude smaller (recalled ≈ 130–150 Sv, **not read**) because the speed is far below the maximum over most of the section.

**Return flow** (Hartmann, optional pp. 227–231): the **Southern Ocean is the key region where deep water returns to the surface**, whereas **upwelling of less dense water** is important in the tropical Pacific, and deep water forms in both the North Atlantic and around Antarctica; hence the North-Atlantic overturning and the Southern-Ocean upwelling are **closely linked**. The wind-driven circulation there raises the **slope of the isopycnals**, which makes the Southern Ocean **vigorously eddying** (horizontal scale ~100 km); the return of deep water means the **warming of the Southern Ocean lags the globe**. In an ice age the strongest westerlies may move equatorward, and **sea ice extending equatorward** may suppress ventilation of the deep ocean and the return of **carbon** to the surface, contributing to lower glacial CO₂; reversing these changes may contribute to the return of CO₂ during interglacials (Hartmann's careful wording: "may"; [[CL17 Orbital Forcing and Glacial Cycles]], [[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]]).

## 4. Time scales and why the circulation matters
<span class="scope-taught">taught</span> *Neena L24 pp. 21–24: [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf#page=21|p. 21]]*

"The thermohaline circulation **brings deep ocean water into contact with the atmosphere every 600 years or so**, and the whole cycle can take **up to 1000 years**." 🔵 For the ocean volume of $\approx1.335\times10^{18}$ m³ (recalled, not in the lectures): renewal in 600 yr needs $71$ Sv, in 1000 yr $42$ Sv (a sum of overturning cells, much larger than the $\sim$15–20 Sv often quoted for the Atlantic cell alone: **recalled**). The lecture lists the **roles** of the circulation:
1. it supplies **heat to the polar regions** ([[CL18 The Ocean as the Climate System's Heat Reservoir]] §7);
2. it affects the **equator-to-pole temperature gradient** and therefore the **atmospheric circulation** ([[CL10 Global Energy Balance and Meridional Structure]]);
3. it influences **polar temperatures and ice formation**, hence the **albedo** and the radiation budget ([[CL04 Feedback and Multiple Steady States]]);
4. it **stores heat and CO₂ in the deep ocean for a very long time** and so adds to the **lag between climate forcing and the planet's response** (the whole ocean has $\sim1500$ times the atmosphere's heat capacity per m², [[CL18 The Ocean as the Climate System's Heat Reservoir]] §5);
5. **small changes in high-latitude surface salinity** (precipitation, evaporation, ice melt, river runoff) can have a **large effect on its strength** (the lecture's closing slide cites the film *The Day After Tomorrow*, 2004: an illustration of the idea, not a forecast).

## Map of this chapter
> [!connection] How CL21 connects
> **Builds on:** [[CL19 Wind-Driven Ocean Circulation]] (Gulf Stream, ACC), [[CL18 The Ocean as the Climate System's Heat Reservoir]] (mixed layer, stratification, salinity, convection), [[CL04 Feedback and Multiple Steady States]] (ice-albedo, multiple states), [[CL17 Orbital Forcing and Glacial Cycles]] (ice ages).
> **Leads to:** the end of Part V; for the ocean in a warming world see the carbon cycle in [[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]] §6.
> **Concepts:** [[Thermohaline Circulation]] · [[Water Mass and T-S Diagram]] · [[Deep Water Formation]] · [[Brine Rejection]] · [[Sea Ice]] · [[Antarctic Circumpolar Current]]
> **Other subjects:** [[Thermodynamics and Statistical Mechanics - Course Map]] ([[TH09 Microstates Macrostates and Multiplicity]], [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]]: freezing-point depression and phase boundaries; density maximum of water), [[Landscapes and Geomorphology - Course Map]] ([[LS14 Glaciers Mass Balance and Ice Flow]], [[LS26 Sea Level and Ocean Waves]]), [[Inorganic Chemistry - Course Map]] (hydrogen bonding in water, the anomalous expansion; [[CH01 VSEPR and Valence Bond Theory]] background), [[Evolution of Earth and Life - Course Map]] (ocean anoxia and ventilation; recalled), [[Eco-Evo - Course Map]] (stratified lakes: [[EE06 Lakes Stratification and Alternative Stable States]]).

## Summary
> [!summary] Cheat-sheet
> - **Thermohaline:** buoyancy-driven, <1 cm/s, 1000–4500 m, ~90 % of the ocean, ~1000 yr; **water masses**: surface/intermediate/deep/bottom; identified by $T$–$S$; $T$, $S$ quasi-conservative below the surface layer; **¹⁴C/¹²C** = age; surface density 1020–1030 kg m⁻³ (nonlinear in $T,S,P$).
> - **Sea ice:** freezing point $\approx-1.8\,^\circ$C; pure-water density maximum at $4\,^\circ$C vs sea water below freezing; **brine rejection** raises $S$ and $\rho$: $S=(35-fS_i)/(1-f)$; dense plumes → deep/bottom water; ≥15 % of the ocean ice-covered seasonally.
> - **Sources:** **NADW** (Greenland), **AABW** (Weddell/Ross/Adélie shelf, ice swept away by winds); > half the ocean's volume; **ACC** west-to-east, <20 cm/s, 2–4 km deep, up to 2000 km wide; Southern Ocean = return of deep water.
> - **Roles:** heat to the poles, equator–pole gradient and atmospheric circulation, ice/albedo, heat and CO₂ storage (**lag**), sensitivity to high-latitude **salinity**; ventilation 600 yr, cycle ~1000 yr.

## Practice
1. **Water mass.** Why does a water mass keep its $T$–$S$ signature below the mixed layer? What happens when two water masses mix?
2. **Density.** With the teaching equation of state compute $\rho$ for $(T,S)=(2\,^\circ\text{C},35.1)$ and $(-1.8\,^\circ\text{C},34.8)$ and say which sinks beneath the other, and by how much.
3. **Brine.** Freeze $10\,\%$ of $35$ psu seawater into ice of salinity $5$: find the remaining salinity and the freezing point (use $0.051$ K per psu).
4. **Overturning.** If the ocean volume is $1.335\times10^{18}$ m³ and all of it is renewed in $600$ yr, what mean flow does that imply (in Sv)? Comment on the comparison with the ACC bound.
5. **Anomalous expansion.** Why do lakes freeze from the top, and why is that argument not enough for the ocean?
6. **Salinity.** Name three processes that raise and three that lower surface salinity, and say which sites form deep water.

> [!example]- Solutions
> 1. Below the surface layer there is no heating, evaporation or rain to change $T$ and $S$, only mixing, so they are quasi-conservative; mixing two masses on a $T$–$S$ diagram gives points on the straight line between them (not exactly in density, because $\rho$ is nonlinear: the denser-than-either result is called cabbeling; recalled).
> 2. $1028.72$ and $1029.27$ kg m⁻³: the Weddell brine is denser by $0.55$ and sinks beneath the North Atlantic winter water (consistent with AABW lying below NADW in the lecture's picture).
> 3. $S=(35-0.5)/0.9=38.33$; freezing point $\approx-0.051\times38.3=-1.95\,^\circ$C.
> 4. $1.335\times10^{18}/(600\times3.156\times10^7)=7.05\times10^7$ m³ s⁻¹ $=71$ Sv, far below the ACC upper bound of $1200$ Sv but larger than the usual Atlantic cell: the overturning is shared among several cells and the renewal time is an average.
> 5. Fresh water is densest at $4\,^\circ$C, so the surface layer cools below $4\,^\circ$C, floats and freezes first; in sea water the maximum density is below the freezing point, so cooling a salty surface layer keeps making it denser and convection continues until the whole mixed layer is at the freezing point; only then does ice form, which then rejects brine.
> 6. Raise: evaporation, sea-ice formation, advection of salty subtropical water; lower: precipitation, river runoff, glacier and ice melt. Deep water forms off Greenland (North Atlantic) and on the Antarctic shelves (Weddell, Ross, Adélie).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | the two circulations, water masses, density, T–S, ¹⁴C, NADW/AABW, subpolar oceans, polar winter cooling, anomalous expansion, freezing point, brine rejection, sea-ice stages, shelf waters, ACC, 600/1000 yr, roles | [[Lecture24_Ocean_Thermohaline circulation_251123_105138 (1).pdf]] pp. 2–24 (text layer only; figures not seen) | taught (2025) |
> | Southern Ocean return of deep water, eddies, link to the North Atlantic, carbon and ice ages, ocean heat transport | [[05_Optional_Hartmann2016_Ocean-Energy-Transport_pp227-231.pdf]] (OCR; read in part) | extra/book (2026, optional) |
> | brine-rejection mass balance, T–S table, overturning rates, ¹⁴C, ACC bound | `scripts/cl_neena_numbers.py` (cl21), `scripts/fig_cl16_21.py` | extra/beyond |
>
> **Notes.** The $T$–$S$ points and the equation of state are **illustrative/assumed**; the ocean volume, the ¹⁴C half-life, the real ACC transport and the cabbeling remark are recalled and not read. The lecture's closing slide about the film is quoted as an illustration only.
