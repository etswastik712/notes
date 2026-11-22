---
title: Landscapes Past Papers 2021 - Solved
aliases: [landscapes paper 2021, EC2123 2021, landscapes and evolution fall 2021]
subject: landscapes
type: practice
scope: [taught, extra-beyond]
by: [exam-paper, own-notes]
status: draft
tags: [subject/landscapes, type/practice, taught, extra/beyond, src/exam-paper, status/draft]
---
# Landscapes Past Papers 2021 (Fall 2021, Argha Banerjee), Solved

[[Landscapes and Geomorphology - Course Map|Course Map]] · other years: [[Landscapes Past Papers 2022 (EC2223) - Solved|2022]] · [[Landscapes Past Papers 2024 - Solved|2024]] · practice: [[LS99 Landscapes Practice Problems]]

<span class="scope-taught">taught · past paper of this course</span> <span class="scope-extra-beyond">extra · beyond (solutions mine)</span>

> [!info] The paper
> [[Landscapes_and_evolution fall 2021 argha banerjee.pdf]] (8 slides, 6 questions × 5 marks), from the **Question Paper Archive → Sem-3 → EC2123** folder on the shared Google Drive, downloaded 2026-11-22 to `earth-and-climate/landscapes-geomorphology/lecture-notes-slides/past-papers/qp-archive/EC2123/`. Read from the text layer plus the slide images (the flexure formula, the slope map and the seismicity plot are images). The archive keeps only this one paper for 2021, with no mid-sem/end-sem label (the 2021 course was online). No key: solutions mine; numbers in `scripts/ls_qp_archive_numbers.py`.

## Q1 (1 + 1 + 1 + 2)
> [!question] (a) Two planets of the same radius $R$, one of rock and one of ice: ratio of the tallest peaks, if rock is ~10× stronger than ice? (b) Why do plumes such as Hawaii stay fixed relative to the Earth's centre despite mantle convection? (c) Why are deep earthquakes common along the western Pacific subduction zones but not under the Himalaya and Tibet? (d) Interpret the slope map of the western Indian Peninsula (bright = steep).

> [!example]- Solution ([[LS06 Maximum Topography]], [[LS05 Shape of Planets]], [[LS08 Plate Tectonics Strain Stress and Convection]], [[LS09 Faults and Earthquakes]], [[LS18 Deccan Traps Terrain]])
> (a) The strength limit is $\rho g\,\Delta h_{max}\sim2\tau_y$, so $\Delta h_{max}\propto\tau_y/(\rho g)$. At equal radius, surface gravity $g=\tfrac43\pi G\rho R\propto\rho$, so $\Delta h_{max}\propto\tau_y/\rho^2$:
> $$\frac{h_{rock}}{h_{ice}}=\frac{\tau_{rock}}{\tau_{ice}}\Big(\frac{\rho_{ice}}{\rho_{rock}}\Big)^2=10\Big(\frac{920}{3000}\Big)^2\approx\mathbf{0.9}\ (\text{1.2 for }\rho=2700).$$
> **About the same height.** The ice planet's weaker rock is offset by its gravity, which is ~3× weaker. (For a rocky planet with an iron core, take the *mean* density for $g$, e.g. 5500: the ratio is ≈ 0.3.)
> (b) Plumes rise from a **thermal boundary layer deep in the mantle (the core–mantle boundary or the 660 km transition)**. The lower mantle is ~10–100× more viscous and moves far more slowly than the plates, so the plume roots act as a quasi-fixed **hotspot reference frame**. The plates slide over them, which leaves age-progressive chains such as Hawaii–Emperor. (In detail plumes drift by a few mm/yr.)
> (c) Earthquakes need cold, brittle rock. Along the western Pacific, **old, cold oceanic lithosphere subducts steeply to 660 km** and stays cold enough to fail (Wadati–Benioff zones, down to ~700 km). Under the Himalaya, **buoyant continental India underthrusts at a shallow angle** and does not sink, so below ~80–100 km the rock is too hot and ductile.
> (d) A **thin, continuous bright band of steep slopes runs parallel to the coast for > 1000 km**, about 50–100 km inland. This is the **Western Ghats escarpment** (a "Great Escarpment"): a single scarp separates a narrow, low, gentle coastal plain (Konkan/Malabar, dark) from a high, gentle plateau (the Deccan, dark). Interesting features:
> - The steep zone is narrow and continuous, a scarp rather than a mountain range. The drainage divide lies at its crest, close to the west coast, so the rivers on that side are short and steep and the east-flowing ones are long.
> - It is a passive-margin scarp, retreating inland from the rift that opened the Arabian Sea.
> - The band thins out near the Palghat Gap (south).

