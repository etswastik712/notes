---
title: BBGKY Hierarchy
aliases: ["Bogoliubov-Born-Green-Kirkwood-Yvon hierarchy", "BBGKY"]
subject: thermo
type: concept
by: [book, own-notes]
status: draft
tags: [subject/thermo, type/concept, src/book, src/own-notes, status/draft]
---
# BBGKY Hierarchy

> [!info] Source
> Kardar §3.3 (pp. 62–65); Huang §3.5 (p. 65); [[SM04 Kinetic Theory and the Boltzmann Equation]] §3.

> [!intuition] In one picture
> Each reduced density feels the next one up (the force from an outside particle), so the equations never close by themselves: a ladder with no top.

> [!key] Key facts
> $\partial_tf_s-\{\mathcal H_s,f_s\}=\sum_{n=1}^s\int\mathrm d^3p_{s+1}\mathrm d^3q_{s+1}\,\partial_{\mathbf q_n}V(\mathbf q_n-\mathbf q_{s+1})\cdot\partial_{\mathbf p_n}f_{s+1}$. For $s=1$: streaming of $f_1$ $=\int\nabla V\cdot\partial_{\mathbf p_1}f_2$. Exact consequence of Liouville's equation.

> [!intuition] Why truncation works
> Time scales: $\tau_c=d/\bar v\ll\tau_\times=\lambda/\bar v\ll\tau_U=L/\bar v$, $\tau_c/\tau_\times\sim nd^3$ (air: $5.5\times10^{-3}$). In the $s=2$ equation the right side is smaller than the streaming terms by $nd^3$; in the $s=1$ equation it is the only thing that changes $f_1$ over $\tau_\times$. Keep the first equation, solve the second as an isolated two-body problem: Boltzmann equation.

Used in: [[SM04 Kinetic Theory and the Boltzmann Equation]]. Related: [[One-Particle Distribution Function]] · [[Boltzmann Equation]] · [[Molecular Chaos]] · [[Liouville's Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
