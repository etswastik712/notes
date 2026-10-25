---
title: Functional and Numerical Responses
aliases: ["Holling functional response", "type II functional response", "numerical response"]
subject: eco-evo
type: concept
scope: [extra-book]
by: [molles, holling]
status: draft
tags: [subject/eco-evo, type/concept, extra/book, src/book, src/paper, status/draft]
---
# Functional and Numerical Responses

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Molles Ch. 14 (tier to be confirmed from the mandatory 'relevant sections'; not on the lecture slides)

> [!intuition] In one picture
> Two answers to 'what happens when prey get denser?': each predator eats more (functional response), and there are more predators (numerical response).

> [!key] Definition
> **Functional response:** prey eaten per predator per unit time as a function of prey density $N$. Type I: linear to a ceiling; Type II: saturating, $f(N)=aN/(1+ahN)$ with attack rate $a$ and handling time $h$; Type III: sigmoid. **Numerical response:** predator density or birth rate as a function of prey density.

> [!verify] Check
> Not covered on the slides. Check which parts of Molles Ch. 14 are the 'relevant sections' (mandatory = syllabus) and re-tier this note accordingly.

## Deriving Holling's curve
A predator spends time $T_s$ searching and $h$ per prey handling. In total time $T$: $T=T_s+hn$, and encounters $n=aNT_s$ ($a$ = searching efficiency, $N$ prey density). Eliminating $T_s$:
$$\frac nT=\frac{aN}{1+ahN},$$
rising almost linearly at low $N$ and levelling at $1/h$ when handling time limits consumption (**type II**). **Type I** is linear up to a ceiling; **type III** is sigmoid (low efficiency at low prey density: switching, learning, refuges). A **numerical response** is the change in predator density through reproduction or immigration as prey change.

> [!example] Numbers
> $a=0.02$ per predator per day per prey, $h=0.5$ day: maximum $1/h=2$ prey per predator per day; at $N=100$ the rate is $0.02\times100/(1+0.02\times100\times0.5)=1.0$ (half the maximum at $N=1/ah=100$); at $N=10$: 0.18 (nearly proportional: the Lotka-Volterra $pN$ with $p=0.02$ gives 0.2). Molles notes that lynx and coyote numbers rose six- to sevenfold after hare increases, while individual lynx also ate more hares (both responses).
> **Stability.** A saturating type II response weakens predation at high prey density, so enrichment can destabilise the interaction (Rosenzweig's paradox of enrichment, 🔵), whereas a type III response gives a refuge at low density that tends to stabilise.

**Ratio-dependence** (Arditi and Ginzburg): feeding depends on prey per predator, $g(N/P)$, because predators interfere with each other. Molles illustrates with the oyster drill *Urosalpinx* and wolves on Isle Royale.

> [!pitfall] Tier check
> Not on the lecture slides; the deck's "relevant sections" of Molles Ch. 14 may or may not include §14.4. The notes' stance: further reading unless the instructor says otherwise. Link: [[Lotka-Volterra Predator-Prey Model]], [[Predator Satiation]].

Used in: [[EE05 Predation]]. Related: [[Lotka-Volterra Predator-Prey Model]] · [[Predator Satiation]] · [[Predation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
