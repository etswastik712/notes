---
id: zettel/d8-routing-algorithm
aliases: ["D8 Routing Algorithm", "D8 Routing", "D8 algorithm"]
tags: [zettel, agent-written, landscape-evolution]
trust_tier: agent_written
---

# D8 Routing Algorithm

A steepest-descent flow routing algorithm on digital elevation models that directs surface flow from each cell to a single neighbour among its eight adjacent cells based on gradient. It is used to generate flow accumulation maps but struggles in divergent flow areas.

## Links
- contrasts-with:: [[zettel/multiple-flow-direction-routing]] — D8 routes flow entirely to a single steepest downhill neighbour whereas MFD distributes flow among multiple downhill neighbours
- used-in:: [[zettel/flow-accumulation-map]] — D8 routing determines the direction of cell-to-cell transfer to compute the cumulative upslope area in flow accumulation maps

---
Source: l_fluvial, pp. 1–11

<!-- kurooto:seen -->
## Seen in
- [[landscape-evolution/books/l-fluvial|l_fluvial]] pp. 1–11
<!-- /kurooto:seen -->
