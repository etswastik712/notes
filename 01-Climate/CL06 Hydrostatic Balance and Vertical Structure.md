---
title: CL06 Hydrostatic Balance and Vertical Structure
aliases: [CL06, Hydrostatic atmosphere, Vertical structure of the atmosphere]
subject: climate
type: chapter
chapter: 6
part: II
scope: [taught, extra-book, extra-beyond]
by: [argha, suhas-pre]
status: draft
prereq: ["[[CL05 Thermodynamic State of the Atmosphere]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# CL06 · Hydrostatic Balance and Vertical Structure

◀ [[CL05 Thermodynamic State of the Atmosphere]] · [[Climate - Course Map|Course Map]] · [[CL07 Optical Properties of the Atmosphere]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1–§2 hydrostatic balance and the weight of the column (Argha L5 sl. 51; Suhas pre-midsem)
> - §3 geopotential and geopotential height (Suhas)
> - §4 $p(z)=p_0e^{-z/H}$, scale height, vertical distribution of mass, the camp-pressure and troposphere-fraction questions (Argha L5 sl. 52; Suhas)
> - §5 the hypsometric equation and thickness (Suhas)
> - §6 sea-level reduction and constant-pressure surfaces (Suhas)
> - §8 "Hydrostatic or not?" (Argha L5 sl. 53–54)
>
> 🟡 **Extra · book**
> - Wallace & Hobbs Exercises 1.2–1.4 and the Standard Atmosphere (§4, §9)
> - diffusive separation above the turbopause (W&H §3.2.2; it is in the consolidated Suhas notes but no class evidence) (§4)
> - pressure-surface form of the pressure-gradient force (Marshall & Plumb §7.1, Eqs. 7-6 to 7-8) (§7)
>
> 🔵 **Extra · beyond**
> - the layer-by-layer Standard Atmosphere computed here (§9)
> - scale analysis of the vertical momentum equation with numbers (§8)
> - mass of the atmosphere and "10 m of water" (§2)
> - where hydrostatic balance fails (§8)

> [!key] After this chapter you can
> - **derive** $\partial p/\partial z=-\rho g$ from a force balance on a slab, and read it as "pressure is the weight of the air above",
> - define geopotential and geopotential height, and say when $Z\ne z$ matters,
> - combine hydrostatic balance with the gas law to get $p(z)=p_0e^{-z/H}$, $H=R_dT/g\approx7$–$8$ km, and use it (half the mass is below 5.5 km; 78 % is in the troposphere; pressure at 5000 m),
> - derive the **hypsometric equation** $Z_2-Z_1=\dfrac{R_d\overline{T_v}}{g_0}\ln\dfrac{p_1}{p_2}$ and explain why warm columns are thick,
> - reduce station pressure to sea level, and explain why meteorologists use pressure surfaces as a vertical coordinate,
> - answer the slides' question "Is the atmosphere really hydrostatic?" with numbers.

## 1. What "vertical structure" asks
<span class="scope-taught">taught</span> *Argha L5, slide 51; Suhas pre-midsem notes p.8*

In [[CL05 Thermodynamic State of the Atmosphere]] we tied $p$, $\rho$ and $T$ together at one level. Now ask: *how do they change with height?* Atmospheric pressure at sea level is about 1000 hPa; on the summit of Everest it is about 315 hPa; at 30 km it is a few hPa. A great simplification is that the vertical variation is **huge** compared with horizontal variations: pressure falls by a factor 3 in 9 km vertically but changes by only a few per cent over 1000 km horizontally. So, to first order, the atmosphere is stratified, and we need a law for the vertical profile.

> [!intuition] A stack of mattresses
> Stack mattresses. The one at the bottom is squashed by the weight of all the others; the one on top feels almost nothing. The *pressure* at any level is the weight, per unit area, of everything stacked above it. Air behaves the same way: each layer of air supports the layers above, and the bottom is squashed hardest, so the air is densest and pressure highest at the ground. That is all hydrostatic balance says.

## 2. The hydrostatic equation
<span class="scope-taught">taught</span> *Argha L5, slide 51; Suhas pre-midsem notes p.8*

Take a thin horizontal slab of air of area $\delta a$ between heights $z$ and $z+\delta z$, at rest. Vertical forces on it (Argha's slide 51, [[climate_intro_L1_L6.pdf#page=51|slide 51]]):

- pressure on its **lower** face pushes up with $p\,\delta a$;
- pressure on its **upper** face pushes down with $(p+\delta p)\,\delta a$ (here $\delta p<0$, since $p$ falls with height);
- gravity pulls down with the weight $\rho g\,\delta a\,\delta z$.

At rest the sum is zero: $p\,\delta a-(p+\delta p)\,\delta a-\rho g\,\delta a\,\delta z=0$, so $-\delta p=\rho g\,\delta z$:

$$\boxed{\frac{\partial p}{\partial z}=-\rho g}\qquad\Longleftrightarrow\qquad g\,\mathrm dz=-\alpha\,\mathrm dp\quad(\alpha=1/\rho).\tag{CL6.1}$$

The minus sign says pressure *decreases* with height. See [[Hydrostatic Balance]].

> [!intuition] Why pressure itself must fall: a tug of war that exactly cancels
> The slab feels two huge forces: the pressure force upward (the pressure *difference* across it) and gravity downward. They are each of order 10 N per kg of air but cancel almost perfectly, which is why we can write an equation with them equal. Anything left over would accelerate the air vertically; section 8 shows that for synoptic-scale flow the leftover is about $10^{8}$ times smaller than either force (and still $\sim10^{3}$ times smaller in deep convection).

**Pressure as a weight.** Integrate (CL6.1) upward from $z$ to the top of the atmosphere, where $p=0$:

$$p(z)=\int_z^\infty\rho g\,\mathrm dz'.\tag{CL6.2}$$

> [!example] Worked example: the weight of the atmosphere
> At the ground $\rho g=1.225\times9.807=12.0$ Pa m⁻¹, so $p$ falls about 1 hPa per **8.3 m** of ascent near sea level. With $p_0=1013.25$ hPa the mass above each square metre is $p_0/g=\mathbf{10\,330}$ kg: the same as a **10.3 m column of water**. Multiplying by the area of the Earth ($5.10\times10^{14}$ m²) gives $5.27\times10^{18}$ kg; Wallace & Hobbs quote $5.10\times10^{18}$ kg ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=24|W&H p.7–8]]) because they use the *mean surface* pressure 985 hPa, lower than 1013 hPa since continents stand above sea level. Pressure is also a mass coordinate: 1 hPa corresponds to $100/9.807=10.2$ kg m⁻² of air above you.

