---
title: Conventions
tags: [meta, type/meta]
---
# Conventions

How every note in this vault is written, labelled and linked. Read this before adding or editing anything (this includes Claude sessions: see [[PROGRESS]] for the resume protocol).

## 1. Organisation: tags, not folders
Folders only separate subjects (`01-Climate/`, `02-Eco-Evo/`, ...). **Global rule (user, 2026-10-25): inside every subject folder, chapters, the course map and quiz-prep/problem pages stay at the top level and every concept note (`type: concept`) goes in that folder's `Concepts/` subfolder** (`01-Climate/Concepts/`, `02-Eco-Evo/Concepts/`, `06-Quantum-Mechanics/Concepts/`, ...). Links are by note name, so the subfolder never appears in a `[[link]]`. Everything else (what a note is, who taught it, whether it was taught or is extra) is a **tag or a property**, so one note can live in several views and [[Dashboard]] pages assemble the lists automatically.

| Tag family | Values | Meaning |
|---|---|---|
| `subject/…` | `climate`, `eco-evo`, `thermo`, `foundations`, … | which course or support area owns the note |
| `type/…` | `moc`, `chapter`, `concept`, `derivation`, `handout`, `canvas`, `meta`, `problems` | what kind of note it is |
| `taught` | (flat tag) | content shown or said in class ⇒ **in the syllabus** |
| `extra/book` | | in an assigned book/excerpt but **not** seen in class |
| `extra/beyond` | | added by me (papers, Wikipedia, textbooks outside the course); **not** in the syllabus |
| `src/…` | `argha`, `suhas-pre`, `suhas-post`, `slides`, `lecture-notes`, `book`, `paper`, `web`, `own-notes` | where the content came from (`slides`: eco-evo decks; `lecture-notes`: typed or handwritten notes of PH2113) |
| `status/…` | `stub`, `draft`, `reviewed` | maturity of the note |

A note carries every scope tag that appears in it. A chapter that is mostly taught but contains a boxed extra has both `taught` and `extra/beyond`.

### Scope labels inside a note (v2)
Three layers, so that you always know *what is in the syllabus and what is extra, for this chapter and for this paragraph*:

1. **Syllabus map** (mandatory, directly under the title). A `[!syllabus]` callout with a short labelled **list** (not a table, so it wraps in a narrow pane) giving, by section, what is 🟢 *taught / in syllabus*, 🟡 *extra · book*, 🔵 *extra · beyond*. Groups with nothing in them are left out.
2. **Section chips.** Every `##` heading (and any `###` whose scope differs) is followed by one line with a chip and its source:
   `<span class="scope-taught">taught</span> *Argha L3, slides 30–31*`  ·  `<span class="scope-extra-book">extra · book</span> *M&P §6.6.1, p.93*`  ·  `<span class="scope-extra-beyond">extra · beyond</span> *derived here*`.
3. **Extras live in callouts**, so the syllabus text reads straight through. Titles are prefixed with the colour dot:
   ```
   > [!extra-book]+ 🟡 Extra (book): <title>      open by default
   > [!extra-beyond]- 🔵 Extra (beyond): <title>  collapsed (long derivations)
   ```
   A section that is *entirely* extra is wrapped in one such callout. Top-of-note badges appear **only for scopes that are present**.

Frontmatter mirrors this: `scope: [taught, extra-book, extra-beyond]`, `by: [argha, suhas-post]`, plus the tags `taught`, `extra/book`, `extra/beyond`.

### How "taught" is decided (climate)
1. **Argha**: the Keynote deck `climate_intro_L1_L6.pdf` (slide numbers cited) is the whole of what Argha taught; everything in it is `taught`.
2. **Suhas, pre-midsem**: `Basics of atmosphere.docx` plus the lecture material consolidated in the AI notes `suhas notes.pdf`; checked against the books.
3. **Suhas, post-midsem**: the dated photo-slides (`7th Oct.pdf` … `22nd Oct.pdf`, `22nd Oct CliSci slides.pdf`) and the handwritten `Suhas post midsem.pdf`. A book passage counts as `taught` only if it (or its figure/equation) appears there; the rest of the assigned excerpt is `extra/book`.
4. Existing AI-generated notes (`argha-climate.pdf`, `suhas notes.pdf`, `climate_intro_notes_L1_L6.pdf`, `climate_book_notes.pdf`) are **secondary**: I use them to cross-check, never as the authority. Disagreements are flagged with `[!verify]`.

## 2. Note types and layout

