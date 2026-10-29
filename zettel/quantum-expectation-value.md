---
id: zettel/quantum-expectation-value
aliases: ["Quantum Expectation Value", "expectation value", "ensemble mean of observable"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Quantum Expectation Value

The ensemble average of measurement outcomes obtained by repeatedly preparing identical copies of a state and measuring an observable. Computed as an eigenvalue sum weighted by Born probabilities, or as an inner product sandwich integral over coordinate space.

$$\langle A \rangle = \sum_a |c_a|^2 a$$

$$\langle A \rangle = \int \Psi^*(x) \hat{A} \Psi(x) \, dx$$

$$\langle p \rangle = \int \Psi^* \left(-i\hbar \frac{d}{dx}\right) \Psi \, dx$$

## Links
- special-case-of:: [[zettel/particle-in-a-box-momentum-expectation-value]] — The integral formula evaluates <p> = 0 for stationary standing-wave box states

---
Source: PH2113_states_operators_notes, pp. 1–9

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-08-31-states-operators-measurements-notes|PH2113_states_operators_notes]] pp. 1–9
<!-- /kurooto:seen -->
