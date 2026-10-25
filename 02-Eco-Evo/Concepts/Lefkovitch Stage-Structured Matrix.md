---
title: Lefkovitch Stage-Structured Matrix
aliases: ["stage-structured model", "stage matrix", "transition matrix"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Lefkovitch Stage-Structured Matrix

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the loggerhead turtle matrix: $G$ = probability of moving to the next stage, $P$ = probability of staying in the same stage ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=24|slide 24]])

> [!intuition] In one picture
> Turtles do not change at fixed ages: a 'large juvenile' may spend years in that class. So let an individual stay (with probability $P$) or move on (with probability $G$) each year.

> [!key] Definition
> When individuals are grouped by **stage**, each stage $i$ has a stay probability $P_i$ (diagonal), a graduation probability $G_i$ (sub-diagonal) and fecundity $F_i$ (top row). Projection is still $\mathbf n_{t+1}=\mathbf A\mathbf n_t$ with the same $\lambda$ and stable-stage results as for the [[Leslie Matrix]].

## Building $P$ and $G$ from stage length
Classify by stage instead of age; each stage $i$ lasts $T_i$ years with annual survival $\sigma_i$. At the stable distribution the share at within-stage age $a$ is proportional to $x^{a-1}$, $x=\sigma_i/\lambda$, and only the oldest age class graduates, so the fraction leaving per year is
$$\gamma_i=\frac{x^{T_i-1}(1-x)}{1-x^{T_i}},\qquad G_i=\sigma_i\gamma_i,\quad P_i=\sigma_i(1-\gamma_i).$$
$\lambda$ appears in $x$, so the matrix and its eigenvalue are found by iterating to a fixed point.

> [!example] Loggerhead, from Table 1 to Table 2
> Small juveniles: $\sigma=0.75$, $T=7$, $\lambda=0.9516$ give $x=0.788$, $\gamma=0.0626$, $G_2=0.047$, $P_2=0.703$ ✓ (Crowder et al.). Large juveniles ($\sigma=0.6758$, $T=8$): $G_3=0.019$, $P_3=0.657$. Fecundity with a post-breeding census: $F_5=76.5\times0.8091=61.896$, $F_4=76.5\times G_4=4.665$. The rebuilt matrix equals Table 2 to within 0.003.

> [!pitfall] $G$ is not "probability of growing" alone
> The slide glosses $G$ as "probability of going to the next stage" and $P$ as "of remaining"; Crowder et al. define them with survival included, so $P_i+G_i=\sigma_i$ and mortality $1-\sigma_i$ is the part missing from the column sum. The long stage keeps a *small* $G$ (only the oldest eighth of an 8-year stage leaves each year).

Age or stage? Use age when age fixes fate and is known; stage when size or development fixes fate and ages are uncertain. The analysis ([[Dominant Eigenvalue and Perron-Frobenius Theorem]], [[Sensitivity and Elasticity of Growth Rate]]) is identical.

Used in: [[EE02 Structured Population Models]]. Related: [[Leslie Matrix]] · [[Loggerhead Turtle and Turtle Excluder Devices]] · [[Sensitivity and Elasticity of Growth Rate]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
