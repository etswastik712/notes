---
id: zettel/hypergeometric-promotion-model
aliases: ["Hypergeometric Promotion Model", "Hypergeometric Sampling Without Replacement"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Hypergeometric Promotion Model

A discrete probability model for the number of members of a designated subgroup selected when drawing a fixed sample size uniformly at random without replacement from a finite population.

$$P[W = k] = \frac{\binom{n}{k}\binom{m}{t-k}}{\binom{m+n}{t}}$$

## Links

---
Source: Practice problems 17th September and following tutorial and weekend, pp. 1–2

<!-- kurooto:seen -->
- contrasts-with:: [[zettel/binomial-promotion-model]] — Both models count how many members of a subgroup are selected, but the binomial model draws each member independently with a constant probability, while the hypergeometric model draws a fixed sample size without replacement
## Seen in
- [[introduction-to-probability/2026-09-17-practice-problems-17th-september-and-following-tutorial-and-weekend|Practice problems 17th September and following tutorial and weekend]] pp. 1–2
<!-- /kurooto:seen -->
