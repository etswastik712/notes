---
title: Landscapes Past Papers 2022 (EC2223) - Solved
aliases: [landscapes past paper, EC2223 midsem 2022, landscapes quizzes 2022, landscape evolution previous year paper]
subject: landscapes
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/landscapes, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# Landscapes Past Papers 2022 (EC2223): Mid-sem and Quizzes, Solved

[[Landscapes and Geomorphology - Course Map|Course Map]] · practice: [[LS99 Landscapes Practice Problems]] · this year's exam-style question: [[LS23 Bedrock Channels and River Incision]] §11A

<span class="scope-taught">taught · past papers of this course</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> The course ran in 2022 as **EC2223 *Landscapes and Their Evolution*** (now EC2123, same coordinator, Argha Banerjee; this year's outline: [[c41EC2123.pdf]]). Two Google Docs shared on your Drive, found by a Drive search on 2026-11-21 and saved (PDF + text) to `earth-and-climate/landscapes-geomorphology/lecture-notes-slides/`:
> - [[EC2223_ Landscapes and Their Evolution (Midsem).pdf]] — 8 questions (figures; read from the page images) **with the instructor's handwritten "Rough Solutions"** (two low-resolution photos, pp. 5–6, partly legible);
> - [[EC2223_ Landscapes and Their Evolution- Quizzes.pdf]] — Quiz 1 (lectures 1–6, 13 marks) and Quiz 2 (lectures 11–15B, 10 marks), no solutions.
> Marks and wording below are the papers'. Numbers: `scripts/ls_pastpapers_2022_numbers.py`. Where the rough solutions were readable they are quoted as **[RS]**; everything else is mine. *This year's mid-sem was open-notes (Classroom, 17 Sep 2026); the final-exam format has not been announced.*

## Mid-semester exam (2022)

> [!question] Q1 · Joint distribution of elevation and slope (1.5 + 1.5 + 1)
> A 2-D histogram of slope angle (0–60°) against elevation (0–1650 m) for an unspecified region: a dense cluster at **low elevation (~100–200 m) and low slope (< 10°)**, a broad band of moderate-to-steep slopes (10–40°) from 200 to ~1200 m, and a second, weaker concentration of low slopes near **~800–1000 m**. (a) Draw the slope distribution. (b) Draw the hypsometry. (c) Comment on the landscape.

> [!example]- Solution ([[LS03 Digital Elevation Models and Terrain Analysis]])
> (a) Integrate over elevation: a distribution **peaked at small slopes** (a few degrees), falling steadily to a long tail at 30–40° and beyond (sketch: area/freq decreasing with slope; mode below 10°). (b) Integrate over slope: **bimodal** hypsometry — a tall peak near 100–200 m and a smaller one near ~900 m, with a low plateau of frequency in between. (c) A **two-level landscape**: a low, gently sloping plain and an elevated, gently sloping upland, joined by a belt of steep (~20°+) slopes — an **escarpment** such as the Western Ghats (Konkan coastal plain, Ghat scarp, Deccan plateau). **[RS]**: "a bi-planar topography (similar to Western Ghats escarpment?), with gently sloping/flat (< 10°) areas at ~100 m and ~900 m elevation and intervening steep (~20°) slopes"; his sketches show the decreasing slope histogram and the two-peaked hypsometry.

> [!question] Q2 · Faults of High Mountain Asia (4)
> A map of the major faults of High Mountain Asia (three types by symbol, not identified) with GPS convergence/deformation rates (arrows: ~21.5 ± 1.5 mm/yr across the Himalaya, 13 ± 7 and 10 ± 3 in the Tien Shan, 30 ± 20 on the ATF, 20 ± 20, 15 ± 5 and 21 ± 5 in Tibet and to its east). Explain the distribution of the fault types given the pattern of deformation.

> [!example]- Solution ([[LS09 Faults and Earthquakes]], [[LS10 Folds Flexure and Mountain Building]])
> India converges on Eurasia roughly N–S. (1) **Thrust (reverse) faults** strike perpendicular to the shortening: the Himalayan front (MFT, MBT, MCT/MHT along the Indo-Gangetic plain), and around the Tarim basin and Tien Shan, Qilian Shan — where crust is shortened and thickened. (2) **Strike-slip faults** (Altyn Tagh, Kunlun, Karakoram, Xianshuihe) let blocks of thickened Tibetan crust **escape eastward** away from the indenter; differences in escape rate between blocks are taken up on these block-bounding faults. (3) **Normal faults** strike roughly **N–S** in southern and central Tibet: the high, thick plateau spreads **E–W** under its own weight (gravitational collapse), extending perpendicular to the convergence. **[RS]**: "thrusting and convergence" at the margins; "N–S trending normal faulting due to extension along E–W"; "escaping blocks of Tibetan crust"; "differential escape rate causing transfer faults at the block borders". *(Fault names are general knowledge; the map labels only abbreviations such as ATF, KF, MBT.)*

> [!question] Q3 · Stress on a diagonal (4)
> A unit cube in equilibrium with normal stress $\sigma_1$ on the top and bottom faces and $\sigma_1+\Delta\sigma_1$ on the left and right faces. Compute the normal and shear stresses on the diagonal plane AC (balance the forces on triangle ABC).

> [!example]- Solution ([[LS08 Plate Tectonics Strain Stress and Convection]])
> The diagonal has length $\sqrt2$ (unit depth). Balance forces on ABC along $x$ and $y$: $\frac{\sqrt2\sigma}{\sqrt2}+\frac{\sqrt2\tau}{\sqrt2}=\sigma_1+\Delta\sigma_1$ and $\frac{\sqrt2\sigma}{\sqrt2}-\frac{\sqrt2\tau}{\sqrt2}=\sigma_1$, so
> $$\sigma=\sigma_1+\frac{\Delta\sigma_1}2,\qquad \tau=\frac{\Delta\sigma_1}2 .$$
> (Mohr's circle: centre $\sigma_1+\Delta\sigma_1/2$, radius $\Delta\sigma_1/2$; the 45° plane is at $2\theta=90°$, the maximum shear.) **[RS]** gives exactly these, and adds: "even if we applied shear on the cube surfaces, $\tau\ne0$ within it as long as $\sigma_{xx}\ne\sigma_{yy}$."

> [!question] Q4 · Uplift of the Himalaya (2.5 + 1.5)
> India moves toward Eurasia at ~3 cm/yr; the speed drops to zero across the ~200 km-wide Himalaya. (a) With a 35 km crust, estimate the mean uplift rate. (b) Limitations?

> [!example]- Solution ([[LS10 Folds Flexure and Mountain Building]], [[LS07 Isostasy]])
> (a) **Mass conservation** (incompressible crust): the crust entering per unit length of the range, $vH$, thickens a belt of width $W$: $\dfrac{dH}{dt}\approx\dfrac{vH}{W}=\dfrac{0.03\times35}{200}\ \text{m/yr}=\mathbf{0.5\ cm/yr}$. **[RS]**: "$\sim(0.03\ \text{m/yr})\times35\ \text{km}/200\ \text{km}\sim\tfrac12$ cm/yr".
> (b) **[RS]**: the equation assumes an **incompressible, homogeneous** crust; there may be additional **mantle flow**; there will be **isostatic adjustment**. Quantitatively: only about $1-\rho_c/\rho_m\approx0.18$ of the thickening appears as surface uplift (the root grows too): ~1 mm/yr of rock uplift by Airy isostasy; erosion removes material; not all convergence is absorbed in the Himalaya (some goes to Tibet and beyond, Q2); and the crust is not thickened uniformly across the 200 km.

> [!question] Q5 · Contour map of the Netrabati headwaters (1.5 + 2.5)
> A 40 m contour map (12.66–12.79 N, 75.55–75.69 E) with the Netrabati river. (a) Locate the highest peak (and elevation), the confluence of the Netrabati with a major tributary, and the steepest slope (location and value). (b) Sketch the hypsometry and the river's long profile.

> [!example]- Solution ([[LS03 Digital Elevation Models and Terrain Analysis]], [[LS20 GIS and TopoToolbox Practicals]], [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]])
> (a) **Highest peak**: the closed summit in the **south-east corner**, ≈ **12.665 N, 75.685 E**, inside the 1400 m contour (≈ 1400–1440 m). **[RS]**: "12.66, 75.67?" (with "apologies for the confusing contour markings"). **Confluence**: where the blue river from the north meets the branch from the north-east, ≈ **12.77 N, 75.67 E** (near 700 m) — read off the figure. **Steepest slope**: around the SE summit, where 40 m contours crowd: ~300 m in ~0.5 km, **slope ≈ 0.6 (≈ 30°)** — any tightly packed spot read honestly earns the mark.
> (b) **Hypsometry**: much of the area low (100–300 m, the western half), a broad middle (400–900 m, the dissected eastern hills), little above 1000 m (only the SE corner): a curve falling steeply from the minimum and with a long thin tail above 1000 m. **Long profile**: from ~700 m at the northern edge, a **steep upper reach** (≈ 500 m of drop in the first ~10 km, through the gorge between the 900 m ridges) then a **gentle lower reach** (≈ 100–200 m over the last ~12 km to the western edge): concave up, the Western Ghats escarpment profile ([[LS23 Bedrock Channels and River Incision]]).

> [!question] Q6 · Sea-level rise from land-ice loss (2 + 2)
> A world map of sea-level change from the loss of land ice over two decades (colour scale −5 to +5 mm/yr). (a) Two important features and why. (b) Greenland's ice sheet is ~2.5 km thick; long-term bedrock uplift if it all melts?

> [!example]- Solution ([[LS15 Glacial Deposits Rebound and Sea Level]], [[LS26 Sea Level and Ocean Waves]])
> (a) **[RS]**: (i) glacier loss raises mean sea level globally, by ~2 mm/yr on the map; (ii) local sea level is affected by **isostatic rebound** where ice is lost. Read off the map: the rise is **not uniform** — largest far from the melting ice (southern oceans, ~3–4 mm/yr) and **negative (falling) near Greenland and around Antarctica**, because (1) the shrinking ice sheet's **gravitational pull** on the ocean weakens, so water moves away from it, and (2) the unloaded crust **rebounds** (the self-attraction "fingerprint" is general knowledge, not in the rough solutions).
> (b) Airy isostasy, mass balance of the column: $\rho_m\,\delta r=\rho_i h$ ⇒ $\delta r=\frac{\rho_i}{\rho_m}h=\frac{917}{3300}\times2.5\ \text{km}=\mathbf{0.69\ km}$ (with $\rho_i\approx1000$: 0.76 km; **[RS]**: "$\sim0.8$ km").

> [!question] Q7 · The 2015 Gorkha earthquake (2.5 + 1.5)
> Slip of ~2 m over 100 km × 50 km at 8 km depth (slip map with aftershocks). (a) Energy released by frictional heating if the friction coefficient is 0.05 (seismic energy is likely a fraction of this). (b) Why are the aftershocks mostly south of the block that moved?

> [!example]- Solution ([[LS09 Faults and Earthquakes]])
> (a) Normal stress ≈ overburden $\sigma_n=\rho gh=2700\times9.8\times8000=2.1\times10^8$ Pa; area $A=10^5\times5\times10^4=5\times10^9$ m²; friction $F=\mu\sigma_nA=0.05\times2.1\times10^8\times5\times10^9=\mathbf{5.3\times10^{16}}$ **N**; heat $E=F\times\text{slip}=\mathbf{1.1\times10^{17}}$ **J**. For comparison the radiated energy of an $M_w$ 7.8 event, $\log E=1.5M+4.8$, is $3\times10^{16}$ J — about 30 % of the frictional heat, consistent with the question's remark.
> > [!warning] [!verify] The rough solution's area
> > **[RS]** writes $A$ as "500 × 10⁶" m² and gets $F\sim5\times10^{15}$ N, $E\sim10^{16}$ J. But 100 km × 50 km $=5\times10^9$ m², so those values are **10× too small**; the correct order is $10^{17}$ J.
> (b) The hanging wall (the Himalaya) slipped **south over India** on the shallow-dipping Main Himalayan Thrust; that slip **compressed and loaded** the locked shallower part of the fault and the crust ahead of (south of) the ruptured patch, raising the stress there, so aftershocks cluster to the south (and at the rupture's edges). **[RS]**: "compression due to the slip from the main earthquake".

> [!question] Q8 · Earth's temperature profile (2 + 2)
> A plot of temperature against depth through Earth. (a) Why is the gradient in the lithosphere an order of magnitude larger than in the mantle? (b) Lithostatic pressure at the core–mantle boundary?

> [!example]- Solution ([[LS08 Plate Tectonics Strain Stress and Convection]])
> (a) Heat crosses the lithosphere by **conduction**, which needs a steep gradient to carry the flux; the mantle **convects**, mixing heat efficiently, so its temperature follows a nearly adiabatic, shallow gradient. **[RS]**: "mantle convection transfers heat efficiently (better mixing) and lowers the gradient; in comparison, conductive transfer is less efficient."
> (b) $P\approx\bar\rho gh=5000\times9.8\times2.9\times10^6\approx\mathbf{1.4\times10^{11}}$ **Pa ≈ 140 GPa** (**[RS]**: "$\sim1.5\times10^{11}$ Pa, ~150 GPa (maybe a bit of overestimate)"; PREM gives 136 GPa).

## Quiz 1 (2022; lectures 1–6; 13 marks)
*Useful numbers given: $R\approx6400$ km, core radius ≈ 3000 km, mean density ≈ 5000 kg m⁻³, core density ≈ 10 000 kg m⁻³, $G=6.7\times10^{-11}$.* ([[LS01 Landscapes as Physical Systems]], [[LS05 Shape of Planets]], [[LS06 Maximum Topography]])

> [!example]- Solutions
> 1. (1) $\omega=2\pi/(\text{sidereal day }86\,164\ \text{s})=\mathbf{7.29\times10^{-5}}$ rad s⁻¹.
> 2. (2) Equator: $\omega^2R/g$. With the given numbers $g=\tfrac43\pi G\rho R=8.98$ m s⁻², ratio $=3.8\times10^{-3}$ (with $g=9.8$: $3.47\times10^{-3}\approx1/288$). **Pole: 0** (on the axis, no centrifugal acceleration).
> 3. (2) Flattening $\propto\omega^2$ (LS05 eq. 15, $\Delta R/R=\bar\rho\omega^2R/2g\rho_s$): $f_{\text{then}}=f_{\text{now}}(24/19)^2=0.00335\times1.596=\mathbf{0.0053}\approx1/187$.
> 4. (3) Inside a spherical shell the mantle exerts no net gravity, so at the core surface $g_c=\tfrac43\pi G\rho_cr_c=8.42$ m s⁻² and $q_c=\omega^2r_c/g_c=1.9\times10^{-3}$. With the slides' formula for a homogeneous core ($\bar\rho=\rho_s$): $f_c=q_c/2\approx\mathbf{1\times10^{-3}}$; the exact homogeneous-fluid (Maclaurin) value $\tfrac54q_c=2.4\times10^{-3}$ — so the core is *less* flattened than the Earth's surface in either model. *(Assumes the core co-rotates and is fluid; the overlying mantle's own bulge is ignored.)*
> 5. (3 + 2) (a) $P$ grows linearly with depth in each layer, slope $\rho_1g$ in the top layer and $\rho_2g$ below: a kinked straight line, steeper in the denser layer, for both orderings. (b) Both are equilibria, but **dense over light** is **unstable** (Rayleigh–Taylor: any perturbation lowers the potential energy by overturning), so it is not common in nature; stable stratification (light over dense) is the norm — the same reason the Earth is layered by density.

## Quiz 2 (2022; lectures 11–15B; 10 marks)

> [!example]- Solutions
> 1. (3) **Two crustal blocks** (crust 2.5, mantle 3.0 g/cc; freeboards $h$ and $h/2$). Freeboard is $1-\rho_c/\rho_m=\tfrac16$ of the thickness, so the blocks are $6h$ and $3h$ thick. Eroding $h/2$ from the top of the taller leaves $5.5h$, freeboard $0.917h$: it rebounds by $5/12$ of what was removed. **Final difference $=\tfrac{11h}{12}-\tfrac h2=\mathbf{5h/12}$** (from $h/2$). ([[LS07 Isostasy]])
> 2. (2) A 1 m³ cube has 6 m²; each cut plane adds 2 m². Six blocks from **five parallel cuts**: 16 m², **×2.67**; from one cut in one direction and two in another (2 × 3 blocks): 12 m², **×2**. The *positions* of the planes don't matter (each adds 2 m² wherever it is); their *arrangement* does. ([[LS11 Weathering and Regolith]])
> 3. (3) $N=N_0e^{-\lambda t}$, $\lambda=0.693/6930=10^{-4}$ yr⁻¹. Carbon from the ocean is already "old": it starts with $N_0e^{-\lambda\cdot1000}$, so the measured age is ≈ 5000 + 1000 = 6000 yr (a well-mixed-box treatment gives a 953-yr offset). The age is **off by a factor ≈ 1.2** — but **over**estimated, not under. [!verify] The question says "underestimated"; the reservoir effect makes marine radiocarbon ages too *old*, so either the wording is reversed or "factor" means that the true age is ≈ 0.83 of the apparent one. ([[LSX1 Clocks in Rocks]])
> 4. (2) Steady state $0=U+Dh''$, $h'(0)=0$, $h(L)=0$ ⇒ $h=\frac U{2D}(L^2-x^2)$: **relief $UL^2/2D=10^{-4}\times10^4/0.01=100$ m.** ([[LS12 Hillslope Transport and the Diffusion Equation]])

## Topic map
| question | topic | vault |
|---|---|---|
| MS Q1, Q5 | slope/elevation statistics, hypsometry, contour reading, long profiles | [[LS03 Digital Elevation Models and Terrain Analysis]], [[LS20 GIS and TopoToolbox Practicals]] |
| MS Q2, Q7; Q1-quiz | faults, earthquakes, plate collision | [[LS09 Faults and Earthquakes]], [[LS10 Folds Flexure and Mountain Building]] |
| MS Q3, Q8 | stress, Mohr circle; geotherm, convection | [[LS08 Plate Tectonics Strain Stress and Convection]] |
| MS Q4, Q6b; Quiz 2 Q1 | mass conservation, isostasy, rebound | [[LS07 Isostasy]], [[LS15 Glacial Deposits Rebound and Sea Level]] |
| MS Q6a | sea-level fingerprints | [[LS26 Sea Level and Ocean Waves]] |
| Quiz 1 | rotation, oblateness, hydrostatics | [[LS05 Shape of Planets]], [[LS06 Maximum Topography]] |
| Quiz 2 Q2–Q4 | weathering surface area, radiocarbon, hillslope diffusion | [[LS11 Weathering and Regolith]], [[LSX1 Clocks in Rocks]], [[LS12 Hillslope Transport and the Diffusion Equation]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | mid-sem questions and figures | [[EC2223_ Landscapes and Their Evolution (Midsem).pdf]] pp.1–4 (Google Doc on Drive, exported 2026-11-21; read as page images; map p.3 at 200 dpi) | taught (past paper) |
> | rough solutions [RS] | the same file pp.5–6 (photos, ~440×600 px, enlarged; Q1, Q3, Q4, Q6, Q7, Q8 and parts of Q2, Q5 legible) | taught (instructor) |
> | quiz questions | [[EC2223_ Landscapes and Their Evolution- Quizzes.pdf]] (text + figure page) | taught (past paper) |
> | course outline 2026 | [[c41EC2123.pdf]] | context |
> | all numbers; the Q7 area check; seismic-energy comparison | `scripts/ls_pastpapers_2022_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] (1) RS Q7 area 10× too small. (2) Quiz 2 Q3 says "underestimated"; the reservoir effect overestimates. (3) Q5's confluence and steepest-slope readings are approximate from a 40 m contour map. (4) Quiz 2 Q3's "equation 1" is not in the export; $N=N_0e^{-\lambda t}$ assumed.
