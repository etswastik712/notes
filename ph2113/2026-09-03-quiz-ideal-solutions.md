---
id: ph2113/2026-09-03-quiz-ideal-solutions
aliases: [PH2113 quiz solutions]
tags: [ph2113, quiz, solutions]
trust_tier: agent_written
---

# PH2113 Quiz: ideal solutions and marking guide (15 marks)

## Covered
Solutions to the quiz held 2026-09-03 (Classroom: PH2113_Quiz_Ideal_Solutions.pdf). Equivalent explanations that make the same physics clear get credit. The question texts are not in the file, so each item is inferred from its solution.

**Q1 Photoelectric effect (2).** Classically, energy is tied to intensity, so intense enough light should eject electrons at any frequency; the observed threshold frequency contradicts this [1]. Photon picture: $E_\gamma=h\nu$; an electron is emitted only if a single photon supplies at least the work function. Intensity at fixed frequency changes the photon number, not the energy per photon; below threshold no photon suffices, above it even weak light ejects electrons [1].

**Q2 Compton scattering as a collision (4).**
- (a) $E_\gamma=hc/\lambda$: longer wavelength means lower photon energy; energy lost goes to the electron's kinetic energy [1].
- (b) A photon's momentum changes (direction, and magnitude after collision); total momentum is conserved, so the electron gets the recoil momentum [1].
- (c) Nearly backward scattering reverses the photon's direction, the largest change of its momentum vector, so the electron gets the larger recoil and energy; the photon emerges with lower energy and the largest wavelength increase [2].

**Q3 Same position density, not the same state (2).** $|\psi_1|^2=|\psi_2|^2$ shows only equal position distributions, not identical states [1]. The factor $e^{ikx}$ in $\psi_2$ is a position-dependent phase, unlike a constant phase, and carries momentum information: $\hat p\psi_2=-i\hbar\frac{d}{dx}(e^{ikx}\psi_1)=e^{ikx}(\hat p\psi_1+\hbar k\psi_1)$ [1].

**Q4 Particle on a ring (4).**
- (a) After one full trip the particle is at the same point, so $\psi$ must return with the same value and phase [1]; a whole number of wavelengths fits, $L=n\lambda$, $n\in\mathbb Z$, so arbitrary wavelengths are not allowed [1].
- (b) Clockwise and anticlockwise waves have opposite momenta: different states [1]. Same $|p|$ and $K=p^2/2m$ independent of the sign of $p$: same kinetic energy [1].

**Q5 Operators, eigenstates, superpositions (3).**
- (a) $\hat p=-i\hbar\,d/dx$: $\hat p\,e^{ikx}=\hbar k\,e^{ikx}$, eigenstate with eigenvalue $\hbar k$ [0.5]. $\psi_2=\cos kx=\frac12(e^{ikx}+e^{-ikx})$, $\hat p\psi_2=\frac{\hbar k}{2}(e^{ikx}-e^{-ikx})$, not proportional, so not a momentum eigenstate [0.5].
- (b) With $\hat Au_\pm=\pm u_\pm$ and $v=\frac1{\sqrt2}(u_++u_-)$: $\hat Av=\frac1{\sqrt2}(u_+-u_-)=\frac1{\sqrt2}(1,-1)^T$ [0.5], not a constant times $v=\frac1{\sqrt2}(1,1)^T$, so $v$ is not an eigenvector [0.5]. In a superposition of eigenstates with different eigenvalues the components are multiplied by different numbers, changing the relative coefficients [1]; same as $e^{ikx}$ (eigenstate) vs $\cos kx$ (contains $\pm\hbar k$, the operator changes their relative sign).

## From the post
solution for todays quiz.

## Files
- [PH2113_Quiz_Ideal_Solutions.pdf](https://drive.google.com/file/d/1Sr-Ni47Xfstfz6W1ysjQF7dvOhLekVZd/view?usp=drive_web)

Posted: [Classroom](https://classroom.google.com/c/ODcxNjgzODU4NzU5/p/ODc3Mjg2MzQxMTY0)

## Related
- [[ph2113/2026-09-02-mock-quiz-and-solutions]]: the mock paper in the same format
- [[06-quantum-mechanics/concepts/particle-on-a-ring]]: Q4
- [[06-quantum-mechanics/concepts/compton-scattering]]: Q2
- [[06-quantum-mechanics/qm03-states-operators-and-measurement]]: Q3 and Q5
