---
title: CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia
aliases: [CL23, effective heat capacity, thermal inertia, slab ocean, heat equation, penetration depth, mixed layer depth, eddy diffusivity, Hasselmann, stochastic climate model, climate timescales, Joy O2, Joy O3]
subject: climate
type: chapter
chapter: 23
part: VI
scope: [taught, extra-beyond]
by: [joy]
status: draft
prereq: ["[[CL22 The Ocean's Ledger I - Accounting for Energy]]", "[[CL18 The Ocean as the Climate System's Heat Reservoir]]", "[[CL04 Feedback and Multiple Steady States]]"]
tags: [subject/climate, type/chapter, taught, extra/beyond, src/joy, status/draft]
---
# CL23 · The Ocean's Ledger II: Heat Capacity and Climate Inertia

◀ [[CL22 The Ocean's Ledger I - Accounting for Energy]] · [[Climate - Course Map|Course Map]] · ▶ CL24 (planned: momentum ledger)

<span class="scope-taught">taught · in syllabus (2026 Joy, O2 and O3)</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-13)
> **Primary source: Joy's Week 2 slide deck** (frames 1–40, "Where does it go?"; PDF with speaker notes in `earth-and-climate/climate/lecture-notes-slides/joy_slides_pdf/`), then the **O2 and O3 handouts**, then the **Daisyworld-with-an-Ocean tutorial** (Part 1), whose numbers I reproduced. Joy's readings for these lectures (Stewart §6.10, Hartmann §4.2–4.3, §4.9, §7.3, §10.6) are on his list but **were not read in this pass**: they appear only as Joy cites them. Neena's 2025 version of the heat-storage and mixed-layer story is [[CL18 The Ocean as the Climate System's Heat Reservoir]] §5–6; CL23 adds Joy's conduction-versus-stirring argument, the slab equation, the timescale ruler and the weather-noise (Hasselmann) result, none of which CL18 has. Every number marked 🔵 was recomputed with `scripts/joy_inertia_numbers.py`, `scripts/daisy_ocean.py` or the CERES files.

> [!syllabus] Syllabus map
> 🟢 **Taught (Joy, 2026)**
> - §1 effective heat capacity; §2 sunlight down the column; §3 **land: conduction** (heat equation, penetration depth d); §4 **ocean: stirring** (why water alone would be no better than soil, eddy diffusivity, the mixed layer and what sets its depth, the thermocline); §5 the **slab equation** C dT′/dt = F′ − λT′ and **τ = C/λ**; §6 the **seasonal-range test**; §7 **same sun and weather on three slabs**, power by timescale, **depth sets the timescale, not the size of the slow swings** (Hasselmann); §8 **inertia today**; §9 the hand-off to ocean transport
>
> 🔵 **Extra · beyond** (my recomputations, labelled)
> - all penetration depths, reaches, timescales and spectra recomputed; the analytic slab spectra of figure B; the seasonal amplitude and lag of a slab; the CERES check of the seasonal-range table

> [!key] After this chapter you can
> - derive the **penetration depth** $d=\sqrt{2\kappa/\omega}$ and explain why land is "always a thin slab" while the ocean's depth is set by **stirring**,
> - state the **slab equation**, get **τ = C/λ** and rank land, atmosphere, mixed layer and full ocean,
> - explain why **Mumbai varies less than Pune** and why a 5–10-day forecast can fix the SST but a seasonal forecast cannot,
> - explain why a deeper mixed layer **shrinks fast swings by (C₁/C₂)² but leaves the slow swings the same size**,
> - say why the Earth's **+1 W m⁻²** imbalance shows up mostly as ocean heat and why warming **lags**.

> [!intuition] The one-sentence story
> Everything responds to the same weather push, but a surface can only lean on the heat it can reach: land reaches **~10 cm in a day, ~2 m in a year** (conduction), while the ocean is **stirred**, so the top **~50 m** act as one slab with **~50 times** the capacity. The slab turns fast random weather into slow wandering without making the slowest swings bigger: *depth sets the timescale, not the size of the slow swings*.

