---
id: zettel/inpaintnans
aliases: ["inpaintnans", "inpaintnans function"]
tags: [zettel, agent-written, landscape-evolution]
trust_tier: agent_written
---

# inpaintnans

A preprocessing function that replaces missing or void values (NaNs) in a DEM raster by interpolating from adjacent grid values.

## Links
- used-in:: [[zettel/digital-elevation-model]] — Interpolates void values and missing data across DEM grid cells
- needs:: [[zettel/gridobj]] — Operates on raster grid objects produced via GRIDobj to eliminate NaN cells

---
Source: Topotoolbox_tut_shubhra, pp. 1–15

<!-- kurooto:seen -->
## Seen in
- [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials|Topotoolbox_tut_shubhra]] pp. 1–15
<!-- /kurooto:seen -->
