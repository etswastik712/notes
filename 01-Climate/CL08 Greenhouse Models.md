---
title: CL08 Greenhouse Models
aliases: [CL08, Layer models, Greenhouse layer models]
subject: climate
type: chapter
chapter: 8
part: III
scope: [taught, extra-book, extra-beyond]
by: [argha, suhas-pre]
status: draft
prereq: ["[[CL07 Optical Properties of the Atmosphere]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# CL08 · Greenhouse Models

◀ [[CL07 Optical Properties of the Atmosphere]] · [[Climate - Course Map|Course Map]] · [[CL09 Radiative-Convective Equilibrium]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 the idealisation and the balances (Argha L6 sl. 60–64)
> - §2 one opaque layer, $T_s=2^{1/4}T_e$ (sl. 67; Suhas Model 1)
> - §3 the leaky layer, $T_s=T_e/(1-\varepsilon/2)^{1/4}$, and the planet check Earth/Mars/Venus/Jupiter (sl. 65–66, 68; Suhas Model 2)
> - §4 many layers (sl. 68 "can we improve the model by having many layers?"; Suhas Model 3, radiative discontinuity)
> - §5 sensitivity and feedbacks: Planck, water vapour, ice–albedo, cloud (Suhas notes)
>
> 🟡 **Extra · book**
> - Wallace & Hobbs §4.3.6 and Exercise 4.8 (the $N$-layer ladder $F,2F,\dots$, convection once the radiative lapse rate exceeds the adiabatic)
> - §10.3.2 water-vapour feedback $f\approx0.5$ (both boxed)
>
> 🔵 **Extra · beyond**
> - exact solution for $N$ grey layers with absorptivity $\varepsilon$ (script `cl08_layers.py`)
> - greenhouse flux $G$
> - optical-depth form $\varepsilon=1-e^{-\tau}$ and the link to CL09's grey atmosphere
> - CO₂ forcing in the layer model ($\Delta\varepsilon=0.019$, $\Delta T=1.1$ K)
> - a water-vapour feedback estimate
> - emission-height view
> - limits of the model

> [!key] After this chapter you can
> - set up the **three energy balances** (top of atmosphere, surface, atmosphere) of a layer model and solve them,
> - derive $T_s=2^{1/4}T_e=303$ K for an opaque layer, $T_s=T_e\,(1-\varepsilon/2)^{-1/4}$ for a leaky one, and $T_s=(N+1)^{1/4}T_e$ for $N$ opaque layers,
> - say what **absorptivity $\varepsilon$** physically is (an optical depth, $\varepsilon=1-e^{-\tau}$, [[CL07 Optical Properties of the Atmosphere]]) and why **$\varepsilon\approx0.78$** reproduces Earth's 288 K,
> - explain why the **same model fails for Venus** and what it leaves out (convection, clouds, spectrum),
> - compute the **no-feedback warming (≈ 1.1 K)** for CO₂ doubling and relate it to the Planck sensitivity and the water-vapour feedback of [[CL04 Feedback and Multiple Steady States]].

## 1. The idealisation: transparent to sunlight, opaque (or partly) to infrared
<span class="scope-taught">taught</span> *Argha L6, slides 60–64; Suhas pre-midsem notes pp.16–17*

[[CL03 Radiation and Planetary Energy Balance]] gave $T_e=255$ K and a surface 33 K warmer than that. We now build the simplest atmosphere that explains the gap, following the slides' sequence ([[climate_intro_L1_L6.pdf#page=61|slides 61–64]]):

1. **Transparent to shortwave** radiation: sunlight passes through the atmosphere and is absorbed at the surface. (From [[CL07 Optical Properties of the Atmosphere]]: roughly a quarter of sunlight is in fact absorbed in the air; ignored here.)
2. **Opaque (or partly opaque) to longwave**: the atmosphere absorbs the surface's infrared and re-emits it.
3. **Two uniform temperatures**: the surface $T_s$ and one atmospheric layer $T_a$. Planar geometry with the globally averaged absorbed sunlight $Q=\tfrac14S(1-\alpha)=238$ W m⁻² as the input at the ground.

The slides then add the shortwave fluxes (slide 63) and the longwave fluxes (slide 64): the upward surface emission $\sigma T_s^4$, the atmosphere's own emission up and down, and any part of the surface emission that leaks straight through. All models in this chapter come from writing **zero net flux** at each place ([[Zero-Dimensional Energy Balance Model]] applied several times): the top of the atmosphere, the surface, and each layer.

> [!intuition] A heated room with a ceiling
> The floor is a heater powered by the Sun at a fixed rate $Q$. With no ceiling the floor must radiate exactly $Q$ to space. Put a **ceiling** above it that absorbs the floor's infrared and radiates *half up and half down*: the ceiling's upward half is all that escapes, so it must equal $Q$; its downward half falls back on the floor, which therefore receives $Q$ **plus** the ceiling's return, and must run hotter to give both up. Add more ceilings and the floor gets hotter again. The ceiling does not create energy; it creates an **extra route of delay** that forces the floor to run hotter to push the same power out.

> [!key] Defining the greenhouse effect as a flux
> $$G\equiv\sigma T_s^4-\mathrm{OLR}\ \ (\approx390-239=151\ \mathrm{W\,m^{-2}}),$$
> the part of the surface's blackbody emission that does **not** reach space. It is the flux version of the 33 K temperature gap: $\sigma T_s^4-\sigma T_e^4=390-238=152$ W m⁻² ([[Greenhouse Effect]], [[Outgoing Longwave Radiation]]).

![[CL08 Leaky Greenhouse.svg|640]]
*Figure CL8.1. The leaky one-layer model (slides 64–66). See: of the surface emission $\sigma T_s^4$, a fraction $\varepsilon$ is absorbed by the layer and the rest ($1-\varepsilon$) goes straight to space; the layer re-emits $\varepsilon\sigma T_a^4$ both up and down. Editable version: [[CL08 Leaky Greenhouse.excalidraw]].*

## 2. Model 1: one fully opaque layer
<span class="scope-taught">taught</span> *Argha L6, slide 67 ("atmosphere is ideal blackbody, ε = 1"); Suhas notes Model 1* · <span class="scope-extra-book">extra · book</span> *W&H Exercise 4.8*

Take $\varepsilon=1$: the layer absorbs **all** longwave radiation that reaches it from below, and emits as a blackbody at $T_a$ in both directions.

**Top of atmosphere.** Only the layer's upward emission reaches space, so it must equal the absorbed sunlight:
$$\sigma T_a^4=\frac{S(1-\alpha)}{4}=\sigma T_e^4\ \Rightarrow\ T_a=T_e=254.6\ \mathrm K.$$
(The layer that radiates to space *is* by definition at the emission temperature, [[Effective Emission Temperature]].)

**Surface.** The ground receives sunlight plus the layer's downward emission and must emit that total:
$$\sigma T_s^4=\frac{S(1-\alpha)}{4}+\sigma T_a^4=2\sigma T_e^4\ \Rightarrow\ \boxed{T_s=2^{1/4}T_e=1.189\times254.6=302.8\ \mathrm K}\tag{CL8.1}$$
which is the slide's "$2\sigma T_a^4=\sigma T_s^4$" ([[climate_intro_L1_L6.pdf#page=67|slide 67]]). The result is **48 K above $T_e$**, compared with the observed 33 K, so the opaque layer *overestimates* the greenhouse effect: the real atmosphere is not opaque over the whole infrared (the window, [[Atmospheric Window]]).

> [!intuition] Why exactly 2? Counting the flux
> The layer must pass **one unit** ($Q$) to space, no matter what. It emits one unit up and one unit down, so the ground receives its own **one** unit of sunlight plus the **one** unit returned: **two** units in total. Because emission goes as $T^4$, the floor's temperature rises by $2^{1/4}=1.19$, not 2: the steep $T^4$ law makes the thermostat stiff ([[CL04 Feedback and Multiple Steady States]]).

> [!extra-book]+ 🟡 Extra (book): Wallace & Hobbs Exercise 4.8
> The same argument, in flux units $F=\sigma T_e^4$, is Exercise 4.8 of Wallace & Hobbs ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=138|PDF p.121–122]], Fig. 4.9): "the downward radiation at the surface is $F$ units of solar radiation plus $F$ of longwave from the atmosphere, a total of $2F$ … the temperature of the surface is **303 K, i.e., 48 K higher** than it would be in the absence of an atmosphere". Their $T_e$ is 255 K. The book then adds the second layer (§4) and notes the lowest layer is at the temperature found here.

