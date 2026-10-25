---
title: Sum Rules
aliases: ["Thomas-Reiche-Kuhn sum rule", "TRK sum rule", "oscillator strength sum rule"]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# Sum Rules

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **extra · beyond.**

> [!intuition] In one picture
> Completeness turns a sum over every intermediate state into a number you can compute from the commutator alone.

> [!key] Definition
> $\displaystyle\sum_n(E_n-E_m)|\langle n|\hat x|m\rangle|^2=\tfrac12\langle m|[\hat x,[\hat H,\hat x]]|m\rangle=\dfrac{\hbar^2}{2m}$ for $\hat H=\hat p^2/2m+V(x)$ (any $V$).

## Proof
Insert $\sum_n|n\rangle\langle n|$ into $\langle m|[\hat x,[\hat H,\hat x]]|m\rangle=2\langle m|\hat x\hat H\hat x|m\rangle-2E_m\langle m|\hat x^2|m\rangle=2\sum_n(E_n-E_m)|x_{nm}|^2$. With $[\hat H,\hat x]=-i\hbar\hat p/m$, $[\hat x,[\hat H,\hat x]]=-\frac{i\hbar}m[\hat x,\hat p]=\frac{\hbar^2}m$.

## Oscillator check
Only $n=m\pm1$: $\hbar\omega\,\sigma^2\big[(m+1)-m\big]=\hbar\omega\frac\hbar{2m\omega}=\frac{\hbar^2}{2m}$ ✓; numerically $0.500000$ for $m=3$ with $\hbar=m=\omega=1$. The simpler completeness sum $\sum_n|x_{mn}|^2=\langle x^2\rangle_m$ gives $3.5$ for $m=3$.

> [!pitfall] Absorption lowers, emission raises
> Terms with $E_n<E_m$ are negative: the rule is a balance between absorption and stimulated emission, not a sum of positive strengths.

Used in: [[QM06 The Oscillator Toolbox]] §3. Related: [[Completeness Relation]] · [[Commutator]] · [[Matrix Elements of Position and Momentum]] · [[Selection Rules]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