## Q2 (2 + 2 + 1) · Seasonal seismicity in Alaska
> [!question] Box plots of earthquake frequency (events/day, ~1.0–1.6) against day of year, 2000–2016, with the monthly mean rates in orange. (a) The most interesting feature? (b) Possible mechanisms? (c) Similar elsewhere?

> [!example]- Solution ([[LS09 Faults and Earthquakes]], [[LS25 Water in the Landscape]])
> (a) A **seasonal cycle**. The rate is highest in late autumn to spring (~1.35–1.4 per day; days ~260–110) and lowest in **summer** (~1.2 per day; days ~140–230), a ~15 % modulation. Tectonic loading is steady, so the cycle must come from something seasonal.
> (b) **Seasonal surface loads change the stress on faults by a few kPa.** Tectonic stress is ~MPa, but faults that are already close to failure respond to small changes in Coulomb stress ($\Delta\tau-\mu\Delta\sigma_n$):
> - snow and ice accumulate in winter and melt in summer (glaciers, snowpack);
> - groundwater and surface-water storage change through the year;
> - pore pressure diffuses (the delayed response to infiltration);
> - smaller contributions from atmospheric pressure and thermoelastic stress.
>
> The winter maximum means the winter load (snow, frozen ground water) moves most faults *towards* failure and its removal in summer moves them away. Which way a load acts depends on the fault's type and orientation, and on the pore-pressure lag.
> (c) **Yes, wherever large seasonal loads act on critically stressed faults.** The classic case is the **Himalaya**: seismicity is higher in winter, when the monsoon water load on the Gangetic plain has drained away, and lower in summer. California and Japan show the same. The sheet links an EPSL paper (2007/08) for this; [!verify] I have not read the paper, and these examples are general knowledge.

## Q3 (2 + 2 + 1) · Two immiscible liquids
> [!question] Two immiscible liquids in hydrostatic equilibrium, densities $d_1$ (top) and $d_2$ (bottom) in a glass. (a) Plot pressure against depth $z$. (b) Exchange two blobs of volume $dV$ across the interface: what is the net force on them? Significance? (c) A landscape where an analogous process is at work?

