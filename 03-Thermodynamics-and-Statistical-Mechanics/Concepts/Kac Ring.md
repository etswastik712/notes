---
title: Kac Ring
aliases: ["Kac ring model", "Kac model of irreversibility"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# Kac Ring

> [!info] Source
> Kac (1956), recalled; simulated in `scripts/sm04_sims.py`; [[SM04 Kinetic Theory and the Boltzmann Equation]] §7.1.

> [!intuition] In one picture
> A ring of balls and markers that is exactly reversible and exactly periodic, yet shows a Boltzmann-like exponential approach to disorder when the markers are random.

> [!key] Key facts
> $N$ sites, $k$ marked edges, $\mu=k/N$; each step the balls move one site and change colour on crossing a marked edge. $m_t$ (white minus black fraction): $\langle m_t\rangle=(1-2\mu)^t$ for $t\le N$ (average over independent markers; Stosszahlansatz), single-ring noise $\sim\sqrt{2.1/N}$; exact period $N$ ($k$ even) or $2N$ ($k$ odd). $H=\tfrac{1+m}2\ln\tfrac{1+m}2+\tfrac{1-m}2\ln\tfrac{1-m}2$.

> [!example] Numbers (recomputed)
> $N=10^4$, $k=10^3$: $m_5=0.328$ ($0.8^5=0.328$), $m_{10}=0.092$ ($0.107$). $N=400$, $k=80$: rms $0.088$ for $15\le t\le300$, then $m_{400}=m_{800}=1$. $N=101$, $k=21$: $m_{101}=-1$, $m_{202}=+1$.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[Loschmidt and Zermelo Paradoxes]] · [[Molecular Chaos]] · [[H-Theorem]] · [[Random Walk]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
