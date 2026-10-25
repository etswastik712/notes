---
title: Eco-Evo Problem Bank
aliases: [Eco-evo problems, BI2113 problem bank]
subject: eco-evo
type: problems
scope: [taught, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/problems, taught, extra/beyond, src/slides, src/own-notes, status/draft]
---
# Eco-Evo Problem Bank

◀ [[Ecology and Evolution - Course Map|Course Map]] · [[Eco-Evo Exam Prep|Exam Prep]] · chapters [[EE02 Structured Population Models|EE02]] · [[EE03 Population Dynamics and Chaos|EE03]] · [[EE04 Competition and Invasions|EE04]] · [[EE05 Predation|EE05]] · [[EE06 Eutrophication and Alternative Stable States|EE06]] · [[EE07 Conservation Biology|EE07]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] What is here
> 25 calculation problems that **mix** the chapters' methods and use **new numbers** (each chapter's own *Practice* section has the standard exercises). Every answer is computed by `scripts/ee_problem_bank.py` and printed there. Problems and numbers are my own constructions (🔵 as exercises), but each uses only methods that are 🟢 taught or labelled in the chapter, and the tag after each title says which.
>
> Sections: **A** structured populations · **B** growth, Ricker, Hassell · **C** competition · **D** predation · **E** lakes · **F** conservation · **G** mixed. Try each problem with the **solution folded**; units are years unless stated.

> [!key] Method cards (the formulas you need)
> $R_0=\sum l_xm_x$, $T=\sum xl_xm_x/R_0$ · $\mathbf n_{t+1}=\mathbf A\mathbf n_t$, $e_{ij}=(a_{ij}/\lambda)v_iw_j/\mathbf v\!\cdot\!\mathbf w$ · $g'(K)=1-r$ (Ricker), $f'=1-\beta(1-\lambda^{-1/\beta})$ (Hassell) · isocline intercepts $K_i$, $K_i/\alpha_{ij}$ · $R^*=mk/(\mu-m)$ · $H^*=m/ap$, $P^*=r/p$ · $p^*=1-e/c$ · $P_L=1.55[P_{in}/(1+\sqrt{\tau_w})]^{0.82}$ · $\dot x=a-bx+rx^p/(x^p+h^p)$ · $P_{ext}=(d/b)^{N_0}$ · $\hat N=Mn/m$ · $N_e=4N_mN_f/(N_m+N_f)$. Full list: [[Eco-Evo Exam Prep]] §1.

## A. Structured populations
**A1. Life table (EE02 §2).** A cohort of 1,000 newborns is followed through four age classes ($x=0,1,2,3$): survivors $n_x=1000,\ 600,\ 300,\ 100$; offspring per individual alive in the class $m_x=0,\ 1.5,\ 2.0,\ 1.0$. (a) Find $l_x$ and $R_0$. (b) Find the generation time $T$ and the approximation $r\approx\ln R_0/T$. (c) Solve the Euler-Lotka equation $1=\sum l_xm_xe^{-rx}$ for $r$ and $\lambda=e^r$; compare. (d) Is the mortality per class constant, and what does that say about the survivorship type?

> [!example]- Solution A1
> (a) $l=(1,\,0.6,\,0.3,\,0.1)$; $l_xm_x=(0,\,0.9,\,0.6,\,0.1)$, so $R_0=1.6$. (b) $T=(1\times0.9+2\times0.6+3\times0.1)/1.6=2.4/1.6=1.5$; $r\approx\ln1.6/1.5=0.313$. (c) Solving $0.9e^{-r}+0.6e^{-2r}+0.1e^{-3r}=1$ gives $r=0.3259$, $\lambda=1.385$; the approximation is 4 % low in $r$ (it is exact only for a narrow reproductive age window). (d) Per-class mortality $q=1-n_{x+1}/n_x=0.40,\ 0.50,\ 0.67$ **rises with age**, so the curve is nearer type I (late mortality) than the straight line of type II. 🔵 for $T$ and Euler-Lotka (EE02 §2).

