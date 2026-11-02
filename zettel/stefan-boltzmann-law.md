---
id: zettel/stefan-boltzmann-law
aliases: ["Stefan-Boltzmann Law", "Stefan-Boltzmann radiation law"]
tags: [zettel, agent-written, introduction-to-climate-science]
trust_tier: agent_written
---

# Stefan-Boltzmann Law

A physical law stating that the total radiant energy flux emitted per unit surface area of a blackbody across all wavelengths is directly proportional to the fourth power of its absolute thermodynamic temperature.

$$F = \sigma T^4$$

## Links
- needs:: [[zettel/planck-function]] — Total hemispherical flux F is obtained by integrating Planck's spectral radiance over all wavelengths and forward solid angles

---
Source: climate_intro_notes, pp. 17–23

<!-- kurooto:seen -->
- needs:: [[zettel/blackbody]] — The law gives the emitted flux F = σT⁴ for a blackbody, so the blackbody idealisation is the object it applies to
- contrasts-with:: [[zettel/wien-s-displacement-law]] — Wien's law locates the peak wavelength of blackbody emission as T rises, while Stefan-Boltzmann gives the total emitted flux, which also rises with T but as T⁴
## Seen in
- [[introduction-to-climate-science/2026-09-17-study-material-5-radiative-balance|Radiative_balance_Marshall_and_Plumb]] pp. 1–11
- [[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature|climate_intro_notes]] pp. 17–23
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 17–24
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 25–33
- [[introduction-to-climate-science/books/intro-clim|intro_clim]]
- [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback|Lecture 3 Planetary Energy Balance]] pp. 1–9

### Added from class
- climate_intro_notes_L1_L6 pp. 17–24: Specifies total emitted energy flux denoted as F with units W/m^2, gives constant value sigma = 5.67e-8 W/m^2/K^4, and contrasts solar shortwave with Earth longwave emission budgets.
- climate_intro_notes_L1_L6 pp. 25–33: Introduces the 16-fold flux scaling for doubled temperature and applies the fourth-power nonlinearity to explain Mercury's lower mean temperature via the inequality of average fourth-power temperature versus fourth power of average temperature.
- intro_clim: Provides the explicit zero-dimensional numerical root-finding formulation balancing incoming shortwave flux S(1-a)/4 against outgoing longwave emission sigma*T^4 across solar system planets.
- Lecture 3 Planetary Energy Balance pp. 1–9: Highlights that doubling absolute temperature increases radiated energy flux by a factor of 16 (2^4).
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| climate_intro_notes_L1_L6, pp. 17–24 | $T$ | Absolute temperature in Kelvins |
| climate_intro_notes, pp. 17–23 | $T$ | Absolute thermodynamic temperature in Kelvins |
| climate_intro_notes, pp. 17–23 | $\sigma$ | Stefan-Boltzmann constant (5.67 × 10^-8 W/m^2/K^4) |
| climate_intro_notes_L1_L6, pp. 17–24 | $\sigma$ | Stefan-Boltzmann constant (5.67e-8 W/m^2/K^4) |
| Lecture 3 Planetary Energy Balance, pp. 1–9 | $\sigma$ | Stefan-Boltzmann constant (5.67×10^-8 W/m^2/K^4) |
| climate_intro_notes_L1_L6, pp. 17–24 | $F$ | Total energy flux in W/m^2 |
| climate_intro_notes, pp. 17–23 | $F$ | Total radiant energy flux per unit area in W/m^2 |
| Lecture 3 Planetary Energy Balance, pp. 1–9 | $F$ | total radiative energy flux in W/m^2 |
<!-- /kurooto:notation -->