## 3. Geopotential and geopotential height
<span class="scope-taught">taught</span> *Suhas pre-midsem notes pp.8–9*

The **geopotential** $\Phi(z)$ is the work needed to lift 1 kg from sea level to height $z$ against gravity:

$$\mathrm d\Phi=g\,\mathrm dz\quad\Rightarrow\quad\Phi(z)=\int_0^zg(z')\,\mathrm dz',\qquad\text{and by (CL6.1)}\quad\mathrm d\Phi=-\alpha\,\mathrm dp.\tag{CL6.3}$$

Units J kg⁻¹ = m² s⁻². The second form is the useful one: radiosondes measure $p$ and $T$, from which $\Phi$ follows without measuring height. The **geopotential height** expresses it in length units with a fixed standard gravity $g_0=9.80665$ m s⁻²: $Z\equiv\Phi/g_0$ (unit: geopotential metre, gpm). See [[Geopotential]].

> [!intuition] An honest ruler for energy
> Gravity weakens slightly with height ($g\propto1/r^2$), so lifting 1 kg through the same 1 km costs a little less energy higher up. Geometric height $z$ is therefore a slightly dishonest measure of *energy*. $Z$ is defined so that **equal steps in $Z$ cost equal energy** ($9.807$ J kg⁻¹ per metre). Weather maps use $Z$ because the physics (pressure forces, potential energy) is written in terms of $\Phi$.

| $z$ (km) | 1 | 10 | 100 | 500 |
|---|---|---|---|---|
| $g$ (m s⁻²) | 9.804 | 9.776 | 9.506 | 8.431 |
| $Z$ (km) | 1.000 | 9.984 | 98.45 | 463.6 |

(Computed with $g(z)=g_0[a/(a+z)]^2$, $a=6371$ km, giving $Z=az/(a+z)$; the Suhas notes' table at 40° latitude agrees to within 0.02 km.) Below ~100 km, $Z$ and $z$ differ by less than 2 %; for the troposphere and stratosphere the difference is a metre or so per kilometre, and $Z$ is used throughout meteorology.

> [!pitfall] "Height" on a weather chart
> The number labelled "500 hPa height = 5580 m" is a **geopotential** height, $Z$, of the surface where $p=500$ hPa. It is not a geometric height and it is not a pressure.

## 4. The exponential atmosphere: $p(z)=p_0e^{-z/H}$
<span class="scope-taught">taught</span> *Argha L5, slides 51–52, 55; Suhas pre-midsem notes pp.9–10*

Combine (CL6.3) with the gas law $\alpha=R_dT_v/p$ (from [[CL05 Thermodynamic State of the Atmosphere]]):

$$\mathrm d\Phi=-R_dT_v\,\frac{\mathrm dp}{p}=-R_dT_v\,\mathrm d(\ln p).\tag{CL6.4}$$

This is the master relation between height, pressure and virtual temperature. If $T_v$ (and $g$) are constant (**isothermal**), integrating from $p_1$ to $p_2$ gives $Z_2-Z_1=H\ln(p_1/p_2)$, or equivalently

$$\boxed{p(z)=p_0\,e^{-z/H},\qquad H=\frac{R_dT}{g}=\frac{k_BT}{mg}}\tag{CL6.5}$$

where $m=M_d/N_A=4.81\times10^{-26}$ kg is the mean molecular mass; $R_d=k_B/m$ shows that Argha's molecular form is identical to the gas-constant form ([[climate_intro_L1_L6.pdf#page=51|slide 51]]). Density follows the same law, $\rho=\rho_0e^{-z/H}$ (since $p=\rho R_dT$ at constant $T$). See [[Scale Height]].

> [!verify] 7.5 km with $m=5\times10^{-26}$ kg?
> Slides 52 and 55 quote $H=k_BT/(mg)\approx7.5$ km for $T=255$ K, $g=9.8$ m s⁻², $m=5\times10^{-26}$ kg. With exactly $m=5\times10^{-26}$ the result is **7.19 km**; 7.5 km corresponds to the true mean molecular mass $m=4.81\times10^{-26}$ kg ($H=7.47$ km at 255 K). The slide's $m$ is a rounding of 29 u. The conclusion stands: $H\approx7.5$ km; but if you compute it with 5×10⁻²⁶ you will get 7.2.

> [!intuition] Why exponential? The pressure supports its own weight
> At each height the *rate* at which pressure falls is proportional to the density, and the density is proportional to the pressure itself (gas law). A quantity whose rate of decrease is proportional to its own size decays exponentially: the same maths as radioactive decay or a draining bucket whose outflow is proportional to the water in it. $H$ is the "decay length": in a height $H$ the pressure falls to $1/e$ (37 %). Equivalently, pressure **halves every $H\ln2\approx5.5$ km** (use 8 km) and falls by a factor 10 every ~17 km.

![[fig_cl06_pressure_profiles.png|760]]
*Figure CL6.1. (a) On a log-pressure axis the isothermal atmospheres are straight lines; the Standard Atmosphere (black) bends because the temperature changes with height. (b) The scale height is proportional to $T$: 6.4 km at 220 K, 7.5 km at 255 K, 8.4 km at 288 K, within the observed 7–8.5 km. See: the 5.5 km, 8.85 km (Everest) and 11 km points all lie along the standard curve.*

> [!example] Worked examples (the questions on slide 52, plus the book's)
> **(a) What fraction of the air is in the troposphere?** The fraction below height $z$ is $1-e^{-z/H}$. For $z=11$ km: $1-e^{-11/7.5}=\mathbf{77\,\%}$ ($H=8.4$ km: 73 %); the Standard Atmosphere gives 77.7 % (computed). About three quarters of the mass of the atmosphere is in the troposphere, which is only 0.17 % of the Earth's radius thick.
> **(b) Pressure at camp (Gya, 5000 m).** $p=1013\,e^{-5/7.5}=\mathbf{520}$ hPa; with $H=8.4$ km, 559 hPa; the Standard Atmosphere gives 540 hPa. A person at that camp breathes air at ~53 % of sea-level pressure.
> **(c) Everest** (8.848 km): the Standard Atmosphere gives 314 hPa ($p/p_0=0.31$); the isothermal formula with $H=7.5$ km gives 311 hPa.
> **(d) Half the mass.** $p=p_0/2$ at $z=H\ln2=5.5$ km (for $H=8$ km): half the atmosphere lies below 500 hPa. 🟡 *(W&H Exercise 1.2, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=25|p.8]])*
> **(e) Where is $\rho=1$ kg m⁻³? Where is $p=1$ hPa?** With $H=7.5$ km: $z=7.5\ln(1.25/1.0)=1.7$ km and $z=7.5\ln(1013)=52$ km. 🟡 *(W&H Exercise 1.3)*

![[fig_cl06_mass_fraction.png|720]]
*Figure CL6.2. (a) Cumulative mass below a height (black = Standard Atmosphere): 50 % below 5.5 km, 78 % below the 11 km tropopause, 95 % below 20 km. (b) Mass in successive scale heights: 63 %, 23 %, 8.6 %, 3.1 %, … (each is $1/e$ of the one below; W&H Ex. 1.4). See: nearly all the atmosphere is within three scale heights of the ground.*

> [!pitfall] Scale height is not "the height of the atmosphere"
> There is no sharp top. $H$ is an e-folding depth. The assumption "$T$ and $g$ constant" (slide 52) is a first approximation: $T$ changes by 70 K over the troposphere and stratosphere, which is why the black curve in Fig. CL6.1(a) is not straight. §5 removes the isothermal assumption.

> [!extra-book]- 🟡 Extra (book): composition above the turbopause
> *Below* ~105 km (the **turbopause**), turbulent mixing keeps the gas well mixed and all species share the mixture scale height. *Above* it molecular diffusion wins and each species $i$ follows its own barometric law with $H_i=R^*T/(M_ig_0)$ (lighter gases have larger $H_i$ and thin out more slowly), so the composition changes with height (the **heterosphere**). Example (W&H §3.2.2, consolidated Suhas notes): at 2000 K, $H_{\rm O}=106$ km and $H_{\rm H}=1700$ km; a factor $10^5$ excess of O over H at 200 km falls to only 2.5 by 1400 km. W&H Ch. 1 ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=26|p.9–10]]) introduces the terms; I found no evidence this was shown in class, so it is extra. Relates to the well-mixed vs short-lived discussion of Argha slide 55 in [[CL05 Thermodynamic State of the Atmosphere]].

