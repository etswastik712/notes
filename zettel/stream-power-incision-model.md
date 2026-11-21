---
id: zettel/stream-power-incision-model
aliases: ["Stream Power Incision Model", "bedrock river advection equation", "stream power incision law"]
tags: [zettel, agent-written, landscape-evolution]
trust_tier: agent_written
---

# Stream Power Incision Model

A continuum geomorphic model representing bedrock river profile evolution governed by an advection equation balancing rock uplift and streampower-dependent incision. The incision rate scales with upstream catchment area and local channel slope.

$$\text{erosion rate} \sim k A(x)^m | \partial_x z |^n$$

## Links
- used-in:: [[zettel/bedrock-river]] — It governs the vertical incision and long-profile transient evolution of bedrock channels
- needs:: [[zettel/hack-s-rule]] — Catchment area scaling with channel length directly relates area A(x) to profile distance x
- used-in:: [[zettel/knickpoint-migration]] — The advective form of the equation dictates the upstream migration speed and shape preservation of knickpoints and waterfalls

---
Source: l_fluvial, pp. 34–43

<!-- kurooto:seen -->
## Seen in
- [[landscape-evolution/books/l-fluvial|l_fluvial]] pp. 34–43
<!-- /kurooto:seen -->
