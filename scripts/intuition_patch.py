"""Add a concept map (mermaid) and section-level [!intuition] boxes to the chapters that only had a one-sentence story.
Idempotent (marker <!-- intuition-v1 -->); never removes text.   python3 scripts/intuition_patch.py
"""
import glob
import os
import re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

DATA = {
"QM01": dict(map="""flowchart LR
  A["double slit:<br/>dots build a wave pattern"] --> B["Born rule<br/>P = |psi|^2"]
  B --> C["psi is complex:<br/>phases interfere"]
  C --> D["Fourier pairs:<br/>short pulse = many k"]
  D --> E["Delta x Delta p >= hbar/2"]
  E --> F["hydrogen:<br/>size and 13.6 eV"]
  E --> G["Compton scale:<br/>where this stops"]""",
 boxes={
 "## 1. ": "> [!intuition] Single outcomes are random, the pattern is not\n> Each electron lands as one dot at a place you cannot predict; after thousands of dots the stripes of a wave are there. The wave does not tell you *where this electron goes*, it tells you *how likely each place is*. That is the whole meaning of $|\\psi|^2$.",
 "## 2. ": "> [!intuition] Why a complex number\n> To make fringes the amplitudes from two slits must be able to **cancel**. Adding two real positive numbers can't; adding two complex numbers with opposite phase can. The phase is invisible in one slit and decisive when two paths meet.",
 "## 3. ": "> [!intuition] The rubber-band trade\n> To make a sharp pulse you must add waves of many different wavelengths so they all agree at one spot and cancel everywhere else. Sharper in $x$ costs spread in $k$, the way squeezing one end of a rubber band makes the other bulge.",
 "## 5. ": "> [!intuition] $\\Delta x\\,\\Delta p\\ge\\hbar/2$ is a fact about waves, not about clumsy instruments\n> Any wave packet, water or sound included, has $\\Delta x\\,\\Delta k\\ge\\tfrac12$. Quantum mechanics only adds $p=\\hbar k$. The 'uncertainty' is that the particle simply has no sharper pair of values.",
 "## 6. ": "> [!intuition] Hydrogen without solving anything\n> Confining the electron to radius $r$ costs kinetic energy $\\sim\\hbar^2/2mr^2$ (squeezing a wave); the Coulomb attraction gains $-e^2/4\\pi\\varepsilon_0r$. The sum is lowest at $r\\sim0.5$ Å with $E\\sim-13.6$ eV: the Bohr radius and the Rydberg, from the uncertainty principle alone.",
 }),
"QM02": dict(map="""flowchart LR
  A["plane wave:<br/>E = hbar w, p = hbar k"] --> B["operators:<br/>p = -i hbar d/dx"]
  B --> C["time-dependent<br/>Schrodinger equation"]
  C --> D["probability conserved<br/>(continuity)"]
  C --> E["separate variables:<br/>stationary states"]
  E --> F["free particle:<br/>continuous spectrum"]
  E --> G["boundary conditions:<br/>discrete spectrum, ring"]""",
 boxes={
 "## 3. ": "> [!intuition] Energy is the speed of the phase\n> $i\\hbar\\,\\partial_t\\psi=\\hat H\\psi$ says: the faster the phase of a component rotates, the higher its energy. Evolution in time is nothing but each energy component spinning at its own rate $\\omega=E/\\hbar$.",
 "## 4. ": "> [!intuition] Probability behaves like an incompressible fluid\n> $\\partial_t\\rho+\\partial_xj=0$: the probability in a region changes only by what flows through its edges; none appears or vanishes. That is what makes $\\int|\\psi|^2=1$ stay true at all times.",
 "## 5. ": "> [!intuition] A stationary state is a standing wave\n> The shape never changes; only the overall phase spins. Every probability, expectation value and spread is therefore constant, which is why the energy eigenstates are the natural 'resting' states.",
 "## 7. ": "> [!intuition] Why boundaries create a ladder\n> A free wave has any wavelength. Force it to fit between two walls (or round a ring) and only whole numbers of half-waves (or full waves) survive, exactly like the notes of a guitar string. Discreteness is a *fitting* condition.",
 "## 9. ": "> [!intuition] What 'allowed' means\n> The function must have finite total probability (square-integrable), and be smooth enough that the energy is finite: kinks are fine if the potential has a step or a delta, but a wavefunction with a jump has infinite kinetic energy.",
 }),
"QM03": dict(map="""flowchart LR
  A["state:<br/>list of amplitudes c_n"] --> B["operator:<br/>a question you can ask"]
  B --> C["eigenstates:<br/>sharp answers"]
  C --> D["probabilities |c_n|^2<br/>expectation, spread"]
  B --> E["commutators:<br/>which questions are compatible"]
  A --> F["two-level system:<br/>2x2 matrices"]
  F --> G["time evolution:<br/>spinning phases"]""",
 boxes={
 "## 1. ": "> [!intuition] A state is an arrow, its amplitudes are coordinates\n> The same arrow has different coordinates in different bases (energy, position, spin-up/down). Superposition just means the arrow is not along any one of your chosen axes.",
 "## 3. ": "> [!intuition] An eigenstate is a direction the operator does not turn\n> Feed an eigenstate to the operator and it comes back stretched by the eigenvalue but pointing the same way. That is why measuring it gives a sharp result: there is only one number to report.",
 "## 4. ": "> [!intuition] Average, spread and outcome are three different things\n> A single measurement returns one eigenvalue; $\\langle A\\rangle$ is the weighted average over many repetitions (it need not be an allowed outcome); $\\Delta A$ says how mixed the state is. A state with $\\Delta A=0$ is an eigenstate.",
 "## 5. ": "> [!intuition] Commuting questions can be answered together\n> If $[A,B]=0$ there is a common set of axes in which both are sharp. If not, sharpening one smears the other: the commutator sets the exchange rate (QM03 §5 and [[Dirac Algebra]] §8).",
 "## 6. ": "> [!intuition] The whole theory in a 2×2 matrix\n> A two-level system (spin-½, a qubit) has every feature: superposition, non-commuting observables ($X,Y,Z$), measurement collapse, interference. Its state is a point on a sphere and its dynamics a rotation.",
 "## 7. ": "> [!intuition] Time evolution is rotation of the phases\n> In the energy basis each coefficient is multiplied by $e^{-iE_nt/\\hbar}$. With two energies the relative phase drifts and the probabilities beat at $(E_2-E_1)/\\hbar$.",
 }),
"QM04": dict(map="""flowchart LR
  A["rigid walls:<br/>psi = 0 at x = 0, a"] --> B["half-waves fit:<br/>lambda = 2a/n"]
  B --> C["E_n = n^2 pi^2 hbar^2/2ma^2"]
  C --> D["orthonormal basis,<br/>nodes, parity"]
  D --> E["superposition:<br/>sloshing at Bohr frequency"]
  C --> F["zero-point energy,<br/>Dx Dp > hbar/2"]
  C --> G["relax the walls:<br/>QM07 finite well"]""",
 boxes={
 "## 1. ": "> [!intuition] A guitar string clamped at both ends\n> Classically the particle bounces back and forth at constant speed with any energy. Quantum mechanically the *wave* must vanish at both walls, so the allowed shapes are the notes of a clamped string.",
 "## 2. ": "> [!intuition] Why $E\\propto n^2$\n> Wavelength $\\lambda=2a/n$ so momentum $p=h/\\lambda=nh/2a$ and kinetic energy $p^2/2m\\propto n^2$. Halve the box and every level quadruples: confinement costs energy.",
 "## 3. ": "> [!intuition] Count the nodes\n> The $n$th state has $n-1$ interior nodes. More nodes means more curvature, more kinetic energy. The ground state has none but still has energy: a wave cannot be perfectly flat *and* vanish at the walls ([[Zero-Point Energy]]).",
 "## 5. ": "> [!intuition] Why the box never reaches $\\hbar/2$\n> The minimum uncertainty needs a Gaussian; the box states are cut off sharply at the walls and have kinks at the edges, which carry extra momentum spread. The $n=1$ product is $0.568\\hbar$, only 14 % above the bound, and grows linearly with $n$.",
 }),
"QM05": dict(map="""flowchart LR
  A["any well near its minimum<br/>is a parabola"] --> B["factorise H:<br/>ladder operators a-, a+"]
  B --> C["[a-, a+] = 1<br/>rungs differ by hbar w"]
  C --> D["ground state:<br/>a- psi0 = 0, E0 = hbar w/2"]
  D --> E["psi_n = (a+)^n psi0"]
  E --> F["large n:<br/>classical density"]
  E --> G["superposition:<br/>sloshes at w"]""",
 boxes={
 "## 1. ": "> [!intuition] Why this one problem is everywhere\n> Every smooth potential looks like a parabola at its bottom, so every small vibration (molecular bonds, lattice phonons, light modes) is an oscillator. Solve this and you have solved the leading behaviour of all of them.",
 "## 2. ": "> [!intuition] A staircase you can step up and down\n> $\\hat a_+$ adds one quantum $\\hbar\\omega$ of energy, $\\hat a_-$ removes one. The algebra $[\\hat a_-,\\hat a_+]=1$ is the statement that the steps are all the same height.",
 "## 4. ": "> [!intuition] Why the staircase has a bottom rung with energy left over\n> You cannot step below the lowest rung, so $\\hat a_-\\psi_0=0$. That condition alone fixes $E_0=\\tfrac12\\hbar\\omega$: the zero-point energy is the price of squeezing $x$ and $p$ at the same time.",
 "## 5. ": "> [!intuition] Equal spacing\n> $E_n=(n+\\tfrac12)\\hbar\\omega$ is a ruler with evenly spaced marks, the quantum image of 'the period does not depend on the amplitude'.",
 "## 9. ": "> [!intuition] Where the classical picture reappears\n> For large $n$ the quantum density, averaged over its fast wiggles, matches the classical probability to be found at $x$, $\\propto1/\\sqrt{x_t^2-x^2}$: a swinging mass spends most time at the turning points where it moves slowest.",
 }),
"QM06": dict(map="""flowchart LR
  A["normalisation<br/>table"] --> B["number basis |n><br/>Dirac notation"]
  B --> C["expectation values<br/>by ladders"]
  C --> D["Hermite polynomials:<br/>n real zeros"]
  D --> E["momentum space:<br/>same shape, phase (-i)^n"]
  C --> F["Ehrenfest, virial,<br/>Heisenberg picture"]
  F --> G["coherent states"]
  B --> H["thermal oscillator:<br/>Planck, Einstein"]""",
 boxes={
 "## 2. ": "> [!intuition] Label the state by how many quanta it holds\n> $|n\\rangle$ is 'the oscillator with $n$ units of energy'. The ladders are then *counting* operators: $\\hat a_-$ removes a unit (and tells you $\\sqrt n$ ways to do it), $\\hat a_+$ adds one.",
 "## 3. ": "> [!intuition] Only terms that come back survive\n> $\\langle n|\\hat x^2|n\\rangle$ contains products of two ladders; since $\\langle n|m\\rangle=\\delta_{nm}$ only those with one raise and one lower return to $|n\\rangle$. That is why $\\langle x^2\\rangle=(n+\\tfrac12)\\hbar/m\\omega$ costs one line.",
 "## 5. ": "> [!intuition] $x$ and $p$ play identical roles\n> $H=\\tfrac12(p^2+x^2)$ in oscillator units is symmetric under $x\\leftrightarrow p$, so the momentum-space wave function has the same Hermite shape: the Fourier transform of $\\psi_n$ is $(-i)^n\\psi_n$.",
 "## 7. ": "> [!intuition] The most classical quantum state\n> A coherent state is a fixed-size Gaussian blob ($\\Delta x\\Delta p=\\hbar/2$) that rides the classical orbit without spreading. It is what a laser emits: a quantum state with a definite amplitude and phase.",
 "## 8. ": "> [!intuition] Temperature fills the ladder\n> At temperature $T$ rung $n$ is occupied with Boltzmann weight $e^{-n\\hbar\\omega/kT}$ (geometric). If $kT\\ll\\hbar\\omega$ the oscillator is frozen in its ground state and does not store heat: that is Einstein's explanation of why heat capacities drop at low $T$.",
 }),
"TH01": dict(map="""flowchart LR
  A["thermal equilibrium<br/>is transitive"] --> B["zeroth law:<br/>temperature exists"]
  B --> C["equation of state<br/>f(P,V,T)=0"]
  C --> D["ideal-gas scale<br/>T = lim PV/nR"]
  C --> E["state functions,<br/>exact differentials"]
  E --> F["response coefficients<br/>alpha, kappa_T"]
  D --> G["climate link:<br/>virtual temperature"]""",
 boxes={
 "## 2. ": "> [!intuition] Why temperature is a label, not a stuff\n> If A is in equilibrium with C and B is in equilibrium with C then A and B are in equilibrium. So one number (what C reads) can label every body that is in mutual equilibrium: that number is temperature. The law says *nothing* about how it should be scaled.",
 "## 3. ": "> [!intuition] An equation of state is a surface\n> For a simple fluid $(P,V,T)$ live on a 2-D surface in 3-D space: fix any two and the third is determined. Every thermodynamic process is a path on this surface.",
 "## 4. ": "> [!intuition] Why gases make the best thermometers\n> Real gases differ at high density but all obey $PV=nRT$ as $P\\to0$. So the *limit* $\\lim PV/nR$ is the same whichever gas you use: a scale that does not depend on the substance.",
 "## 6. ": "> [!intuition] State function versus path\n> Altitude is a state function (it depends on where you are); distance walked is not. $dU$ is exact: integrating around any closed loop gives zero. $\\delta Q$ and $\\delta W$ are not, which is why they get a $\\delta$.",
 }),
"TH02": dict(map="""flowchart LR
  A["quasi-static processes"] --> B["work W = sum X dx"]
  B --> C["first law:<br/>dU = dQ - dW"]
  C --> D["Joule free expansion:<br/>U depends on T only"]
  C --> E["heat capacities:<br/>C_P - C_V = nR"]
  B --> F["PV diagram:<br/>area = work"]
  F --> G["exact vs inexact"]""",
 boxes={
 "## 1. ": "> [!intuition] Work is organised energy transfer, heat is disorganised\n> Pushing a piston moves *all* molecules in step (work). Warming through a wall nudges molecules at random (heat). Both move energy; only the first can lift a weight.",
 "## 2. ": "> [!intuition] Pick a sign convention and say it out loud\n> $\\Delta U=Q-W$ ($W$ done *by* the system) is the convention of these notes and the engines chapter; $\\Delta U=Q+W$ is the convention of the climate and chemistry texts. They describe the same energy bookkeeping; mixing them is the commonest error.",
 "## 3. ": "> [!intuition] $U$ is the bank balance, $Q$ and $W$ are transactions\n> You cannot say a gas 'contains' so much heat or so much work; you can say it has so much internal energy, and that deposits (heat in, work done on it) change it.",
 "## 4. ": "> [!intuition] Why free expansion tells you about $U$\n> The gas expands into a vacuum: it does no work and exchanges no heat, so $\\Delta U=0$. If the temperature does not change then $U$ cannot depend on volume: $U=U(T)$ for an ideal gas.",
 "## 6. ": "> [!intuition] Read the diagram: area is work\n> The area under a path on the $PV$ plane is the work done by the gas; a closed loop encloses the *net* work. Going round clockwise is an engine, anticlockwise a refrigerator.",
 }),
"TH03": dict(map="""flowchart LR
  A["ideal gas PV = nRT"] --> B["degrees of freedom:<br/>C_V = f R/2"]
  B --> C["gamma = C_P/C_V"]
  C --> D["reversible adiabat<br/>PV^gamma = const"]
  D --> E["Ruchhardt's gamma"]
  D --> F["speed of sound<br/>c = sqrt(gamma R T / M)"]
  D --> G["atmosphere:<br/>dry lapse rate"]""",
 boxes={
 "## 2. ": "> [!intuition] $\\gamma$ counts the ways a molecule can hold energy\n> Monatomic gas: 3 ways (translation), $\\gamma=5/3$. Diatomic at room temperature: 5 (add 2 rotations), $\\gamma=7/5$. The more storage modes, the more heat it takes per kelvin and the closer $\\gamma$ is to 1.",
 "## 3. ": "> [!intuition] Why the adiabat is steeper than the isotherm\n> Compress quickly: all the work goes into heating the gas (no time for heat to leave), so pressure rises both from smaller $V$ *and* higher $T$. The isotherm only has the first effect.",
 "## 5. ": "> [!intuition] Sound is adiabatic\n> Compressions and rarefactions pass too fast for heat to flow between neighbours, so the stiffness is $\\gamma P$, not $P$, giving $c=\\sqrt{\\gamma RT/M}$ (343 m/s at 20 °C).",
 "## 6. ": "> [!intuition] A rising parcel cools without losing heat\n> Rising air expands into lower pressure and does work on its surroundings, so it cools: $dT/dz=-g/c_p\\approx-9.8$ K/km. This is the dry adiabatic lapse rate used throughout the climate chapters.",
 }),
"TH04": dict(map="""flowchart LR
  A["Kelvin and Clausius<br/>statements"] --> B["Carnot cycle:<br/>maximum efficiency"]
  B --> C["eta = 1 - Tc/Th"]
  C --> D["thermodynamic<br/>temperature scale"]
  B --> E["Clausius theorem:<br/>sum dQ/T <= 0"]
  E --> F["entropy dS = dQ_rev/T"]
  F --> G["lost work,<br/>arrow of time"]""",
 boxes={
 "## 2. ": "> [!intuition] Two faces of one law\n> Clausius: heat will not flow from cold to hot by itself. Kelvin: you cannot turn heat from one reservoir entirely into work. If either failed, you could use it to break the other: they are equivalent.",
 "## 3. ": "> [!intuition] Carnot is the speed limit\n> No engine between two reservoirs beats a reversible one, and all reversible engines have the same efficiency $1-T_c/T_h$, independent of the working substance. A 500 K to 300 K engine can never exceed 40 %.",
 "## 5. ": "> [!intuition] Entropy is what's conserved in a reversible round trip\n> $\\delta Q$ is not exact, but $\\delta Q_{\\rm rev}/T$ is: dividing by $T$ turns heat into the change of a state function. In an irreversible process the total entropy goes *up*.",
 "## 7. ": "> [!intuition] Why time has a direction\n> Entropy counts microstates. The macrostate with overwhelmingly more microstates is the one you will find; the reverse path is not forbidden, just absurdly unlikely. That is the arrow of time.",
 }),
"TH05": dict(map="""flowchart LR
  A["which variable is fixed?<br/>picks the potential"] --> B["U, H, F, G"]
  B --> C["chemical work:<br/>mu, grand potential"]
  B --> D["Maxwell relations<br/>(mixed 2nd derivatives)"]
  D --> E["stability:<br/>C_V > 0, kappa_T > 0"]
  C --> F["Gibbs-Duhem,<br/>phase equilibrium"]
  E --> G["third law:<br/>S -> 0"]""",
 boxes={
 "## 1. ": "> [!intuition] The potential is the thing nature minimises under your constraints\n> Hold $T$ and $V$ fixed and the system minimises $F=U-TS$; hold $T$ and $P$ and it minimises $G=U-TS+PV$. Same physics, different bookkeeping for the surroundings.",
 "## 4. ": "> [!intuition] Maxwell relations let you measure the unmeasurable\n> Entropy has no meter, but $(\\partial S/\\partial V)_T=(\\partial P/\\partial T)_V$ and the right side does. They all come from one fact: for a smooth potential the order of the two derivatives does not matter.",
 "## 5. ": "> [!intuition] A ball in a bowl, not on a hill\n> Stable equilibrium needs the potential to be convex: $C_V>0$ and $\\kappa_T>0$. If $\\kappa_T$ were negative squeezing the gas would *lower* its pressure and it would collapse.",
 "## 6. ": "> [!intuition] Why absolute zero cannot be reached\n> Cooling steps remove less entropy the colder you get because $S\\to0$; infinitely many steps would be needed. The third law is a statement about entropy differences vanishing, not just about a number.",
 }),
"TH06": dict(map="""flowchart LR
  A["collisions with walls<br/>give pressure"] --> B["Maxwell speed<br/>distribution"]
  B --> C["mean free path,<br/>effusion"]
  B --> D["equipartition:<br/>kT/2 per mode"]
  D --> E["microstates:<br/>S = k ln Omega, Sackur-Tetrode"]
  E --> F["canonical ensemble<br/>Z, Boltzmann factor"]
  F --> G["Planck mean energy,<br/>radiation constants"]""",
 boxes={
 "## 1. ": "> [!intuition] Pressure is a rain of tiny impacts\n> Each molecule hitting the wall delivers a momentum $2mv_x$; billions per second average into a steady force. $P=\\tfrac13n m\\langle v^2\\rangle$ and so $\\tfrac12m\\langle v^2\\rangle=\\tfrac32kT$: temperature is average kinetic energy.",
 "## 2. ": "> [!intuition] Why the distribution has that shape\n> Each velocity component is independent and Gaussian. Speeds are the length of a 3-D Gaussian vector: few are very slow (small phase-space), few very fast (Boltzmann suppression); the peak sits at $\\sqrt{2kT/m}$.",
 "## 4. ": "> [!intuition] Equipartition works until $kT$ is smaller than the level spacing\n> Each quadratic degree of freedom stores $\\tfrac12kT$ if the thermal energy is large compared with its quantum spacing. Vibrations freeze out at room temperature (the Einstein oscillator, [[QM06 The Oscillator Toolbox]] §8).",
 "## 6. ": "> [!intuition] The Boltzmann factor weighs every state\n> A state of energy $E$ is $e^{-E/kT}$ times as likely as one of zero energy. The partition function $Z=\\sum e^{-E/kT}$ is the normaliser and the generating function: derivatives of $\\ln Z$ give everything.",
 }),
"PR01": dict(map="""flowchart LR
  A["counting:<br/>multiplication principle"] --> B["permutations,<br/>combinations"]
  B --> C["sample space,<br/>events"]
  C --> D["axioms of probability"]
  D --> E["inclusion-exclusion"]
  D --> F["continuity of P"]""",
 boxes={
 "## 1. ": "> [!intuition] Choices multiply, orderings divide\n> If a task has $m$ choices then $n$ choices, there are $mn$ ways. Orderings that you do not care about are over-counted by the number of ways to shuffle them, so divide by it: that is the whole of $\\binom nk=n!/k!(n-k)!$.",
 "## 3. ": "> [!intuition] Three meanings, one calculus\n> Long-run frequency, degree of belief, and a measure on outcomes all satisfy the same three axioms; the theorems do not care which one you have in mind.",
 "## 4. ": "> [!intuition] Add, subtract the double-counted, add back the triple-counted\n> Summing $P(A_i)$ counts overlaps twice; subtract pairwise overlaps; that removes triples too often; add them back; and so on with alternating signs.",
 }),
"PR02": dict(map="""flowchart LR
  A["P(A|B) = P(AB)/P(B)"] --> B["total probability"]
  B --> C["Bayes' rule"]
  A --> D["independence"]
  C --> E["Monty Hall,<br/>urns, exchangeability"]
  D --> F["conditional probability<br/>is a probability"]""",
 boxes={
 "## 1. ": "> [!intuition] Conditioning is zooming in\n> Given $F$ you throw away every outcome outside $F$ and renormalise what is left so it adds to 1. $P(E\\mid F)$ is the share of $F$ that is also in $E$.",
 "## 2. ": "> [!intuition] Bayes flips the question\n> You know how likely the evidence is *given* each cause; you want how likely each cause is *given* the evidence. Multiply the prior by the likelihood, divide by the evidence: updating belief on data.",
 "## 4. ": "> [!intuition] Independent means 'learning one tells you nothing about the other'\n> $P(A\\mid B)=P(A)$. It is not the same as mutually exclusive: exclusive events with positive probabilities are *highly* dependent (knowing one happened rules out the other).",
 "## 6. ": "> [!intuition] The host's choice carries information\n> In Monty Hall the host never opens your door and never the car, so his choice is not random relative to the prize: switching wins with probability 2/3 because the 2/3 that was on the other doors collapses onto the remaining one.",
 }),
"PR03": dict(map="""flowchart LR
  A["random variable:<br/>outcome -> number"] --> B["pmf and cdf"]
  B --> C["expectation = centre of mass"]
  C --> D["Bernoulli, binomial,<br/>hypergeometric, uniform"]
  D --> E["geometric,<br/>negative binomial"]
  D --> F["Poisson limit"]""",
 boxes={
 "## 1. ": "> [!intuition] A random variable is a function, the pmf is its histogram\n> The randomness lives in the experiment; $X$ just reads off a number from each outcome. The pmf says how much probability sits on each number.",
 "## 2. ": "> [!intuition] Expectation is the balance point\n> Put weights $p(x)$ on a ruler at the positions $x$: $E[X]$ is where it balances. It need not be a possible value.",
 "## 3. ": "> [!intuition] Binomial counts successes; hypergeometric counts them without replacement\n> $n$ independent yes/no trials give binomial; draw from a finite pot without putting back and the trials become dependent: hypergeometric. For a big pot they look the same.",
 "## 4. ": "> [!intuition] Waiting for the first success has no memory\n> Having failed $k$ times tells you nothing about the next trial, so the geometric distribution is memoryless (the only discrete one). Convention warning in the chapter: trials or failures.",
 "## 5. ": "> [!intuition] Poisson is the law of rare events\n> $n$ independent trials with tiny success chance $p$ and $np=\\lambda$ fixed: the binomial becomes $e^{-\\lambda}\\lambda^k/k!$. Phone calls per minute, typos per page, decays per second.",
 }),
"PR04": dict(map="""flowchart LR
  A["joint pmf,<br/>marginals"] --> B["independence:<br/>joint = product"]
  A --> C["linearity of expectation<br/>(no independence needed)"]
  C --> D["variance, moments"]
  D --> E["variances of the<br/>standard distributions"]
  D --> F["variance of a sum,<br/>covariance"]""",
 boxes={
 "## 2. ": "> [!intuition] The indicator trick\n> Write a count as a sum of 0/1 indicators; $E[\\text{count}]=\\sum P(\\text{each})$, whatever the dependence. A hat-check problem with $n$ people has $E[\\text{matches}]=1$ for every $n$.",
 "## 3. ": "> [!intuition] Variance is the typical squared distance from the mean\n> It measures spread in *squared* units; the standard deviation takes the root to get back to the units of $X$. $\\mathrm{Var}(X)=E[X^2]-(E[X])^2$ is the shortcut.",
 "## 6. ": "> [!intuition] Covariance is co-movement\n> If $X$ and $Y$ rise together, $\\mathrm{Var}(X+Y)$ exceeds the sum of the variances; if one rises when the other falls, it is smaller (diversification). Independent variables have zero covariance (the converse is false).",
 }),
"PR05": dict(map="""flowchart LR
  A["pdf = density<br/>P(X=x) = 0"] --> B["cdf and pdf"]
  B --> C["uniform, normal,<br/>exponential, gamma ..."]
  C --> D["E[g(X)] by LOTUS"]
  B --> E["transformations:<br/>the cdf method"]
  C --> F["exponential:<br/>memoryless"]""",
 boxes={
 "## 1. ": "> [!intuition] Density, not probability\n> $f(x)\\,dx$ is the probability of being in a tiny interval; a single point has probability 0. The pdf can exceed 1 (a narrow spike) as long as its area is 1.",
 "## 3. ": "> [!intuition] LOTUS saves a step\n> To get $E[g(X)]$ you do not need the distribution of $g(X)$; just integrate $g(x)f(x)$. It works because averaging after transforming equals transforming, then averaging over the original weights.",
 "## 5. ": "> [!intuition] When in doubt, transform the cdf\n> $P(g(X)\\le y)$ is an event about $X$; compute it, then differentiate. The pdf formula with Jacobians is a shortcut for the monotone case only.",
 "## 6. ": "> [!intuition] The exponential has no memory\n> $P(X>s+t\\mid X>s)=P(X>t)$: if a bulb has lasted $s$ hours its remaining life has the same distribution as a new bulb's. It is the only continuous distribution with this property.",
 }),
"PR06": dict(map="""flowchart LR
  A["moments:<br/>location, spread,<br/>skew, tails"] --> B["MGF M(t) = E e^{tX}"]
  B --> C["MGFs by first principles"]
  C --> D["applications:<br/>sums, identification"]
  D --> E["Markov, Chebyshev"]
  E --> F["law of large numbers,<br/>central limit theorem"]""",
 boxes={
 "## 1. ": "> [!intuition] Four numbers tell the story of a distribution\n> Mean = where it sits, variance = how wide, skewness = which way it leans, kurtosis = how heavy the tails are. Two distributions with the same mean and variance can look very different.",
 "## 2. ": "> [!intuition] The MGF is all the moments in one function\n> Expand $e^{tX}=\\sum t^kX^k/k!$: the coefficient of $t^k/k!$ is $E[X^k]$. Derivatives at $t=0$ read the moments off, and the MGF of a sum of independent variables is the *product* of their MGFs.",
 "## 5. ": "> [!intuition] Averages settle down, and their wobble is Gaussian\n> The LLN says $\\bar X_n\\to\\mu$; the CLT says the leftover wobble $(\\bar X_n-\\mu)\\sqrt n/\\sigma$ looks like a standard normal whatever the original distribution (finite variance). That is why the bell curve is everywhere.",
 }),
"PA01": dict(map="""flowchart LR
  A["statements,<br/>connectives"] --> B["truth tables,<br/>equivalence"]
  B --> C["tautologies,<br/>contradictions"]
  B --> D["conditionals:<br/>converse, contrapositive"]
  D --> E["predicates,<br/>quantifiers"]
  E --> F["methods of proof"]""",
 boxes={
 "## 2. ": "> [!intuition] A truth table is a logic calculator\n> Two statements are the same *logically* exactly when their columns agree on every row. Checking a table replaces arguing.",
 "## 5. ": "> [!intuition] 'If P then Q' is only broken by P true and Q false\n> A promise is violated only if the condition holds and the result fails. So the contrapositive ($\\neg Q\\Rightarrow\\neg P$) is equivalent, but the converse ($Q\\Rightarrow P$) is a different claim.",
 "## 6. ": "> [!intuition] $\\forall$ is an infinite AND, $\\exists$ an infinite OR\n> Negating swaps them: 'not every swan is white' means 'some swan is not white'. Order of mixed quantifiers matters: $\\forall x\\exists y$ is weaker than $\\exists y\\forall x$.",
 "## 8. ": "> [!intuition] Choose the proof by what the negation gives you\n> Direct if the hypothesis hands you something to work with; contrapositive if the negated conclusion does; contradiction if assuming the opposite quickly gets absurd; induction if the claim is a list indexed by $\\mathbb N$.",
 }),
"PA02": dict(map="""flowchart LR
  A["sets, subsets,<br/>power set"] --> B["algebra of sets<br/>(mirrors logic)"]
  B --> C["indexed families,<br/>products"]
  C --> D["ordered pairs<br/>(Kuratowski)"]
  D --> E["Russell's paradox<br/>-> ZFC axioms"]""",
 boxes={
 "## 1. ": "> [!intuition] A set is defined by its members, nothing else\n> Order and repetition do not matter. The power set of an $n$-element set has $2^n$ members because each element is 'in' or 'out' of a subset.",
 "## 2. ": "> [!intuition] Set algebra is logic in disguise\n> $\\cup\\leftrightarrow\\vee$, $\\cap\\leftrightarrow\\wedge$, complement $\\leftrightarrow\\neg$: De Morgan for sets is De Morgan for statements.",
 "## 4. ": "> [!intuition] How to make order out of unordered sets\n> $(a,b):=\\{\\{a\\},\\{a,b\\}\\}$. All that is needed of an ordered pair is $(a,b)=(c,d)\\iff a=c,\\ b=d$, and this definition has it.",
 "## 5. ": "> [!intuition] Why axioms\n> 'The set of all sets that are not members of themselves' contradicts itself (Russell). ZFC restricts how sets may be built (separation instead of free comprehension) so that such objects never arise.",
 }),
"PA03": dict(map="""flowchart LR
  A["relation = set of pairs"] --> B["reflexive, symmetric,<br/>transitive, antisymmetric"]
  B --> C["equivalence relation<br/>= partition"]
  B --> D["partial order,<br/>Hasse diagram"]
  D --> E["Zorn's lemma"]
  E --> F["every vector space<br/>has a basis"]""",
 boxes={
 "## 1. ": "> [!intuition] Draw a relation as arrows\n> Reflexive: a loop at every point. Symmetric: every arrow has a return arrow. Transitive: two-step paths have a shortcut. A property is a pattern you can check by eye.",
 "## 2. ": "> [!intuition] An equivalence relation sorts things into bins\n> Equivalence classes never overlap and cover everything: that is a *partition*, and every partition comes from a unique equivalence relation. Congruence mod $n$ sorts integers into $n$ bins.",
 "## 3. ": "> [!intuition] Partial: some pairs can't be compared\n> Divisibility is a partial order: neither 2 nor 3 divides the other. Hasse diagrams draw only the cover relations; a *chain* is a totally ordered path through it.",
 "## 4. ": "> [!intuition] Zorn: if every chain has a ceiling, something is maximal\n> It is the tool that lets you pick a largest object without constructing it: maximal linearly independent sets are bases, maximal ideals exist. It is equivalent to the axiom of choice.",
 }),
"PA04": dict(map="""flowchart LR
  A["function:<br/>one output per input"] --> B["injective, surjective,<br/>bijective"]
  B --> C["same cardinality<br/>= bijection"]
  C --> D["countable sets:<br/>N, Z, Q"]
  C --> E["uncountable:<br/>R, power set (Cantor)"]""",
 boxes={
 "## 2. ": "> [!intuition] No collisions, nothing missed, both\n> Injective: different inputs, different outputs. Surjective: every target is hit. Bijective: a perfect pairing, so you can undo it (an inverse exists).",
 "## 3. ": "> [!intuition] 'Same size' means 'can be paired off'\n> That definition, not counting, is the one that works for infinite sets, and it has surprises: the even numbers pair off perfectly with all of $\\mathbb N$ (Hilbert's hotel).",
 "## 4. ": "> [!intuition] Countable = can be listed\n> $\\mathbb Z$ and $\\mathbb Q$ can be put in an infinite list, even though $\\mathbb Q$ is dense: walk the grid of fractions diagonally and skip repeats.",
 "## 5. ": "> [!intuition] Cantor's diagonal\n> Given any list of real numbers, build a new one that differs from the $n$th number in its $n$th digit: it is not on the list. So $\\mathbb R$ is strictly bigger than $\\mathbb N$, and $P(S)$ is always bigger than $S$.",
 }),
"PA05": dict(map="""flowchart LR
  A["induction:<br/>base case + step"] --> B["warnings:<br/>false proofs"]
  A --> C["well-ordering principle"]
  C --> D["strong induction"]
  D --> E["where the numbers<br/>come from"]""",
 boxes={
 "## 1. ": "> [!intuition] Dominoes\n> The base case tips the first domino; the inductive step says each domino tips the next. Both are needed: a step without a base is a row of dominoes nobody pushes; a base without a step is one fallen domino.",
 "## 3. ": "> [!intuition] 'Every nonempty set of naturals has a least element'\n> This is induction in different clothing, and it is the engine of proofs by 'minimal counterexample': if a counterexample exists, the smallest one leads to a contradiction.",
 "## 4. ": "> [!intuition] Strong induction lets you use *all* smaller cases\n> Prime factorisation: $n$ is prime or $ab$ with $a,b<n$, so assume the claim for every smaller number. Weak induction (only $n-1$) would not be enough.",
 }),
"PA06": dict(map="""flowchart LR
  A["Q has holes<br/>(sqrt 2)"] --> B["completeness:<br/>sup exists"]
  B --> C["consequences:<br/>Archimedes, density"]
  B --> D["sequences,<br/>limits (epsilon-N)"]
  D --> E["monotone convergence,<br/>Cauchy, Bolzano-Weierstrass"]""",
 boxes={
 "## 1. ": "> [!intuition] $\\mathbb Q$ is full of invisible holes\n> The rationals $1,\\,1.4,\\,1.41,\\,1.414,\\dots$ keep getting closer to each other but converge to no rational number. $\\mathbb R$ is $\\mathbb Q$ with every such hole filled.",
 "## 2. ": "> [!intuition] Completeness: no holes\n> Every nonempty set that is bounded above has a *least* upper bound in $\\mathbb R$. This one property separates $\\mathbb R$ from $\\mathbb Q$ and is behind every theorem of calculus.",
 "## 4. ": "> [!intuition] $\\varepsilon$-$N$ is a game\n> I give you a tolerance $\\varepsilon$; you must find a point $N$ after which the sequence never again strays by more than $\\varepsilon$. A limit exists when you can always win.",
 "## 5. ": "> [!intuition] Three faces of completeness\n> Bounded monotone sequences converge; Cauchy sequences converge; bounded sequences have convergent subsequences. Each is the least-upper-bound property in a different costume.",
 }),
"PA07": dict(map="""flowchart LR
  A["metric: distance<br/>with three rules"] --> B["convergence, continuity,<br/>completeness"]
  B --> C["topological space:<br/>forget distance, keep 'open'"]
  C --> D["compactness"]
  C --> E["connectedness,<br/>intermediate value theorem"]""",
 boxes={
 "## 1. ": "> [!intuition] Three rules make a notion of nearness\n> Positive (distinct points are apart), symmetric, and the triangle inequality (a detour is never shorter). Anything that satisfies them, from city blocks to functions to words, supports limits and continuity.",
 "## 3. ": "> [!intuition] Topology keeps only 'who is near whom'\n> You can bend, stretch and squash a space; as long as neighbourhoods are preserved, topology does not notice. A coffee cup and a doughnut are the same.",
 "## 4. ": "> [!intuition] Compact: no escape to infinity or to a missing boundary point\n> In $\\mathbb R^n$ that is exactly closed and bounded (Heine–Borel). Its great consequence: a continuous function on a compact set attains its maximum.",
 "## 5. ": "> [!intuition] Connected: in one piece\n> A set that cannot be split into two disjoint open parts. The intermediate value theorem is the statement that a continuous image of an interval is connected: it cannot jump over a value.",
 }),
"CH01": dict(map="""flowchart LR
  A["octet rule fails:<br/>BeH2, NO, SF6"] --> B["VSEPR:<br/>electron pairs repel"]
  A --> C["valence bond:<br/>spin-paired overlap"]
  C --> D["promotion,<br/>hybridisation"]
  D --> E["Coulson:<br/>cos(theta) = S/(S-1)"]
  E --> F["Bent's rule"]
  B --> G["steric number,<br/>lone-pair rules"]""",
 boxes={
 "## 2. ": "> [!intuition] Tie balloons at a point\n> Each region of electron density is a balloon: they push apart until the angles are as large as they can be. A lone pair is a fatter balloon (closer to the nucleus), so it squeezes the bonds and takes the roomy equatorial site.",
 "## 3. ": "> [!intuition] A bond is two electrons sitting between two nuclei\n> Valence bond theory writes Lewis's electron pair as a wave function: the electrons are shared in the overlap region, with opposite spins. More overlap, stronger bond.",
 "## 4. ": "> [!intuition] Hybrids are orbitals pointed at the bonds\n> Mixing $s$ and $p$ on one atom gives lobes that point towards the neighbours and overlap better than pure $s$ or $p$; the energy cost of promotion is repaid by the stronger bonds.",
 "## 5. ": "> [!intuition] More $s$ means a wider angle\n> Orthogonality of two equivalent hybrids forces $\\cos\\theta=S/(S-1)$: $s$-richer hybrids spread out ($sp$ 180°, $sp^2$ 120°, $sp^3$ 109.5°); $p$-richer ones close up towards 90°.",
 "## 7. ": "> [!intuition] Electronegative groups prefer the $p$-rich orbitals\n> Putting the bonding electrons in orbitals with little $s$ character keeps the low-energy $s$ electrons on the central atom: so electronegative substituents take the $p$-rich (axial) sites, and angles close up.",
 }),
}

