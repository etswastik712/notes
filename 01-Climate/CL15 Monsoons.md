---
title: CL15 Monsoons
aliases: [CL15, Monsoon dynamics, Indian monsoon]
subject: climate
type: chapter
chapter: 15
part: IV
scope: [taught, extra-book, extra-beyond]
by: [suhas-post]
status: draft
prereq: ["[[CL14 Observed Winds - Jets, Trades and the ITCZ]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-post, status/draft]
---
# CL15 · Monsoons

◀ [[CL14 Observed Winds - Jets, Trades and the ITCZ]] · [[Climate - Course Map|Course Map]] · (last chapter of the course map)

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!note] Neena 2025 cross-reference (2026-11-13)
> The 2025 course (Neena) covered this ground too: Neena 2025 **L18–L19** (atmospheric general circulation) for the circulation background (`earth-and-climate/climate/lecture-notes-slides/ec2113_neena`, PDFs listed in [[Climate - Course Map]]). This chapter is built from **this year's** Argha/Suhas material, which stays primary here. In the earlier new-source comparison (PROGRESS, 2026-11-07) those lectures were judged to **repeat** this chapter's content; **no Neena-specific content has been added to this chapter** beyond this pointer, and it has **not been re-read line by line** for differences (L18-L19). Where a Neena lecture was found to add material, it is added and labelled in the chapter that needed it (for example CL10 §7).

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 seasonal wind reversal and the five monsoon systems (Suhas 22 Oct p25–26, 30–31; 21 Oct p17–19)
> - §2 Indian rainfall maps, west coast / Meghalaya / Burma coast, orography, annual cycle (22 Oct p27–29)
> - §3 the warm-column / cold-column sketches with H and L (22 Oct p34–36)
> - §4 "how do we explain the cross-equatorial flow?": pressure gradient (PG), Coriolis (C) and friction (F) in the non-rotating vs rotating panels, lower and upper troposphere (22 Oct p32–33, 36–40)
>
> 🟡 **Extra · book**
> - Webster & Fasullo (2003): Halley/Hadley history, specific-heat numbers, slab equations [1]–[3], hydrostatic column Eqs. [4]–[6] and the onset threshold, moisture transport Eq. [7] and the "solar collector", Eqs. [8]–[10], easterly jet, thermal wind, Somali jet, Tibetan Plateau, ocean heat transport, ENSO (in §§3–5, 7)
> - Hartmann §6.5.1–6.5.4: land–sea pressure contrast, monsoonal climates, deserts, wet climates, Sahel, Figs. 6.19–6.25 (in §§1, 2, 6)
>
> 🔵 **Extra · beyond**
> - slab-model amplitudes and lags, numbers for the column argument, explicit steady cross-equatorial solution, orographic rain-rate estimate, latent heating in W m⁻², Rossby-number comparison, regime-shift view of the Sahel (in §§2–5, 8)

> [!key] After this chapter you can
> - define a monsoon, name the main systems, and describe the Indian monsoon's rainfall pattern and annual cycle,
> - explain, with hydrostatic balance, why a warm land column gives **low pressure at the surface and high pressure aloft**, and why land and sea heat so differently,
> - explain why a monsoon crosses the equator: draw and explain the **PG–C–F balance** on a non-rotating and a rotating planet, in the lower and upper troposphere,
> - say what orography, moisture (latent heating) and the Tibetan Plateau add, and why the monsoon rains fall poleward of the ITCZ.

## 1. What is a monsoon?
<span class="scope-taught">taught</span> *Suhas 22 Oct p25–26, 30–31; 21 Oct p17–19* · <span class="scope-extra-book">extra · book</span> *Webster & Fasullo p.151; Hartmann §6.5.1, p.183*

The word comes from the Arabic *mausim*, "season". A **monsoon** is a regular **seasonal change in wind speed and direction**, accompanied by a shift between very dry and very rainy conditions ([[22nd Oct.pdf#page=25|22 Oct p25]]: "seasonal variations in the wind speed and direction"). The slide lists the systems: **South Asian (Indian), Australian, North American, South American and African** monsoons ([[22nd Oct.pdf#page=26|p26]]), and shows the 850 hPa winds, 200 hPa streamlines and outgoing longwave radiation (a convection proxy) for each ([[22nd Oct.pdf#page=30|p30–31]]; the clean copy is [[22nd Oct CliSci slides.pdf#page=31|CliSci p31]]). The same pattern appears on the 850 hPa map shown on 21 Oct ([[21st Oct.pdf#page=19|p19]], "monsoon winds").

> [!intuition] A sea breeze with a seasonal clock
> On a sunny afternoon the land warms faster than the sea, the air above it rises, and a cool breeze blows in from the sea: a **sea breeze**. At night it reverses. A monsoon is the same idea stretched out: the *continent* warms for a whole summer, the air is drawn in from the *ocean* for months, and because the inflow has travelled thousands of kilometres over warm water it arrives loaded with vapour, enough to rain for a season. Two things must be added to the sea-breeze picture: **rotation** (the scale is too big to ignore it, §4) and **moisture** (the latent heat of the rain becomes the engine, §5).

> [!example] Why rotation matters for a monsoon but hardly for a sea breeze 🔵
> The Rossby number $\mathrm{Ro}=U/(fL)$ ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]]) compares the acceleration with the Coriolis term. Sea breeze at 30° N: $U=5$ m s⁻¹, $L=30$ km, $f=7.3\times10^{-5}$ s⁻¹: $\mathrm{Ro}\approx2.3$, rotation is weak. Monsoon at 15° N: $U=10$ m s⁻¹, $L=3000$ km, $f=3.8\times10^{-5}$ s⁻¹: $\mathrm{Ro}\approx0.09\ll1$: rotation dominates the large-scale flow, **except** right at the equator where $f\to0$.

