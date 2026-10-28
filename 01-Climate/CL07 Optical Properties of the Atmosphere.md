---
title: CL07 Optical Properties of the Atmosphere
aliases: [CL07, Atmospheric optics, Absorption and scattering]
subject: climate
type: chapter
chapter: 7
part: III
scope: [taught, extra-book, extra-beyond]
by: [argha, suhas-pre]
status: draft
prereq: ["[[CL06 Hydrostatic Balance and Vertical Structure]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# CL07 · Optical Properties of the Atmosphere

◀ [[CL06 Hydrostatic Balance and Vertical Structure]] · [[Climate - Course Map|Course Map]] · [[CL08 Greenhouse Models]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**
> - §1 what can happen to a beam (Argha L5 sl. 56)
> - §2 Beer–Lambert law and optical depth (sl. 56 derivation)
> - §3 scattering and "why is the sky blue, red or grey?" (sl. 56, Fig. 4.11)
> - §4 absorption needs a transition; N₂/O₂ vs greenhouse gases (sl. 57)
> - §5 shortwave spectrum below and above the atmosphere (sl. 58)
> - §6 longwave spectrum, windows (sl. 59; Suhas pre-midsem notes p.15)
>
> 🟡 **Extra · book**
> - Wallace & Hobbs §4.4: size parameter and Mie scattering, photoionisation and photodissociation, $E=E_o+E_v+E_r$, Doppler and Lorentz line shapes (boxes in §3, §4 and §7)
>
> 🔵 **Extra · beyond**
> - why Rayleigh scattering goes as $\lambda^{-4}$ (§3)
> - the sunset worked example (§3)
> - CO₂ and H₂O vibration modes and the dipole selection rule, group theory (§4)
> - band fractions of the 288 K spectrum (§6)
> - emission, Kirchhoff and $\varepsilon=1-e^{-\tau}$ (§6)
> - what fraction of the greenhouse effect each gas supplies (§7)

> [!key] After this chapter you can
> - write the **Beer–Lambert law**, define **optical depth** $\tau$, and say what transmitted fraction goes with $\tau=0.1,\,1,\,3$,
> - explain **why the sky is blue, sunsets are red and clouds are white** with one number: the size parameter $x=2\pi r/\lambda$,
> - say **why N₂ and O₂ are transparent to infrared but H₂O, CO₂, O₃, CH₄ are not**, using energy levels and the dipole rule,
> - read the **shortwave and longwave absorption spectra** (UV ozone cut, visible window, CO₂ 15 µm band, 8–12 µm window) and give the fraction of Earth's emission that each part of the spectrum carries,
> - connect the optical depth of a layer to its **absorptivity/emissivity** $\varepsilon=1-e^{-\tau}$, the parameter of [[CL08 Greenhouse Models]].

## 1. What can happen to light in the atmosphere?
<span class="scope-taught">taught</span> *Argha L5, slide 56 ("Atmospheric gases/particles absorb and/or scatter radiation depending on wavelength, size, …")*

In [[CL03 Radiation and Planetary Energy Balance]] and [[CL04 Feedback and Multiple Steady States]] the atmosphere was a black box with one number, an emissivity $\varepsilon$. To understand that number, and why it differs between sunlight and Earth's glow, we have to open the box. A beam of radiation of wavelength $\lambda$ crossing a layer of air can

| fate | what happens to the photon | effect on the energy budget |
|---|---|---|
| **transmitted** | passes through untouched | none |
| **absorbed** | energy goes into the molecule (internal energy → heat by collisions, or re-emission later) | heats the air; later re-emitted in all directions |
| **scattered** | direction changes, wavelength unchanged | no heating; redirects light: some of it back to space (a contribution to the [[Albedo]]) |
| **emitted** (the reverse) | the air itself radiates, by Kirchhoff's law as efficiently as it absorbs | cools the air; adds to the outgoing glow |

Scattering and absorption together are called **extinction**. The slide poses the question that scattering answers: *why does the sky sometimes appear blue, red or grey?* (§3).

![[CL07 Photon Fates.svg|640]]
*Figure CL7.1. The four things that can happen to a beam in a layer. See: absorption and scattering both remove light from the beam, but only absorption heats the air. Editable version: [[CL07 Photon Fates.excalidraw]].*

> [!connection] Where this goes
> Extinction in the shortwave decides how much sunlight reaches the ground (the idealisation "transparent to shortwave" of [[CL08 Greenhouse Models]]); extinction in the longwave decides how much of the ground's glow escapes to space (the idealisation "opaque to longwave"). Both idealisations are *rough*, and the rest of this chapter says how rough.

## 2. Extinction of a beam: the Beer–Lambert law
<span class="scope-taught">taught</span> *Argha L5, slide 56 (the derivation is on the slide); Wallace & Hobbs §4.4–4.5.1, Eq. 4.16*

Consider a beam of monochromatic intensity $I_\lambda$ travelling a path element $\mathrm ds$ through air containing $N$ absorbers/scatterers per unit volume, each presenting an area (cross-section) $\sigma$ with an efficiency $K_\lambda$. The fraction removed is proportional to how many targets it meets, so ([[climate_intro_L1_L6.pdf#page=56|slide 56]]; W&H Eq. 4.16)

$$\mathrm dI_\lambda=-I_\lambda\,K_\lambda N\sigma\,\mathrm ds .$$

Separate variables and integrate along a path of length $s$:

$$\int_{I_{\lambda,0}}^{I_\lambda}\frac{\mathrm dI'}{I'}=-K_\lambda N\sigma\int_0^s\mathrm ds'\ \Rightarrow\ \ln\frac{I_\lambda}{I_{\lambda,0}}=-K_\lambda N\sigma\,s\ \Rightarrow\ \boxed{I_\lambda(s)=I_{\lambda,0}\,e^{-\tau_\lambda}},\quad\tau_\lambda=\int_0^sK_\lambda N\sigma\,\mathrm ds' .\tag{CL7.1}$$

$\tau_\lambda$ is the **optical depth** (dimensionless): the path integral of the extinction coefficient. If the concentration varies along the path, $\tau=\int(\text{extinction coefficient})\,\mathrm ds$. Wallace & Hobbs also write the extinction coefficient in terms of the **mass absorption coefficient** $k$ (m² kg⁻¹) and the absorber mass mixing ratio $r$: $\mathrm dI=-I\,\rho\,r\,k\,\mathrm ds$ (Eq. 4.17), which is more convenient for a gas whose abundance is quoted as a mixing ratio ([[CL05 Thermodynamic State of the Atmosphere]]). Different species add: $\tau=\tau_{\rm molecules}+\tau_{\rm aerosol}+\tau_{\rm cloud}+\dots$, and so do scattering and absorption (Eq. 4.18).

> [!intuition] A corridor with a constant crowd: every metre removes the same *fraction*
> Imagine walking a beam of "tennis balls" down a corridor full of people, each of whom grabs any ball that comes near. If each metre of corridor catches 10 % of the balls that reach it (not 10 % of the original number), then after 1 m you have 90 %, after 2 m 81 %, after 3 m 73 %…: an exponential. **The loss is proportional to what is left**, so the survival fraction is $e^{-\tau}$ and the loss never quite reaches 100 %. Optical depth is simply *how many e-foldings of crowd you have crossed*: $\tau=1$ means "one mean free path": the photon has on average met one target.

| $\tau$ | 0.1 | 0.5 | 1 | 2 | 3 | 5 |
|---|---|---|---|---|---|---|
| transmitted $e^{-\tau}$ | 0.905 | 0.607 | 0.368 | 0.135 | 0.050 | 0.0067 |
| absorbed $1-e^{-\tau}$ | 0.095 | 0.393 | 0.632 | 0.865 | 0.950 | 0.993 |

![[fig_cl07_beer_lambert.png|700]]
*Figure CL7.2. Left: transmitted fraction against optical depth. See: it is nearly linear (≈ $1-\tau$) for thin layers and flattens beyond $\tau\approx3$, when almost everything is removed. Right: the slant path through a plane-parallel atmosphere is $1/\cos\theta$ times longer, so the optical depth is multiplied by the **air mass** $m=\sec\theta$; the dashed line marks 60° from the zenith ($m=2$), where the transmission is the square of the overhead value.*

**Slant paths.** For a plane-parallel atmosphere with *vertical* optical depth $\tau_0$, a ray at zenith angle $\theta$ crosses the same layers along a path longer by $\sec\theta$, so $\tau=\tau_0\sec\theta$. At 60° the air mass is 2, so the transmission is $e^{-2\tau_0}$: the *square* of the overhead value. At the horizon the flat-slab formula diverges, and the real value (including the curvature of the Earth and refraction) is about **38** `[verify]` (Kasten & Young 1989); this is why the setting Sun is dim and red.

> [!example] Worked example: "thin" and "thick" are relative to $\tau=1$
> A column of air with $\tau_{\rm vis}\approx0.1$ at 0.55 µm (the Rayleigh optical depth of the whole atmosphere, §3) transmits 90.7 % of green light overhead. The same atmosphere in the thermal infrared at 15 µm has $\tau\gg1$ at the CO₂ line centres: in a few tens of metres of surface air nearly all of the 15 µm photons are absorbed, then re-emitted. The *same* gas column is "transparent" in one colour and "opaque" in another. That contrast is the greenhouse effect.

> [!connection] Probability and ecology
> $e^{-\tau}$ is the **survival probability** of a photon that interacts at a constant rate: the same exponential law as the lifetime of a radioactive nucleus or the waiting time of a Poisson process ($\tau$ = number of expected events; mean free path $=1/N\sigma$); see [[Probability - Course Map]]. The same law governs **light in lakes and canopies**: algae shade the water column below them with $I(z)=I_0e^{-k_dz}$, a key feedback in [[Ecology and Evolution - Course Map]] (turbid vs clear lakes: [[Bistability and Tipping Points]]).

> [!extra-book]+ 🟡 Extra (book): where Beer's law is developed further
> Wallace & Hobbs §4.5.1 ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=147|PDF p.147, book p.130]]) defines the optical depth between two heights, the transmissivity $T=e^{-\tau}$ and the absorptivity of a layer, and §4.5.3 uses these in the equation of radiative transfer. The slides stop at Eq. (CL7.1); the emission term appears in the extra-beyond box of §6.

## 3. Scattering: why the sky is blue, sunsets are red and clouds are white
<span class="scope-taught">taught</span> *Argha L5, slide 56 (Fig. 4.11; the question "blue, red or grey?")* · <span class="scope-extra-book">extra · book</span> *W&H §4.4.1, Eqs. 4.19–4.20* · <span class="scope-extra-beyond">extra · beyond</span> *dipole argument, sunset numbers*

How strongly a particle scatters depends on its size compared with the wavelength, through the **size parameter**

$$x=\frac{2\pi r}{\lambda}$$

(W&H Eq. 4.19; Fig. 4.11 on the slide plots $x$ for various particles and wavelengths). Three regimes:

| regime | size parameter | typical scatterers | wavelength dependence | what you see |
|---|---|---|---|---|
| **Rayleigh** | $x\ll1$ | air molecules ($r\sim10^{-4}\,\mu$m) | scattering efficiency $K\propto\lambda^{-4}$ (W&H Eq. 4.20) | **blue sky**, red sunsets |
| **Mie** | $x\sim1$ | haze, smoke, dust, aerosol ($r\sim0.1$–1 µm) | weaker, forward-peaked; $\sim\lambda^{-1}$ to $\lambda^0$ | whitish haze |
| **geometric** | $x\gg1$ | cloud droplets ($r\sim10\ \mu$m), raindrops | independent of $\lambda$ | **white or grey clouds** |

Rayleigh scattering is divided equally into forward and backward hemispheres (W&H Fig. 4.12a); for $x\gtrsim1$ the scattered light is directed mostly forward.

> [!intuition] Why short waves scatter more: a tiny antenna
> A molecule is far smaller than a wavelength, so the passing wave simply **shakes its charges up and down**; the shaken charges act as a tiny antenna and re-radiate in all directions. A faster shake (higher frequency, shorter wavelength) radiates *much* more power: dipole radiation grows as the **fourth power of the frequency**. Hence blue (0.45 µm) scatters $(0.70/0.45)^4=5.9$ times more than red (0.70 µm), and violet (0.40 µm) 9.4 times more. Large drops are not small antennas at all: the wave sees a big transparent ball and bounces off its surface for *every* colour almost equally, so a cloud of drops looks white (thin) or grey (thick).

**Answering the slide's question.**
- **Blue sky.** Sunlight arrives in parallel from one direction; the molecules scatter the blue part sideways into your eye from every direction, so the whole dome glows blue. (Violet is scattered even more but the Sun emits less of it, ozone absorbs part of the UV end, and the eye is less sensitive to it.)
- **Red sunset.** Near the horizon the sunlight crosses a path up to 38 times longer, so blue is scattered out of the beam, leaving the red (numbers below).
- **Grey/white sky.** Cloud droplets scatter all visible wavelengths alike ($x\gg1$); a deep cloud also absorbs a little and so looks grey underneath.

![[fig_cl07_rayleigh_sky.png|760]]
*Figure CL7.3. Left: the Rayleigh optical depth of the whole atmosphere, $\tau_R(\lambda)\propto\lambda^{-4}$, normalised to 0.097 at 0.55 µm. Right: the fraction of direct sunlight that survives at three air masses (overhead, 5, horizon). See: at the horizon the blue is gone (0.03 %) and about a quarter of the red survives.*

> [!example] Worked example: the numbers behind the red sunset (`fig_cl07_rayleigh_sky.py`)
> Take $\tau_R(0.55\,\mu\mathrm m)=0.097$ (standard sea-level value, Bodhaine et al. 1999) and $\tau_R\propto\lambda^{-4}$:
> | $\lambda$ (µm) | $\tau_R$ | transmitted, overhead ($m=1$) | $m=5$ | horizon ($m=38$) |
> |---|---|---|---|---|
> | 0.40 (violet) | 0.348 | 0.71 | 0.18 | $\approx10^{-6}$ |
> | 0.45 (blue) | 0.217 | 0.80 | 0.34 | $2.6\times10^{-4}$ |
> | 0.55 (green) | 0.097 | 0.91 | 0.61 | 0.025 |
> | 0.70 (red) | 0.037 | 0.96 | 0.83 | **0.24** |
>
> Overhead the Sun's colour is almost unchanged (blue is only 20 % weaker than red); at the horizon blue is attenuated by a factor 4,000 and red by 4. (Ignores ozone, aerosols and refraction, which add reddening and change the exact values.)

> [!extra-beyond]- 🔵 Extra (beyond): where $\lambda^{-4}$ comes from
> A particle of radius $r\ll\lambda$ in a field $E_0\cos\omega t$ acquires an induced dipole $p=\alpha_pE_0\cos\omega t$ ($\alpha_p$ the polarisability, independent of $\omega$ far from resonance). An oscillating dipole radiates a power $P\propto\omega^4p_0^2$ (Larmor). The incident flux is $\propto E_0^2$, so the scattering cross-section is the ratio $\sigma_s\propto\omega^4\alpha_p^2\propto\lambda^{-4}$. For a dielectric sphere $\sigma_s=\frac{8\pi}{3}k^4r^6\big(\frac{m^2-1}{m^2+2}\big)^2$ with $k=2\pi/\lambda$ and $m$ the refractive index: strongly size dependent ($r^6$), which is why Rayleigh scattering by molecules is weak but by tiny droplets would be much stronger. Electromagnetism: see [[Waves - Course Map]].

> [!extra-book]+ 🟡 Extra (book): Mie theory and the extinction efficiency
> Wallace & Hobbs §4.4.1 ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=140|PDF pp.140–142]]) give the scattering efficiency $K$ for a spherical particle as a function of $x$ and a complex refractive index $m=m_r+im_i$ (Fig. 4.13 for $m_r=1.5$), explain that $K$ oscillates around 2 for $x\gg1$, and show the angular patterns of Fig. 4.12. §4.4.2 treats absorption by particles (soot, mineral dust, droplets). None of this was shown beyond the size-parameter figure; the Rayleigh statement above is the examinable content.

