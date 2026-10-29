---
id: zettel/parity-operator-eigenvalue-action
aliases: ["Parity Operator Eigenvalue Action", "spatial inversion operator", "parity eigenstate", "parity reflection action"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Parity Operator Eigenvalue Action

An operator that maps a spatial wave function to its coordinate inversion psi(-x). Even functions satisfy P psi(x) = +psi(x) (eigenvalue +1) and odd functions satisfy P psi(x) = -psi(x) (eigenvalue -1), whereas complex exponential plane waves map to counter-propagating states e^{-ikx} and are not parity eigenstates.

$$\hat{P} \psi(x) = \psi(-x)$$

$$\psi_1(x) = \cos kx$$

$$\psi_2(x) = e^{ikx}$$

## Links
- contrasts-with:: [[zettel/plane-wave-momentum-eigenstate]] — A plane wave e^{ikx} is an eigenstate of the momentum operator but is mapped to e^{-ikx} by parity, failing to be an eigenstate of P̂
- example-of:: [[zettel/non-preservation-of-eigenstate-under-non-degenerate-superposition]] — Decomposing cos(kx) into (e^{ikx} + e^{-ikx})/2 illustrates how superpositions of opposite-momentum eigenstates form parity eigenstates

---
Source: PH2113_Mock_Quiz_50min_15marks, pp. 1–2

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_50min_15marks]] pp. 1–2
<!-- /kurooto:seen -->