> [!example]- Solution ([[LS07 Isostasy]], [[LS02 Mechanics and Mathematics Toolkit]])
> (a) $p=p_0+d_1gz$ down to the interface at $z=h_1$, then $p=p_0+d_1gh_1+d_2g(z-h_1)$: **two straight lines** that meet at the interface, with slopes $d_1g$ and $d_2g$ (the kink is steeper below if $d_2>d_1$).
> (b) A blob of liquid 1 moved down into liquid 2 feels buoyancy $d_2gdV$ against its weight $d_1gdV$: net **upward** force $(d_2-d_1)g\,dV$. The blob of liquid 2 moved up feels a net **downward** force $(d_2-d_1)g\,dV$.
> - If $d_2>d_1$ (light over heavy), both forces push the blobs **back**: the state is **stable**. The swap raises the potential energy by $(d_2-d_1)g\,dV\,\Delta z$.
> - If $d_1>d_2$ (heavy over light), the forces drive the swap further and the potential energy falls. This is the **Rayleigh–Taylor instability**: the layers overturn.
>
> The significance is that hydrostatic equilibrium is not enough; *stability* depends on the density order.
> (c) **Salt diapirs and salt domes.** Rock salt (~2200 kg m⁻³) buried under denser sediment (~2500) rises as domes and walls, which pierce the surface as salt glaciers, e.g. the Zagros of Iran and the Gulf Coast. Others: mud diapirs and mud volcanoes, and the evenly spaced magma diapirs that feed arc volcanoes (the 2024 mid-sem's South Sandwich question, [[Landscapes Past Papers 2024 - Solved]]).

## Q4 (2 + 2 + 1) · Panchgani table land
> [!question] An aerial photo of the Panchgani table land (~100 km south of Pune, ~1400 m), a flat-topped hill with steep sides. For the table land and its surroundings: (a) plot the hypsometry; (b) plot the slope distribution; (c) why are such flat hilltops common around Pune?

> [!example]- Solution ([[LS03 Digital Elevation Models and Terrain Analysis]], [[LS18 Deccan Traps Terrain]], [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]], [[laterite-cappings]], [[planation-surfaces]])
> (a) **Bimodal hypsometry.**
> - A tall, narrow peak at **~1300–1400 m**: the flat top occupies a large area at almost one elevation.
> - A broader peak at the valley floors (~700–900 m around Panchgani and the Krishna valley).
> - Little area in between: the scarp is steep, so it covers little map area per metre of height.
>
> (b) **Also bimodal**, or a spike plus a tail. Most of the area is at **< 5°** (the plateau top and the valley floors). A second, smaller mode at **~25–35°** comes from the scarp faces, with near-vertical cliffs at the top where the cap rock is exposed. Intermediate slopes are rare.
> (c) **Deccan Traps stratigraphy.** The Western Deccan is a pile of **near-horizontal basalt flows**. Massive, jointed flow interiors (and laterite caps) are **resistant**; vesicular flow tops, red boles and weathered inter-flow horizons are weak. Erosion strips the weak layers and stalls on a resistant flow, which leaves **flat-topped mesas** bounded by stepped scarps ("trap" topography). The laterite crust on many tops (Panchgani is lateritic) armours the surface further, and some tops are remnants of old planation surfaces.

## Q5 (2 + 2 + 1) · Flexure under a line load
> [!question] $w=w_0e^{-x/\alpha}\big(\cos\frac x\alpha+\sin\frac x\alpha\big)$, downward deflection, $\alpha\approx100$ km. (1) Plot it from $x=0$ to $5\alpha$. (2) What does it imply for the topography of India, which carries the Himalaya along its northern edge? (3) Is the thin-plate solution valid for India?

> [!example]- Solution ([[LS10 Folds Flexure and Mountain Building]])
> (1) $w(0)=w_0$ (deepest, under the load), and $w'(0)=0$. The curve falls to **zero at $x=3\pi\alpha/4=236$ km**, then rises *above* the reference level to a **peripheral bulge of height $0.043\,w_0$ at $x=\pi\alpha=314$ km**. After that the oscillation is negligible ($|w|/w_0<0.005$ at $5\alpha$). Sketch: a deep, broad trough, a gentle low hump, then flat. These are the numbers from LS10 eq. (21).
> (2) The trough south of the Himalaya is the **foreland basin**, filled by the **Indo-Gangetic plains** sediment, deepest (~5–6 km) at the mountain front and thinning southward. About 250–300 km further south a **forebulge** should stand slightly high. [!verify] It is usually identified with the Bundelkhand–Vindhyan uplands and the buried Delhi–Haridwar and Faizabad ridges; this is general knowledge, not from the course. A sediment-filled basin has a larger $\alpha$ (LS10: 82 versus 59 km), so the basin widens.
> (3) **Roughly yes, with caveats.**
> - Thin-plate theory needs the elastic thickness ($T_e\sim40$–70 km for India) to be much smaller than the flexural wavelength ($2\pi\alpha\approx600$ km). That holds.
> - Small slopes are assumed. That holds too.
> - Caveat 1: the Indian plate is **broken or strongly weakened under the Himalaya**, so a broken-plate solution (free end at the load) fits better and gives a narrower, deeper basin. The 2024 end-sem uses this form ([[Landscapes Past Papers 2024 - Solved]], Q3).
> - Caveat 2: the load is distributed, not a line.
> - Caveat 3: $T_e$ varies along strike, and the plate is not purely elastic (inelastic yielding where curvature is high).