## 5. The real atmosphere is not isothermal: the hypsometric equation
<span class="scope-taught">taught</span> *Suhas pre-midsem notes pp.9–10* · <span class="scope-extra-book">extra · book</span> *thickness examples: W&H §3.2.2–3.2.3*

If $T_v$ varies with height, integrate (CL6.4) between pressure levels $p_1$ (lower) and $p_2$ (upper) and define the **mean virtual temperature**, weighted by $\ln p$ (so that thick, near-surface layers are not over-counted):

$$\overline{T_v}\equiv\frac{\int_{p_2}^{p_1}T_v\,\mathrm d(\ln p)}{\ln(p_1/p_2)}.$$

Then exactly as for the isothermal case,

$$\boxed{Z_2-Z_1=\frac{R_d\overline{T_v}}{g_0}\,\ln\frac{p_1}{p_2}=\overline H\,\ln\frac{p_1}{p_2}}\tag{CL6.6}$$

the **hypsometric equation**; $Z_2-Z_1$ is the **thickness** of the layer between the pressure surfaces. See [[Hypsometric Equation]]. Notice that thickness depends only on the pressure ratio and the mean virtual temperature.

> [!intuition] Warm air is fluffy
> Heat a column of air and it expands: the same mass (the same pressure drop between the ground and the top) now occupies *more height*. Thickness is "how tall the same amount of air stands", and it grows in proportion to the mean temperature. That is why a warm, tropical column has high pressure surfaces aloft and a cold polar column has them sagging low, even if the *surface* pressure is the same. This is the root of the upper-level pressure gradients that drive the jet streams ([[CL14 Observed Winds - Jets, Trades and the ITCZ]]).

