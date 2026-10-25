---
id: introduction-to-climate-science/2026-08-19-lecture-3-planetary-energy-balance
aliases: [Lecture 3: Planetary Energy Balance]
tags: [introduction-to-climate-science, lecture, energy-balance]
trust_tier: agent_written
---

# Lecture 3: Planetary Energy Balance

## Covered
Student-written notes (made with Gemini Notebook, reviewed by Yugansh and Anjali) on slides 30–39. Textbook: Kump, Kasting & Crane, *The Earth System*.

**I. Atmospheric state (slides 30–31)**
- Variables of state and the conservation law each represents: pressure $P$ and density $\rho$ (ideal gas law, mass conservation); wind $(u,v,w)$ (momentum); humidity $q$ (water mass); temperature $T$ (energy/enthalpy).
- Water vapour is ~0.25 % of the atmosphere's mass but ~2.5 % of its energy content. Latent heat of vaporization ≈ 2260 kJ/kg; the hydrologic cycle moves latent heat from the surface to where vapour condenses into clouds.
- Energy conservation: $c_p\,\partial T/\partial t = $ rate of (net heat supply by winds + heating from condensation, absorption, …).
- 0-D model: average over the whole surface and over time to get a nearly constant temperature, so $\partial T/\partial t = 0$ (steady state). Internal redistribution (winds, ocean currents carrying heat from the tropics to the poles) drops out; only exchanges at the top of the atmosphere count: incoming solar and outgoing infrared.
- Textbook: Ch. 3 Introduction, Atmospheric Composition and Structure; Ch. 4 "The Driving Force".

**II. Thermal radiation (slides 31–34)**
- Blackbody: perfect absorber and emitter. Planck function $I(\lambda,T)=\dfrac{2hc^2}{\lambda^5\left(e^{hc/\lambda k_BT}-1\right)}$, unit W m$^{-2}$ sr$^{-1}$ m$^{-1}$; $h=6.626\times10^{-34}$ J s, $c=2.998\times10^{8}$ m/s, $k_B=1.38\times10^{-23}$ J/K. The notes give the ratio of peak radiation emitted by the Sun to that of the Earth as ≈ 205.
- Wien's law: $\lambda_{\max}\approx 2898/T$ ($\mu$m, $T$ in K). Sun (~5800 K) peaks in the visible; Earth (~288 K) peaks at ~10 $\mu$m (infrared). The notes pose "Can you derive this relation from Planck's law?" as an exercise.
- Stefan–Boltzmann: $F=\sigma T^4$, $\sigma=5.67\times10^{-8}$ W m$^{-2}$ K$^{-4}$; doubling $T$ gives 16 times the emission.
- Shortwave: Sun's surface (~5780 K), visible 400–700 nm. Longwave: Earth (~288 K), thermal IR, 8–14 $\mu$m.
- Inverse-square law: $S=S_0\,(r_0/r)^2$.
- Textbook: Ch. 3 "Electromagnetic Radiation" (pp. 38–41), "Blackbody Radiation" (p. 41).

**III. Zero-dimensional energy balance model (slides 35–36)**
- Solar luminosity $=(4\pi R_{\rm Sun}^2)(\sigma T_{\rm Sun}^4)$. Spread over a sphere of radius $R_{S\to E}$: $S=\sigma T_{\rm Sun}^4\,R_{\rm Sun}^2/R_{S\to E}^2$.
- The Earth intercepts sunlight as a disk of area $\pi r^2$ but has surface area $4\pi r^2$, so the mean incoming flux is $S/4$ (~340 W/m$^2$): $S\cdot\pi R^2/(4\pi R^2)=S/4$.
- Albedo $\alpha$ = fraction reflected; Earth ≈ 0.3 (clouds and ice).
- Equilibrium: $\dfrac{S}{4}(1-\alpha)=\sigma T^4$. Earth: $T_e=255$ K ($-18$ °C); observed $T_s=288$ K ($+15$ °C). The 33 K difference is the greenhouse effect.
- Stable steady state: a disturbance triggers internal responses that return the system to it. Earth's climate is mainly stabilised by the IR flux/temperature feedback (negative). Warmer than equilibrium: $\mathrm{LW_{out}}>\mathrm{SW_{net}}$, so the planet cools; cooler: $\mathrm{SW_{net}}>\mathrm{LW_{out}}$, so it warms.
- Unstable steady state: stays only if undisturbed; any perturbation pushes it away. Example: in the Snowball transition, once polar ice reaches ~30° latitude, ice-albedo feedback is unstoppable (a slight cooling leads to runaway freeze, a slight warming might lead to runaway melt).
- Textbook: Ch. 3 Box "A Closer Look: Planetary Energy Balance" (p. 44), "The IR Flux/Temperature Feedback" (p. 44); Ch. 2 Daisyworld, Equilibrium States (pp. 23–24).

**IV. Comparative planetology (slides 37–39)**
Plot of observed vs calculated temperature; a perfect blackbody model would put all planets on the 1:1 line.
- Earth: calculated 255 K, observed 288 K; the 33 K is the natural greenhouse effect.
- Venus (runaway greenhouse): observed ≈ 730 K (460 °C) as quoted in the notes. The atmosphere (93-bar CO$_2$ plus thick water vapour) became so thick that outgoing IR reached a limit and could no longer rise with surface temperature, removing the stabilising negative feedback (an unstable steady state). Hotter than Mercury despite being further from the Sun.
- Mars: model fairly accurate (210 K calculated vs 218 K observed). Thin (~10 mbar) CO$_2$ atmosphere and no water vapour limit the greenhouse effect to ~5 K; mean surface about $-55$ °C.
- Mercury: no atmosphere, extreme day/night swings. The model overestimates its mean temperature because $\langle T^4\rangle>\langle T\rangle^4$: the hot side radiates away energy much more efficiently than the model expects.
- Jupiter and Saturn: above the 1:1 line because of internal heat not included in a sunlight-only model. Sources: residual heat from accretion (4.6 Gyr ago), gravitational contraction, and (Saturn) helium "raining" toward the core, releasing gravitational energy.
- Textbook: Ch. 3 Introduction (p. 37); Ch. 19 "Martian Climate Evolution" (p. 385).

## From the post
"These are the notes for Lectures 3 and 4. Hope everyone can access them.

PS. The textbook references mentioned in notes for Lectures 1, 2, 3, and 4 are for the book, The Earth System (Lee R. Kump, James F. Kasting, Robert G. Crane)." (Classroom announcement, 2026-08-19)

## Files
- [Lecture 3 Planetary Energy Balance.pdf](https://drive.google.com/file/d/1Hb6fYXoqLWA-Ija-NFUIcFkdiXk5oi7G/view?usp=drive_web)
- The full slides [climate_intro_L1_L6.pdf](https://drive.google.com/file/d/1msXI1WI9XnSUhwqgBeG1DpU-ukYtGrpm/view?usp=drive_web) (54 MB, latest version) were too large to read; only these student notes are summarised.

## Related
- [[01-climate/cl03-radiation-and-planetary-energy-balance]]: your own chapter on the same material
- [[01-climate/concepts/zero-dimensional-energy-balance-model]]: the $S/4(1-\alpha)=\sigma T^4$ model
- [[01-climate/concepts/effective-emission-temperature]]: $T_e=255$ K
- [[01-climate/concepts/albedo]]: albedo definition and values
- [[introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance]]: Marshall & Plumb version of the same derivation
- [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback]]: next lecture, builds on this balance
