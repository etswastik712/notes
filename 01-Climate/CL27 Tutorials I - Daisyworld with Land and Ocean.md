---
title: CL27 Tutorials I - Daisyworld with Land and Ocean
aliases: [CL27, Daisyworld land and ocean, Daisyworld with an Ocean, Daisyworld tutorial, causal loop diagram, boom-bust cycle, balancing loop, delay, Joy tutorial 1, Joy tutorial 2]
subject: climate
type: chapter
chapter: 27
part: VI
scope: [taught, extra-beyond]
by: [joy]
status: draft
prereq: ["[[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]]", "[[CL04 Feedback and Multiple Steady States]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/joy, status/draft]
---
# CL27 · Tutorials I: Daisyworld with Land and Ocean

◀ [[CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch]] · [[Climate - Course Map|Course Map]] · ▶ CL28 (planned: the CERES tutorial worked)

<span class="scope-taught">taught · in syllabus (2026 Joy, tutorials "Daisyworld, land and ocean" and "Daisyworld with an Ocean")</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> Joy's two tutorial apps and their three handouts (`earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/tutorials/` and `transcripts/tut_pdf/`; the apps are interactive web pages I did **not** run). The handouts state the models completely ("The model in full" and the app's "How it works" page), so I **re-implemented both models and reproduced the runs**: `scripts/daisy_land_ocean.py` (tutorial 1), `scripts/daisy_ocean.py`, `scripts/daisy_ocean_runs.py`, `scripts/daisy_ocean_busts.py` (tutorial 2, Parts 1 and 2). This chapter is the **worked solution**: for each run, what to set, the handout's number, my number, and the explanation. Where I could **not** reproduce a number I say so (§6). The slab-and-weather theory behind tutorial 2 is [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §5–7; Daisyworld itself first appears in [[CL04 Feedback and Multiple Steady States]] (Argha's part).

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 **Daisyworld with land and ocean**: leverage, dark ocean, surviving versus regulating, hysteresis, sudden change, heat store, fast versus slow forcing (ten runs); §2 **Daisyworld with an Ocean, Part 1**: land, mixed layer, deep ocean, weather, timescale bars, spectrum, depth, brightening (six runs); §3 **Part 2, adding life**: daisies, grazers, the **causal loop diagram**, balancing loops with a delay make a **cycle**, busts, the ocean sets the beat (six runs)
>
> 🔵 **Extra · beyond** (my own)
> - the numerical reproduction of every run, with the handout's numbers set against mine; which numbers do not reproduce

