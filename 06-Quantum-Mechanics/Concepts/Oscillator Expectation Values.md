---
title: Oscillator Expectation Values
aliases: ["moments of x in psi_n", "<x^4>", "oscillator moments"]
subject: qm
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Oscillator Expectation Values

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** $\langle x\rangle,\langle p\rangle,\langle x^2\rangle,\langle p^2\rangle$ ([[Harmonic_oscillator.pdf#page=12|lecture pp.12–13]], [[Tutorial3.pdf#page=1|Tutorial III Q1–Q2]]). · 🔵 **extra · beyond:** $\langle x^4\rangle$, superpositions, $\langle V\rangle,\langle T\rangle$.

> [!intuition] In one picture
> Count the rungs: a word of $\hat a$ and $\hat a^\dagger$ only contributes on the diagonal if it goes up as often as it goes down.

> [!key] Definition
> With $\sigma^2=\hbar/2m\omega$: $\ \langle x^2\rangle_n=(2n+1)\sigma^2$, $\ \langle x^4\rangle_n=(6n^2+6n+3)\sigma^4$, $\ \langle p^2\rangle_n=(2n+1)\dfrac{m\hbar\omega}2$, $\ \langle x\rangle=\langle p\rangle=\langle x^3\rangle=0$.

## Recipe
Write the operator with $\hat x=\sigma(\hat a+\hat a^\dagger)$, $\hat p=\frac{i\hbar}{2\sigma}(\hat a^\dagger-\hat a)$; each word moves $n\to n\pm1$ with a factor $\sqrt{\max(n_{\rm in},n_{\rm out})}$; keep only balanced words. For $\hat x^4$ six words contribute: $(n+1)(n+2)+(n+1)^2+2n(n+1)+n^2+n(n-1)=6n^2+6n+3$.

## Derived quantities
$\langle V\rangle=\tfrac12m\omega^2\langle x^2\rangle=\tfrac14(2n+1)\hbar\omega=\tfrac12E_n$ and $\langle T\rangle=\langle p^2\rangle/2m=\tfrac12E_n$; $\Delta x\Delta p=(n+\tfrac12)\hbar$. $\langle x^4\rangle/\langle x^2\rangle^2=3,\ 1.667,\ 1.56,\ \dots\to1.5$ for $n=0,1,2,\dots\to\infty$.

## Superpositions
$\langle x\rangle=\sqrt{2\hbar/m\omega}\sum_n\sqrt{n+1}\,\mathrm{Re}(c_n^*c_{n+1})$ oscillates at exactly $\omega$ for every state; $\langle x^2\rangle$ has frequencies $0$ and $2\omega$.

> [!pitfall] Normal ordering matters
> $\hat a\hat a^\dagger=\hat a^\dagger\hat a+1$: forgetting the $+1$ turns $2n+1$ into $2n$.

Used in: [[QM05 The Harmonic Oscillator]] §6, [[QM06 The Oscillator Toolbox]] §3. Related: [[Expectation Value]] · [[Ladder Operators]] · [[Number Operator]] · [[Matrix Elements of Position and Momentum]] · [[Normal Ordering]] · [[Heisenberg Uncertainty Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