![[fig_cl23_inertia.png]]
*A: reach $d=\sqrt{2\kappa/\omega}$ against the period of the swing for soil, still water and eddy diffusion below the mixed layer. B: temperature power of weather-kicked slabs (land, mixed layer, mixed layer + deep ocean) with the app's numbers (C_L = 10⁷, C_m = 4.2×10⁶ × 75 m, C_d = 4.2×10⁹ J m⁻² K⁻¹, b = 2.09, γ = 0.7 W m⁻² K⁻¹); dotted lines mark the bend period 2πτ. C: τ = C/λ with Argha's Planck λ = 3.8. Numbers: `scripts/joy_inertia_numbers.py`; figure: `scripts/fig_cl23.py`.*

## 1. Which heat capacity?
<span class="scope-taught">taught</span> *O2 handout §4*

A continental climate has big swings, a coastal one small swings. It is not that water "retains heat" better: anything stores heat. The question is **how much the temperature changes per joule absorbed**, i.e. the heat capacity $C$. But *which* heat capacity? The ocean is 4 km deep and the rock under your feet kilometres thick; if all of it took part in every exchange no temperature would ever change. What matters is the **effective** heat capacity: that of the part the weather's push actually reaches. That depends on **how heat gets below the surface**: by **conduction** on land, by **stirring** in the ocean.

