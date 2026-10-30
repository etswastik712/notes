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
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026|Practice problems 21st August 2026]] pp. 1–3
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026|Practice problems 21st August 2026]] pp. 1–2
- [[introduction-to-probability/2026-09-22-mid-semester-solutions|Mid-semester solutions]] pp. 1–3

### Added from class
- Practice problems 21st August 2026 pp. 1–3: Poses the standard formulation with p being the probability of knowing and m being the number of multiple-choice alternatives.
- Practice problems 21st August 2026 pp. 1–2: Introduces the specific parameterization where p is the probability of knowing and 1/m is the random guess success probability across m alternatives.
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| Mid-semester solutions, pp. 1–3 | $R$ | event that the examinee gets the answer right |
| Mid-semester solutions, pp. 1–3 | $K$ | event that the examinee knows the answer |
| Practice problems 21st August 2026, pp. 1–2 | $m$ | number of multiple-choice alternatives |
| Practice problems 21st August 2026, pp. 1–3 | $m$ | number of multiple-choice alternatives |
| Practice problems 21st August 2026, pp. 1–3 | $m$ | number of multiple-choice alternatives |
| Mid-semester solutions, pp. 1–3 | $n$ | number of multiple-choice options |
| Practice problems 21st August 2026, pp. 1–2 | $p$ | probability that the student knows the answer |
| Practice problems 21st August 2026, pp. 1–3 | $p$ | probability that the student knows the answer |
| Practice problems 21st August 2026, pp. 1–3 | $p$ | probability the student knows the answer |
<!-- /kurooto:notation -->