## 3. Model 2: the leaky layer
<span class="scope-taught">taught</span> *Argha L6, slides 65–66 (emissivity ε<1, the three balances); Suhas notes Model 2*

Relax $\varepsilon=1$. The layer now has longwave **absorptivity** $\varepsilon\in[0,1]$: it absorbs a fraction $\varepsilon$ of the radiation reaching it and **transmits** the fraction $1-\varepsilon$. By **Kirchhoff's law** (absorptivity = emissivity, [[Blackbody Radiation]]; slide 65) it also emits with efficiency $\varepsilon$: $\varepsilon\sigma T_a^4$ upward and the same downward.

**The three balances** (slide 66, with the surface a blackbody for longwave):

| where | equation | meaning |
|---|---|---|
| top of atmosphere | $\dfrac{S(1-\alpha)}4=\varepsilon\sigma T_a^4+(1-\varepsilon)\sigma T_s^4$ | absorbed sunlight = layer's emission to space + the part of the surface emission that leaks through |
| surface | $\dfrac{S(1-\alpha)}4+\varepsilon\sigma T_a^4=\sigma T_s^4$ | absorbed sunlight + back-radiation = surface emission |
| atmosphere | $2\varepsilon\sigma T_a^4=\varepsilon\sigma T_s^4$ | emitted up and down = absorbed from below |

Only two are independent (energy conservation; subtract the first from the second to get the third). From the third:

$$T_a^4=\tfrac12T_s^4\ \Longrightarrow\ \boxed{T_a=2^{-1/4}T_s=0.841\,T_s}\quad\text{(independent of }\varepsilon\text{)}.$$

Insert in the surface equation: $\tfrac14S(1-\alpha)=\sigma T_s^4(1-\varepsilon/2)$, so

$$\boxed{T_s=\frac{T_e}{(1-\varepsilon/2)^{1/4}}=\Big(\frac{2}{2-\varepsilon}\Big)^{1/4}T_e}\qquad\Big[\text{OLR}=\sigma T_s^4\,(1-\tfrac{\varepsilon}{2})=\sigma T_e^4\Big].\tag{CL8.2}$$

