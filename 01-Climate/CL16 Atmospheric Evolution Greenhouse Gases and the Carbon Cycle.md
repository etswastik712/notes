---
title: CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle
aliases: [CL16, atmospheric evolution, secondary atmosphere, atmospheric escape, greenhouse gases, carbon cycle, biogeochemical cycles, runaway greenhouse, Neena Lecture 4, Neena Lecture 6]
subject: climate
type: chapter
chapter: 16
part: V
scope: [taught, extra-beyond]
by: [neena]
status: draft
prereq: ["[[CL08 Greenhouse Models]]", "[[CL05 Thermodynamic State of the Atmosphere]]", "[[CL04 Feedback and Multiple Steady States]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/neena, status/draft]
---
# CL16 · Atmospheric Evolution, Greenhouse Gases and the Carbon Cycle

◀ [[CL15 Monsoons]] · [[Climate - Course Map|Course Map]] · ▶ [[CL17 Orbital Forcing and Glacial Cycles]]

<span class="scope-taught">taught · in syllabus (2025 lectures, Neena)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-07)
> The folder `earth-and-climate/climate/lecture-notes-slides/ec2113_neena/` holds the **2025 course** (Neena taught EC2113 *until last year*; this year it is Argha, Suhas and Joy, see `instructors info.txt`: "make sure none of the context is missed … add parts which are specific to last year and ofc this year"). The folder was not used by earlier chapters (CL01–CL15 are built on Argha, Suhas and the books), so this chapter and CL17–CL21 add what is **specific to the 2025 lectures**. Here: **Lecture 4** (atmospheric composition and evolution) and **Lecture 6** (greenhouse-gas absorption, water vapour, carbon cycle, methane, nitrous oxide, Venus). Overlaps are kept short and point to the chapters that already cover them: molecular absorption and the greenhouse effect ([[CL07 Optical Properties of the Atmosphere]], [[CL08 Greenhouse Models]]), the one-layer models of Lectures 3–4 and the Tutorial 2 problems ([[CL08 Greenhouse Models]] Practice), composition and scale height ([[CL05 Thermodynamic State of the Atmosphere]], [[CL06 Hydrostatic Balance and Vertical Structure]]), silicate weathering and the snowball ([[CL04 Feedback and Multiple Steady States]]). Slides are **text-layer PDFs**; the figures on them (the carbon-cycle diagrams, the planet comparison) were not seen as images, only their text. Whether the 2025 syllabus is this year's syllabus is **not stated**: treat "taught" as *taught in 2025*.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught (2025: Lectures 4 and 6)**
> - §1 mass distribution of the atmosphere, permanent/variable gases, aerosols, homosphere/heterosphere; §2 the **escape criterion** ($v_\text{thermal}>\tfrac16v_\text{esc}$: Earth loses H, holds H₂O; Mars loses H₂O, holds CO₂); §3 **atmospheric evolution** (primary, secondary atmosphere, volcanic outgassing, reduced early gases, oceans, weathering, photosynthesis, ozone), Venus–Earth–Mars; §4 **molecular absorption** needs an oscillating dipole; §5 water vapour, CO₂, CH₄, N₂O (shares of the greenhouse effect, lifetimes, potency); §6 **biogeochemical and carbon cycle** (inorganic, organic, short- and long-term, natural and human sources and sinks), §7 runaway greenhouse on Venus
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 the escape calculation with numbers (thermal speeds at an assumed 1000 K); §5 decay curves of the lifetimes and the Clausius–Clapeyron rate; §3 the Venus/Earth/Mars one-layer comparison

> [!key] After this chapter you can
> - say which gases a planet can keep and apply the **one-sixth escape rule** with numbers,
> - narrate the **evolution** of Earth's atmosphere (primary → secondary → today) and say what changed it (outgassing, oceans, weathering, life),
> - explain **why only some molecules absorb infrared** (a changing dipole moment),
> - rank the **greenhouse gases** by their share, lifetime and potency, and compute the fraction left after a time $t$,
> - draw the **inorganic and organic carbon cycles**, separate short-term from long-term cycling and say what the 200-Myr residence time means,
> - explain why Earth's CO₂ is in rocks and Venus's in the air.

