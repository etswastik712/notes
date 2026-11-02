---
title: Statistical Mechanics Quiz Prep
aliases: [SM quiz prep, stat mech quiz prep, statistical mechanics self-test, SM formula sheet and traps, SM revision]
subject: thermo
type: moc
by: [own-notes, book]
status: draft
tags: [subject/thermo, type/moc, src/own-notes, src/book, status/draft]
---
# Statistical Mechanics Quiz Prep

◀ [[Thermodynamics and Statistical Mechanics - Course Map|Course Map]] · chapters [[SM01 Probability Large Numbers and Information|SM01]] · [[SM02 Phase Space Liouville and the Microcanonical Ensemble|SM02]] · [[SM03 The Canonical Ensemble|SM03]] · [[SM04 Kinetic Theory and the Boltzmann Equation|SM04]] · [[SM05 The Grand Canonical Ensemble and Chemical Equilibrium|SM05]] · [[SM06 Entropy Information and the Arrow of Time|SM06]] · [[SM07 Equipartition the Virial Theorem and Magnetic Systems|SM07]] · [[SM08 Quantum Ensembles and Identical Particles|SM08]]

> [!info] What this page is
> There is no quiz behind Part II: it is **self-study** (no taught/extra labels). This page is the revision layer for SM01–SM08, built to the pattern of [[Climate Quiz Prep]] and [[Quantum Mechanics Quiz Prep]]: the printable formula sheet ([[sm-formula-sheet.pdf]], 3 pages, Part II-A), the traps that cut across chapters, the derivations worth doing on a blank page, and a **24-question self-test** with collapsed answers. Every number here was recomputed (`scripts/sm_quiz_numbers.py` and the chapter scripts); the sheet's recalled inputs are listed on its last page. As Part II-B grows (SM09–SM13) this page and the sheet will be extended.

> [!tip] How to use it
> 1. Read §1 once and fill the gaps from the chapter Summary boxes. 2. Do §3 *with the page covered* before looking at the chapter derivations. 3. Do §4 in one sitting, answers hidden, then compare. 4. Anything missed twice becomes a card (the concept notes in `Concepts/` are one idea each).

## 1. The ten formulas that carry the subject
> [!key] Core formulas (full tables: [[sm-formula-sheet.pdf]])
> - **Entropy and temperature:** $S=k_B\ln\Omega$, $\frac1T=\partial_ES$, $\frac PT=\partial_VS$, $\frac\mu T=-\partial_NS$; ideal gas $S=Nk_B[\ln\frac V{N\lambda^3}+\frac52]$, $\lambda=h/\sqrt{2\pi mk_BT}$ ([[SM02 Phase Space Liouville and the Microcanonical Ensemble|SM02]]).
> - **Canonical:** $p_i=e^{-\beta E_i}/Z$, $F=-k_BT\ln Z$, $E=-\partial_\beta\ln Z$, $\kappa_n(E)=(-1)^n\partial_\beta^n\ln Z$, $\mathrm{Var}\,E=k_BT^2C_V$; $F[q]-F=k_BT\,D(q\|p)\ge0$ ([[SM03 The Canonical Ensemble|SM03]]).
> - **Grand canonical:** $p=e^{-\beta(E-\mu N)}/\mathcal Z$, $\Phi=-k_BT\ln\mathcal Z=-PV$, $\mathrm{Var}\,N=k_BT\,\partial_\mu\langle N\rangle=\langle N\rangle nk_BT\kappa_T$ ([[SM05 The Grand Canonical Ensemble and Chemical Equilibrium|SM05]]).
> - **Occupations:** $\langle n\rangle=1/(e^{x}\pm1)$ (FD/BE), $e^{-x}$ (MB), $x=\beta(\varepsilon-\mu)$ ([[SM05 The Grand Canonical Ensemble and Chemical Equilibrium|SM05]], [[SM08 Quantum Ensembles and Identical Particles|SM08]]).
> - **Large numbers:** $\ln N!=N\ln N-N+\tfrac12\ln2\pi N$; CLT $\kappa_n\propto N^{1-n/2}$; $P\sim e^{-NI}$, $I=\sup_t[ts-K(t)]$ ([[SM01 Probability Large Numbers and Information|SM01]]).
> - **Information:** $S=-\sum p\ln p$, $D(p\|q)\ge0$; MaxEnt $p\propto e^{-\lambda f}$; Landauer $\ge k_BT\ln2$; availability $W=k_BT\,D(p\|p_{\rm eq})$ ([[SM06 Entropy Information and the Arrow of Time|SM06]]).
> - **Kinetic:** $\partial_tf+\mathbf v\!\cdot\!\nabla f=C[f]$; $H$-theorem $\dot H\le0$; $\eta=nk_BT\tau$, $\kappa=\frac52nk_B^2T\tau/m$, $\mathrm{Pr}=\frac23$ ([[SM04 Kinetic Theory and the Boltzmann Equation|SM04]]).
> - **Equipartition and virial:** $\langle x_i\partial_j\mathcal H\rangle=\delta_{ij}k_BT$; $2\langle K\rangle=s\langle V\rangle$ ([[SM07 Equipartition the Virial Theorem and Magnetic Systems|SM07]]).
> - **Quantum:** $\hat\rho=e^{-\beta\hat H}/Z$; $g(r)=1\pm e^{-2\pi r^2/\lambda^2}$; $P=nk_BT[1\mp n\lambda^3/(g_s2^{5/2})]$; $PV=\tfrac23E$ ([[SM08 Quantum Ensembles and Identical Particles|SM08]]).
> - **Magnetism:** $M=N\mu\tanh x$; $S=S(B/T)$ so $T_f=T_iB_f/B_i$; Bohr–van Leeuwen: classical $M=0$ ([[SM07 Equipartition the Virial Theorem and Magnetic Systems|SM07]]).

