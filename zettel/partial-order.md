---
id: zettel/partial-order
aliases: ["Partial Order", "partially ordered set relation", "poset relation"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Partial Order

A binary relation on a set that satisfies reflexivity, antisymmetry, and transitivity.

$$a \le a$$

$$a \le b \land b \le a \implies a = b$$

$$a \le b \land b \le c \implies a \le c$$

## Links
- contrasts-with:: [[zettel/equivalence-relation]] — Both are reflexive and transitive relations, but a partial order requires antisymmetry whereas an equivalence relation requires symmetry

---
Source: Mid-Sem-Exam-MT2133-solutions-students, pp. 1–4

<!-- kurooto:seen -->
- example-of:: [[zettel/product-order-on-z-x-z]] — Its summary defines a partial order on pairs of integers, with (a, b) ≤ (c, d) iff a ≤ c and b ≤ d, which is a concrete instance of the partial order defined here
- needs:: [[zettel/chain-in-a-poset]] — A chain is defined as a subset of a partially ordered set in which any two elements are comparable under its ordering relation, so the partial order is required to define it
- needs:: [[zettel/upper-bound-in-a-poset]] — An upper bound is defined as an element of a partially ordered set that is greater than or equal to every element of a given subset, which relies on the partial order's ≤
- needs:: [[zettel/maximal-element-in-a-poset]] — The maximal element summary uses the partial order's ≤ in its condition m ≤ x implies x = m, so it depends on this relation
- needs:: [[zettel/minimum-element-in-a-poset]] — A minimum element is described as an element of a partially ordered set that is less than or equal to every element in the set, so it is defined using the partial order
## Seen in
- [[intro-to-proofs/2026-10-05-mid-term-paper-answer-key|Mid-Sem-Exam-MT2133-solutions-students]] pp. 1–4
<!-- /kurooto:seen -->