> [!intuition] The one-sentence story
> An atmosphere is a **balance of sources and sinks** that has been shifting for 4.6 billion years: volcanoes pour gas in, the sea and the rocks take it out, life turns it over, and the planet's gravity and temperature decide what leaks to space. The greenhouse gases are the ones that have a **dipole to shake** in the infrared; their abundance is set by cycles (water: days, methane: a decade, CO₂: a decade to millions of years), and the slowest cycle, **weathering against volcanism**, is the planet's thermostat.

![[fig_cl16_atmosphere.png]]
*A: mean thermal speeds against one sixth of the escape speed (§2, assumed temperature 1000 K). B: lifetimes as exponential decay (§5). C: the one-layer model for Mars, Earth and Venus: it reproduces Earth within 15 K and misses Venus by 460 K (§3). Numbers: `scripts/cl_neena_numbers.py` (cl16), `scripts/fig_cl16_21.py`.*

## 1. What the atmosphere is made of
<span class="scope-taught">taught</span> *Neena L4 pp. 5–10: [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf#page=6|p. 6]], [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf#page=9|p. 9]], [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf#page=10|p. 10]]*

- **Mass:** air density and pressure fall exponentially with height; **99 %** of the atmospheric mass lies below **32 km** and **99.999 %** below **80 km** (L4 p. 6). *Check* 🔵: with $p\propto e^{-z/H}$ and $H=7$ km, $1-e^{-32/7}=0.9897$ and $1-e^{-80/7}=0.999989$; with $H=7.5$ km $0.9860$ and $0.999977$: the slide's numbers are the right order for a scale height of about $7$ km ([[CL06 Hydrostatic Balance and Vertical Structure]]). If the whole mass were spread uniformly the sea-level pressure would be $1013$ hPa $=1$ atm; that corresponds to $5.27\times10^{18}$ kg of air.
- **Constituents:** *permanent gases* (constant proportion: N₂ 78 %, O₂ 21 %), *variable gases* (water vapour, CO₂, O₃…), and **aerosols**, suspended particles with diameters $10^{-9}$–$10^{-4}$ m (desert dust, sea salt, smoke, volcanic ash, volatile organics from vegetation), excluding cloud droplets (L4 p. 9; compare [[CL07 Optical Properties of the Atmosphere]]).
- **Homosphere / heterosphere** (L4 p. 10): turbulent mixing keeps the composition uniform up to $\sim80$–$100$ km (*homosphere*); above that molecules **separate by weight** (heavy ones settle low, H₂ and He float to the top: *heterosphere*). Zettel: [[homosphere-and-heterosphere]].

## 2. Which gases can a planet keep?
<span class="scope-taught">taught</span> *Neena L4 p. 11: [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf#page=11|p. 11]]* · <span class="scope-extra-beyond">extra · beyond</span> *numbers*

> [!key] The escape criterion (L4 p. 11)
> The composition of a planet's atmosphere is set by its **gravity and escape velocity**. If the mean speed of the gas molecules in the outer atmosphere exceeds **1/6 of the escape velocity**, they escape in significant amounts. "Earth can thus lose hydrogen but hold water. Mars can lose water but hold CO₂."

**Why one sixth?** Molecular speeds follow the Maxwell distribution ([[SM04 Kinetic Theory and the Boltzmann Equation]], [[Maxwell-Boltzmann Distribution]]): even if the *mean* speed is well below $v_\text{esc}$, a **tail** of fast molecules exceeds it, and over geological time the tail is replenished by collisions. The factor $\frac16$ (the lecture's rule of thumb; the full Jeans calculation is not in the lecture) says that when $\bar v\approx v_\text{esc}/6$ the tail has been drained over the age of the planet. The mean speed is $\bar v=\sqrt{8k_BT/\pi m}$, so lighter molecules escape first.

> [!example] The rule in numbers 🔵
> At an assumed **exospheric temperature of 1000 K** (my assumption: the lecture states no temperature):
>
> | gas | $m$ (u) | $\bar v$ (m/s) | lost by Earth ($v_\text{esc}/6=1864$ m/s)? | lost by Mars ($838$ m/s)? | Venus ($1727$ m/s)? |
> |---|---|---|---|---|---|
> | H₂ | 2.016 | 3241 | **yes** | yes | yes |
> | He | 4.003 | 2300 | **yes** | yes | yes |
> | H₂O | 18.02 | 1084 | no | **yes** | no |
> | N₂ | 28.01 | 869 | no | marginal (869 vs 838) | no |
> | CO₂ | 44.01 | 694 | no | **no** | no |
>
> with $v_\text{esc}=11.19,\ 5.03,\ 10.36$ km/s for Earth, Mars, Venus. The lecture's two statements come out: Earth keeps H₂O and loses H₂; Mars loses H₂O and holds CO₂. The result is **sensitive to $T$**: at $1500$ K the mean speed of CO₂ is $850$ m/s, just above Mars's threshold, so "holds CO₂" is a statement about *the order of magnitude*, not a sharp line. Only the ratio $v_\text{esc}/\bar v$ matters: **$v_\text{esc}^2\propto M/R$**, so a heavy, cold planet keeps light gases (Jupiter keeps H₂), a small, hot one loses almost everything.

## 3. How the atmosphere evolved
<span class="scope-taught">taught</span> *Neena L4 pp. 12–15: [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf#page=12|pp. 12–14]], [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf#page=15|p. 15]]* · <span class="scope-extra-beyond">extra · beyond</span> *planet comparison numbers*

**The story on the slides (L4 pp. 12–14):**
1. **Primary atmosphere** (impact degassing, the *Hadean*, 4.6–4 Ga): H₂ and He, lost to space under the high temperatures; they *still* escape.
2. **Secondary atmosphere** from **volcanic outgassing**. Present-day volcanic gas: **80–90 % H₂O, 6–12 % CO₂, 1–2 % SO₂**, traces of H₂, N₂, CO, NH₃, CH₄. The young crust and mantle were **less oxidised**, so the early emissions were richer in reduced gases (H₂, CO, CH₄); **methane would have been the dominant greenhouse gas**, with concentrations **2–3 orders of magnitude above today's 1.7 ppmv**. Free O₂ from photolysis of CO₂ and H₂O was consumed by reduced gases and minerals. NH₃ and other nitrogen-rich compounds gave **N₂, which, being unreactive, accumulated**.
3. **Oceans and weathering:** the Earth cooled, water vapour condensed, CO₂ dissolved in the oceans; falling volcanic activity and **weathering** lowered atmospheric CO₂ over time, **locking it in sedimentary rocks**.
4. **Life:** by 3.8 Ga conditions were stable enough for microbes; photosynthetic **cyanobacteria** in the ocean produced O₂; once the crust was oxidised the oxygen **accumulated in the atmosphere**; sunlight made **ozone**, which allowed colonisation of the land and complex life.

> [!connection] Where the rest of this is in the vault
> The faint young Sun and the thermostat ([[Faint Young Sun Paradox]], [[CL04 Feedback and Multiple Steady States]]); the rise of oxygen and the geological record in [[Evolution of Earth and Life - Course Map]]; ozone and the stratosphere in [[CL06 Hydrostatic Balance and Vertical Structure]] and [[CL07 Optical Properties of the Atmosphere]].

**Venus, Earth, Mars (L4 p. 15):** distance $1.52,\ 1.00,\ 0.72$ AU; solar flux $590,\ 1368,\ 2600$ W m⁻²; albedo $25\,\%$, $30\,\%$, $75\,\%$ (the slide's table is partly scrambled in the text layer: albedos are assigned in the order Mars, Earth, Venus as the standard values, `[!verify]`); Venus: 96 % CO₂, 3.5 % N₂, an atmosphere **90 times as thick** as Earth's; Earth: 78 % N₂, 21 % O₂, 0.04 % CO₂.

> [!example] The one-layer model across three planets 🔵
> With $T_e=[S(1-\alpha)/4\sigma]^{1/4}$ and the one-layer result $T_s=2^{1/4}T_e$ ([[CL08 Greenhouse Models]], Tutorial 2): **Mars** $T_e=210.2$ K ($T_s=250$ K); **Earth** $255.0$ K ($303$ K, observed $288$ K); **Venus** ($S=2642.3$ W m⁻², $\alpha=0.75$) $T_e=232.3$ K, one-layer $276$ K, **observed 735 K**, a greenhouse effect of $503$ K that one opaque layer (adding only $44$ K) cannot explain: it needs **very many optical depths** ($96\,\%$ CO₂, $90$ bar) and the water-vapour runaway of §7 ([[CL08 Greenhouse Models]]). Note: the slide's $\sim$$1368$ W m⁻² and Tutorial 2's $1369.77$ W m⁻² differ from the $1361$ W m⁻² used elsewhere in the vault by $<1\,\%$.

## 4. Why some molecules are greenhouse gases
<span class="scope-taught">taught</span> *Neena L6 p. 2: [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=2|p. 2]]*

Molecular absorption in the infrared and beyond can happen only if the molecular motion generates an **oscillating electric field** that matches the radiation: the molecule must act as an **oscillating dipole**, with a charge separation (a dipole moment) that **changes in time**. So: **vibrations of polar molecules** are IR active if the vibration changes the dipole; the **asymmetric stretch and the bend of non-polar molecules** such as CO₂ are IR active because they create a dipole; **rotations of polar molecules** are IR active if the dipole direction changes. The symmetric stretch of CO₂ and the vibration of N₂ and O₂ (no dipole at all) are not: that is why 99 % of the atmosphere is transparent to infrared. *Consequences on the slide:* the atmosphere is mostly transparent to sunlight and mostly **opaque to terrestrial radiation**; it is **H₂O, not CO₂**, that absorbs strongly over a wide range of IR wavelengths; short solar wavelengths are removed by photodissociation and scattering. Details of band structure and the window: [[CL07 Optical Properties of the Atmosphere]]; zettel [[greenhouse-gas-absorption-mechanisms]]; the symmetry argument is the one of [[Inorganic Chemistry - Course Map]] (IR-active modes by symmetry).

## 5. The greenhouse gases one by one
<span class="scope-taught">taught</span> *Neena L6 pp. 6–7, 15: [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=6|p. 6]], [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=7|p. 7]], [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=15|p. 15]]* · <span class="scope-extra-beyond">extra · beyond</span> *decay and Clausius–Clapeyron numbers*

| gas | share (slide) | by volume | lifetime (slide) | potency | main sources |
|---|---|---|---|---|---|
| **water vapour** | ~60–70 % of the **natural** greenhouse effect | 1–2 % ($\sim10^4$ ppm) | ~10 days | (feedback) | evaporation; phase changes at $273.16$ K, $6.11$ hPa |
| **CO₂** | ~20 % of the natural effect; ~**75 %** of the warming caused by human activity | 0.04 % (400 ppm) | "at least a decade" ($\sim$10–100 yr) before uptake by photosynthesis; depends on which "sphere" the carbon enters | 1 (reference) | volcanoes, respiration, ocean release, fossil fuels, land use |
| **CH₄** | ~17 % of the anthropogenic effect | ~1.9 ppm | ~12 yr | 25–30× CO₂ (per molecule) | wetlands, landfills, livestock, coal mining, biomass burning |
| **N₂O** | ~6 % of the anthropogenic effect | ~335 ppb | ~114 yr | ~273× CO₂ | fertilisers, burning of coal and wood, industry |

> [!verify] Two numbers to check
> L4 gives CH₄ as **1.7 ppmv** (today, p. 13) and L6 as **~1.9 ppm** (p. 15): both are the same quantity at different dates or roundings. The CO₂ "lifetime" of the slide is a *residence time before a molecule is taken up*; the **perturbation lifetime** of a pulse of CO₂ is not one exponential (the vault does not treat it; recalled, not read).

**Water vapour** is a *feedback*, not a forcing: its amount is not set by human emissions but by temperature ("warmer air holds more water vapour"): higher surface temperature → more evaporation → more vapour → more greenhouse warming (L6 p. 6; [[Water-Vapour Feedback]], [[CL08 Greenhouse Models]]). Only a thousandth of a percent of Earth's water is vapour; its short life (~10 days) means it is constantly recycled. *Rate* 🔵: Clausius–Clapeyron with $L=2.5\times10^6$ J kg⁻¹: $e_s(288\ \text{K})=16.98$ hPa, $e_s(298\ \text{K})=31.91$ hPa, a factor $1.88$ per $10$ K, i.e. $d\ln e_s/dT=L/R_vT^2=6.3\,\%$ per K at $293$ K (a $1$ K step gives $6.5\,\%$; [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]] for the derivation).

**Lifetimes as decay** 🔵 (figure B): after $t=\tau$ a fraction $e^{-1}=0.368$ of a pulse remains, after $3\tau$ $0.050$, after $5\tau$ $0.0067$. For CH₄ ($\tau=12$ yr): $0.368$ after 12 yr, $0.050$ after 36 yr; for N₂O ($114$ yr): $0.368$ after $114$ yr; for water vapour ($10$ d) $0.050$ after $30$ days. This is why **cutting methane acts within decades**, cutting N₂O or CO₂ takes much longer, and why potency per molecule and lifetime must both enter a comparison (the lecture's "25–30×" and "273×" are *potencies*, global warming potentials, over a fixed horizon not given on the slides).

## 6. The carbon cycle
<span class="scope-taught">taught</span> *Neena L6 pp. 8–14: [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=8|p. 8]], [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=10|p. 10]], [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=13|p. 13]]*

