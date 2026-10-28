---
title: Transcendental Equation
aliases: ["quantisation condition", "matching equation"]
subject: qm
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/qm, type/concept, taught, src/slides, status/draft]
---
# Transcendental Equation

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $\kappa/k_0=\tan k_0a$ and $\kappa/k_0=-\cot k_0a$ ([[Finite_well.pdf#page=4|pp.3–4]]).

> [!intuition] In one picture
> An equation that mixes a trigonometric function with an algebraic one: it has no closed-form solution, but a graph shows every root at a glance.

> [!key] Definition and key results
> For the finite well: $\sqrt{z_0^2/z^2-1}=\tan z$ (even) and $=-\cot z$ (odd), $z=k_0a$. The left side falls from $\infty$ to 0, each branch of the right side rises from 0 to $\infty$, so each branch crossed contributes **exactly one** root.

Roots are found graphically (Figure QM7.2/QM7.4) or numerically (`scripts/qm07_numbers.py`). Example: $z_0=5$ gives $k_0a=1.3064,\ 2.5957,\ 3.8375,\ 4.9063$.

Used in: [[QM07 The Finite Square Well]] §3, §9, §10. Related: [[Finite Square Well]] · [[Logarithmic Derivative Matching]] · [[Bound State]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
