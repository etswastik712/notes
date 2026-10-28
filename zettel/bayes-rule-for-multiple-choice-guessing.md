---
id: zettel/bayes-rule-for-multiple-choice-guessing
aliases: ["Bayes' Rule for Multiple Choice Guessing", "multiple-choice examination guessing model"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Bayes' Rule for Multiple Choice Guessing

An application of Bayes' theorem and the law of total probability to infer the posterior probability that an examinee knows the answer given that they answered correctly, assuming random guessing among n options upon not knowing.

$$P[R] = P[R|K]P[K] + P[R|K^c]P[K^c] = p + \frac{1}{n}(1 - p)$$

$$P[K|R] = \frac{P[R|K]P[K]}{P[R]} = \frac{np}{1 + p(n - 1)}$$

## Links

---
Source: Mid-semester solutions, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-22-mid-semester-solutions|Mid-semester solutions]] pp. 1–3
<!-- /kurooto:seen -->
