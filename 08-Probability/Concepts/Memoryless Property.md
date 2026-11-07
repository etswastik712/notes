---
title: Memoryless Property
aliases: ["memorylessness", "no memory", "lack of memory"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Memoryless Property

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week2_notes.pdf#page=3|Week 2, pp.3–5]] (definition, theorem, both proofs). · 🔵 **extra · beyond:** the degenerate cases, counter-examples.

> [!intuition] In one picture
> Having waited a while tells you nothing about how much longer you must wait.

> [!key] Definition
> $P[X\ge t+s\mid X\ge s]=P[X\ge t]$ for all $s,t\ge0$ (non-negative integers for a discrete $X$). **Theorem:** a non-negative memoryless $X$ is Geom$(p)$ (discrete) or Expo$(\lambda)$ (continuous).

## Proof sketch (lecture)
Since $\{X\ge m+n\}\subset\{X\ge m\}$, memorylessness is $P[X\ge m+n]=P[X\ge m]\,P[X\ge n]$. *Discrete:* $a_n=P[X\ge n]$ satisfies $a_{m+n}=a_ma_n$, so $a_n=a_1^n$: $P[X\ge k]=q^k$ with $q=a_1$, the geometric law (failures counted). *Continuous:* $G(x)=P[X\ge x]$ has $G(t+s)=G(t)G(s)$, so $G(\tfrac mn)=G(1)^{m/n}$ for rationals, and by continuity $G(x)=G(1)^x=e^{-\lambda x}$ with $\lambda=-\ln G(1)$.

## Examples
Exponential: $P[T\ge10\mid T>9]=e^{-1/2}$ (HW2 Q1). Geometric ($q=0.6$): $P[G\ge5]/P[G\ge2]=0.216=P[G\ge3]$. **Not memoryless:** $U(0,1)$ ($P[X\ge0.75\mid X\ge0.25]=\tfrac13\ne P[X\ge0.5]=\tfrac12$), Pareto, a bus on a timetable.

> [!pitfall] The theorem needs $G(1)\in(0,1)$
> $G(1)=0$ or $1$ gives degenerate variables ($X=0$ or $X=\infty$); the lecture does not mention it. Also "memoryless" is a modelling assumption: wear-out failures are not.

Used in: [[PR05 Continuous Random Variables]] §6. Related: [[Exponential Distribution]] · [[Geometric Distribution]] · [[Conditional Probability]] · [[Pareto Distribution]].


## Continued in the vault (added 2026-11-07)
- Repeated memorylessness gives the Rényi gaps of exponential order statistics: [[Exponential Order Statistics]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```

## Across subjects
- [[Radioactive Decay Law]] (Landscapes): the half-life is constant, independent of the sample's age, because nuclear decay is memoryless.
