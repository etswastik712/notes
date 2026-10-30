---
id: zettel/diurnal-thermal-inertia-model
aliases: ["Diurnal Thermal Inertia Model", "diurnal temperature variation model", "transient surface heat-balance model", "transient diurnal energy balance"]
tags: [zettel, agent-written, introduction-to-climate-science]
trust_tier: agent_written
---

# Diurnal Thermal Inertia Model

A transient zero-dimensional energy balance model governing the diurnal surface temperature cycle of an airless body by balancing surface layer heat storage against periodic solar insolation and quartic longwave emission.

$$C \frac{dT_s}{dt} = S_0 (1 - \alpha) \sin\left(\frac{2\pi t}{86400}\right) \Theta\left(\sin\left(\frac{2\pi t}{86400}\right)\right) - \sigma T_s^4$$

$$C = \rho \cdot d \cdot c_p$$

## Links
- needs:: [[zettel/stefan-boltzmann-law]] — Provides the radiative cooling sink -\sigma T_s^4 in the governing differential equation
- generalises:: [[zettel/zero-dimensional-energy-balance-model]] — Extends steady-state 0-D radiative equilibrium to a time-dependent differential equation with finite thermal capacity

---
Source: climate_intro_notes_L1_L6, pp. 53–63

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 53–63
<!-- /kurooto:seen -->
