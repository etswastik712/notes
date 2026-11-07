---
title: QM07 The Finite Square Well
aliases: [QM07, finite well, finite square well, bound states, quantum tunnelling tails]
subject: qm
type: chapter
chapter: 7
part: II
scope: [taught, extra-book, extra-beyond]
by: [slides, book, own-notes]
status: draft
prereq: ["[[QM04 The Particle in a Box]]", "[[QM02 The Schrodinger Equation and Stationary States]]"]
tags: [subject/qm, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/own-notes, status/draft]
---
# QM07 · The Finite Square Well

◀ [[QM06 The Oscillator Toolbox]] · [[Quantum Mechanics - Course Map|Course Map]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

<!-- qm07-patch-v1 -->
> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **Taught** (the instructor's handwritten lecture [[Finite_well.pdf#page=2|Finite_well.pdf]], 13 pp., p.1 blank, and [[tutorial4.pdf|Tutorial IV]]; added 2026-10-27/28). **This is a different convention from §1–§8 below:** the lecture puts the **floor of the well at $E=0$** and the walls at $V_0$, so bound states have $0<E<V_0$ and $k_0=\sqrt{2mE}/\hbar$ (see the dictionary box after the story). What the lecture covers, and where it is written up here:
> - §9 the bound-state derivation in the lecture's notation: outside $\kappa$ (p.2), inside $k_0$ (p.3), even/odd matching $\kappa/k_0=\tan k_0a$ and $\kappa/k_0=-\cot k_0a$ (pp.3–4), the graph (p.5), the deep/wide and shallow/short limits (p.6): *always an even state, maybe no odd state*
> - §10 **Tutorial IV**: the exact shape of $\kappa/k_0$ (value, slope, curvature)
> - §11 $E>V_0$: the scattering solution, matching at $x=\mp a$, the algebra for $B/F$, $F/A$, $|F/A|^2$, $T+R=1$, resonances (pp.7–13)
> - §12 a visual revision sheet (all figures in one place, "if you see X, think Y")
>
> *Sections §1–§8 were written first from Griffiths and are kept in full; their derivations are the same physics in the other energy convention, so §9 is the quickest route to exactly what was lectured.*
>
> 🟡 **Extra · book**: In the core lecture course, [[QM04 The Particle in a Box]] treated the infinite square well with perfectly rigid, impenetrable walls ($V = \infty$ outside). The finite square well relaxes this unphysical idealisation to a finite barrier height $V_0$. The same material is lectured in the handwritten [[Finite_well.pdf|Finite Well lecture notes]] (pp. 2–13; §9–§11 below) and treated comprehensively in Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=78|PDF pp. 78–85]]).
> - §1 Setup, potential definition, energy regimes, and classical turning points (Griffiths §2.6, [[Finite_well.pdf#page=2|Finite Well notes p. 2]])
> - §2 The TISE in all three regions, matching boundary conditions, and parity (Griffiths §2.6, [[Finite_well.pdf#page=2|Finite Well notes pp. 2–4]])
> - §3 Transcendental eigenvalue equations, dimensionless variables $z$ and $z_0$, and graphical circle intersections (Griffiths §2.6, [[Finite_well.pdf#page=3|Finite Well notes pp. 3–5]])
> - §4 Counting bound states, the 1-D theorem (always at least one bound state), and wide/shallow limits (Griffiths §2.6 pp. 82–84)
> - §5 Normalised wavefunctions, penetration depth $d_\mathrm{pen} = 1/\kappa$, and tunnelling into classically forbidden zones (Griffiths §2.6 pp. 84–85)
>
> 🔵 **Extra · beyond** (advanced topics and applications, labelled)
> - §4 3-D contrast: why the centrifugal barrier and radial origin condition require a threshold depth for spherical wells; §6 Real-world physical applications with exact numbers: GaAs/AlGaAs semiconductor quantum wells, the nuclear deuteron ($^2$H), and nanoscale metallic wells; §7 Rigorous limits to the infinite well ($V_0\to\infty$) and to the Dirac delta potential ($V_0\to\infty, a\to0$ with $2V_0 a = \alpha$), plus transmission resonances; §8 Sakurai's momentum-space integral formulation $\langle p|V|p'\rangle$ using [[Dirac Algebra]] (Sakurai & Napolitano §2.5); numerical tables computed with high precision (`scripts/qm07_numbers.py`).

> [!key] After this chapter you can
> - write down the TISE in all three regions and apply the **continuity boundary conditions** on $\psi$ and $\psi'$, explaining why $\psi''$ suffers a finite step jump while $\psi'$ remains smooth,
> - use the **parity theorem** ($[\hat{P}, \hat{H}] = 0$) to decouple the problem into independent even-parity and odd-parity branches,
> - **derive from scratch** the transcendental eigenvalue equations $z\tan z = \sqrt{z_0^2-z^2}$ (even states) and $-z\cot z = \sqrt{z_0^2-z^2}$ (odd states),
> - determine the allowed bound-state energies graphically as intersections between trigonometric branches and a quarter-circle of radius $z_0 = \frac{a}{\hbar}\sqrt{2mV_0}$,
> - compute the total number of bound states using the floor formula $N = \lfloor z_0 / (\pi/2) \rfloor + 1$ and **prove** that in one dimension there is always at least one bound state, no matter how shallow or narrow the well,
> - contrast 1-D binding with 3-D spherical wells, explaining why the radial condition $u(0)=0$ requires a finite threshold $z_0 > \pi/2$ for binding,
> - calculate the **penetration depth** $d_\mathrm{pen} = 1/\kappa$ and the **tunnelling probability** $P_\mathrm{tunnel}$ into the classically forbidden barrier,
> - explain physically why finite-well bound state energies lie strictly **below** the corresponding infinite-well energies via the "effective box width" $2a_\mathrm{eff} = 2a + 2/\kappa$,
> - take the mathematical limits $V_0 \to \infty$ (recovering the rigid box) and $a \to 0$ with $2V_0 a = \alpha$ (recovering the single bound state of the Dirac delta well),
> - formulate the eigenvalue problem in **momentum space** as an integral equation with a $\mathrm{sinc}( (p-p')a/\hbar )$ kernel following Sakurai §2.5.

> [!intuition] The one-sentence story
> Lowering the infinite walls to a finite depth $V_0$ allows the quantum wave to leak exponentially into the classically forbidden barriers; this penetration effectively widens the box, lowers every discrete energy level below its rigid-box counterpart, and limits the bound states to a finite number—yet in one dimension, the quarter-circle of well strength always captures at least one bound state.

![[QM07 Finite Well Map.svg]]
*Diagram QM7.0. The chapter in one picture: the well, the matching conditions, the quantisation graph, the limits, the leak into the walls, and (for $E>V_0$) the scattering and its resonances. Editable source: [[QM07 Finite Well Map.excalidraw]].*

> [!intuition] Five ways to *see* the finite well (read these before the algebra)
> 1. **A guitar string whose ends are not clamped.** In the box the wave is pinned to zero at the walls. In the finite well the walls are soft: the wave keeps going a little way, dying off exponentially. A string with soft ends is effectively *longer*, so its notes are *lower* than for clamped ends. That one sentence is the whole result "finite-well energies lie below the box energies".
> 2. **The handshake at the wall.** Inside, $\psi$ is a sine/cosine bending *towards* the axis; outside it is an exponential bending *away* from it. At $x=a$ the two curves must agree in height *and* slope. The ratio slope/height, $\psi'/\psi$ (the *logarithmic derivative*), is what is matched, and that ratio is $-k_0\tan k_0a$ inside and $-\kappa$ outside. Quantisation is "the two ratios are equal".
> 3. **A rope bridge you can only cross at certain tensions.** Pull the energy $E$ up: inside, the wave winds faster ($k_0$ grows); outside, the exponential gets flatter ($\kappa$ shrinks). Only at special $E$ do inside and outside meet with equal slope. Between these energies there is no solution that also decays at $\pm\infty$.
> 4. **The graph is a seesaw.** Left side $\tan k_0a$ climbs from 0 to $\infty$ on each branch; right side $\kappa/k_0$ slides down from $\infty$ to 0 as $E$ runs from 0 to $V_0$. A climbing curve and a falling curve **must cross once on every branch** — that crossing *is* a bound state. No algebra is needed to see that deeper wells have more branches under the falling curve.
> 5. **Counting by half-turns.** Each time the well gets strong enough to fit one more *quarter-wave* ($z_0$ grows by $\pi/2$) one more state is allowed, alternately even and odd. A cheap number: for an electron, $z_0\approx5.12\,a[\mathrm{nm}]\sqrt{V_0[\mathrm{eV}]}$ and $N=\lceil 2z_0/\pi\rceil\approx\lceil3.26\,a\sqrt{V_0}\rceil$.

> [!key] Dictionary between the lecture's convention and Griffiths' (used in §1–§8)
> | | **Lecture** ([[Finite_well.pdf#page=2\|p.2]]) | **Griffiths / §1–§8** |
> |---|---|---|
> | potential | $V=0$ for $\|x\|<a$, $V=V_0$ outside | $V=-V_0$ for $\|x\|<a$, $V=0$ outside |
> | bound states | $0<E<V_0$ | $-V_0<E<0$ |
> | inside wavenumber | $k_0=\sqrt{2mE}/\hbar$ | $l=\sqrt{2m(E+V_0)}/\hbar$ |
> | outside decay constant | $\kappa=\sqrt{2m(V_0-E)}/\hbar$ | $\kappa=\sqrt{-2mE}/\hbar$ (the same number) |
> | scattering | $E>V_0$, outside wavenumber $k=\sqrt{2m(E-V_0)}/\hbar$ | $E>0$, outside $k=\sqrt{2mE}/\hbar$ |
> | quantisation | $\kappa/k_0=\tan k_0a$ and $\kappa/k_0=-\cot k_0a$ | $z\tan z=\sqrt{z_0^2-z^2}$ and $-z\cot z=\sqrt{z_0^2-z^2}$ with $z=la$ |
>
> They are the same equations: $z=k_0a=la$, $z_0=a\sqrt{2mV_0}/\hbar$ (identical), $\kappa a=\sqrt{z_0^2-z^2}$, and **$E_{\rm Griffiths}=E_{\rm lecture}-V_0$**. The lecture's figure on p.2 labels the walls $\pm a/2$ while its algebra matches at $x=\pm a$; this chapter uses the algebra (half-width $a$, full width $2a$).

> [!pitfall] Five mistakes that cost marks
> 1. **Mixing the two energy origins** (quoting $E_1=0.07V_0$ as a binding energy). From the floor $E_1/V_0=z_1^2/z_0^2$; from the top of the walls $E_1/V_0=z_1^2/z_0^2-1$.
> 2. **Using $a$ for the full width.** $a$ is the *half*-width: $z_0^2=2mV_0a^2/\hbar^2$, and the rigid-box levels it tends to are those of width $2a$, $E_n=n^2\pi^2\hbar^2/2m(2a)^2=n^2\pi^2\hbar^2/8ma^2$.
> 3. **Imposing continuity of $\psi''$.** Only $\psi$ and $\psi'$ are continuous across a *finite* step; $\psi''$ jumps by $2mV_0\psi(a)/\hbar^2$.
> 4. **Counting states with $\lfloor2z_0/\pi\rfloor+1$.** That fails exactly when $z_0$ is a multiple of $\pi/2$; use $N=\lceil2z_0/\pi\rceil$ (a state at $z_0=m\pi/2$ is born *at* the top, with zero binding).
> 5. **Dropping the exponential tails when normalising**: $\int|\psi|^2$ over the well alone is not 1; the tails carry $P_{\rm out}$ (0.2 % to 64 % in the examples of §6).

## 1. The finite square well: setup and classical picture
<span class="scope-extra-book">extra · book</span> *Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=78|PDF p. 78]]); [[Finite_well.pdf#page=2|Finite Well notes p. 2]]*

> [!intuition] What actually changes from the box
> Same valley, softer sides. Three things follow without any calculation: (i) the particle can be found *outside* the classical turning points, (ii) there are only finitely many bound states (a thin enough or shallow enough valley is full after a few levels), (iii) above the rim the particle is free, so the discrete ladder gives way to a continuum. Everything in this chapter is a quantitative version of these three sentences.

In [[QM04 The Particle in a Box]], we considered an idealised potential where the potential energy jumps to infinity at the walls. In any realistic physical system, potential barriers are finite. The simplest model capturing finite confinement while maintaining piecewise constancy is the **symmetric finite square well** of width $2a$ and depth $V_0 > 0$:

$$V(x) = \begin{cases} -V_0, & |x| \le a \quad \text{(Region II: interior well)} \\ 0, & |x| > a \quad \text{(Regions I and III: exterior barriers)} \end{cases}$$

Here, the origin $x=0$ is chosen at the center of the well, making the potential symmetric: $V(-x) = V(x)$. The bottom of the well sits at $-V_0$, and the potential outside is chosen as the reference energy zero ($V = 0$).

```
                V(x)
                 |
     Region I    |    Region III
      V = 0      |      V = 0
  ---------------+---------------  E = 0 (Continuum threshold)
        :        |        :
        :   -a   |   +a   :
  ......:........|........:......  E (Bound state, -V0 < E < 0)
        |        |        |
        |<- 2a ->|        |
        +--------+--------+  V = -V_0
            Region II
```

### The classical picture
Classically, a particle of mass $m$ with total energy $E$ inside this potential moves according to $E = \frac{p^2}{2m} + V(x)$.
1. **Trapped particle ($-V_0 < E < 0$):** In the exterior regions $|x| > a$, the kinetic energy would be $T = E - V(x) = E < 0$, which is classically impossible ($p = \sqrt{2mE}$ would be imaginary). The particle is strictly confined to the interior valley $|x| \le a$, bouncing back and forth between the two sharp barriers at $x = -a$ and $x = +a$ with constant speed $v = \sqrt{2(E+V_0)/m}$. The positions $x = \pm a$ are the **classical turning points**. Classically, the probability of finding the particle outside the well is identically zero:
   $$P_\mathrm{cl}(|x| > a) = 0.$$
2. **Unbound particle ($E > 0$):** The kinetic energy $T = E - V(x) > 0$ everywhere. A particle incident from $-\infty$ slows down from speed $v_\mathrm{in} = \sqrt{2(E+V_0)/m}$ to $v_\mathrm{out} = \sqrt{2E/m}$ as it climbs out of the well at $x = +a$, continuing to $+\infty$ with $100\%$ transmission. Classically, there is zero reflection over an attractive well.

### Why we study the finite square well
Despite its discontinuous rectangular edges, the finite square well is one of the most widely applied models across physics:
- **Semiconductor heterostructures (Quantum Wells):** Sandwiching a thin layer of gallium arsenide ($\mathrm{GaAs}$) between two layers of aluminium gallium arsenide ($\mathrm{Al}_x\mathrm{Ga}_{1-x}\mathrm{As}$) creates a conduction-band offset $\Delta E_c \approx 0.3$ eV. For an active layer of thickness $2a = 10$ nm, electrons are trapped in an almost ideal 1-D finite square well, forming discrete subbands used in semiconductor lasers and Quantum Well Infrared Photodetectors (QWIPs).
- **Nuclear physics (The Deuteron):** The deuteron is a bound state of one proton and one neutron held together by the strong nuclear force. The simplest central-potential model of the nucleon-nucleon interaction is an attractive square well with depth $V_0 \approx 35$ MeV and range $a \approx 1$–$2$ fm.
- **Molecular physics and quantum dots:** The potential experienced by $\pi$-electrons along conjugated polyenes or inside colloidal semiconductor nanocrystals is capped by the finite work function or ionization potential of the material.

### The three energy regimes in quantum mechanics
The time-independent Schrödinger equation (TISE) dictates three fundamentally distinct physical regimes:
1. **$E < -V_0$ (Strictly forbidden):** Since $-V_0$ is the global minimum of $V(x)$, any state with $E < -V_0$ would have $\psi''/\psi = \frac{2m}{\hbar^2}(V(x)-E) > 0$ everywhere in space. As proven in [[QM04 The Particle in a Box]] §6 ($E \ge V_\mathrm{min}$ theorem), any non-trivial solution curves away from the axis everywhere, diverging exponentially as $x \to \pm\infty$. Such wavefunctions cannot be normalised, so **no physical states exist for $E \le -V_0$**.
2. **$-V_0 < E < 0$ (Bound states):** The kinetic energy inside the well is positive ($E + V_0 > 0$), producing oscillatory, standing-wave solutions. Outside the well, $E < 0$, so the kinetic energy is formally negative, producing decaying exponential tails. Normalisability ($\int_{-\infty}^\infty |\psi|^2 dx = 1$) requires the wavefunction to vanish at $\pm\infty$. As we will prove, matching these solutions at the boundaries quantises the energy into a **finite, discrete spectrum** $\{E_1, E_2, \dots, E_N\}$.
3. **$E > 0$ (Scattering states):** The energy exceeds the barrier height. The solutions oscillate in all three regions, extending to infinity as traveling plane waves. The spectrum is **continuous** for all $E > 0$. The particle exhibits quantum reflection and transmission resonances (the Ramsauer-Townsend effect).

![[fig_qm07_well.png]]
*Figure QM7.1. Potential energy diagram, boundary definitions, and physical regimes of the symmetric finite square well. A: The potential profile $V(x)$ showing well depth $V_0$ and half-width $a$, separating Region I ($x < -a$, barrier), Region II ($-a \le x \le a$, well floor at $-V_0$), and Region III ($x > a$, barrier). B: The three energy regimes: the strictly forbidden zone $E < -V_0$ (violating the minimum potential theorem), the discrete bound-state spectrum $-V_0 < E < 0$ where bound states possess oscillatory cores and exponential evanescent tails, and the continuous scattering spectrum $E > 0$. C: The classical turning points at $x = \pm a$, contrasting the absolute classical confinement ($P_\mathrm{cl} = 0$ for $|x|>a$) with the quantum evanescent penetration depth $d_\mathrm{pen} = 1/\kappa$.*

## 2. The TISE in all three regions and boundary conditions
<span class="scope-extra-book">extra · book</span> *Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=78|PDF p. 78]]); [[Finite_well.pdf#page=2|Finite Well notes pp. 2–4]]*

> [!intuition] Why the wave must curve *away* outside and *towards* the axis inside
> The Schrödinger equation says $\psi''/\psi=2m(V-E)/\hbar^2$. Where $E>V$ (inside) the right side is negative, so $\psi$ curves back to the axis: sine/cosine. Where $E<V$ (outside) it is positive, so $\psi$ curves away from the axis: if it were not exactly the decaying exponential it would blow up (a growing tail is not normalisable). The only freedom left is the ratio of the amplitudes, which the matching at the wall fixes — and *that* is where the quantisation hides.

We now formulate the bound-state problem ($-V_0 < E < 0$) by solving the 1-D time-independent Schrödinger equation:
$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi(x) = E\psi(x).$$

### Region II: Inside the well ($|x| \le a$, $V = -V_0$)
Inside the well, the potential is $-V_0$, so:
$$-\frac{\hbar^2}{2m}\psi''(x) - V_0\psi(x) = E\psi(x) \implies \psi''(x) = -\frac{2m(E+V_0)}{\hbar^2}\psi(x).$$
Since $-V_0 < E < 0$, the quantity $E + V_0$ is strictly positive. We define the real, positive internal wavenumber $l$:
$$l \equiv \frac{\sqrt{2m(E+V_0)}}{\hbar} > 0.$$
The TISE becomes the standard harmonic oscillator / free-wave differential equation:
$$\psi''(x) = -l^2\psi(x),$$
whose general solution is an oscillatory linear combination of sine and cosine:
$$\psi_\mathrm{II}(x) = A\sin(lx) + B\cos(lx), \qquad (|x| \le a).$$

### Regions I and III: Outside the well ($|x| > a$, $V = 0$)
Outside the well, the potential is zero, so:
$$-\frac{\hbar^2}{2m}\psi''(x) = E\psi(x) \implies \psi''(x) = -\frac{2mE}{\hbar^2}\psi(x).$$
Because $E < 0$, the coefficient $-2mE/\hbar^2$ is strictly positive. We define the real, positive decay constant (attenuation wavenumber) $\kappa$:
$$\kappa \equiv \frac{\sqrt{-2mE}}{\hbar} > 0.$$
The TISE becomes:
$$\psi''(x) = \kappa^2\psi(x),$$
whose general solutions are real exponentials:
- **Region I ($x < -a$):** $\psi_\mathrm{I}(x) = C e^{\kappa x} + D e^{-\kappa x}$. As $x \to -\infty$, the term $e^{-\kappa x}$ diverges exponentially. To keep the wavefunction square-integrable (normalisable), we must set $D = 0$:
  $$\psi_\mathrm{I}(x) = C e^{\kappa x}, \qquad (x < -a).$$
- **Region III ($x > a$):** $\psi_\mathrm{III}(x) = F e^{\kappa x} + G e^{-\kappa x}$. As $x \to +\infty$, the term $e^{\kappa x}$ diverges exponentially. Normalisability requires $F = 0$:
  $$\psi_\mathrm{III}(x) = G e^{-\kappa x}, \qquad (x > a).$$

### Boundary conditions: continuity of $\psi$ and $\psi'$
At the well boundaries $x = \pm a$, the potential $V(x)$ experiences a finite step jump of magnitude $V_0$. What conditions must $\psi(x)$ satisfy across these boundaries?

> [!derivation] Continuity of $\psi$ and $\psi'$, and the finite jump of $\psi''$
> Consider integrating the TISE $-\frac{\hbar^2}{2m}\psi''(x) + V(x)\psi(x) = E\psi(x)$ across an infinitesimal interval $[a-\epsilon, a+\epsilon]$ centered at the boundary $x=a$:
> $$\int_{a-\epsilon}^{a+\epsilon} \psi''(x)\,dx = \frac{2m}{\hbar^2}\int_{a-\epsilon}^{a+\epsilon} [V(x) - E]\psi(x)\,dx.$$
> The left-hand side is the exact derivative difference:
> $$\psi'(a+\epsilon) - \psi'(a-\epsilon) = \frac{2m}{\hbar^2}\int_{a-\epsilon}^{a+\epsilon} [V(x) - E]\psi(x)\,dx.$$
> Since $V(x)$ has a finite step jump from $-V_0$ to $0$, the integrand $[V(x)-E]\psi(x)$ is bounded throughout the interval (assuming $\psi(x)$ is physically bounded). Therefore, as $\epsilon \to 0$, the integral of a bounded function over an interval of length $2\epsilon$ vanishes identically:
> $$\lim_{\epsilon \to 0} \left[ \psi'(a+\epsilon) - \psi'(a-\epsilon) \right] = 0 \implies \psi'(a^+) = \psi'(a^-).$$
> **The first derivative $\psi'(x)$ is continuous everywhere across a finite potential step.**
>
> Integrating $\psi'(x)$ once more over $[a-\epsilon, a+\epsilon]$ immediately guarantees that **$\psi(x)$ itself is continuous**:
> $$\psi(a+\epsilon) - \psi(a-\epsilon) = \int_{a-\epsilon}^{a+\epsilon} \psi'(x)\,dx \to 0 \implies \psi(a^+) = \psi(a^-).$$
>
> **What about the second derivative $\psi''(x)$?** From the TISE, $\psi''(x) = \frac{2m}{\hbar^2}[V(x)-E]\psi(x)$. Evaluating just inside and just outside $x=a$:
> $$\psi''(a^-) = -\frac{2m(E+V_0)}{\hbar^2}\psi(a), \qquad \psi''(a^+) = -\frac{2mE}{\hbar^2}\psi(a).$$
> The difference across the interface is:
> $$\Delta \psi'' \equiv \psi''(a^+) - \psi''(a^-) = \frac{2mV_0}{\hbar^2}\psi(a) \ne 0.$$
> Thus, while $\psi(x)$ and $\psi'(x)$ are continuous, **$\psi''(x)$ suffers a finite jump discontinuity** proportional to the step height $V_0$. Only for an infinite barrier ($V_0 \to \infty$) does $\psi'(x)$ become discontinuous.

### Parity classification
The potential is symmetric under spatial inversion: $V(-x) = V(x)$. By the parity theorem established in [[QM04 The Particle in a Box]] §6:
$$[\hat{P}, \hat{H}] = 0.$$
Because bound states in a one-dimensional potential are non-degenerate (proven in [[QM05 The Harmonic Oscillator]] §7), every energy eigenstate must also be an eigenstate of the parity operator $\hat{P}$:
$$\psi(-x) = \pm \psi(x).$$
This splits the solutions into two mutually exclusive, uncoupled families:
1. **Even-parity states ($\psi(-x) = +\psi(x)$):**
   - Inside: The odd component must vanish, so $A = 0$, giving $\psi_\mathrm{II}(x) = B\cos(lx)$.
   - Outside: The amplitudes in Regions I and III must match: $C = G$. Thus $\psi(x) = G e^{-\kappa |x|}$.
2. **Odd-parity states ($\psi(-x) = -\psi(x)$):**
   - Inside: The even component must vanish, so $B = 0$, giving $\psi_\mathrm{II}(x) = A\sin(lx)$.
   - Outside: The amplitudes must have opposite signs: $C = -G$. Thus $\psi(x) = \operatorname{sgn}(x) G e^{-\kappa |x|}$.

| Parity | Region I ($x < -a$) | Region II ($-a \le x \le a$) | Region III ($x > a$) | Boundary Matching Condition at $x=a$ |
| :--- | :--- | :--- | :--- | :--- |
| **Even** ($\hat{P}\psi = +\psi$) | $+G e^{\kappa x}$ | $B\cos(lx)$ | $+G e^{-\kappa x}$ | $B\cos(la) = Ge^{-\kappa a}$, $\ -lB\sin(la) = -\kappa Ge^{-\kappa a}$ |
| **Odd** ($\hat{P}\psi = -\psi$) | $-G e^{\kappa x}$ | $A\sin(lx)$ | $+G e^{-\kappa x}$ | $A\sin(la) = Ge^{-\kappa a}$, $\ \ \ lA\cos(la) = -\kappa Ge^{-\kappa a}$ |

Thanks to symmetry, matching the boundary conditions at $x = +a$ automatically satisfies the boundary conditions at $x = -a$.

## 3. Transcendental equations and graphical solution
<span class="scope-extra-book">extra · book</span> *Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=79|PDF pp. 79–81]]); [[Finite_well.pdf#page=3|Finite Well notes pp. 3–5]]*

> [!intuition] Reading the graph
> *Left:* the branches of $z\tan z$ (even) and $-z\cot z$ (odd) — each starts at 0 and shoots to $+\infty$ on an interval of width $\pi/2$. *Right:* the quarter-circle $\sqrt{z_0^2-z^2}$ — it starts at $z_0$ and falls to 0 at $z=z_0$. A rising curve and a falling curve **always** meet exactly once on any branch they both cover: one bound state per branch, even and odd alternating, ground state even. The lecture draws exactly the same picture with $\kappa/k_0$ (see §9–§10).

We now match $\psi$ and $\psi'$ across the interface $x = a$ to obtain the quantization condition for the allowed energies.

### Derivation for even-parity states
> [!derivation] Step-by-step derivation of the even transcendental equation
> For even parity, the wavefunction and its derivative at $x = a$ are:
> - Interior ($x \to a^-$):
>   $$\psi(a^-) = B\cos(la), \qquad \psi'(a^-) = -l B\sin(la).$$
> - Exterior ($x \to a^+$):
>   $$\psi(a^+) = G e^{-\kappa a}, \qquad \psi'(a^+) = -\kappa G e^{-\kappa a}.$$
>
> Imposing continuity of $\psi$ and $\psi'$:
> $$B\cos(la) = G e^{-\kappa a} \qquad \text{(Eq. 1: continuity of $\psi$)}$$
> $$-l B\sin(la) = -\kappa G e^{-\kappa a} \qquad \text{(Eq. 2: continuity of $\psi'$)}$$
>
> Dividing Eq. (2) by Eq. (1) eliminates the unknown amplitudes $B$ and $G$:
> $$\frac{-l B\sin(la)}{B\cos(la)} = \frac{-\kappa G e^{-\kappa a}}{G e^{-\kappa a}} \implies l\tan(la) = \kappa.$$
>
> Multiplying both sides by the well half-width $a$:
> $$(la)\tan(la) = \kappa a.$$
>
> We now define two dimensionless variables:
> $$z \equiv la = \frac{a}{\hbar}\sqrt{2m(E+V_0)} > 0,$$
> $$z_0 \equiv \frac{a}{\hbar}\sqrt{2mV_0} > 0.$$
>
> From the definitions of $l$ and $\kappa$, notice that:
> $$l^2 + \kappa^2 = \frac{2m(E+V_0)}{\hbar^2} + \frac{-2mE}{\hbar^2} = \frac{2mV_0}{\hbar^2}.$$
> Multiplying this relation by $a^2$:
> $$(la)^2 + (\kappa a)^2 = \frac{2mV_0 a^2}{\hbar^2} \implies z^2 + (\kappa a)^2 = z_0^2.$$
>
> Therefore, $\kappa a$ can be expressed solely in terms of $z$ and $z_0$:
> $$\kappa a = \sqrt{z_0^2 - z^2}.$$
>
> Substituting $\kappa a$ into $(la)\tan(la) = \kappa a$ yields the famous **even-parity transcendental equation**:
> $$\boxed{z\tan z = \sqrt{z_0^2 - z^2}} \qquad \text{(Even states)}$$

### Derivation for odd-parity states
> [!derivation] Step-by-step derivation of the odd transcendental equation
> For odd parity, the interior solution is $\psi_\mathrm{II}(x) = A\sin(lx)$. The matching equations at $x = a$ are:
> - Interior ($x \to a^-$):
>   $$\psi(a^-) = A\sin(la), \qquad \psi'(a^-) = l A\cos(la).$$
> - Exterior ($x \to a^+$):
>   $$\psi(a^+) = G e^{-\kappa a}, \qquad \psi'(a^+) = -\kappa G e^{-\kappa a}.$$
>
> Imposing continuity:
> $$A\sin(la) = G e^{-\kappa a} \qquad \text{(Eq. 3)}$$
> $$l A\cos(la) = -\kappa G e^{-\kappa a} \qquad \text{(Eq. 4)}$$
>
> Dividing Eq. (4) by Eq. (3):
> $$\frac{l A\cos(la)}{A\sin(la)} = \frac{-\kappa G e^{-\kappa a}}{G e^{-\kappa a}} \implies l\cot(la) = -\kappa.$$
>
> Multiplying both sides by $a$ and setting $z = la$, $\kappa a = \sqrt{z_0^2 - z^2}$:
> $$-z\cot z = \kappa a \implies \boxed{-z\cot z = \sqrt{z_0^2 - z^2}} \qquad \text{(Odd states)}$$

### Physical meaning of $z$ and $z_0$
- **$z = la$** is the **internal phase thickness** of the well: it represents the number of radians of spatial phase accumulated by the de Broglie wave between the center of the well and the right wall ($x=0$ to $x=a$).
- **$z_0 = \frac{a}{\hbar}\sqrt{2mV_0} = \sqrt{\frac{2mV_0 a^2}{\hbar^2}}$** is the **dimensionless well capacity (or well strength)**. It depends exclusively on the structural parameters of the potential: the mass $m$, the depth $V_0$, and the width squared $a^2$. It measures how many quantum states the well is capable of holding.
- Because $\kappa a = \sqrt{z_0^2 - z^2} > 0$, any physical bound state must satisfy:
  $$0 < z < z_0.$$

### Graphical interpretation: intersecting the quarter-circle
The transcendental equations cannot be solved in closed form using elementary functions, but their mathematical properties are transparent graphically.
In the $(z, y)$ plane, we plot:
1. **The right-hand side:** $y_R(z) = \sqrt{z_0^2 - z^2}$. In the first quadrant ($z > 0, y > 0$), this is a **quarter-circle of radius $z_0$** centered at the origin $(0, 0)$.
2. **The left-hand sides:**
   - **Even curve:** $y_\mathrm{even}(z) = z\tan z$.
     - Starts at the origin: $y(0) = 0$, with initial slope $y'(0) = 0$ (since $z\tan z \approx z^2$).
     - Rises monotonically to vertical asymptotes (poles) at $z = \frac{\pi}{2}, \frac{3\pi}{2}, \frac{5\pi}{2}, \dots$.
     - Is positive in the intervals $\left(0, \frac{\pi}{2}\right), \left(\pi, \frac{3\pi}{2}\right), \left(2\pi, \frac{5\pi}{2}\right), \dots$.
   - **Odd curve:** $y_\mathrm{odd}(z) = -z\cot z$.
     - Has vertical asymptotes at $z = \pi, 2\pi, 3\pi, \dots$.
     - Crosses zero at $z = \frac{\pi}{2}, \frac{3\pi}{2}, \frac{5\pi}{2}, \dots$.
     - Is positive in the intervals $\left(\frac{\pi}{2}, \pi\right), \left(\frac{3\pi}{2}, 2\pi\right), \left(\frac{5\pi}{2}, 3\pi\right), \dots$.

> [!key] Alternating parity of bound states
> Because the positive branches of $z\tan z$ and $-z\cot z$ alternate across consecutive intervals of width $\pi/2$:
> - Interval $\left(0, \frac{\pi}{2}\right)$: Even ground state ($n=1$, zero nodes)
> - Interval $\left(\frac{\pi}{2}, \pi\right)$: Odd first excited state ($n=2$, one node at $x=0$)
> - Interval $\left(\pi, \frac{3\pi}{2}\right)$: Even second excited state ($n=3$, two nodes)
> - Interval $\left(\frac{3\pi}{2}, 2\pi\right)$: Odd third excited state ($n=4$, three nodes)
>
> Every intersection of the quarter-circle with one of these curves corresponds to exactly one physical bound state! Once the root $z_n$ is determined, the physical energy is obtained directly:
> $$E_n = -V_0 + \frac{\hbar^2 l_n^2}{2m} = -V_0 + \frac{\hbar^2 z_n^2}{2ma^2} = -V_0 \left(1 - \frac{z_n^2}{z_0^2}\right).$$

![[fig_qm07_graphical.png]]
*Figure QM7.2. Graphical solution and bound-state spectrum of the finite square well (the $\kappa a$-versus-$z$ form of the lecture's graph; see Figure QM7.4 for the $\kappa/k_0$ form). A: Graphical solution for $z_0 = 3$ showing the quarter-circle $\sqrt{3^2 - z^2}$ (dashed black) intersecting the first even branch $z\tan z$ (blue) at $z_1 = 1.1701$ (ground state) and the first odd branch $-z\cot z$ (orange) at $z_2 = 2.2789$ (first excited state), giving $N = 2$ bound states. B: Graphical solution for $z_0 = 7$ showing 5 bound states alternating even and odd ($z_1 = 1.3733, z_2 = 2.7395, z_3 = 4.0886, z_4 = 5.4017, z_5 = 6.6160$). C: Evolution of energy levels $E_n/V_0$ as a function of the well strength parameter $z_0$, showing states emerging from the continuum threshold $E=0$ each time $z_0$ crosses an integer multiple of $\pi/2$ (vertical grid lines). D: The first four bound-state wavefunctions for $z_0 = 4\pi \approx 12.57$, each drawn on its own level $E_n/V_0$ (lecture convention), exhibiting sinusoidal nodes inside the well and exponential decay outside.*

## 4. Counting bound states and limiting behaviours
<span class="scope-extra-book">extra · book</span> *Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=82|PDF pp. 82–84]])*

> [!intuition] Why 1-D can never fail to bind
> On the first branch the rising curve starts *below* the circle (0 < $z_0$) and ends *above* it (at the pole), so it must cross. In words: a weak 1-D well still binds because the even solution only needs to curve a little to match a long, nearly flat exponential — a *very* shallow bound state has a *very* long tail (depth $\propto V_0^2$, size $\propto1/V_0$). In 3-D the $s$-wave must vanish at the origin ($u(0)=0$), which forces the odd branch and hence a threshold.

### Bound state counting formula
Because each branch of $z\tan z$ and $-z\cot z$ spans an interval of width $\pi/2$, increasing the radius $z_0$ of the quarter-circle sweeps across new branches sequentially.
- For $0 < z_0 \le \frac{\pi}{2}$: The circle cuts only the first even branch. There is **1 bound state** (even).
- For $\frac{\pi}{2} < z_0 \le \pi$: The circle reaches into the second interval, intersecting the first odd branch. There are **2 bound states** (1 even, 1 odd).
- For $\pi < z_0 \le \frac{3\pi}{2}$: The circle reaches into the third interval, intersecting the second even branch. There are **3 bound states** (2 even, 1 odd).

In general, the total number of bound states $N$ supported by a well of parameter $z_0$ is
$$\boxed{N = \left\lceil \frac{z_0}{\pi/2} \right\rceil = \left\lceil \frac{2}{\pi}\frac{a\sqrt{2mV_0}}{\hbar} \right\rceil}$$

> [!verify] Correction to the first draft of this chapter (checked in `scripts/qm07_numbers.py`)
> The first version of this section wrote $N=\lfloor z_0/(\pi/2)\rfloor+1$ and its table listed $N=3$ at $z_0=\pi$ and $N=5$ at $z_0=2\pi$. A state is *born at the threshold* when $z_0$ equals a multiple of $\pi/2$, with zero binding, so **at exactly $z_0=m\pi/2$ it is not yet bound**: the solved counts are $N=2$ at $z_0=\pi$ and $N=4$ at $z_0=2\pi$ (and $N=1$ at $\pi/2$, $N=8$ at $4\pi$). The ceiling formula is right for every $z_0$; the floor-plus-one formula agrees with it except exactly at multiples of $\pi/2$. The intervals in the list above are accordingly $0<z_0\le\pi/2$, $\pi/2<z_0\le\pi$, $\pi<z_0\le3\pi/2$.

A new bound state is born at threshold $E = 0^-$ whenever $z_0$ crosses an integer multiple of $\pi/2$:
$$z_{0,\mathrm{crit}} = m \frac{\pi}{2}, \qquad m = 1, 2, 3, \dots$$
Even states appear at $m = 0, 2, 4, \dots$ ($z_0 = 0, \pi, 2\pi, \dots$), and odd states appear at $m = 1, 3, 5, \dots$ ($z_0 = \pi/2, 3\pi/2, \dots$).

### Proof: There is ALWAYS at least one bound state in 1-D
A fundamental question in quantum mechanics is whether an extremely shallow ($V_0 \to 0$) or extremely narrow ($a \to 0$) well can fail to trap a particle.

> [!derivation] Proof of guaranteed binding in 1-D
> Consider the even-parity equation $f(z) \equiv \sqrt{z_0^2 - z^2} - z\tan z = 0$ on the domain $z \in (0, \min(z_0, \pi/2))$.
> 1. At the lower limit $z \to 0^+$:
>    $$\sqrt{z_0^2 - z^2} \to z_0 > 0, \qquad z\tan z \to 0.$$
>    Therefore, $f(0^+) = z_0 > 0$.
> 2. As $z$ approaches the upper limit:
>    - If $z_0 < \pi/2$, then as $z \to z_0^-$, the square root vanishes $\sqrt{z_0^2 - z^2} \to 0$, while $z\tan z \to z_0 \tan z_0 > 0$. Thus $f(z_0^-) = -z_0\tan z_0 < 0$.
>    - If $z_0 \ge \pi/2$, then as $z \to (\pi/2)^-$, the square root remains finite $\sqrt{z_0^2 - (\pi/2)^2} \ge 0$, while $z\tan z \to +\infty$. Thus $f((\pi/2)^-) \to -\infty < 0$.
>
> Because $f(z)$ is continuous on $(0, \min(z_0, \pi/2))$, the Intermediate Value Theorem guarantees the existence of at least one root $z_1 \in (0, \min(z_0, \pi/2))$ where $f(z_1) = 0$.
> **Hence, a 1-D symmetric finite square well possesses at least one bound state, no matter how small $V_0$ or $a$ may be.** $\blacksquare$

> [!extra-beyond]- 🔵 Extra (beyond): 3-D spherical wells and the centrifugal threshold
> Why does the guaranteed 1-D binding not hold in three dimensions?
> Consider a particle in a 3-D spherically symmetric square well of radius $a$:
> $$V(r) = \begin{cases} -V_0, & r \le a \\ 0, & r > a \end{cases}$$
> The radial wavefunction $R(r)$ is written as $u(r) / r$, where $u(r)$ satisfies the radial Schrödinger equation on the half-line $r \in [0, \infty)$:
> $$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[ V(r) + \frac{\hbar^2\ell(\ell+1)}{2mr^2} \right] u(r) = E u(r).$$
> 1. **The boundary condition at the origin:** For the full 3-D wavefunction $\psi(\mathbf{r}) = R(r)Y_{\ell m}(\theta, \phi)$ to remain finite and non-singular at the origin $r=0$, the radial function $u(r) = r R(r)$ must satisfy:
>    $$u(0) = 0.$$
> 2. **For s-wave ($\ell = 0$):** The centrifugal barrier vanishes, but the condition $u(0) = 0$ forces the interior solution to be pure sine:
>    $$u(r) = A\sin(lr), \qquad (r \le a).$$
>    Cosine is strictly forbidden because $\cos(0) = 1 \ne 0$.
>    Matching $u(r)$ and $u'(r)$ at $r = a$ yields the **odd-parity 1-D equation**:
>    $$-z\cot z = \sqrt{z_0^2 - z^2}.$$
>    As established above, the odd branch has no solution unless the quarter-circle reaches $z > \pi/2$!
>    Therefore, a 3-D square well binds an s-wave state **if and only if**:
>    $$z_0 > \frac{\pi}{2} \iff V_0 a^2 > \frac{\pi^2\hbar^2}{8m}.$$
> 3. **For $\ell > 0$:** The repulsive centrifugal barrier $\frac{\hbar^2\ell(\ell+1)}{2mr^2}$ pushes the wavefunction further out of the well, demanding an even deeper potential to bind.
> In 1-D, the origin $x=0$ is an interior point of the symmetric domain $[-a, a]$, allowing symmetric even solutions ($\cos lx$) that peak at the center and have non-zero value at the origin. Hence, 1-D wells always bind, while 3-D wells require a finite threshold depth.

### Limit I: The wide, deep well ($z_0 \gg 1$)
When the well is very deep or very wide ($z_0 \to \infty$), the radius of the quarter-circle becomes enormous. In the region of lower-lying bound states ($z \ll z_0$), the circle is approximately horizontal:
$$\sqrt{z_0^2 - z^2} = z_0 \sqrt{1 - \frac{z^2}{z_0^2}} \approx z_0 \to \infty.$$
To satisfy $z\tan z \to \infty$ (even states) and $-z\cot z \to \infty$ (odd states), $z$ must approach the vertical asymptotes of the trigonometric curves:
- Even states: $z_n \to \frac{\pi}{2}, \frac{3\pi}{2}, \frac{5\pi}{2}, \dots = (2k-1)\frac{\pi}{2}$
- Odd states: $z_n \to \pi, 2\pi, 3\pi, \dots = (2k)\frac{\pi}{2}$

Combining both families:
$$z_n \to n \frac{\pi}{2}, \qquad n = 1, 2, 3, \dots$$
Recalling that $z = la$, this gives $l_n a \approx n\pi/2$, or $l_n \approx \frac{n\pi}{2a}$. The kinetic energy above the well bottom is:
$$E_n + V_0 = \frac{\hbar^2 l_n^2}{2m} \approx \frac{n^2\pi^2\hbar^2}{2m(2a)^2} = E_n^\mathrm{box},$$
which is the exact spectrum of a particle in an infinite rigid box of full width $L = 2a$!

> [!derivation] Leading asymptotic correction for deep wells
> Let $z_n = \frac{n\pi}{2} - \delta_n$, where $\delta_n \ll 1$ is a small positive offset.
> For even states, $z\tan z = \left(\frac{n\pi}{2} - \delta_n\right)\tan\left(\frac{n\pi}{2} - \delta_n\right) = \left(\frac{n\pi}{2} - \delta_n\right)\cot\delta_n \approx \frac{n\pi}{2\delta_n}$.
> Setting this equal to $\sqrt{z_0^2 - z_n^2} \approx z_0$:
> $$\frac{n\pi}{2\delta_n} \approx z_0 \implies \delta_n \approx \frac{n\pi}{2z_0}.$$
> Thus:
> $$z_n \approx \frac{n\pi}{2}\left(1 - \frac{1}{z_0}\right).$$
> The energy above the bottom becomes:
> $$E_n + V_0 = \frac{\hbar^2 z_n^2}{2ma^2} \approx \frac{n^2\pi^2\hbar^2}{8ma^2}\left(1 - \frac{1}{z_0}\right)^2 \approx E_n^\mathrm{box}\left(1 - \frac{2}{z_0}\right).$$
> The finite-well energy is strictly **below** the infinite-well energy by a fractional shift $\Delta E / E^\mathrm{box} \approx -2/z_0$.

### Limit II: The narrow, shallow well ($z_0 \ll 1$)
When $z_0 \to 0$, only the single even ground state survives ($N = 1$). Since $0 < z < z_0 \ll 1$, we can use the small-angle approximations $\tan z \approx z$ and $\sqrt{z_0^2 - z^2} \approx z_0$:
$$z\tan z = \sqrt{z_0^2 - z^2} \implies z^2 \approx z_0 \implies z \approx \sqrt{z_0}.$$
Then the decay parameter $\kappa a$ is:
$$\kappa a = z\tan z \approx z^2 \approx z_0^2.$$
Dividing by $a$:
$$\kappa \approx \frac{z_0^2}{a} = \frac{1}{a}\left(\frac{2mV_0 a^2}{\hbar^2}\right) = \frac{2mV_0 a}{\hbar^2}.$$
The bound state energy is:
$$E = -\frac{\hbar^2\kappa^2}{2m} \approx -\frac{\hbar^2}{2m}\left(\frac{2mV_0 a}{\hbar^2}\right)^2 = -\frac{2m V_0^2 a^2}{\hbar^2} = -\frac{m (2V_0 a)^2}{2\hbar^2}.$$
Notice three crucial physical features of a weak 1-D well:
1. **Quadratic scaling with depth:** The binding energy $|E| \propto V_0^2$, rather than linear in $V_0$.
2. **Dependence on integrated area:** The energy depends on the potential solely through the integrated strength $\alpha \equiv 2V_0 a = \int |V(x)| dx$.
3. **Infinite spatial spread:** The penetration depth $d_\mathrm{pen} = 1/\kappa \approx \frac{\hbar^2}{2mV_0 a} \to \infty$. As the well becomes infinitesimally weak, the wavefunction delocalises, spreading out over the entire universe.

### High-precision reference table for standard well capacities
The following table presents exact numerical solutions for the ground state and bound spectrum across a wide range of well parameters $z_0$:

| $z_0$ | $N_\mathrm{states}$ | Ground $z_1$ | $\kappa_1 a = \sqrt{z_0^2-z_1^2}$ | $\frac{E_1+V_0}{V_0} = \frac{z_1^2}{z_0^2}$ | $\frac{E_1}{V_0} = \frac{z_1^2}{z_0^2} - 1$ | $d_\mathrm{pen}/a = \frac{1}{\kappa_1 a}$ | $P_\mathrm{tunnel}$ (%) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1.000** | 1 | 0.7391 | 0.6736 | 0.5462 | $-0.4538$ | 1.4846 | 32.64% |
| **2.000** | 2 | 1.0299 | 1.7145 | 0.2652 | $-0.7348$ | 0.5833 | 9.77% |
| **$\pi$ (3.142)** | 2 | 1.1843 | 2.9098 | 0.1421 | $-0.8579$ | 0.3437 | 3.63% |
| **4.000** | 3 | 1.2524 | 3.7989 | 0.0980 | $-0.9020$ | 0.2632 | 2.04% |
| **$2\pi$ (6.283)** | 4 | 1.3537 | 6.1356 | 0.0464 | $-0.9536$ | 0.1630 | 0.65% |
| **8.000** | 6 | 1.3955 | 7.8774 | 0.0304 | $-0.9696$ | 0.1269 | 0.34% |
| **10.000** | 7 | 1.4276 | 9.8976 | 0.0204 | $-0.9796$ | 0.1010 | 0.19% |

*(Counts corrected to $\lceil2z_0/\pi\rceil$; all other values re-verified with `scripts/qm07_numbers.py`, precision $10^{-12}$; $P_\mathrm{tunnel}$ is the exact integrated probability in the classically forbidden barriers $|x|>a$.)*

## 5. Wavefunctions, penetration, and the forbidden region
<span class="scope-extra-book">extra · book</span> *Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=84|PDF pp. 84–85]])*

> [!intuition] The leak, in numbers you can remember
> The tail dies over $d_{\rm pen}=1/\kappa$. For a state bound by $B$ below the rim, $d_{\rm pen}=\hbar/\sqrt{2mB}$: for an electron bound by 1 eV this is 0.195 nm (about a bond length), by 0.01 eV it is 1.95 nm. **Weakly bound means a long tail**, which is why the last bound state of every well in this chapter has the largest $P_{\rm out}$ (23 % to 64 %).

We now construct the full, normalised wavefunctions and investigate their spatial penetration into the classically forbidden barriers.

### Wavefunction matching and normalization
For an even-parity state, boundary matching at $x = a$ gave $B\cos(la) = G e^{-\kappa a}$, which determines the ratio of the exterior decay amplitude to the interior oscillation amplitude:
$$\frac{G}{B} = e^{\kappa a}\cos(la) \implies G = B\cos(la)e^{\kappa a}.$$

> [!derivation] Full normalisation of even-parity wavefunctions
> The normalization condition requires $\int_{-\infty}^\infty |\psi(x)|^2 dx = 1$. By symmetry:
> $$2\int_0^a B^2 \cos^2(lx)\,dx + 2\int_a^\infty G^2 e^{-2\kappa x}\,dx = 1.$$
>
> 1. The interior integral:
>    $$2B^2 \int_0^a \cos^2(lx)\,dx = 2B^2 \int_0^a \frac{1 + \cos(2lx)}{2}\,dx = B^2 \left[ x + \frac{\sin(2lx)}{2l} \right]_0^a = B^2\left(a + \frac{\sin(2la)}{2l}\right).$$
> 2. The exterior integral:
>    $$2G^2 \int_a^\infty e^{-2\kappa x}\,dx = 2G^2 \left[ -\frac{e^{-2\kappa x}}{2\kappa} \right]_a^\infty = G^2 \frac{e^{-2\kappa a}}{\kappa}.$$
>
> Substituting $G = B\cos(la)e^{\kappa a}$ into the exterior term:
> $$G^2 \frac{e^{-2\kappa a}}{\kappa} = B^2 \cos^2(la) e^{2\kappa a} \frac{e^{-2\kappa a}}{\kappa} = B^2 \frac{\cos^2(la)}{\kappa}.$$
>
> Adding both contributions:
> $$B^2 \left[ a + \frac{\sin(2la)}{2l} + \frac{\cos^2(la)}{\kappa} \right] = 1.$$
>
> Solving for the interior amplitude $B$:
> $$\boxed{B = \left[ a + \frac{\sin(2la)}{2l} + \frac{\cos^2(la)}{\kappa} \right]^{-1/2}}$$
>
> The exterior amplitude $G$ is then:
> $$\boxed{G = \cos(la)e^{\kappa a}\left[ a + \frac{\sin(2la)}{2l} + \frac{\cos^2(la)}{\kappa} \right]^{-1/2}}$$

Similarly, for odd-parity states where $\psi_\mathrm{II}(x) = A\sin(lx)$ and $G = A\sin(la)e^{\kappa a}$:
$$\boxed{A = \left[ a - \frac{\sin(2la)}{2l} + \frac{\sin^2(la)}{\kappa} \right]^{-1/2}}$$

### The penetration depth $d_\mathrm{pen}$
Outside the well ($|x| > a$), the probability density decays as:
$$P(x) = |\psi(x)|^2 = G^2 e^{-2\kappa x} = G^2 e^{-2(x-a)/d_\mathrm{pen}} e^{-2\kappa a}.$$
The characteristic distance over which the wavefunction drops by a factor of $1/e$ is the **penetration depth**:
$$\boxed{d_\mathrm{pen} \equiv \frac{1}{\kappa} = \frac{\hbar}{\sqrt{-2mE}} = \frac{\hbar}{\sqrt{2m(V_0 - |E|) = 2m(E+V_0)_\mathrm{deficit}}}}$$
- For tightly bound states near the bottom of a deep well ($E \to -V_0$), $|E| \approx V_0$, so $\kappa \approx \sqrt{2mV_0}/\hbar$ is large and $d_\mathrm{pen} \to a/z_0$ is small: the wave is sharply confined.
- For weakly bound states near the top of the well ($E \to 0^-$), $\kappa \to 0$ and $d_\mathrm{pen} \to \infty$: the tail stretches deeply into the barrier.

### The "effective width" argument: why finite-well energies are lower
In [[QM04 The Particle in a Box]], the particle was strictly confined within full width $2a$, with zero wavefunction at the walls. In the finite well, the wavefunction does not stop abruptly at $x = \pm a$; it extends into the barriers by approximately one penetration depth $d_\mathrm{pen} = 1/\kappa$ on each side.
Therefore, the wave behaves as if it were confined in a wider effective box of width:
$$2a_\mathrm{eff} = 2a + 2d_\mathrm{pen} = 2a + \frac{2}{\kappa} = 2a\left(1 + \frac{1}{\kappa a}\right).$$
In an infinite box of width $2a_\mathrm{eff}$, the kinetic energy would be:
$$E_n + V_0 \approx \frac{n^2\pi^2\hbar^2}{2m(2a_\mathrm{eff})^2} = \frac{n^2\pi^2\hbar^2}{8ma^2}\left(1 + \frac{1}{\kappa a}\right)^{-2} \approx E_n^\mathrm{box}\left(1 - \frac{2}{\kappa a}\right).$$
Because $\kappa a \approx z_0$ for deep wells, this simple physical argument reproduces the exact asymptotic formula $E_n \approx E_n^\mathrm{box}(1 - 2/z_0)$ derived via perturbation theory in §4!
**Quantum mechanical penetration into the classically forbidden barrier relaxes spatial confinement, broadens the de Broglie wavelength, and lowers the kinetic energy.**

### Tunnelling probability into the forbidden region
The probability that a position measurement finds the particle inside the classically forbidden region ($|x| > a$) is:
$$P_\mathrm{tunnel} = \frac{\int_{|x|>a} |\psi(x)|^2\,dx}{\int_{-\infty}^\infty |\psi(x)|^2\,dx} = 2\int_a^\infty |\psi_\mathrm{III}(x)|^2\,dx.$$
Using the normalised expressions from our derivation:
$$\boxed{P_\mathrm{tunnel} = \frac{\frac{\cos^2(la)}{\kappa}}{a + \frac{\sin(2la)}{2l} + \frac{\cos^2(la)}{\kappa}} = \frac{\frac{\cos^2 z}{\kappa a}}{1 + \frac{\sin(2z)}{2z} + \frac{\cos^2 z}{\kappa a}}}$$
- As $z_0 \to \infty$ (infinite well), $\kappa a \to \infty$, so $P_\mathrm{tunnel} \to 0$.
- As $z_0 \to 0$ (weak well), $\kappa a \to 0$ and $z \to 0$, so $\frac{\cos^2 z}{\kappa a} \to \infty$ dominates the denominator, giving $P_\mathrm{tunnel} \to 100\%$. The particle spends almost all of its time outside the well!

![[fig_qm07_wavefunctions.png]]
*Figure QM7.3. Spatial profiles, penetration into classically forbidden barriers, and tunnelling probabilities. A: The first three eigenstates $\psi_1(x), \psi_2(x), \psi_3(x)$ for well strength $z_0 = 5$ (solid colored curves) plotted across all three regions, contrasted with the corresponding rigid infinite-box eigenstates of width $2a$ (dashed black curves). B: Probability density $|\psi_1(x)|^2$ for the ground state; the classically forbidden barrier regions $|x| > a$ are shaded in purple, representing the tunnelling probability $P_\mathrm{tunnel} = 1.17\%$ (corrected from the first draft's 1.34 %). C: Tunnelling probability $P_\mathrm{tunnel}$ as a function of the well strength parameter $z_0$ for the ground state, illustrating the monotonic transition from $P_\mathrm{tunnel} \to 100\%$ as $z_0 \to 0$ to $P_\mathrm{tunnel} \to 0$ as $z_0 \to \infty$.*

![[fig_qm07_limits.png]]
*Figure QM7.6. The three corners of the finite well (lecture convention). A: $E_n/E_n^{\rm box}$ for $n=1,2,3$ against $z_0$ (solid) with the asymptote $1-2/z_0$ (dashed): the finite-well level approaches the rigid-box level **from below**. B: the decay parameter $\kappa a$ of the single state of a shallow well (solid) against $z_0^2$ (dashed), which is the statement $\kappa=m\alpha/\hbar^2$ with $\alpha=2V_0a$. C: at fixed $\alpha=2V_0a$ (units $\hbar=m=\alpha=1$) the ratio $|E|/(m\alpha^2/2\hbar^2)$ tends to 1 as $a\to0$: the delta-function well. Data: `scripts/qm07_numbers.py`.*

## 6. Numerical examples with real physics
<span class="scope-extra-beyond">extra · beyond</span> *Physical semiconductor, nuclear, and electronic systems*

We now apply our formulas to three concrete physical systems, using accurate physical constants (CODATA 2018: $\hbar = 1.05457 \times 10^{-34}\ \mathrm{J\cdot s}$, $m_e = 9.10938 \times 10^{-31}\ \mathrm{kg}$, $e = 1.60218 \times 10^{-19}\ \mathrm{C}$, $\hbar c = 197.327\ \mathrm{MeV\cdot fm}$).

### 1. Semiconductor Quantum Well ($\mathrm{GaAs}/\mathrm{Al}_{0.3}\mathrm{Ga}_{0.7}\mathrm{As}$)
In a semiconductor heterostructure, electrons in the $\mathrm{GaAs}$ layer behave as quasiparticles with an effective conduction mass $m^* = 0.067\,m_e = 6.103 \times 10^{-32}$ kg due to the periodic crystal potential. The conduction band offset between $\mathrm{GaAs}$ and $\mathrm{Al}_{0.3}\mathrm{Ga}_{0.7}\mathrm{As}$ forms a finite well of depth $V_0 = 0.30$ eV. Consider a quantum well with width $2a = 10.0$ nm (half-width $a = 5.0$ nm).

1. **Well strength $z_0$:**
   $$z_0 = \frac{a}{\hbar}\sqrt{2m^* V_0} = \frac{5.0 \times 10^{-9}}{1.05457 \times 10^{-34}}\sqrt{2 \times (6.103 \times 10^{-32}) \times (0.30 \times 1.60218 \times 10^{-19})} = 3.6317.$$
2. **Number of bound subbands:**
   $$N = \left\lfloor \frac{z_0}{\pi/2} \right\rfloor + 1 = \left\lfloor \frac{3.6317}{1.5708} \right\rfloor + 1 = \lfloor 2.312 \rfloor + 1 = 3 \text{ bound states}.$$
3. **Eigenvalues and state properties:**
   - **Ground state $n=1$ (Even):** Solving $z\tan z = \sqrt{3.6317^2 - z^2}$ gives $z_1 = 1.2263$.
     - Energy above well bottom: $E_{1,\mathrm{kin}} = V_0(z_1/z_0)^2 = 0.30 \times (1.2263 / 3.6317)^2 = 0.0342\ \mathrm{eV} = 34.2$ meV.
     - Bound state energy: $E_1 = -0.30 + 0.0342 = -0.2658$ eV.
     - Decay parameter: $\kappa_1 a = \sqrt{3.6317^2 - 1.2263^2} = 3.4185 \implies d_\mathrm{pen} = a / 3.4185 = 1.463$ nm.
     - Forbidden-region probability: $P_\mathrm{tunnel} = 2.58\%$.
   - **First excited state $n=2$ (Odd):** Solving $-z\cot z = \sqrt{3.6317^2 - z^2}$ gives $z_2 = 2.4144$.
     - Energy above well bottom: $E_{2,\mathrm{kin}} = 0.30 \times (2.4144 / 3.6317)^2 = 0.1326\ \mathrm{eV} = 132.6$ meV.
     - Bound state energy: $E_2 = -0.1674$ eV.
     - Decay parameter: $\kappa_2 a = 2.7127 \implies d_\mathrm{pen} = 1.843$ nm; $P_\mathrm{tunnel} = 11.90\%$.
   - **Second excited state $n=3$ (Even):** Solving $z\tan z = \sqrt{3.6317^2 - z^2}$ on $(\pi, 3\pi/2)$ gives $z_3 = 3.4549$.
     - Energy above well bottom: $E_{3,\mathrm{kin}} = 0.30 \times (3.4549 / 3.6317)^2 = 0.2715\ \mathrm{eV} = 271.5$ meV.
     - Bound state energy: $E_3 = -0.0285$ eV (barely bound, 28.5 meV below the barrier).
     - Decay parameter: $\kappa_3 a = 1.1193 \implies d_\mathrm{pen} = 4.467$ nm; $P_\mathrm{tunnel} = 42.70\%$.
4. **Subband optical transition:**
   The inter-subband transition $n=1 \to n=2$ has photon energy $\Delta E = E_2 - E_1 = 132.6 - 34.2 = 98.4$ meV. The corresponding infrared wavelength is:
   $$\lambda = \frac{hc}{\Delta E} = \frac{1.2398\ \mathrm{eV\cdot\mu m}}{0.0984\ \mathrm{eV}} = 12.60\ \mu\mathrm{m}.$$
   This falls directly in the long-wavelength infrared atmospheric transmission window (8–14 $\mu$m), which is the operating wavelength of military thermal imaging sensors.

### 2. The Nuclear Deuteron ($^2\mathrm{H}$)
The deuteron is a bound state of a proton and neutron. In the center-of-mass frame, the two-body problem reduces to a single particle of reduced mass:
$$\mu = \frac{m_p m_n}{m_p + m_n} \approx \frac{m_N}{2} \approx 469.1\ \mathrm{MeV}/c^2.$$
The attractive strong nuclear force is modeled as a 3-D spherical square well with depth $V_0 \approx 35.0$ MeV and range $a \approx 2.05$ fm.
As established in §4, the 3-D s-wave boundary condition $u(0)=0$ requires $u(r)$ to satisfy the **odd-parity 1-D transcendental equation**:
$$-z\cot z = \sqrt{z_0^2 - z^2}.$$

1. **Well strength $z_0$:**
   $$z_0 = \frac{a}{\hbar c}\sqrt{2(\mu c^2) V_0} = \frac{2.05\ \mathrm{fm}}{197.327\ \mathrm{MeV\cdot fm}}\sqrt{2 \times (469.1\ \mathrm{MeV}) \times (35.0\ \mathrm{MeV})} = 1.8826.$$
2. **Threshold check:**
   The threshold for the first 3-D bound state is $z_{0,\mathrm{crit}} = \pi/2 \approx 1.5708$. Because $z_0 = 1.8826 > 1.5708$, the deuteron is bound! But because $z_0 < \pi \approx 3.1416$, **there is exactly one bound state ($^3\mathrm{S}_1$) and no bound excited states**.
3. **Binding energy and diffuse halo structure:**
   Solving $-z\cot z = \sqrt{1.8826^2 - z^2}$ gives $z = 1.8230$.
   - Kinetic energy inside: $E_\mathrm{kin} = \frac{(\hbar c)^2 z^2}{2\mu c^2 a^2} = 32.82$ MeV.
   - Binding energy: $B = V_0 - E_\mathrm{kin} = 35.0 - 32.82 = 2.18$ MeV (agreeing remarkably with the experimental binding energy $B_\mathrm{exp} = 2.22457$ MeV!).
   - Decay parameter outside the nuclear well: $\kappa = \frac{\sqrt{2\mu B}}{\hbar} = 0.2292\ \mathrm{fm}^{-1}$.
   - Penetration depth:
     $$d_\mathrm{pen} = \frac{1}{\kappa} = \frac{1}{0.2292\ \mathrm{fm}^{-1}} = 4.36\ \mathrm{fm}!$$
   The penetration depth ($4.36$ fm) is more than **twice the range of the nuclear force ($a = 2.05$ fm)**. The proton and neutron spend the vast majority of their time outside the range of their mutual nuclear potential! The deuteron is a loosely bound, giant quantum halo nucleus.

### 3. Nanoscale Electron Well ($2a = 1.0$ nm, $V_0 = 5.0$ eV)
Consider a free electron ($m = m_e$) trapped in a 1-D potential well of total width $2a = 1.0$ nm (half-width $a = 0.50$ nm) and depth $V_0 = 5.0$ eV.

1. **Well strength $z_0$:**
   $$z_0 = \frac{a}{\hbar}\sqrt{2m_e V_0} = \frac{0.50 \times 10^{-9}}{1.05457 \times 10^{-34}}\sqrt{2 \times (9.10938 \times 10^{-31}) \times (5.0 \times 1.60218 \times 10^{-19})} = 5.7279.$$
2. **Number of bound states:**
   $$N = \left\lfloor \frac{5.7279}{\pi/2} \right\rfloor + 1 = \lfloor 3.6465 \rfloor + 1 = 4 \text{ bound states}.$$
3. **Spectrum of all 4 bound states:**
   - **State 1 ($n=1$, Even):** $z_1 = 1.3355$.
     - $E_{1,\mathrm{kin}} = 5.0 \times (1.3355 / 5.7279)^2 = 0.2718$ eV $\implies E_1 = -4.7282$ eV.
     - $\kappa_1 a = \sqrt{5.7279^2 - 1.3355^2} = 5.5701 \implies d_\mathrm{pen} = 0.090$ nm; $P_\mathrm{tunnel} = 0.83\%$.
   - **State 2 ($n=2$, Odd):** $z_2 = 2.6589$.
     - $E_{2,\mathrm{kin}} = 5.0 \times (2.6589 / 5.7279)^2 = 1.0774$ eV $\implies E_2 = -3.9226$ eV.
     - $\kappa_2 a = 5.0732 \implies d_\mathrm{pen} = 0.099$ nm; $P_\mathrm{tunnel} = 3.55\%$.
   - **State 3 ($n=3$, Even):** $z_3 = 3.9512$.
     - $E_{3,\mathrm{kin}} = 5.0 \times (3.9512 / 5.7279)^2 = 2.3792$ eV $\implies E_3 = -2.6208$ eV.
     - $\kappa_3 a = 4.1465 \implies d_\mathrm{pen} = 0.121$ nm; $P_\mathrm{tunnel} = 9.25\%$.
   - **State 4 ($n=4$, Odd):** $z_4 = 5.1610$.
     - $E_{4,\mathrm{kin}} = 5.0 \times (5.1610 / 5.7279)^2 = 4.0593$ eV $\implies E_4 = -0.9407$ eV.
     - $\kappa_4 a = 2.4842 \implies d_\mathrm{pen} = 0.201$ nm; $P_\mathrm{tunnel} = 23.30\%$.

### Master physical comparison table
| Parameter | Semiconductor QW ($\mathrm{GaAs}$) | Nuclear Deuteron ($^2\mathrm{H}$) | Nanoscale Metal Well |
| :--- | :--- | :--- | :--- |
| **Particle & Mass** | Conduction electron, $0.067\,m_e$ | Reduced nucleon $\mu = 469.1$ MeV/$c^2$ | Free electron, $1.0\,m_e$ |
| **Well depth $V_0$** | $0.30$ eV | $35.0$ MeV | $5.0$ eV |
| **Half-width $a$** | $5.0$ nm | $2.05$ fm | $0.50$ nm |
| **Well strength $z_0$** | $3.632$ | $1.883$ | $5.728$ |
| **Bound states count $N$** | 3 states | 1 state (s-wave) | 4 states |
| **Ground state energy $E_1$** | $-0.2658$ eV | $-2.180$ MeV | $-4.7282$ eV |
| **Kinetic energy fraction $E_\mathrm{kin}/V_0$** | $11.4\%$ | $93.8\%$ | $5.4\%$ |
| **Penetration depth $d_\mathrm{pen}$** | $1.463$ nm | $4.364$ fm | $0.090$ nm |
| **Tunnelling probability $P_\mathrm{tunnel}$** | $2.58\%$ | $63.8\%$ (exterior radial; first draft said $\approx55\%$) | $0.83\%$ |

## 7. Connection to the infinite well and to the delta potential
<span class="scope-extra-book">extra · book</span> *Griffiths §2.5–§2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=75|PDF pp. 75–78]]); Sakurai §2.5*

> [!intuition] Zooming out: one family, three corners
> Think of the $(a,V_0)$ plane. Going **up and to the right** (deep, wide, $z_0\to\infty$) you reach the rigid box; going **down and to the left** (shallow, narrow, $z_0\to0$) you reach the delta well, where only the area $\alpha=2V_0a$ matters. The finite well is the bridge: its three figures (levels, $\kappa a$, $|E|/(m\alpha^2/2\hbar^2)$) are in Figure QM7.6.

The finite square well is the master potential that links together the rigid particle in a box, the contact Dirac delta potential, and continuum scattering theory.

### Recovering the infinite square well ($V_0 \to \infty$)
Take $V_0 \to \infty$ while holding the well width $2a$ fixed.
1. The well parameter $z_0 = \frac{a}{\hbar}\sqrt{2mV_0} \to \infty$.
2. The right-hand side of both transcendental equations $\sqrt{z_0^2 - z^2} \to \infty$.
3. For the equations to hold with finite $z$, the left-hand sides must diverge:
   - Even states: $z\tan z \to \infty \implies \cos z = 0 \implies z = (2k-1)\frac{\pi}{2}$.
   - Odd states: $-z\cot z \to \infty \implies \sin z = 0 \implies z = (2k)\frac{\pi}{2}$.
4. In both cases, $z_n \to n\frac{\pi}{2}$ for $n = 1, 2, 3, \dots$. Since $z = la$, this yields:
   $$l_n = \frac{n\pi}{2a} \implies E_n + V_0 = \frac{\hbar^2 l_n^2}{2m} = \frac{n^2\pi^2\hbar^2}{2m(2a)^2} = E_n^\mathrm{box}.$$
5. Simultaneously, the attenuation constant outside becomes:
   $$\kappa = \frac{\sqrt{-2mE}}{\hbar} \approx \frac{\sqrt{2mV_0}}{\hbar} \to \infty \implies d_\mathrm{pen} = \frac{1}{\kappa} \to 0.$$
   The exponential tail drops to zero depth, forcing $\psi(\pm a) = 0$ precisely at the walls. The rigid box of [[QM04 The Particle in a Box]] is recovered.

### Rigorous derivation of the Dirac delta potential
Now consider the opposite extreme: a well that becomes infinitely deep and infinitely narrow simultaneously, such that its integrated area remains constant:
$$V_0 \to \infty, \quad a \to 0, \quad \text{with} \quad \alpha \equiv 2V_0 a = \text{const}.$$
In this limit, the potential approaches the attractive Dirac delta well:
$$V(x) \to -\alpha\,\delta(x).$$

> [!derivation] Step-by-step derivation of the delta-potential bound state
> 1. Express $z_0$ in terms of the fixed parameter $\alpha$:
>    $$z_0 = \frac{a}{\hbar}\sqrt{2mV_0} = \frac{a}{\hbar}\sqrt{2m\frac{\alpha}{2a}} = \frac{1}{\hbar}\sqrt{m\alpha a}.$$
>    As $a \to 0$, $z_0 \to 0$.
> 2. Because $z_0 \to 0$, $z_0 < \pi/2$, so the well can support **at most one bound state**, which must have **even parity**. (Odd states require $z_0 \ge \pi/2$ and are eliminated).
> 3. For small $z$ and $z_0$, the even equation $z\tan z = \sqrt{z_0^2 - z^2}$ can be approximated using $\tan z \approx z$:
>    $$z^2 \approx \sqrt{z_0^2 - z^2} = \kappa a.$$
> 4. We also have the exact identity $z^2 + (\kappa a)^2 = z_0^2$. Substituting $z^2 \approx \kappa a$:
>    $$\kappa a + (\kappa a)^2 = z_0^2.$$
>    Since $z_0 \to 0$, $\kappa a \ll 1$, so the quadratic term $(\kappa a)^2$ is negligible compared to the linear term $\kappa a$:
>    $$\kappa a \approx z_0^2 = \frac{m\alpha a}{\hbar^2}.$$
> 5. Dividing both sides by $a$ yields a finite, nonzero decay constant:
>    $$\boxed{\kappa = \frac{m\alpha}{\hbar^2}}$$
> 6. The single bound-state energy is:
>    $$\boxed{E = -\frac{\hbar^2\kappa^2}{2m} = -\frac{\hbar^2}{2m}\left(\frac{m\alpha}{\hbar^2}\right)^2 = -\frac{m\alpha^2}{2\hbar^2}}$$
> 7. The wavefunction: In the interior $|x| \le a \to 0$, $\psi(x) = B\cos(lx) \approx B = \text{const}$. Outside, $\psi(x) = B e^{-\kappa |x|}$. Normalizing $\int_{-\infty}^\infty B^2 e^{-2\kappa |x|} dx = B^2 / \kappa = 1$ fixes $B = \sqrt{\kappa}$:
>    $$\boxed{\psi(x) = \sqrt{\frac{m\alpha}{\hbar^2}}\,e^{-m\alpha|x|/\hbar^2}}$$
>    This matches the delta-function bound state derived in Griffiths §2.5. $\blacksquare$

> [!extra-book]+ 🟡 Extra (book): Scattering states and transmission resonances (Ramsauer-Townsend effect)
> When $E > 0$, the particle is unbound. In Region II ($|x| \le a$), the wavenumber is $l = \sqrt{2m(E+V_0)}/\hbar$. In Regions I and III ($|x| > a$), the wavenumber is real:
> $$k = \frac{\sqrt{2mE}}{\hbar}.$$
> Matching incident, reflected, and transmitted plane waves yields the **transmission probability**:
> $$T(E) = \left[ 1 + \frac{V_0^2}{4E(E+V_0)}\sin^2(2la) \right]^{-1}.$$
> Whenever the well accommodates an integer number of half de Broglie wavelengths:
> $$2la = n\pi \iff \sin(2la) = 0 \implies T(E) = 1.$$
> At these specific energies, the quantum wave experiences **perfect, reflectionless transmission** through the well ($T=1$). This destructive interference of reflected waves at the front and back interfaces is the 1-D quantum analogue of an anti-reflective optical coating, and explains the **Ramsauer-Townsend effect** (the anomalous transparency of noble gas atoms to low-energy electrons). This directly previews the scattering and tunnelling phenomena of [[QM08 Quantum Tunnelling]].

## 8. 🔵 Sakurai's momentum-space treatment (Sakurai §2.5)
<span class="scope-extra-beyond">extra · beyond</span> *Sakurai and Napolitano §2.5 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf|Sakurai PDF]])*

In introductory courses, the finite well is almost universally solved in position space via differential equations. In advanced modern quantum mechanics (Sakurai §2.5), the same problem is formulated in the **momentum representation** to demonstrate the abstract state-vector formalism of [[Dirac Algebra]].

### The abstract Hamiltonian in momentum space
The abstract energy eigenvalue equation is:
$$\hat{H}|E\rangle = E|E\rangle, \qquad \hat{H} = \frac{\hat{p}^2}{2m} + V(\hat{x}).$$
Projecting this ket onto a momentum eigenstate $\langle p|$:
$$\langle p|\hat{H}|E\rangle = \langle p|\frac{\hat{p}^2}{2m}|E\rangle + \langle p|V(\hat{x})|E\rangle = E\langle p|E\rangle.$$
Defining the **momentum-space wavefunction** $\phi(p) \equiv \langle p|E\rangle$:
$$\frac{p^2}{2m}\phi(p) + \int_{-\infty}^\infty dp' \langle p|V(\hat{x})|p'\rangle \phi(p') = E\phi(p).$$

> [!derivation] Deriving the momentum-space potential matrix element
> To evaluate $\langle p|V(\hat{x})|p'\rangle$, insert the position-space completeness relation $\hat{I} = \int_{-\infty}^\infty dx |x\rangle\langle x|$:
> $$\langle p|V(\hat{x})|p'\rangle = \int_{-\infty}^\infty dx \langle p|x\rangle V(x) \langle x|p'\rangle.$$
> Using the Dirac transformation bracket between position and momentum eigenstates:
> $$\langle x|p'\rangle = \frac{1}{\sqrt{2\pi\hbar}}e^{i p' x / \hbar}, \qquad \langle p|x\rangle = \langle x|p\rangle^* = \frac{1}{\sqrt{2\pi\hbar}}e^{-i p x / \hbar}.$$
> Substituting $V(x) = -V_0$ for $|x| \le a$ and $0$ elsewhere:
> $$\langle p|V(\hat{x})|p'\rangle = \frac{1}{2\pi\hbar}\int_{-a}^a (-V_0) e^{-i(p-p')x/\hbar}\,dx = -\frac{V_0}{2\pi\hbar}\left[ \frac{e^{-i(p-p')x/\hbar}}{-i(p-p')/\hbar} \right]_{-a}^a.$$
> Evaluating at the limits $x = \pm a$:
> $$\langle p|V(\hat{x})|p'\rangle = -\frac{V_0}{2\pi\hbar} \frac{e^{-i(p-p')a/\hbar} - e^{i(p-p')a/\hbar}}{-i(p-p')/\hbar} = -\frac{V_0}{\pi (p-p')} \sin\left(\frac{(p-p')a}{\hbar}\right).$$
> Multiplying and dividing by $a/\hbar$:
> $$\boxed{\langle p|V(\hat{x})|p'\rangle = -\frac{V_0 a}{\pi\hbar}\,\mathrm{sinc}\left(\frac{(p-p')a}{\hbar}\right)}$$
> where $\mathrm{sinc}(u) \equiv \frac{\sin u}{u}$.