![[fig_cl06_thickness.png|760]]
*Figure CL6.3. (a) The 1000–500 hPa thickness is 20.29 m per kelvin of mean virtual temperature. (b) Two columns with the same surface pressure and a 40 K contrast: the 500 hPa surface is 812 m higher over the warm one, so at any fixed height aloft the pressure is higher over the warm air. See: the isobars fan out toward the warm side and their spacing is the temperature.*

> [!example] Worked examples
> **(a) 1000–500 hPa thickness:** $\Delta Z=\dfrac{287.05}{9.80665}\ln2\ \overline{T_v}=20.29\,\overline{T_v}$ m. For a polar winter column ($\overline{T_v}=242$ K): **4910 m**; at 266 K: **5400 m** (the "5400 m line" used by forecasters to separate rain from snow in mid-latitudes); tropical ($\overline{T_v}=286$ K): **5800 m**. (The W&H/Suhas example uses 288 K and 233 K: 5846 m and 4730 m; the tropical value is the layer mean, not the surface temperature.)
> **(b) Height of the 1000 hPa surface.** If sea-level pressure is 1014 hPa and $H\approx8$ km, $Z_{1000}=H\ln(1014/1000)=112$ m (so, near the ground, $\Delta Z\approx8.3$ m per hPa).
> **(c) Height of the 500 hPa surface** above a place where $Z_{1000}=100$ m and $\overline{T_v}=270$ K: $Z_{500}=100+20.29\times270=5578$ m.

> [!connection] Warm-core and cold-core lows
> Equation (CL6.6) explains why the pressure deficit of a **warm-core** system (a hurricane) is deepest at the ground and weakens with height (the thick warm layer partially fills in the depression aloft), whereas an **elevated low** that does not reach the ground must be cold below its level of maximum intensity and warm above it (Suhas notes p.12). Vertical structure of storms follows from temperature: [[CL13 Horizontal Motion - Geostrophic Balance and Friction]].

## 6. Reduction to sea level, and constant-pressure surfaces
<span class="scope-taught">taught</span> *Suhas pre-midsem notes pp.10–11*

**Sea-level reduction.** A station at elevation $Z_g$ measures pressure $p_g$. Applying (CL6.6) between the ground and sea level gives the pressure the station *would* read at sea level:

$$p_0=p_g\exp\!\Big(\frac{g_0Z_g}{R_d\overline{T_v}}\Big).\tag{CL6.7}$$

Without it every hill station would look like a deep low. Weather maps therefore show sea-level-reduced pressure.

> [!example] Worked example: a station on the Deccan plateau
> Pune is at about 560 m. A station pressure of 950 hPa and a layer-mean temperature of 300 K give $p_0=950\exp\big(9.807\times560/(287.05\times300)\big)=950\times1.0659=\mathbf{1012.6}$ hPa. At Shimla (2200 m, $p_g=780$ hPa, $\overline T=285$ K) the same formula gives 1015 hPa. The correction is large at height and rests on an assumed $\overline T$, so reduced pressure over high terrain is only approximate.

