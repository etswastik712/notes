---
title: BB84 Protocol
aliases: [BB84, quantum key distribution, QKD]
subject: qm
type: concept
scope: [extra-beyond]
by: [own-notes]
status: draft
tags: [subject/qm, type/concept, extra/beyond, src/own-notes, status/draft]
---
# BB84 Protocol

<span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🔵 **Extra · beyond:** derived here ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11.4); Bennett and Brassard (1984) recalled.

> [!intuition] In one picture
> Encode bits in two incompatible bases ($\sigma_z$ and $\sigma_x$ eigenstates); an eavesdropper must disturb them because the bases do not commute.

> [!key] Definition and key results
> Alice sends $|{\pm z}\rangle$ or $|{\pm x}\rangle$ at random; Bob measures in a random basis; they keep the half of the bits with matching bases. Intercept–resend by Eve: wrong basis with probability $\frac12$, then Bob wrong with probability $\frac12$: **25 % errors** in the sifted key.

Comparing $n$ test bits misses Eve with probability $(3/4)^n$: $1.0\times10^{-5}$ for $n=40$; $n=73$ gives $<10^{-9}$. Probability: [[Conditional Probability]], [[Binomial Distribution]].

> [!pitfall] Pitfall
> The security comes from non-commutation and no-cloning, not from secrecy of the encoding.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §11.4. Related: [[No-Cloning Theorem]] · [[Pauli Matrices]] · [[Measurement Postulate]] · [[Conditional Probability]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