> [!pitfall] Scattering is not absorption
> A clean, cloud-free atmosphere **scatters** about 5 % of the sun's visible light but **absorbs** very little of it. Scattered light is not lost from the energy budget: it is redirected, some of it back to space (that fraction is part of the planetary albedo, [[CL03 Radiation and Planetary Energy Balance]]), the rest downwards as diffuse skylight. Only absorption warms the air directly.

## 4. Absorption: a molecule needs a suitable transition
<span class="scope-taught">taught</span> *Argha L5, slide 57* · <span class="scope-extra-book">extra · book</span> *W&H §4.4.3* · <span class="scope-extra-beyond">extra · beyond</span> *modes, dipole rule, symmetry*

The slide gives the whole logic in four lines:
1. Atmospheric gases absorb radiation at different wavelengths.
2. Absorption depends on the **availability of a suitable transition between two energy levels**.
3. Symmetric molecules N₂ and O₂ have **few absorption lines** in the visible and thermal ranges.
4. Greenhouse gases, with **asymmetric molecules**, have rotational and rotational–vibrational levels.

A photon of frequency $\nu$ is absorbed only if $h\nu$ equals the energy gap between two allowed states of the molecule, $\Delta E=h\nu$ (W&H Eq. 4.23). The allowed states are quantised, so absorption is a **line spectrum**: narrow lines separated by wide gaps where the gas is transparent.

