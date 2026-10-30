---
id: zettel/temperature-dependent-ice-albedo-feedback
aliases: ["Temperature-Dependent Ice-Albedo Feedback", "T-dependent albedo", "Piecewise albedo model"]
tags: [zettel, agent-written, introduction-to-climate-science]
trust_tier: agent_written
---

# Temperature-Dependent Ice-Albedo Feedback

A zero-dimensional energy balance model incorporating a piecewise temperature-dependent surface albedo that represents high reflectance in cold, glaciated conditions (snowball Earth) and lower reflectance at higher temperatures, creating multiple radiative equilibria between net shortwave gain and longwave loss.

$$a(T) = \begin{cases} 0.7, & T < 253 \text{ K} \\ 0.7 - \frac{T - 253}{40} \cdot 0.5, & 253 \le T \le 293 \text{ K} \\ 0.2, & T > 293 \text{ K} \end{cases}$$

$$LW^{\text{out}} = e \sigma T^4$$

$$SW^{\text{net}} = \frac{S(1-a)}{4}$$

## Links
- generalises:: [[zettel/stefan-boltzmann-law]] — Generalises constant-albedo radiative equilibrium by treating albedo as an explicit state-dependent function of temperature

---
Source: intro_clim

<!-- kurooto:seen -->
## Seen in
- [[introduction-to-climate-science/books/intro-clim|intro_clim]]
<!-- /kurooto:seen -->