### Chapter (`type/chapter`)
Numbered `CLnn Title` (`EEnn`, `QMnn`, `THnn`, `PRnn` probability, `PAnn` proofs/analysis/topology for other subjects). Sequential, self-contained, redundancy between lectures removed. Full anatomy in §7; copy [[Chapter Template]].
```
---
title: CL03 Radiation and Planetary Energy Balance
subject: climate
type: chapter
chapter: 3
part: I
scope: [taught, extra-book, extra-beyond]     # only the scopes that occur
by: [argha, suhas-pre]
status: draft
prereq: ["[[CL02 Observing Global Temperature]]"]
tags: [subject/climate, type/chapter, taught, extra/book, extra/beyond, src/argha, src/suhas-pre, status/draft]
---
# Title
◀ prev · Course Map · next ▶
badges (only scopes present)
> [!syllabus] Syllabus map            ← what is taught / extra IN THIS chapter, by section
> [!key] After this chapter you can
## sections, each followed by a scope chip line
## Map of this chapter · ## Summary · ## Practice (+ Solutions) · ## Provenance
```

### Concept (`type/concept`)
One definition/law per note, 100–400 words, always: a `[!syllabus]` line (what is taught vs extra), an `[!intuition]` picture, the `[!key]` definition, equation/units/numbers, where it is used, and a live **Linked from** list (`LIST FROM [[]]`). Concepts are the graph's hubs; chapters link to them on first use. `scripts/build_glossary.py` turns all concept notes into [[Glossary]].

### Callout vocabulary
`key` core idea · `derivation` full steps · `intuition` · `example` worked numbers · `pitfall` common error · `connection` bridge to another subject · `verify` unresolved or inconsistent claim · `provenance` source map · `taught` / `extra-book` / `extra-beyond` scope boxes.

## 3. Linking and citing
- Wikilinks everywhere: `[[Albedo]]`, `[[CL04 Feedback and Multiple Steady States#Stability of a steady state]]`. Use an alias when the title is awkward: `[[Stefan–Boltzmann Law|σT⁴]]`.
- **Citing the course material** (clickable, opens the PDF on the right page; `page=` is the *PDF* page index):
  - Argha deck: `[[climate_intro_L1_L6.pdf#page=35|Argha L3, slide 35]]`
  - photo slides: `[[14th Oct.pdf#page=10|14 Oct, p10]]`
  - books: `[[Atmospheric Science - An Introductory Surv - John M. Wallace.pdf#page=464|Wallace & Hobbs §10.3, p.447]]` (book page = PDF page − 17)
  - embed a page: `![[15th Oct.pdf#page=10&height=380]]`
- Source registry with all file names and offsets: [[Sources]].
- External citations in `[Author Year]` form with a link at the end of the note; web pages are academic, governmental or Wikipedia only.

## 4. Mathematics (MathJax)
- Inline `$…$`, display `$$…$$`; multi-line derivations in `aligned`. Key results are boxed with `\boxed{}` and, if cited later, tagged `\tag{CL3.4}`.
- Vectors bold (`\mathbf{u}`), unit vectors with hats, `\mathrm{d}` for differentials, `\partial` for partials, `\mathrm{D}/\mathrm{D}t` for the material derivative.
- Always give units; show a numerical sanity check next to any formula that will be used on numbers.
- LaTeX source for PDF handouts lives in `Assets/latex/`; compiled PDFs in `Assets/pdf/` and embedded with `![[name.pdf]]`.

### Climate notation
| Symbol | Meaning | Value / unit |
|---|---|---|
| $S$ ($S_0$) | solar irradiance at Earth's distance | 1361 W m⁻² |
| $\alpha$ | (Bond/planetary) albedo | 0.30 |
| $\sigma$ | Stefan–Boltzmann constant | $5.67\times10^{-8}$ W m⁻² K⁻⁴ |
| $T_e$ | effective (emission) temperature | 255 K |
| $T_s$ | surface temperature | 288 K |
| $\Lambda_P$ | Planck sensitivity $1/(4\sigma T^3)$ | 0.27 K (W m⁻²)⁻¹ |
| $f_i$, $f$ | feedback factors | dimensionless |
| $\Omega$ | Earth's rotation rate | $7.292\times10^{-5}$ s⁻¹ |
| $a$ | Earth's radius | 6371 km |
| $\varphi$ | latitude | rad |
| $g$ | gravitational (effective) acceleration | 9.81 m s⁻² |
| $H$ | scale height | ≈ 8 km |

## 5. Figures
- **Generated** (preferred): one script per figure in `scripts/`, named `fig_<chapter>_<slug>.py`, output PNG to `Assets/figures/`. Style lives in `scripts/figlib.py`: a fixed categorical order, thin lines, direct labels. Rebuild with `make_figures.py` (see [[Toolkit]]).
- **Excalidraw** sketches in `Assets/excalidraw/` for conceptual diagrams; **Canvas** files for concept maps; **TikZ** for geometry inside PDF handouts.
- **Page embeds / crops** from the course PDFs with a citation under the figure (personal-use study material).
- Every chapter has at least one figure and one diagram or canvas link.

