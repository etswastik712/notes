---
id: zettel/cantor-diagonal-argument
aliases: ["Cantor Diagonal Argument", "diagonalization", "Cantor's diagonal method"]
tags: [zettel, agent-written, intro-to-proofs]
trust_tier: agent_written
---

# Cantor Diagonal Argument

A method of constructing an element outside the image of any proposed enumeration f: N -> (0, 1) by deliberately inverting or altering each n-th digit along the diagonal to ensure non-surjectivity.

$$b_k = \begin{cases} 3 & \text{if } a_{kk} \neq 3 \\ 7 & \text{if } a_{kk} = 3 \end{cases}$$

## Links
- used-in:: [[zettel/uncountability-of-the-unit-interval]] — Directly proves that no function f : N -> (0, 1) can be surjective by generating b not in Im(f)

---
Source: Countable-Uncountable-sets, pp. 1–6

<!-- kurooto:seen -->
## Seen in
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20|Countable-Uncountable-sets]] pp. 1–6
<!-- /kurooto:seen -->
