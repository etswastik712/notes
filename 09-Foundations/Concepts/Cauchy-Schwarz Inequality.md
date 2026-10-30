---
title: Cauchy-Schwarz Inequality
aliases: ["Cauchy–Schwarz", "Schwarz inequality", "correlation bound"]
subject: foundations
type: concept
by: [own-notes]
status: draft
tags: [subject/foundations, type/concept, src/own-notes, status/draft]
---
# Cauchy-Schwarz Inequality

> [!intuition] In one picture
> A vector cannot overlap another by more than the product of their lengths: $|\langle u,v\rangle|\le\|u\|\|v\|$, with equality only when they are parallel.

> [!key] Key facts
> In any real inner-product space $\langle u,v\rangle^2\le\langle u,u\rangle\langle v,v\rangle$. **Proof:** $0\le\langle u+tv,u+tv\rangle=\|u\|^2+2t\langle u,v\rangle+t^2\|v\|^2$ for all real $t$, so the discriminant is $\le0$. Equality iff $u,v$ are linearly dependent.
> - **Probability:** $u=X-\mu_X$, $v=Y-\mu_Y$ with $\langle u,v\rangle=E[uv]$ gives $\mathrm{Cov}(X,Y)^2\le\mathrm{Var}X\,\mathrm{Var}Y$, i.e. $|\rho|\le1$, with $|\rho|=1$ exactly for $Y=aX+b$.
> - **Quantum mechanics:** applied to $(A-\langle A\rangle)\psi$ and $(B-\langle B\rangle)\psi$ it gives the uncertainty relation.
> - **Integrals and sums:** $\big(\int fg\big)^2\le\int f^2\int g^2$ and $(\sum a_ib_i)^2\le\sum a_i^2\sum b_i^2$.

> [!pitfall] Watch out
> The argument needs $\|v\|\ne0$ (if $\|v\|=0$ then $v=0$ and both sides vanish); for complex inner products rotate the phase of $v$ so that $\langle u,v\rangle$ is real and non-negative first.

Used in: [[PR07 Sums of Independent Variables Covariance and Correlation]], [[Generalised Uncertainty Principle]]. Related: [[Covariance Matrix]] · [[Covariance and Correlation]] · [[Heisenberg Uncertainty Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