## 2. Twelve traps that cut across chapters
> [!pitfall] Traps
> 1. **$1/N!$ is not optional.** Without it $S$ is not extensive (Gibbs paradox, SM02 §7); with it, it is the identity term of the permutation sum in quantum statistics (SM08 §5.1). It matters for *mixing identical* gases ($\Delta S=0$), not for the entropy change at fixed $N$.
> 2. **Fluctuations are $1/\sqrt N$, but ensembles are equivalent only away from phase transitions and for stable (positive) $C_V$.** The microcanonical ensemble permits negative heat capacity (stars, SM07 §4); the canonical does not.
> 3. **The CLT is about the bulk, large deviations about the tails.** $P(m\ge0.6)$ for $N=100$ coin tosses: exact $0.0284$, Chernoff bound $0.134$; the CLT is *wrong in the exponent* far from the mean (SM01 §6).
> 4. **$S_G$ of Gibbs is constant under Hamiltonian flow** (Liouville); entropy increase needs coarse-graining or the Boltzmann $S_B$ of a macrostate (SM06 §1). Do not "prove the second law from Liouville".
> 5. **Negative temperature is hotter than infinity**: heat flows from a negative-$T$ to any positive-$T$ system (two-level spins, SM02 §5).
> 6. **Molecular chaos is an assumption about *incoming* pairs only.** Outgoing pairs are correlated; that is the time asymmetry of the Boltzmann equation (SM04 §4, §7). Loschmidt and Zermelo are answered by the *initial condition* and the size of the recurrence time.
> 7. **Relaxation-time $\kappa$ and $\eta$ are not exact**: only the *form* $\propto\sqrt T$ and independence of density are; the Chapman–Enskog coefficients $\frac5{16}$, $\frac{15}4$ are not 1 (SM04 §10).
> 8. **Equipartition fails when quantum effects freeze modes** ($k_BT\ll\hbar\omega$): N$_2$ has $C_V=\frac52R$ at 300 K because vibration ($\theta_v=3394$ K) is frozen; the rotor curve overshoots to $1.098k_B$ at $0.81\,\theta_r$ before settling (SM07 §2).
> 9. **The virial theorem needs time averages and bound motion**; for gravity it gives $E=-K$, hence $C=-\frac32Nk_B$ (SM07 §4).
> 10. **Quantum correction is not a force.** The exchange term changes $P$ by $\mp n\lambda^3/(g_s2^{5/2})$ with no interaction; only *same-spin* fermions have $g(0)=0$ (SM08 §5.1).
> 11. **$g\gg N$ is not enough for classical counting; $g\gg N^2$ is** (SM08 §4.2).
> 12. **The density matrix is not a wavefunction.** Different preparations give the same $\hat\rho$; the *reduced* state of an entangled pair is mixed (SM06 §5, SM08 §2).

