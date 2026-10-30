---
id: zettel/multiplication-rule-for-conditional-probability
aliases: ["Multiplication Rule for Conditional Probability", "general chain rule for conditional probabilities", "multiplication rule for n events", "Multiplication Rule", "chain rule of probability"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Multiplication Rule for Conditional Probability

The probability of an intersection of n events, each with positive probability, equals the product of successive conditional probabilities, each factor conditioning on all earlier events in the sequence.

$$P\left[\bigcap_{i=1}^n E_i\right] = P[E_n \mid E_1 \cap \cdots \cap E_{n-1}] \cdots P[E_2 \mid E_1]\, P[E_1]$$

## Links
- generalises:: [[zettel/chain-rule-for-finite-intersection-probabilities]] — The product of unconditional probabilities in that note is this formula with every conditional factor reduced to P[E_i] under independence

---
Source: Class notes 19th August 2026, pp. 1–2

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-08-19-class-notes-19th-august-2026|Class notes 19th August 2026]] pp. 1–2
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026|Class notes 13th August 2026]] pp. 1–3

### Added from class
- Class notes 13th August 2026 pp. 1–3: Provides the explicit chain product formula expressing joint intersection probability as successive conditional factors.
<!-- /kurooto:seen -->