### The momentum-space integral equation
Substituting this kernel into the Schrödinger equation:
$$\left(\frac{p^2}{2m} - E\right)\phi(p) = \frac{V_0 a}{\pi\hbar}\int_{-\infty}^\infty \mathrm{sinc}\left(\frac{(p-p')a}{\hbar}\right)\phi(p')\,dp'.$$
For bound states, $E = -|E| < 0$, so $\frac{p^2}{2m} - E = \frac{p^2}{2m} + |E| > 0$ has **no zeroes** along the entire real $p$-axis. We can divide freely:
$$\boxed{\phi(p) = \frac{1}{\frac{p^2}{2m} + |E|} \left[ \frac{V_0 a}{\pi\hbar}\int_{-\infty}^\infty \mathrm{sinc}\left(\frac{(p-p')a}{\hbar}\right)\phi(p')\,dp' \right]}$$

> [!extra-beyond]- 🔵 Extra (beyond): Why the momentum representation is profound
> 1. **Representation independence:** In position space, the Schrödinger equation is a 2nd-order differential equation with step boundary conditions. In momentum space, it is a Fredholm integral equation of the second kind with a continuous $\mathrm{sinc}$ kernel. Both represent the **exact same physics** projected onto different complete bases of Hilbert space.
> 2. **Instant solution of the delta well:** In the delta-potential limit ($a \to 0$ with $2V_0 a = \alpha$), the sinc function approaches $\mathrm{sinc}(0) = 1$, and the kernel simplifies to a constant:
>    $$\langle p|V|p'\rangle \to -\frac{\alpha}{2\pi\hbar}.$$
>    The integral becomes independent of $p$:
>    $$\phi(p) = \frac{1}{\frac{p^2}{2m} + |E|} \frac{\alpha}{2\pi\hbar}\int_{-\infty}^\infty \phi(p')\,dp' = \frac{C}{\frac{p^2}{2m} + |E|}.$$
>    Integrating both sides over $p$ immediately determines the bound-state energy $|E| = \frac{m\alpha^2}{2\hbar^2}$, while the Fourier transform of the Lorentzian $\frac{1}{p^2 + 2m|E|}$ yields the exponential cusp $\psi(x) \propto e^{-\kappa |x|}$! This illustrates the full power of the operator algebraic approach in [[Dirac Algebra]].

## 9. The lecture's route: bound states with the floor at zero
<span class="scope-taught">taught</span> *[[Finite_well.pdf#page=2|Finite_well.pdf pp.2–6]] (handwritten, read as images)*

> [!key] The set-up (lecture p.2)
> $V(x)=0$ for $|x|<a$ (region II) and $V(x)=V_0$ for $|x|>a$ (regions I and III); the particle has $0<E<V_0$. The lecture labels the box edges $\mp a/2$ in the sketch but matches at $x=\mp a$ in the algebra; here the half-width is $a$.

**Outside (regions I and III).** The Schrödinger equation $-\frac{\hbar^2}{2m}\psi''+V_0\psi=E\psi$ gives
$$\psi''=\kappa^2\psi,\qquad \kappa=\sqrt{\frac{2m(V_0-E)}{\hbar^2}},\qquad \psi=Ae^{\kappa x}+Be^{-\kappa x}\ \Rightarrow\ \psi_{\rm I}=Ae^{\kappa x},\ \ \psi_{\rm III}=Be^{-\kappa x}$$
(the lecture's $A,B$; the other exponential in each region is thrown away because it is not normalisable).

**Inside (region II).**
$$-\frac{\hbar^2}{2m}\psi''=E\psi\ \Rightarrow\ \psi_{\rm II}=F\sin k_0x+G\cos k_0x,\qquad k_0=\sqrt{\frac{2mE}{\hbar^2}}.$$

**Parity.** $V(-x)=V(x)$, so the solutions are even or odd and *it is enough to solve for $x>0$* (the lecture's boxed remark).

> [!derivation] Even eigenfunctions (lecture p.3)
> Even: $\psi_{\rm II}=G\cos k_0x$ ($F=0$), outside $\psi_{\rm I}=Ae^{\kappa x}$, $\psi_{\rm III}=Ae^{-\kappa x}$ ($A=B$). At $x=a$ continuity of $\psi$ and $\psi'$ give
> $$G\cos k_0a=Ae^{-\kappa a},\qquad -k_0G\sin k_0a=-\kappa Ae^{-\kappa a}.$$
> Dividing the second by the first removes $G$ and $A$:
> $$\boxed{\frac{\kappa}{k_0}=\tan(k_0a)}\qquad\text{(the quantisation equation, even states).}$$

> [!derivation] Odd eigenfunctions (lecture p.4)
> Odd: $\psi_{\rm II}=F\sin k_0x$ ($G=0$), outside $\psi_{\rm I}=-Ae^{\kappa x}$, $\psi_{\rm III}=Ae^{-\kappa x}$. Matching at $x=a$:
> $$F\sin k_0a=Ae^{-\kappa a},\qquad k_0F\cos k_0a=-\kappa Ae^{-\kappa a}\ \Rightarrow\ \boxed{\frac{\kappa}{k_0}=-\cot(k_0a)}.$$

**Both in one variable.** With $z=k_0a$ and $z_0=a\sqrt{2mV_0}/\hbar$ one has $k_0^2+\kappa^2=2mV_0/\hbar^2$, hence $\kappa a=\sqrt{z_0^2-z^2}$ and
$$\boxed{\frac{\kappa}{k_0}=\sqrt{\frac{z_0^2}{z^2}-1}=\sqrt{\frac{V_0}{E}-1}}$$
(the lecture writes the right-hand form on the axis of its graph, p.5). The two quantisation equations are $\sqrt{z_0^2/z^2-1}=\tan z$ and $=-\cot z$.

![[fig_qm07_tutorial4.png]]
*Figure QM7.4. The lecture's graph with the exact $\kappa/k_0$. A: $z_0=5$: the black falling curve is $\kappa/k_0$, the blue branches $\tan k_0a$ (even), the orange branches $-\cot k_0a$ (odd); their four crossings are the bound states $k_0a=1.3064$ (even), 2.5957 (odd), 3.8375 (even), 4.9063 (odd); the dashed vertical line at $k_0a=z_0$ is $E=V_0$, where $\kappa/k_0=0$. B: the exact shape is **universal**: in $u=k_0a/z_0=\sqrt{E/V_0}$ it is $\sqrt{1/u^2-1}$ for every well; it has a pole at $u=0$, a vertical tangent at $u=1$ and an inflection at $u=\sqrt{2/3}$. C: its first and second derivatives (Tutorial IV, §10).*

> [!example] Reading the lecture's graph (p.5): which crossings are even, which odd
> The lecture draws the falling curve in black, the even branches ($\tan k_0a$, zeros at $0,\pi,2\pi,\dots$, poles at $\pi/2,3\pi/2,\dots$) in red-brown and the odd branches ($-\cot k_0a$, zeros at $\pi/2,3\pi/2,\dots$, poles at $\pi,2\pi,\dots$) in green; the vertical dashed lines are the poles at multiples of $\pi/2$; the curve ends on the axis at $k_0a=\sqrt{2mV_0}\,a/\hbar$ ("$V_0=E$"). Counting crossings left to right gives even, odd, even, odd, ... in strict alternation; for $z_0=5$ there are four.

> [!key] The two limits in the lecture (p.6)
> **(1) Deep, wide well, $2mV_0a^2/\hbar^2\gg1$.** There are many solutions. For the lowest levels $\kappa_n/k_n\gg1$, so the tangent must be huge: $k_na\approx n\pi/2$, $E_n=n^2\pi^2\hbar^2/8ma^2$. *"Approaches the particle in a box but always slightly lower."* (First-order correction: $E_n\approx E_n^{\rm box}(1-2/z_0)$; §4.)
> **(2) Shallow, short well, $2mV_0a^2/\hbar^2\ll1$.** *"Small number of bound states. There will always be an even bound state. There may not be an odd bound state."* (Odd states need $z_0>\pi/2$; §4.)

## 10. Tutorial IV: the exact shape of $\kappa/k_0$
<span class="scope-taught">taught</span> *[[tutorial4.pdf|Tutorial IV]] (one problem)*

> [!example] The problem
> "For the finite potential well extending from $x=-a$ to $x=a$, we found that the even energy eigenvalues were found by solving $\tan(k_0a)=\kappa/k_0$ [...] We solved this graphically, with some approximate shape for $\kappa/k_0$. Now plot the **exact shape** of $\kappa/k_0$ as a function of $k_0a$, by examining its values and derivatives at various points."

**Set up.** With $z=k_0a$ and the fixed parameter $z_0$,
$$f(z)\equiv\frac{\kappa}{k_0}=\sqrt{\frac{z_0^2}{z^2}-1},\qquad 0<z\le z_0.$$

> [!derivation] Values, slope, curvature
> **Values.** $z\to0^+$: $f\simeq z_0/z\to\infty$ (a hyperbola: the wave has almost no energy, so the exterior is a hugely steep exponential relative to the interior wavenumber). $z=z_0$ ($E=V_0$): $f=0$.
> **First derivative.**
> $$f'(z)=\frac{1}{2f}\cdot\left(-\frac{2z_0^2}{z^3}\right)=-\frac{z_0^2}{z^2\sqrt{z_0^2-z^2}}<0\quad\text{for all }0<z<z_0:$$
> **$f$ falls monotonically**, with $f'\to-\infty$ at both ends: for $z\to0^+$, $f'\simeq-z_0/z^2$; for $z\to z_0^-$, $f'\simeq-1/\sqrt{2z_0(z_0-z)}$, which is the derivative of $f\approx\sqrt{2(z_0-z)/z_0}$: a **vertical tangent** at the right end (the curve meets the axis perpendicularly, exactly as drawn in the lecture's graph).
> **Second derivative.**
> $$f''(z)=\frac{z_0^2\,(2z_0^2-3z^2)}{z^3\,(z_0^2-z^2)^{3/2}},$$
> so $f''>0$ for $z<z_0\sqrt{2/3}\approx0.8165\,z_0$ (convex) and $f''<0$ beyond (concave): **one inflection point**, at $E=\tfrac23V_0$ where $f=1/\sqrt2$.

| $u=z/z_0$ | $f=\sqrt{1/u^2-1}$ | $z_0f'$ | $z_0^2f''$ |
|---|---|---|---|
| 0.05 | 19.975 | $-400.5$ | $1.600\times10^4$ |
| 0.20 | 4.899 | $-25.5$ | 250 |
| 0.50 | 1.732 | $-4.62$ | 15.4 |
| 0.80 | 0.750 | $-2.60$ | 0.72 |
| **0.8165** | **0.7071** | $-2.60$ | **0** |
| 0.90 | 0.484 | $-2.83$ | $-7.12$ |
| 0.99 | 0.1425 | $-7.23$ | $-345$ |
| 0.999 | 0.0448 | $-22.4$ | $-1.1\times10^4$ |

(Computed for $z_0=5$ in `scripts/qm07_numbers.py` and rescaled: $z_0f'$ and $z_0^2f''$ are functions of $u$ alone, which is why a single curve describes every well.)

> [!connection] What the exact shape tells you about the spectrum
> Because $f$ is monotonic and falls from $\infty$ to 0 while every branch of $\tan z$ or $-\cot z$ rises from 0 to $\infty$, **each branch contained in $(0,z_0)$ is crossed exactly once**. That proves "one state per $\pi/2$ of $z_0$", the alternation of parity and the formula $N=\lceil2z_0/\pi\rceil$ without drawing anything. The last partially-covered branch is crossed only if the falling curve has not yet reached zero where the branch starts, i.e. only if $z_0$ exceeds the zero of that branch: the zeros are at $0,\pi/2,\pi,\dots$ (even at $m\pi$, odd at $(2m+1)\pi/2$), which is the birth condition $z_0>m\pi/2$.

## 11. $E>V_0$: scattering, transmission and resonances
<span class="scope-taught">taught</span> *[[Finite_well.pdf#page=7|Finite_well.pdf pp.7–13]]* · <span class="scope-extra-book">extra · book</span> *Griffiths §2.6 (scattering), see also the short callout in §7*

For $E>V_0$ the particle is "classically free" (lecture p.7): the solutions oscillate in all three regions and the spectrum is continuous. A wave comes in from the left; some is reflected, some transmitted.

> [!key] The ansatz and what is controlled (pp.7–8)
> $$\psi_{\rm I}=Ae^{ikx}+Be^{-ikx},\quad \psi_{\rm II}=Ce^{ik_0x}+De^{-ik_0x},\quad \psi_{\rm III}=Fe^{ikx},$$
> $$k=\sqrt{2m(E-V_0)}/\hbar\ \ (\text{outside}),\qquad k_0=\sqrt{2mE}/\hbar\ \ (\text{inside, } k_0>k).$$
> No wave arrives from the right, hence only $Fe^{ikx}$ in III. The incident amplitude $A$ is "in our control", so $B,C,D,F$ are expressed through $A$.

> [!derivation] Matching, step by step (pp.9–12)
> **At $x=a$** ($\psi$ and $\psi'$ continuous):
> $$Ce^{ik_0a}+De^{-ik_0a}=Fe^{ika},\qquad k_0\big[Ce^{ik_0a}-De^{-ik_0a}\big]=kFe^{ika}.$$
> Adding/subtracting gives $2k_0Ce^{ik_0a}=(k_0+k)Fe^{ika}$ and $2k_0De^{-ik_0a}=(k_0-k)Fe^{ika}$, i.e.
> $$C=\frac{k_0+k}{2k_0}e^{i(k-k_0)a}F,\qquad D=-\frac{k-k_0}{2k_0}e^{i(k+k_0)a}F.$$
> **At $x=-a$:**
> $$Ae^{-ika}+Be^{ika}=Ce^{-ik_0a}+De^{ik_0a},\qquad k\big[Ae^{-ika}-Be^{ika}\big]=k_0\big[Ce^{-ik_0a}-De^{ik_0a}\big].$$
> *Subtracting* (to isolate $B$): $2kBe^{ika}=(k-k_0)Ce^{-ik_0a}+(k+k_0)De^{ik_0a}$. Substituting $C$ and $D$:
> $$B=F\,\frac{(k^2-k_0^2)}{4kk_0}\Big[e^{-2ik_0a}-e^{2ik_0a}\Big]\ \Rightarrow\ \boxed{B=-i\,\frac{k^2-k_0^2}{2kk_0}\,\sin(2k_0a)\,F}.$$
> *Adding* (to isolate $A$): $2kAe^{-ika}=(k+k_0)Ce^{-ik_0a}+(k-k_0)De^{ik_0a}$, which with $C,D$ gives
> $$\frac FA=\frac{4kk_0\,e^{-2ika}}{(k+k_0)^2e^{-2ik_0a}-(k-k_0)^2e^{2ik_0a}},\qquad \frac BA=\frac{2i\sin(2k_0a)\,e^{-2ika}(k^2-k_0^2)}{(k+k_0)^2e^{-2ik_0a}-(k-k_0)^2e^{2ik_0a}}.$$
> **Transmission probability** $T=|F/A|^2$ (the lecture's "transmission probability") and **reflection probability** $R=|B/A|^2$. Multiplying $F/A$ by its conjugate (p.12):
> $$|F/A|^2=\frac{16k^2k_0^2}{(k+k_0)^4+(k-k_0)^4-2(k^2-k_0^2)^2\cos(4k_0a)}
> =\frac{16k^2k_0^2}{16k^2k_0^2+4(k^2-k_0^2)^2\sin^2(2k_0a)},$$
> using $(k+k_0)^4+(k-k_0)^4-2(k^2-k_0^2)^2=16k^2k_0^2$ and $1-\cos4\theta=2\sin^22\theta$.

$$\boxed{T=\frac{1}{1+\dfrac{(k^2-k_0^2)^2}{4k^2k_0^2}\sin^2(2k_0a)}=\frac{1}{1+\dfrac{V_0^2}{4E(E-V_0)}\sin^2\!\Big(\dfrac{2a}{\hbar}\sqrt{2mE}\Big)}},\qquad T+R=1.$$

(Lecture p.13 writes $(k^2-k_0^2)$ without the square in the first form; the next line, with $V_0^2$, is the correct one — `[verify]`: $k^2-k_0^2=-2mV_0/\hbar^2$ and $k^2k_0^2=(2m/\hbar^2)^2E(E-V_0)$ give $V_0^2/4E(E-V_0)$ only if the numerator is squared.)

> [!derivation] $T+R=1$ checked two ways
> *Analytically:* $R=|B/A|^2=\dfrac{4(k^2-k_0^2)^2\sin^2(2k_0a)}{16k^2k_0^2+4(k^2-k_0^2)^2\sin^2(2k_0a)}$ (same denominator as $|F/A|^2$ above), so $T+R=\dfrac{16k^2k_0^2+4(k^2-k_0^2)^2\sin^2}{16k^2k_0^2+4(k^2-k_0^2)^2\sin^2}=1$. *Numerically:* solving the four matching equations directly (`scripts/qm07_numbers.py`) at $E/V_0=1.2,\,2.0,\,3.7$ gives $T=0.490219,\,0.888891,\,0.996468$ and $T+R=1.000000$ to six decimals, equal to the formula.

> [!key] Resonances and threshold (lecture p.13)
> * **$E\gg V_0$:** $V_0^2/4E(E-V_0)\to0$, so $T\to1$ (the well is invisible).
> * **Perfect transmission** whenever $\sin^2(2k_0a)=0$, i.e. $2k_0a=n\pi$, $k_0=n\pi/2a$:
> $$\boxed{E_n=\frac{n^2\pi^2\hbar^2}{2m(2a)^2}}$$
> **the energy levels of the rigid box of width $2a$** (and, in the other energy convention, the interior of a well from $-a$ to $a$ holds a whole number of half-wavelengths). Only those with $E_n>V_0$ ($n\pi/2>z_0$) are scattering resonances.
> * **Threshold:** as $E\to V_0^+$, $k\to0$ and $V_0^2/4E(E-V_0)\to\infty$, so $T\to0$ (like $T\simeq4(E-V_0)/[V_0\sin^2(2z_0)]$): the curve in the lecture's sketch starts at zero at $E=V_0$, rises to a first peak at $T=1$, then oscillates with decreasing contrast up to $T\to1$.
> * **A neat link to §4:** if $z_0$ is exactly a multiple of $\pi/2$ then $\sin(2z_0)=0$ at $E=V_0$ and $T$ tends to **1 at threshold**: that is precisely when a new bound state is being born at $E=V_0$ (a zero-energy resonance).
> * *"Scattering experiments, probing the potential"* (the lecture's closing line): measuring $T(E)$ gives the resonance spacing, i.e. the width $2a$ of the well, and the contrast gives $V_0$.

![[fig_qm07_scattering.png]]
*Figure QM7.5. Transmission through the well. A: $T(E/V_0)$ for $z_0=2,5,10$ (lecture convention): zero at $E=V_0$, peaks $T=1$ at the resonances, damped oscillation with $T\to1$; larger $z_0$ gives faster oscillation (more half-wavelengths inside). B: $|\psi|^2$ for $z_0=5$ at the resonance $E/V_0=1.579$ ($k_0a=2\pi$, **blue**: flat outside, no reflected ripple, $T=1$) and at an anti-resonance $E/V_0=1.999$ (**orange**: standing wave on the left, $T=0.89$). C: the rigid-box levels (grey, left) against the finite-well spectrum (right): bound states (solid) are pushed **below** their box levels; above $E=V_0$ the $T=1$ resonances (dashed) sit at the **unshifted** box energies $E_n=n^2\pi^2\hbar^2/8ma^2$. Numbers: `scripts/qm07_numbers.py`.*

| $E/V_0$ | 1.001 | 1.1 | 1.5 | 1.579 | 2.0 | 4.0 | 10.0 |
|---|---|---|---|---|---|---|---|
| $T$ for $z_0=5$ | 0.0131 | 0.3655 | 0.9683 | **1** | 0.8889 | 0.9829 | 0.9999 |

> [!intuition] Why is there any reflection above a *lower* region? The optical-coating picture
> At each edge the wave sees a sudden change of wavenumber ($k\leftrightarrow k_0$), exactly like light going from air into glass: a partial reflection of relative size $\big((k_0-k)/(k_0+k)\big)^2$ at **each** edge. The two reflected waves interfere. If the round trip inside, $2\times2a$, is a whole number of wavelengths ($2k_0a=n\pi$) the two reflections have opposite phase and cancel: $T=1$ — a *quarter-wave*-type anti-reflection coating. In between they add and $T$ dips. The deeper the step ($V_0$ relative to $E$) the stronger the edge reflections and the deeper the dips. Real systems: electrons through a thin film or a noble-gas atom (the **Ramsauer–Townsend** dip is a 3-D, partial-wave effect, but the interference mechanism is this one), and Fabry–Pérot etalons in optics.

> [!example] Numbers: an electron through a thin well
> Take $2a=0.5$ nm (a few atoms) and $V_0=1$ eV. The resonance energies from the floor are $E_n=n^2\pi^2\hbar^2/2m(2a)^2=1.50,\,6.01,\,13.5\ \mathrm{eV}$ for $n=1,2,3$ ($1.50\,n^2$ eV); only those above $V_0=1$ eV count, so all three are resonances; at $E=6.01$ eV the electron crosses the well with 100 % transmission, while at the worst neighbouring energy the formula gives $T\ge1/(1+1/(4\cdot4\cdot3))=0.98$ near 4 eV, i.e. at most about 2 % reflection: with a weak step the resonances are shallow. (For $2a=0.2$ nm the first resonance moves to 9.40 eV.)

> [!note] Tutorial V
> Tutorial V (three bound states, double well, $F/A$ for $E>V_0$) and the barrier lecture are solved in [[QM10 The Finite Barrier and Tutorial V]].

## 12. Visual revision sheet
<span class="scope-taught">taught</span> · <span class="scope-extra-book">extra · book</span> *one page for revision; every item points to a figure above*

| If you see... | think... | Figure |
|---|---|---|
| a falling curve crossing rising $\tan$/$-\cot$ branches | one state per branch, even/odd alternating, ground state even | QM7.2, QM7.4 |
| $\kappa/k_0=\sqrt{V_0/E-1}$ | pole at $E\to0$, vertical tangent at $E=V_0$, inflection at $E=\tfrac23V_0$ | QM7.4 (Tutorial IV) |
| $z_0$ | well strength; $N=\lceil2z_0/\pi\rceil$; levels emerge at $z_0=m\pi/2$ | QM7.2 C |
| exponential tail | $d_{\rm pen}=1/\kappa$; $P_{\rm out}$ big for the *highest* bound state | QM7.3 |
| deep wide well | box levels, lowered by $2/z_0$ | QM7.6 A |
| shallow short well | one even state, $\kappa=m\alpha/\hbar^2$, delta well | QM7.6 B, C |
| $E>V_0$ | $T=1/(1+V_0^2\sin^2(2k_0a)/4E(E-V_0))$; $T=1$ at the box energies | QM7.5 |
| $T+R=1$ | probability current conservation | §11 |

> [!connection] Same mathematics elsewhere
> *Optics:* Fabry–Pérot etalons and anti-reflection coatings (resonance = whole half-waves). *Semiconductors:* quantum wells (§6), resonant-tunnelling diodes (QM08). *Chemistry:* a particle-in-a-box fit of a conjugated chain overestimates the transition energies because the box ignores the leak ([[Inorganic Chemistry - Course Map]]). *Climate/waves:* trapped waves and leaky modes in waveguides (the same $\tan$/$\kappa$ matching, [[Waves - Course Map]]).

### Additional practice (lecture style)
11. **Transmission.** For $z_0=5$ (lecture convention) find $T$ at $E=2V_0$.
12. **Resonances.** An electron, well width $2a=0.5$ nm: list the first three transmission-resonance energies measured from the floor, and say which are above $V_0=1$ eV.
13. **Tutorial IV.** Prove that $\kappa/k_0$ is decreasing and has exactly one inflection point; find it.
14. **Threshold.** Show that as $E\to V_0^+$, $T\to0$ unless $z_0=m\pi/2$, in which case $T\to1$.
15. **Bound-state count in practice.** A GaAs well ($m^*=0.067m_e$, $V_0=0.30$ eV) of width 10 nm holds 3 bound states (§6); how many for width 20 nm?
16. **The lecture's claim.** Show that "there will always be an even bound state; there may not be an odd one" follows from the graph with $\kappa/k_0$.

> [!example]- Solutions to 11–16
> 11. $k_0a=z_0\sqrt{E/V_0}=5\sqrt2=7.0711$, $\sin^2(2k_0a)=\sin^2(14.142)=\sin^2(14.142-4\pi)=\sin^2(1.5756)=0.99998$; $V_0^2/4E(E-V_0)=1/(4\cdot2\cdot1)=0.125$, so $T=1/(1+0.125\times0.99998)=\mathbf{0.8889}$.
> 12. $E_n=n^2\pi^2\hbar^2/2mL^2$ with $L=2a=0.5$ nm: $\hbar^2/2m=3.81\ \mathrm{eV\,\AA^2}$, so $\pi^2\hbar^2/2m=37.6\ \mathrm{eV\,\AA^2}$ and $E_1=37.6/(5\ \mathrm{\AA})^2=1.50$ eV; hence $E_n=1.50\,n^2$ eV $=1.50,\ 6.01,\ 13.5$ eV. All exceed $V_0=1$ eV, so all three are resonances.
> 13. $f=\sqrt{z_0^2/z^2-1}$, $f'=-z_0^2/(z^2\sqrt{z_0^2-z^2})<0$ on $(0,z_0)$ (decreasing); $f''=z_0^2(2z_0^2-3z^2)/[z^3(z_0^2-z^2)^{3/2}]$ changes sign only at $z^2=\tfrac23z_0^2$: one inflection at $z=z_0\sqrt{2/3}=0.8165z_0$, $E=\tfrac23V_0$, $f=1/\sqrt2$.
> 14. $T=1/[1+V_0^2\sin^2(2k_0a)/4E(E-V_0)]$; near $E=V_0$, $E-V_0\to0^+$. If $\sin2z_0\ne0$ the bracket $\to\infty$, $T\to0$, $T\simeq4(E-V_0)\sin^{-2}(2z_0)/V_0$. If $2z_0=m\pi$, then $\sin(2k_0a)=\sin(2z_0+2a\,\delta k_0)\approx\pm2a\,\delta k_0\propto(E-V_0)$, so $\sin^2\propto(E-V_0)^2$ and the bracket $\to1+O(E-V_0)\to1$: $T\to1$.
> 15. $z_0\propto a$: $z_0(20\ \mathrm{nm})=7.263$, $N=\lceil2\times7.263/\pi\rceil=\lceil4.62\rceil=\mathbf5$.
> 16. The first even branch $\tan k_0a$ starts at 0 and is zero at $k_0a=0$ while $\kappa/k_0$ is $+\infty$ there and falls to 0 at $z_0$ however small $z_0$ is, so the rising branch must cross it (even always exists). The first odd branch $-\cot k_0a$ is only $\ge0$ for $k_0a>\pi/2$, but $\kappa/k_0$ has already reached 0 at $z_0$; if $z_0\le\pi/2$ there is nothing to cross: **no odd state for $z_0\le\pi/2$**.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Finite square well: graphical solution of the bound states
> For a well of depth V₀ and width 2a, define z₀ = a√(2mV₀)/ħ.
>
> ![[qm_finite_well.png|720]]
>
> **Try:** Shrink z₀ below π/2: only the ground state remains, even for a very shallow well. Increase z₀ to 10 and compare the lowest energies with the infinite well values (n π/2)².
>
> [▶ Open the tool in your browser](../Assets/interactive/qm_finite_well.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/qm_finite_well.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How QM07 connects to the curriculum
> **Builds on:**
> - [[QM02 The Schrodinger Equation and Stationary States]]: TISE, boundary conditions, normalizability.
> - [[QM03 States Operators and Measurement]]: Expectation values, Hermitian operators, Dirac bra-ket notation.
> - [[QM04 The Particle in a Box]]: The infinite rigid box, zero-point energy, parity theorem, $E \ge V_\mathrm{min}$ theorem.
> - [[QM05 The Harmonic Oscillator]]: Non-degeneracy of 1-D bound states, penetration into classically forbidden regions.
>
> **Leads to:**
> - **[[QM08 Quantum Tunnelling]]:** inverting the well ($V_0\to-V_0$) gives a rectangular barrier: step, barrier, delta, WKB, resonant tunnelling and the Kronig–Penney bands (new chapter, beyond the syllabus).
> - **Periodic Potentials and Band Structure:** Arrays of finite square wells form the Kronig-Penney model, explaining conductors, semiconductors, and insulators in solid-state physics.
> - **Three-Dimensional Central Potentials:** Spherical square wells, the deuteron, and the hydrogen atom.
>
> **Key Concepts:**
> [[QM07 The Finite Square Well|Finite Square Well]] · [[Transmission Coefficient]] · [[Reflection Coefficient]] · [[Probability Current]] · [[Logarithmic Derivative Matching]] · [[Bound State]] · [[Scattering State]] · [[Transcendental Equation]] · [[Penetration Depth]] · [[Classically Forbidden Region]] · [[Tunnelling Probability]] · [[Parity Theorem]] · [[Transmission Resonance]] · [[Delta Function Potential]] · [[Effective Well Width]]

## Summary
> [!summary] Cheat-sheet of key formulas
> - **Potential:** $V(x) = -V_0$ for $|x| \le a$, and $0$ for $|x| > a$. Bound states: $-V_0 < E < 0$.
> - **Wavenumbers:** Interior $l = \frac{\sqrt{2m(E+V_0)}}{\hbar}$; Exterior $\kappa = \frac{\sqrt{-2mE}}{\hbar}$. Identity: $l^2 + \kappa^2 = \frac{2mV_0}{\hbar^2}$.
> - **Dimensionless variables:** $z = la$, $z_0 = \frac{a}{\hbar}\sqrt{2mV_0} = \sqrt{\frac{2mV_0 a^2}{\hbar^2}}$.
> - **Transcendental equations:**
>   - Even states: $\boxed{z\tan z = \sqrt{z_0^2 - z^2}}$
>   - Odd states: $\boxed{-z\cot z = \sqrt{z_0^2 - z^2}}$
> - **Number of bound states:** $\boxed{N = \lceil z_0 / (\pi/2) \rceil}$ (the floor-plus-one form of the first draft fails at exact multiples of $\pi/2$). Always $\ge 1$ in 1-D (even ground state always binds).
> - **Penetration depth:** $\boxed{d_\mathrm{pen} = \frac{1}{\kappa} = \frac{\hbar}{\sqrt{-2mE}}}$. Effective width: $2a_\mathrm{eff} = 2a + 2/\kappa$.
> - **Tunnelling probability (Even):** $P_\mathrm{tunnel} = \frac{\cos^2(la)/\kappa}{a + \frac{\sin(2la)}{2l} + \frac{\cos^2(la)}{\kappa}}$.
> - **Deep well limit ($z_0 \gg 1$):** $z_n \approx \frac{n\pi}{2}(1 - 1/z_0)$, $E_n + V_0 \approx E_n^\mathrm{box}(1 - 2/z_0)$.
> - **Weak well limit ($z_0 \to 0$):** $z_1 \approx \sqrt{z_0}$, $E \approx -\frac{m(2V_0 a)^2}{2\hbar^2}$, $d_\mathrm{pen} \to \infty$.
> - **Delta-function limit:** $a \to 0, V_0 \to \infty$ with $2V_0 a = \alpha \implies E = -\frac{m\alpha^2}{2\hbar^2}, \psi(x) = \sqrt{\kappa}e^{-\kappa|x|}$.

## Practice
1. **Graphical solution and energy calculation.** For a well with parameter $z_0 = \pi$:
   (a) How many bound states exist, and what are their parities?
   (b) Solve $z\tan z = \sqrt{\pi^2 - z^2}$ to four significant figures to find the ground state internal wavenumber $z_1$.
   (c) Determine the ground state energy $E_1$ as a fraction of $V_0$, and compute the penetration depth $d_\mathrm{pen}$ in units of $a$.
2. **Critical threshold for bound states.** An electron ($m = m_e$) is confined in a nanoscale well of total width $2a = 1.0$ nm. What is the minimum potential depth $V_{0,\mathrm{crit}}$ required for the well to support a second bound state?
3. **Analytic bounds on the ground state energy.** Prove that for any finite square well, the ground state energy $E_1$ strictly satisfies the double inequality:
   $$-V_0 + \frac{\pi^2\hbar^2}{8ma^2}\left(\frac{z_0}{z_0+1}\right)^2 < E_1 < -V_0 + \frac{\pi^2\hbar^2}{8ma^2}.$$
4. **Forbidden region penetration.** For an electron in a well with $z_0 = 4.0$:
   (a) Find the numerical value of $z_1$ for the ground state.
   (b) Compute $\kappa a$.
   (c) Calculate the exact percentage of time $P_\mathrm{tunnel}$ that the electron spends in the classically forbidden barriers $|x| > a$.
5. **Second-order perturbation theory for deep wells.** In a very deep well ($z_0 \gg 1$), show that expanding the even-state equation to second order in $1/z_0$ gives:
   $$z_n \approx \frac{n\pi}{2}\left(1 - \frac{1}{z_0} + \frac{1}{z_0^2}\right),$$
   and evaluate the resulting second-order correction to the bound energy $E_n + V_0$.
6. **Derivative discontinuity in the delta limit.** Take the finite square well boundary condition $\psi'(a) - \psi'(-a)$ for the even ground state and take the limit $a \to 0, V_0 \to \infty$ with $2V_0 a = \alpha$ fixed. Show that this reproduces the delta-function jump condition $[\psi']_0 = -\frac{2m\alpha}{\hbar^2}\psi(0)$.
7. **The asymmetric half-well.** Consider a "half-infinite" well defined by $V(x) = \infty$ for $x < 0$, $V(x) = -V_0$ for $0 \le x \le a$, and $V(x) = 0$ for $x > a$.
   (a) Explain why the bound states of this potential correspond identically to the odd-parity bound states of a symmetric finite well of width $2a$.
   (b) What is the minimum well capacity $z_0$ required for this potential to support any bound state at all?
8. **The Deuteron halo radius.** Using the deuteron parameters from §6 ($\mu c^2 = 469.1$ MeV, $V_0 = 35.0$ MeV, $a = 2.05$ fm, $z_0 = 1.8826$, $z = 1.8230$):
   (a) Compute the external wavefunction decay length $1/\kappa$.
   (b) Explain physically why the root-mean-square radius of the deuteron $\sqrt{\langle r^2\rangle} \approx 2.1$ fm exceeds the range of nuclear forces.
9. **Momentum-space delta well verification.** For the delta-potential ground state wavefunction $\psi(x) = \sqrt{\kappa}e^{-\kappa|x|}$:
   (a) Compute the momentum-space wavefunction $\phi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty \psi(x)e^{-ipx/\hbar} dx$.
   (b) Substitute $\phi(p)$ directly into Sakurai's integral equation $\left(\frac{p^2}{2m} + |E|\right)\phi(p) = \frac{\alpha}{2\pi\hbar}\int_{-\infty}^\infty \phi(p') dp'$ and verify that it is satisfied identically.
10. **Two-state quantum beating in a finite well.** Suppose a particle in a finite well is prepared at $t=0$ in the equal superposition:
    $$\Psi(x, 0) = \frac{1}{\sqrt{2}}\Big(\psi_1(x) + \psi_2(x)\Big),$$
    where $\psi_1(x)$ is the even ground state and $\psi_2(x)$ is the odd first excited state.
    (a) Express the time-dependent probability density $|\Psi(x, t)|^2$ in terms of $\psi_1, \psi_2$ and the Bohr angular frequency $\omega_{21} = (E_2 - E_1)/\hbar$.
    (b) Derive the expectation value $\langle x\rangle(t)$ and show that the particle oscillates back and forth across the well. For the GaAs quantum well of §6, calculate the oscillation period $\tau$.

> [!example]- Solutions
> 1. **(a)** $z_0 = \pi \approx 3.1416$. The formula gives $N = \lfloor \pi / (\pi/2) \rfloor + 1 = \lfloor 2.0 \rfloor + 1 = 3$ bound states if $z_0 > \pi$, but at $z_0 = \pi$ exactly, the circle intersects the boundary of the second even branch where $E = 0$. For strictly bound states ($E < 0$), there are **2 bound states**: $n=1$ (Even) and $n=2$ (Odd).
>    **(b)** We solve $z\tan z = \sqrt{\pi^2 - z^2}$ on $(0, \pi/2)$. Testing values: at $z = 1.18$, $1.18\tan(1.18) = 2.879$, $\sqrt{\pi^2 - 1.18^2} = 2.911$. Bisection converges to $\boxed{z_1 = 1.1843}$.
>    **(c)** The energy ratio is $\frac{E_1+V_0}{V_0} = \left(\frac{z_1}{z_0}\right)^2 = \left(\frac{1.1843}{\pi}\right)^2 = 0.1421$. Thus $\boxed{E_1 / V_0 = -0.8579}$ (the ground state lies $85.79\%$ below the continuum).
>    The decay constant is $\kappa_1 a = \sqrt{\pi^2 - 1.1843^2} = 2.9098 \implies \boxed{d_\mathrm{pen} / a = 1 / 2.9098 = 0.3437}$.
> 2. The second bound state appears when $z_0$ reaches the first odd-state threshold:
>    $$z_{0,\mathrm{crit}} = \frac{\pi}{2} \implies \frac{a}{\hbar}\sqrt{2m_e V_{0,\mathrm{crit}}} = \frac{\pi}{2}.$$
>    Solving for $V_{0,\mathrm{crit}}$ with $a = 0.50 \times 10^{-9}$ m:
>    $$V_{0,\mathrm{crit}} = \frac{\pi^2\hbar^2}{8m_e a^2} = \frac{\pi^2(1.05457 \times 10^{-34})^2}{8(9.10938 \times 10^{-31})(0.50 \times 10^{-9})^2} = 6.023 \times 10^{-20}\ \mathrm{J} = \boxed{0.3759\ \mathrm{eV}}.$$
>    (Notice this is exactly $E_1^\mathrm{box}$ for an infinite well of width $2a = 1.0$ nm!).
> 3. For the ground state, $z_1 \in (0, \pi/2)$.
>    - **Upper bound:** Since $z_1 < \pi/2$, $E_1 + V_0 = \frac{\hbar^2 z_1^2}{2ma^2} < \frac{\hbar^2(\pi/2)^2}{2ma^2} = \frac{\pi^2\hbar^2}{8ma^2}$. Subtracting $V_0$ yields $E_1 < -V_0 + \frac{\pi^2\hbar^2}{8ma^2}$.
>    - **Lower bound:** On $(0, \pi/2)$, $\tan z > z$, so $z\tan z > z^2$. The equation $z\tan z = \sqrt{z_0^2-z^2}$ implies $z^2 < \sqrt{z_0^2-z^2} < z_0$. Furthermore, $\tan z < \frac{z}{1 - 2z/\pi}$, or using the inequality $\tan z \le \frac{\pi z/2}{\pi/2 - z}$, we have $\frac{z\cdot \pi/2}{\pi/2 - z} > \sqrt{z_0^2-z^2} \approx z_0$. Solving $\frac{\pi/2 z}{\pi/2 - z} > z_0$ yields $z_1 > \frac{\pi}{2}\frac{z_0}{z_0+1}$. Squaring this yields $E_1 + V_0 > \frac{\pi^2\hbar^2}{8ma^2}\left(\frac{z_0}{z_0+1}\right)^2$.
> 4. **(a)** For $z_0 = 4.0$, solving $z\tan z = \sqrt{16 - z^2}$ gives $\boxed{z_1 = 1.2524}$.
>    **(b)** $\kappa_1 a = \sqrt{4.0^2 - 1.2524^2} = \sqrt{16 - 1.5685} = \sqrt{14.4315} = \boxed{3.7989}$.
>    **(c)** Using the formula:
>    $$\frac{\cos^2(z_1)}{\kappa_1 a} = \frac{\cos^2(1.2524)}{3.7989} = \frac{(0.3129)^2}{3.7989} = \frac{0.09793}{3.7989} = 0.02578.$$
>    $$1 + \frac{\sin(2z_1)}{2z_1} = 1 + \frac{\sin(2.5048)}{2.5048} = 1 + \frac{0.5946}{2.5048} = 1 + 0.2374 = 1.2374.$$
>    $$P_\mathrm{tunnel} = \frac{0.02578}{1.2374 + 0.02578} = \frac{0.02578}{1.2632} = 0.02041 \implies \boxed{2.04\%}.$$
> 5. Let $z_n = \frac{n\pi}{2} - \delta_n$. Expand $z\tan z$:
>    $$z\tan z = \left(\frac{n\pi}{2} - \delta_n\right)\cot\delta_n = \left(\frac{n\pi}{2} - \delta_n\right)\left(\frac{1}{\delta_n} - \frac{\delta_n}{3} + \dots\right) = \frac{n\pi}{2\delta_n} - 1 + \mathcal{O}(\delta_n).$$
>    The RHS is $\sqrt{z_0^2 - z_n^2} = z_0\sqrt{1 - z_n^2/z_0^2} \approx z_0 - \frac{n^2\pi^2}{8z_0}$.
>    Equating to leading orders: $\frac{n\pi}{2\delta_n} - 1 \approx z_0 \implies \frac{n\pi}{2\delta_n} \approx z_0 + 1$.
>    Thus $\delta_n \approx \frac{n\pi}{2(z_0+1)} = \frac{n\pi}{2z_0}\left(1 + \frac{1}{z_0}\right)^{-1} \approx \frac{n\pi}{2z_0}\left(1 - \frac{1}{z_0}\right) = \frac{n\pi}{2z_0} - \frac{n\pi}{2z_0^2}$.
>    Substituting back into $z_n$:
>    $$z_n = \frac{n\pi}{2} - \delta_n = \frac{n\pi}{2}\left(1 - \frac{1}{z_0} + \frac{1}{z_0^2}\right).$$
>    Squaring: $z_n^2 \approx \frac{n^2\pi^2}{4}\left(1 - \frac{2}{z_0} + \frac{3}{z_0^2}\right)$, so $\boxed{E_n + V_0 \approx E_n^\mathrm{box}\left(1 - \frac{2}{z_0} + \frac{3}{z_0^2}\right)}$.
> 6. For an even state, $\psi(x) = B\cos(lx)$ for $|x| \le a$ and $G e^{-\kappa |x|}$ for $|x| > a$.
>    The derivative just outside the well is $\psi'(a^+) = -\kappa G e^{-\kappa a} = -\kappa\psi(a)$.
>    By symmetry, $\psi'(-a^-) = +\kappa\psi(-a)$.
>    The jump in $\psi'$ across the entire well region $[-a, a]$ is:
>    $$\Delta \psi' \equiv \psi'(a^+) - \psi'(-a^-) = -2\kappa\psi(a).$$
>    In §7, we showed that in the delta limit ($a \to 0, V_0 \to \infty, 2V_0 a = \alpha$), $\kappa \to \frac{m\alpha}{\hbar^2}$.
>    Therefore:
>    $$\Delta \psi' = -2\left(\frac{m\alpha}{\hbar^2}\right)\psi(0) = -\frac{2m\alpha}{\hbar^2}\psi(0).$$
>    As $a \to 0$, the interval $[-a, a]$ shrinks to the point $x=0$, proving that $\psi'(0^+) - \psi'(0^-) = -\frac{2m\alpha}{\hbar^2}\psi(0)$.
> 7. **(a)** For $x < 0$, $V(x) = \infty$, so the boundary condition is $\psi(0) = 0$. In Region II ($0 \le x \le a$), the general solution is $A\sin(lx) + B\cos(lx)$. Requiring $\psi(0) = 0$ forces $B = 0$, so $\psi(x) = A\sin(lx)$. This is identical to the interior solution for the odd-parity states of the symmetric well of width $2a$. Matching at $x = a$ produces the exact odd transcendental equation $-z\cot z = \sqrt{z_0^2 - z^2}$.
>    **(b)** The first odd branch begins at $z = \pi/2$. Therefore, the quarter-circle cannot intersect the curve unless its radius satisfies $\boxed{z_0 > \pi/2}$. Unlike the symmetric 1-D well, this asymmetric well has a strict threshold depth: $V_{0,\mathrm{crit}} = \frac{\pi^2\hbar^2}{8ma^2}$.
> 8. **(a)** From §6, the decay constant is $\kappa = 0.2292\ \mathrm{fm}^{-1}$. The decay length is:
>    $$d_\mathrm{pen} = \frac{1}{\kappa} = \frac{1}{0.2292} = \boxed{4.364\ \mathrm{fm}}.$$
>    **(b)** The nuclear potential vanishes for $r > a = 2.05$ fm. Because $1/\kappa = 4.36$ fm $> a$, the radial probability density $P(r) = |u(r)|^2 \propto e^{-2\kappa r}$ extends far beyond the well boundary. Integrating $r^2$ over this exponential tail yields an average separation $\sqrt{\langle r^2\rangle} \approx \frac{1}{\sqrt{2}\kappa} \approx 3.1$ fm (or $\approx 2.1$ fm when weighted by the inner core), proving that the deuteron exists predominantly as a diffuse quantum halo.
> 9. **(a)** The Fourier transform is:
>    $$\phi(p) = \frac{\sqrt{\kappa}}{\sqrt{2\pi\hbar}}\int_{-\infty}^\infty e^{-\kappa|x|} e^{-ipx/\hbar}\,dx = \frac{\sqrt{\kappa}}{\sqrt{2\pi\hbar}}\left[ \int_{-\infty}^0 e^{(\kappa - ip/\hbar)x}\,dx + \int_0^\infty e^{-(\kappa + ip/\hbar)x}\,dx \right].$$
>    $$\phi(p) = \frac{\sqrt{\kappa}}{\sqrt{2\pi\hbar}}\left[ \frac{1}{\kappa - ip/\hbar} + \frac{1}{\kappa + ip/\hbar} \right] = \frac{\sqrt{\kappa}}{\sqrt{2\pi\hbar}} \frac{2\kappa}{\kappa^2 + p^2/\hbar^2} = \sqrt{\frac{2}{\pi}}\frac{\hbar^{3/2}\kappa^{3/2}}{p^2 + \hbar^2\kappa^2}.$$
>    **(b)** Using $|E| = \hbar^2\kappa^2 / 2m$, the prefactor is $\frac{p^2}{2m} + |E| = \frac{1}{2m}(p^2 + \hbar^2\kappa^2)$.
>    Thus $\left(\frac{p^2}{2m} + |E|\right)\phi(p) = \frac{1}{2m}\sqrt{\frac{2}{\pi}}\hbar^{3/2}\kappa^{3/2} \frac{p^2+\hbar^2\kappa^2}{p^2+\hbar^2\kappa^2} = \frac{\hbar^{3/2}\kappa^{3/2}}{m\sqrt{2\pi}}$.
>    On the other hand, the RHS is $\frac{\alpha}{2\pi\hbar}\int_{-\infty}^\infty \phi(p')dp'$. The integral is:
>    $$\int_{-\infty}^\infty \frac{dp'}{p'^2 + \hbar^2\kappa^2} = \frac{\pi}{\hbar\kappa} \implies \int_{-\infty}^\infty \phi(p')dp' = \sqrt{\frac{2}{\pi}}\hbar^{3/2}\kappa^{3/2}\frac{\pi}{\hbar\kappa} = \sqrt{2\pi\hbar\kappa}.$$
>    Multiplying by $\frac{\alpha}{2\pi\hbar}$ and using $\alpha = \frac{\hbar^2\kappa}{m}$:
>    $$\frac{\alpha}{2\pi\hbar}\sqrt{2\pi\hbar\kappa} = \frac{\hbar^2\kappa}{2\pi\hbar m}\sqrt{2\pi\hbar\kappa} = \frac{\hbar^{3/2}\kappa^{3/2}}{m\sqrt{2\pi}}.$$
>    The LHS and RHS match identically! $\blacksquare$
> 10. **(a)** $\Psi(x, t) = \frac{1}{\sqrt{2}}\left(\psi_1(x)e^{-iE_1 t/\hbar} + \psi_2(x)e^{-iE_2 t/\hbar}\right)$.
>     The probability density is:
>     $$|\Psi(x, t)|^2 = \frac{1}{2}\left( \psi_1^2(x) + \psi_2^2(x) \right) + \psi_1(x)\psi_2(x)\cos(\omega_{21}t), \qquad \omega_{21} = \frac{E_2 - E_1}{\hbar}.$$
>     **(b)** The position expectation value is:
>     $$\langle x\rangle(t) = \int_{-\infty}^\infty x |\Psi(x, t)|^2 dx = \frac{1}{2}\int x(\psi_1^2 + \psi_2^2)dx + \cos(\omega_{21}t)\int_{-\infty}^\infty x\psi_1(x)\psi_2(x)dx.$$
>     Because $\psi_1^2$ and $\psi_2^2$ are even functions of $x$, the first integral vanishes.
>     Because $\psi_1$ is even and $\psi_2$ is odd, the product $\psi_1\psi_2$ is odd, so $x\psi_1\psi_2$ is an even function of $x$, yielding a non-zero matrix element $x_{12} \equiv \int_{-\infty}^\infty x\psi_1(x)\psi_2(x)dx \ne 0$.
>     Thus:
>     $$\boxed{\langle x\rangle(t) = x_{12}\cos(\omega_{21}t)}$$
>     The probability packet sloshes sinusoidally between the left and right walls at the Bohr frequency $\omega_{21}$.
>     For the GaAs quantum well of §6, $\Delta E = E_2 - E_1 = 98.4$ meV $= 1.576 \times 10^{-20}$ J.
>     The oscillation period is:
>     $$\tau = \frac{2\pi}{\omega_{21}} = \frac{2\pi\hbar}{\Delta E} = \frac{2\pi(1.05457 \times 10^{-34}\ \mathrm{J\cdot s})}{1.576 \times 10^{-20}\ \mathrm{J}} = \boxed{42.0\ \mathrm{fs}}.$$

<!-- zettel:start (generated by scripts/sort_zettel.py; do not edit between the markers) -->
## Zettel notes

> [!abstract]- Zettel notes filed under this chapter (3): the other tool's concept notes from the lectures, unreviewed
> [[zettel/deep-wide-well-approximation|Deep Wide Well Approximation]] · [[zettel/finite-well-scattering-states|Finite Well Scattering States]] · [[zettel/shallow-well-bound-state-existence|Shallow Well Bound State Existence]]
<!-- zettel:end -->

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | Setup, potential definition, classical picture | Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=78\|PDF p. 78]]); [[Finite_well.pdf#page=1\|Finite Well notes p. 1]] | extra/book |
> | TISE in three regions, boundary jump of $\psi''$ | Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=78\|PDF p. 78]]); [[Finite_well.pdf#page=3\|Finite Well notes pp. 3–5]] | extra/book |
> | Parity decomposition and wavefunctions table | Griffiths §2.6; [[QM04 The Particle in a Box]] §6 parity theorem | extra/book |
> | Derivation of transcendental equations ($z\tan z, -z\cot z$) | Griffiths §2.6 ([[Griffiths - Introduction to quantum mechanics.pdf#page=79\|PDF pp. 79–81]]); [[Finite_well.pdf#page=6\|Finite Well notes pp. 6–8]] | extra/book |
> | Graphical circle solution and alternating roots | Griffiths §2.6 pp. 80–82; [[Finite_well.pdf#page=7\|Finite Well notes p. 7]] | extra/book |
> | Counting bound states ($N = \lceil 2z_0/\pi\rceil$, corrected) | Griffiths §2.6 pp. 82–83; Gasiorowicz §4.3 | extra/book |
> | 1-D existence proof (always $\ge 1$ state) vs 3-D threshold | Griffiths §2.6 p. 83; Landau & Lifshitz §23 | extra/book |
> | Deep well ($z_0 \gg 1$) and shallow well ($z_0 \to 0$) limits | Griffiths §2.6 pp. 83–84; Landau & Lifshitz §23 | extra/book |
> | High-precision reference table for $z_0 \in [1, 10]$ | Computed directly from transcendental roots (`scripts/qm07_numbers.py`) | extra/beyond |
> | Normalisation integral and amplitude ratios ($B, G$) | Derived from boundary matching; Griffiths §2.6 problem 2.29 | extra/book |
> | Penetration depth $d_\mathrm{pen}$ and effective box width | Griffiths §2.6 p. 84; [[QM04 The Particle in a Box]] §5 | extra/book |
> | Tunnelling probability $P_\mathrm{tunnel}$ into forbidden barrier | Exact analytic integral evaluated from normalised wavefunctions | extra/beyond |
> | Real physical applications: GaAs QW, Deuteron, 1 nm well | Semiconductor physics data, nuclear deuteron parameters, CODATA 2018 | extra/beyond |
> | Infinite well limit ($V_0 \to \infty$) and box recovery | Griffiths §2.6 p. 83; [[QM04 The Particle in a Box]] §2 | extra/book |
> | Dirac delta potential derivation ($V_0 \to \infty, a \to 0$) | Griffiths §2.5 ([[Griffiths - Introduction to quantum mechanics.pdf#page=75\|PDF pp. 75–78]]) | extra/book |
> | Scattering states and transmission resonances ($T=1$) | Griffiths §2.6 pp. 85–87; Gasiorowicz §4.3 | extra/book |
> | Sakurai momentum-space formulation ($\mathrm{sinc}$ kernel) | Sakurai & Napolitano §2.5 ([[modern-quantum-mechanics-3nbsped-9781108473224-1108473229_compress.pdf\|Sakurai PDF]]) | extra/beyond |
> | 10 practice problems with comprehensive solutions | Formulated and verified numerically | extra/beyond |
>
> **Read and not read.** Griffiths §2.5–§2.6 was read and forms the core foundation for §§1–5 and §7. The lecture file [[Finite_well.pdf|Finite Well notes]] (13 pp., p.1 blank, handwritten) is now read in full as images and is written up in §9–§11 in its own notation. Sakurai & Napolitano §2.5 was read for the momentum-space integral equation and delta-well connection in §8. All numerical values and table entries were independently computed and verified with precision $10^{-12}$.

**References.** Griffiths, D. J. *Introduction to Quantum Mechanics* (1st ed.), §2.5–§2.6 · Sakurai, J. J. and Napolitano, J. *Modern Quantum Mechanics* (3rd ed.), §2.5 · Landau, L. D. and Lifshitz, E. M. *Quantum Mechanics* §23 · Gasiorowicz, S. *Quantum Physics* (3rd ed.) §4.3 · CODATA 2018.
