---
title: CL30 Tutorials III - Three Boxes of Carbon
aliases: [CL30, Three Boxes of Carbon, BEAM, Bolin and Eriksson, Glotter 2014, carbon box model, carbon-boxes exercise, Joy tutorial 4, Revelle factor model]
subject: climate
type: chapter
chapter: 30
part: VI
scope: [taught, extra-beyond]
by: [joy]
status: draft
prereq: ["[[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]]", "[[CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/joy, status/draft]
---
# CL30 · Tutorials III: Three Boxes of Carbon

◀ [[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]] · [[Climate - Course Map|Course Map]] · (last chapter of Part VI)

<span class="scope-taught">taught · in syllabus (2026 Joy, O7 app, handout and exercise; "understanding the model is part of the course, and it may come up in the exam")</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-21)
> Joy's handout *Three Boxes of Carbon: a guide to the app* (11 pp.) and *exercise* (3 pp.), both read in full (`tutorials/carbon-boxes/handout.pdf`, `exercise.pdf` in the site mirror; also `books/joy_lecture_readings/O7_Three-Boxes-of-Carbon_exercise.pdf` from the Dropbox folder). The app's "How it works" text and constants were read from the mirrored page. **Every number below was recomputed** with an independent Python coding of the model (`scripts/cl_carbon_boxes.py`: same equations and constants, the app's emissions series read as data, but a stiff ODE solver instead of the app's RK4): it reproduces the handout's tables to the last digit except where noted. No tutorial session (exercise for self-study).

> [!syllabus] Syllabus map
> 🟢 **Taught**: §1 why the model exists (Bolin–Eriksson 1959, DICE, Glotter et al. 2014); §2 the model: three boxes, the equations, the chemistry ($A$, $B$, Revelle), where it settles and how fast, what it leaves out; §3 testing against the past and the 200-year fix; §4 the seven runs; §5 take-aways.
> 🔵 **Extra · beyond**: §6 the exercise's eight questions, solved with the re-implementation; the analytic catch-up times.

