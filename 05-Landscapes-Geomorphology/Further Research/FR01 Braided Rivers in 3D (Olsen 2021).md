---
title: FR01 Braided Rivers in 3D (Olsen 2021)
aliases: [FR01, Olsen 2021, braided river modelling, SSIIM braiding, 3D numerical modelling of braided channel formation]
subject: landscapes
type: chapter
part: Further Research
scope: [extra-book]
by: [papers, ai-notes]
status: draft
prereq: ["[[LS16 Fluvial Landscapes]]", "[[LS02 Mechanics and Mathematics Toolkit]]"]
tags: [subject/landscapes, type/chapter, extra/book, src/papers, src/ai-notes, status/draft]
---
# FR01 · Braided Rivers in 3D (Olsen 2021)

◀ [[Further Research - Landscapes Papers]] · [[Landscapes and Geomorphology - Course Map|Course Map]] · next: [[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]]

<span class="scope-extra-book">extra · paper (not examinable, read for understanding)</span>

> [!summary] The paper in one paragraph
> N. R. B. Olsen, **"3D numerical modelling of braided channel formation"**, *Geomorphology* 375 (2021) 107528 ([[1-s2.0-S0169555X20305018-main.pdf]]). The author takes a **laboratory flume experiment** (Egozi and Ashmore 2009) in which a single straight sand channel *spontaneously breaks up into a braided network*, and reproduces it on a computer with a **fully three-dimensional** solution of the Navier–Stokes equations coupled to a sediment-transport formula, using the author's own code **SSIIM**. The model reproduces the growth of the *braiding intensity*, and the numerical experiments show two things: the braiding depends strongly on **which sediment-transport formula** is used, and on the **strength of the secondary (spiral) currents**, a 3D effect that depth-averaged (2D) models must approximate.

> [!key] After this chapter you can
> - say what a braided river is and why it is a good *test* for a numerical model,
> - read the paper's governing ingredients (Navier–Stokes, $k$-$\varepsilon$ turbulence, free surface, Engelund–Hansen transport, Exner continuity, wetting and drying) and relate each to a chapter of this vault,
> - compute the key dimensionless numbers of the experiment (Froude, Shields, aspect ratio) and say why the bed is highly mobile,
> - explain what a *braiding index* is and what the numerical experiments (sediment formula, secondary currents, grid, wet/dry threshold) showed,
> - say where the paper's model sits relative to the vault's other river material (stream power, LS16; the SSIIM-Landlab vault).

> [!intuition] Why braiding is the hard case
> A meandering river is one channel that slowly migrates. A **braided river** is a network of many channels, separated by bars, that split and rejoin and *change every flood*: channels abandon, new ones cut across (an **avulsion**), banks collapse. Because the pattern is complex, rough and changes in time, any numerical model that can reproduce it has passed a hard test ("it is therefore well suited for testing new algorithms for modelling sediment transport", the paper says). Beyond curiosity: braiding appears when **reservoirs are flushed or dams removed**, when the water level falls and sediment is released through a wide braided channel instead of one deep channel, so the erodible volume depends on the braiding.

## 1. Background you already have
> [!connection] What this paper uses from the vault
> | Ingredient in the paper | Where it is developed here |
> |---|---|
> | open-channel flow, bed shear stress $\tau=\rho ghS$ | [[LS16 Fluvial Landscapes]], [[LS02 Mechanics and Mathematics Toolkit]] |
> | Shields threshold, transport $\propto$ (stress)$^{3/2}$ | [[LS16 Fluvial Landscapes]] (Shields), [[LS19 Glacial and Aeolian Landforms]] (analogous wind threshold) |
> | Navier–Stokes, Reynolds numbers, turbulence | [[LS02 Mechanics and Mathematics Toolkit]] (Reynolds number $\sim10^6$ for rivers) |
> | conservation of bed sediment (Exner) | the master equation $\partial_tc=-\nabla\!\cdot\mathbf q+P$ of [[LS01 Landscapes as Physical Systems]] with $c=$ bed elevation |
> | instability of a flat bed $\to$ bars $\to$ braids | the AI-written notes [[river_braiding-1.pdf]] (`river_braiding.tex`), Ch. 4–5: linear stability and the aspect ratio $\beta=B/2D$; a flat bed with $\beta$ above a critical value $\beta_c(m)\approx m\beta_c(1)$ develops $m$ rows of bars; **$m=1$ alternate bars are the precursor of meanders, several simultaneous rows give braiding** |
> | modelling a river with a code you can run | the SSIIM–Landlab vault (`~/Documents/Landlab-SSIIM-Vault`): SSIIM is the model of this paper |

