---
title: FR03 Flow at a River Bend with CCHE2D (Das and Biswal 2023)
aliases: [FR03, Das and Biswal 2023, CCHE2D, Gomati River, flow at a river bend, Manning roughness calibration]
subject: landscapes
type: chapter
part: Further Research
scope: [extra-book]
by: [papers]
status: draft
prereq: ["[[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]]", "[[LS16 Fluvial Landscapes]]"]
tags: [subject/landscapes, type/chapter, extra/book, src/papers, status/draft]
---
# FR03 · Flow at a River Bend with CCHE2D (Das and Biswal 2023)

◀ [[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]] · [[Further Research - Landscapes Papers]] · next: [[FR04 Building the Himalaya (Dal Zilio et al 2021)]]

<span class="scope-extra-book">extra · paper (not examinable, read for understanding)</span>

> [!summary] The paper in one paragraph
> A. Das and S. K. Biswal, **"Numerical Modeling of Flow Pattern at a Right-angled River Bend Using CCHE2D Model"**, *Scientific Research Communications* 3(1) (2023), doi 10.52460/src.2023.005 ([[SRC-3-1-5-Das.pdf]]), from NIT Agartala (Tripura, India). The authors simulate the flow in a $90^\circ$ bend of the **Gomati River** (Tripura) with the software **CCHE2D** (developed at the National Center for Computational Hydroscience and Engineering, University of Mississippi), a **depth-averaged 2D** finite-volume model with $k$–$\varepsilon$ turbulence. They **calibrate the bed roughness (Manning's $n$)** against field data for two discharges ($68$ and $102$ m³/s) and report the velocity, depth, Froude number and bed shear stress through the bend, finding that the **fastest water and the highest water surface move toward the outer bank**.

> [!key] After this chapter you can
> - explain what a *depth-averaged* flow model solves and what Manning's $n$ does in it,
> - describe the study site and the workflow (DEM $\to$ mesh $\to$ boundary conditions $\to$ calibration),
> - state the reported results and check them against simple hand estimates, and
> - read the paper critically (where the numbers are hard to reconcile and why that is a useful exercise).

> [!intuition] Where this sits relative to [[FR01 Braided Rivers in 3D (Olsen 2021)]]
> FR01 is a *research* 3D model run for days on an ordinary PC to study how braids form. FR03 is a *practical engineering* study: a 2D, ready-made package applied to **one bend of a real river** to predict where the flow is fastest and the bed is stressed, so that bank erosion and sedimentation can be anticipated. It is the same physics (secondary currents in a bend, [[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]]) at a much lower computational cost, with the secondary current represented by empirical closure instead of being computed.

## 1. The study site and the workflow
> [!example] The Gomati River bend (paper §2.1, Table 1)
> The Gomati is the largest river of Tripura, $167.4$ km long, elevations $18.3$–$112.2$ m above sea level, with a catchment of $2492$ km² ($1921$ km² hilly, $571$ km² or $23\,\%$ plain), about $56$ km south-west of Agartala. The simulated reach:
> | stream length | valley length | width $B$ | bed slope $S$ | bend angle | radius of curvature | sinuosity |
> |---|---|---|---|---|---|---|
> | 94.62 m | 53.16 m | 42.7 m | 0.0006 | $90^\circ$ | 60.22 m | 1.78 |
> *Check:* sinuosity $=94.62/53.16=1.78$ ✓ (stream length over valley length, the definition used in [[LS03 Digital Elevation Models and Terrain Analysis]] for planform measures); radius over width $=1.41$, a **tight** bend (natural meanders typically have $r/B\approx2$–$3$, recalled). Discharges were obtained from upstream stage recorders via a **stage–discharge rating curve** (water level $\to$ flow), a field-data step the paper notes is needed because discharge is not a unique function of stage when slope and unsteadiness vary.
> **Workflow (paper Fig. 2):** survey the bathymetry $\to$ clip the DEM in ArcGIS and export as ASCII ($\to$ [[LS20 GIS and TopoToolbox Practicals]] for the GIS side) $\to$ build a structured mesh with the CCHE2D mesh generator $\to$ set the inflow/outflow boundary conditions (water-surface level and discharge) and roughness $\to$ run with a $10$ s time step for a day $\to$ compare to field data and adjust $n$.

## 2. What a depth-averaged model solves
> [!derivation] The 2D shallow-water equations in one paragraph (standard; the paper states "depth-averaged two-dimensional conservation equations")
> Average the 3D equations over the depth $h$ (valid when $h\ll$ the horizontal scales). With depth-averaged velocity $\mathbf U=(U,V)$:
> $$\partial_th+\nabla\!\cdot(h\mathbf U)=0,\qquad\partial_t\mathbf U+(\mathbf U\!\cdot\nabla)\mathbf U=-g\nabla\eta-\frac{\boldsymbol\tau_b}{\rho h}+\nabla\!\cdot(\nu_T\nabla\mathbf U)\ \ (+\text{Coriolis}),$$
> where $\eta$ is the water-surface elevation, $\nu_T$ the turbulent eddy viscosity (from the $k$–$\varepsilon$ closure) and $\boldsymbol\tau_b$ the **bed friction**, written with **Manning's coefficient** as $\boldsymbol\tau_b=\rho gn^2\lvert\mathbf U\rvert\mathbf U/h^{1/3}$. *Meaning of $n$:* a single number lumping the grain roughness, bedforms and vegetation of the channel. $n=0.015$ is a smooth channel, $0.03$ a clean natural channel, $0.04$ a weedy or cobbly one; the shear stress it produces for $n=0.03$, $U=1$ m/s, $h=2$ m is $\tau_b=1000\times9.81\times9\times10^{-4}\times1/1.26=7.0$ Pa. The **centrifugal term** $(\mathbf U\cdot\nabla)\mathbf U$ is what tilts the water surface toward the outer bank ([[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]] §1, $\Delta h=u^2B/gr$). The solution method is the **finite-volume** method with a **second-order upwind** scheme.

## 3. What was found
> [!example] Results reported (abstract and conclusions)
> - **Roughness calibration.** The abstract and the conclusions word this slightly differently: the best roughness factors are $n=0.030$–$0.040$ for one range of discharges and $n=0.015$–$0.025$ for the medium and high discharges (the printed abstract has the inequality signs reversed and is ambiguous: `[verify]`).
> - **Velocity and stress.** The mean velocities for the two discharges $68$ and $102$ m³/s are **$0.56$ and $0.77$ m/s** and the mean bed shear stresses **$27.99$ and $35.62$ N/m²**; the **water surface and the highest velocities shift toward the outer bank** through the bend, with changes in shear stress, velocity, depth and Froude number controlled by **centrifugal force and helical cells**; velocity and shear stress are **linearly related** over the reach (reported with $R^2$ and $r$).
> - **Conclusion of the authors.** The model "is efficient to simulate a wide range of flow parameters in riverine systems and can better predict sedimentation and erosion".

## 4. A sanity check you can do on a napkin
> [!derivation] 🔵 Extra (my computation, `scripts/fr_numbers.py`): can the reported averages be reconciled with simple uniform-flow estimates?
> Use only numbers printed in the paper: $B=42.7$ m, $S=0.0006$, $Q=68$ and $102$ m³/s, $U=0.56$ and $0.77$ m/s.
> - **Depth from continuity,** $h=Q/(UB)$: $2.84$ m and $3.10$ m. The Froude numbers are tiny ($0.11$, $0.14$): very **deep and slow, subcritical** flow.
> - **Uniform-flow shear stress** $\tau=\rho ghS$: $16.7$ Pa and $18.3$ Pa, against the reported $28.0$ and $35.6$ Pa: the reported values are $\approx1.7\times$ and $1.9\times$ larger.
> - **Manning's $n$ implied by the reported velocity:** $n=h^{2/3}S^{1/2}/U=0.088$ and $0.068$, much larger than the calibrated $0.015$–$0.040$. Conversely, with $n=0.03$ and the bed slope a *uniform* flow of $68$ m³/s would have depth $1.5$ m and speed $1.07$ m/s, about twice the reported mean speed.
> **How to read this.** The mismatch is not necessarily an error: in a tight bend with backwater from downstream the flow is *non-uniform*, the water-surface slope can differ from the bed slope $0.0006$, and a mean over the model reach is not a mean over a uniform channel; also a 2D model's reported "mean" depends on how the mean is taken. But the paper (in the parts I read) does not discuss this gap, and a student reading a result should always ask whether **simple physics reproduces the order of magnitude**. Here it reproduces the *trend* (higher discharge $\to$ higher velocity and stress) but not the *magnitudes* to better than a factor of about 2.

## 5. Reading the paper critically
> [!pitfall] Things to notice (and to check in a real project)
> 1. **Calibration vs validation:** the same field data are used to calibrate $n$ and then to claim the model is accurate; an independent data set (another flood) would validate it.
> 2. **No explicit secondary currents:** a depth-averaged model captures the *centrifugal* surface tilt and uses closures for the helical flow; the paper attributes effects to "helical cells" that this model does not directly resolve ([[FR01 Braided Rivers in 3D (Olsen 2021)]] §3 explains why).
> 3. **Hydraulics only:** the sediment module of CCHE2D was *not* used ("This study only utilise the hydraulics capability of CCHE2D"), so claims about *sedimentation and erosion* are inferences from shear stress, not model results.
> 4. **Scale:** a $95$ m stream length is a *very short* reach for an inflow–outflow boundary-driven model; boundary effects can dominate.
> 5. **Editorial glitches** (reversed inequality in the abstract, both latitudes given as $23^\circ47'$ N, different wording of the calibration result in abstract and conclusions) are signs to double-check any quoted numbers against the original data.

## 6. Connections
> [!connection] Where this fits in the vault
> - **Open-channel flow, Manning, shear stress, Shields:** [[LS16 Fluvial Landscapes]]; Reynolds number and turbulence: [[LS02 Mechanics and Mathematics Toolkit]].
> - **Bend flow and secondary currents:** [[FR02 Secondary Currents and River Channel Patterns (Njenga 2013)]]; **meandering as an instability:** the AI notes `river_braiding`.
> - **Terrain data to model:** DEM, projections and GIS: [[LS03 Digital Elevation Models and Terrain Analysis]], [[LS04 Map Projections and Reference Surfaces]], [[LS20 GIS and TopoToolbox Practicals]] (the same DEM $\to$ ASCII workflow, in India).
> - **Model testing:** calibration versus validation is an inference problem: [[Probability - Course Map]].
> - **Indian context:** the Gomati drains the hills and plains of Tripura; for Himalayan and Deccan rivers see [[FR04 Building the Himalaya (Dal Zilio et al 2021)]] and [[LS18 Deccan Traps Terrain]].

> [!question] Check yourself (answers below)
> 1. What does Manning's $n$ represent, and what happens to the computed velocity if $n$ is increased?
> 2. Why does the highest velocity move toward the outer bank in a bend?
> 3. From $Q=68$ m³/s, $B=42.7$ m and $U=0.56$ m/s find the mean depth.
> 4. Name two reasons a calibrated 2D model may not reproduce the stress of a uniform-flow estimate.
> *Answers.* (1) A lumped bed-roughness coefficient in the friction law $\tau_b=\rho gn^2U^2/h^{1/3}$; larger $n$ means more friction and, for the same discharge, a lower velocity and a greater depth. (2) The centrifugal force pushes the fast core outward and the water surface tilts up toward the outer bank, with the thalweg shifting toward it. (3) $h=68/(0.56\times42.7)=2.84$ m. (4) Non-uniform flow (backwater, a surface slope different from the bed slope) and the way "mean" values are defined; also calibration compensating other errors.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Priority |
> |---|---|---|
> | abstract, introduction, study area and Table 1, model description, conclusions | [[SRC-3-1-5-Das.pdf]] (read: abstract, introduction, §2.1–2.3, conclusions; **§3 results with the figures were not read in detail**) | d · paper |
> | shallow-water equations and Manning friction | standard (my statement) | extra · beyond |
> | continuity depths, uniform-flow stress, implied $n$ | my computation (`scripts/fr_numbers.py`) from the paper's printed values | extra · beyond |
>
> **Flags.** (1) The reported $\tau$ and $U$ values were taken from the conclusions; their definition (reach average? cross-section average?) was not checked. (2) The "typical $r/B\approx2$–$3$" is recalled general knowledge. (3) The comparison with uniform flow is a plausibility check, not a claim that the paper is wrong.
