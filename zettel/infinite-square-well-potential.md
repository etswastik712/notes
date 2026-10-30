---
id: zettel/infinite-square-well-potential
aliases: ["Infinite Square Well Potential", "particle in a box potential", "one-dimensional box potential"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Infinite Square Well Potential

A one-dimensional potential that is identically zero inside a finite interval between zero and width a, and infinite everywhere outside. This potential strictly confines a particle to the interior domain since the wavefunction must vanish where the potential is infinite.

$$V(x) = \begin{cases} 0 & 0 < x < a \\ \infty & \text{elsewhere} \end{cases}$$

## Links
- generalises:: [[zettel/deep-wide-well-approximation]] — The infinite square well represents the exact infinite depth limit approached by the finite potential well

---
Source: Particle_in_a_box, pp. 1–10

<!-- kurooto:seen -->
- example-of:: [[zettel/particle-in-a-box-momentum-expectation-value]] — It computes the momentum expectation value for the stationary states of this same infinite well and shows it vanishes by parity
- example-of:: [[zettel/particle-in-a-box-position-expectation-value]] — It computes the position expectation value for the stationary states of this infinite well, using the reflection symmetry about the midpoint
- example-of:: [[zettel/particle-in-a-box-time-evolution]] — It applies the time-dependent phase factor e^{-iE_n t/ħ} to the energy eigenstates of this infinite well
## Seen in
- [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators|Particle_in_a_box]] pp. 1–10
<!-- /kurooto:seen -->
