---
title: Median and Mode
aliases: ["median", "mode", "midpoint and peak"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Median and Mode

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week3_notes.pdf#page=1|Week 3, p.1]] (definitions) and Homework 3 Q1–Q2 ([[Week3_notes.pdf#page=6|p.6]]). · 🔵 **extra · beyond:** the mean–median–mode order, the Gumbel example.

> [!intuition] In one picture
> The median is the point that splits the probability in half; the mode is the peak of the density (or the most likely value).

> [!key] Definition
> **Median:** $c$ with $P[X\le c]\ge\tfrac12$ **and** $P[X\ge c]\ge\tfrac12$ (continuous: $F(c)=\tfrac12$). **Mode:** continuous, a global maximum of $f$; discrete, a value $x_i$ with $p_i\ge p_j$ for all $j$.

## Discrete median (the lecture's recipe)
Find the first $i$ with $p_1+\dots+p_{i-1}<\tfrac12\le p_1+\dots+p_i$. If the sum exceeds $\tfrac12$, $x_i$ is the **unique** median; if it equals $\tfrac12$, **every** $c\in[x_i,x_{i+1}]$ is a median (in practice $x_i$ or the midpoint).

## Table (checked)
| Law | Median | Mode |
|---|---|---|
| fair die | every $c\in[3,4]$ | all six faces |
| $U(a,b)$ | $\tfrac{a+b}2$ | every point of $[a,b]$ |
| Expo$(\lambda)$ | $\ln2/\lambda$ | $0$ (convention $f(0)=\lambda$) |
| Pareto$(a)$ | $2^{1/a}$ | $1$ |
| Gumbel | $-\ln\ln2=0.3665$ | $0$ |
| $N(\mu,\sigma^2)$ | $\mu$ | $\mu$ |

For right-skewed laws **mean $>$ median $>$ mode** (Expo$(1)$: $1>0.693>0$; Gumbel: $0.577>0.367>0$; Pareto$(2)$: $2>1.414>1$).

> [!pitfall] Three "averages", three questions
> Mean = balance point (uses all the values), median = the 50 % point (robust to outliers), mode = most likely value. In quantum mechanics $\langle x\rangle$ is the mean of $|\psi|^2$; for $\psi_1$ of the oscillator it is $0$ while the modes are $\pm\sqrt{\hbar/m\omega}$ ([[Expectation Value]]).

Used in: [[PR06 Moments Generating Functions and Limit Theorems]] §1, §3.3. Related: [[Cumulative Distribution Function]] · [[Expectation]] · [[Uniform Distribution]] · [[Exponential Distribution]] · [[Pareto Distribution]] · [[Gumbel Distribution]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
