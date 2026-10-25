---
title: Atmospheric Stability
subject: climate
type: concept
scope: [taught, extra-book]
by: [suhas-pre, book]
status: draft
tags: [subject/climate, type/concept, taught, extra/book, src/suhas-pre, src/book, status/draft]
---
# Atmospheric Stability

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!key] Static stability
> A layer is **statically stable** if a parcel displaced vertically returns, **unstable** if it keeps going. For unsaturated air: stable ⇔ $\Gamma<\Gamma_d$ ⇔ $\partial\theta/\partial z>0$ ⇔ $N^2>0$, with the **buoyancy (Brunt–Väisälä) frequency**
> $$N^2=\frac{g}{\theta}\frac{\partial\theta}{\partial z}=\frac{g}{T}\big(\Gamma_d-\Gamma\big).$$

| | $\Gamma$ | $N^2$ | behaviour |
|---|---|---|---|
| stable | $<\Gamma_d$ | $>0$ | oscillation at $N$, period $2\pi/N$ |
| neutral | $=\Gamma_d$ | 0 | stays put |
| unstable | $>\Gamma_d$ | $<0$ | exponential growth: convection |

- **Taught:** the criterion "unstable if the environmental lapse rate exceeds $\Gamma_d$" (Suhas pre-midsem notes). **Extra (book):** the $N^2$ formula and parcel oscillation (M&P Problem 1; W&H §3.6.1).
- **Numbers:** troposphere $N\approx0.011$ s⁻¹ (period ≈ 9–10 min); stratosphere $N\approx0.02$ s⁻¹ (≈ 5 min).
- **Saturated air:** replace $\Gamma_d$ by $\Gamma_s$. **Conditional instability:** $\Gamma_s<\Gamma<\Gamma_d$: stable if dry, unstable if saturated and lifted past the level of free convection (W&H §3.6.3).

> [!intuition] Ball in a bowl, on a table, on a hill
> Stable = bowl, neutral = table, unstable = hill. Mathematically the displacement obeys $\ddot z=-N^2z$: oscillation for $N^2>0$, exponential escape for $N^2<0$, the same as the linear stability of a fixed point ([[Fixed Points and Linear Stability]]).

Stable layers carry internal gravity waves ([[Waves - Course Map]]); neutral layers are the convecting ones ([[Convection]], [[Convective Adjustment]]). Derivations and the numerical example in [[CL09 Radiative-Convective Equilibrium]]; ingredients: [[Adiabatic Process and Potential Temperature]], [[Dry Adiabatic Lapse Rate]], [[Lapse Rate]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
