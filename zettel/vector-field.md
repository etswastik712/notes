---
id: zettel/vector-field
aliases: ["Vector Field", "smooth vector field", "vectorfields"]
tags: [zettel, agent-written, mt3184-differential-geometry-and-lie-groups]
trust_tier: agent_written
---

# Vector Field

A smooth vector field on a manifold M is a smooth section of the tangent bundle TM, meaning a smooth map X: M -> TM such that pi circ X = id_M. Locally in coordinates, it acts as a derivation on smooth functions and forms a module over C^infinity(M).

$$\pi \circ X = \operatorname{id}_M$$

$$X = \sum_i X^i \frac{\partial}{\partial x^i}$$

## Links
- used-in:: [[zettel/lie-bracket-of-vector-fields]] — The Lie bracket is an algebraic operation defined specifically on pairs of smooth vector fields
- used-in:: [[zettel/integral-curve]] — An integral curve is defined by requiring its velocity vector at each point to equal the value of the vector field

---
Source: DG10, pp. 1–4

<!-- kurooto:seen -->
## Seen in
- [[mt3184-differential-geometry-and-lie-groups/2026-08-27-august-24-28|DG10]] pp. 1–4
<!-- /kurooto:seen -->
