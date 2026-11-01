---
id: zettel/well-ordering-principle
aliases: ["Well-Ordering Principle", "WOP"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Well-Ordering Principle

The principle stating that every non-empty subset of the natural numbers contains a unique least element.

$$\forall S \subseteq \mathbb{N}, (S \neq \emptyset \implies \exists m \in S \text{ such that } \forall s \in S, m \le s)$$

## Links
- equivalent-to:: [[zettel/principle-of-strong-induction]] — WOP implies strong induction by taking the least counterexample in S = {n in N : P(n) is false}
- used-in:: [[zettel/method-of-minimal-counterexample]] — The standard application of WOP assumes a nonempty set of counterexamples S and derives a contradiction from min S

---
Source: Assignment-9, pp. 1–1

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-10-30-assignment-9|Assignment-9]] pp. 1–1
<!-- /kurooto:seen -->
