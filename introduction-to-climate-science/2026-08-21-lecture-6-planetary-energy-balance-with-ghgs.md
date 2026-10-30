---
id: introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs
aliases: [Lecture 6: Planetary energy balance with GHGs, Lectures 1-6 compiled notes]
tags: [lecture-notes, introduction-to-climate-science, climate]
trust_tier: agent_written
---

# Lecture 6: Planetary energy balance with GHGs (from the compiled L1–L6 notes)

## Covered
Source: `climate_intro_notes_L1_L6.pdf`, student-written notes for Lectures 1–6 compiled into one PDF, posted 2026-08-21 (Classroom: compiled L1–L6 notes). Lectures 1–4 duplicate material already filed ([[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature]], [[introduction-to-climate-science/2026-08-19-lecture-3-planetary-energy-balance]], [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback]]) and Lecture 5 is in [[introduction-to-climate-science/2026-08-20-lecture-5-atmosphere-and-greenhouse-gases]]. This note holds Lecture 6, which was not filed before. In the extracted text most of the Lecture 6 equations and symbols are blank (they are images in the PDF), so the algebra below is the line of argument stated in words; the closed-form results are the ones already derived in [[introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance]].

**Why layers (introduction).** The 0-D model without atmosphere gives 255 K (≈ −18 °C); observed mean surface temperature is 288 K (15 °C); $\Delta T_g=33$ K is the greenhouse effect. To go beyond subtraction, the atmosphere is modelled as a discrete layer that intercepts and recycles outgoing longwave radiation.

**Mechanism.** The atmosphere is transparent to incoming shortwave, which warms the surface. Greenhouse gases (asymmetric or triatomic molecules: H$_2$O, CO$_2$, O$_3$) have rotational and vibrational states that absorb outgoing longwave; the atmosphere re-radiates in all directions, including down (back-radiation). References: Kump et al. Ch. 3 Box "How the Greenhouse Effect Works: The One-Layer Atmosphere"; Wallace & Hobbs §4.3.6.

**Slide 65, one-layer semi-transparent model, assumptions:** (1) atmosphere fully transparent to shortwave; (2) semi-transparent to longwave with longwave emissivity $\varepsilon$, $0\le\varepsilon\le1$; (3) Kirchhoff's law: absorptivity = emissivity, so the layer absorbs a fraction $\varepsilon$ of the upwelling surface emission and a fraction $1-\varepsilon$ escapes to space. Fluxes: absorbed solar flux (the global-mean $\frac{S}{4}(1-\alpha)$) reaches the surface; the surface emits $\sigma T_s^4$ upward; the atmosphere at $T_a$ emits $\varepsilon\sigma T_a^4$ both up and down.

**Slide 66, three steady-state balances and derivation.**
1. Top of atmosphere: net absorbed solar = outgoing (transmitted surface emission plus atmospheric upward emission).
2. Atmosphere: energy absorbed = energy emitted; the common factor $\varepsilon$ cancels, giving the fundamental relation between surface and atmospheric temperature.
3. Surface: absorbed solar plus atmospheric back-radiation = surface emission.
Derivation steps: (1) express atmospheric emission via surface emission from balance 2; (2) substitute into the surface balance; (3) group the $\sigma T_s^4$ terms; (4) solve for $T_s^4$; (5) take the fourth root. Writing $T_e=\left[\frac{S(1-\alpha)}{4\sigma}\right]^{1/4}$ for the effective radiating temperature without a greenhouse effect, the result is $T_s=\left(\frac{2}{2-\varepsilon}\right)^{1/4}T_e$ (same result as in study material 5). Reference: Wallace & Hobbs §4.5.2.

**Slide 67, ideal blackbody atmosphere ($\varepsilon=1$).** $T_s=2^{1/4}T_e$, which for Earth is 303 K, 15 K above the observed 288 K. The model overestimates because the real atmosphere has the 8–12 µm window, through which a significant fraction of surface radiation escapes directly.

**Slide 68, temperature vs emissivity for planets** (blue model curves, dashed grey lines are observed temperatures):
- Earth: matching 288 K needs a realistic intermediate $\varepsilon$ (greenhouse gases and clouds leave some vents open to space).
- Mars: very thin CO$_2$ atmosphere (~10 mbar), fits at a low $\varepsilon$ and adds only a few kelvin of warming.
- Venus: the one-layer model fails even at $\varepsilon=1$. Albedo is high (thick sulfuric-acid clouds), so its effective radiating temperature is cold and the model's maximum is far below the actual surface temperature. Reason: a multi-layer greenhouse with optical depth far above 1 (about 1000 times), so infrared is absorbed and re-emitted many times before escaping.
- Jupiter and Saturn: lie above the model curves because of internal heat sources (residual formation heat, gravitational contraction) giving an upward flux independent of solar heating.
(The numerical values on slide 68 did not survive text extraction.)

