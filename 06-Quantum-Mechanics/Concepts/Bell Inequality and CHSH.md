---
title: Bell Inequality and CHSH
aliases: [Bell's theorem, CHSH inequality, Tsirelson bound, local hidden variables]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Bell Inequality and CHSH

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.10.2–3.10.3 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=247|PDF p.247 ff.]]). 🔵 **Extra · beyond:** CHSH, Tsirelson, the local model ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11).

> [!intuition] In one picture
> No pre-written list of answers for every axis can reproduce the singlet's correlations.

> [!key] Definition and key results
> Local models: $P(\mathbf a{+};\mathbf b{+})\le P(\mathbf a{+};\mathbf c{+})+P(\mathbf c{+};\mathbf b{+})$ (Wigner–Bell) and $|S|\le2$ with $S=\langle AB\rangle-\langle AB'\rangle+\langle A'B\rangle+\langle A'B'\rangle$. Quantum singlet: $P(\mathbf a{+};\mathbf b{+})=\frac12\sin^2\frac\theta2$; $|S|=|3\cos\varphi-\cos3\varphi|$, maximum $2\sqrt2$ at $\varphi=45^\circ$ (Tsirelson: $C^2=4+[A,A'][B,B']$).

Wigner–Bell at $\theta_{ac}=\theta_{cb}=60^\circ$: $0.375\not\le0.25$. CHSH is violated for $0<\varphi<68.5^\circ$ (root of $2c^3-3c+1=0$, $c=(\sqrt3-1)/2$). The simple local model $E=-1+2\theta/\pi$ reaches exactly $|S|=2$. Tested by Freedman–Clauser (1972), Aspect (1982), loophole-free (2015), Nobel 2022 (recalled).

> [!pitfall] Pitfall
> Bell does not refute hidden variables; it refutes **local** ones. Quantum mechanics also respects no-signalling, and $2\sqrt2<4$.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11.2–§11.3. Related: [[Entanglement]] · [[Singlet and Triplet States]] · [[Covariance and Correlation]] · [[Measurement Postulate]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
