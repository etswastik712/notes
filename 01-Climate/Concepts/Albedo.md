---
title: Albedo
subject: climate
type: concept
scope: [taught]
by: [argha, suhas-pre]
status: draft
tags: [subject/climate, type/concept, taught, src/argha, src/suhas-pre, status/draft]
---
# Albedo

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** definition, typical values, effect on $T_e$ (Argha L3) · 🔵 **extra:** the $\Delta T_e$ rule of thumb

> [!intuition] In one picture
> Albedo is the planet's *paint job*. A white roof stays cool in the sun, a black roof gets hot: the same sunlight, a different fraction kept. A 1 % change in how much sunlight is reflected moves the planet by about 1 K, so small changes in ice, cloud or vegetation matter.

> [!key] Definition
> The **albedo** $\alpha$ is the fraction of incident shortwave (solar) radiation that is reflected back to space (or from a surface) without being absorbed: $\alpha=\dfrac{\text{reflected}}{\text{incident}}\in[0,1]$.

- **Bond albedo** (all wavelengths, all angles): the one that enters the energy balance. Earth: $\alpha\approx0.30$ (NASA lists 0.294; see [[CL03 Radiation and Planetary Energy Balance]] for why the 3rd digit matters).
- **Surface** vs **planetary (top-of-atmosphere)** albedo: the planetary value includes clouds, aerosol and atmospheric scattering, and is the global mean of a strongly varying field: highest over polar regions and bright cloud decks, lowest over tropical oceans.
- Typical values: ocean 0.02–0.10 · forest 0.06–0.18 · grass 0.07–0.25 · soil 0.10–0.20 · desert sand 0.35–0.45 · thin/thick cloud 0.30 / 0.60–0.70 · old snow 0.40–0.60 · fresh snow 0.75–0.95.

**Effect on temperature.** In the zero-d balance $T_e\propto(1-\alpha)^{1/4}$, so
$$\Delta T_e\approx-\frac{T_e}{4}\,\frac{\Delta\alpha}{1-\alpha}\quad(\Delta\alpha=0.01\Rightarrow\Delta T_e\approx-0.9\ \mathrm K).$$

**Albedo is not constant.** It changes with temperature (snow and ice), clouds, vegetation and Sun angle: the origin of the [[Ice-Albedo Feedback]] and of multiple steady states ([[CL04 Feedback and Multiple Steady States]]).

Used in: [[CL03 Radiation and Planetary Energy Balance]] · [[Effective Emission Temperature]] · [[Zero-Dimensional Energy Balance Model]].
Connections: vegetation albedo as a population-driven feedback (Daisyworld) in [[Bistability and Tipping Points]]; glaciers and snow cover in [[Landscapes and Geomorphology - Course Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
