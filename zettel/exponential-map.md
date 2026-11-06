---
id: zettel/exponential-map
aliases: ["Exponential Map", "exp", "Lie group exponential map"]
tags: [zettel, agent-written, mt3184-differential-geometry-and-lie-groups]
trust_tier: agent_written
---

# Exponential Map

A map from the Lie algebra to the Lie group that sends each element to the value at time one of the one-parameter subgroup it generates. It naturally intertwines with Lie group homomorphisms via the commutative diagram exp(Phi_*(X)) = Phi(exp(X)).

$$\exp(X) = \gamma(1)$$

$$\Phi(\exp(X)) = \exp(\Phi_*(X))$$

$$\theta_t(g) = g \exp(tX) = R_{\exp(tX)}(g)$$

## Links

---
Source: DG28, pp. 1–5

<!-- kurooto:seen -->
- [[zettel/weakly-embedded-submanifold]] — needed to show that exp(tX) ∈ H for all t implies X lies in the Lie algebra of the Lie subgroup H
- [[mt3184-differential-geometry-and-lie-groups/2026-11-06-hw10]] — Problem 1 uses naturality Φ∘exp = exp∘Φ_*
## Seen in
- [[mt3184-differential-geometry-and-lie-groups/2026-11-06-october-26-30|DG28]] pp. 1–5
<!-- /kurooto:seen -->
