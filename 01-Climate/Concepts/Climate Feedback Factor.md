---
title: Climate Feedback Factor
subject: climate
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/climate, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Climate Feedback Factor

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $f_i$ and $\Lambda=\Lambda_P/(1-\sum f_i)$ (Argha L4) · 🔵 **extra:** geometric-series reading, IPCC conversion

> [!intuition] In one picture
> A microphone next to its loudspeaker: part of the output is fed back to the input. If the fed-back fraction $f$ is below 1 the sound is just louder by $1/(1-f)$; at $f\ge1$ it howls.

> [!key] Definition
> If an auxiliary variable $y_i$ (water vapour, albedo, cloud, …) depends on global temperature, its **feedback factor** is $f_i=\dfrac{\partial T}{\partial y_i}\dfrac{\mathrm dy_i}{\mathrm dT}$ (dimensionless). Factors add, and the total sensitivity is
> $$\Lambda=\frac{\Lambda_P}{1-\sum_if_i}.$$

$f_i>0$ amplifies, $f_i<0$ damps, $f\ge1$ is runaway in the linear model. Interpretation as an **iteration**: warming $\Delta T_0=\Lambda_PF$ changes $y_i$, which adds $f\Delta T_0$, which changes $y_i$ again … so $\Delta T=\Lambda_PF(1+f+f^2+\cdots)=\Lambda_PF/(1-f)$ for $|f|<1$.

> [!extra-beyond]- Extra (beyond): the same bookkeeping in IPCC language
> IPCC uses feedback *parameters* $\lambda_i$ in W m⁻² K⁻¹ (negative = stabilising) so that $\Lambda=1/(-\lambda_{\rm net})$. The two are related by $f_i=\lambda_i/|\lambda_P|$. Approximate AR6-type values (`[verify]`): Planck −3.2, water vapour +1.8, lapse rate −0.5, surface albedo +0.35, clouds +0.4, so $\lambda_{\rm net}\approx-1.15$, gain $\approx3.2/1.15\approx2.8$ and $f_{\rm WV}\approx0.56$ (compare Wallace & Hobbs: 0.5). For $F_{2\times\mathrm{CO}_2}=3.7$ W m⁻² this gives ≈ 3.2 K.

Used in [[CL04 Feedback and Multiple Steady States]], [[CL08 Greenhouse Models]]. See [[Ice-Albedo Feedback]], [[Planck Sensitivity]], [[Linearisation and Sensitivity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
