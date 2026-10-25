---
title: Mark-Recapture Estimation
aliases: ["capture-recapture", "Lincoln-Petersen estimator", "Chapman estimator"]
subject: eco-evo
type: concept
scope: [extra-book, extra-beyond]
by: [karanth, own-notes]
status: draft
tags: [subject/eco-evo, type/concept, extra/book, extra/beyond, src/paper, src/own, status/draft]
---
# Mark-Recapture Estimation

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Karanth and Nichols (2010), non-invasive tiger survey chapter (paper tier)  ·  🔵 **extra · beyond:** the estimator and its assumptions

> [!intuition] In one picture
> Mark some animals and release them. If a later sample has a large share of marked animals, the population is small; a small share means it is large.

> [!key] Definition
> Lincoln-Petersen: mark $M$ animals and release; later catch $n$, of which $m$ are marked; then $\hat N=Mn/m$ (less biased: $\hat N=\frac{(M+1)(n+1)}{m+1}-1$). Assumes a closed population and equal capture probability. With capture probability $p$ and $C$ animals counted, $N=C/p$.

## Estimators and their precision
$M$ animals are marked; a later sample of $n$ contains $m$ marked. Equal chances give $m/n\approx M/N$, so $\hat N_{LP}=Mn/m$ (Lincoln-Petersen). The Chapman form $\hat N=\frac{(M+1)(n+1)}{m+1}-1$ has less small-sample bias, with variance $\frac{(M+1)(n+1)(M-m)(n-m)}{(m+1)^2(m+2)}$.

> [!example] Precision depends on recaptures
> $M=50$, $n=40$: $m=20$: $\hat N=99$, SE 11, approximate 95 % interval 76–121. $m=8$: $\hat N=231$, SE 59, interval 116–347. $m=3$: $\hat N=522$, SE 213, interval 104–940. A problem sample $M=40$, $n=50$, $m=10$: $\hat N_{LP}=200$, Chapman 189, SE 42 (108–271). **Fewer recaptures, much less information.**
> **General form:** $\hat N=C/\hat p$ (count over detection probability). With per-occasion capture probability $p=0.1$ and $K=10$ occasions, the chance of at least one capture is $1-0.9^{10}=0.651$; $C=30$ distinct animals then give $\hat N=46$.

**Assumptions.** A *closed* population (no births, deaths, immigration, emigration during the study), equal capture probability for all individuals (relaxed by models of heterogeneity, $M_h$), marks that are not lost and are always recognised. **Open** models (Cormack-Jolly-Seber) estimate survival and recruitment from several occasions; multi-occasion closed models use the full capture history matrix ([[Tiger Population Surveys]]).

> [!pitfall] The estimate hides unmarked animals' behaviour
> "Trap-happy" or "trap-shy" animals bias $\hat p$; marking itself can change survival; if capture depends on the animal, $\hat N$ is biased low. Sampling theory: [[Probability - Course Map]]. Tool in conservation: [[EE07 Conservation Biology]].

Used in: [[EE07 Conservation Biology]]. Related: [[Tiger Population Surveys]] · [[Bayes' Theorem]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
