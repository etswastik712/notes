---
title: Water Wave Dispersion
aliases: [gravity wave dispersion, deep-water and shallow-water waves, swell dispersion]
subject: waves
type: concept
status: draft
tags: [subject/waves, type/concept, src/own-notes, status/draft]
---
# Water Wave Dispersion

> [!intuition] In one picture
> Long surface waves outrun short ones in deep water, but in shallow water the depth alone sets the speed.

> [!key] Definition and key results
> $\omega^2=gk\tanh kh$. Deep ($kh\gg1$): $C=\sqrt{g/k}=gT/2\pi$ (20 s: 31 m/s, $\lambda=625$ m). Shallow ($kh\ll1$): $C=\sqrt{gh}$ (4 km ocean: 198 m/s; tsunami). Group velocity $C_g=nC$, $n=\tfrac12(1+2kh/\sinh2kh)$: $\tfrac12$ deep, $1$ shallow. Swell from a storm distance $D$ arrives with period $T(t)=4\pi D/gt$.

> [!pitfall] Pitfall
> Energy and wave groups move at $C_g$, not at $C$: a 20 s swell crosses 8000 km in 6 days, not 3.

Used in: [[LS26 Sea Level and Ocean Waves]]. Related: [[Wave Energy and Power]] · [[Wave Shoaling and Refraction]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Dispersion Relation]] and [[Phase and Group Velocity]] (Foundations): the general theory; here the dispersion relation is $\omega^2=gk\tanh kh$
- [[Fourier Transform and Wave Packets]] (Quantum Mechanics): a wave packet's group velocity $d\omega/dk$ and its dispersive spreading are the same mathematics