**Features of a monsoon** (Webster & Fasullo 2003, [[Dynamical_theory_of_Monsoon_Webster.pdf#page=1|p.151]]):
- In summer, **low-level winds blow towards the heated continent**, away from the cooler ocean of the winter hemisphere; in the **upper troposphere the flow is reversed**.
- Rain is concentrated in a low-pressure **monsoon trough** over the continents and adjacent seas, mostly in synoptic disturbances grouped into **active periods** of 10–30 days, separated by **breaks**.
- The monsoon trough lies **well poleward of the oceanic [[Intertropical Convergence Zone]]**; South Asian monsoon rain falls at the same latitudes as the planet's great deserts.
- **Systems:** the Asian–Australian monsoon, the West African monsoon and the American monsoons. The North and South American monsoons are nearly separate (no clear cross-equatorial part). Equatorial land (Amazon, Congo, Indonesia) has *two* rainfall maxima at the equinoxes and is not strictly monsoonal: a monsoon has **one solstitial maximum**.

| system | where | notes (Webster & Fasullo) |
|---|---|---|
| Asian–Australian | India–SE Asia and N Australia | strongest, truly **interhemispheric** moisture source |
| West African | Gulf of Guinea → Sahel | weaker, coastal belt, limited northward by the easterly-jet secondary circulation (§7) |
| North American | Mexico–SW USA | weak, no clear cross-equatorial part |
| South American | Amazon basin to the subtropics | weak, nearly separate from the northern one |

> [!extra-book]+ 🟡 Extra (book): Hartmann on the pressure pattern behind it
> Hartmann (§6.5, [[Large-scale_patterns_Hartmann.pdf#page=3|pp.182–183]]) starts from the **land–sea pressure contrast**: in January high pressure sits over Asia and the lows over the high-latitude oceans (Aleutian, Icelandic); in July the contrast reverses and the dominant low in the Northern Hemisphere is centred over Asia at ≈ 30° N, associated with the **Asian summer monsoon**. He attributes this to the seasonal cycle of insolation and to the different response of land and ocean: ocean heating is spread through a deep layer and consumed by evaporation, while land "warms up dramatically in summer and cools in winter" ([[CL10 Global Energy Balance and Meridional Structure]], [[Insolation]]).

## 2. The Indian monsoon: rain, orography and the annual cycle
<span class="scope-taught">taught</span> *Suhas 22 Oct p27–29* · <span class="scope-extra-book">extra · book</span> *Hartmann pp.183–184 & Fig. 6.21; Webster & Fasullo p.156* · <span class="scope-extra-beyond">extra · beyond</span> *rain-rate estimate derived here*

**What the slides show.** January and July maps of precipitation (mm per month) with winds over South Asia ([[22nd Oct.pdf#page=27|p27]]; Hartmann's version is Fig. 6.21, [[Large-scale_patterns_Hartmann.pdf#page=6|p.185]]). Text on the slide: the **west coast of India, north-east India (Meghalaya) and the west coast of Burma** receive large amounts of precipitation. Next slide ([[22nd Oct.pdf#page=28|p28]]): "regional distribution of monsoon precipitation is strongly influenced by **orography**" (relief map of the Himalaya, Western Ghats and Burma ranges, and a schematic of air rising over a mountain). Then the **annual cycle of rainfall over India** ([[22nd Oct.pdf#page=29|p29]]): a bar chart with a single, bell-shaped maximum in mid-summer (July–August) and very little rain in winter.

In winter the situation reverses: the Himalaya cool dramatically, air flows from land to the Indian Ocean at low levels, and India has a dry season (Hartmann p.183). The switch from dry to wet is **abrupt**, at monsoon onset, typically around the middle of June in Hartmann's account; the date of onset, the intensity and duration of the rains vary from year to year and decide flood or drought (p.184).

> [!verify] When does the monsoon "start"?
> Hartmann says onset is "typically around the middle of June"; Webster & Fasullo (p.154) say "late May or early June" for the sudden onset over South Asia. The difference is largely *where* onset is defined: the operational onset over the southern tip (Kerala) is about 1 June, and the rains reach central and north-west India weeks later (India Meteorological Department normals; `[verify]` the current dates before quoting them in an exam answer).

### Orographic precipitation
Monsoon air arrives at the coast warm and moist, and the mountains force it **up**. Rising air expands and cools: at the dry adiabatic rate $\Gamma_d=g/c_p\approx9.8$ K km⁻¹ ([[Dry Adiabatic Lapse Rate]]) until it is saturated, at the **lifting condensation level** $z_{\rm LCL}\approx125\ \mathrm{m\,K^{-1}}\times(T-T_d)$; above it the parcel cools more slowly, along the **moist adiabat**, and the vapour in excess of saturation condenses ([[Clausius-Clapeyron Relation]], [[Atmospheric Stability]]). On the lee side the air descends, warms and dries: a **rain shadow** (Hartmann p.186: the Gobi, the Patagonian desert, the Deccan interior).

> [!intuition] The wet sponge
> Squeeze a wet sponge and water comes out. Lifting air over a mountain "squeezes" it: the lower the temperature, the less vapour it can hold ([[Clausius-Clapeyron Relation]]: ≈ 7 % less per kelvin), so the excess has to leave as cloud droplets and rain. Once the air has gone over the top it is a dry sponge: the lee side stays dry.

> [!example] Worked example 🔵: how much rain from a mountain wall?
> Take boundary-layer air at $T=27$ °C, $p=1000$ hPa, RH $=85$ %: mixing ratio $q_0=19.5$ g kg⁻¹, dew point 24.3 °C, so $z_{\rm LCL}\approx125\times(27-24.3)=340$ m (the parcel calculation in `fig_cl15_orographic.py` gives 340 m ✓).
> Lift it by $h$ and let all the extra vapour fall out. The condensed amount is $\Delta q=q_0-q_{\rm sat}(h)$:
> | lift $h$ | parcel $T$ | condensed $\Delta q$ | rain rate $P$ |
> |---|---|---|---|
> | 500 m | 23.1 °C | 0.41 g kg⁻¹ | 12 mm day⁻¹ |
> | 1000 m | 21.1 °C | 1.58 g kg⁻¹ | 45 mm day⁻¹ |
> | 1500 m | 19.1 °C | 2.74 g kg⁻¹ | 78 mm day⁻¹ |
> | 2000 m | 17.1 °C | 3.88 g kg⁻¹ | 111 mm day⁻¹ |
>
> The rain rate assumes a layer of depth $D=1500$ m moving at $U=10$ m s⁻¹ over a windward slope of length $L=50$ km: $P=\rho U D\,\Delta q/L$ (kg m⁻² s⁻¹, ×86 400 for mm per day). At 1000 m: $1.1\times10\times1500\times1.58\times10^{-3}/(5\times10^{4})=5.2\times10^{-4}$ kg m⁻² s⁻¹ $=45$ mm day⁻¹. This is an **upper bound** (no evaporation, perfect efficiency), but it shows why the windward slopes of the Western Ghats and Meghalaya, a metre or more of lift, receive metres of rain in a season. The rain rate is linear in the wind speed ($U$ doubled gives twice the rain), and zero below the condensation level.

![[fig_cl15_orographic.png|860]]
*Figure CL15.1. Left: the parcel cools along the dry adiabat to the condensation level (340 m) and then more slowly along the moist adiabat. Middle: its water vapour is constant until then, then decreases. Right: the resulting windward-slope rain rate. See: the rain rate is zero below 340 m and rises steadily with the lift (script `fig_cl15_orographic.py`; illustrative parcel numbers, not observations).*

> [!extra-book]+ 🟡 Extra (book): Webster & Fasullo on the dry-to-wet transition over land
> When the rains arrive the land surface moistens and its temperature **falls**: the daily maximum at New Delhi often exceeds 45 °C before onset and drops to 30–32 °C in active rainy periods (p.156); winds strengthen at the same time. This looks like a negative feedback, but the stronger winds import so much more water vapour that the latent heating takes over as the driver (§5).

## 3. Why a land–sea contrast drives a circulation
<span class="scope-taught">taught</span> *Suhas 22 Oct p34–36 (hand-drawn sketches of land and ocean and of warm and cold air columns with H and L, then Webster's cross-section)* · <span class="scope-extra-book">extra · book</span> *Webster & Fasullo pp.151–156: Eqs. [1]–[6]* · <span class="scope-extra-beyond">extra · beyond</span> *slab solution, numbers*

Suhas's explanation on 22 Oct is qualitative and drawn by hand: a Sun over a continent next to an ocean ([[22nd Oct.pdf#page=34|p34]]); then **a "warmer air column" and a "colder air column" with H and L labels**, and arrows closing the loop ([[22nd Oct.pdf#page=35|p35]]); then Webster's schematic of the moist monsoon circulation ([[22nd Oct.pdf#page=36|p36]], with cold (C) and warm (W) air columns and the dashed constant-pressure surfaces tilting upward to the north aloft). The rest of this section supplies the physics and the numbers behind those sketches.

### 3.1 Why land warms and cools more than the ocean
<span class="scope-extra-book">extra · book</span> *Webster & Fasullo p.151–152* · <span class="scope-extra-beyond">extra · beyond</span> *slab solution*

The surface layer heats according to the flux divergence in it (Webster Eq. [1]):
$$\frac{\mathrm dT}{\mathrm dt}=-\frac{1}{\rho c_p}\frac{\mathrm dF}{\mathrm dz}\approx\frac{F_{z=0}}{\rho c_p\,\Delta z},$$
with the surface flux $F_{z=0}=I_{\rm net}-H_s-H_e$ (net radiation minus sensible and latent heat loss; Eqs. [2]–[3]). Two factors make land respond more: the **specific heat** is lower (dry land ≈ 1300 vs 4218 J kg⁻¹ K⁻¹ for water: a factor ≈ 3–4), and above all the **active depth** $\Delta z$ is tiny: the soil is opaque and conducts heat slowly, so the seasonal signal reaches only about **1 m**, whereas sunlight penetrates the ocean to an e-folding depth of ≈ 10 m and wind mixing spreads the heat deeper. Dry land even has the higher albedo (20–40 % vs ≈ 10 %), yet still warms faster (Halley, 1686, was the first to propose this as the cause of monsoons).

> [!derivation]- Seasonal response of a slab (periodic steady state)
> Let $T$ be the departure from the annual mean, $C=\rho c_p\Delta z$ the heat capacity per unit area, $\lambda=4\varepsilon\sigma T_0^3\approx3.3$ W m⁻² K⁻¹ the linearised loss ([[Planck Sensitivity]], with $\varepsilon=0.6$, $T_0=289$ K) and $F_0\cos\omega(t-t_s)$ the seasonal forcing (maximum at the solstice $t_s$):
> $$C\frac{\mathrm dT}{\mathrm dt}=F_0\cos\omega(t-t_s)-\lambda T.$$
> Write $T=\mathrm{Re}\,[\hat T e^{i\omega(t-t_s)}]$: $i\omega C\hat T=F_0-\lambda\hat T$, so
> $$\hat T=\frac{F_0}{\lambda+i\omega C},\qquad |\hat T|=\frac{F_0}{\sqrt{\lambda^2+(\omega C)^2}},\qquad\text{lag }\varphi/\omega,\ \ \varphi=\arctan\frac{\omega C}{\lambda}.$$
> For $\omega C\gg\lambda$ the lag tends to a **quarter period** and the amplitude to $F_0/\omega C$ (Webster's "lagging by a quarter period"); for $\omega C\ll\lambda$ the slab follows the forcing at once with amplitude $F_0/\lambda$. The time constant is $\tau=C/\lambda$ ([[Relaxation Time]], [[CL03 Radiation and Planetary Energy Balance]]).

| layer | $C$ (J m⁻² K⁻¹) | $\tau=C/\lambda$ | amplitude for $F_0=50$ W m⁻² | lag |
|---|---|---|---|---|
| dry land, 1 m | $2.0\times10^{6}$ | 6.9 days | **15.1 K** | 7 days |
| ocean, 10 m | $4.3\times10^{7}$ | 152 days | 5.4 K | 70 days |
| ocean, 50 m | $2.2\times10^{8}$ | 2.1 years | **1.2 K** | 87 days |

![[fig_cl15_slab.png|860]]
*Figure CL15.2. Land and ocean slabs forced by the same seasonal flux ($F_0=50$ W m⁻², illustrative, not a measurement; only the ratios matter). See: land (orange) follows the Sun within a week; the 50 m ocean (blue) barely changes and lags by almost a quarter year. Script `fig_cl15_slab.py`.*

> [!intuition] A thimble and a swimming pool
> Put the same heater under a thimble of water and under a swimming pool. The thimble warms at once and cools at once; the pool hardly changes in a day and peaks long after the heater is turned down. Land is the thimble (1 m), the ocean the pool (tens of metres). So by May the continent is already hot while the sea is still cool: there is a **temperature difference exactly when the Sun moves north**. In winter the contrast reverses.

> [!pitfall] A 10 m ocean is too responsive
> Webster notes that using the 10 m e-folding depth gives ocean temperature variations much larger than observed (our 5.4 K vs the observed 1–2 K); realistic amplitudes need a **deeper active layer** (here 50 m gives 1.2 K) because the ocean mixes and transports heat (§7).

### 3.2 A warm column is a tall column: high pressure aloft, low pressure below
<span class="scope-taught">taught</span> *the sketch of warm and cold air columns with H and L, 22 Oct p35* · <span class="scope-extra-book">extra · book</span> *Webster & Fasullo p.154, Eqs. [4]–[6]* · <span class="scope-extra-beyond">extra · beyond</span> *numbers*

**Hydrostatic balance** plus the ideal gas law (CL05, CL06) give $\partial p/\partial z=-\rho g=-pg/RT$, i.e. Webster's Eq. [4]

$$\frac{\partial\ln p}{\partial z}=-\frac{g}{RT}.$$

The rate at which pressure falls with height is **inversely proportional to the column temperature**: in warm air pressure falls more slowly. Integrate from the surface to $z_1$ for a mean column temperature $\bar T$: $p(z_1)=p(0)\,e^{-gz_1/R\bar T}$ ([[CL06 Hydrostatic Balance and Vertical Structure]]; the scale height $H=R\bar T/g$ is 7.76 km for 265 K and 8.05 km for 275 K: the warm column is 4 % "taller"). The difference between the warm (land, $T_w$) and cold (ocean, $T_c$) columns at height $z_1$ is Webster's Eq. [5]

$$\boxed{\Delta\ln p(z_1)=\frac{g\,z_1}{R}\Big(\frac{1}{T_c}-\frac{1}{T_w}\Big)+\Delta\ln p(0)}\tag{CL15.1}$$

where $\Delta$ means (warm column) − (cold column) on a **constant-height** surface. If the surface pressures are equal, $\Delta\ln p(0)=0$, and for $T_w>T_c$ the warm column has the **higher pressure at every height above the ground**.

![[fig_cl15_columns.png|880]]
*Figure CL15.3. Left: two columns with equal surface pressure, 265 K and 275 K. Middle: pressure difference vs height for ΔT = 3, 6, 10 K (maximum 4.1, 8.2, 13.6 hPa at about 8 km). Right: the height above which the gradient is reversed when the warm column has a surface low (Eq. CL15.2). Script `fig_cl15_columns.py`.*

> [!intuition] Two stacks of bricks and a spring
> Imagine two columns of air, each holding the same weight at the bottom. Heat one: it expands, its upper layers rise (it is a *taller* column), and at any fixed height there is *more* air above that level in the warm column than in the cold one, so the pressure there is higher. Air aloft is pushed from the warm column towards the cold one. That removes mass from the warm column, so its **surface pressure falls**: a thermal low. Down below the surface pressure gradient points the other way, and air flows from the cold ocean into the warm land ("low pressure draws the air in"). This is exactly the hand-drawn picture: **L at the surface and H aloft over the warm column**.

> [!example] Worked example 🔵: how big is the pressure difference aloft?
> $T_c=265$ K, $T_w=275$ K, equal surface pressure, $z_1=10$ km:
> $\Delta\ln p=\dfrac{9.81\times10^4}{287}\Big(\dfrac1{265}-\dfrac1{275}\Big)=341.8\times1.372\times10^{-4}=0.0469$, so $p_w/p_c=e^{0.0469}=1.048$. With $p_c(10\ \mathrm{km})=275$ hPa the warm column has $p_w=289$ hPa: **13 hPa more**, in the sense that sends air from land to sea aloft.

**But the surface low undoes some of this.** Over the heated continent the surface pressure falls (by up to ≈ 20 hPa relative to the winter-hemisphere subtropics, Webster p.154), so $\Delta\ln p(0)<0$ and the sign of $\Delta\ln p(z_1)$ is no longer obvious. Setting (CL15.1) to zero gives the height above which the upper-level gradient is **reversed**:

$$z^*=-\frac{R\,\Delta\ln p(0)}{g\,(1/T_c-1/T_w)}\ \ (\text{Webster's Eq. [6] rearranged}),\qquad T_w>\frac{g z_1T_c}{g z_1+R\,\Delta\ln p(0)\,T_c}.\tag{CL15.2}$$

For $T_c=265$ K, $T_w=275$ K and a surface low of 10 hPa ($\Delta\ln p(0)=-0.0100$): $z^*=287\times0.0100/(9.81\times1.372\times10^{-4})=2.1$ km. With a 20 hPa low it is 4.3 km; to bring $z^*$ down to the mid-troposphere (5.5 km) with a 10 hPa low needs only $\Delta T=3.8$ K.

> [!extra-book]+ 🟡 Extra (book): a threshold, and the sudden onset
> Webster & Fasullo point out that (CL15.2) is a **threshold**: until the mean temperature of the warm column exceeds that of the cold column by enough, there is no reversed gradient aloft and no deep circulation. They suggest this may explain the **sudden onset** of the South Asian monsoon in late May or early June, when deep convection and heavy rain begin (p.154). In their Fig. 2 (panels (i) circulation, (ii) temperature profiles, (iii) mass distribution in the columns, (iv) pressure vs height) the dry and the moist cases are compared; the moist monsoon fills the whole troposphere (§5).

### 3.3 The dry monsoon loop and its size
<span class="scope-extra-book">extra · book</span> *Webster & Fasullo p.154* · <span class="scope-extra-beyond">extra · beyond</span> *worked example*

Once the gradient is reversed aloft the circulation is **thermally direct**: surface air flows cold → warm, rises over the heat source, flows warm → cold aloft, and sinks over the ocean, the same overturning as the [[Hadley Cell]] but seasonal and longitudinally localised (compare [[CL11 Mean Meridional Circulation and Angular Momentum]]). In steady state the heat gained at the surface must be radiated to space. The **horizontal scale** is the distance an upper-level parcel travels before it has radiated away its excess heat; radiative damping is slow (e-folding ≈ 20 days). For a parcel speed of 1 m s⁻¹ that is $1\times20\times86400\approx1.7\times10^{3}$ km; at 10 m s⁻¹ it is 17,000 km, longer than a hemisphere, so upper-level air crosses the whole basin before it cools. The efficiency of radiation therefore sets the *longitudinal extent* of the monsoon.

![[Monsoon Circulation Loop.svg|640]]
*Figure CL15.4. The monsoon as a land–sea circulation loop (static copy; editable version [[Monsoon Circulation Loop.excalidraw]]). See: the heating contrast sets a pressure contrast, which drives the loop; moisture imported at low levels returns as latent heat aloft (§5).*

## 4. Crossing the equator: rotation and friction
<span class="scope-taught">taught</span> *Suhas 22 Oct p32–33, 36–40 (the PG–C–F panels, lower and upper troposphere; hand-drawn hemisphere sketch)* · <span class="scope-extra-book">extra · book</span> *Webster & Fasullo pp.157–158, Eqs. [8]–[10]* · <span class="scope-extra-beyond">extra · beyond</span> *explicit steady solution and numbers*

**The question** ([[22nd Oct.pdf#page=32|p32–33]], over a 3-D relief map of South Asia with winds): *how do we explain the cross-equatorial flow over South Asia during the monsoon?* In northern summer the low pressure is over the heated continent (north of the equator) and high pressure over the cool subtropical Indian Ocean in the south. A flow from the southern high to the northern low must **cross the equator**. But with rotation we normally expect flow **along** the isobars (geostrophic balance, [[CL13 Horizontal Motion - Geostrophic Balance and Friction]]), and near the equator $f=2\Omega\sin\varphi\to0$ so geostrophy cannot hold. What decides the flow there? Answer: the balance of **pressure gradient (PG), Coriolis force (C) and friction (F)**.

### 4.1 The force-balance panels
The slides reproduce Webster's Fig. 5 ([[22nd Oct.pdf#page=37|p37]] lower troposphere, [[22nd Oct.pdf#page=38|p38]] a zoom, [[22nd Oct.pdf#page=39|p39]] upper troposphere). Each has two columns: **(i) non-rotating** and **(ii) rotating** planet, with a constant pressure gradient in latitude, Coriolis effects (C) and friction (F) proportional to the speed, drawn at several latitudes between 30° S and 30° N ($p_0\dots p_4$ label the isobars).

- **Lower troposphere, non-rotating** (i): the pressure gradient PG points north (from high pressure in the south to low pressure in the north) and friction F opposes the motion, so the steady balance $\mathrm{PG}=\mathrm F$ gives a flow **straight down the gradient** (northward) at every latitude, crossing the equator without a kink (Webster Eq. [9]).
- **Lower troposphere, rotating** (ii): at each latitude PG, C and F must sum to zero. C is perpendicular to the wind (to its **right** in the Northern Hemisphere, to its **left** in the Southern), F is opposite to the wind, so the wind must cross the isobars from high to low pressure at an angle. At the equator C vanishes and the flow is again along the gradient. The flow therefore **diverges out of the winter-hemisphere anticyclone, crosses the equator, and converges into the continental low**; the broad arrows on the figure show the integrated Ekman mass transport in the boundary layer.
- **Upper troposphere** ([[22nd Oct.pdf#page=39|p39]]): the pressure gradient is **reversed** (high pressure to the north, low to the south) and friction is an order of magnitude weaker, so the flow is much closer to geostrophic: C nearly balances PG, and F only slightly deflects the flow across the isobars.

The last slide of the section is a hand drawing ([[22nd Oct.pdf#page=40|p40]]): "lower level", N.H. with **L** in the north, S.H. with **H** in the south, a wind arrow running from H to L across the equator.

### 4.2 The steady solution
<span class="scope-extra-book">extra · book</span> *Webster & Fasullo Eqs. [8]–[10]* · <span class="scope-extra-beyond">extra · beyond</span> *solution and numbers*

On a rotating platform with linear friction (rate $\alpha$, s⁻¹) the horizontal momentum equations in a boundary layer are

$$\frac{\mathrm Du}{\mathrm Dt}=fv-\alpha u,\qquad\frac{\mathrm Dv}{\mathrm Dt}=G-fu-\alpha v,\qquad G=-\frac1\rho\frac{\partial p}{\partial y}.\tag{CL15.3}$$

($G>0$ when pressure falls northwards.) The steady solution is found by solving the two linear equations $\alpha u=fv$, $\alpha v=G-fu$:

$$\boxed{v=\frac{G\alpha}{\alpha^2+f^2},\qquad u=\frac{G f}{\alpha^2+f^2}},\qquad\tan\theta=\frac{f}{\alpha}\tag{CL15.4}$$

where $\theta$ is the angle by which the wind is turned away from the pressure-gradient direction ($\theta=0$ is down the gradient, $\theta=90^\circ$ is geostrophic). At the equator $f=0$: $v=G/\alpha$, $u=0$, the frictional balance of Webster's Eq. [9]. For $f\gg\alpha$ the flow tends to geostrophy: $u\to G/f$, $v\to G\alpha/f^2$.

> [!intuition] A trolley on a slope with the brake half on
> Push a trolley down a long slope with the handbrake half on: the brake (friction) makes it go **down the slope** at a modest speed rather than accelerating. Now add steering that gets stronger the farther you are from the equator and always pulls to the right (in the north) or to the left (in the south): the trolley still heads down the slope but **veers sideways**, more so where the steering is strong. At the equator there is no steering at all: it goes straight. Cross the equator and the steering flips, so the track bends the other way: that is the "S" of the monsoon wind, **south-easterly → southerly → south-westerly**.

> [!example] Worked example 🔵: the monsoon flow numerically
> Take a 10 hPa pressure difference over 3000 km and $\rho=1.15$ kg m⁻³: $G=10^{3}/(3\times10^{6}\times1.15)=2.9\times10^{-4}$ m s⁻². Boundary-layer friction with e-folding time 0.5 day: $\alpha=2.31\times10^{-5}$ s⁻¹. Then $v_{\rm eq}=G/\alpha=12.5$ m s⁻¹ and
> | latitude | $u$ | $v$ | speed | wind comes from |
> |---|---|---|---|---|
> | 20° S | −4.8 | +2.2 | 5.3 m s⁻¹ | ESE (115°) |
> | 10° S | −6.2 | +5.7 | 8.4 | SE (132°) |
> | 5° N | +5.3 | +9.6 | 11.0 | SSW (209°) |
> | 10° N | +6.2 | +5.7 | 8.4 | SW (228°) |
> | 20° N | +4.8 | +2.2 | 5.3 | WSW (245°) |
>
> At 10° N the wind is turned $\theta=\arctan(f/\alpha)=\arctan(1.10)=48^\circ$ from the gradient direction; at 5° N, 29°. The parameters are illustrative, but the pattern (south-easterly in the south, southerly on the equator, south-westerly north of it) is the observed summer monsoon at low levels.

![[fig_cl15_crossequator.png|700]]
*Figure CL15.5. Top: eastward ($u$) and northward ($v$) components of the steady wind for a constant pressure gradient; bottom: the corresponding wind vectors. See: $u$ changes sign at the equator and $v$ is largest there. Script `fig_cl15_crossequator.py` (illustrative $G$, $\alpha$).*

> [!pitfall] Flow crosses the isobars, towards low pressure
> In (CL15.4) the wind has a component **down the pressure gradient** ($v>0$ means towards the low). That is what makes the monsoon work: friction lets the flow fall into the low and **converge** there, where it must rise. In the free atmosphere, with weak friction, the flow follows the isobars instead and does not fill the low.

### 4.3 The upper troposphere: the easterly jet
<span class="scope-taught">taught</span> *the upper-troposphere panel, 22 Oct p39* · <span class="scope-extra-book">extra · book</span> *Webster & Fasullo pp.157–159*

With the pressure gradient reversed and $\alpha$ an order of magnitude smaller, (CL15.4) gives $\theta=\arctan(f/\alpha_{\rm up})\approx85^\circ$ at 10° N: the flow is almost geostrophic. In the Northern Hemisphere geostrophic flow circulates **clockwise around high pressure**, so on the southern side of the upper-level anticyclone over South Asia the wind is **westward**: the **Tropical Easterly Jet**, extending from South Asia across Africa with speeds of 40–50 m s⁻¹ (Webster). The vertical change of the geostrophic wind follows from the **thermal wind** relation (differentiate geostrophic balance in the vertical): easterly shear above south-westerlies means the layer-mean temperature must **increase towards the pole**, which is the case in boreal summer over South Asia: the 500–200 hPa layer over the Tibetan Plateau is the warmest on Earth, more than 5 °C warmer than the equator at the same longitude (§7, [[Tibetan Plateau and Monsoon Heating]], [[CL14 Observed Winds - Jets, Trades and the ITCZ]]).

> [!extra-book]- 🟡 Extra (book): the Somali jet
> Where the East African highlands block the south-east trades of the southern Indian Ocean, they concentrate the cross-equatorial flow into the **Somali (Somalia) jet**, with a core above 20–25 m s⁻¹ (Webster p.161, Fig. 9). It drives a strong Somali current and intense coastal upwelling and a drop in sea surface temperature of 3–4 °C; it is the low-level counterpart of the upper easterly jet.

## 5. Moisture: the monsoon as a solar collector
<span class="scope-extra-book">extra · book</span> *Webster & Fasullo pp.154–157 (Figs. 3–4, Eq. [7])* · <span class="scope-taught">taught</span> *only visually: OLR (convection) and 200 hPa/850 hPa maps, 22 Oct p31* · <span class="scope-extra-beyond">extra · beyond</span> *latent-heating numbers*

So far moisture was ignored. The rain is **evaporated ocean water**, carried in by the low-level flow. Webster defines the vertically integrated moisture transport

$$B_q=\int_0^\infty q\,\mathbf V\,\mathrm dz\tag{CL15.5}$$

(Eq. [7]); because $q$ decreases roughly exponentially with height, the boundary layer dominates. In boreal summer the moisture sources lie in the *winter-hemisphere* ocean south of Asia, and in boreal winter north of Australia: only the Asian–Australian monsoon has a truly **interhemispheric moisture collector** (Webster, Fig. 4). The boundary-layer air warms along its path as sea surface temperature increases towards the continent, and saturation vapour pressure rises ([[Clausius-Clapeyron Relation]]), so the air arrives loaded.

> [!intuition] The ocean is the boiler, the monsoon trough the steam outlet
> Over the long track across the Indian Ocean the wind keeps evaporating water: the **sun's heat is stored as latent heat in the vapour**. When that air rises over the continent the vapour condenses and releases the stored heat *in the middle of the troposphere*, concentrated on a small region. The whole ocean's collected sunshine is delivered to the monsoon trough: a **solar collector**.

> [!example] Worked example 🔵: latent heating in W m⁻²
> Condensing 1 kg m⁻² of water releases $L_v=2.5\times10^{6}$ J m⁻². Rain of **1 mm per day** ($=1$ kg m⁻² day⁻¹) therefore heats the atmospheric column by $2.5\times10^{6}/86\,400=29$ W m⁻². A monsoon region with 8 mm day⁻¹ (illustrative) receives about **230 W m⁻²** of latent heating, comparable to the *global-mean* absorbed sunshine (≈ 240 W m⁻², [[CL03 Radiation and Planetary Energy Balance]]). That is why, once the rains are established, latent heating rather than surface heating dominates the driving of the circulation.

**Dry versus moist monsoon** (Webster & Fasullo, Fig. 2a vs 2b; the slide shows panel b(i)). Before the rains the circulation is shallow, driven by surface heat. Once there is enough imported vapour, the rising air releases latent heat and the circulation fills the whole troposphere; the lapse rate moves towards the **moist adiabat** ([[CL09 Radiative-Convective Equilibrium]], [[Convection]], [[Lapse Rate]]), so the *mean tropospheric temperature rises even though the surface cools*. Because so much more heat is added aloft, the time needed to radiate it away is longer and the circulation spreads over a larger horizontal scale. Surface winds that were weak before onset exceed 10 m s⁻¹ afterwards, and the sea surface temperature of the north Indian Ocean falls by 1–2 °C (evaporation and mixing).

**The monsoon as a migrated ITCZ.** Seen on the global scale (CL11, CL14) the rain belt follows the Sun into the summer hemisphere: the monsoon trough is the part of the [[Intertropical Convergence Zone]] that has moved onto the heated continent, far poleward of its oceanic position, because the land surface can heat strongly and the inflow supplies moisture. This is why the Indian monsoon falls at the latitudes of the Sahara ([[Hadley Cell]], [[Trade Winds and Westerlies]], [[Meridional Temperature Structure]]).

> [!extra-book]+ 🟡 Extra (book): a positive feedback that makes the onset sudden
> Webster & Fasullo describe the feedback loop: stronger winds import more vapour; more vapour means more latent heating aloft; that strengthens the upper-level temperature gradient (and the pressure contrast); which strengthens the winds. Against it, the rain cools the land surface and the sea, which weakens the *surface* gradient. After onset the driving passes from the surface temperature gradient to latent heating aloft, so the cooling at the surface no longer matters (p.155). This explains why the transition is abrupt rather than gradual.

## 6. Other monsoons, deserts and wet climates
<span class="scope-taught">taught</span> *the five systems on 22 Oct p26 and 30–31* · <span class="scope-extra-book">extra · book</span> *Hartmann §6.5.2–6.5.4, pp.184–192, Figs. 6.22–6.25*

The slides list the five monsoon systems and show their circulation and convection (p30–31); **Hartmann's §6.5 adds the climates around them** (this is all extra relative to the slides):

- **Deserts** ([[Large-scale_patterns_Hartmann.pdf#page=5|pp.184–187]], Fig. 6.22): where precipitation is far smaller than potential evaporation. Causes: (i) the **descending branch of the [[Hadley Cell]]** at 10°–40° latitude; (ii) subsidence on the **lee side of mountains** (rain shadow); (iii) **cold coastal ocean** (Peru, Atacama: stable air, fog but no rain); (iv) great distance from moisture. Deserts are regions of **net radiation loss** (high albedo, high outgoing longwave, [[Top-of-Atmosphere Radiation Budget]], [[Outgoing Longwave Radiation]]), supplied with energy by import of high-energy air aloft which then subsides ([[Poleward Energy Transport]]). Annual rain: Ouallen (Sahara) ≈ 22 mm, Antofagasta (Atacama) ≈ 2 mm.
- **Wet climates** (pp.187–188, Fig. 6.23): rain heavy and exceeding evaporation; the rain follows the ITCZ and the summer hemisphere; the biggest region of intense precipitation on Earth is the Indonesian–western Pacific (high SST, small islands, land–sea breezes); the **Amazon** (> 2 m of rain per year) is fed by the north-east trades and by recycling of its own rainfall.
- **Tropical wet and dry** (pp.189–192, Fig. 6.24): northern Africa goes from wet near the equator to extremely dry at 25° N; rain and low-level convergence follow the insolation into the summer hemisphere. In July the pressure falls over the central Sahara and winds along 15° N blow from the south-west; the Sahel gets rain only in summer, when solar heating can support upward motion and moist low-level inflow from the Gulf of Guinea. Over the central Sahara the convergence occurs but the air has travelled a long way over dry land, so there is almost no rain (p.190).

> [!extra-book]- 🟡 Extra (book): why the West African monsoon stays near the coast
> Webster & Fasullo (pp.158–159): the easterly jet decelerates over Africa, which generates a **secondary circulation** opposite to the monsoon's own: sinking air on the poleward side of the jet and rising on its equatorward side. This restricts the northward reach of monsoon rain over the continent and may explain why rain decreases so rapidly over the Sahel and Sahara; on the other hand it *enhances* the South Asian monsoon on the north side of the jet entrance over the Bay of Bengal.

## 7. The Tibetan Plateau, the ocean, and year-to-year variability
<span class="scope-extra-book">extra · book</span> *Webster & Fasullo pp.158–164; Hartmann p.183*

- **Tibetan Plateau** ([[Tibetan Plateau and Monsoon Heating]]): in spring and summer it intercepts sunlight at 4–5 km height, transfers sensible and latent heat to a deep layer of air, and creates the warmest upper troposphere on Earth, more than 5 K warmer than the equator at the same longitude; this reversed temperature gradient maintains the easterly jet. The plateau and Himalaya also block the cold dry northerly air and force the moist monsoon flow upward (§2).
- **Ocean heat transport** the ocean carries heat across the equator and stores it, **reducing the amplitude** of the monsoon's annual cycle; "without ocean heat transports ... [it] would quite likely be much wetter" (pp.160–163).
- **Interannual variability:** ENSO explains about **40 %** of the variance of Indian rainfall, with El Niño often associated with drought and La Niña with flood; there is also a biennial tendency (strong and weak years alternating) (p.162). Extreme excess rainfall in successive years has occurred only twice (1892–94, 1916–17) and successive deficits three times (1904–05, 1965–66, 1985–87).

> [!extra-beyond]- 🔵 Extra (beyond): where the course goes from here
> ENSO and the Indian Ocean Dipole are the main drivers of year-to-year changes; both are **coupled ocean–atmosphere modes**, and the waves behind them (Kelvin and Rossby waves) are the subject of [[Waves - Course Map]]. The same atmospheric dynamics control how tropical rainfall responds to warming (a stronger moisture supply, [[Clausius-Clapeyron Relation]], against a weaker circulation).

## 8. Tipping behaviour: monsoons as switches
<span class="scope-extra-beyond">extra · beyond</span> *synthesis; Hartmann p.192 for the Sahel feedback*

Three features of the monsoon are the signature of a **threshold system** ([[Bistability and Tipping Points]], [[Fixed Points and Linear Stability]]):

1. **Onset is abrupt.** The upper-level gradient reverses only when the temperature contrast passes the threshold (CL15.2), and then latent heating switches on and reinforces it: a positive feedback with a threshold.
2. **Active and break periods** alternate on 10–30 days: the system hovers near its threshold.
3. **Regime shifts in the Sahel.** Hartmann (p.192): a few years of enhanced rain can foster vegetation, which holds the sand and *lowers* the surface albedo; the desert surface, in contrast, reflects more of the sunlight. Charney (1975) proposed a feedback between albedo, subsidence and rainfall that can drive a region into drought ([[Ice-Albedo Feedback]] is the same kind of feedback). Paleoclimate evidence shows the Sahara was not always a desert (Hartmann p.192), consistent with **two possible states**, green and desert, separated by a threshold (`[verify]` the bistability interpretation before relying on it).

> [!connection] Dynamical systems and ecology
> A monsoon switching on, an ice sheet snowballing and a shallow lake turning turbid are the same mathematics: a slow parameter pushes a stable state to a fold, and a fast positive feedback completes the jump ([[CL04 Feedback and Multiple Steady States]], [[Ecology and Evolution - Course Map]]).

## Map of this chapter
> [!connection] How CL15 connects
> **Builds on:** [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (jets, trades, ITCZ) · [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (geostrophy, friction, Rossby number) · [[CL12 Rotating Frames and the Coriolis Force]] (Coriolis, $f$) · [[CL11 Mean Meridional Circulation and Angular Momentum]] (Hadley cell, ITCZ) · [[CL10 Global Energy Balance and Meridional Structure]] (insolation, net radiation) · [[CL09 Radiative-Convective Equilibrium]] (moist convection) · [[CL06 Hydrostatic Balance and Vertical Structure]] (hydrostatic columns) · [[CL03 Radiation and Planetary Energy Balance]] (heat capacity, relaxation)
> **Leads to:** the course closes here; for quiz preparation use the checklists at the end of CL09–CL12.
> **Concepts (new in this chapter):** [[Monsoon]] · [[Land-Sea Thermal Circulation]] · [[Orographic Precipitation]] · [[Cross-Equatorial Flow]] · [[Tibetan Plateau and Monsoon Heating]]
> **Concepts (used):** [[Intertropical Convergence Zone]] · [[Hadley Cell]] · [[Trade Winds and Westerlies]] · [[Coriolis Force]] · [[Coriolis Parameter]] · [[Dry Adiabatic Lapse Rate]] · [[Clausius-Clapeyron Relation]] · [[Atmospheric Stability]] · [[Relaxation Time]] · [[Insolation]] · [[Poleward Energy Transport]] · [[Outgoing Longwave Radiation]]
> **Other subjects:** [[Waves - Course Map]] (ENSO and equatorial waves) · [[Thermodynamics and Statistical Mechanics - Course Map]] (adiabats, Clausius–Clapeyron) · [[Landscapes and Geomorphology - Course Map]] (orography, erosion by monsoon rain) · [[Ecology and Evolution - Course Map]] (regime shifts) · [[Probability - Course Map]] (rainfall statistics)

> [!connection] Landscapes
> Monsoon rain on steep, uplifted terrain is one of the strongest erosive agents on Earth, tying climate to landscape evolution ([[Landscapes and Geomorphology - Course Map]]): orographic rain feeds the rivers that carve the Himalayan front.

> [!connection] Thermodynamics
> Hydrostatic columns, adiabatic cooling and latent heating are applications of the ideal gas law, the first law and the Clausius–Clapeyron relation ([[Thermodynamics and Statistical Mechanics - Course Map]]; [[First Law of Thermodynamics]], [[Adiabatic Process and Potential Temperature]]).

## Summary
> [!summary] Cheat-sheet
> - **Monsoon** = seasonal reversal of low-level wind + a dry/wet switch; one solstitial rain maximum; trough poleward of the oceanic ITCZ; systems: S Asian, Australian, N and S American, African (Asian–Australian is interhemispheric).
> - **Indian monsoon:** heavy rain on the west coast, in NE India (Meghalaya) and on the Burma coast (orography); annual cycle single-peaked, July–August; onset abrupt (late May–mid June).
> - **Land vs sea:** land has small heat capacity and shallow active depth (≈ 1 m) vs ocean (10–50 m): amplitude $F_0/\sqrt{\lambda^2+(\omega C)^2}$, lag → quarter period for the ocean.
> - **Columns:** $\partial\ln p/\partial z=-g/RT$; $\Delta\ln p(z_1)=\dfrac{gz_1}{R}\big(\dfrac1{T_c}-\dfrac1{T_w}\big)+\Delta\ln p(0)$: warm column = high pressure aloft, surface low; reversed gradient aloft above $z^*=-R\Delta\ln p(0)/[g(1/T_c-1/T_w)]$.
> - **Circulation:** low-level inflow to the land, ascent, upper outflow, subsidence over the ocean (thermally direct).
> - **Rotation:** PG + C + F = 0. Non-rotating: flow straight down the gradient. Rotating: flow crosses the isobars (high → low), turns right in the NH and left in the SH; at the equator $f=0$, flow purely meridional. $v=G\alpha/(\alpha^2+f^2)$, $u=Gf/(\alpha^2+f^2)$.
> - **Upper level:** reversed PG, weak friction ⇒ nearly geostrophic ⇒ easterly jet (40–50 m s⁻¹) over the heated plateau.
> - **Moisture:** 1 mm/day ≈ 29 W m⁻² of latent heating; the monsoon is a solar collector; positive feedback gives sudden onset.

> [!summary] Quiz checklist
> - Define a monsoon and list the five systems from the slide. *(seasonal reversal of wind speed and direction; South Asian, Australian, North American, South American, African.)*
> - Why do the west coast of India, Meghalaya and the west coast of Burma get so much rain? *(orography: forced ascent of moist onshore flow.)*
> - Draw the warm-column / cold-column sketch with H and L at the surface and aloft, and the circulation arrows.
> - **Trap 1:** "warm air rises so pressure is lower aloft over land" is *wrong*: pressure is *higher* aloft over the warm column (pressure falls more slowly with height in warm air); the low is at the *surface*.
> - Explain the non-rotating and rotating panels: which forces, which directions, why the flow crosses the equator; which hemisphere turns which way. **Trap 2:** friction is what lets the flow cross the isobars; with no friction and $f\ne0$ it would follow them.
> - **Trap 3:** the upper-tropospheric flow is *not* a mirror image of the lower: reversed pressure gradient, much weaker friction, so closer to geostrophic.
> - What is different about the monsoon rainfall latitude compared with the oceanic ITCZ? *(poleward, over heated land.)*

## Practice
1. **Rossby number.** Compare a sea breeze ($U=5$ m s⁻¹, $L=30$ km, 30° N) with a monsoon flow ($U=10$ m s⁻¹, $L=3000$ km, 15° N). What does each result say about the importance of rotation?
2. **Pressure aloft.** Two columns have mean temperatures 265 K and 275 K and equal surface pressure 1000 hPa. Find the pressure difference at 10 km. Which column has higher pressure?
3. **Reversal height.** The warm column has a surface low of 15 hPa and $T_c=265$ K, $T_w=273$ K. At what height does the gradient aloft reverse? What $\Delta T$ is needed to bring this height to 5.5 km for a 10 hPa low?
4. **Slab.** Compute the ratio of the annual-cycle amplitudes of the land slab (1 m) and the 50 m ocean slab for the same forcing. Why does the ocean lag by almost a quarter year?
5. **Cross-equatorial wind.** With $G=2.9\times10^{-4}$ m s⁻², $\alpha=2.31\times10^{-5}$ s⁻¹ find $u$, $v$ and the turning angle at 5° N. What are they at the equator?
6. **Orographic rain.** Using the table in §2, estimate the rain rate for an 800 m lift. What changes if the wind speed doubles? If the layer depth halves?
7. **Latent heating.** What heating (W m⁻²) corresponds to 10 mm day⁻¹ of rain? Compare with the global-mean absorbed sunshine.
8. **Radiative scale.** If radiative damping has an e-folding time of 20 days, how far does an upper-level parcel move at 1 m s⁻¹ and at 10 m s⁻¹ before cooling?
9. **Conceptual.** Explain why the South Asian monsoon rain falls at 20–30° N while the oceanic ITCZ is at 5–10° N.
10. **Conceptual.** Why does the monsoon south-westerly in the Northern Hemisphere start as a south-easterly in the Southern Hemisphere? Use the sign of $f$.

> [!example]- Solutions
> 1. Sea breeze: $f=7.29\times10^{-5}$, $\mathrm{Ro}=5/(7.29\times10^{-5}\times3\times10^{4})=2.3$ (rotation weak: the flow follows the pressure gradient). Monsoon: $f=3.78\times10^{-5}$, $\mathrm{Ro}=10/(3.78\times10^{-5}\times3\times10^{6})=0.088$ (rotation dominates the large scale).
> 2. $\Delta\ln p=341.8\times(1/265-1/275)=0.0469$; $p_c=275.4$ hPa, $p_w=288.7$ hPa: **13.2 hPa higher in the warm column**.
> 3. $\Delta\ln p(0)=\ln(985/1000)=-0.01511$; $1/265-1/273=1.106\times10^{-4}$; $z^*=287\times0.01511/(9.81\times1.106\times10^{-4})=4.0$ km. For 10 hPa, $z^*=5.5$ km needs $1/T_c-1/T_w=287\times0.01005/(9.81\times5500)=5.35\times10^{-5}$, so $1/T_w=3.7736\times10^{-3}-5.35\times10^{-5}$, $T_w=268.8$ K: $\Delta T=3.8$ K.
> 4. $F_0/\sqrt{\lambda^2+(\omega C)^2}$: land $\omega C=0.39$ ⇒ 15.1 K; ocean 50 m $\omega C=43$ ⇒ 1.16 K; ratio ≈ 13. For $\omega C\gg\lambda$ the response is $\hat T\approx F_0/(i\omega C)$, a phase lag of 90° (a quarter period): the ocean storage integrates the forcing, so the temperature peaks when the forcing has already fallen to zero.
> 5. $f=2\Omega\sin5^\circ=1.27\times10^{-5}$; $\alpha^2+f^2=6.95\times10^{-10}$; $v=2.9\times10^{-4}\times2.31\times10^{-5}/6.95\times10^{-10}=9.6$ m s⁻¹; $u=1.27\times10^{-5}\times2.9\times10^{-4}/6.95\times10^{-10}=5.3$ m s⁻¹; $\theta=\arctan(0.55)=29^\circ$. At the equator $u=0$, $v=G/\alpha=12.5$ m s⁻¹.
> 6. 800 m: $\Delta q\approx1.11$ g kg⁻¹ ⇒ $P=1.1\times10\times1500\times1.11\times10^{-3}/5\times10^{4}\times86\,400=31.7$ mm day⁻¹. $P\propto U$: doubling $U$ doubles it (63 mm day⁻¹). $P\propto D$: halving the depth halves it (but $\Delta q$ would not change).
> 7. $10\times29=289$ W m⁻², more than the global-mean absorbed 240 W m⁻².
> 8. $1\times20\times86\,400=1.7\times10^{6}$ m = 1,700 km; at 10 m s⁻¹, 17,000 km.
> 9. The monsoon trough follows the **heated land** and the moisture supply: land warms far more than the sea (Fig. CL15.2) and the Himalaya force ascent, so the heat low and the rain lie far poleward; over the ocean the rain is tied to the warmest SST (ITCZ) which is near 5–10° N.
> 10. In the Southern Hemisphere $f<0$ so $u=Gf/(\alpha^2+f^2)<0$: the flow turns to the **left** and is a south-easterly (blowing toward NW). After crossing the equator $f>0$, $u>0$: it turns to the **right** and becomes a south-westerly.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (3): the other tool's concept notes from the lectures, unreviewed
> [[zettel/monsoon-circulation|Monsoon Circulation]] · [[zettel/monsoon-dynamics|Monsoon Dynamics]] · [[zettel/orographic-uplift|Orographic Uplift]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | seasonal variations in wind speed and direction; five monsoon systems | [[22nd Oct.pdf#page=25\|22 Oct p25–26]]; [[22nd Oct CliSci slides.pdf#page=26\|CliSci p26]] | taught |
> | monsoon systems: OLR, 200 hPa streamlines, 850 hPa winds | [[22nd Oct.pdf#page=30\|22 Oct p30–31]]; [[21st Oct.pdf#page=19\|21 Oct p19]] | taught |
> | precipitation over South Asia, W coast of India, Meghalaya, Burma coast | [[22nd Oct.pdf#page=27\|22 Oct p27]] | taught |
> | orography, regional distribution of rain; annual cycle over India | [[22nd Oct.pdf#page=28\|22 Oct p28–29]] | taught |
> | cross-equatorial flow question; 3-D map | [[22nd Oct.pdf#page=32\|22 Oct p32–33]] | taught |
> | hand-drawn land/ocean, warm/cold column sketches with H and L | [[22nd Oct.pdf#page=34\|22 Oct p34–35]] | taught |
> | Webster Fig. 2b(i) circulation cross-section | [[22nd Oct.pdf#page=36\|22 Oct p36]] | taught |
> | PG–C–F panels, lower and upper troposphere, rotating and non-rotating | [[22nd Oct.pdf#page=37\|22 Oct p37–39]] | taught |
> | hand drawing: H (S) → L (N), low-level wind across the equator | [[22nd Oct.pdf#page=40\|22 Oct p40]] | taught |
> | definition, features, systems, heat capacity (4218 vs 1300 J kg⁻¹ K⁻¹), Eqs. [1]–[3] | [[Dynamical_theory_of_Monsoon_Webster.pdf#page=1\|Webster & Fasullo pp.151–152]] | extra/book |
> | Eqs. [4]–[6], onset threshold | [[Dynamical_theory_of_Monsoon_Webster.pdf#page=4\|Webster & Fasullo p.154]] | extra/book |
> | moist processes, solar collector, moisture transport Eq. [7], Fig. 4 | [[Dynamical_theory_of_Monsoon_Webster.pdf#page=4\|Webster & Fasullo pp.154–157]] | extra/book |
> | rotation Eqs. [8]–[10], easterly jet, thermal wind | [[Dynamical_theory_of_Monsoon_Webster.pdf#page=7\|Webster & Fasullo pp.157–159]] | extra/book |
> | Somali jet, Tibetan Plateau, ocean heat transport, ENSO | [[Dynamical_theory_of_Monsoon_Webster.pdf#page=10\|Webster & Fasullo pp.160–164]] | extra/book |
> | land–sea pressure contrast, monsoonal climates | [[Large-scale_patterns_Hartmann.pdf#page=3\|Hartmann pp.182–184]] | extra/book |
> | deserts, wet climates, tropical wet and dry, Sahel | [[Large-scale_patterns_Hartmann.pdf#page=5\|Hartmann pp.184–192]] | extra/book |
> | slab solution and numbers; column numbers; steady cross-equatorial solution; orographic rain rate; latent heating; Rossby comparison | computed here (`fig_cl15_*.py`) | extra/beyond |
> | regime-shift view of the Sahel and monsoon onset | Hartmann p.192; Charney (1975) | extra/beyond |
>
> **Dropped as redundant:** the repeated slides of the cross-equatorial question (22 Oct p32 and p33), the three near-identical hand-drawn sketches (p34, p35, p40) are merged into §§3–4, and the CliSci copies of p26–38 duplicate the photographed slides.

**References.** Webster, P. J. & Fasullo, J. (2003) "Monsoon: Dynamical Theory", in *Encyclopedia of Atmospheric Sciences* (Elsevier) · Hartmann, D. L. (2016) *Global Physical Climatology*, 2nd ed., §6.5 · Halley, E. (1686) *Phil. Trans.* 16, 153 · Charney, J. G. (1975) *Q. J. R. Meteorol. Soc.* 101, 193 · India Meteorological Department monsoon onset normals.

## Across subjects
- [[LS10 Folds Flexure and Mountain Building]] (Landscapes): the Himalaya and the Tibetan Plateau are both a tectonic product and a boundary condition of the monsoon circulation; rainfall focused on the range feeds back on erosion and isostatic uplift.
