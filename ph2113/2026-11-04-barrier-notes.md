---
id: ph2113/2026-11-04-barrier-notes
aliases: [Finite barrier notes, Barrier.pdf]
tags: [ph2113, finite-barrier, tunnelling, scattering]
trust_tier: agent_written
---

# Notes from the finite barrier (2026-11-03)

## Covered
Handwritten lecture notes (Classroom: Barrier.pdf). The text extraction is heavily garbled (OCR on handwriting), so what follows is rebuilt from the legible fragments and the standard result; anything marked (check) should be compared with the PDF. The barrier appears to occupy $-a<x<a$ with height $V_0$ (the sketch shows $-a$ and $+a$; check).

**Classical picture.** A particle thrown from the left ($x\to-\infty$) at a barrier: if $E<V_0$ it is reflected back; if $E>V_0$ it crosses and continues to the right. The notes tackle $E<V_0$ first in quantum mechanics.

**Setup, $E<V_0$ (check labels).**
- Regions I ($x<-a$) and III ($x>a$), $V=0$: $\psi''=-k^2\psi$ with $k=\sqrt{2mE}/\hbar$. Region I: $\psi_I=Ae^{ikx}+Be^{-ikx}$ (incident + reflected). Region III: $\psi_{III}=Fe^{ikx}$ (transmitted only, no wave coming from the right).
- Region II ($-a<x<a$), $V=V_0$: $-\frac{\hbar^2}{2m}\psi''+V_0\psi=E\psi$, i.e. $\psi''=\kappa^2\psi$ with $\kappa=\sqrt{2m(V_0-E)}/\hbar$. Solution $\psi_{II}=Ce^{\kappa x}+De^{-\kappa x}$ (real exponentials: the particle is in a classically forbidden region).
- The amplitude $A$ of the incoming wave is chosen; $B,C,D,F$ follow from matching.

**Matching conditions** (continuity of $\psi$ and $\psi'$, since $V$ has a finite jump).
- At $x=-a$: $Ae^{-ika}+Be^{ika}=Ce^{-\kappa a}+De^{\kappa a}$ and $ik\,(Ae^{-ika}-Be^{ika})=\kappa\,(Ce^{-\kappa a}-De^{\kappa a})$ (the scan shows these as the first two equations; exponent signs reconstructed, check).
- At $x=a$: $Ce^{\kappa a}+De^{-\kappa a}=Fe^{ika}$ (eq. 3 in the scan) and $\kappa\,(Ce^{\kappa a}-De^{-\kappa a})=ik\,Fe^{ika}$ (eq. 4).
- The notes solve eqs. 3-4 for $C$ and $D$ in terms of $F$: $C=\frac12\big(1+\frac{ik}{\kappa}\big)Fe^{ika-\kappa a}$ and $D=\frac12\big(1-\frac{ik}{\kappa}\big)Fe^{ika+\kappa a}$ (check; the scan has $(\kappa\pm ik)Fe^{ika}$ terms). Substituting into the $x=-a$ equations gives $A$ and $B$ in terms of $F$; the scan then introduces combinations of the form $(1\mp\frac{ik}{\kappa})$, $\big(\frac{\kappa}{k}\mp\frac{k}{\kappa}\big)$ and hyperbolic functions to simplify $B/F$ and $A/F$.
- Result visible in the scan: $B$ is proportional to $\sinh(2\kappa a)$ times $(k^2+\kappa^2)/(2k\kappa)$ (reflected amplitude, check), and the transmission coefficient is
$$T=\frac{|F|^2}{|A|^2}=\left[1+\frac{V_0^2\,\sinh^2(2\kappa a)}{4E\,(V_0-E)}\right]^{-1}\quad(\text{check against the PDF}).$$
  Consistency check (derived, not from the post): this is the finite-well formula of [[ph2113/2026-10-27-finite-well-notes]], $T=\big[1+\frac{V_0^2}{4E(E-V_0)}\sin^2(2k_0a)\big]^{-1}$, with $k_0\to i\kappa$, since $\sin^2(i y)=-\sinh^2 y$ and $E-V_0<0$. Also $R=|B/A|^2=1-T$.

**Tunnelling.** $T\neq0$ even for $E<V_0$: the particle can cross a classically forbidden region. The scan's closing remark: tunnelling is a quantum phenomenon where a particle can cross into/over a classically forbidden range. The notes also record $\sinh x = (e^x-e^{-x})/2$ at the end.

**Limit (derived, not in the scan; check).** For a thick or high barrier, $\kappa a\gg1$: $\sinh(2\kappa a)\approx\frac12e^{2\kappa a}$, so $T\approx\frac{16E(V_0-E)}{V_0^2}e^{-4\kappa a}$, exponentially small in the barrier width $2a$ and in $\kappa$.

## From the post
Notes from the finite barrier.

## Files
- [Barrier.pdf](https://drive.google.com/file/d/1lVuWe8NfECjzdjNj7e4EOmMgGlkBUv1f/view?usp=drive_web): handwritten; the OCR is garbled (Korean/CJK characters in place of symbols), so the derivation above is partly reconstructed and the final $T$ formula is not legible in full. Post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODk3MzAxNjc4MzM0

## Related
- [[ph2113/2026-10-27-finite-well-notes]]: same method (plane waves outside, matching $\psi,\psi'$ at $\pm a$); the barrier is the well with $E<V_0$ inside the region
- [[ph2113/2026-11-02-tutorial-v-finite-well-double-well-transmission]]: Problem 3 derives $F/A$ and $T$ for $E>V_0$; the double well also uses a barrier between wells
- [[ph2113/2026-10-26-tutorial-iv-finite-well-practice]]: decay constant outside a well, the same $\kappa$ as inside this barrier
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: why $\psi$ and $\psi'$ are continuous at a finite jump in $V$
- [[ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties]]: free-particle waves $e^{\pm ikx}$ and their direction of motion
- [[zettel/finite-well-scattering-states]]: concept note on scattering states of the finite well
