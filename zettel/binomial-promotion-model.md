---
id: zettel/binomial-promotion-model
aliases: ["Binomial Promotion Model", "Independent Bernoulli Promotions"]
tags: [zettel, agent-written, introduction-to-probability]
trust_tier: agent_written
---

# Binomial Promotion Model

A discrete probability model where each member of a population is selected independently with a constant success probability, resulting in a binomial distribution for the total number of selected members in a subpopulation.

$$P[W = k] = \binom{n}{k} p^k (1-p)^{n-k}$$

## Links
- contrasts-with:: [[zettel/hypergeometric-promotion-model]] — Replaces fixed-sample without-replacement sampling from the joint pool by independent Bernoulli trials per individual

---
Source: Practice problems 17th September and following tutorial and weekend, pp. 1–2

<!-- kurooto:seen -->
- used-in:: [[zettel/binomial-overbooking-survival-sum]] — The overbooking note computes a cumulative sum of Binomial(N, p) probabilities for independent attendance, which is the binomial promotion model applied to seat capacity
- equivalent-to:: [[zettel/sum-of-independent-bernoulli-trials-representation-of-binomial]] — The promotion model's count of independently selected members is the sum of n independent Bernoulli(p) indicators, which is the representation this note states for the binomial
## Seen in
- [[introduction-to-probability/2026-09-17-practice-problems-17th-september-and-following-tutorial-and-weekend|Practice problems 17th September and following tutorial and weekend]] pp. 1–2
<!-- /kurooto:seen -->
