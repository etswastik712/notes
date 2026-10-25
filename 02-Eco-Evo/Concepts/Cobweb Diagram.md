---
title: Cobweb Diagram
aliases: ["cobweb plot", "Verhulst diagram"]
subject: eco-evo
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/eco-evo, type/concept, extra/beyond, src/own, status/draft]
---
# Cobweb Diagram

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond:** not on the slides (they show time series and a bifurcation diagram); added as the standard picture of a 1-D map

> [!intuition] In one picture
> Bounce between the curve and the diagonal. Inward spirals mean the fixed point is stable; outward spirals and closed boxes mean it is not.

> [!key] Definition
> To iterate $n_{t+1}=g(n_t)$ graphically: from $(n_t,0)$ go vertically to the curve $g$, horizontally to the line $n_{t+1}=n_t$, repeat. A fixed point $n^*$ is stable iff $|g'(n^*)|<1$; $g'<0$ gives a spiral, $g'>0$ a staircase.

## Drawing and reading it
To iterate $n_{t+1}=g(n_t)$: plot the curve $g$ and the line $y=x$; from $(n_0,0)$ go up to the curve, across to the line, up again. A fixed point $n^*$ is where the curve crosses the line. Near it the web behaves like $\delta_{t+1}\approx g'(n^*)\delta_t$: a staircase if $g'>0$, a spiral if $g'<0$, inward if $|g'|<1$.

> [!example] Ricker, $K=100$
> At $r=1.3$, $g'(K)=-0.3$: a small inward spiral. At $r=2.3$, $g'(K)=-1.3$: the web leaves the fixed point and lands on a closed rectangle: the 2-cycle 159.2 and 40.8, where the curve crosses its own second iterate $g(g(n))$. At $r=3.0$ the web never closes (chaos). The slope $g'$ is the same number that decides [[Fixed Points and Linear Stability]] for maps.

**Why period doubling shows up.** At $g'=-1$ the second iterate $g^{(2)}$ has slope $+1$ at $n^*$ and sprouts two new fixed points (May: "the curve $F^{(2)}$ must develop a loop"): the 2-cycle ([[Period Doubling and Route to Chaos]]).

> [!pitfall] Cobwebs are for one-dimensional maps
> They need a single variable and a single lag. With delayed density dependence the state is two-dimensional and the cobweb is no longer a complete picture ([[Time-Series Reconstruction]]).

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Ricker Model]] · [[Period Doubling and Route to Chaos]] · [[Fixed Points and Linear Stability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
