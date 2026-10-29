---
title: Entanglement
aliases: [entangled state, EPR pair, Einstein-Podolsky-Rosen]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Entanglement

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.10.1 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=244|PDF p.244]]). 🔵 **Extra · beyond:** the proof of $E=-\mathbf a\cdot\mathbf b$ and the no-signalling check ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11).

> [!intuition] In one picture
> A pure state of two systems that cannot be written as a product: each part is a coin toss, together they are perfectly correlated.

> [!key] Definition and key results
> Singlet: $E(\mathbf a,\mathbf b)=\langle\sigma_{\mathbf a}\otimes\sigma_{\mathbf b}\rangle=-\mathbf a\cdot\mathbf b$; marginals $\frac12$ for every setting (**no signalling**); reduced states $\rho_{1,2}=\frac12\mathbf1$ with entropy $\ln2$ (one bit of entanglement).

Proof: $(\boldsymbol\sigma_1+\boldsymbol\sigma_2)|0,0\rangle=0$, so $(\mathbf a\cdot\boldsymbol\sigma_1)(\mathbf b\cdot\boldsymbol\sigma_2)|0,0\rangle=-[\mathbf a\cdot\mathbf b+i(\mathbf a\times\mathbf b)\cdot\boldsymbol\sigma_1]|0,0\rangle$ and $\langle\boldsymbol\sigma_1\rangle=0$. The correlations are strong enough to violate Bell/CHSH ([[Bell Inequality and CHSH]]).

> [!pitfall] Pitfall
> Entanglement does not send signals: Bob's statistics do not change whatever Alice measures; correlations appear only when results are compared.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §10–§11. Related: [[Singlet and Triplet States]] · [[Bell Inequality and CHSH]] · [[No-Cloning Theorem]] · [[Density Matrix]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