## 3. Derivations to do on a blank page
| # | Derive | Hint | Where |
|---|---|---|---|
| 1 | Cumulants of a sum of independent variables; the CLT | $\kappa_n$ add, scale as $N^{1-n/2}$ | SM01 §4 |
| 2 | Stirling and the binomial entropy function by the saddle point | $\varphi''<0$ at the maximum | SM01 §5 |
| 3 | Gibbs' inequality and MaxEnt gives $e^{-\lambda f}$ | Lagrange multipliers | SM01 §7 |
| 4 | Ideal-gas $\Sigma(E,V,N)$ and Sackur–Tetrode | volume of a $3N$-ball, Stirling | SM02 §6 |
| 5 | Canonical from microcanonical (heat bath, expand $\ln\Omega_R$) | $\Omega_R(E_{\rm tot}-E)\propto e^{-\beta E}$ | SM03 §1 |
| 6 | $\mathrm{Var}\,E=k_BT^2C_V$ and $\partial_\lambda\langle B\rangle=\beta\mathrm{Var}B$ | differentiate $\ln Z$ twice | SM03 §2.6 |
| 7 | Maxwell velocity distribution and the barometric law | factorise $e^{-\beta(p^2/2m+mgz)}$ | SM03 §4 |
| 8 | $\mathrm{Var}N=k_BT\partial_\mu N$ and $=N nk_BT\kappa_T$ | Gibbs–Duhem | SM05 §3 |
| 9 | FD, BE and MB from a single mode | sum over $n$ | SM05 §5 |
| 10 | Law of mass action and the Saha equation | $\sum\nu_i\mu_i=0$, $\mu=kT\ln(n\lambda^3/z_{\rm int})$ | SM05 §7 |
| 11 | H-theorem | symmetrise over $1\leftrightarrow2$ and $\to\,'$, $(a-b)\ln(a/b)\ge0$ | SM04 §6 |
| 12 | Generalised equipartition $\langle x_i\partial_j\mathcal H\rangle=\delta_{ij}k_BT$ | integrate by parts | SM07 §1 |
| 13 | Bohr–van Leeuwen | shift $\mathbf p\to\mathbf p-q\mathbf A$ | SM07 §5 |
| 14 | Exchange correlation $g(r)$ and $B_2=\mp\lambda^3/2^{5/2}$ | two-particle permutation term | SM08 §5.1 |
| 15 | $PV=\frac23E$ for any statistics | integrate $\ln\mathcal Z$ by parts | SM08 §5.2 |

## 4. Self-test (24 questions; answers collapsed)
**A. Probability and large numbers**
1. $\ln100!$ by Stirling with and without the $\tfrac12\ln2\pi N$ term.
2. A fair coin is tossed $N=100$ times. Give the rate function $I(0.6)$, the Chernoff bound on $P(\text{heads}\ge60)$, and compare with the exact value.
3. The variables $x_i$ are independent Poisson($\lambda$). What are $\kappa_n$ of the sum, and the fourth moment of one variable?
> [!example]- Answers (A)
> 1. $\ln100!=363.739$; $N\ln N-N=360.517$ ($0.89\%$ low); adding $\tfrac12\ln(2\pi\cdot100)=3.2224$ gives $363.739$.
> 2. $I(m)=\ln2+m\ln m+(1-m)\ln(1-m)=0.020136$; $e^{-NI}=0.134$; exact $0.0284$. The bound is not tight but has the correct exponent for $N\to\infty$ ($N=1000$: bound $1.8\times10^{-9}$, exact $1.4\times10^{-10}$).
> 3. $\kappa_n=N\lambda$ for all $n$; $\langle x^4\rangle=\lambda^4+6\lambda^3+7\lambda^2+\lambda$ (sum over set partitions of $\kappa_{|B|}=\lambda$).