> [!extra-book]+ 🟡 Extra (book): the energy of a molecule and the three kinds of line (W&H §4.4.3)
> The internal energy is $E=E_o+E_v+E_r+E_t$ (Eq. 4.22): electronic orbits, vibration, rotation and translation. Only translation is not quantised. Each kind of change gives lines in a different part of the spectrum:
> | transition | typical photon energy | spectral region |
> |---|---|---|
> | **photoionisation** (strip an electron) | > 12 eV | extreme UV, < 0.1 µm: absorbed above ~90 km |
> | **photodissociation** ($\mathrm{O_2}$ → O + O; $\mathrm{O_3}$ → $\mathrm{O_2}$ + O) | 4–6 eV | UV < 0.24 µm (O₂), < 0.31 µm (O₃) |
> | **electronic** | ~1–6 eV | UV and visible |
> | **vibrational** | 0.05–0.5 eV | near and thermal infrared (1.5–25 µm) |
> | **rotational** | 10⁻³–10⁻² eV | far infrared and microwave (> 17 µm) |
>
> Photons in the UV continuum (< 0.31 µm) are absorbed by the ionosphere and the ozone layer; photons at longer wavelengths cannot ionise or dissociate, so absorption there is by lines only. "Most of the solar radiation with wavelengths longer than 0.31 µm penetrates to the Earth's surface" ([[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=144|W&H p.127]]). The 15 µm photon energy is only 0.083 eV, a *vibrational* quantum; hence the infrared is the home of the greenhouse effect.