> [!key] Biogeochemical cycles (L6 p. 8)
> The Earth has natural recycling systems for the elements of life (C, H, O, N, P, S). A **biogeochemical cycle** is the complete pathway an element follows through the Earth system, from geosphere to biosphere, atmosphere and hydrosphere and back: **bio** (life and biological reservoirs), **geo** (rocks and soils), **chemical** (transformations on the way). Atmospheric and ocean circulation **and plate tectonics** together form the planet's "circulatory system".

The **carbon cycle** recycles carbon between the Earth's interior, surface, ocean and atmosphere, is strongly coupled to the **water cycle**, and regulates atmospheric CO₂ **on two time scales**: *short term* (tens to hundreds of years) and *long term* (millions of years).

- **Inorganic carbon cycle** (CO₂, carbonates; L6 p. 10): **atmosphere–ocean exchange** of CO₂; **carbonate and silicate weathering** on land → erosion → **carbonate ions in the ocean**; **carbonate precipitation** by shell-forming organisms → sedimentation → carbonates in the sedimentary-rock reservoir → **subduction → metamorphism and volcanism → CO₂ returned to the atmosphere**.
- **Organic carbon cycle** (L6 pp. 10–12): **photosynthesis**, **respiration**, storage in trees and in soil organic matter, decay; sometimes before decay the soil **erodes**, is carried to the sea, buried and **lithified**; marine sediments rich in organic matter can become **petroleum**.
- **Short-term cycling:** atmosphere ⇄ biosphere (land and sea) by photosynthesis and respiration, storage in trees, burial in soil, decomposition. It repeats **several times before a "leak"** feeds the long-term cycle.
- **Long-term cycling** (L6 p. 13): dominated by **geological processes**; organic carbon spends about **200 million years** in the sedimentary-rock reservoir before **weathering** returns it to the atmosphere; weathering of organic carbon is an **oxidation that needs O₂**, directly from the air or from oxygenated groundwater.
- **Natural sources:** volcanoes, weathering of organic carbon, respiration, release from the oceans, microbial decomposition, wildfires. **Natural sinks:** carbonate weathering, photosynthesis, dissolution in the ocean. **Human sources:** fossil fuels, deforestation, burning, land clearing for agriculture, manufacturing. **Human sinks: "?"** (the slide leaves it as a question). Mining, pumping and burning fossil fuels **interferes with the long-term cycle**, accelerating release from the sedimentary reservoir.

