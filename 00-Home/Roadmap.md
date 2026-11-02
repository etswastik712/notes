---
title: Roadmap
tags: [meta, type/meta]
---
# Roadmap

Order of work, with the reasons from [[Subject Map]]. Status of each item is tracked in [[PROGRESS]] and live in [[Dashboard]].

## Phases
| Phase | Subjects | Why this order |
|---|---|---|
| **1** | **Climate** (+ parallel: **Thermodynamics**, **Foundations**), then **Ecology and Evolution** | climate was requested first; it shares radiation and gas-law tools with thermodynamics and stability/feedback tools with eco-evo, which is next |
| **2** | Evolution of Earth and Life · Landscapes and Geomorphology · Waves · Probability | each is strongly tied to Phase 1 (paleoclimate; weathering/erosion; atmospheric waves; stochastic models) |
| **3** | Quantum Mechanics · Group Theory · Inorganic Chemistry · Proofs, Analysis and Topology | a tight cluster: symmetry → orbitals → spectra; analysis as rigour |
| **4** | Neuroscience | currently a single paper, least connected |

## Phase 1a: Climate
| Step | Work | Status |
|---|---|---|
| 0 | vault shell: plugins, tags, conventions, Home/Roadmap/PROGRESS/Toolkit, templates, canvases | **done** |
| 1 | pilot: CL03, CL04, CL12 + concept notes + figures + handouts | **done** |
| 1b | v2 standard (syllabus map, scope chips, intuition, depth) applied; quiz chapters [[CL09 Radiative-Convective Equilibrium]], [[CL10 Global Energy Balance and Meridional Structure]], [[CL11 Mean Meridional Circulation and Angular Momentum]], [[CL12 Rotating Frames and the Coriolis Force]]; then [[CL13 Horizontal Motion - Geostrophic Balance and Friction]], [[CL14 Observed Winds - Jets, Trades and the ITCZ]], [[CL15 Monsoons]]; [[Climate Quiz Prep]] | **done, awaiting your review** |
| 2 | the remaining chapters [[CL01 Earth as a System]], [[CL02 Observing Global Temperature]], [[CL05 Thermodynamic State of the Atmosphere]], [[CL06 Hydrostatic Balance and Vertical Structure]], [[CL07 Optical Properties of the Atmosphere]], [[CL08 Greenhouse Models]] | **done (draft), awaiting your review** |
| 3 | formula sheet, full-book PDF (LaTeX), problem bank, spaced-repetition lists | todo |
| 4 | cross-link audit in Obsidian, canvas refresh, taught/extra audit against the photos with the instructors' answers to the `[!verify]` boxes | todo |

All 15 climate chapters now follow the v2 standard.