> [!intuition] Absorption as resonance: the molecule needs a "handle" for the wave
> A guitar string only picks up a sound if the sound contains its own notes (resonance): same for molecules, whose "notes" are the quantised vibration and rotation frequencies. And even at the right frequency the molecule must have **a handle for the electromagnetic wave to grab**: a light wave pushes charges to and fro, so it can only drive a vibration that makes the molecule's **electric dipole moment** oscillate. N₂ and O₂ are symmetric dumbbells: stretching them keeps the charge distribution symmetric, no dipole ever appears, so there is no handle. CO₂ is also symmetric when it stretches symmetrically (no handle) but its **bend** and its **asymmetric stretch** make the charges slosh (a handle appears). The wave "feels" those two and grabs them.

![[fig_cl07_molecule_modes.png|760]]
*Figure CL7.4. The vibration modes of CO₂ (linear) and H₂O (bent). Arrows show how the atoms move; a "+" or "−" on the oxygen and a dipole arrow indicate whether the motion makes the dipole moment oscillate. See: the CO₂ symmetric stretch is IR-inactive (no dipole change); the bend (15 µm) and asymmetric stretch (4.26 µm) are active; all three modes of the bent H₂O molecule are active. Approximate band centres: CO₂ 15.0, 7.2 (inactive), 4.26 µm; H₂O 2.7, 2.66, 6.27 µm.*

> [!extra-beyond]- 🔵 Extra (beyond): modes, selection rule and symmetry
> A molecule of $N$ atoms has $3N-6$ vibrational modes ($3N-5$ if linear). CO₂ (linear, $N=3$): 4 modes: symmetric stretch $\nu_1$ (1388 cm⁻¹, 7.2 µm), **doubly degenerate bend** $\nu_2$ (667 cm⁻¹, 15.0 µm), asymmetric stretch $\nu_3$ (2349 cm⁻¹, 4.26 µm). H₂O (bent): 3 modes: $\nu_1$ (3657 cm⁻¹, 2.73 µm), $\nu_2$ bend (1595 cm⁻¹, 6.27 µm), $\nu_3$ (3756 cm⁻¹, 2.66 µm). O₃: $\nu_3$ at 1042 cm⁻¹ (9.6 µm); CH₄: 7.66 and 3.3 µm; N₂O: 17, 7.8 and 4.5 µm (band centres from standard tables, rounded). A photon energy: $E=1.2398\ \mathrm{eV}/\lambda[\mu\mathrm m]$: 15 µm = 0.083 eV, 4.26 µm = 0.29 eV.
> **Selection rule (electric dipole):** a vibrational transition is infrared-active only if the mode changes the molecule's dipole moment, $\partial\mu/\partial Q\neq0$. In group-theory language the mode must transform like one of the coordinates $x,y,z$ in the molecule's symmetry group. For CO₂ ($D_{\infty h}$) the bend $\Pi_u$ and the asymmetric stretch $\Sigma_u^+$ transform like $(x,y)$ and $z$ (active), while the symmetric stretch $\Sigma_g^+$ transforms like $x^2+y^2,z^2$ only (inactive in the IR, active in Raman). Pure **rotational** lines need a *permanent* dipole: H₂O has one (strong far-infrared absorption beyond 17 µm), CO₂, N₂, O₂ do not. Vibration changes also carry rotational structure, so a band is a **comb** of lines (P, Q, R branches). Links: [[Group Theory - Course Map]] (character tables), [[Quantum Mechanics - Course Map]] (harmonic oscillator and rigid rotor), [[Inorganic Chemistry - Course Map]] (molecular symmetry, vibrational spectroscopy).

