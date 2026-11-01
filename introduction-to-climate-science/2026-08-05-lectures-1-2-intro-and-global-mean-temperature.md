---
id: introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature
aliases: [Lectures 1-2 notes, Climate intro notes]
tags: [climate, introduction-to-climate-science, lecture]
trust_tier: agent_written
---

# Lectures 1–2: Introduction and Global Mean Annual Temperature

Lecture notes written by the instructor team (generated with Gemini Notebook, reviewed by the TAs). Textbook: Kump, Kasting, Crane, *The Earth System*. The notes and slides are described as evolving documents.

## Covered

### Lecture 1: Introduction
**Motivation.** Human activity is changing the Earth system at an unprecedented rate (the Anthropocene). Forecasting across time scales, from hourly weather to century-scale climate, matters for the economy, policy, and water and food security.
- Indian Summer Monsoon Rainfall (ISMR) anomaly vs Index of Foodgrain Production (IFGP): correlation 0.76–0.79. In 1951–80, surplus rain also raised production; in 1981–04 surplus rain did not necessarily raise it. Below-average rain sharply lowers production.

**Planetary boundaries** (Richardson et al. 2023): nine boundaries define a "safe operating space"; 6 of 9 are transgressed.
- Transgressed: climate change (CO$_2$ boundary 350 ppm, now >417 ppm; radiative forcing boundary 1.0 W m$^{-2}$, now ~2.91 W m$^{-2}$); biosphere integrity (extinction rate boundary <10 per million species-years, now >100; HANPP boundary <10 %, now ~30 %); land-system change (remaining forest cover); freshwater change (blue and green water); biogeochemical flows (N and P); novel entities.
- Within safe limits: ocean acidification (aragonite saturation $\Omega_{arag}$, close to the limit), atmospheric aerosol loading (AOD; fine globally, breached regionally, e.g. South Asia), stratospheric ozone (Dobson units; recovering after the 1987 Montreal Protocol).
- Conclusions: crossing boundaries raises systemic risk without guaranteeing immediate collapse; boundaries are interdependent (deforestation affects biosphere integrity and CO$_2$); climate targets alone are not enough.

**Earth-system approach.** Four components: atmosphere, hydrosphere (including cryosphere), biota, solid Earth; the anthroposphere is the part created or changed by humans. The Amsterdam Declaration (2001) treats the Earth system as a single self-regulating system of physical, chemical, biological and human components. Reference: Kump et al. Ch. 1, "Three Major Themes".
- Tipping points: critical thresholds where a small change in one component can cause a large, potentially irreversible shift. Connections (Lenton et al. 2019): Arctic sea ice (B) → Greenland ice sheet (G) and Boreal forest (D), Permafrost (H); sea ice and Greenland → AMOC (C), with a ~15 % AMOC slowdown since the mid-20th century; AMOC → Amazon (A) and West Antarctic ice sheet (I) and Wilkes Basin (J). Coral reefs (F): 99 % of tropical corals projected lost at +2 °C.

**Scales.** Stommel diagram: time scale vs spatial scale (micro-turbulence: seconds and metres; ENSO: years and thousands of km).

**Newtonian prediction.** A future state follows from a Taylor series $\bar x(t)=\bar x(t_0)+\frac{\partial \bar x}{\partial t}\big|_{t_0}t+\frac{\partial^2 \bar x}{\partial t^2}\big|_{t_0}\frac{t^2}{2}+\dots$, which needs infinitely many coefficients; instead use $m\,\partial^2\bar x/\partial t^2=\bar F(x,t)$, giving $\bar x(t)=\bar x(t_0)+v(t_0)t+\frac1m\int_{t_0}^{t}\bar F\,dt'$ for a cricket ball. Earth-system prediction is harder: many variables, incomplete and noisy observations, non-linear and emergent interactions.

**Patterns** (Kump et al. Ch. 3–5):
- Temperature: latitudinal energy imbalance (tropical surplus, polar deficit) drives circulation; IR flux/temperature feedback is the basic negative feedback; lapse rate and topography (Tibetan Plateau as summer heat source); snow and ice albedo 0.8–0.9 gives a positive feedback.
- Precipitation: convection, ITCZ convergence, land–ocean contrast (continentality), latent heat release as the "pump" of Hadley cells, monsoon as seasonal wind reversal.
- Ocean surface currents: wind-forced gyres and eddies; coastlines create closed subtropical gyres and western boundary currents such as the Gulf Stream.

**Long-term history and feedbacks.**
- Ice-albedo: ice reflects up to 90 % (snow) and 50–70 % (ice); ~100 ky glacial cycles triggered by Milankovitch cycles and amplified by the feedback.
- Biosphere: conifers darken snow (positive albedo feedback); transpiration; CO$_2$ fertilization; silicate weathering.
- Lithosphere: tropical continents favour weathering and lower CO$_2$; volcanism emits CO$_2$; orogeny enhances weathering.
- Case study: Huronian glaciation, ~2.4 billion years ago.

### Lecture 2: Global Mean Annual Temperature
**Measuring temperature.** Mercury thermometers (thermal expansion) and resistance thermometers. IMD protocol: sensors at 1.25–2.0 m inside a Stevenson screen (white, louvered), away from heat islands; historical data need correction for systematic errors such as city growth. Proxies: tree rings, glacier length, mineral assemblages, isotopes in sediment or ice.

**Temporal variability.** ERA5 reanalysis (observations assimilated into a model to fill gaps). Use folding or the Fourier transform to find daily and annual cycles; annual means reveal the long-term warming trend.