**A2. A three-class Leslie matrix (EE02 §4).** $\mathbf L=\begin{pmatrix}0&1.5&1.0\\0.6&0&0\\0&0.5&0\end{pmatrix}$. (a) Write the characteristic equation and find $\lambda$. (b) Find the stable age distribution and the reproductive values (scaled so $v_0=1$). (c) Compute $\mathbf n_t$ for $t=1,\dots,6$ from $\mathbf n_0=(100,0,0)$. (d) Check $\lambda>1\iff R_0>1$ with $R_0=F_1s_0+F_2s_0s_1$. (e) Culling removes 30 % of the survivors of the first class each step ($s_0=0.6\to0.42$): new $\lambda$?

> [!example]- Solution A2
> (a) $\lambda^3=0.9\lambda+0.3$, giving $\lambda=1.0847$. (b) SAD $=(0.553,\ 0.306,\ 0.141)$; $\mathbf v=(1,\ 1.81,\ 0.92)$: the middle class is worth most, because it is about to breed with high fecundity and the oldest class has little time left. (c) Totals $60,\ 120,\ 84,\ 126,\ 111.6,\ 138.6$: strongly oscillating transients (the age classes at $t=1$: $(0,60,0)$; $t=2$: $(90,0,30)$ …) that damp towards growth at 1.0847. (d) $R_0=1.5\times0.6+1.0\times0.6\times0.5=1.2>1$ and $\lambda>1$: consistent. (e) $\lambda=0.926<1$: the cull turns a growing population into a declining one, even though $R_0$ only falls from 1.2 to $1.5\times0.42+0.21=0.84$.

**A3. Where to act? (EE02 §5).** A threatened species has three stages with $\mathbf A=\begin{pmatrix}0.30&0&2.0\\0.20&0.50&0\\0&0.20&0.70\end{pmatrix}$ (juvenile, subadult, adult; fecundity $F_3=2.0$ into the juvenile class). (a) Find $\lambda$ and how long it takes to lose half and 90 % of the population. (b) Find the elasticity of every non-zero entry. Which *stage* (the sum over what it does) matters most? (c) By how much must each single entry rise for $\lambda=1$? (d) Compare: fecundity $+25$ %; both growth entries $G_1,G_2$ each $+0.1$; adult stay $+0.05$.

> [!example]- Solution A3
> (a) $\lambda=0.9618$ ($-3.8$ %/yr): half after $\ln0.5/\ln0.9618=17.8$ yr, 90 % lost after 59.1 yr. (b) Elasticities: $P_1=0.063$, $G_1=0.139$, $P_2=0.150$, $G_2=0.139$, $P_3=0.371$, $F_3=0.139$ (sum 1.00). By stage: juvenile $0.20$, subadult $0.29$, adult $0.51$. **Adults** matter most (proportionally), so survival of the long-lived stage is the lever, as for the loggerhead's large juveniles. (c) Rises needed for $\lambda=1$: $P_3$ $+0.071$ (to 0.771); $G_1$ or $G_2$ $+0.062$; $P_2$ $+0.119$; $P_1$ $+0.167$; $F_3$ $+0.625$ (to 2.625, **+31 %**). (d) Fecundity $+25$ %: $\lambda=0.993$ (not enough); fecundity doubled: 1.067; $G_1$ and $G_2$ each $+0.1$: 1.088; $P_3+0.05$: 0.988. **Lesson:** protecting births alone is the weakest action; a small gain in survival or growth through the middle stages beats a large gain in fecundity. Elasticity ranks *proportional* effects; what can actually be changed (c) decides the action. 🔵 numbers, method 🟢/🟡.

**A4. Doubling and momentum (EE02 §6).** A country grows at $r=0.012$ yr$^{-1}$. Doubling time, factor over 50 years, and $\lambda$?

> [!example]- Solution A4
> $t_d=\ln2/0.012=57.8$ yr; $e^{0.6}=1.82$ after 50 yr; $\lambda=e^{0.012}=1.0121$.

