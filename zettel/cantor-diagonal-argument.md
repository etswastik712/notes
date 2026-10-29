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
- needs:: [[zettel/normalized-decimal-expansion]] — The diagonal construction works on the digits a_kk of a real number, so it depends on the normalized expansion giving each real number a unique digit representation
- contrasts-with:: [[zettel/diagonal-traversal-enumeration]] — Diagonal traversal builds a surjection from N onto pairs or rationals by walking anti-diagonals, while the Cantor diagonal argument builds an element missed by every enumeration, so the two share a name but prove opposite kinds of results
## Seen in
- [[intro-to-proofs/2026-10-20-countable-and-uncountable-sets-lectures-17-to-20|Countable-Uncountable-sets]] pp. 1–6
<!-- /kurooto:seen -->