> [!example] What a 200-Myr residence time means 🔵
> A reservoir that holds its carbon for $\tau_\text{res}=2\times10^8$ yr loses a fraction $1/\tau_\text{res}=5\times10^{-9}$ per year; the oil, gas and coal burnt in roughly two centuries are the product of several hundred million years of burial. The fast cycle (photosynthesis and respiration) turns the atmosphere's carbon over in a few years to a decade; the slow cycle sets where the *average* sits over $10^5$–$10^8$ yr. That separation of time scales is why the human perturbation (fast) outruns the natural thermostat (slow).

> [!key] The thermostat (L6 p. 16)
> "Over the history of the planet, **CO₂ release by volcanism has been balanced by the consumption of CO₂ by silicate and carbonate weathering**; the water and carbon cycles are critical for maintaining the CO₂ concentration." Weathering needs liquid water and speeds up when it is warm and wet, so a warmer climate removes CO₂ faster and cools: a **negative feedback** on time scales of $10^5$–$10^6$ yr (the same feedback as in the snowball Earth recovery, [[CL04 Feedback and Multiple Steady States]], [[silicate-weathering-feedback]]).

## 7. The Venus counter-example
<span class="scope-taught">taught</span> *Neena L6 p. 17: [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf#page=17|p. 17]]*

"On Venus the carbon is in the **atmosphere**; on Earth it is in **sedimentary rocks**." Early Venus (first $\sim$2 Gyr) likely had water like Earth. As the solar luminosity increased the temperature rose; **water-vapour feedback** boiled the oceans; with **no liquid water and no rain there is no CO₂ regulation by chemical weathering**; the hot vapour escaped to space (§2: H₂O is lost when it is hot and high). Result: a thick **96 % CO₂** atmosphere and a surface at **~462 °C** ($735$ K, the Tutorial 2 value). Compare [[CL08 Greenhouse Models]] (the runaway greenhouse) and §3: the comparison with Earth is **not about which gas** but about **whether the thermostat can work**.

## Map of this chapter
> [!connection] How CL16 connects
> **Builds on:** [[CL08 Greenhouse Models]] (layer models, runaway greenhouse), [[CL07 Optical Properties of the Atmosphere]] (absorption bands, windows), [[CL05 Thermodynamic State of the Atmosphere]] / [[CL06 Hydrostatic Balance and Vertical Structure]] (composition, scale height), [[CL04 Feedback and Multiple Steady States]] (weathering thermostat, snowball).
> **Leads to:** [[CL17 Orbital Forcing and Glacial Cycles]] (glacial CO₂ is part of the long-term cycle), [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] (the ocean stores CO₂ and heat for centuries).
> **Concepts:** [[Atmospheric Escape]] · [[Atmospheric Evolution]] · [[Infrared-Active Molecule]] · [[Greenhouse Gas Lifetime and Potency]] · [[Biogeochemical Cycle]] · [[Carbon Cycle]]
> **Other subjects:** [[Thermodynamics and Statistical Mechanics - Course Map]] ([[SM04 Kinetic Theory and the Boltzmann Equation]]: the Maxwell tail behind escape; [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]]: Clausius–Clapeyron), [[Evolution of Earth and Life - Course Map]] (early atmosphere, oxygen), [[Inorganic Chemistry - Course Map]] (IR-active vibrations by symmetry), [[Landscapes and Geomorphology - Course Map]] (weathering and erosion, [[LS11 Weathering and Regolith]]), [[Eco-Evo - Course Map]] (photosynthesis and respiration as the fast carbon cycle).

