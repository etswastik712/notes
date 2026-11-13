---
title: CL22 The Ocean's Ledger I - Accounting for Energy
aliases: [CL22, climate as accounting, three hats, net radiation at the top of the atmosphere, poleward energy transport, energy ledger, Joy O1, Joy O2, Joy O3, CERES energy budget]
subject: climate
type: chapter
chapter: 22
part: VI
scope: [taught, extra-beyond]
by: [joy]
status: draft
prereq: ["[[CL03 Radiation and Planetary Energy Balance]]", "[[CL10 Global Energy Balance and Meridional Structure]]", "[[CL11 Mean Meridional Circulation and Angular Momentum]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/joy, status/draft]
---
# CL22 · The Ocean's Ledger I: Accounting for Energy

◀ [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] · [[Climate - Course Map|Course Map]] · ▶ CL23 (planned: heat capacity and inertia)

<span class="scope-taught">taught · in syllabus (2026 Joy, ocean module, O1 and the start of O2/O3)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> **Joy Monteiro's 2026 ocean module is the primary source for Joy's part**, in the priority order the user set: (1) the slide decks on the course site, (2) the readings, (3) the lecture and tutorial handouts, (4) Neena's 2025 slides. This chapter uses **slides** (Week 1 deck, O1, and the Week 2 deck's heat-transport frames; PDFs of the decks are in `earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf/`), the **O1 handout**, the **CERES tutorial handout** and **the CERES data behind it**, which I re-computed (`scripts/joy_ceres_numbers.py`). The O1 core reading (Hartmann 2016 §2.8–2.9, pp. 40–48) is on Joy's list but **was not read in this pass**, so nothing here is cited to it. Neena's 2025 treatment of the same ground is in [[CL10 Global Energy Balance and Meridional Structure]] and [[CL18 The Ocean as the Climate System's Heat Reservoir]]; CL22 does not replace them, it re-frames them as Joy teaches it.

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 climate as **accounting**: energy, momentum, mass, salt, carbon ledgers; the **three hats** (accountant, data scientist, physicist/biologist); §2 a planet as **one dot**: the books must balance; §3 why one dot is not enough; §4 Earth's **map of net radiation** and the **5.8 PW** that must cross each latitude; §5 moving energy moves **mass and momentum**; §6 **"it depends"**: every answer has a scale; §7 who absorbs the sunlight (the ocean takes about half); §8 the ocean's **surface budget** and why the air above stays humid; §9 who carries the heat (**transport = mass moved × energy contrast**; the Gulf Stream sum)
>
> 🔵 **Extra · beyond** (my own, labelled)
> - re-computation of the CERES numbers from the tutorial's data files, including **which convention gives 5.8/5.7 PW**; the 1,100 K and 3-year sums checked; the Practice section (the CERES exercises worked)

> [!key] After this chapter you can
> - explain why a planet **cannot stay out of balance** and why Earth's *places* are never in balance,
> - read the **zonal-mean ASR/OLR curves**, find where they cross (≈ 37°S and 36°N) and turn the net curve into the **poleward transport**, with its convention caveat,
> - do the two **accounting thought experiments** (1,100 K; 3 years) and say what they prove,
> - derive the **bulk-formula argument** for why near-surface air over the ocean sits near 80 % relative humidity,
> - do the **Gulf Stream sum** and state the "mass × contrast" rule for heat transport.

> [!intuition] The one-sentence story
> Climate science is **bookkeeping**: every place gains or loses energy (and momentum, mass, salt, carbon) and the winds and currents are how the books are kept balanced. The tropics gain about **+72 W m⁻²** and the poles lose about **−126 W m⁻²**; without transport the tropics would warm by ~1,100 K in 20 years, so ~**5.8 PW** must be carried poleward, by the air mostly, by the ocean near the equator.

![[fig_cl22_energy_ledger.png]]
*A: zonal-mean absorbed sunlight (ASR), outgoing longwave (OLR) and net radiation, CERES EBAF Ed4.2.1, 2010–2024 annual mean. B: northward transport implied by the net curve, with and without the +1.26 W m⁻² global imbalance. Numbers: `scripts/joy_ceres_numbers.py`; figure: `scripts/fig_cl22.py`.*

## 1. Climate as accounting
<span class="scope-taught">taught</span> *Joy O1 handout §7; Week 1 deck; the O1 handout also records "the best climate scientists are accountants"*

Argha's module was energy balance, Suhas's was air in motion; Joy's thesis is that these are **one** subject: a planet's climate is a set of **account books** and the circulation of air and water is how the books are kept balanced. The module keeps four ledgers, one a week:

| Ledger | Week |
|---|---|
| Energy | 1 |
| Momentum | 2 |
| Mass and salt | 3 |
| Carbon (and N, P, Fe, Ca, which life in the ocean needs) | 4 |

For each ledger three **hats**: **accountant** (which budget, what goes in and out?), **data scientist** (what does it look like in the data?), **physicist or biologist** (why does it look like that?). Later chapters label sections with the hat being worn: CL23 (planned) for the heat capacity, CL24 momentum, CL25 salt, CL26 mass.

## 2. A planet as one dot, and why one dot is not enough
<span class="scope-taught">taught</span> *O1 handout §2–3*

- **The books must balance.** A planet gaining even a few W m⁻² for a billion years would heat until its rock boiled; one losing them would cool to the ≈ 3 K cosmic background. Thousands of observed planets are neither, so on average planets are near balance. Exceptions: **Jupiter** radiates about twice what it absorbs (≈ 7 in, ≈ 14 out, W m⁻², Argha's numbers; leftover formation heat); **55 Cancri e** is a lava world.
- **Earth's internal heat is negligible:** geothermal flux ≈ **0.09 W m⁻²** against ≈ **240 W m⁻²** absorbed, a ratio of ≈ 2,700 (🔵 my division), because heat leaks out slowly through the lithosphere. So Earth's balance is purely radiative.
- **One dot hides the map.** Many habitable-zone planets around small cool stars are probably tidally locked: the *global mean* can say "temperate" while the day side scorches and the night side freezes. Heat transport decides habitability, and it can decide *which climates are possible* (Joy's pointer: tidally locked planets are modelled as having no snowball bistability, Checlair et al. 2019; the paper was **not read**).

## 3. Earth's map: no place is in balance
<span class="scope-taught">taught</span> *O1 handout §4; CERES tutorial, Exercises 1 and 3* · <span class="scope-extra-beyond">extra · beyond</span> *my recomputation*

CERES (EBAF Ed4.2.1, 2° grid, **2010–2024 annual mean**; recomputed from the tutorial's data files):

| Quantity | Value (recomputed) |
|---|---|
| global-mean ASR / OLR / net | **241.95 / 240.69 / +1.26** W m⁻² |
| largest zonal-mean gain | **+71.5** W m⁻² at 1°S |
| zonal-mean net near the poles | **−126.4** (89°N), **−90.9** (89°S) |
| ASR = OLR at | **37.2°S** and **36.3°N** |
| ASR equator vs 89°N | 322 vs 68 W m⁻² |
| OLR equator vs 89°N | 251 vs 195 W m⁻² |
| Sahara (23°N, 11°E) | net **−28** (ASR 255, OLR 283, albedo 0.34): bright, dry, hot |
| West-Pacific warm pool (1°N, 151°E) | net **+85** (ASR 315, OLR 230, albedo 0.24): dark ocean, cold cloud tops |

**Why the curves cross.** Sunlight arrives almost head-on in the tropics and glances off the poles, so ASR varies a lot with latitude; OLR depends on temperature (σT⁴), which varies much less. The Sahara loses energy *despite* being hot and sunny.

**The accounting thought experiment (Joy O1).** Put the tropical gain (+72 W m⁻²) into the top 10 m of ocean and carry nothing away: in 20 years ΔT = 72 × 20 × 3.156×10⁷ / (4.2×10⁶ × 10) ≈ **1,080 K** (🔵 recomputed; Joy: "about 1,100 K"). Put the polar loss (−126 W m⁻²) on 10 m of water and it would be 273 K colder after 273 × 4.2×10⁷ / 126 / 3.156×10⁷ ≈ **2.9 yr**, i.e. down to absolute zero (Joy: "about 3 years"). Neither has happened, so energy is **moved**. (Joy's caveat: this asks where the energy *went*, not what would happen if transport stopped. If it stopped, temperatures would change, the radiation would change and each latitude would find its own balance: the tutorial's first-principles runs.)

**The transport.** Integrate the net curve from a pole: northward transport across latitude φ is

$$F(\varphi)=2\pi R^2\int_{-90^\circ}^{\varphi}\overline{N}(\varphi')\cos\varphi'\,d\varphi' .$$

🔵 **Convention (my finding).** Integrating the raw net curve gives **6.3 PW** at 36°N (from the south pole) or **5.7 PW** (from the north pole), because the global imbalance (+1.26 W m⁻² = 0.64 PW) has to go somewhere. Subtracting the global mean **uniformly** first gives **5.82 PW northward at 36°N** and **5.74 PW southward at 36°S**: these are the "5.8 and 5.7 PW" of Joy's handout and slides. Treat the third digit as convention, not measurement.

## 4. Moving energy means moving mass and momentum
<span class="scope-taught">taught</span> *O1 handout §5*

- **Mass.** If air kept flowing poleward out of the tropics, the tropics would run out of air: what goes poleward must come back. That closed loop is the **Hadley cell** ([[CL11 Mean Meridional Circulation and Angular Momentum]]).
- **Angular momentum.** A parcel moving poleward on a rotating sphere nears the axis and spins faster; keeping its angular momentum all the way it would reach about **130 m s⁻¹** in the subtropics (Joy's figure). Such shear is unstable, so the Hadley cell ends. On slowly rotating **Titan** one cell reaches almost to the poles; on fast rotators energy must be passed poleward in **shorter steps** (more cells).
- **Momentum is exchanged with the solid Earth:** where surface winds are westerly the air gives momentum to the ground, in the trades the air gains it. Even the **length of day** varies slightly as air and water shift. This is the bridge to the momentum ledger of CL24.
- **Why a fluid at all?** The Moon has no air or ocean, only conduction through rock: about 100 K at night to 390 K by day at its equator. Only a moving fluid evens a planet out.

## 5. "It depends": every answer has a scale
<span class="scope-taught">taught</span> *O1 handout §6*

Atmosphere: days to weeks. Ocean, land, vegetation, ice: years to millennia (El Niño, ice ages, Milankovitch cycles). The slow parts set the conditions the fast parts respond to; an ice sheet looks still but changes albedo, heat capacity and the fresh water the ocean sees. So the right first words to "is X important for climate?" are **"it depends"** on the space and time scale. Newton's laws are scale-free; climate's "laws" are not. For the ice ages ignore the atmosphere; for next week's weather ignore the ice sheets.

## 6. Who absorbs the sunlight
<span class="scope-taught">taught</span> *O1 handout §8; Week 2 deck, frame 1*

Of ≈ **242 W m⁻²** absorbed, ≈ **78** (a third) is absorbed **in the atmosphere** and ≈ **164** at the surface. The ocean covers 72 % of the surface but takes ≈ **77 %** of the surface's share: ≈ **126 W m⁻²** global-mean equivalent (🔵 0.77 × 164 = 126; 126/242 = 52 %), "about half of all the sunlight Earth absorbs" (slide: ✓ CERES EBAF).

## 7. The ocean's surface budget, and why the air stays humid
<span class="scope-taught">taught</span> *O2 handout §3; Week 2 deck frames 5–10*

Sunlight comes in; the sea loses energy as **infrared**, **conduction** (sensible heat, small) and **evaporation** (latent heat, the biggest). For the tropical ocean the handout quotes Hartmann §10.6 (p. 315): ≈ 200 W m⁻² in, 120 evaporation, 50 net infrared, 10 conduction, ≈ 20 carried off by currents. (The Hartmann pages are on the O2 list but **not read here**; the numbers are as given in Joy's handout.) The slides' latitude strips (tropical-ocean zonal means: ≈ 222 W m⁻² sunlight, ≈ 48 net infrared, ≈ 145 evaporation + conduction as the residual, net ≈ +29) add that the terms go roughly as **wind × difference**, so every gust, dry spell or cloud is a **kick F′(t)** to the surface budget: *weather is a fluctuating push* (used in CL23).

> [!example] Why relative humidity over the ocean is ≈ 80 % (Joy's "promised" argument, O2 handout §3)
> Bulk formula: $LE\approx\rho\,L\,C\,U\,q^*(T_s)\,(1-\mathrm{RH})$. With ρ = 1.2 kg m⁻³, L = 2.5×10⁶ J kg⁻¹, C = 1.2×10⁻³, U = 7 m s⁻¹, q* = 0.022 kg kg⁻¹ (27 °C): the prefactor is **554 W m⁻²** (🔵 recomputed), so $LE\approx 550\,(1-\mathrm{RH})$ W m⁻².
> - At RH = 0.80: ≈ **110 W m⁻²**, close to Hartmann's 120. Each percentage point of RH is worth ≈ **5.5 W m⁻²**; drying the air from 80 % to 70 % would add ≈ 55 W m⁻² of evaporation, which sunlight cannot pay, so the sea would cool and moisten the air back.
> - Humid air shuts evaporation off, the unspent sunlight warms the sea, and evaporation resumes. So the surface budget **pins** $1-\mathrm{RH}\approx 110/550\approx 0.2$. Joy's caveat: back-of-envelope with typical numbers, not a full theory; winds, air temperature and dry air mixed down move it by a few per cent.

**Why evaporation peaks in the subtropics (15–30°).** Evaporation ∝ wind × (vapour the air could hold − vapour it holds). The **sinking Hadley branch** brings very dry air over a warm sea with steady trades; at the ITCZ the near-surface air is already humid and winds are weak. The dip in sunlight just north of the equator is the ITCZ cloud ([[CL14 Observed Winds - Jets, Trades and the ITCZ]]). Concept notes: [[Sea Surface Energy Budget]], [[Bulk Aerodynamic Formulas]].

## 8. Who carries the heat: mass × contrast
<span class="scope-taught">taught</span> *Week 2 deck frames 46–50; O3 handout §7*

Across 35°N the total of ≈ **5.8 PW** is shared: the **atmosphere** dominates poleward of ≈ 30°, the **ocean** matters most in the deep tropics, where the total is small and the ocean carries as much as or more than the air. Observational estimates put the ocean's share near **2 PW** around 20°N (Joy cites Stewart Fig. 5.11 and Trenberth and Caron 2001; the slide notes the reanalysis's own surface fluxes imply only ≈ **1.2 PW** at 14°N: the lines of evidence disagree, and Joy says so).

**The accountant's rule: transport = mass moved × energy contrast** (Czaja and Marshall 2006; the paper was not read). Air moves far more mass; water carries far more heat per kilogram per degree.

> [!example] The Gulf Stream sum (Joy O3)
> 1 Sv = 10⁶ m³ s⁻¹. Width 100 km, depth 600 m, speed 0.5 m s⁻¹: $Q=10^5\cdot 600\cdot 0.5=3\times10^7$ m³ s⁻¹ = **30 Sv**. With a ~6 °C contrast, ρ = 1025 kg m⁻³, c ≈ 4200 J kg⁻¹ K⁻¹: $\rho c Q\Delta T\approx 0.77$ PW per current (🔵), so the Gulf Stream plus the Kuroshio ≈ **1.5–1.6 PW**, the slide's "~1.6 PW" (Joy cites Hartmann §7.8, not read).
> Per unit cross-section and degree, water carries ρc·v: ≈ 4×10⁵ W m⁻² K⁻¹ for a 0.1 m s⁻¹ current against 1.2×10⁴ for a 10 m s⁻¹ wind, **≈ 34 times more** (O3 handout).

## Map of this chapter
> [!connection] How CL22 connects
> **Builds on:** [[CL03 Radiation and Planetary Energy Balance]] (ASR/OLR, Planck), [[CL10 Global Energy Balance and Meridional Structure]] (meridional structure; Neena's version of the transport), [[CL11 Mean Meridional Circulation and Angular Momentum]], [[CL14 Observed Winds - Jets, Trades and the ITCZ]], [[CL18 The Ocean as the Climate System's Heat Reservoir]] (Neena L20, surface budget, MHT).
> **Leads to:** CL23 heat capacity and inertia (the slab driven by F′(t)), CL24 momentum ledger, CL25 salt ledger, CL26 mass ledger (all planned); the CERES data below are also used for El Niño in [[CL20 ENSO and the Walker Circulation]].
> **Concepts:** [[Sea Surface Energy Budget]] · [[Bulk Aerodynamic Formulas]] · [[Mixed Layer]] · [[Zero-Dimensional Energy Balance Model]] · [[Planck Sensitivity]] · [[Climate as Accounting]] · [[Cloud Radiative Effect]] · [[Sverdrup (Unit)]]

## Summary
> [!summary] Cheat-sheet
> - Ledgers: energy, momentum, mass/salt, carbon; hats: accountant, data scientist, physicist. Geothermal 0.09 vs ≈ 240 W m⁻².
> - CERES 2010–24: ASR 241.95, OLR 240.69, **net +1.26 W m⁻²** (≈ 2.0×10²² J per year); zonal net +72 (1°S) to −126 (89°N); ASR = OLR at 37°S/36°N.
> - Transport: $F=2\pi R^2\int N\cos\varphi\,d\varphi$; **5.8 PW (N), 5.7 PW (S)** with the imbalance removed uniformly; raw 6.3/5.7 PW (S-pole/N-pole integration).
> - Ocean takes ≈ 126 W m⁻² ≈ half of the absorbed sunlight (78 in the air, 164 at the surface).
> - $LE\approx550(1-\mathrm{RH})$ W m⁻² ⇒ RH ≈ 80 %; Gulf Stream 30 Sv ⇒ ≈ 0.77 PW; water carries ≈ 34× more heat per m² of cross-section than the wind.

## Practice
1. **Accounting.** Put +72 W m⁻² into 10 m of water for 20 years ($\rho c=4.2\times10^6$ J m⁻³ K⁻¹). What is ΔT, and what does the result prove?
2. **Transport convention.** The raw integral gives 6.33 PW at 36°N from the south pole and 5.69 PW from the north pole. Explain the 0.64 PW gap and show how removing the global mean gives ≈ 5.8 PW.
3. **Humidity.** Using the bulk formula above, how much does evaporation change if the wind rises from 7 to 8 m s⁻¹ at fixed RH = 0.8? What must happen to RH to restore the budget?
4. **Gulf Stream.** Redo the sum for a current 80 km wide, 500 m deep at 0.4 m s⁻¹ with ΔT = 5 °C.
5. **The Sahara.** The Sahara loses 28 W m⁻² at TOA although it is hot and sunny. Give the two reasons.
6. **The column puzzle (CERES Ex. 6).** The atmosphere loses ≈ 110 W m⁻² by radiation yet does not cool by ≈ 0.9 K per day. What supplies the energy, and why is rain not balancing the radiation place by place?
7. **El Niño (CERES Ex. 7–8).** In DJF 2015–16 against 2010–11 the OLR difference at 1°S, 161°W is −92 W m⁻² but the net TOA difference is only +7. Explain, and say what the global-mean net radiation does and when.

> [!example]- Solutions
> 1. $\Delta T=72\times20\times3.156\times10^{7}/(4.2\times10^{6}\times10)=1.08\times10^{3}$ K. Nothing like it is observed, so the energy is carried away (not that the tropics would really warm so: the radiation would change).
> 2. The net curve integrates to the global imbalance 1.26 W m⁻² × 5.1×10¹⁴ m² = 0.64 PW. Integrating from the south pole the 0.64 PW is counted in the northern flux (6.33), from the north pole it is not (5.69). Subtract the global mean uniformly: $F_{bal}(36^\circ N)=6.33-0.644\,(1+\sin 36^\circ)/2=6.33-0.51=5.82$ PW; at 36°S $-5.61-0.644(1-\sin36^\circ)/2=-5.74$ PW (🔵 verified numerically).
> 3. $LE\propto U$: 550 W m⁻² × (1−0.8) × 8/7 = 126 vs 110, i.e. **+16 W m⁻²**. The sea must cool and moisten the air: RH rises until $(1-\mathrm{RH})\cdot 8/7=0.2$, i.e. RH ≈ 82.5 %.
> 4. $Q=8\times10^4\times500\times0.4=1.6\times10^7$ m³ s⁻¹ = 16 Sv; $\rho c Q\Delta T=1025\times4200\times1.6\times10^{7}\times5=3.4\times10^{14}$ W = 0.34 PW.
> 5. (i) Bright sand: albedo 0.34 (ASR only 255). (ii) Dry, almost cloudless air, so the hot surface radiates freely (OLR 283 W m⁻²); the atmosphere is kept warm by air that sank after losing its water over the rainy tropics.
> 6. Latent heat (≈ 80 W m⁻², Trenberth et al. 2009; 88, Stephens et al. 2012) and sensible heat (≈ 17–24) from the surface: sums 97 and 112 bracket 110 (as quoted in Joy's CERES handout). Rain cannot balance the radiation locally: the warm pool loses only −81 W m⁻² (high cloud traps infrared, +40) while dry subtropical oceans lose −157 (Peru); the Hadley circulation moves the energy sideways. 1 mm day⁻¹ of rain ≈ 29 W m⁻², so 80 W m⁻² ≈ 2.8 mm day⁻¹ (🔵 recomputed 2.76).
> 7. Deep convection shifts east: OLR drops (cold high cloud) but absorbed sunlight drops almost as much (−84 W m⁻²), the cloud shortwave and longwave effects (−81, +71) nearly cancel, so the net changes by only a few W m⁻². Globally the OLR rises (+1.22 W m⁻² A−B) and the net falls by 0.44, about **six months after** the Niño-3.4 peak (corr −0.23 at 6 months, OLR +0.41 at 2 months, ASR +0.27 at lag 0; all 🔵 recomputed).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | accounting, hats, planet-as-dot, map, thought experiments, mass/momentum, "it depends", who absorbs sunlight | [[handout_o1.md]] (Joy O1 handout, read in full); Week 1 deck [[O1_Week1_The-ocean-ledger.pdf]] | taught (2026) |
> | surface budget, humidity argument, latitude strips, "weather is a fluctuating push" | [[handout_o2.md]]; Week 2 deck [[O2-O3_Week2_Where-does-it-go_and_The-ponderous-ocean.pdf]] frames 1, 5–10 | taught (2026) |
> | who carries the heat, mass × contrast, Gulf Stream | Week 2 deck frames 46–50; [[handout_o3.md]] §7 | taught (2026) |
> | ASR/OLR, crossings, transport, thought-experiment arithmetic, CERES Ex. 1–8 | CERES tutorial handout (`tut_pdf/handout.txt`, read in full) and the explorer's data files, recomputed with `scripts/joy_ceres_numbers.py`, `scripts/fig_cl22.py` | taught (2026) / extra-beyond (recomputation) |
>
> **Notes.** Hartmann pp. 40–48 (O1 core), Hartmann §10.6, §7.8 and Stewart §5.6–5.7 are **cited only as Joy cites them** and were not read in this pass; Kite et al. (2011), Checlair et al. (2019), Czaja and Marshall (2006) and Trenberth and Caron (2001) are not in the course folders. The 5.8/5.7 PW convention (§3) is my reconstruction, confirmed numerically against the handout's values.
