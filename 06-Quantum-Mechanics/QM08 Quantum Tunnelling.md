---
title: QM08 Quantum Tunnelling
aliases: [QM08, tunnelling, tunneling, scattering in one dimension, step and barrier, WKB and Gamow, Kronig-Penney]
subject: qm
type: chapter
chapter: 8
part: II
scope: [extra-book, extra-beyond]
by: [book, own-notes]
status: draft
prereq: ["[[QM07 The Finite Square Well]]", "[[QM02 The Schrodinger Equation and Stationary States]]"]
tags: [subject/qm, type/chapter, extra/book, extra/beyond, src/book, src/own-notes, status/draft]
---
# QM08 · Quantum Tunnelling

◀ [[QM07 The Finite Square Well]] · [[Quantum Mechanics - Course Map|Course Map]] · next: [[QM09 The Stern-Gerlach Experiment and Spin]]

<span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> **No lecture source.** The Lecture 9 notes announce *tunnelling and step potentials* as the next topic ([[Quantum Mechanics - Course Map]], Gaps) and the instructor's finite-well lecture ends with the scattering formula for $E>V_0$ ([[Finite_well.pdf#page=13|p.13]]); nothing later is in the folder. This chapter therefore **extends QM07 §11** to the cases that follow naturally and labels everything 🟡/🔵.
> 🟡 **Extra · book**
> - §1–§3 step, probability current, rectangular barrier: Griffiths §2.5–§2.6 (delta-function scattering and the finite well/barrier; book p.65 onward = [[Griffiths - Introduction to quantum mechanics.pdf#page=80|PDF p.80 ff.]]); the transmission coefficients themselves are the *analytic continuation* of the lecture's formula (QM07 §11)
> - §5 WKB approximation and the connection formulas: Sakurai and Napolitano §2.5.4 (printed pp.104–108, [[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=124|PDF pp.124–128]])
> 🔵 **Extra · beyond** (my additions, all numbers in `scripts/qm08_numbers.py`, every closed form checked against a transfer-matrix solver)
> - §4 delta barrier and the pole of $T$ at the bound-state energy; §5 the Gamow factor evaluated for $^{238}$U, $^{232}$Th, $^{212}$Po; §6 the real-world scales (STM, protons versus electrons, fusion, ammonia); §7 resonant tunnelling by two barriers; §8 the Kronig–Penney delta comb and its band edges; §9 unitarity of the $S$-matrix

> [!key] After this chapter you can
> - define the **probability current** $j=\frac\hbar m\mathrm{Im}(\psi^*\psi')$ and prove $R+T=1$ for any real potential that vanishes at $\pm\infty$ (and see why $T\neq|t|^2$ when the two outer regions differ),
> - solve the **step potential** both above and below the step and describe the evanescent wave,
> - derive the **rectangular-barrier transmission** $T=\big[1+\frac{V_0^2\sinh^2\kappa L}{4E(V_0-E)}\big]^{-1}$ from the finite-well formula by $k_0\to i\kappa$, and its thick-barrier form $T\simeq16\frac E{V_0}(1-\frac E{V_0})e^{-2\kappa L}$,
> - show that the **delta barrier** has $T=[1+m\alpha^2/2\hbar^2E]^{-1}$ and that the bound state of the delta *well* is a pole of the same amplitude,
> - state the **WKB tunnelling formula** $T\approx e^{-2\int\kappa\,dx}$ and use it for **$\alpha$ decay** (the Gamow factor) with real numbers,
> - explain **resonant tunnelling** in a double barrier and the **band structure** of a periodic potential (Kronig–Penney, Bloch's theorem).

> [!intuition] The one-sentence story
> A wave that meets a wall higher than its energy does not stop dead: inside the wall it dies *exponentially*, and if the wall is thin enough some amplitude is still there on the far side, where it propagates again — a particle "tunnelling" through a region it classically could not enter, with probability $e^{-2\kappa L}$ that falls by a fixed factor for every extra ångström.

![[QM08 Tunnelling Map.svg]]
*Diagram QM8.0. The chapter in one page: step, barrier, the thick-barrier exponential, WKB and Gamow, resonant tunnelling and bands. Editable source: [[QM08 Tunnelling Map.excalidraw]].*

> [!intuition] Four pictures to carry around
> 1. **Light in a prism.** Total internal reflection leaves an *evanescent wave* in the air; bring a second prism within a wavelength and light crosses the gap (frustrated total internal reflection). Quantum tunnelling is exactly this with the Schrödinger equation in place of Maxwell's.
> 2. **A staircase of tiny dips.** Cut a smooth barrier into thin slices. Each slice lets through a factor $e^{-2\kappa_i\,dx}$ of the amplitude-squared; the factors *multiply*, so exponents *add*: $T\approx\exp(-2\int\kappa\,dx)$. That is the whole of WKB.
> 3. **The mass and width penalty are exponential, not linear.** Doubling the width squares a tiny number; quadrupling the mass doubles the exponent. An electron tunnels a nanometre; a proton through the same barrier is $10^{-96}$ (§6). This is why tunnelling is a *light-particle, thin-barrier* phenomenon.
> 4. **Wells and barriers are two faces of one function.** The transmission amplitude $t(E)$ of a *barrier*, continued to negative energy, has poles exactly at the bound-state energies of the corresponding *well*. Scattering and bound states are the same object seen at positive and negative $E$ (§4).

> [!pitfall] Four traps
> 1. **$T$ is a ratio of currents, not of $|\psi|^2$.** If the wavenumbers differ on the two sides, $T=|t|^2k_{\rm out}/k_{\rm in}$ (the step at $E=2V_0$ has $|t|^2=1.373>1$ but $T=0.971$).
> 2. **"Energy below the barrier" does not mean "particle inside the barrier".** The probability of *finding* it inside is nonzero but its kinetic energy $E-V<0$ is never measured: any measurement that localises it inside is a different state ([[Measurement Postulate]]).
> 3. **Do not use $e^{-2\kappa L}$ for thin barriers.** The prefactor $16(E/V_0)(1-E/V_0)$ is up to 4 and the bare exponential can be wrong by that factor (e.g. $\kappa L=2.12$: $T=0.0559$ exact against $e^{-2\kappa L}=0.0144$).
> 4. **Resonant tunnelling is not "more tunnelling through each barrier"**; it is the two barriers acting as a cavity: $T=1$ only when the energy matches a quasi-bound level of the well between them.

## 1. Scattering, probability current and $R+T=1$
<span class="scope-extra-book">extra · book</span> *Griffiths §2.5 ([[Griffiths - Introduction to quantum mechanics.pdf#page=80|PDF p.80 ff.]]); QM07 §11*

A *scattering state* has $E$ in the continuum. Send a plane wave $e^{ikx}$ from the left; some is reflected ($re^{-ikx}$) and some is transmitted ($te^{ik'x}$ on the right, $k'$ the wavenumber there). The stationary Schrödinger equation does not know about time, so what conserves probability is the **current**.

> [!derivation] The current and why $R+T=1$
> For $\Psi=\psi(x)e^{-iEt/\hbar}$ the probability density $\rho=|\psi|^2$ is constant, and the continuity equation $\partial_t\rho+\partial_xj=0$ with $j=\frac{\hbar}{2mi}(\psi^*\psi'-\psi\psi'^*)=\frac\hbar m\,\mathrm{Im}(\psi^*\psi')$ gives
> $$\frac{dj}{dx}=0\ \Rightarrow\ j(x)=\text{const.}$$
> (Directly: $\frac{d}{dx}(\psi^*\psi'-\psi\psi'^*)=\psi^*\psi''-\psi\psi''^*=\frac{2m}{\hbar^2}(V-E)(|\psi|^2-|\psi|^2)=0$ for real $V$.) On the left $j=\frac{\hbar k}{m}(1-|r|^2)$, on the right $j=\frac{\hbar k'}{m}|t|^2$. Equality gives
> $$\boxed{R\equiv|r|^2,\quad T\equiv\frac{k'}{k}|t|^2,\quad R+T=1.}$$
> Only the *ratio of currents* is a probability; the prefactor $k'/k$ is the ratio of speeds.

*Link to the Dirac chapter:* for a time-reversal-invariant, real potential the map from incoming to outgoing amplitudes is **unitary** (§9), which is $R+T=1$ in matrix form ([[Dirac Algebra]] §7).

## 2. The step potential
<span class="scope-extra-book">extra · book</span> *Griffiths §2.5 problems; Gasiorowicz ch.4*

$V=0$ for $x<0$ and $V=V_0$ for $x>0$; the wave comes from the left with $k_1=\sqrt{2mE}/\hbar$.

**$E>V_0$.** On the right $k_2=\sqrt{2m(E-V_0)}/\hbar$. Matching $\psi,\psi'$ at $x=0$: $1+r=t$, $k_1(1-r)=k_2t$, so
$$r=\frac{k_1-k_2}{k_1+k_2},\quad t=\frac{2k_1}{k_1+k_2},\qquad \boxed{R=\Big(\frac{k_1-k_2}{k_1+k_2}\Big)^2,\quad T=\frac{4k_1k_2}{(k_1+k_2)^2}}.$$
Classically $R=0$; quantum mechanically a wave reflects at *any* change of wavenumber, exactly like light at an air–glass interface. $R\to1$ at threshold ($k_2\to0$) and $R\to0$ as $E\gg V_0$.

| $E/V_0$ | 1.001 | 1.2 | 2 | 4 | 10 |
|---|---|---|---|---|---|
| $T$ | 0.1188 | 0.8234 | 0.9706 | 0.9948 | 0.9993 |
| $R$ | 0.8812 | 0.1766 | 0.0294 | 0.0052 | 0.0007 |

(Equal to the transfer-matrix solution to six digits.)

**$E<V_0$.** Now $k_2=i\kappa$, $\kappa=\sqrt{2m(V_0-E)}/\hbar$, and the right-hand solution is $te^{-\kappa x}$. Then $|r|^2=\big|\frac{k_1-i\kappa}{k_1+i\kappa}\big|^2=1$: **total reflection**, but with a phase shift, and a non-zero probability density in the forbidden region, $|t|^2e^{-2\kappa x}=\frac{4k_1^2}{k_1^2+\kappa^2}e^{-2\kappa x}=\frac{4E}{V_0}e^{-2\kappa x}$. *No current flows into the step*: $\mathrm{Im}(\psi^*\psi')=0$ for a real exponential. For an electron with $V_0-E=1$ eV the penetration depth is $1/\kappa=0.195$ nm.

![[fig_qm08_step_barrier.png]]
*Figure QM8.1. Step and barrier. A: $|\psi|^2$ for $E=2V_0$ (blue: standing-wave ripples on the left from the partial reflection, constant on the right) and $E=0.5V_0$ (orange: total reflection, a decaying tail inside the shaded step). B: $T$ and $R$ for the step against $E/V_0$: $T=0$ at threshold, $R+T=1$ everywhere, and for $E<V_0$ the total reflection ($R=1$). C: the rectangular barrier, $T(E/V_0)$ for widths $L=1,2,4$ (units $\hbar/\sqrt{2mV_0}$): below the top, $T$ is non-zero but exponentially small (tunnelling); above the top, $T$ oscillates with peaks $T=1$ at $k_2L=n\pi$.*

## 3. The rectangular barrier
<span class="scope-extra-book">extra · book</span> *Griffiths §2.5–§2.6; QM07 §11 (the same calculation with the well turned upside down)*

$V=V_0$ for $0<x<L$ and 0 outside. QM07 §11 solved the *well* of width $L=2a$: outside wavenumber $k$, inside $k_0$, and
$$T=\Big[1+\frac{(k^2-k_0^2)^2}{4k^2k_0^2}\sin^2(k_0L)\Big]^{-1}.$$
The algebra never used the sign of $V_0$: it only used the two wavenumbers. For a barrier with $E<V_0$ the outside wavenumber is $k=\sqrt{2mE}/\hbar$ and the *inside* one is imaginary, $k_0\to i\kappa$:
$$(k^2-k_0^2)^2\to(k^2+\kappa^2)^2,\quad 4k^2k_0^2\to-4k^2\kappa^2,\quad \sin^2(k_0L)\to-\sinh^2(\kappa L).$$
Using $k^2+\kappa^2=2mV_0/\hbar^2$ and $k^2\kappa^2=(2m/\hbar^2)^2E(V_0-E)$:

$$\boxed{T=\frac{1}{1+\dfrac{V_0^2\sinh^2(\kappa L)}{4E(V_0-E)}},\qquad R=1-T}\qquad(E<V_0).$$

> [!derivation] Limits
> * **Thick barrier** ($\kappa L\gg1$): $\sinh\kappa L\to\tfrac12e^{\kappa L}$, so $T\simeq\dfrac{16E(V_0-E)}{V_0^2}\,e^{-2\kappa L}=16\frac E{V_0}\Big(1-\frac E{V_0}\Big)e^{-2\kappa L}$. The exponent is the *leading, universal* part; the prefactor is at most $4$ (at $E=V_0/2$).
> * **Thin barrier** ($\kappa L\ll1$ at fixed area $\alpha=V_0L$): $\sinh^2\kappa L\to\kappa^2L^2$ and $V_0^2\kappa^2L^2/4E(V_0-E)\to\dfrac{m\alpha^2}{2\hbar^2E}$: the delta barrier of §4.
> * **Over the top** ($E>V_0$): $\kappa\to ik_2$, $\sinh\to i\sin$: $T=\big[1+\frac{V_0^2\sin^2k_2L}{4E(E-V_0)}\big]^{-1}$, with **resonances** $T=1$ at $k_2L=n\pi$: the same standing-wave condition as the well resonances of QM07 §11.

| Barrier | $\kappa$ (nm$^{-1}$) | $\kappa L$ | exact $T$ | $e^{-2\kappa L}$ |
|---|---|---|---|---|
| electron, $E=1$, $V_0=2$ eV, $L=0.5$ nm | 5.123 | 2.562 | **0.0235** | 0.0060 |
| same, $L=1.0$ nm | 5.123 | 5.123 | **$1.42\times10^{-4}$** | $3.5\times10^{-5}$ |
| electron, $E=4$, $V_0=5$ eV, $L=0.3$ nm (STM-like) | 5.123 | 1.537 | **0.115** | 0.046 |

(Here $\kappa=5.1231\,\mathrm{nm^{-1}}\sqrt{(V_0-E)/\mathrm{eV}}$. Doubling $L$ from 0.5 to 1.0 nm multiplies $T$ by $6\times10^{-3}$, not by $\tfrac12$.)

## 4. The delta barrier, and a well-barrier duality
<span class="scope-extra-beyond">extra · beyond</span> *Griffiths §2.5 (delta potential); QM07 §7*

Take $V=\alpha\delta(x)$. Integrating the Schrödinger equation across $x=0$ gives $\psi'(0^+)-\psi'(0^-)=\frac{2m\alpha}{\hbar^2}\psi(0)$ with $\psi$ continuous. For $e^{ikx}+re^{-ikx}$ on the left and $te^{ikx}$ on the right:
$$t=\frac{1}{1+i\beta},\quad r=\frac{-i\beta}{1+i\beta},\quad \beta=\frac{m\alpha}{\hbar^2k}\ \Rightarrow\ \boxed{T=\frac{1}{1+\dfrac{m\alpha^2}{2\hbar^2E}}},\quad R=\frac{\beta^2}{1+\beta^2}.$$
This agrees with the thin-barrier limit of §3 and with the transfer-matrix solution (e.g. $T=0.5000$ at $E=\alpha^2/4$ in units $\hbar^2/2m=1$).

> [!connection] The pole of $t$ *is* the bound state of QM07
> $t(k)=\dfrac{1}{1+im\alpha/\hbar^2k}=\dfrac{k}{k+im\alpha/\hbar^2}$ has a pole at $k=-i\,m\alpha/\hbar^2$. For an **attractive** delta ($\alpha\to-|\alpha|$) the pole moves to $k=+i\,m|\alpha|/\hbar^2\equiv i\kappa$, i.e. a wave $e^{ikx}=e^{-\kappa x}$ that decays on both sides: **exactly the bound state** $\kappa=m|\alpha|/\hbar^2$, $E=-m\alpha^2/2\hbar^2$ of QM07 §7. Bound states are the poles of the scattering amplitude on the positive imaginary $k$-axis; resonances are poles slightly off the real axis (§7). This is the seed of scattering theory.

## 5. WKB and the Gamow factor
<span class="scope-extra-book">extra · book</span> *Sakurai and Napolitano §2.5.4 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=124|PDF pp.124–128]])* · <span class="scope-extra-beyond">extra · beyond</span> *the Gamow numbers*

**WKB in one line.** For a slowly varying potential write $\psi=\exp(iS/\hbar)$; to lowest order $S'=\pm p(x)$ with $p=\sqrt{2m(E-V)}$. In a forbidden region $p=i\hbar\kappa(x)$, so the amplitude grows or decays as $\exp(\pm\int\kappa\,dx)$. Slicing the barrier between the classical turning points $x_1$ and $x_2$ and multiplying the slice factors:
$$\boxed{T\simeq\exp\Big(-2\int_{x_1}^{x_2}\kappa(x)\,dx\Big),\qquad\kappa(x)=\frac{\sqrt{2m[V(x)-E]}}{\hbar}}$$
*Validity:* $|d\lambda/dx|\ll1$ (the local wavelength changes little over one wavelength), which fails at the turning points themselves (Sakurai's connection formulas supply the missing factors) and for thin barriers: for a rectangle the exact prefactor is $16\frac E{V_0}(1-\frac E{V_0})$, not 1.

> [!derivation] The Gamow factor for the Coulomb barrier
> An $\alpha$ particle of energy $E$ inside a nucleus of radius $R$ feels (outside) $V(r)=\dfrac{Z_dZ_\alpha e^2}{4\pi\varepsilon_0r}$, with outer turning point $R_c=\dfrac{Z_dZ_\alpha e^2}{4\pi\varepsilon_0E}$. Then $\kappa(r)=\dfrac{\sqrt{2\mu E}}{\hbar}\sqrt{R_c/r-1}$, and
> $$G=\int_R^{R_c}\kappa\,dr=\frac{\sqrt{2\mu E}}{\hbar}R_c\Big[\arccos\sqrt x-\sqrt{x(1-x)}\Big],\qquad x=\frac R{R_c},\qquad T\simeq e^{-2G}.$$
> The decay constant is $\lambda\approx\nu\,e^{-2G}$ with an "assault frequency" $\nu\approx v/2R$ (the $\alpha$ hits the wall $v/2R$ times per second).

| Decay | $E_\alpha$ (MeV) | $R_c$ (fm) | $2G$ | estimated $T_{1/2}$ | measured $T_{1/2}$ |
|---|---|---|---|---|---|
| $^{238}$U → $^{234}$Th | 4.267 | 60.7 | 88.0 | $4.9\times10^9$ yr | $4.47\times10^9$ yr |
| $^{232}$Th → $^{228}$Ra | 4.012 | 63.2 | 90.6 | $6.2\times10^{10}$ yr | $1.40\times10^{10}$ yr |
| $^{212}$Po → $^{208}$Pb | 8.954 | 26.4 | 32.3 | $2.0\times10^{-15}$ yr ($6\times10^{-8}$ s) | $2.99\times10^{-7}$ s |

(For $^{238}$U: $R=1.2(234^{1/3}+4^{1/3})=9.30$ fm, $x=0.153$, $G=44.03$, $e^{-2G}=5.8\times10^{-39}$, $v=0.048c$, $\nu=7.8\times10^{20}\,\mathrm{s}^{-1}$.) **Twenty-four orders of magnitude** in lifetime ($3\times10^{-7}$ s for $^{212}$Po against $1.4\times10^{17}$ s for $^{238}$U) come from a factor of about two in $E_\alpha$ (and the larger $Z$): the exponent $2G\propto Z/\sqrt E$ is the **Geiger–Nuttall law**. The estimates are within a factor of about five of the measured values (the model has no adjustable parameters other than the nuclear radius and the assault frequency; `[verify]` the measured values against a nuclear data table).

![[fig_qm08_tunnelling.png]]
*Figure QM8.2. Tunnelling at work. A: $|\psi|^2$ for $E=0.5V_0$ and $L=3$ (units $\hbar/\sqrt{2mV_0}$): interference ripples on the left (incident plus reflected), exponential decay in the shaded barrier, a flat transmitted wave with $T=0.056$. B: $T$ against width for $E/V_0=0.2,0.5,0.8$ on a logarithmic axis: asymptotically straight lines of slope $-2\kappa$ ($-1.79,-1.41,-0.89$) with prefactor $16\frac E{V_0}(1-\frac E{V_0})$. C: the Coulomb barrier of $^{238}$U: the $\alpha$ particle with $E=4.27$ MeV tunnels between $R=9.3$ fm and $R_c=60.7$ fm through a region with $2G=88$.*

## 6. How big is tunnelling in the real world?
<span class="scope-extra-beyond">extra · beyond</span> *numbers from `scripts/qm08_numbers.py`; atomic constants from the CODATA values used throughout the vault*

| System | Barrier | Result |
|---|---|---|
| **Electron vs proton** | $E=1$ eV, $V_0=2$ eV, $L=0.5$ nm | electron $T=2.4\times10^{-2}$; proton ($\kappa=219\ \mathrm{nm^{-1}}$) $T\approx e^{-2\kappa L}=4.6\times10^{-96}$ |
| **Scanning tunnelling microscope** | work function $\phi\approx4$ eV: $\kappa=10.25\ \mathrm{nm^{-1}}$ | current $\propto e^{-2\kappa d}$: **factor 7.8 per 0.1 nm (one ångström)**; a tip held to $<0.01$ nm resolves single atoms |
| **Fusion in the Sun** | proton–proton Coulomb barrier $\approx1.4$ MeV at $r=1$ fm; core $kT\approx1.3$ keV | classically impossible ($T\sim10^{10}$ K needed); the Gamow factor of §5 (with $Z_1Z_2=1$, $\mu=m_p/2$) makes the rate small but non-zero |
| **Ammonia inversion** | N atom through the plane of the three H: double-well potential | splitting $\approx0.8\ \mathrm{cm^{-1}}$, i.e. the 23.87 GHz maser line |
| **Flash memory, tunnel diode, Josephson junction** | thin oxide or insulating layer | tunnelling current is the working principle |

> [!extra-beyond]- 🔵 Extra (beyond): why a doubled width squares $T$ but a quadrupled mass only doubles the exponent
> $T\sim e^{-2\kappa L}$ with $\kappa=\sqrt{2m(V_0-E)}/\hbar\propto\sqrt m$ and the exponent linear in $L$. Width enters linearly in the exponent ($T\to T^2$ when $L\to2L$); mass enters as a square root ($m\to4m$ doubles the exponent). An electron to a proton is a factor $\sqrt{1836}=42.8$ in the exponent: from $\kappa L=2.56$ to $110$, i.e. from $T=0.02$ to $T=10^{-96}$.

## 7. Two barriers: resonant tunnelling
<span class="scope-extra-beyond">extra · beyond</span> *transfer-matrix calculation, units $\hbar^2/2m=1$*

Put two identical barriers ($V_0=1$, width 1) a distance 2 apart. The space between is a finite well of half-width $a=1$, $z_0=a\sqrt{V_0}=1$ (QM07), which has **one** quasi-bound level at $E/V_0=z_1^2/z_0^2=0.546$ if the walls were infinitely thick.

* A single barrier at $E=0.1V_0$ transmits $T=0.230$; two barriers in series *off* resonance transmit down to $10^{-3}$ — **much less**, because the waves between the barriers interfere destructively.
* On resonance, $E/V_0=0.5616$ (the quasi-bound level, pushed from 0.546 by the finite wall thickness), the transmission is $T=1.0000$: **perfect transmission through two opaque barriers**. The wave amplitude inside the well is large (Fig. QM8.3 B) — the particle is trapped between the barriers for a time $\tau\approx\hbar/\Gamma$, where $\Gamma$ is the width of the transmission peak.
* Near a resonance the shape is Lorentzian (**Breit–Wigner**): $T(E)\approx\dfrac{\Gamma_L\Gamma_R}{(E-E_r)^2+(\Gamma/2)^2}$ with $\Gamma=\Gamma_L+\Gamma_R$; symmetric barriers give $T=1$ at $E_r$. The width is the *imaginary part* of a complex pole $E_r-i\Gamma/2$ of the transmission amplitude: the continuation of §4's pole from the negative real axis into the lower half-plane.

The same picture explains the **resonant-tunnelling diode**: a bias shifts $E_r$ through the Fermi level and the current peaks.

![[fig_qm08_resonant_bands.png]]
*Figure QM8.3. Resonant tunnelling and bands. A: $T(E/V_0)$ for two barriers (blue) against a single barrier (orange dashed) on a log scale: the double barrier is less transparent almost everywhere but reaches $T=1$ at the quasi-bound level $E/V_0=0.56$. B: $|\psi|^2$ on resonance (blue: flat outside, strong build-up between the barriers) and off resonance (orange: a standing wave on the left, little inside). C: the band structure of a periodic delta comb with $P=3$: the allowed bands (blue) lie around the free-particle parabola (orange dashed) and are separated by gaps at $qa=0,\pm\pi$ (§8).*

## 8. Periodic potentials: Bloch's theorem and the Kronig–Penney bands
<span class="scope-extra-beyond">extra · beyond</span> *standard solid-state theory; the delta comb is the thin-barrier limit of §3*

If $V(x+a)=V(x)$, the stationary states can be chosen as **Bloch states** $\psi(x+a)=e^{iqa}\psi(x)$ (the translation operator of [[Dirac Algebra]] §7 commutes with $H$, so its eigenvalue $e^{iqa}$ labels the state; $q$ is the **crystal momentum**, defined modulo $2\pi/a$).

> [!derivation] Kronig–Penney with delta barriers
> Take $V=\alpha\sum_n\delta(x-na)$. In $0<x<a$: $\psi=A\sin kx+B\cos kx$, $k=\sqrt{2mE}/\hbar$. Bloch's condition fixes $\psi$ in $-a<x<0$: $\psi(x)=e^{-iqa}[A\sin k(x+a)+B\cos k(x+a)]$. Continuity at $x=0$ and the delta jump $\psi'(0^+)-\psi'(0^-)=\frac{2m\alpha}{\hbar^2}\psi(0)$ give two linear equations in $A,B$, with the condition
> $$\boxed{\cos(qa)=\cos(ka)+\frac{m\alpha}{\hbar^2k}\sin(ka)=\cos y+P\,\frac{\sin y}{y},\qquad y=ka,\ \ P=\frac{m\alpha a}{\hbar^2}.}$$
> Real $q$ requires $|\cos y+P\sin y/y|\le1$: **allowed bands**; elsewhere $q$ is complex (a wave growing in one direction): **forbidden gaps**.

* **Band edges.** At $y=n\pi$ the right side is $(-1)^n$: *one edge of every band sits at the box level $y=n\pi$*, $E_n=n^2\pi^2\hbar^2/2ma^2$ (the levels of a box of width $a$).
* **Numbers** ($y/\pi$ at the edges): $P=1$: bands $[0.416,1]$, $[1.169,2]$, $[2.096,3]$; $P=3$: $[0.629,1]$, $[1.384,2]$, $[2.255,3]$; $P=10$: $[0.836,1]$, $[1.689,2]$, $[2.568,3]$. In energy units $\hbar^2\pi^2/2ma^2$, the bands for $P=3$ are $[0.40,1.00]$, $[1.92,4.00]$, $[5.09,9.00]$.
* **Limits.** $P\to0$: free particle, no gaps. $P\to\infty$: the bands shrink to the lines $y=n\pi$: isolated boxes, i.e. *tight-binding*. Larger $P$ (more opaque barriers) means narrower bands and wider gaps.
* **Why chemists care.** $N$ coupled atoms turn each atomic level into $N$ closely spaced levels: a band (the LCAO picture of [[CH02 Molecular Orbital Theory Diatomics]] and [[CH03 Molecular Orbital Theory Polyatomics]] with $N\to\infty$). Whether a solid conducts depends on whether the highest occupied band is full, and the gap is the reason an insulator is an insulator.

## 9. Unitarity: $R+T=1$ as a statement about a matrix
<span class="scope-extra-beyond">extra · beyond</span> *links to [[Dirac Algebra]] §7 and §9*

Collect the amplitudes in the **scattering matrix** $S=\begin{pmatrix}r&t'\\t&r'\end{pmatrix}$ ($r,t$: incidence from the left; $r',t'$ from the right). For a real potential, flux conservation says $S^\dagger S=\mathbf1$: $S$ is **unitary**, the same property that makes time evolution $U=e^{-iHt/\hbar}$ preserve probability. For a *symmetric* potential $t=t'$, $r=r'$, and the off-diagonal part of $S^\dagger S=1$ gives $rt^*+r^*t=0$: **$r/t$ is purely imaginary.** Check: the delta barrier has $r/t=-i\beta$ ✓; the finite well of QM07 §11 has $B/F=-i\frac{k^2-k_0^2}{2kk_0}\sin2k_0a$ ✓ (purely imaginary); the step is not symmetric, so it is exempt.

## Map of this chapter
> [!connection] How QM08 connects
> **Builds on:** [[QM07 The Finite Square Well]] (the formula for $T$ and the matching algebra), [[QM02 The Schrodinger Equation and Stationary States]] (matching conditions), [[QM03 States Operators and Measurement]], [[Dirac Algebra]] (translation operator, unitarity).
> **Concepts:** [[Probability Current]] · [[Transmission Coefficient]] · [[Reflection Coefficient]] · [[Step Potential]] · [[Rectangular Barrier]] · [[Quantum Tunnelling]] · [[Evanescent Wave]] · [[WKB Approximation]] · [[Gamow Factor]] · [[Resonant Tunnelling]] · [[Transfer Matrix]] · [[Bloch Theorem]] · [[Kronig-Penney Model]] · [[Delta Function Potential]]
> **Other subjects:** [[Inorganic Chemistry - Course Map]] (bands from MOs, STM of surfaces), [[Thermodynamics - Course Map]] (nuclear lifetimes, solar fusion rates), [[Waves - Course Map]] (frustrated total internal reflection, band gaps for waves), [[Climate - Course Map]] (the Sun's luminosity, CL03, rests on tunnelling in proton fusion).

## Summary
> [!summary] Cheat-sheet
> - **Current:** $j=\frac\hbar m\mathrm{Im}(\psi^*\psi')$, constant in $x$; $R=|r|^2$, $T=\frac{k'}{k}|t|^2$, $R+T=1$.
> - **Step ($E>V_0$):** $R=\big(\frac{k_1-k_2}{k_1+k_2}\big)^2$, $T=\frac{4k_1k_2}{(k_1+k_2)^2}$; **$E<V_0$:** $R=1$, tail $\propto e^{-\kappa x}$.
> - **Barrier ($E<V_0$):** $T=\big[1+\frac{V_0^2\sinh^2\kappa L}{4E(V_0-E)}\big]^{-1}$; thick: $T\simeq16\frac E{V_0}(1-\frac E{V_0})e^{-2\kappa L}$. Over the top: $\sinh\to\sin$, resonances at $k_2L=n\pi$.
> - **Delta:** $T=[1+m\alpha^2/2\hbar^2E]^{-1}$; the well's bound state is a pole of $t$ at $k=i m|\alpha|/\hbar^2$.
> - **WKB:** $T\simeq e^{-2\int\kappa dx}$; **Gamow:** $G=\frac{\sqrt{2\mu E}}\hbar R_c[\arccos\sqrt x-\sqrt{x(1-x)}]$, $x=R/R_c$.
> - **Numbers:** electron 1 eV / 2 eV / 0.5 nm: $T=0.024$; STM: $\times7.8$ per 0.1 nm; $^{238}$U: $2G=88$, $T_{1/2}\approx5\times10^9$ yr.
> - **Double barrier:** $T=1$ at the quasi-bound level, Breit–Wigner width $\Gamma$, lifetime $\hbar/\Gamma$.
> - **Kronig–Penney:** $\cos qa=\cos ka+\frac{m\alpha}{\hbar^2k}\sin ka$; band edges at $ka=n\pi$; $P\to\infty$ gives boxes, $P\to0$ free.
> - **Unitarity:** $S^\dagger S=1$; symmetric potential $\Rightarrow$ $r/t$ imaginary.

## Practice
1. **Step.** Find $R$ and $T$ for $E=2V_0$ and check $R+T=1$. What are $|t|^2$ and why is it larger than 1?
2. **Barrier.** An electron with $E=1$ eV meets a $V_0=2$ eV barrier of width $L=0.5$ nm. Find $\kappa$, $T$ (exact) and the thick-barrier estimate.
3. **Why not protons?** Repeat problem 2 for a proton.
4. **STM.** For $\phi=4$ eV by what factor does the tunnelling current change when the tip moves $0.1$ nm?
5. **Delta barrier.** Derive $T=[1+m\alpha^2/2\hbar^2E]^{-1}$ and find the pole of $t(k)$ for an attractive delta.
6. **Current.** Prove $dj/dx=0$ and show that $j_{\rm transmitted}/j_{\rm incident}=\frac{k'}{k}|t|^2$.
7. **Thick-barrier limit.** Show $T\to16\frac{E}{V_0}(1-\frac E{V_0})e^{-2\kappa L}$ and find where the prefactor is maximal.
8. **Gamow.** Compute $x$, $G$ and $e^{-2G}$ for $^{238}$U ($E_\alpha=4.267$ MeV, $Z_d=90$, $R=9.30$ fm, $\mu=3665$ MeV).
9. **Bands.** Show that for the delta comb one edge of each band lies at $ka=n\pi$ and find the first band for $P=3$ in units of $\hbar^2\pi^2/2ma^2$.
10. **Resonances over a barrier.** For $E=2V_0$ find the smallest barrier width with $T=1$ (units $\hbar^2/2m=1$, $V_0=1$).

> [!example]- Solutions
> 1. $k_1=\sqrt E$, $k_2=\sqrt{E-V_0}$ with $E=2V_0=2$: $k_1=1.4142$, $k_2=1$: $R=\big(\frac{0.4142}{2.4142}\big)^2=0.0294$, $T=\frac{4(1.4142)}{(2.4142)^2}=0.9706$, sum 1.0000. $t=2k_1/(k_1+k_2)=1.1716$, $|t|^2=1.373$: the transmitted *amplitude* exceeds the incident one, but the transmitted wave is slower ($k_2<k_1$), so the *current* is smaller: $T=|t|^2k_2/k_1=0.9706$.
> 2. $\kappa=5.123\,\mathrm{nm^{-1}}\sqrt{1}$, $\kappa L=2.562$. $\sinh(2.562)=\tfrac12(e^{2.562}-e^{-2.562})=6.44$, $\sinh^2=41.5$; $\frac{V_0^2}{4E(V_0-E)}=\frac{4}{4\cdot1\cdot1}=1$, so $T=1/(1+41.5)=\mathbf{0.0235}$ (the script gives 2.3549 %). Thick estimate $16\cdot\tfrac12\cdot\tfrac12\,e^{-2(2.562)}=4\times5.96\times10^{-3}=0.0238$ (1 % too high).
> 3. $\kappa_p=\kappa_e\sqrt{1836}=219.5\ \mathrm{nm^{-1}}$, $\kappa L=109.7$, $T\approx4e^{-219.5}\approx4.6\times10^{-96}$: one in $10^{95}$, i.e. never. (The mass scales the exponent by $\sqrt m$.)
> 4. $\kappa=5.123\sqrt4=10.25\ \mathrm{nm^{-1}}$; $e^{2\kappa\,\Delta d}=e^{2.05}=\mathbf{7.8}$ per 0.1 nm: the current falls by almost an order of magnitude when the tip is retracted by one ångström, which is why STM resolves atoms.
> 5. $\psi'(0^+)-\psi'(0^-)=\frac{2m\alpha}{\hbar^2}\psi(0)$ and $1+r=t$ give $ik(t-1+r)=\ldots$: $ikt-ik(1-r)=\frac{2m\alpha}{\hbar^2}t$, with $1-r=2-t$: $2ikt-2ik=\frac{2m\alpha}{\hbar^2}t\Rightarrow t=\frac{1}{1+i\beta}$, $\beta=\frac{m\alpha}{\hbar^2k}$; $T=|t|^2=\frac1{1+\beta^2}=\big[1+\frac{m\alpha^2}{2\hbar^2E}\big]^{-1}$ using $k^2=2mE/\hbar^2$. Pole where $1+i\beta=0$: $k=-im\alpha/\hbar^2$; for $\alpha<0$, $k=+im|\alpha|/\hbar^2$, $E=-m\alpha^2/2\hbar^2$.
> 6. $\frac{d}{dx}(\psi^*\psi'-\psi\psi'^*)=\psi^*\psi''-\psi\psi''^*$; with $\psi''=\frac{2m}{\hbar^2}(V-E)\psi$ and $V,E$ real both terms equal $\frac{2m}{\hbar^2}(V-E)|\psi|^2$ and cancel. Left side: $\psi=e^{ikx}+re^{-ikx}$ gives $j=\frac{\hbar k}m(1-|r|^2)$; right side $\psi=te^{ik'x}$ gives $j=\frac{\hbar k'}m|t|^2$; incident $j_{\rm in}=\hbar k/m$.
> 7. For $\kappa L\gg1$, $\sinh^2\kappa L\to\frac14e^{2\kappa L}$ and the "1" in the denominator is negligible: $T\to\frac{4E(V_0-E)}{V_0^2}\cdot4e^{-2\kappa L}$. The prefactor $16u(1-u)$ with $u=E/V_0$ is maximal at $u=\frac12$ where it equals 4.
> 8. $R_c=\frac{90\cdot2\cdot1.43996}{4.267}=60.74$ fm, $x=9.30/60.74=0.1531$, $\arccos\sqrt x=\arccos0.3913=1.1688$, $\sqrt{x(1-x)}=0.3599$, bracket $=0.8089$; $\sqrt{2\mu E}/\hbar c=\sqrt{2\cdot3665\cdot4.267}/197.327=176.9/197.327=0.8963\ \mathrm{fm^{-1}}$; $G=0.8963\times60.74\times0.8089=44.03$, $e^{-2G}=e^{-88.05}=5.8\times10^{-39}$.
> 9. At $y=n\pi$: $\sin y=0$, so the right side is $\cos n\pi=\pm1$, i.e. $\cos qa=\pm1$: $q=0$ or $\pi/a$, an edge (it is the box level). For $P=3$ the first band is $y/\pi\in[0.629,1]$, i.e. $E/(\hbar^2\pi^2/2ma^2)=(y/\pi)^2\in[0.396,1]$.
> 10. $T=1$ when $\sin(k_2L)=0$: $k_2=\sqrt{E-V_0}=1$ (units $\hbar^2/2m=1$, $E=2$, $V_0=1$), so $L=\pi=3.1416$ ($T=1.000000$, verified); the width $L=\pi/k_2$ fits exactly half a de Broglie wavelength inside the barrier region.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | scattering ansatz and the lecture's $T$ formula | [[Finite_well.pdf#page=7\|Finite_well.pdf pp.7–13]] (read as images) | taught (QM07 §11); starting point |
> | probability current, step, barrier | Griffiths §2.5–§2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=80\|PDF p.80 ff.]], section start from the Sources table) | extra/book |
> | analytic continuation $k_0\to i\kappa$, thick/thin limits, $T=1$ over the top | derived here from QM07 §11 and checked against a transfer matrix (`scripts/qm08_numbers.py`) | extra/beyond |
> | delta barrier, pole of $t$ = bound state | derived here; Griffiths §2.5 for the delta well | extra/beyond |
> | WKB and connection formulas | Sakurai §2.5.4 (printed pp.104–108, [[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf#page=124\|PDF pp.124–128]]) | extra/book |
> | Gamow factor and the $\alpha$-decay table | derived here; decay data recalled (`[verify]`) | extra/beyond |
> | STM, proton, fusion, ammonia | standard values (recalled) | extra/beyond |
> | double barrier, Breit–Wigner | transfer-matrix calculation (`scripts/qm08_numbers.py`, `scripts/fig_qm08.py`); Breit–Wigner form recalled | extra/beyond |
> | Bloch's theorem, Kronig–Penney band edges | derived here; numbers from `scripts/qm08_numbers.py` | extra/beyond |
> | unitarity of $S$ | derived here; links to [[Dirac Algebra]] | extra/beyond |
>
> **Notes.** (1) No lecture source exists for steps, barriers or tunnelling; the instructor's QM07 formula is the only taught input. (2) $\alpha$-decay half-lives, STM work function, ammonia splitting and the Sun's $kT$ are recalled values, flagged `[verify]`; every other number is computed. (3) The $^{232}$Th and $^{212}$Po estimates miss the measured values by factors of 4.4 and 0.2; the model's two free inputs (nuclear radius, assault frequency) are not tuned.

**References.** Griffiths, D. J. *Introduction to Quantum Mechanics* (1st ed.), §2.5–§2.6 · Sakurai, J. J. and Napolitano, J. *Modern Quantum Mechanics* (3rd ed.), §2.5.4 · Gamow, G. (1928) *Z. Phys.* 51, 204 · Kronig, R. de L. and Penney, W. G. (1931) *Proc. R. Soc. A* 130, 499 · Bloch, F. (1929) *Z. Phys.* 52, 555 · Binnig, G. and Rohrer, H. (1982) *Helv. Phys. Acta* 55, 726.

## Across subjects
- [[LSX1 Clocks in Rocks]] (Landscapes): tunnelling is why radioactive decay constants are fixed, and so why isotopic clocks work: the same barrier-penetration integral dates rocks.
