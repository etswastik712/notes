---
id: zettel/first-colour-arrival-probability-under-sampling-with-replacement
aliases: ["First Colour Arrival Probability under Sampling with Replacement", "First Arrival Order with Replacement", "Geometric First Arrival Probability"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# First Colour Arrival Probability under Sampling with Replacement

The probability that a specific colour is drawn before another designated colour in independent sampling with replacement from a multi-colour urn, evaluated by summing geometric probabilities over disjoint trials.

$$P[E_n] = r^{n-1} g$$

$$P\left[\bigcup_n E_n\right] = \sum_{n \in \mathbb{N}} P[E_n] = \sum_{n \in \mathbb{N}} r^{n-1} g = \frac{g}{1-r} = \frac{g}{g+y}$$

## Links
- equivalent-to:: [[zettel/first-colour-arrival-probability-under-sampling-without-replacement]] — Both models evaluate the exact same probability g/(g+y) for the event that a green ball appears before a yellow ball

---
Source: Quiz 2 solutions, pp. 1–2

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-04-quiz-2-solutions|Quiz 2 solutions]] pp. 1–2
<!-- /kurooto:seen -->
