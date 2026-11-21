---
title: Toolkit
tags: [meta, type/meta]
---
# Toolkit

Everything installed or scripted for this vault, and how to use it.

## 1. Obsidian plugins
Installed from `~/Documents/Landlab-SSIIM-Vault/.obsidian/plugins` into `.obsidian/plugins/` (25 folders, with their saved settings); the same 23 are enabled in `community-plugins.json`. In Obsidian: *Settings → Community plugins → turn off Restricted mode*; they load from disk, no download needed. `card-note` and `just-simple-excalidraw` are installed but disabled, as in the source vault.

| Group | Plugins | Use here |
|---|---|---|
| **Math** | Latex Suite, Latex Environments, Fix Math, Math+ | fast LaTeX typing; `Fix Math` converts `\( \)`-style equations pasted from AI output into `$…$` |
| **Data** | Dataview | [[Dashboard]], status lists, tag counts |
| **Excalidraw** | Excalidraw (core), Excalidraw Extras, Mind Map, Plotter, Mirror, PureRef, Stylus Menu, Excalink, Drawculator, Merefolk, ExcaliBrain, Insert Image Plus | sketches in `Assets/excalidraw/`; **ExcaliBrain** gives an editable graph view; **Plotter** plots functions on a drawing |
| **Canvas** | Canvas Export, CanvasPort, Canvas Draw, CardNote (off) | export canvases to HTML/PDF/Excalidraw; see §3 |
| **Other** | Tech Tree Companion, Triggers, Virtual Pen Cursor | dependency trees; automation |

Core plugins on: file explorer, search, graph, backlinks, outgoing links, tags, properties, canvas, templates, bookmarks, outline, page preview, **bases**, sync. The CSS snippet `second-brain.css` is enabled and styles the callouts.

> [!warning] Git
> `.obsidian/plugins/` is excluded in `.gitignore` (≈50 MB of binaries). To restore on another machine run `scripts/install_plugins.sh` (copies from the Landlab vault) or reinstall from Obsidian.
>
> **New machine (added 2026-11-21):** download `setup_vault.sh` (Linux/macOS) or `setup_vault.ps1` (Windows) from the GitHub release **vault-setup** of `etswastik712/notes` and run it: it clones or updates the vault, installs the plugins from the release's `obsidian-plugins.tar.gz`/`.zip`, builds `.venv` from `requirements.txt`, and lists the manual steps (books, Classroom login). Re-run to update.

## 2. Writing notes
- **Templates:** [[Chapter Template]], [[Concept Template]], [[Course Map Template]] in `00-Home/Templates/` (insert with the core Templates command).
- **Callouts:** `key`, `derivation`, `intuition`, `example`, `pitfall`, `connection`, `verify`, `provenance`, and the scope callouts `taught`, `extra-book`, `extra-beyond` ([[Conventions]]).
- **Math:** MathJax: `$…$`, `$$…$$`, `\begin{aligned}`; `\boxed{}`; `\tag{…}`.
- **Link a PDF page:** `[[file.pdf#page=12|label]]`; **embed** one: `![[file.pdf#page=12&height=400]]`.
- **Tags:** frontmatter `tags:` lists (no `#`); search `tag:#extra/book`.

