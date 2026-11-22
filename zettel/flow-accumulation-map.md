---
id: zettel/flow-accumulation-map
aliases: ["Flow Accumulation Map", "accumulation map"]
tags: [zettel, agent-written, landscape-evolution]
trust_tier: agent_written
---

# Flow Accumulation Map

A spatial raster mapping upslope contributing drainage area across a digital elevation model by aggregating routed cells. Applying a threshold to this accumulated source area identifies the location and geometry of the stream network.

## Links

---
Source: l_fluvial, pp. 1–11

<!-- kurooto:seen -->
- contrasts-with:: [[zettel/d8-routing-algorithm]] — The accumulation map is built by routing flow, and D8 is the single-direction steepest-descent routing that the map summary implies, while its note says D8 struggles in divergent areas
- contrasts-with:: [[zettel/multiple-flow-direction-routing]] — MFD distributes discharge across several downhill neighbours, an alternative routing scheme for the same accumulated-area calculation that the flow accumulation map relies on
- used-in:: [[zettel/stream-network]] — Applying a threshold to the accumulated source area is what identifies the stream network's location and geometry, so the map is the step that produces it
## Seen in
- [[landscape-evolution/books/l-fluvial|l_fluvial]] pp. 1–11
<!-- /kurooto:seen -->
