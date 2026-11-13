---
title: CL28 Tutorials II - Earth's Energy Budget from Space (CERES)
aliases: [CL28, CERES, EBAF, CERES energy budget explorer, cloud radiative effect, cloud effect, column energy budget, El Nino energy budget, Joy tutorial 3]
subject: climate
type: chapter
chapter: 28
part: VI
scope: [taught, extra-beyond]
by: [joy]
status: draft
prereq: ["[[CL22 The Ocean's Ledger I - Accounting for Energy]]", "[[CL03 Radiation and Planetary Energy Balance]]", "[[CL20 ENSO and the Walker Circulation]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/joy, status/draft]
---
# CL28 · Tutorials II: Earth's Energy Budget from Space (CERES)

◀ [[CL27 Tutorials I - Daisyworld with Land and Ocean]] · [[Climate - Course Map|Course Map]] · (last chapter written so far in Part VI)

<span class="scope-taught">taught · in syllabus (2026 Joy, tutorial "CERES energy budget explorer")</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> Joy's handout "Earth's energy budget from space: a guide to the CERES explorer" (17 pages, read in full; text in `earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/transcripts/tut_pdf/handout.txt`) and **the data behind the app** (CERES EBAF Ed4.2.1 TOA and surface monthly means averaged to a 2° grid, January 2010 – January 2025, plus the NOAA CPC Niño-3.4 index), which I downloaded from the course site and **recomputed**: `scripts/fetch_ceres_zarr.py`, `scripts/joy_ceres_numbers.py`, `scripts/fig_cl28_ceres.py`. All eight exercises reproduce the handout's numbers; the one reconstruction is the poleward-transport convention (CL22 §3). I did **not** run the app itself; the handout's cited papers (Wielicki 1996, Loeb 2018, Kato 2018, Loeb 2020, Trenberth 2009, Stephens 2012, Loeb 2021) were **not read**.

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 what CERES is and what **EBAF** means (and its honest caveats); §2 reading conventions; §3 the eight exercises: TOA pattern, seasons, planetary imbalance, clouds, clear- versus all-sky OLR, the **column puzzle**, **El Niño versus La Niña**, does El Niño change the global budget?
>
> 🔵 **Extra · beyond** (my own)
> - recomputation of every exercise from the data files; the transport convention; the lag correlations

> [!key] After this chapter you can
> - say what CERES measures, what "Energy Balanced and Filled" does, and **which numbers are measured and which are anchored or computed**,
> - read ASR, OLR, net radiation, albedo and the **cloud radiative effect** and their signs,
> - explain the **Sahara** (loses energy while hot), the **warm pool** (gains), why **stratocumulus cool** and **deep convection nearly cancels**,
> - explain the **column puzzle** (the atmosphere loses ≈ 110 W m⁻² by radiation; the surface hands energy up as latent and sensible heat),
> - explain why **El Niño rearranges clouds far more than it changes the global energy budget**.

> [!intuition] The one-sentence story
> The Earth takes in more sunlight than it gives back as infrared in the tropics and less near the poles, so air and ocean carry energy poleward; overall the planet gains ≈ **1.26 W m⁻²**, most of it ending up in the ocean; clouds cool by ≈ **20 W m⁻²**; and the atmosphere, which loses ≈ **110 W m⁻²** by radiation, is kept warm by the evaporation and conduction of the surface.

![[fig_cl28_ceres.png]]
*A: global-mean net TOA radiation (monthly, 12-month mean, trend with the seasonal cycle removed), shaded by El Niño (red) and La Niña (blue) spells. B: outgoing longwave anomaly, DJF 2015–16 (strong El Niño) minus DJF 2010–11 (strong La Niña): the dipole of Exercise 7 (crosses at 1°S 161°W and 1°S 119°E). C: correlation of the global-mean anomalies of net TOA, OLR and ASR with Niño-3.4 as the global series lags (months): Exercise 8. Data: CERES EBAF Ed4.2.1 (2010–2024 climatology), Niño-3.4 from CPC. Script: `scripts/fig_cl28_ceres.py`.*

## 1. What CERES is, and what EBAF is
<span class="scope-taught">taught</span> *handout §1–3*

- **CERES** (Clouds and the Earth's Radiant Energy System): identical **broadband scanning radiometers** flown on Terra, Aqua and NOAA-20. On Terra and Aqua three channels: shortwave (reflected sunlight), total, and a narrow infrared window; **longwave = total − shortwave** (NOAA-20 has a longwave channel). *Broadband* matters: energy, at all wavelengths, is what the budget is about. The top of the atmosphere is the only place where the budget is simple (energy crosses it only as radiation), and no ground station can see it.
- **The app's data:** monthly means on a 1° grid averaged (area-weighted) onto a 2° grid (90 × 180 cells), Jan 2010 – Jan 2025 = **181 months**.
- **EBAF = Energy Balanced and Filled.** *Filled*: clear-sky fluxes (needed for what clouds do) have holes where CERES never sees a cloud-free scene; EBAF fills them with the clear parts of MODIS scenes and radiative-transfer calculations (and fills the hours between passes with geostationary data). *Energy balanced*: each instrument is very stable (so it detects **changes** well) but its absolute calibration is uncertain by a few W m⁻², more than the planet's whole imbalance; so the SW and LW fluxes are adjusted, each within its uncertainty, so that the long-term global mean net flux matches the **rate at which the ocean is measured to be gaining heat**. Hence: **the size of the global-mean imbalance is anchored to ocean measurements, not measured by CERES alone; the patterns and the changes month to month and year to year come from CERES itself.**
- **Surface fluxes are computed, not measured**: a radiative-transfer model fed with satellite clouds and aerosols and reanalysis temperature and humidity, nudged to agree with CERES at the top. They are less certain than TOA values, and the **column** (TOA − surface) inherits that uncertainty.
- **Cloud radiative effect (CRE)** = (net flux, all skies) − (net flux, clear skies), separately for SW, LW and their sum; the clear-sky flux is that of the whole box with its clouds removed (the "total region" definition used by climate models). Negative = clouds make the Earth (or surface) lose energy relative to clear sky.
- **Why it is used:** the benchmark for climate-model TOA budgets; clouds are the largest uncertainty in how much warming a given CO₂ causes; monitoring the imbalance; and the link to the ocean (the ocean is where the imbalance shows up as warming).

## 2. Conventions in the app
<span class="scope-taught">taught</span> *handout §4*

**Positive = energy going into the thing named**: into the Earth at TOA, into the surface at the surface, into the atmosphere for the column. OLR and absorbed sunlight are plain positive amounts. **Mean** vs **anomaly** (difference from the 2010–2024 average of the same calendar months: the seasonal cycle drops out). **Seasons:** DJF = Dec–Feb etc.; "DJF 2015–16" is Dec 2015 + Jan + Feb 2016. Time series are shaded **red in El Niño spells and blue in La Niña spells** (at least 5 months with the 3-month Niño-3.4 at or beyond ±0.5 °C). Five views: TOA, clouds, surface and column, El Niño versus La Niña, free explore.

## 3. The eight exercises, solved
<span class="scope-taught">taught</span> *handout §5* · <span class="scope-extra-beyond">extra · beyond</span> *every number recomputed (all 2010–2024 annual or climatological means unless stated)*

**Exercise 1: the pattern of the net budget at TOA.** *Predict: where is there a gain, where a loss; same latitude in both hemispheres; hot desert?* Handout | 🔵 recomputed:
- global mean: net **+1.26**, ASR **241.95**, OLR **240.69** W m⁻² | same;
- largest zonal-mean gain **+72 W m⁻² at 1°S** | **+71.5** at 1°S; poles **−126** (89°N), **−91** (89°S) | −126.4, −90.9;
- ASR = OLR near **37°S and 36°N** | 37.2°S, 36.3°N; ASR equator vs 89°N 322 vs 68; OLR 251 vs 195;
- **Sahara** (23°N, 11°E): net **−28** (ASR 255, OLR 283, albedo 0.34); **warm pool** (1°N, 151°E): **+85** (ASR 315, OLR 230, albedo 0.24) | identical.
*Why:* sunlight arrives head-on in the tropics, glancing at the poles (ASR varies a lot), OLR depends on $\sigma T^4$ (varies little), so the curves cross; a region that gains every year should keep warming, so air and ocean carry ≈ **5.8 PW north across 36°N and 5.7 PW south across 36°S** (🔵 5.82 and 5.74 PW after removing the global-mean 1.26 W m⁻² uniformly; 5.7 PW from the north pole or 6.3 PW from the south pole if it is kept: [[CL22 The Ocean's Ledger I - Accounting for Energy]] §3). The Sahara's bright sand reflects, its dry cloudless air lets the hot surface radiate, and its atmosphere is kept warm by sinking air that carried energy from the rainy tropics.

**Exercise 2: seasons.** | Handout | 🔵 |
|---|---|---|
| gain band, January | 67°S to 13°N | −67 to +13 |
| gain band, July | 7°S to 81°N | −7 to +81 |
| winter-pole net | −171 (89°N, Jan), −113 (89°S, Jul) | −171, −113 |
| summer-pole net | −23 (89°N Jun), −11 (Jul), −21 (89°S Dec) | −23, −11, −21 |
| incoming sunlight (24 h mean) | 517 (89°N, June) vs 386 (equator); 549 (89°S, Dec) vs 412 | 517 vs 386; 549 vs 412 |
| polar albedo | 0.61 (89°N June) ⇒ absorbs 201; 0.70 (89°S Dec) ⇒ 166 | 0.61, 201 ✓ (the 89°S values are the handout's) |

*Why:* at the solstice the polar Sun is low but shines all day, so the pole receives more (24-h mean) sunlight than the equator; it absorbs little because snow, ice and summer clouds make it bright (albedo 0.61), so it is near balance, and Antarctica (albedo 0.70) is brighter still, so the southern summer gain stops at 67°S, over the ocean around the ice sheet. In winter the polar night gets no sunlight but keeps radiating; the energy carried in keeps it from getting colder and colder, so the poleward transport is **strongest in winter**.

**Exercise 3: the planetary imbalance.** Global net **+1.26 W m⁻²** (ASR 241.95 − OLR 240.69), only **0.5 %** of the absorbed sunlight. Monthly values swing from ≈ −9 (June) to ≈ +9 (February) (🔵 −8.5 to +9.2). **Trend +0.61 W m⁻² per decade** (🔵 0.61 with calendar-month means removed; 0.63 including Jan 2025; the raw regression, which does not remove the seasonal cycle from a record that starts in January and ends in January, gives 0.40: the reason the handout fits month by month); 2010–2014 average **+0.93**, 2020–2024 **+1.50** (🔵 identical); smallest year 2010 (+0.24), largest 2023 (+2.06) (🔵 identical). 🔵 **Energy per year:** 1.26 W m⁻² × 5.1×10¹⁴ m² × 3.156×10⁷ s = **2.0×10²² J**. Most goes into the ocean ([[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §8). The imbalance exists because greenhouse gases keep accumulating; part of the increase is more absorbed sunlight (fewer low clouds, less snow and sea ice, cleaner air). The seasonal swing is unrelated (perihelion in early January; the Southern Hemisphere is mostly ocean). *Caveat from §1:* the size of the mean is anchored to ocean heat measurements; the change since 2010 comes from CERES.

**Exercise 4: clouds cool the planet.** Global net CRE **−19.6 W m⁻²** = SW **−45.0** + LW **+25.4**; without clouds the Earth would gain **+20.9 W m⁻²** instead of +1.26 (🔵 −19.65 = −45.01 + 25.37; clear-sky net 20.91). Places (net / SW / LW; cloud cover; cloud-top temperature) | 🔵 identical:

| Place | Net | SW | LW | Cloud | Top T |
|---|---|---|---|---|---|
| off Peru 19°S 81°W | −69 | −84 | +15 | 87 % | 279 K |
| off Namibia 17°S 7°E | −48 | −57 | +9 | 78 % | 284 K |
| off California 27°N 125°W | −48 | −64 | +16 | 78 % | 276 K |
| warm pool 1°N 151°E | −9 | −59 | +50 | 83 % | 239 K |

Net effect positive (red) over Greenland and Antarctica, up to **+39 W m⁻² at 61°N, 45°W** (🔵 +39). *Why:* SW effect depends on how much brighter the cloud is than what lies below; LW effect on how much colder the cloud top is than the surface. Off Peru, Namibia and California the clouds are **stratocumulus**: low, flat, bright, covering most of the sky, with tops nearly as warm as the sea (they hide little infrared), under sinking air: SW wins, strong cooling. Over the warm pool the clouds are deep convective towers and anvils: reflective but with tops at 239 K (−34 °C) that trap much infrared: the two effects **nearly cancel**. Over snow the surface is already bright so clouds add little reflection but still trap infrared: they **warm**. Globally cooling wins by a lot: **≈ 15 times the planet's imbalance**, which is why a small change in clouds matters so much.

**Exercise 5: clear-sky and all-sky OLR.** Warm pool: **230** all-sky, **280** clear-sky (clouds hold back **+50**; 83 % cover, tops 239 K); Sahara: **283** vs **293** (+10; 17 % cover) | 🔵 identical (🔵 Sahara cloud-top 250 K). With the clouds removed the two differ by only ≈ 13 W m⁻²; with clouds the warm pool emits ≈ 53 W m⁻² less. A cloud top at 239 K emits $\sigma T^4=$ **185 W m⁻²** (🔵), far less than the warm sea below; where deep clouds cover most of the sky the planet "shows" space its cold tops. Even clear-sky the warm pool emits less than the Sahara though its surface is as warm: its air is full of water vapour, which absorbs the surface infrared and re-emits it from higher, colder levels, while the Sahara's dry air lets it escape. (Hence low tropical OLR marks deep raining convection.)

**Exercise 6: the column puzzle.** Global means: TOA **+1.26**, surface **+111.6**, column **−110.4 W m⁻²** (column = TOA net − surface net); the column absorbs **+77.9** of sunlight but loses **−188.3** in the longwave | 🔵 +1.26, +111.6, −110.4; +77.9, −188.3. The column loses energy by radiation in **every one of the 16,200 cells** (🔵 the best is −53.5 at 3°N, 97°E; the worst −158 at 23°S, 75°W). **Warm pool column −81, off Peru −157, Sahara −69; surface gains warm pool +166, Peru +151, Sahara +42** (🔵 identical). *Why:* radiation alone would cool the atmosphere by ≈ **0.9 K per day** (🔵 0.95 K day⁻¹ for 110 W m⁻² on ≈ 10⁷ J m⁻² K⁻¹); it does not, so something else heats it by the same amount: the surface, which gains 111.6 W m⁻² by radiation yet does not keep warming, hands its excess up by **latent heat** (evaporation, released when vapour condenses into rain; estimates ≈ 80 W m⁻², Trenberth et al. 2009 gave 80, Stephens et al. 2012 gave 88 ± 10) and **sensible heat** (≈ 17–24 W m⁻²: 17, 24 ± 7); the sums 97 and 112 bracket 110. **1 mm of rain per day ≈ 29 W m⁻²**, so 80 W m⁻² of latent heating means ≈ **2.8 mm per day** of global-mean rain (🔵 2.76). **The twist:** if rain balanced the radiation place by place the rainiest places would show the biggest radiative loss; over the oceans the opposite holds: the warm pool loses only −81 (its high thick clouds trap infrared: column cloud effect +40), the dry subtropical oceans lose most (−157). Dry land differs: the Sahara's ground gets very hot, loses −130 W m⁻² as infrared (much absorbed by the air above) and also heats the air directly, so its column loses only −69. So rain cannot balance the budget place by place: **the atmosphere moves energy sideways**; condensation in the rain belts releases far more than the column loses, the air rises, spreads to the subtropics and sinks, warming by compression the dry columns that lose the most (**the Hadley circulation**). Off Peru the sea gains a lot by radiation (+151) but much of that warms cold water welling up along the coast: another place where the ocean stores and moves energy ([[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] §7).

**Exercise 7: El Niño versus La Niña.** DJF 2015–16 (Niño-3.4 +2.5 °C) minus DJF 2010–11 (−1.4 °C), tropical Pacific. OLR difference: **−92 W m⁻² at 1°S 161°W** (🔵 −92), strongest **−104 at 1°N 173°W** (🔵 −104 at 1°N, 173°W), **+30 at 1°S 119°E** (🔵 +30): a **dipole**. At 1°S 161°W the cloud effects change a lot in opposite directions (SW **−81**, LW **+71**), so the net cloud effect changes only by −10; net radiation changes far less than OLR: **+7 W m⁻²** at 1°S 161°W and +11 at 1°S 119°E (🔵 +7 at 1°S 161°W), while absorbed sunlight changes almost as much as OLR (−84), the two nearly cancelling. 2023–24 minus 2020–21 (Niño-3.4 +1.8 vs −1.1 °C): the same dipole, weaker and further west: largest OLR drop −67 at 3°N 177°E, only **−16** at 1°S 161°W (🔵 −16 at 1°S 161°W). *Why:* deep convection sits over the warmest water, normally the western Pacific warm pool; in El Niño the warm water and convection shift **east** (more high cold cloud in the central Pacific, much lower OLR; less over the maritime continent, higher OLR), the Walker circulation weakens and shifts ([[CL20 ENSO and the Walker Circulation]]). The net radiation hardly changes for the reason of Exercise 4: deep convective clouds reflect about as much sunlight as the infrared they trap, and moving them east moves both together: **El Niño rearranges clouds and rain far more than it changes the energy gained at TOA**; its energy effect is mainly at the surface and inside the ocean and atmosphere (the ocean releases heat to the atmosphere). No two El Niños are alike (2023–24 peaked further west and the clouds followed).

**Exercise 8: does El Niño change the global budget?** DJF 2015–16 minus 2010–11: global-mean OLR anomaly **+0.61** (A) and **−0.60** (B), A−B **+1.22 W m⁻²**; net anomaly **−0.69** and **−0.25**, A−B **−0.44** (🔵 identical). 2023–24 minus 2020–21: OLR **+0.76**, net **+0.39** (opposite sign: absorbed sunlight rose even more, +1.15). Monthly global net anomaly: standard deviation **0.7 W m⁻²** (🔵 0.67), range ±1.7. Correlation with Niño-3.4 (same month | strongest, lag), 🔵 identical to the handout:

| Global anomaly of | same month | strongest |
|---|---|---|
| net radiation (TOA) | **+0.03** | **−0.23, 6 months later** |
| outgoing longwave | **+0.32** | **+0.41, 2 months later** |
| absorbed sunlight | **+0.27** | **+0.27, same month** |

(Averaged over El Niño months the global OLR anomaly is +0.39 W m⁻², over La Niña months −0.20.) *Why:* in El Niño the ocean releases heat to the atmosphere over the central and eastern Pacific, the atmosphere warms and emits more infrared (global OLR rises, peaking ≈ 2 months after Niño-3.4); on its own that would make the Earth lose energy, but the absorbed sunlight changes too as clouds rearrange, and in these years it rose along with OLR; the two largely cancel, and only ≈ half a year after the peak does the global net show a small loss (−0.23). La Niña does the reverse. **A little, and late**: El Niño mainly moves energy between ocean and atmosphere and from place to place; the long-term imbalance (Exercise 3) is set by greenhouse gases and the planet's reflectivity, and El Niño adds wiggles. **2023** shows how much else matters: an El Niño year might be expected to lose energy, yet the Earth gained more in 2023 than in any other year of the record (🔵 +2.06), mostly because it absorbed more sunlight.

## 4. Practice
1. **Convention.** Using the zonal net curve of figure A in [[CL22 The Ocean's Ledger I - Accounting for Energy]], explain why the transport at 36°N is 6.3 PW integrating from the south pole and 5.7 PW from the north pole, and what 5.8 PW assumes.
2. **Imbalance in joules.** Convert +1.26 W m⁻² to joules per year and to a fraction of the sunlight absorbed; if 91 % goes into a 700 m ocean layer, by how much would it warm in a year (ocean area 3.6×10¹⁴ m², ρc = 4.1×10⁶)?
3. **Clouds.** Why do the clouds off Peru cool by 69 W m⁻² while those over the warm pool cool by only 9? Use SW, LW, cloud-top temperatures.
4. **Column.** Show that the column's radiative loss (110 W m⁻²) would cool the atmosphere by ≈ 0.9 K per day, and convert 80 W m⁻² of latent heat into a rain rate.
5. **El Niño.** In Exercise 7, why does OLR drop by 92 W m⁻² at 1°S 161°W while net radiation changes by only +7?
6. **Correlation.** Why is the net-radiation correlation with Niño-3.4 −0.23 at a 6-month lag but +0.03 in the same month?

> [!example]- Solutions
> 1. The net curve integrates to the global imbalance 1.26 W m⁻² × 5.1×10¹⁴ m² = 0.64 PW. Integrating from the south pole counts it in the northern flux (6.33), from the north pole it does not (5.69). Subtracting the global mean uniformly: $6.33-0.644(1+\sin36^\circ)/2=5.82$ PW (5.8 PW assumes the 0.64 PW is spread uniformly over the globe rather than left at either end).
> 2. 1.26 × 5.1×10¹⁴ × 3.156×10⁷ = 2.0×10²² J per year, 0.52 % of the 241.95 W m⁻² absorbed. 0.91 × 2.0×10²² = 1.8×10²² J into 3.6×10¹⁴ × 700 = 2.5×10¹⁷ m³ ⇒ ΔT = 1.8×10²² / (4.1×10⁶ × 2.5×10¹⁷) = **0.018 K per year**: the ocean's inertia: a large heat uptake barely shows at the surface.
> 3. Off Peru: low, bright stratocumulus (cloud cover 87 %) with tops at 279 K, almost as warm as the sea, so the LW effect is only +15 while the SW effect is −84. Warm pool: deep convective towers with tops at 239 K, so LW = +50, nearly cancelling SW = −59: net −9.
> 4. $110\times86400/10^7=0.95$ K day⁻¹ (atmospheric heat capacity ≈ 10⁷ J m⁻² K⁻¹). Latent heat of vaporisation 2.5×10⁶ J kg⁻¹: 80 W m⁻² × 86400 s / 2.5×10⁶ = **2.76 mm day⁻¹**.
> 5. Convection and its cold high cloud move east: OLR falls strongly, but the same clouds reflect more sunlight (absorbed sunlight −84), so the two nearly cancel.
> 6. Same month: the ocean heat released to the atmosphere raises OLR (+0.32) and the changing clouds raise absorbed sunlight (+0.27), cancelling in the net (+0.03); six months later, the OLR contribution persists while the cloud contribution has faded, so the net becomes slightly negative (−0.23).

## Map of this chapter
> [!connection] How CL28 connects
> **Builds on:** [[CL22 The Ocean's Ledger I - Accounting for Energy]] (the same data and the transport), [[CL03 Radiation and Planetary Energy Balance]] (ASR, OLR, albedo), [[CL20 ENSO and the Walker Circulation]] (Neena's ENSO), [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] (the ocean's uptake).
> **Concepts:** [[Sea Surface Energy Budget]] · [[Zero-Dimensional Energy Balance Model]] · [[Albedo]] · [[Cloud Radiative Effect]]

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | CERES, EBAF, conventions, eight exercises, sources | Joy's CERES handout (`transcripts/tut_pdf/handout.txt`, read in full; `tutorials/ceres-energy-budget/handout.pdf`) | taught (2026) |
> | every 🔵 number and figure | CERES explorer data files (`assets/data/series/global.json`, `nino34.json`, `ceres.zarr/clim` and year chunks) via `scripts/joy_ceres_numbers.py`, `scripts/fetch_ceres_zarr.py`, `scripts/fig_cl28_ceres.py` | extra-beyond |
>
> **Notes.** Data and numbers are the app's (CERES EBAF Ed4.2.1; Niño-3.4 from ERSSTv5, 1991–2020 base); the 89°S albedo values and the sensible/latent heat estimates are the handout's. Not run: the app. The latent and sensible heat references (Trenberth et al. 2009; Stephens et al. 2012) and the CERES papers were not read.
