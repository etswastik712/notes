---
id: zettel/principle-of-strong-induction
aliases: ["Principle of Strong Induction", "strong induction"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Principle of Strong Induction

A proof method asserting that a statement P(n) holds for all natural numbers n if the base case P(1) is true and the truth of P(1) through P(k) collectively implies P(k + 1) for every k in N.

$$(P(1) \land (\forall k \in \mathbb{N}, (P(1) \land \dots \land P(k) \implies P(k+1)))) \implies \forall n \in \mathbb{N}, P(n)$$

## Links
- equivalent-to:: [[zettel/well-ordering-principle]] — PMI, strong induction, and WOP are stated as three equivalent statements about the natural numbers N

---
Source: Assignment-9, pp. 1–1

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-10-30-assignment-9|Assignment-9]] pp. 1–1
<!-- /kurooto:seen -->
