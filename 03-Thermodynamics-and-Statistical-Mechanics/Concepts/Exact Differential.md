---
title: Exact Differential
aliases: ["inexact differential", "integrating factor"]
subject: thermo
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/thermo, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Exact Differential

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[0d0ec730e8e02ed0399d39ff05054a72_MIT8_333F13_Lec1.pdf#page=4|MIT L1 eq. I.12]] (the bar notation). · 🟡 **extra · book:** exactness test and cyclic relation (Zemansky Ch. 2).

> [!intuition] In one picture
> An exact differential is the small change of a real function; an inexact one depends on the road.

> [!key] Definition
> $\mathrm dz=M\,\mathrm dx+N\,\mathrm dy$ is **exact** iff $\partial M/\partial y=\partial N/\partial x$; then $z(x,y)$ exists. Otherwise it is inexact (written $\bar\mathrm dz$). Reciprocity $(\partial x/\partial y)_z=1/(\partial y/\partial x)_z$ and cyclic $(\partial x/\partial y)_z(\partial y/\partial z)_x(\partial z/\partial x)_y=-1$.

## Examples
$y\,\mathrm dx+x\,\mathrm dy$ is exact ($=\mathrm d(xy)$); $y\,\mathrm dx$ is not. $\bar\mathrm dQ_{\rm rev}$ is inexact but $\bar\mathrm dQ_{\rm rev}/T$ is exact: **$1/T$ is the integrating factor** that defines $S$. Cyclic rule gives $(\partial P/\partial T)_V=\beta/\kappa_T$.

> [!pitfall] Hold-fixed subscripts
> $(\partial P/\partial T)_V\ne(\partial P/\partial T)_S$: always write what is held constant.

Used in: [[TH01 Temperature and the Zeroth Law]], [[TH02 Work Heat and the First Law]]. Related: [[State Function]] · [[Response Functions]] · [[Entropy]] · [[Internal Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