(Check with the top-of-atmosphere balance: $\varepsilon\sigma T_a^4+(1-\varepsilon)\sigma T_s^4=\sigma T_s^4[\tfrac\varepsilon2+1-\varepsilon]=\sigma T_s^4(1-\tfrac\varepsilon2)$ ✓.) **Limits:** $\varepsilon\to0$ (no greenhouse gas): $T_s\to T_e$; $\varepsilon\to1$: $T_s\to2^{1/4}T_e$, Model 1 ✓; for $0<\varepsilon<1$ the surface is in between ($T_e<T_s<2^{1/4}T_e$).

> [!key] The effective emissivity of the planet
> Written as OLR $=\varepsilon_{\rm eff}\,\sigma T_s^4$, Eq. (CL8.2) says $\varepsilon_{\rm eff}=1-\varepsilon/2$. With $\varepsilon=0.8$ this is **0.6**: exactly the factor that appears in the steady-state plot of [[CL04 Feedback and Multiple Steady States]] (slide 45's code `.6 σ T^4`), so that "greenhouse factor" of CL04 is *this model* (the Argha AI notes make the same identification).

![[fig_cl08_one_layer.png|760]]
*Figure CL8.2. Left: surface temperature $T_s(\varepsilon)$ of the one-layer model (script `fig_cl08_one_layer.py`). See: it rises from $T_e=255$ K ($\varepsilon=0$) to $2^{1/4}T_e=303$ K ($\varepsilon=1$); $\varepsilon=0.78$ gives the observed 288 K; Mars sits at $\varepsilon\approx0.15$. Right: the greenhouse flux $G=\sigma T_s^4\varepsilon/2$ and the back-radiation $\varepsilon\sigma T_a^4$ at the same $\varepsilon$.*

> [!example] Worked examples
> **(a) $\varepsilon=0.5$.** $T_s=254.6\times(2/1.5)^{1/4}=254.6\times1.0746=273.6$ K, $T_a=273.6/1.189=230.0$ K.
> **(b) The $\varepsilon$ that gives Earth's 288 K.** Solve (CL8.2) for $\varepsilon=2[1-(T_e/T_s)^4]=2\,[1-(254.6/288)^4]=\mathbf{0.78}$. Then $T_a=288/2^{1/4}=242$ K, the greenhouse flux $G=\sigma T_s^4\varepsilon/2=390\times0.39=152$ W m⁻² ✓ (matches 151 from the budget), and the leak $1-\varepsilon=0.22$: **22 % of the surface emission escapes directly**, close to the 25 % of a 288 K spectrum that lies in the 8–12 µm window ([[CL07 Optical Properties of the Atmosphere]]).
> **(c) Mars.** $T_e=209.8$ K, $T_s=214$ K: $\varepsilon=2[1-(209.8/214)^4]=0.15$; in terms of optical depth (below) $\tau\approx0.16$: a thin, mostly transparent atmosphere ([[CL03 Radiation and Planetary Energy Balance]] §5).

> [!intuition] $T_a$ does not depend on $\varepsilon$. Why?
> Whatever fraction the layer absorbs, it emits the same fraction in each direction (Kirchhoff). The ratio of *emitted* to *absorbed* power is fixed by $T_a$ alone: $2\varepsilon\sigma T_a^4=\varepsilon\sigma T_s^4$, and $\varepsilon$ cancels. The layer is simply the temperature at which its two-sided emission balances what it takes from below. A thin (small-$\varepsilon$) layer takes and gives little, but it still settles to $0.84\,T_s$.

**Planet check (slide 68).** The slide concludes:
- the model "**works for Earth (~10⁵ Pa) and Mars**": single-layer values $\varepsilon\approx0.78$ and $0.15$ reproduce the temperatures;
- "the atmosphere is thick (~10⁷ Pa) and **not transparent** for **Venus**": the needed $\varepsilon=2[1-(226.6/737)^4]=1.98>1$ is impossible, the model cannot exceed $2^{1/4}T_e=269$ K for Venus (observed 737 K), and in addition Venus's clouds absorb the sunlight *in the atmosphere*, not at the ground;
- "**Jupiter and Saturn have internal sources**": the balance of sunlight alone fails ([[CL03 Radiation and Planetary Energy Balance]]);
- "Can we improve the model by having **many layers**?" → §4.

> [!verify] Mars's pressure on slide 68
> Slide 68 writes Mars's surface pressure as "~10¹ Pa" and slide 39 (L3) as "~10 mbar" (= 10³ Pa). The mean surface pressure of Mars is about **6 mbar ≈ 6×10² Pa**. The conclusion (very thin atmosphere, small $\varepsilon$) is unaffected, but quote 600 Pa.

> [!pitfall] The one-layer model gets the *total* right, not the *split*
> It reproduces the missing OLR $G=152$ W m⁻² by construction (we fitted $\varepsilon$), but its back-radiation $A_\downarrow=\varepsilon\sigma T_a^4=152$ W m⁻² (equal to $G$ in this model; Fig. CL8.2, right) is less than half the observed ≈ 340 W m⁻² at the ground, and even a fully opaque layer could return only 238 W m⁻², because the real surface "sees" the warm lower air (≈ 280 K), not an isothermal layer at 242 K. The layer is not a real level: $T_a$ is an **effective temperature of the whole absorbing column**.

## 4. Model 3: many layers
<span class="scope-taught">taught</span> *Argha L6, slide 68 (question); Suhas notes Model 3* · <span class="scope-extra-book">extra · book</span> *W&H Exercise 4.8 (induction), p.122* · <span class="scope-extra-beyond">extra · beyond</span> *exact solver, grey layers*

Stack $N$ isothermal layers, each opaque in the longwave, each emitting up and down. Number them from the **top**.

In equilibrium nothing is absorbed or created between levels except at the ground, so the **net upward flux through every interface is $F=\sigma T_e^4=Q$**. A fully opaque layer $k$ passes nothing through: it emits $E_k=\sigma T_k^4$ upward and the same downward. Hence at the interface between layer $k$ (above) and layer $k+1$ (below) the upward flux is $E_{k+1}$ and the downward flux is $E_k$, and
$$E_{k+1}-E_k=F .$$
At the top only the first layer's emission leaves, $E_1-0=F$, so $T_1=T_e$. Stepping down, $E_k=kF$. At the ground the net upward flux is $\sigma T_s^4-E_N=F$:

$$\sigma T_k^4=k\,F,\quad k=1,\dots,N,\qquad\sigma T_s^4=(N+1)F\ \Rightarrow\ \boxed{T_s=(N+1)^{1/4}\,T_e}\tag{CL8.3}$$

(emissions $F,2F,3F,\dots,NF$ down the ladder and $(N+1)F$ from the ground: the ladder of W&H p.122). Numbers for $T_e=254.6$ K:

| $N$ | 1 | 2 | 3 | 5 | 10 | 20 |
|---|---|---|---|---|---|---|
| $T_s$ (K) | 302.8 | 335.0 | 360.0 | 398.4 | 463.6 | 545.0 |

> [!intuition] A bucket brigade needs a gradient
> Think of heat passed upward from hand to hand along a chain of people, each of whom can only hand it to the next at a rate set by how much *hotter* they are than the next person. The ground-level worker must handle all the sunlight, so to push it to the person above he must be hotter; the second worker must be hotter than the third, and so on. The more people in the chain, the hotter the bottom of the chain must be to keep the same throughput. Each opaque layer is one more handover, so the ground temperature climbs, and the **steps between layers are largest at the bottom**: $T_k^4=kT_e^4$ means $\Delta T$ grows as the layer index increases.

![[fig_cl08_layers.png|760]]
*Figure CL8.3. Left: the surface temperature against the number of fully opaque layers (script `cl08_layers.py`, an exact numerical solution that reproduces $(N+1)^{1/4}T_e$ to 0.01 K). Right: the layer temperatures for $N=5$. See: the temperature rises steeply downward and the **ground is hotter than the air just above it** (398 K against 381 K): the "radiative discontinuity".*

**Grey layers.** With a real $\varepsilon<1$ per layer the same method gives a linear system for the $T_k$ (solved in `scripts/cl08_layers.py`): each layer has $\sigma T_k^4=\tfrac12(U_{k-1}+D_k)$ regardless of $\varepsilon$, but the flux transmitted past layers depends on $\varepsilon$.

| $T_s$ (K) | $N=1$ | 2 | 3 | 5 | 10 |
|---|---|---|---|---|---|
| $\varepsilon=0.5$ per layer | 273.6 | 289.3 | 302.8 | 325.3 | 367.3 |
| $\varepsilon=0.78$ per layer | 288.1 | 312.8 | 332.7 | 364.4 | 419.8 |
| $\varepsilon=1$ (opaque) | 302.8 | 335.0 | 360.0 | 398.4 | 463.6 |

Two layers of $\varepsilon=0.5$ give the same surface temperature (289.3 K) as one layer of $\varepsilon=0.8$: *what matters is the total longwave optical depth*, not how it is divided.

> [!extra-beyond]- 🔵 Extra (beyond): from layers to optical depth: the continuum limit
> For a layer with optical depth $\tau$ the absorptivity is $\varepsilon=1-e^{-\tau}$ ([[CL07 Optical Properties of the Atmosphere]], Kirchhoff). Replace the $N$ steps by a continuous vertical optical depth: the grey-atmosphere radiative equilibrium derived in [[CL09 Radiative-Convective Equilibrium]] gives $T^4(\tau)=\tfrac12T_e^4(1+D\tau)$ with diffusivity factor $D=1.66$, so the ground (just above which the air has the same $T$ up to a jump) has $T_g^4=T_e^4(1+\tfrac D2\tau_s)=T_e^4(1+0.83\,\tau_s)$. Comparing with (CL8.3): **$N+1\leftrightarrow1+0.83\,\tau_s$**, i.e. one opaque layer is worth about **1.2 units of longwave optical depth**. Earth's $\varepsilon=0.78$ ↔ $\tau=1.5$ (≈ 1.3 opaque layers); Venus with $(T_s/T_e)^4=112$ needs $\tau_s\approx134$, of order $10^2$ (a crude estimate; Venus's sunlight is absorbed in cloud, not at the ground).