## Summary
> [!summary] Cheat-sheet
> - Atmospheric mass: 99 % below 32 km, 99.999 % below 80 km ($H\approx7$ km). Permanent vs variable gases; aerosols $10^{-9}$–$10^{-4}$ m; homosphere to ~80–100 km, heterosphere above.
> - **Escape:** lost if $\bar v=\sqrt{8kT/\pi m}\gtrsim\frac16v_\text{esc}$: Earth loses H₂, He, holds H₂O; Mars loses H₂O, holds CO₂ (at ~1000 K); $v_\text{esc}^2\propto M/R$.
> - **Evolution:** primary H/He (lost) → secondary by outgassing (80–90 % H₂O, 6–12 % CO₂, 1–2 % SO₂; reduced early gases, CH₄ the main GHG) → oceans, weathering (CO₂ into rocks) → cyanobacteria, O₂, ozone. Venus 96 % CO₂, 90× thicker; one layer gives $276$ K vs $735$ K.
> - **Infrared activity** needs a changing dipole (asymmetric stretch/bend of CO₂, polar vibrations/rotations).
> - **GHGs:** H₂O 60–70 % of the natural effect, ~10 d, feedback ($\approx6.3$ % per K); CO₂ 20 % (75 % of anthropogenic warming), 0.04 %; CH₄ 17 %, 12 yr, 25–30×; N₂O 6 %, 114 yr, 273×. Decay $e^{-t/\tau}$. Vapour pressure rises $\approx6.3\,\%$ per K.
> - **Carbon cycle:** inorganic (weathering, carbonate precipitation, subduction, volcanism) and organic (photosynthesis, respiration, burial); short-term (decades) vs long-term ($10^8$ yr); **volcanism ⇄ weathering** = thermostat; fossil fuels short-circuit the slow cycle. **Venus: no liquid water, no thermostat.**

