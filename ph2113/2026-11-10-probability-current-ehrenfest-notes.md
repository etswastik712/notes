---
id: ph2113/2026-11-10-probability-current-ehrenfest-notes
aliases: [Probability current and Ehrenfest theorem notes]
tags: [ph2113, lecture-notes, ehrenfest, probability-current]
trust_tier: agent_written
---

# Notes for probability current and Ehrenfest Theorem

## Covered
Source: Ehrenfest.pdf (Classroom, 2026-11-10). It is a handwritten scan and the text extraction is badly garbled. What follows is the structure that is legible in the scan (section titles and the phrases "Terms proportional to V cancel", "Local conservation of probability", "First theorem", "using integration by parts", "For quadratic potentials", "second law", "special cases"), with the algebra filled in by standard steps. The intermediate lines are reconstructed, not read directly; compare with the PDF.

**1. Probability current and local conservation of probability.** Start from $\rho=\Psi^*\Psi$ and the TDSE $i\hbar\,\partial_t\Psi=-\frac{\hbar^2}{2m}\Psi''+V\Psi$ with real $V(x)$, together with its complex conjugate:
$$\partial_t\Psi=\frac{i\hbar}{2m}\Psi''-\frac{i}{\hbar}V\Psi,\qquad \partial_t\Psi^*=-\frac{i\hbar}{2m}\Psi^{*\prime\prime}+\frac{i}{\hbar}V\Psi^*.$$
Then $\partial_t\rho=\Psi^*\partial_t\Psi+\Psi\,\partial_t\Psi^*$. The terms proportional to $V$ cancel (scan: "Terms proportional to V cancel"), leaving
$$\partial_t\rho=\frac{i\hbar}{2m}\big(\Psi^*\Psi''-\Psi\Psi^{*\prime\prime}\big)=\frac{i\hbar}{2m}\,\partial_x\big(\Psi^*\Psi'-\Psi\Psi^{*\prime}\big)=-\partial_x j,$$
$$j=\frac{\hbar}{2mi}\big(\Psi^*\Psi'-\Psi\Psi^{*\prime}\big),\qquad \partial_t\rho+\partial_xj=0.$$
This is the local conservation of probability (continuity equation). It holds only for real $V$; a complex potential adds a non-cancelling term (see [[ph2113/2026-09-24-midsem-solutions]]).

**2. Ehrenfest's theorem, first equation.** For the mean position $\langle x\rangle=\int x\,\rho\,dx$:
$$\frac{d\langle x\rangle}{dt}=\int x\,\partial_t\rho\,dx=-\int x\,\partial_xj\,dx=\int j\,dx=\frac1m\int\Psi^*\Big(-i\hbar\frac{\partial}{\partial x}\Big)\Psi\,dx=\frac{\langle p\rangle}{m}.$$
Step used: integration by parts, with the boundary term vanishing because $\Psi$ and $j$ go to zero at $\pm\infty$ (scan: "using integration by parts"). The scan itself appears to expand $\partial_t\Psi$ and $\partial_t\Psi^*$ directly inside $\int\Psi^*x\Psi$; the terms proportional to $V$ cancel again and two kinetic terms remain, which integration by parts turns into $\langle p\rangle/m$ (reconstructed).

**3. Ehrenfest's theorem, second equation.**
$$\frac{d\langle p\rangle}{dt}=-\Big\langle\frac{dV}{dx}\Big\rangle.$$
Derivation pattern (as in [[ph2113/2026-11-09-tutorial-vi-ehrenfest-barrier-above]]): differentiate $\int\Psi^*(-i\hbar\partial_x)\Psi\,dx$ in time, insert the TDSE and its conjugate, the kinetic terms form a total derivative that vanishes at infinity, and the potential terms give $-\int V'|\Psi|^2dx$.

**4. Consequences.**
- For quadratic potentials $V'(x)$ is linear in $x$, so $\langle V'(x)\rangle=V'(\langle x\rangle)$ and the mean obeys Newton's law exactly: $m\,\frac{d^2\langle x\rangle}{dt^2}=-V'(\langle x\rangle)$. For $V=kx^2/2$: $m\ddot{\langle x\rangle}=-k\langle x\rangle$.
- In general $\langle V'(x)\rangle\neq V'(\langle x\rangle)$, so the mean position does not follow the classical trajectory (the scan's closing lines on "special cases" appear to say this; garbled, check).

## From the post
Notes for probability current and Ehrenfest Theorem.

## Files
- [Ehrenfest.pdf](https://drive.google.com/file/d/1CM--feqfCJOGM7lzWKIRrfSpS5CmsRnq/view?usp=drive_web): read, but the handwriting extracted poorly, so the derivation above is partly reconstructed.

## Related
- [[ph2113/2026-11-09-tutorial-vi-ehrenfest-barrier-above]]: Problem 1 is the second Ehrenfest equation derived from the TDSE.
- [[ph2113/2026-08-20-lecture-6-7-fourier-synthesis-to-schrodinger]]: first appearance of the probability current.
- [[ph2113/2026-08-27-tutorial-solutions-wavefunctions-uncertainty-schrodinger]]: probability-conservation proof (problem 4).
- [[ph2113/2026-09-24-midsem-solutions]]: free-particle current, complex potential and non-conservation.
- [[ph2113/2026-10-19-harmonic-oscillator-ladder-operator-notes]]: the quadratic-potential case where the Ehrenfest equations are exact.