## 2. The experiment being reproduced
The physical model (Egozi and Ashmore 2009) is a sand-filled flume 18 m long and 3 m wide, slope $1.5\,\%$, with a $0.5$ m wide, $1.5$ cm deep channel dug along the middle. The sand has mean diameter $d_{50}=1.2$ mm ($d_{90}=3.6$ mm) and is recirculated. The water discharge is raised in three stages: $1.4$ L/s for the first $70$ h, $2.1$ L/s up to $140$ h, then $2.8$ L/s to $210$ h. The pattern is measured every hour through two braiding indices:
- **BIT, the total braiding intensity**: the average number of channels with a finite water depth per cross section (13 cross sections); it rose from 1 to about 4.
- **BIA, the active braiding intensity**: the average number of channels *with visible sediment transport*; it rose from 1 to about 1.84 in the third stage.
> [!intuition] Why two indices?
> A water-filled channel that carries no sediment is not shaping the bed. BIT counts every wet channel, BIA only the active ones, so BIA $\le$ BIT; the gap between them is the "dormant" part of the braid plain.

> [!derivation] 🔵 Extra (computed, `scripts/fr_numbers.py`): the dimensionless numbers of the flume
> With the initial channel ($W=0.5$ m, $h=1.5$ cm, $S=0.015$, $Q=1.4$ L/s):
> | Quantity | Formula | Value | Meaning |
> |---|---|---|---|
> | mean velocity | $U=Q/Wh$ | 0.187 m/s | slow, shallow flow |
> | Froude number | $U/\sqrt{gh}$ | **0.49** | subcritical |
> | bed shear stress | $\tau=\rho ghS$ | 2.2 Pa | |
> | Shields number | $\tau/[(\rho_s-\rho)gd_{50}]$ | **0.114** | $2.5\times$ the critical value (0.045): the bed is strongly mobile |
> | shear velocity | $u_*=\sqrt{\tau/\rho}$ | 0.047 m/s | $\ll$ settling speed of the 1.2 mm sand ($\sim0.15$ m/s, recalled): **bedload-dominated** |
> | aspect ratio | $\beta=W/2h$ | 16.7 | wide and shallow |
> *Reading:* a wide, shallow, supercritically-mobile bed is exactly the regime in which the linear-stability analysis of the AI notes predicts several simultaneous unstable modes, i.e. braiding.

## 3. The model: what was solved
> [!key] The ingredients, in the order of the paper (§3)
> 1. **Flow:** the full 3D Navier–Stokes equations with a **non-hydrostatic pressure** (the SIMPLE algorithm), on an unstructured, *adaptive* grid that follows the free surface and has 0–9 cells over the depth depending on the water depth (Eq. 4: $n=0$ if $d<d_{c1}$, $n=2$ between $d_{c1}$ and $d_{c2}$, else $n_{max}(d/d_{max})^{0.7}$, with $n_{max}=9$, $d_{max}=2$ cm, $d_{c1}=d_{c2}=3$ mm).
> 2. **Turbulence:** the $k$–$\varepsilon$ model (two transport equations for turbulent kinetic energy and its dissipation), so turbulence made upstream can be *carried* downstream. The paper contrasts this with the zero-equation closure of 2D codes, $\nu_T=K_2hu_*$, which assumes local equilibrium in each cell.
> 3. **Free surface:** the IPDA method (an implicit pressure-gradient algorithm; Olsen 2015); the downstream water level is fixed.
> 4. **Sediment:** convection–diffusion for suspended load plus bedload, **ten grain-size fractions** (0.2–4 mm, 10 % each initially), the bed elevation updated from the sediment continuity (Exner) equation separately for each fraction so the **grain-size distribution of the bed evolves** (coarser grains remain, finer are carried). The roughness is $k_s=3d_{90}$ (van Rijn 1982).
> 5. **Transport formula (Engelund and Hansen 1967), the paper's Eq. 3:**
> $$q_s=0.05\,\rho_sU^2\sqrt{\frac{d_{50}}{g(\rho_s/\rho-1)}}\ \Big[\frac{\tau}{g(\rho_s-\rho)d_{50}}\Big]^{3/2}.$$
> *Dimensional check:* $\rho_sU^2$ is kg m⁻¹s⁻², the square root is a time (s), so $q_s$ is kg m⁻¹s⁻¹, a **mass flux per unit width**. The factor in brackets is the **Shields number**; transport therefore grows as $U^2\theta^{3/2}$. For the flume numbers above this gives $q_s=1.5\times10^{-3}$ kg m⁻¹s⁻¹ ($5.5$ kg per metre per hour; $\approx2.7$ kg/h of sand through the $0.5$ m channel, $\approx1$ L/h); doubling the Shields number would multiply transport by $2^{3/2}=2.8$.
> 6. **Banks and lateral migration:** *no explicit bank-erosion formula*; channels move laterally only through the **wetting and drying** algorithm (a cell with depth below $d_{c1}$ dries) and the 3D secondary currents.
> **Cost:** $4$ s time step, $210$ h $\Rightarrow189\,000$ steps; five days on a 3.6 GHz PC (coarse grid, $380\times100$ cells) or eight days (fine grid, $450\times120$ cells of $4\times2.5$ cm). *(Checked: $18\ \mathrm m/4\ \mathrm{cm}=450$, $3\ \mathrm m/2.5\ \mathrm{cm}=120$, $210\times3600/4=189\,000$.)*

