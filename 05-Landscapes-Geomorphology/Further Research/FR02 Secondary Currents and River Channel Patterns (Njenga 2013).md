---
title: FR02 Secondary Currents and River Channel Patterns (Njenga 2013)
aliases: [FR02, Njenga 2013, secondary current, helical flow, meander stability, phase shift angle, river channel classification]
subject: landscapes
type: chapter
part: Further Research
scope: [extra-book]
by: [papers, ai-notes]
status: draft
prereq: ["[[LS16 Fluvial Landscapes]]", "[[FR01 Braided Rivers in 3D (Olsen 2021)]]"]
tags: [subject/landscapes, type/chapter, extra/book, src/papers, src/ai-notes, status/draft]
---
# FR02 · Secondary Currents and River Channel Patterns (Njenga 2013)

◀ [[FR01 Braided Rivers in 3D (Olsen 2021)]] · [[Further Research - Landscapes Papers]] · next: [[FR03 Flow at a River Bend with CCHE2D (Das and Biswal 2023)]]

<span class="scope-extra-book">extra · paper (not examinable, read for understanding)</span>

> [!summary] The paper in one paragraph
> K. J. Njenga, K. J. Kioko and G. P. Wanjiru, **"Secondary Current and Classification of River Channels"**, *Applied Mathematics* 4 (2013) 70–78 ([[Secondary_Current_and_Classification_of_River_Chan.pdf]]). It is an **analytical** paper, a pencil-and-paper counterpart of the computer study in [[FR01 Braided Rivers in 3D (Olsen 2021)]]. Starting from the force-momentum (Navier–Stokes-type) equations in a curved channel, the authors do a **small-perturbation stability analysis** of a straight channel with a sinuous disturbance and ask how the **secondary current** (the spiral flow in a bend) feeds back on the channel. Their main claim: the **phase shift angle** between the secondary current and the displacement of the channel axis controls the planform; as that angle decreases the river passes **from straight, to meandering, to braided**, and meander **growth** dominates meander **migration** at small phase shift.

> [!key] After this chapter you can
> - define secondary currents and explain the transverse force balance that creates them (superelevation of the water surface),
> - state what a linear (small-perturbation) stability analysis does, and read its output as a **growth rate** and a **migration rate**,
> - say what the paper concludes about the phase shift angle and how it classifies river patterns, and
> - judge the claim critically: what the analysis assumes and what it leaves out.

> [!intuition] The picture in words
> Water in a bend feels a **centrifugal** push outward. The water *surface* tilts up toward the outer bank until the pressure difference balances the push on the average flow (superelevation). Near the bed, however, the water moves more slowly (friction), so the centrifugal push is weaker there while the pressure gradient (set by the surface tilt) is the same: **near the bed the water flows inward, at the surface outward**, a spiral superimposed on the downstream flow. The spiral carries bed sediment toward the **inner bank** (bar building) while the surface flow presses on the **outer bank** (erosion): the bend grows. The paper asks: *does the spiral help the bend grow, or move it, or stabilise it?*