**B. Microcanonical and canonical**
4. A two-level system with $\varepsilon=\varepsilon_1-\varepsilon_0$ has 25% in the upper level. Find $S/Nk_B$ and $k_BT/\varepsilon$. What if 75%?
5. One mole of A and one mole of B (distinguishable, each in volume $V$) are allowed to mix by removing a partition. $\Delta S$? And if A and B are the same gas?
6. The energy of an ideal gas in the canonical ensemble is Gamma-distributed. Give the relative width and the skewness for $N=100$ and $N=10^{23}$.
7. Barometric law: scale heights of air and CO$_2$ at 288.15 K.
> [!example]- Answers (B)
> 4. $S/Nk_B=-0.25\ln0.25-0.75\ln0.75=0.5623$; $k_BT/\varepsilon=1/\ln3=0.910$. At 75% the temperature is **negative**, $-0.910\,\varepsilon/k_B$, with the same entropy (SM02 §5).
> 5. $\Delta S=2R\ln2=11.53$ J/K (each gas doubles its volume). Same gas: $\Delta S=0$ ($1/N!$).
> 6. Relative width $\sqrt{2/3N}$: $0.0816$ ($N=100$), $2.6\times10^{-12}$ ($10^{23}$); skewness $\sqrt{8/3N}=0.163$ (100).
> 7. $H=k_BT/mg=8.43$ km (28.97 u), $5.55$ km (44.01 u).

**C. Grand canonical, chemical equilibrium and entropy**
8. Occupation of a level at $\varepsilon-\mu=k_BT$ for FD, BE and MB.
9. Langmuir: at what $P/P_0$ is the coverage $0.9$? What is $\theta$ at $P=3P_0$?
10. In a grand canonical ideal gas with $\langle N\rangle=10$, what is the probability of finding no particle in the sub-volume?
11. Landauer limit at 300 K, in joules and eV; and the work to erase one bit in a CMOS gate switching at $\sim10^{-15}$ J: how many times the limit?
12. Ratio of the entropy flux of the Earth's emission to that of absorbed sunlight (same energy flux, $T_e=254.6$ K, $T_\odot=5772$ K); entropy per photon of blackbody radiation in units of $k_B$.
> [!example]- Answers (C)
> 8. FD $0.2689$, BE $0.5820$, MB $0.3679$ (the three bracket the classical value; FD $<$ MB $<$ BE).
> 9. $\theta=P/(P+P_0)$: $0.9\Rightarrow P/P_0=9$; $P=3P_0\Rightarrow\theta=0.75$.
> 10. Poisson: $e^{-\langle N\rangle}=4.5\times10^{-5}$.
> 11. $k_BT\ln2=2.871\times10^{-21}$ J $=0.0179$ eV; $10^{-15}/2.871\times10^{-21}=3.5\times10^5$ (recalled switching energy, only the order of magnitude matters).
> 12. $T_\odot/T_e=22.7$ (equal energy flux, so entropy flux $\propto1/T$); $s/(nk_B)=2\pi^4/(45\zeta(3))=3.60$ per photon (mean energy $2.70\,k_BT$).

**D. Kinetic theory and equipartition**
13. Which approximation turns the Boltzmann collision integral into $-(f-f_{\rm eq})/\tau$, and what are $\eta$ and $\kappa$ in terms of $\tau$?
14. State the molecular-chaos assumption and why the H-theorem is not in conflict with reversible dynamics.
15. $\langle\mathcal E\rangle$ of an oscillator of frequency $\omega$ in units of $k_BT$ at $x=\hbar\omega/k_BT=0.5$ and 2.
16. Hydrogen atom: $K$, $V$, $E$ (eV); the Sun's mean temperature from the virial theorem.
> [!example]- Answers (D)
> 13. The relaxation-time (BGK) approximation. $\eta=nk_BT\tau$, $\kappa=\frac52nk_B^2T\tau/m$; (exact Chapman–Enskog $\kappa=\frac{15}4\frac{k_B}m\eta$, $\mathrm{Pr}=\frac23$).
> 14. The two-particle distribution factorises *before* a collision, $f_2=f_1f_1$, but not after. A reversed trajectory has outgoing correlations that do not factorise, so molecular chaos fails for it; and the recurrence time is $\sim e^{N}$ (SM02 §2.3). Loschmidt is answered by the initial condition, Zermelo by the astronomical recurrence time.
> 15. $\tfrac x2\coth\tfrac x2$: $x=0.5\Rightarrow1.0207$ (near classical 1); $x=2\Rightarrow1.3130$ (frozen: the zero-point $x/2=1$ plus a small thermal part).
> 16. $K=13.606$, $V=-27.211$, $E=-13.606$ eV; the Sun $\bar T=GM\mu m_H/5k_BR=2.8\times10^6$ K (SM07 §4; recalled solar inputs).