> [!key] After this chapter you can
> - write the three box equations and say what each bracket wears away,
> - explain $A$ (Henry's law), $B$ (carbonate speciation), $1/B\approx170$ and why the ocean holds ~60× the air's carbon,
> - show why the **settled level** contains no exchange rates, and estimate the two **timescales** (months for the upper ocean, ~1000 years for the deep),
> - explain the **1000 → 200 year fix**, what it fits and what it costs,
> - reproduce the runs' headline numbers (480 / 422 ppm; 334 ppm, 22 %; 24 % / 42 % of pulses; 1.6 % without chemistry) and answer the exercise.

## 1. Why this model exists
<span class="scope-taught">taught</span> *handout Part 1*

The question (lecture): of 752 GtC emitted 1750–2024, 41 % is in the air, 28 % in the ocean, 25 % in the land. (1) The ocean holds ~50× the air's carbon: why has it taken only a quarter? (2) If we stopped today, would CO₂ return to 280 ppm, and how fast?

**History** (as Glotter et al. tell it; Joy did not read the originals): **Bolin & Eriksson (1959)** split carbon into air, top of the ocean and deep ocean, using the carbonate chemistry Revelle & Suess pointed to in 1957, but held the coefficients fixed: a **linear** model. Fifty years later economists priced the damage from CO₂ with linear models of the same form, notably **DICE** (Nordhaus). **Glotter, Pierrehumbert, Moyer et al. (2014)** showed that DICE-2007, run with high emissions falling to zero after 300 years, pulled nearly all the CO₂ out within a few hundred years, where fuller models keep about half for millennia: an error of ~1000 ppm and ~6 °C on millennial timescales. The cause is the chemistry: a more acidic ocean holds less carbon, so the ocean's **appetite falls as it eats**; a linear model tuned to today's rate keeps eating forever. Their fix, keeping the three boxes but letting the chemistry change, is **BEAM** (Bolin and Eriksson Adjusted Model); over 2000 years it tracks two much larger models.

## 2. The model
<span class="scope-taught">taught</span> *handout Part 2; app "How it works"*

### 2.1 Three boxes
| box | before we started |
|---|---|
| air, $M_{AT}$ | 595 GtC (280 ppm; **1 ppm = 2.124 GtC**) |
| upper ocean, $M_{UP}$ | top 1/51 of the volume (~75 m, the stirred layer): 714 GtC |
| deep ocean, $M_{LO}$ | the other 50/51: 35 680 GtC |

$$\frac{dM_{AT}}{dt}=E(t)-k_a\big(M_{AT}-AB\,M_{UP}\big),\qquad
\frac{dM_{UP}}{dt}=k_a\big(M_{AT}-AB\,M_{UP}\big)-k_d\Big(M_{UP}-\frac{M_{LO}}{\delta}\Big),\qquad
\frac{dM_{LO}}{dt}=k_d\Big(M_{UP}-\frac{M_{LO}}{\delta}\Big).$$
Each bracket is a **difference** between neighbouring boxes and each exchange **wears it away** (like the heat and salt exchanges of Stommel's boxes, [[Stommel Two-Box Model]]). $M_{UP}-M_{LO}/\delta=0$ when both parts of the ocean hold the same carbon per litre ($\delta=50$); the **deep turnover** is $\delta/k_d=1000$ yr with the paper's $k_d=0.05$ yr⁻¹ (Hartmann's value, met in O6). $M_{AT}-AB\,M_{UP}=0$ when air and upper ocean are in balance; $1/k_a=5$ yr.

### 2.2 The chemistry
$AB$ is the air's carbon, in balance, per GtC in the upper ocean. **$A$ is Henry's law** (dissolved CO₂ ∝ CO₂ above). **$B$ is the catch**: only a small part of seawater carbon is dissolved CO₂; the rest is ions,
$$\frac1B=1+\frac{k_1}{[\mathrm H^+]}+\frac{k_1k_2}{[\mathrm H^+]^2}\quad(\text{all carbon per unit dissolved CO}_2).$$
Pre-industrial $1/B\approx170$ (re-implementation: 170.8): for each CO₂ molecule dissolved as gas the upper ocean holds ~170 carbon atoms as ions, so the whole system holds ~**60×** the air's carbon (62.2). Adding CO₂ releases H⁺, pushes the reactions left, and **$1/B$ falls**: the **Revelle (buffer) factor**, the one thing that separates BEAM from DICE. The app finds $[\mathrm H^+]$ from the upper-ocean carbon at fixed **alkalinity** (767 GtC ≈ 2317 μmol kg⁻¹) and reports the surface pH (8.29 at the start).

### 2.3 Where the carbon settles, and two timescales
**Where.** Wait long enough and every bracket vanishes; neither $k_a$ nor $k_d$ appears in those two conditions, so **the settled level depends only on the chemistry and the size of the ocean**, not on how fast it gets there. (The app draws it as a blue dashed line.)

**How fast.**
- The **upper ocean catches up with the air within months**, although $1/k_a=5$ years: it is small and buffered, so it needs to take only ~1 part in 14 of an addition to rebalance. (Pre-industrially, $d(AB\,M_{UP})/dM_{UP}\approx13$: ~13 GtC more in the air per extra GtC held in the top; re-implementation 12.9.) Its catch-up time is $1/(k_a\times14)\approx$ **4 months** (4.3).
- The **deep ocean is the bottleneck**: the top passes carbon down with time constant $1/k_d\approx20$ yr, but the deep box is 50× bigger, so filling it takes the full turnover $\delta/k_d\approx$ **1000 years**.

### 2.4 What it leaves out
**Land** (21 % of emissions in 2015–2024); the **sea floor and rocks** (CaCO₃ dissolution over 3000–7000 years, weathering over 10⁵ years, Archer et al. 2009): so its settled level is "where the ocean alone would leave us", not the end; **warming** (a warmer ocean holds less CO₂; Glotter et al. include it and find it changes little for centuries); **biology and currents** except as the two exchange times.

### 2.5 The app
Presets along the top; **What goes in** (*Our emissions*: the carbon that went into air or sea each year 1750–2024, then today's 8.8 GtC yr⁻¹ until *Emissions stop in*; *One pulse* into a pre-industrial world); **Ocean** (chemistry on/off, the two exchange times); **Show** (time span, *Keep this run*); four charts: CO₂ with Mauna Loa dots, where the added carbon is, ocean uptake with the GCB dots, surface pH.

## 3. Testing the model against the past
<span class="scope-taught">taught</span> *handout Part 3*

- **Only the carbon that reached air or sea goes in**: emissions minus the land's uptake, from the GCB (measured air growth + estimated ocean uptake): **522 GtC**, 1750–2024. A fair test of the ocean, but not independent of the measurements: a match with Mauna Loa means the model **splits** the carbon between air and ocean the way the world did — exactly the question.
- **Small fixes**: the paper's Table 4 upper ocean (713 GtC) balances 277 ppm with its rounded constants; the app keeps 280 ppm and balances the top with it (714 GtC, pH 8.29; <1 %). Adaptive time steps (the paper used 0.01 yr and warned its scheme can't take a pulse); checked against a second Python coding.
- **The real problem: the paper's ocean is too slow** (preset *Our emissions, then stop*):

| | model, 1000-yr turnover | measured |
|---|---|---|
| CO₂ in 2024 | **480 ppm** | 425 ppm (Mauna Loa) |
| first reaches 380 ppm | 1989 (re-impl. 1988) | 2006 |
| ocean uptake 2015–2024 | 1.3 GtC/yr | 3.2 GtC/yr (GCB) |

(The paper's own run reaches 380 ppm "near year 1994".) **The fix**: turnover 1000 → **200 years** ($k_d$ 0.05 → 0.25 yr⁻¹; preset *Faster deep exchange*): **313, 359, 422 ppm** in 1959, 1994, 2024 (measured 316, 359, 425), 380 ppm in 2006, uptake 3.3 GtC/yr.
- **Why the fix is not the end**: one deep box stands for the decades-fast thermocline and the millennium-slow abyss ([[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]] §12). After emissions stop, the 200-year ocean draws CO₂ **halfway to its settled level by 2066** and nine-tenths by **2156** (re-impl. 2157); with 1000 years, **2229** and **2667** (2666). Larger models: 2–20 centuries, so for the long tail the slower ocean is closer to right.
- **What the fix doesn't change**: the settled **334 ppm**, **22 %** of the 522 GtC in the air. Compared with Archer et al.'s ocean-only models (~20 % of a 1000 GtC pulse and ~35 % of 5000 GtC stay), BEAM keeps 24 % and 42 %: same pattern, a little more; "we haven't pinned down why".

## 4. Seven runs
<span class="scope-taught">taught</span> *handout Part 4; all values re-computed*

> [!example]- Run 1 · the paper's ocean (turnover 1000 yr)
> CO₂ pulls away from the dots after ~1960 and reaches **480 ppm** in 2024; uptake ~1.3 GtC/yr; in 2024 **82 %** of the added carbon is in the air, 4 % in the upper ocean, 13 % in the deep. *Why*: the top keeps up within months but is small and nearly full; the rest must go to a deep ocean that turns over in 1000 years.

> [!example]- Run 2 · faster deep exchange, and the turnover scan
> 200 yr runs through the Mauna Loa dots; the surface pH in 2024 is **8.14** (8.08 with 1000 yr: a faster ocean passes carbon down, so the surface acidifies less). The settled line doesn't move.
>
> | deep turnover (yr) | 1000 | 500 | 300 | 200 | 100 |
> |---|---|---|---|---|---|
> | CO₂ 2024 (425 measured) | 480 | 458 | 439 | 422 | 396 |
> | uptake 2015–24, GtC/yr (3.2 measured) | 1.3 | 2.0 | 2.7 | 3.3 | 4.4 |
> | settles at (ppm) | 334 | 334 | 334 | 334 | 334 |
>
> *Which turnover fits CO₂ best? ~200 (422 vs 425). Uptake? ~200–250 (3.3 vs 3.2). They roughly agree* (they are linked: what the ocean doesn't take stays in the air).

> [!example]- Run 3 · air–sea exchange time instead
> 1 → 20 years: CO₂ 2024 **420 → 431 ppm**, uptake **3.4 → 3.1** GtC/yr: hardly any change. The surface is not the bottleneck; "to speed up a chain of steps, find the slowest one".

> [!example]- Run 4 · stop later (turnover 200)
> | stop in | 2025 | 2050 | 2075 | 2100 | 2150 |
> |---|---|---|---|---|---|
> | added (GtC) | 522 | 742 | 961 | 1181 | 1621 |
> | peak (ppm) | 424 | 482 (re-impl. 481) | 533 | 580 | 672 |
> | pH at stop | 8.14 | 8.09 | 8.05 | 8.01 | 7.95 |
> | settles (ppm) | 334 | 360 | 388 | 418 | 486 |
> | share left in air | 22 % | 23 % | 24 % | 25 % | 27 % |
>
> The settled level depends only on the **total** added, but the steps grow (26, 28, 30 ppm per 25 years) and the share rises: the buffer weakening.

> [!example]- Run 5 · pulses (turnover 1000)
> | pulse | in air after 10 yr | 100 yr | 1000 yr | once settled |
> |---|---|---|---|---|
> | 100 GtC | 91 % | 68 % | 21 % | 20 % |
> | 1000 GtC | 94 % | 80 % | 28 % | 24 % |
> | 5000 GtC | 98 % | 91 % | 54 % (re-impl. 55 %) | 42 % |
>
> A bigger pulse acidifies more (surface pH **7.4** after 5000 GtC vs **7.9** after 1000), so the ocean holds a smaller share, for longer. On a log time axis the uptake shows **two stages**: a plateau for decades while the top keeps up, then a fall over centuries as the deep ocean catches up. Joos et al. (2013), many larger models with land, 100 GtC into today's air: **25 ± 9 %** left after 1000 years; BEAM 21 %.

> [!example]- Run 6 · no buffer (the linear model)
> 1000 GtC pulse with the chemistry off: only **2 %** stays (re-impl. 1.6 %), and it leaves within decades (41 % after 10 yr, 5 % after 100). **Pencil check**: with $AB$ fixed at 0.83 and the deep box holding $\delta=50$ GtC per GtC in the top, the air's settled share is $\dfrac{AB}{AB+1+\delta}=\dfrac{0.83}{51.83}=1.6\%$. *Why can't you do the same sum with the chemistry on?* Because $AB$ then depends on $M_{UP}$, which depends on how much was added: the share must be found by solving a nonlinear equation (the app's `settle` does it by bisection).

> [!example]- Run 7 · on paper: a better deep ocean
> 1. Four boxes: air ↔ upper ocean ↔ **thermocline** ↔ **abyss** (and possibly upper ↔ abyss directly at the deep-water formation sites: the North Atlantic and Antarctic shortcut).
> 2. $\dot M_{TC}=k_1(M_{UP}-M_{TC}/\delta_1)-k_2(M_{TC}/\delta_1-M_{AB}/\delta_2)$, $\dot M_{AB}=k_2(\dots)$, with the upper-ocean equation losing $k_1(\dots)$ instead of $k_d(\dots)$. **New numbers**: the volume split ($\delta_1$, $\delta_2$ with $\delta_1+\delta_2=50$) and two exchange rates — three in all.
> 3. Mauna Loa alone cannot pin three numbers (Run 2: several turnovers fit something reasonably); add the GCB ocean uptake, ocean interior tracers (CFCs, bomb ¹⁴C, anthropogenic carbon inventories by depth) that measure how deep and how fast surface water penetrates.
> 4. **No**: the settled level depends only on the chemistry and the total ocean volume, not on how the deep ocean is divided or how fast it exchanges.

## 5. What to take away
<span class="scope-taught">taught</span> *handout Part 5*

1. The ocean takes our carbon slowly because **the deep ocean is replaced slowly**; the top keeps up within months but is small.
2. **The chemistry makes the ocean less willing the more it takes**: about a fifth stays in the air once the ocean has caught up; bigger additions leave bigger shares; a linear model gets the long run badly wrong.
3. **Where** carbon settles depends on chemistry and ocean size; **how fast**, on the exchange times.
4. **Measure, test, revise, and know what your fix costs.**
5. **The ocean's memory works both ways**: centuries to catch up with what we do, and it gives it back as slowly.

## 6. The exercise, solved
<span class="scope-extra-beyond">extra · beyond</span> *[[O7_Three-Boxes-of-Carbon_exercise.pdf|exercise]] questions; answers mine, numbers from `scripts/cl_carbon_boxes.py`*

> [!example]- Q1 · the books in 2024 (turnover 200)
> (a) In 2024: **≈ 59 % air, 3 % upper ocean, 38 % deep ocean**. (b) GCB: air 0.41 × 752 = 308 GtC, ocean 0.28 × 752 = 211 GtC; the air's share of (air + ocean) = **59 %** — the same as the model. (c) The input *is* the measured air growth plus ocean uptake, so total carbon is fixed by the data; the agreement tests only **how the model splits** it between air and ocean. The 1000-year run fails the test (82 % in the air).

> [!example]- Q2 · a pencil check on where it settles
> (a) 334 − 280 = 54 ppm × 2.124 = **115 GtC** above pre-industrial. (b) 115 / 522 = **22 %** ✓. (c) The rest (~407 GtC) is in the ocean, overwhelmingly the **deep** ocean: at equilibrium the deep box holds $\delta=50$ times the upper box's carbon per unit volume-share, so ~98 % of the ocean's extra carbon sits in the deep box.

> [!example]- Q3 · find the bottleneck
> | air–sea time | deep turnover | peak CO₂ |
> |---|---|---|
> | 5 yr | 200 yr | 424 ppm |
> | 10 yr | 200 yr | 427 ppm |
> | 5 yr | 400 yr | 452 ppm |
>
> (a, b) Doubling the **deep turnover** raises the peak ~10× more: the deep ocean (50/51 of the volume) is where the carbon must go; the small upper box is in near-balance with the air within months either way. (c) All three settle at **334 ppm**: the settled level contains no exchange rates.

> [!example]- Q4 · same carbon, different path
> (a) Stop in 2050: **742 GtC** added, peak **482 ppm** (re-impl. 481), settles **360 ppm**. (b) Pulses: 700 GtC settles at **355 ppm**, 800 GtC at **367 ppm**. (c) Yes, 360 lies between: the settled level depends only on the **total** added, not the path. (d) The pulses' peaks are far higher (**610 and 657 ppm**, the whole amount at once) than the gradual run's 482, because the gradual run lets the ocean take carbon while it is being added. For people living through it, the peak sets the warming they experience and the rate of change they must adapt to.

> [!example]- Q5 · how sure are we about 2100? (stop 2050)
> | turnover | CO₂ 2100 | CO₂ 3000 | settles |
> |---|---|---|---|
> | 200 yr | 415 ppm | 360 ppm | 360 ppm |
> | 1000 yr | 539 ppm | 369 ppm | 360 ppm |
>
> (a) The 200-year run fits the past. (b) They disagree most around **2100** (124 ppm), because that is when the drawdown rate matters; by 3000 both have nearly reached the same settled level, which doesn't depend on the turnover. (c) **Higher** than 415: the 200-year ocean is too fast for the long tail, so after 2050 the real CO₂ should fall more slowly, somewhere between the two runs.

> [!example]- Q6 · how much more acidic?
> pH when emissions stop: 2025 **8.14**, 2075 **8.05**, 2150 **7.95**. (a) For 7.95: $10^{8.29-7.95}=$ **2.2×** the pre-industrial H⁺ (1.4× for 2025, 1.7× for 2075). (b) More H⁺ pushes $\mathrm{CO_2+H_2O\rightleftharpoons HCO_3^-+H^+\rightleftharpoons CO_3^{2-}+2H^+}$ to the left, so $1/B$ (carbon held per unit dissolved CO₂) falls; each extra tonne raises the surface's dissolved CO₂ more, so the air–sea difference closes after taking a smaller share.

> [!example]- Q7 · what the linear model misses (turnover 1000, to 10 000 yr)
> | pulse | chemistry on | chemistry off |
> |---|---|---|
> | 1000 GtC | 24 % | 1.6 % |
> | 5000 GtC | 42 % | 1.6 % |
>
> (a) Off: **independent** of the pulse (linear: $AB/(AB+1+\delta)$). On: grows with the pulse. (b) A "chemistry-off" model **underestimates** how much CO₂ stays (and for how long), so it underestimates long-run warming and damage; the error grows with cumulative emissions because acidification, which it ignores, grows with them (Glotter et al.: ~1000 ppm, ~6 °C on millennial scales for high emissions).

> [!example]- Q8 · in your own words (≈150 words)
> No. If we stopped all emissions tomorrow, CO₂ (about 425 ppm now) would fall, quickly at first, as the ocean keeps absorbing it — but not to 280 ppm. The ocean's surface layer keeps up with the air within months, but most of the carbon has to go into the deep ocean, whose water is replaced only about every thousand years, so the decline takes centuries: in a simple three-box model CO₂ gets halfway to its final level by the 2060s but needs until well after 2150 for most of the rest. And it settles around **334 ppm**: about **22 %** of the carbon we added stays in the air, because seawater becomes more acidic as it absorbs CO₂ and less able to take more. The model leaves out the land and the sea floor: over 3000–7000 years, dissolving carbonate sediments would draw CO₂ down further, and over hundreds of thousands of years the weathering of rocks would remove the rest.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Three boxes of carbon: air, upper ocean, deep ocean (BEAM)
> The Bolin–Eriksson three-box carbon model with Glotter et al.'s (2014) carbonate chemistry, as in Joy's O7 app: the air exchanges with the upper ocean (time 1/k_a) and the upper ocean with a deep ocean 50 times its volume (turnover δ/k_d).
>
> ![[cl_three_boxes.png|720]]
>
> **Try:** History, stop 2025: turnover 1000 yr reaches 480 ppm in 2024 (Mauna Loa 425); set 200 yr: 422 ppm, on the dots, and the settled level stays 334 ppm. Pulse 1000 vs 5000 GtC: 24 % vs 42 % stays in the air once settled; untick the chemistry: 1.6 % for both (measured while building, matching the handout).
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_three_boxes.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_three_boxes.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL30 connects
> **Builds on:** [[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]] (§7–§12), [[CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch]] (the 1000-year turnover; box models), [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] (relaxation times). Sister tutorials: [[CL27 Tutorials I - Daisyworld with Land and Ocean]], [[CL28 Tutorials II - Earth's Energy Budget from Space (CERES)]].
> **Concepts:** [[Three-Box Carbon Model]] · [[Revelle Factor]] · [[Ocean Carbon Sink and Airborne Fraction]] · [[Carbon Commitment]] · [[Stommel Two-Box Model]] · [[Carbon Cycle]]
> **Other subjects:** [[Inorganic Chemistry - Course Map]] (acid–base equilibria, $k_1,k_2$ of carbonic acid) · [[EE02 Structured Population Models]] (compartment models, slowest-eigenvalue bottlenecks)

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | Parts 1–5, all runs and tables | Joy, *Three Boxes of Carbon: a guide to the app* (handout, 11 pp., read in full) | taught |
> | the eight questions | Joy, *Three Boxes of Carbon: exercise* (3 pp., read in full) | taught (exercise) |
> | constants, alkalinity, the settle routine, emissions series | the app page's "How it works" text and data (read as text, not run) | taught |
> | every number re-computed; exercise answers; Run 7 sketch | `scripts/cl_carbon_boxes.py` (independent coding: LSODA instead of RK4) | extra/beyond |
>
> **Agreement.** Matches the handout everywhere to the printed precision except: first 380 ppm 1988 vs 1989 (annual-mean rounding), 2050 peak 481 vs 482, nine-tenths year 2157 vs 2156 and 2666 vs 2667, 5000 GtC at 1000 yr 55 % vs 54 %, no-buffer share 1.6 % (handout rounds to 2 %). Glotter et al. (2014), Archer et al. (2009) and Joos et al. (2013) are cited as the handout cites them (the Glotter extract and Archer preprint are in `O7_readings/`, not read here).
