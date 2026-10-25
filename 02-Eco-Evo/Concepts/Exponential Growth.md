---
title: Exponential Growth
aliases: ["geometric growth", "first law of population dynamics", "Malthusian growth"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Exponential Growth

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** both forms, the 'first law' argument, Fibonacci as the first ecological modeller, and the practice sums ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=9|slide 9]])

> [!intuition] In one picture
> With nothing to stop it, a population multiplies by the same factor every step, so it doubles on a fixed schedule however large it is. That constant-factor behaviour is the population analogue of Newton's first law: what happens when nothing external acts.

> [!key] Definition
> Discrete: $N_{t+1}=N_t+N_t(b-d+i-e)=\lambda N_t$, so $N_t=\lambda^tN_0$ with $\lambda=1+b-d+i-e$. Continuous: $\frac1N\frac{dN}{dt}=r$, so $N=N_0e^{rt}$, and $\lambda=e^{r}$. Doubling time $t_d=\ln 2/r$.

## Derivations and numbers
Discrete: $N_{t+1}=\lambda N_t\Rightarrow N_t=\lambda^tN_0$ with $\lambda=1+b-d+i-e$. Continuous: $\dot N=rN\Rightarrow N=N_0e^{rt}$; the two agree at integer times when $\lambda=e^{r}$, i.e. $r=\ln\lambda$. Doubling time $t_d=\ln2/r=\ln2/\ln\lambda$. For small rates $r\approx\lambda-1$.

> [!example] The practice sums (answers)
> Humans: doubling in 50 years gives $r=\ln2/50=0.0139$ and $5.4\times10^9e^{0.0139\times7}=5.95\times10^{9}$ after 7 years. A plant growing 12 % a year: $r=\ln1.12=0.113$, $t_d=6.1$ years. Beetles with 400 births and 150 deaths in 3,000 a month: $r=0.0833$, $N_6=3000e^{0.5}=4{,}946$ (discrete: $3000\times1.0833^6=4{,}849$; $\ln1.0833=0.0800$). Algae 100,000 to 500,000 in 10 days: $r=\ln5/10=0.161$ per day and 2.5 million ten days later.
> **Molles' infection example.** One case infecting 3 a day: day $k$ has $3^k$ new cases and the total after day 7 is $\sum_{k=0}^{6}3^k=(3^7-1)/2=1{,}093$ (729 new cases on the last day): the same arithmetic as growth at $\lambda=3$.

> [!pitfall] "No limit" cannot last
> Exponential growth has no steady state (only growth, constancy or decay). *Phlox* at $\lambda=2.4177$ would reach about 77 plants per square metre over North America in 32 years: the point is that a limit must appear ([[Density Dependence]]). Also, doubling time depends only on $r$, not on size, which is why early exponential growth (an epidemic) looks slow and then sudden.

> [!extra-beyond]- 🔵 Extra (beyond): Fibonacci's rabbits
> $\begin{pmatrix}1&1\\1&0\end{pmatrix}$ has dominant eigenvalue $(1+\sqrt5)/2=1.618$, the first projection and the first stable-age ratio ([[Leslie Matrix]]).

"First law" status: the null model in the sense of Hardy-Weinberg; departures (density, structure, noise) explain the rest of [[EE03 Population Dynamics and Chaos]].

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Logistic Growth]] · [[Density Dependence]] · [[Population Ecology]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
