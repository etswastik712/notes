---
title: Genetic Drift and Inbreeding Depression
aliases: ["genetic drift", "inbreeding depression", "loss of heterozygosity"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Genetic Drift and Inbreeding Depression

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide's one line: genetic drift leading to inbreeding depression and loss of heterozygosity ([[07_Conservation Biology.pdf#page=15|slide 15]])  ·  🔵 **extra · beyond:** the heterozygosity decay formula

> [!intuition] In one picture
> In a small population allele frequencies wander by chance, rare variants vanish, and relatives mate; harmful recessives then show up more often.

> [!key] Definition
> **Genetic drift:** random change of allele frequencies, strongest in small populations. Expected heterozygosity decays as $H_t=H_0\big(1-\tfrac{1}{2N_e}\big)^t$ for effective size $N_e$. **Inbreeding depression:** reduced fitness caused by mating among relatives (expression of deleterious recessives).

## Drift in numbers
With $2N_e$ gene copies sampled each generation, the expected heterozygosity declines by $1/2N_e$: $H_t=H_0(1-1/2N_e)^t$; the inbreeding coefficient is $F_t=1-H_t/H_0$. Half of the variation is lost after $t_{1/2}=\ln2/(-\ln(1-1/2N_e))\approx1.39N_e$ generations.

> [!example] Effective size and the clock
> After 100 generations $H/H_0=0.006,\ 0.37,\ 0.905$ for $N_e=10,\ 50,\ 500$; half-lives 13.5, 69 and 693 generations. **$N_e$ is smaller than the census $N$:** for an unequal sex ratio $N_e=\dfrac{4N_mN_f}{N_m+N_f}$: 10 males and 40 females give $N_e=4\times10\times40/50=32$, not 50. Variation in family size and fluctuating population size reduce it further.
> **Inbreeding depression:** as $F$ rises deleterious recessives are expressed more often; if fitness falls by a fraction $\delta F$, a population with $F=0.25$ (full-sib mating) and $\delta=0.5$ loses about 12 % of fitness (illustrative). Low diversity also limits adaptation to change ([[Population Biology of Invasions]]: founder bottlenecks).

**Link to extinction.** Inbreeding lowers survival and fecundity, which makes the population smaller, which increases drift: a feedback, part of the "extinction vortex" ([[Demographic Genetic and Environmental Stochasticity]]). The passenger pigeon genome paper (Murray et al. 2017) is cited on slide 13 without a claim about its role in the extinction.

> [!pitfall] Drift is not selection
> Drift changes allele frequencies by chance, not adaptively; its strength depends on $N_e$ and on time. Gene flow (a few migrants per generation) can offset it, one reason for corridors ([[Reserve Design and Management]]). Figure: [[Minimum Viable Population]].

Used in: [[EE07 Conservation Biology]]. Related: [[Demographic Genetic and Environmental Stochasticity]] · [[Minimum Viable Population]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Continued in the vault (added 2026-10-29)
- Quantitative treatment of drift as a diffusion (Wright-Fisher, Kimura, fixation probability $=p_0$): [[Wright-Fisher Drift as Diffusion]].
