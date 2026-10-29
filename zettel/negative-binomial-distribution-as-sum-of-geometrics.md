---
id: zettel/negative-binomial-distribution-as-sum-of-geometrics
aliases: ["Negative Binomial Distribution as Sum of Geometrics", "Negative Binomial decomposition"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Negative Binomial Distribution as Sum of Geometrics

A Negative Binomial(k, p) random variable, representing the number of independent Bernoulli(p) trials needed to observe the k-th success, decomposes into a sum of k independent Geometric(p) random variables representing the waiting times between successive successes.

$$Y = X_1 + X_2 + \cdots + X_k$$

## Links
- needs:: [[zettel/independence-of-random-variables]] — The components X_i representing waiting intervals between heads are independent due to trial independence
- used-in:: [[zettel/linearity-of-expectation]] — Linearity of expectation allows immediate computation of E[Y] as the sum of k identical Geometric expectations

---
Source: Class notes 2nd September 2026, pp. 1–4

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-02-proof-of-expectation-of-binomial-rv|Class notes 2nd September 2026]] pp. 1–4
<!-- /kurooto:seen -->
