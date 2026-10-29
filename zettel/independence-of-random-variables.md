---
id: zettel/independence-of-random-variables
aliases: ["Independence of Random Variables", "independent random variables"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Independence of Random Variables

Two real-valued random variables are independent if the joint probability of their lower contour sets factors into the product of their individual probabilities for all real thresholds. For discrete variables, this is equivalent to the joint probability mass function factorising into the product of the marginal mass functions for all outcome pairs.

$$P[X_1 \leqslant x_1, X_2 \leqslant x_2] = P[X_1 \leqslant x_1] P[X_2 \leqslant x_2] \quad \text{for all } x_1, x_2 \in \mathbb{R}$$

$$P[X_1 = a_i, X_2 = b_j] = P[X_1 = a_i] P[X_2 = b_j] \quad \text{for all } i, j$$

## Links
- needs:: [[zettel/joint-probability-mass-function]] — Discrete independence requires the joint probability mass function P[X_1 = a_i, X_2 = b_j] to factor into marginal probabilities
- used-in:: [[zettel/negative-binomial-distribution-as-sum-of-geometrics]] — The decomposition of the waiting time for the k-th success into a sum requires the intervening Geometric intervals to be independent

---
Source: Class notes 2nd September 2026, pp. 1–4

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv|Class notes 2nd September 2026]] pp. 1–4
<!-- /kurooto:seen -->