**Why the layers pile up temperature at the bottom, and why that is unphysical.** The sunlight is absorbed at the ground (an assumption), the infrared must climb out through layer after layer, and the ground ends up *much* hotter than the air above it, with a large temperature drop (a steep lapse rate) in the lowest layers. W&H state the consequence: "the radiative equilibrium lapse rate steepens with increasing depth. In effect, radiative transfer becomes less and less efficient at removing the energy absorbed at the surface… **Once the radiative equilibrium lapse rate exceeds the adiabatic lapse rate, convection becomes the primary mode of energy transfer**" ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=139|W&H p.122]]). That convection is the subject of [[CL09 Radiative-Convective Equilibrium]]: the surface of Earth is **not** at the radiative-equilibrium temperature (CL09's grey column has the ground at 337 K without convection, 290 K with it).

## 5. Sensitivity, feedback and CO₂ in the layer model
<span class="scope-taught">taught</span> *Suhas pre-midsem notes pp.18–19: climate sensitivity and feedbacks (Planck, water vapour, ice–albedo, cloud)* · <span class="scope-extra-book">extra · book</span> *W&H §10.3.2* · <span class="scope-extra-beyond">extra · beyond</span> *forcing as $\Delta\varepsilon$, a water-vapour estimate*

**Planck feedback (taught).** The dominant negative feedback: warming raises emission. Linearising $Q=\sigma T_e^4$: $\partial T/\partial Q=1/(4\sigma T_e^3)=0.27$ K per W m⁻² (the Suhas notes quote 0.26; [[Planck Sensitivity]], [[CL04 Feedback and Multiple Steady States]]). The layer model refines this: since OLR $=\sigma T_s^4(1-\varepsilon/2)$ the relevant slope is $4\sigma T_s^3(1-\varepsilon/2)=3.3$ W m⁻² K⁻¹ at $T_s=288$ K, so $\Lambda_P=0.30$ K per W m⁻² (as found in CL04 for $\varepsilon_{\rm eff}=0.6$).

**The feedback table of the Suhas notes (taught):**

| feedback | sign | mechanism | note |
|---|---|---|---|
| Planck (blackbody) | negative | emission rises as $T^4$ | 0.26–0.30 K per W m⁻² alone |
| water vapour | positive | warmer air holds ~7 % more vapour per K (Clausius–Clapeyron), vapour is a greenhouse gas | roughly **doubles** the Planck-only response |
| ice–albedo | positive | ice melts → lower albedo → more absorption | strongest at high latitudes ([[Ice-Albedo Feedback]]) |
| cloud | uncertain | albedo cooling vs infrared trapping | largest source of model spread |

> [!extra-book]+ 🟡 Extra (book): the water-vapour feedback factor (W&H §10.3.2)
> At constant relative humidity the saturation vapour pressure rises ≈ 7 % K⁻¹ ([[Clausius-Clapeyron Relation]]), and the feedback factor is **$f\approx0.5$**, i.e. a gain $1/(1-f)=2$ ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=464|W&H p.447]]). Because of the nonlinearity of Clausius–Clapeyron, the feedback strengthens with temperature; if tropical SST rose from 28 °C to above 60 °C the factor would approach 1 and set up a **runaway greenhouse**, possibly the fate of Venus. These are the factors $f_i$ of [[Climate Feedback Factor]]; [[Water-Vapour Feedback]].