## Q6 (1 + 1 + 1.5 + 1.5) · Post-glacial rebound and mantle viscosity
> [!question] Uplift after the LGM ice sheets (20 kyr BP) decays exponentially with $\tau=5000$ yr. (1) Why so slow? (2) From $\rho=3300$ kg m⁻³, $\lambda=3000$ km and $g=10$ m s⁻², build a pressure $P$. (3) From $\tau$ and $P$, build a quantity with the units of viscosity. (4) Estimate the mantle viscosity.

> [!example]- Solution ([[LS15 Glacial Deposits Rebound and Sea Level]], [[LS07 Isostasy]])
> (1) The lithosphere can only rise as fast as **mantle rock flows back** beneath it. The mantle is a solid that creeps, with a viscosity ~10²¹ Pa s, so restoring isostasy over a 3000 km wide region takes thousands of years. Elastic response is instantaneous; viscous flow is not.
> (2) $P=\rho g\lambda=3300\times10\times3\times10^6=\mathbf{9.9\times10^{10}}$ **Pa**. This is the hydrostatic pressure scale of a load of that size.
> (3) Viscous stress = $\mu\times$ (velocity gradient), and a velocity gradient has units s⁻¹, so $[\mu]$ = Pa s, and $\mu\sim P\tau$.
> (4) $\mu\sim P\tau=9.9\times10^{10}\times(5000\times3.156\times10^7\ \text{s})=\mathbf{1.6\times10^{22}}$ **Pa s**. The exact half-space result $\tau=4\pi\mu/(\rho g\lambda)$ (LS15 eq. 29) gives $\mu=P\tau/4\pi=\mathbf{1.2\times10^{21}}$ Pa s, the accepted upper-mantle value. Dimensional analysis gets the scaling right but misses the factor $4\pi$, i.e. one order of magnitude.

## Topic map
| question | topic | vault |
|---|---|---|
| Q1a | maximum topography, gravity | [[LS06 Maximum Topography]], [[LS05 Shape of Planets]] |
| Q1b–c, Q2 | plumes, subduction, earthquakes, seasonal seismicity | [[LS08 Plate Tectonics Strain Stress and Convection]], [[LS09 Faults and Earthquakes]] |
| Q1d, Q4 | Western Ghats, Deccan mesas, hypsometry and slope statistics | [[LS03 Digital Elevation Models and Terrain Analysis]], [[LS18 Deccan Traps Terrain]], [[LS28 Deccan Field Guide Lava Architecture and Sahyadri Stratigraphy]] |
| Q3 | hydrostatics, density inversion | [[LS07 Isostasy]] |
| Q5 | flexure, foreland basin | [[LS10 Folds Flexure and Mountain Building]] |
| Q6 | glacial rebound, mantle viscosity | [[LS15 Glacial Deposits Rebound and Sea Level]] |

## Provenance
> [!provenance]- Source map
> | Topic | Source | Scope |
> |---|---|---|
> | all questions | [[Landscapes_and_evolution fall 2021 argha banerjee.pdf]] (Drive QP archive, 2026-11-22; text layer + slide images) | taught (past paper) |
> | flexure zero and bulge, rebound formula | [[LS10 Folds Flexure and Mountain Building]] eq. (21), [[LS15 Glacial Deposits Rebound and Sea Level]] eq. (29) (read this session) | vault |
> | numbers | `scripts/ls_qp_archive_numbers.py` | extra/beyond |
>
> **Flags.** [!verify] (1) The Q2 mechanism and the Himalayan example are general knowledge; the linked paper was not read. (2) The forebulge locations in Q5 are general knowledge. (3) The Panchgani elevations are estimates from the photo and the stated 1400 m.
