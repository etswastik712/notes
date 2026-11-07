---
title: CL18 The Ocean as the Climate System's Heat Reservoir
aliases: [CL18, ocean heat budget, sea surface energy balance, light in the ocean, mixed layer, thermocline, pycnocline, ocean stratification, bulk formulas, heat storage, Neena Lecture 20, Joy O1, Joy O2, Joy O3]
subject: climate
type: chapter
chapter: 18
part: V
scope: [taught, extra-book, extra-beyond]
by: [neena, joy, book]
status: draft
prereq: ["[[CL10 Global Energy Balance and Meridional Structure]]", "[[CL03 Radiation and Planetary Energy Balance]]", "[[CL06 Hydrostatic Balance and Vertical Structure]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/neena, src/joy, src/book, status/draft]
---
# CL18 · The Ocean as the Climate System's Heat Reservoir

◀ [[CL17 Orbital Forcing and Glacial Cycles]] · [[Climate - Course Map|Course Map]] · ▶ [[CL19 Wind-Driven Ocean Circulation]]

<span class="scope-taught">taught · in syllabus (2025 Neena L20; 2026 Joy core readings)</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] Where this chapter comes from (added 2026-11-07)
> Two new sources meet here. **(a) Neena Lecture 20** (2025: solar absorption by the oceans, surface heat balance, SST, salinity, density stratification, the mixed layer and convection). **(b) Joy's ocean readings O1–O3** (this year; `earth-and-climate/climate/books/joy_lecture_readings/`, git-ignored; there are **no Joy slides**, only the tiered reading list). The file names carry the tier, which is used for the labels: **Core** = 🟢 taught (Stewart 2008 pp. 97–100 *Light in the ocean*; Hartmann 2016 pp. 96–101 *surface energy budget and heat storage*, pp. 126–129 *geographic variation of the surface balance*, pp. 200–206 *the mixed layer*; Stewart pp. 65–70 *heat budget geography and transport*), **Optional** = 🟡 extra · book (Stewart pp. 53–61 *heat-budget terms and bulk formulas*; Hartmann pp. 17–19 *the world ocean*, pp. 227–231 *ocean energy transport*, pp. 176–180 *angular momentum balance*), **NotCoveredInClass** = 🟡 (used in [[CL19 Wind-Driven Ocean Circulation]]). The O1 core reading (Hartmann pp. 40–48, TOA balance and poleward flux) repeats [[CL10 Global Energy Balance and Meridional Structure]] (Suhas); it is not re-derived. The Hartmann PDFs are scans with an OCR layer in which **formulas are garbled** (cited by equation number and checked against the dimensions); Stewart's text is clean. Figures in the readings were not read as images.

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught (Neena L20; Joy core readings)**
> - §2 **light in the ocean** (reflectivity 2 %, Beer–Lambert, water types, euphotic zone, ~half the solar flux absorbed in the first metre, blue-green light to >100 m); §3 the **surface energy balance** (storage = net radiation − latent − sensible − horizontal divergence; global means; geography of each term; western boundary currents; upwelling regions); §5 **heat storage** (ocean 30× atmosphere in the mixed layer, land penetration depths); §6 the **mixed layer**, thermocline, pycnocline, salinity, convection, seasonal cycle; §7 meridional heat transport (6 PW, 22 %/8 % ocean at 35°)
>
> 🟡 **Extra · book** (optional readings)
> - §1 the **world ocean** (Hartmann §1.7); §4 **bulk formulas** and measurement (Stewart §5.2–5.5); §7 the three methods for ocean heat transport and the oceanic maximum near 20°N (Hartmann pp. 227–231)
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 attenuation numbers; §4 bulk-formula worked examples; §5 the damped slab model (amplitude and lag) and the penetration-depth factor; §7 the heat-transport consistency check

> [!key] After this chapter you can
> - write the **surface energy balance** of the ocean and name the size and geography of each term,
> - say how deep sunlight goes and why the ocean's **heating is spread over tens of metres**,
> - use the **bulk formulas** for sensible and latent heat flux,
> - explain **why the oceans moderate the seasons**: heat capacity, with a number,
> - describe the **mixed layer, thermocline and pycnocline**, how they change with latitude and season, and what sets salinity and density,
> - quote the **meridional heat transport** and the ocean's share.

> [!intuition] The one-sentence story
> The atmosphere is heated mostly from below and has the heat capacity of 2.5 m of water; the ocean is **heated from above** by light that penetrates tens of metres, **cools at its surface** by evaporation, and its top 70 m already store as much heat per degree as **30 atmospheres**. Between sunlight and the sea floor sits a **stirred layer** (the mixed layer) that talks to the atmosphere, and below it a stable **thermocline** that keeps the deep ocean out of that conversation for centuries.

![[fig_cl18_ocean_heat.png]]
*A: Beer–Lambert transmittance for water of different clarity (§2). B: heat capacity per m² of surface: rock layer, atmosphere, mixed layer, whole ocean (§5). C: the global-mean surface budget of Stewart Fig. 5.6: $168+324=390+78+24=492$ W m⁻² (§3). Numbers: `scripts/cl_neena_numbers.py` (cl18), `scripts/fig_cl16_21.py`.*