## 1. The physics the paper starts from
> [!derivation] Transverse force balance and the superelevation (my worked example of the paper's assumption)
> The abstract states the assumption: *the transverse force from the bed is negligible, so the pressure force from the transverse surface inclination is balanced by the centripetal force.* For a channel bend of radius $r$ with depth-mean downstream velocity $u$ and transverse surface slope $S_r$ this is $gS_r=u^2/r$, so across a channel of width $B$ the water level on the outside is higher by
> $$\Delta h=S_rB=\frac{u^2B}{gr}.$$
> For the Gomati bend of [[FR03 Flow at a River Bend with CCHE2D (Das and Biswal 2023)]] ($B=42.7$ m, $r=60.2$ m) and $u=0.56$ m/s: $\Delta h=2.3$ cm; for $u=0.77$ m/s: $4.3$ cm (`scripts/fr_numbers.py`). *A few centimetres of tilt is all it takes to drive the helical flow.* The paper's two momentum equations (their Eqs. 1–2, for the downstream and transverse directions in cylindrical coordinates) contain exactly these terms plus the shear stresses; after dropping time derivatives (steady flow) and the small vertical velocity, only the **transverse** component $v$ of the secondary current matters.

## 2. What a small-perturbation stability analysis does
> [!key] The method in four steps
> 1. Start from a **base state**: a straight channel with uniform flow (stable until perturbed).
> 2. **Perturb** the channel axis by a small sinuous displacement of wavenumber $k$, and write the perturbation as $e^{i(kx-\omega t)}$ with *complex* $\omega$.
> 3. **Linearise** the equations (keep terms linear in the small perturbation), obtaining an algebraic relation $\omega(k)$.
> 4. **Read the answer:** the imaginary part of $\omega$ is a **growth rate** (positive: the perturbation grows, the channel is unstable) and the real part gives a **migration speed** $\operatorname{Re}\omega/k$ (the meander moves downstream).
> This is the same procedure as for waves and diffusion in [[Fourier and Laplace Transforms]] §6, and the growth/migration split is exactly the **pole** picture of §7.6 ($s=-i\omega$: $\operatorname{Re}s$ is growth or decay, $\operatorname{Im}s$ is oscillation). It is also the method of the AI-written notes on braiding ([[river_braiding-1.pdf]], Ch. 4), where the unstable perturbation is a *bar* instead of a sinuous axis.
> **The paper's result for the linear equation:** orthogonal components of the solution give **the rates of meander growth and downstream migration**. The key parameter is the **phase shift angle** $\phi$ between the secondary current and the axis displacement: how far (in phase) the bed-sediment-moving spiral lags or leads the sinuous channel.

## 3. The conclusions of the paper
> [!example] What Njenga et al. report (abstract, §5)
> - **Instability increases as the phase shift angle decreases.** Quantitatively they classify using values of $\phi$ (the symbol was lost in the PDF text extraction; the numbers, probably radians since $\pi/2=1.5708$, are quoted as): *stable* above $\approx1.56$; *moderately stable* $1.55$–$1.56$; *moderately unstable* $1.53$–$1.55$; *unstable* $1.46$–$1.53$; *highly unstable* below $1.46$. In terms of patterns: **straight** for $\phi\ge1.56$; the **straight-to-meandering transition** at $1.55$–$1.56$; **meandering** at $1.53$–$1.55$; the **meandering-to-braiding transition** at $1.46$–$1.53$; **braiding** below $1.46$. The *dominant meander wavelength* occurs for $\phi$ between $1.53$ and $1.55$. `[verify]` against the printed paper (Figs 4–5 and the discussion of Eq. 37).
> - **Why (their explanation):** a smaller phase shift means the secondary current exerts **more resistance on the primary flow**, which causes **more deposition** and hence bars and **braiding**; secondary currents are then directed more at the banks, causing **more erosion on the concave bank and more deposition on the convex bank**.
> - **Growth versus migration:** at small $\phi$ meander **growth dominates** downstream migration, and vice versa.
> - **A second parameter:** the pattern changes from straight to meandering to braided as the ratio of the **longitudinal surface velocity to the bottom shear velocity decreases**, i.e. as the bottom shear velocity (roughness) increases: more roughness $\Rightarrow$ more resistance $\Rightarrow$ more deposition $\Rightarrow$ bars $\Rightarrow$ braiding.
> - **Triggers:** anything that generates secondary currents (a change in slope, a change in width, ripples) can destabilise a channel.

> [!intuition] The empirical background the paper cites
> Before the analysis the paper reviews older, *empirical* classifications: slope–discharge diagrams (Leopold and Wolman), the finding that **larger width-to-depth ratios** characterise braided rivers, a lower limit of **sinuosity $\approx1.5$** for meandering rivers, and rules built from the depth–width ratio $H/B$, the slope $S$ and the Froude number $F$ (the Simons-type diagram, their Fig. 1) that separate braided, meandering, transitional and straight channels. Their contribution is to give such classifications a **mechanistic** basis through the secondary-current phase shift. The same slope–discharge diagram is discussed in the AI notes (the chapter on quantifying braided patterns).

## 4. Reading it critically
> [!pitfall] Limits of the analysis
> 1. **Linear and small-amplitude:** it describes the *onset* of meandering or braiding; actual meanders and braids are finite-amplitude, nonlinear (cut-offs, avulsions, [[FR01 Braided Rivers in 3D (Olsen 2021)]] §4).
> 2. **Sub-critical flow, hydrostatic pressure, shallow channels ($H\ll B,r$)**, as stated by the authors; mostly the lower course of a river.
> 3. **Assumptions about the form of the transverse velocity profile** are taken from earlier work and *"existing equations of the transverse velocity profile were analysed"*; the result depends on that closure.
> 4. The quantitative thresholds for $\phi$ are tied to the particular model and to the data they apply it to (a river example with figures); there is no independent field test of the classification in the parts of the paper I read.
> 5. The mechanism is *one* of several (alternate-bar instability, bank erosion, vegetation) that can lead to braiding.

## 5. Connections
> [!connection] Where this fits in the vault
> - **Meandering and braiding as instabilities:** see [[FR01 Braided Rivers in 3D (Olsen 2021)]] (numerical experiment), the AI notes `river_braiding` (bar-instability theory with $\beta_c(m)$), and [[LS16 Fluvial Landscapes]] (alluvial rivers).
> - **Complex growth rate $\omega$** and stability by the sign of $\operatorname{Im}\omega$: [[Fourier and Laplace Transforms]] §7.6; [[Fixed Points and Linear Stability]] (eigenvalue sign), [[Bistability and Tipping Points]].
> - **Rotating-frame forces:** a bend is a rotating frame, and centrifugal and Coriolis effects are the same physics at river and atmospheric scale: [[Rotating Reference Frames]], [[CL12 Rotating Frames and the Coriolis Force]].
> - **Probability/statistics of planform:** [[Probability - Course Map]] (sinuosity distributions) and [[LS03 Digital Elevation Models and Terrain Analysis]] (measuring planform from DEMs).

> [!question] Check yourself (answers below)
> 1. Explain in two sentences why the near-bed flow in a bend is directed *inward*.
> 2. A bend has $B=100$ m, $r=400$ m, $u=1.5$ m/s. What is the superelevation?
> 3. In a linear stability analysis, what do the real and imaginary parts of $\omega$ mean?
> 4. According to the paper, what happens to the planform as the phase shift angle decreases?
> *Answers.* (1) The surface tilt gives the same transverse pressure gradient at all depths, but the centrifugal force $\propto u^2$ is weaker near the bed where $u$ is small, so the pressure gradient wins and drives water inward near the bed. (2) $\Delta h=u^2B/gr=2.25\times100/(9.81\times400)=5.7$ cm. (3) $\operatorname{Re}\omega/k$ is the migration speed; $\operatorname{Im}\omega>0$ is growth (instability). (4) The channel goes from straight to meandering to braided, becoming more unstable.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Priority |
> |---|---|---|
> | abstract, introduction, model set-up, conclusions, phase-shift thresholds | [[Secondary_Current_and_Classification_of_River_Chan.pdf]] (read: abstract, §1, start of §2, conclusions; the middle sections with the equations were **not** read in detail) | d · paper |
> | stability picture, braiding regime diagram | [[river_braiding-1.pdf]] (AI notes) | a · AI notes |
> | superelevation formula and numbers, the pole interpretation, critical reading | my reasoning, `scripts/fr_numbers.py` | extra · beyond |
>
> **Flags.** (1) The numerical thresholds are read from garbled text (the symbol for the angle did not survive extraction): `[verify]`. (2) I did not follow the derivation of their Eqs. 3–37, so statements about the mathematics are qualitative. (3) The paper is in an applied-mathematics journal and is analytical; it contains no direct field validation in the sections read.
