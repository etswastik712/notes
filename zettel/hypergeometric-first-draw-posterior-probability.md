---
id: zettel/hypergeometric-first-draw-posterior-probability
aliases: ["Hypergeometric First-Draw Posterior Probability", "urn draw exchangeability conditional probability"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Hypergeometric First-Draw Posterior Probability

The conditional probability that the first ball drawn without replacement is of a designated type given the total count of that type drawn over n trials.

$$P[B] = \frac{b}{b+w}$$

$$P[B_k] = \frac{\binom{b}{k}\binom{w}{n-k}}{\binom{b+w}{n}}$$

## Links
- special-case-of:: [[zettel/hypergeometric-promotion-model]] — Uses the hypergeometric probability mass function P[B_k] = \binom{b}{k}\binom{w}{n-k}/\binom{b+w}{n} for the overall count of black balls

---
Source: Practice problems 21st August 2026, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026|Practice problems 21st August 2026]] pp. 1–3
<!-- /kurooto:seen -->
