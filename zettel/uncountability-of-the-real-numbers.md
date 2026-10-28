---
id: zettel/uncountability-of-the-real-numbers
aliases: ["Uncountability of the Real Numbers", "R is uncountable"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Uncountability of the Real Numbers

The set of real numbers R is uncountable, proven by constructing an explicit piecewise algebraic bijection between (0, 1) and R and applying the uncountability of (0, 1).

$$f(x) = \begin{cases} 1 - \frac{1}{2x} & 0 < x \le \frac{1}{2} \\ \frac{1}{2(1 - x)} - 1 & \frac{1}{2} \le x < 1 \end{cases}$$

$$g(y) = \begin{cases} \frac{1}{2(1 - y)} & y \le 0 \\ 1 - \frac{1}{2(1 + y)} & y \ge 0 \end{cases}$$

$$(0, 1) \sim \mathbb{R}$$

## Links

---
Source: Countable-Uncountable-sets, pp. 1–6

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20|Countable-Uncountable-sets]] pp. 1–6
<!-- /kurooto:seen -->