## B. Growth, Ricker and Hassell
**B1. Logistic harvest (EE03 §4).** $r=0.4$ yr$^{-1}$, $K=500$, $N_0=20$. (a) When does the population reach $K/2$? (b) $N(10)$? (c) Maximum growth rate and where? (d) A constant harvest $H=20$, $40$, $50$ or $55$ per year is taken. Find the equilibria and say what happens to a stock that starts at 100 with $H=40$.

> [!example]- Solution B1
> (a) $t=\ln(480/20)/0.4=7.95$ yr. (b) $N(10)=500/(1+24e^{-4})=347.3$. (c) $rK/4=50$ at $N=250$. (d) Equilibria solve $rN(1-N/K)=H$: $H=20$: 56.4 (unstable) and 443.6 (stable); $H=40$: 138.2 and 361.8; $H=50$: 250 (a single, semi-stable point); $H=55$: none, so the stock collapses. A stock of 100 with $H=40$ is below 138.2 and declines to zero: **a constant-quota harvest has an extinction threshold even in the plain logistic**, and the maximum sustainable quota is exactly $rK/4=50$.

**B2. What does the Ricker model do? (EE03 §5).** $K=100$. For $r=0.8,\ 1.5,\ 2.2,\ 2.6,\ 2.8,\ 3.0$, predict the behaviour from $g'(K)=1-r$ and the bifurcation values, then check against long runs.

> [!example]- Solution B2
> | $r$ | $g'(K)$ | behaviour (long run) |
> |---|---|---|
> | 0.8 | $+0.2$ | monotone approach to 100 |
> | 1.5 | $-0.5$ | damped oscillation to 100 |
> | 2.2 | $-1.2$ | 2-cycle: 49.7 and 150.3 |
> | 2.6 | $-1.6$ | 4-cycle: 18.1, 39.1, 152.3, 190.5 |
> | 2.8 | $-1.8$ | chaos, $\Lambda=0.24$, range 8-216 |
> | 3.0 | $-2.0$ | chaos, $\Lambda\approx0.39$ (0.386 in long runs), range 3-246 |
>
> $|g'(K)|<1$ for $0<r<2$; the 4-cycle needs $2.5265<r<2.6564$, and 2.6 lies inside it; for $r=2.8$ and $3$ the orbit never repeats and has a positive Lyapunov exponent. $\Lambda(2.2)=-0.77$ confirms a stable cycle.

**B3. When is the Hassell model unstable? (EE03 §6).** $f'(N^*)=1-\beta(1-\lambda^{-1/\beta})$. (a) $\lambda=4$: $f'$ for $\beta=1,2,6,50,1000$. (b) The same for $\lambda=20$. (c) For $\lambda=20$, at what $\beta$ does $f'=-1$? (d) What $\lambda$ is the minimum for instability at *any* $\beta$?

> [!example]- Solution B3
> (a) $0.25,\ 0,\ -0.238,\ -0.367,\ -0.385$: always stable; as $\beta\to\infty$, $f'\to1-\ln\lambda=-0.386$. (b) $0.05,\ -0.553,\ -1.358,\ -1.908,\ -1.991$: unstable for large $\beta$. (c) $\beta_c=3.44$. (d) $f'\to1-\ln\lambda<-1$ requires $\ln\lambda>2$, so $\lambda>e^2=7.39$. For $\beta=1$ (the Beverton-Holt case) $f'=1/\lambda>0$: **never oscillatory**, which is why the "natural populations are simple" result is not a statement about $\lambda$ alone but about the **shape** of density dependence.

**B4. How far ahead can we forecast? (EE03 §5).** For $\Lambda=0.39$, range 100 and initial error $\delta_0=0.01$: horizon? If the measurement is made 100 times more precise?

> [!example]- Solution B4
> $\ln(100/0.01)/0.39=23.6$ generations. A hundred-fold better data adds only $\ln100/0.39=11.8$ generations (total 35.4). **Precision buys additive, not multiplicative, forecast time.**