## 6. Verification policy
- Numbers are recomputed (script or by hand) before they go in a note. When a slide, a book or my own computation disagree, the note says so in a `[!verify]` box and states which value is used.
- Out-of-course material is checked against an academic or government source and cited.

## 7. Global theme v2: anatomy of every chapter
> **Narrow panes.** Keep tables short: ≤ 4 columns, cells of a few words. Long prose belongs in lists or callouts, not table cells (they force side-scrolling). The syllabus map is therefore a list.

This is the standard for every subject (climate, eco-evo, …). Template: [[Chapter Template]].

| Block | Rule |
|---|---|
| **Header** | nav line (◀ prev · Course Map · next ▶), accurate scope badges, `[!syllabus]` map, `[!key]` learning goals |
| **Body** | sequential narrative in teaching order; **section chips**; redundancy between lectures merged |
| **Intuition first** | every non-trivial idea gets an `[!intuition]` box with a concrete analogy *before or right after* the formalism (ice skater, ball in a valley, feedback howl…). If a reader could ask "but why?", there is a box |
| **Depth** | full derivations (no "it can be shown"), each step justified; limits and special cases; orders of magnitude; at least **two worked examples** with numbers (`[!example]`) |
| **Pitfalls** | `[!pitfall]` for the classic mistakes and exam traps |
| **Figures** | at least one generated figure + one diagram/canvas; every figure has a caption stating what to see |
| **Links** | every concept linked on first use; `[!connection]` boxes for other subjects; a **Map of this chapter** callout (builds on · leads to · concepts · cross-subject); concept notes carry a live *Linked from* list |
| **Close** | `[!summary]` cheat-sheet (formulas + one-liners), **Practice** with answers/solutions in a collapsed `[!example]- Solutions`, then **Provenance** with the source map and "dropped as redundant" |
| **Quality gates** | numbers recomputed; `[!verify]` for source disagreements; link check passes (`scripts/check_links.py`) |

**Depth target.** A chapter should be readable on its own by someone who missed the lectures *and* detailed enough to answer a derivation question: ~4,500–7,000 words, 5+ intuition boxes, 2+ worked examples, 6+ practice problems.

## 8. Graph view colours (2026-10-29)
The global graph (`.obsidian/graph.json`) is **generated** by `scripts/graph_colors.py` (`--apply` writes it, no flag only reports coverage, `--validate` measures the palette, `--preview out.png` simulates the layout). Do not hand-edit the colour groups: edit `SUBJECTS` in the script and re-run.

**Rules.** (1) Obsidian paints a node with the **first** colour group that matches, so the groups are *only subjects*; note-type groups (`type/moc`, `type/concept`, `extra`) used to sit above the subjects and repainted every concept note by type, which is why QM, group theory, chemistry and probability looked like one subject. To look at a type temporarily, type it into the graph's search box (`tag:#type/moc`). (2) A subject matches by **folder or `subject/` tag**, so both are kept consistent (audited: 0 mismatches; Bayes' Theorem and AIC carry two subject tags on purpose and take the Probability colour because it precedes Eco-Evo). (3) The other tool's notes (un-numbered folders and `zettel`, found by their course tag) take their course's colour at 45 % opacity; its loose notes are a dim grey. (4) `00-Home` (the Glossary alone links 640 notes), `digests`, `master`, `dailies`, `Assets` and `scripts` are filtered out of the graph because they link to everything; open the *local* graph on them.

| Subject | Colour | Hex | Basis |
|---|---|---|---|
| Climate | blue | `#3987e5` | validated palette slot |
| Thermodynamics | red | `#e66767` | validated |
| Quantum Mechanics | gold | `#c98500` | validated |
| Probability | aqua | `#199e70` | validated |
| Eco-Evo | orange | `#d95926` | validated |
| Group Theory | green | `#008300` | validated |
| Inorganic Chemistry | magenta | `#d55181` | validated |
| Proofs, Analysis, Topology | violet | `#9085e9` | validated |
| Landscapes | purple | `#914cad` | extension hue (farthest-point search) |
| Waves (stub) | cyan | `#37a1b8` | extension hue |
| Neuroscience (stub) | brick | `#a0555c` | extension hue |
| Earth and Life (stub) | orange | `#d95926` | shares Eco-Evo until written |
| Foundations | grey | `#85857f` | neutral on purpose: the toolkit that links every subject |

