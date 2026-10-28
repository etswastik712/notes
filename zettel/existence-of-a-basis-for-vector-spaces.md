---
id: zettel/existence-of-a-basis-for-vector-spaces
aliases: ["Existence of a Basis for Vector Spaces", "every vector space has a basis"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Existence of a Basis for Vector Spaces

Every vector space over an arbitrary field possesses a basis, proven by treating the trivial space with the empty set and using Zorn's lemma on inclusion-ordered linearly independent subsets for non-trivial spaces.

$$\operatorname{span}(\emptyset) = \{0\}$$

$$U = \bigcup_{S \in C} S$$

## Links
- needs:: [[zettel/zorn-s-lemma]] — The proof relies on Zorn's lemma to extract a maximal linearly independent subset from the poset
- needs:: [[zettel/linear-independence]] — The poset used in the non-trivial case consists of all linearly independent subsets of V

---
Source: Zorn's_lemma, pp. 1–5

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-09-15-application-of-zorn-s-lemma|Zorn's_lemma]] pp. 1–5
<!-- /kurooto:seen -->
