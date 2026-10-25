---
id: ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators
aliases: [PH2113 Tutorial II]
tags: [ph2113, tutorial, harmonic-oscillator, ladder-operators]
trust_tier: agent_written
---

# Tutorial II: ladder operators, ground-state uniqueness, Gaussians (12 October 2026)

## Covered
Given on the sheet:
- $\hat a_\pm=\frac1{\sqrt{2\hbar m\omega}}(m\omega\hat x\mp i\hat p)$ ($\hat a_+$ with minus, $\hat a_-$ with plus, i.e. $\hat a_\mp$ as printed: $\hat a_+=\frac1{\sqrt{2\hbar m\omega}}(m\omega\hat x-i\hat p)$, $\hat a_-=\frac1{\sqrt{2\hbar m\omega}}(m\omega\hat x+i\hat p)$).
- $[\hat a_-,\hat a_+]=1$.
- $\hat H=\hbar\omega(\hat a_+\hat a_-+\tfrac12)=\hbar\omega(\hat a_-\hat a_+-\tfrac12)$.
- Hermitian-conjugate property: $\int f^*(\hat a_\mp g)\,dx=\int(\hat a_\pm f)^*g\,dx$.
- Ground state $\psi_0=(m\omega/\pi\hbar)^{1/4}e^{-m\omega x^2/2\hbar}$; $\psi_n=\frac1{\sqrt{n!}}(\hat a_+)^n\psi_0$.

Problems and what each practises:
1. Prove $\hat H(\hat a_-\psi)=(E-\hbar\omega)(\hat a_-\psi)$: the lowering property from the commutator.
2. Compute $\psi_1,\psi_2$ explicitly with $\hat a_+$ and state the pattern in $\psi_n$ (polynomial times the Gaussian).
3. Sketch $\psi_0,\psi_1,\psi_2$ and densities; infer $\langle x\rangle$ for each from the sketches. Then $\psi=\tfrac1{\sqrt2}(\psi_0+\psi_1)$: not an eigenstate; sketch it and $|\psi|^2$; is $\langle x\rangle$ the same as for $\psi_0$ or $\psi_1$? Explain (practises: cross term and time dependence of $\langle x\rangle$, as in Midsem Q3d).
4. Nodeless ground state is unique: (a) with two independent positive ground states $\psi_1,\psi_2$ and $\phi=\psi_1-c\psi_2$, show $c$ can be chosen so $\phi$ has a node; (b) explain why this contradicts the assumption and conclude non-degeneracy.
5. Gaussian integrals and Fourier transforms: (a) $I=\int e^{-ax^2}dx$ via $I^2$ in polar coordinates; (b) $J=\int e^{-ax^2+bx}dx$ by completing the square; (c) Fourier transform $\tilde f(k)=\frac1{\sqrt{2\pi}}\int f(x)e^{-ikx}dx$ of $f=e^{-x^2/2\sigma^2}$: show it is a Gaussian and relate its width to that of $f$.

No solutions posted.

## From the post
Tutorial problem set for this week.

## Files
- [Tutorial2.pdf](https://drive.google.com/file/d/1l_279phJE-9VrZtauo3OnAM1K0b2cNqV/view?usp=drive_web)

## Related
- [[06-quantum-mechanics/qm05-the-harmonic-oscillator]]: your own oscillator notes
- [[06-quantum-mechanics/concepts/ladder-operators]]: your concept note on $\hat a_\pm$
- [[ph2113/2026-09-13-tutorial-wavefunctions-potentials-schrodinger]]: Gaussian/Fourier primer (Problem 6)
- [[ph2113/2026-10-06-tutorial-i-particle-in-a-box]]: Problem 5 there is a related bounded-energy argument
