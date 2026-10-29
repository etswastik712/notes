---
id: zettel/wave-function-physical-acceptability-conditions
aliases: ["Wave Function Physical Acceptability Conditions", "physically acceptable wave functions", "quantum well-behavedness criteria", "admissibility of wave functions", "quantum admissibility criteria"]
tags: [zettel, agent-written, ph2113]
trust_tier: agent_written
---

# Wave Function Physical Acceptability Conditions

The standard mathematical criteria a candidate wave function must fulfill to represent a physically viable quantum state in a finite, non-singular potential: square-integrability (normalizability as |x| -> infinity), continuity of the wave function across all coordinates, and single-valuedness.

$$\psi_A(x) = N e^{-x^2/a^2}$$

$$\psi_B(x) = N e^{+x^2/a^2}$$

## Links
- needs:: [[zettel/square-integrability-of-wave-functions]] — Candidate wave functions such as exp(+x^2/a^2) are ruled out because divergence at spatial infinity violates square-integrability
- needs:: [[zettel/wave-function-boundary-matching-across-discontinuities]] — Requires continuity of the wavefunction across points like x = 0 in finite, non-singular potentials, disqualifying piecewise step discontinuities

---
Source: PH2113_Mock_Quiz_50min_15marks, pp. 1–2

<!-- kurooto:seen -->
## Seen in
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_50min_15marks]] pp. 1–2
- [[ph2113/2026-09-02-mock-quiz-and-solutions|PH2113_Mock_Quiz_Ideal_Solutions]] pp. 1–2

### Added from class
- PH2113_Mock_Quiz_Ideal_Solutions pp. 1–2: Supplies concrete test examples illustrating each admissibility failure mode: unconstrained exponential growth destroying normalizability and finite boundary step jumps violating spatial continuity.
<!-- /kurooto:seen -->
