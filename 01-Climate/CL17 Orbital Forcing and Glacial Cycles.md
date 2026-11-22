---
title: CL17 Orbital Forcing and Glacial Cycles
aliases: [CL17, Milankovitch cycles, orbital forcing, eccentricity, obliquity, precession, glacial cycles, ice ages, glacier mass balance, last glacial maximum, ice cores, Neena Lecture 9, Neena Lecture 10]
subject: climate
type: chapter
chapter: 17
part: V
scope: [taught, extra-beyond]
by: [neena]
status: draft
prereq: ["[[CL10 Global Energy Balance and Meridional Structure]]", "[[CL04 Feedback and Multiple Steady States]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/neena, status/draft]
---
# CL17 · Orbital Forcing and Glacial Cycles

◀ [[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]] · [[Climate - Course Map|Course Map]] · ▶ [[CL18 The Ocean as the Climate System's Heat Reservoir]]

<span class="scope-taught">taught · in syllabus (2025 lectures, Neena)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-07)
> **Neena Lectures 9 (orbital cycles) and 10 (glaciations)** of the 2025 course (`ec2113_neena/`; see the warning box of [[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]] for why 2025 material is added). [[CL10 Global Energy Balance and Meridional Structure]] §2 already derives the **exact daily-mean insolation** and *names* the Milankovitch cycles with a short extra box (Suhas, 7 Oct p. 6; the numbers there came from Hays, Imbrie and Shackleton 1976, **not read**); this chapter is the full treatment of what Lectures 9–10 say, reusing the exact formula of CL10 (`scripts/cl10lib.py`) to **check the lecture's numbers**. Two numbers in the slides are inconsistent with each other (`[!verify]` in §2). The slides are text-layer PDFs; their pictures (orbit diagrams, ice-core plots, glacial landforms) were not seen. The seasonal-cycle part of Lecture 8 and **Tutorial 5** (longitude, local time, solar altitude) are in [[CL10 Global Energy Balance and Meridional Structure]] (Practice 9–12, added 2026-11-07).

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught (2025: Lectures 9 and 10)**
> - §1 Sun–Earth geometry today (perihelion 3 Jan, aphelion 4 July; $\sim$3 % in distance, $\sim$6.8 % in flux); §2 the **three Milankovitch cycles** (eccentricity $\sim$100 kyr, obliquity 41 kyr, precession $\sim$26 kyr and the 112 kyr apsidal precession); §3 the **evidence** of past climates (ice cores, sediment cores, glacial landforms, the Last Glacial Maximum, the Pleistocene); §4 **orbit → glaciation**: seasonality and continentality, snowfall and melt, **glacier mass balance**, why **high-latitude northern summer** insolation matters, the **lag** of ice volume, the next glaciation
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 the lecture numbers checked by the exact insolation formula (eccentricity 23 % vs 27.5 %; obliquity alone 8 %, precession alone 7 % at today's eccentricity, 20 % at $e=0.05$; the latitude dependence of the obliquity effect); §4 the remark on the 100 kyr problem

> [!key] After this chapter you can
> - say what the three **orbital parameters** are, their ranges and periods, and what each does to insolation (and what it does *not* do: obliquity does not change the annual mean at the equator; eccentricity barely changes the annual global mean),
> - compute the perihelion/aphelion flux ratio $((1+e)/(1-e))^2$ and the **annual-mean** change $(1-e^2)^{-1/2}$,
> - explain why the **precession signal is multiplied by the eccentricity**,
> - state the **Milankovitch criterion** (high-latitude northern *summer* insolation) and argue it from the **mass balance** of an ice sheet,
> - list the **evidence** for glacial cycles and say how an ice-core temperature proxy works,
> - say what the lecture says about the **next glaciation**.

> [!intuition] The one-sentence story
> The orbit changes slowly in shape, tilt and orientation; none of it changes the energy the Earth gets in a year by more than a fraction of a percent, but it **moves energy between seasons and latitudes** by tens of W m⁻². An ice sheet is a **ratchet**: it grows if the summer sun fails to melt the winter's snow, so a cool summer at 65°N is enough, repeated for thousands of years, to start a glaciation.

![[fig_cl17_orbit.png]]
*A: perihelion flux above aphelion flux against eccentricity; the lecture's two numbers are marked (§2). B: daily insolation at 65°N on 21 June against the longitude of perihelion for three eccentricities (exact formula, obliquity 23.44°): precession matters only when $e$ is large. C: effect of tilting from 22.1° to 24.5°: a change at high latitudes, almost none (even a small fall) in the tropics. Numbers: `scripts/cl_neena_numbers.py` (cl17), `scripts/cl10lib.py`.*

> [!tip] 🔬 Interactive: orbital forcing
> Open [▶ cl_milankovitch.html](../Assets/interactive/cl_milankovitch.html) (self-contained, works offline). Choose a latitude, the obliquity (22.1°–24.5°), the eccentricity (0–0.0607) and the longitude of perihelion; the left panel shows the daily insolation through the year against today's, the right panel the June-solstice insolation against precession. Reproduce: 65°N, today: **477.9 W m⁻²**; $e=0.05$, $\varpi=90^\circ$: **547.0**; $\varpi=270^\circ$: **447.7**.

## 1. The seasons and today's orbit
<span class="scope-taught">taught</span> *Neena L9 pp. 2–5: [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=3|p. 3]]*

The southern hemisphere receives **relatively more insolation in its summer** than the north does in its own. The Earth is nearest the Sun (**perihelion**) on about **3 January**, thirteen days after the northern winter solstice, and farthest (**aphelion**) on about **4 July**; the distance differs by about **3 %**, so the flux in January is about **6.8 %** higher than in July (L9 p. 3). *Check* 🔵: $\big(\tfrac{1.0167}{0.9833}\big)^2-1=6.9\,\%$ ($e=0.0167$). By Kepler's second law the planet moves **faster at perihelion**: northern winters are **somewhat milder and shorter**, northern summers (near aphelion) **somewhat milder and longer** than the southern ones. The seasons themselves are caused by **tilt, not distance** ([[CL10 Global Energy Balance and Meridional Structure]] §2: January is *summer* in the south although the Earth is closest to the Sun). The detail of daily and seasonal insolation (declination, solar altitude, daylength, the polar maximum) is in CL10 and its Practice problems from Tutorial 5.

## 2. The three cycles
<span class="scope-taught">taught</span> *Neena L9 pp. 6–18: [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=6|p. 6]], [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=9|p. 9]], [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=10|p. 10]], [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=11|p. 11]], [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=13|p. 13]]* · <span class="scope-extra-beyond">extra · beyond</span> *checks*

