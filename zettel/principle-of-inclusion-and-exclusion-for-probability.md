---
id: zettel/principle-of-inclusion-and-exclusion-for-probability
aliases: ["Principle of Inclusion and Exclusion for Probability", "inclusion-exclusion principle", "general addition rule for probabilities"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Principle of Inclusion and Exclusion for Probability

A formula expressing the probability of the union of n events as an alternating sum of probabilities of all possible intersections of k events for k ranging from 1 to n.

$$P\left(\bigcup_{i=1}^n E_i\right) = \sum_{i=1}^n P(E_i) - \sum_{i<j} P(E_i \cap E_j) + \sum_{i<j<k} P(E_i \cap E_j \cap E_k) - \cdots + (-1)^{n-1} P\left(\bigcap_{i=1}^n E_i\right)$$

## Links
- generalises:: [[zettel/addition-rule-for-two-events]] — It generalizes the two-event union formula to any finite collection of n events

---
Source: Class notes 12th August 2026, pp. 1–5

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-08-19-class-notes-20th-august-2026|Class notes 12th August 2026]] pp. 1–5
<!-- /kurooto:seen -->