> [!tip] 🔬 Interactive: a slab ocean and the seasons
> Open [[Assets/interactive/cl_slab_ocean.html|▶ cl_slab_ocean.html]] (self-contained, works offline). A mixed layer of depth $h$ forced by $Q_0\cos\omega t$ and damped by $\lambda$: amplitude $Q_0/\sqrt{(C\omega)^2+\lambda^2}$ and lag $\arctan(C\omega/\lambda)$. $h=50$ m, $Q_0=100$ W m⁻², $\lambda=20$: **2.16 K, 64°** (about 2.2 months); $h=100$ m: $1.2$ K, $76^\circ$; $h=1$ m (land-like): $5.0$ K, $2^\circ$.

## 1. The world ocean
<span class="scope-extra-book">extra · book</span> *Hartmann 2016 §1.7: [[03_Optional_Hartmann2016_The-World-Ocean_pp17-19.pdf#page=2|pp. 17–18]]*; <span class="scope-taught">taught</span> *Neena L20 pp. 7–10*

The Earth holds $\approx1.35\times10^9$ km³ of water, **97 %** of it seawater. The **world ocean** covers **71 %** of the surface to a mean depth of **3730 m**; it stores and releases heat and chemicals on time scales of seasons to centuries, carries heat poleward, supplies the water vapour for rain and snow, and exchanges CO₂ and O₂ ([[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]]). **Temperature** falls with depth from near the surface-air value to near freezing: a thin well-mixed surface layer, a **thermocline** of rapid change in the first kilometre or so, and a deep layer of almost uniform temperature; in mid and high latitudes the mixed layer is thin in summer and deep in winter. **Salinity** is the mass of dissolved salts per kg of seawater (g kg⁻¹, "psu"): $33$–$38$ in the open ocean; at $35$ g kg⁻¹ about $30$ g kg⁻¹ are sodium ($10.8$) and chloride ($19.4$). Neena's L20 gives the **annual-mean SST range** $4$–$30\,^\circ$C (smaller lateral variation than the atmosphere's because of the heat capacity) and compares the two fluids:

| | atmosphere | ocean |
|---|---|---|
| density | $\rho(P,T)$: $1.2\to0.001$ kg m⁻³, exponentially with height | $\rho(P,T,S)$: $1025\to1065$ kg m⁻³, slightly increasing with depth |
| compressibility | highly compressible | very low |
| heated | from below | from above |

## 2. Sunlight in the ocean
<span class="scope-taught">taught</span> *Stewart 2008 §6.10: [[01_Core_Stewart2008_Light-in-the-Ocean_pp97-100.pdf#page=1|p. 97]], [[01_Core_Stewart2008_Light-in-the-Ocean_pp97-100.pdf#page=2|p. 98]], [[01_Core_Stewart2008_Light-in-the-Ocean_pp97-100.pdf#page=3|p. 99]]; Hartmann §7.3 [[01_Core_Hartmann2016_The-Mixed-Layer_pp200-206.pdf#page=1|p. 200]]; Neena L20 pp. 2–3* · <span class="scope-extra-beyond">extra · beyond</span> *numbers*

Light matters because it **heats** the surface layers, feeds **phytoplankton**, guides animals and, through the colour of the sea, lets satellites map chlorophyll.
- **Reflection:** light travels at $c/n$ with $n=1.33$ ($2.25\times10^8$ m s⁻¹). For vertical incidence the reflectivity is $(n-1)^2/(n+1)^2=0.0201\approx\mathbf{2\,\%}$: **most sunlight enters the sea** (the surface albedo of the ocean is much lower than land's; it rises with solar zenith angle, cloud and wind: Hartmann §4.4).
- **Attenuation** by absorption (pigments, water) and scattering depends on **wavelength**: blue is absorbed least, red most. **Beer–Lambert**: $dI/dx=-cI$, so $I=I_0e^{-cx}$ for constant $c$ (Stewart 6.13–6.14).
- **Water types (Jerlov):** type I (clearest, mid-ocean, "cobalt blue, almost black"): **10 % of the light below the surface reaches 90 m**; productive water (much chlorophyll) is blue-green or green and absorbs shallower (types II, III); **coastal waters** (types 1–9, with "gelbstoffe" and mud) let very little through more than a few metres.
- **All wavelengths together:** infrared and long wavelengths are absorbed in the **top centimetre**; the solar heating rate is greatest at the surface and falls off exponentially: under **average conditions the flux is halved within about 1 m**, yet there is still significant heating at more than 100 m, and in clear water blue-green light penetrates past 100 m (Hartmann p. 200–201). **Neena L20:** about 50 % of the incoming solar radiation reaches the ocean surface (mostly visible and IR); most is absorbed in the upper **200 m, the euphotic zone**.

> [!example] Numbers 🔵
> Type I water: $c=\ln10/90=0.0256$ m⁻¹, an e-folding depth of $39$ m, the **1 % level at 180 m**: the "euphotic zone of about 200 m" of Lecture 20. The total solar flux, "half in the first metre", is $c_\text{eff}=\ln2/1\text{ m}=0.69$ m⁻¹ (dominated by red and infrared) but a **tail** of blue-green light carries a few per cent to tens of metres: **a single exponential is not a good model of the broadband heating**, only of one wavelength band at a time (figure A). Consequence: the solar heating is deposited over a depth of tens of metres, while the cooling (evaporation, long-wave emission, sensible loss) happens at the very surface, so a continual **upward turbulent heat flux** in the upper ocean is needed to balance the two (Hartmann p. 201).

## 3. The surface energy balance
<span class="scope-taught">taught</span> *Hartmann §4.2: [[02_Core_Hartmann2016_Surface-Energy-Budget-and-Heat-Storage_pp96-101.pdf#page=1|p. 96]]; §4.9: [[03_Core_Hartmann2016_Geographic-Variation-of-the-Surface-Energy-Balance_pp126-129.pdf#page=1|pp. 126–129]]; Stewart §5.6: [[02_Core_Stewart2008_Heat-Budget-Geography-and-Transport_pp65-70.pdf#page=1|pp. 65–70]]; Neena L20 pp. 4–6*

> [!key] Hartmann (4.1)–(4.2); Neena L20
> Per unit area through the air–surface interface: $$\frac{\partial E_s}{\partial t}=G=R_s-LE-SH-\Delta F_o,\qquad R_s=LE+SH+\Delta F_o\ (\text{steady, annual or diurnal over land}),$$ with $G$ the storage of energy below the surface, $R_s$ the **net radiation** ($S^\downarrow-S^\uparrow+F^\downarrow-F^\uparrow$), $LE$ the **latent** and $SH$ the **sensible** heat flux from the surface to the atmosphere, and $\Delta F_o$ the **horizontal flux out of the column** (the divergence of the ocean's heat transport; for land ≈ 0). Radiation usually heats the surface and latent and sensible fluxes cool it, so all three are mostly positive. Neglected small terms: **latent heat of fusion** (up to ~10 % of the radiative imbalance for limited periods), kinetic-to-thermal conversion, heat carried by **precipitation** (summer showers cooler than the surface), **photosynthesis** (<1 % globally, ~5 % locally), oxidation of biological matter, geothermal and fossil/nuclear heat. **Neena L20:** over a **non-transparent** surface $R_n=LE+SH+G$; for the ocean the surface is transparent to sunlight, the **net solar $R_o$ enters the water and is absorbed there**, and the total uptake is $R_o$ plus the heat flux $Q$ transferred across the surface.

**Global mean (Stewart Fig. 5.6, after Kiehl and Trenberth):** of $342$ W m⁻² incoming, $107$ are reflected (clouds, aerosols and atmosphere $77$, surface $30$) and $235$ leave as OLR ($165$ emitted by the atmosphere, $30$ by cloud tops, $40$ through the window). **Surface:** gains $168$ (absorbed solar) $+\,324$ (back radiation) $=492$; losses $390$ (IR emitted) $+\,78$ (latent) $+\,24$ (sensible) $=492$. **Atmosphere:** gains $67+78+24+350=519$, losses $165+30+324=519$ (all sums checked). Stewart's point: only **20 %** of the insolation is absorbed *directly* by the atmosphere and **49 %** by ocean and land; what drives the atmosphere is **rain** (the latent heat released where trade-wind vapour condenses in the convergence zone: up to $\sim125$ W m⁻² as an annual mean) **and the infrared** from the sea absorbed by the moist tropical air. Neena's L7 version of the same budget (percentages of $340$ W m⁻²: $30$ % reflected, $22$ % absorbed in the atmosphere, $48$ % at the surface; the surface loses $79$ % as IR, $17$ % latent, $4$ % sensible; net radiative loss of the atmosphere $105$ W m⁻² balanced by $105$ of convective transfer) is the same picture with a $340$ base.

**Geography** (Hartmann §4.9, Stewart §5.6):
- **Net radiation** at the surface peaks in the tropics, following the insolation; over the tropical oceans (low albedo, moderate temperature) it often exceeds $180$ W m⁻²; poleward of the mid-latitudes the annual mean approaches zero. Long-wave up and down are much larger than the net solar but nearly cancel, so the net long-wave cooling is weak.
- **Latent cooling mirrors the insolation**: globally most of the radiative heating of the surface is used to evaporate water; it is largest over the **mid-latitude western boundary currents** (Kuroshio, Gulf Stream; $>200$ W m⁻², winter maximum, "much greater than the local net radiative heating") and across the subtropical oceans, which Hartmann calls "the boiler that drives the circulation of the atmosphere and the hydrologic cycle". **Sensible** loss is small and uniform, largest over dry land and over the western boundary currents when cold continental air blows over them in winter ($>50$ W m⁻² as an annual mean).
- **Ocean divergence** $\Delta F_o$: large and negative (heat supplied by transport, lost to the air) over the western boundary currents; the air heats the water along the **equator** and the **eastern margins** where **upwelling** brings cold water up and latent loss is reduced. Stewart's zonal means: insolation largest in the tropics, evaporation balancing it, and a net ocean **gain in the tropics balanced by loss at high latitudes**; the unconstrained net flux integrates to $+16$ W m⁻² (it should be $\le$ a few W m⁻²: pure error) and $-3$ W m⁻² when constrained by known transports; reanalysis products give $+3.7$ and $-5.8$ W m⁻²: **no data set is ideal**.
- **Why the errors matter** (Stewart): an accuracy of $\pm15$ W m⁻² is needed because that flux warms or cools a 100 m column by $1.1$ K in a year ($15\times3.156\times10^7/(100\times4.2\times10^6)=1.12$ K, 🔵).

## 4. Bulk formulas
<span class="scope-extra-book">extra · book</span> *Stewart §5.2–5.5: [[05_Optional_Stewart2008_Heat-Budget-Terms-and-Bulk-Formulas_pp53-61.pdf#page=1|pp. 53–61]]* · <span class="scope-extra-beyond">extra · beyond</span> *worked examples*

Turbulent fluxes are measured directly only by gust probes (fast wind, humidity and temperature in the surface layer): $\tau=\rho_a\langle u'w'\rangle$, $Q_S=\rho_ac_p\langle w't'\rangle$, $Q_L=L_E\langle w'q'\rangle$. For long-term global values Stewart uses **bulk formulas**:
$$\tau=\rho_aC_DU_{10}^2,\qquad Q_S=\rho_ac_pC_SU_{10}(t_s-t_a),\qquad Q_L=\rho_aL_EC_LU_{10}(q_s-q_a)$$ with $\rho_a=1.3$ kg m⁻³, $c_p=1030$ J kg⁻¹ K⁻¹, $C_D=(0.50+0.071U_{10})\times10^{-3}$, $C_S=1.0\times10^{-3}$, $C_L=1.2\times10^{-3}$, $L_E=2.5\times10^6$ J kg⁻¹; $q_s$ is the saturation specific humidity at the sea-surface temperature, $q_a$ the specific humidity at 10 m. Fluxes depend on **wind speed and air–sea temperature or humidity difference**. Annual-mean ranges (Stewart 5.5–5.8): $Q_{SW}$ $30$–$260$, $Q_{LW}$ $-60$ to $-30$, $Q_L$ $-130$ to $-10$, $Q_S$ $-42$ to $-2$ W m⁻² (the sign is Stewart's: into the ocean positive).

> [!example] Worked examples 🔵 (instantaneous, not annual means)
> Saturation specific humidity from a Tetens-type formula (my addition; $p=1013$ hPa):
>
> | case | $U_{10}$ | $t_s$, $t_a$, RH | $q_s$, $q_a$ | $Q_S$ | $Q_L$ |
> |---|---|---|---|---|---|
> | tropical trade-wind ocean | 8 m/s | 27, 25 °C, 80 % | 0.0222, 0.0157 | **21.4** | **201.1** W m⁻² |
> | Gulf Stream under cool continental air (winter) | 10 m/s | 20, 10 °C, 70 % | 0.0145, 0.0053 | **133.9** | **357.9** W m⁻² |
> | calm, neutral | 5 m/s | 15, 15 °C, 80 % | 0.0105, 0.0084 | 0.0 | 41.1 W m⁻² |
>
> The trade-wind latent flux ($\sim200$ W m⁻²) is above Stewart's annual-mean range ($\le130$) because it is an instantaneous value at a fairly windy, dryish moment; Hartmann's statement that evaporative loss "may exceed 200 W m⁻²" in the western boundary currents and over the subtropical oceans is consistent. The wind stress for $U_{10}=6$, $10$, $15$ m/s is $0.043$, $0.157$, $0.458$ N m⁻².

## 5. Heat storage: why oceans moderate climate
<span class="scope-taught">taught</span> *Hartmann §4.3: [[02_Core_Hartmann2016_Surface-Energy-Budget-and-Heat-Storage_pp96-101.pdf#page=2|pp. 97–98]], [[02_Core_Hartmann2016_Surface-Energy-Budget-and-Heat-Storage_pp96-101.pdf#page=5|p. 100]]; §7.3 p. 202* · <span class="scope-extra-beyond">extra · beyond</span> *model and checks*

The stored energy is a heat capacity times a temperature, $E=C_eT_e$ (4.3). **Atmosphere:** $C_a=c_pp_s/g=1004\times10^5/9.81\approx10^7$ J m⁻² K⁻¹; **ocean:** $\rho c_wd_w=4.2\times10^6\,d_w$ J m⁻² K⁻¹ per m of depth. So the **whole atmosphere equals a little over $2$ m of water** ($2.46$ m); the top $\sim70$ m of ocean that exchange heat with the air in a year hold about **$30$ times** the atmosphere's capacity ($28.5$), and the whole ocean ($3730$ m) $\sim1500$ times. **Land** has a much smaller effective capacity (heat reaches only the top 1–2 m by conduction, not by fluid motion; air in soil pores has almost no heat capacity, water in them a lot).

**Stewart's seasonal comparison:** ocean $100$ m, $\Delta t=10$ K: $4.0\times10^9$ J m⁻²; land $1$ m of rock ($3000$ kg m⁻³, $800$ J kg⁻¹ K⁻¹), $\Delta t=20$ K: $4.8\times10^7$ J m⁻²: ratio $\mathbf{83}$ (Stewart writes "$=100$": a rounding of the order of magnitude, `[!verify]`). Hence the seasonal air-temperature range on land grows with distance from the sea (over $40\,^\circ$C inland, $60$ in Siberia) and is under $10\,^\circ$C over oceans and coasts.

**Penetration depth into soil** (Hartmann 4.7–4.10): conduction $C_s\partial_tT=\partial_z(K_T\partial_zT)$, so with diffusivity $D_T=K_T/C_s$ the depth reached by a periodic signal of period $\tau$ scales as $\sqrt{D_T\tau}$. Hartmann quotes, for $D_T=5\times10^{-7}$ m² s⁻¹, **$\sim10$ cm (daily), $\sim1.5$ m (annual), $\sim150$ m for $10^4$ yr**. `[!verify]` The OCR prints $h=\sqrt{D_T\tau}$, which gives $0.21$, $4.0$, $397$ m; the three quoted depths are reproduced by $h=\sqrt{D_T\tau/2\pi}$: $0.083$, $1.58$, $158$ m (a factor $2\pi$ lost in the scan). Because conduction is so slow, horizontal heat transport under the land can be ignored in climate models. The diurnal soil-temperature figure (amplitude down to $e^{-1}$ at $\sim10$ cm) agrees.

**The damped slab** 🔵 (the interactive tool): $C\,dT/dt=Q_0\cos\omega t-\lambda T$ with $C=\rho c_wh$ gives the steady response $T=A\cos(\omega t-\phi)$, $A=Q_0/\sqrt{(C\omega)^2+\lambda^2}$, $\tan\phi=C\omega/\lambda$. With $Q_0=100$ W m⁻², $\lambda=20$ W m⁻² K⁻¹: $h=25$ m: $A=3.5$ K ($\phi=46^\circ$); $h=50$ m: $2.16$ K ($64.4^\circ$); $h=100$ m: $1.16$ K ($76.5^\circ$). *Without* damping, $A=Q_0/C\omega$ ($4.8$, $2.4$, $1.2$ K). The relaxation time of a 50 m layer is $C/\lambda=0.33$ yr. The ocean's thick, well-mixed layer is why the **sea-surface temperature lags the sun by a couple of months and varies by only a few kelvin**, and why a continent a thousand km from the sea has the climate it has ([[CL15 Monsoons]], [[CL17 Orbital Forcing and Glacial Cycles]] §4 continentality). *Hartmann Exercise 4.1* (a 100 m layer warming by 5 K in 3 months absorbs $267$ W m⁻²; the atmosphere warming by 20 K, $26$ W m⁻²) fixes the scale.

## 6. The mixed layer and the stratification
<span class="scope-taught">taught</span> *Hartmann §7.3: [[01_Core_Hartmann2016_The-Mixed-Layer_pp200-206.pdf#page=2|pp. 201–206]]; Neena L20 pp. 10–24*

> [!key] The mixed layer (Hartmann §7.3; Neena L20 pp. 18–24)
> The layer exchanging heat, momentum and moisture with the atmosphere. In it **turbulent mixing and convection are so efficient that temperature, salinity and other properties are almost independent of depth**. Its depth is set by the competition between **buoyancy** (cooling and evaporation → dense surface water → convection; heating and rain → light surface water → stratification) and **mechanical stirring** by wind and waves (which can entrain denser water from below, cooling and deepening the layer). **Global-average depth ≈ 70 m**; a few metres where subsurface water upwells (equator, eastern boundary currents) to the **whole ocean depth** in high-latitude regions where cold, saline water sinks to the bottom; regions deeper than 500 m are a small fraction of the area. It is thin where the ocean is heated and thick where it loses energy; its heat capacity is the effective heat capacity of the ocean on years to a decade.

**Seasonal cycle** (Hartmann Fig. 7.6; Neena L20 p. 24). Warmest and thinnest in **late summer**; as the surface cools and storminess rises it deepens and cools through winter, to **several hundred metres** by late winter, merging with the permanent thermocline; the rest of the year a **seasonal thermocline** links the permanent thermocline to the layer's base. Below the deepest mixed layer there is little seasonal change. In mid-latitudes the summer warm layer and shallow thermocline are **destroyed by convective mixing in winter** (Neena). A fresh summer cap over salty water means that in winter salt is mixed up, creating cold, salty, very dense water near the surface, "especially in the far North Atlantic": this is where **deep water forms** ([[CL21 Thermohaline Circulation Water Masses and Sea Ice]]); anomalies sealed under the summer cap can **re-emerge in winter**. The Southern Hemisphere layer stays deeper in summer because the strong westerlies persist.

**Stratification** (Neena L20 pp. 11–22):
- **Density** is a function of **temperature, salinity and pressure** (nonlinear); the upper $100$–$200$ m is well mixed (**mixed layer**), below it (to $\sim1$–$2$ km) density increases rapidly with depth: the **pycnocline** (the **thermocline** for temperature, **halocline** for salinity); below, density varies little.
- **Tropics**: strongly stratified and density controlled by temperature; **high latitudes**: no permanent thermocline (surface as cold as the deep ocean, $0$–$3\,^\circ$C below), density controlled by **salinity**.
- **Salinity** (33–38, from riverine input of weathered crustal salts) is set by **evaporation minus precipitation**: low at the ITCZ and in subpolar regions (frontal precipitation), **high under the subtropical highs** (cloud-free, $E>P$); highest in the Mediterranean and Red Sea; lowered by rivers (Bay of Bengal, Gulf of Alaska), glacier melt and sea ice. Conductivity measures it ([[CL16 Atmospheric Evolution Greenhouse Gases and the Carbon Cycle]] §5 for the water cycle).
- **Oceanic convection**: sinking when surface water becomes denser than the water below (cooling, or salinisation by evaporation); a **wind-stirred** layer reaches $\sim100$–$150$ m, **convective** mixing several hundred metres to $>1$ km, in cold regions and in winter.
- **Neena's question** ("difference between upper and deeper ocean temperature and salinity is largest in which region?"): the tropics for temperature (warm layer over cold deep water), where the thermocline is strong; the high latitudes have almost none.

## 7. Meridional heat transport
<span class="scope-taught">taught</span> *Stewart §5.7: [[02_Core_Stewart2008_Heat-Budget-Geography-and-Transport_pp65-70.pdf#page=5|pp. 68–70]]* · <span class="scope-extra-book">extra · book</span> *Hartmann Ch. 7: [[05_Optional_Hartmann2016_Ocean-Energy-Transport_pp227-231.pdf#page=3|pp. 229–231]]*

The Earth gains heat at the top of the tropical atmosphere and loses it at the top of the polar atmosphere, so ocean and atmosphere must carry heat **from low to high latitudes** ([[CL10 Global Energy Balance and Meridional Structure]] §4). The total is obtained from the **zonal-mean net flux at the top of the atmosphere** (measured by satellites) by integrating over latitude. **Trenberth and Caron (2001), as quoted by Stewart: the total annual-mean transport peaks at 6 PW towards each pole near 35°; the ocean carries 22 % of it in the northern and 8 % in the southern hemisphere at 35°** ($1.3$ and $0.5$ PW 🔵). Three ways to find the **oceanic** part: (1) the **surface-flux method** (integrate the heat flux through the sea surface), (2) the **direct method** (northward velocity times heat content along a zonal section), (3) the **residual method** (total minus the atmospheric transport from the atmosphere's own budget). The estimates agree within realistic error bars. Hartmann (optional): direct measurement is hard (full-depth sections, small scales), so the transport is inferred from budgets; the ocean maximum is in the **tropics (about 20°N)**, much smaller than the atmosphere's mid-latitude maximum, with a clear hemispheric asymmetry; **the Atlantic transports energy northward across the equator**. Neena L22 quotes $\sim10^{15}$ J s⁻¹ for the western boundary currents: *check* 🔵: $\rho c_p\Delta T\,V=1025\times3990\times10\times3\times10^7=1.2\times10^{15}$ W for a $30$ Sv flow with a $10$ K contrast ([[CL19 Wind-Driven Ocean Circulation]]).

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Why the ocean damps and delays the seasons: a slab mixed layer
> Take a mixed layer of depth h (heat capacity C = ρ c_w h per m², with ρ c_w = 4.2×10⁶ J m⁻³ K⁻¹) forced by a seasonal net surface heating Q₀ cos(ωt) and relaxed to equilibrium by a feedback λ: C dT/dt = Q₀ cos ωt − λT.
>
> ![[cl_slab_ocean.png|720]]
>
> **Try:** Q₀ = 100 W m⁻², λ = 20 W m⁻² K⁻¹, h = 50 m: amplitude 2.15 K and lag 64.5° (about 2.2 months after the heating peak). For h = 1 m of water (land-like) the amplitude is 5.0 K and the lag only 2.4°: the temperature follows the forcing. For h = 100 m the amplitude is 1.2 K and the lag is 76°.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_slab_ocean.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_slab_ocean.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL18 connects
> **Builds on:** [[CL10 Global Energy Balance and Meridional Structure]] (TOA budget, poleward transport), [[CL03 Radiation and Planetary Energy Balance]] (relaxation time, diurnal slab), [[CL06 Hydrostatic Balance and Vertical Structure]] (heat capacity $c_pp_s/g$), [[CL07 Optical Properties of the Atmosphere]] (Beer–Lambert).
> **Leads to:** [[CL19 Wind-Driven Ocean Circulation]] (the currents that carry the heat), [[CL20 ENSO and the Walker Circulation]], [[CL21 Thermohaline Circulation Water Masses and Sea Ice]].
> **Concepts:** [[Mixed Layer]] · [[Thermocline and Pycnocline]] · [[Sea Surface Energy Budget]] · [[Bulk Aerodynamic Formulas]] · [[Light Attenuation in the Ocean]] · [[Ocean Heat Capacity and Seasonal Storage]] · [[Seawater Salinity]]
> **Other subjects:** [[Thermodynamics and Statistical Mechanics - Course Map]] ([[TH07 Enthalpy Thermochemistry and Calorimetry]]: heat capacity and latent heat; [[THX1 Diffusion Random Walks and the Heat Equation]]: soil conduction and the $\sqrt{D\tau}$ penetration depth), [[Landscapes and Geomorphology - Course Map]] ([[LS25 Water in the Landscape]], [[LS26 Sea Level and Ocean Waves]]), [[Eco-Evo - Course Map]] ([[EE06 Lakes Stratification and Alternative Stable States]]: stratified water bodies, light and the mixed layer), [[Waves - Course Map]], [[Probability - Course Map]] (error budgets).

## Summary
> [!summary] Cheat-sheet
> - **Surface balance:** $\partial E_s/\partial t=R_s-LE-SH-\Delta F_o$; global means (Stewart Fig. 5.6): $168+324=390+78+24=492$ W m⁻²; latent loss is the biggest cooling; rain heats the atmosphere ($\sim125$ W m⁻²).
> - **Light:** 2 % reflected; $I=I_0e^{-cz}$; type I water 10 % at 90 m (1 % at 180 m); broadband flux halves in ~1 m; IR in the top cm; euphotic zone ~200 m.
> - **Geography:** net radiation peaks in the tropics; latent mirrors insolation, peaks over western boundary currents ($>200$ W m⁻²); sensible small except over them (annual mean $>50$); ocean gains at the equator and eastern margins (upwelling), loses at high latitudes and western boundary currents.
> - **Bulk formulas:** $\tau=\rho_aC_DU^2$, $Q_S=\rho_ac_pC_SU\Delta t$, $Q_L=\rho_aL_EC_LU\Delta q$; $C_L=1.2\times10^{-3}$, $C_S=1.0\times10^{-3}$.
> - **Storage:** atmosphere = 2.46 m of water; top 70 m of ocean = 28.5 atmospheres; ocean/land seasonal storage ≈ 83–100; damped slab: amplitude $Q_0/\sqrt{(C\omega)^2+\lambda^2}$, lag $\arctan(C\omega/\lambda)$.
> - **Mixed layer** ≈ 70 m global mean, thin where heated, deep where cooled; thermocline/pycnocline below; high latitudes salinity-controlled; salinity = $E-P$ + rivers + ice; deep formation where winter mixing reaches cold, salty water.
> - **Heat transport:** total 6 PW at 35°; ocean 22 % (N), 8 % (S); ocean maximum near 20°N; ~$10^{15}$ W in the western boundary currents.

## Practice
1. **Light.** In type I water 10 % of 465 nm light reaches 90 m. Find $c$, the depth of the 1 % level and the fraction left at 30 m. Compare with the lecture's euphotic zone.
2. **Heat capacity.** Compute $C_a=c_pp_s/g$ and express it as metres of water; find the ratio of the top 70 m of ocean to the atmosphere.
3. **Hartmann Exercise 4.1.** A 100 m layer warms by 5 K in 3 months; the atmosphere warms by 20 K. Find the mean net heating rates.
4. **Seasonal storage.** Reproduce Stewart's ocean/land ratio ($100$ m, $10$ K vs 1 m of rock, $20$ K) and say whether "100" is right.
5. **Bulk formulas.** $U_{10}=8$ m/s, $t_s=27$ °C, $t_a=25$ °C, RH $=80$ %: find $Q_S$ and $Q_L$ (take $q_s=0.0222$, $q_a=0.0157$). Why are they larger than Stewart's annual-mean ranges?
6. **Budget check.** Verify that the surface and atmosphere columns of Stewart Fig. 5.6 balance, and that the OLR is $165+30+40$.
7. **Slab.** For $Q_0=100$ W m⁻², $\lambda=20$: find the amplitude and lag for $h=25$, $100$ m and the relaxation time of a 50 m layer.
8. **Heat transport.** The total transport peaks at 6 PW at 35°; the ocean carries 22 % (N) and 8 % (S): find both. A 30 Sv current with a 10 K temperature contrast carries how much?
9. **Soil.** With $D_T=5\times10^{-7}$ m² s⁻¹ compute $\sqrt{D_T\tau/2\pi}$ for one day, one year and $10^4$ yr; compare with $\sqrt{D_T\tau}$.
10. **Concept.** Why does high-latitude stratification depend on salinity rather than temperature, and why can a thin summer mixed layer "seal" a winter anomaly?

> [!example]- Solutions
> 1. $c=\ln10/90=0.0256$ m⁻¹; $1\,\%$ at $\ln100/c=180$ m; at 30 m $e^{-0.768}=0.464$ (46 %); the euphotic zone ($\sim$1 % level) is $\sim180$–$200$ m.
> 2. $C_a=1.04\times10^7$ J m⁻² K⁻¹ $=2.46$ m of water ($\rho c_w=4.218\times10^6$ J m⁻³ K⁻¹); $70\times4.218\times10^6=2.95\times10^8$: $28.5\times$.
> 3. $\dfrac{100\times4.2\times10^6\times5}{0.25\times3.156\times10^7}=267$ W m⁻²; atmosphere $\dfrac{1.04\times10^7\times20}{7.89\times10^6}=26.3$ W m⁻².
> 4. $\dfrac{4000\times10^5\times10}{800\times3000\times20}=\dfrac{4.0\times10^9}{4.8\times10^7}=83$: "100" is a rounding of the order of magnitude.
> 5. $Q_S=1.3\times1030\times10^{-3}\times8\times2=21.4$ W m⁻²; $Q_L=1.3\times2.5\times10^6\times1.2\times10^{-3}\times8\times(0.0222-0.0157)=201$ W m⁻²; instantaneous trade-wind values at 8 m/s exceed annual means (which average over calms, humid periods and all latitudes).
> 6. $168+324=492=390+78+24$; $67+78+24+350=519=165+30+324$; $235=165+30+40$; $342=107+235$.
> 7. $h=25$: $C\omega=20.9$, $A=100/\sqrt{20.9^2+400}=3.5$ K, $\phi=\arctan(20.9/20)=46^\circ$; $h=100$: $A=1.16$ K, $\phi=76.5^\circ$; relaxation time $C/\lambda=2.1\times10^8/20=1.05\times10^7$ s $=0.33$ yr.
> 8. $0.22\times6=1.3$ PW (N), $0.08\times6=0.5$ PW (S); $1025\times3990\times10\times3\times10^7=1.2\times10^{15}$ W.
> 9. $0.083$, $1.58$, $158$ m vs $0.21$, $4.0$, $397$ m: Hartmann's depths agree with the $2\pi$ form.
> 10. Near freezing the thermal expansion coefficient is small, so $T$ differences hardly change the density, whereas salinity differences do; a thin warm and fresh summer layer is so light that winter-cooling signals below it are not mixed up until the layer is eroded in autumn.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | solar absorption, surface heat balance, SST, composition, E−P, density stratification, pycnocline, convection, mid-latitude cycle, western boundary currents ($10^{15}$ W) | [[Lecture20_Ocean_stratification_251113_133828 (1).pdf]] pp. 2–24; [[Lecture22_Ocean_wind_driven_circulation-2_251113_133827 (1).pdf]] p. 15; L7 for the percentage budget | taught (2025) |
> | light in the ocean (reflectivity, Beer–Lambert, water types, chlorophyll) | [[01_Core_Stewart2008_Light-in-the-Ocean_pp97-100.pdf]] (Core; read) | taught (2026, Joy) |
> | surface energy budget, heat storage, soil penetration, radiative heating | [[02_Core_Hartmann2016_Surface-Energy-Budget-and-Heat-Storage_pp96-101.pdf]] (Core; OCR garbled equations) | taught (2026) |
> | geographic variation of the surface balance | [[03_Core_Hartmann2016_Geographic-Variation-of-the-Surface-Energy-Balance_pp126-129.pdf]] (Core) | taught (2026) |
> | the mixed layer | [[01_Core_Hartmann2016_The-Mixed-Layer_pp200-206.pdf]] (Core) | taught (2026) |
> | budget figure, geography of terms, meridional heat transport | [[02_Core_Stewart2008_Heat-Budget-Geography-and-Transport_pp65-70.pdf]] (Core; also the O1 optional copy) | taught (2026) |
> | bulk formulas, measurement, seasonal storage | [[05_Optional_Stewart2008_Heat-Budget-Terms-and-Bulk-Formulas_pp53-61.pdf]] (Optional) | extra/book |
> | world ocean; ocean energy transport | [[03_Optional_Hartmann2016_The-World-Ocean_pp17-19.pdf]], [[05_Optional_Hartmann2016_Ocean-Energy-Transport_pp227-231.pdf]] (Optional; the second read in part) | extra/book |
> | attenuation numbers, bulk examples, slab model, penetration-depth factor, transport check | `scripts/cl_neena_numbers.py` (cl18), `scripts/fig_cl16_21.py`, tool `cl_slab_ocean` | extra/beyond |
>
> **Notes.** [!verify] Stewart's "ratio = 100" is 83; Hartmann's (4.10) printed without its $1/2\pi$ (the quoted depths fix the factor); the Hartmann equations (4.1)–(4.9) are read through garbled OCR. The O1 core reading (Hartmann pp. 40–48) and the optional angular-momentum pages (pp. 176–180) were **not re-read** for this chapter (CL10, CL11 already cover that content from Suhas and Marshall–Plumb). Tetens saturation humidity and the damped-slab form are my additions.
