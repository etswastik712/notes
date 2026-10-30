---
id: zettel/gambler-s-ruin-difference-recurrence
aliases: ["Gambler's Ruin Difference Recurrence", "gambler's ruin recurrence relation", "gambler's ruin problem"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Gambler's Ruin Difference Recurrence

A difference equation expressing the probability of bankruptcy from an initial capital of i units in terms of step-by-step transitions with success probability p and failure probability 1 - p.

$$p_i = p p_{i+1} + (1 - p) p_{i-1}$$

$$p_{i+1} - p_i = \frac{1-p}{p} (p_i - p_{i-1})$$

## Links

---
Source: Practice problems 21st August 2026, pp. 1–3

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-probability/2026-08-19-practice-problems-21st-august-2026|Practice problems 21st August 2026]] pp. 1–3
<!-- /kurooto:seen -->