## C. Competition
**C1. Three outcomes from isocline intercepts (EE04 §4).** $K_1=200$, $K_2=150$, $r_1=r_2=0.5$. For each case (i) $\alpha_{12}=0.6,\ \alpha_{21}=0.9$; (ii) $0.6,\ 0.5$; (iii) $1.6,\ 0.9$: give the outcome, the interior point, and (if it exists) its stability.

> [!example]- Solution C1
> Thresholds: $\alpha_{12}<K_1/K_2=1.333$ and $\alpha_{21}<K_2/K_1=0.75$ for coexistence. (i) $\alpha_{21}=0.9>0.75$ but $\alpha_{12}=0.6<1.333$: **species 1 wins**. Note $\alpha_{12}\alpha_{21}=0.54<1$, so the product test alone would wrongly predict coexistence; the interior point $(239,\,-65)$ has $N_2<0$ and is not feasible. (ii) both below: coexistence at $(157.1,\ 71.4)$, eigenvalues $-0.50,\ -0.131$: stable node. (iii) $\alpha_{12}=1.6>1.333$ and $\alpha_{21}=0.9>0.75$ (product 1.44): **priority effect**; interior point $(90.9,\ 68.2)$ is a saddle (eigenvalues $+0.046,\ -0.50$) and the winner depends on the start. (EE04 §4; [[Lotka-Volterra Competition Model]].)

**C2. The fast grower loses (EE04 §3).** $m=0.1$ day$^{-1}$. Species A: $\mu=1.5$, $k=8$; species B: $\mu=0.9$, $k=1$. (a) $R^*$ of each. (b) Growth rates at $R=20$ and $R=1$. (c) At what $R$ do the growth curves cross? (d) In a chemostat with inflow 20 who wins, and what is B's equilibrium (yield 1)?

> [!example]- Solution C2
> (a) $R^*_A=0.1\times8/1.4=0.571$; $R^*_B=0.1\times1/0.8=0.125$. (b) At 20: A 1.071, B 0.857; at 1: A 0.167, B 0.450. (c) Equal at $R=9.5$: A grows faster above it. (d) **B wins** (lower $R^*$) even though A is faster whenever food is plentiful; $N_B^*=20-0.125=19.875$. A cannot grow at 0.125 (growth $1.5\times0.125/8.125=0.023<0.1$). (Tilman; [[Tilman R-Star Rule]].)

**C3. Niche overlap (EE04 §6, 🔵).** With $\alpha=\exp(-d^2/4\sigma^2)$, find $d/\sigma$ giving $\alpha=0.5,\ 0.25,\ 0.1$, and $\alpha$ at $d/\sigma=0.5,1,2,3$.

> [!example]- Solution C3
> $d/\sigma=2\sqrt{-\ln\alpha}=1.665,\ 2.355,\ 3.035$. $\alpha=0.939,\ 0.779,\ 0.368,\ 0.105$. Overlap falls quickly: species separated by two niche widths compete about a third as strongly as identical species.

## D. Predation
**D1. Equilibria and cycles (EE05 §3).** $r=0.8$, $p=0.01$, $a=0.4$, $m=0.6$. (a) $H^*,\ P^*$ and the small-cycle period. (b) Double $r$. (c) A pesticide adds a death rate $0.2$ to both species. (d) On the orbit through $(H,P)=(100,40)$, what is conserved and what are the ranges?

> [!example]- Solution D1
> (a) $H^*=0.6/(0.4\times0.01)=150$, $P^*=80$, $T=2\pi/\sqrt{0.48}=9.07$. (b) $P^*=160$, $H^*$ unchanged at 150: extra prey production is eaten by more predators. (c) $r\to0.6$, $m\to0.8$: $H^*=200$ (up), $P^*=60$ (down): Volterra's principle. (d) $V=apH-m\ln H+pP-r\ln P=-4.9142$ throughout; $H$ swings between 58.7 and 306.8, $P$ between 36.1 and 150.1.

**D2. Adding a carrying capacity (EE05 §4).** In D1 let prey be logistic with $K=300$. $P^*$, stability, period. What if $K=150$?

