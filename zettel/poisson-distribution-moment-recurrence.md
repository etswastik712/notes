---
id: zettel/poisson-distribution-moment-recurrence
aliases: ["Poisson Distribution Moment Recurrence", "Poisson moments relation", "expectation recurrence for Poisson"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Poisson Distribution Moment Recurrence

A recursive relation expressing the n-th moment of a Poisson-distributed random variable in terms of the expectation of the (n-1)-th power of the shifted variable. It is derived by shifting the summation index in the definition of expected value.

$$E[X^n] = \lambda E[(X + 1)^{n-1}]$$

## Links

---
Source: Mid-semester solutions, pp. 1–3

<!-- kurooto:seen -->
- special-case-of:: [[zettel/raw-moment]] — The note gives a recurrence for the n-th moment of a Poisson variable, and the raw moment is the general quantity E[X^n] that this recurrence computes for the Poisson case
## Seen in
- [[introduction-to-probability/2026-09-22-mid-semester-solutions|Mid-semester solutions]] pp. 1–3
<!-- /kurooto:seen -->
