---
id: zettel/position-dependent-phase-and-momentum-content
aliases: ["Position-Dependent Phase and Momentum Content", "spatial phase factor", "position-dependent phase factor", "momentum shift via spatial phase"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Position-Dependent Phase and Momentum Content

Multiplying a wavefunction by a spatially varying phase factor e^{i k x} preserves the local position probability density but modifies the momentum expectation value and action of the momentum operator. Consequently, two quantum states with identical spatial probability distributions can possess completely different momentum content.

$$|\psi_1(x)|^2 = |\psi_2(x)|^2$$

$$\hat{p}\psi_2 = -i\hbar \frac{d}{dx} (e^{ikx}\psi_1) = e^{ikx}(\hat{p}\psi_1 + \hbar k \psi_1)$$

## Links
- needs:: [[zettel/canonical-commutation-relation-position-momentum]] — The differential representation p̂ = -iℏ d/dx generates the extra ℏk shift through the product rule
- contrasts-with:: [[zettel/potential-energy-zero-gauge-invariance]] — A constant temporal phase leaves all physical observables invariant, whereas a position-dependent phase alters momentum observables

---
Source: PH2113_Quiz_Ideal_Solutions, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-03-quiz-ideal-solutions|PH2113_Quiz_Ideal_Solutions]] pp. 1–3
<!-- /kurooto:seen -->
