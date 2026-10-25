---
id: ph2113/2026-08-04-lectures-1-2-double-slit-and-compton
aliases: [PH2113 Lectures 1-2, Double-slit puzzle, Compton scattering lecture 2]
tags: [ph2113, lecture, double-slit, photoelectric, compton]
trust_tier: agent_written
---

# Lectures 1-2: the double-slit puzzle and Compton scattering (2026-08-04)

## Covered

### Lecture 1: the double-slit puzzle
Four facts (Classroom: PH2113_Lecture1.pdf): (1) an individual quantum detection is localised; (2) many repeated detections reveal a probability distribution; (3) with two slits open the distribution contains interference and is not the sum of the single-slit distributions; (4) quantum theory combines probability amplitudes first and gets probabilities afterwards.

**Classical particles.** Same flux and exposure in all runs. If every projectile takes exactly one of two independent routes, the expected count densities add:
$$R_{AB}(x)=R_A(x)+R_B(x).$$
Count densities are used because two separately normalised probability densities do not simply add without weights. Opening a second slit may add detections but cannot create a position where the count falls: counts have no phase and no negative cross term.

**Classical waves.** Complex amplitudes add first, then square:
$$u_{AB}=u_A+u_B,\qquad I_{AB}=|u_A+u_B|^2=I_A+I_B+2\sqrt{I_AI_B}\cos\delta,$$
with $\delta$ the relative phase at the point on the screen. $\delta=0$: constructive; $\delta=\pi$: destructive (equal amplitudes cancel completely). Example: $I_A=I_B=I_0$ gives $I_{AB}=4I_0$ at $\delta=0$ and $0$ at $\delta=\pi$. The cross term is the entire origin of interference.

**Electrons one at a time.** Emission rate so low that the mean number of electrons in the apparatus is far below one, which rules out electron-electron collisions as the source. Each electron gives one localised dot; no single dot shows fringes; the histogram of many dots approaches an interference pattern. With amplitudes $\psi_A,\psi_B$:
$$p_{AB}(x)=|\psi_A+\psi_B|^2,\quad p_A=|\psi_A|^2,\quad p_B=|\psi_B|^2,\quad p_{AB}\ne p_A+p_B.$$
It rules out the model where each electron has a definite slit history and histories are mixed with ordinary probabilities. Careful language: do not conclude that the electron is a tiny classical wave or splits in two; the safe conclusion is that the classical exclusive-path description is inadequate and alternatives combine at the amplitude level.

**Which-path information.** If the path is physically recorded (even in principle) the alternatives are distinguishable and interference is reduced or lost. Rule: indistinguishable alternatives, add amplitudes; distinguishable alternatives, add probabilities for the distinct final records. The cause is the physical correlation with a detector or environment, not a human looking. Optional precise form with detector states $|D_A\rangle,|D_B\rangle$:
$$p(x)=|\psi_A|^2+|\psi_B|^2+2\,\mathrm{Re}\big[\psi_A^*\psi_B\langle D_A|D_B\rangle\big].$$
Identical detector states: full interference; orthogonal path records: none.

"With what does a lone electron interfere?" The amplitudes associated with the indistinguishable alternatives interfere.

**Photoelectric effect (the mirror clue).** Weak-field, one-photon regime, frequency $\nu$ on a metal:
- Increasing intensity at fixed $\nu$: more electrons, same maximum kinetic energy.
- Below a threshold frequency $\nu_0$: no ordinary one-photon emission.
- Very weak light: emission stays prompt, just rarer.

Einstein: $E_\gamma=h\nu$; with work function $\Phi$,
$$K_{\max}=h\nu-\Phi,\qquad \nu_0=\Phi/h.$$
Intensity sets the photon arrival rate and so the current; frequency sets $K_{\max}$. At extreme intensities multiphoton processes can occur, so the formula is for the one-photon regime.

**Putting it together.** Quantum systems are not particles on some occasions and waves on others; "particle" and "wave" each capture one visible aspect of a theory whose basic object is a state or amplitude. QM must supply: a quantity that superposes and carries relative phase; a rule turning it into probabilities; localised outcomes at measurement; one description for light and matter. Minimal preview: add amplitudes, take $|\cdot|^2$, predict probabilities. Cross term: $|\psi_A+\psi_B|^2=|\psi_A|^2+|\psi_B|^2+2\mathrm{Re}(\psi_A^*\psi_B)$.

Precise-language list from the note: avoid "the electron definitely travelled through both slits", "observation by a conscious person destroys interference", "the electron is just a wave", "two normalised probabilities simply add"; say instead that the classical exclusive-path model does not describe the unmeasured experiment, that a physical path record makes alternatives distinguishable, that amplitudes superpose while detections are localised, and that count densities from exclusive routes add under fixed exposure.

