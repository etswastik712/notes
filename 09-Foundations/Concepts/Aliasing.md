---
title: Aliasing
aliases: ["aliasing", "folding", "wagon-wheel effect"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Aliasing

> [!intuition] In one picture
> Frequencies above the Nyquist frequency are folded onto lower ones and cannot be told apart from them.

> [!key] Key facts
> Apparent frequency $=\lvert\nu-f_s\,\mathrm{round}(\nu/f_s)\rvert$. 9 Hz sampled at 10 Hz appears at 1 Hz; a 40 m wavelength on a 30 m DEM appears as 120 m.

## In this vault
Slopes and curvature from a coarse DEM; seasonal cycle aliasing in monthly-sampled records.

> [!pitfall] Watch out
> Cannot be undone after sampling.

Used in: [[Fourier and Laplace Transforms]]. Related: [[Sampling Theorem]] · [[Discrete Fourier Transform]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
