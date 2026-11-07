---
title: QM10 The Finite Barrier and Tutorial V
aliases: [QM10, finite barrier, barrier lecture, Tutorial V, double well, tunnel splitting]
subject: qm
type: chapter
chapter: 10
part: II
scope: [taught, extra-beyond]
by: [lecture-notes, own-notes]
status: draft
prereq: ["[[QM07 The Finite Square Well]]", "[[QM08 Quantum Tunnelling]]"]
tags: [subject/qm, type/chapter, taught, extra/beyond, src/lecture-notes, src/own-notes, status/draft]
---
# QM10 · The Finite Barrier and Tutorial V

◀ [[QM09 The Stern-Gerlach Experiment and Spin]] · [[Quantum Mechanics - Course Map|Course Map]] · related: [[QM07 The Finite Square Well]], [[QM08 Quantum Tunnelling]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map
> 🟢 **Taught:** the handwritten lecture [[Barrier.pdf#page=2|Barrier.pdf]] (7 pp., p.1 blank): the barrier on $[-a,a]$ with $E<V_0$, matching, $F/A$, $T$, $R=1-T$, tunnelling; and [[Tutorial5.pdf|Tutorial V]] (three questions). Added 2026-11-04.
> 🔵 **Extra · beyond (mine):** §2 the proof that $R=1-T$ and the phase of $t$; §3 numbers; §6 the double-well splitting law $\propto e^{-\kappa d}$ checked against exact roots; §7 extra practice. All numbers: `scripts/qm10_numbers.py`; figures: `scripts/fig_qm10.py`.
> **Overlap:** [[QM08 Quantum Tunnelling]] §3 already derived the same $T$ from the well by $k_0\to i\kappa$ with the barrier on $[0,L]$ ($L=2a$). Here the lecture's *direct* route is written out in its own notation. [[QM07 The Finite Square Well]] §11 already derives Tutorial V Q3; §5 below only re-derives it by another route and checks it.

> [!key] After this chapter you can
> - solve the barrier $E<V_0$ by matching $\psi,\psi'$ at $\pm a$ and obtain $C,D$, $F/A$ and $B/F$,
> - show $T=\big[1+\tfrac{V_0^2\sinh^2(2\kappa a)}{4E(V_0-E)}\big]^{-1}$ and $R=1-T$,
> - answer all of Tutorial V (three bound states need $V_0a^2>\pi^2\hbar^2/2m$; double-well ground states; $F/A$ and $T$ for $E>V_0$ with sketches).

> [!intuition] One sentence
> Classically a particle with $E<V_0$ bounces off; quantum mechanically the wave decays like $e^{-\kappa x}$ inside the wall and, if the wall is thin, a small plane wave emerges on the far side.

![[fig_qm10_barrier.png]]
*Figure QM10.1. A: $|\psi|^2$ for $V_0=1$, $a=1$ ($\hbar^2/2m=1$) at $E=0.5V_0$ ($T=0.211$) and $0.2V_0$ ($T=0.070$): standing-wave ripples on the left (incident plus reflected), decay in the shaded barrier, a flat tail on the right (only a transmitted wave). B: $T(E)$ for three widths is continuous through $E=V_0$; above the top $T=1$ resonances appear. C: $T$ against width on a log axis is a straight line of slope $-4\kappa$ per unit $a$, i.e. $-2\kappa$ per unit width; dashed = thick-barrier formula.*

## 1. Setup and classical expectation
Region I $x<-a$ and III $x>a$: $V=0$; region II $|x|<a$: $V=V_0$ (lecture p.2). Throw a particle from $-\infty$: for $E<V_0$ it reflects, for $E>V_0$ it crosses. Quantum mechanics changes the first statement.

**Region I, III** ($-\tfrac{\hbar^2}{2m}\psi''=E\psi$, $k=\sqrt{2mE}/\hbar$):
$$\psi_{\rm I}=Ae^{ikx}+Be^{-ikx},\qquad \psi_{\rm III}=Fe^{ikx}$$
(no wave comes from the right). **Region II** ($-\tfrac{\hbar^2}{2m}\psi''=-(V_0-E)\psi$, $\kappa=\sqrt{2m(V_0-E)}/\hbar$):
$$\psi_{\rm II}=Ce^{\kappa x}+De^{-\kappa x}.$$
Note both exponentials are kept: the region is finite, so $e^{\kappa x}$ does not blow up (contrast the bound-state tails of QM07).

## 2. Matching and the transmission amplitude
<span class="scope-taught">taught</span> *Barrier.pdf pp.4–6*

**At $x=a$:** $Ce^{\kappa a}+De^{-\kappa a}=Fe^{ika}$ and $\kappa(Ce^{\kappa a}-De^{-\kappa a})=ikFe^{ika}$. Adding and subtracting,
$$2\kappa Ce^{\kappa a}=(\kappa+ik)Fe^{ika},\quad 2\kappa De^{-\kappa a}=(\kappa-ik)Fe^{ika}\ \Rightarrow\ \boxed{C=\tfrac{\kappa+ik}{2\kappa}e^{-(\kappa-ik)a}F,\quad D=\tfrac{\kappa-ik}{2\kappa}e^{(\kappa+ik)a}F}$$
**At $x=-a$:** $Ae^{-ika}+Be^{ika}=Ce^{-\kappa a}+De^{\kappa a}$ and $ik(Ae^{-ika}-Be^{ika})=\kappa(Ce^{-\kappa a}-De^{\kappa a})$. Combining ($ik\times$first $\mp$ second):
$$2ikBe^{ika}=-(\kappa-ik)Ce^{-\kappa a}+(\kappa+ik)De^{\kappa a},\qquad 2ikAe^{-ika}=(\kappa+ik)Ce^{-\kappa a}-(\kappa-ik)De^{\kappa a}.$$
Insert $C,D$. The $A$-equation gives, using $(\kappa+ik)^2e^{\ldots}$ terms that collapse to hyperbolic functions,
$$\boxed{\frac FA=\frac{e^{-2ika}}{\cosh(2\kappa a)+i\,\dfrac{\kappa^2-k^2}{2k\kappa}\sinh(2\kappa a)}}$$
The lecture writes $\cosh(2\kappa a)+\tfrac{i\epsilon}{2}\sinh(2\kappa a)$ with $\epsilon=\tfrac{\kappa^2-k^2}{k\kappa}$ (p.5). Similarly, with $\eta=\tfrac{\kappa^2+k^2}{k\kappa}$ (p.6),
$$\boxed{B=-\tfrac{i\eta}{2}\sinh(2\kappa a)\,F}.$$
**Transmission.** $|F/A|^{-2}=\cosh^2(2\kappa a)+\tfrac{\epsilon^2}{4}\sinh^2(2\kappa a)=1+\sinh^2(2\kappa a)\big(1+\tfrac{\epsilon^2}{4}\big)$, and $1+\epsilon^2/4=\eta^2/4$ (since $4k^2\kappa^2+(\kappa^2-k^2)^2=(\kappa^2+k^2)^2$). With $\kappa^2+k^2=2mV_0/\hbar^2$ and $k^2\kappa^2=(2m/\hbar^2)^2E(V_0-E)$:
$$\boxed{T=\Big|\frac FA\Big|^2=\frac1{1+\dfrac{(k^2+\kappa^2)^2\sinh^2(2\kappa a)}{4k^2\kappa^2}}=\frac1{1+\dfrac{V_0^2\sinh^2(2\kappa a)}{4E(V_0-E)}}}$$
> [!derivation] $R=1-T$ (the lecture's "verify", p.7)
> $R=|B/A|^2=\tfrac{\eta^2}4\sinh^2(2\kappa a)\,|F/A|^2$. Since $|F/A|^{-2}=1+\tfrac{\eta^2}{4}\sinh^2(2\kappa a)$, we get $R=\dfrac{X}{1+X}$ and $T=\dfrac1{1+X}$ with $X=\tfrac{\eta^2}4\sinh^2(2\kappa a)$: $R+T=1$. Both coefficients are positive, and neither is 0 or 1 for finite $a$: the reflection is never total.

> [!derivation] Phase of the transmitted wave
> $\arg(F/A)=-2ka-\arctan\!\big[\tfrac\epsilon2\tanh(2\kappa a)\big]$. Numerically (checked): $E=0.2V_0$, $a=1$: $\arg(F/A)+2ka=-0.6169$ rad. For $E=V_0/2$, $\epsilon=0$ and the only phase is the free-propagation $-2ka$.

**Direct check.** Solving the four matching equations as a linear system for $(B,C,D,F)$ reproduces $C,D,B,F/A$ to $10^{-16}$ (three parameter sets), and $T$ equals the transfer-matrix value of QM08 (e.g. $V_0=1$, $E=0.5$, $a=0.5$: $T=0.629290$, $R=0.370710$).

## 3. Tunnelling, limits and numbers
The lecture's conclusion (p.6): $T\ne0$ for $E<V_0$ — **tunnelling**, a quantum particle crossing a classically forbidden region.

* **Thick barrier** $2\kappa a\gg1$: $\sinh^2\to\tfrac14e^{4\kappa a}$, so $T\simeq16\tfrac E{V_0}(1-\tfrac E{V_0})e^{-4\kappa a}$ ($=e^{-2\kappa L}$, $L=2a$, as in QM08).
* **Thin barrier** $2\kappa a\ll1$: $T\to\big[1+\tfrac{V_0^2(2a)^2\kappa^2}{4E(V_0-E)}\big]^{-1}\to\big[1+\tfrac{m\,\alpha^2}{2\hbar^2E}\big]^{-1}$ with $\alpha=2aV_0$ (delta barrier).
* **Over the top:** $\kappa\to ik_2$, $k_2=\sqrt{2m(E-V_0)}/\hbar$: $T=\big[1+\tfrac{V_0^2\sin^2(2k_2a)}{4E(E-V_0)}\big]^{-1}$ with $T=1$ at $2k_2a=n\pi$ (§5, Fig. QM10.1B). $T$ is continuous across $E=V_0$: at $E=V_0\pm$ with $V_0=1,a=0.5$ both sides give $T=0.8000$.

| Electron, $E=1$ eV, $V_0=2$ eV, $\kappa=5.123$ nm$^{-1}$ | $2\kappa a$ | exact $T$ | thick formula |
|---|---|---|---|
| $2a=0.2$ nm ($a=0.1$) | 1.025 | 0.404 | 0.515 (bad) |
| $2a=0.5$ nm | 2.562 | **0.0235** | 0.0238 |
| $2a=1.0$ nm | 5.123 | $1.42\times10^{-4}$ | $1.42\times10^{-4}$ |

The middle row reproduces QM08's $0.0235$ for $L=0.5$ nm.

> [!pitfall] Traps
> 1. The width in the exponent is $2a$, not $a$: $T\sim e^{-4\kappa a}$.
> 2. $\epsilon$ vanishes at $E=V_0/2$ only (where $\kappa=k$); $\eta\ge2$ always.
> 3. $T=|F/A|^2$ needs no $k'/k$ factor here because both outer regions have the same wavenumber $k$.

## 4. Tutorial V Question 1: the first three bound states of the finite well
<span class="scope-taught">taught</span> *[[Tutorial5.pdf|Tutorial V]]*

Well $|x|<a$ with $V=0$, $V=V_0$ outside (the convention of QM07 §9). Bound states have $0<E<V_0$; $k_0=\sqrt{2mE}/\hbar$, $\kappa=\sqrt{2m(V_0-E)}/\hbar$, $z=k_0a$, $z_0=a\sqrt{2mV_0}/\hbar$, $z^2+(\kappa a)^2=z_0^2$.

**Sketch.** The ground state is even, no node, one hump; the first excited is odd with a node at the centre; the second excited is even with two nodes at $\pm x_*$. Inside, $\cos k_0x$ (even) or $\sin k_0x$ (odd); outside, decay $e^{-\kappa(|x|-a)}$, with the *slope continuous* at $\pm a$ so the wave bends over the edge; each state penetrates more as its energy approaches $V_0$ (Fig. QM10.2A for $z_0=3.3$: $E=0.132,\ 0.507,\ 0.983\,V_0$).

**Existence.** Even states satisfy $\tan z=\sqrt{z_0^2/z^2-1}$, odd $-\cot z=\sqrt{z_0^2/z^2-1}$ (QM07 §3). The $n$-th state is born at $z_0=(n-1)\pi/2$ (at the birth $E=V_0$, $\kappa=0$). Three states therefore need
$$z_0>\pi\iff\frac{2mV_0a^2}{\hbar^2}>\pi^2\iff\boxed{V_0a^2>\frac{\pi^2\hbar^2}{2m}}.$$
It is strict ($z_0=\pi$ puts the third state exactly at $E=V_0$, unbound). Roots confirm it: $z_0=\pi-10^{-6}$ gives 2 states, $z_0=3.3$ gives 3 ($k_0a=1.199,\ 2.349,\ 3.272$; third node at $|x|/a=0.480$), $z_0=5$ gives 4 (the count is $\lceil2z_0/\pi\rceil$). **Numbers (electron):** $\pi^2\hbar^2/2m_e=0.3760$ eV nm$^2$, so $a=0.5$ nm needs $V_0>1.504$ eV, $a=0.2$ nm needs $V_0>9.40$ eV, $a=1$ nm needs $0.376$ eV. Physical reading: the threshold is when $V_0$ equals the *second* level of the rigid box of width $2a$, $\pi^2\hbar^2/2ma^2$.

## 5. Tutorial V Question 3: $E>V_0$ for the well ($F/A$ and $T$)
<span class="scope-taught">taught</span> · also in [[QM07 The Finite Square Well]] §11

Well region $|x|<a$ ($V=0$): $k_0=\sqrt{2mE}/\hbar$; outside ($V_0$): $k=\sqrt{2m(E-V_0)}/\hbar$, $k_0>k$. Equations (4)–(7) of the tutorial. **Elimination (compact route):** (6)$\pm$(7)/$ik_0$ at $x=a$:
$$C=\tfrac{k_0+k}{2k_0}e^{i(k-k_0)a}F,\qquad D=\tfrac{k_0-k}{2k_0}e^{i(k+k_0)a}F.$$
Insert into the $x=-a$ combination $2kAe^{-ika}=(k+k_0)Ce^{-ik_0a}+(k-k_0)De^{ik_0a}$ (from (4)$\cdot k$ + (5)$/i$):
$$2kAe^{-ika}=\frac{Fe^{ika}}{2k_0}\Big[(k+k_0)^2e^{-2ik_0a}-(k-k_0)^2e^{2ik_0a}\Big]\ \Rightarrow\ \boxed{\frac FA=\frac{4kk_0e^{-2ika}}{(k+k_0)^2e^{-2ik_0a}-(k-k_0)^2e^{2ik_0a}}}$$
(the $e^{ika}$ on the right moves to the left as $e^{-2ika}$ after dividing by $2kAe^{-ika}$.)
**Transmission.** $|{\rm den}|^2=(k+k_0)^4+(k-k_0)^4-2(k^2-k_0^2)^2\cos4k_0a=16k^2k_0^2+4(k^2-k_0^2)^2\sin^2 2k_0a$, so
$$\boxed{T=\frac1{1+\dfrac{V_0^2}{4E(E-V_0)}\sin^2\!\Big(\dfrac{2a}{\hbar}\sqrt{2mE}\Big)}}$$
using $k_0^2-k^2=2mV_0/\hbar^2$, $k^2k_0^2=(2m/\hbar^2)^2E(E-V_0)$. Solving the four equations numerically at $E/V_0=1.001,\,1.579,\,2,\,4,\,10$ ($z_0=5$) reproduces (8) and (9) to $10^{-16}$: $T=0.013148,\ 1.000000,\ 0.888891,\ 0.982932,\ 0.999883$, with $R=1-T$.

**Sketches (Fig. QM10.2E, F).**
* **$T=1$:** $\sin(2k_0a)=0$, i.e. $2k_0a=n\pi$ ($E/V_0=(2\pi/5)^2=1.579$ for $z_0=5$, $n=4$): no reflected wave, so $|\psi|^2$ is flat $=|A|^2$ in I and III; Re$\,\psi$ is a pure cosine of wavenumber $k$ there, and inside the well fits a whole number of half-wavelengths ($2\cdot2\pi=4\pi$).
* **$T<1$** (e.g. $E=2V_0$, $T=0.889$): region I has a standing-wave ripple of $|\psi|^2$ between $(1\pm\sqrt R)^2=(1\pm0.333)^2$, i.e. $0.44$ and $1.78$; region III is a flat $|F|^2=0.889$ travelling wave; inside the well the amplitude changes at the interfaces. Optical analogue: an anti-reflection coating.

## 6. Tutorial V Question 2: the double well
<span class="scope-taught">taught</span> *Tutorial5.pdf; the quantitative law is* <span class="scope-extra-beyond">extra · beyond</span>

Two wells of width $w$ ($V=0$) separated by a barrier of width $d$ and height $V_0$, with $V_0$ also outside. The ground state is **even** (no node, as always for the lowest state; QM04 parity theorem).

* **(a) $d\ll w$.** The thin barrier is a small perturbation of one well of width $2w$: the ground state looks like the single wide-well ground state (a half-sine hump) with a small **dip** at the centre where the barrier cuts the wave, and exponential tails outside. Numerically ($V_0=20$, $w=1$, $\hbar^2/2m=1$): at $d=10^{-4}$, $E_0=1.641$ against $1.639$ for a single well of width $2w$.
* **(b) $d\gg w$.** The wells decouple: the ground state is two *equal* humps, one per well, each like the single-well ground state of width $w$ ($E=4.590$), with a tiny, node-free exponential bridge across the barrier. The **odd** partner has the same humps with opposite signs and a node at the centre. Fig. QM10.2B, C.

> [!derivation] Why the two lowest levels split
> The even state in the barrier is $\cosh\kappa x$, the odd one $\sinh\kappa x$. Matching the log-derivative at $x=d/2$ to the well solution gives for the exact levels $\psi'/\psi=\kappa\tanh(\kappa d/2)$ (even) and $\kappa\coth(\kappa d/2)$ (odd). For $\kappa d\gg1$ they differ by $\approx 4\kappa e^{-\kappa d}$, so the energy splitting is $\propto e^{-\kappa d}$. Verified: from $d=2$ to $5$, the slope of $\ln(E_1-E_0)$ versus $d$ is $-3.92556$, against $-\kappa=-3.92556$ ($\kappa=\sqrt{V_0-E}$ at the single-well energy). Values: $d=1$: $E_0=4.5429$, $E_1=4.6371$ (splitting $0.0942$); $d=3$: $3.67\times10^{-5}$; $d=5$: $1.43\times10^{-8}$. The even state is the lower one: the ground state of the double well lies **below** the single-well level ($E_0<4.590$): that is the energy lowering that makes covalent bonds (H$_2^+$) and the ammonia inversion doublet.

![[fig_qm10_tutorial.png]]
*Figure QM10.2. Tutorial V. A: the three bound states of the well for $z_0=3.3$ (offset by their energies). B, C: ground states of the double well for $d=0.1w$ (single wide hump with a central dip) and $d=3w$ (two lobes; dashed: the odd state with an opposite lobe, almost degenerate). D: the splitting $E_1-E_0$ is a straight line on a log axis with slope $-\kappa$. E, F: the well at $E>V_0$ ($z_0=5$): $T=1$ gives flat $|\psi|^2$; $E=2V_0$ gives ripples on the left and $T=0.889$.*

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Tunnelling through a barrier: transmission and the standing-wave pattern
> A plane wave of energy E hits a rectangular barrier of height V₀ and width 2a (units ħ²/2m = 1).
>
> ![[qm_tunnelling.png|720]]
>
> **Try:** Make the barrier wider: T falls like e^{−4κa}. Raise E above V₀: T oscillates and reaches 1 when 2qa = nπ.
>
> [▶ Open the tool in your browser](../Assets/interactive/qm_tunnelling.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/qm_tunnelling.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Summary
> [!summary] Cheat-sheet
> - **Barrier $E<V_0$ on $[-a,a]$:** $\psi_{II}=Ce^{\kappa x}+De^{-\kappa x}$; $\frac FA=\frac{e^{-2ika}}{\cosh2\kappa a+i\frac{\kappa^2-k^2}{2k\kappa}\sinh2\kappa a}$; $B=-\frac{i}{2}\frac{\kappa^2+k^2}{k\kappa}\sinh(2\kappa a)F$.
> - $T=\big[1+\frac{V_0^2\sinh^2(2\kappa a)}{4E(V_0-E)}\big]^{-1}$, $R=1-T$; thick: $16\frac E{V_0}(1-\frac E{V_0})e^{-4\kappa a}$; over the top $\sinh\to\sin$.
> - **Q1:** three bound states iff $z_0>\pi$, i.e. $V_0a^2>\pi^2\hbar^2/2m$.
> - **Q2:** thin barrier $\to$ one wide well with a dip; thick barrier $\to$ two lobes, splitting $\sim e^{-\kappa d}$.
> - **Q3:** $\frac FA=\frac{4kk_0e^{-2ika}}{(k+k_0)^2e^{-2ik_0a}-(k-k_0)^2e^{2ik_0a}}$, $T=[1+\frac{V_0^2}{4E(E-V_0)}\sin^2(2a\sqrt{2mE}/\hbar)]^{-1}$.

> **Concepts:** [[Rectangular Barrier]] · [[Quantum Tunnelling]] · [[Transmission Coefficient]] · [[Reflection Coefficient]] · [[Double Well Potential]] · [[Tunnel Splitting]] · [[Transmission Resonance]] · [[Bound State]] · [[Evanescent Wave]]

## Practice
1. **Barrier numbers.** $V_0=1$, $E=0.5$, $a=0.5$ ($\hbar^2/2m=1$): find $\kappa$, $k$, $T$, $R$.
2. **Electron.** $E=1$ eV, $V_0=2$ eV, $2a=0.3$ nm: find $T$.
3. **$R=1-T$.** Prove it from $|B/A|^2$.
4. **Phase.** Find $\arg(F/A)$ for $E=0.2V_0$, $a=1$ ($V_0=1$).
5. **Three states.** For $a=0.3$ nm what is the minimum $V_0$ (eV) for three bound states of an electron?
6. **Birth of a state.** Show the fourth bound state appears at $z_0=3\pi/2$.
7. **Resonance.** For the well at $z_0=5$ list the resonances $T=1$ with $E>V_0$ below $E=10V_0$.
8. **Double well.** Why does the splitting vanish as $d\to\infty$? Estimate the ratio of splittings between $d=2$ and $d=3$ ($V_0=20,w=1$).
9. **Odd partner.** Explain which of $\cosh\kappa x$, $\sinh\kappa x$ the ground state of the double well uses in the barrier.

> [!example]- Solutions
> 1. $\kappa=k=\sqrt{0.5}=0.7071$; $2\kappa a=0.7071$; $\sinh=0.7675$, $\sinh^2=0.5890$; $V_0^2/4E(V_0-E)=1$; $T=1/1.5890=\mathbf{0.6293}$, $R=0.3707$ (matches the script).
> 2. $\kappa=5.123$ nm$^{-1}$, $2\kappa a=1.537$; $\sinh^2(1.537)=4.918$, prefactor 1: $T=1/5.918=\mathbf{0.169}$.
> 3. See §2: $R=X/(1+X)$, $T=1/(1+X)$.
> 4. $\epsilon=1.5$, $\kappa=\sqrt{0.8}$, $2\kappa a=1.789$, $\tanh=0.9456$: correction $-\arctan(0.75\times0.9456)=-0.6169$; $2ka=2\sqrt{0.2}=0.894$. So $\arg(F/A)=-0.894-0.617=\mathbf{-1.511}$ rad.
> 5. $0.3760/(0.3)^2=\mathbf{4.18}$ eV.
> 6. $n$-th state born at $z_0=(n-1)\pi/2$: $n=4\Rightarrow3\pi/2=4.712$; at $z_0=5$ there are 4 states ✓.
> 7. $T=1$ at $2k_0a=n\pi$, $k_0a=n\pi/2$ with $E/V_0=(n\pi/2z_0)^2$: $n=4$: $1.579$; $n=5$: $2.467$; $n=6$: $3.553$; $n=7$: $4.836$; $n=8$: $6.317$; $n=9$: $7.995$; $n=10$: $9.870$ ($n=3$: $0.888<1$ is a sub-barrier box level, not a scattering resonance).
> 8. The barrier overlap is $e^{-\kappa d}\to0$. Ratio $\approx e^{\kappa\cdot1}$: $0.001859/3.668\times10^{-5}=50.7$ against $e^{3.9256}=50.7$ ✓.
> 9. $\cosh\kappa x$ (even, no node); $\sinh\kappa x$ is the odd partner with a node at $x=0$.

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | Barrier setup, $C,D,A,B$, $F/A$, $\eta,\epsilon$, $T$, $R=1-T$, tunnelling | [[Barrier.pdf#page=2\|Barrier.pdf pp.2–7]] (handwritten, read as images; p.1 blank) | taught |
> | Three questions | [[Tutorial5.pdf\|Tutorial V]] | taught |
> | Proof of $R=1-T$, phase, thick/thin limits, numbers | derived and checked (`scripts/qm10_numbers.py`) | extra/beyond |
> | Double-well splitting law, exact roots | derived and checked (`scripts/qm10_numbers.py`, `scripts/fig_qm10.py`) | extra/beyond |
>
> **Notes.** (1) Lecture p.7 leaves "$R=1-T=|B/A|^2$ (verify)" open: verified here. (2) The lecture's $B$ in terms of $F$ (p.6) is correct as written (checked numerically). (3) Tutorial V's wells: the picture shows $V_0$ also outside both wells; $d$ and $w$ are widths. (4) The page-5 box for $C$ and $D$ uses the same $e^{\mp(\kappa\mp ik)a}$ phases as here.

**References.** Griffiths, D. J. *Introduction to Quantum Mechanics* §2.5–§2.6 · [[QM07 The Finite Square Well]] · [[QM08 Quantum Tunnelling]].
