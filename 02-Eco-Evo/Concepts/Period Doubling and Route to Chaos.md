---
title: Period Doubling and Route to Chaos
aliases: ["bifurcation diagram", "period-doubling cascade", "Feigenbaum"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, may]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Period Doubling and Route to Chaos

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the bifurcation diagram: 'the periodicity for a given $r$ equals the number of points plotted at that $r$' ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=25|slide 25]])  ·  🟡 **extra · book:** May (1976), *Nature* 261: 459-467, 'Simple mathematical models with very complicated dynamics'  ·  🔵 **extra · beyond:** Feigenbaum's universal ratio

> [!intuition] In one picture
> Turn up the growth rate and the steady state wobbles into a 2-year cycle, then a 4-year cycle, then 8, each split coming sooner than the last until the pattern never repeats.

> [!key] Definition
> A fixed point of a map $g$ loses stability when $g'(n^*)=-1$ and a 2-cycle is born; that cycle later splits into a 4-cycle, and so on, at values $r_1<r_2<\dots$ that accumulate at $r_\infty$. Beyond $r_\infty$ the dynamics can be chaotic with windows of periodic behaviour. The **bifurcation diagram** plots the long-run values of $n_t$ against $r$.

## Thresholds and the universal ratio
At each doubling a cycle's multiplier passes through $-1$. Ricker ($K=100$): $r_1=2$, $r_2=2.5265$, $r_3=2.6564$, $r_4=2.6846$, accumulation $r_\infty=2.6924$. The logistic map $x\to ax(1-x)$ has $a=3,\ 3.4495,\ 3.5441,\ 3.5644\to3.5700$; for the discrete logistic $N_{t+1}=N_t[1+r(1-N_t/K)]$ ($a=1+r$) that is $r=2,\ 2.4495,\ 2.5441,\ 2.5644\to2.5699$.

> [!example] Predicting the end of the cascade
> The gaps shrink by $\delta_n=\frac{r_n-r_{n-1}}{r_{n+1}-r_n}\to4.669$ (Feigenbaum): for the Ricker $0.5265/0.1299=4.05$, then $0.1299/0.0282=4.6$. So the remaining distance after $r_4$ is $(r_4-r_3)/(\delta-1)=0.0282/3.669=0.0077$ and $r_\infty\approx2.6846+0.0077=2.6923$ ✓ (exact 2.6924). The same $\delta$ for the logistic map and the Ricker map is why simple models can say something general.

**Beyond $r_\infty$.** Chaos with *periodic windows* (the white bands of the diagram), e.g. the period-3 window of the logistic map at $a\approx3.83$; odd periods first appear at $a=3.6786$ (May). The diagram is the long-run set $\{n_t\}$ against $r$; the number of points at a given $r$ is the period (slide 25).

> [!pitfall] Order inside chaos
> "Past $r_\infty$ is chaotic" is true only on a large set: windows of stable cycles occur ($\Lambda=-0.07$ at $r=3.6$). And the cascade is *deterministic*: noise smears the fine structure of the diagram, so observed series show it only coarsely ([[Deterministic Chaos]]).

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Ricker Model]] · [[Deterministic Chaos]] · [[Fractals]] · [[Bistability and Tipping Points]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