> [!key] Milankovitch theory (L9 p. 6)
> Cyclic variations in three elements of the Earth–Sun geometry combine to change the amount of solar energy that reaches the Earth: **(1)** the **eccentricity** of the orbit, **(2)** the **obliquity** (tilt of the axis to the orbital plane), **(3)** the **precession** (the direction of the axis traces a circle, like a spinning top winding down). Periods: $\sim100{,}000$, $\sim41{,}000$ and $\sim26{,}000$ yr.

| cycle | what changes | range and period (slides) | effect |
|---|---|---|---|
| **eccentricity** | shape of the orbit; Jupiter and Saturn pull on it | $0.005$–$0.0607$, ~100 kyr; today $0.0167$, decreasing | annual-mean insolation barely changes; seasons' distance contrast changes |
| **obliquity** | tilt of the axis | $22.1^\circ$–$24.5^\circ$, 41 kyr; today $23.5^\circ$, decreasing | more tilt = warmer summers and colder winters in **both** hemispheres, strongest at high latitudes |
| **axial precession** | the axis wobbles: the equatorial bulge ($21$ km, equatorial minus polar radius) feels the torque of the Sun and Moon | 25,700 yr; Polaris today, **Vega 13,000 yr ago** | moves the solstices and equinoxes around the orbit |
| **apsidal precession** | the orbit itself rotates (pull of the planets) | 112,000 yr | moves perihelion in space |

