---
title: Spin Rotation Operator
aliases: [rotation operator for spin-1/2, SU(2) rotation, 4π rotation]
subject: qm
type: concept
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
tags: [subject/qm, type/concept, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# Spin Rotation Operator

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟡 **Extra · book:** Sakurai §3.1–3.2 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=169|PDF p.169 ff.]]), neutron interferometry §3.2.3 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=178|PDF p.178]]). 🔵 **Extra · beyond:** SI form of $\Delta B$ ([[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §7.2–§7.3).

> [!intuition] In one picture
> Turn the spin by an angle $\theta$ about an axis and the ket picks up *half* the angle: a full turn gives $-1$.

> [!key] Definition and key results
> $U(\mathbf n,\theta)=e^{-i\theta\,\mathbf n\cdot\mathbf S/\hbar}=\cos\frac\theta2\,\mathbf1-i\sin\frac\theta2\,\mathbf n\cdot\boldsymbol\sigma$; $U(\mathbf n,2\pi)=-\mathbf1$, $U(\mathbf n,4\pi)=\mathbf1$; $U\sigma_iU^\dagger=R_{ij}\sigma_j$ ($R\in SO(3)$): $SU(2)\to SO(3)$ is two-to-one.

Neutron interferometer: one arm in a field, spin rotated by $\varphi=|\gamma_n|B\ell/v$; intensity $\propto1+\cos(\varphi/2)$, maxima $\Delta B=4\pi v/|\gamma_n|\ell$ apart: $7.5$ mT for $\lambda=1.8$ Å, $\ell=2$ cm. $2\pi$ would give half that step. The character $\chi_{1/2}(\theta)=2\cos(\theta/2)$ shows the double cover ([[GT10 Symmetry Representations and Characters]]).

> [!pitfall] Pitfall
> A global sign is unobservable *unless* a rotated beam is compared with an unrotated one, which is what the interferometer does.

Used in: [[QM09 The Stern-Gerlach Experiment and Spin|QM09]] §7.2–§7.3, §12.5. Related: [[Spinor]] · [[Larmor Precession]] · [[Unitary Operator]] · [[Time Evolution Operator]] · [[Quaternion Group]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