> [!example]- Solution D2
> $P^*=80\,(1-150/300)=40$. Jacobian $\begin{pmatrix}-0.4&-1.5\\0.16&0\end{pmatrix}$ has eigenvalues $-0.2\pm0.447i$: a **stable spiral**, period 14.05, amplitude shrinking by $e$ every 5 time units. For $K=150=H^*$ the predator equilibrium is $0$ ($K$ must exceed $m/ap=150$): the prey cannot feed a predator, which dies out.

**D3. Handling time (EE05 §6, 🟡).** A predator has $a=0.05$ per prey per day and handling time $h=0.2$ day. Compute the kill rate and the fraction of the prey density removed per predator per day for $N=2,\ 10,\ 40,\ 100,\ 400$. Max rate? Half-saturation? What does the trend of the fraction imply for stability?

> [!example]- Solution D3
> Rate $aN/(1+ahN)$: $0.098,\ 0.455,\ 1.429,\ 2.500,\ 4.000$; fraction $=\text{rate}/N$: $0.049,\ 0.0455,\ 0.0357,\ 0.025,\ 0.010$. Maximum $1/h=5$ per day; half-saturation $N=1/(ah)=100$. A **falling fraction** is inversely density-dependent mortality, destabilising: predation relaxes exactly when prey are plentiful. The linear (type I) rule $aN$ would give 5 at $N=100$ instead of 2.5.

**D4. Metapopulations (EE05 §5, 🔵).** Levins' model with $c=0.5$, $e=0.2$. (a) $p^*$. (b) Predators raise local extinction to $e=0.3,\ 0.4,\ 0.5$: $p^*$? (c) Destroy a fraction $D$ of patches: $p^*$ for $D=0.2,\ 0.4,\ 0.6$ and the threshold.

> [!example]- Solution D4
> (a) $p^*=1-0.2/0.5=0.60$. (b) $0.40,\ 0.20,\ 0$: at $e=c$ the metapopulation vanishes. (c) $p^*=1-D-e/c=0.40,\ 0.20,\ 0$: threshold $D=0.6$. When 40 % of patches are gone, the metapopulation occupies only 20 % of the original network, a third of the starting 60 %.

## E. Lakes
**E1. Retention time (EE06 §3).** $P_L=1.55[P_{in}/(1+\sqrt{\tau_w})]^{0.82}$ (µg L⁻¹). For $P_{in}=60$ and 30 µg L⁻¹ and $\tau_w=0.5,\ 4,\ 25$ yr, compute $P_L$ and classify (< 5, 5-10, 10-30, 30-100, > 100). What happens when $P_{in}$ is halved? What $P_{in}$ gives $P_L=10$ for $\tau_w=4$?

> [!example]- Solution E1
> | $\tau_w$ | $P_{in}=60$ | $P_{in}=30$ |
> |---|---|---|
> | 0.5 | 28.7 (meso) | 16.3 (meso) |
> | 4 | 18.1 (meso) | 10.2 (meso, on the boundary) |
> | 25 | 10.2 (meso, boundary) | 5.8 (oligo) |
>
> Halving $P_{in}$ multiplies $P_L$ by $0.5^{0.82}=0.566$, a bit less than half. For $P_L=10$ at $\tau_w=4$: $P_{in}=(10/1.55)^{1/0.82}\times3=29.1$. A slowly flushed lake is *less* productive per unit load: retention time acts through settling.

**E2. Hysteresis in the Box 1 model (EE06 §6, 🟡/🔵).** $\dot x=a-bx+rx^8/(x^8+1)$ with $b=1$, $r=1.4$ ($x$ = turbidity, $a$ = loading). (a) Where are the folds and the bistable window? (b) Equilibria for $a=0.2,\ 0.5,\ 0.7$. (c) A clear lake at $a=0.5$ is pushed to $a=0.7$ and then relaxed. Trace $x$ when $a$ returns to 0.5, 0.2 and 0.03. (d) How large a relative cut in loading restores clarity?

