---
id: zettel/peano-system
aliases: ["Peano System", "Peano's axioms", "Peano axioms"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Peano System

A triple consisting of a set N, a distinguished element 1, and a successor function s from N to N satisfying three foundational axioms: 1 is not in the image of s, s is injective, and any subset containing 1 and closed under s equals N.

$$1 \notin \operatorname{Im}(s)$$

$$s(m) = s(n) \implies m = n$$

$$S \subseteq \mathbb{N}, 1 \in S, s(S) \subseteq S \implies S = \mathbb{N}$$

## Links
- used-in:: [[zettel/successor-function-predecessor-property]] — Axioms (P2) and (P3) are directly invoked to show every element except 1 has a unique predecessor
- used-in:: [[zettel/recursive-definition-of-addition]] — Induction axiom (P3) guarantees that addition is well-defined across all natural numbers

---
Source: L-25, pp. 1–3

<!-- kurooto:seen -->
- used-in:: [[zettel/recursive-definition-of-multiplication]] — The recursive multiplication rules n · 1 := n and n · (m + 1) := n · m + n are defined on the same Peano system, using the addition that the system's successor function generates
## Seen in
- [[intro-to-proofs/2026-11-10-peano-s-axioms|L-25]] pp. 1–3
<!-- /kurooto:seen -->
