---
title: Central Limit Theorem
aliases: ["CLT"]
subject: probability
type: concept
scope: [extra-book]
by: [lecture-notes]
status: draft
tags: [subject/probability, type/concept, extra/book, src/lecture-notes, status/draft]
---
# Central Limit Theorem

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **extra · book:** AI notes Example 2.8 and §1.5 (Lyapunov); Ross Ch. 8.

> [!intuition] In one picture
> Sums of many small independent pieces look normal, whatever the pieces look like.

> [!key] Definition
> For iid $X_i$ with mean $\mu$ and variance $\sigma^2>0$: $S_n^*=\frac{\sum X_i-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$.

## Proof via MGFs
$M_{S_n^*}(t)=[M_Z(t/\sqrt n)]^n=(1+\frac{t^2}{2n}+o(\frac1n))^n\to e^{t^2/2}$, then the continuity theorem.

## Rate
For sums of Exp$(1)$, $\sup_x|F_n-\Phi|=0.158,0.0596,0.0243,0.0133,0.0042$ at $n=1,5,30,100,1000$, matching $\gamma_1/(6\sqrt{2\pi n})$ with $\gamma_1=2$ (Figure PR6.2).

> [!pitfall] Finite variance required
> Heavy-tailed laws such as the Cauchy do not satisfy it.

Used in: [[PR06 Moments Generating Functions and Limit Theorems]]. Related: [[Normal Approximation to the Binomial]] · [[Moment Generating Function]] · [[Standardisation of a Random Variable]].

## Added with QM06 (oscillator toolbox)
**Hermite link:** the Edgeworth corrections to the CLT are series in $\mathrm{He}_n(x)\varphi(x)$; the leading cdf term $-\frac{\gamma_1}{6\sqrt n}\mathrm{He}_2(x)\varphi(x)$ has maximum modulus $\gamma_1/(6\sqrt{2\pi n})$ ([[Probabilists' Hermite Polynomials]]).

> [!connection] See also
> Proof sketch through characteristic functions with a numerical check: [[Fourier and Laplace Transforms]] §9.

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
