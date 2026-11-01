---
id: zettel/area-weighted-mean-temperature
aliases: ["Area-Weighted Mean Temperature", "area-weighted average temperature", "global mean temperature averaging"]
tags: [zettel, agent-written, introduction-to-climate-science]
trust_tier: agent_written
---

# Area-Weighted Mean Temperature

A spatially weighted average where temperature observations are gridded into spatial boxes and weighted proportionally by the surface area of each box. This prevents spatial bias caused by sparse station coverage and the convergence of meridians near the poles.

$$\overline{T} = \frac{\sum_i T_i A_i}{\sum_i A_i}$$

## Links
- generalises:: [[zettel/surface-temperature-field-survey]] — Area-weighted mean aggregates heterogeneous local surface observations across geographic grid cells to construct a single global metric

---
Source: climate_intro_notes, pp. 17–23

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-climate-science/2026-08-05-lectures-1-2-intro-and-global-mean-temperature|climate_intro_notes]] pp. 17–23
- [[introduction-to-climate-science/2026-08-21-lecture-6-planetary-energy-balance-with-ghgs|climate_intro_notes_L1_L6]] pp. 17–24
- [[introduction-to-climate-science/books/intro-clim|intro_clim]]

### Added from class
- intro_clim: Introduces the programmatic framework using Python libraries (NumPy, Matplotlib, SymPy) to numerically analyze and solve for global mean temperature.
<!-- /kurooto:seen -->

<!-- kurooto:notation -->
## Notation
| Source | Notation | What it stands for |
|---|---|---|
| climate_intro_notes, pp. 17–23 | $A_i$ | Area of box i |
| climate_intro_notes_L1_L6, pp. 17–24 | $A_i$ | Area of box i |
| climate_intro_notes_L1_L6, pp. 17–24 | $\overline{T}$ | Area-weighted mean temperature |
| climate_intro_notes, pp. 17–23 | $T_i$ | Temperature of box i |
| climate_intro_notes_L1_L6, pp. 17–24 | $T_i$ | Temperature of box i |
<!-- /kurooto:notation -->