**Slides 69–70, transition to time-dependent models.** Steady state ($\partial T/\partial t=0$) is a poor approximation on diurnal timescales; thermal reservoirs and convective fluxes (Kump et al. Ch. 3) are introduced.

**Slide 71, diurnal temperature of a bare-rock planet.** Transient heat balance: heat capacity per unit area (density × active depth × specific heat; depth 20 cm of soil/rock) times $dT_s/dt$ equals absorbed solar flux, switched on only in daytime by the Heaviside step $\Theta(\cdot)$ applied to a sinusoid in the rotation phase (day = 86 400 s), minus outgoing longwave $\sigma T_s^4$.
- Role of heat capacity: with zero heat capacity temperature would follow sunlight instantly, peaking at noon and collapsing at sunset; real heat capacity stores heat by day and releases it at night.
- Diurnal lag: the temperature peak comes in the afternoon, typically 2–4 h after noon, because absorbed solar still exceeds outgoing longwave after noon; temperature falls only once outgoing exceeds the declining solar input.
- The model overestimates the day–night swing because it omits: the atmospheric greenhouse effect (warmer nights), sensible and latent heat fluxes (daytime surface cooling), deep soil conduction (damping).
- References: Kump et al. Ch. 4 "The Sea Breeze"; Wallace & Hobbs §9.2 "The Surface Energy Balance".

## From the post
Hi guys! Hope you had a good time with the quiz :) Here are the notes for all the 6 lectures compiled into a single pdf. Hope it is accessible to all.

PS. Textbook references include sections from The Earth System (Lee R. Kump, James F. Kasting, Robert G. Crane) and Atmospheric Science (John M. Wallace and Peter V. Hobbs). (Classroom announcement, 2026-08-21: https://classroom.google.com/c/ODY5MDg2NTA1Mzg0/p/ODU2MDI2ODgyNDE0)

## Files
- [climate_intro_notes_L1_L6.pdf](https://drive.google.com/file/d/1bb28KHDLmKQSZ29sazWWN44EneXvcR4G/view?usp=drive_web): read in full. In Lecture 6 the equations and symbols are images and came out blank, so the exact formulas and the slide 68 numbers are not captured here; check the PDF.
- [climate_intro_L1_L6.pdf](https://drive.google.com/file/d/15JvEMAH7vXGEuBhX6th_lCBGhnwb9apN/view?usp=drive_web): the slides for Lectures 1–6 (60 MB), not read (too large); open the link.

## Related
- [[introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance]]: the same single-layer opaque and leaky greenhouse models with explicit formulas.
- [[introduction-to-climate-science/2026-08-19-lecture-3-planetary-energy-balance]]: the 0-D model and the Venus/Mars/Jupiter comparison that Lecture 6 extends.
- [[introduction-to-climate-science/2026-08-13-tutorial-2-energy-balance-problems]]: includes the diurnal OLR/ASR lag problem.
- [[01-climate/cl08-greenhouse-models]]: your chapter notes on greenhouse models.
- [[01-climate/concepts/one-layer-greenhouse-model]]: your concept note on the one-layer model.

<!-- kurooto:material8ec6b0aa -->
## Concepts in climate_intro_notes_L1_L6
[[zettel/planetary-boundaries]], [[zettel/earth-system]], [[zettel/atlantic-meridional-overturning-circulation]], [[zettel/stommel-diagram]], [[zettel/newtonian-deterministic-climate-prediction]], [[zettel/latitudinal-energy-imbalance]], [[zettel/infrared-flux-temperature-feedback]], [[zettel/orographic-uplift]], [[zettel/ice-albedo-feedback]], [[zettel/land-ocean-thermal-contrast]], [[zettel/latent-heat-release-in-convection]], [[zettel/oceanic-gyres-and-surface-currents]], [[zettel/silicate-weathering-feedback]], [[zettel/area-weighted-mean-temperature]], [[zettel/oxygen-isotope-paleothermometry]], [[zettel/planck-function]], [[zettel/wien-s-displacement-law]], [[zettel/stefan-boltzmann-law]], [[zettel/atmospheric-conservation-of-energy]], [[zettel/inverse-square-law-of-radiation]], [[zettel/zero-dimensional-energy-balance-model]], [[zettel/planetary-emission-temperature]], [[zettel/runaway-greenhouse-effect]], [[zettel/planetary-internal-heat-sources]], [[zettel/parameter-sensitivity-via-logarithmic-differentiation]], [[zettel/radiative-forcing]], [[zettel/piecewise-linear-albedo-model]], [[zettel/multiple-climate-equilibria-in-energy-balance-models]], [[zettel/snowball-earth]], [[zettel/runaway-ice-albedo-instability]], [[zettel/cap-carbonates]], [[zettel/hydrostatic-balance]], [[zettel/atmospheric-scale-height]], [[zettel/vertical-pressure-gradient]], [[zettel/beer-s-law]], [[zettel/radiative-extinction]], [[zettel/greenhouse-gas-absorption-mechanisms]]
<!-- /kurooto:material8ec6b0aa -->
