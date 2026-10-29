---
id: zettel/particle-in-a-box-time-evolution
aliases: ["Particle in a Box Time Evolution", "time evolution of energy eigenstates in a box", "time-dependent infinite well eigenstate", "Stationary State Time Evolution", "energy eigenstate time evolution", "phase factor time evolution", "single energy eigenstate phase evolution", "Stationary State", "state of definite energy", "Stationary State Probability Invariance", "time-independent probability density"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Particle in a Box Time Evolution

The temporal progression of an energy eigenstate inside the box, governed by the multiplication of the spatial mode by a stationary phase factor e^{-i E_n t / \hbar}. Because the time dependence is purely a phase factor, the state remains stationary with a static spatial probability distribution.

$$\Psi(x, t) = \psi(x) e^{-i E_n t / \hbar} = A_n \sin\left(\frac{n\pi x}{a}\right) e^{-i E_n t / \hbar}$$

## Links

---
Source: Particle_in_a_box, pp. 1–10

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger|PH2113_wavefunctions_potentials_schrodinger_Tutorial]] pp. 1–4
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_50min_15marks]] pp. 1–2
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_Ideal_Solutions]] pp. 1–2
- [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators|Particle_in_a_box]] pp. 1–10
- [[ph2113/2026-08-24-lecture-8-uncertainty-wavefunctions-schrodinger|PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1)]] pp. 1–10
- [[ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties|PH2113_Lecture9_FreeParticle_Ring_GeneralProperties]] pp. 1–9

### Added from class
- PH2113_wavefunctions_potentials_schrodinger_Tutorial pp. 1–4: Demonstrates that evolving purely via the stationary phase factor e^{-i E_n t / \hbar} with time-independent probability density holds universally for any Hamiltonian eigenstate, not merely the infinite box.
- PH2113_Mock_Quiz_50min_15marks pp. 1–2: Formalizes the general time-evolution mapping rule phi(x) -> phi(x)exp(-iEt/hbar) for stationary states beyond specific infinite square well configurations.
- PH2113_Mock_Quiz_Ideal_Solutions pp. 1–2: Isolates the general property that any single energy eigenstate has a stationary probability density due to unit-modulus phase cancellation, independent of spatial box geometry.
- PH2113_Lecture9_FreeParticle_Ring_GeneralProperties pp. 1–9: Extends the stationary state concept from the infinite well to general time-independent potentials via separation of variables, proving the time invariance of the spatial probability density.
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| PH2113_Mock_Quiz_50min_15marks, pp. 1–2 | $E$ | energy eigenvalue associated with the stationary state |
| PH2113_Lecture9_FreeParticle_Ring_GeneralProperties, pp. 1–9 | $E$ | Separation constant identifying the definite energy of the state |
| PH2113_Mock_Quiz_50min_15marks, pp. 1–2 | $\phi(x)$ | spatial stationary state wave function of energy E |
| PH2113_Mock_Quiz_Ideal_Solutions, pp. 1–2 | $e^{-iE_1 t/\hbar}$ | stationary state temporal phase factor |
| PH2113_Lecture8_Uncertainty_Wavefunctions_Schrodinger (1), pp. 1–10 | $e^{-iEt/\hbar}$ | stationary temporal phase factor |
<!-- /kurooto:notation -->
