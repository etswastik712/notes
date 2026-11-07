---
title: CL14 Observed Winds - Jets, Trades and the ITCZ
aliases: [CL14, Observed winds, Jet streams and trades, Zonal-mean zonal wind]
subject: climate
type: chapter
chapter: 14
part: IV
scope: [taught, extra-book, extra-beyond]
by: [suhas-post]
status: draft
prereq: ["[[CL13 Horizontal Motion - Geostrophic Balance and Friction]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/suhas-post, src/own-notes, status/draft]
---
# CL14 · Observed Winds: Jets, Trades and the ITCZ

◀ [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] · [[Climate - Course Map|Course Map]] · [[CL15 Monsoons]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 the question: why are there zonal winds at all? (14 Oct p4–7, 21 Oct p1–3)
> - §2 notation $u(\lambda,\varphi,p,t)$, snapshots vs averages, the three averaging configurations (21 Oct p3–8)
> - §3 zonal-mean zonal wind: easterlies/westerlies, jets, ~30 m/s at ~200 hPa, winter stronger, link to the temperature gradient (21 Oct p9–12; handwritten notes p.2)
> - §5 low-level easterlies = trade winds; angular-momentum bookkeeping (notes pp.2–3)
> - §6 ITCZ, convergence, the 3-D structure of cells and jets (14 Oct p3, 22 Oct p1–7, CliSci p1–11)
> - §7 the circulation is not zonally symmetric: jets stronger at some longitudes, 850 hPa and 250 hPa maps, monsoon winds (21 Oct p13–19)
>
> 🟡 **Extra · book**
> - footnote on instantaneous jet speeds (~50 m/s) and the Maury/trade-wind history, Fig. 5.22 (M&P §5.4, pp.74–78)
> - thermal-wind equation in Webster & Fasullo p.8 (§4)
> - Hartmann §6.5 on storm tracks, eddy heat flux, land–sea pressure patterns (pp.180–182, Figs 6.17–6.19) (§7)
>
> 🔵 **Extra · beyond**
> - what a reanalysis is (§2)
> - full derivation of the thermal wind and its numbers (§4)
> - the weak-temperature-gradient explanation of persistent tropical easterlies (§4)
> - idealised jets from thermal-wind balance (Fig. CL14.1)
> - mass-continuity estimate of ITCZ ascent (§6)
> - eddy-driven vs angular-momentum jets (§4)

> [!key] After this chapter you can
> - describe the observed zonal-mean zonal wind (where, how strong, which season, which level) and read it off a latitude–pressure section,
> - **derive the thermal-wind relation** $\partial u_g/\partial z=-\dfrac{g}{fT}\dfrac{\partial T}{\partial y}$ from geostrophic and hydrostatic balance and use it to explain why jets sit where the temperature gradient is large, why they are stronger in winter, and why the tropics have no jets,
> - explain trade winds, the ITCZ and the three-dimensional picture of cells and jets,
> - say why the real winds are *not* zonally symmetric and name what breaks the symmetry (land–sea contrast, mountains, eddies).

## 1. The question: why are there zonal winds at all?
<span class="scope-taught">taught</span> *Suhas 14 Oct p4–7 and 21 Oct p1–3; notes pp.2–3*

By the end of [[CL11 Mean Meridional Circulation and Angular Momentum|CL11]] the energy budget ([[CL10 Global Energy Balance and Meridional Structure|CL10]]) had given us a *meridional* circulation, and angular-momentum conservation had forbidden a single pole-to-pole cell. [[CL12 Rotating Frames and the Coriolis Force|CL12]] then showed that on a rotating Earth every meridional motion is turned sideways. Suhas summarises the chain on 21 Oct ([[21st Oct.pdf#page=2|p2]]):

1. the spatial gradient in the energy balance explains the meridional circulation and the vertical winds;
2. conservation of angular momentum does not permit a single meridional cell;
3. meridional winds are deflected to the **right** (NH) of their path, which **introduces winds in the zonal direction**.

On 14 Oct he had put the question to the class ([[14th Oct.pdf#page=4|p4–5]]): *what actually causes zonal (east–west) winds?* Land–ocean contrast, topography and vegetation certainly can, **but "even if the Earth were zonally homogeneous, zonal winds would be found in the atmosphere."** The next slide asks the observational question this chapter answers: *do the zonal winds observed in the atmosphere show a clear form and structure?* ([[14th Oct.pdf#page=7|p7]]: "we try to explain the main features of observed wind regimes in the atmosphere and their impact on the climate.")

> [!intuition] Weather map vs climate map
> A weather map is a photograph: swirling lows, ribbons of fast air, a wind that changes every hour. A climate map is a long-exposure photograph: average the wind over many years and over all longitudes and the swirls blur out, leaving only the structure that is always there, the *skeleton* of the circulation. This chapter studies the skeleton (§§3–6), then adds back the flesh: the longitude-dependent parts (§7).

```mermaid
flowchart LR
  A["CL10<br/>energy imbalance<br/>pole vs tropics"] --> B["CL11<br/>meridional cells,<br/>angular momentum"]
  B --> C["CL12<br/>Coriolis turns<br/>flow sideways"]
  C --> D["CL13<br/>geostrophic balance,<br/>friction"]
  D --> E["CL14<br/>what the winds<br/>look like and why"]
  E --> F["CL15<br/>monsoons:<br/>seasonal reversal"]
```

## 2. Describing and averaging the wind
<span class="scope-taught">taught</span> *Suhas 21 Oct p3–8; handwritten notes p.2* · <span class="scope-extra-beyond">extra · beyond</span> *what a reanalysis is*

**Notation.** Wind is a vector $\mathbf u=(u,v,w)$ (eastward, northward, upward; "westerly" means *from* the west, i.e. $u>0$). It is a function of longitude, latitude, pressure and time: $u=u(\lambda,\varphi,p,t)$ ([[21st Oct.pdf#page=7|21 Oct p7]]). The vertical component is tiny, $w\ll u,v$ except in violent disturbances (a consequence of the atmosphere's thinness), so it **cannot be measured directly** and is inferred from the horizontal wind via mass continuity (handwritten notes p.2; M&P §5.4.1; see Practice 6). Pressure is the natural vertical coordinate because pressure surfaces are the natural surfaces of the hydrostatic atmosphere ([[CL06 Hydrostatic Balance and Vertical Structure]]); 200 hPa is about 12 km.

**Snapshots.** The slides open with a live snapshot: the 100 m wind and mean sea-level pressure at 18 UTC on 19 October 2026, and the 200 hPa wind field ([[21st Oct.pdf#page=4|p4–6]]). A snapshot is dominated by *weather*: lows and highs, fronts, jets that wiggle.

**Averages.** To expose the climate we average, and the slides name **three configurations** ([[21st Oct.pdf#page=8|p8]]):

| configuration | what is averaged |
|---|---|
| **annual mean** | zonal wind from many years, averaged in time and in longitude |
| **DJF mean** | only December–February data, averaged in time and longitude |
| **JJA mean** | only June–August data, averaged in time and longitude |

The **zonal mean** is $\overline u(\varphi,p)=\dfrac1{2\pi}\oint u\,\mathrm d\lambda$ (an average along a latitude circle), the **time mean** is an average over the chosen period; together they reduce $u(\lambda,\varphi,p,t)$ to a *latitude–pressure picture* $\overline u(\varphi,p)$ for each season.

> [!example] Worked example: what averaging hides
> Eight values of $u$ (m s⁻¹) around one latitude circle at 200 hPa: 14, −3, 22, 8, 31, 5, −2, 19. The zonal mean is $\overline u=11.75$ m s⁻¹. The strongest sample is 31 m s⁻¹ and the standard deviation is 11 m s⁻¹, so the "jet" of 31 is invisible in the mean. That is exactly the effect behind the numbers quoted by M&P: the **mean** subtropical jet is ~30 m s⁻¹, but local **instantaneous** maxima approach **50 m s⁻¹** because the jet wiggles in longitude and time and is smoothed out by the averaging.

> [!intuition] Averaging a wiggling garden hose
> A jet of water that sweeps from side to side wets the whole lawn lightly; a long-exposure photograph shows a broad faint band, never the thin hard jet you see in a single frame. Time- and zonal-averaging a meandering atmospheric jet does the same: the average is broader and weaker than the instantaneous reality.

> [!extra-beyond]- 🔵 Extra (beyond): where do these maps come from? Reanalysis
> The maps are from **ERA5** reanalysis (ECMWF, 0.5° × 0.5°), shown through the University of Maine "Climate Reanalyzer". A [[Reanalysis Data|reanalysis]] re-runs a fixed weather model over decades and *assimilates* every observation (balloons, aircraft, satellites, surface stations) at each step, giving a gap-free, physically consistent estimate of $u,v,T,p,\dots$ everywhere, including where nobody measured. It is also how $w$ is obtained: not by measuring it, but as the vertical motion consistent with the observed horizontal winds and mass continuity. Think of the observations as GPS fixes, and the model as the road map that fills the gaps between fixes.

## 3. The zonal-mean zonal wind
<span class="scope-taught">taught</span> *Suhas 21 Oct p9–12; notes p.2; M&P §5.4.1, Fig. 5.20*

![[fig_cl14_idealised_ubar.png|620]]
*Figure CL14.1. **Idealised, not data.** Zonal-mean zonal wind constructed from thermal-wind balance of a prescribed temperature contrast (§4; script `fig_cl14_idealised_ubar.py`): contrast 12 K at 40° (annual), 14.5 K at 33° in the winter hemisphere and 8.5 K at 46° in the summer hemisphere (DJF: NH winter; JJA: SH winter), reversed above the tropopause. See: jets at ~12 km (≈ 200 hPa), stronger and nearer the equator in winter, weaker and further poleward in summer, easterlies in the tropics persisting through the troposphere, weak winds at the surface. Compare with the real ERA5 sections on slides 10–12 (embedded below).*

**What the slides state** ([[21st Oct.pdf#page=10|p10]], [[21st Oct.pdf#page=11|p11]], [[21st Oct.pdf#page=12|p12]]; the shading is green for westerly, brown for easterly, with thick black lines at the zero contour):

- **Zonal winds are predominantly easterly in the tropics and westerly in the mid-latitudes.** Their distribution can be used as a *metric to distinguish the tropical atmosphere from the mid-latitude atmosphere* (p10).
- **Away from the equator the wind strength increases with height**, with a maximum near **200 hPa and 35° N/S**; the zonal-wind maximum is **~30 m s⁻¹** (p11).
- **The narrow region of strong winds is called a jet stream.** Jet streams are found in **both hemispheres in all seasons**, and **stronger in the winter hemisphere**. "These observations suggest a possible link between the strength of the jet streams and the latitudinal gradient in temperature" (p12).

**What your handwritten notes add** ([[Suhas post midsem.pdf#page=2|p.2]], after Marshall & Plumb §5.4.1): zonal-mean winds are eastward (westerly) *almost everywhere except close to the equator*; the strongest winds lie at the core of the **subtropical jets**, the strongest of which is near **30° in the winter hemisphere**, with a weaker jet near **45° in the summer hemisphere**; near the ground the winds are much weaker but have the same pattern.

> [!verify] 30° or 35°?
> Slide 11 says the maximum is at "200 hPa and 35° N/S", Marshall & Plumb and your notes say the strongest jet is near **30°** in the winter hemisphere (summer jet near 45°). Both are right for different averages: the latitude of the zonal-mean maximum shifts with season (≈ 30° in winter, ≈ 40–45° in summer) and with the dataset, so the **annual-mean maximum lies between**, at ≈ 35°. Quote "~30–35°" unless a question specifies the season.

> [!intuition] Reading a latitude–pressure section
> Stand on the equator and imagine the atmosphere sliced like a layer cake along a meridian. The vertical axis is height (pressure falls upward), the horizontal axis is latitude, the colour is the eastward speed of the average wind. Two green "mountains" of strong westerlies rise on either side of a low, flat brown "plateau" of weak easterlies over the equator. The summits are the jets; the foot of each mountain at the ground is where the surface winds change from easterly to westerly.

**Numbers worth knowing:** summit ≈ 200 hPa (≈ 12 km); mean speed ≈ 30 m s⁻¹ (annual-mean; winter hemisphere larger); weaker jet ≈ 20 m s⁻¹ near 45° in the summer hemisphere; meridional winds are weak (< 1 m s⁻¹) except in the tropical upper troposphere, where they reach ≈ 3 m s⁻¹ toward the winter hemisphere (notes p.2).

> [!provenance]- Slide evidence (click to expand)
> ![[21st Oct.pdf#page=10&height=320]]
> ![[21st Oct.pdf#page=12&height=320]]

## 4. Why jets? Thermal wind
<span class="scope-taught">taught</span> *the hint on 21 Oct p12; M&P §5.4 closing paragraph* · <span class="scope-extra-book">extra · book</span> *thermal-wind equation: Webster & Fasullo p.8* · <span class="scope-extra-beyond">extra · beyond</span> *full derivation, numbers, weak-temperature-gradient tropics*

Slide 12 ends with a suggestion: **jet strength and the latitudinal temperature gradient are linked.** Marshall & Plumb finish §5.4 with the same message: warming the tropics and cooling the poles, through hydrostatic balance, tilts the pressure surfaces; the resulting pressure-gradient force is balanced on the large scale by the Coriolis force on the winds. The quantitative statement that ties the wind to the temperature is the **thermal wind**. This section makes the link exact.

**Recap from [[CL13 Horizontal Motion - Geostrophic Balance and Friction|CL13]] (three lines).** Away from the ground and the equator, the horizontal pressure-gradient force balances the Coriolis force: **geostrophic balance**, $fu_g=-\dfrac1\rho\dfrac{\partial p}{\partial y}$, $fv_g=\dfrac1\rho\dfrac{\partial p}{\partial x}$, with $f=2\Omega\sin\varphi$ ([[Coriolis Parameter]]). The wind blows *along* the isobars, with low pressure on its left (NH). Pressure is hydrostatic: $\partial p/\partial z=-\rho g$ ([[CL06 Hydrostatic Balance and Vertical Structure]]).

> [!intuition] Why the wind must grow with height: a staircase of ramps
> A warm air column is **puffed up** (less dense, so it takes more height to get from 1000 to 500 hPa); a cold column is **squashed**. So between warm tropics and cold pole the layer *thickness* shrinks poleward, and every pressure surface tilts downward toward the pole. The tilt is **cumulative**: the 1000 hPa surface is nearly flat, the 700 hPa surface a bit tilted, the 500 hPa more, the 300 hPa most (Fig. CL14.2a). Each is a steeper ramp than the one below. A steeper ramp means a bigger pressure-gradient force, hence a bigger geostrophic wind. **Temperature differences on the horizontal make the wind increase with height**, without any need for a strong wind at the bottom (where friction anyway keeps winds weak).

![[fig_cl14_thermal_wind.png|760]]
*Figure CL14.2. (a) Warm tropics (left) and cold pole (right) tilt the pressure surfaces more and more with height (vertical scale and contrast exaggerated). The pressure-gradient force points poleward; Coriolis must balance it, so the wind is a westerly (out of the page) that grows with height. (b) The resulting wind profile for the two gradients used in this chapter: winter 14.5 K per 2000 km, summer 8.5 K per 2000 km, at 35°. Script `fig_cl14_thermal_wind.py`.*

> [!derivation]- Derivation: from geostrophic + hydrostatic balance to the thermal wind
> Use **pressure coordinates** (the slick route; M&P Eq. 7-8 gives the geostrophic wind there, [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=4|p.113]]):
> $$u_g=-\frac gf\,\frac{\partial Z}{\partial y}\Big|_p,\qquad v_g=\frac gf\,\frac{\partial Z}{\partial x}\Big|_p ,$$
> where $Z(x,y,p)$ is the height of the pressure surface. The **hypsometric equation** (hydrostatic balance + ideal gas, [[CL06 Hydrostatic Balance and Vertical Structure]]) gives the thickness of a layer: $\dfrac{\partial Z}{\partial\ln p}=-\dfrac{RT}{g}$. Differentiate $u_g$ with respect to $\ln p$ and swap the order of derivatives (the Coriolis parameter does not depend on $p$):
> $$\frac{\partial u_g}{\partial\ln p}=-\frac gf\frac{\partial}{\partial y}\Big(\frac{\partial Z}{\partial\ln p}\Big)=-\frac gf\frac{\partial}{\partial y}\Big(-\frac{RT}{g}\Big)=\frac Rf\,\frac{\partial T}{\partial y}\Big|_p .$$
> Convert to height with $\mathrm dz=-(RT/g)\,\mathrm d\ln p$, i.e. $\partial/\partial\ln p=-(RT/g)\,\partial/\partial z$:
> $$\boxed{\frac{\partial u_g}{\partial z}=-\frac{g}{fT}\,\frac{\partial T}{\partial y}},\qquad\frac{\partial v_g}{\partial z}=\frac g{fT}\frac{\partial T}{\partial x}.\tag{CL14.1}$$
> In vector form $\partial\mathbf V_g/\partial z=\dfrac g{fT}\,\nabla T\times\hat{\mathbf k}$, which is Webster & Fasullo's eq. [11] ([[Dynamical_theory_of_Monsoon_Webster.pdf#page=8|p.8]]: "if the mean temperature of a layer decreases towards the poles, the vertical shear will be positive (lower-level easterlies, upper-level westerlies)").
> **Sign check (NH).** $f>0$ and $\partial T/\partial y<0$ (colder to the north) ⇒ $\partial u_g/\partial z>0$: westerly shear ✓. **SH.** $f<0$ and $\partial T/\partial y>0$ (colder to the south) ⇒ again $\partial u_g/\partial z>0$ ✓: jets are westerly in **both** hemispheres.

> [!example] Worked example 1: how big a jet does a typical gradient give?
> Take 35° N: $f=2\Omega\sin35^\circ=8.37\times10^{-5}$ s⁻¹, mean layer temperature $T=250$ K, a mid-latitude contrast $\Delta T=13$ K over $L=2000$ km. Then
> $$\frac{\partial u_g}{\partial z}=\frac{g}{fT}\frac{\Delta T}{L}=\frac{9.81}{8.37\times10^{-5}\cdot250}\cdot\frac{13}{2\times10^{6}}=3.05\times10^{-3}\ \mathrm{s^{-1}}=3.0\ \mathrm{m\,s^{-1}\,km^{-1}}.$$
> Over the 10 km of the troposphere: $u_g\approx\mathbf{30\ m\,s^{-1}}$, exactly the observed mean subtropical jet. The mean temperature difference across the jet region needed is only ~13 K, a modest fraction of the ≈ 40 K equator–pole contrast, because the contrast is concentrated in a belt.

> [!example] Worked example 2: winter vs summer
> A 20 m s⁻¹ summer-hemisphere jet at the same latitude needs $\Delta T=8.5$ K over 2000 km; the 30 m s⁻¹ winter jet needs 12.8 K: jet speed is **proportional** to the temperature contrast (Fig. CL14.3a), so the winter jet is stronger because the winter hemisphere has a stronger pole-to-tropics gradient (little sunlight at the pole, full sunlight in the tropics), exactly the link suggested on slide 12. A second effect: the same gradient gives a weaker jet at higher latitude since $u\propto1/f\propto1/\sin\varphi$ (Fig. CL14.3b).
>
> ![[fig_cl14_jet_scaling.png|720]]
> *Figure CL14.3. (a) Jet speed at 10 km versus the temperature contrast for three jet widths $L$ at 35° (the dotted levels are the observed mean 30 m s⁻¹ and the weaker summer jet 20 m s⁻¹). (b) For a fixed contrast the speed falls as $1/\sin\varphi$ poleward, and the formula (like geostrophy) fails near the equator ($f\to0$). Script `fig_cl14_jet_scaling.py`.*

> [!example] Worked example 3: the pressure-coordinate form
> The same relation in pressure coordinates, $\partial u_g/\partial\ln p=(R/f)\,\partial T/\partial y$, is handy for layers. At 45° N with $\partial T/\partial y=-10\ \mathrm K/1000\ \mathrm{km}$: $R/f=287/1.03\times10^{-4}=2.78\times10^{6}$ m² s⁻¹ K⁻¹; $\partial u_g/\partial\ln p=-27.8\ \mathrm{m\,s^{-1}}$ per unit $\ln p$. Between 850 and 250 hPa ($\ln(850/250)=1.22$): $u_g(250)-u_g(850)=+34\ \mathrm{m\,s^{-1}}$ (the wind *increases* upward because pressure decreases).

> [!intuition] Why no jets (and persistent easterlies) at the equator?
> Two reasons come from (CL14.1). First $f\to0$ at the equator, so the pressure gradient is not balanced by Coriolis and the relation breaks down. Second, and more physical: the tropical atmosphere cannot sustain horizontal temperature differences. Rapid convection and fast gravity waves flatten them (the **weak-temperature-gradient** regime: temperature is nearly uniform across the tropics at a given height). Little horizontal gradient ⇒ little shear ⇒ the tropical *surface* easterlies (§5) simply persist upward through the troposphere, which is exactly the broad brown plateau between the jets in the observed sections.

> [!extra-beyond]- 🔵 Extra (beyond): two kinds of jet, one picture
> The subtropical jet appears in two complementary explanations that must agree. **Angular momentum** ([[CL11 Mean Meridional Circulation and Angular Momentum]]): poleward-moving upper-level air conserves its large equatorial absolute angular momentum, so it is turned eastward and arrives at 30° with a strong westerly ($134$ m s⁻¹ in the frictionless ring of air, reduced to ~30–50 by eddies and friction). **Thermal wind** (this section): the Hadley cell's edge is where the temperature gradient steepens, and (CL14.1) says that gradient *requires* a westerly shear. The two are the same physics seen from the momentum and from the thermodynamic side: the Held–Hou model of CL11 uses both. A *different*, **eddy-driven** jet forms near 50–60° where the temperature gradient is also large and the mid-latitude eddies (storm tracks, §7) stir momentum into it; M&P note that the real surface westerlies peak near 50° N and S, well poleward of the subtropical jet, "explained by eddies" ([[climate-suhas merged.pdf#page=24|M&P §8.2.1, p.144]]). The two jets merge in some seasons and longitudes.

## 5. Trade winds, westerlies and the surface
<span class="scope-taught">taught</span> *notes pp.2–3 (M&P §5.4.1)* · <span class="scope-extra-book">extra · book</span> *M&P footnote 7 and the link to the ocean (Ch. 10)*

Near the ground the zonal-mean wind has the same sign pattern as aloft but much weaker amplitude (notes p.2): **westerlies poleward of ~30°, easterlies equatorward**. The tropical easterlies are really **north-easterlies** in the NH and **south-easterlies** in the SH, because the low-level return flow of the Hadley cell is directed toward the equator (and weakly toward the summer hemisphere) and is turned **right** (NH) / **left** (SH) by the Coriolis force. These are the **trade winds** ([[Trade Winds and Westerlies]]).

> [!intuition] Why north-*east*: Coriolis does the "east" part
> The Hadley return flow at the surface moves toward the equator, southward in the NH. Facing south, the Coriolis deflection is to the right, i.e. toward the **west**. So the air arrives from the north (northerly component) and the east (easterly component): a *north-easterly*. In the SH the same flow moves north and is deflected left, again toward the west: a *south-easterly*. The east–west part of the trade wind is the signature of the Earth's rotation ([[CL12 Rotating Frames and the Coriolis Force]]).

**Angular-momentum bookkeeping** (notes p.3, [[CL11 Mean Meridional Circulation and Angular Momentum|CL11]]). The Earth rotates west→east. Where the surface wind is easterly, the ground moves *east faster than the air*, so friction drags the air forward and the atmosphere **gains** angular momentum; where the surface wind is westerly the air runs east faster than the ground and friction pulls it back: the atmosphere **loses** angular momentum to the Earth. In steady state the gains in the tropics and the losses in mid-latitudes must balance (the net frictional torque on the whole atmosphere is zero, else the day length would drift): this is why the atmosphere needs *both* belts.

> [!extra-book]+ 🟡 Extra (book): where "trade" comes from and why it matters for the ocean
> M&P footnote 7: the term "trade winds" comes from the days of sailing ships, when these winds together with the mid-latitude westerlies let ships complete a circuit of the North Atlantic. They also note that this pattern of surface winds and the stress it exerts is a **primary driver of ocean circulation** (their Chapter 10): the trades and westerlies drive the sub-tropical ocean gyres ([[Landscapes and Geomorphology - Course Map]] for the coastal consequences).

## 6. The ITCZ and the three-dimensional picture
<span class="scope-taught">taught</span> *Suhas 14 Oct p3, 22 Oct p1–7 and CliSci p1–11* · <span class="scope-extra-beyond">extra · beyond</span> *mass-continuity estimate*

[[14th Oct.pdf#page=3|14 Oct p3]] defines the tropics *dynamically*: "Tropics: definition based on the dynamics of air: the **Inter-Tropical Convergence Zone (ITCZ)**". The trades from the two hemispheres blow toward each other and meet near the equator in a narrow band ([[22nd Oct.pdf#page=4|22 Oct p4–6]]): the surface air **converges**, is forced upward, and builds the tall cloud band that circles the globe on satellite images (the white belt on the Earth photograph, slides p4–5). The surface pressure there is low (Hartmann: the trades blow toward the equator from both hemispheres and meet in the ITCZ, "where the surface pressure is low and deep convection occurs with its attendant latent heat release and large-scale upward motion").

![[CL14 ITCZ Convergence Loop.svg|620]]
*Figure CL14.4. The ITCZ is a self-reinforcing loop: convergence feeds ascent, condensation heats the column and deepens the low, which draws in more convergence. Editable version: [[CL14 ITCZ Convergence Loop.excalidraw]].*

> [!intuition] A drain in the sky
> Think of a bathtub drain: the surrounding water flows in toward the drain from all sides (convergence) and then has to go down. The ITCZ is a drain for the lowest kilometre of air, except that it is also a heater: the water vapour in the rising air condenses, releasing latent heat that warms the column and keeps the drain low and open. The "drain" is bounded north and south by the sinking dry air of the subtropical highs; those belts contain the world's deserts ([[Hadley Cell]]).

**Where is the ITCZ?** Near the equator but not on it: it follows the summer hemisphere. In DJF air rises just *south* of the equator and sinks around 30° N; in JJA it rises just *north* and sinks around 30° S (notes p.2; M&P Fig. 5.21): "strong upward motion on the summer side of the equator, where the warm surface triggers convection, strong descent on the winter side". The clean slides show the migrating rainfall band month by month (CliSci [[22nd Oct CliSci slides.pdf#page=7|p7–10]]: accumulated precipitation maps). ITCZ concept note: [[Intertropical Convergence Zone]].

> [!example] Worked example: how fast does the air rise? (🔵 beyond)
> Mass continuity in the lowest layer: $\partial u/\partial x+\partial v/\partial y=-\partial w/\partial z$ (nearly incompressible at low levels). A horizontal convergence $\nabla\!\cdot\!\mathbf V=-4\times10^{-6}$ s⁻¹ (winds changing by 4 m s⁻¹ over 1000 km) acting through a 1 km layer gives $w\approx4\times10^{-6}\times10^{3}=4\ \mathrm{mm\,s^{-1}}\approx0.35$ km day⁻¹: slow (it would take about a month to rise 10 km). Deep convective towers do it in an hour by concentrating the ascent in a few percent of the area at ≈ 1–10 m s⁻¹; the mean is slow but the clouds are fast. The same equation is why $w$ is *inferred* from $u,v$ (§2).

**The three-dimensional structure** (22 Oct p7, [[22nd Oct.pdf#page=7|slide]]). The schematic stacks the pieces of CL11 and this chapter into one picture: the **Hadley cell** with deep convection at the equator and descent near 30°; the **subtropical jet** at the poleward edge of the Hadley cell (near 30°, high up); the **polar front** and **polar jet** near 60° where cold polar air meets warmer air; and the **tropopause** (≈ 16 km in the tropics, ≈ 10 km poleward), above which is the stratosphere. 22 Oct p3 ([[22nd Oct.pdf#page=3|slide]]) adds the jets seen from above: bands wrapped around each hemisphere, subtropical and polar, the latter meandering most.

> [!provenance]- Slide evidence (click to expand)
> ![[22nd Oct.pdf#page=7&height=320]]
> ![[14th Oct.pdf#page=5&height=320]]

## 7. The circulation is not zonally symmetric
<span class="scope-taught">taught</span> *Suhas 21 Oct p13–19, 22 Oct p1–2; notes p.2–3 (eddies and waves)* · <span class="scope-extra-book">extra · book</span> *Hartmann §6.5, Figs 6.18–6.19; M&P Fig. 5.22* · <span class="scope-extra-beyond">extra · beyond</span> *storm-track explanation*

The zonal mean is a **construction**. 21 Oct p13 asks to "look at the longitude–latitude distribution of winds at different pressure levels" and the answer is a series of ERA5 maps (1999–2022, from Climate Reanalyzer):

- **850 hPa, DJF** (p14–16): "the circulation of the atmosphere is not zonally symmetric": westerlies at mid-latitudes and easterlies in the tropics, but broken into **cells and ribbons** over each ocean basin, with a very strong, narrow zonal ribbon along the Southern Ocean (westerlies near 50° S).
- **250 hPa, DJF** (p17–18): the **jet streams** appear as ribbons of 24–70 m s⁻¹ and "**the strength of the jet stream is not equal at all longitudes**". The map shows one strong core downstream of Asia over the western Pacific, with colours reaching the top of the scale ($\approx60$–$70$ m s⁻¹, read off the colourbar; `[verify]`), a weaker maximum over North America and the Atlantic, and an unbroken southern-hemisphere (summer) band with speeds of $\approx24$–$36$ m s⁻¹.
- **850 hPa, JJA** (p19): "monsoon winds": a strong low-level jet in the western Indian Ocean (the Somali/Arabian Sea region), the seed of [[CL15 Monsoons]].
- **500 hPa, month by month** (22 Oct p1–2, CliSci p1): the same structure evolves seasonally; the winter-hemisphere jet is the strongest.

> [!intuition] A river with islands
> The zonal mean says "there is a river of westerlies at 35°". The map says: yes, but the river is fast through some channels (over East Asia and the West Pacific in northern winter) and slow in others, meanders, and sometimes splits around obstacles. Mountains and warm/cold ocean–land contrasts are the rocks and islands; the weather systems that grow in the fast stretches are the whirlpools.

**What breaks the symmetry** (and why the *slides* have already hinted at it on 14 Oct p5: land–ocean contrast, topography, vegetation):

1. **Land–sea heating contrast** and **orography** (the Tibetan Plateau and the Rocky Mountains) push the flow around and set up standing waves.
2. **Eddies**: your notes (p.2–3) record that the atmosphere is variable in time and three-dimensional; localized highs and lows in instantaneous maps indicate **eddies**, the "key agency (mid–high latitudes)" of meridional heat and moisture transport (M&P §5.4.1 and Ch. 8, [[CL11 Mean Meridional Circulation and Angular Momentum]]). M&P Fig. 5.22 is a typical *instantaneous* 500 hPa height map (12 GMT, 21 June 2003, 6 dam contours) set against the smooth monthly mean of Fig. 5.12 ([[climate-suhas merged.pdf#page=18|p.78]]).

> [!extra-book]+ 🟡 Extra (book): Hartmann on jets and storm tracks (§6.5, pp.180–182)
> Hartmann (scanned excerpt, [[Large-scale_patterns_Hartmann.pdf#page=1|pp.180–182]]) describes exactly the longitude dependence seen in the slides, with the mechanism: "the subtropical jet of mid-latitudes is not equally strong at all longitudes, but has local maxima associated with the distribution of land and ocean (Fig. 6.18). During January in the Northern Hemisphere the subtropical jet stream has **two local wind speed maxima downstream of the Tibetan Plateau and Rocky Mountains**, over the Pacific and Atlantic". These maxima in the time-mean wind coincide with maxima of **transient eddy activity** and eddy fluxes of heat and moisture: the **storm tracks** where vigorous mid-latitude cyclones are most frequent ([[Storm Tracks and Eddy Fluxes]]). The seasonal migration of the storm tracks drives the annual cycle of rainfall on the west coast of North America. In July the NH wind maximum is weaker and farther poleward; in the Southern Hemisphere the mid-latitude jet near 50° S exists in all seasons but the *subtropical* jet is strongest in July (winter), centred over the western Pacific and Australia, where strong convection over Indonesia drives a localized Hadley circulation. The seasonal variation of eddy heat fluxes is much larger in the NH. Fig. 6.17 shows the angular-momentum cycle (westerly angular momentum from the Earth to the atmosphere in the easterlies, and eddies carrying it poleward and downward to the westerlies).
> Hartmann's Figs 6.19–6.20 add the 1000 hPa pressure patterns: the January Aleutian and Icelandic lows over the northern ocean basins and the Siberian high, reversed in July when the dominant low is over Asia (the Asian monsoon low): a preview of [[CL15 Monsoons]].

> [!connection] Waves and eddies
> The meanders of the jet are planetary-scale **Rossby waves**, and eddies are the baroclinic waves that grow on the strong temperature gradient (Chapter 8 of M&P). The mathematics of waves, dispersion and group velocity is in [[Waves - Course Map]]; the jet is the waveguide.

## 8. What the winds tell us
<span class="scope-extra-beyond">extra · beyond</span> *synthesis*

Putting the chapters together:

| regime | where / level | typical speed | direction | cause (chapter) |
|---|---|---|---|---|
| **trade winds** | tropics, near surface | 5–10 m s⁻¹ | easterly: NE (NH) / SE (SH) | Hadley return flow turned by Coriolis (CL11, CL12) |
| **ITCZ** | near equator, summer side | light, convergent | convergence → ascent | warm surface, latent heating (§6) |
| **subtropical highs / deserts** | ~30°, surface | calm | descent | Hadley descent (CL11) |
| **mid-latitude westerlies** | 35–60°, surface and aloft | 5–10 m s⁻¹ at the surface, 30–50 aloft | westerly | eddies, angular momentum (CL11, §4) |
| **subtropical jet** | ~30–35°, 200 hPa | ~30 mean, 50 instantaneous | westerly | thermal wind + angular momentum (§4) |
| **polar-front jet** | ~50–60° | variable | westerly | thermal wind + eddies (§4) |
| **monsoon low-level jets** | W Indian Ocean, summer | 15–30 | cross-equatorial, then westerly | land–sea heating (CL15) |

Two big-picture messages: (1) the observed wind field is the *outcome* of the energy imbalance (CL10), the overturning cells (CL11), rotation (CL12) and friction (CL13) acting together, and the thermal wind is the exact bridge from the temperature field to the wind field; (2) because the atmosphere is **fluid**, "the wind" has structure on every scale: the zonal mean, the stationary waves (land–sea, mountains), the transient eddies. The rest of the course (CL15) asks what happens when the *seasonal* land–sea contrast reverses the wind altogether.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Why the Hadley cell stops: angular momentum and the ring of air
> A ring of air conserves its absolute angular momentum per unit mass A = Ωa² cos²φ + u a cos φ as it drifts poleward.
>
> ![[cl_angular_momentum.png|720]]
>
> **Try:** Slide φ to 30°: u = 134 m/s (the observed subtropical jet is weaker, because eddies and friction break the conservation); at 60°: 697 m/s, at 80° more than 2500 m/s. Start the ring at 10° instead of the equator to see the wind it picks up. Switch to 'surface (friction)' to see the trade-wind sign.
>
> [▶ Open the tool in your browser](../Assets/interactive/cl_angular_momentum.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/cl_angular_momentum.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How CL14 connects
> **Builds on:** [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (geostrophic balance, friction) · [[CL12 Rotating Frames and the Coriolis Force]] (right-turning deflection, $f$) · [[CL11 Mean Meridional Circulation and Angular Momentum]] (cells, angular momentum) · [[CL10 Global Energy Balance and Meridional Structure]] (why there is a gradient) · [[CL06 Hydrostatic Balance and Vertical Structure]] (hypsometric equation, pressure coordinates)
> **Leads to:** [[CL15 Monsoons]] (seasonal reversal; cross-equatorial flow)
> **Concepts (new):** [[Thermal Wind]] · [[Jet Streams]] · [[Zonal-Mean Zonal Wind]] · [[Reanalysis Data]] · [[Storm Tracks and Eddy Fluxes]]
> **Concepts (existing):** [[Subtropical Jet]] · [[Trade Winds and Westerlies]] · [[Intertropical Convergence Zone]] · [[Hadley Cell]] · [[Ferrel Cell and Polar Cell]] · [[Mass Stream Function]] · [[Absolute Angular Momentum of Air]] · [[Coriolis Force]] · [[Coriolis Parameter]] · [[Meridional Temperature Structure]] · [[Poleward Energy Transport]]
> **Other subjects:** [[Waves - Course Map]] (Rossby waves, waveguides) · [[Probability - Course Map]] (averages, variance, sampling) · [[Thermodynamics and Statistical Mechanics - Course Map]] (hypsometric equation, ideal gas) · [[Landscapes and Geomorphology - Course Map]] (orography, ocean gyres) · [[Fixed Points and Linear Stability]] (baroclinic instability as an instability of a balanced state)

> [!connection] Statistics: mean, variance, signal and noise
> The zonal and time mean is an **expectation** over longitude and time; the snapshot's departure from it is a **fluctuation** (an eddy). Mean 11.75 vs standard deviation 11 in the worked example of §2 is the same "signal-to-noise" question that [[Probability - Course Map]] formalises; ensembles and long averages are how climatology separates the robust skeleton from the weather.

## Summary
> [!summary] Cheat-sheet
> - $u=u(\lambda,\varphi,p,t)$; zonal mean $\overline u=\frac1{2\pi}\oint u\,\mathrm d\lambda$; three configurations: annual, DJF, JJA. $w\ll u,v$: inferred, not measured.
> - **Zonal-mean zonal wind:** easterly in the tropics, westerly in mid-latitudes; speed grows with height, maximum at **~200 hPa**, **~30–35° N/S**, **~30 m s⁻¹ mean** (50 instantaneous); **winter hemisphere stronger** (jet near 30°); weaker jet (~20) near 45° in summer; surface winds weak with the same pattern.
> - **Jet streams** exist in both hemispheres in all seasons. They are a thermal-wind phenomenon: $\partial u_g/\partial z=-\dfrac g{fT}\dfrac{\partial T}{\partial y}$; $u\propto\Delta T$ and $\propto1/\sin\varphi$. 13 K over 2000 km at 35° gives 30 m s⁻¹.
> - Tropical easterlies persist through the troposphere: weak temperature gradient ⇒ no shear.
> - **Trades:** low-level NE (NH) / SE (SH): Hadley return flow turned right/left by Coriolis. **ITCZ:** trade-wind convergence → low pressure → ascent → latent heat; follows the summer hemisphere.
> - Angular-momentum bookkeeping: easterlies (tropics) gain it from the Earth, westerlies (mid-lat) lose it; net torque zero.
> - **Not zonally symmetric:** jets stronger over East Asia–Pacific and N America–Atlantic (storm tracks); caused by land–sea contrast, topography, eddies.

> [!summary] Quiz checklist (verified against M&P §5.4 and the slides)
> - [ ] "Westerly" = wind **from** the west ($u>0$).
> - [ ] Strongest jets: **winter hemisphere**, ~30° (annual-mean max ~35°), **200 hPa ≈ 10–12 km**, ~30 m s⁻¹ mean; instantaneous up to ~50.
> - [ ] Near the surface the wind is much weaker but has the same easterly/westerly pattern; the tropical easterlies are really **NE/SE trades**.
> - [ ] Mean meridional winds are weak (< 1 m s⁻¹) except tropical upper levels (≤ 3 m s⁻¹ toward the winter hemisphere); the return flow below goes toward the summer hemisphere.
> - [ ] Jet strength is tied to the **latitudinal temperature gradient** (slide 12): give the thermal-wind reasoning, not just the observation.
> - [ ] Hadley ascent follows the summer hemisphere (ITCZ off the equator): **trap:** it is *not* exactly on the equator.
> - [ ] The upper-level ring-of-air $u=\Omega a\sin^2\varphi/\cos\varphi$ applies to the frictionless upper branch only, never at the surface.
> - [ ] The winds are **not** zonally symmetric (jet maxima over Asia–Pacific and N America–Atlantic).

## Practice
1. **Zonal mean.** The 200 hPa $u$ at 8 equally spaced longitudes on a latitude circle is 18, 5, −4, 27, 33, 12, 0, 21 m s⁻¹. Find the zonal mean and the largest departure from it, and explain why the mean underestimates the local jet.
2. **Thermal wind.** At 40° N, mean layer temperature 255 K, the temperature falls by 15 K over 2500 km toward the pole. Find the shear and the jet speed at 10 km if the surface wind is zero.
3. **Winter vs summer.** The winter gradient is 1.5 times the summer one at the same latitude. By what factor do the jets differ? Where else in the chapter does the same factor appear?
4. **Pressure coordinates.** Use $\partial u_g/\partial\ln p=(R/f)\partial T/\partial y$ to find $u_g(250)-u_g(850)$ at 45° for $\partial T/\partial y=-10$ K per 1000 km.
5. **Why no jet at the equator?** Give both the mathematical and the physical reason.
6. **Vertical motion.** Estimate $w$ at 1 km for a horizontal convergence of $5\times10^{-6}$ s⁻¹ in the lowest kilometre. How is $w$ obtained in practice?
7. **Direction of trades.** Explain with Coriolis why SH trades are south-easterlies.
8. **SH sign check.** Show that the thermal-wind shear is westerly in the Southern Hemisphere too.
9. **Longitude dependence.** List three reasons the jet is not equally strong at all longitudes, and one observational sign of each.
10. **Two jets.** Distinguish the angular-momentum (subtropical) jet from the eddy-driven jet in latitude, mechanism and seasonal behaviour.

> [!example]- Solutions
> 1. Mean $=(18+5-4+27+33+12+0+21)/8=14.0$ m s⁻¹; the largest departure is $33-14=+19$ m s⁻¹ (also $-18$ at $-4$). The mean smooths longitude structure: the local maximum (33) is 2.4× the mean, just like the 50 vs 30 m s⁻¹ of M&P.
> 2. $f=2\Omega\sin40^\circ=9.37\times10^{-5}$ s⁻¹; shear $=\dfrac{9.81}{9.37\times10^{-5}\times255}\cdot\dfrac{15}{2.5\times10^{6}}=2.46\times10^{-3}$ s⁻¹ $=2.5$ m s⁻¹ km⁻¹ ⇒ $u(10\ \mathrm{km})\approx25$ m s⁻¹.
> 3. Jet speed $\propto|\partial T/\partial y|$, so the winter jet is 1.5× the summer one (30 vs 20 m s⁻¹ ✓). The same ratio 30/20 = 1.5 was used in worked example 2; the physical origin is the stronger winter pole–tropics contrast on slide 12.
> 4. $R/f=2.78\times10^{6}$; $\partial u_g/\partial\ln p=(2.78\times10^{6})(-10^{-5})=-27.8$ m s⁻¹; times $\Delta\ln p=\ln(250/850)=-1.22$ gives $+34$ m s⁻¹.
> 5. Mathematical: $f=2\Omega\sin\varphi\to0$ so geostrophic balance, and hence (CL14.1), cannot be applied. Physical: the tropical temperature field is nearly uniform horizontally at a given height (weak-temperature-gradient regime), so there is little shear to generate a jet; the tropical easterlies persist with height.
> 6. $w\approx-\nabla\!\cdot\!\mathbf V\,H=5\times10^{-6}\times10^{3}=5$ mm s⁻¹ ≈ 0.43 km day⁻¹. In practice $w$ is computed from the observed horizontal winds by integrating continuity (reanalysis), not measured.
> 7. SH: equatorward flow is northward; Coriolis in the SH deflects to the **left**, i.e. toward the **west**: air from the south (southerly component) and the east: a south-easterly.
> 8. SH: $f<0$ and the pole (south) is colder, so $\partial T/\partial y>0$. (CL14.1): $\partial u_g/\partial z=-\dfrac g{fT}\dfrac{\partial T}{\partial y}=-(\text{neg}\ f)^{-1}\times(+)\Rightarrow$ positive ✓: westerly shear in both hemispheres. Numerically $+3.0\times10^{-3}$ s⁻¹ for the 35° S version of worked example 1.
> 9. (i) land–sea contrast: winter–summer reversal of the pressure pattern (Aleutian/Icelandic lows, Siberian high); (ii) mountains: downstream jet maxima behind the Tibetan Plateau and Rockies; (iii) eddies/storm tracks: maxima of transient eddy heat flux collocated with the time-mean jet maxima. Each is visible in the 250 hPa and 850 hPa maps and in Hartmann Fig. 6.18.
> 10. Subtropical jet: ~30–35°, driven by poleward transport of angular momentum in the Hadley cell and the temperature gradient at its edge; strongest in winter; the eddy-driven jet: ~50–60°, maintained by eddy momentum flux convergence in mid-latitudes, more variable, present all year in the SH; they may merge.

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (2): the other tool's concept notes from the lectures, unreviewed
> [[zettel/intertropical-convergence-zone|Intertropical Convergence Zone]] · [[zettel/trade-winds|Trade Winds]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | the question: zonal winds even without zonal asymmetry; chain of arguments | [[14th Oct.pdf#page=4\|14 Oct p4–7]]; [[21st Oct.pdf#page=1\|21 Oct p1–3]] | taught |
> | snapshots (100 m wind, MSLP, 200 hPa), notation $u(\lambda,\varphi,p,t)$, three averaging configurations | [[21st Oct.pdf#page=4\|21 Oct p4–8]] | taught |
> | zonal-mean zonal wind: easterlies/westerlies, 200 hPa and 35°, 30 m s⁻¹, jet streams, winter stronger, link with temperature gradient | [[21st Oct.pdf#page=9\|21 Oct p9–12]]; [[Suhas post midsem.pdf#page=2\|notes p.2]] | taught |
> | weaker summer jet ~20 m s⁻¹ near 45°; near-ground same pattern; trades NE/SE; meridional winds ≤ 3 m s⁻¹; Hadley/Ferrel cells; eddies and waves | [[Suhas post midsem.pdf#page=2\|notes pp.2–3]] (M&P §5.4.1) | taught |
> | ITCZ; 3-D structure; jets schematic; precipitation maps | [[14th Oct.pdf#page=3\|14 Oct p3]]; [[22nd Oct.pdf#page=3\|22 Oct p3–7]]; [[22nd Oct CliSci slides.pdf#page=7\|CliSci p1–11]] | taught |
> | longitude–latitude winds at several levels; jets not equal at all longitudes; monsoon winds | [[21st Oct.pdf#page=13\|21 Oct p13–19]]; [[22nd Oct.pdf#page=1\|22 Oct p1–2]] | taught |
> | instantaneous jet speed ~50 m s⁻¹ (footnote 6), "trade winds" history (footnote 7), link to ocean circulation (Ch. 10), Fig. 5.22, closing paragraph of §5.4 | [[climate-suhas merged.pdf#page=15\|M&P §5.4, pp.74–78]] | extra/book |
> | Hartmann §6.5: jet maxima and storm tracks, eddy heat flux, SH jets, Figs 6.17–6.19 (pressure patterns) | [[Large-scale_patterns_Hartmann.pdf#page=1\|Hartmann pp.180–182]] | extra/book |
> | thermal-wind equation (eq. [11]); sign statement | [[Dynamical_theory_of_Monsoon_Webster.pdf#page=8\|Webster & Fasullo p.8]] | extra/book |
> | geostrophic wind in pressure coordinates (used in the derivation) | [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=4\|M&P Eq. 7-8, p.113]] | extra/book (CL13 domain) |
> | derivation of (CL14.1); numbers; scaling; weak-temperature-gradient explanation; idealised jets; mass-continuity estimate; reanalysis | derived here | extra/beyond |
> | eddy-driven vs angular-momentum jets | M&P §8.2.1 p.144; Held & Hou (1980) via CL11 | extra/book, extra/beyond |
>
> **Dropped as redundant:** the repeated slide on the three averaging configurations (21 Oct p7–8) is merged into §2; the repeated colour-bar slides of the 250 hPa and 850 hPa maps (21 Oct p14–17) are merged into §7; the AI notes' table of winds ([[climate_book_notes.pdf#page=9|book notes §5.2]]) is checked against M&P and merged into §3 and §5.

**References.** Marshall, J. & Plumb, R. A. (2008) *Atmosphere, Ocean and Climate Dynamics*, §5.4, Ch. 7–8 · Hartmann, D. L. (2016) *Global Physical Climatology*, 2nd ed., §6.5 · Webster, P. J. & Fasullo, J. (2003) "Monsoon: dynamical theory", *Encyclopedia of Atmospheric Sciences* · Hersbach, H. et al. (2020) ERA5 global reanalysis, *Q. J. R. Meteorol. Soc.* 146, 1999 · Held, I. M. & Hou, A. Y. (1980) *J. Atmos. Sci.* 37, 515.
