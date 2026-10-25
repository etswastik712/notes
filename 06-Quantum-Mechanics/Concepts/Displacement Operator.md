---
title: Displacement Operator
aliases: ["D(alpha)", "translation in phase space"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Displacement Operator

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Pick up the vacuum Gaussian and slide it to the point $\alpha$ in phase space.

> [!key] Definition
> $\hat D(\alpha)=\exp(\alpha\hat a^\dagger-\alpha^*\hat a)$, unitary; $\hat D(\alpha)|0\rangle=|\alpha\rangle$ and $\hat D^\dagger(\alpha)\,\hat a\,\hat D(\alpha)=\hat a+\alpha$.

## Checks
$\hat D(\alpha)|0\rangle$ built with a matrix exponential agrees with the coherent-state formula to $3\times10^{-16}$ ($\alpha=1.2+0.9i$). Since $\hat D^\dagger\hat a\hat D=\hat a+\alpha$, $\hat a\hat D|0\rangle=\hat D(\hat a+\alpha)|0\rangle=\alpha\hat D|0\rangle$: the state is an eigenstate of $\hat a$.

> [!pitfall] $\hat D(\alpha)\hat D(\beta)\ne\hat D(\alpha+\beta)$
> They differ by a phase $e^{i\,\mathrm{Im}(\alpha\beta^*)}$, because $[\alpha\hat a^\dagger-\alpha^*\hat a,\ \beta\hat a^\dagger-\beta^*\hat a]\ne0$.

Used in: [[QM06 The Oscillator Toolbox]] §7. Related: [[Coherent State]] · [[Unitary Operator]] · [[Ladder Operators]] · [[Phase Space Picture of the Oscillator]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
