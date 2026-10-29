---
id: zettel/countability-of-subsets
aliases: ["Countability of Subsets", "subset of countable set is countable", "subsets of countable sets"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Countability of Subsets

Every non-empty subset of a countable set is countable. If the ambient set is finite, the subset is finite; if the ambient set is countably infinite and the subset infinite, the subset is countably infinite via the well-ordering principle.

$$n_{k+1} = \min\{n \in \mathbb{N} : n > n_k, f(n) \in S\}$$

$$g(k) = f(n_k)$$

## Links
- contrasts-with:: [[zettel/uncountable-set]] — Establishing that subsets of countable sets remain countable shows countability is hereditary, contrasting with sets having uncountable cardinality

---
Source: Solutions_Assignment_7, pp. 1–2

<!-- kurooto:seen -->
- used-in:: [[zettel/finite-set-proper-subset-non-equivalence]] — The note's finite-ambient case (a subset of a finite set is finite) relies on the fact that finite sets are not in bijection with proper subsets, which that note establishes
## Seen in
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20|Solutions_Assignment_7]] pp. 1–2
<!-- /kurooto:seen -->
