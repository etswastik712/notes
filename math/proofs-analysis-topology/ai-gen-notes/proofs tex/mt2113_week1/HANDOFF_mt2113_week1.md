# MT2113 Week 1 (post mid-term) — LaTeX notes: HANDOFF / MEMORY FILE

Purpose: if the chat session ends before the notes are finished, paste this file into a new chat
(together with `week1_mt2113.pdf` and `probability_notes.pdf`) and say "continue from the handoff file".

Note: Claude could only write inside `~/Downloads/proofs tex/` and `~/Downloads/eco-evo prems/`
(not the Desktop), so this file lives in `~/Downloads/proofs tex/mt2113_week1/`. Move it wherever you like.

## 1. The task (as the user stated it)
- Input 1: `week1_mt2113.pdf` = 9 handwritten pages (Xournal++). Pages 1-2 = homework Q1-Q6; pages 3-9 = lecture notes
  (continuous RVs, pdf, Uniform, Logistic, Rayleigh, cdf, expectation, LOTUS, variance, Standard Normal, N(mu, sigma)).
- Input 2: `probability_notes.pdf` = template (38 pages, "Rigorous Study Notes: Combinatorics and Probability Theory").
  Style: notation key, theorem/proof style, boxed Intuition paragraphs, comparison tables, red = beyond-syllabus material, appendix master table.
- Output: LaTeX notes for the handwritten material in EXACTLY the template's style. Detailed but to the point,
  structurally continuous, intuition where required, nothing from the handwritten notes missed, homework solved at the end.
- Deliver BOTH `.tex` and `.pdf`.

## 2. Decisions the user confirmed
1. Structure: CONTINUE the template numbering after Section 8 (Continuous RVs) -> new sections start at Section 9
   (one-line change: `\setcounter{section}{8}` in the preamble).
2. Go beyond the handwritten notes with adjacent extra material (decently deep, not too much).
   Every extra piece must be FLAGGED as either "completely extra" or "used in question X".
3. Add summaries, comparison tables and similar reading aids wherever applicable (chapter summaries, key-formula boxes, tables).
4. Save in `proofs tex/mt2113_week1/`.

## 3. Planned outline (status column to be updated)
| Sec | Title | Source | Status |
|-----|-------|--------|--------|
| 9  | Notation and terminology additions + how to read tags ([Extra], [Used in Qx]) | new | todo |
| 10 | Densities and CDFs (heuristic, def, requirements, P[X=x]=0, F'=f) | notes p.3-4 | todo |
| 11 | Catalogue: Uniform, Logistic, Rayleigh (+ Exponential, Gumbel as flagged extras) + comparison table | notes p.3-4 + extras | todo |
| 12 | Expectation of continuous RVs (Uniform, Logistic, Rayleigh) | notes p.5 | todo |
| 13 | Tail-integral lemma and LOTUS (proof for g>=0) | notes p.6-7 | todo |
| 14 | Variance (+ Uniform variance) | notes p.7-8 | todo |
| 15 | Normal distribution (Gaussian integral, N(0,1), N(mu,sigma), inflection points) | notes p.8-9 | todo |
| 16 | Extras: cdf method for transforming RVs, quantiles, probability integral transform, memorylessness, convergence in distribution | extras | todo |
| 17 | Worked solutions: homework Q1-Q6 | HW p.1-2 | todo |
| 18 | Worked solutions: 3 extra questions | user | todo |
| App | Master comparison table (continuous distributions) + key-formula sheet | new | todo |

## 4. Homework (handwritten pages 1-2), transcribed
- Q1) Rayleigh pdf f(x) = x e^{-x^2/2} (x>0), else 0. (a) P(1<X<3). (b) first quartile, median, third quartile q_i with P(X<=q_i)=i/4.
- Q2) Circle with random radius R ~ Unif(0,1), A = area. (a) mean and variance of A WITHOUT first finding cdf/pdf of A. (b) cdf and pdf of A.
- Q3) Stick of length 1 broken at U ~ Unif(0,1). p a fixed point on the stick. X = length of the piece containing p. Find E(X); for which p is it maximal?
- Q4) Z ~ N(0,1), c in (0, inf). Find E(max{Z-c, 0}).
- Q5) Inflection points of phi(x) = e^{-x^2/2}/sqrt(2 pi). For N(mu, sigma) show pdf = (1/sigma) phi((x-mu)/sigma); find its inflection points.
- Q6*) (a) For any RV Y: E(Y) = int_0^inf P(Y>y) dy - int_0^inf P(Y<-y) dy. (b) Prove LOTUS for any g, using (a).