**CO₂ doubling in the layer model.** *(🔵 beyond; derived here.)* A doubling of CO₂ gives a radiative forcing of about **3.7 W m⁻²** at the tropopause (empirical fit $\Delta F=5.35\ln(C/C_0)$, Myhre et al. 1998: $5.35\ln2=3.71$). In the layer model the forcing is **a rise in absorptivity** $\varepsilon$ at fixed temperatures: it reduces OLR by $\Delta\mathrm{OLR}=-\tfrac12\sigma T_s^4\,\Delta\varepsilon$, so

$$\Delta\varepsilon=\frac{2F}{\sigma T_s^4}=\frac{2\times3.7}{390}=\mathbf{0.019}\quad(\varepsilon:0.78\to0.80).$$

The system then warms until OLR is restored. Two routes give the **no-feedback response**, and they agree:

$$\Delta T_s=\frac{F}{4\sigma T_s^3(1-\varepsilon/2)}=\frac{3.7}{3.3}=\mathbf{1.1\ K}\qquad\text{and}\qquad\Delta T_s=\frac{\partial T_s}{\partial\varepsilon}\,\Delta\varepsilon=\frac{T_s}{8(1-\varepsilon/2)}\Delta\varepsilon=59\ \tfrac{\rm K}{\rm unit}\times0.019=1.1\ \mathrm K.$$

![[fig_cl08_forcing.png|640]]
*Figure CL8.4. A CO₂ forcing in the one-layer model (script `fig_cl08_forcing.py`). See: at fixed $T_s=288$ K the higher absorptivity cuts the outgoing flux by 3.7 W m⁻² (vertical gap); the planet must warm by 1.1 K for the OLR to climb back to the absorbed 238 W m⁻². With the water-vapour feedback ($f\approx0.5$) the warming doubles to 2.2 K.*

**Water vapour in the layer model.** *(🔵 beyond; illustrative.)* Suppose a share $s$ of the longwave optical depth $\tau=-\ln(1-\varepsilon)=1.51$ is due to water vapour, which increases 7 % per K at fixed relative humidity. Then $\mathrm d\tau/\mathrm dT=0.07\,s\,\tau$, $\mathrm d\varepsilon/\mathrm dT=(1-\varepsilon)\,\mathrm d\tau/\mathrm dT$ and the feedback factor is $f=(\mathrm dT_s/\mathrm d\varepsilon)(\mathrm d\varepsilon/\mathrm dT)$:

