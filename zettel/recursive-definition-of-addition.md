---
id: zettel/recursive-definition-of-addition
aliases: ["Recursive Definition of Addition", "Addition on Peano systems"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Recursive Definition of Addition

A binary operation on a Peano system defined recursively from the successor function by setting addition of 1 to be the successor, and addition of a successor to be the successor of the sum.

$$n + 1 := s(n)$$

$$n + s(m) := s(n + m)$$

## Links
- needs:: [[zettel/peano-system]] — The induction axiom guarantees that specifying the value for 1 and for s(m) covers all second arguments
- used-in:: [[zettel/associativity-of-addition]] — The inductive definition provides the base case and inductive step identity for proving associativity
- used-in:: [[zettel/commutativity-with-one]] — The defining clauses are substituted directly into the base and inductive steps of the proof

---
Source: L-25, pp. 1–3

<!-- kurooto:seen -->
- used-in:: [[zettel/recursive-definition-of-multiplication]] — The multiplication note defines n · (m + 1) as n · m + n, which relies on the addition defined here
- used-in:: [[zettel/natural-number-order]] — The order relation is defined by a < b iff b = a + x for some natural x, so it depends on the addition defined here
## Seen in
- [[intro-to-proofs/2026-11-10-peano-s-axioms|L-25]] pp. 1–3
<!-- /kurooto:seen -->