**Spatial variability and global mean.** Grid the globe and use the area-weighted mean
$$\bar T=\frac{\sum_i T_iA_i}{\sum_i A_i},$$
with box size set by the correlation length (hundreds of km to ~1000 km). Global average surface temperature rose by about 0.8 °C during the 20th century.

**Isotopic thermometers.**
$$\delta^{18}\mathrm{O}=\left(\frac{(^{18}\mathrm{O}/^{16}\mathrm{O})_{\text{sample}}}{(^{18}\mathrm{O}/^{16}\mathrm{O})_{\text{standard}}}-1\right)\times1000\ ‰$$
(standard: Standard Mean Ocean Water). $^{16}$O evaporates more easily and $^{18}$O rains out first on the way to the poles, so polar ice is depleted in $^{18}$O (ice sheets $\delta^{18}\mathrm{O}\approx-50$ ‰) and the ocean is relatively enriched. In ice cores, colder periods give more negative $\delta^{18}$O. In foraminifera shells, ice ages give heavier (higher) $\delta^{18}$O. Deuterium ($\delta$D) is also used.

**Thermal radiation.** A blackbody absorbs all incident radiation. Planck function
$$I(\lambda,T)=\frac{2hc^2}{\lambda^5\left(e^{hc/(\lambda k_BT)}-1\right)}.$$
Wien: $\lambda_{\max}\approx 2898/T\ \mu$m (Sun ~5800 K peaks in the visible; Earth 288 K peaks at ~10 µm). The notes pose "derive Wien's law from Planck's law" as a question. Stefan–Boltzmann: $F=\sigma T^4$, $\sigma=5.67\times10^{-8}$ W m$^{-2}$ K$^{-4}$ (doubling $T$ gives 16 times the flux). Solar radiation is shortwave and terrestrial radiation is longwave, which is why greenhouse gases let sunlight in but trap outgoing heat.

Textbook pointers: Kump et al. Ch. 1 (pp. 3–13); Ch. 3 (Electromagnetic Radiation p. 37, Blackbody Radiation p. 41, Stefan–Boltzmann Law p. 42); Ch. 14 (pp. 274, 280).

## From the post
Post 1 (2026-08-05): "thanks a lot for being in the class and participating in the discussion. I had a good time – hope you did too :) the lecture slides are here. I'll add some notes, and the tutorials (a list of numerical problems and a python notebook – both based on lecture 1 & 2). You are supposed to attempt them, and then the TAs will help you with your doubts during the T on Friday. For my part, please consult the recommended text book: Kump/Kasting/Crane EARTH SYSTEM. The notes will point you to the appropriate parts of the book (wherever possible). All the other material that I refer to is linked (articles, websites, ...), please click on the links and explore. Feel free to bug me & the TAs with questions/comments in/outside the class."

Post 2 (2026-08-05): "Uploading 1. the problem set, 2. data-analysis exercise (a pynb notebook file+2 csv data files; drag all of them into google collab, and run the python nootebook step by step), and 3. A quick notes explaining the slides, and pointing you to appropriate text book pages. The note and slides are meant to encourage you to think critically, read the text book and more. Also, the slides and notes are evolving documents, keep an eye on the updated version, if any. Feel free to share your comments, suggestions on all that I have shared so far."

Post 3 (2026-08-05), a curiosity question, not an assignment: a photo of droplets dripping off the bottom of a pipe; "Is it possible to predict the separation between the droplets...? Think about it only if you have time to kill."

## Files
- [climate_intro_notes.pdf](https://drive.google.com/file/d/1Abllm65kYMP3O2YNoFKiB-FEhLFQ1SMf/view?usp=drive_web): read in full (text above).
- [climate_intro_L1_L6_argha.pdf](https://drive.google.com/file/d/1fs4H0-ud8Xp_SVuTRaz2ug_9ZP6zrEoX/view?usp=drive_web): lecture slides L1–L6, 36 MB, too large to read; not read.
- [WhatsApp Image 2026-08-05 at 12.58.17.jpeg](https://drive.google.com/file/d/1mf3TMmtVF2QviJF7Z1EE6bcjErwIcelb/view?usp=drive_web): photo of the dripping pipe; image not read.
- Exercises: [[introduction-to-climate-science/2026-08-05-problem-set-1]], [[introduction-to-climate-science/2026-08-05-tutorial-1-data-analysis-notebook]].

## Related
- [[01-climate/cl01-earth-as-a-system]]: their chapter on Lecture 1 (Earth as a system)
- [[01-climate/cl02-observing-global-temperature]]: their chapter on Lecture 2 (measuring and averaging temperature)
- [[01-climate/cl03-radiation-and-planetary-energy-balance]]: radiation laws and energy balance
- [[01-climate/concepts/isotopic-thermometers]]: $\delta^{18}$O proxy
- [[01-climate/concepts/ice-albedo-feedback]]: positive feedback described in Lecture 1
- [[01-climate/concepts/earth-system]]: Earth-system concept note
- [[09-foundations/concepts/bistability-and-tipping-points]]: tipping points
- [[03-thermodynamics/concepts/stefan-boltzmann-law]]: $F=\sigma T^4$
- [[03-thermodynamics/concepts/blackbody-radiation]]: Planck function and Wien's law

<!-- kurooto:material4e3d2ded -->
## Concepts in climate_intro_notes
(none new)
<!-- /kurooto:material4e3d2ded -->
