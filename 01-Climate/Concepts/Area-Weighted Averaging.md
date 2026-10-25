---
title: Area-Weighted Averaging
subject: climate
type: concept
scope: [taught, extra-beyond]
by: [argha]
status: draft
tags: [subject/climate, type/concept, taught, extra/beyond, src/argha, status/draft]
---
# Area-Weighted Averaging

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $\bar T=\sum T_iA_i/\sum A_i$ after gridding (Argha L2 sl. 25–26) · 🔵 **extra:** derivation of the $\cos\varphi$ weight, sampling error of correlated fields

> [!intuition] In one picture
> On a Mercator map Greenland looks as big as Africa. If every pixel voted equally, Greenland would get far too many votes. Equal-angle grid cells have the same problem near the poles: each cell must vote in proportion to the *land (or sea) it actually covers*.

> [!key] Definition
> Average a field over the sphere by weighting each grid cell by its **area**: $\bar T=\dfrac{\sum_iT_iA_i}{\sum_iA_i}$. For a regular latitude–longitude grid the area is proportional to $\cos\varphi_i$, so the weights are $\cos\varphi_i$.

**Derivation.** $\mathrm dA=a^2\cos\varphi\,\mathrm d\varphi\,\mathrm d\lambda$ ⇒ $\bar T=\int T\cos\varphi\,\mathrm d\varphi\,\mathrm d\lambda\big/\int\cos\varphi\,\mathrm d\varphi\,\mathrm d\lambda$.

**Numbers.** Toy field $T=255+45\cos^2\varphi$ K: the exact area-weighted mean is $255+45\cdot\tfrac23=285$ K; the plain average over latitude bands is $255+45\cdot\tfrac12=277.5$ K, a **7.5 K cold bias**. A coarse three-band estimate (0–30°, 30–60°, 60–90°, areas 0.500, 0.366, 0.134) gives 284.6 K.

**Sampling theory.** For $N$ samples of pairwise correlation $\rho$, $N_{\rm eff}=N/[1+(N-1)\rho]\to1/\rho$: stations must be *spread out*, not just numerous. Time series with lag-1 correlation $r$: $N_{\rm eff}=N(1-r)/(1+r)$.

Chapter: [[CL02 Observing Global Temperature]]. The same weights give the factor $\tfrac14$ in [[CL03 Radiation and Planetary Energy Balance]] (sphere average of $S\cos\theta$) and the flux integral of [[Poleward Energy Transport]]. Related: [[Global Mean Surface Temperature]], [[Probability - Course Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