## 5. Extra questions from the user
- E1) Repair time ~ Exponential(lambda = 1/2) hours. (a) P(repair > 2h). (b) P(repair >= 10h | repair > 9h).
- E2) Gumbel = distribution of -log X, X ~ Expo(1). (a) its CDF. (b) X_1..X_n iid Expo(1), M_n = max. Show M_n - log n -> Gumbel in distribution.
- E3) X continuous with cdf F. Find E[F(X)] (i) without LOTUS and (ii) with LOTUS.

## 6. Worked answers (already derived; double-check when typesetting)
- Q1a) F(x) = 1 - e^{-x^2/2}. P(1<X<3) = e^{-1/2} - e^{-9/2} ~ 0.5954.
- Q1b) q_i = sqrt(2 ln(4/(4-i))): q1 = sqrt(2 ln(4/3)) ~ 0.7585, median = sqrt(2 ln 2) ~ 1.1774, q3 = sqrt(4 ln 2) = 2 sqrt(ln 2) ~ 1.6651.
- Q2a) E[A] = pi E[R^2] = pi/3. E[A^2] = pi^2 E[R^4] = pi^2/5. Var(A) = pi^2(1/5 - 1/9) = 4 pi^2/45.
- Q2b) F_A(a) = sqrt(a/pi) on [0,pi] (0 below, 1 above). f_A(a) = 1/(2 sqrt(pi a)) on (0,pi). Check: mean = pi/3.
- Q3) U<p: piece containing p is [U,1], length 1-U. U>p: [0,U], length U. E[X] = 1/2 + p(1-p). Max at p = 1/2, value 3/4.
- Q4) E[max(Z-c,0)] = phi(c) - c (1 - Phi(c)). (int_c^inf z phi(z) dz = phi(c) since phi' = -z phi.) Check c=0: 1/sqrt(2 pi).
- Q5) phi' = -x phi, phi'' = (x^2-1) phi. Inflection points x = +-1, i.e. (+-1, e^{-1/2}/sqrt(2 pi)). For N(mu,sigma): cdf method then chain rule; inflection at mu +- sigma, height phi(1)/sigma.
- Q6a) Y = Y+ - Y-. P(Y+>y) = P(Y>y), P(Y->y) = P(Y<-y) for y>=0. Use E[Z] = int_0^inf P(Z>y) dy for Z>=0 (prove via indicator + Tonelli so atoms at 0 are allowed; the pdf-based lemma on p.6 of the notes needs a density).
- Q6b) E[g(X)] = int_{g>0} g f - int_{g<0} (-g) f = int g f, by swapping integrals for each part (needs E|g(X)| < inf).
- E1) rate lambda = 1/2 (mean 2 h): (a) e^{-1} ~ 0.3679. (b) e^{-1/2} ~ 0.6065 (memorylessness: = P(T>1)). [If lambda meant the MEAN 1/2: (a) e^{-4}, (b) e^{-2}.]
- E2a) G(x) = exp(-e^{-x}), x in R.
- E2b) P(M_n - log n <= x) = (1 - e^{-x}/n)^n -> exp(-e^{-x}) for every fixed x. G is continuous everywhere so convergence at all x = convergence in distribution.
- E3) F(X) ~ Unif(0,1) (proof via x_u = sup{x: F(x)<=u}, F(x_u)=u, {F(X)<=u} = {X<=x_u}) so E = 1/2.
      With LOTUS: int F f dx = int F F' dx = [F^2/2] = 1/2.  (Extra remark: also = P(X' <= X) = 1/2 for iid copy X'.)

## 7. LaTeX build notes
- Toolchain on Claude's side: pdflatex / xelatex / latexmk (TeX Live 2023) with amsmath, tcolorbox, booktabs, xcolor, hyperref, mdframed, tikz, pgfplots.
- Template: US letter, Latin Modern fonts, theorem counter shared per section (Proposition 2.1, 2.2, Theorem 2.3 ...).
- Main file: `mt2113_week1_notes.tex` (single file). Compile twice for the table of contents.
- Limitation: Claude's file tool can only write TEXT into this folder, so the compiled PDF is delivered as a chat download;
  compile locally with `pdflatex mt2113_week1_notes.tex` (twice) to regenerate it here.

## 8. Progress log
- [session 1] Read all 9 pages, answered 3 setup questions, created this folder and this handoff file. Next: build the .tex.
