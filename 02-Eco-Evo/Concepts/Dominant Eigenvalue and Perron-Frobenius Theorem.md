---
title: Dominant Eigenvalue and Perron-Frobenius Theorem
aliases: ["Perron-Frobenius theorem", "dominant eigenvalue", "lambda"]
subject: eco-evo
type: concept
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/beyond, src/slides, status/draft]
---
# Dominant Eigenvalue and Perron-Frobenius Theorem

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide's statement for 'the mathematically oriented' (others can ignore): $\lambda$ is the dominant eigenvalue, the SAD its eigenvector ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=21|slide 21]])  ·  🔵 **extra · beyond:** primitivity and the strong form of the theorem

> [!intuition] In one picture
> A matrix with no negative entries cannot cancel itself out, so one growth factor must win in the long run.

> [!key] Definition
> For a square matrix with non-negative entries the **Perron-Frobenius theorem** guarantees that its spectral radius is an eigenvalue with a non-negative eigenvector. If the matrix is also **primitive** (irreducible and aperiodic, as a Leslie matrix with two adjacent fertile ages is), that eigenvalue $\lambda_1>0$ is simple, strictly larger in modulus than all others, and its eigenvector is strictly positive. It is the growth factor and the stable age distribution.

## The theorem and how to check its hypotheses
**Irreducible**: the life-cycle graph is connected (a path from every class to every other). **Primitive**: the greatest common divisor of the loop lengths is 1 (equivalently, some power $\mathbf A^k$ is strictly positive). For such a non-negative matrix: one simple, real, positive eigenvalue $\lambda_1$, strictly larger in modulus than all others, with strictly positive right ($\mathbf w$) and left ($\mathbf v$) eigenvectors. Then $\mathbf n_t/\lambda_1^t\to c\,\mathbf w$ with $c=\mathbf v^{T}\mathbf n_0/\mathbf v^{T}\mathbf w$ (Caswell's "ergodicity": the population forgets its start).

> [!example] Three small matrices
> - **Slide Leslie matrix** ($F_2,F_3,F_4>0$): loops of length 2, 3, 4, gcd 1: primitive; $\lambda=1.0508$, others of modulus $0.952,\ 0.10,\ 0.10$.
> - **Fibonacci's rabbits** $\begin{pmatrix}1&1\\1&0\end{pmatrix}$: loops of length 1 and 2, primitive; $\lambda=(1+\sqrt5)/2=1.618$.
> - **Semelparous** (single loop of length 3): all three eigenvalues have modulus $(F_3P_1P_2)^{1/3}$: not primitive; the population cycles with period 3.

**Computing it.** Power iteration $\mathbf n_{t+1}=\mathbf A\mathbf n_t$ converges at the rate $|\lambda_2|/\lambda_1$; that is what the slides' simulation does.

> [!pitfall] The slide states the weak form
> "A non-negative matrix has at least one real eigenvalue" is true but not enough to guarantee that the simulation settles; primitivity is the extra condition. The stability picture is that of [[Fixed Points and Linear Stability]]: the zero-population state of the linear model is unstable iff $\lambda_1>1$.

Used in: [[EE02 Structured Population Models]]. Related: [[Leslie Matrix]] · [[Stable Age Distribution]] · [[Linearisation and Sensitivity]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
