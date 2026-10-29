---
id: zettel/countability-of-the-rationals
aliases: ["Countability of the Rationals", "countability of Q"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Countability of the Rationals

The set of rational numbers Q is countable by demonstrating that positive rationals can be enumerated via diagonal traversal omitting duplicates, extending to negative rationals by symmetry, and interleaving with zero.

$$f : \mathbb{N} \to \mathbb{Q}_{>0} = \{a_1, a_2, a_3, \dots\}$$

$$\mathbb{Q} = \mathbb{Q}_{<0} \cup \mathbb{Q}_{>0} \cup \{0\}$$

## Links
- needs:: [[zettel/diagonal-traversal-enumeration]] — The explicit enumeration sequence {a_k} of Q_{>0} is constructed by traversing the grid of fractions along diagonals m + n = c

---
Source: Countable-Uncountable-sets, pp. 1–6

<!-- kurooto:seen -->
- generalises:: [[zettel/countability-of-subsets]] — Countability of Q follows from the rationals being a superset of the countable set of positive rationals and the subset-of-countable principle, so the subsets note covers the same countability reasoning in general form
- contrasts-with:: [[zettel/uncountable-set]] — The uncountable-set note defines the opposite property, so it marks the boundary that the rationals are shown not to cross, which gives a useful contrast with countability of Q
- contrasts-with:: [[zettel/uncountability-of-the-real-numbers]] — Showing R is uncountable while Q is countable is the standard contrast between the two sets, and the real-numbers note sits directly on that boundary
## Seen in
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20|Countable-Uncountable-sets]] pp. 1–6
<!-- /kurooto:seen -->