**E. Magnetism and information**
17. A spin-½ at 1 K in 1 T: entropy per spin and the final temperature if $B$ is reduced adiabatically to 0.01 T.
18. Why can a classical gas of charged particles not be paramagnetic or diamagnetic?
19. What is the maximum work extractable from a system with distribution $p$ in a bath at $T$ in which the equilibrium distribution is $p_{\rm eq}$?
> [!example]- Answers (E)
> 17. $S=0.5099\,k_B$ per spin; $T_f=T_iB_f/B_i=0.01$ K (the entropy depends on $B/T$ only).
> 18. Bohr–van Leeuwen: the Lorentz force does no work, the shift $\mathbf p\to\mathbf p-q\mathbf A$ removes $B$ from $Z$, so $M=-\partial_BF=0$. Magnetism is a quantum effect (spins, orbital quantisation).
> 19. $W_{\max}=k_BT\,D(p\|p_{\rm eq})$ (availability), equivalently $F[p]-F_{\rm eq}$.

**F. Quantum statistics**
20. Number of states of $N=3$ particles in $g=10$ levels: distinguishable, boson, fermion; compare with $g^N/N!$.
21. $g(r)$ for bosons and fermions at $r=\lambda/2$; at which separation is the exchange term $<1\%$?
22. Compute the first quantum correction to $P/nk_BT$ for He-4 ($n\lambda^3=0.135$) and He-3 at 4.2 K, 1 atm.
23. Give the density matrix of a spin-½ at 1 K in 1 T: Bloch vector, eigenvalues, purity.
24. Show that the Uehling–Uhlenbeck equilibrium is FD for fermions and BE for bosons.
> [!example]- Answers (F)
> 20. $1000,\ 220,\ 120$ against $166.7$ (ratios $1.32$ and $0.72$): classical counting needs $g\gg N^2$.
> 21. $g=1.208$ (bosons), $0.792$ (fermions); $e^{-2\pi r^2/\lambda^2}<0.01\iff r>0.86\,\lambda$.
> 22. He-4: $1-0.135/5.657=0.976$ ($-2.4\%$). He-3 ($n\lambda^3=0.206$, $g_s=2$): $1+0.206/(2\times5.657)=1.018$ ($+1.8\%$).
> 23. $|\mathbf r|=\tanh(0.6717)=0.586$, eigenvalues $0.793,\ 0.207$, purity $\tfrac12(1+r^2)=0.672$, $S=0.510\,k_B$.
> 24. The bracket vanishes iff $\ln[f/(1+\epsilon f)]$ is a collision invariant $=\alpha-\beta\varepsilon$, i.e. $f=1/(e^{\beta\varepsilon-\alpha}-\epsilon)$ (SM08 §6, Problem 11).

> [!summary] Revision order
> Formula sheet (20 min) → traps (10 min) → derivations 1, 4, 5, 9, 11, 14 (the six that cover the structure of the subject) → self-test A–F → the chapters' practice sets for what remains.

## Provenance
> [!provenance]- Source map for this page
> | Material | Source | Origin |
> |---|---|---|
> | formulas, traps, derivation list | SM01–SM08 and their cited book sections | book / mine |
> | self-test questions and answers | my own; numbers recomputed in `scripts/sm_quiz_numbers.py`, `scripts/sm0*_numbers.py` | mine |
> | recalled inputs | switching energy of a CMOS gate ($\sim10^{-15}$ J), solar $M,R,L$, $T_\odot=5772$ K, $T_e$ from $S=1361$ W/m$^2$ and albedo $0.3$ (SM06) | recalled |
>
> **Flags.** (1) Answer 11's CMOS energy is an order of magnitude only. (2) No course sets the quiz style; question types follow the chapters' own practice problems.