## 3. Generating material (run from the vault root)
```bash
.venv/bin/python -W ignore scripts/make_figures.py            # all fig_*.py  -> Assets/figures/*.png
.venv/bin/python -W ignore scripts/make_figures.py cl04       # only matching scripts
.venv/bin/python -W ignore scripts/diagrams.py                # Excalidraw + SVG diagrams (specs inside)
.venv/bin/python -W ignore scripts/build_canvases.py          # Subject Map (canvas + note) and Climate canvas
.venv/bin/python -W ignore scripts/contact_sheet.py in.pdf out_prefix 5 3 480   # triage a PDF of page images
.venv/bin/python -W ignore scripts/build_interactive.py [--only id1,id2] [--no-shots] [--sheet N]  # interactive tools: scripts/interactive/tools/*.js -> Assets/interactive/*.html + previews (syntax check + headless-Firefox PNGs)
.venv/bin/python -W ignore scripts/embed_interactive.py [--dry]   # put the Interactive callouts into the chapters and regenerate [[Interactive Tools]] (hub + coverage table)
cd Assets/latex && latexmk -pdf -outdir=build <name>.tex && cp build/<name>.pdf ../pdf/
```
| Script | Purpose |
|---|---|
| `scripts/figlib.py` | shared matplotlib style, constants, `save()`, palette |
| `scripts/fig_<chapter>_<slug>.py` | one script per figure; the numbers printed by each are the ones quoted in the notes |
| `scripts/diagrams.py` | node-and-arrow diagrams → `.excalidraw.md` **and** `.svg` (the SVG is embedded; the Excalidraw file is the editable source) |
| `scripts/build_canvases.py` | JSON Canvas files from tables; edit `SUBJECTS`/`RELATIONS`/`CH` |
| `scripts/graph_colors.py` | **graph-view colour groups, filter and forces** → `.obsidian/graph.json` (one colour per subject; see [[Conventions]] §8) |
| `scripts/graph_spine.py` | **Atlas blocks**: links every note of a subject from its map (Home → maps → everything); `--apply` rewrites the blocks ([[Conventions]] §8b) |
| `scripts/link_audit.py` | **strict (Obsidian-faithful) link audit**: counts alias-only and ambiguous links that `check_links.py` accepts; `--fix` rewrites them in the vault's own notes |
| `scripts/pa_numbers2.py`, `scripts/fig_pa08_induction2.py`, `fig_pa09_strong.py`, `fig_pa10_wellorder.py` | every number and the 3 figures of PA08–PA10 (induction identities, Moser, $n^2+n+41$, tromino tiling, Hanoi BFS, postage, Zeckendorf, Josephus, Catalan, Euler's cubic, lexicographic order, Ackermann), each recomputed |
| `scripts/pr_numbers2.py`, `scripts/fig_pr07_sums.py` | numbers of PR07 and the PR05 Quiz 1 items (convolution of normals incl. the symbolic completed square, $E|X-Y|$, covariance quadratic form, $|\rho|\le1$, practice answers) |
| `scripts/organise_books.py` | **files books** from Downloads/zips into `<subject>/<topic>/books/` (hash-deduplicated, manifest in `Assets/data/books-manifest.csv`; `--plan` then `--apply`; [[Conventions]] §10) |
| `scripts/graph_sim.py` | **graph simulator**: builds the link graph as Obsidian draws it (real filter, strict resolution) and runs a d3-style layout, metrics and a PNG (`--png`); output to the git-ignored `scripts/_work/` |
| `scripts/ls_hydro_coast_numbers.py`, `scripts/fig_ls_hydro_coast.py` | every number and the 7 figures of LS25-LS27 (A&A Ch. 11 and 16), each cross-checked (Monte Carlo, quadrature, finite differences, pseudo-spectral, ODE solver) |
| `scripts/cross_links.py` | **curated cross-subject bridges** → an `## Across subjects` bullet on both notes (idempotent; `--apply`) |
| `scripts/ls_rivers_numbers.py`, `scripts/fig_ls_rivers.py` | every number and the 8 figures of LS21–LS24 (A&A Ch. 12–14), each cross-checked (quadrature, finite differences, ODE) |
| `scripts/interdisc_numbers.py` | numbers and Monte Carlo/finite-difference checks for LSX1 (decay, Gamow half-lives, cosmogenic, Dodson) and THX1 (random walk, kernels, skin depth, Wright–Fisher) |
| `scripts/ls_rigour_numbers.py` | numbers of the LS14 rigour layer (plastic and Vialov ice-sheet profiles, abrasion) |
| `scripts/contact_sheet.py` | numbered thumbnail sheets for reading image-only PDFs |
| `Assets/latex/preamble-brain.tex` | shared LaTeX preamble: tcolorbox boxes that mirror the callouts, siunitx, pgfplots, TikZ |

## 4. LaTeX and PDFs
Handouts are LaTeX (full TeX Live is installed: tcolorbox, pgfplots, siunitx, mhchem, tikz-3dplot, physics…). Compiled PDFs live in `Assets/pdf/` and are embedded in notes. Current handouts: [[climate-part1-energy-balance-handout.pdf]] and [[climate-rotating-frames-handout.pdf]].

![[climate-part1-energy-balance-handout.pdf#page=1&height=420]]

## 5. Dataview patterns
```dataview
TABLE WITHOUT ID file.link AS "Note", scope AS "Scope", status AS "Status"
FROM #subject/climate AND #type/chapter
SORT chapter ASC
```
```dataview
LIST FROM #extra/beyond AND #subject/climate
```
Property names are single words (`chapter`, `scope`, `by`, `status`) so queries need no quoting.

## 6. Checks
- **Link check:** `scripts/check_links.py` reports unresolved `[[wikilinks]]` and missing embeds (run it before ending a session).
- **Figure numbers:** every figure script prints its key numbers; compare with the note text after any change.

## 7. Web and sources
Search and fetch are used for academic/government/Wikipedia pages only; every external fact is cited at the bottom of its note and listed in [[Sources]].
