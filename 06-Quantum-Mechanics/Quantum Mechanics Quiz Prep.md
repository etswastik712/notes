---
title: Quantum Mechanics Quiz Prep
aliases: [QM quiz prep, PH2113 quiz, PH2113 exam prep, QM formula sheet and traps]
subject: qm
type: moc
scope: [taught, extra-beyond]
by: [lecture-notes]
status: draft
tags: [subject/qm, type/moc, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# Quantum Mechanics Quiz Prep

◀ [[Quantum Mechanics - Course Map|Course Map]] · chapters [[QM01 From Waves to Probabilities|QM01]] · [[QM02 The Schrodinger Equation and Stationary States|QM02]] · [[QM03 States Operators and Measurement|QM03]] · [[QM04 The Particle in a Box|QM04]] · [[QM05 The Harmonic Oscillator|QM05]] · [[QM06 The Oscillator Toolbox|QM06]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!warning] What this page is built from
> The **mock quiz** (posted 2 Sep 2026) and the **actual quiz** held **3 Sep 2026, 10:00–11:00, 15 marks** exist in the folder only as summaries of two Google Classroom posts made by another tool: [[2026-09-02-mock-quiz-and-solutions]] and [[2026-09-03-quiz-ideal-solutions]] (`trust_tier: agent_written`; the PDFs `PH2113_Mock_Quiz_50min_15marks.pdf`, `PH2113_Mock_Quiz_Ideal_Solutions.pdf` and `PH2113_Quiz_Ideal_Solutions.pdf` are **not** in `physics/quantum-mechanics/`). **The question texts of the 3 Sep quiz are not available**, only its ideal solutions, so each item is reconstructed from its solution. I re-derived every solution below from my chapters and recomputed every number (`scripts/qm_numbers.py`, section "QM quiz prep"). The instructor's style: **explanations are expected, not bare formulas**; equivalent explanations that make the same physics clear get credit. No assessment after 3 Sep is announced ([[ph2113/exam-prep|exam-prep]] lists this as a gap).

> [!syllabus] Syllabus map
> 🟢 **Taught / examined so far:** the photoelectric effect and the Compton collision as *explanations*, acceptable wavefunctions, global versus relative phase, momentum and parity eigenstates, the ring, superpositions and time dependence, a $2\times2$ operator, the commutator. 🔵 **Extra · beyond:** numerical versions, the oscillator material (QM05–QM06) which was **not** in the 3 Sep quiz.

## 1. Formula sheet (what the two quizzes used)
> [!key] Quantum basics
> - Photon: $E=h\nu=hc/\lambda$, $p=h/\lambda$; $hc=1239.84$ eV nm. Photoelectric: $K_{\max}=h\nu-\varphi$, emission iff $\nu\ge\nu_0=\varphi/h$ (single photon, **intensity changes number, not energy**).
> - Compton: $\Delta\lambda=\lambda_C(1-\cos\theta)$, $\lambda_C=h/m_ec=2.4263$ pm; max at $\theta=180^\circ$: $2\lambda_C=4.853$ pm; $\lambda_C\propto1/m$.
> - Acceptable $\psi$ (finite non-singular $V$ on the line): **finite, single-valued, continuous, normalisable** ([[Admissible Wavefunction]]).
> - Phase: $e^{i\alpha}\psi$ same state; $e^{ikx}\psi$ **not** the same (momentum shifts by $\hbar k$). $|\psi|^2=2+2\cos(2kx-\varphi)$ for $e^{ikx}+e^{i\varphi}e^{-ikx}$.
> - Operators: $\hat x=x$, $\hat p=-i\hbar\,\partial_x$, $\hat H=\hat p^2/2m+V$, parity $\hat P\psi(x)=\psi(-x)$. $[\hat x,\hat p]=i\hbar$.
> - Ring: $\psi_n=e^{ik_nx}/\sqrt L$, $k_n=2\pi n/L$, $E_n=2\pi^2\hbar^2n^2/mL^2$, $E_n=E_{-n}$, $p_{-n}=-p_n$ ([[Particle on a Ring]]).
> - Born: $\Psi=\sum c_a\phi_a\Rightarrow P(a)=|c_a|^2$; $\langle A\rangle=\sum|c_a|^2a=\int\Psi^*\hat A\Psi$; $(\Delta A)^2=\langle A^2\rangle-\langle A\rangle^2$.
> - Time: $\Psi=\sum c_ne^{-iE_nt/\hbar}\psi_n$; $|c_n|$, $\langle E\rangle$, $\Delta E$ constant; **relative phases** change $|\Psi|^2$.
> - Uncertainty: $\Delta A\Delta B\ge\frac12|\langle[\hat A,\hat B]\rangle|$; $\Delta x\Delta p\ge\hbar/2$.

## 2. The actual quiz, 3 Sep 2026 (15 marks), with full solutions
> [!example] Q1 · Photoelectric effect (2 marks)
> **Classical failure [1].** Classically the energy delivered is tied to the **intensity**, so a bright enough beam should eject electrons at any frequency and the kinetic energy should grow with intensity. Observation: a sharp **threshold frequency** $\nu_0$ and a $K_{\max}$ that depends on $\nu$, not on intensity.
> **Photon picture [1].** One photon of energy $E_\gamma=h\nu$ is absorbed by one electron, which escapes iff $h\nu\ge\varphi$; intensity changes only the **number** of photons per second. Below threshold no single photon suffices, however many arrive; above it even a faint beam ejects electrons at once.
> *Numbers (own example, $\varphi=2.0$ eV):* $\nu_0=4.836\times10^{14}$ Hz ($\lambda_0=620$ nm); 400 nm light (3.100 eV) gives $K_{\max}=1.100$ eV ($v=6.2\times10^5$ m/s); 550 nm (2.254 eV) gives $0.254$ eV; 700 nm (1.771 eV) gives **nothing at any intensity**.

> [!example] Q2 · Compton scattering as a collision (4 marks)
> **(a) [1]** $E_\gamma=hc/\lambda$: the energy the electron gains as kinetic energy comes out of the photon, so the photon has **less energy, hence a longer wavelength**.
> **(b) [1]** The photon's momentum changes (direction, and magnitude after the collision); total momentum is conserved, so the **electron recoils** with the momentum the photon lost: photons carry momentum $p=h/\lambda$.
> **(c) [2]** Nearly backward scattering reverses the photon's direction, the largest change of its momentum vector, so the electron gets the largest recoil and kinetic energy and the photon the **largest wavelength increase**. Quantitatively $\Delta\lambda=\lambda_C(1-\cos\theta)$: $0.325$ pm at $30^\circ$, $2.426$ pm at $90^\circ$, $4.853$ pm at $180^\circ$.
> *Mock Q2(c) (heavy particle):* for a very heavy charged particle the recoil is tiny since $\lambda_C=h/mc\propto1/m$: for a proton $\lambda_C=1.3214$ fm, **1836 times smaller** (the $180^\circ$ shift $2.64$ fm against the X-ray wavelength $71.1$ pm is $4\times10^{-5}$), so the wavelength change is negligible and the scattering looks like Thomson (elastic, no shift).

> [!example] Q3 · Same position density, not the same state (2 marks)
> $|\psi_1|^2=|\psi_2|^2$ shows only that the **position distributions** agree **[1]**. If $\psi_2=e^{ikx}\psi_1$ the factor is a **position-dependent phase**, unlike a constant phase, and it carries momentum information **[1]**:
> $$\hat p\psi_2=-i\hbar\,\partial_x\big(e^{ikx}\psi_1\big)=e^{ikx}\big(\hat p\psi_1+\hbar k\,\psi_1\big),$$
> so the mean momentum is shifted by $\hbar k$ and $\psi_2$ is a different state. (Global vs relative phase, [[Global and Relative Phase]].)

> [!example] Q4 · Particle on a ring (4 marks)
> **(a)** After one full trip the particle is back at the same point, so $\psi$ must return with the same value **and** phase **[1]**: $\psi(x+L)=\psi(x)$, a whole number of wavelengths fits, $L=n\lambda$, $n\in\mathbb Z$, so arbitrary wavelengths are forbidden **[1]**: $k_n=2\pi n/L$.
> **(b)** Clockwise and anticlockwise waves have **opposite momenta** $\pm p_n$: they are **different states** **[1]**, but the same $|p|$ gives $K=p^2/2m$ independent of the sign: **same kinetic energy** (degenerate) **[1]**.
> *Numbers:* electron on a benzene-sized ring $L=0.83$ nm: $E_n=2.183\,n^2$ eV; $L=1$ cm: $E_1=1.5\times10^{-14}$ eV, about $1.7\times10^{12}$ times below $k_BT(300\,\mathrm K)=0.0259$ eV, so the spectrum looks continuous. $E_n\propto1/L^2$.

> [!example] Q5 · Operators, eigenstates, superpositions (3 marks)
> **(a)** $\hat p\,e^{ikx}=\hbar k\,e^{ikx}$: an eigenstate, eigenvalue $\hbar k$ **[0.5]**. $\cos kx=\frac12(e^{ikx}+e^{-ikx})$ gives $\hat p\cos kx=\frac{\hbar k}2(e^{ikx}-e^{-ikx})=i\hbar k\sin kx$, **not proportional** to $\cos kx$, so not a momentum eigenstate **[0.5]**.
> **(b)** The argument does not depend on the matrix. Let $\hat Au_\pm=\pm u_\pm$ and $v=\frac1{\sqrt2}(u_++u_-)$. Then $\hat Av=\frac1{\sqrt2}(u_+-u_-)$ **[0.5]**, which is **not a constant times $v$** (the relative sign of the two components has flipped), so $v$ is **not an eigenvector [0.5]**. In a superposition of eigenstates with different eigenvalues each component is multiplied by a different number, so the relative coefficients change **[1]**: the same as $e^{ikx}$ (an eigenstate) versus $\cos kx$ (contains $\pm\hbar k$; the operator flips their relative sign).
> *Two concrete realisations.* The solution as summarised has $\hat Av=\frac1{\sqrt2}(1,-1)^{\mathsf T}$ and $v=\frac1{\sqrt2}(1,1)^{\mathsf T}$, which fits $\hat A=\mathrm{diag}(1,-1)$ with $u_+=(1,0)^{\mathsf T}$, $u_-=(0,1)^{\mathsf T}$; the mock paper uses $\hat A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $u_\pm=\frac1{\sqrt2}(1,\pm1)^{\mathsf T}$, $v=(1,0)^{\mathsf T}$, $\hat Av=(0,1)^{\mathsf T}$. Both give $\langle A\rangle_v=0$ and $\Delta A=1$ (checked): the outcomes $\pm1$ are equally likely.

## 3. The mock quiz (50 min, 15 marks)
> [!example] Mock Q1 (2): threshold
> Metal X emits and Y does not at the same $\nu$: **(a)** $\nu_{0X}\le\nu<\nu_{0Y}$ (the frequency lies above X's threshold and below Y's). **(b)** Raising the intensity at fixed $\nu$ sends more photons, not more energy per photon: one photon still lacks the energy to free an electron from Y, so Y still emits nothing.

> [!example] Mock Q2 (3): Thomson versus Compton
> **(a)** A recoiling electron carries kinetic energy that came from the photon, so the photon has less energy, hence a longer wavelength. **(b)** The electron, initially at rest, is observed to recoil, so it gained momentum, which momentum conservation says came from the photon: photons carry momentum. **(c)** For a very heavy charged particle the recoil, and the energy taken, is much smaller, so the wavelength change becomes unimportant (proton: $\Delta\lambda_{\max}=2.64$ fm).

> [!example] Mock Q3 (3): acceptable wavefunctions
> Finite non-singular potential on the whole line.
> - $\psi_A=Ne^{-x^2/a^2}$: **acceptable** (finite, continuous, decays; $N=(2/\pi a^2)^{1/4}$ since $\int e^{-2x^2/a^2}\mathrm dx=a\sqrt{\pi/2}$).
> - $\psi_B=Ne^{+x^2/a^2}$: **not acceptable**: grows without bound, $\int|\psi_B|^2$ diverges (no $N$ works).
> - $\psi_C$ ($+Ne^{-x^2/a^2}$ for $x<0$, $-Ne^{-x^2/a^2}$ for $x\ge0$): **not acceptable**: a finite jump from $+N$ to $-N$ at $x=0$, so $\psi$ is not continuous (it would need an infinite $V$ there; $\psi''$ would contain $\delta'$).
> Tutorial analogues ([[Admissible Wavefunction]]): $Ae^{-|x|/a}$ normalises to $A=1/\sqrt a$ (and has a kink, still acceptable); $|\psi|^2\sim1/|x|$ fails normalisability since $\int\mathrm dx/x$ diverges; a half-line $Ae^{-x/a}$ with $\psi=0$ for $x<0$ has $A=\sqrt{2/a}$ but a jump at $0$, so it fails continuity.

> [!example] Mock Q4 (4): time evolution of a superposition
> $\Psi(x,0)=\frac1{\sqrt2}(\phi_1+\phi_2)$, $E_1\ne E_2$.
> **(a)** $\Psi(x,t)=\frac1{\sqrt2}\big[\phi_1e^{-iE_1t/\hbar}+\phi_2e^{-iE_2t/\hbar}\big]$.
> **(b)** The claim "only phases, so $|\Psi|^2$ cannot change" is **wrong in general**: the **relative** phase $e^{-i(E_2-E_1)t/\hbar}$ changes, and $|\Psi|^2=\frac12\big(|\phi_1|^2+|\phi_2|^2\big)+\mathrm{Re}\big(\phi_1^*\phi_2e^{-i(E_2-E_1)t/\hbar}\big)$: the interference term varies at the Bohr frequency $(E_2-E_1)/\hbar$ ([[Time Evolution of a Superposition]]).
> **(c)** Only $\phi_1$: $\Psi=\phi_1e^{-iE_1t/\hbar}$ and $|\Psi|^2=|\phi_1|^2$ is time-independent: a **stationary state**.

> [!example] Mock Q5 (3): parity and a matrix
> **(a)** $\hat P\cos kx=\cos kx$ (eigenstate, eigenvalue $+1$); $\hat Pe^{ikx}=e^{-ikx}$, not proportional to $e^{ikx}$, so not a parity eigenstate: the operator gives the opposite travelling wave. **(b)** as Q5(b) above.

## 4. Traps (the ones both quizzes test)
1. **Intensity vs frequency.** Brightness changes how many electrons, never whether the threshold is met.
2. **"Only phases, so nothing changes."** Global phase: yes. **Relative** phase: the density oscillates.
3. **$e^{ikx}\psi$ is not $\psi$.** Same $|\psi|^2$, different momentum (shift $\hbar k$).
4. **An eigenstate of which operator?** $e^{ikx}$ is a $\hat p$ eigenstate but not a parity eigenstate; $\cos kx$ is a parity and energy eigenstate but not a momentum eigenstate.
5. **$\langle p\rangle=0$ is not $p=0$.** For $\cos kx$ each result is $\pm\hbar k$ with probability $\tfrac12$ ($\Delta p=\hbar|k|$).
6. **Degenerate means same energy, different states** ($\pm n$ on the ring).
7. **Continuity of $\psi$ vs of $\psi'$.** A finite jump in $\psi$ is never allowed for finite $V$; a kink is.
8. **Normalisable $\ne$ normalised.** $e^{+x^2/a^2}$ cannot be fixed by any $N$.
9. **Compton: bigger angle, bigger shift; heavier target, smaller shift.**
10. **Stationary does not mean at rest** (ring $\psi_n$ has uniform density but momentum $p_n$).
11. **$\hat A v\propto v$?** The test for an eigenvector: apply the matrix and check proportionality.
12. **Time is not an operator.** $[\hat T,\hat H]=i\hbar$ would force a spectrum unbounded below; time is a parameter ([[Time Is Not an Operator]]).

## 5. Self-test (cover the answers)
1. Metal with $\varphi=2.0$ eV is lit with 550 nm light of very low intensity. Emission? $K_{\max}$? *(Yes, immediately; $0.254$ eV.)*
2. Same metal, 700 nm, a million times brighter. *(No: 1.771 eV $<2.0$ eV.)*
3. Maximum Compton shift for an electron? For a proton? *($4.853$ pm; $2.643$ fm.)*
4. $\psi=e^{ikx}+e^{-ikx}$ on a ring: probabilities of $+\hbar k$ and $-\hbar k$, $\langle p\rangle$, $\Delta p$? *($\tfrac12,\tfrac12$; $0$; $\hbar|k|$.)*
5. $\Psi=\sqrt{3/4}\,\psi_n+\tfrac12\psi_{-n}$: $\langle p\rangle$? $\Delta p$? *($\tfrac12p_n$; $2|a||b||p_n|=\frac{\sqrt3}{2}p_n$.)*
6. $|\Psi|^2$ for $\frac1{\sqrt2}(\psi_0+\psi_1)$ on a ring: constant? *(No: $\frac1L[1+\cos(kx-\omega t)]$, a pattern rotating at $E_1/\hbar$.)*
7. $\psi=Ae^{-|x|/a}$: $A$? Acceptable? *($1/\sqrt a$; yes.)*
8. $\hat A=\begin{pmatrix}0&1\\1&0\end{pmatrix}$, $v=(1,0)^{\mathsf T}$: $\langle A\rangle$, $\Delta A$, eigenvector? *($0$; $1$; no.)*
9. Box $n=1$: $\Delta x\,\Delta p/\hbar$. *($0.568>0.5$.)*
10. Why can't the oscillator absorb at $2\omega$? *(Only $\Delta n=\pm1$, [[Selection Rules]]; not examined yet.)*

## 6. Where each item lives in the notes
| Quiz item | Chapter and concept |
|---|---|
| photoelectric, Compton | [[QM01 From Waves to Probabilities]] ([[Wave-Particle Duality]], [[Compton Scattering]], [[Compton Wavelength]]) |
| acceptable wavefunctions, normalisation | [[QM02 The Schrodinger Equation and Stationary States]] ([[Admissible Wavefunction]], [[Normalisation of a Wavefunction]]) |
| phase, ring, momentum eigenstates | [[Global and Relative Phase]], [[Particle on a Ring]], [[Eigenstate and Eigenvalue]] |
| operators, superposition, probabilities | [[QM03 States Operators and Measurement]] ([[Measurement Postulate]], [[Expectation Value]], [[Parity Operator]], [[Two-Level System]]) |
| time dependence | [[Time Evolution of a Superposition]], [[Stationary State]] |

> [!verify] Two points in the source summaries
> (1) The summary of the 27 Aug tutorial writes "$\Delta x$ taken as $2\times10^{-10}$ in the denominator": the standard bound $\Delta p_{\min}=\hbar/2\Delta x$ with $\Delta x=10^{-10}$ m gives $5.27\times10^{-25}$ kg m s$^{-1}$, $\Delta v=5.79\times10^5$ m s$^{-1}=1.93\times10^{-3}c$ (recomputed). (2) The 31 Aug note says $E_1(1\,\mathrm{cm})$ is "about $10^{13}$" below $k_BT$; recomputed at 300 K the ratio is $1.7\times10^{12}$. The physics is unchanged. (3) In the summary of the 3 Sep Q5(b) the vectors $u_\pm=\frac1{\sqrt2}(1,\pm1)^{\mathsf T}$ and $v=\frac1{\sqrt2}(1,1)^{\mathsf T}$ are not mutually consistent ($v$ would equal $u_+$, an eigenvector); they are consistent for $\hat A=\mathrm{diag}(1,-1)$. Since the quiz text is missing, §2 gives the matrix-independent argument.

## Provenance
> [!provenance]- Source map
> | Item | Source | Scope |
> |---|---|---|
> | mock quiz Q1–Q5 and ideal solutions | [[2026-09-02-mock-quiz-and-solutions]] (summary of a Classroom post; PDF not in the folder) | taught |
> | 3 Sep quiz Q1–Q5 solutions and marks | [[2026-09-03-quiz-ideal-solutions]] (question texts absent) | taught |
> | assessment status, "must know", gaps | [[ph2113/exam-prep|exam-prep]] (kept by the other tool) | meta |
> | all numbers, own examples (2.0 eV metal, proton Compton, ring energies) | `scripts/qm_numbers.py`, section "QM quiz prep" | extra/beyond |
>
> The quiz summaries link to my notes with lower-case paths (`06-quantum-mechanics/concepts/...`); those links are the other tool's, and resolve here only by note name.
