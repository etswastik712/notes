---
id: zettel/joint-probability-mass-function
aliases: ["Joint Probability Mass Function", "joint pmf", "joint distribution of discrete random variables"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Joint Probability Mass Function

The joint probability mass function of two discrete random variables assigns probabilities to the simultaneous realization of specific values for both variables, defined as the probability of the intersection of the two corresponding pre-image events.

$$p(a_i, b_j) = P[X_1 = a_i, X_2 = b_j] = P(\{X_1 = a_i\} \cap \{X_2 = b_j\})$$

## Links
- used-in:: [[zettel/independence-of-random-variables]] — Independence of discrete random variables is formulated as the factorisation of the joint pmf into the product of marginal pmfs
- used-in:: [[zettel/linearity-of-expectation]] — The discrete derivation of E[X_1 + X_2] expands the sum weighted by the joint pmf p(a_i, b_j)

---
Source: Class notes 2nd September 2026, pp. 1–4

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv|Class notes 2nd September 2026]] pp. 1–4
<!-- /kurooto:seen -->
