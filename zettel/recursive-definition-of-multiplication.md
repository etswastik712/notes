---
id: zettel/recursive-definition-of-multiplication
aliases: ["Recursive Definition of Multiplication", "Multiplication on Peano systems"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Recursive Definition of Multiplication

A binary operation on a Peano system defined recursively by fixing the product with 1 to be the element itself, and the product with a successor as the original product plus the multiplicand.

$$n \cdot 1 := n$$

$$n \cdot (m + 1) := n \cdot m + n$$

## Links
- needs:: [[zettel/recursive-definition-of-addition]] — The inductive step defines multiplication by adding n to the prior product

---
Source: L-25, pp. 1–3

<!-- kurooto:seen -->
- needs:: [[zettel/peano-system]] — The summary defines multiplication as a binary operation on a Peano system, so the Peano system's set, distinguished element 1 and successor function are the setting for the definition
## Seen in
- [[intro-to-proofs/2026-11-10-peano-s-axioms|L-25]] pp. 1–3
<!-- /kurooto:seen -->
