---
title: EE02 Structured Population Models
aliases: [EE02, Structured populations, Stage-structured dynamics, Leslie matrix, BI2113 lecture 2]
subject: eco-evo
type: chapter
chapter: 2
part: I
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE01 Introduction to Biology and Ecological Thinking]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/paper, src/own-notes, status/draft]
---
# EE02 · Structured Population Models

◀ [[EE01 Introduction to Biology and Ecological Thinking]] · [[Ecology and Evolution - Course Map|Course Map]] · [[EE03 Population Dynamics and Chaos]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture of 11 Aug 2026 ([[02_StageStructuredDynamics_11-Aug-2026.pdf|31 slides]]) **and** the mandatory reading, Molles §10.3–10.4 ([[Section 10.3-10.4_Manuel Molles_9Ed.pdf|pp. 224–231]]) and Ch. 11 ([[Ch 11_Ecology _ concepts & applications_9Ed_2022_Molles.pdf|pp. 237–253]])
> - §1 what ecology asks; why populations; distribution, demography, dynamics (sl. 1–8)
> - §2 cohort life tables, the *Phlox* table, $R_0$ (sl. 9–10; Molles 10.3)
> - §3 survivorship curves, Types I–III, why the axis is logarithmic (sl. 11–13; Molles 10.3)
> - §4 age-structured dynamics: the Leslie matrix, stable age distribution, $\lambda$, Perron-Frobenius (sl. 14–21)
> - §5 stage-structured dynamics: the loggerhead turtle, sensitivity, turtle excluder devices (sl. 22–28)
> - §6 age distributions and pyramids; human demography (sl. 29; Molles 10.4 and 11.4)
> - §7 the pedagogical note and what the readings cover (sl. 30–31)
>
> 🟡 **Extra · book** (papers and self-study readings; the instructor gives papers no exam weight)
> - §5 Crowder et al. 1994 (paper): the model, its tables, the TED scenarios and the transient "waves"
> - §4–5 Caswell 1997 (paper, a methods chapter): irreducible and primitive matrices, ergodicity, sensitivity and elasticity
> - §1 self-study items of slide 3: temperature (Begon and Townsend) and biogeochemical cycles (Spellman)
> - §6 UN *World Population Prospects 2024* key messages; the *Data for India* article
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §2 generation time and Euler-Lotka; §4 the discrete Euler-Lotka derivation and the damping ratio
> - §5 the elasticity table, stage duration to $P$ and $G$, my reproduction of Crowder's figures
> - §6 replacement fertility from $R_0$; a population-momentum example

> [!key] After this chapter you can
> - build a **cohort life table**, compute $l_x$ and the net reproductive rate $R_0=\sum l_xm_x$, and say what $R_0>1$ means,
> - draw the three **survivorship curves** and explain why survivorship is plotted on a log axis,
> - write down a **Leslie matrix**, iterate it by hand, and state what the **stable age distribution** and the **dominant eigenvalue** $\lambda$ are,
> - build a **stage-structured matrix** from stage durations and survival, and use **sensitivity or elasticity** to decide *where* conservation should act,
> - retell the loggerhead turtle case (why egg protection fails, why turtle excluder devices work, why recovery is slow),
> - read an **age pyramid** and relate its base to $\lambda$.

## 1. What ecology asks, and why start with populations
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=1|slides 1–8]]*

The word **ecology** was coined by Ernst Haeckel in 1866 from two Greek words, *oikos* (house, environment) and *logia* (study of). The deck defines it as the study of *interactions among organisms and their biophysical environments (biotic and abiotic) and how that leads to their distribution and abundance patterns* ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=2|slide 2]]). Slide 4 repeats the **domain of BI2113** from EE01 ([[Levels of Biological Organisation]]): the individual and everything above it, with the levels from population to biosphere "changing" on ecological time scales and microevolution, speciation and macroevolution on longer ones. This lecture zooms in on one rung of that ladder, the **population**.

Slide 5 gives an *anthropocentric* reason to study populations (a short film on UN demographic projections; the slide notes that the 2019 data leave the predictions largely unchanged) and slide 6 notes that **human demography** is conceptually a subset of **population ecology**. Slide 7 supplies the definition and the agenda:

> [!key] Population, and what population ecologists study
> A **population** is a group of similar individuals inhabiting a defined space at a given time. For non-human populations the reasons to study them are **conservation** of endangered species, **management** of economically important species (agriculture, fisheries), management of harmful species (pests, invaders), and the fact that the population is the **fundamental unit of evolution**.
> Population ecologists study **distribution** (how individuals are spread over space), **demography** (age structure, survivorship, birth rate) and **dynamics** (how numbers change in time and space). *Population dynamics* is the study of **how and why** numbers change ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=8|slide 8]]).

> [!intuition] A population is a ledger
> Every individual that is alive now was born, immigrated, or both; every one that vanishes died or emigrated. A population is the running balance of those entries. The whole of population ecology can be seen as asking how the entries depend on *who* the individuals are (their age, their stage), on *how many* there are, and on *what else* is around.

The ledger has one line of algebra, which EE03 will use:

$$N_{t+1}=N_t+B-D+I-E,$$

births, deaths, immigration and emigration in one time step ([[Population Ecology]]). If the per-capita rates are the same for every individual and do not depend on $N$, the population grows geometrically ([[Exponential Growth]]). This lecture asks the *prior* question: what if **individuals are not interchangeable**, so that an infant, a breeder and an old animal have different survival and fecundity? That is **population structure**, and the answer is a matrix.

> [!connection] Why age and stage matter for management
> A conservation plan has to say *which* animals to protect. If every individual counted the same, one number $r$ would be enough; with structure, protecting the wrong class can be wasted effort. The loggerhead case in §5 is the standard example.

> [!extra-book]- 🟡 Extra (self-study, slide 3): temperature and biogeochemical cycles
> Slide 3 lists two **self-study** topics. They are not developed in the lecture, so they are kept short here.
> **Effects of temperature** (Begon and Townsend, §2.3.1–2.3.4, [[Reading on Temperature_From Begon_Harper_Townsend.pdf|reading]]): 'extreme' is relative to the organism (a desert is not extreme to a cactus); biological rates respond roughly exponentially to temperature, a rise of 10 °C often about doubling enzymatic rates ($Q_{10}\approx2$); in an effectively linear range development is summarised by **day-degrees** (e.g. the predatory mite *Amblyseius californicus* needs about 123.5 day-degrees above a 9.9 °C threshold: $24.22\ \text{d}\times5.1=8.18\ \text{d}\times15.1$); the **temperature-size rule** (final size falls with rearing temperature; about 2.5 % in cell volume per °C in protists); ectotherms versus endotherms (low cost, low benefit versus high cost, high benefit); and life at low temperatures (chilling injury, freezing, freeze avoidance and tolerance, acclimatisation).
> **Biogeochemical cycles** (Spellman 2008, Ch. 2, [[Ch2_Ecology for Non-ecologists.pdf|reading]]): energy flows through ecosystems but **matter cycles**; each cycle has **reservoirs** (pools) and **fluxes**; cycles are *gaseous* (carbon, nitrogen; main pool atmosphere and ocean) or *sedimentary* (phosphorus, sulfur; main pool soil and rock); the chapter treats water, carbon, nitrogen, phosphorus and sulfur. Chemistry side: [[Inorganic Chemistry - Course Map]]; the phosphorus cycle returns in [[EE06 Eutrophication and Alternative Stable States]].

## 2. Documenting change: the cohort life table
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=9|slides 9–10]] · Molles §10.3*