> [!example] Worked example: why the "trace" gas matters: the CO₂ column
> There are $p_0/g=1.0132\times10^5/9.81=1.03\times10^4$ kg of air above each square metre. CO₂ at 420 ppm by volume has a mass ratio of $420\times10^{-6}\times44.01/28.97=6.4\times10^{-4}$, so there are **6.6 kg of CO₂** (≈ $9\times10^{25}$ molecules) above every m². At 15 µm each molecule has a huge absorption cross-section at the centre of its lines, so this "trace" column is optically thick ($\tau\gg1$) at the line centres. What matters for radiation is not the *fraction* of the atmosphere (N₂ is 78 %) but the **number of absorbers times their cross-section at the wavelengths where the Earth emits**.

## 5. The shortwave spectrum: below and above the atmosphere
<span class="scope-taught">taught</span> *Argha L5, slide 58 (NASA solar-irradiance spectra at top of atmosphere and at the surface)*

Slide 58 compares sunlight at the top of the atmosphere (yellow) with the spectrum reaching the surface (orange), 200–3000 nm:

- **UV (< 0.31 µm).** Removed almost completely by ozone (and O₂ below 0.24 µm); the pink-brown cliff at 0.3 µm on the slide. This is the ozone layer's service to life, and the reason the stratosphere is heated by ozone ([[CL05 Thermodynamic State of the Atmosphere]] for the temperature profile).
- **Visible (0.4–0.7 µm).** The **atmospheric window for sunlight**: only weak absorption (O₃ in the Chappuis band, 0.5–0.7 µm; O₂ at the 0.76 µm A-band). The solar peak lies in the window, so the surface is heated directly (the first greenhouse idealisation: "transparent for shortwave").
- **Near infrared (0.7–3 µm).** The orange curve is bitten by H₂O bands at about 0.94, 1.1, 1.4, 1.9 and 2.6 µm, CO₂ at 1.4, 2.0 and 2.7 µm, CH₄ near 2.3 µm, O₂ at 0.76 µm. The absorbed energy warms the air directly and is *not* available to the surface.

![[fig_cl07_absorption_spectrum.png|780]]
*Figure CL7.5. Schematic of where the absorbing gases act (band positions rounded from standard tables; **illustrative, not a line-by-line calculation**). Top: Planck curves for the Sun (5772 K) and Earth (288 K) on a log wavelength axis, normalised. Below: the main bands of each gas, with the 8–12 µm window shaded. See: sunlight lives where almost nothing absorbs; Earth's glow lives where H₂O, CO₂ and O₃ do.*

> [!verify] Which Sun temperature?
> The Wikipedia figure on slide 59 labels the solar curve **5525 K**, while CL03 uses the effective temperature 5772 K (IAU). The difference (4 %) moves the Wien peak from 0.50 to 0.52 µm and is irrelevant for the argument. The solar spectrum is not a perfect blackbody (Fraunhofer lines, UV deficit), which is why the two numbers differ.

> [!example] How much sunlight does the atmosphere absorb?
> The "transparent to shortwave" idealisation is rough: the clear and cloudy atmosphere together absorbs about 75–80 W m⁻² of the 340 W m⁻² incident, i.e. roughly **a fifth to a quarter** (Trenberth, Fasullo & Kiehl 2009: 78 W m⁻², `[verify]`); about 100 W m⁻² is reflected and about 160 W m⁻² reaches and warms the surface. Water vapour in the near-IR, ozone in the UV and clouds supply most of this absorption. In the layer model of [[CL08 Greenhouse Models]] it is neglected, which means that model puts all solar heating at the ground, exactly the assumption that makes pure radiative equilibrium unstable ([[CL09 Radiative-Convective Equilibrium]]).

## 6. The longwave spectrum: Earth's glow, windows and bands
<span class="scope-taught">taught</span> *Argha L5, slide 59 (Wikipedia "Atmospheric window"); Suhas pre-midsem notes p.15* · <span class="scope-extra-beyond">extra · beyond</span> *band fractions, Schwarzschild/Kirchhoff*