The eight validated hues are the dataviz reference palette's dark-column steps (they keep at least 3:1 on both Obsidian surfaces); **which hue goes to which subject was optimised on the real link graph**, so the most heavily linked subject pairs get the most separable colours (Climate–Thermodynamics 29, Climate–Eco-Evo 32, Climate–QM 31, Probability–QM 20 normal-vision ΔE; worst heavy pair QM–Thermodynamics 13.0 normal and 6.7 under colour-blind simulation). Eight hues cannot all be pairwise distinct (a limit of the method), so the weakest pairs are placed on subjects that barely link (Eco-Evo–Thermodynamics 3 links, Climate–Analysis 1). Forces: `centerStrength 0.25`, `repelStrength 16`, `linkDistance 110`, thinner lines (`0.6`), unresolved links hidden.

> [!warning] Obsidian rewrites `graph.json` while the graph pane is open
> If the colours revert, Obsidian saved its in-memory copy over the file. Close the graph tab (or run *Reload app without saving*), then `.venv/bin/python -W ignore scripts/graph_colors.py --apply`, then reopen the graph.

### 8b. Graph structure: one centre, then subjects, then everything (2026-10-29)
**User instruction:** the graph "seems very disoriented, make it such that it stems from a single centre in home to all subject maps and then all the other stuff from there".
- **Home is the centre.** The filter (`graph_colors.py` `SEARCH`) now hides the other `00-Home` notes by name (Conventions, Dashboard, Glossary, PROGRESS, Roadmap, Sources, Subject Map, Tag Index, Templates, Toolkit) but **not** `Home.md`, which has its own colour group (`#f4f1de`, near-white: on a light theme change it in `HOME_GROUP`). Home links the 13 subject maps (incl. [[Foundations - Course Map]]).
- **Every subject map is the hub of its cluster.** `scripts/graph_spine.py --apply` writes an **Atlas** block (between `<!-- graph-spine:start -->` and `<!-- graph-spine:end -->`, at the end of each map) that links *every* chapter, concept note, other vault note and source note (the other tool's) of the subject; Home carries an atlas of the 4 loose source notes. Dataview lists do not make graph edges, hence static links. Re-run it after adding notes.
- **Cross-subject chords** are real links: the concept notes' `## Across subjects` sections and the chapters' `Map of this chapter` boxes; `scripts/cross_links.py` holds the curated bridges (each must carry a mathematical or physical identity, not a shared word) and adds a bullet to both notes if they are not already linked; re-running is idempotent.
- **Forces:** repel 20, link distance 100, centre 0.2, link strength 1 (an estimate: a d3-like simulation of the real link graph gives Home within the central 1 % of nodes, subject clusters tighter than their spacing, and 79 % of each node's six nearest neighbours in its own subject, against 61 % before the change; Obsidian itself was not opened).

## 9. Interdisciplinary chapters and concept notes (2026-10-29)
**User instruction:** relate subjects wherever "5–6 concept notes or 1–2 chapters" would make a real bridge; "put such stuff normally" in the subject folders, but a *very interdisciplinary chapter* goes in the subject it leans on most, inside an **`Interdisciplinary/`** subfolder.
- **Where:** `<subject folder>/Interdisciplinary/<code> <title>.md`; concept notes stay in the usual `Concepts/` folder of the subject they belong to.
- **Codes:** `<subject letters>X<n>`: `LSX1` (Landscapes), `THX1` (Thermodynamics). Front matter has `chapter: X1`, `interdisciplinary: [subjects it touches]` and the tag `interdisciplinary`. The first callout explains *why it is interdisciplinary and where it lives*.
- **Written so far:** [[LSX1 Clocks in Rocks]] (decay, Poisson counting, alpha-decay tunnelling, cosmogenic nuclides, closure temperature; A&A Ch. 6) and [[THX1 Diffusion Random Walks and the Heat Equation]] (random walk, Fick/Fourier, kernel, skin depth, Einstein relation, Péclet, Wright–Fisher, free propagator). Numbers: `scripts/interdisc_numbers.py`.
- **Bridges found but not written** (candidates, each with the shared identity): weathering kinetics and the carbon thermostat (Landscapes/Chemistry/Climate; A&A Ch. 7 §"Chemical alteration" and "Long-term carbon cycle"); the logistic/sigmoid function (logistic growth = logistic CDF = Fermi–Dirac = $\tanh$ polarisation); Perron–Frobenius across Leslie matrices, Markov chains and ground states; water waves and the shoaling of coastal waves (Waves, A&A Ch. 16); the Hilbert-space/metric-space completeness bridge (Analysis–QM, partly done by links).