Slide 9 shows *Phlox drummondii* (an annual plant) and asks: *if you wish to document how the numbers changed over time, how would you go about it?* The answer is to follow a **cohort**, a group born in the same period, from birth to death and record who survives and how many offspring they make. Molles ([[Section 10.3-10.4_Manuel Molles_9Ed.pdf#page=1|p. 224, "Estimating patterns of survival"]]) lists three ways to obtain survival data:

1. **Cohort life table**: follow a cohort to the last death. Most reliable, but impractical for long-lived or mobile species.
2. **Static life table**: record the *age at death* of many individuals born at different times (Murie's Dall sheep, from 608 skulls aged by horn rings and tooth wear). It assumes the age distribution of deaths represents survival.
3. **From an age distribution**: take the differences between successive age classes. It assumes the population is neither growing nor declining, and closed to migration; those assumptions are often false, so this is the least accurate.

![[02_StageStructuredDynamics_11-Aug-2026.pdf#page=10&height=330]]
*The Phlox table of slide 10 (data of Leverich and Levin 1979).*

### 2.1 The table and its columns
The *Phlox* cohort started with 996 individuals ([[Cohort Life Table]]). For each age class $x$:

| symbol | meaning | in the slide |
|---|---|---|
| $n_x$ | number alive at the start of the class | 996, 158, 154, … |
| $l_x=n_x/n_0$ | proportion surviving to class $x$ | 1.0000, 0.1586, … |
| $m_x$ | mean seeds per survivor in the class | 0, 0.3352, 0.7963, … |
| $l_xm_x$ | expected seeds *per newborn* from the class | 0, 0.0532, 0.1231, … |

The first class lumps the first 299 days (dormant seed, germination, vegetative growth, Molles Fig. 10.15); from day 299 the plants are censused weekly (299–306, 306–313, …, 355–362 days) because flowering and seed set, and the end of life, all happen in those last eight weeks.

> [!key] Net reproductive rate
> $$R_0=\sum_x l_x\,m_x$$ is the mean number of offspring a newborn produces over its whole life ([[Net Reproductive Rate]]). If $R_0>1$ each generation is larger than the last; if $R_0<1$ it shrinks. The slide gives $R_0=2.4177$.

> [!example] Worked example 1: recomputing $R_0$ from the table
> Multiply the $l_x$ and $m_x$ columns class by class: $0,\ 0.0532,\ 0.1231,\ 0.3638,\ 0.4589,\ 0.3469,\ 0.3330,\ 0.6436,\ 0.0952,\ 0$. Their sum is $2.4176$ from the rounded printed values (the slide prints 2.4177, computed from unrounded data). Three readings of the numbers:
> - **Survival is front-loaded and back-loaded.** $1-0.1586=84\,\%$ of the seeds die before day 299; the next four classes lose only 22 of the 158 survivors (2 % of the original seeds); then losses accelerate (the last two classes lose $70\,\%$ and $100\,\%$ of survivors).
> - **Reproduction is concentrated.** The single class 341–348 days has $l_xm_x=0.6436$, $27\,\%$ of $R_0$, because few plants are left (7.4 %) but each makes 8.7 seeds.
> - **$R_0\approx2.4$.** An average seed leaves 2.4 seeds behind, so the population multiplies by about 2.4 per year.

> [!pitfall] $R_0$ is a per-generation factor, not (in general) the growth rate per year
> For an **annual plant** with non-overlapping generations, each generation is one year and the growth factor per year is $\lambda=R_0=2.4177$, which is what Molles uses ([[Ch 11_Ecology _ concepts & applications_9Ed_2022_Molles.pdf#page=2|p. 238]]). When generations overlap, $R_0$ and the yearly growth factor differ and the right one is $\lambda$ from §4 (they still agree on the *threshold*: $\lambda>1$ exactly when $R_0>1$).

> [!extra-beyond]- 🔵 Extra (beyond): generation time and the growth rate per day
> The mean age at reproduction is the **generation time** $T=\sum_x x\,l_xm_x/R_0$. With class mid-points in days, $T\approx331$ d, so $r\approx\ln R_0/T=\ln2.4177/331=0.0027\ \text{d}^{-1}$. The exact rate solves the **Euler-Lotka equation** $\sum_x e^{-rx}l_xm_x=1$, which gives the same $r=0.00267\ \text{d}^{-1}$ here (`scripts/ee02_numbers.py`). Per 365 days that is a factor $e^{0.00267\times365}=2.65$.

> [!example] Worked example 2: how long can $\lambda=2.4177$ last? (Molles §11.1)
> Geometric growth with non-overlapping generations is $N_t=N_0\lambda^t$ ([[Ch 11_Ecology _ concepts & applications_9Ed_2022_Molles.pdf#page=3|Molles pp. 238–240]]). Starting from the 996 plants:
>
> | year $t$ | 1 | 2 | 3 | 8 | 16 | 32 |
> |---|---|---|---|---|---|---|
> | $N_t$ | 2,408 | 5,822 | 14,076 | $1.16\times10^{6}$ | $1.36\times10^{9}$ | $1.85\times10^{15}$ |
>
> Spread evenly over North America (about $24\times10^{6}$ km²) the 32-year figure is about 77 plants per square metre, and 8 years later about 90,000 per square metre. The exercise is absurd on purpose: **natural populations have a tremendous capacity for increase, and unlimited growth cannot be maintained for many generations**. Something must change as $N$ grows (density dependence, EE03).

## 3. Survivorship curves
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=11|slides 11–13]] · Molles §10.3*

A **survivorship curve** plots the number (or proportion) surviving against age, usually with a **logarithmic** vertical axis ([[Survivorship Curve]]). Slide 11 shows the *Phlox* curve next to the three idealised curves.

![[fig_ee02_survivorship.png|760]]
*Figure EE2.1. A: the three idealised survivorship types on a log axis (schematic). B: the slide-10 table plotted on a log axis. The segment from day 0 to day 299 is dashed because the table contains no data inside that class.*

> [!key] The three types
> **Type I:** mortality is low until late in life, then high (large mammals, humans; Molles' examples: Dall sheep, *Phlox*, the rotifer *Floscularia*). **Type II:** a constant proportion dies in each interval, so the log-curve is a straight line (birds such as the American robin and white-crowned sparrow; the common mud turtle after its first year). **Type III:** very high juvenile mortality, then high survival for those that pass that stage (marine fish such as the mackerel, the prawn *Leander*, the desert shrub *Cleome*).

Molles' numbers show how extreme Type III can be: of 1 million mackerel eggs more than 999,990 die in 70 days; 1 million *Leander* eggs leave about 2,000 survivors after a year; for *Cleome*, about 39 per million seeds reach age 1 (0.0039 %) ([[Section 10.3-10.4_Manuel Molles_9Ed.pdf#page=4|pp. 226–227]]).

### 3.1 Why the y-axis is logarithmic
Slide 12 poses the question and answers it with a hypothetical Type II population in which **60 % die between age 1 and 2, and again between age 2 and 3**.

> [!derivation] Constant risk is a straight line on a log axis
> If an individual has the same probability $q$ of dying in every interval, then $n_{x+1}=(1-q)\,n_x$, so
> $$n_x=n_0(1-q)^x\quad\Longrightarrow\quad \ln n_x=\ln n_0+x\ln(1-q).$$
> Plotted on a log axis the curve is a **straight line of slope $\ln(1-q)$**. In continuous time, $dn/dx=-\mu n$ gives $n=n_0e^{-\mu x}$ with a constant hazard $\mu$. For slide 12: $q=0.6$, so from 1000 the numbers are $1000,\ 400,\ 160,\ 64$. The *losses* are $600,\ 240,\ 96$ (shrinking), but the *proportion* lost is $0.6$ each time, and the log-slope is $\ln0.4=-0.916$ each time.

> [!intuition] A log axis shows rates, a linear axis shows amounts
> On a linear axis, the fall from 1000 to 400 looks far worse than the fall from 400 to 160, although the risk to an individual is identical. Ask "how likely is *one animal* to die here?" and you want a log axis; ask "how many bodies are there to bury?" and you want a linear one. Population dynamics asks the first question.

> [!pitfall] What the types do and do not say
> - A steep early drop (Type III) is about **juvenile survival**, not about short life: the survivors may live long. The *Phlox* curve (Fig. EE2.1B) mixes features: a large early loss like Type III, a plateau and then a rapid end like Type I. Molles files it with the Type I pattern because survival is high among the young *and* middle-aged after the initial period.
> - The idealised curves "seldom followed exactly by natural populations" (slide 13); they mark **boundaries of what is possible**, and real curves are approximations and mixtures. Molles adds that their value is as summaries and as bounds.
> - The slope of the log-curve is the per-capita **hazard**, not the number of deaths.

## 4. Age-structured dynamics: the Leslie matrix
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=14|slides 14–21]]*

Slide 14 asks how the population of *Phlox* will change, and then *removes a constraint*: **let there be kids**. A cohort life table follows only one batch of birth; it ignores that the cohort has children, who enter at age 0 in later years. To project a whole population forward we keep a count in every age class, and let each year's births join the first class.

### 4.1 Building the matrix
Slide 15 shows the life-cycle graph of four age classes and the **Leslie matrix**:

$$\begin{pmatrix}n_1\\n_2\\n_3\\n_4\end{pmatrix}_{t+1}=\begin{pmatrix}F_1&F_2&F_3&F_4\\P_1&0&0&0\\0&P_2&0&0\\0&0&P_3&0\end{pmatrix}\begin{pmatrix}n_1\\n_2\\n_3\\n_4\end{pmatrix}_{t}$$

([[Leslie Matrix]]). Two kinds of entry: the **survival probability** $P_x$ moves a fraction of class $x$ up to class $x+1$ (sub-diagonal), and the **fecundity** $F_x$ gives the offspring per member of class $x$ (top row, which feeds class 1).

![[02_StageStructuredDynamics_11-Aug-2026.pdf#page=15&height=300]]
*Slide 15: the life-cycle graph and the Leslie matrix.*

> [!intuition] Every row is a sentence
> Row 1 reads "this year's babies = Σ (fecundity × number in each class)". Row 2 reads "class 2 = the survivors of class 1". The matrix is only a compact way of writing a ledger with one line per age. Multiplying by it once is one year; multiplying $t$ times is $t$ years.

### 4.2 The simulation on slide 16, by hand and by computer
Slide 16 gives $P=(0.5,0.2,0.1,0)$ and $F=(0,2,1,1)$, starts with **200 individuals of age class 0**, and asks for 200 time steps.

> [!example] Worked example 3: first four steps by hand
> Write $\mathbf n=(n_1,n_2,n_3,n_4)$. Class 1 gets $0\cdot n_1+2n_2+1\cdot n_3+1\cdot n_4$; class 2 gets $0.5\,n_1$; class 3 gets $0.2\,n_2$; class 4 gets $0.1\,n_3$.
>
> | $t$ | $\mathbf n$ | $N_t=\sum n$ | $N_{t+1}/N_t$ |
> |---|---|---|---|
> | 0 | (200, 0, 0, 0) | 200 | 0.50 |
> | 1 | (0, 100, 0, 0) | 100 | 2.20 |
> | 2 | (200, 0, 20, 0) | 220 | 0.55 |
> | 3 | (20, 100, 0, 2) | 122 | 1.90 |
> | 4 | (202, 10, 20, 0) | 232 | 0.64 |
>
> The totals alternate up and down: the 200 initial newborns are one **cohort**, and their fertile years (ages 2 to 4) come in pulses, so the births echo every two or three steps. This is the "initial oscillations" of slides 18–20.

![[fig_ee02_leslie.png|860]]
*Figure EE2.2. The slide-16 simulation reproduced. A: total population on a log axis, with the straight-line asymptote $c\lambda^t$. B: age shares converge to the stable age distribution (dotted). C: $N_{t+1}/N_t$ converges to $\lambda$ inside a shrinking envelope.*

What slides 18–20 show, and the numbers behind them (`scripts/ee02_numbers.py`):

- **Total size** (slide 18) "increases monotonically and exponentially" after some initial oscillations; at $t=200$ it is about $3.0\times10^{6}$ (the slide's axis runs to $3.5\times10^{6}$).
- **Age proportions** (slide 19) settle at **0.634921, 0.302108, 0.057499, 0.005472**, the **stable age distribution (SAD)**: although the population grows, the *shares* of the classes stop changing. The slide notes: "age distribution = proportion of the population in each age class".
- **Growth ratio** (slide 20): $N_{t+1}/N_t\to\lambda=1.05082$. Once the SAD is reached, the whole population is governed by this single number.

The reproduced numbers agree with the slide to all printed digits.

### 4.3 Why it settles: eigenvalues
Slide 21 states the general result ("true for any biologically realistic Leslie matrix") and, "for the mathematically oriented (others can ignore)", that $\lambda$ is the **dominant eigenvalue** of the matrix and the SAD is the corresponding **eigenvector** ([[Stable Age Distribution]], [[Dominant Eigenvalue and Perron-Frobenius Theorem]]). Here is the mechanism.

> [!derivation] The long-run behaviour from the eigen-equation
> Look for a solution in which every class grows by the same factor, $\mathbf n(t)=\lambda^t\mathbf w$. Then $\mathbf A\mathbf w=\lambda\mathbf w$: $\mathbf w$ is an eigenvector. For a Leslie matrix the sub-diagonal rows give $\lambda w_{x+1}=P_xw_x$, so
> $$w_x=w_1\,\frac{l_x}{\lambda^{\,x-1}},\qquad l_x=P_1P_2\cdots P_{x-1}.$$
> The first row gives $\lambda w_1=\sum_xF_xw_x$, i.e. after dividing by $w_1$ and using the formula above,
> $$\boxed{\;1=\sum_x F_x\,l_x\,\lambda^{-x}\;}$$
> the discrete **Euler-Lotka equation**. For the slide-16 numbers, $l=(1,\ 0.5,\ 0.1,\ 0.01)$, so $1=\dfrac{1}{\lambda^2}+\dfrac{0.1}{\lambda^3}+\dfrac{0.01}{\lambda^4}$, or $\lambda^4=\lambda^2+0.1\lambda+0.01$. Substituting $\lambda=1.05082$: $1.2193=1.1042+0.1051+0.0100=1.2193$. ✓ And the age proportions satisfy $w_{x+1}/w_x=P_x/\lambda$: $0.5/1.0508=0.4758$, which is the ratio of the slide's first two proportions, $0.302108/0.634921$.
>
> The right-hand side of the Euler-Lotka equation falls steadily as $\lambda$ grows, so there is exactly **one positive root**. At $\lambda=1$ the right-hand side equals $\sum F_xl_x=R_0$ (here $0+1+0.1+0.01=1.11$). Therefore $\lambda>1\iff R_0>1$, which links §2 to §4.

> [!example] What the other eigenvalues do
> The eigenvalues of the slide-16 matrix are $+1.0508$, $-0.9518$ and a complex pair of modulus $0.100$. Any starting state is a sum of eigen-contributions $c_i\lambda_i^t\mathbf w_i$. The second eigenvalue is **real and negative**: its sign flips every step, which is the zig-zag of Fig. EE2.2. It comes from the two-step loop class 1 → class 2 → class 1 (a newborn reaches class 2 with probability $P_1=0.5$ and leaves $F_2=2$ newborns, a gain $F_2P_1=1$ per two steps), which behaves like $\lambda^2\approx1$ and so has roots near $\pm1$. Relative to the dominant term the flip-flop decays like $(0.9518/1.0508)^t=0.906^t$ (damping ratio 0.906 per step), so after about 40 steps every age share is within 0.01 of the SAD.

> [!intuition] The matrix forgets where it started
> Whatever mix of ages you begin with, repeated multiplication by the same matrix squeezes the population toward one shape that the matrix merely rescales. This is the same idea as relaxing to a fixed point in [[Fixed Points and Linear Stability]], except that the thing being approached is a *direction* (a proportion) rather than a number, and the growth is geometric. Caswell calls this "forgetting the past" **ergodicity**.

### 4.4 When the matrix is "biologically realistic": Perron-Frobenius
Slide 21 says that because a Leslie matrix has no negative entries, "the Perron-Frobenius theorem ensures that there will be at least one real eigenvalue; if there are more, the largest is called the dominant one". That is the weak form; the strong form that makes the simulation always settle needs two more words.

> [!key] Perron-Frobenius for population matrices
> A non-negative matrix $\mathbf A$ is **irreducible** if its life-cycle graph is connected (there is a path from every class to every other) and **primitive** if the greatest common divisor of its loop lengths is 1. For a non-negative, irreducible, primitive $\mathbf A$: (1) there is a **simple, real, positive eigenvalue $\lambda_1$ strictly larger in modulus than all others**; (2) its right eigenvector $\mathbf w$ is strictly positive (the SAD); (3) its left eigenvector $\mathbf v$ is strictly positive (the reproductive values). Then the population converges to $\lambda_1^t\mathbf w$ from any non-zero start.

A Leslie matrix with fertility in two *adjacent* classes (as on the slide: $F_2,F_3,F_4>0$) has loops of lengths 2, 3, 4 and gcd 1, so it is primitive.

> [!extra-book]+ 🟡 Extra (book): Caswell (1997) on the same points
> Caswell ([[Caswell_Matrix Methods for Population Analysis.pdf#page=12|pp. 30–31]]) states the theorem exactly as above, adds that "most population-projection matrices encountered in practice are both irreducible and primitive", and names three results of **demographic ergodicity**: the population eventually grows geometrically at $\lambda_1$; its structure becomes proportional to $\mathbf w$; and the constant of proportionality is a weighted sum of the starting numbers, $\mathbf v^{T}\mathbf n(0)$, with the weights the **reproductive values** ([[Caswell_Matrix Methods for Population Analysis.pdf#page=13|p. 31]]). He stresses that $\lambda_1,\mathbf w,\mathbf v$ are "properties of the vital rates, not of the initial conditions" and are *projections of what would happen if the vital rates stayed constant*, not predictions.

> [!pitfall] A matrix that does *not* settle
> If only **one** age class reproduces, the life cycle has a single loop and the matrix is imprimitive (the example is a **semelparous** species, one that breeds once and dies). Take $F_3=6$, $P_1=0.5$, $P_2=0.4$: all three eigenvalues have the same modulus $(6\times0.5\times0.4)^{1/3}=1.063$, and the population just repeats a 3-step cycle ($N=100,\,50,\,20,\,120,\,60,\,24,\,144,\dots$). There is a growth factor per *three steps* (1.2) but no SAD and no limit for $N_{t+1}/N_t$. Practice problem 4 asks you to see why.

> [!pitfall] Indexing and census timing
> The slides number the classes 1–4 in the matrix (slide 15–16) but 0–3 in the plots (slide 19). They are the same classes; slide 16's "age class 0" is the newborn class. Also, *when* you count matters: Crowder et al. count right **after** breeding ("post-breeding census"), so a newborn is first counted at the next census and fecundity entries include the mother's survival. Different census times give differently written but equivalent matrices.

## 5. Stage-structured dynamics: the loggerhead turtle
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=22|slides 22–28]]* · <span class="scope-extra-book">extra · book</span> *Crowder et al. 1994 (paper)*

Slide 22 introduces the loggerhead sea turtle, *Caretta caretta*, as an application. The pedagogical note of slide 30 explains the move: *remove one more constraint*. For a turtle, **age is hard to measure** (animals are marked late, ages are guessed) and **size or stage drives fate** (a 10-year-old and an 18-year-old may both be "large juveniles" facing the same risks). So classify by **stage**, and let an individual either stay in its stage or move on ([[Lefkovitch Stage-Structured Matrix]]).

### 5.1 The model of Crouse (1987) and Crowder (1994)
Slide 23 poses the conservation context, the long-standing practice of **protecting nests and hatchlings**, and slide 24 shows the matrix with the note "G is the probability of going to the next stage class; P is the probability of remaining in the same stage class":

$$\mathbf A=\begin{pmatrix}P_1&F_2&F_3&F_4&F_5\\G_1&P_2&0&0&0\\0&G_2&P_3&0&0\\0&0&G_3&P_4&0\\0&0&0&G_4&P_5\end{pmatrix}\qquad\text{loggerhead: }\begin{pmatrix}0&0&0&4.665&61.896\\.675&.703&0&0&0\\0&.047&.657&0&0\\0&0&.019&.682&0\\0&0&0&.061&.8091\end{pmatrix}$$

![[fig_ee02_lifecycle.png|800]]
*Figure EE2.3. The life-cycle graph of the loggerhead matrix. Blue arrows are growth to the next stage ($G$), green loops are staying ($P$), orange arrows are fecundity.*

Crowder et al. *reduced* the seven-stage model of Crouse et al. (1987) to five stages by merging the three adult stages (they share one annual survival), and rebuilt the matrix from stage durations and survival ([[Crowder+_EcolAppl_1994_Predicting the Impact of Turtle Excluder Devices on Loggerhead Sea Turtle Populations.pdf#page=4|Table 1 and Table 2, p. 439]]):

| stage | duration (yr) | annual survival $\sigma$ | annual fecundity |
|---|---|---|---|
| 1 eggs/hatchlings | 1 | 0.6747 | 0 |
| 2 small juveniles | 7 | 0.75 | 0 |
| 3 large juveniles | 8 | 0.6758 | 0 |
| 4 subadults | 6 | 0.7425 | 0 |
| 5 adults | > 32 | 0.8091 | 76.5 |

> [!pitfall] The slide's wording of $G$ and $P$
> The slide says $G$ is "the probability of going to the next stage" and $P$ "of remaining". Crowder et al. define them more carefully as the probability of **surviving and** growing into the next stage ($G$) or **surviving and** remaining in the stage ($P$). So $P_i+G_i=\sigma_i$, the stage's annual survival, and mortality $1-\sigma_i$ is what is left out of the matrix. The numbers confirm it: $P_2+G_2=0.703+0.047=0.750=\sigma_2$.

### 5.2 From duration and survival to $P$ and $G$
> [!derivation] Why a stage of $T$ years graduates only a few percent per year
> Within a stage, individuals have a *within-stage age* $a=1,\dots,T$. A fraction $\sigma$ of each age survives a year, and at the stable distribution every class also grows by $\lambda$ per year, so the share at within-stage age $a$ is proportional to $x^{a-1}$ with $x=\sigma/\lambda$. Only the oldest ($a=T$) leave, so the fraction of the stage that graduates in a year is
> $$\gamma=\frac{x^{T-1}(1-x)}{1-x^{T}},\qquad G=\sigma\gamma,\quad P=\sigma(1-\gamma).$$
> This is the Caswell (1989) calculation used in Crowder's Appendix 1 ([[Crowder+_EcolAppl_1994_Predicting the Impact of Turtle Excluder Devices on Loggerhead Sea Turtle Populations.pdf#page=9|p. 444]]). Because it contains $\lambda$, which is itself the eigenvalue of the matrix, the authors iterate until the starting and final $\lambda$ agree to four decimals.

> [!example] Worked example 4: rebuilding two entries of Table 2
> **Small juveniles** ($\sigma=0.75,\ T=7$, $\lambda=0.9516$): $x=0.7882$, $\gamma=\dfrac{0.7882^{6}(0.2118)}{1-0.7882^{7}}=0.0626$, so $G_2=0.75\times0.0626=0.047$ and $P_2=0.75-0.047=0.703$ ✓.
> **Large juveniles** ($\sigma=0.6758,\ T=8$): $x=0.7102$, $\gamma=0.0282$, so $G_3=0.019$, $P_3=0.657$ ✓.
> **Fecundity**, with a post-breeding census: adults lay $76.5$ eggs a year and must survive to the next census, so $F_5=76.5\times P_5=76.5\times0.8091=61.896$ ✓; subadults that mature this year also contribute, $F_4=76.5\times G_4=76.5\times0.061=4.665$ ✓.
> The long stage (large juveniles, 8 years) has a *small* $G$ simply because only the oldest eighth of them leave each year; the matrix keeps them there with $P_3=0.657$. Rebuilding the whole matrix this way reproduces Crowder's Table 2 to within 0.003.

### 5.3 What the matrix says
- **$\lambda=0.9516$**, or **$r=\ln\lambda=-0.0496$**: the population declines about **5 % a year**. Crowder et al. note that they lowered small-juvenile survival from Frazer's 0.8144 to 0.75 so that the model matches a decline of about 5 % a year observed on Little Cumberland Island (a 3 % decline would otherwise be implied). The baseline of **−0.050** is the dashed line in the original Fig. 4.
- **Stable stage distribution** (right eigenvector, Table 3): $0.2385,\ 0.6478,\ 0.1033,\ 0.0073,\ 0.0031$. At the SAD, small juveniles dominate (65 %) and **adults are only 0.3 %**.
- **Reproductive values** (left eigenvector, $v_1=1$): $1,\ 1.4,\ 7.5,\ 115,\ 432$. A hatchling is worth little because few hatchlings survive to breed; a surviving subadult is worth a great deal, and an adult more still. The reproductive value jumps most across the **large-juvenile** stage.

The reproductive value $v_i$ is the expected long-term contribution of an individual in stage $i$; the SAD $w_j$ is how many individuals are in stage $j$. Their product $v_iw_j$ is exactly what controls how much $\lambda$ responds to a change in $a_{ij}$ (next).

### 5.4 Where should effort go? Sensitivity and elasticity
Slides 25–26 ask: *given this distribution of survivorship and mortality, on what stage should conservation efforts be directed, and by how much?* The answer, drawn from Crowder et al.'s Fig. 4:

![[02_StageStructuredDynamics_11-Aug-2026.pdf#page=26&height=330]]
*Slide 26 (Crowder et al. 1994, Fig. 4): the change in the intrinsic rate of increase $r$ when annual **mortality** in one stage is cut by 10, 50 or 90 %. Dashed baseline: $r=-0.050$.*

*"Improving egg survival will never make the population growth rate positive and hence not stem the population decline. The analysis suggests that loggerhead population declines are best reversed by focusing conservation efforts at improving survival of large juveniles."* (slide 26).

I recomputed this experiment from Table 1 (`scripts/ee02_numbers.py`, `scripts/fig_ee02_loggerhead.py`).

![[fig_ee02_loggerhead.png|900]]
*Figure EE2.4. Recomputed from the Table 1 survivals. A: $r$ after cutting one stage's mortality by 10, 50 or 90 % (compare slide 26: the bar heights agree to about ±0.002). B: elasticity of $\lambda$ to annual survival, in two conventions explained below. C: projected time for a ten-fold recovery under the paper's two TED scenarios.*

The checks against the slide-26 bars (my values, rounded; slide values read from the figure):

| stage | cut by 10 % / 50 % / 90 % (mine) | slide |
|---|---|---|
| egg/hatchling | −0.048 / −0.042 / −0.0365 | −0.049 / −0.042 / −0.036 |
| small juvenile | −0.041 / −0.010 / +0.019 | −0.041 / −0.010 / +0.020 |
| large juvenile | −0.036 / +0.015 / **+0.060** | −0.035 / +0.015 / +0.060 |

So: a 10 % cut anywhere leaves the population declining; a 50 % cut helps only in the **large juvenile** stage (then $r>0$); a 90 % cut works in every stage except eggs and hatchlings. **Even perfect egg survival** ($\sigma_1\to1$) leaves $\lambda=0.965<1$, while perfect large-juvenile survival gives $\lambda=1.073$. Reasonable increases in fecundity alone cannot reverse the decline.

> [!intuition] A stage matters in proportion to how long you stay and how valuable you are when you leave
> Eggs and hatchlings last one year and become, on average, small juveniles worth only 1.4 times as much. Large juveniles last eight years, which means eight chances per animal to be lost, and each survivor is on the verge of a jump in reproductive value of more than fifteen times. Saving one extra large juvenile is therefore worth many saved eggs.

> [!derivation] Sensitivity of $\lambda$ to a matrix entry
> Let $\mathbf A\mathbf w=\lambda\mathbf w$ and $\mathbf v^{T}\mathbf A=\lambda\mathbf v^{T}$. Perturb $\mathbf A\to\mathbf A+d\mathbf A$; to first order $\mathbf A\,d\mathbf w+d\mathbf A\,\mathbf w=\lambda\,d\mathbf w+d\lambda\,\mathbf w$. Multiply on the left by $\mathbf v^{T}$: the $d\mathbf w$ terms cancel because $\mathbf v^{T}\mathbf A=\lambda\mathbf v^{T}$, leaving
> $$d\lambda=\frac{\mathbf v^{T}d\mathbf A\,\mathbf w}{\mathbf v^{T}\mathbf w}\quad\Longrightarrow\quad s_{ij}=\frac{\partial\lambda}{\partial a_{ij}}=\frac{v_iw_j}{\mathbf v\!\cdot\!\mathbf w},\qquad e_{ij}=\frac{a_{ij}}{\lambda}\,s_{ij}.$$
> The **elasticity** $e_{ij}$ is the *proportional* change of $\lambda$ per proportional change of $a_{ij}$, and $\sum_{ij}e_{ij}=1$ (it is the share of $\lambda$ "contributed" by each entry). This is the first-order idea of [[Linearisation and Sensitivity]] applied to an eigenvalue ([[Sensitivity and Elasticity of Growth Rate]]).

> [!extra-beyond]- 🔵 Extra (beyond): the elasticity of every entry of the loggerhead matrix
> Computed from Table 2 (`scripts/ee02_numbers.py`):
>
> | entry | value | sensitivity $s_{ij}$ | elasticity $e_{ij}$ |
> |---|---|---|---|
> | $P_2$ small juvenile stays | 0.703 | 0.222 | 0.164 |
> | $P_3$ large juvenile stays | 0.657 | 0.187 | 0.129 |
> | $P_4$ subadult stays | 0.682 | 0.204 | 0.147 |
> | $P_5$ adult stays | 0.809 | 0.329 | **0.280** |
> | $G_1,\ G_2,\ G_3$ | .675, .047, .019 | 0.08, 1.17, 2.90 | 0.058 each |
> | $G_4$ | 0.061 | 0.768 | 0.049 |
> | $F_4,\ F_5$ | 4.665, 61.9 | 0.002, 0.0008 | 0.009, 0.049 |
>
> By type: **$P$ 0.72, $G$ 0.22, $F$ 0.06**, matching Crowder's remark that "changes in $P$ values will have a greater effect on the population than changes in reproductive output or growth". Note the *sensitivity* of $G_3$ (2.9) is the largest of all, because $G_3$ is tiny; its *elasticity* is small. That is why elasticity is the better yardstick for comparing entries of very different size. Also curious: $e_{G_1}=e_{G_2}=e_{G_3}=e_F$ total (0.058), because every reproductive loop in the graph passes through those arrows exactly once.
> Elasticity to *survival* $\sigma_i$ combines the effect on $P_i$ and $G_i$. Crowder's Fig. 2 puts large juveniles first, then small juveniles. Their bars (≈0.06, 0.41, 0.46, 0.32, 0.28) add up to about **1.6**, because they hold $\lambda$ fixed inside the duration formula; my recomputation, in which $\lambda$ also moves inside the formula, gives $0.04,\ 0.25,\ 0.29,\ 0.22,\ 0.21$ summing to 1. Caswell notes (his eq. 33) that elasticities with respect to lower-level parameters "do not in general sum to one". The ranking is the same in both.

> [!extra-book]+ 🟡 Extra (book): Caswell on sensitivity versus elasticity
> Caswell ([[Caswell_Matrix Methods for Population Analysis.pdf#page=15|pp. 33–35]]) derives the same formula $\partial\lambda/\partial a_{ij}=\bar v_iw_j$ from the eigen-equations, uses the chain rule for lower-level parameters, and argues that sensitivities and elasticities are **not competitors**: they answer different questions, like plotting the same numbers on arithmetic or logarithmic axes. Sensitivity answers "what does a small *additive* change do"; elasticity "what does a small *proportional* change do". He also lists the uses: which vital rate matters most for management, how selection acts, and how much of an observed difference in $\lambda$ between two populations each rate difference explains.

### 5.5 Trawling, TEDs, and why recovery is slow
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=27|slides 27–28]]* · <span class="scope-extra-book">extra · book</span> *Crowder et al. 1994*

*What causes juvenile mortality?* Slide 27: **fish trawling in general, and shrimp trawling in particular**, with on average **5.7 kg of by-catch for every kilogram of shrimp caught**. Crowder et al. add that **large juveniles are the most common size class among dead turtles stranded on beaches** and that 70–80 % of strandings are thought to be trawl-related; a National Research Council panel judged incidental capture in shrimp trawls to account for more deaths than all other human activities combined. A **turtle excluder device (TED)** is an escape hatch built into the trawl net ([[Loggerhead Turtle and Turtle Excluder Devices]]).

So if large juveniles are the most sensitive stage and trawls kill them, TEDs are the right intervention. Slide 28: *simulations showed that if used occasionally, about 70 years are needed for a substantial effect; therefore it was suggested that they be used all the time. Indian government legislation in 1996.*

> [!verify] "Used occasionally" in the slide versus the paper
> The paper's ~70 years refers to the **"seasonal offshore"** TED regulations in force in 1990–1992 (TEDs required offshore, during the shrimping season only), not literally to occasional use. In the paper, the expanded rule (all waters, all seasons, with good compliance) gives **nearly twice the speed**. The slide's wording compresses this. I could not check the 1996 Indian legislation; it is taken from the slide.

How the paper gets its numbers ([[Crowder+_EcolAppl_1994_Predicting the Impact of Turtle Excluder Devices on Loggerhead Sea Turtle Populations.pdf#page=6|pp. 440–441]]):

1. Reduce the annual mortality of large juveniles, subadults and adults (small juveniles are offshore and less available to trawls). The model is deterministic, so each scenario is a straight line on a log plot (Fig. 5 of the paper).
2. To estimate *how much* mortality a TED removes, take the difference between the survival of a relatively **unexploited** population (Heron Island, Australia: 0.83, 0.885 and 0.91 for large juveniles, subadults, adults) and the US values, and multiply by **0.67** (Henwood et al.: seasonal offshore TEDs cut trawling mortality by two-thirds) or **0.99** (all waters, all seasons).
3. A second, independent estimate from **South Carolina strandings**: a 37 % fall in strandings during TED years agrees with the first (they call the agreement "remarkable").

> [!example] Worked example 5: the TED numbers recomputed
> With the 0.67 rule the survivals become 0.779, 0.838 and 0.877 for large juveniles, subadults and adults; the matrix is rebuilt and gives $\lambda=1.0348$ (**+3.5 % per year**; the paper says 3.6 %), so a ten-fold increase takes $\ln10/\ln1.0348=67$ years (paper: about 70). With the 0.99 rule, $\lambda=1.073$ and ten-fold in **33 years**, about half. A uniform cut of $x$ in mortality across the three stages makes $\lambda=1$ at $x=19.7\,\%$ (the paper: "20 % or more"), and a 40 % cut gives ten-fold in about 48 years (paper: "50 yr or less"). Halving large-juvenile mortality *alone* gives $\lambda=1.015$.
> **Reading:** a loggerhead population cannot recover quickly because a turtle takes more than 20 years to mature, so the effect of today's saved juvenile shows up as breeding adults only decades later.

> [!extra-book]+ 🟡 Extra (book): the transient "waves" in nesting females
> The matrix model has stable-stage dynamics. The population today does **not** have the stable distribution that the new survivals imply (it reflects decades of heavy trawling). To explore the transient, the authors expand the model into a **$54\times54$ Leslie matrix** (one row per year of life), start with $10^{6}$ turtles at the stable age distribution, and cut large-juvenile, subadult and adult mortality by 37 % at year 6. Result: the number of nesting females first **rises**, then **levels or dips 10–15 years** after TEDs, and then rises again about 25–30 years on. The reason is a "hole" in the age structure: fewer eggs were laid in the early years, and that smaller cohort reaches maturity later. The wave dissipates as the population approaches its new SAD. The practical message is for beach surveys: a flat or falling nest count a decade after TEDs is *not* evidence that TEDs failed.

> [!pitfall] How much to trust the numbers
> The authors call quantitative predictions "risky": the data are poor (tagging is hard; small-juvenile survival is a guess), the model is deterministic, and it assumes TED savings are **additive** (if other mortality rises to compensate, recovery is slower). They defend the model as a way to **identify which parameters matter** and so direct research and management, "not as a product in itself". Use the qualitative results (large juveniles; P-entries; recovery is slow) with confidence and the 70 years with care.

### 5.6 Age or stage?
| | age-structured (Leslie) | stage-structured (Lefkovitch) |
|---|---|---|
| classes | years of age (any number) | biological stages of unequal length |
| transitions | move up one class or die | stay ($P$), move on ($G$) or die |
| fits when | age fixes fate; ages are known | size/stage fixes fate; ages are uncertain |
| price | many classes, many parameters | assumes a stable distribution inside each stage |

Both give a non-negative matrix with a dominant eigenvalue $\lambda$, stable distribution $\mathbf w$ and reproductive values $\mathbf v$, and the same sensitivity formulas.

## 6. Back to humans: age distributions and pyramids
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=29|slide 29]] · Molles §10.4 and §11.4*

Slide 29: **greater the $\lambda$, the broader the base; a narrow base indicates a declining population and vice versa.** An **age pyramid** shows the share of the population in each age class, males and females back to back ([[Age Pyramid]]). It is the age distribution of §4 made visible.

![[fig_ee02_pyramids.png|860]]
*Figure EE2.5. Stable age distributions of one Leslie model of a human-like population with fertility scaled to three values of $R_0$ (schematic, my construction). The base widens with $\lambda$.*

An age distribution is also a record of **history** (Molles §10.4, [[Section 10.3-10.4_Manuel Molles_9Ed.pdf#page=5|pp. 228–229]]):

- **White oak** (*Quercus alba*) in an Illinois forest (Miller 1923): most trees are in the 1–50-year class with progressively fewer older ones, so the oldest trees are being replaced: stable or growing.
- **Rio Grande cottonwood** (*Populus deltoides*): dominated by 40–50-year-old trees and **no reproduction for over a decade**. Seedlings need floods to clear bare, moist soil; dams ended the floods, so the population is ageing and not replacing itself.
- **Large cactus finch** on Genovesa (Galápagos; Grant and Grant): the 1983 age distribution has a **gap at age 6** (no breeding in the 1977 drought); the 1987 one is dominated by 4-year-olds hatched in the wet 1983 and has new gaps (droughts of 1984–85). Age structure follows the weather.

Molles §11.4 ([[Ch 11_Ecology _ concepts & applications_9Ed_2022_Molles.pdf#page=14|p. 250, Fig. 11.24]]) contrasts three countries using UN data for 2020: **Sweden** (birth rate $b=0.010$, death rate $d=0.010$, $r=b-d=0$: a stable shape), **Hungary** ($b=0.010,\ d=0.013,\ r=-0.003$: a narrow base, declining) and **Rwanda** ($b=0.037,\ d=0.010,\ r=+0.027$: a very broad base, growing).

> [!example] Worked example 6: what those $r$ values mean
> With $r$ constant the population is exponential, $N=N_0e^{rt}$ ([[Exponential Growth]]), so it doubles in $t_d=\ln2/r$. **Rwanda:** $\ln2/0.027=25.7$ years. **Hungary:** $r<0$, so it halves in $\ln2/0.003=231$ years: a slow decline. **Sweden:** $r=0$ and no change. The yearly growth factor is $\lambda=e^{r}$: Rwanda 1.027, Hungary 0.997.

> [!extra-book]+ 🟡 Extra (book): UN *World Population Prospects 2024* and India
> The course folder includes the WPP 2024 key messages ([[WPP2024_Key-Messages.pdf|reading]]). Several map directly onto this chapter: the world population is expected to **peak at about 10.3 billion in the mid-2080s** (from 8.2 billion in 2024); the global **fertility rate is 2.3** births per woman (3.3 in 1990), and more than half of all countries are **below 2.1**, "the level required for a population to maintain a constant size in the long run without migration"; and, most relevant here, "**the main driver of global population increase through mid-century will be the momentum created by growth in the past**": today's youthful age structure accounts for 79 % of the increase through 2054. The *Data for India* article ([[Population growth in India.pdf|reading]]) reports that India's growth has slowed sharply since the 1980s, faster in the southern states, with the UN projection of a peak near 1.7 billion in the mid-2060s. These are *news-level* readings, not on the slides, so treat them as background.

> [!extra-beyond]- 🔵 Extra (beyond): why replacement fertility is 2.1, and what "momentum" means
> **Replacement.** $R_0=\text{TFR}\times(\text{share of births that are girls})\times(\text{survival to childbearing})$. With about 105 boys per 100 girls the girl share is $100/205=0.488$, so $R_0=1$ needs TFR $=2.05/s$; with $s\approx0.98$ survival to the reproductive ages this is $\approx2.09\approx2.1$.
> **Momentum.** A young age structure keeps growing for a generation even after fertility is cut to replacement, because the large cohorts of young people have yet to have children. A four-class toy model (20-year classes; $\lambda=1.275$ per class step, $R_0=1.73$) whose fertility is instantly cut to $R_0=1$ still ends **17 % larger** (it overshoots, wobbles, then settles). This is the mechanism behind "79 % of the increase through 2054".

## 7. The pedagogical note, and what the readings cover
<span class="scope-taught">taught</span> *[[02_StageStructuredDynamics_11-Aug-2026.pdf#page=30|slides 30–31]]*

Slide 30 spells out the shape of the lecture:
1. Start with an **over-simplified** way of looking at things and derive some insight (the cohort life table).
2. **Remove one constraint** (add the offspring to the cohort), getting into age- and stage-structured dynamics: more insight.
3. Next, a **completely different way** of tackling the same problem: [[EE03 Population Dynamics and Chaos]] drops structure and looks at the total $N(t)$ with simple density-dependent models.

Reading tiers (slide 31, using the rule of [[EE01 Introduction to Biology and Ecological Thinking]] §7):

| item | tier |
|---|---|
| lecture slides | syllabus |
| Molles §10.3–10.4 (survival; age distribution) | **mandatory**, syllabus |
| Molles Ch. 11 (population growth) | **mandatory**, syllabus; §11.1 geometric and exponential growth, §11.2 sigmoidal (logistic) growth and §11.3 density dependence are the subject of EE03, §11.4 humans is §6 here |
| Crowder et al. 1994; Caswell 1997 | papers: no exam weight (summarised here) |

> [!verify] Where to file the rest of Molles Chapter 11
> The deck lists the whole chapter as mandatory reading, but its first three sections (growth models, density dependence) are lectured in EE03. They are used there, not duplicated here; the Phlox projection (Worked example 2) is the bridge. Whether the exam expects them in the structured-populations context is for the instructor to say.

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Age-structured growth: the Leslie matrix settles into a stable age distribution
> Four age classes with fecundities F and survivals P: n_{t+1} = L n_t.
>
> ![[ee_leslie.png|720]]
>
> **Try:** Defaults P = (0.5, 0.2, 0.1), F = (0, 2, 1, 1) and 200 newborns reproduce the slide: λ = 1.05082, SAD (0.635, 0.302, 0.057, 0.005). Lower F₂ until R₀ < 1 and the population dies out. Start with all adults instead of newborns to change the transient, not the limit.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_leslie.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_leslie.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How EE02 connects
> **Builds on:** [[EE01 Introduction to Biology and Ecological Thinking]] (levels; models as oversimplification; Mayr's population thinking, [[Population Thinking]]).
> **Leads to:** [[EE03 Population Dynamics and Chaos]] (drop structure, add density dependence) → [[EE04 Competition and Invasions]] → [[EE05 Predation]] → [[EE06 Eutrophication and Alternative Stable States]] → [[EE07 Conservation Biology]] (the same "where do I act?" question for tigers, [[Project Tiger]]).
> **Concepts:** [[Population Ecology]] · [[Cohort Life Table]] · [[Survivorship Curve]] · [[Net Reproductive Rate]] · [[Leslie Matrix]] · [[Stable Age Distribution]] · [[Dominant Eigenvalue and Perron-Frobenius Theorem]] · [[Lefkovitch Stage-Structured Matrix]] · [[Sensitivity and Elasticity of Growth Rate]] · [[Loggerhead Turtle and Turtle Excluder Devices]] · [[Age Pyramid]]
> **Other subjects:** [[Fixed Points and Linear Stability]] (eigenvalues and stability) · [[Linearisation and Sensitivity]] · [[Relaxation Time]] (the SAD is approached at a rate set by the second eigenvalue) · [[Probability - Course Map]] (stochastic demography) · [[Inorganic Chemistry - Course Map]] (biogeochemical cycles)

![[EE02 From Life Table to Management.svg|760]]
*Figure EE2.6. The chapter in one picture. Editable: [[EE02 From Life Table to Management.excalidraw]].*

> [!connection] Eigenvalues again
> The condition "$\lambda>1$" is the matrix version of "a fixed point is unstable when the multiplier $|g'(x^*)|>1$" ([[Fixed Points and Linear Stability]]): the zero-population state of a linear projection model is unstable exactly when the dominant eigenvalue exceeds 1. Structure only changes *which* number plays the role of the single growth factor.

## Summary
> [!summary] Cheat-sheet
> - **Population** = similar individuals in a place and time; study **distribution, demography, dynamics**. Bookkeeping: $N_{t+1}=N_t+B-D+I-E$.
> - **Cohort life table**: $n_x$, $l_x=n_x/n_0$, $m_x$; **$R_0=\sum l_xm_x$** (Phlox: 2.4177). Three ways to get survival data: cohort, static, age distribution.
> - **Survivorship**: log axis shows *per-capita* rates; constant risk ⇒ straight line, $\ln n_x=\ln n_0+x\ln(1-q)$. **Type I** late mortality, **II** constant, **III** early. Real curves are mixtures.
> - **Leslie matrix**: $\mathbf n_{t+1}=\mathbf L\mathbf n_t$; fecundities on row 1, survivals on the sub-diagonal. After transients: exponential growth by $\lambda$ (dominant eigenvalue) and a fixed **stable age distribution** (eigenvector). Slide example: $\lambda=1.05082$; SAD $=(0.635,\ 0.302,\ 0.057,\ 0.005)$. Euler-Lotka: $1=\sum F_xl_x\lambda^{-x}$; $\lambda>1\iff R_0>1$.
> - **Perron-Frobenius** (needs non-negative, irreducible, primitive): simple positive $\lambda_1$, strictly positive $\mathbf w$ and $\mathbf v$.
> - **Stage model**: $P$ stay, $G$ grow, $F$ fecundity; $P+G=\sigma$. Loggerhead: $\lambda=0.9516$ (−5 %/yr); adults 0.3 % of the stable population.
> - **Where to act**: sensitivity $v_iw_j/\mathbf v\!\cdot\!\mathbf w$, elasticity $(a_{ij}/\lambda)s_{ij}$ (sums to 1). Large juveniles matter most; **egg protection alone cannot make $\lambda>1$**. 5.7 kg by-catch per kg of shrimp ⇒ **TEDs**; seasonal-offshore use ≈ 70 yr for 10×, full use about half.
> - **Pyramids**: broad base ⇔ $\lambda>1$; Sweden $r=0$, Hungary $-0.003$, Rwanda $+0.027$ (doubling 25.7 yr).

## Practice
1. **Life table.** A cohort of 1000 seeds has $n_x=1000,\ 500,\ 200,\ 0$ at ages $x=0,1,2,3$, and survivors make $m_x=0,\ 2,\ 3,\ 0$ offspring at those ages. Find $l_x$, $R_0$, the mean age at reproduction $T=\sum x\,l_xm_x/R_0$ and the approximate growth rate $r\approx\ln R_0/T$.
2. **Survivorship.** A cohort numbers 1000, 400, 160 at ages 1, 2, 3. (a) What is the survival probability per step? (b) How many are left at age 5 if the risk per step stays constant? (c) Which type is it and what does a log plot show? (d) Why would a linear plot mislead?
3. **Leslie matrix.** A species has three age classes with $F=(0,\ 1.2,\ 0.8)$ and $P=(0.5,\ 0.4)$. (a) Write the matrix. (b) Find $R_0$. (c) Use the Euler-Lotka form to find $\lambda$ and the stable age distribution. (d) What does the population do in the long run?
4. **A matrix that never settles.** Take $F_3=6$, $P_1=0.5$, $P_2=0.4$ and no other fecundity (a species that breeds once, in its third year). (a) Iterate from $(100,0,0)$ for six steps. (b) Find the moduli of the eigenvalues. (c) Why does Perron-Frobenius in its strong form not apply?
5. **Stage matrix.** For large juveniles ($\sigma=0.6758$, $T=8$) with $\lambda=0.9516$ compute $\gamma$, $G_3$ and $P_3$ and compare with Table 2 of Crowder et al.
6. **Elasticity.** The elasticity of $\lambda$ to the annual survival of large juveniles is about 0.29. By how much does $\lambda$ change if that survival is raised by 10 % (relative)?
7. **Management.** For the loggerhead model compare (i) nest protection that raises egg/hatchling survival from 0.675 to 1.0 and (ii) halving large-juvenile mortality. Give $\lambda$ for each and explain the difference in words.
8. **Humans.** (a) Rwanda has $b=0.037$, $d=0.010$: find the doubling time. (b) Hungary has $b=0.010$, $d=0.013$: find the halving time. (c) Why is the replacement fertility close to 2.1 rather than exactly 2?
9. **Exam-style.** "What is the stable age distribution of a population, and why does a Leslie-matrix population reach it?" Outline an answer in five lines.
10. **Discussion.** The Rio Grande cottonwood age distribution is dominated by 40–50-year-old trees. Is the species "in danger"? What does the distribution *predict*, and what intervention does the explanation suggest?

> [!example]- Solutions
> 1. $l_x=1,\ 0.5,\ 0.2,\ 0$. $R_0=0.5\times2+0.2\times3=1+0.6=1.6$ (each seed leaves 1.6 seeds behind). $T=(1\times0.5\times2+2\times0.2\times3)/1.6=(1+1.2)/1.6=1.375$. $r\approx\ln1.6/1.375=0.470/1.375=0.34$ per year.
> 2. (a) $400/1000=0.4$. (b) Age 5 is four steps after age 1: $1000\times0.4^{4}=25.6$ (1000, 400, 160, 64, 25.6 at ages 1…5). (c) Type II: a straight line of slope $\ln0.4=-0.916$ per step on a log axis; the per-capita hazard is constant. (d) The linear plot shows losses of 600 then 240 and makes the second period look better, although the risk per individual is the same.
> 3. (a) $\begin{pmatrix}0&1.2&0.8\\0.5&0&0\\0&0.4&0\end{pmatrix}$. (b) $l=(1,0.5,0.2)$, $R_0=1.2\times0.5+0.8\times0.2=0.76<1$. (c) $1=1.2\,(0.5)/\lambda^2+0.8\,(0.2)/\lambda^3\Rightarrow\lambda^3=0.6\lambda+0.16$, root $\lambda=0.884$; shares $w\propto(1,\ 0.5/\lambda,\ 0.2/\lambda^2)=(1,0.566,0.256)$, normalised $(0.549,\ 0.311,\ 0.141)$. (d) Because $R_0<1$ and $\lambda<1$ the population declines by $1-0.884=11.6\,\%$ a year with those shares fixed.
> 4. (a) Totals: 100, 50, 20, 120, 60, 24, 144: the pattern $(100,0,0)\to(0,50,0)\to(0,0,20)\to(120,0,0)\dots$ repeats every three steps and multiplies by $6\times0.5\times0.4=1.2$ per cycle. (b) All three eigenvalues have modulus $1.2^{1/3}=1.063$ (one real, two complex). (c) There is a single loop of length 3, so gcd of loop lengths is 3, not 1: the matrix is irreducible but **imprimitive**; no eigenvalue strictly dominates in modulus, hence no limit for the age shares or for $N_{t+1}/N_t$.
> 5. $x=\sigma/\lambda=0.6758/0.9516=0.7102$; $\gamma=x^{7}(1-x)/(1-x^{8})=0.0282$; $G_3=\sigma\gamma=0.0191$; $P_3=\sigma(1-\gamma)=0.6567$. Table 2 gives 0.019 and 0.657 ✓.
> 6. $\Delta\lambda/\lambda\approx0.29\times10\,\%=2.9\,\%$, so $\lambda\approx0.9516\times1.029=0.979$ (exact: $\sigma_3=0.7434$ gives $0.9786$, a 2.8 % rise). Still below 1, which is why a single stage needs a larger cut.
> 7. (i) $\lambda=0.965$ (still declining ≈ 3.5 % a year): eggs are a one-year stage of low reproductive value. (ii) $\lambda=1.015$ (growth ≈ 1.5 % a year). A large juvenile spends eight years in the stage (eight chances to be lost), is worth about 5 times a small juvenile ($v=7.5$ against $1.4$), and at the next step its value rises about 15-fold (to $115$); a hatchling lasts one year and is worth little.
> 8. (a) $\ln2/0.027=25.7$ yr. (b) $\ln2/0.003=231$ yr. (c) $R_0=\text{TFR}\times0.488\times s$; for $R_0=1$, TFR $=2.05/s\approx2.09$ with $s\approx0.98$: the extra 0.05–0.1 covers more boys than girls at birth and a few women dying before reproducing.
> 9. Stable age distribution (SAD): the set of age-class proportions that no longer changes. It arises because repeated multiplication by the same non-negative, primitive matrix is dominated by the eigenvector of the largest eigenvalue $\lambda$; the other terms decay as $(|\lambda_i|/\lambda)^t$. Then every class grows by $\lambda$ and $N_{t+1}/N_t=\lambda$ (slide: 1.05082, proportions 0.635, 0.302, 0.057, 0.005). State primitivity if asked for the full condition.
> 10. The distribution predicts decline: older trees die with no replacement, so the stand will thin and then vanish unless seedlings establish. The explanation (seedlings need floods to clear bare, moist soil; dams removed floods) suggests an intervention: **managed flood releases**, rather than planting.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | ecology, populations, why study | [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=1\|sl. 1–8]] | taught |
> | cohort life table, Phlox, $R_0$ | [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=9\|sl. 9–10]]; Molles §10.3 | taught |
> | survivorship curves, log axis | [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=11\|sl. 11–13]]; Molles §10.3 | taught |
> | Leslie matrix, SAD, $\lambda$, Perron-Frobenius | [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=14\|sl. 14–21]] | taught |
> | stage matrix, loggerhead, sensitivity, TEDs | [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=22\|sl. 22–28]] | taught |
> | age pyramids; age distributions; humans | [[02_StageStructuredDynamics_11-Aug-2026.pdf#page=29\|sl. 29]]; Molles §10.4, §11.4 | taught |
> | geometric growth of Phlox | Molles §11.1 | taught (used again in EE03) |
> | the model, Tables 1–3, Fig. 4–5, Appendix | Crowder et al. 1994 (paper) | extra/book |
> | irreducible/primitive, ergodicity, sensitivity | Caswell 1997 (paper) | extra/book |
> | temperature; biogeochemical cycles | Begon and Townsend §2.3.1–2.3.4; Spellman Ch. 2 (self-study, slide 3) | extra/book |
> | WPP 2024; India | UN key messages; *Data for India* (not on the reading slide) | extra/book |
> | generation time, Euler-Lotka; damping ratio; elasticity table; reproduction of Crowder's figures; replacement and momentum | computed here (`scripts/ee02_numbers.py`, `fig_ee02_*.py`) | extra/beyond |
>
> **Reading slide.** Slide 31 lists Molles §10.3–10.4 and Ch. 11 as mandatory and Crowder and Caswell as papers. The folder also holds WIRED's article on undersea sculptures against illegal trawlers and the *Interesting Links* file (pyramid links); neither is on the reading slide.
>
> **Checks.** My Leslie simulation reproduces slides 16–20 to every printed digit ($\lambda=1.05082$, proportions 0.634921/0.302108/0.057499/0.005472). The Crowder matrix rebuilt from Table 1 matches Table 2 to within 0.003, gives $\lambda=0.9516$ and the paper's Table 3, and reproduces the bars of Fig. 4 to about ±0.002 and the TED times (67 and 33 yr versus about 70 and about half).
>
> **Transcription notes.** (1) The slide's $R_0=2.4177$ versus 2.4176 from the printed columns is rounding. (2) The slides index classes 1–4 in the matrix and 0–3 in the plots. (3) Crowder's Fig. 2 survival elasticities sum to about 1.6 (they hold $\lambda$ fixed inside the stage-duration formula); mine sum to 1 (see §5.4). (4) The PDFs of Molles and Crowder have an unusable text layer; the text here comes from OCR of the page images.

**References.** Crowder, L. B., Crouse, D. T., Heppell, S. S. & Martin, T. H. (1994) *Ecological Applications* 4, 437–445 · Crouse, D. T., Crowder, L. B. & Caswell, H. (1987) *Ecology* 68, 1412–1423 · Caswell, H. (1997) in Tuljapurkar & Caswell (eds) *Structured-Population Models in Marine, Terrestrial and Freshwater Systems*, ch. 2 · Caswell, H. (1989) *Matrix Population Models* · Lefkovitch, L. P. (1965) *Biometrics* 21, 1 · Leslie, P. H. (1945) *Biometrika* 33, 183 · Leverich, W. J. & Levin, D. A. (1979) *Am. Nat.* 113, 881 · Molles, M. C. (2022) *Ecology: Concepts and Applications*, 9th ed., §10.3–10.4 and Ch. 11 · Murie, A. (1944) *The Wolves of Mount McKinley* · Miller, R. B. (1923) *Illinois Nat. Hist. Surv. Bull.* 14 · Grant, P. R. & Grant, B. R. · Begon, M. & Townsend, C. R. *Ecology: Individuals to Ecosystems*, §2.3 · Spellman, F. R. (2008) *Ecology for Non-ecologists*, ch. 2 · UN DESA (2024) *World Population Prospects 2024: Summary of Results* · Rukmini S. (2024) *Data for India*, "Population growth in India".