Slide 59 shows the same idea for the infrared: the emitted spectra of Sun (5525 K curve) and Earth (210–310 K curves), the total atmospheric absorption plus scattering, and below it the contribution of each gas (water vapour, carbon dioxide, oxygen and ozone, methane, nitrogen oxides, Rayleigh scattering). Reading it, as the Suhas notes also do ([[suhas notes.pdf#page=15|suhas notes p.15]]):

- **Near-total transparency in the visible**, where the solar flux peaks.
- **Strong opacity in the UV**, due to ozone.
- **Patchy opacity in the infrared**, where the terrestrial flux peaks: nearly opaque at the **CO₂ 15 µm band** and the **H₂O bands** (6.3 µm and the rotational band beyond ~17 µm), nearly transparent in the **atmospheric window** at 8–12 µm (with a notch at 9.6 µm from ozone).
- **N₂ contributes essentially no absorption anywhere**; O₂ only in the far UV and weakly in the near IR; the dominant absorbers, though trace constituents, are the **triatomic molecules** H₂O, CO₂, O₃ (and CH₄, N₂O).

> [!intuition] A curtain with holes: the **emission level** and the fog analogy
> Looking up from space, **what temperature you see depends on how much "fog" there is at that wavelength**. In the 8–12 µm window the fog is thin: you see all the way to the warm ground (≈ 288 K). At 15 µm the fog is thick: you only see the *top* of it, which is high and cold (≈ 220 K, the lower stratosphere). So the Earth's emitted spectrum, seen from space, is a 288 K blackbody *with a bite taken out* at each absorbing band, down to the temperature of the layer you see. The total flux out is smaller than $\sigma T_s^4$: the missing power is the **greenhouse effect** ($\approx150$ W m⁻², [[CL08 Greenhouse Models]]).

> [!example] Worked example: how much of Earth's 288 K emission sits in each region? (numerical integral of the Planck curve)
> | band | what lives there | fraction of $\sigma T^4$ at 288 K |
> |---|---|---|
> | 5–8 µm | H₂O 6.3 µm vibration–rotation band | 11 % |
> | **8–12 µm** | **the window** (ozone notch at 9.6 µm) | **25 %** |
> | 13–17 µm | **CO₂ 15 µm band** | 19 % |
> | > 17 µm | H₂O pure rotation band | 37 % |
>
> The window carries only a quarter of the surface emission; the other three-quarters faces absorption by CO₂ and H₂O. (The rotational band beyond 17 µm is almost fully saturated by water vapour near the surface, so adding CO₂ there changes little.) The fractions add to ≈ 93 %; the rest is at 3–5 µm and 12–13 µm, plus tails.

> [!extra-beyond]- 🔵 Extra (beyond): emission, Kirchhoff and $\varepsilon=1-e^{-\tau}$
> The reverse of absorption is emission. For a ray of intensity $I$ crossing a thin layer at temperature $T$ with optical thickness $\mathrm d\tau$, the Beer loss $-I\,\mathrm d\tau$ is joined by the layer's own emission $+B(T)\,\mathrm d\tau$, where $B$ is the Planck function ([[Planck Law]]); the factor is the same $\mathrm d\tau$ because of **Kirchhoff's law** (emissivity = absorptivity). This is **Schwarzschild's equation**
> $$\frac{\mathrm dI}{\mathrm d\tau}=-I+B(T).$$
> For an *isothermal* layer of total optical depth $\tau$ and incoming intensity $I_0$ the solution is $I=I_0e^{-\tau}+B\,(1-e^{-\tau})$. So the layer absorbs the fraction $1-e^{-\tau}$ of what is incident, **and** emits $(1-e^{-\tau})B$: its **absorptivity = emissivity $=\varepsilon=1-e^{-\tau}$**. This is the bridge to the next chapter: an emissivity of $\varepsilon=0.78$ (the value that gives 288 K) corresponds to a longwave optical depth $\tau=-\ln(1-\varepsilon)=1.5$; Mars ($\varepsilon\approx0.15$) has $\tau\approx0.16$; $\varepsilon\to1$ needs $\tau\gtrsim3$ ([[One-Layer Greenhouse Model]]). Radiative transfer: [[Blackbody Radiation]].

## 7. Line shapes, saturation and who supplies the greenhouse effect
<span class="scope-extra-book">extra · book</span> *W&H §4.4.3c, Eqs. 4.24–4.29 (not shown in the slides)* · <span class="scope-extra-beyond">extra · beyond</span> *attribution numbers*

> [!extra-book]+ 🟡 Extra (book): why a line has a width, and what the wings do (W&H pp.128–129)
> Lines are not infinitely sharp. **Natural broadening** (uncertainty principle) is negligible; the width is set by the motion and the collisions of the molecules:
> - **Doppler broadening** (random thermal motion towards/away from the photon): Gaussian profile, half-width $\alpha_D=(\nu_0/c)\sqrt{2k_BT/m}$.
> - **Pressure (collision) broadening**: **Lorentz** profile $f(\nu-\nu_0)=\dfrac{\alpha_L/\pi}{(\nu-\nu_0)^2+\alpha_L^2}$ with $\alpha_L\propto p/T^N$ ($N$ between ½ and 1): proportional to the collision frequency, so it dominates in the lower atmosphere and pressure falls off with height.
> The absorption coefficient near a line is $k=S\,f(\nu-\nu_0)$ with line intensity $S=\int k\,\mathrm d\nu$ (Eq. 4.24–4.25). The Lorentz profile has **long wings**: far from the line centre $k\propto S\alpha_L/(\nu-\nu_0)^2$ is small but not zero, so adding absorber keeps increasing absorption in the wings even after the centre is saturated. That is why a band keeps growing slowly (roughly logarithmically) with the amount of gas: doubling CO₂ adds a similar increment of forcing each time (about 3.7 W m⁻² per doubling, [[CL08 Greenhouse Models]]), not a doubling of the effect.

> [!extra-beyond]- 🔵 Extra (beyond): who supplies the greenhouse effect, and where do the trace gases stand?
> Single-gas attribution experiments in a global climate model (Schmidt et al. 2010, *J. Geophys. Res.* 115, D20106) give the share of the clear-and-cloudy-sky greenhouse effect as roughly **water vapour 50 %, clouds 25 %, CO₂ 19 %, the rest 6 %** (`[verify]`: shares depend on the method and overlap between gases). Water vapour dominates the *size* of the effect, but it is **a feedback** of the temperature set by the long-lived gases (CO₂, CH₄, N₂O, O₃), because its concentration is controlled by evaporation and condensation and responds within days to the temperature ([[Water-Vapour Feedback]], [[Clausius-Clapeyron Relation]]). The long-lived gases are "well mixed" ([[CL05 Thermodynamic State of the Atmosphere]], Argha slide 55), the short-lived ones concentrate near their sources.

## Map of this chapter
> [!connection] How CL07 connects
> **Builds on:** [[CL03 Radiation and Planetary Energy Balance]] (spectra, $T_e$, shortwave/longwave) · [[CL05 Thermodynamic State of the Atmosphere]] (composition, mixing ratios) · [[CL06 Hydrostatic Balance and Vertical Structure]] (how much gas lies above a level)
> **Leads to:** [[CL08 Greenhouse Models]] (the absorptivity $\varepsilon$, one and many layers) · [[CL09 Radiative-Convective Equilibrium]] (what the absorbed energy does to the lapse rate)
> **Concepts:** [[Beer-Lambert Law and Optical Depth]] · [[Rayleigh Scattering]] · [[Atmospheric Window]] · [[Greenhouse Gases and Absorption Bands]] · [[Greenhouse Effect]] · [[Blackbody Radiation]] · [[Planck Law]] · [[Albedo]] · [[Outgoing Longwave Radiation]] · [[Water-Vapour Feedback]]
> **Other subjects:** [[Quantum Mechanics - Course Map]] (quantised levels) · [[Group Theory - Course Map]] (selection rules) · [[Inorganic Chemistry - Course Map]] (molecular vibrations) · [[Probability - Course Map]] (exponential survival) · [[Ecology and Evolution - Course Map]] (light in water) · [[Waves - Course Map]] (scattering of waves)

> [!connection] Quantum mechanics, group theory, chemistry
> The statement "absorption needs a transition between levels" *is* quantum mechanics: the vibration of a molecule is a harmonic oscillator with levels $E_n=(n+\tfrac12)h\nu$, the rotation a rigid rotor with $E_J=BJ(J+1)$, and the photon couples to them through the **dipole matrix element**. Whether that element vanishes is a **symmetry** question answered by character tables, the central tool of molecular orbital theory in [[Inorganic Chemistry - Course Map]].

## Summary
> [!summary] Cheat-sheet
> - **Beer–Lambert:** $\mathrm dI=-IK N\sigma\,\mathrm ds\ \Rightarrow\ I=I_0e^{-\tau}$, $\tau=\int KN\sigma\,\mathrm ds$; $\tau=1\Rightarrow37\%$ transmitted; slant path $\tau=\tau_0\sec\theta$.
> - **Size parameter** $x=2\pi r/\lambda$: Rayleigh $x\ll1$ ($K\propto\lambda^{-4}$, blue sky, red sunset), Mie $x\sim1$ (haze), geometric $x\gg1$ (white clouds).
> - Scattering redirects; **absorption heats**. Scattering by air $\tau_R(0.55)\approx0.1$; sunsets at air mass ≈ 38.
> - **Absorption needs a transition**, $h\nu=\Delta E$, **and** a changing dipole. N₂, O₂: no. CO₂ (bend 15 µm, asym. stretch 4.26 µm), H₂O (6.3 µm, rotation > 17 µm), O₃ (9.6 µm, UV), CH₄, N₂O: yes.
> - **Shortwave:** UV cut by O₃ (< 0.31 µm); visible window; near-IR H₂O/CO₂ bands. **Longwave:** CO₂ 15 µm, H₂O bands, **window 8–12 µm** (25 % of 288 K emission).
> - **Emission level:** at opaque wavelengths you see the cold top, in the window you see the warm ground. Greenhouse effect ≈ 150 W m⁻² ≈ 33 K.
> - **Absorptivity of a layer** $\varepsilon=1-e^{-\tau}$; $\varepsilon=0.78\Leftrightarrow\tau=1.5$.

## Practice
1. **Beer.** A beam has $\tau=2.3$. What fraction is transmitted? Through how many "factors of 10" is it dimmed? What $\tau$ transmits 1 %?
2. **Air mass.** If the vertical optical depth is 0.2 at some wavelength, what fraction of overhead light is transmitted, and at 60° from the zenith?
3. **Blue vs red.** By what factor is 0.45 µm scattered more than 0.70 µm by air molecules? Why is the sky not violet?
4. **Size parameter.** Compute $x$ at 0.55 µm for (a) an air molecule ($r=0.2$ nm), (b) a 0.5 µm haze particle, (c) a 10 µm cloud droplet. Which regime is each?
5. **Photon energies.** Give the energy in eV of 0.5 µm, 4.26 µm, 9.6 µm and 15 µm photons. Which transitions (electronic, vibrational, rotational) do they correspond to?
6. **Dipole rule.** Why is the symmetric stretch of CO₂ infrared-inactive but its bend active? Why does N₂ not absorb at all?
7. **Window.** Use the table in §6 to estimate what fraction of Earth's surface emission can escape directly to space if the atmosphere were opaque outside the 8–12 µm window. Which absorption would you have to add to close the window?
8. **Optical depth and emissivity.** What longwave optical depth gives $\varepsilon=0.78$? What fraction of the surface emission is transmitted?
9. **Beyond.** Why can the CO₂ centre of the 15 µm band be *saturated* and yet doubling CO₂ still adds forcing?

> [!example]- Solutions
> 1. $e^{-2.3}=0.100$: transmitted 10 %, one factor of ten in dimming; 1 % needs $\tau=\ln100=4.6$.
> 2. Overhead $e^{-0.2}=0.819$; at 60° the air mass is 2, so $e^{-0.4}=0.670$.
> 3. $(0.70/0.45)^4=5.9$. Violet (0.40 µm) would be 9.4× red, but the Sun emits less violet, ozone absorbs some of the UV end, and the eye's sensitivity falls toward violet: the sky looks blue.
> 4. $x=2\pi r/\lambda$: (a) $2\pi\times0.2\times10^{-3}/0.55=2.3\times10^{-3}$ (Rayleigh); (b) $2\pi\times0.5/0.55=5.7$ ($x\gtrsim1$: Mie); (c) $2\pi\times10/0.55=114$ (geometric; white cloud).
> 5. $E=1.2398/\lambda$ eV: 2.48 eV (electronic/visible), 0.291 eV, 0.129 eV and 0.083 eV (the last three are **vibrational** quanta of CO₂ $\nu_3$, O₃ $\nu_3$ and CO₂ $\nu_2$); rotational quanta are ~10⁻³–10⁻² eV (far IR).
> 6. In the symmetric stretch the two O atoms move outward together, so the molecule stays symmetric and the net dipole remains zero ($\partial\mu/\partial Q=0$). In the bend the C atom moves off the O–O axis, making a net dipole that oscillates, so the field can drive it. N₂ is a symmetric diatomic: its only vibration (stretch) never creates a dipole, and it has no permanent dipole for rotation, so it has essentially no lines in the visible or IR.
> 7. Only 25 % of the emission lies in the window, so if the atmosphere were opaque outside it, only ≈ 25 % would escape directly; adding an absorber at 9.6 µm (ozone) or at 8–12 µm (water-vapour continuum, CFCs, high CO₂) closes it further.
> 8. $\tau=-\ln(1-0.78)=1.51$; the transmitted fraction is $e^{-\tau}=1-\varepsilon=0.22$. (This is the "leak" in the leaky greenhouse.)
> 9. At line centres $\tau\gg1$ so extra gas changes nothing there; but the *wings* of the lines and the band edges, where $\tau\sim1$, become opaque and widen the absorbing band, so the effective absorption keeps growing (logarithmically): about 3.7 W m⁻² per doubling.

> [!connection] Group theory used here
> The infrared selection rule for CO$_2$ and H$_2$O (a mode is active if it transforms like a coordinate) is worked out for NH$_3$ and H$_2$O in [[GT10 Symmetry Representations and Characters]] §4; see [[Where Groups Appear in the Vault]].

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | scattering and absorption, Beer–Lambert derivation, "why blue/red/grey" | [[climate_intro_L1_L6.pdf#page=56\|Argha L5 sl. 56]] (cites W&H §4.4, Fig. 4.11) | taught |
> | absorption needs a transition; symmetric vs asymmetric molecules | [[climate_intro_L1_L6.pdf#page=57\|Argha L5 sl. 57]] | taught |
> | shortwave spectrum at top and bottom | [[climate_intro_L1_L6.pdf#page=58\|Argha L5 sl. 58]] (NASA) | taught |
> | longwave spectrum, windows, component gases | [[climate_intro_L1_L6.pdf#page=59\|Argha L5 sl. 59]] (Wikipedia); [[suhas notes.pdf#page=15\|Suhas notes p.15]] | taught |
> | size parameter, Rayleigh $K\propto\lambda^{-4}$, Mie, Fig. 4.11–4.13 | Wallace & Hobbs §4.4.1, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=140\|PDF p.140]] | extra/book |
> | photoionisation/dissociation, $E=E_o+E_v+E_r+E_t$, line broadening, Lorentz/Doppler | W&H §4.4.3, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=144\|PDF pp.144–146]] | extra/book |
> | Beer's law in W&H notation, $\rho r k$ form | W&H §4.5.1, [[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=147\|PDF p.147]] | extra/book |
> | $\lambda^{-4}$ from the dipole, sunset numbers | derived here; $\tau_R(0.55)=0.097$ (Bodhaine et al. 1999) | extra/beyond |
> | CO₂/H₂O modes, band centres, dipole rule, symmetry | standard spectroscopy tables; derived here | extra/beyond |
> | band fractions of 288 K emission, $\varepsilon=1-e^{-\tau}$, CO₂ column | computed here | extra/beyond |
> | atmospheric solar absorption (78 W m⁻²); single-gas attribution shares | Trenberth et al. (2009); Schmidt et al. (2010) | extra/beyond (`[verify]`) |
>
> **Dropped as redundant:** the Suhas pre-midsem description of the absorption spectrum (p.15) repeats Argha's slides 57–59 almost word for word; the two are merged in §§4–6. The AI notes `argha-climate.pdf` (secondary) agree with the slides on all formulas.

**References.** Wallace, J. M. & Hobbs, P. V. (2006) *Atmospheric Science*, §4.3–4.5 · Bodhaine, B. A. et al. (1999) *J. Atmos. Oceanic Technol.* 16, 1854 (Rayleigh optical depth) · Kasten, F. & Young, A. T. (1989) *Appl. Opt.* 28, 4735 (air mass) · Trenberth, K. E., Fasullo, J. T. & Kiehl, J. (2009) *Bull. Amer. Meteor. Soc.* 90, 311 · Schmidt, G. A. et al. (2010) *J. Geophys. Res.* 115, D20106 · NASA solar irradiance science page (slide 58) · Wikipedia, *Atmospheric window* (slide 59).