### Lecture 2: Compton scattering
Setup (Classroom: PH2113_Lecture2.pdf): near-monochromatic X-rays on a target; scattered wavelength measured versus angle $\theta$; electron treated as initially free and at rest when the photon energy far exceeds its binding energy.

Observations: a shifted component with $\lambda'>\lambda$; shift depends on $\theta$, zero forward, largest backward; recoil electron carries kinetic energy; real spectra may also have an unshifted component (coherent scattering from tightly bound electrons or the whole atom).

Shift law:
$$\Delta\lambda=\lambda'-\lambda=\frac{h}{m_ec}(1-\cos\theta)=\lambda_C(1-\cos\theta),\qquad \lambda_C=\frac{h}{m_ec}=2.426\ \text{pm},$$
independent of incident intensity, $0\le\Delta\lambda\le2\lambda_C$.

| $\theta$ | $1-\cos\theta$ | $\Delta\lambda$ (pm) |
|---|---|---|
| 0° | 0 | 0 |
| 45° | 0.293 | 0.711 |
| 90° | 1 | 2.426 |
| 135° | 1.707 | 4.141 |
| 180° | 2 | 4.852 |

Worked example: $\lambda=71$ pm, $\theta=90^\circ$: $\lambda'=73.426$ pm, $E_\gamma=17.46$ keV, $E'_\gamma=16.89$ keV, $K_e\simeq0.58$ keV.

Energy: $\lambda'>\lambda\Rightarrow E'_\gamma<E_\gamma$. With $E_\gamma+m_ec^2=E'_\gamma+E_e$, $E_e=m_ec^2+K_e$:
$$K_e=E_\gamma-E'_\gamma=hc\Big(\frac1\lambda-\frac1{\lambda'}\Big).$$
Energy is a scalar and cannot fix directions, so momentum conservation is needed. Photon momentum $p_\gamma=E_\gamma/c=h\nu/c=h/\lambda$; vector conservation $\mathbf p_\gamma=\mathbf p'_\gamma+\mathbf p_e$ gives (momentum triangle) $p_e^2=p_\gamma^2+p'^2_\gamma-2p_\gamma p'_\gamma\cos\theta$. Small $\theta$: little momentum transferred; $\theta=180^\circ$: largest transfer. The recoil electron obeys $E_e^2=p_e^2c^2+m_e^2c^4$.

Conservation applies to the whole isolated system; for a bound electron the atom or lattice carries energy and momentum and must be included. Energy conservation reflects uniformity of time, momentum conservation uniformity of space.

**Thomson vs Compton.** Thomson (classical driven oscillation, $h\nu\ll m_ec^2$, recoil negligible): $\nu'=\nu$, $\lambda'=\lambda$; describes angular distribution and polarisation of low-energy scattering, a correct limit. Compton: relativistic photon-electron collision, $\Delta\lambda=\lambda_C(1-\cos\theta)$, plus correlated recoil energy. Correction in the note: it is wrong to say a classical EM wave has no momentum (radiation pressure exists); what classical theory misses is the discrete transfer with $E=h\nu$, $p=h/\lambda$. The photon is not a tiny billiard ball: diffraction and interference remain.

Summary relations: $\lambda'-\lambda=\frac h{m_ec}(1-\cos\theta)$; $E_\gamma=h\nu=hc/\lambda$; $p_\gamma=E_\gamma/c=h/\lambda$; $K_e=E_\gamma-E'_\gamma$; $\mathbf p_\gamma=\mathbf p'_\gamma+\mathbf p_e$.

## From the post
"Please find attached lecture note for first 2 lectures. Thursday we'll have lecture. Tutorial will start next week."

## Files
- [PH2113_Lecture1.pdf](https://drive.google.com/file/d/1T0uNCLLACYZac79yDmp6hemKHgUHeC0b/view?usp=drive_web)
- [PH2113_Lecture2.pdf](https://drive.google.com/file/d/1MSiqs1ytH4d2eOJmX7msmiVjlYNVUS8H/view?usp=drive_web)

Small numeric inconsistency between the lecture notes: Lecture 2 tabulates 4.852 pm at 180° and 4.141 pm at 135°, Lecture 3 gives 4.853 and 4.142 (rounding of $\lambda_C$).

## Related
- [[ph2113/2026-08-06-lecture-3-compton-scattering]]: Lecture 3 repeats Compton with the full derivation
- [[ph2113/2026-08-11-problem-set-1]]: problems on exactly this material
- [[ph2113/2026-09-03-quiz-ideal-solutions]]: quiz asking photoelectric and Compton in words
- [[ph2113/2026-09-10-tutorial-solutions-states-interference-uncertainty]]: later double-slit intensity and fringe spacing