## 2. Sunlight down the column
<span class="scope-taught">taught</span> *Week 2 deck frames 2–4; O2 handout §1; fuller treatment in [[CL18 The Ocean as the Climate System's Heat Reservoir]] §2 (Neena)*

Only ≈ 2 % of overhead sunlight is reflected (Stewart §6.10, as Joy cites it), so nearly everything enters the water, **colour by colour**: red is gone within ≈ 10 m, blue reaches 100–200 m in clear open-ocean water; counting the infrared (gone in centimetres), **more than half is absorbed in the top metre** and only ≈ 5 % is left at 50 m. The ocean is **heated from the top**. (Why blue goes deepest: pure water absorbs red and infrared strongly through molecular vibration and is most transparent in the blue; coastal water adds chlorophyll and dissolved yellow matter that absorb short wavelengths, so lakes look green or brown: O2 handout §1.) The surface then pays out energy in the four terms of [[CL22 The Ocean's Ledger I - Accounting for Energy]] §7.

## 3. Land: heat has to conduct
<span class="scope-taught">taught</span> *Week 2 deck frames 12–17; O2 handout §5* · <span class="scope-extra-beyond">extra · beyond</span> *numbers recomputed*

Soil cannot stir itself. **Fourier's law** $q=-k\,\partial T/\partial z$ and conservation $\rho c\,\partial T/\partial t=-\partial q/\partial z$ give the **heat equation**
$$\frac{\partial T}{\partial t}=\kappa\frac{\partial^2T}{\partial z^2},\qquad \kappa=\frac{k}{\rho c}\approx(0.3\text{–}1)\times10^{-6}\ \text{m}^2\text{s}^{-1}\ \text{(moist soil, } \rho c\approx2\times10^{6}\ \text{J m}^{-3}\text{K}^{-1}).$$
For a surface swing of angular frequency $\omega$ the solution is
$$T'(z,t)=A\,e^{-z/d}\cos\!\big(\omega t-z/d\big),\qquad d=\sqrt{2\kappa/\omega}:$$
the swing **fades** with depth and **lags** (peaks later deeper). Fast forcing gives small $d$, slow forcing larger $d$ (reach ∝ √period: a year is 365 days, so $\sqrt{365}\approx19$ times deeper than a day).

| Swing | $d$ for κ = 0.3 / 0.5 / 1 ×10⁻⁶ m² s⁻¹ (🔵) | As a slab: metres of water with the same surface flux (🔵) |
|---|---|---|
| a day | 9.1 / 11.7 / 16.6 cm | 3.1 / 4.0 / 5.6 cm |
| a year | 1.74 / 2.24 / 3.17 m | 0.59 / 0.76 / 1.07 m |

(Slab equivalent $C=\rho c\,d/\sqrt2$, with ρc(soil)/ρc(water) = 2/4.2. These reproduce the slide's "9/12/17 cm, 1.7/2.2/3.2 m, 3–6 cm, 0.6–1.1 m". Hartmann's (4.10) omits the factor 2 in $d$, so he quotes ≈ 10 cm and ≈ 1.5 m: same physics, his depth is ours ÷ √2: 🔵 8.3 cm and 1.58 m.) So **land is not a fixed slab** (its $C$ grows with the timescale, as $\sqrt{\text{period}}$) **but it is always thin**: about **1 m of water** for a year's swing, about 5 cm for a day's. The Moon, where conduction is all there is, goes from ≈ 100 K at night to ≈ 390 K by day at its equator.

## 4. Ocean: it can stir itself
<span class="scope-taught">taught</span> *Week 2 deck frames 18–28; O2 handout §6 and "Read this part"; O3 handout §2*

**If water only conducted** it would be no better than soil: its molecular diffusivity is only κ ≈ 1.4×10⁻⁷ m² s⁻¹, so a day reaches ≈ 6 cm and a year ≈ 1.2 m (🔵 6.2 cm, 1.19 m), a slab of ≈ **0.8 m** of water (🔵 0.84 m) against soil's 0.6–1.1 m. Water's large ρc only makes up for its short reach. The ocean's inertia comes from **stirring**: wind and breaking waves from above, cooling water sinking at night and in winter. Turbulent eddies mix heat **10⁴–10⁶ times faster** than molecules (Stewart ch. 8, as Joy cites it), so the top layer is at one temperature all the way down: the **mixed layer** ([[Mixed Layer]]). Conduction only: ≈ 1.2 m; soil: 1.7–3.2 m; stirred: tens to hundreds of metres.

**What sets the depth (stirring against stratification).** Wind drags the top water, the layer below less; the shear is turbulent and eddies carry water up and down. The stirring stops where the warm light water above sits on cold dense water below, because mixing them raises the column's potential energy and the wind must supply that energy.

| Place and time | Mixed-layer depth (ocean reanalysis, as shown on the slides, ✓ by Joy) |
|---|---|
| Arabian Sea (60–70°E, 10–20°N) | ≈ **20 m** in April, ≈ **62 m** in July: the monsoon winds stir it deeper |
| Near Bermuda (64°W, 32°N) | ≈ **91 m** in January, ≈ **6 m** in July: winter cooling and storms; thin warm lid in summer |
| Global | median ≈ **44 m**; March North Atlantic (45–65°N, 60–10°W) ≈ **304 m**, > 1 km in places; September Southern Ocean (45–60°S) ≈ **171 m** |

Why the deepest northern mixed layers (off Japan, off North America) coincide with the starts of the **storm tracks** (storms stir, and warm water supplies the vapour that fuels them), and why the Southern Ocean's is deep and uniform (strong winds all the way round and **no land** in the way: land is "sandpaper" to the wind, the sea is smooth): O3 handout §2. The monsoon wind itself is the surface inflow replacing air that rose in the rain belt (same handout).

**Below the mixed layer.** The thermocline resists stirring; the eddy diffusivity there is $K\sim10^{-5}$–$10^{-4}$ m² s⁻¹ (≈ 10⁻⁵ from the tracer-release experiment of Ledwell et al. 1993, a paper not read). With the same $d=\sqrt{2K/\omega}$ the reach **from the base of the mixed layer** is (🔵, matching the slide): 1 yr → **10 / 32 m**, 10 yr → **32 / 100 m**, 100 yr → **100 / 317 m** (for $K=10^{-5}$ / $10^{-4}$). The deep ocean joins in only at long timescales. And note Joy's point: **no water has gone anywhere**; mixing up and down alone sets the ocean's active thermal inertia.

## 5. The slab equation and the timescale ruler
<span class="scope-taught">taught</span> *Week 2 deck frames 29–31; O3 handout §3*

Take away everything below the mixed layer (right for the **fast climate**, seasons to a few years) and treat the surface, land or mixed layer, as a slab with heat capacity $C$ (per m²). For departures $T'$ from the mean, with $F'$ the weather and $\lambda$ the Planck response of [[CL04 Feedback and Multiple Steady States]]:
$$C\frac{dT'}{dt}=F'(t)-\lambda T' .$$
Land and ocean are **the same equation with very different $C$**. Without kicks $T'$ decays exponentially, and since both terms are in W m⁻², **$\tau=C/\lambda$** is a time.

| $C$ as metres of water | $\tau=C/\lambda$, $\lambda=3.8$ W m⁻² K⁻¹ (🔵 $\rho c=4.2\times10^6$) |
|---|---|
| land (a year's swing): ≈ 1 | 12.8 days ("about 12 days") |
| whole atmosphere: 2.4 | 30.7 days ("about a month") |
| mixed layer: 50 | 1.75 yr ("about 1.7 years") |
| full ocean: 4,000 | 140 yr (longer in practice: mixing to depth is slow) |

So weather has **50 times** more to warm over the mixed layer than over land before the deep ocean even joins in. (The tutorial app uses a net feedback $b=2.09$, a 75 m layer and a land box that carries the air above it, 2.4 m of water: its mixed layer takes ≈ **5 years** (🔵 4.8) and its land ≈ 2 months (🔵 55 days incl. no ocean exchange); the physics is the same.)

**Why Mumbai varies less than Pune.** Land like Pune responds to a strong push within a couple of weeks; the mixed layer off Mumbai takes more than a year, and Mumbai's air comes off that sea.

## 6. The test: the same seasons swing land far more than sea
<span class="scope-taught">taught</span> *Week 2 deck frame 32; O3 handout §3*

Seasonal range (warmest minus coldest month) of surface temperature from CERES upwelling longwave ($\sigma T^4$, emissivity 1). 🔵 My recomputation from the explorer's 2° climatology (2010–2024; the slide used 2010–2020) is in the last column.

| Place | Slide | 🔵 recomputed |
|---|---|---|
| Yakutsk | 57 K | 57 K |
| Almaty | 35 K | 33 K |
| Delhi | 23 K | 22 K |
| Pune | 9 K | 7 K |
| Mumbai | 5 K | 7 K (a 2° cell is not coastal-resolving) |
| Arabian Sea (10–20°N, 60–70°E) | 5 K | 4.0 K |
| Equatorial Pacific | 2 K | 1.8 K |

Joy's caveat: tropical ranges are small anyway, so 2 K there cannot be compared directly with 23 K in Delhi, but Delhi and Mumbai under not very different suns can: land, land and more land against a coast.

**A slab check (🔵).** ±30 % seasonal sunlight on the app's numbers: land (C = 10⁷, albedo 0.32) F′ = 73 W m⁻², range $2F'/\sqrt{b^2+\omega^2C^2}\approx$ **51 K** with a lag of 44° ≈ 1.5 months (slide: 49 K); mixed layer alone (albedo 0.28) range ≈ **2.5 K**, lag **88° ≈ 2.9 months** (slide: 3.3 K, warmest in September, ≈ 3 months after the sun; the extra kelvin comes from coupling to the land). The shrunken and lagged ocean season is the slab at work: a season is a slow push but **not slow enough for a ~5-year slab to catch up**.

**Practical consequence (O3 handout §4).** A forecast for 5–10 days can start from today's SST and hold it fixed; a seasonal forecast (the monsoon rainfall over four months) needs an ocean that responds, because a small SST change over a season is a large heat flow.

## 7. Same weather, three slabs: Hasselmann's point
<span class="scope-taught">taught</span> *Week 2 deck frames 33–38; O3 handout §4 and "Depth sets the timescale"* · tutorial: *Daisyworld with an Ocean, Part 1, Runs 1–5*

Drive land, a mixed layer and a mixed layer over a deep ocean with the **same** random weather (a push lasting ≈ 3 days; a day's mean spreads **30 W m⁻²**; nothing in it swings slowly). The slide numbers (the tutorial app's own runs): land follows the seasons (**49 K** Feb–Aug) and every spell of weather (month-to-month ±**3.2 K**); the day–night swing is only ≈ 1.2 K because the app's land is one slab sized for the year; the mixed layer has seasons of **3.3 K**, warmest in September, month-to-month departures ±**0.7 K** that **wander** (it adds up the kicks); a deep ocean below changes little at these zooms.

Sorted by timescale (power spectrum of departures from the average year):
- **Fast swings:** on these timescales the kicks have no time to be balanced by heat loss, so $C$ alone sets the response and power falls as $(C_\text{land}/C_\text{ocean})^2$ ≈ **992** for the app (🔵 $31.5^2$). Slide: mixed layer has **190×** less power than land at 6 months–2 years and **490×** at 2–6 months. 🔵 Analytically (white push, $|T|^2\propto1/|iωC+λ|^2$): 1/473 at 1 yr, 1/184 at 2 yr, 1/25 at 6 yr.
- **Slow swings:** the surface has time to balance, $F'\approx\lambda T'$, **$C$ drops out**: mixed/land power = **0.99** at 100–1,000 yr (slide ✓; 🔵 0.99 at 300 yr). The bend is at period $2\pi\tau$: land ≈ 1 yr, mixed layer ≈ 30 yr (🔵 0.95 yr, 30.0 yr).
- **Depth sets the timescale, not the size of the slow swings.** Fast, random weather produces slow climate variations with nothing slow driving them (**Hasselmann 1976**; paper not read).
- **A deep ocean calms, it does not add:** a second corner far out (τ ≈ 190 yr, period ≈ 1,200 yr) and extra damping at centennial scales: slow power falls to **0.65** of land's (slide); 🔵 analytic **0.53–0.68** over 100–1,000 yr, slow limit $(b/(b+\gamma))^2=0.56$. A leak to a big reservoir acts like a larger λ.

🔵 **Tutorial check.** My simulation of the app's three-slab model (`scripts/daisy_ocean.py bare`) gives block-mean spreads (month / year / 10 yr / 100 yr): land only 3.17–3.21 / 1.75–1.79 / 0.58–0.61 / 0.16–0.20 K; with a mixed layer 0.74–0.75 / 0.68–0.69 / 0.47–0.49 / 0.15–0.20 K, inside the handout's ranges (3.20–3.26, 1.75–1.83, 0.55–0.67, 0.14–0.28; 0.74–0.80, 0.67–0.74, 0.45–0.54, 0.14–0.26). Depth runs (year / decade bar): 25 m 1.10/0.56, 75 m 0.69/0.49, 150 m 0.50/0.40 K: the fast bars shrink, the century bar stays (0.17–0.18 K). With the deep ocean the century bar falls (0.17 → 0.15 K). The year bar barely drops from the month bar with a mixed layer: the ocean *keeps a month's warmth for years*.

## 8. Inertia today
<span class="scope-taught">taught</span> *Week 2 deck frame 39; O3 handout §5*

Earth gains ≈ **+1.0 W m⁻²** (CERES 2010–2020, slide; 🔵 +1.26 W m⁻² for 2010–2024 with a trend of +0.61 W m⁻² per decade, [[CL22 The Ocean's Ledger I - Accounting for Energy]] §3). The slide cites WMO (State of the Global Climate 2025: > 91 % of the excess heat goes into the ocean) and Forster et al. (2026: imbalance more than doubled since 1976–1995); neither was read. The satellite global mean is **pinned to ocean thermometers** (EBAF adjusted to in-situ heat storage, Loeb et al. 2018, as Joy cites it). **Inertia is why warming lags**: most of the extra heat goes where it barely shows at the surface.

*No free lunch.* The mixed layer catches up within a few τ but keeps leaking heat into the deep ocean, which takes centuries to fill; the deep circulation returns deep water only after centuries, so the whole system needs of order **1,000 years** to rebalance and the emissions of the past 150 years shape the climate for centuries (O3 handout §5). 🔵 In the tutorial model a 5 % brighter sun (ΔL = 0.05) warms the planet by **5.79 K** eventually (handout 5.8): the share reached after 10 / 100 / 500 yr is **79 / 87 / 98 %** with the deep ocean and **94 / 100 / 100 %** without (handout 80 / 87 / 98 and 95 / 100 / 100). My one-year share (26–27 %) is lower than the handout's (35 %, 37 %): the convention behind that one number is not recoverable from the handout.

## 9. Hand-off: the ocean gains heat where it is cold
<span class="scope-taught">taught</span> *Week 2 deck frames 40–41; O3 handout §6*

A slab that only stores heat nets **zero over a year at every place**. The reanalysis map of annual-mean net heat flux (2011) does not: the ocean **gains** heat along the equator (the cold tongue) and on the Somali and Arabian coasts, where the water is **cold**, and **loses** it over the Gulf Stream and Kuroshio, where warm water has been carried under cold dry winter air. (On the equator the sunlight is the same east and west, so the evaporation must differ: cold water evaporates little, and most of the sunlight stays in the ocean: O3 handout §6.) So the **water must move**; what moves it is the momentum ledger, [[CL22 The Ocean's Ledger I - Accounting for Energy]] §4 → CL24 (planned).

## Map of this chapter
> [!connection] How CL23 connects
> **Builds on:** [[CL22 The Ocean's Ledger I - Accounting for Energy]] (the budget and the weather push F′), [[CL18 The Ocean as the Climate System's Heat Reservoir]] (Neena's heat storage and mixed layer), [[CL04 Feedback and Multiple Steady States]] (Planck λ, Daisyworld), [[CL15 Monsoons]] (the monsoon mixed layer).
> **Leads to:** CL24 momentum ledger (why the heat map is the way it is), CL27 Daisyworld tutorials (planned; the model checked in §7–8).
> **Concepts:** [[Mixed Layer]] · [[Thermocline and Pycnocline]] · [[Planck Sensitivity]] · [[Sea Surface Energy Budget]]

## Summary
> [!summary] Cheat-sheet
> - $\partial_tT=\kappa\partial_z^2T$; periodic forcing ⇒ $T'=Ae^{-z/d}\cos(\omega t-z/d)$, $d=\sqrt{2\kappa/\omega}$: soil **9–17 cm (day), 1.7–3.2 m (year)**; slab ≈ 5 cm / 1 m of water. Still water 6 cm / 1.2 m. Below the mixed layer $K=10^{-5}$–$10^{-4}$: 10–32 m (1 yr), 100–317 m (100 yr).
> - Stirred mixed layer ≈ 44 m median; Arabian Sea 20 → 62 m; Bermuda 91 → 6 m; March N. Atlantic ≈ 304 m.
> - $C\,dT'/dt=F'-\lambda T'$; $\tau=C/\lambda$: land 12 d, air 1 month, mixed layer 1.7 yr, ocean 140 yr (λ = 3.8). Seasonal range: Yakutsk 57, Delhi 23, Pune 9, Mumbai 5, Arabian Sea 5, equatorial Pacific 2 K.
> - Fast swings: power ∝ 1/C² (≈ 992 for the app); slow swings: same size (0.99); deep ocean ×0.65. **Depth sets the timescale, not the size.** Bend at period 2πτ.
> - Imbalance ≈ +1 W m⁻², > 91 % into the ocean; two-stage warming (≈ 80 % in 10 yr, the rest over centuries).

## Practice
1. **Soil.** A soil has twice the diffusivity of another. How much deeper does the annual swing reach, and how much more heat does it hold as a slab?
2. **The Moon with water.** If the Moon's surface were covered with 1 m of still water, would the day–night contrast change much? What if the water were stirred? (Joy O2 handout.)
3. **Decay.** A 1 K anomaly appears in a 50 m mixed layer. How long until only a third is left if only the Planck response acts ($\lambda=3.8$)? Why might the real answer be longer? (Joy O3 handout.)
4. **Reach.** Compute the reach from the base of the mixed layer for $K=10^{-4}$ over a decade; compare with a 75 m mixed layer.
5. **Spectra.** Show that the slab power spectrum is $\propto 1/(\omega^2C^2+\lambda^2)$ for a white push, and find the period where land and the mixed layer power are each half their slow-limit value.
6. **Hasselmann.** Explain in one paragraph why a deeper mixed layer reduces month-to-month swings but not 100-year swings.
7. **Forecasting.** Whose temperature next month would you rather forecast, Delhi's or the Arabian Sea's? What would make you less sure? (Joy's tutorial question.)

> [!example]- Solutions
> 1. $d\propto\sqrt\kappa$: **√2 ≈ 1.41 times deeper**; heat held as a slab $\propto \rho c\,d$: **1.41 times more**.
> 2. Still water 1 m ≈ the 0.8 m slab: **little change** (water conducts like soil over a day, reach ≈ 6 cm): the day–night contrast stays large. Stirred, the day's heat spreads over the stirred depth, so the contrast shrinks greatly.
> 3. $\tau=C/\lambda=50\times4.2\times10^6/3.8=5.5\times10^{7}$ s = 1.75 yr; one third left after $t=\tau\ln3=1.9$ yr. Longer in reality because the layer exchanges heat with the deep ocean and feedbacks (water vapour) reduce the net λ; the tutorial's λ = 2.09 gives τ ≈ 3.2 yr for 50 m.
> 4. For a decade $\omega=2\pi/(3.156\times10^{8}\ \text{s})=1.99\times10^{-8}\ \text{s}^{-1}$, so $d=\sqrt{2\times10^{-4}/1.99\times10^{-8}}=100$ m (the table). Measured from the base of a ≈ 50 m mixed layer the decade's swing reaches ≈ 150 m, deeper than a 75 m layer.
> 5. $|T|^2=|F|^2/|i\omega C+\lambda|^2=|F|^2/(\omega^2C^2+\lambda^2)$; half the slow limit when $\omega C=\lambda$, i.e. $P=2\pi\tau$: land (τ = 55 d, b = 2.09) ≈ **0.95 yr**, mixed layer (τ = 4.8 yr) ≈ **30 yr** (🔵 the dotted lines of figure B).
> 6. At periods shorter than 2πτ the kicks are not balanced by λT′, so $C\,dT'/dt\approx F'$ and the response ∝ 1/C: more depth ⇒ less fast variance. At periods longer than 2πτ the surface is in balance, $\lambda T'\approx F'$, and $C$ has dropped out: the variance of 100-year means depends on λ, which depth does not change. So depth moves the corner (the timescale), not the plateau (the size).
> 7. The Arabian Sea: the large mixed-layer inertia means a persistent anomaly; Delhi is dominated by fast weather and seasons. Less sure when the ocean's depth changes through the year (20 m in April to 62 m in July), when upwelling and wind-driven advection move cold water in (the monsoon summer cooling 29.9 → 26.6 °C, not in the slab model) and El Niño-like feedbacks act (Joy's tutorial leaves these out).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | effective heat capacity, conduction, penetration depth, slab equivalent, still water, eddy reach, mixed layer, slab equation, ruler, seasonal test, three-slab runs, spectrum, deep ocean, imbalance, hand-off | Week 2 deck, frames 1–41 (PDF [[O2-O3_Week2_Where-does-it-go_and_The-ponderous-ocean.pdf]], speaker notes in the `_with-notes` version) | taught (2026) |
> | narrative, the humidity/bulk-formula box (CL22), what sets the mixed layer's depth, forecasting, "depth sets the timescale", inertia today | [[handout_o2.md]] and [[handout_o3.md]] (read in full) | taught (2026) |
> | tutorial numbers (bars, depth runs, brightening) | Daisyworld-with-an-Ocean handout, Part 1 (`tut_pdf/daisyworld_ocean_handout.txt`) and the app's "How it works" page; reproduced with `scripts/daisy_ocean.py` | taught (2026) / extra-beyond (recomputation) |
> | all 🔵 numbers: penetration depths, reaches, τ, spectra, seasonal slab, seasonal ranges from CERES | `scripts/joy_inertia_numbers.py`, `scripts/fig_cl23.py`, CERES explorer data | extra-beyond |
>
> **Notes.** Hartmann §4.2–4.3 (pp. 96–101), §4.9, §7.3 (pp. 200–206), §10.6, Stewart §6.10 and ch. 8, Ledwell et al. (1993), Hasselmann (1976), Czaja and Marshall (2006), Loeb et al. (2018), WMO (2025) and Forster et al. (2026) are cited only as Joy cites them; none was read in this pass. The mixed-layer depths are from Joy's slides (ocean reanalysis), not recomputed.
