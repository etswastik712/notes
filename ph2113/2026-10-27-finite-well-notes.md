---
id: ph2113/2026-10-27-finite-well-notes
aliases: [Finite well notes]
tags: [ph2113, finite-well, scattering]
trust_tier: agent_written
---

# Notes for the finite well system (2026-10-27)

## Covered
Handwritten lecture notes (scan with heavy OCR damage: reconstructed below from the legible parts and standard results; formulas marked (check) are inferred, so compare with the PDF). Well $-a\le x\le a$, potential $V_0$ outside (Classroom: Finite_well.pdf).

**Bound states, $E<V_0$.**
- TISE inside: $\psi''=-k_0^2\psi$, $k_0=\sqrt{2mE}/\hbar$; outside: $\psi''=\kappa^2\psi$, $\kappa=\sqrt{2m(V_0-E)}/\hbar$ (called $k$ in Tutorial IV). Outside solutions must decay: $Ae^{\kappa x}$ for $x<-a$, $Be^{-\kappa x}$ for $x>a$.
- Symmetric $V$ gives wavefunctions that are either symmetric ($\psi(-x)=\psi(x)$) or antisymmetric ($\psi(-x)=-\psi(x)$); solve the even and odd cases separately.
- Even: inside $G\cos k_0x$. Match $\psi$ and $\psi'$ at $x=a$: $G\cos k_0a=Be^{-\kappa a}$ and $-k_0G\sin k_0a=-\kappa Be^{-\kappa a}$. Dividing: $\tan(k_0a)=\kappa/k_0$, the quantisation condition.
- Odd: inside $F\sin k_0x$. Matching at $x=a$: $F\sin k_0a=Be^{-\kappa a}$, $k_0F\cos k_0a=-\kappa Be^{-\kappa a}$, so $\cot(k_0a)=-\kappa/k_0$ (check).
- With $z_0^2=2mV_0a^2/\hbar^2$: $\kappa^2+k_0^2=2mV_0/\hbar^2$ ties the two sides together; solve graphically.
- Deep, wide well ($2mV_0a^2/\hbar^2\gg1$): many bound states; for the lowest, $\kappa_n/k_0\gg1$ so $k_na\approx n\pi/2$ and $E_n\approx n^2\pi^2\hbar^2/(8ma^2)$ (infinite box of width $2a$), always slightly lower than the box value because the wavefunction leaks into the walls.
- Shallow/narrow well: only a small number of bound states. There is always an even (ground) bound state; there may be no odd one.

**Scattering states, $E>V_0$ (classically free in regions I and III).**
- Regions I, III: $\psi=Ae^{ikx}+Be^{-ikx}$ (incident + reflected) for $x<-a$, and $Fe^{ikx}$ for $x>a$ (transmitted only); inside $Ce^{ik_0x}+De^{-ik_0x}$.
- Impose continuity of $\psi$ and $\psi'$ at $x=-a$ and $x=a$. The amplitude $A$ of the incoming wave is under our control, so express $B,C,D,F$ in terms of $A$.
- Matching at $x=a$ gives $C$ and $D$ in terms of $F$ (e.g. $2k_0Ce^{ik_0a}=(k_0+k)Fe^{ika}$); matching at $x=-a$ then gives $A$ in terms of $F$.
- Transmission probability $T=|F/A|^2$, reflection $R=|B/A|^2$, $T+R=1$. Result (check):
$$T=\left[1+\frac{(k^2-k_0^2)^2}{4k^2k_0^2}\sin^2(2k_0a)\right]^{-1}.$$
- Perfect transmission ($T=1$) when $\sin(2k_0a)=0$, i.e. $2k_0a=n\pi$, $k_0=n\pi/2a$, giving $E=n^2\pi^2\hbar^2/(2m(2a)^2)$ measured from the well bottom: resonances where the well width is a whole number of half-wavelengths.
- Interpretation: this is a scattering experiment, probing the potential.

## From the post
Notes for the finite well system.

## Files
- [Finite_well.pdf](https://drive.google.com/file/d/1cE24B3ZXQgCyIrUIHUKhWl4X37glWd_9/view?usp=drive_web): handwritten; text extraction garbled, so the summary above is partly reconstructed (see "check" marks). Post: https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODk2MDE5Mzk2MzQ2

## Related
- [[ph2113/2026-10-26-tutorial-iv-finite-well-practice]]: practice question on the even-state condition
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: infinite well, the deep-well limit
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: continuity of $\psi,\psi'$ at a finite jump in $V$
- [[ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties]]: free-particle waves $e^{\pm ikx}$ and their direction of motion

<!-- kurooto:material62580c63 -->
## Concepts in Finite_well
[[zettel/deep-wide-well-approximation]], [[zettel/shallow-well-bound-state-existence]], [[zettel/finite-well-scattering-states]]
<!-- /kurooto:material62580c63 -->
