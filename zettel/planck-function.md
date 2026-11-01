---
id: zettel/planck-function
aliases: ["Planck Function", "Planck's law", "spectral radiance of a blackbody"]
tags: [zettel, agent-written, introduction-to-climate-science]
trust_tier: agent_written
---

# Planck Function

The mathematical function specifying the spectral radiance emitted by an ideal blackbody in thermal equilibrium as a function of wavelength and absolute temperature.

$$I(\lambda, T) = \frac{2hc^2}{\lambda^5 \left( e^{\frac{hc}{\lambda k_B T}} - 1 \right)}$$

## Links
- generalises:: [[zettel/wien-s-displacement-law]] — Wien's law is derived directly by setting the derivative of the Planck function with respect to wavelength to zero to locate its spectral peak
- generalises:: [[zettel/stefan-boltzmann-law]] — Integrating the Planck spectral radiance over all wavelengths and solid angles yields the Stefan-Boltzmann total radiative flux equation

---
Source: climate_intro_notes, pp. 17–23

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature|climate_intro_notes]] pp. 17–23
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 17–24
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 25–33
- [[introduction-to-climate-science/books/intro-clim|intro_clim]]
- [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback|Lecture 3 Planetary Energy Balance]] pp. 1–9

### Added from class
- climate_intro_notes_L1_L6 pp. 25–33: Adds the explicit spectral radiance SI unit specification and establishes that the ratio of peak blackbody spectral radiance between the Sun and Earth is approximately 205.
- Lecture 3 Planetary Energy Balance pp. 1–9: Specifies spectral radiance units as W m^-2 sr^-1 m^-1 and notes the Sun to Earth peak radiance ratio of roughly 205.
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| intro_clim | $k$ | Boltzmann constant |
| Lecture 3 Planetary Energy Balance, pp. 1–9 | $k_B$ | Boltzmann constant (1.38×10^-23 J/K) |
| climate_intro_notes, pp. 17–23 | $k_B$ | Boltzmann's constant (1.38 × 10^-23 J/K) |
| climate_intro_notes_L1_L6, pp. 17–24 | $k_B$ | Boltzmann's constant (1.38e-23 J/K) |
| intro_clim | $h$ | Planck constant |
| climate_intro_notes, pp. 17–23 | $h$ | Planck's constant (6.626 × 10^-34 J·s) |
| climate_intro_notes_L1_L6, pp. 17–24 | $h$ | Planck's constant (6.626e-34 J s) |
| climate_intro_notes_L1_L6, pp. 25–33 | $I(\lambda, T)$ | spectral radiance |
| intro_clim | $B_\lambda$ | spectral radiance |
| climate_intro_notes, pp. 17–23 | $I(\lambda, T)$ | Spectral radiance / radiation intensity at wavelength λ and temperature T |
| Lecture 3 Planetary Energy Balance, pp. 1–9 | $I(\lambda, T)$ | spectral radiance in W m^-2 sr^-1 m^-1 |
| intro_clim | $c$ | speed of light |
| climate_intro_notes, pp. 17–23 | $c$ | Speed of light (2.998 × 10^8 m/s) |
| climate_intro_notes_L1_L6, pp. 17–24 | $c$ | Speed of light (2.998e8 m/s) |
<!-- /kurooto:notation -->