> [!example]- Solution E2
> (a) Folds at $x=0.723$ and $1.268$; bistable for $0.050<a<0.626$. (b) $a=0.2$: $0.2,\ 1.06,\ 1.561$ (clear, unstable, turbid); $a=0.5$: $0.506,\ 0.886,\ 1.892$; $a=0.7$: only $2.096$ (turbid). (c) At $0.7$ the lake is at $x=2.096$; at $a=0.5$ it stays at $1.892$; at $0.2$ at $1.561$ (still turbid); only at $a=0.03$ does it fall to $0.03$. (d) The forward switch is at $a=0.626$ and the return at $0.050$: a cut of $1-0.050/0.626=92$ % of the loading that caused the collapse.

## F. Conservation
**F1. Founders (EE07 §4, 🔵).** A colony has per-capita birth $b=1.2$ and death $d=1.0$. (a) $P_{ext}$ for $N_0=1,\ 2,\ 5,\ 10,\ 25$. (b) How many founders for $P_{ext}<1$ %? (c) The same for $b=1.05$ and $b=2$.

> [!example]- Solution F1
> $P_{ext}=(d/b)^{N_0}=0.833,\ 0.694,\ 0.402,\ 0.162,\ 0.0105$. For $<1$ %: $N_0>\ln0.01/\ln(1/1.2)=25.3$, i.e. **26** founders (0.87 %). With $b=1.05$: 95; $b=1.5$: 12; $b=2$: 7. A weakly growing species needs many more founders: why propagule pressure matters for invasions and re-introductions.

**F2. Harvesting with an Allee effect (EE07 §4, 🔵).** $f(N)=rN(N/A-1)(1-N/K)$ with $r=0.5$, $A=20$, $K=100$. (a) Maximum sustainable constant harvest? (b) Equilibria for $H=10,\ 20,\ 30$. (c) What happens at $H=20$ if the stock is 50? (d) Growth of 10 animals?

> [!example]- Solution F2
> (a) $\max f=26.26$ at $N=70.6$. (b) $H=10$: 37.1 (unstable) and 94.3; $H=20$: 52.05 and 85.85; $H=30$: none (above the maximum). (c) 50 is below 52.05, so the stock declines to zero although 20 is below the maximum: **the safe zone is bounded below by an unstable equilibrium that moves up with $H$**. (d) $f(10)=-2.25$ per year (per capita $-0.225$): the Allee effect makes growth negative.

**F3. Counting (EE07 §7).** 80 animals are marked; a later sample of 60 contains 12 marked. (a) Lincoln-Petersen and Chapman estimates with 95 % interval. (b) The sample had 4 marked: same estimates.

> [!example]- Solution F3
> (a) $\hat N_{LP}=80\times60/12=400$; Chapman $=81\times61/13-1=379.1$, $SE=82.6$, interval 217-541. (b) $\hat N_{LP}=1200$; Chapman 987, $SE=374$, interval 253-1721. **Few recaptures give estimates that are huge and uncertain**; plan the survey so that $m$ is not small.

**F4. Camera traps (EE07 §7, 🟡/🔵).** Per-occasion capture probability $p$, $K$ occasions, $C$ animals detected. (a) $p=0.15$, $K=8$, $C=44$: $\hat N$? (b) $p=0.05$, $K=8$. (c) $p=0.15$, $K=30$.

> [!example]- Solution F4
> Overall detection $p^*=1-(1-p)^K$: (a) 0.7275 so $\hat N=44/0.7275=60.5$; (b) 0.3366 so $\hat N=130.7$; (c) 0.9924 so $\hat N=44.3$. The correction is large when detection is poor: with $p=0.05$ the raw count is a third of the estimate. Longer surveys shrink the correction but run into the closure assumption (30-60 days in tiger surveys).

**F5. Drift (EE07 §4, 🔵).** A reserve holds 5 breeding males and 45 breeding females. (a) $N_e$? (b) Heterozygosity retained after 20 generations; compare with the census-size calculation. (c) Half-life in generations? (d) $N_e$ for 25+25 and 1+49.

