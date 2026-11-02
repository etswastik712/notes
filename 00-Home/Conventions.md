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

### Zettel notes (the other tool's concept notes), filed 2026-10-30
Kurooto writes one small concept note per idea into `zettel/` (`id: zettel/<slug>`, tags `zettel`, `agent-written`, the source course). **User request 2026-10-30: sort them into the respective vaults.** `scripts/sort_zettel.py --apply` files each note by its course tag into `<subject folder>/Concepts/zettel/` (climate → `01-`, landscape-evolution → `05-`, ph2113 → `06-`, introduction-to-probability → `08-`, mt3184 → `14-` (it was `10-` until 2026-11-02, when the Differential Geometry vault was written), intro-to-proofs → `11-`, ch2113 → `12-`), adds the tag `subject/<x>`, and writes a generated `vault:links` block at the end of the note: `chapter::` (the chapter that covers it), `concept::` (the vault's concept note on the same idea), `related-concept::`, or `map::` when no chapter covers it. The other direction is generated too: every chapter gets a `## Zettel notes` block before `## Provenance`, every concept note one before `## Linked from`.
- **File names and `id:` are unchanged**, so every `[[zettel/<slug>]]` link (the notes' own, and the source layer's) still resolves: Obsidian matches a path link by suffix (`scripts/link_audit.py` checks it).
- **They are agent-written and unreviewed.** Never cite a zettel note in a Provenance table; the sources stay the un-numbered folders. Do not edit between the generated markers; hand decisions on which chapter owns a note live in `OVERRIDES` in the script (the lecture named in the note's `Source:` line is the best guide).
- **Kurooto only scans `zettel/`** (`core/conceptgraph.py: concept_dirs`), so it no longer sees the filed notes: after each ingest run `.venv/bin/python -W ignore scripts/sort_zettel.py --apply`. If Kurooto re-created a slug that is already filed the script prints `DUPLICATE` and leaves the loose copy alone (merge by hand). `scripts/_work/zettel_sort.json` records every old and new path.
- **Without a chapter:** the 22 MT3184 differential-geometry prerequisites (vector fields, flows, rank theorem, submanifolds, Baire) and the 4 Landscapes field-trip safety notes link to their course map. *(Update 2026-11-02: MT3184 now has its own vault, `14-Differential-Geometry`, so none of its 43 notes is without a chapter; they sit under DM02–DM14. `sort_zettel.py --vault 14-Diff` restricts the apply to one vault and `LEGACY_VAULTS` retires the generated zettel blocks left in `10-Group-Theory`.)*

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
| Differential Geometry | teal | `#0b7491` | added 2026-11-02: contrast ≥ 3:1 on both surfaces, min ΔE 13.7 to the others (farthest-point search in OKLab) |
| Earth and Life (stub) | orange | `#d95926` | shares Eco-Evo until written |
| Foundations | grey | `#85857f` | neutral on purpose: the toolkit that links every subject |

The eight validated hues are the dataviz reference palette's dark-column steps (they keep at least 3:1 on both Obsidian surfaces); **which hue goes to which subject was optimised on the real link graph**, so the most heavily linked subject pairs get the most separable colours (Climate–Thermodynamics 29, Climate–Eco-Evo 32, Climate–QM 31, Probability–QM 20 normal-vision ΔE; worst heavy pair QM–Thermodynamics 13.0 normal and 6.7 under colour-blind simulation). Eight hues cannot all be pairwise distinct (a limit of the method), so the weakest pairs are placed on subjects that barely link (Eco-Evo–Thermodynamics 3 links, Climate–Analysis 1). Forces: `centerStrength 0.25`, `repelStrength 16`, `linkDistance 110`, thinner lines (`0.6`), unresolved links hidden.

> [!warning] Obsidian rewrites `graph.json` while the graph pane is open
> If the colours revert, Obsidian saved its in-memory copy over the file. Close the graph tab (or run *Reload app without saving*), then `.venv/bin/python -W ignore scripts/graph_colors.py --apply`, then reopen the graph.

### 8b. Graph structure: one centre, then subjects, then everything (2026-10-29, revised the same day)
**User instruction:** the graph "seems very disoriented, make it such that it stems from a single centre in home to all subject maps and then all the other stuff from there ... make it a bit symmetrical". Second round, after a screenshot of the real graph: "the graph is still disoriented, maybe the links aren't proper".
- **Links audit** (`scripts/link_audit.py`): resolves links **the way Obsidian does** (file name or path, never frontmatter aliases) and `--fix` repairs the vault's own notes. It found 16 alias-only links (unresolved in Obsidian, hence invisible in the graph because `hideUnresolved` is on) and 20 bare names that also match a source note of the same name (e.g. `[[Variance]]` could resolve to `zettel/variance.md`); both are now written as `[[File|alias]]` / `[[folder/File|name]]`. All 13,916 vault links resolve. `scripts/check_links.py` still counts aliases as valid, so **run `link_audit.py` as well**. The Glossary builder now path-qualifies ambiguous names.
- **Home is the centre.** The filter (`graph_colors.py` `SEARCH_BASE`) hides the other `00-Home` notes by name but **not** `Home.md`, which has its own colour group (`#f4f1de`). Home links the 13 subject maps and, through a generated *All chapters* index, **every chapter** (108): the best-connected node, so the largest.
- **Every subject map is the hub of its cluster.** `scripts/graph_spine.py --apply` writes an **Atlas** block (markers `graph-spine:start/end`, end of each map) linking every chapter, concept note, other vault note and source note of the subject, and the chapter index on Home (markers `graph-spine-chapters`). Dataview lists make no graph edges, hence static links. Re-run it after adding notes.
- **The other tool's source notes are hidden by default** (`SOURCE_FOLDERS`: ph2113, ch2113-..., mt3184-..., intro-to-proofs, introduction-to-probability, introduction-to-climate-science, landscape-evolution, zettel, maps, inbox). They are ~40 % of the nodes, hang off their subject only through the atlas, and in the real screenshot formed long stalks and blobs far from the structure. `graph_colors.py --apply --with-sources` brings them back (dimmed, in their subject's colour); the links stay in the atlases either way (backlinks, local graph).
- **Cross-subject chords** are real links and are kept: concept notes' `## Across subjects` sections, chapters' `Map of this chapter` boxes; `scripts/cross_links.py` holds the curated bridges (each must carry a mathematical or physical identity); idempotent.
- **How it was tested** (`scripts/graph_sim.py`, a d3-force-style layout of the real link graph with strict link resolution and the real filter, calibrated by eye against the real screenshot: link strength 1/min(degree), charge $-400$, centre 0.03 reproduces its stalks and central tangle). Metrics on the final vault: Home in the central 1 % of nodes; spacing of the subject lobes around Home and tightness within a lobe improved against the previous structure (numbers in PROGRESS). Findings worth knowing: (i) the flat atlas beats a "tidy" chapter-parent hierarchy; (ii) Home to every chapter evens out the angular spacing; (iii) a rim of map-to-map links does nothing (d3's link strength is tiny between two hubs); (iv) the force sliders barely matter compared with the structure; (v) 25 % of the vault's links are cross-subject, which is what stops the layout being a perfect flower; with them all removed the simulator gives purity 0.99. **Not verified in Obsidian itself** (no screenshot of the new graph yet; Obsidian's force constants are unpublished).
- **Still asymmetric by content:** Waves, Neuroscience and Earth-and-life are single stub notes and sit in the middle with Foundations; they will take their place on the ring when written.

## 9. Interdisciplinary chapters and concept notes (2026-10-29)
**User instruction:** relate subjects wherever "5–6 concept notes or 1–2 chapters" would make a real bridge; "put such stuff normally" in the subject folders, but a *very interdisciplinary chapter* goes in the subject it leans on most, inside an **`Interdisciplinary/`** subfolder.
- **Where:** `<subject folder>/Interdisciplinary/<code> <title>.md`; concept notes stay in the usual `Concepts/` folder of the subject they belong to.
- **Codes:** `<subject letters>X<n>`: `LSX1` (Landscapes), `THX1` (Thermodynamics). Front matter has `chapter: X1`, `interdisciplinary: [subjects it touches]` and the tag `interdisciplinary`. The first callout explains *why it is interdisciplinary and where it lives*.
- **Written so far:** [[LSX1 Clocks in Rocks]] (decay, Poisson counting, alpha-decay tunnelling, cosmogenic nuclides, closure temperature; A&A Ch. 6) and [[THX1 Diffusion Random Walks and the Heat Equation]] (random walk, Fick/Fourier, kernel, skin depth, Einstein relation, Péclet, Wright–Fisher, free propagator). Numbers: `scripts/interdisc_numbers.py`.
- **Bridges found but not written** (candidates, each with the shared identity): weathering kinetics and the carbon thermostat (Landscapes/Chemistry/Climate; A&A Ch. 7 §"Chemical alteration" and "Long-term carbon cycle"); the logistic/sigmoid function (logistic growth = logistic CDF = Fermi–Dirac = $\tanh$ polarisation); Perron–Frobenius across Leslie matrices, Markov chains and ground states; water waves and the shoaling of coastal waves (Waves, A&A Ch. 16); the Hilbert-space/metric-space completeness bridge (Analysis–QM, partly done by links).

## 10. The book library (2026-10-29)
**Scheme (unchanged, extended):** `<subject>/<topic>/books/` in the un-numbered source tree (physics, math, chemistry, biology, earth-and-climate); course material in `<subject>/<topic>/lecture-notes-slides/`. Topics that are vault subjects keep their folder (`physics/quantum-mechanics`, `physics/thermodynamics-stat-mech`, `physics/waves`, `math/group-theory`, `math/probability`, `math/proofs-analysis-topology`); the other topics are named after the user's own Drive folders (kebab-case), e.g. `math/differential-geometry`, `math/functional-analysis`, `physics/quantum-field-theory`, `physics/relativity`, `physics/nonlinear-dynamics`.
- **Source of this batch:** 21 Google-Drive zips from Downloads (the big `Mathematics` and `Physics` zips are the parent libraries, the others partial copies) plus the loose books in Downloads: 758 files, 4.8 GiB, filed by `scripts/organise_books.py` (re-run it for the next batch: `--plan` first). The Elementary/Intermediate/Advanced levels of the user's maths library are merged into one topic folder and kept in `Assets/data/books-manifest.csv` (file, size, origin zip, level, path in the origin).
- **Judgement calls** (all in `PER_FILE` of the script, easy to change): Lie groups/algebras, representation theory and reflection groups go to `math/group-theory`; Real Analysis, Point-Set Topology, Foundations and Bridge reading go to `math/proofs-analysis-topology`; Landau–Lifshitz is split by topic (Vol. 2 to electromagnetism, Vol. 4 to QFT, Vols. 6–7 to `continuum-mechanics`) while Feynman stays together in `general-physics`; "Nonlinear Dynamics" is filed under physics (it came with IISER's PHY342 notes, now `physics/nonlinear-dynamics/lecture-notes-slides/Santhanam Notes`); a companion's own sub-folders (Sakurai's instructor resources, Hartle's Mathematica notebooks, the Shankar solutions manual) stay intact under the book's topic.
- **Duplicates:** identical files (sha256) are filed once, including against the 41 books already in the repo; 23 were dropped. Different scans, editions or formats of one book (pdf and djvu) are all kept.
- **Git:** the vault is committed **and pushed to GitHub automatically by Kurooto**, so the new library is kept out of git by `.gitignore` (`<area>/*/books/`). Books tracked before today stay tracked. `git add -f <file>` tracks one; deleting the lines tracks all of them (about 8 GB: not recommended without LFS thought).