## Practice
1. **Escape.** Compute the mean thermal speed $\sqrt{8kT/\pi m}$ of H₂, H₂O, N₂ and CO₂ at 1000 K and compare with $v_\text{esc}/6$ for Earth ($11.19$ km/s) and Mars ($5.03$ km/s). Which are retained? How does the answer for CO₂ on Mars change at 1500 K?
2. **Mass fraction.** What fraction of the atmosphere's mass lies below 32 km and below 80 km for $H=7$ km? Compare with the slide.
3. **Lifetimes.** After how long has a methane pulse ($\tau=12$ yr) decayed to $5\,\%$? To $1\,\%$? What fraction of an N₂O pulse remains after $100$ yr?
4. **Water vapour.** Using $L=2.5\times10^6$ J kg⁻¹, compute the percentage increase of saturation vapour pressure per kelvin at 293 K and the factor between 288 K and 298 K.
5. **Venus.** With $S=2642.3$ W m⁻², $\alpha=0.75$ find $T_e$, the one-layer $T_s$ and the greenhouse effect; why does the one-layer model fail?
6. **Mars.** With $S=590$ W m⁻², $\alpha=0.25$ find $T_e$. (The slide gives no observed value.)
7. **Cycle.** A reservoir holds its carbon 200 Myr. What fraction leaves per year? How many e-foldings is the history of oil formation compared with the human fossil-fuel era ($\sim200$ yr)?
8. **Concept.** Why does water vapour amplify but not *start* warming, and why is the lecture's "human sinks: ?" an honest question?

