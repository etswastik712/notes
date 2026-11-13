---
title: CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch
aliases: [CL26, mass ledger, overturning circulation, AMOC, thermohaline circulation, deep water formation, North Pacific no deep water, Southern Ocean upwelling, isopycnals, turnover time, RAPID array, Stommel box model, hysteresis, bistability, IPCC AR6 AMOC, Joy O6]
subject: climate
type: chapter
chapter: 26
part: VI
scope: [taught, extra-book, extra-beyond]
by: [joy, book]
status: draft
prereq: ["[[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]]", "[[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]]", "[[CL04 Feedback and Multiple Steady States]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/joy, src/book, status/draft]
---
# CL26 · The Ocean's Ledger V: Mass, the Overturning and the Switch

◀ [[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]] · [[Climate - Course Map|Course Map]] · ▶ CL27 (planned: Daisyworld tutorials)

<span class="scope-taught">taught · in syllabus (2026 Joy, O6)</span> <span class="scope-extra-book">extra · book (Stewart 2008 pp. 222, 229: read)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> **Primary source: Joy's O6 deck only** ("The overturning: the slow ocean, and can it switch?", 26 frames, dated 13 Nov 2026; **there is no O6 handout on the site**). PDF with speaker notes: `earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf/O6_The-overturning_with-notes.pdf`. The deck cites Hartmann 2016 pp. 222–231 and Stewart 2008 pp. 211–222; of these I **read** only Stewart p. 222 (the 1,000-year, 1 mm s⁻¹ passage) and p. 229 (RAPID, the Antarctic Circumpolar Current); every Hartmann and other Stewart page is **cited as the slide cites it**. The RAPID record itself (rapid.ac.uk) was **not** downloaded: the 17.0 Sv and its range are the slide's. Neena's 2025 view of the same circulation (600-year ventilation, NADW off Greenland, AABW) is [[CL21 Thermohaline Circulation Water Masses and Sea Ice]]. 🔵 marks my recomputations (`scripts/fig_cl26.py`, which reuses the EOS-80 validation of [[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]]).

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 the **mass ledger**; §2 **where water sinks** and how much; §3 **why not the North Pacific**; §4 **coming back up**: the Southern Ocean, isopycnals, the westerlies; §5 **how slow**; §6 **measuring it** (RAPID); §7 **can it switch?** (Stommel's two boxes, the salt feedback, two stable states, hysteresis, the past); §8 **could it switch off?** (IPCC AR6)
>
> 🟡 **Extra · book** (passages actually read)
> - Stewart p. 222 (1,000 years ⇒ 1 mm s⁻¹, hard to observe against 10 cm s⁻¹ deep currents); p. 229 (the RAPID/MOCHA design and first-year numbers; the ACC transport)
>
> 🔵 **Extra · beyond** (my own)
> - the Stommel model analysed and simulated (branches, collapse, recovery); the Pacific–Atlantic density comparison recomputed; renewal-time and 1 mm s⁻¹ consistency checks

> [!key] After this chapter you can
> - say **where** deep water forms (two regions), **how much** (15–20 Sv and ≈ 10 Sv), and **why not in the North Pacific**,
> - explain how deep water **returns to the surface** in the Southern Ocean (isopycnals, Ekman pumping, the westerlies) and give the **≈ 1,000-year** turnover with its 1 mm s⁻¹ meaning,
> - describe the **RAPID** measurement and why 20 years cannot show a trend in a 1,000-year system,
> - derive the **two stable states** and **hysteresis** of the two-box model and say what is known about past and future switching.

> [!intuition] The one-sentence story
> Heavy water sinks in only two places, so the same mass must **rise** somewhere (mostly the wind-pulled Southern Ocean) and the round trip takes **~1,000 years**; because the northward salt carried by the flow keeps the north heavy, the circulation feeds itself, and a feedback that feeds itself can have **two stable states**: the overturning can be **on or off for the same fresh water**, and off is hard to undo.

![[fig_cl26_overturning.png]]
*A: steady states of the two-box model (my nondimensionalisation of Stommel's idea; q > 0: sinking in the cold box) against freshwater forcing F, with a slow up-and-down ramp of F (black: increasing, green: decreasing). B: surface σ of the North Atlantic (S = 35.1) and North Pacific (S = 32.8) as they are cooled (EOS-80), with the σ of the water at 2,000 m. C: transports in Sv (slide and handout values; RAPID mean from the slide). Script: `scripts/fig_cl26.py`.*

## 1. The mass ledger
<span class="scope-taught">taught</span> *O6 deck frames 1–2*

Momentum (O4), salt (O5), and now **mass**: heavy water sinks, but sea level is not falling, so the same amount has to come back up somewhere. Today: where it sinks, where and how it comes up, how long the round trip takes, and whether it can stop. (Opening question carried from O5: along 165°W in the Pacific there is **no salty tongue from the north**. Why not?)

## 2. Where water sinks, and how much
<span class="scope-taught">taught</span> *O6 deck frames 3–4*

Tracers (oxygen, CFCs, radiocarbon) show that deep water forms today **only at high latitudes in the North Atlantic and in the Southern Ocean** (Hartmann p. 224 and Stewart p. 211 as the slide cites them: "Bottom water is produced only in these two regions").
- **North Atlantic:** the Gulf Stream carries warm salty water north into the **Norwegian and Greenland Seas**, where very cold air cools it until it is dense enough to sink (the **Labrador Sea** also makes deep water). Cooling of salty water, not brine ([[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]] §8).
- **Around Antarctica**, especially the **Weddell and Ross Seas**: brine from sea ice (katabatic winds, polynyas).
- Convection happens in patches a few kilometres across; the sinking that matters for the mass budget is spread over larger areas (Stewart p. 219 as cited).

**How much** (Hartmann p. 230 as cited): North Atlantic **1.5–2×10¹⁰ kg s⁻¹ ≈ 15–20 Sv**, around Antarctica **≈ 10¹⁰ kg s⁻¹ ≈ 10 Sv** (1 Sv = 10⁶ m³ s⁻¹ ≈ 10⁹ kg s⁻¹). For scale: the ACC ≈ **125 Sv**, the Gulf Stream off Florida ≈ **30 Sv** (figure C). Joy's note: do not repeat Hartmann's "more than a factor of ten smaller than the western boundary currents", since his own boundary-current figure (≈ 60 Sv) gives a factor of 3–4; say "smaller than the Gulf Stream, but it fills the whole deep ocean".

## 3. Why not the North Pacific?
<span class="scope-taught">taught</span> *O6 deck frames 5–8*

Both oceans get cold enough to freeze at high latitude (Stewart p. 215 as cited: every ocean makes ≈ −2 °C surface water and only the saltiest sinks; the North Pacific "is not salty enough to sink to the bottom"), so **temperature cannot be the difference**. The surfaces (WOCE annual means, Joy's boxes): **North Atlantic** 50–65°N, 40–10°W: S **35.1**, 10.3 °C; **North Pacific** 45–55°N, 160°E–140°W: S **32.8**, 8.4 °C: the Pacific is **2.3 g/kg fresher**.

Cool each to freezing at its own salinity (🔵 EOS-80, figure B): the North Pacific reaches **σ = 26.4 at −1.8 °C** (Joy: 26.4), still far lighter than the water at 2,000 m beneath it (σ 27.7): it **cannot sink far, however cold it gets**. The salinity it would need at −1.8 °C to match 27.7 is **34.41**, i.e. **1.6 g/kg more** than it has (🔵). The North Atlantic reaches the σ ≈ 27.8 of the water at 2,000 m beneath it once cooled to ≈ **4.6 °C** (🔵; Joy: "below ≈ 4 °C"), well before freezing. **Why so fresh?** [[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]] §4: the trade winds carry fresh water from the Atlantic over Central America into the Pacific (0.32 Sv; surfaces 35.6 against 34.6 g/kg between 30°S and 60°N): *the atmosphere's fresh-water export is what lets the Atlantic overturn.* The oxygen agrees (Hartmann Fig. 7.16 and p. 222 as the slide cites them): high oxygen reaches great depths in the North Atlantic, the North Pacific shows "no evidence of downwelling".

## 4. Coming back up: the Southern Ocean
<span class="scope-taught">taught</span> *O6 deck frames 9–13*

Back to the Ekman pumping map of [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] §7: the **Southern Ocean belt 50–62°S is pulled up ≈ 25 m yr⁻¹**. What comes up there? **The deep water from the North Atlantic.**
- **Along surfaces of equal density.** Below the mixed layer mixing is weak, so deep water moves almost along isopycnals (Hartmann p. 225 as cited). On the 30°W salinity section with the four density surfaces Hartmann draws (σ = 27.2, 27.4, 27.6, 27.8): flat and deep in the north and the tropics; **south of ≈ 45°S they tilt up and reach the surface**.
- **The path.** The NADW goes south at 2–3 km (the salty tongue) and rises along the sloping surfaces (drawn along σ 27.8) "in the vicinity of 60°S" (Hartmann p. 222), where the isopycnals reach the mixed layer (Hartmann p. 225, after Marshall and Speer 2012).
- **What pulls it up: Wednesday's wind.** The westerlies blow east; south of the equator Ekman transport is to the **left** of the wind, i.e. **north**. Poleward of the jet more water leaves than arrives, so water comes up from below; equatorward of it, water is pushed down (Hartmann pp. 225–227). The same wind physics drives the slow ocean's return: **the tie between O4 and O6**. (Eddies matter a lot here and partly cancel the wind's overturning: Hartmann pp. 227, 231; one sentence.)
- **The rest of the loop.** Some risen water is made dense again by cold and brine near Antarctica and sinks as **bottom water**, spreading north along the floor; some goes north near the surface and sinks again at ≈ 1 km as the fresh **intermediate water** ([[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]]). Hartmann p. 225: "The Southern Ocean is thus a key region for both forming bottom water and bringing deep water back to the surface."

## 5. How slow? About 1,000 years
<span class="scope-taught">taught</span> *O6 deck frames 14–15* · <span class="scope-extra-book">extra · book</span> *Stewart p. 222, read*

Week 2's ruler gave τ = C/λ ≈ **140 years** for 4,000 m of water *if it were all mixed at once* ([[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §5). It is not: the deep water is replaced only as fast as it forms and returns; Hartmann p. 225 puts the turnover time "on the order of **1000 years**".
- **Stewart p. 222 (read):** "if the deep circulation takes roughly 1,000 years to transport water from the north Atlantic to the Antarctic Circumpolar Current and then to the north Pacific, the mean flow is about **1 mm/s**. Observing this small mean flow in the presence of typical deep currents having variable velocities of up to 10 cm/s or greater, is very difficult." 🔵 Check: 1,000 yr × 3.156×10⁷ s × 10⁻³ m s⁻¹ = **31,600 km**, indeed the length of the route. Hence most of our knowledge comes from tracers (T–S, oxygen, tritium, fluorocarbons) which are far more stable than direct current measurements.
- 🔵 **Renewal arithmetic.** With an ocean volume of 1.335×10¹⁸ m³ (recalled, used in CL21; not read): at 42 Sv the whole ocean is renewed in 1,007 yr, at the formation rate 17.5 + 10 = 27.5 Sv in ≈ 1,540 yr (≈ 1,380 yr for 90 % of the volume): order 1,000 years, consistent. (Neena's lecture quotes ≈ 600 years for contact with the surface and up to 1,000 for the cycle, CL21 §4: same order.)
- **The oldest water** is not at the bottom near Antarctica but at **middle depths in the North Pacific**, farthest from both formation sites (Hartmann p. 225 as cited); so deep water must slowly rise elsewhere, as the mass budget requires. It matches the oxygen: the deep North Pacific has ≈ **10–15 %** oxygen saturation, the North Atlantic ≈ **85 %** (Hartmann p. 222 as cited).
- **Why it matters for climate.** It is the slow brake on warming (the deep ocean as a heat sink, CL23 §8), and the Southern Ocean warms more slowly than the rest of the globe because the water rising there has not been at the surface for centuries (Hartmann p. 227 as cited).

## 6. Measuring it: the RAPID array
<span class="scope-taught">taught</span> *O6 deck frames 16–18* · <span class="scope-extra-book">extra · book</span> *Stewart p. 229, read*

Since **April 2004** a line of moorings across the Atlantic (Florida to Africa, **26.5°N**) with cable measurements of the Florida Current and satellite winds for the Ekman part measures the whole overturning: **RAPID-MOCHA-WBTS** (UK, US, Florida; dataset v2024.1a, rapid.ac.uk, doi 10.5285/48d0bf43-0598-ceb2-e063-7086abc062f1). Slide numbers (the record was not downloaded here): northward upper-ocean transport, 10-day low-pass, 2004-04-07 to 2024-03-22: **mean 17.0 Sv**; 10-day values from **−4 to 32 Sv**; yearly means from **14.9 Sv (2009) to 19.1 Sv (2006)**. A straight line through the record falls ≈ 0.9 Sv per decade (Joy's own fit, **no significance test, not a course reading; do not present it as a trend**).

Stewart p. 229 (read) describes the early array: bottom pressure, temperature and salinity throughout the water column at **15 locations along 24°N** near the western and eastern boundaries and either side of the mid-Atlantic ridge (since 2004, Church 2007), the Gulf Stream through the Strait of Florida, and satellite wind stress giving the **Ekman transports**; net transport across the section is **zero within accuracy** as expected, and the first year gave a Meridional Overturning Circulation of **18.7 ± 5.6 Sv**, varying from **4.4 to 35.3 Sv**, accuracy ± 1.5 Sv. (Stewart's 24°N and Joy's 26.5°N are the same programme described at different times; the numbers agree in magnitude.) *Never still*: week to week it swings by tens of Sv; year to year 15–19.

**The question Joy leaves on the screen:** twenty years of record for a system with a **1,000-year memory** and large weather swings. Not much yet about a long-term trend; a lot about how the overturning works, and a baseline. (Stewart p. 222 makes the same point about direct measurements of the deep flow.)

## 7. Can it switch?
<span class="scope-taught">taught</span> *O6 deck frames 19–23* · <span class="scope-extra-beyond">extra · beyond</span> *my analysis of the model*

**Two boxes** (Stommel 1961, not a course reading; Stewart pp. 215–218 gives the behaviour, not read here): a warm salty low-latitude box and a cold fresher polar box. Dense water sinks in the cold box and returns at depth; the surface flow carries **salty water north**, which keeps the northern water heavy, which keeps it sinking. **Add fresh water in the north** (rain, rivers, melting ice): the northern box gets lighter, the flow weakens, it carries **less salt north**, the north gets fresher still, and the flow weakens further: a **positive feedback**, the same kind as Argha's ice–albedo feedback ([[CL04 Feedback and Multiple Steady States]]).

🔵 **The model (my nondimensionalisation; Joy's "our calculation, dimensionless").** With $x$ the equator–pole temperature difference and $y$ the salinity difference, flow $q=x-y$ ($q>0$: sinking in the cold box, thermally direct):
$$\dot x=1-x(1+|q|),\qquad \dot y=F-|q|\,y .$$
*Steady states.* $x=1/(1+|q|)$, $y=F/|q|$. For $q>0$:
$$F=\frac{q\,(1-q-q^2)}{1+q},$$
which rises from 0, has a **maximum $F_{\max}=0.141$ at $q=0.30$** and falls (so for $0<F<F_{\max}$ there are **two** thermally driven states, the larger $q$ **stable**, the smaller **unstable**: e.g. at $F=0.10$, $q=0.47$ stable, $q=0.13$ unstable). For $q<0$ (salt-driven, reversed):
$$F=\frac{|q|}{1+|q|}+q^2>0,$$
which is monotonic: for **every $F>0$ there is exactly one reversed/weak state, stable** (e.g. $F=0.10$: $q\approx-0.10$). Both exist for the same forcing: **two stable states**.
*Hysteresis.* Walk the path: (1) freshen slowly along the top branch: the flow weakens a little; (2) past $F_{\max}$ there is **no "on" state left** and the flow **drops** (from $q=+0.30$ to $-0.14$); (3) take the fresh water away again: it **stays off**, because the reversed branch exists for all $F>0$; (4) only when $F<0$, i.e. the **north is saltier than where it started**, does the "on" state return. 🔵 A slow numerical ramp (`fig_cl26.py`) confirms: collapse at $F=0.147$ (analytic 0.141; the small excess is the finite ramp rate) and recovery at $F=0.000$. This is Stewart's remark (p. 218, after Rahmstorf 1995, as the slide quotes it): "Surface waters must become saltier than average for the first state to return." **Hysteresis: where you are depends on how you got there**; the same structure as Argha's snowball multiple equilibria (Stewart Fig. 13.3 draws it in T and S).

**Has it happened?** (slide, Stewart pp. 215–218 as cited, none read): in Rahmstorf's (1995) model **±0.1 Sv** of extra fresh water into the North Atlantic switched a **14 Sv** circulation on or off; ice cores show abrupt changes many times in the last ice age: ≈ **11,500 years ago Greenland warmed by ≈ 8 °C in 40 years** (Alley 2000; 🔵 2 K per decade); **Heinrich events**, surges of icebergs whose melt water is thought to have shut down deep-water formation and chilled the North Atlantic (Fig. 13.2). The causes are still argued over (Stewart p. 218). The model is the **simplest** one: it shows that bistability is *possible*, not that the real ocean has it.

## 8. Could it switch off?
<span class="scope-taught">taught</span> *O6 deck frames 24–26*

Joy's pair-and-share (no right answer; reward reasoning about evidence): which way does warming push the fresh-water ledger (more rain at high latitudes, melting Greenland)? Who lives near the rain belts? What would RAPID show, and how long would we need to watch? **The assessed answer** (slide, quoting IPCC AR6 WGI SPM C.3.4, 2021, ✓ against the SPM on 12 Nov): the AMOC "is **very likely to weaken** over the 21st century for all emissions scenarios"; **high confidence** in the decline, **low confidence** in its size; **medium confidence that there will not be an abrupt collapse before 2100**. If it did collapse: "a **southward shift in the tropical rain belt**, weakening of the African and Asian monsoons and strengthening of Southern Hemisphere monsoons, and drying in Europe": *the Asian monsoon is us* ([[CL15 Monsoons]]). Joy's note: several recent papers argue tipping could come earlier; none has been read for the course, so **they are not cited** here either. Next week (O7, the last lecture of the module, not yet on the site): *the ocean remembers, and the ocean is changing*.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Can the Atlantic overturning switch off? The Stommel two-box model
> A warm salty box and a cold fresher box.
>
> ![[cl_stommel_box.png|720]]
>
> **Try:** Start at F = 0 (q = 0.62, on). Slide F slowly up to 0.12: q falls but stays on. Go to 0.15: it drops to the reversed branch (q < 0). Slide F back down to 0.05, then 0.0: it stays off. Only at F slightly below 0 does it switch back on. Press 'ramp up and down' to watch the whole loop.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_stommel_box.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_stommel_box.html) · all tools and coverage: [[Interactive Tools]]

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
> [!connection] How CL26 connects
> **Builds on:** [[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]] (density, water masses, the Atlantic–Pacific salt difference), [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] (the pumping that pulls the deep water up), [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] (the 140-year ruler and ocean heat uptake), [[CL04 Feedback and Multiple Steady States]] (positive feedback, multiple equilibria), [[CL21 Thermohaline Circulation Water Masses and Sea Ice]] (Neena's version), [[CL17 Orbital Forcing and Glacial Cycles]] (abrupt climate change in the last ice age).
> **Leads to:** CL27–CL28 (tutorials, planned); O7 when it is on the site.
> **Concepts:** [[Thermohaline Circulation]] · [[Deep Water Formation]] · [[Water Mass and T-S Diagram]] · [[Antarctic Circumpolar Current]] · [[Ice-Albedo Feedback]] · [[Stommel Two-Box Model]] · [[Atlantic Meridional Overturning Circulation]] · [[Hysteresis]] · [[Sverdrup (Unit)]]

## Summary
> [!summary] Cheat-sheet
> - Deep water forms only in the **North Atlantic** (15–20 Sv; Nordic and Labrador Seas, cooling of salty water) and **around Antarctica** (≈ 10 Sv; Weddell, Ross; brine). Gulf Stream 30 Sv, ACC 125 ± 11 Sv.
> - **North Pacific**: surface 2.3 g/kg fresher (32.8 vs 35.1); cooled to −1.8 °C σ = 26.4 < 27.7 below (needs S ≈ 34.4); the Atlantic exports fresh water to it.
> - **Return**: isopycnals (σ 27.2–27.8) rise to the surface south of 45°S; westerlies ⇒ Ekman transport north ⇒ pulled up ≈ 25 m yr⁻¹; the Southern Ocean forms bottom water and brings deep water up.
> - **~1,000 yr** turnover ⇒ ≈ 1 mm s⁻¹ (31,600 km); oldest water mid-depth North Pacific; Southern Ocean warms slowly.
> - **RAPID** (2004–, 26.5°N): mean 17.0 Sv, 10-day −4…32, yearly 14.9–19.1; 20 yr ≪ 1,000 yr.
> - **Stommel box**: $F=q(1-q-q^2)/(1+q)$, $F_{\max}=0.141$ at $q=0.30$; reversed state exists for all $F>0$; collapse at $F_{\max}$, recovery only at $F<0$: **hysteresis**. IPCC AR6: very likely to weaken, medium confidence no abrupt collapse before 2100.

## Practice
1. **Mass.** 17 Sv of deep water forms in the North Atlantic. Convert to kg s⁻¹, and find how long it would take to fill a deep-ocean volume of 10¹⁸ m³ alone.
2. **1 mm per second.** How far does water travel in 1,000 years at 1 mm s⁻¹? Compare with the route NADW takes to the North Pacific.
3. **The Pacific.** At −1.8 °C, what salinity does North Pacific surface water need to reach σ = 27.7? By how much is it short? (Use figure B or the EOS-80 values.)
4. **Southern Ocean.** Westerlies blow east over 50–60°S. In which direction is the Ekman transport, and why does water rise poleward of the wind maximum and sink equatorward of it?
5. **Stommel.** At F = 0.10 give the number of steady states, their stability and q; then at F = 0.20. What happens if F is raised from 0.10 to 0.20 and back to 0.10?
6. **Hysteresis path.** Starting "on" at F = 0, list the order of events as F rises to 0.25 and then falls to −0.05; at what F does the circulation switch each way?
7. **Detection.** RAPID has measured 20 years of a system with a 1,000-year memory. Why can it not show a trend yet, and what can it show?
8. **IPCC.** State the IPCC AR6 statement on the AMOC in your own words, including the confidence levels, and name one consequence of a collapse.

> [!example]- Solutions
> 1. 17×10⁶ m³ s⁻¹ × 1,025 kg m⁻³ = **1.7×10¹⁰ kg s⁻¹** (Hartmann's 1.5–2×10¹⁰). 10¹⁸/(17×10⁶) = 5.9×10¹⁰ s = **1,860 yr** (so both sources, ≈ 27.5 Sv, give ≈ 1,150 yr for 10¹⁸ m³).
> 2. 1,000 × 3.156×10⁷ × 10⁻³ = 3.16×10⁷ m = **31,600 km**: roughly the length of the route, North Atlantic to the ACC to the North Pacific.
> 3. ≈ **34.4** at −1.8 °C (🔵 34.41); the North Pacific surface is 32.8, so ≈ **1.6 g/kg short**.
> 4. Southern hemisphere: transport to the **left** of the wind, i.e. **north**. Poleward of the westerly maximum the transport diverges (more water leaves than arrives), so water rises (the Southern Ocean belt is pulled up ≈ 25 m yr⁻¹); equatorward of the maximum it converges and water is pushed down.
> 5. F = 0.10 < F_max: **three** steady states: q = +0.47 (stable), +0.13 (unstable), −0.10 (stable, reversed). F = 0.20 > F_max: **one** state, reversed, q ≈ −0.17 (🔵: |q|/(1+|q|)+q² = 0.2 ⇒ |q| = 0.17). Raising F from 0.10 to 0.20 on the "on" branch crosses F_max = 0.141, so the flow **collapses** to the reversed state; lowering F back to 0.10 leaves it **reversed** (q ≈ −0.10): hysteresis.
> 6. F rises: flow weakens slowly (q from 0.62 at F = 0 down to 0.30); **at F ≈ 0.14 it collapses** to q ≈ −0.14 and then follows the reversed branch (to q ≈ −0.24 at F = 0.25); as F falls it stays reversed all the way down to F = 0⁺ (q → 0⁻) and **switches back on only as F crosses zero** (F < 0).
> 7. Weather noise gives 10-day swings of tens of Sv and year-to-year changes of 15–19 Sv; a 20-year record is one or two "memory times" of the *fast* components only and a few per cent of the 1,000-year turnover, so a decadal slope of −0.9 Sv is inside the noise. It can show how the overturning works (its components, variability, response to winds) and gives a **baseline**.
> 8. "The AMOC is very likely to weaken over the 21st century in all scenarios (high confidence in the decline, low confidence in how much); medium confidence that it will not collapse abruptly before 2100." A collapse would shift the tropical rain belt south, weaken the African and Asian monsoons, strengthen Southern Hemisphere monsoons and dry Europe.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | sinking sites and rates, North Pacific, Southern Ocean return, 1,000 yr, oldest water, RAPID, Stommel box, hysteresis, the past, IPCC AR6 | O6 deck, 26 frames ([[O6_The-overturning.pdf]]; speaker notes and every Hartmann/Stewart page citation in [[O6_The-overturning_with-notes.pdf]]); no O6 handout exists | taught (2026) |
> | 1,000 years ⇒ 1 mm s⁻¹; RAPID/MOCHA design, 24°N first-year 18.7 ± 5.6 Sv; ACC 125 ± 11 Sv | Stewart 2008 pp. 222, 229 (`transcripts/readings/O5__04…`, read in part) | extra/book (2026) |
> | wind pumping and the 25 m yr⁻¹ number; salt, σ and water masses | [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]], [[CL25 The Ocean's Ledger IV - Salt, Density and Water Masses]] (O4, O5 sources) | taught (2026) |
> | Stommel model, branches, collapse and recovery, Pacific vs Atlantic σ, renewal and 1 mm s⁻¹ arithmetic | `scripts/fig_cl26.py` (+ EOS-80 of `scripts/fig_cl25.py`) | extra-beyond |
>
> **Notes.** The RAPID record, the IPCC wording, the Rahmstorf, Alley and Heinrich results, the Hartmann pp. 222–231 content and Stewart pp. 211–219 are **as Joy's slides give them**; none was read except Stewart pp. 222 and 229. The ocean volume (1.335×10¹⁸ m³) is recalled. The Stommel model is my own simple nondimensionalisation and illustrates the mechanism; its numbers (0.141, 0.30) are properties of that model, not of the ocean. O7 ("the ocean remembers, and the ocean is changing") was not on the site when this was written.