**Precession of the equinoxes.** The two precessions combine: the solstices and equinoxes move along the orbit (one full turn in $\sim$26 kyr in the lecture's phrase); **today** northern winter is near perihelion and northern summer near aphelion; **13,000 yr ago** (half a cycle) the reverse. **Every half-cycle the hemisphere with the larger seasonal contrast switches** (L9 p. 17). *Check* 🔵: $360^\circ/25{,}700\ \text{yr}=0.0140^\circ/\text{yr}$; half a cycle $=12{,}850$ yr; the combined *climatic* precession period is $1/(1/25{,}700+1/112{,}000)=20{,}900$ yr (the "$\sim$19–23 kyr" often quoted; **not on the slides**).

> [!verify] Two numbers in the slides do not agree
> * L9 p. 3 says the January flux is **6.8 %** above July; L10 p. 23 says "in the current near-circular orbit only a **6 %** difference between perihelion and aphelion". The exact ratio is $6.9\,\%$ ($e=0.0167$). Both are roundings.
> * L9 p. 9: "when the orbit is at its **highest eccentricity**, **about 23 %** more radiation reaches the Earth at perihelion than at aphelion"; the same slide gives the maximum $e=0.0607$, for which $((1+e)/(1-e))^2-1=\mathbf{27.5\,\%}$. A ratio of $1.23$ corresponds to $e=0.052$. (Numbers: `cl_neena_numbers.py`.)

**What the cycles do to energy** 🔵 (exact formula of CL10; $S=1361$ W m⁻²; Kepler-weighted annual means):
- **Annual mean** scales as $(1-e^2)^{-1/2}$: from $e=0.005$ to $0.0607$ it changes by **$0.18\,\%$**, matching L10 p. 20 ("the total change in global annual insolation due to the eccentricity cycle is only about 0.2 %"). Eccentricity acts on the **seasons**, through precession.
- **Obliquity**, tilting from $22.1^\circ$ to $24.5^\circ$: the annual mean at the **pole** rises from $163.0$ to $179.7$ W m⁻² ($+16.7$), at $65^\circ$N from $209.9$ to $217.0$ ($+7.1$), at the **equator** it *falls* from $417.5$ to $414.0$ ($-3.5$): a **redistribution** towards the poles (figure C). The 21 June daily insolation at 65°N changes by **$39$ W m⁻² ($8.2\,\%$)**: $456.6$ ($22.1^\circ$), $477.9$ ($23.44^\circ$), $495.8$ ($24.5^\circ$).
- **Precession** at today's $e=0.0167$ (obliquity $23.44^\circ$): $510.5$ W m⁻² with perihelion at the June solstice vs $477.5$ at the December solstice: **$33$ W m⁻² ($6.9\,\%$)**. At $e=0.05$ the swing is $447.7$–$547.0$ W m⁻² (**$20\,\%$**); at $e=0$ there is **no** precession signal ($493.6$ W m⁻² for every $\varpi$). *The precession effect is multiplied by the eccentricity* (figure B): "eccentricity modulates the amplitude of the seasonal insolation changes associated with the precession cycle" (L10 p. 23).
- **Extremes combined** (65°N, 21 June): cool summer ($22.1^\circ$, $e=0.05$, aphelion at the solstice) $427.7$; present $477.9$; warm summer ($24.5^\circ$, $e=0.05$, perihelion at the solstice) $567.4$ W m⁻², a range of $140$ W m⁻² ($29\,\%$ of today's value). The lecture's "obliquity and precession can bring about a **10–12 %** change in seasonal insolation" (L10 p. 21) is of the right order for each alone.

## 3. Evidence of past climates
<span class="scope-taught">taught</span> *Neena L9 pp. 19–26: [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=20|p. 20]], [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=24|p. 24]], [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf#page=26|p. 26]]*

- **Temperature reconstructions from Greenland and Antarctic ice cores** show the global mean fluctuating by about **4–5 K** (up to $\sim$10 K over Antarctica and Greenland) as the planet cycled in and out of **glacial periods of roughly 100,000 years** (L9 p. 19). The ratios of the stable isotopes of oxygen and hydrogen (**δ¹⁸O, δD**) in ice indicate the **temperature when the snow fell**; **trapped air bubbles** record the past atmospheric composition ([[CL02 Observing Global Temperature]], [[Isotopic Thermometers]]).
- **Marine sediment cores:** layers laid down with the oldest at the bottom, in places up to **140 million years old**; **geochemistry of marine microfossils** gives age, origin and past temperature; **ice-rafted debris** in ocean cores is evidence of past glaciations.
- **Glacial landforms:** glacial striations (Mount Rainier), a huge **glacial erratic** left in place (Central Park, New York), glacial grooves (Ohio), glacial valleys (Leh Valley, Ladakh): [[LS19 Glacial and Aeolian Landforms]], [[LS14 Glaciers Mass Balance and Ice Flow]], [[LS15 Glacial Deposits Rebound and Sea Level]].
- **The Last Glacial Maximum**, 18,000 yr ago: glaciers covered about **32 %** of the land area ($\approx4.8\times10^7$ km² of $1.49\times10^8$ km², 🔵), ice sheets thousands of metres thick, most of Europe and North America under ice. The **Pleistocene** (2.6 Myr to 11,700 yr ago) is the epoch of repeated glaciation; it ended with the extinction of megafauna, "linked both to rapid climate change and the spread of modern humans" (L9 p. 26).

## 4. From orbits to ice sheets
<span class="scope-taught">taught</span> *Neena L10 pp. 2–26: [[Lecture10_Glaciations_250918_132625 (1).pdf#page=7|continentality, p. 7]], [[Lecture10_Glaciations_250918_132625 (1).pdf#page=15|mass balance, p. 15]], [[Lecture10_Glaciations_250918_132625 (1).pdf#page=16|p. 16]], [[Lecture10_Glaciations_250918_132625 (1).pdf#page=23|p. 23]], [[Lecture10_Glaciations_250918_132625 (1).pdf#page=26|p. 26]]*

**Seasonal insolation drives the seasonal geography of temperature and circulation** (L10 p. 2); the annual range of insolation is larger at high latitudes. **Continentality** (L10 pp. 7–9): coasts have a *maritime* climate (small annual range), the interiors a *continental* one (large extremes), because **oceans have lower albedo**, the **heat capacity of water is 3–4 times that of dry soil**, ocean heat is carried down by **turbulent mixing** while **land conducts poorly**; so oceans absorb more of the available solar energy, **land is warmer than ocean in summer and colder in winter**, and seasonal temperature variability is **much larger over continents** ([[CL18 The Ocean as the Climate System's Heat Reservoir]] §5 quantifies the heat capacity; [[CL15 Monsoons]] uses the land–sea contrast).

**Snow and ice.** Snowfall needs winter temperature below freezing; at high latitudes and altitudes precipitation is snow, at low latitudes rain. Snow that falls in winter **melts in summer** if the summer temperature exceeds $0\,^\circ$C. Glaciers are compressed snow that moves slowly like a river; an **ice sheet** exceeds **50,000 km²**.

> [!key] Glacier mass balance (L10 p. 15)
> **Accumulation in winter, ablation in summer.** If winter accumulation is balanced by summer ablation, the annual mass change is zero and the glacier does not grow. If the summer is **mild** (low summer insolation), the snowpack does **not melt completely** and next winter's snow piles on top: the glacier grows. In the other case, warm summers turn precipitation into rain and **accelerate ablation**.

> [!key] The Milankovitch criterion (L10 pp. 16–22)
> The critical factor for **northern continental glaciation** is **not the total insolation** but the **summer insolation at high northern latitudes**: low summer insolation → cool summers → snow survives and accumulates → glaciation; high summer insolation → rain and ablation → ice shrinks. The cycles combine as follows:
> * **Eccentricity** alone: the total annual change is $\sim0.2\,\%$, too small; but it modulates the seasonal contrast.
> * **Obliquity:** the greater the tilt the more extreme the seasons, mostly at **high latitudes**; low tilt = cool summers.
> * **Precession:** summers at **aphelion** are cooler; the effect is effective **only when the eccentricity is large**.
> * **Glaciation of the north is favoured when the eccentricity is large, northern summer falls at aphelion and the tilt is small.**

> [!example] Why the north? 🔵 (the slide poses the question; this answer is mine)
> The northern hemisphere has **land** at 60–70°N where snow can lie all year and ice sheets can sit; the southern hemisphere at the same latitudes is ocean (whose heat capacity keeps summers cool and melts snow from below), and Antarctica is already glaciated. The lecture also asks: "If the northern and southern hemispheres can alternately have summers at aphelion, why have the glaciations been **globally synchronous**?" Its slide on *glacial–climate feedbacks* names no answer in the text layer; the usual candidates (ice-albedo, CO₂ in the ocean and atmosphere, deep-ocean circulation) are the feedbacks of [[CL04 Feedback and Multiple Steady States]], [[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]] and [[CL21 Thermohaline Circulation Water Masses and Sea Ice]], **recalled and not read**.

> [!intuition] Why *summer* insolation at 65°N is the key number (the Milankovitch argument)
> An ice sheet grows if some of each winter's snow **survives the summer**. Winter is cold enough for snow almost everywhere at high latitude, so winters are not the bottleneck: the **summer** decides whether the snow melts. Most of the land where an ice sheet could start (Canada, Scandinavia, Siberia) lies near 60–70°N, while the Southern Hemisphere at that latitude is mostly ocean or already-glaciated Antarctica. So the climatically sensitive number is the **summer insolation at about 65°N**.
> - Low obliquity and aphelion in the northern summer → cool summers → snow survives → ice sheets grow.
> - High obliquity and perihelion in the northern summer → warm summers → the ice melts back.
>
> This is why §2 tracks 21 June at 65°N rather than the annual mean, which barely changes (0.18 %).

> [!pitfall] The 100-kyr puzzle
> The glacial cycles of the last ~1 Myr have a dominant period of ~100 kyr (§3), the period of eccentricity. Yet eccentricity alone changes the *annual* insolation by only 0.2 %, and its main effect is to modulate the ~21 kyr precession signal (§2). So the orbit is the **pacemaker, not the engine**. The large response needs amplifying feedbacks:
> - ice-albedo ([[CL04 Feedback and Multiple Steady States]]);
> - CO₂, which falls by ~90 ppm in glacials ([[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]]);
> - the slow dynamics of big ice sheets, which grow slowly and collapse fast.
>
> Exactly why the 100 kyr rhythm wins is still debated; the lecture does not claim to settle it.

**The lag** (L10 p. 24). The **maximum of ice volume lags thousands of years behind the minimum of summer insolation**: the ice sheets took **tens of thousands of years** to reach their maximum extent. *Reading:* ice volume responds to the **accumulated** (time-integrated) mass imbalance rather than to the instantaneous insolation, like a slab of heat capacity forced by a seasonal heating (the slab ocean of [[CL18 The Ocean as the Climate System's Heat Reservoir]] §5 shows how a large reservoir delays and damps a forcing).

**The next glaciation** (L10 p. 26). Northern summer falls at aphelion once per precession cycle (favourable); the tilt is decreasing and will reach a minimum in about **9,800 yr**; the eccentricity will decrease to a minimum in about **30,000 yr**. The lecture's statement: climatologists predict the **present interglacial will be long-lived (at least 1.5–2.5 precession cycles)** because the conditions needed to initiate ice-sheet growth will not occur at low eccentricity (`[verify]` the slide's wording "unusually cold winters": by the argument of the box above, what is needed is unusually **cool summers**; at low eccentricity the precession swing is small, so northern summers never get cool enough); the **CO₂ warming** is expected to delay the next glaciation further.

> [!verify] The 100,000-year puzzle (not addressed on the slides) 🔵
> Eccentricity changes the annual insolation by only $\sim0.2\,\%$ and its direct forcing has no 41- or 26-kyr character, yet the ice-age period of the last $\sim$0.8 Myr is $\sim$100 kyr (L9 p. 19). The lecture ends with "Milankovitch theory links orbital cycles to long-term climate changes, **explaining the pacing** of Earth's ice ages" (L9 p. 26). That the *pacing*, not the full amplitude, follows from the orbit, and that the large response needs the feedbacks above, is the standard position (**recalled, not read**; Hartmann §12 and Marshall & Plumb are the natural books, not in this folder).

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Orbital forcing: how obliquity, eccentricity and precession change the insolation
> Exact daily-mean top-of-atmosphere insolation Q = S (a/r)² /π · [h₀ sin φ sin δ + cos φ cos δ sin h₀] as a function of the <b>solar longitude</b> λ (0° = March equinox, 90° = June solstice), for a chosen latitude and orbit.
>
> ![[cl_milankovitch.png|720]]
>
> **Try:** Latitude 65°, e = 0.0167, ε = 23.44°, ϖ = 283°: the June solstice (λ = 90°) value is 478 W m⁻². Raise ε to 24.5° (495.8) or move perihelion to the June solstice (ϖ = 90°: 510.5). With e = 0.05 and ϖ = 90° the June value is 547 W m⁻², with ϖ = 270° it is 447.7: precession matters only when the eccentricity is large (Lecture 10). At the equator the tilt barely changes the annual mean (it falls 3.5 W m⁻² from ε = 22.1° to 24.5°); at the pole it rises by 16.7.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_milankovitch.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_milankovitch.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL17 connects
> **Builds on:** [[CL10 Global Energy Balance and Meridional Structure]] (exact daily insolation, Kepler weighting, Milankovitch box), [[CL03 Radiation and Planetary Energy Balance]] (energy balance), [[CL04 Feedback and Multiple Steady States]] (ice-albedo feedback, snowball).
> **Leads to:** [[CL18 The Ocean as the Climate System's Heat Reservoir]] (heat capacity and lags), [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] (deep ocean and carbon in glacial cycles).
> **Concepts:** [[Milankovitch Cycles]] · [[Orbital Eccentricity]] · [[Obliquity]] · [[Precession of the Equinoxes]] · [[Glacier Mass Balance]] · [[Glacial-Interglacial Cycles]] · [[Last Glacial Maximum]] · [[Seasons and Earth's Orbit]] · [[Insolation]]
> **Other subjects:** [[Landscapes and Geomorphology - Course Map]] ([[LS14 Glaciers Mass Balance and Ice Flow]], [[LS15 Glacial Deposits Rebound and Sea Level]], [[LS19 Glacial and Aeolian Landforms]]: the same glaciers seen from the landform side), [[Classical Mechanics - Course Map]] (orbital precession, torque on the equatorial bulge: [[CM04 Central Forces and Effective One-Dimensional Motion]]; recalled), [[Evolution of Earth and Life - Course Map]] (Pleistocene megafauna), [[Probability - Course Map]] (spectral peaks and quasi-periodicity).

## Summary
> [!summary] Cheat-sheet
> - **Today:** perihelion ~3 Jan, aphelion ~4 Jul; $((1+e)/(1-e))^2-1=6.9\,\%$ ($e=0.0167$); Kepler II: northern winter shorter and milder.
> - **Eccentricity** 0.005–0.0607, ~100 kyr; annual mean $\propto(1-e^2)^{-1/2}$ ($0.18\,\%$); perihelion/aphelion flux up to $27.5\,\%$ ($e=0.0607$; the slide's 23 % is $e=0.052$).
> - **Obliquity** 22.1°–24.5°, 41 kyr: pole annual mean +16.7 W m⁻², equator −3.5; 65°N June +39 W m⁻² (8 %).
> - **Precession** 25.7 kyr (axis) and 112 kyr (apsides) → ~21 kyr climatic; swing $6.9\,\%$ at $e=0.0167$, $20\,\%$ at $e=0.05$, 0 at $e=0$.
> - **Evidence:** ice-core δ¹⁸O/δD and air bubbles, marine cores, ice-rafted debris, glacial landforms; LGM 18 kyr ago, 32 % of land under ice; 100-kyr cycles of 4–5 K (up to 10 K polar).
> - **Mechanism:** mass balance (winter accumulation vs summer ablation); **high-latitude northern summer insolation** decides; glaciation favoured by large $e$, aphelion summer, low tilt; ice volume **lags** by thousands of years; next glaciation delayed (low $e$, CO₂).

## Practice
1. **Eccentricity.** Compute $((1+e)/(1-e))^2-1$ for $e=0.005$, $0.0167$, $0.05$, $0.0607$. For which $e$ is it $23\,\%$? Comment on the two slides.
2. **Annual mean.** By what percentage does the annual-mean insolation change between $e=0.005$ and $e=0.0607$?
3. **Precession times.** The axis precesses once in 25,700 yr and the apsides once in 112,000 yr. Find the period of the combined cycle and how long ago perihelion was at the northern summer solstice (if it is at the northern winter one today, within a few days).
4. **65°N.** Using the interactive tool (or `cl10lib`) find the 21 June insolation at 65°N for (a) $e=0$, $\varepsilon=23.44^\circ$; (b) today; (c) $e=0.05$, perihelion at the December solstice; (d) $e=0.05$, perihelion at the June solstice. Rank the effects of obliquity and precession.
5. **Obliquity.** Explain with the geometry of the polar day why the annual mean at the **pole** rises with tilt while that at the **equator** falls.
6. **Mass balance.** An ice margin receives $0.8$ m of snow-water per winter and loses $0.2$ m per month of melt on the days when the mean temperature exceeds $0\,^\circ$C. How many warm months per year does it take to stop the glacier from growing? What does a warmer summer insolation do?
7. **LGM.** Estimate the ice-covered area at the LGM from "32 % of land" (use $1.49\times10^8$ km² for the land area).
8. **Concept.** Why does the lecture stress *summer* rather than *annual* insolation, and why is the effect strongest at high latitudes? Why does the ice volume lag the insolation?

> [!example]- Solutions
> 1. $2.0\,\%$ ($0.005$), $6.9\,\%$ ($0.0167$), $22.2\,\%$ ($0.05$), $27.5\,\%$ ($0.0607$); $23\,\%$ at $e=0.052$: the slide's maximum $0.0607$ and its "23 %" are inconsistent (the latter is for $e\approx0.05$).
> 2. $(1-e^2)^{-1/2}$: $1.001846$ vs $1.0000125$: $+0.18\,\%$.
> 3. $1/(1/25{,}700+1/112{,}000)=20{,}900$ yr; half a cycle $\approx10{,}450$ yr (perihelion in northern summer about $10$–$11$ kyr ago; that this coincides with the early-Holocene insolation maximum is recalled, not on the slides); the lecture's "13,000 yr ago" uses the 25,700-yr axis cycle alone.
> 4. (a) $493.6$; (b) $477.9$; (c) $447.7$ (at $e=0.05$, $\varepsilon=23.44^\circ$); (d) $547.0$. Obliquity alone: $456.6$–$495.8$ ($8.2\,\%$); precession alone at today's $e$: $477.5$–$510.5$ ($6.9\,\%$); at $e=0.05$: $20\,\%$.
> 5. At the pole the Sun is above the horizon only in summer, and the summer noon altitude is $\varepsilon$: a bigger $\varepsilon$ increases the summer daily mean more than winter darkness can decrease it; at the equator the annual mean has the factor $\cos\delta$, which falls slightly as $|\delta|\le\varepsilon$ grows.
> 6. Growth stops when melt $\ge0.8$ m: $0.8/0.2=4$ warm months. A warmer summer lengthens the melt season and raises the melt rate, so the margin retreats.
> 7. $0.32\times1.49\times10^8=4.8\times10^7$ km².
> 8. Winter accumulates snow regardless; what decides the net balance is whether the **summer** melts it; at high latitudes the summer insolation changes most with tilt and precession; ice integrates the mass imbalance over thousands of years, so its maximum lags the insolation minimum.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (1): the other tool's concept notes from the lectures, unreviewed
> [[zettel/land-ocean-thermal-contrast|Land-Ocean Thermal Contrast]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | perihelion/aphelion, Kepler II, Milankovitch theory, eccentricity, apsidal and axial precession, obliquity, precession of the equinoxes, ice cores, sediment cores, landforms, LGM, Pleistocene | [[Lecture9_Orbital_cycles - Copypptx_250918_132736 (1).pdf]], pp. 2–26 (text layer read this session; pictures not seen) | taught (2025) |
> | seasonal cycle and continentality, snow, glacier mass balance, orbital changes and glaciation, 23 %, 6 %, 0.2 %, 10–12 %, lag, next glaciation | [[Lecture10_Glaciations_250918_132625 (1).pdf]], pp. 2–26 (text layer read this session) | taught (2025) |
> | exact daily insolation and annual means | `scripts/cl10lib.py` (CL10), `scripts/cl_neena_numbers.py` (cl17), `scripts/fig_cl16_21.py`, tool `cl_milankovitch` | extra/beyond |
>
> **Notes.** [!verify] Slide inconsistencies in §2. The "why the north" argument, the feedbacks for global synchrony and the 100-kyr puzzle are **not** in the slides and are recalled, not read. The combined precession period of 20.9 kyr is derived from the two periods the lecture gives. The $\varpi$ convention is the solar longitude of perihelion measured from the March equinox (today $\approx283^\circ$).
