---
title: Low-Pass Filter
aliases: ["moving average", "ocean as a low-pass filter", "red noise from white noise"]
subject: climate
type: concept
scope: [taught, extra-beyond]
by: [joy]
status: draft
tags: [subject/climate, type/concept, taught, extra/beyond, src/joy, status/draft]
---
# Low-Pass Filter

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** Joy O7 notes §3
> 🔵 **extra · beyond:** the 1/√w arithmetic, CL29 §3

> [!intuition] In one picture
> A slow system averages fast forcing: it keeps the slow wiggles and throws away the fast ones.

> [!key] Definition
> An ocean responding to atmospheric noise does roughly $O(t)\approx\frac1\tau\int_{t-\tau}^ta\,dt'$: fast variations removed, slow ones kept, no energy added. A moving average of white noise over $w$ samples has standard deviation $\propto1/\sqrt w$ (0.109 for $w=100$, 0.051 for 400).

Used in: [[CL29 The Ocean's Ledger VI - Slow Swings and the Ocean's Memory for Carbon]], [[CL23 The Ocean's Ledger II - Heat Capacity and Climate Inertia]]. Related: [[Climate Anomaly]] · [[Climate Response Time]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
