---
title: CL25 The Ocean's Ledger IV - Salt, Density and Water Masses
aliases: [CL25, salt ledger, salinity, E minus P, evaporation minus precipitation, Atlantic saltier than Pacific, Broecker, Bay of Bengal, freshwater lid, potential density, sigma, T-S diagram, brine rejection, katabatic wind, polynya, water mass, NADW, AAIW, AABW, Circumpolar Deep Water, core method, Joy O5]
subject: climate
type: chapter
chapter: 25
part: VI
scope: [taught, extra-book, extra-beyond]
by: [joy, book]
status: draft
prereq: ["[[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]]", "[[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]]", "[[CL21 Thermohaline Circulation Water Masses and Sea Ice]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/joy, src/book, status/draft]
---
# CL25 · The Ocean's Ledger IV: Salt, Density and Water Masses

◀ [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] · [[Climate - Course Map|Course Map]] · ▶ CL26 (planned: the mass ledger and the overturning)

<span class="scope-taught">taught · in syllabus (2026 Joy, O5)</span> <span class="scope-extra-book">extra · book (Stewart 2008, Hartmann 2016: passages read)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> **Primary source: Joy's O5 deck** ("The salt ledger", 22 frames; PDF with speaker notes in `earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf/`), then the **O5 readings I actually read** (Stewart 2008 pp. 77–81 on salinity and E − P; Hartmann 2016 §7.2 pp. 196–200 on seawater; Stewart pp. 222–229 on water masses, T–S plots, the core method and tracers; the first and last parts only, text of the middle figures not used), then the **O5 handout** (read in full). Not read in this pass (cited only as Joy cites them): Stewart pp. 83–88 (σ, potential temperature, neutral density), Stewart Table 13.1 and pp. 224–227 in detail, Hartmann pp. 221–225. This is Joy's **third budget**; Neena's 2025 water-mass lecture is [[CL21 Thermohaline Circulation Water Masses and Sea Ice]], which used a **linearised assumed equation of state and illustrative points**: CL25 gives Joy's real numbers and my validation of an actual equation of state. 🔵 marks my recomputations (`scripts/fig_cl25.py`).

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 from momentum to salt; §2 the **salt ledger** (accountant); §3 where the sea is **salty and fresh**, **E − P**; §4 why the **Atlantic is saltier than the Pacific**; §5 the **Arabian Sea and the Bay of Bengal** (freshwater lid); §6 **what makes seawater heavy** (σ, T–S diagram, warm versus cold water, no 4 °C maximum, brine rejection, katabatic winds and polynyas); §7 why **sinking is rare**; §8 **water masses** (fingerprints, T–S mixing rules, the Atlantic section, NADW, AAIW, AABW, the Pacific)
>
> 🟡 **Extra · book** (passages actually read)
> - Hartmann's density-versus-temperature remarks, the 24.7 g/kg threshold and the halocline that lets sea ice form; Stewart's Broecker passage, the Tomczak definition of a water mass, the T–S argument, the core method and its cautions, the tracer list
>
> 🔵 **Extra · beyond** (my own)
> - an actual equation of state (UNESCO EOS-80, recalled and validated against Joy's TEOS-10 values) used to recompute every σ, α, β and mixing example

> [!key] After this chapter you can
> - explain why salinity is a record of **E − P** and do the accountant's sums,
> - explain why the subtropics are salty, the ITCZ and the high latitudes fresh, why the **Atlantic is saltier than the Pacific**, and the **Bay of Bengal's** freshwater lid,
> - read a **T–S diagram**: density lines, mixing lines, the warm-water (temperature) and cold-water (salt) regimes,
> - say why **sinking is rare** and where it happens, and identify **NADW, AAIW, AABW** from their T–S fingerprints and the Atlantic section.

> [!intuition] The one-sentence story
> Salt never leaves the sea, only water does, so salinity records **evaporation minus rain**; temperature and salt together set density; **warm water is ruled by temperature, near-freezing water by salt**, so deep water forms only where cold *and* salty surface water meets the heavy deep ocean, and each water mass keeps its birth fingerprint for centuries.

![[fig_cl25_salt.png]]
*A: T–S diagram with σ = ρ − 1000 contours from the UNESCO EOS-80 equation of state at surface pressure (recalled, validated against Joy's TEOS-10 values), the freezing line, Joy's water-mass fingerprints (NADW 4 °C/35.0, AAIW 3.3 °C/34.15, AABW 0.4 °C/34.67) and the two surfaces of O6. B: density sensitivity to cooling (ρα) and to salt (ρβ) at S = 35. C: Joy's box means of E − P and surface salinity (slides and handout; not recomputed). Script: `scripts/fig_cl25.py`.*

## 1. From momentum to salt
<span class="scope-taught">taught</span> *O5 deck frame 1; O5 handout §1*

The ledgers come in a chain. To explain the heat budget we needed the momentum budget; momentum is **mass × velocity**, and the mass in a cubic metre of seawater is its **density**, which depends on **temperature, salinity and (slightly) pressure**. We have done heat; now salt. And the hook from the Antarctic Circumpolar Current ([[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] §9): under the current with no coast, deep water comes up: why was it down there?

## 2. The salt ledger: the accountant's hat
<span class="scope-taught">taught</span> *O5 deck frame 2; O5 handout §2* · <span class="scope-extra-book">extra · book</span> *Hartmann p. 196; Stewart p. 80 (as in the handout)*

- **Salinity** is grams of dissolved salt per kilogram of seawater, about **35** on average (Hartmann p. 196, read: the average salinity and temperature of the world ocean are ≈ 34.7‰ and 3.6 °C; Stewart (p. 80) gives S = 34.7 and t = 3.5 °C; Joy's WOCE value 34.72). Hartmann writes ‰, Stewart the practical salinity scale without a unit; "g/kg" is close enough. Salinity ranges only a few per cent at the surface (Joy: half of all water lies between 34.6 and 34.8, Stewart p. 80) but the differences are what matter for density.
- **Water comes and goes, salt stays.** Rivers and rain only add water; land ice only adds it when it melts; sea ice does either (freezing takes water out, melting returns it); evaporation is essentially the only way water leaves. Evaporation and freezing take the water and leave the salt; rivers bring dissolved salt from rock weathering, but that matters only over geological time. So the ocean holds a fixed amount of salt over the timescales here, and the **salinity of the surface ocean is a record of evaporation minus precipitation, E − P** (plus rivers and ice melt).
- **The accountant's sum (Joy's, 🔵 checked).** A 50 m mixed layer at S = 35 that loses 1 m of fresh water a year (E − P ≈ 2.7 mm day⁻¹ = 0.99 m yr⁻¹, subtropical) becomes saltier by $35\times1/50=$ **0.7 g/kg every year**; at 1 mm day⁻¹ it is 0.26 g/kg yr⁻¹. It does not keep rising, so **currents and mixing must carry the salt away as fast as evaporation concentrates it**: that is the ledger balancing.
- **Coupled ledgers** (handout aside): the salt budget cannot be separated from the water budget; rain and evaporation carry latent heat, so it is tied to the heat budget, which is tied to momentum. Each conservation law is simple; the coupled system does things no single budget predicts.

## 3. Where the sea is salty: the data scientist's hat
<span class="scope-taught">taught</span> *O5 deck frames 3–4; O5 handout §3* · <span class="scope-extra-book">extra · book</span> *Stewart p. 77, read: SSS zonal, saltiest at mid-latitudes where evaporation is high, fresher near the equator (rain) and at high latitudes (melted sea ice)*

Where should the sea be saltiest? Evaporation high, rain low:
- **The subtropics win twice**: clear skies let sunlight through and the sinking Hadley air is very dry, so evaporation is high and rain low.
- **The ITCZ loses twice**: clouds block much of the sunlight and the air is already humid.
- **High latitudes are fresh**: vapour carried poleward rains out, cold air holds little vapour (Clausius–Clapeyron) so evaporation is small, and rivers and melting ice add fresh water.

Joy's box means (WOCE salinity, OAFlux − GPCP E − P 2010–2020; **not recomputed**, figure C):

| Place | E − P (mm day⁻¹) | Surface salinity (g/kg) |
|---|---|---|
| North Atlantic subtropics, 20–30°N, 50–30°W | +2.8 | 37.2 |
| South Pacific subtropics, 25–15°S, 130–100°W | +3.3 | 36.2 |
| East Pacific under the ITCZ, 5–10°N, 130–90°W | −3.9 | 33.8 |
| West Pacific warm pool, 5°S–5°N, 140–170°E | −3.6 | 34.5 |

The Mediterranean and Red Sea sit in the subtropics with little river water and are very salty; the largest river sources of fresh water are the Amazon and the Ganga–Brahmaputra (handout).

## 4. Why the Atlantic is saltier than the Pacific
<span class="scope-taught">taught</span> *O5 deck frames 5–6; O5 handout §4* · <span class="scope-extra-book">extra · book</span> *Stewart pp. 78–79, read*

Between 30°S and 60°N the surface salinity averages **35.6 (Atlantic) against 34.6 (Pacific)** (Joy, WOCE). The reason is in the atmosphere. Stewart (p. 78, read): because many large rivers drain into the Atlantic and the Arctic, why is the Atlantic saltier? Broecker (1997) showed that **0.32 Sv** of the water evaporated from the Atlantic does not fall as rain on land but is **carried by winds into the Pacific**; "the quantity is small, equivalent to a little more than the flow in the Amazon River" and "were this flux not compensated by an exchange of more salty Atlantic waters for less salty Pacific waters, the salinity of the entire Atlantic would rise about **1 gram per liter per millennium**". The trade winds blow from the Atlantic towards the Pacific and only the narrow Isthmus of Panama stands in the way (the Panama Canal plays no part: the transfer is in the air). Joy's E − P check (30°S–60°N): Atlantic **+1.1 mm day⁻¹**, Pacific **+0.2** (basin masks rough; not recomputed). The result depends on where the continents are today. **Keep it: O6 needs it.** (The Atlantic's exchange of salty for fresh water is carried by the ocean circulation, the next chapter.)

## 5. Close to home: the Arabian Sea and the Bay of Bengal
<span class="scope-taught">taught</span> *O5 deck frames 7–9; O5 handout §5*

Same latitude (10–20°N), same monsoon, different ledgers (Joy's box means):

| | Arabian Sea (60–70°E) | Bay of Bengal (83–93°E) |
|---|---|---|
| surface salinity | **36.2** | **32.9** (a 3 g/kg contrast side by side is rare in the world ocean) |
| E − P (mm day⁻¹) | **+2.6** (deck: +2.5) | **−1.1**, *plus the rivers* |
| surface σ (kg m⁻³) | 23.4 (🔵 23.5) | 20.7 (🔵 20.7) |

The Bay is fresh because the Ganga–Brahmaputra and others (Irrawaddy, Mahanadi) drain into it and monsoon rain falls on it; the Arabian Sea is salty because little river water reaches it, evaporation is high and the subsiding monsoon air suppresses rain there (the subtropical recipe again; slide notes flag the Red Sea/Persian Gulf outflows and the river details as general knowledge, ⚠ not from a course reading). The difference goes down to at least 500 m in salinity, but **below ≈ 200 m the densities are the same** (σ 26.15 and 26.14 at 200 m: temperature makes up the difference); above, the Bay's water is much lighter.

**A freshwater lid.** Fresh water poured gently on salt water stays separate; the Bay does this all the time. The wind's stirring stops at a strong density step ([[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §4), so the Bay's mixed layer stays shallow and the sunlight's heat is spread over a thin layer: the surface stays warm (WOCE annual mean **28.3 °C against 27.5 °C** though both get comparable sunlight). Warm water feeds the air with heat and vapour; most North Indian Ocean tropical cyclones form over the Bay (the IMD also cites the Arabian Sea's stronger shear, and some Bay storms are remnants of Pacific typhoons: handout, general knowledge). Which comes first, the rain or the warm fresh Bay? **Both**: rain and rivers make the lid, the lid keeps the surface warm, a warm surface favours more rain: a feedback, one more way the budgets are coupled.

## 6. What makes seawater heavy: the physicist's hat
<span class="scope-taught">taught</span> *O5 deck frames 10–14; O5 handout §6 and "Read this part"* · <span class="scope-extra-book">extra · book</span> *Hartmann pp. 196–200, read*

**σ.** Seawater is always within a few per cent of 1,000 kg m⁻³ (surface water ≈ 1,027), so one quotes $\sigma=\rho-1000$ (Hartmann p. 199: "usually reported as a deviation from 1000 kg m⁻³"). **Potential density** $\sigma_\theta$ is the density the sample would have brought to the surface without exchanging heat, so that waters from different depths can be compared (Hartmann p. 199; Joy: all densities here are of this kind). On a **T–S diagram** (figure A) lines of equal σ curve across; **colder (down) or saltier (right) is denser**. Hartmann: "salinity and temperature variations have roughly equal importance for density variations in the ocean" (p. 196).

**The two regimes** (🔵 from EOS-80, Joy's TEOS-10 values in brackets; S = 35, surface pressure):

| | at 25 °C | at 0 °C |
|---|---|---|
| density change per K of cooling | **+0.304** kg m⁻³ [0.30] | **+0.054** [0.054] |
| density change per g/kg of salt | +0.756 [0.74] | +0.808 [0.80] |
| cooling equal to +1 kg m⁻³ | **3.3 K** [3.3] | **18.5 K** [18] (impossible: it freezes first) |
| salt equal to +1 kg m⁻³ | 1.32 g/kg [1.4] | **1.24 g/kg** [1.2] |
| 1 g/kg of salt is worth | 2.5 K of cooling [2.4] | 15 K |

- **Warm water: temperature does most of the work** (density very sensitive to T, and surface temperatures span tens of degrees while salinity varies a few g/kg); the density lines lie flat.
- **Cold water: salt decides.** Near freezing cooling is ≈ 5.6× weaker, the lines stand almost upright.
- **No 4 °C maximum in the ocean.** Fresh water is densest at 4 °C (so a lake cools until all of it is at 4 °C, then freezes from the top, keeping 4 °C water at the bottom where fish survive). **Seawater with salinity greater than 24.7 g/kg has no such maximum**: it keeps getting denser all the way to freezing (Hartmann p. 197, read), at **−1.92 °C for S = 35** (🔵 EOS-80 −1.92). So the coldest seawater is also the densest.
- **A puzzle and its answer.** If cooling always makes seawater denser, the whole column would have to cool to freezing before ice could form. Sea ice forms anyway because at high latitudes the surface is **fresher** than the water beneath (rain, rivers, melting ice make a **halocline**): the fresh water stays on top even when colder, and only that thin layer must reach freezing (Hartmann pp. 197–198, read; he notes that diverting some big rivers from the Arctic could in principle upset the thin ice cover).
- **Brine rejection.** Sea ice is almost fresh; the salt is pushed out as **brine** into the water below, making it saltier and (cold: salt decides) so dense that it can no longer stay at the surface.
- **Katabatic winds and polynyas** (handout §7): the Antarctic ice sheet cools the air in contact with it; cold dense air flows downhill off the dome over the sea (a katabatic wind), chilling the water and blowing new sea ice offshore, leaving open water (**polynyas**) where more ice forms quickly and rejects more brine (Hartmann p. 224, as Joy cites it). The result is the **densest water in the ocean**, made against the Antarctic coast. (Neena's CL21 §3 gives the same brine-rejection story with an illustrative mass balance.)

## 7. Why sinking is rare
<span class="scope-taught">taught</span> *O5 deck frames 15–16; O5 handout §7 and "How rare dense surface water is"*

Hartmann p. 225 (as Joy cites it): **75 %** of the ocean's volume has potential density above σ = **27.4**, but only **4 %** of the surface water is that dense. Joy's WOCE check: **78 %** of the volume, only **1.4 %** of the surface in the annual mean (Hartmann's 4 % includes winter, when the dense patches are largest). So deep water forms in only a few places and only in winter: the **Mediterranean and Red Sea** (extremely salty; their water sinks within those seas and spills out at middle depths), the **far North Atlantic near Greenland**, and a few patches **close to Antarctica** (cold and salty, §6). Everywhere else the ocean is **light water on heavy**: the stratification that stopped the wind's stirring ([[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §4). The link between the upper few hundred metres (mixed layer, Ekman transport, gyres) and the deep ocean is **density**, and at high latitudes that means **salt**.

## 8. Water masses: fingerprints of where water has been
<span class="scope-taught">taught</span> *O5 deck frames 17–22; O5 handout §8 (longer than the class time)* · <span class="scope-extra-book">extra · book</span> *Stewart pp. 222–229, read in part*

**One place, top to bottom** (WOCE, 30°S 25°W; handout):

| Depth | T (°C) | S | |
|---|---|---|---|
| surface | 22.1 | 36.0 | warm and salty: the subtropics |
| 200 m | 15.2 | 35.5 | cooler, still salty |
| ≈ 900 m | 4.2 | 34.3 | a **salinity minimum** |
| ≈ 3,000 m | 2.4 | 34.9 | a **salinity maximum** |
| 4,750 m (bottom) | 0.8 | 34.8 | the coldest water |

Temperature falls all the way down but salinity goes down, up, down: these are **layers that came from different places**. T and S are set only at the surface (heating, cooling, rain, evaporation, freezing); below the mixed layer they change only by **mixing** with neighbours, which in the deep ocean is very weak (Stewart p. 223, read: "water properties… are formed only when the water is at the surface or in the mixed layer… once the water sinks below the mixed layer temperature and salinity can change only by mixing with adjacent water masses"). So a parcel carries its birth T and S for decades to centuries; such **conservative** properties are why oceanographers plot T against S rather than depth. (Oxygen is only partly conserved: respiration uses it. Stewart's tracer list: salinity, oxygen, silicates, phosphates, ³He, tritium with half-life 12.3 yr, fluorocarbons, SF₆; the absence of tritium south of 30°N after 25 years implies a mean flow of **under a mm s⁻¹**; p. 228, read.)

**What a water mass is.** The concept comes from meteorology (Bjerknes' air masses and fronts). Tomczak's definition quoted by Stewart (p. 223, read): a **body of water with a common formation history, having its origin in a physical region of the ocean**; in its formation region it has exclusive occupation of a part of the ocean, elsewhere it shares the ocean with other water masses with which it mixes. Three rules for reading a T–S diagram (handout, Stewart pp. 224):
- mixing two water masses gives a **straight line** between their points (🔵 to first order); a 50–50 mix sits halfway;
- mixing three gives two lines meeting at a corner, which further mixing rounds off (the kinks of the 30°S profile);
- **mixing makes water denser** (the σ lines curve): 🔵 a 50–50 mix of AAIW and NADW is only 0.001 kg m⁻³ denser than the mean of the two (the two are nearly on a straight σ line), but for a warm–cold pair of equal σ (0 °C/34.0 and 20 °C/38.3, σ = 27.30) the mixture is **0.56 kg m⁻³ denser than either**: mixing alone can make water sink (cabbeling).

**The core method** (Stewart pp. 225–227, read in part): follow a property's maximum or minimum (the core) back to where it is strongest, usually near where it formed. It works for a tracer that does not influence density (**salinity**, not temperature: "if the tracer controls density then flow will be around the core according to ideas of geostrophy, not along core"); it works especially well in the South Atlantic. Cautions (Stewart pp. 226–227): slow drift and sideways mixing leave the same pattern, so the method cannot tell them apart; the water moves mostly along surfaces of constant density, not literally along the arrows; the flow in the plane perpendicular to the figure may be at least as strong.

**The Atlantic section** (salinity along 30°W, Antarctica to Greenland; slide frames 18–20): a **salty tongue at 2–3 km** from the far North Atlantic spreading south; a **fresh tongue at ≈ 1 km** from near 50°S spreading north; under both the **coldest, densest water**, from around Antarctica.

| Water mass | Where and how it forms | Fingerprint (Joy, Stewart Table 13.1) | Goes |
|---|---|---|---|
| **North Atlantic Deep Water (NADW)** | Norwegian, Greenland and Labrador Seas; Gulf Stream carries warm salty water north, very cold winter air cools it until it sinks: **cooling of salty water, not brine** | ≈ 4 °C, 35.0 (🔵 σ 27.79); in the 30°W section a salinity maximum 34.8–35.0 at ≈ 1,750–3,000 m, 20°N–40°S | south at 2–3 km, then into the Southern Ocean where, mixed with deep water from the other oceans, it becomes **Circumpolar Deep Water** carried round all three oceans by the ACC |
| **Antarctic Intermediate Water (AAIW)** | Southern Ocean near 50–55°S at the Antarctic Polar Front: rain exceeds evaporation and melting ice adds fresh water; pushed down in winter on the northern edge of the ACC: **Ekman convergence equatorward of the westerlies** ([[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] §7) | ≈ 3.3 °C, 34.15 (🔵 σ 27.18); section minimum 34.2–34.5 at 700–900 m from 40°S to the equator | north at ≈ 1 km, fading by 10–20°N |
| **Antarctic Bottom Water (AABW)** | Antarctic continental shelves in winter, mostly Weddell and Ross Seas: katabatic winds, polynyas, brine | ≈ 0.4 °C, 34.67 (🔵 σ 27.82); −0.1 °C and 34.67 at 40°S, −0.7 °C at 4,000 m near the Weddell Sea | north along the floor, 50°S to 30°N in the Atlantic, and into the Indian and Pacific deep basins |

AABW is **colder and denser but not saltier** than NADW: cold water's density depends mostly on salt, but AABW is so cold it is denser anyway (🔵 σ 27.82 against 27.79: 0.03 kg m⁻³). Two more masses (handout): **Mediterranean Water** (35.95 and 9.8 °C at 1,100 m west of Gibraltar, the orange blob near 35°N at 1 km) and **central water** (warm salty subtropical upper few hundred metres, pushed below the surface by Ekman pumping in the gyres: Stewart's Table 13.1 lists one at 18 °C and 35.9). **The stack**: central water, AAIW, NADW, AABW on the floor, "syrups of different densities in one glass"; each keeps its identity over thousands of kilometres and centuries because the interior mixes so weakly (motion nearly adiabatic along density surfaces, Hartmann p. 225 as cited). Air masses are stirred away in days to weeks; water masses last far longer.

**The Pacific is different** (slide frame 21): the section along 165°W has the fresh intermediate water and the Antarctic bottom water but **no salty tongue from the north**: the North Pacific forms no deep water (Hartmann p. 199–200, read: potential density in the North Atlantic is greater than in the North Pacific, especially near the surface, "because the Atlantic Ocean is more saline"; "deep water can be formed in the Southern Ocean poleward of 50°S, and in the North Atlantic, but not in the North Pacific at the present time"). Why, when it gets just as cold? The answer is §4: the Atlantic exports fresh water to the Pacific. → CL26.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: T–S diagram: what makes seawater heavy, and why mixing sinks
> Seawater density from the UNESCO EOS-80 equation of state at surface pressure, drawn as lines of equal σ = ρ − 1000 kg m⁻³ on a temperature–salinity diagram.
>
> ![[cl_ts_density.png|720]]
>
> **Try:** Sample A = 0 °C, S = 34.0 and B = 20 °C, S = 38.3 (σ = 27.30 for both): the 50 % mixture is 0.56 kg m⁻³ denser than either. Then put A at the AAIW point (3.3 °C, 34.15) and B at NADW (4 °C, 35.0): the excess is only 0.001. Set S = 32.8 and cool to the freezing line: σ stays near 26.4, never the 27.7 of the deep Pacific.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_ts_density.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_ts_density.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL25 connects
> **Builds on:** [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] (Ekman pumping pushes water down in the gyres and pulls it up round Antarctica), [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] (stirring versus stratification), [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] (Neena's lecture: layers, ¹⁴C, sea ice, brine mass balance; its equation of state is only illustrative), [[CL15 Monsoons]] (the Arabian Sea).
> **Leads to:** CL26: where water sinks, how it comes back up (the Southern Ocean), how long the round trip takes, and whether it can switch off.
> **Concepts:** [[Water Mass and T-S Diagram]] · [[Brine Rejection]] · [[Sea Ice]] · [[Thermohaline Circulation]] · [[Deep Water Formation]] · [[Evaporation Minus Precipitation]] · [[Potential Density]] · [[North Atlantic Deep Water]] · [[Antarctic Intermediate Water]] · [[Antarctic Bottom Water]] · [[Katabatic Wind and Polynya]] · [[Seawater Salinity]]

## Summary
> [!summary] Cheat-sheet
> - Salt stays, water goes: **S records E − P**. Mean S ≈ 34.7; 50 m, 1 m yr⁻¹ ⇒ +0.7 g/kg yr⁻¹ (carried away by currents).
> - Subtropics salty (E − P > 0: clear, dry, sinking air), ITCZ fresh; Atlantic 35.6 vs Pacific 34.6 because 0.32 Sv (≈ Amazon) is carried across Central America (1 g/L per millennium otherwise). Arabian Sea 36.2 vs Bay 32.9; σ 23.4 vs 20.7: freshwater lid, warm shallow Bay.
> - σ = ρ − 1000. **Warm: T rules** (0.30 kg m⁻³ K⁻¹ vs 0.74 per g/kg); **cold: salt rules** (0.054 vs 0.80). No 4 °C maximum for S > 24.7; freezing −1.92 °C. Brine rejection + katabatic winds + polynyas ⇒ densest water.
> - 75 % of the volume has σ > 27.4, 4 % (1.4 % annual) of the surface does: sinking is rare.
> - Water masses: conservative T, S. NADW 4 °C/35.0 (2–3 km, south), AAIW 3.3/34.15 (≈ 1 km, north), AABW 0.4/34.67 (bottom, densest, not saltiest). Mixing ⇒ straight lines, corners; cabbeling. Core method works with salinity.

## Practice
1. **Ledger.** A 50 m mixed layer at S = 35 loses 1 mm day⁻¹ of fresh water. How fast does it get saltier, and why does it not keep doing so?
2. **Which matters more?** For 25 °C water (S = 35), compare warming by 2 °C with a rainstorm that freshens the mixed layer by 0.5 g/kg. (Joy's question; use the table.)
3. **AABW below NADW.** AABW is less salty than NADW yet lies beneath it. Explain with the slope of the σ lines. (Joy's question.)
4. **A sample.** Water at 1 km depth, 10°S in the Atlantic, S = 34.4, T = 5 °C. Which water mass is it mostly, and roughly where did it last touch the surface? (Joy's question.)
5. **Mixing.** Draw a T–S diagram for two water masses mixed in equal parts and use the curvature of the σ lines to show the mixture is denser than either. (Joy's question.)
6. **ITCZ.** The ITCZ moves north and south with the seasons. What do you expect for surface salinity at 5°N over a year? (Joy's question.)
7. **Sea ice.** Sea ice forms in winter and melts in summer. Over a full year does it change the salt ledger of the polar ocean? Where might the answer differ if the ice is blown away from where it formed? (Joy's question.)
8. **A lid.** Why does a freshwater lid make the surface warmer rather than spreading the same heat over a deeper layer and leaving the total unchanged? (Joy's question.)

> [!example]- Solutions
> 1. $\Delta S=35\times(1\ \text{mm/day}\times365.25)/50\ \text{m}=0.26$ g/kg per year (🔵). It does not keep rising because currents and mixing carry salt away as fast as evaporation concentrates it (and rain, rivers and ice melt offset it elsewhere).
> 2. Warming 2 °C: $\Delta\rho=-0.62$ kg m⁻³ (🔵); freshening 0.5 g/kg: $-0.38$ kg m⁻³. **Warming wins** (temperature rules in warm water: $\rho\alpha=0.30$ vs $\rho\beta=0.76$ but T changes by 2 K against 0.5 g/kg).
> 3. NADW (4 °C, 35.0) σ = 27.79; AABW (0.4 °C, 34.67) σ = 27.82 (🔵). Going from NADW to AABW: cooling by 3.6 K at S = 35 adds +0.30 kg m⁻³ and freshening by 0.33 g/kg subtracts 0.27 kg m⁻³ (🔵), net +0.03: the cold wins narrowly. On the T–S diagram the σ lines lean over to the right as T falls, but cooling still moves a point onto a higher σ line faster than the small loss of salt lowers it, so AABW (below and to the left of NADW) sits on a slightly higher σ line.
> 4. S = 34.4 lies between AAIW (34.15) and NADW (35.0): fraction of NADW ≈ (34.4 − 34.15)/(35.0 − 34.15) = 0.29, so **mostly AAIW**, which last touched the surface near **50–55°S at the Antarctic Polar Front**; the temperature of 5 °C is warmer than both end-members' linear mix (≈ 3.5 °C), so it also has some warmer (central) water: salinity, which does not influence density as much, is the better tracer.
> 5. Pick two points on one σ line; the straight line between them lies on the denser side of that line because σ lines are concave. 🔵 Example: 0 °C/34.0 and 20 °C/38.3 (σ = 27.30) mix to 10 °C/36.15 with σ 27.86: +0.56 kg m⁻³.
> 6. The rain band is at about 5–10°N in the east Pacific: when the ITCZ is over 5°N, rain freshens the surface (low S); when it moves south, E − P at 5°N rises and S increases, so a seasonal salinity swing with a fresh phase when the ITCZ is overhead (a lag from the mixed layer is expected).
> 7. Over a full year freezing and melting cancel if the ice melts where it formed. If the ice is blown away and melts elsewhere, salt is exported from where it formed (more brine, saltier and denser there, as in a polynya) to where it melts (fresher): a redistribution, a net salt source at the formation site and sink at the melting site.
> 8. The lid makes the density step strong, so the wind's mixing stops at it (stirring against stratification): the same sunlight heats a **thinner** layer, whose temperature rises more, and a shallower mixed layer means a smaller $C$ ([[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]]); the heat is not "spread over a deeper layer" because nothing mixes it down.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | the salt ledger, salty/fresh maps and E − P boxes, Atlantic–Pacific, Arabian Sea–Bay of Bengal, density, T–S, α and β, no 4 °C maximum, brine, sinking rarity, fingerprints, Atlantic and Pacific sections, water-mass names | O5 deck, 22 frames ([[O5_The-salt-ledger.pdf]]; speaker notes in the `_with-notes` version) | taught (2026) |
> | everything above in prose, the 30°S profile, water-mass table with Stewart Table 13.1 fingerprints, katabatic winds, questions | [[handout_o5.md]] (read in full) | taught (2026) |
> | Broecker/0.32 Sv, mean S 34.7, SSS zonal pattern | Stewart 2008 pp. 77–79 (`transcripts/readings/O5__01…`, read in part) | extra/book (2026) |
> | density, 24.7, halocline, sea ice, σ, potential density, North Atlantic vs North Pacific | Hartmann 2016 pp. 196–200 (`O5__02…`, OCR, read) | extra/book (2026) |
> | water-mass definition, T–S, core method, tracers, 1 mm s⁻¹, RAPID (24°N), ACC | Stewart 2008 pp. 222–229 (`O5__04…`, read in part) | extra/book (2026) |
> | all 🔵 numbers: EOS-80 density, α, β, σ of the two seas and the water masses, mixing examples | `scripts/fig_cl25.py` | extra-beyond |
>
> **Notes.** The EOS-80 polynomial and the freezing-point formula are **recalled, not read**; they reproduce Joy's TEOS-10 values (freezing point −1.92 °C, ρα 0.304 and 0.054, σ 26.4 for the N Pacific, 20.7 for the Bay) to 2–3 %, and are labelled 🔵 throughout. The salinity/E − P box means, the 4 %/1.4 % and 75 %/78 % figures and the section values are Joy's (WOCE, OAFlux, GPCP, TEOS-10) and were not recomputed. Not read: Stewart pp. 83–88, Table 13.1 (values as in the handout), Hartmann pp. 221–225, Broecker (1997).