FILES = {}
for pat in ("0*/*.md", "1*/*.md"):
    for f in glob.glob(os.path.join(ROOT, pat)):
        b = os.path.basename(f)
        m = re.match(r"((?:QM|TH|PR|PA|CH)\d\d) ", b)
        if m:
            FILES[m.group(1)] = f


def insert_after_heading(s, prefix, block):
    m = re.search(r"^" + re.escape(prefix) + r"[^\n]*\n", s, re.M)
    if not m:
        return s, False
    pos = m.end()
    # skip blank lines, then a scope/citation span line if present
    rest = s[pos:]
    m2 = re.match(r"((?:[ \t]*\n)*)(<span class=\"scope[^\n]*\n)", rest)
    if m2:
        pos += m2.end()
        return s[:pos] + "\n" + block + "\n" + s[pos:], True
    return s[:pos] + "\n" + block + "\n" + s[pos:], True


done = []
for key, d in DATA.items():
    f = FILES.get(key)
    if not f:
        print("no file for", key); continue
    s = open(f).read()
    if "<!-- intuition-v1 -->" in s:
        continue
    miss = []
    for prefix, block in d["boxes"].items():
        s, ok = insert_after_heading(s, prefix, block)
        if not ok:
            miss.append(prefix)
    # concept map after the one-sentence story callout (end of its '>' block)
    m = re.search(r"^> \[!intuition\] The one-sentence story[^\n]*\n(?:>[^\n]*\n)*", s, re.M)
    mapblock = ("\n<!-- intuition-v1 -->\n```mermaid\n" + d["map"] + "\n```\n*Concept map: how the ideas of this chapter depend on each other (read left to right; every box is a section).*\n")
    if m:
        s = s[:m.end()] + mapblock + s[m.end():]
    else:
        miss.append("(story)")
    open(f, "w").write(s)
    done.append(key)
    if miss:
        print(key, "missing anchors:", miss)
print("patched", len(done), done)
