---
id: introduction-to-climate-science/2026-08-20-lecture-5-atmosphere-and-greenhouse-gases
aliases: [Lecture 5: Atmosphere & Greenhouse gases]
tags: [lecture-notes, introduction-to-climate-science, climate]
trust_tier: agent_written
---

# Lecture 5: Atmosphere & Greenhouse gases

## Covered
Source: student-written lecture notes for Lecture 5 (slides 51–59), posted 2026-08-20 (Classroom: Lecture 5 notes). Textbooks cited in the notes: Kump, Kasting & Crane, *The Earth System*; Wallace & Hobbs, *Atmospheric Science*.

**I. Hydrostatic equation and barometric law (slides 51–54)**
- Slab of thickness $dz$, area $dA$: weight $dW=\rho g\,dA\,dz$; balance $p\,dA-(p+dp)\,dA=\rho g\,dA\,dz$ gives $\frac{dp}{dz}=-\rho g$.
- Ideal gas $pV=Nk_BT$ gives $\rho=\frac{mp}{k_BT}$, so $\frac{dp}{p}=-\frac{mg}{k_BT}dz$. Integrating from $(z=0,p_0)$ at constant mean $T$: $p(z)=p_0e^{-z/H}$.
- Scale height $H\doteq\frac{k_BT}{mg}$: the height over which $p$ falls by $1/e$ (~37 %). For $T=255$ K, $g=9.8$ m s$^{-2}$, $m=5\times10^{-26}$ kg: $H\approx7.5$–$8$ km.

**II. Vertical vs horizontal pressure gradients (slides 53–54)**
- Vertical: ~1013 hPa at sea level, ~100 hPa at 16 km (top of the tropical troposphere); near the surface ~1 hPa per 8 m = 125 hPa km$^{-1}$ = 12 500 Pa km$^{-1}$.
- Horizontal: highs ~1030 hPa vs lows ~1000 hPa over thousands of km; even an intense typhoon (940 hPa centre, 1010 hPa environment, ~500 km) gives only 70 hPa over ~500 km, i.e. 0.14 hPa km$^{-1}$.
- Ratio vertical/horizontal ≈ 90 000, i.e. 4–5 orders of magnitude (10$^4$–10$^5$), which is why the hydrostatic approximation works.
- References: Kump et al. Ch. 3 "How Atmospheric Pressure Varies with Altitude"; Wallace & Hobbs §3.2 and 3.2.2.

**III. Thermal structure and composition (slide 55)**
- Troposphere: up to ~10–15 km, heated from below, temperature falls 6.5 °C km$^{-1}$; holds ~80 % of the mass and nearly all water vapour.
- Stratosphere: up to ~50 km, temperature rises with height because ozone absorbs UV; this inversion makes it very stable against vertical mixing.
- Homosphere (below ~100 km): turbulent mixing keeps N$_2$ (78 %), O$_2$ (21 %), Ar (0.9 %) in constant proportions. Heterosphere (above ~100 km): gases separate by molecular weight; H and He dominate at the top.
- Long-lived gases: lifetime much longer than the global mixing time (1–2 years for inter-hemispheric mixing). Short-lived gases: removed (chemistry, rainout) faster than they mix, so concentrations vary strongly in space and time, high near sources.
- References: Kump et al. Ch. 3 "Atmospheric Structure"; Wallace & Hobbs §1.3.4.

**IV. Optical properties: Beer's law and scattering (slide 56)**
- $dI_\lambda=-I_\lambda K_\lambda N\sigma\,ds$ ($N$ particle number, $\sigma$ cross-section, $ds$ path length) integrates to $I_\lambda=I_{\lambda,0}e^{-\tau_\lambda}$.
- Optical depth $\tau_\lambda=\int\rho\,r\,k_\lambda\,dz$ (dimensionless); $\tau_\lambda=1$ means intensity down to 37 % of the original.
- Extinction = scattering + absorption: $K_\lambda(\text{ext})=K_\lambda(\text{sca})+K_\lambda(\text{abs})$.
- Rayleigh scattering ($r\ll\lambda$, molecules): $\propto\lambda^{-4}$, hence the blue sky. Mie scattering ($r\approx\lambda$, droplets and aerosols): weakly wavelength-dependent, hence white or grey clouds.
- References: Kump et al. Ch. 3 "Physical Causes of the Greenhouse Effect" (pp. 48–51); Wallace & Hobbs §4.4.1 (p. 123) and §4.5.1 (p. 130).

