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
# Landscapes Past Papers 2022 (EC2223 and EC2123): Mid-sems, End-sem and Quizzes, Solved

[[Landscapes and Geomorphology - Course Map|Course Map]] · practice: [[LS99 Landscapes Practice Problems]] · this year's exam-style question: [[LS23 Bedrock Channels and River Incision]] §11A

<span class="scope-taught">taught · past papers of this course</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The papers
> The course ran in 2022 as **EC2223 *Landscapes and Their Evolution*** (now EC2123, same coordinator, Argha Banerjee; this year's outline: [[c41EC2123.pdf]]). Two Google Docs shared on your Drive, found by a Drive search on 2026-11-21 and saved (PDF + text) to `earth-and-climate/landscapes-geomorphology/lecture-notes-slides/`:
> - [[EC2223_ Landscapes and Their Evolution (Midsem).pdf]] — 8 questions (figures; read from the page images) **with the instructor's handwritten "Rough Solutions"** (two low-resolution photos, pp. 5–6, partly legible);
> - [[EC2223_ Landscapes and Their Evolution- Quizzes.pdf]] — Quiz 1 (lectures 1–6, 13 marks) and Quiz 2 (lectures 11–15B, 10 marks), no solutions.
> - **Added 2026-11-22** from the Drive Question Paper Archive (Sem-3 → EC2123): the **EC2123 mid-sem (26 Sep 2022)** and **end-sem (30 Nov 2022)**, [[EC2123_midsem_22.pdf]] and [[EC2123_endsem_22.pdf]] (scans, saved to `…/past-papers/qp-archive/EC2123/`), solved in the last two sections. Other years: [[Landscapes Past Papers 2021 - Solved|2021]] · [[Landscapes Past Papers 2024 - Solved|2024]].
>
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

## EC2123 Mid-semester (26 Sep 2022, 28 marks)
*Added 2026-11-22 from the Drive **Question Paper Archive → Sem-3 → EC2123**: [[EC2123_midsem_22.pdf]] (2 pp., scanned; header "End-Semester … 2022 January Semester" with "mid" written in by hand). The same instructor, and a different paper from the EC2223 mid-sem above. Open notes; "approximate numerical answers with the right order of magnitude … are sufficient". Numbers: `scripts/ls_qp_archive_numbers.py`.*

> [!question] Q1 (1 + 1 + 2 + 2) · Himalayan sediment budget
> A satellite image of the Himalaya and the Indo-Gangetic plains (67.5–97.5°E, 22.5–37.5°N). (a) Estimate the sediment volume stored in the Indo-Gangetic plains. (b) Estimate the volume of rock removed by denudation of the Himalaya. (c) Do they match, or is something missing? (d) Is the present sediment load of the Ganga–Brahmaputra and Indus comparable to the long-term value?

> [!example]- Solution ([[LS10 Folds Flexure and Mountain Building]], [[LS16 Fluvial Landscapes]], [[LS27 Coasts Beaches Deltas and Rocky Shores]])
> (a) The plains run ~2500 km along the mountains (Indus to Brahmaputra) and are ~250–400 km wide. As a flexural foreland basin, the fill is a **wedge** up to ~5–6 km deep at the mountain front, thinning to zero at the southern edge: mean thickness ~2.5 km. $V\approx2500\times300\times2.5\approx\mathbf{2\times10^6}$ **km³**.
> (b) The belt is ~2500 km × ~250 km. The rocks at the surface (Higher Himalayan gneisses, metamorphosed at 20–30 km depth) show **~10–20 km of exhumation**. $V\approx2500\times250\times15\approx\mathbf{10^7}$ **km³** (more if Tibet's southern rim is counted).
> (c) **No: the plains hold only ~20 % of it.** The rest went past the plains to the **Bengal Fan** (the world's largest submarine fan, of order 10⁷ km³) and the **Indus Fan**, the deltas and the shelves, with some dissolved (chemical denudation, ~10–20 %). The basin is a transfer zone, not the final store. Also, some foreland fill has itself been thrust up and recycled (the Siwaliks).
> (d) The long-term average is ~10⁷ km³ × 2.7 t/m³ over ~50 Myr ≈ **0.5 Gt/yr**. Measured modern loads are ~1 Gt/yr for the Ganga–Brahmaputra plus ~0.25 Gt/yr for the pre-dam Indus: **~2× the long-term mean**, the same order. Plausible reasons for the excess: Quaternary glaciation and monsoon intensification, land-use change, and a few large floods and landslides dominating short records. Dams now trap much of the Indus load, so the present-day value is lower. [!verify] The fan volumes and modern loads are general knowledge (not from the course).

> [!question] Q2 (1 + 2 + 2 + 1) · An idealised weathering profile near Pune
> A 1 m regolith. At its base bedrock fractures into ~1 m cubes; each cube splits into 8 equal cubes every 10 cm of exhumation towards the surface. (a) Particle size at the top? (b) Plot free surface area per unit volume against depth. (c) Plot chemical weathering rate per unit volume against depth; assumptions and departures? (d) Expected deviations in real profiles around campus?

> [!example]- Solution ([[LS11 Weathering and Regolith]], [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]], [[laterite-cappings]])
> (a) Ten halvings of the side: $1\ \text{m}/2^{10}\approx\mathbf{1\ mm}$ (coarse sand).
> (b) A cube of side $a$ has $S/V=6/a$. At depth $z$ (m, from the top) the side is $2^{-(10-\lfloor10(1-z)\rfloor)}$ m, so $S/V=6\times2^{\,n}$ with $n$ the number of halvings: a **staircase**, **doubling every 10 cm upward**, from **6 m⁻¹ at the base to 6144 m⁻¹ at the top**. On a log axis it is a straight (stepped) line, i.e. $S/V\approx6\times2^{10(1-z)}$: exponential in height.
> (c) If the dissolution rate per unit mineral area is constant (water everywhere far from saturation, same mineralogy), the rate per volume ∝ $S/V$: the **same exponential staircase**, ~10³× faster at the top. Assumptions that fail:
> - Water reaching depth is already near **saturation**, so the deep rate is lower still.
> - Near the top, the **reactive minerals are used up** (the residue is clay or laterite), so the rate there falls. The real profile peaks at a **weathering front** at depth and declines upward.
> - Coatings and cementation hide fresh surface.
> - Temperature, CO₂ and organic acids vary with depth.
>
> (d) Around campus (basalt):
> - Fractures follow **cooling joints** (columns, sheets), not ideal cubes.
> - **Spheroidal weathering** leaves **corestones** with onion-skin shells (rounded boulders in saprolite), not uniform cubes.
> - The front is **sharp**: saprolite over fresh rock within decimetres.
> - Vesicular flow tops and red boles weather faster than massive interiors, so profiles follow flow units.
> - **Laterite** caps the plateau tops, and transported colluvium covers the slopes.
> - Thickness varies a lot with topography.

> [!question] Q3 (2 + 2 + 1) · Isostasy and sediment accommodation
> Block A: continental crust 35 km thick, 2700 kg m⁻³, floating on mantle of 3300 kg m⁻³. (a) Ignoring the loads of the ocean water (~4 km) and of basaltic oceanic crust, compute A's elevation above mean sea level. (b) Surrounding blocks stand 1 km higher and shed sediment (2000 kg m⁻³) at 1 mm/yr uniformly over A. How long can A keep receiving sediment? (c) When could A accommodate more?

> [!example]- Solution ([[LS07 Isostasy]], [[LS10 Folds Flexure and Mountain Building]])
> (a) The block floats with freeboard $H(1-\rho_c/\rho_m)=35\times600/3300=\mathbf{6.4}$ **km** above the free mantle surface. Ignoring water and crust means the ocean floor (4 km below sea level) is bare mantle at that free level, so A stands at $6.4-4\approx\mathbf{2.4}$ **km** above sea level. (Including 4 km of water and a 7 km, 2900 kg m⁻³ oceanic crust, the pressure balance at A's base gives 2.7 km. Both are higher than real continents (~0.8 km) because real crust is denser and thinner on average.) [!verify] The reading of "ignoring the loads" as "free mantle level at the ocean floor" is mine.
> (b) Sediment of thickness $s$ adds load, and A sinks by $s\rho_s/\rho_m$, so the surface rises only $s(1-\rho_s/\rho_m)=0.394s$. Filling the 1 km height difference needs $s=1/0.394=\mathbf{2.5}$ **km** of sediment: **~2.5 Myr** at 1 mm/yr. After that the sediment bypasses A.
> (c) More room appears if A **subsides for other reasons**:
> - thermal subsidence after rifting, or crustal thinning by extension;
> - **flexural loading by a nearby mountain belt** (foreland basins hold ~5 km);
> - sediment denser or compacting with burial;
> - sea-level rise (if base level is the sea);
> - the surrounding blocks being raised (their uplift raises the spill level).

> [!question] Q4 (3 + 2) · Steady-state ¹⁰Be
> Surface production $P\approx10$ atoms/yr per g of quartz, decaying exponentially with depth (scale $z^*\approx1$ m), steady erosion $e\approx1$ mm/yr. (a) Steady-state ¹⁰Be concentration at the surface? (b) How to interpret an observed value lower or higher than this?

> [!example]- Solution ([[Cosmogenic Erosion Rate]], [[Cosmogenic Nuclides]], [[LSX1 Clocks in Rocks]])
> (a) A grain approaching the surface at speed $e$ accumulates $\int P e^{-z/z^*}dz/e=Pz^*/e$ (radioactive decay is negligible: $\lambda=5\times10^{-7}$/yr ≪ $e/z^*=10^{-3}$/yr): $N=10\times1/10^{-3}=\mathbf{10^4}$ **atoms/g**.
> (b) $N\propto1/e$, so **lower $N$ ⇒ faster erosion** than 1 mm/yr. It can also mean deep-seated sediment from **landslides** (shielded material), a surface not yet at steady state, or lower production (lower altitude or latitude, shielding by snow or topography). **Higher $N$ ⇒ slower erosion.** It can also mean **inheritance** from earlier exposure (recycled sediment), or a long-exposed stable surface (approaching the decay limit $P/\lambda$).

> [!question] Q5 (2) · Steady circular hill
> A regolith-covered hill with circular contours; regolith production $w$ mm/yr, downhill flux per unit contour length $Q(r)=-K\,\partial_rz$. For a steady landscape, find and plot the radial profile.

> [!example]- Solution ([[LS12 Hillslope Transport and the Diffusion Equation]])
> At steady state, everything produced inside radius $r$ (the surface lowers at $w$ everywhere and is balanced by uplift, i.e. regolith produced at $w$) must leave through the circle: $2\pi rQ=\pi r^2w$ ⇒ $Q=wr/2$ ⇒ $\partial_rz=-wr/(2K)$ ⇒ $\boxed{z=z_0-\dfrac{w}{4K}r^2}$. A **paraboloid**, convex-up, with curvature $-w/2K$ in each direction. (The 1-D ridge gives $w/2K$ for its single curvature; here $\nabla^2z=-w/K$ is shared between two directions.)

> [!question] Q6 (2) · Tree throw
> One tree per 10 m², mean lifespan 30 yr; each throw moves 1 m³ of soil 0.3 m. Regolith flux?

> [!example]- Solution ([[LS12 Hillslope Transport and the Diffusion Equation]])
> Throws per unit area per year $=1/(10\ \text{m}^2\times30\ \text{yr})=3.3\times10^{-3}$ m⁻² yr⁻¹. Flux per unit contour width = (rate per area) × volume × distance $=3.3\times10^{-3}\times1\times0.3=\mathbf{10^{-3}\ m^2/yr}$ (10 cm²/yr). This assumes every tree dies by uprooting and the displacement is net downslope; on real slopes only a fraction falls downhill, so the net flux is smaller and grows with slope (giving a diffusivity).

> [!question] Q7 (2) · Filling the oceans
> With a mean sediment load of 50 t km⁻² yr⁻¹ in global rivers, how long would sediment take to fill the ocean basins? Implications?

> [!example]- Solution ([[LS27 Coasts Beaches Deltas and Rocky Shores]], [[LS07 Isostasy]])
> Flux $=50\times1.49\times10^8\ \text{km}^2\approx7.5\times10^9$ t/yr (all land; ~2/3 drains to the sea). Ocean volume $1.34\times10^{9}$ km³; at a deposited bulk density ~2 t/m³ that holds $2.7\times10^{18}$ t: **~350 Myr** (~500 Myr at rock density).
> **Implications:**
> - Oceans have existed ~4 Gyr yet are not full, so sediment must be **removed**: subduction of the sea floor (no ocean crust is older than ~200 Myr) and accretion and uplift back onto the continents (the rock cycle).
> - The same rate lowers the continents by 50 t/km²/yr ÷ 2.7 t/m³ ≈ 18.5 m/Myr, flattening the mean 840 m of land in **~45 Myr**. Continents survive only because **isostatic rebound and tectonic uplift keep replacing** what is eroded.

## EC2123 End-semester (30 Nov 2022, 28 marks)
*Added 2026-11-22: [[EC2123_endsem_22.pdf]] (2 pp., scanned; "End-Semester Examination, 2022 August Semester", EC2123, 2 h). Open notes, calculators allowed.*

> [!question] Q1 (3 + 2 + 3 + 2 + 2 + 2) · Bedrock rivers of the Bhutan Himalaya
> (a) Major processes by which bedrock rivers erode, and their dependence on sediment concentration. (b) The plot of main-stream length (km) against catchment area (km²) for Bhutan (log–log, blue line fit from ~(1 km², ~1.4 km) to (10⁵ km², ~10³ km)): find an empirical $A(x)$. (c) For bedrock rivers, uniform uplift and $q=cA(x)$, solve the steady profile $z(x)$, ignoring variations in rock strength. (d) Plot it. (e) Plot it for uplift $u_1$ upstream and $u_2$ downstream. (f) Cross-sections of a meandering bedrock river at two times, and a mechanism.

> [!example]- Solution ([[LS23 Bedrock Channels and River Incision]], [[Stream Power Law]], [[Knickpoint]], [[bedrock-gorges-and-entrenched-meanders]], [[Strath Terrace]])
> (a) Main processes:
> - **plucking (quarrying)** of joint-bounded blocks;
> - **abrasion** by saltating bedload, and by suspended load at high transport stages;
> - cavitation (rare);
> - dissolution and weathering of the bed between floods.
>
> Dependence on sediment: the **tools and cover effects**. With little sediment there are few tools, so erosion rises with supply. Too much sediment **covers** the bed and shields it. Erosion therefore peaks at an intermediate supply relative to transport capacity (the saltation–abrasion model), as in LS23.
> (b) The line spans ~2.85 decades in $L$ over 5 decades in $A$: $L\approx1.4\,A^{0.57}$ km (**Hack's law**, exponent ≈ 0.57, typical 0.5–0.6). Distance from the divide ≈ main-stream length, so $\boxed{A(x)\approx0.55\,x^{1.75}}$ (km², $x$ in km).
> (c) Stream power: $\partial_tz=u-K q^mS^n$ (with $S=-\partial_xz$). Steady state: $S=(u/Kc^m)^{1/n}A^{-m/n}=k_s(0.55x^{1.75})^{-\theta}$, $\theta=m/n$. With $\theta=0.5$: $S\propto x^{-0.88}$, and integrating from the outlet at $x=L$:
> $$z(x)=z(L)+\frac{k_s0.55^{-\theta}}{p}\big(L^{p}-x^{p}\big),\qquad p=1-1.75\theta\approx0.12 .$$
> Steepness ∝ $u^{1/n}$: faster uplift gives steeper rivers.
> (d) A **concave-up** profile: very steep near the head (the form fails within the channel-head distance, where hillslopes take over, [[Channel Head]]) and flattening downstream. Plotted against $\log x$ it is almost straight, since $p$ is small.
> (e) Each reach adjusts to its own uplift: $k_s\propto u^{1/n}$. For $u_1>u_2$, the upper reach is steeper by $(u_1/u_2)^{1/n}$: a **slope break (knickzone)** at the boundary, with $z$ continuous and the upper reach standing higher than in (d). For $u_1<u_2$ the lower reach is steeper and the profile is convex at the boundary. ([[Chi Transform]]: two straight segments with different slopes in χ–z.)
> (f) Two cross-sections show an **asymmetric valley migrating sideways as it deepens**:
> - Earlier: a channel with a steep cut bank on the outer bend and a gentler slip-off slope on the inner side.
> - Later: deeper, shifted towards the outside of the bend, with the abandoned inner floor left as a sloping bench or **strath terraces**: an *ingrown meander*.
>
> Mechanism: at the outer bank the flow is faster and the secondary circulation drives high shear stress and bedload impacts against the wall, which undercuts it. On the inner side the point bar shelters the bed with sediment (the cover effect). Lateral erosion during incision gives the asymmetry; pure vertical incision would give a symmetric **entrenched** meander.

> [!question] Q2 (2 + 2 + 2 + 1) · Post-glacial sea-level rise
> A plot of relative sea level from ~−125 m at the LGM to 0 today, with Meltwater Pulse 1A. (a) Why was sea level so low ~18 kyr ago? (b) Why did raised beaches form on islands near the Arctic Circle even as global sea level rose? (c) Sketch a coral atoll at the LGM, with the LGM and present sea levels. (d) Sea-level rise near Kolkata has been ~75 % faster than near Mumbai. Why?

> [!example]- Solution ([[LS15 Glacial Deposits Rebound and Sea Level]], [[LS26 Sea Level and Ocean Waves]], [[Relative Sea Level]], [[Marine Terrace]])
> (a) Water was **locked on land in ice sheets** (Laurentide, Fennoscandian, Antarctic growth): ~120–130 m of global sea level, ~5 × 10⁷ km³ of ice.
> (b) **Glacio-isostatic rebound.** The land under the former ice sheets rose faster than the global sea rose, so *relative* sea level fell there and successive beaches were lifted above the sea (a staircase of raised beaches, the youngest lowest). The eustatic rise slowed after ~7 kyr, while the rebound continued (τ ~ 3–5 kyr).
> (c) At the LGM the sea stood ~120 m lower. The atoll's reef rim and lagoon floor became a **flat-topped limestone island ~100 m high** with cliffs. Rain dissolved it (karst), so the old lagoon became a closed depression, and live reefs survived only as a fringe ~120 m down the steep outer slopes. Sketch: a volcanic core sinking slowly beneath a thick carbonate cap; the present reef growing back on the karstified LGM surface; the two sea levels marked 120 m apart. (This karst-rim origin also explains the dish shape of atolls.)
> (d) **Relative** sea-level rise = global rise + **land subsidence** + regional ocean effects. Kolkata sits on the **Ganga–Brahmaputra delta**, which subsides through **compaction of young sediment** (worsened by groundwater pumping) and through the delta's sediment load; dams starve it of the sediment that would build it up. Mumbai stands on Deccan basalt. The Bay of Bengal's regional rise (freshwater, warming, monsoon circulation) may differ too. [!verify] The attribution is general knowledge.

> [!question] Q3 (3 + 1 + 2 + 1) · A Himalayan glacier and its proglacial lake
> A contour map (5400–6400 m) of a glacier with a ~4 km proglacial lake at its snout (3 km scale bar). (a) Draw the hypsometry of the glacier and of the lake (axes, ticks, values). (b) Why did the lake form? (c) Does the lake affect the glacier's retreat? (d) Snow-line elevation on the day of the image?

> [!example]- Solution ([[LS14 Glaciers Mass Balance and Ice Flow]], [[LS19 Glacial and Aeolian Landforms]], [[LS15 Glacial Deposits Rebound and Sea Level]])
> (a) **Lake:** a single **spike** at its surface elevation (~5500 m on the map), holding all of its area, of order 4 km × 1 km ≈ 3–4 km². **Glacier:** area spread from the terminus (~5550 m) to ~6400 m. Most of it lies in a broad band at ~5800–6200 m (the wide upper basin), with a narrow tongue lower down and steep headwalls near the top. Sketch: area (km² per 100 m bin, peak ~1–2 km²) against elevation. [!verify] The values are read approximately from the scanned contours.
> (b) As the glacier **retreated** from its Little Ice Age extent, meltwater ponded in the **overdeepened basin** it had carved, dammed by its own **terminal and lateral moraines** (moraine-dammed proglacial lake).
> (c) **Yes, it speeds retreat.**
> - The front loses ice by **calving**.
> - Lake water warmer than 0 °C melts the ice face underwater (thermal undercutting).
> - The lake floats the snout, which removes basal drag and **accelerates flow and thinning**.
> - The lake then grows into the deepening trough: a positive feedback.
>
> It is also a GLOF hazard if the moraine fails.
> (d) The **snow line** is the boundary between bright snow and darker bare ice on the glacier. On the image it lies at **~5900–6000 m** (around the 5900–6000 m contours), which approximates the end-of-season ELA. [!verify] Read from the scan.

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
| EC2123 MS Q1, Q7 | Himalayan sediment budget, filling the oceans | [[LS10 Folds Flexure and Mountain Building]], [[LS27 Coasts Beaches Deltas and Rocky Shores]] |
| EC2123 MS Q2–Q6 | weathering profile, isostatic accommodation, ¹⁰Be, steady hill, tree throw | [[LS11 Weathering and Regolith]], [[LS07 Isostasy]], [[Cosmogenic Erosion Rate]], [[LS12 Hillslope Transport and the Diffusion Equation]] |
| EC2123 ES Q1 | bedrock rivers, Hack's law, steady profiles | [[LS23 Bedrock Channels and River Incision]] |
| EC2123 ES Q2–Q3 | post-glacial sea level, atolls, glaciers and proglacial lakes | [[LS15 Glacial Deposits Rebound and Sea Level]], [[LS26 Sea Level and Ocean Waves]], [[LS14 Glaciers Mass Balance and Ice Flow]] |

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
> | EC2123 mid-sem and end-sem 2022 | [[EC2123_midsem_22.pdf]], [[EC2123_endsem_22.pdf]] (Drive QP archive, 2026-11-22; scans read at 110 dpi); numbers `scripts/ls_qp_archive_numbers.py` | taught (past papers) / extra (solutions) |
>
> **Flags.** [!verify] (EC2123) the MS Q1 fan volumes and modern loads, the MS Q3a reading, the ES Q2d attribution, and the ES Q3 values read from the scan. (1) RS Q7 area 10× too small. (2) Quiz 2 Q3 says "underestimated"; the reservoir effect overestimates. (3) Q5's confluence and steepest-slope readings are approximate from a 40 m contour map. (4) Quiz 2 Q3's "equation 1" is not in the export; $N=N_0e^{-\lambda t}$ assumed.