## Phase 1b: Ecology and Evolution
| Step | Work | Status |
|---|---|---|
| 1 | [[EE01 Introduction to Biology and Ecological Thinking]] + 10 concept notes + 6 figures/diagrams | **done (draft), awaiting your review** |
| 2 | [[EE02 Structured Population Models]] + 11 concept stubs + 5 figures, 1 diagram | **done (draft v2)** |
| 3 | [[EE03 Population Dynamics and Chaos]] (12 figures checked, 6 worked examples, 10 practice problems) | **done (draft v2)** |
| 4 | [[EE04 Competition and Invasions]] (3 own figures/diagrams, `ee04_numbers.py`) | **done (draft v2)** |
| 5 | [[EE05 Predation]] (1 figure, `ee05_numbers.py`; Molles Ch. 14 OCR'd) | **done (draft v2)** |
| 6 | [[EE06 Eutrophication and Alternative Stable States]] (hysteresis figure, loop diagram, `ee06_numbers.py`) | **done (draft v2)** |
| 7 | [[EE07 Conservation Biology]] (tigers and drift figure, concept diagram; earlier 2 figures checked) | **done (draft v2)** |
| 8 | **Elaborate the 68 eco-evo concept stubs** (user's instruction: after all 7 chapters) | **done (draft)**, 2026-10-25 |
| 9 | [[Eco-Evo Exam Prep]], [[Eco-Evo Problem Bank]] (25 problems, all computed), 2-page formula-sheet PDF | **done (draft)**, 2026-10-25 |

Course map: [[Ecology and Evolution - Course Map]].

## Phase 3a: Quantum Mechanics (PH2113)
| Step | Work | Status |
|---|---|---|
| 1 | [[QM01 From Waves to Probabilities]] · [[QM02 The Schrodinger Equation and Stationary States]] · [[QM03 States Operators and Measurement]] · [[QM04 The Particle in a Box]] · [[QM05 The Harmonic Oscillator]] (9 figures + 1 diagram, `qm_numbers.py`) | **done (draft)**, 2026-10-25 |
| 2 | 51 concept notes (`06-Quantum-Mechanics/Concepts/`, plus Dimensional Analysis and Gaussian Integral in `09-Foundations/Concepts/`) | **done (draft)** |
| 3 | course map, 2-page formula sheet ([[qm-formula-sheet.pdf]]) | **done** |
| 3b | **QM05 rebuilt** on the handwritten oscillator lecture and Tutorial III; **[[QM06 The Oscillator Toolbox]]** (number basis, expectation values, normalisation, Hermite polynomials in full, momentum space, Ehrenfest/Heisenberg/virial, coherent and thermal states) with 35 new concept notes; [[Quantum Mechanics Quiz Prep]] (mock quiz + 3 Sep quiz) | **done (draft)**, 2026-10-25 |
| 4 | tunnelling/steps, hydrogen, angular momentum, spin: **sources needed** (not in the folder); a full problem bank | todo |

## Phase 3b: Thermodynamics
| Step | Work | Status |
|---|---|---|
| 1 | [[TH01 Temperature and the Zeroth Law]] · [[TH02 Work Heat and the First Law]] · [[TH03 The Ideal Gas and Adiabatic Processes]] · [[TH04 The Second Law Carnot Engines and Entropy]] · [[TH05 Potentials Maxwell Relations Stability and the Third Law]] · [[TH06 From Kinetic Theory to Statistical Mechanics]] (7 figures + 1 diagram, `th_numbers.py`) | **done (draft)**, 2026-10-25 |
| 2 | 50 concept notes (`03-Thermodynamics-and-Statistical-Mechanics/Concepts/`), course map, 2-page formula sheet ([[th-formula-sheet.pdf]]) | **done (draft)** |
| 3 | confirm the syllabus (which lectures are examinable); MIT Lectures 5+; exam prep and problem bank | todo |


### Phase 3b-II: Statistical mechanics (self-study, from the books; added 2026-10-30)
Part II of the same subject: 31 chapters planned in five parts (foundations and ensembles; quantum statistics; interacting systems and phase transitions; non-equilibrium; applications), Kardar as the spine, Pathria and Beale and others for what Kardar's particle volume lacks. **SM01–SM07 done (draft): Part II-A (foundations, ensembles, kinetic theory, grand canonical, entropy and information, equipartition and magnetism) is complete (2026-11-02)**, awaiting review; next: formula sheet and quiz prep, then Part II-B (quantum statistics, SM08–SM13). Plan and source map: [[Thermodynamics and Statistical Mechanics - Course Map]]; handoff: [[PROGRESS]].

## Phase 3c: Probability (MT2113)
| Step | Work | Status |
|---|---|---|
| 1 | [[PR01 Counting and the Axioms of Probability]] · [[PR02 Conditional Probability Bayes Rule and Independence]] · [[PR03 Discrete Random Variables and Distributions]] · [[PR04 Joint Distributions Expectation and Variance]] · [[PR05 Continuous Random Variables]] · [[PR06 Moments Generating Functions and Limit Theorems]] (6 figures + 1 diagram, `pr_numbers.py`, 60 practice problems with solutions) | **done (draft)**, 2026-10-25 |
| 2 | 58 new concept notes (60 in `08-Probability/Concepts/`), course map, 2-page formula sheet ([[pr-formula-sheet.pdf]]) | **done (draft)** |
| 2b | **Week 2 and Week 3 handwritten lectures integrated** (PR05: folded normal, exponential, memoryless theorem, HW2; PR06: median, mode, moments, MGFs, HW3), 6 new concept notes, formula sheet rebuilt | **done (draft)**, 2026-10-25 |
| 3 | confirm with the instructor whether Markov/Chebyshev/LLN/CLT are examinable; the "updated 27 Aug" notes; a Week 4 lecture; exam prep and problem bank | todo |

## Phase 3d: Proofs, Analysis and Topology
| Step | Work | Status |
|---|---|---|
| 1 | [[PA01 Logic and Methods of Proof]] · [[PA02 Sets Families and the ZFC Foundations]] · [[PA03 Relations Equivalence and Order]] · [[PA04 Functions and Cardinality]] · [[PA05 Induction and the Number Systems]] · [[PA06 The Real Numbers and Sequences]] · [[PA07 Metric and Topological Spaces]] (6 figures + 2 diagrams, `pa_numbers.py`, 70 practice problems with solutions) | **done (draft)**, 2026-10-25 |
| 2 | 56 concept notes (`11-Proofs-Analysis-Topology/Concepts/`), full course map, 2-page formula sheet ([[pa-formula-sheet.pdf]]) | **done (draft)** |
| 3 | confirm how far the course goes (PA06–PA07 have no lecture source); Lectures 1–16; exam prep and problem bank | todo |

## Phase 3e: Inorganic Chemistry (CH2113) — pilot
| Step | Work | Status |
|---|---|---|
| 1 | [[Inorganic Chemistry - Course Map]] (real), [[CH01 VSEPR and Valence Bond Theory]] + 13 concept notes + 1 figure + 1 diagram | **done (draft pilot)**, 2026-10-25 |
| 2 | CH02–CH03 molecular orbital theory (slides 27–52, MOT Part 2); CH04–CH06 acids, bases and HSAB (53–82); CH07–CH08 main-group clusters, rings, polymers (83–119); CH09 redox (S&A Ch. 5) | todo, **after the user's review of the pilot** |

## Phase 3f: Differential Geometry (MT3184)
| Step | Work | Status |
|---|---|---|
| 1 | prerequisites in the analysis vault: [[PA11 Subspaces, Products and Quotients]] · [[PA12 Separation, Countability and Local Compactness]] · [[PA13 The Derivative and the Inverse Function Theorem]] · [[PA14 ODE Existence Uniqueness and Smooth Dependence]] · [[PA15 Covering Spaces and the Fundamental Group]] + 40 concept notes + 5 figures | **done (draft)**, 2026-10-30 to 11-01 |
| 2 | [[Differential Geometry - Course Map]] and [[DM01 Smooth Manifolds]] … [[DM15 Closed Subgroups and the Lie Correspondence]] (Lee, *Introduction to Smooth Manifolds*, primary; 🟢/🟡/🔵 by MT3184 coverage) + 98 concept notes + 15 figures + `scripts/dm_numbers.py` (every number recomputed) + `scripts/check_lee_cites.py` (every Lee citation checked against the PDF) | **done (draft)**, 2026-11-02 |
| 3 | the 38 MT3184 zettel notes moved from `10-Group-Theory/Concepts/zettel/` to `14-Differential-Geometry/Concepts/zettel/` and filed under the DM chapters (+5 new from HW1) | **done**, 2026-11-02 |
| 4 | read the scans DG1–DG7 (weeks 1–3), confirm whether Frobenius/Sard are examinable, formula sheet, exam prep and problem bank (Test 2 on 2026-11-02, end-sem 11-23 to 12-02) | todo |

## Parallel topics added alongside climate
- **Thermodynamics** ([[Thermodynamics and Statistical Mechanics - Course Map]]): done: blackbody laws, ideal gas law. To add: first law and adiabats, moist thermodynamics (Clausius–Clapeyron), entropy and heat engines, kinetic theory, statistical mechanics of photons.
- **Foundations**: done: stability, linearisation, bistability, Jensen, relaxation, rotating frames. To add: ODE/PDE basics, vector calculus identities, dimensional analysis, Fourier series, dynamical systems (bifurcations, chaos for eco-evo).
- **Climate extras** (out of syllabus, labelled `extra/beyond`): paleoclimate proxies, carbonate–silicate cycle, AMOC/Stommel box model (an existing AI note has figures), ENSO, climate models hierarchy.

## Definition of done for a chapter
1. Sequential, continuous narrative; overlaps between lecturers merged (the "dropped as redundant" line in *Provenance* says what).
2. Every taught claim traceable to a slide or page; extras boxed and labelled; disagreements in `[!verify]`.
3. Numbers recomputed; at least one generated figure, one diagram or canvas, practice problems with answers.
4. Concept notes linked on first use; cross-subject `[!connection]` boxes.
5. Frontmatter and tags per [[Conventions]]; status raised from `stub` → `draft` → `reviewed` (after you have read it).

## Beyond notes
Per-subject glossary, a formula/constant sheet, a full printable PDF book per subject (LaTeX, built from the same sources as the notes), and spaced-repetition question lists.
