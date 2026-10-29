---
id: zettel/first-colour-arrival-probability-under-sampling-without-replacement
aliases: ["First Colour Arrival Probability under Sampling without Replacement", "First Arrival Order without Replacement", "Combinatorial First Arrival Sequence Counting"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# First Colour Arrival Probability under Sampling without Replacement

The combinatorial formulation for the probability that a designated colour is observed before another in sampling without replacement from an urn with fixed ball counts, computed by enumerating favourable permutations of indistinguishable coloured balls.

$$\sum_{k=0}^{rN} \frac{[(rN - k) + (gN - 1) + yN]!}{(rN - k)!(gN - 1)!(yN)!} = \binom{gN + yN - 1}{yN} \sum_{k=0}^{rN} \binom{N - k - 1}{rN - k}$$

$$\frac{(rN)!(gN)!(yN)!}{N!} \times \frac{(gN + yN - 1)!}{(gN - 1)!(yN)!} \times \frac{N!}{(gN + yN)!(rN)!} = \frac{g}{g+y}$$

## Links
- equivalent-to:: [[zettel/first-colour-arrival-probability-under-sampling-with-replacement]] — Yields the identical final probability g/(g+y) despite evaluating finite permutations without replacement

---
Source: Quiz 2 solutions, pp. 1–2

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-09-04-quiz-2-solutions|Quiz 2 solutions]] pp. 1–2
<!-- /kurooto:seen -->
