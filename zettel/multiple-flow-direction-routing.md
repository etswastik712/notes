---
id: zettel/multiple-flow-direction-routing
aliases: ["Multiple Flow Direction Routing", "MFD"]
tags: [zettel, agent-written, landscape-evolution]
trust_tier: agent_written
---

# Multiple Flow Direction Routing

A flow routing method that distributes discharge among multiple downhill neighbouring cells rather than routing to a single cell. It handles divergent flow topographies where single-direction steepest-descent algorithms get stuck.

## Links
- contrasts-with:: [[zettel/d8-routing-algorithm]] — MFD fractions flow across multiple downhill neighbours to resolve divergent flow where D8 restricts flow to a single steepest neighbour

---
Source: l_fluvial, pp. 1–11

<!-- kurooto:seen -->
- used-in:: [[zettel/flow-accumulation-map]] — Flow routing (including MFD) produces the cell-to-cell flow that is aggregated into a flow accumulation map, so the routing method feeds the accumulation raster
## Seen in
- [[landscape-evolution/books/l-fluvial|l_fluvial]] pp. 1–11
<!-- /kurooto:seen -->
