---
title: Change of Variables for Densities
aliases: ["Jacobian", "transformation of densities", "f_Y = f_X(g^{-1}(y)) |dg^{-1}/dy|", "density of g(X)", "determinant of the Jacobian"]
subject: probability
type: concept
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
tags: [subject/probability, type/concept, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft, quiz/probability, quiz/pr-hw5, quiz/pr-hw6]
---
# Change of Variables for Densities

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[Week5_notes.pdf#page=8|Week 5 notes]], pp. 8–9: the formula in one variable and in $n$ variables with $\det\partial g^-1/\partial y$.
> 🔵 **extra · beyond:** several roots, polar coordinates, the linear map and Box–Muller examples (mine, simulation-checked).

> [!intuition] In one picture
> Probability is conserved; densities are probability per unit length (area, volume). Stretch space by a factor $|\det Dg|$ and the density is divided by it.

> [!key] Definition
> $Y=g(X)$, $g$ invertible: $f_Y(y)=f_X(g^{-1}(y))\,\Big|\dfrac{\mathrm dg^{-1}}{\mathrm dy}(y)\Big|=\dfrac{f_X(g^{-1}(y))}{|g'(g^{-1}(y))|}$. In $n$ variables: $f_Y(y)=f_X(g^{-1}(y))\,|\det\partial g^{-1}/\partial y|=f_X(g^{-1}(y))/|\det\partial g/\partial x|$. Several roots $x_i$ of $g(x)=y$: sum $f_X(x_i)/|g'(x_i)|$.

$Y=e^X$ ($X\sim N(0,1)$): $f_Y=\varphi(\ln y)/y$. $Y=X^2$: $\frac{e^{-y/2}}{\sqrt{2\pi y}}$ (two roots). $Y=AX$: divide by $|\det A|$. Polar coordinates (Jacobian $r$): iid $N(0,1)$ pairs give $R\sim$ Rayleigh and $\Theta\sim U[0,2\pi)$ independent.

Used in: [[PR09 Change of Variables the Multivariate Normal and Products of Uniforms]], [[PR05 Continuous Random Variables]], [[PR08 Order Statistics and the Multinomial Distribution]]. Related: [[Cdf Method for Transformations]] · [[Probability Integral Transform]] · [[Box-Muller Transform]] · [[Rayleigh Distribution]] · [[Multivariate Normal Distribution]] · [[Joint Density Function]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