**Pressure surfaces as the natural coordinate.** Meteorologists plot the **height of constant-pressure surfaces** (500 hPa ≈ 5.5 km, "half the atmosphere below") instead of pressure at constant height. Reasons: (i) pressure is what radiosondes and aircraft measure; (ii) hydrostatic balance turns the map of $Z(x,y)$ on a pressure surface into a map of the horizontal pressure force; (iii) the density disappears from the equations (next box). Warm regions bulge the surfaces upward, cold regions let them sag: a map of $Z_{500}$ is a map of the mean temperature below plus the surface pressure pattern.

> [!extra-book]+ 🟡 Extra (book): the pressure-gradient force on a pressure surface is $-\nabla_p\Phi$
> Marshall & Plumb §7.1 (Eqs. 7-6 to 7-8, [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=4|p.113]]) derive what makes pressure coordinates so convenient. Take two points at the same height $z_0$; the pressure surface through $A$ rises to a different height at $B$. By hydrostatic balance, $(\partial p/\partial x)_z=-(\partial p/\partial z)(\partial z/\partial x)_p=\rho g\,(\partial z/\partial x)_p$, hence
> $$-\frac1\rho\Big(\frac{\partial p}{\partial x}\Big)_{\!z}=-g\Big(\frac{\partial z}{\partial x}\Big)_{\!p}=-\Big(\frac{\partial\Phi}{\partial x}\Big)_{\!p}.$$
> The horizontal pressure-gradient force per unit mass is the **gradient of geopotential on a pressure surface**, with no $\rho$. So geostrophic balance (CL13) becomes $f\mathbf k\times\mathbf u_g=-\nabla_p\Phi$: wind blows along the height contours of the 500 hPa chart, stronger where they are packed. That is why upper-air charts are height maps.

## 7. Layers of the atmosphere: the standard atmosphere
<span class="scope-extra-book">extra · book</span> *W&H Ch. 1 (Fig. 1.8–1.9; §1.3.4)* · <span class="scope-extra-beyond">extra · beyond</span> *computed here*

Because the vertical variation dominates, it is useful to define a **standard atmosphere**, a horizontally and temporally averaged profile as a function of height only ([[Standard Atmosphere]]). The US Standard Atmosphere 1976 prescribes the temperature in layers of constant lapse rate; the pressure then follows from (CL6.4), integrated layer by layer with $g_0$ and $R_d=287.053$ (computed in `cl06lib.py`):

| layer | base (km) | $T$ at base (K) | lapse rate (K km⁻¹) | $p$ at base (hPa) |
|---|---|---|---|---|
| troposphere | 0 | 288.15 | −6.5 | 1013.25 |
| tropopause | 11 | 216.65 | 0 | 226.32 |
| stratosphere | 20 | 216.65 | +1.0 | 54.75 |
| " | 32 | 228.65 | +2.8 | 8.68 |
| stratopause | 47 | 270.65 | 0 | 1.109 |
| mesosphere | 51 | 270.65 | −2.8 | 0.669 |
| " | 71 | 214.65 | −2.0 | 0.0396 |

![[fig_cl06_standard_atmosphere.png|560]]
*Figure CL6.4. Temperature of the Standard Atmosphere with its layer bases and pressures. See: temperature falls in the troposphere (by convection, [[CL09 Radiative-Convective Equilibrium]]), rises in the stratosphere (ozone absorbs sunlight, [[CL07 Optical Properties of the Atmosphere]]), falls again in the mesosphere.*

- **Troposphere** (0–11 km): $T$ falls at 6.5 K km⁻¹, the mean **lapse rate**, because convection mixes heat upward ([[Lapse Rate]], [[Dry Adiabatic Lapse Rate]], [[Atmospheric Stability]]); contains 78 % of the mass and nearly all weather.
- **Tropopause**: the cold lid. In reality it is higher in the tropics (~16–17 km) and lower at the poles (~8–9 km); the standard 11 km is a mid-latitude average. `[verify]` the real heights if they matter.
- **Stratosphere** (to ~47–50 km): $T$ increases with height because ozone absorbs solar ultraviolet; very stable.
- **Mesosphere** and above: $T$ falls again, then rises in the thermosphere.

These are the names behind the lapse-rate and emission-height arguments of the earlier chapters: the effective emission level of [[CL03 Radiation and Planetary Energy Balance]] ($T_e=255$ K, ≈ 5 km) sits in the troposphere.

## 8. Is the atmosphere really hydrostatic?
<span class="scope-taught">taught</span> *Argha L5, slides 53–54 (the questions)* · <span class="scope-extra-beyond">extra · beyond</span> *numbers and scale analysis derived here*

