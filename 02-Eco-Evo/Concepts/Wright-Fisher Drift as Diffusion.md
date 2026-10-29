---
title: Wright-Fisher Drift as Diffusion
aliases: [Kimura diffusion, neutral drift diffusion limit, genetic drift random walk]
subject: eco-evo
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/eco-evo, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Wright-Fisher Drift as Diffusion

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond** ([[THX1 Diffusion Random Walks and the Heat Equation]] §7; the qualitative idea is in [[Genetic Drift and Inbreeding Depression]]).

> [!intuition] In one picture
> In a small population allele frequencies take a random walk, with bigger steps at intermediate frequency, and are absorbed at 0 and 1.

> [!key] Definition and key results
> $p'\sim\operatorname{Bin}(2N,p)/2N$: $\langle p'\rangle=p$, $\operatorname{Var}=p(1-p)/2N$. Diffusion limit $D(p)=p(1-p)/4N$ per generation. $\operatorname{Var}(p_t)=p_0(1-p_0)[1-(1-1/2N)^t]$; fixation probability $=p_0$ (martingale); time scale $\sim2N$–$4N$ generations.

> [!pitfall] Pitfall
> Drift acts on frequencies of neutral alleles; it does not drive adaptation, but it erases variation fastest in small populations.

Used in: [[THX1 Diffusion Random Walks and the Heat Equation]]. Related: [[Genetic Drift and Inbreeding Depression]] · [[Random Walk]] · [[Binomial Distribution]] · [[Diffusion Equation]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Binomial Distribution]] (Probability): the sampling step of Wright–Fisher
- [[EE07 Conservation Biology]] (Eco-Evo): effective population size and loss of heterozygosity
