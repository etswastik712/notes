---
title: Pauli Matrices
aliases: ["spin matrices", "X, Y, Z matrices"]
subject: qm
type: concept
scope: [taught, extra-book]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/concept, taught, extra/book, src/lecture-notes, status/draft]
---
# Pauli Matrices

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[PH2113_matrices_expectation_uncertainty.pdf#page=1|MX §1]] (called $X,Y,Z$). · 🟡 **extra · book:** the name and the link to spin (Griffiths Ch. 4, not in the course notes).

> [!intuition] In one picture
> The three simplest non-commuting questions you can ask of a two-state system.

> [!key] Definition
> $X=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $Y=\begin{pmatrix}0&-i\\i&0\end{pmatrix}$, $Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$; eigenvalues $\pm1$; $[X,Y]=2iZ$, $[Y,Z]=2iX$, $[Z,X]=2iY$; $X^2=Y^2=Z^2=I$.

## Eigenvectors and basis change
$|{\pm z}\rangle=\binom10,\binom01$; $|{\pm x}\rangle=\frac1{\sqrt2}\binom1{\pm1}$; $|{\pm y}\rangle=\frac1{\sqrt2}\binom1{\pm i}$. $|{+x}\rangle=\frac{1-i}2|{+y}\rangle+\frac{1+i}2|{-y}\rangle$; $X|{+y}\rangle=i|{-y}\rangle$.

> [!pitfall] Same state, different matrix
> Basis change alters the coordinates of states and operators, not the physics: eigenvalue equations hold in every basis.

Used in: [[QM03 States Operators and Measurement]]. Related: [[Two-Level System]] · [[Commutator]] · [[Generalised Uncertainty Principle]] · [[Eigenstate and Eigenvalue]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
