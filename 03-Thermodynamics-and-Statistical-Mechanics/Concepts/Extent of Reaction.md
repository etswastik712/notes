---
title: Extent of Reaction
aliases: ["reaction coordinate", "advancement of a reaction", "n_i = n_i0 + nu_i xi", "driving force of a reaction", "limiting reagent"]
subject: thermo
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/thermo, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Extent of Reaction

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Bhagwat.pdf#page=1|Bhagwat notes]], p. 4: $n_i=n_i^0+\nu_i\varepsilon$, $\mathrm dG^{\rm t}=\sum\mu_i\mathrm dn_i=(\sum\nu_i\mu_i)\mathrm d\varepsilon$.
> 🔵 **extra · beyond:** the interior minimum of $G(\varepsilon)$ and the numerical tables (mine).

> [!intuition] In one picture
> One number, $\varepsilon$, counts how far the reaction has gone: every species changes by $\nu_i\varepsilon$ moles; the Gibbs energy of the whole mixture, as a function of $\varepsilon$, is a bowl and equilibrium is the bottom.

> [!key] Definition
> For $\sum\nu_iA_i=0$ ($\nu<0$ reactants): $n_i=n_i^0+\nu_i\varepsilon$. At constant $T,P$: $(\partial G^{\rm t}/\partial\varepsilon)_{T,P}=\sum_i\nu_i\mu_i=\Delta_rG=RT\ln(Q/K)$; zero at equilibrium.

$\mathrm{SO_2}+\tfrac12\mathrm{O_2}\rightleftharpoons\mathrm{SO_3}$ from $1$ mol SO$_2$ and $\tfrac12$ mol O$_2$: moles $(1-\varepsilon,\tfrac{1-\varepsilon}2,\varepsilon)$. $\partial G/\partial\varepsilon\to-\infty$ at $\varepsilon\to0$ and $+\infty$ at the end: the minimum is interior (entropy of mixing), so no ideal-gas reaction goes to completion.

Used in: [[TH10 Open Systems Mixing and Reacting Gases]], [[TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries]]. Related: [[Equilibrium Constant]] · [[Law of Mass Action]] · [[Chemical Potential]] · [[Pressure Dependence of Chemical Equilibrium]] · [[Gibbs Free Energy]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