**V. Molecular mechanics of the greenhouse effect (slides 57–59)**
- Spectrum split at 4 µm. Shortwave ($\lambda<4$ µm): UV 10–400 nm, visible 400–700 nm, near-IR 0.7–4 µm (counted as shortwave because solar-dominated). Longwave ($\lambda>4$ µm): terrestrial thermal emission.
- Wien: $\lambda_{\max}\approx\frac{2897}{T}$ µm. Sun (photosphere ≈ 5780 K) peaks at ≈ 0.5 µm; Earth (≈ 288 K) peaks at ≈ 10 µm.
- Absorption needs a (transition) dipole moment. Symmetric N$_2$, O$_2$ are transparent to IR; H$_2$O, CO$_2$, O$_3$ (and CH$_4$) absorb. Rotational transitions: far-IR, $\lambda>12$ µm. Vibrational transitions: mid-IR, e.g. CO$_2$ bending mode at 15 µm, O$_3$ vibration–rotation at 9.6 µm.
- Shortwave spectrum (slide 58, top of atmosphere vs surface): UVC (200–290 nm) fully absorbed high up by O$_2$ (photodissociation, forming ozone); UVB (290–320 nm) partly absorbed by stratospheric ozone; UVA (320–400 nm) poorly absorbed, nearly all reaches the surface. Visible (400–700 nm) is the "optical window", slightly reduced by Rayleigh scattering ($\propto\lambda^{-4}$). Near-IR (0.7–3 µm) shows dips from H$_2$O and CO$_2$ absorption, heating the troposphere by about 17 units of incoming solar energy.
- Longwave spectrum (slide 59, Planck envelopes vs satellite-measured outgoing radiation): low outgoing radiation marks gas absorption and re-emission at colder, higher altitude. CO$_2$ 15 µm bending band sits near the peak of Earth's outgoing radiation. H$_2$O rotation band ($\lambda>12$ µm) absorbs virtually 100 % of upwelling longwave there.
- Atmospheric window 8–12 µm (between the CO$_2$ band and the main H$_2$O bands): brightness temperature ≈ 288–290 K, matching the surface (excluding the 9.6 µm ozone dip); the main route by which surface heat escapes to space. CH$_4$, N$_2$O and CFCs absorb inside this window, so small amounts of them are potent greenhouse gases.
- References: Kump et al. Ch. 3 "Molecular Motions and the Greenhouse Gases" (pp. 48–49); Wallace & Hobbs §4.4.3 (p. 127).

## From the post
Hi, Find below the notes of lecture 5 : Atmosphere & Greenhouse gases. (Classroom announcement, 2026-08-20: https://classroom.google.com/c/ODY5MDg2NTA1Mzg0/p/ODc1MjI3ODYxOTYz)

## Files
- [Lecture 5: Atmosphere & Green house gases.pdf](https://drive.google.com/file/d/1LNWhUocLIai26gy-FkiQse6X-PcYNvnR/view?usp=drive_web): read in full. The same text reappears in the compiled L1–L6 notes ([[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs]]).

## Related
- [[introduction-to-climate-science/2026-09-03-study-material-3-pressure-and-geopotential]]: the same hydrostatic equation and scale height derived with $R_dT/g_0$.
- [[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature]]: Planck/Wien/Stefan–Boltzmann background for the spectrum split.
- [[introduction-to-climate-science/2026-09-10-solutions-quiz-1]]: the vertical vs horizontal pressure-gradient ratio appears as a quiz question.
- [[introduction-to-climate-science/2026-09-10-reading-manabe-and-strickler-1964]]: the roles of H$_2$O, CO$_2$, O$_3$ absorption bands.
- [[01-climate/cl06-hydrostatic-balance-and-vertical-structure]]: your chapter notes on hydrostatic balance.
- [[01-climate/concepts/beer-lambert-law-and-optical-depth]]: your concept note on Beer's law and optical depth.
- [[01-climate/concepts/greenhouse-gases-and-absorption-bands]]: your concept note on absorption bands.
- [[01-climate/concepts/atmospheric-window]]: your concept note on the 8–12 µm window.
