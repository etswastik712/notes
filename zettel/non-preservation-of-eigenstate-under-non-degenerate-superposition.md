---
id: zettel/non-preservation-of-eigenstate-under-non-degenerate-superposition
aliases: ["Non-Preservation of Eigenstate Under Non-Degenerate Superposition", "superposition of non-degenerate eigenstates", "eigenvalue weighting of superposition components"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Non-Preservation of Eigenstate Under Non-Degenerate Superposition

A linear superposition of eigenstates corresponding to distinct eigenvalues is not an eigenstate of the operator. When the operator acts on the superposition, each constituent is scaled by its own distinct eigenvalue, altering their relative coefficients and yielding a resulting state that is not proportional to the original vector.

$$\hat{A}v = \frac{1}{\sqrt{2}}(\hat{A}u_+ + \hat{A}u_-) = \frac{1}{\sqrt{2}}(u_+ - u_-)$$

$$\frac{1}{\sqrt{2}}(u_+ + u_-) \longrightarrow \frac{1}{\sqrt{2}}(u_+ - u_-)$$

## Links
- contrasts-with:: [[zettel/eigenstate-definite-value-principle]] — Shows that superpositions of distinct eigenstates destroy definite measurement outcomes by altering relative component amplitudes
- used-in:: [[zettel/two-dimensional-quantum-state]] — Employs two-component vectors [1, 1]^T and [1, -1]^T to explicitly evaluate operator action on superpositions
- generalises:: [[zettel/plane-wave-momentum-eigenstate]] — Provides the general linear algebraic theorem explaining why standing wave cos(kx) is not an eigenstate of momentum

---
Source: PH2113_Quiz_Ideal_Solutions, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_50min_15marks]] pp. 1–2
- [[ph2113/2026-09-03-quiz-ideal-solutions|PH2113_Quiz_Ideal_Solutions]] pp. 1–3

### Added from class
- PH2113_Mock_Quiz_50min_15marks pp. 1–2: Supplies the explicit 2x2 matrix representation involving the Pauli-X operator Â and the canonical basis state v = (1, 0)^T = (u_+ + u_-)/sqrt(2), showing Av = (0, 1)^T is orthogonal rather than proportional.
<!-- /kurooto:seen -->