> [!example]- Solution F5
> (a) $N_e=4\cdot5\cdot45/50=18$ (census 50). (b) $(1-1/36)^{20}=0.569$ against $0.818$ if the census size were used. (c) $\ln2/(-\ln(1-1/36))=24.6$ generations. (d) 25+25: 50; 1+49: 3.9. **A skewed sex ratio can cut the effective size by a factor of three or more.**

**F6. Tiger trend (EE07 §6, 🔵).** 1,706 (2011) and 2,967 (2018; CI 2,603-3,346). Growth rate and doubling time; relative half-width of the CI; minimum increase on 2011.

> [!example]- Solution F6
> $r=\ln(2967/1706)/7=0.0791$ yr$^{-1}$, doubling 8.8 yr; $\pm12.5$ %; even at the lower bound 2,603 the count is at least $1.53\times$ the 2011 figure. Using the ends of the 2018 interval alone, $r$ runs from $0.060$ (doubling 11.5 yr) to $0.096$ (7.2 yr): the rate is only as certain as the counts, and the 2011 count has its own error.

## G. Mixed problems
**G1. Which lake intervention works? (EE06 §6-7).** In the Box 1 model of E2 a lake sits turbid ($x=1.733$) at loading $a=0.35$. Options: (i) wait; (ii) cut $a$ to 0.20; (iii) cut $a$ to 0.03; (iv) a one-off biomanipulation that removes planktivorous fish and cuts turbidity temporarily. What does each do, and how large must (iv) be?

> [!example]- Solution G1
> At $a=0.35$ the equilibria are $0.35$ (clear), $0.973$ (unstable) and $1.733$ (turbid). (i) stays turbid. (ii) at $a=0.2$ the turbid branch is still at $1.561$: no recovery. (iii) at $a=0.03$ clear branch only: recovery after a 91 % cut. (iv) the push must carry $x$ below the unstable point $0.973$, a 44 % reduction of turbidity: from $0.923$ the lake relaxes to $0.35$, from $1.023$ back to $1.733$. **Biomanipulation is a threshold-crossing push, and it persists only if the loading is within the bistable window.**

**G2. Harvesting a chaotic population (EE03 §7, EE07; 🔵).** $N_{t+1}=(1-h)N_te^{r(1-N_t/K)}$ with $r=2.8$, $K=100$ (chaotic if $h=0$). Show that the equilibrium is $N^*=K(1+\ln(1-h)/r)$, find the harvest fraction $h$ above which it is stable, and test $h=0.3,\ 0.55,\ 0.6,\ 0.7$.

> [!example]- Solution G2
> $g(N)=(1-h)Ne^{r(1-N/K)}$; $g(N^*)=N^*$ gives $r(1-N^*/K)=-\ln(1-h)$, i.e. $N^*=K(1+\ln(1-h)/r)$. $g'(N^*)=1-rN^*/K=1-r-\ln(1-h)$; stability needs $-1<g'$, i.e. $\ln(1-h)<2-r$, so $h>1-e^{2-r}=1-e^{-0.8}=0.551$. Tests: $h=0.3$: $N^*=87.3$, $g'=-1.44$, 2-cycle (146.8, 27.7); $h=0.55$: $g'=-1.001$, a 2-cycle (74.9, 68.1) just at the threshold; $h=0.6$: $N^*=67.3$ stable; $h=0.7$: $N^*=57.0$, $g'=-0.60$, stable, with equilibrium catch $hN^*/(1-h)=133$. **Strong harvesting can stabilise a chaotic stock**, but a low-to-moderate harvest rate leaves it cycling.

## Provenance
> [!provenance]- Source map
> Problems are my own; the methods and data come from the chapters named in each heading, and every numerical answer is produced by `scripts/ee_problem_bank.py` (run it to see the full output). Conventions follow the chapters ($\alpha_{ij}$ = effect of $j$ on $i$; $\mathbf v$, $\mathbf w$ left and right eigenvectors; Ricker $g'(K)=1-r$). Not used as a source for any number: the earlier AI notes in `biology/eco-evo/_progress/`.
