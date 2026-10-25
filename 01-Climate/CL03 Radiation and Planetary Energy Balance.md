---
title: CL03 Radiation and Planetary Energy Balance
aliases: [CL03, Zero-D energy balance, Planetary energy balance]
subject: climate
type: chapter
chapter: 3
part: I
scope: [taught, extra-book, extra-beyond]
by: [argha, suhas-pre]
status: draft
prereq: ["[[CL02 Observing Global Temperature]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# CL03 · Radiation and Planetary Energy Balance

◀ [[CL02 Observing Global Temperature]] · [[Climate - Course Map|Course Map]] · [[CL04 Feedback and Multiple Steady States]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 global budget (Argha L3)
> - §2 Planck / Wien / Stefan–Boltzmann, shortwave vs longwave (Argha L3, Suhas pre-midsem)
> - §3 solar constant and the factor 4
> - §4 $T_e=255$ K, albedo values, the 33 K gap
> - §5 other planets, Jensen remark (Mercury)
> - §6 diurnal cycle of an airless slab (Argha L6)
>
> 🟡 **Extra · book**
> - Kirchhoff's law and emissivity (Wallace & Hobbs §4.3.5, in §2)
> - the same balance in *The Earth System* Ch. 3 (in §4)
>
> 🔵 **Extra · beyond**
> - derivation of $\sigma$ and the $T^4$ scaling argument (§2)
> - power-in-watts, emission height, emissivity form (worked examples in §4)
> - faint young Sun (§5)
> - linearisation, relaxation times and the analytic diurnal check (§6)

> [!key] After this chapter you can
> - turn the local energy budget of the atmosphere into a **global, steady, zero-dimensional** equation,
> - state [[Planck Law]], [[Wien Displacement Law]] and [[Stefan-Boltzmann Law]], explain **why** the spectrum has a peak, and say why sunlight is "shortwave" and Earth's glow "longwave",
> - derive $T_e=[S(1-\alpha)/4\sigma]^{1/4}\approx255$ K, explain every factor in it, and apply it to other planets,
> - say *why* the answer is wrong for Earth's surface (33 K too cold) and for Mercury (too hot), and how long a planet takes to respond.

## 1. From a local budget to a global one
<span class="scope-taught">taught</span> *Argha L3, slides 30–31*

Everything in the atmosphere is a state variable obeying a conservation law: three momentum components $(u,v,w)$, density $\rho$ (mass), humidity $q$ (water), pressure $P$ (ideal gas law, see [[Ideal Gas Law]]) and temperature $T$ (energy) [[climate_intro_L1_L6.pdf#page=30|(slide 30)]]. The temperature equation is a heat budget,

$$c_P\,\frac{\partial T}{\partial t}=\text{(net heat supplied by winds)}+\text{(condensation, absorption of radiation, …)} .$$

Only $\sim0.25\%$ of the atmosphere is water, yet it carries $\sim2.5\%$ of its enthalpy and drives evaporation, clouds, rain and a large share of poleward energy transport ([[CL10 Global Energy Balance and Meridional Structure]]).

To get the *simplest* model of the global-mean surface temperature $T_s$ take a planet with **no atmosphere** and average the budget over the whole surface and over a long time (this removes daily, seasonal and decadal cycles). Then [[climate_intro_L1_L6.pdf#page=31|(slide 31)]]

- $\mathrm{d}T_s/\mathrm{d}t\approx0$ (steady),
- winds only *move* energy around inside the planet, so the flow terms integrate to zero,
- geothermal heating is negligible (~0.09 W m⁻² against ~240 W m⁻²),
- what remains is **absorbed sunlight in, emitted thermal radiation out**:

$$\underbrace{C^*\frac{\mathrm{d}T_s}{\mathrm{d}t}}_{\approx0}=\text{(absorbed solar)}-\text{(emitted thermal)}\ \Rightarrow\ \text{absorbed solar}=\text{emitted thermal}.$$

> [!intuition] The leaky bucket
> Think of a bucket with a hole. Water pours in at a fixed rate (absorbed sunlight) and leaks out faster when the water is deeper (emission grows with temperature). The level settles where inflow = outflow, **whatever the starting level**: if it is too high it leaks faster than it fills; if too low, the reverse. Temperature plays the role of the water level, and that self-correction is what "stable steady state" will mean in §6 and [[CL04 Feedback and Multiple Steady States]]. The only difference: the planet's "hole" gets bigger as $T^4$.

This is the [[Zero-Dimensional Energy Balance Model]]. To use it we need the two radiation terms.

## 2. Thermal (blackbody) radiation
<span class="scope-taught">taught</span> *Argha L3, slides 32–34; Suhas pre-midsem notes p.14*

A body in thermal equilibrium with its radiation field emits the **Planck spectrum** [[climate_intro_L1_L6.pdf#page=32|(slide 32)]]:

$$I(\lambda,T)=\frac{2hc^{2}}{\lambda^{5}\left(e^{hc/\lambda k_BT}-1\right)}\qquad[\mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}}].$$

Read it as a product of three physical factors (the way the slide does): *(number of available photon states)* $\propto\mathrm{d}\lambda/\lambda^{4}$, times the *Bose–Einstein occupation* $1/(e^{hc/\lambda k_BT}-1)$, times the *energy per photon* $hc/\lambda$ ($\lambda^{-4}\cdot\lambda^{-1}=\lambda^{-5}$). Its limits:

| regime | form | name |
|---|---|---|
| $\lambda\to0$ | $I\sim e^{-hc/\lambda k_BT}/\lambda^{5}$ (exponential cut-off) | Wien tail |
| $\lambda\to\infty$ | $I\simeq 2ck_BT/\lambda^{4}$ (power law) | Rayleigh–Jeans |
| maximum | $\lambda_mT=b=2898\ \mu\mathrm m\,K$ | [[Wien Displacement Law]] |

> [!intuition] Why does the curve have a peak? (a budget argument)
> Each photon of wavelength $\lambda$ costs energy $hc/\lambda$, and the object can only spend about $k_BT$ per mode ("pocket change").
> - **Short wavelengths:** lots of modes available, but each photon costs $hc/\lambda\gg k_BT$: like paying with a banknote you almost never have. Occupation dies off exponentially ($e^{-hc/\lambda k_BT}$).
> - **Long wavelengths:** photons are cheap ($\ll k_BT$) but there are few modes per unit wavelength (the $\lambda^{-4}$ factor).
>
> The best compromise is a photon that costs about **five** $k_BT$ (the Wien root $x=4.965$). Numbers: at 288 K, $k_BT=0.0248$ eV, and a 10 µm photon has 0.124 eV $=5.0\,k_BT$ ✓; a 0.5 µm visible photon has 2.48 eV $=100\,k_BT$, so the Earth emits visible light with probability $\sim e^{-100}\approx10^{-44}$. That is why Earth is dark in the visible and the Sun (whose $k_BT\approx0.5$ eV) shines there.

> [!intuition] Why $T^4$? (a scaling argument, no integral)
> Raise the temperature and the whole curve slides to shorter wavelength ($\lambda_m\propto1/T$). The peak value is $B(\lambda_m)\propto\lambda_m^{-5}\propto T^{5}$ (from the $\lambda^{-5}$ prefactor), while the width of the bump is proportional to $\lambda_m\propto T^{-1}$. Area = height × width $\propto T^{5}\cdot T^{-1}=T^{4}$. Doubling the temperature therefore multiplies the emission by 16: this steepness is what makes a planet's thermostat work.

Integrating over all wavelengths and over the hemisphere above the surface gives the **total emitted flux**

$$F=\sigma T^{4},\qquad\sigma=5.67\times10^{-8}\ \mathrm{W\,m^{-2}K^{-4}}$$
(the [[Stefan-Boltzmann Law]]).

Sanity check: melting ice at 273 K emits $\sigma T^4=316$ W m⁻² ("~300", slide 33).

![[fig_cl03_planck_spectra.png|640]]
*Figure CL3.1. Planck spectra (each scaled to its own peak; the real Sun is ~$10^{8}$ times brighter per area). Wien peaks: 0.50 µm for the Sun, 10.1 µm at 288 K, 11.4 µm at 255 K. See: almost no overlap between the Sun's curve and Earth's curves.*

The Sun ($T\approx5800$ K) peaks in the visible, Earth ($\sim255$–$288$ K) in the thermal infrared, about **20× apart in wavelength**. The two spectra barely overlap, so radiation divides cleanly into **shortwave** (solar, $\lesssim4\ \mu$m) and **longwave** (terrestrial, $\gtrsim4\ \mu$m), each of which can be treated as its own stream and interacts with atmospheric gases in a different way ([[CL07 Optical Properties of the Atmosphere]]).

> [!pitfall] Which "peak"?
> The $\lambda_mT=2898\ \mu\mathrm{m\,K}$ above is the peak of the spectrum **per unit wavelength**. If you plot energy per *logarithmic* wavelength interval ($\lambda B_\lambda$) the peak moves to $\lambda T=3670\ \mu\mathrm{m\,K}$, i.e. 14.4 µm for 255 K and 0.64 µm for the Sun. The "~14 µm" quoted in the consolidated pre-midsem notes ([[suhas notes.pdf#page=14|suhas notes, p.14]]) comes from this second convention (or from scaling a 0.6 µm solar peak), not from $b=2898$. Both are fine; just don't mix them.

> [!extra-beyond]- 🔵 Extra (beyond): where $\sigma$ comes from
> The pre-midsem notes say the derivation of $\sigma$ "requires quantum statistical mechanics, out of scope", and the Argha slide only quotes $\sigma\propto k_B^4/h^3c^2$. The steps are short. Energy emitted per unit area into a hemisphere is $\pi\int_0^\infty I\,\mathrm d\lambda$. Substitute $x=hc/\lambda k_BT$, $\lambda=hc/(k_BTx)$, $\mathrm{d}\lambda=-\frac{hc}{k_BT}x^{-2}\mathrm dx$:
> $$F=\pi\int_0^\infty\frac{2hc^{2}}{\lambda^{5}(e^{x}-1)}\,\mathrm d\lambda=\frac{2\pi k_B^{4}T^{4}}{h^{3}c^{2}}\int_0^\infty\frac{x^{3}}{e^{x}-1}\,\mathrm dx=\frac{2\pi k_B^{4}}{h^{3}c^{2}}\cdot\frac{\pi^{4}}{15}\,T^{4}.$$
> So $\sigma=\dfrac{2\pi^{5}k_B^{4}}{15\,h^{3}c^{2}}=5.6704\times10^{-8}$ W m⁻² K⁻⁴ (numerically checked). The integral is $\int_0^\infty x^3/(e^x-1)\,\mathrm dx=\Gamma(4)\zeta(4)=6\cdot\pi^4/90$ (expand $1/(e^x-1)=\sum_{n\ge1}e^{-nx}$ and integrate term by term: $\sum_n 3!/n^4$). See also [[Planck Law]] and [[Blackbody Radiation]].

> [!extra-book]+ 🟡 Extra (book): emissivity and Kirchhoff's law
> A real surface emits $\varepsilon\sigma T^4$ with emissivity $0<\varepsilon\le1$; **Kirchhoff's law** says emissivity equals absorptivity at each wavelength, $\varepsilon_\lambda=a_\lambda$ (Wallace & Hobbs §4.3.5, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=138|p.121]]). The Argha deck only uses it implicitly when the atmosphere is "not an ideal blackbody, $\epsilon<1$" ([[climate_intro_L1_L6.pdf#page=68|slide 68]], [[CL08 Greenhouse Models]]).
>
> **Intuition:** whatever is good at absorbing a colour is good at emitting it. A black pot heats and cools quickly; a polished thermos is slow both ways. Without this symmetry thermal equilibrium would be impossible: a black object next to a shiny one would end up at different temperatures, violating the second law ([[Thermodynamics - Course Map]]).

## 3. The solar constant and the geometry factor 4
<span class="scope-taught">taught</span> *Argha L3, slide 35; Suhas pre-midsem notes p.14*

The Sun radiates $\sigma T_\odot^4$ per unit area of its surface. At distance $d$ this is spread over a sphere, so the irradiance on a surface facing the Sun is [[climate_intro_L1_L6.pdf#page=35|(slide 35)]]

$$S=\sigma T_\odot^{4}\,\frac{4\pi R_\odot^{2}}{4\pi d^{2}}=\sigma T_\odot^4\Big(\frac{R_\odot}{d}\Big)^{2}\approx1361\ \mathrm{W\,m^{-2}}.$$

(Check: $T_\odot=5772$ K, $R_\odot=6.957\times10^8$ m, $d=1.496\times10^{11}$ m give 1361.2 W m⁻².) See [[Solar Constant]].

> [!verify] 1361 vs 1367
> The Argha slides use $S=1361$ W m⁻². The pre-midsem notes use the older $S_0=1367$ W m⁻². The lower figure is the modern one: space radiometers before 2008 suffered from scattered light, and the SORCE/TIM instrument measured $1360.8\pm0.5$ W m⁻² at the 2008 solar minimum (Kopp & Lean 2011). Effect on the result: $T_e=254.9$ K vs $254.6$ K for $\alpha=0.30$, a 0.3 K difference. **This vault uses 1361.**

Earth intercepts the beam on its **cross-sectional disc**, area $\pi a^2$ ($a$ the Earth radius), so the intercepted power is $S\pi a^{2}$. Rotation spreads it over the whole sphere, $4\pi a^{2}$. A fraction $\alpha$ (the [[Albedo]]) is reflected. The shortwave absorbed per unit area of surface, averaged over the globe, is therefore

$$\frac{\pi a^{2}S(1-\alpha)}{4\pi a^{2}}=\frac{S(1-\alpha)}{4}\approx\frac{1361\times0.70}{4}=238\ \mathrm{W\,m^{-2}}.$$

> [!intuition] Why 4? Shadows and sphere
> Hold a ball in a beam of parallel light. The beam it *catches* is the size of the ball's **shadow**: a disc, $\pi a^2$. But the ball has a *whole surface* of area $4\pi a^2$ to share that light and to radiate from, day side and night side alike. The surface is exactly 4 times the shadow (Archimedes: the area of a sphere is four times that of its great circle). So **average sunlight per unit surface = $S/4$**: the tropics at noon get $\sim S$, the night side gets 0, the pole gets a glancing fraction, and the global mean is a quarter.

> [!derivation]- The same factor from averaging $\cos\theta$
> At a point where the Sun is at angle $\theta$ from the zenith the flux is $S\cos\theta$ (only on the lit side), so
> $$\frac{1}{4\pi a^2}\int_{\text{lit}}S\cos\theta\,\mathrm dA=\frac{S}{4\pi}\int_0^{2\pi}\!\!\int_0^{\pi/2}\cos\theta\sin\theta\,\mathrm d\theta\,\mathrm d\phi=\frac S4 .$$
> ($\int_0^{\pi/2}\cos\theta\sin\theta\,\mathrm d\theta=\tfrac12$, times $2\pi$, over $4\pi$.)

> [!example] Earth's energy budget in watts
> Intercepted: $S\pi a^2=1361\times1.275\times10^{14}=1.74\times10^{17}$ W (174 PW). Reflected (30 %): 52 PW. **Absorbed: 121 PW** $=1.21\times10^{17}$ W. World primary energy use is ≈ 600 EJ/yr ≈ 19 TW (Energy Institute 2023), so the Earth absorbs sunlight **about 6,400 times faster** than humanity uses all fuels combined, and must radiate the same 121 PW back out.

## 4. Equation for $T_s$ and the effective temperature
<span class="scope-taught">taught</span> *Argha L3, slides 35–36; Suhas pre-midsem notes p.14*

In steady state the planet must emit exactly what it absorbs, $\sigma T_s^4$ per unit area [[climate_intro_L1_L6.pdf#page=36|(slide 36)]]:

$$\boxed{\frac{S(1-\alpha)}{4}=\sigma T_e^{4}}\quad\Longrightarrow\quad\boxed{T_e=\Big[\frac{S(1-\alpha)}{4\sigma}\Big]^{1/4}}\tag{CL3.1}$$

With $S=1361$ W m⁻² and the global-mean (Bond) albedo $\alpha=0.30$:

$$T_e=\Big[\frac{238.2}{5.67\times10^{-8}}\Big]^{1/4}=\mathbf{254.6\ K}\approx255\ \mathrm K .$$

Three remarks:
1. The planet's radius cancelled: $T_e$ depends only on $S$ (i.e. distance) and $\alpha$.
2. $T_e$ is the temperature of the **emitting level seen from space** ([[Effective Emission Temperature]]). Earth's actual global-mean surface temperature is 288 K, so the real surface is **33 K warmer** than this airless-planet estimate. That gap is the [[Greenhouse Effect]] (slide 36, derived in [[CL08 Greenhouse Models]]).
3. Albedo depends strongly on the surface: snow ~0.9, ice ~0.4, bare ground ~0.2, ocean ~0.1 (slide 36); more finely, ocean 2–10 %, forest 6–18 %, soil 10–20 %, desert sand 35–45 %, thick cloud 60–70 %, fresh snow 75–95 % (pre-midsem notes). The global value 0.30 is itself dynamic, depending on $T_s$, on the angle of the Sun and on clouds. This dependence is the subject of [[CL04 Feedback and Multiple Steady States]].

> [!intuition] What an alien telescope sees
> From far away you cannot see the surface, only the infrared glow that escapes to space. That glow has the same total power as a 255 K blackbody, so to the alien the Earth "is" a 255 K disc. The 288 K you feel at the surface is higher because the glow is released from **higher, colder** air, not from the ground. Going up in the atmosphere cools you, so the level that radiates at 255 K must be above you.

> [!example] Worked examples
> **(a) Earth with Venus's albedo.** $\alpha=0.77$: $T_e=[1361\times0.23/(4\sigma)]^{1/4}=193$ K, 62 K colder. Clouds that raise $\alpha$ from 0.30 to 0.77 would freeze the planet (and Venus is hot only because of its 92-bar CO₂ greenhouse).
>
> **(b) Height of the emission level.** A tropospheric lapse rate of 6.5 K km⁻¹ and a surface at 288 K reach 255 K at $z\approx(288-255)/6.5\approx5$ km. Radiative-transfer models give 5–6 km. *(🔵 my arithmetic.)*
>
> **(c) Emissivity form.** For a grey surface, $S(1-\alpha)/4=\varepsilon\sigma T^4$ gives $T=T_e\,\varepsilon^{-1/4}$. With $\varepsilon=0.6$: $T=254.6\times1.136=289$ K, which is nearly the real 288 K. This is the number the Argha slide uses in the steady-state plot of [[CL04 Feedback and Multiple Steady States]].

> [!extra-book]+ 🟡 Extra (book): same derivation, different notation
> *The Earth System* (Kump, Kasting & Crane) develops the same balance in Chapter 3, "Global Energy Balance" ([[vdoc.pub_the-earth-system.pdf#page=50|PDF p.50]]), including the Earth's energy-budget diagram and the effect of clouds on the radiation budget ([[vdoc.pub_the-earth-system.pdf#page=59|p.51]]). Wallace & Hobbs write the emission temperature as $T_E$ in §4.3 ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=137|p.120]]).

## 5. Other planets
<span class="scope-taught">taught</span> *Argha L3, slides 37–39; Suhas pre-midsem notes p.14*

Apply (CL3.1) to the other solar-system planets [[climate_intro_L1_L6.pdf#page=37|(slides 37–39)]]. Data below are NASA Planetary Fact Sheet values (solar irradiance $S$, Bond albedo $\alpha$, measured temperature); $T_e$ is recomputed from (CL3.1).

| Planet | $S$ (W m⁻²) | $\alpha$ | $T_e$ (K) | measured $T$ (K) | gap (K) |
|---|---|---|---|---|---|
| Mercury | 9083 | 0.068 | 440 | 440 (NASA) / ~340 | see below |
| Venus | 2601 | 0.77 | 227 | 737 (surface) | +510 |
| Earth | 1361 | 0.294 | 255 | 288 | +33 |
| Mars | 586 | 0.250 | 210 | 214 | +4 |
| Jupiter | 50.3 | 0.343 | 110 | 165 (at 1 bar) | internal heat |
| Saturn | 14.8 | 0.342 | 81 | 134 (at 1 bar) | internal heat |

![[fig_cl03_planets.png|600]]
*Figure CL3.2. Prediction vs measurement. See: the bars track each other across a factor of 10 in $T$ (the pattern is right) but every atmosphere-bearing planet sits above its blue bar. Source: NASA Planetary Fact Sheet (nssdc.gsfc.nasa.gov/planetary/factsheet), accessed 2026-10-23; script `fig_cl03_planets.py`.*

The pattern is captured, and the misses are informative:

- **Mars is best** (+4 K): a thin atmosphere (a few mbar), mostly CO₂, almost no water vapour, so a greenhouse effect of only ~5 K (slide 39).
- **Venus** is wildly warmer than $T_e$: ~92 bar of 97 % CO₂ (slide: "~100 bar"). Its circulation is so efficient that the surface is nearly isothermal despite the 243-day rotation (slide 38).
- **Jupiter and Saturn** are the opposite kind of failure: they radiate **more** than they absorb, so there is an *internal* source (primordial heat, radioactivity, tidal dissipation, gravitational settling; slide 37). The slide quotes ~7 W m⁻² absorbed and ~14 W m⁻² emitted for Jupiter. These follow the revised Bond albedo $\alpha=0.503\pm0.012$ of Li et al. (2018), with internal heat $7.5\pm0.2$ W m⁻² (previous values 0.343 and 5.4 W m⁻²). With it, absorbed $=50.3\times0.497/4=6.2$ W m⁻² and emitted $\approx6.2+7.5=13.7$ W m⁻² ✓. Using the old albedo, as the fact-sheet table above does, understates the internal heat.
- **Mercury** is *over*-predicted in the slide's version (slide 39). Mercury rotates slowly (58.6 d sidereal, 3:2 spin–orbit resonance), has no axial tilt and no atmosphere to move heat, so the equator–pole contrast is ~5× that of Earth. Then the day side is hot, the night side cold, and **the uniform-temperature assumption fails**: see the next boxes.

> [!verify] Mercury's "mean temperature"
> The fact sheet lists 440 K (167 °C) as Mercury's mean, which equals $T_e$ by coincidence of definition (it is nearer the sunlit-equator value), while many references quote a global mean of ~340 K. The slide's claim "over-estimate" holds for the latter. Check the definition before comparing.

> [!intuition] Why a lumpy planet looks colder than the formula says
> Imagine two rooms, one at 250 K and one at 350 K. The *average temperature* is 300 K, but the hot room radiates so much more (a factor $(350/250)^4\approx3.8$) that the pair radiate like a uniform 312 K object. The hot spots "win" in the total because $T^4$ rises ever more steeply. So if you *force* a planet to balance with a uniform $T$ you need a **higher** $T$ than the real mean: the formula over-estimates the temperature (Mercury). Conversely, a planet with efficient heat transport (Venus) is nearly uniform and obeys the formula well.

> [!key] $\langle T^4\rangle>\langle T\rangle^4$
> Emission goes as $T^4$, a **convex** function, so by [[Jensen Inequality]] the area-mean of $T^4$ exceeds the fourth power of the area-mean $T$. Half at 250 K, half at 350 K has $\bar T=300$ K but $\langle T^4\rangle^{1/4}=311.8$ K, i.e. 17 % more emission than a uniform 300 K body. For small contrast $T=T_0(1\pm\epsilon)$, $\langle T^4\rangle^{1/4}\approx T_0(1+\tfrac32\epsilon^2)$ (Practice 4).

> [!extra-beyond]- 🔵 Extra (beyond): the faint young Sun
> Stellar models say the Sun was ~30 % fainter 4 Gyr ago ($S\approx0.7\times1361$). Keeping $\alpha=0.30$, (CL3.1) gives $T_e\approx233$ K and, adding today's 33 K, a surface at ~266 K: *frozen*. Yet there is evidence for liquid water 3.8 Gyr ago. Resolving this [[Faint Young Sun Paradox]] needs a stronger greenhouse effect, and it is exactly why the ice–albedo feedback of [[CL04 Feedback and Multiple Steady States]] and the long-term carbon-cycle thermostat (see [[Snowball Earth]]) matter. Cross-subject link: [[Evolution of Earth and Life - Course Map]].

## 6. How fast does the planet respond? Relaxation and the diurnal cycle
<span class="scope-taught">taught</span> *Argha L6, slides 69–71 (the diurnal ODE and its plot)* · <span class="scope-extra-beyond">extra · beyond</span> *linearisation, relaxation times and the analytic check: derived here*

Eq. (CL3.1) is a *steady* state. To see the approach to it, keep the heat capacity per unit area $C=\rho Vc$ [J m⁻² K⁻¹] of the surface layer. Argha returns to this "no-atmosphere case" at the end of L6 [[climate_intro_L1_L6.pdf#page=70|(slides 69–71)]]; it belongs here because the model is identical.

$$C\frac{\mathrm dT}{\mathrm dt}=\frac{S(1-\alpha)}{4}-\sigma T^{4}.$$

**Linearise** about $T_e$ with $T=T_e+\theta$: $\sigma T^4\approx\sigma T_e^4+4\sigma T_e^3\theta$, so
$$\frac{\mathrm d\theta}{\mathrm dt}=-\frac{\theta}{\tau},\qquad\tau=\frac{C}{4\sigma T_e^{3}}.$$
The steady state is **stable** (a warm perturbation emits more than it gains and cools). The time constant is [[Relaxation Time]]; with $4\sigma T_e^3=3.76$ W m⁻² K⁻¹:

| layer | $C$ (J m⁻² K⁻¹) | $\tau$ |
|---|---|---|
| soil slab of the slide: $1500\times0.20\times2500$ | $7.5\times10^{5}$ | 2.3 days |
| ocean mixed layer, 50 m | $2.0\times10^{8}$ | 1.7 years |
| whole atmosphere ($c_Pp_0/g$) | $1.0\times10^{7}$ | ~1 month |

> [!intuition] The bucket again: bigger bucket, slower response
> $\tau$ is the "size of the bucket" ($C$, how much heat it takes to warm the layer by one degree) divided by the "size of the hole" ($4\sigma T^3$, extra emission per degree). A thin dry soil layer is a thimble: it follows the Sun within hours. The ocean is a swimming pool: its temperature barely reacts within a day but integrates changes over years. This is why continents have large daily and seasonal swings and the sea coasts are mild, and why the climate at any moment lags its eventual equilibrium ([[CL04 Feedback and Multiple Steady States]]).

**The diurnal problem.** At the equator on an equinox the Sun's elevation gives incoming flux $S(1-\alpha)\max(\sin\omega t,0)$ with $\omega=2\pi/86400$ s⁻¹, so (slide 70, $\alpha=0.31$, $\rho Vc=7.5\times10^5$ J m⁻² K⁻¹)

$$\rho Vc\,\frac{\mathrm dT}{\mathrm dt}=(1-\alpha)S\,\Theta(\sin\omega t)\sin\omega t-\sigma T^{4}.$$

![[fig_cl03_diurnal.png|560]]
*Figure CL3.3. Numerical solution (script `fig_cl03_diurnal.py`, 12 days of spin-up). See: the temperature (bottom) peaks at 279 K about 10.6 h after sunrise, i.e. 4.6 h **after** local noon (red dotted line), and bottoms out at 260 K just after dawn.*

> [!intuition] Why is the afternoon hotter than noon?
> A bathtub: the tap (sunlight) is at full flow at noon, but the water level keeps **rising** as long as the tap flow exceeds the drain flow (emission), and that stays true for hours after noon. The level peaks at the moment the two flows cross (when absorbed = emitted), which is in the afternoon, not when the tap is widest. The bigger the tub ($C$), the later and smaller the peak.

A quick analytic check explains both numbers:

- The time-mean absorbed flux of a half-rectified sine is $(1-\alpha)S/\pi=299$ W m⁻², which sets the mean emission, so $\langle T^4\rangle^{1/4}=(299/\sigma)^{1/4}=269.5$ K ✓ (numerical mean 269.2 K).
- The first harmonic of the forcing has amplitude $\tfrac12(1-\alpha)S=470$ W m⁻²; the response of $C\,\mathrm d\theta/\mathrm dt=-4\sigma T^3\theta+F_1\sin\omega t$ has amplitude $F_1/\sqrt{(4\sigma T^3)^2+(C\omega)^2}\approx F_1/C\omega=470/54.5\approx8.6$ K, against ±9.5 K numerically ✓. Since $C\omega\gg4\sigma T^3$, emission barely matters on a 1-day timescale: the swing is heat-capacity limited.

> [!example] Changing the heat capacity (numerical solutions of the same ODE)
> | $C$ (J m⁻² K⁻¹) | peak $T$ (K) | min $T$ (K) | peak time after sunrise |
> |---|---|---|---|
> | $7.5\times10^{4}$ (thin, dry) | 336 | 194 | 8.7 h |
> | $7.5\times10^{5}$ (slide) | 279 | 260 | 10.6 h |
> | $7.5\times10^{6}$ (wet, deep) | 268.5 | 266.5 | 10.8 h |
>
> Smaller $C$: bigger swing, earlier peak. Larger $C$: smooth and nearly constant at $\langle T^4\rangle^{1/4}$.

> [!pitfall] "Right pattern, but maybe wrong magnitude" (slide 71)
> The slide poses this on purpose: which terms are missing? Real land surfaces have an effective heat capacity that depends on frequency (a conduction layer of depth $\sqrt{2\kappa/\omega}$ rather than a fixed slab), exchange **sensible and latent heat** with the air, lose heat by winds (the atmosphere is not a passive lid), have $\varepsilon<1$, clouds that change both $\alpha$ and the downward longwave, and a Sun angle that depends on latitude and season. Each is a topic of the chapters ahead.

## 7. Where this leaves us
<span class="scope-taught">taught</span> *synthesis of Argha L3–L6*

- The balance (CL3.1) correctly orders the planets and gives Earth $T_e\approx255$ K, **but** the surface is 33 K warmer: the atmosphere must act on the outgoing longwave stream → [[CL07 Optical Properties of the Atmosphere]], [[CL08 Greenhouse Models]].
- $\alpha$ was taken constant. If it depends on $T$ the same equation has more than one solution and its sensitivity to a forcing changes → [[CL04 Feedback and Multiple Steady States]].
- The model has no latitude. Where the energy goes and how it is redistributed is the business of [[CL10 Global Energy Balance and Meridional Structure]] onwards.

## Map of this chapter
> [!connection] How CL03 connects
> **Builds on:** [[CL01 Earth as a System]] · [[CL02 Observing Global Temperature]]
> **Leads to:** [[CL04 Feedback and Multiple Steady States]] (sensitivity, stability) · [[CL07 Optical Properties of the Atmosphere]] and [[CL08 Greenhouse Models]] (the 33 K) · [[CL10 Global Energy Balance and Meridional Structure]] (latitude)
> **Concepts:** [[Blackbody Radiation]] · [[Planck Law]] · [[Wien Displacement Law]] · [[Stefan-Boltzmann Law]] · [[Solar Constant]] · [[Albedo]] · [[Effective Emission Temperature]] · [[Zero-Dimensional Energy Balance Model]] · [[Greenhouse Effect]] · [[Jensen Inequality]] · [[Relaxation Time]] · [[Faint Young Sun Paradox]]
> **Other subjects:** [[Thermodynamics - Course Map]] (blackbody, Kirchhoff) · [[Quantum Mechanics - Course Map]] (quantisation, photon statistics) · [[Fixed Points and Linear Stability]] (stability) · [[Evolution of Earth and Life - Course Map]] (young Sun) · [[Probability - Course Map]] (Jensen)

> [!connection] Thermodynamics and quantum mechanics
> Planck's law is the founding result of quantum theory and the standard application of Bose–Einstein statistics to photons. The underlying quantisation is the subject of [[Quantum Mechanics - Course Map]]; the thermodynamic side (Kirchhoff, entropy of radiation, $u\propto T^4$) is in [[Thermodynamics - Course Map]].

> [!connection] Dynamical systems
> "Is this steady state stable? Perturb and see" is the linear stability analysis of [[Fixed Points and Linear Stability]], the same mathematics that decides whether a population settles at its carrying capacity ([[Ecology and Evolution - Course Map]]). The sensitivity $\partial T/\partial F$ computed in the next chapter is [[Linearisation and Sensitivity]].

## Summary
> [!summary] Cheat-sheet
> - **Planck:** $B_\lambda\propto\lambda^{-5}/(e^{hc/\lambda kT}-1)$; **Wien** $\lambda_mT=2898$ µm K; **SB** $F=\sigma T^4$, $\sigma=5.67\times10^{-8}$.
> - Sun peaks at 0.5 µm (shortwave), Earth at ~10 µm (longwave): ~20× apart, no overlap.
> - $S=\sigma T_\odot^4(R_\odot/d)^2=1361$ W m⁻²; global mean $=S/4=340$ W m⁻² (disc vs sphere).
> - **$T_e=[S(1-\alpha)/4\sigma]^{1/4}=255$ K**; actual $T_s=288$ K, so greenhouse $=33$ K; radius cancels.
> - Mars +4 K, Earth +33 K, Venus +510 K; Jupiter/Saturn have internal heat; Mercury over-predicted ($\langle T^4\rangle>\langle T\rangle^4$).
> - $\Delta T_e=-\tfrac{T}{4}\tfrac{\Delta\alpha}{1-\alpha}$ ($\Delta\alpha=0.01\Rightarrow-0.9$ K).
> - Relaxation $\tau=C/(4\sigma T^3)$: slab 2.3 d, 50 m ocean 1.7 yr; diurnal peak lags noon.

## Practice
1. **Mars.** Use $S=586$ W m⁻² and $\alpha=0.25$ to obtain $T_e$, then compute the greenhouse increment against 214 K.
2. **Black sphere at 1 AU.** Show $T=[S/4\sigma]^{1/4}=278$ K, so $T_e=278\,(1-\alpha)^{1/4}$ K. Check Mars at 1.52 AU.
3. **Albedo error.** By how much does $T_e$ change if $\alpha$ goes from 0.30 to 0.31?
4. **Jensen.** A planet has two halves at $T_0(1\pm\epsilon)$. Show that $\langle T^4\rangle^{1/4}\approx T_0\,[1+\tfrac32\epsilon^2]$ for small $\epsilon$.
5. **Relaxation time.** Compute $\tau$ for a 4 km deep ocean assumed fully mixed. Is the "equilibrium" warming under a forcing reached by 2100?
6. **Diurnal.** Why does a *drier* (smaller $C$) surface have a larger afternoon peak? Predict the amplitude if $C$ is 10× smaller using $F_1/\sqrt{(4\sigma T^3)^2+(C\omega)^2}$ and say why it fails.
7. **Wien.** At what wavelength does a 5772 K body peak? Which colour? What temperature peaks at 10 µm?
8. **Photon cost.** Show a 0.5 µm photon is worth ≈ 100 $k_BT$ at 288 K.

> [!example]- Solutions
> 1. $T_e=[586\times0.75/(4\sigma)]^{1/4}=209.8$ K → $214-209.8=+4$ K.
> 2. $S=1361$: $(1361/(4\times5.67\times10^{-8}))^{1/4}=278.3$ K. Mars: $278.3\times0.75^{1/4}/\sqrt{1.524}=278.3\times0.9306/1.2345=209.8$ K ✓.
> 3. $\Delta T_e=-\tfrac{254.6}{4}\cdot\tfrac{0.01}{0.70}=-0.91$ K.
> 4. $\langle(1+\delta)^4\rangle$ with $\delta=\pm\epsilon$ equally likely: $1+6\epsilon^2+\epsilon^4$; fourth root $\approx1+\tfrac64\epsilon^2=1+\tfrac32\epsilon^2$.
> 5. $C=\rho cH=1025\times3990\times4000=1.6\times10^{10}$ J m⁻² K⁻¹; $\tau=C/3.76=4.4\times10^{9}$ s $\approx140$ yr. No: the deep ocean takes centuries, so the equilibrium response is **not** reached by 2100 (and positive feedback lengthens $\tau$ further).
> 6. Smaller $C$ heats faster during the day and cools faster at night. Linear estimate: $C=7.5\times10^4$: $C\omega=5.45$, $\sqrt{4.46^2+5.45^2}=7.0$ ⇒ ±67 K, a swing as large as the mean itself, so the linearisation fails. The numerical solution gives 336/194 K (±71 K around a mean of 256 K), confirming a very large swing.
> 7. $b/T=2898/5772=0.502$ µm (blue-green); $T=2898/10=290$ K.
> 8. $E=hc/\lambda=1239.84\ \mathrm{eV\,nm}/500\ \mathrm{nm}=2.48$ eV; $k_B\cdot288\ \mathrm K=0.0248$ eV; ratio $=99.9$.

## PDF handout
Formula sheet, derivations and worked numbers for CL03–CL04 as a printable two-page LaTeX PDF: [[climate-part1-energy-balance-handout.pdf]].

![[climate-part1-energy-balance-handout.pdf#page=1&height=460]]

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | state variables, global-average budget | [[climate_intro_L1_L6.pdf#page=30\|Argha L3 sl. 30–31]] | taught |
> | Planck, Wien, RJ, $\sigma T^4$, shortwave/longwave | [[climate_intro_L1_L6.pdf#page=32\|Argha L3 sl. 32–34]]; [[suhas notes.pdf#page=14\|Suhas notes p.14]] | taught |
> | $S$, factor 4, $T_e=255$ K, albedo values | [[climate_intro_L1_L6.pdf#page=35\|Argha L3 sl. 35–36]]; [[suhas notes.pdf#page=14\|Suhas notes p.14]] | taught |
> | planets, Jensen remark | [[climate_intro_L1_L6.pdf#page=37\|Argha L3 sl. 37–39]] | taught |
> | diurnal transient | [[climate_intro_L1_L6.pdf#page=70\|Argha L6 sl. 69–71]] | taught |
> | linearised relaxation time, analytic diurnal check, $C$ sweep | derived here | extra/beyond |
> | derivation of $\sigma$; $T^4$ scaling; photon-cost intuition | derived here | extra/beyond |
> | power in watts, emission height, emissivity form | derived here; Energy Institute (2023) | extra/beyond |
> | Kirchhoff's law | Wallace & Hobbs §4.3.5 | extra/book |
> | Earth System Ch. 3 parallel treatment | Kump et al. | extra/book |
> | faint young Sun | standard result; Kopp & Lean (2011) for $S$ | extra/beyond |
> | NASA planetary data | NASA Planetary Fact Sheet; Li et al. (2018, *Nat. Commun.* 9:3709) for Jupiter | extra/beyond |
>
> **Dropped as redundant:** the pre-midsem notes' separate derivation of $T_e$ (identical to Argha's) and Argha's two repeats of the "no atmosphere" slide 31/36 equation. Both instructors' versions are merged in §§3–4.

**References.** Kopp, G. & Lean, J. L. (2011) *Geophys. Res. Lett.* 38, L01706 · Li, L. et al. (2018) *Nat. Commun.* 9, 3709 · NASA Planetary Fact Sheet, nssdc.gsfc.nasa.gov/planetary/factsheet · Wallace & Hobbs (2006) *Atmospheric Science*, §4.3 · Energy Institute (2023) *Statistical Review of World Energy*.