> [!example]- Solutions
> 1. $\bar v=3241,\ 1084,\ 869,\ 694$ m/s for H₂, H₂O, N₂, CO₂ at 1000 K; Earth threshold $1864$: loses H₂ only (He $2300$ too); Mars threshold $838$: loses H₂, He, H₂O, and marginally N₂; holds CO₂ ($694$). At $1500$ K CO₂ has $694\sqrt{1.5}=850$ m/s $>838$: marginally lost.
> 2. $1-e^{-32/7}=0.9897$, $1-e^{-80/7}=0.999989$ (slide: 99 %, 99.999 %).
> 3. $5\,\%$: $t=\tau\ln20=36.0$ yr; $1\,\%$: $\tau\ln100=55.3$ yr. N₂O after $100$ yr: $e^{-100/114}=0.416$.
> 4. $\frac{L}{R_vT^2}=\frac{2.5\times10^6}{461.5\times293^2}=0.0631$: $6.3\,\%$ per K as a derivative ($6.5\,\%$ for a $1$ K step); factor $e_s(298)/e_s(288)=31.91/16.98=1.88$.
> 5. $T_e=232.3$ K, $T_s=2^{1/4}T_e=276.3$ K (one-layer greenhouse effect $44$ K); observed $735$ K means $503$ K: one thin opaque layer cannot supply it; Venus has $\sim90$ bar of CO₂ (many optical depths) and no liquid water to remove it.
> 6. $T_e=210.2$ K.
> 7. $1/(2\times10^8)=5\times10^{-9}$ yr⁻¹; $200$ yr is $10^{-6}$ of a residence time, so burning returns in $\sim200$ yr what was removed over $\sim10^8$ yr: a rate $\sim10^6$ times the natural weathering return.
> 8. Vapour is controlled by temperature (it condenses), so it responds to warming caused by CO₂ and amplifies it; "human sinks" are limited (growth of biomass and ocean uptake are real but reversible), whereas the geological sink (weathering) is far slower than emissions.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | mass distribution, constituents, aerosols, homosphere/heterosphere, the escape criterion, atmospheric evolution (Hadean, volcanic gases, reduced gases, N₂, oceans, life, ozone), Venus–Earth–Mars | [[Lecture4_Atmospheric_composition_evolution_250828_142428 (1).pdf]], pp. 6–15 (text layer read this session) | taught (2025) |
> | oscillating-dipole absorption, water vapour, CO₂, carbon cycle (inorganic, organic, short/long-term), 200 Myr, sources and sinks, CH₄, N₂O, Venus | [[Lecture6_Greenhouse gas regulation in the atmosphe_250828_152840 (1).pdf]], pp. 2–17 (text layer read this session) | taught (2025) |
> | Tutorial 2 (one-layer Venus/Earth) | [[Tutorial_2_CR_One and Two Layer models_250828_142702 (1).pdf]] | practice (see CL08) |
> | escape speeds with numbers, decay curves, Clausius–Clapeyron rate, planet comparison | `scripts/cl_neena_numbers.py` (cl16), `scripts/fig_cl16_21.py` | extra/beyond |
>
> **Notes.** [!verify] The figures on the slides (carbon-cycle diagrams, planet comparison) are images not seen here; the Venus/Earth/Mars albedo assignment follows the standard values, the slide's own table order is garbled in the text layer. The escape numbers use an **assumed 1000 K**; the slides give none. The perturbation lifetime of CO₂ and the Jeans escape integral are recalled, not read. Venus's "462 °C" is the lecture's value; Tutorial 2 quotes $735$ K.