| $s$ (water vapour's share of $\tau$) | 0.3 | 0.5 |
|---|---|---|
| $f_{\rm WV}$ | **0.41** | **0.69** |

— the same order as W&H's 0.5 (and ≈ 0.5–0.6 in climate models, [[Climate Feedback Factor]]). The total sensitivity is $\Lambda=\Lambda_P/(1-f)$ ([[Linearisation and Sensitivity]]): for $f=0.5$, **$\Delta T=1.1/(1-0.5)=2.2$ K per doubling**, the number found in CL04. The layer model supplies the *structure* of the feedback; it cannot supply the lapse-rate, cloud and ice-albedo contributions (there is no vertical structure or surface type).

> [!intuition] The thermostat and its amplifier
> The Planck response is the thermostat: heat the planet and it radiates harder. Water vapour is an **amplifier wired in parallel**: warming adds vapour, vapour thickens the blanket (higher $\varepsilon$), the thicker blanket warms the surface further. It is a positive feedback (an echo, $f=0.5$ ⇒ each loop adds half as much as the previous, the total is twice the initial kick), but not a runaway as long as $f<1$.

## 6. Reading the model: emission height and its limits
<span class="scope-taught">taught</span> *synthesis of slide 68* · <span class="scope-extra-beyond">extra · beyond</span> *emission-height view*

**Emission height.** Seen from space the planet radiates at $T_e$ from some effective height $z_e$ (≈ 5 km) above a surface at $T_s$. If the temperature falls with height at the lapse rate $\Gamma\approx6.5$ K km⁻¹, then $T_s\approx T_e+\Gamma z_e$ and the greenhouse effect is $G\approx\Gamma z_e$: $(288-255)/6.5\approx5$ km ✓. Increasing $\varepsilon$ raises $z_e$ (the opaque layer is higher), and the surface warms by $\Delta T_s=\Gamma\,\Delta z_e$: for the 1.1 K of §5 this needs $\Delta z_e=1.1/6.5\approx170$ m. *The one-layer model hides this inside $\varepsilon$; CL09 makes it explicit.*

> [!extra-beyond]- 🔵 Extra (beyond): consistency checks between CL03, CL04, CL07 and CL08
> 1. $T_s=T_e\varepsilon_{\rm eff}^{-1/4}$ with $\varepsilon_{\rm eff}=0.6$ gives 289.3 K (CL03, CL04) and equals Eq. (CL8.2) with $\varepsilon=0.8$ ✓; with the exact $\varepsilon=0.78$ ($\varepsilon_{\rm eff}=0.61$) it gives the observed 288 K ✓.
> 2. $\Lambda_P(\varepsilon_{\rm eff}=0.6,T=289)=0.304$ K per W m⁻² (CL04) equals $1/[4\sigma T_s^3(1-\varepsilon/2)]$ here ✓.
> 3. $\varepsilon=0.78\Leftrightarrow\tau=1.51$ (CL07); the leak $1-\varepsilon=0.22$ vs the 25 % window fraction of the 288 K spectrum ✓ (a coincidence of the same order, not an identity).
> 4. $N$ opaque layers ⇔ $\tau_s\approx1.2N$ (continuum limit, CL09) ✓.
> No inconsistency found among the four chapters.

**What the layer model leaves out** (and where it returns):
- **Convection and latent heat** carry about a third to half of the surface's energy flux; the real ground is not in radiative equilibrium ([[CL09 Radiative-Convective Equilibrium]]).
- **Clouds** change both $\alpha$ and $\varepsilon$.
- **Shortwave absorption in the air** (≈ 22 %) is neglected.
- **Spectral structure**: $\varepsilon$ is one number but really varies from 0 (window) to 1 (CO₂ band centres); the real absorptivity grows slowly (logarithmically) with CO₂ ([[CL07 Optical Properties of the Atmosphere]]).
- **Geometry**: one global mean, no latitude ([[CL10 Global Energy Balance and Meridional Structure]]).

## Map of this chapter
> [!connection] How CL08 connects
> **Builds on:** [[CL03 Radiation and Planetary Energy Balance]] ($T_e$, 33 K) · [[CL04 Feedback and Multiple Steady States]] ($\Lambda_P$, $\varepsilon=0.6$, feedback factors) · [[CL07 Optical Properties of the Atmosphere]] ($\varepsilon=1-e^{-\tau}$)
> **Leads to:** [[CL09 Radiative-Convective Equilibrium]] (what happens when the radiative lapse rate is too steep) · [[CL10 Global Energy Balance and Meridional Structure]] (latitude)
> **Concepts:** [[One-Layer Greenhouse Model]] · [[Multi-Layer Greenhouse Model]] · [[Greenhouse Effect]] · [[Water-Vapour Feedback]] · [[Climate Feedback Factor]] · [[Planck Sensitivity]] · [[Effective Emission Temperature]] · [[Outgoing Longwave Radiation]] · [[Atmospheric Window]] · [[Blackbody Radiation]] · [[Clausius-Clapeyron Relation]]
> **Other subjects:** [[Thermodynamics - Course Map]] (Kirchhoff, equilibrium) · [[Evolution of Earth and Life - Course Map]] (faint young Sun and the greenhouse, [[Faint Young Sun Paradox]]) · [[Ecology and Evolution - Course Map]] (feedback and regime shifts, [[Bistability and Tipping Points]])

> [!connection] Linear algebra
> The $N$-layer model is a **linear system** ($3N+1$ equations) in the emitted powers $\sigma T_k^4$; its solution at $\varepsilon=1$ is the simple arithmetic ladder $kF$. Writing the solver (`cl08_layers.py`) is a small exercise in setting up and solving $A\mathbf x=\mathbf b$, and the continuum limit is a boundary-value problem for a differential equation ([[CL09 Radiative-Convective Equilibrium]]).

> [!connection] Deep time
> A stronger greenhouse (larger $\varepsilon$) is the standard way to keep the early Earth warm under a fainter Sun: $T_s=T_e(\varepsilon)$ with $S\to0.7S$ needs $\varepsilon\approx0.94$ to reach 273 K at $\alpha=0.3$ (derived here from (CL8.2); Practice 8), compared with 0.78 today ([[Faint Young Sun Paradox]]).

## Summary
> [!summary] Cheat-sheet
> - Idealisation: **transparent to shortwave, partly opaque to longwave**, planar balance, absorbed sunlight $Q=238$ W m⁻² at the ground. Greenhouse flux $G=\sigma T_s^4-\mathrm{OLR}\approx150$ W m⁻² (33 K).
> - **One opaque layer:** $T_a=T_e$, $T_s=2^{1/4}T_e=303$ K (+48 K): too warm.
> - **Leaky layer** (absorptivity = emissivity $\varepsilon$): $T_a=2^{-1/4}T_s$, $T_s=T_e(1-\varepsilon/2)^{-1/4}$; OLR $=\sigma T_s^4(1-\varepsilon/2)$; Earth $\varepsilon=0.78$ ($T_a=242$ K, $\varepsilon_{\rm eff}=0.6$ as in CL04); Mars 0.15; Venus would need 1.98 (impossible).
> - **$N$ opaque layers:** $T_s=(N+1)^{1/4}T_e$ (303, 335, 360, 398 K…); ground hotter than the lowest layer (radiative discontinuity) ⇒ convection (CL09).
> - $\varepsilon=1-e^{-\tau}$: $\varepsilon=0.78\Leftrightarrow\tau=1.5$; $N$ layers $\approx1.2N$ optical depths.
> - **Feedbacks:** Planck (−, 0.27–0.30 K per W m⁻²), water vapour (+, $f\approx0.5$, ×2), ice–albedo (+), cloud (±). CO₂ doubling: $F=3.7$ W m⁻² ⇒ $\Delta\varepsilon=0.019$, no-feedback 1.1 K, with vapour 2.2 K.

## Practice
1. **Derive** the leaky-layer result (CL8.2) from the three balances and show that $T_a=2^{-1/4}T_s$.
2. **Numbers.** With $T_e=254.6$ K find $T_s$ and $T_a$ for $\varepsilon=0.5$ and $\varepsilon=0.9$.
3. **Earth.** Which $\varepsilon$ gives $T_s=288$ K? What are $G$, the back-radiation $\varepsilon\sigma T_a^4$ and the fraction of surface emission that escapes directly?
4. **Mars and Venus.** Compute $\varepsilon$ needed for Mars ($T_e=209.8$, $T_s=214$ K) and Venus ($T_e=226.6$, $T_s=737$ K). Why does the model fail for Venus?
5. **Layers.** Show by induction that $N$ opaque layers give $T_s=(N+1)^{1/4}T_e$. How many layers would reproduce $T_s=288$ K?
6. **Forcing.** Using $\Delta F=5.35\ln(C/C_0)$, find the forcing for $C=420$ ppm relative to 280 ppm, then the corresponding $\Delta\varepsilon$ and the no-feedback warming in the one-layer model.
7. **Feedback.** With $f_{\rm WV}=0.5$, $f_{\rm albedo}=0.1$, $f_{\rm cloud}=0.1$, $f_{\rm lapse}=-0.2$, find $\Lambda$ and the warming for $F=3.7$ W m⁻².
8. **Faint Sun.** What $\varepsilon$ would the one-layer model need for $T_s=273$ K when $S=0.7\times1361$ and $\alpha=0.3$?
9. **Interpretation.** Why can the one-layer model not tell you the *lapse rate* feedback? Which chapter does?

> [!example]- Solutions
> 1. Surface: $Q+\varepsilon\sigma T_a^4=\sigma T_s^4$; TOA: $Q=\varepsilon\sigma T_a^4+(1-\varepsilon)\sigma T_s^4$. Subtract: $2\varepsilon\sigma T_a^4=\varepsilon\sigma T_s^4$ ⇒ $T_a^4=T_s^4/2$. Then $Q=\sigma T_s^4[\varepsilon/2+1-\varepsilon]=\sigma T_s^4(1-\varepsilon/2)$ ⇒ $T_s=T_e(1-\varepsilon/2)^{-1/4}$.
> 2. $\varepsilon=0.5$: $T_s=273.6$ K, $T_a=230.0$ K. $\varepsilon=0.9$: $T_s=254.6\times(1/0.55)^{1/4}=254.6\times1.1612=295.6$ K, $T_a=248.6$ K.
> 3. $\varepsilon=2[1-(254.58/288)^4]=0.779$; $G=\varepsilon\sigma T_s^4/2=0.779\times390.1/2=152$ W m⁻²; back-radiation $=\varepsilon\sigma T_a^4=0.779\times0.5\times390.1=152$ W m⁻²; leak $=1-\varepsilon=0.22$.
> 4. Mars: $\varepsilon=2[1-(209.8/214)^4]=0.152$. Venus: $\varepsilon=2[1-(226.6/737)^4]=1.982>1$: impossible; the maximum is $2^{1/4}T_e=269$ K. Venus's atmosphere is optically thick ($\tau\sim10^2$, many layers) and absorbs sunlight in its clouds.
> 5. Layer $k$ opaque: upward flux just above it $=E_k$, downward just below it $=E_k$. Net upward flux $F$ at every interface gives $E_{k+1}-E_k=F$ with $E_1=F$ ⇒ $E_k=kF$; at the ground $\sigma T_s^4-E_N=F$ ⇒ $\sigma T_s^4=(N+1)F$. For $T_s=288$ K: $N+1=(288/254.58)^4=1.64$ ⇒ $N=0.64$: *less than one* opaque layer (a single leaky layer with $\varepsilon=0.78$ is the equivalent).
> 6. $\Delta F=5.35\ln(420/280)=5.35\times0.405=2.17$ W m⁻²; $\Delta\varepsilon=2\times2.17/390=0.011$; $\Delta T=2.17/3.3=0.66$ K.
> 7. $f=0.5+0.1+0.1-0.2=0.5$ ⇒ $\Lambda=\Lambda_P/0.5=2\times0.30=0.61$ K per W m⁻² ⇒ $\Delta T=2.2$ K.
> 8. $Q=0.7\times238.2=166.7$ W m⁻² ⇒ $T_e=(166.7/\sigma)^{1/4}=232.9$ K; $\varepsilon=2[1-(232.9/273)^4]=2[1-0.5297]=0.94$. The faint young Sun needs a nearly opaque greenhouse (or a lower albedo): a very strong requirement.
> 9. A single isothermal layer has no vertical structure, so no way to describe how warming changes the *decrease of temperature with height*; the lapse rate is set by convection and moist thermodynamics ([[CL09 Radiative-Convective Equilibrium]]).

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | idealisation; two temperatures; shortwave and longwave fluxes | [[climate_intro_L1_L6.pdf#page=61\|Argha L6 sl. 61–64]]; [[suhas notes.pdf#page=16\|Suhas notes pp.16–17]] | taught |
> | three balances; emissivity $\varepsilon<1$; Kirchhoff | [[climate_intro_L1_L6.pdf#page=65\|Argha L6 sl. 65–66]]; Suhas Model 2 | taught |
> | $\varepsilon=1$: $2\sigma T_a^4=\sigma T_s^4$ | [[climate_intro_L1_L6.pdf#page=67\|Argha L6 sl. 67]]; Suhas Model 1 | taught |
> | planets, thick Venus, internal heat, "many layers?" | [[climate_intro_L1_L6.pdf#page=68\|Argha L6 sl. 68]] | taught |
> | multi-layer model, radiative discontinuity | Suhas Model 3, [[suhas notes.pdf#page=18\|Suhas notes pp.18–19]] | taught |
> | feedback table (Planck, water vapour, ice–albedo, cloud) | [[suhas notes.pdf#page=19\|Suhas notes p.19]] | taught |
> | $N$-layer ladder $F,2F,\dots$; 303 K; convection onset | Wallace & Hobbs Ex. 4.8, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=138\|PDF pp.138–139]] | extra/book |
> | water-vapour feedback $f\approx0.5$; runaway | Wallace & Hobbs §10.3.2, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=464\|PDF p.464]] | extra/book |
> | exact grey $N$-layer solver; $G$; $\Delta\varepsilon$ for CO₂; $f_{\rm WV}$ estimate; consistency checks | computed here (`cl08_layers.py`); Myhre et al. (1998) for $5.35\ln(C/C_0)$ | extra/beyond |
>
> **Dropped as redundant:** Argha L6 (slides 61–68) and Suhas Models 1–2 derive the same one-layer results (the same balances, the same $T_s=2^{1/4}T_e$ and $T_s=(2/(2-\varepsilon))^{1/4}T_e$); the two are merged into §§2–3 and the redundant derivation of the atmosphere balance is stated once. The Suhas notes' separate "emission temperature" derivation was already merged in [[CL03 Radiation and Planetary Energy Balance]]. The AI notes `argha-climate.pdf` (secondary) agree with the slides on all formulas and identify $0.6=1-\varepsilon/2$ with $\varepsilon=0.8$.

**References.** Wallace, J. M. & Hobbs, P. V. (2006) *Atmospheric Science*, §4.3.6, Ex. 4.8, §10.3 · Myhre, G. et al. (1998) *Geophys. Res. Lett.* 25, 2715 · NASA Planetary Fact Sheet (planet data) · Manabe, S. & Wetherald, R. T. (1967) *J. Atmos. Sci.* 24, 241 (radiative–convective model with fixed relative humidity).