> [!key] After this chapter you can
> - write the Daisyworld energy balance, albedo and patch-temperature equations and the app's heat-store formula $C=fC_\text{land}+(1-f)\rho c h$,
> - explain **leverage** (daisies' dial is $0.5f$ wide), **dark-ocean shift**, why **surviving is not regulating**, and the hysteresis loop,
> - explain **spike-then-correction** (fast physics + slow biology), $\tau=C/\lambda$, and why heat capacity changes the **path** not the **destination**,
> - draw and read the **causal loop diagram** (count the minus signs), and explain why a **delay turns a balancing loop into a cycle** and why the ocean "sets the beat",
> - state what the models leave out.

> [!intuition] The one-sentence story
> The ocean does two things to a planet: it makes it **darker** and **slower**. Daisies can only recolour land, so more ocean means less control; heat capacity changes how long the planet takes to respond but not where it ends up; and a slow ocean in a loop of balancing feedbacks makes the whole system overshoot into a boom–bust cycle with nothing outside cycling.

![[fig_cl27_daisyworld.png]]
*My simulations of Joy's models. A: tutorial 1, slow brightening (L 0.4 → 1.8 over 600 years), daisy planet (solid) against its bare twin (dashed) for all land, 30 % and 70 % ocean; the band is the daisies' 22.5 ± 5 °C comfort zone. B: tutorial 1, sudden change L 0.78 → 0.86, daisy planet (solid) and bare planet (dashed) as a change from before, log time axis. C: tutorial 2, Part 2 ("grazers, no weather"): grazers (log) and land and mixed-layer temperature over 40 years: an 8-year cycle with no outside forcing. Scripts: `scripts/fig_cl27.py`, `daisy_land_ocean.py`, `daisy_ocean.py`.*

## 1. Tutorial 1: Daisyworld with land and ocean
<span class="scope-taught">taught</span> *handout `daisyworld_land_ocean_handout.pdf` (19 pp, read in full); app "How the model works"*

**The model** (one temperature for the whole planet; no places, no seasons): sunlight $S=917$ W m⁻² at $L=1$; albedos white daisies 0.75, bare ground 0.50, black daisies 0.25, ocean 0.10 (adjustable).
$$A=f\,(a_wA_w+a_bA_b+xA_g)+(1-f)A_o,\quad C\frac{dT}{dt}=SL(1-A)-\sigma T^4,\quad C=fC_\text{land}+(1-f)\rho c\,h,$$
patches $T_w=T+q'(A-A_w)$, $T_b=T+q'(A-A_b)$ with $q'=20$ K, growth $\beta(T)=1-0.003265(22.5-T)^2$ (zero outside 5–40 °C), $da_i/dt=a_i[x\beta(T_i)-\gamma]$ with $x=1-a_w-a_b$, $\gamma=0.3$ yr⁻¹, a 1 % seed floor; $C_\text{land}=10^7$ J m⁻² K⁻¹ (land plus air, ≈ 2.5 m of water), $\rho c=4.1\times10^6$ J m⁻³ K⁻¹, $h=50$ m (so 50 m of ocean stores ≈ 20× land per m²). The bare twin has the same land, ocean and sun with no daisies.

**The ten runs** (handout number | 🔵 my model):

| Run | What to set | Handout | 🔵 Reproduced |
|---|---|---|---|
| 1. all land, slow brightening | classic Daisyworld | planet within 5 °C of 22.5 for **L = 0.76–1.52**; bare planet 0.88–1.01; at L = 1.47 white = 69 % of land, planet 24.3 °C, bare 56.8; 23.4 → 20.9 °C (daisies) vs 22.9 → 48.8 (bare) between L = 0.95 and 1.33 | **0.759–1.520**; bare **0.883–1.010**; 69 %, 24.5, 57.0; 23.4 → 20.9 vs 22.9 → 48.9 |
| 2. add ocean 30 % / 70 % | windows | within 5 °C: 0.64–1.01 / 0.55–0.61; bare 0.71–0.82 / 0.57–0.65; daisies survive 0.63–1.15 / 0.52–0.89 | 0.644–1.009 / 0.546–0.610; bare 0.713–0.816 / 0.568–0.649; survive 0.60–1.16 / 0.50–0.90 |
| 3. bright ocean A_o = 0.5 | separates dark from small | window 0.77–1.32 (30 %), 0.80–1.13 (70 %): starts at ≈ 0.75 every time | 0.766–1.324; 0.803–1.127 |
| 4. surviving ≠ regulating | 70 % ocean, cursor at L = 0.85 | planet 44.8 °C (> 40 limit) yet white = 47 % of land | ≈ 45 °C, ≈ 50 % (cursor position differs slightly) |
| 5. brighten then dim | 300 yr up, 300 down | daisies die at **1.63 / 1.18 / 0.91**, return at **1.17 / 0.97 / 0.80** (0 / 30 / 70 % ocean) | die 1.65 / 1.20 / 0.93; return (cover > 5 %) **1.18 / 0.97 / 0.80** |
| 6. sudden change, all land | L 0.78 → 0.86 | before: black 59 %, daisy planet 25.0 °C, bare 8.7; bare +7.0 K in **22 days**; daisy planet jumps +7 then settles after ≈ 18 yr at **−1.4 K** | 59 %, 25.0, 8.7; +7.0 K in 24 d; peak +7.0 at 0.21 yr; end **−1.4** |
| 7. 30 % ocean, 50 m | store 6.8× | bare +7.3 K in **127 d**; daisy peak +6.5 K after ≈ 1 yr, end −1.3 | +7.3 in 139 d; +6.5 at 1.07 yr; −1.3 |
| 8. deeper ocean | 200 m / 500 m | peak +5.6 K at ≈ 2.7 yr / +4.7 K at ≈ 5 yr; end −1.3 / −1.4 | +5.6 at 2.69 yr / +4.7 at 4.84 yr; −1.3 / −1.4 |
| 9. 70 % ocean, sudden | slow feedback takes over | before: daisy 36.7 °C (white 67 %), bare 41.8; bare +7.8 K in ≈ 8 months; daisy planet **+12.9 K → 49.6 °C = the bare planet** (200 m: +12.8); gentle 0.58 → 0.62: **+4.8 vs +4.9** | 36.7 (67 %), 41.8; +7.8 K in 250 d (8.2 mo); **+12.9** (200 m: +12.8); **+4.8 vs +4.9** |
| 10. too fast to follow | brighten and dim over 30 yr (15 + 15) | bare lag up to 1.3 / 6.2 / 21 K (all land / 30 % 50 m / 30 % 300 m); daisies alive on the way up 0.95–1.44 / 0.86–1.16 / 1.02–1.28 | lag on the up-leg **1.3 / 6.2 / 21.3**; alive (cover > 5 %) **0.95–1.44 / 0.86–1.15 / 1.03–1.28**; on the way down they persist to L ≈ 0.4–0.5 |

**Why it happens.**
- **Leverage** (Runs 2–4). On land the daisies move the albedo anywhere between 0.25 and 0.75, a swing of 0.5; on the whole planet that swing is $0.5f$: **0.5 with all land, 0.35 with 30 % ocean, 0.15 with 70 %**. The ocean's share is fixed and dark, so more ocean gives the daisies a smaller dial *and* sets the planet warmer to begin with. A bright ocean (Run 3) removes the shift (the window always starts near L = 0.75) but not the narrowing: going from all land to 70 % ocean, the top of the range in which daisies *survive* still falls from 1.59 to 1.30, and the top of the *comfortable* window from 1.52 to 1.13 (handout table, Run 3). The shift came from the ocean's darkness, the narrowing from the smaller dial alone: the two effects are separate.
- **Surviving is not regulating** (Run 4). $T_w=T+20(A-0.75)$: on a dark ocean planet ($A\approx0.25$) white patches sit 10 °C below the planet, a cool niche in which white daisies keep growing; but land is 30 % of the planet and white covers under half of it, so they cannot cool the rest.
- **Hysteresis** (Run 5). A planet without daisies is darker than one with white daisies, so hotter; the sun must dim a long way before white patches are cool enough for seeds to take. Less land ⇒ smaller loop (width 0.45, 0.21, 0.11).
- **Spike and correction** (Runs 6–8). The energy budget with storage $C\,dT/dt=SL(1-A)-\sigma T^4$: at the jump the planet absorbs 46 W m⁻² more at once, the surplus fills the store until the planet is warm enough to emit it away. Response time **$\tau=C/\lambda$ with $\lambda=4\sigma T^3\approx5.4$ W m⁻² K⁻¹** (no greenhouse in this model, so λ is larger than Argha's 3.8 and τ shorter: 50 m of water gives ≈ 1.2 yr here against 1.7 yr in lecture). 🔵 Heat-store table: all land 1.0× (**21 days**), 30 %/10 m 1.9× (41 d), 30 %/50 m 6.9× (**148 d**), 30 %/200 m 25× (1.5 yr), 30 %/500 m 62× (3.6 yr), 70 %/50 m 15× (0.86 yr), 70 %/200 m 58× (3.4 yr) (handout: 21 d, 41 d, 146 d, 1.5 yr, 3.6 yr, 0.85 yr, 3.4 yr). The measured two-thirds times are a little shorter than τ (127 against 146 d) because the planet emits more steeply as it warms. **Heat capacity does not change where the planet ends up** (set $dT/dt=0$ and $C$ drops out); it changes only the *path*. Fast physics plus slow biology gives an **overshoot**: the temperature jumps within weeks, the daisies need years, so for the first months the daisy planet behaves like the bare one, then the white daisies spread (8 % → 22 % of the land) and pull it back to 1.4 K *cooler than before*, which is not a bug (Run 1 already cooled slightly mid-range as the sun brightened). A deeper ocean slows the warming and gives the daisies time, so the peak is smaller (Run 8).
- **A slow feedback sets the pace** (Run 9). With 70 % ocean the heat from the sun arrives within a year, but the white daisies die back over 10–20 years as the brighter sun pushes their patches past 40 °C, darkening and warming the planet further, until it *is* the bare planet. In the narrow comfortable window (0.58 → 0.62) the daisies make no difference and all that is left is the ocean's delay (≈ 10 months at 50 m, ≈ 3 years at 200 m).
- **Too fast** (Run 10). With all land the temperature keeps up (lag ≤ 1.3 K) but the daisies do not (they start at L = 0.95, not 0.76: they need years to spread); with a 300 m ocean the temperature itself falls 21 K behind its balance: the transient version of hysteresis.

**Three clocks** (handout): land and air respond in **weeks** (small heat capacity); the ocean mixed layer in **months to years** (each metre of water stores 0.4 × what land and air do, so 50 m stores 20×); the daisies in **years to decades** (growth and death rates). When temperature is much faster than the daisies you get a spike (Run 6); as they get closer the spike shrinks (Run 8); when the daisy clock runs the show the planet responds as slowly as the biology (Run 9).

## 2. Tutorial 2, Part 1: Daisyworld with an Ocean (bare planet)
<span class="scope-taught">taught</span> *handout `daisyworld_ocean_handout.pdf` (12 pp, read in full); app "How it works" (read in full)*

**Model.** Three heat stores with one temperature each: **land** (30 % of the planet, $C_L=10^7$, ≈ 2 months), **mixed layer** (70 %, $C_m=4.2\times10^6\times75\approx3.2\times10^8$, ≈ 30× land, ≈ 5 yr), **deep ocean** (≈ 1,000 m, $C_d=4.2\times10^9$, ≈ 190 yr), with $C\,dT/dt=Q(1-A)-(a+bT)-\ldots+\text{weather}$, $a=203.3$ W m⁻², $b=2.09$ W m⁻² K⁻¹ (so the app's λ is 2.09, not Argha's 3.8: it includes other feedbacks), land–ocean exchange $k=15$, mixed–deep $\gamma_o=0.7$ W m⁻² K⁻¹, $Q=342L$ with $L=1.05$. **Weather**: a random push, the same on land and ocean, spread $\sigma=30$ W m⁻² for a day's mean; with "Day and seasons" it lasts ≈ 3 days (98.6 % hourly retention), sun ±30 % through the year. The theory is [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] §5–7.

| Run | Handout | 🔵 Reproduced |
|---|---|---|
| 1. land only: spread of block means (1 month / 1 yr / 10 yr / 100 yr) | 3.2 / 1.8 / 0.6 / 0.2 K; seasons −5 → 44 °C | 3.17–3.21 / 1.75–1.79 / 0.58–0.61 / 0.16–0.20 K |
| 2. add a mixed layer | 0.74–0.80 / 0.67–0.74 / 0.45–0.54 / 0.14–0.26; seasons ≈ 3 K, warmest in September | 0.74–0.75 / 0.68–0.69 / 0.47–0.49 / 0.15–0.20; slab lag 2.9 months |
| 3. spectrum | mixed layer ≈ 100× below land at months–2 yr, same past 30–50 yr | 1/473 at 1 yr, 1/25 at 6 yr, 0.99 at 300 yr (single slab); bend 2πτ at 30 yr |
| 4. depth (year / decade / century bar) | 25 m 1.08–1.14 / 0.51–0.62 / 0.14–0.28; 75 m 0.67–0.74 / 0.45–0.54 / 0.14–0.26; 150 m 0.48–0.54 / 0.37–0.45 / 0.13–0.24 | 1.10 / 0.56 / 0.18; 0.69 / 0.49 / 0.17; 0.50 / 0.40 / 0.17 |
| 5. add a deep ocean | century bar 0.14–0.26 → 0.12–0.22; slow power −⅓ | 0.17 → 0.15 K; analytic slow power 0.53–0.68 of land |
| 6. brighten the sun 5 % (ΔL = 0.05) | final warming 5.8 K; share after 1 / 10 / 100 / 500 yr: with deep 35 / 80 / 87 / 98 %, without 37 / 95 / 100 / 100 % | **5.79 K**; with deep **26 / 79 / 87 / 98 %**, without **27 / 94 / 100 / 100 %** (1-year share does **not** match) |

**Take-aways** (handout): how much heat a surface can lean on depends on how heat gets below it; the ocean **adds up** weather (fast random pushes become slow wandering); **depth sets the timescale, not the size of the slow swings**; a deep ocean adds a slower stage, calms the slowest swings a little and makes warming arrive in **two stages** (most in ≈ 10 years, the last fifth over centuries); and all this happens **with no water moving sideways**. Left out: currents, geography (one place's day and year; the app's land swings ≈ 1 K between day and night whereas real bare ground, warmed only in its top ≈ 10 cm by a day, swings far more), changing mixed-layer depth, and feedbacks that depend on ocean temperature (El Niño). Joy's discussion questions: whose temperature next month would you forecast, Delhi's or the Arabian Sea's? And what explains the Arabian Sea cooling from ≈ 30 °C in May to ≈ 27 °C in August while the sun is high (answer: [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]] §10: not in this model).

## 3. Tutorial 2, Part 2: adding life
<span class="scope-taught">taught</span> *handout `daisyworld_ocean_life_handout.pdf` (14 pp, read in full)*

**What life adds** (all on the land): white daisies (cooler patches, ≈ 3–4 K below the land), black daisies (warmer patches), both growing best at 22.5 °C; **grazers** that eat both colours but prefer black ($p=0.3$ taste for white), multiply when food is plentiful, eat fastest at land 25 °C (the land usually sits at 19–22 °C, below their best, so warmer land means hungrier grazers). Life touches climate only through the colour of the land; climate touches life only through temperature. The life presets run **without** day and seasons.

**The causal loop diagram** (read: an arrow A → B with + means they move the same way, − the opposite; a loop with an **odd** number of − signs is **balancing (B)**, an **even** number or none **reinforcing (R)**; ‖ marks a delay). **B1**, the white-daisy thermostat: warmer land → white daisies spread (+) → more sunlight reflected, land cools (−): one minus, balancing. **B2**, the black-daisy thermostat: warmer land → black patches too hot, black shrinks (−) → less absorbed → cooler (+): balancing (turned round: cold land favours black). **B3, B4**, food: more daisies → more grazers (+); more grazers → fewer daisies (−): balancing but slow (months). **Appetite**: warmer land → hungrier grazers (+). **Land–ocean**: the land is dragged toward the ocean's temperature, **years late** (‖); not a runaway loop. **Outside drivers** (sun, weather) push but nothing pushes back. *Handout exercise:* the path Land temperature → Grazers → White daisies → Land temperature has **two** minus signs, so it is **reinforcing**: hungrier grazers strip the white daisies, the land darkens and warms, the grazers eat faster still: this is what makes a boom run away until the food is gone.

**Why balancing loops cycle.** With no delay a balancing loop holds the planet steady (Runs 1 and 3); with a long delay it **overshoots**: the shower with a long pipe. The ocean is the long pipe. Grazers strip the land, the planet brightens, but the land cools only as fast as the ocean lets it, and by the time it is cold the daisies have already changed again.

| Run | Handout | 🔵 Reproduced |
|---|---|---|
| 1. daisies, no grazers (B1, B2 only) | white ≈ 42 %, black ≈ 26 %, land ≈ 22 °C; bars vs bare: year 0.24–0.27 vs 0.23–0.25, decade 0.07–0.09 vs 0.15–0.18, century 0.013–0.023 vs 0.05–0.08; sun table (L = 0.95…1.15): bare 12.4 / 18.2 / 23.9 / 29.7 / 35.5 °C, with daisies 19.0 / 24.9 / 22.0 / 21.6 / 27.1, cover (white/black %) 0/69, 1/68, 43/26, 70/0, 69/0 | sun table **identical** (bare 12.4 / 18.2 / 23.9 / 29.7 / 35.5; daisies 19.0 / 24.9 / 22.0 / 21.6 / 27.0; 0/69, 1/68, 43/26, 70/0, 69/0); century bars: bare 0.048–0.062, daisies only 0.013–0.016 |
| 2. add grazers, no weather | cycle ≈ **8 yr** (turns alternate ≈ 7 and 9); grazers swing ×24 (0.016 → 0.39); land 18–21 °C; white up to 64 %, black up to 15 %; boom → planet warmest 0.7 yr later → white bloom 1.1 yr → land coldest 3.6 yr, mixed layer 4.5 yr → black peak 5.6 yr | mean turn **7.9 yr** (alternating 6.8 and 9.2); ×**24** (0.016 → 0.39); land **18.1–21.1**; white **64 %**, black 17 % |
| 3. take the ocean away | no cycle: grazers 0.19, white 29 %, black 26 %, land 18.3 °C; all-land with weather: busts every ≈ 2 yr, small; 30 % ocean: ≈ 3 yr | **0.19, 29 %, 26 %, 18.3 °C**; 30 % ocean **3.0 yr** |
| 4. add weather: busts of every size | bust falls ×8–17 typical, ×3 smallest tenth, ×200–330 largest tenth; century bar 0.11–0.28 K (2–4× the bare planet's); correlation of bust depth with the ocean's temperature in the 3 yr before ≈ **−0.8** | century bar **0.16–0.20 K** (bare 0.05–0.06): ✓. Bust statistics and the −0.8 correlation: **not reproduced** (§6) |
| 5. the ocean sets the beat (clockwork: best 26 °C, tolerance 5 K) | turn 6.7 / 7.7 / 8.4 / 10.7 yr at 25 / 50 / 75 / 150 m | **6.7 / 7.7 / 8.4 / 10.7** |
| 6. change the grazers (preset 6) | best 22 °C: 1.1 yr, ×37, 21–23 °C; best 28: 8.4 yr, > 10⁴, 19–23; best 30: die out, land 22; tolerance 4 K: 7.8 yr; 8 K: 1.3 yr, ×38; taste 0.5: 1.2 yr, ×48, 23–24; taste 1: ≈ 4 yr, > 10⁴, 26–30 | best 22: **1.1 yr, ×37, 21–23**; 28: **8.3 yr**, ×15,000, 19–23; 30: **die out, 22 °C**; tol 4: **7.8 yr**; tol 8: **1.3 yr, ×38**; taste 0.5: **1.2 yr, ×48, 23–24**; taste 1: **4.1 yr**, ×20,000, 27–30 |

Also reproduced: without the deep ocean the cycle is ≈ 7.4 yr, with it ≈ 7.9 yr (handout: ≈ 7.4 and ≈ 8).

**Why (handout).** No step needs anything from outside: each balancing loop answers the last change **through the ocean, years late**, so each answer overshoots (follow the loop: grazers → black daisies (B4), food runs out, white daisies take the land (B3), the land cools through the ocean's delay, black daisies spread (B2), the land warms, the grazers' appetite returns). Take the ocean away and the delay disappears: the planet settles (Run 3). A deeper mixed layer holds more heat, so cooling after each white bloom drags on: a **longer** beat (Run 5). Weather is fast and small, but the ocean **adds up** the pushes, so a run of cold years leaves a cold ocean going into a bust: the colder the ocean, the deeper the bust; the loop sets **when** busts come, the ocean's memory of the weather sets **how big**. Daisies alone took the slow swings **out** (Run 1: century bar 3× smaller); daisies + grazers + ocean put far more **back in** (Run 4). The cycle needs the **climate in the loop**: grazers that do not care about temperature cycle fast with their food alone; grazers held back too hard die out (Run 6). *Take-it-further exercise* (spreadsheet): download the stacked busts, work with anomalies, average bust, big against small, regress bust depth on the mixed-layer anomaly in years −3 to −1.

**What the models leave out** (handouts): places (no daisy can move somewhere cooler), evolution, geography, any real greenhouse, clouds, sea ice (the real ocean's albedo jumps from ≈ 0.06 to ≈ 0.6 on freezing), a deep ocean in tutorial 1 (one slab), and in tutorial 1 **one temperature for land and ocean** (the biggest simplification: on Earth the annual range is tens of K inside continents and a few K over the open ocean; here ocean slows the land down too). Earth's living things do change its climate (forests darken snowy land, plants move water into the air) but much more weakly than Daisyworld, which is built to make the link strong.

## 4. Practice
1. **Leverage.** Show that with land fraction $f$ the albedo swing available to the daisies is $0.5f$, and compute the temperature of the all-black and all-white all-land planet at $L=1$ (no ocean, $S=917$).
2. **Response time.** Compute $\tau$ for all land, 30 % ocean with 50 m and 70 % ocean with 200 m using $\lambda=5.4$ W m⁻² K⁻¹, $C_\text{land}=10^7$, $\rho c=4.1\times10^6$.
3. **Path and destination.** Explain in two sentences why the bare planet always ends ≈ 7 K warmer after the sudden change whatever the depth, but the daisy planet's *peak* depends on the depth.
4. **Loop signs.** Using the diagram's links, show that the path Grazers → Black daisies → Land temperature → Grazers is balancing or reinforcing. (Links: grazers eat black daisies (−); black daisies darken the land, more black ⇒ warmer (+); warmer land ⇒ hungrier grazers (+).)
5. **Weather and memory.** A mixed layer adds up random pushes. If the pushes are independent from day to day, how does the standard deviation of the average of $N$ days shrink, and why do the bars sit *above* that line for the ocean?
6. **Forecast.** The Arabian Sea cools from ≈ 30 °C in May to ≈ 27 °C in August. Which ingredients of the real ocean are missing from the model, and which three of Joy's lectures supply them?

> [!example]- Solutions
> 1. On land $A$ runs from 0.25 (all black) to 0.75 (all white): a swing of 0.5; the ocean contributes a fixed $(1-f)A_o$, so the planet's swing is $0.5f$. All black: $T=[917\times0.75/(5.67\times10^{-8})]^{1/4}=$ 331.9 K = **58.7 °C** (🔵 for $A=0.25$); all white: $A=0.75$, $T=[917\times0.25/\sigma]^{1/4}=252.2$ K = **−20.9 °C**.
> 2. All land: $10^7/5.4=1.85\times10^6$ s = **21 d**. 30 % ocean, 50 m: $C=0.7\times10^7+0.3\times4.1\times10^6\times50=6.9\times10^7$: **148 d**. 70 % ocean, 200 m: $C=0.3\times10^7+0.7\times4.1\times10^6\times200=5.77\times10^8$: **3.4 yr**.
> 3. The final state has $dT/dt=0$ so $C$ drops out, and the bare planet's equilibrium shift ($\approx\Delta F/\lambda$) is the same. The daisy planet is pulled back by biology on a years-long clock; a larger $C$ stretches the warming over more years, so the daisies have time to respond and the peak is lower.
> 4. Count the minus signs: eat (−), darken (+), appetite (+): **one** minus ⇒ **balancing**.
> 5. The spread of the mean of $N$ independent values falls as $1/\sqrt N$; the ocean keeps a month's warmth for years, so successive months are **not independent** and averaging washes out less: the bars sit **above** the dashed weather-alone line.
> 6. Missing: **water moving** (Ekman transport and coastal upwelling off Somalia and Oman), a **deeper mixed layer** stirred by the monsoon winds (20 → 62 m), and monsoon clouds. Lectures: O3 (mixed layer, [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]]), O4 (Ekman, [[CL24 The Ocean's Ledger III - Wind and the Momentum Ledger]]), and the cloud and energy-budget story of [[CL22 The Ocean's Ledger I - Accounting for Energy]].

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Depth sets the timescale, not the size of the slow swings: weather-kicked slabs
> A slab with heat capacity C and restoring strength λ obeys C dT′/dt = F′ − λT′.
>
> ![[cl_inertia_spectrum.png|720]]
>
> **Try:** Defaults (mixed layer 75 m, b = 2.09, land 10⁷ J m⁻² K⁻¹): the mixed layer has ≈ 470× less power than land at 1 year and the same power (0.99) at 300 years. Change the depth: the fast end moves, the slow plateau does not. Tick the deep ocean: the plateau falls to ≈ 0.55 of land's at the slowest periods.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_inertia_spectrum.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_inertia_spectrum.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## 5. Map of this chapter
> [!connection] How CL27 connects
> **Builds on:** [[CL04 Feedback and Multiple Steady States]] (Daisyworld, Planck λ, hysteresis), [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]] (slab, τ, weather noise), [[CL22 The Ocean's Ledger I - Accounting for Energy]].
> **Leads to:** CL28 (CERES tutorial), the Stommel switch in [[CL26 The Ocean's Ledger V - Mass, the Overturning and the Switch]] (positive feedback with two stable states, like Run 5).
> **Concepts:** [[Zero-Dimensional Energy Balance Model]] · [[Albedo]] · [[Ice-Albedo Feedback]] · [[Planck Sensitivity]] · [[Daisyworld]] · [[Causal Loop Diagram]] · [[Hysteresis]] · [[Climate Response Time]]

## 6. What I could not reproduce
- **One-year share of the final warming after brightening** (Part 1, Run 6): mine 26–27 %, the handout's 35 % (with deep) and 37 % (without). The later shares (10, 100, 500 yr) and the final 5.8 K match, so the model is right and the convention of the "1 year" number (how the app reads it) is not recoverable from the handout.
- **Bust statistics and the −0.8 correlation** (Part 2, Run 4): with my bust definition (a peak of the 3-month-smoothed grazers, separated by ≥ 1.5 yr, drop = peak over the minimum before the next peak) the median drop is ×26 (10th percentile ×1.5–1.9, 90th ×28–29) and the correlation of log drop with the mixed-layer anomaly in the 3 yr before is **+0.2**, not ×8–17 and **−0.8**. The app's definition (circles ≥ 12 yr apart, "how many times the grazers fell") is not given in enough detail. The century bars (0.16–0.20 K, inside 0.11–0.28) and the mechanism are reproduced; the sign of the correlation is **not**.
- Tutorial 1 Run 10: the "return on the way down" row (0.96 / 0.75 / 0.63) is not defined clearly enough in the handout; the other Run 10 numbers are reproduced (§1).
- The apps are stochastic in the life runs (another browser gives busts at different times): exact matches are not expected there.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | tutorial 1 model, ten runs, three clocks, what is left out | `tutorials/daisyworld-land-ocean/daisyworld_land_ocean_handout.pdf` (text in `transcripts/tut_pdf/daisyworld_land_ocean_handout.txt`, read in full) | taught (2026) |
> | tutorial 2 Part 1 (bare planet), six runs | `daisyworld_ocean_handout.pdf`; app page "How it works" (`transcripts/tutorial_daisyworld-ocean.md`, read in full) | taught (2026) |
> | tutorial 2 Part 2 (life): loop diagram, six runs, take-it-further | `daisyworld_ocean_life_handout.pdf` (read in full) | taught (2026) |
> | every 🔵 number | `scripts/daisy_land_ocean.py` (`part2` argument), `scripts/daisy_ocean.py` (`bare`, `life`), `scripts/daisy_ocean_runs.py`, `scripts/daisy_ocean_busts.py`, `scripts/fig_cl27.py` | extra-beyond |
>
> **Notes.** Equations and parameters are those printed in the handouts and the app's explanation page; the integration is mine (explicit Euler, 0.25–0.5 day step for the non-linear models, exact modal discretisation for the linear three-slab model). I did not run Joy's apps; "reproduced" means my re-implementation agrees with the handout's printed numbers.
