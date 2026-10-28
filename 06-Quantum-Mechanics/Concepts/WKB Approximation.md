---
title: WKB Approximation
aliases: ["semiclassical approximation", "Wentzel-Kramers-Brillouin"]
subject: qm
type: concept
scope: [extra-book]
by: [book]
status: draft
tags: [subject/qm, type/concept, extra/book, src/book, status/draft]
---
# WKB Approximation

<span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §2.5.4 (printed pp.104–108, [[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=124|PDF p.124]]).

> [!intuition] In one picture
> Treat a slowly varying potential as a staircase of tiny flat pieces and multiply their exponentials.

> [!key] Definition and key results
> $\psi\simeq\exp\big(\pm\tfrac i\hbar\int p\,dx\big)/\sqrt p$, $p=\sqrt{2m(E-V)}$. Tunnelling: $T\simeq\exp(-2\int_{x_1}^{x_2}\kappa\,dx)$. Valid when $|d\lambda/dx|\ll1$.

Fails at the turning points (connection formulas needed) and for thin barriers (prefactor $16\frac E{V_0}(1-\frac E{V_0})$ missing).

Used in: [[QM08 Quantum Tunnelling]] §5. Related: [[Gamow Factor]] · [[Quantum Tunnelling]] · [[Correspondence Principle]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
