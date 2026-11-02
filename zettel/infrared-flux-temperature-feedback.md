---
id: zettel/infrared-flux-temperature-feedback
aliases: ["Infrared Flux-Temperature Feedback", "IR Flux/Temperature Feedback", "Planck Feedback"]
tags: [zettel, agent-written, introduction-to-climate-science]
trust_tier: agent_written
---

# Infrared Flux-Temperature Feedback

A stabilizing negative climate feedback mechanism whereby an increase in surface temperature increases outgoing longwave infrared radiation emitted to space, inducing radiative cooling that restores thermal equilibrium.

## Links
- part-of:: [[zettel/earth-system-science]] — Acts as the fundamental negative feedback loop maintaining thermal homeostasis in the planetary energy balance
- contrasts-with:: [[zettel/ice-albedo-feedback]] — Contrasts as a stabilizing negative radiative feedback against the destabilizing positive feedback of ice-albedo

---
Source: climate_intro_notes, pp. 2–16

<!-- kurooto:seen -->
- needs:: [[zettel/stefan-boltzmann-law]] — The outgoing longwave radiation whose increase with surface temperature drives this feedback is governed by the fourth-power dependence in the Stefan-Boltzmann law
- needs:: [[zettel/planck-function]] — The spectral distribution of outgoing infrared emission that the feedback depends on is specified by the Planck function, which the notes list among the blackbody emission relations
- needs:: [[zettel/blackbody]] — The feedback concerns thermal emission to space from the Earth's surface, which the notes model using the blackbody radiator idealization
## Seen in
- [[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature|climate_intro_notes]] pp. 2–16
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 2–16
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 25–33
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 34–42
- [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback|Lecture 4 Sensitivity & (albedo) Feedback]] pp. 1–7
- [[introduction-to-climate-science/2026-08-19-lecture-4-sensitivity-and-albedo-feedback|Lecture 3 Planetary Energy Balance]] pp. 1–9

### Added from class
- climate_intro_notes_L1_L6 pp. 25–33: Formulates stable equilibrium stability criteria via graphical intersection analysis where outgoing longwave flux exceeds net shortwave insolation during warming perturbations.
- climate_intro_notes_L1_L6 pp. 34–42: Formulates the Planck feedback mathematically as the differential sensitivity parameter Λ_P = dT_s/dF = 1/(4σ T_s^3), yielding ~0.28 K (W m^-2)^-1 at Earth's effective radiating temperature of 255 K.
- Lecture 4 Sensitivity & (albedo) Feedback pp. 1–7: Provides the explicit analytical derivative formulation Lambda_P = dTs/dF = 1/(4 sigma Ts^3) evaluating to ~0.28 K (W m^-2)^-1 at Te = 255 K (requiring ~3.8 W/m^2 per 1 K rise).
- Lecture 3 Planetary Energy Balance pp. 1–9: Analyzes dynamic perturbation response curves: displacement right causes LWout > SWnet inducing cooling, while displacement left causes SWnet > LWout inducing warming.
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| Lecture 3 Planetary Energy Balance, pp. 1–9 | $SW_{net}$ | net absorbed incoming shortwave solar flux |
| climate_intro_notes_L1_L6, pp. 25–33 | $SW_{net}$ | net incoming shortwave solar radiation |
| climate_intro_notes_L1_L6, pp. 25–33 | $LW_{out}$ | outgoing longwave radiation |
| Lecture 3 Planetary Energy Balance, pp. 1–9 | $LW_{out}$ | outgoing longwave radiative flux |
| climate_intro_notes_L1_L6, pp. 34–42 | $\Lambda_P$ | Planck climate sensitivity |
| Lecture 4 Sensitivity & (albedo) Feedback, pp. 1–7 | $\Lambda_P$ | Planck feedback sensitivity parameter |
<!-- /kurooto:notation -->
