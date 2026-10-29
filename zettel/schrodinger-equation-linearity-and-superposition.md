---
id: zettel/schrodinger-equation-linearity-and-superposition
aliases: ["Schrödinger Equation Linearity and Superposition", "quantum superposition principle", "Dynamical Evolution of Non-Commuting Observables via Relative Phase", "relative phase time evolution", "off-diagonal expectation value oscillation", "Dynamical Evolution of Observables Driven by Relative Phase", "Superposition Relative Phase Dynamics", "interference cross-term oscillation", "Superposition Principle"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Schrödinger Equation Linearity and Superposition

The property that any linear combination of solutions to the time-dependent Schrödinger equation is itself a valid solution, leading to interference phenomena between non-degenerate states.

$$\psi = c_1 \phi_1 e^{-iE_1 t/\hbar} + c_2 \phi_2 e^{-iE_2 t/\hbar}$$

## Links
- generalises:: [[zettel/particle-in-a-box-time-evolution]] — A general superposition of energy eigenstates contains relative phase differences leading to time-dependent interference terms, generalising single stationary states

---
Source: PH2113_wavefunctions_potentials_schrodinger_Tutorial, pp. 1–4

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger|PH2113_wavefunctions_potentials_schrodinger_Tutorial]] pp. 1–4
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_50min_15marks]] pp. 1–2
- [[ph2113/2026-09-08-tutorial-states-interference-uncertainty|PH2113_tutorial-pdf]] pp. 1–2
- [[ph2113/2026-08-31-states-operators-measurements-notes|PH2113_states_operators_notes]] pp. 1–9
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty|PH2113_tutorial_solutions]] pp. 1–5

### Added from class
- PH2113_Mock_Quiz_50min_15marks pp. 1–2: Explicitly contrasts an individual stationary state's constant probability density with a two-state superposition where differential phase evolution drives non-vanishing time dependence in |Psi(x, t)|^2.
- PH2113_tutorial-pdf pp. 1–2: Explicitly addresses two-state system time evolution |ψ(t)⟩ = (e^{-iE1 t/ħ}|1⟩ + e^{-iE2 t/ħ}|2⟩)/sqrt(2), demonstrating how stationary energy probabilities coexist with oscillating expectation values of non-commuting observables.
- PH2113_states_operators_notes pp. 1–9: Adds the explicit orthonormal basis expansion normalization sum |cn|^2 = 1 and the formal definition of operator linearity preserving superposition.
- PH2113_tutorial_solutions pp. 1–5: Provides the explicit discrete two-level matrix derivation showing how relative phase evolution exp(-i(E2-E1)t/hbar) drives harmonic oscillation in expectation values <X> = cos((E2-E1)t/hbar) of off-diagonal observables while diagonal energy probabilities remain static at 1/2.
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| PH2113_Mock_Quiz_50min_15marks, pp. 1–2 | $E_1, E_2$ | distinct energy eigenvalues of the constituent stationary states |
| PH2113_tutorial_solutions, pp. 1–5 | $X = \|1\rangle\langle 2\| + \|2\rangle\langle 1\|$ | off-diagonal observable operator |
| PH2113_Mock_Quiz_50min_15marks, pp. 1–2 | $\Psi(x, t)$ | time-dependent superposition wave function |
<!-- /kurooto:notation -->