Slides 53–54 ask: *Is the atmosphere really in hydrostatic equilibrium? Check the pressure differences that drive monsoons and cyclones (the picture spans ~8000 km). What do you compare them with? What is the vertical pressure gradient? What are typical horizontal gradients?* ([[climate_intro_L1_L6.pdf#page=53|slide 53]].)

**Step 1: compare the pressure forces.** Vertical: $\rho^{-1}\partial p/\partial z=g=9.8$ m s⁻². Horizontal: a strong synoptic gradient is 10 hPa per 1000 km, giving $\rho^{-1}\partial p/\partial x=1000/(10^6\times1.2)=8\times10^{-4}$ m s⁻². The ratio is about $\mathbf{1.2\times10^{4}}$: the pressure gradient is a **vertical** gradient to better than 1 part in $10^4$.

**Step 2: ask what is left over.** The vertical equation of motion is $\mathrm Dw/\mathrm Dt=-\rho^{-1}\partial p/\partial z-g$. Write $p=\bar p(z)+p'$ where $\bar p$ is a reference state in *exact* hydrostatic balance: it cancels $g$ identically. What remains are perturbation terms, $\mathrm Dw/\mathrm Dt=-\rho^{-1}\partial p'/\partial z+(\text{buoyancy})$.

- *Synoptic scale* ($L\sim1000$ km, depth $H\sim10$ km, $U\sim10$ m s⁻¹, $W\sim1$ cm s⁻¹): $\mathrm Dw/\mathrm Dt\sim WU/L=10^{-7}$ m s⁻² against terms of order $10^{-1}$ m s⁻² in the perturbation pressure force: balanced to **1 part in $10^{6}$**. Hydrostatic balance is superb.
- *Deep convection* ($W\sim10$ m s⁻¹, $L\sim10$ km): $W^2/L\sim10^{-2}$ m s⁻², comparable with the buoyancy of a 1 K virtual-temperature excess ($0.033$ m s⁻²): the vertical acceleration **cannot** be neglected, so convection is *non-hydrostatic*.

![[fig_cl06_hydrostatic_check.png|620]]
*Figure CL6.5. Order-of-magnitude accelerations (scale estimates, not data). See: gravity and the vertical pressure force (10 m s⁻²) dwarf everything; the vertical acceleration of large-scale motion is $10^{-7}$; only in deep convection does it approach the buoyancy terms.*

> [!intuition] A tightrope walker: enormous forces, tiny wobble
> Two hands pull on the rope with enormous, equal and opposite forces. The walker's *acceleration* is the minuscule difference between them. Hydrostatic balance is the statement that the up and down forces cancel to a part in a million; the weather in the vertical is the tiny leftover. Whether that leftover can be neglected depends on how big it is compared with the *other* terms that matter at the scale you care about.

**Rule of thumb.** Hydrostatic balance holds when the horizontal scale $L$ is much greater than the vertical depth $H$ (small *aspect ratio* $H/L\ll1$): synoptic systems, monsoons, the general circulation. It fails for deep convection ($L\sim H$), steep orography, and for **sound waves** travelling vertically (the hydrostatic approximation filters them out, which is why weather models use it for large scales). Large-scale models therefore treat the vertical with hydrostatic balance and the horizontal with the full momentum equations ([[CL13 Horizontal Motion - Geostrophic Balance and Friction]]).

## Map of this chapter
> [!connection] How CL06 connects
> **Builds on:** [[CL05 Thermodynamic State of the Atmosphere]] (gas law, $T_v$, $R_d$) · [[CL03 Radiation and Planetary Energy Balance]] (emission level 5 km)
> **Leads to:** [[CL07 Optical Properties of the Atmosphere]] (absorption depends on the amount of gas above, i.e. on $p$) · [[CL09 Radiative-Convective Equilibrium]] (lapse rate from hydrostatic + first law) · [[CL13 Horizontal Motion - Geostrophic Balance and Friction]] (pressure-surface heights and geostrophy) · [[CL14 Observed Winds - Jets, Trades and the ITCZ]] (thermal wind from thickness)
> **Concepts:** [[Hydrostatic Balance]] · [[Geopotential]] · [[Scale Height]] · [[Hypsometric Equation]] · [[Standard Atmosphere]] · [[Virtual Temperature]] · [[Ideal Gas Law]] · [[Lapse Rate]] · [[Dry Adiabatic Lapse Rate]] · [[Atmospheric Stability]] · [[Atmospheric Composition]]
> **Other subjects:** [[Thermodynamics and Statistical Mechanics - Course Map]] (barometric law, equilibrium) · [[Fixed Points and Linear Stability]] (hydrostatic equilibrium is a stable steady state of the vertical momentum equation) · [[Landscapes and Geomorphology - Course Map]] (elevation and climate) · [[Ecology and Evolution - Course Map]] (altitude zonation, hypoxia at height)

> [!connection] Equilibrium and exponentials
> The exponential law (CL6.5) is the **barometric formula** of statistical mechanics: in an isothermal gas in a gravitational field, number density follows the Boltzmann factor $e^{-mgz/k_BT}$. The scale height is the height at which the potential energy $mgz$ equals the thermal energy $k_BT$. This is also why heavier gases (CO₂, Ar) are slightly more concentrated near the ground above the turbopause: [[Thermodynamics and Statistical Mechanics - Course Map]].

> [!connection] Altitude and organisms
> Pressure at 5000 m is 53 % of sea-level pressure: the *fraction* of oxygen is unchanged (21 %) but its partial pressure falls to 113 hPa, which sets the physiology of altitude and the vertical limits of plants and animals ([[Ecology and Evolution - Course Map]]).

## Summary
> [!summary] Cheat-sheet
> - **Hydrostatic:** $\partial p/\partial z=-\rho g$; $p(z)=\int_z^\infty\rho g\,\mathrm dz'$ = weight of the column above; $p_0/g=10\,330$ kg m⁻² (10.3 m of water); 1 hPa per 8.3 m near the ground.
> - **Geopotential** $\Phi=\int g\,\mathrm dz$, $\mathrm d\Phi=-\alpha\,\mathrm dp$; **$Z=\Phi/g_0$**; $Z\approx z$ to 2 % below 100 km.
> - **With the gas law:** $\mathrm d\Phi=-R_dT_v\,\mathrm d\ln p$. Isothermal: **$p=p_0e^{-z/H}$, $H=R_dT/g=k_BT/mg\approx7.5$ km**; 6.4 / 7.5 / 8.4 km at 220 / 255 / 288 K.
> - Half the mass below 5.5 km (500 hPa); 78 % below the 11 km tropopause; pressure at 5000 m ≈ 540 hPa; Everest ≈ 314 hPa.
> - **Hypsometric:** $Z_2-Z_1=(R_d\overline{T_v}/g_0)\ln(p_1/p_2)$; 1000–500 hPa thickness $=20.29\,\overline{T_v}$ m (5400 m at 266 K). Warm = thick.
> - Sea-level reduction $p_0=p_g\exp(g_0Z_g/R_d\overline{T_v})$.
> - Pressure force on a pressure surface $=-\nabla_p\Phi$ (no density).
> - Hydrostatic is excellent for $L\gg H$ (error $10^{-6}$ synoptic), fails for deep convection.
> - Standard atmosphere: lapse rate −6.5 K km⁻¹ to 11 km (216.65 K, 226.3 hPa), isothermal to 20 km, then warming.

## Practice
1. **Derive** (CL6.1) from the force balance on a slab, and compute $\rho g$ at sea level in Pa m⁻¹ and hPa per metre.
2. **Pressure at altitude.** Leh is at 3500 m. Estimate its pressure with $H=7.5$ and $8.4$ km, and compare with the Standard Atmosphere.
3. **Mass above Everest.** What fraction of the atmosphere's mass lies below the summit? (p = 314 hPa.)
4. **Thickness.** The mean virtual temperature of the 1000–500 hPa layer is 270 K. Find the thickness. If $Z_{1000}=100$ m, what is $Z_{500}$?
5. **Sea-level reduction.** Shimla (2200 m): $p_g=780$ hPa, $\overline{T}=285$ K. Find $p_0$. How sensitive is $p_0$ to a 5 K error in $\overline T$?
6. **Equivalence of forms.** Show $H=k_BT/(mg)=R_dT/g$.
7. **Potential energy.** How much energy per kg does it take to lift air to the 500 hPa surface ($Z=5.5$ km)?
8. **Hydrostatic or not?** Estimate the ratio of vertical to horizontal pressure gradient for 10 hPa per 1000 km. For a thunderstorm with $W=10$ m s⁻¹ and $L=10$ km, estimate $W^2/L$ and compare with the buoyancy of a 1 K excess.
9. **Derive** the pressure-surface form of the pressure-gradient force: $-\rho^{-1}(\partial p/\partial x)_z=-(\partial\Phi/\partial x)_p$.
10. **Conceptual.** Why does a mountain station's raw pressure not belong on a weather map? Why is the hurricane's pressure anomaly weaker at 500 hPa than at the surface?

> [!example]- Solutions
> 1. Slab force balance above gives $-\delta p=\rho g\,\delta z$. $\rho g=1.225\times9.807=12.0$ Pa m⁻¹ $=0.12$ hPa m⁻¹ (≈ 1 hPa per 8.3 m).
> 2. $H=7.5$: $1013\,e^{-3.5/7.5}=635$ hPa; $H=8.4$: $668$ hPa; the Standard Atmosphere: **658** hPa. The isothermal $H=8.4$ km overestimates because the real air above 3.5 km is colder; $H=7.5$ underestimates.
> 3. $1-314/1013=69\,\%$ of the mass lies below the summit; 31 % above.
> 4. $\Delta Z=20.29\times270=5478$ m; $Z_{500}=100+5478=5578$ m.
> 5. $p_0=780\exp(9.807\times2200/(287.05\times285))=780\times1.302=1015$ hPa. With $\overline T=290$ K: exponent 0.2592, $p_0=780\times1.2961=1011$ hPa: a **4 hPa** change for 5 K, the kind of error that matters on a weather map.
> 6. $R_d=k_B/m$ (since $R^*=N_Ak_B$ and $M_d=N_Am$), so $R_dT/g=k_BT/(mg)$ ∎.
> 7. $\Phi=gZ=9.807\times5500=53.9$ kJ kg⁻¹.
> 8. Vertical $=g=9.8$; horizontal $=8\times10^{-4}$: ratio $1.2\times10^{4}$. Convection: $W^2/L=10^{-2}$ m s⁻²; buoyancy of 1 K: $g\cdot1/300=3.3\times10^{-2}$ m s⁻². Comparable ⇒ non-hydrostatic.
> 9. $(\partial p/\partial x)_z=-(\partial p/\partial z)_x(\partial z/\partial x)_p$ (chain rule on a surface of constant $p$) $=\rho g\,(\partial z/\partial x)_p$; divide by $-\rho$ and use $\Phi=gz$: $-\rho^{-1}(\partial p/\partial x)_z=-g(\partial z/\partial x)_p=-(\partial\Phi/\partial x)_p$.
> 10. Raw pressure at height reflects altitude, not weather; a 560 m difference is 65 hPa, vastly larger than a typical synoptic signal of 5–10 hPa; reduction removes it. The hurricane is a warm-core system: the warm layer is thick, so the pressure surfaces rise toward the centre aloft and partly fill the surface depression (CL06 §5).

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (7): the other tool's concept notes from the lectures, unreviewed
> [[zettel/atmospheric-scale-height|Atmospheric Scale Height]] · [[zettel/atmospheric-thermal-stratification|Atmospheric Thermal Stratification]] · [[zettel/geopotential-height|Geopotential Height]] · [[zettel/homosphere-and-heterosphere|Homosphere and Heterosphere]] · [[zettel/hydrostatic-balance|Hydrostatic Balance]] · [[zettel/hypsometric-equation|Hypsometric Equation]] · [[zettel/vertical-pressure-gradient|Vertical Pressure Gradient]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | hydrostatic force balance, $-\partial p/\partial z=\rho g$, ideal-gas form $H=k_BT/mg$ | [[climate_intro_L1_L6.pdf#page=51\|Argha L5 sl. 51]]; [[suhas notes.pdf#page=8\|Suhas notes p.8]] | taught |
> | $p=p_0e^{-z/H}$, 7.5 km, troposphere fraction, camp pressure | [[climate_intro_L1_L6.pdf#page=52\|Argha L5 sl. 52]]; Suhas notes pp.9–10 | taught |
> | composition and vertical distribution of long/short-lived gases | [[climate_intro_L1_L6.pdf#page=55\|Argha L5 sl. 55]] | taught (in CL05) |
> | geopotential, geopotential height, table | [[suhas notes.pdf#page=9\|Suhas notes pp.8–9]] | taught |
> | hypsometric equation, thickness, warm/cold-core lows, sea-level reduction, constant-pressure surfaces | [[suhas notes.pdf#page=10\|Suhas notes pp.10–11]] | taught |
> | "Hydrostatic or not?", ~8000 km picture | [[climate_intro_L1_L6.pdf#page=53\|Argha L5 sl. 53–54]] | taught (questions) |
> | W&H Exercises 1.2–1.4, standard atmosphere, turbopause | W&H Ch. 1, pp.8–10 | extra/book |
> | pressure-surface pressure-gradient force | [[Geostrophic_motion_Marshall_and_Plumb.pdf#page=4\|M&P §7.1 Eqs. 7-6–7-8]] | extra/book |
> | numerical answers to slide 52–54 questions, scale analysis, layer-by-layer Standard Atmosphere, mass of atmosphere | computed here (`cl06lib.py`, `fig_cl06_*`) | extra/beyond |
>
> **Dropped as redundant:** Argha L5's $p(z)=p_0e^{-z/H}$ derivation and Suhas's (merged in §4); Argha's repeat of the same slide for the composition discussion (slide 55, kept in [[CL05 Thermodynamic State of the Atmosphere]]).
>
> **Corrections:** slide 52's $m=5\times10^{-26}$ kg gives $H=7.2$ km, not 7.5 km (true $m=4.81\times10^{-26}$ kg). The consolidated Suhas notes' thickness example uses $\overline{T_v}=288$ K for the tropics, which is surface temperature, not the layer mean.

**References.** Wallace & Hobbs (2006) *Atmospheric Science*, §1.3.4, §3.2 · Marshall & Plumb (2008) *Atmosphere, Ocean and Climate Dynamics*, §7.1 · US Standard Atmosphere 1976 (NOAA/NASA/USAF).
