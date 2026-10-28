---
id: zettel/coupon-collector-draw-independence-and-conditioning
aliases: ["Coupon Collector Draw Independence and Conditioning", "type absence probabilities under independent sampling", "stamp collection conditional probability"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Coupon Collector Draw Independence and Conditioning

A technique using complement probabilities under independent multinomial draws to evaluate the joint and conditional probabilities of observing specific stamp types across k trials.

$$P[A_i] = 1 - (1 - p_i)^k$$

$$P[A_i \cup A_j] = 1 - (1 - p_i - p_j)^k$$

$$P[A_i \cap A_j] = 1 - (1 - p_i)^k - (1 - p_j)^k + (1 - p_i - p_j)^k$$

$$P[A_i|A_j] = \frac{1 - (1 - p_i)^k - (1 - p_j)^k + (1 - p_i - p_j)^k}{1 - (1 - p_j)^k}$$

## Links

---
Source: Mid-semester solutions, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-22-mid-semester-solutions|Mid-semester solutions]] pp. 1–3
<!-- /kurooto:seen -->