> [!intuition] Secondary currents: why 3D matters
> In a bend the water on the surface is pushed outward by centrifugal force and the water near the bed spirals inward: a **helical (secondary) flow** that carries sediment toward the inner bank and builds bars. A depth-averaged 2D model cannot compute it and must use a closure such as $\tan\delta=-K_1h/R$ (Eq. 1: the angle between bed-load and depth-averaged flow, $h$ = depth, $R$ = streamline radius of curvature, $K_1\approx7$ in many studies). That closure gives the secondary flow only from the *local* curvature, but a spiral born in one bend persists downstream; the 3D model carries it automatically. *Worked example (mine):* with the Gomati bend of [[FR03 Flow at a River Bend with CCHE2D (Das and Biswal 2023)]] ($h=2.8$ m, $R=60$ m) $K_1h/R=0.33$, i.e. a deflection of about $18^\circ$.

## 4. What the experiments showed
> [!example] Results of Olsen's runs (paper §§4–7)
> - **Braiding develops from a perturbation.** After about 18 h a *wavy depth pattern* forms over the whole flume (as in Einstein and Shen 1964), the 50 cm channel splits into several channels, some become asymmetric (31 h), side channels grow, the pattern becomes a typical braided plain with one main and several smaller channels. The computed time series of **BIA compares reasonably** with the measured one ($\sim1\to1.84$).
> - **Secondary currents are important.** Multiplying the vertical diffusion coefficient by 5 couples bed and surface velocities more strongly and **weakens the spiral flow**; the result is **less braiding** (fewer channels).
> - **The transport formula matters most.** The **Engelund–Hansen** formula (a total-load formula with *no explicit threshold*) gives a *higher* braiding intensity than **van Rijn** or **Meyer-Peter and Müller**, which give a planform *more like a meandering river*. *Interpretation (mine):* Meyer-Peter–Müller has a critical Shields stress below which nothing moves, so shallow flow on bar tops is shut off; Engelund–Hansen lets sediment move at any stress, so bars are reworked and channels re-route easily.
> - **Numerics do not change the story.** The grid size and the critical depth for wetting/drying changed details (random in detail, since a braided pattern is sensitive to small differences) but not the main features.
> - **An avulsion in detail.** The figures show how a **chute** forms across a bar: the water level at the *outside* of a bend rises because of the centrifugal force at the entrance of the chute, the new channel steals flow, an old bend dries (by $175$ h) and may become wet again ($210$ h).

