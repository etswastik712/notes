---
id: zettel/natural-number-order
aliases: ["Natural Number Order", "Order on N", "Strict and non-strict order"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Natural Number Order

A relation defined such that a is strictly less than b if b equals a plus some natural number, and less than or equal if either strictly less or equal.

$$a < b \iff \exists x \in \mathbb{N} \ (b = a + x)$$

$$a \leq b \iff a < b \lor a = b$$

## Links
- needs:: [[zettel/recursive-definition-of-addition]] — The order relation is defined directly in terms of additive decomposition by an element x in N
- used-in:: [[zettel/discrete-order-step-property]] — Supplies the definitions of < and <= used to evaluate the gap between a and b

---
Source: L-25, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-11-10-peano-s-axioms|L-25]] pp. 1–3
<!-- /kurooto:seen -->
