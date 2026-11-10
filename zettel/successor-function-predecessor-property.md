---
id: zettel/successor-function-predecessor-property
aliases: ["Successor Function Predecessor Property", "Lemma 1", "Existence and uniqueness of predecessors"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Successor Function Predecessor Property

Every element of a Peano system distinct from the distinguished element 1 is the successor of exactly one element.

$$n \neq 1 \implies \exists! m \in \mathbb{N} \text{ such that } n = s(m)$$

## Links
- needs:: [[zettel/peano-system]] — The proof establishes surjectivity onto N \ {1} via induction (P3) and uniqueness via injectivity (P2)
- used-in:: [[zettel/discrete-order-step-property]] — Expressing any x distinct from 1 as y + 1 provides the decomposition needed to show a + 1 <= b

---
Source: L-25, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-11-10-peano-s-axioms|L-25]] pp. 1–3
<!-- /kurooto:seen -->