## 5. Reading the paper critically
> [!pitfall] What the paper does *not* claim
> 1. It does **not** predict a *particular* braided pattern: "the braiding process will have a random feature", two runs with tiny differences give different patterns. What is compared are **statistics** (BI), not channel positions.
> 2. Only **one laboratory case** is reproduced; the agreement of BIA is called "reasonable", not exact. Whether the model works in a field river (the Tana River in Norway and a New Zealand river, both listed in the introduction) is a different question (the introduction lists 2D studies that start from a natural geometry).
> 3. The sediment-transport formula is the dominant uncertainty; the author notes that *improved formulas are a topic for future research*.
> 4. Cohesion and **vegetation** are absent (the lab sand has none); in the AI notes' framework these raise the effective critical Shields stress and promote fewer, more stable channels.

## 6. Connections and what to do next
> [!connection] Where this fits
> - **Stream power and bedrock incision** ([[LS16 Fluvial Landscapes]]) describe the *long-term* lowering of a channel; this paper describes the *short-term, alluvial* morphodynamics ($10^2$ h of experiment $\leftrightarrow$ decades in a river). The two meet in the response-time discussion: alluvial rivers adjust in $10^2$–$10^3$ yr ([[LS01 Landscapes as Physical Systems]]).
> - **Instability and pattern formation:** a straight channel becomes unstable and breaks into bars and braids through a mode growing as $e^{\sigma t}e^{ikx}$: the same Fourier-mode analysis as the Rayleigh–Bénard convection of [[LS08 Plate Tectonics Strain Stress and Convection]] and [[Fourier and Laplace Transforms]] (§6 dispersion relations; §7.6 growth rate = pole crossing the imaginary axis).
> - **Threshold-and-power-law transport:** $q_s\propto\theta^{3/2}$ is the fluvial cousin of the aeolian $q\propto u_*^3$ of [[LS19 Glacial and Aeolian Landforms]]; both illustrate the "steeper transport law $\Rightarrow$ rarer formative event" argument of [[LS01 Landscapes as Physical Systems]].
> - **Probability:** the randomness of the pattern (small perturbations, different outcome) calls for statistics such as BI, not trajectories: [[Probability - Course Map]].
> - **Related papers:** [[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]] (an analytic stability theory in which a *phase shift of the secondary current* separates straight, meandering and braided) and [[FR03 Flow at a River Bend with CCHE2D (Das and Biswal 2023)]] (a 2D simulation of one bend in an Indian river).

> [!question] Check yourself (answers below)
> 1. What does BIA count that BIT does not, and why is BIA $\le$ BIT?
> 2. Why can a 2D depth-averaged model not compute the spiral flow in a bend directly, and what does it use instead?
> 3. From Eq. 3, how does $q_s$ change if the depth-averaged velocity doubles at the same Shields number?
> 4. Why does a formula with a critical Shields stress produce a more meander-like pattern than one without?
> 5. The Shields number of the flume channel is 0.114 and the critical value is 0.045. What does the ratio say about the bed?
> *Answers.* (1) BIA counts channels with visible sediment transport; every active channel is wet, so BIA $\le$ BIT. (2) The spiral is a motion in the cross-section plane (vertical structure), which a depth average removes; 2D codes use $\tan\delta=-K_1h/R$ with a calibrated $K_1$ ($\approx7$). (3) $q_s\propto U^2$: four times. (4) A threshold shuts off transport on shallow, low-stress bar tops, so flow concentrates in one dominant channel. (5) $\theta/\theta_c\approx2.5$: the bed is far above the threshold, easily mobilised: the condition for braiding.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Priority |
> |---|---|---|
> | all statements about the paper (flume, model, equations 1–5, results, conclusions) | [[1-s2.0-S0169555X20305018-main.pdf]] (read: abstract, introduction, §2 physical model, §3 model, §4 results start, conclusions) | d · paper |
> | stability picture ($\beta_c(m)$, alternate bars vs braiding), BI definitions | [[river_braiding-1.pdf]] (`river_braiding.tex`, AI-written; chapters 4–5 skimmed) | a · AI notes |
> | dimensionless numbers, Engelund–Hansen evaluation, 18° example, interpretations marked "mine" | `scripts/fr_numbers.py` and my reasoning | extra · beyond |
>
> **Flags.** (1) I did not read the paper's later results sections (figures 5–9, the numerical BI curves) in detail; the BIA comparison is quoted from the abstract and conclusions. (2) The settling velocity of 1.2 mm sand ($0.15$ m/s) is recalled. (3) The explanation of why Meyer-Peter–Müller gives meander-like patterns is my interpretation, not the author's.
