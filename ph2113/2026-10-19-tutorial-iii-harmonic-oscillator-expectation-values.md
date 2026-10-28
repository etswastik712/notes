---
id: ph2113/2026-10-19-tutorial-iii-harmonic-oscillator-expectation-values
aliases: ["Tutorial III: harmonic oscillator expectation values and orthogonality (19 October 2026)"]
tags: []
trust_tier: agent_written
---

# Tutorial III: harmonic oscillator expectation values and orthogonality (19 October 2026)

## Covered
Given on the sheet (Classroom: Tutorial3.pdf), with $\hat a_\pm$ as in [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]]:
- $\hat a_+=\frac1{\sqrt{2\hbar m\omega}}(m\omega\hat x-i\hat p)$, $\hat a_-=\frac1{\sqrt{2\hbar m\omega}}(m\omega\hat x+i\hat p)$, $[\hat a_-,\hat a_+]=1$.
- $\hat H=\hbar\omega\hat a_+\hat a_-+\frac{\hbar\omega}2=\hbar\omega\hat a_-\hat a_+-\frac{\hbar\omega}2$.
- $\hat x=\sqrt{\frac{\hbar}{2m\omega}}(\hat a_++\hat a_-)$, $\hat p=i\sqrt{\frac{\hbar m\omega}{2}}(\hat a_+-\hat a_-)$.
- Hint given: $\hat a_+\psi_n=\sqrt{n+1}\,\psi_{n+1}$, $\hat a_-\psi_n=\sqrt n\,\psi_{n-1}$.
- Ground state $\psi_0(x)=\left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar}$.

Problems and what each practises:
1. $\langle\hat p^2\rangle$ in an arbitrary eigenstate $\psi_n$: write $\hat p^2=-\frac{\hbar m\omega}{2}(\hat a_+-\hat a_-)^2$, expand, and use the raising/lowering action and orthonormality (only the $\hat a_+\hat a_-$ and $\hat a_-\hat a_+$ terms survive, since $\hat a_\pm^2\psi_n\propto\psi_{n\pm2}$). Practises: expectation values by ladder operators, the same pattern as the end of the handwritten oscillator notes ([[ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes]]). Working it through gives $\langle\hat p^2\rangle=\hbar m\omega\,(n+\tfrac12)$ (my derivation, consistent with $\langle \hat a_+\hat a_-\rangle=n$, $\langle \hat a_-\hat a_+\rangle=n+1$).
2. $\langle x\rangle=\int\psi_0^*x\psi_0\,dx$ by the explicit Gaussian integral, then what goes wrong for $\langle x^2\rangle$ by the same method. Practises: parity/odd integrand ($\langle x\rangle=0$), and $\int x^2e^{-ax^2}dx$ by integration by parts or by differentiating the standard Gaussian integral with respect to $a$ (the sheet's suggestions: integration by parts, or rewriting as a standard Gaussian integral). Link: Gaussian integrals in [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]] Problem 5.
3. Orthogonality of eigenfunctions with $E_n\ne E_m$: $\int_{-\infty}^{\infty}\psi_m^*\psi_n\,dx=0$. Sheet's hints: start from $\hat H\psi_n=E_n\psi_n$ and $\hat H\psi_m=E_m\psi_m$; multiply the first by $\psi_m^*$ and integrate; take the complex conjugate of the second, multiply by $\psi_n$, integrate. Practises: Hermiticity of $\hat H$ (the two integrals $\int\psi_m^*\hat H\psi_n$ and $\int(\hat H\psi_m)^*\psi_n$ agree) gives $(E_n-E_m)\int\psi_m^*\psi_n=0$, hence the integral vanishes for $E_n\neq E_m$.

No solutions posted.

## From the post
Problem set for Tutorial 3.

## Files
- [Tutorial3.pdf](https://drive.google.com/file/d/1cdyv4CPTTd5dU5zizGKDgu5MFH0TijvL/view?usp=drive_web)

## Related
- [[ph2113/2026-10-12-tutorial-ii-harmonic-oscillator-ladder-operators]]: same operators and conventions, previous sheet
- [[ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes]]: lecture notes with the ladder-operator results used here
- [[ph2113/2026-10-06-particle-in-a-box-notes]]: orthogonality of box eigenfunctions
- [[06-quantum-mechanics/qm05-the-harmonic-oscillator]]: your own oscillator notes
- [[06-quantum-mechanics/concepts/ladder-operators]]: your concept note on $\hat a_\pm$
- [[06-quantum-mechanics/concepts/oscillator-expectation-values]]: your note on $\langle x^2\rangle$, $\langle p^2\rangle$
- [[06-quantum-mechanics/concepts/orthonormality-of-eigenfunctions]]: your note on the orthogonality proof
- [[06-quantum-mechanics/concepts/hermitian-operator]]: why the proof in Problem 3 works

<!-- kurooto:material8c36e347 -->
## Concepts in Tutorial3
[[zettel/orthogonality-of-energy-eigenstates]]
<!-- /kurooto:material8c36e347 -->

<!-- kurooto:materiala471099d -->
## Concepts in Harmonic_oscillator
(none new)
<!-- /kurooto:materiala471099d -->
