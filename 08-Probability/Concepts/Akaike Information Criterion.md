---
title: Akaike Information Criterion
aliases: [AIC, AICc, Akaike weights, information-theoretic model selection]
subject: probability
type: concept
scope: [extra-book, extra-beyond]
by: [holdo]
status: draft
tags: [subject/probability, subject/eco-evo, type/concept, extra/book, extra/beyond, src/paper, src/own-notes, status/draft]
---
# Akaike Information Criterion

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** Holdo et al. (2009) compare 14 models with ΔAICc ([[Holdo_2009_Opposing rainfall and nutritional gradients best explain the wildebeest migration in the Serengeti.pdf#page=5|Table 1, p.435]]); the instructor says not to be "awed by the details" · 🔵 **extra · beyond:** the definition, the weights and my computation from Table 1.

> [!intuition] A fit penalised for showing off
> Adding parameters can only improve a model's fit to the data in hand, so "best fit" would always pick the most baroque model. AIC subtracts a price for each parameter: you must *earn* a parameter by improving the fit by more than it costs.

> [!key] Definitions
> $\mathrm{AIC}=-2\ell+2K$, with $\ell$ the maximised log-likelihood and $K$ the number of fitted parameters. For $n$ observations the small-sample correction is $\mathrm{AICc}=-2\ell+\dfrac{2Kn}{n-K-1}$ (Holdo's Eq. 2 is a modified form for spatially correlated data, with $K=p+k+1$). Only **differences** matter: $\Delta_i=\mathrm{AICc}_i-\min\mathrm{AICc}$.
> **Akaike weight:** $w_i=\dfrac{e^{-\Delta_i/2}}{\sum_j e^{-\Delta_j/2}}$, the relative support for model $i$ within the candidate set (Burnham & Anderson 2002).

- Rules of thumb: $\Delta<2$ substantial support; $4$–$7$ considerably less; $>10$ essentially none.
- **Pitfall:** it ranks only the models you entered. The "best" of a bad set is still bad; and it is a comparison of fits, not a test of the mechanism.

> [!example] Worked example: weights from Holdo's Table 1 (my computation)
> At the 10 km lattice (OLS): $I,T,N$ ($\Delta=0$), $I,T,N,F$ ($0.4$), $I,T,N,R$ ($4.1$) give $e^{0}=1$, $e^{-0.2}=0.819$, $e^{-2.05}=0.129$, others $<10^{-9}$. Sum $=1.948$, so $w=0.513,\ 0.420,\ 0.066$. The total weight of models **containing plant N** is 1.000 at both lattices; the total weight of models driven by green *biomass* $G$ is $2\times10^{-24}$ (10 km) and $2\times10^{-10}$ (25 km). So the data decisively favour *intake and protein* over *biomass*, but cannot say whether water (F) matters.

![[fig_ee01_aicc.png|700]]

Used in: [[EE01 Introduction to Biology and Ecological Thinking]] · [[Serengeti Wildebeest Migration]].
Connections: [[Bayes' Theorem]] (Akaike weights can be read as approximate posterior model probabilities under particular priors) · [[Strong Inference]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
