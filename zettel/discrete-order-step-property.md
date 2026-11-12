---
id: zettel/discrete-order-step-property
aliases: ["Discrete Order Step Property", "Theorem 5", "No natural number strictly between a and a + 1"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Discrete Order Step Property

If a is strictly less than b in a Peano system, then the successor a + 1 is less than or equal to b, demonstrating the discrete nature of the order.

$$a < b \implies a + 1 \leq b$$

## Links
- needs:: [[zettel/natural-number-order]] — The hypothesis and conclusion are assertions about the order relations < and <=
- needs:: [[zettel/successor-function-predecessor-property]] — Decomposes the additive witness x into y + 1 whenever x is not equal to 1
- needs:: [[zettel/commutativity-with-one]] — Commutes y + 1 to 1 + y within the additive expression a + (y + 1)
- needs:: [[zettel/associativity-of-addition]] — Re-associates a + (1 + y) into (a + 1) + y

---
Source: L-25, pp. 1–3

<!-- kurooto:seen -->
- needs:: [[zettel/recursive-definition-of-addition]] — The statement uses a + 1, and that sum is only defined by the recursive definition n + 1 := s(n) given in the addition note
## Seen in
- [[intro-to-proofs/2026-11-10-peano-s-axioms|L-25]] pp. 1–3
<!-- /kurooto:seen -->
