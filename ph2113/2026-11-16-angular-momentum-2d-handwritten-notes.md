---
id: ph2113/2026-11-16-angular-momentum-2d-handwritten-notes
aliases: [2-dimensional systems and intro to angular momentum]
tags: [ph2113, lecture-notes]
trust_tier: agent_written
---

# 2-dimensional systems and intro to angular momentum (handwritten notes)

## Covered
Source: handwritten lecture scan (Classroom: Angular_momentum.pdf, second file). The text extraction is badly garbled, so only the outline below was legible; formulas marked "reconstructed" are standard results filled in, not read directly. Compare with the PDF.

- **Canonical commutators generalise to 2-d:** $[x,p_x]=i\hbar$, $[y,p_y]=i\hbar$; mixed pairs such as $[x,p_y]$ commute (reconstructed; the scan has the pairs but the zeros are unreadable). The reason given is that $x$ and $y$ are independent coordinates.
- **TISE in 2-d:** $\Big[-\frac{\hbar^2}{2m}\Big(\partial_x^2+\partial_y^2\Big)+V(x,y)\Big]\psi(x,y)=E\psi(x,y)$.
- **Circular symmetry:** if $V$ depends only on the distance from the centre, $V(x,y)=V(\sqrt{x^2+y^2})=V(r)$, it is easier to work in polar coordinates $r=\sqrt{x^2+y^2}$, $\theta=\tan^{-1}(y/x)$; the page then does the chain-rule derivatives $\partial_x,\partial_y$ in terms of $\partial_r,\partial_\theta$ with $\cos\theta$, $\sin\theta$.
- **After transformation:** $-\frac{\hbar^2}{2m}\Big[\partial_r^2+\frac1r\partial_r+\frac1{r^2}\partial_\theta^2\Big]\psi+V(r)\psi=E\psi$.
- **Angular momentum:** classically $\mathbf L=\mathbf r\times\mathbf p$, so $L_z=xp_y-yp_x$; quantum mechanically $\hat L_z=x\hat p_y-y\hat p_x$, which in polar coordinates is $-i\hbar\,\partial_\theta$ (reconstructed).
- **Commutation:** since $V$ depends only on $r$, $[\hat H,\hat L_z]=0$. If two operators commute, one can find simultaneous eigenfunctions of both. So the eigenfunctions of $\hat H$ can be chosen to be angular momentum eigenfunctions.
- **Eigenfunctions:** $\hat L_z\psi=\lambda\psi$ gives $\psi(r,\theta)=R(r)e^{il\theta}$ (the scan has $\hat L_z\psi_l=\hbar l\,\psi_l$ with $\Theta=e^{il\theta}$).
- **Single-valuedness:** $\theta\to\theta+2\pi$ must leave the wavefunction unchanged, so $l=0,\pm1,\pm2,\dots$.
- **Radial equation** after substituting $R(r)e^{il\theta}$: $\Big[-\frac{\hbar^2}{2m}\Big(\frac{d^2}{dr^2}+\frac1r\frac d{dr}-\frac{l^2}{r^2}\Big)+V(r)\Big]R=ER$; this has to be solved for the energy eigenvalues and eigenfunctions.
- **Degeneracy:** $l$ and $-l$ enter only through $l^2$, so they have the same energy irrespective of the details of $V(r)$.

## From the post
Notes and python notebook for this week and last.

## Files
- [Angular_momentum.pdf (handwritten notes)](https://drive.google.com/file/d/14tXjuZCFyhXP6WvffgR3haux6OZVsgqp/view?usp=drive_web): read, but the scan is largely unreadable in the text extraction.

## Related
- [[ph2113/2026-11-16-tutorial-vii-polar-schrodinger-2d-oscillator]]: Problem 1 asks for exactly this polar-coordinate derivation
- [[ph2113/2026-11-16-circular-well-2d-and-density-notebook]]: this setup applied to the circular infinite well
- [[ph2113/2026-11-16-hydrogen-atom-3d-notes]]: the 3-d generalisation ($\hat L^2$, $\hat L_z$)
- [[ph2113/2026-08-25-lecture-9-free-particle-ring-general-properties]]: the ring, where single-valuedness first gave integer quantum numbers
- [[ph2113/2026-08-31-states-operators-measurements-notes]]: commuting operators and common eigenstates
- [[06-quantum-mechanics/concepts/angular-momentum-algebra]]: their own concept note on angular momentum
