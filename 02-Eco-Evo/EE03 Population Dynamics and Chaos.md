---
title: EE03 Population Dynamics and Chaos
aliases: [EE03, Population dynamics, Simple models, Chaos in ecology, BI2113 lecture 3]
subject: eco-evo
type: chapter
chapter: 3
part: II
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE02 Structured Population Models]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/paper, src/own-notes, status/draft]
---
# EE03 · Population Dynamics and Chaos

◀ [[EE02 Structured Population Models]] · [[Ecology and Evolution - Course Map|Course Map]] · [[EE04 Competition and Invasions]] ▶

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture of 18 Aug 2026 ([[04_PopDyn_Chaos_18Aug_2026.pdf|37 slides]]) and the six practice sums in [[Pop Dyn_Practise sums.docx]]
> - §1 predicting numbers: the locust record (sl. 1–4)
> - §2 models and Rosen's modelling relation (sl. 5–7)
> - §3 exponential growth, "the first law of population dynamics" (sl. 8–16)
> - §4 density dependence and the logistic model; the four forms of the realised rate; empirical checks (sl. 17–23)
> - §5 the Ricker model, period doubling, chaos, fractals (sl. 24–26)
> - §6 the real world: the Hassell model and the puzzle (sl. 27–30)
> - §7 taming chaos: the lattice effect and model complexity (sl. 31–35)
> - §8 references and reading tiers (sl. 36–37)
>
> 🟡 **Extra · book** (the *paper* tier, the *detailed reading* tier and the "fun" extract: no exam weight)
> - §5 May (1976), *Nature* 261: the logistic map, the cascade of cycles, Table 4 for the Ricker equation
> - §7 Turchin and Taylor (1992), *Ecology* 73: response-surface reconstruction of dynamics from time series
> - §5 Crichton, *Jurassic Park* extracts on sensitive dependence and fractals ("fun")
> - not read in detail: Rockwood, *Introduction to Population Ecology*, Ch. 1–2 (a 65-page scan) and Dey and Joshi (unpublished, not in the folder)
>
> 🔵 **Extra · beyond** (my additions, labelled)
> - §3 Fibonacci's rabbits as a Leslie matrix; §4 the delayed logistic; the discrete logistic as the logistic map
> - §5 stability slopes for all four models, Lyapunov exponents, the Feigenbaum ratio, cobweb diagrams
> - §6 the stability map of the Hassell model; §7 integerised cycle lengths and a delayed-density-dependence example

> [!key] After this chapter you can
> - explain what a model is (Rosen's **modelling relation**) and why the course uses *oversimplified* ones,
> - derive **exponential growth** (discrete and continuous), the link $\lambda=e^{r}$, and solve the doubling-time problems,
> - derive the **logistic** model from a linearly falling realised growth rate and solve it,
> - write the **Ricker** model, find when its equilibrium is stable, and describe **period doubling**, **chaos** and **sensitive dependence**,
> - read a **bifurcation diagram** and say what its self-similarity means,
> - state the **Hassell-model puzzle** (simple models allow chaos; data show simple dynamics) and its two resolutions: the **lattice effect** and **model complexity**.

## 1. Predicting numbers is an old problem
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=1|slides 1–4]]*

Slide 1: *predicting changes in population numbers has been a BIG question for humans for a very long time.* The earliest known written record of **locusts** is on an ox bone in Oracle Script (Jiaguwen) about 3,500 years ago and asks: "Will locusts appear in the field; will it not rain?" The slide plots a reconstructed **1,910-year** locust index (A.D. 2 to 1911; Tian et al., *PNAS* 2011, log-transformed index, not numbers): it rises and falls irregularly, with outbreaks.

Slide 2 asks the question that drives the lecture: *but nature is complex… so what do we do?* The answer, slide 3: study **simple models**, in this order: exponential growth → logistic growth → limit cycles and chaos → *amelioration of chaos*. Slide 4 places the topic on the "domain of BI2113" ladder: this lecture is about **populations**, treating one population's total size $N$ and ignoring its structure (which EE02 added back).

> [!intuition] Why simple models, if nature is complex?
> A road map leaves out the trees and the potholes and is still the right tool for deciding which way to drive. A simple model keeps a handful of the *causes* of change and sees what they imply on their own. If the implication is wrong, you have learnt which cause was missing. That is the logic of EE01's "breadth over depth" and of [[Strong Inference]]: the model is a question put to nature.

## 2. Models and the modelling relation
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=5|slides 5–7]]*

Slides 5–7 use **Robert Rosen's modelling relation** (Fig. 1 of Simeonov 2010) to say what a model is ([[Modelling Relation]]).

![[fig_ee03_rosen.png|620]]
*Figure EE3.1. Rosen's modelling relation (slide 7). The natural system $N$ is linked by encoding $\varepsilon$ to a formal system $F$; $c$ is causal entailment in nature, $i$ is inferential entailment in the formalism, $\delta$ is decoding.*

> [!key] The loop
> A **natural system** $N$ has causes and effects (causal entailment $c$). We **encode** ($\varepsilon$) some of it into a **formal system** $F$ (an equation); inside $F$ we **infer** ($i$) consequences by calculation; we **decode** ($\delta$) the answer back into a prediction about $N$. A model is good when going round the loop, $\varepsilon\to i\to\delta$, agrees with what nature does along $c$. Slide 6 labels the four arrows: ① causation, ② observation, analysis and encoding, ③ inference, ④ prediction, synthesis and decoding.

> [!example] Exponential growth on the loop
> *Encode:* count the population, $N_0=996$ plants, and estimate a net per-capita rate $R=b-d+i-e$. *Infer:* in $F$, $N_{t+1}=N_t(1+R)$ gives $N_t=(1+R)^tN_0$. *Decode:* "in 8 years there will be about a million plants". *Check:* compare with counts. If they disagree, the failure is in $\varepsilon$ (a variable was dropped: space, food, age structure) or in $i$ (the equation form), never in the arithmetic. EE02's *Phlox* projection (Worked example 2 there) is exactly such a failed check.

> [!connection] Where this idea has come up before
> The loop is the vault's recurring picture of science: a nomothetic formal system on one side, an idiographic world on the other ([[Nomothetic versus Idiographic Science]]); the zero-dimensional energy balance of [[CL01 Earth as a System]] is an $\varepsilon$ that deliberately drops almost everything. The lattice effect (§7) is a case where an *encoding* (real-valued $N$) hides a property of the world (whole animals).

## 3. Exponential growth: "the first law of population dynamics"
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=8|slides 8–16]]* · *[[Pop Dyn_Practise sums.docx|practice sums]]*

Slide 8 credits **Leonardo Pisano (Fibonacci, 1170–1250)** as the earliest modeller in ecology. Slide 9 states the first law:

$$N_{t+1}=N_t+N_t\,(b-d+i-e)\quad\Longrightarrow\quad N_t=\lambda^{t}N_0,\qquad \lambda=1+(b-d+i-e)$$

where $b,d,i,e$ are per-capita birth, death, immigration and emigration rates per time step ([[Exponential Growth]]). Slide 10 gives the steps: $N_1=\lambda N_0$, $N_2=\lambda N_1=\lambda^2N_0$, …, $N_t=\lambda^tN_0$.

> [!key] Why a "law"?
> Slide 11: the equation "**gives the behaviour of a population in the absence of any external influence** (cf. Hardy-Weinberg, the first law of motion)", and "the **subject develops by studying departures from the assumptions**". Newton's first law describes a body acted on by no force; real motion is then explained by the forces. The exponential law describes a population with nothing limiting it; real dynamics are then explained by what limits it (food, space, predators, structure, noise). This is the template for the whole subject.

### 3.1 The continuous-time version
Slide 12–13: let the change per unit time be proportional to $N$,

$$\frac1N\frac{dN}{dt}=r\ \Longrightarrow\ \int\frac{dN}{N}=\int r\,dt\ \Longrightarrow\ \ln N=rt+C\ \Longrightarrow\ N=N_0e^{rt}$$

(with $N_0=e^{C}$ from $t=0$). Comparing with $N_t=\lambda^tN_0$ at integer times: $e^{rt}=\lambda^{t}$, i.e.

$$\boxed{\lambda=e^{r},\qquad r=\ln\lambda}$$

Slide 14 writes this "for a sufficiently small value of $t$".

> [!pitfall] What "sufficiently small" is doing on slide 14
> $\lambda=e^{r}$ is exact: it just says one time step of the continuous model multiplies $N$ by $e^{r}$. What is only approximate is the link to the *rates*: $r=\ln\lambda=\ln(1+R)\approx R=b-d+i-e$ when $R$ is small, i.e. when the time step is short compared with the time scale of change. For the June-beetle problem below, $R=0.0833$ per month gives $r=\ln1.0833=0.0800$, a 4 % difference, and over 6 months $\lambda^6$ and $e^{rt}$ agree exactly but $e^{Rt}$ overshoots by about 2 %.

> [!example] Worked example 1: a human population that doubles in 50 years
> Practice sum 1–2 ([[Pop Dyn_Practise sums.docx|docx]]): if the human population doubles in 50 years, $N=N_0e^{rt}$ with $N=2N_0$ gives $t_d=\ln2/r$, so $r=\ln2/50=0.0139\ \text{yr}^{-1}$. For a start of 5.4 billion in 1993 the size in 2000 is $5.4\times10^9\,e^{0.0139\times7}=5.95\times10^{9}$. The doubling time depends only on $r$, not on the size of the population: that is the signature of exponential growth.

![[04_PopDyn_Chaos_18Aug_2026.pdf#page=13&height=300]]
*Slide 13: the integration steps.*

> [!intuition] The compound-interest picture
> $r$ is an interest rate and $N$ is the bank balance. Doubling time $0.69/r$ is the rule of 70 in disguise ($\ln2\approx0.69$). A population that grows at 1.4 % a year doubles in about 50 years; at 12 % in about 6. Nothing in the equation notices how large $N$ is: the rich get richer at the same percentage rate as the poor. That is why a model without a limit must fail, and what slide 16 means by asking "*does this agree with our observations? Why or why not?*".

What the slide-15 simulations show: for $r>0$ ($\lambda>1$) unlimited exponential increase; for $r=0$ constancy; for $r<0$ exponential decay to zero. No other behaviour is possible: the model has no stable non-zero state. The disagreement with observations is the reason for §4.

> [!extra-beyond]- 🔵 Extra (beyond): Fibonacci's rabbits are a Leslie matrix
> Fibonacci's 1202 puzzle (each pair breeds from its second month and produces a new pair every month) is the age-structured model with matrix $\begin{pmatrix}1&1\\1&0\end{pmatrix}$ (young and mature pairs). Its dominant eigenvalue is $\lambda=(1+\sqrt5)/2=1.618$, the golden ratio, which is why Fibonacci numbers have ratio 1.618: the first population projection is also the first stable-age-distribution example of [[Leslie Matrix|EE02]].

## 4. Density dependence and the logistic model
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=17|slides 17–23]]*

Slide 17: *refining the model: density dependence.* Plot the **realised growth rate** (the per-capita rate actually experienced) against $N$: instead of a constant $r$, let it **fall linearly** from $r$ at $N=0$ to $0$ at $N=K$ ([[Density Dependence]]):

$$r'(N)=r\Big(1-\frac NK\Big),\qquad r'(0)=r,\quad r'(K)=0.$$

Replacing $r$ by $r'$ in $\frac1N\frac{dN}{dt}=r$ gives the **continuous logistic (Verhulst-Pearl) model** (slide 18):

$$\boxed{\frac{dN}{dt}=rN\Big(1-\frac NK\Big)}\qquad\text{[[Logistic Growth]]}$$

> [!derivation] Solving the logistic
> Separate variables and use partial fractions, $\dfrac{1}{N(1-N/K)}=\dfrac1N+\dfrac{1/K}{1-N/K}$:
> $$\int\Big(\frac1N+\frac1{K-N}\Big)dN=\int r\,dt\ \Longrightarrow\ \ln\frac{N}{K-N}=rt+C\ \Longrightarrow\ N(t)=\frac{K}{1+\dfrac{K-N_0}{N_0}\,e^{-rt}}.$$
> **Properties.** (i) $N\to K$ as $t\to\infty$. (ii) Growth rate $\dot N=rN(1-N/K)$ is a parabola in $N$, largest at $N=K/2$ where $\dot N=rK/4$; the curve has its **inflection at $N=K/2$**. (iii) Fixed points $0$ (slope $r>0$: unstable) and $K$ (slope $-r<0$: stable), see [[Fixed Points and Linear Stability]]. (iv) Near $K$ the deviation decays as $e^{-rt}$: a **relaxation time of $1/r$** ([[Relaxation Time]]).

![[fig_ee03_growth.png|760]]
*Figure EE3.2. Left: exponential (orange) against logistic (blue) growth for $K=100$, $r=0.6$, $N_0=2$; the dot is the inflection at $K/2$. Right: the per-capita rate falls linearly, the total growth rate is a parabola peaking at $rK/4=15$.*

> [!example] Worked example 2: the numbers behind Fig. EE3.2
> $K=100$, $r=0.6$, $N_0=2$: the population reaches $K/2$ at $t=\ln49/0.6=6.49$, and $N(10)=100/(1+49e^{-6})=89.2$. The fastest growth is $rK/4=15$ individuals per time unit at $N=50$. The exponential curve passes $K$ at $t\approx\ln50/0.6=6.5$ and carries on, which is the sense in which the logistic is the exponential "bent over" by density.

> [!intuition] A thermostat that bites near the target
> At low $N$ the thermostat is off and the population grows freely. As $N$ nears $K$ each added individual reduces everyone's rate a little, until births equal deaths at $K$. The **carrying capacity** $K$ ([[Carrying Capacity]]) is not a number written in the habitat; it is where the realised rate hits zero, and it can move with food, space or climate.

### 4.1 Four ways to write the same idea
Slide 19–20 turn the picture into a question: the realised rate can be measured in four ways, and setting each equal to $r(1-N/K)$ gives a different model ("class work: plug in these values of $r'$ and work out the expressions"):

| realised growth rate | resulting model | name |
|---|---|---|
| $\dfrac1N\dfrac{dN}{dt}$ | $\dfrac{dN}{dt}=rN\big(1-\frac NK\big)$ | continuous logistic |
| $\dfrac{N_{t+1}-N_t}{N_t}$ | $N_{t+1}=N_t\big[1+r\big(1-\frac{N_t}{K}\big)\big]$ | discrete logistic |
| $\dfrac{N_{t+1}}{N_t}$ | $N_{t+1}=rN_t\big(1-\frac{N_t}{K}\big)$ | alternative logistic |
| $\ln\dfrac{N_{t+1}}{N_t}$ | $N_{t+1}=N_t\,e^{\,r(1-N_t/K)}$ | exponential logistic (**Ricker**) |

$r$ means a slightly different thing in each row (a rate per time in the first, a rate per step in the second, the growth *ratio* at low density in the third, a log-ratio in the fourth). All four have a fixed point at $K$ (except the third, at $K(1-1/r)$), but only the first behaves simply, as the next section shows.

> [!extra-beyond]- 🔵 Extra (beyond): the second row is the logistic map in disguise
> Put $X=\dfrac{r}{(1+r)K}N$. Then $N_{t+1}=N_t[1+r(1-N_t/K)]$ becomes $X_{t+1}=aX_t(1-X_t)$ with $a=1+r$, May's canonical form. So all the famous results about $a$ translate with $r=a-1$.

### 4.2 Empirical checks and the problem with the straight line
Slide 22 tests the logistic against two data sets: the **US census** (Pearl and Reed 1920; the data follow the fitted S-curve from the early 1800s, but the later points lie above it) and the **rotifer** *Brachionus plicatilis* in laboratory culture (Yoshinaga et al. 2001), which climbs to a plateau of about 1,500 and then fluctuates around it. Slide 23 then warns: *the realised growth rate is often not a linearly decreasing function of $N$.* Its hypothetical curve falls steeply from about 8 at low $N$ and flattens to nearly 0 by $N\approx600$: the first few individuals matter most. "*How to take care?*" is left open: choose a form of $r'(N)$ that matches the data (the Ricker form of the last row, or others such as the Hassell model of §6, are such choices).

![[04_PopDyn_Chaos_18Aug_2026.pdf#page=22&height=300]]
*Slide 22: the US population and the rotifer culture.*

> [!extra-beyond]- 🔵 Extra (beyond): a delay turns the logistic into a cycle
> The logistic ODE is one-dimensional, so it can never oscillate. Put in a **delay** $\tau$ (for example gestation or maturation), $\dfrac{dN}{dt}=rN(t)\Big(1-\dfrac{N(t-\tau)}{K}\Big)$ (Hutchinson), and the equilibrium becomes unstable once $r\tau>\pi/2\approx1.571$: below it the overshoot is damped, above it there are sustained cycles.
>
> ![[fig_ee03_delay.png|760]]
> *Figure EE3.3. Hutchinson's delayed logistic: $r\tau=1.0$ (damped), $1.5$ (barely damped), $2.0$ (sustained cycle). Numerical solution (`scripts/fig_ee03_delay.py`).*
>
> Discrete time steps act like a delay: that is why the *discrete* versions of the logistic can cycle and be chaotic although the continuous one cannot.

## 5. The Ricker model: from stability to chaos
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=24|slides 24–26]]* · <span class="scope-extra-book">extra · book</span> *May 1976*

Slide 24: the **Ricker model** for a single population,

$$n_{t+1}=n_t\exp\!\Big[r\Big(1-\frac{n_t}{K}\Big)\Big]\qquad[[Ricker Model]]$$

with two parameters: $r$, the **intrinsic growth rate, which "determines the qualitative nature of the dynamics"**, and $K$, the **carrying capacity, "the population size at which $n_t=n_{t+1}$"**, which "does not affect the qualitative nature of the dynamics". (Rescale $n=Kx$ and $K$ disappears: $x_{t+1}=x_t\exp[r(1-x_t)]$.) For $n\ll K$ the factor is $\approx e^{r}$: growth by $\lambda=e^{r}$ per generation.

### 5.1 Stability of the equilibrium
Fixed points: $n=0$ and $n=K$. For a map $n_{t+1}=g(n_t)$ a fixed point $n^*$ is stable iff $|g'(n^*)|<1$ ([[Fixed Points and Linear Stability]]). Here $g'(n)=e^{r(1-n/K)}(1-rn/K)$, so

$$g'(K)=1-r\quad\Longrightarrow\quad \text{stable for }0<r<2:\ \ \begin{cases}0<r<1:&\text{monotone approach}\\1<r<2:&\text{damped oscillation}\end{cases}$$

and at $r=2$ the slope passes through $-1$: the equilibrium loses stability. The same linearisation, $\delta_{t+1}\approx(1-r)\,\delta_t$ for the deviation $\delta=n-K$, explains the damping: a negative multiplier makes $\delta$ alternate in sign.

> [!intuition] Overcompensation
> At large $r$ a population just below $K$ grows by so much that it jumps *above* $K$ by more than it was below; the next step pushes it back down by even more. Each step overcorrects. Stability needs the correction to be at most as big as the error, $|1-r|<1$. In continuous time the correction is applied continuously, so it can never overshoot; discrete reproduction (a pulse of births once a year) is what allows it.

![[fig_ee03_ricker_series.png|720]]
*Figure EE3.4. Ricker time series for $K=100$, $N_0=20$. $r=1.3$: damped to a point; $r=2.3$: a 2-point cycle (159.2, 40.8); $r=2.6$: a 4-point cycle (152.3, 39.1, 190.5, 18.1); $r=3.3$: chaos, no repetition.*

> [!example] Worked example 3: iterate by hand
> $r=1.3$, $K=100$, $n_0=20$: $n_1=20\,e^{1.3(0.8)}=56.6$; $n_2=56.6\,e^{1.3(1-0.566)}=99.5$; $n_3=100.1$; then $100.0$: damped oscillation about $K$ with multiplier $1-r=-0.3$ (each overshoot is 30 % of the last). For $r=2.3$ the multiplier is $-1.3$, so deviations grow until a **2-cycle** captures them: the long-run values are 159.22 and 40.78.

> [!verify] The slide's $r=2.5$ panel is a 2-cycle, not a 4-cycle
> Slide 25 captions its $r=2.5$ time series "4-point limit cycle". The Ricker map has period 2 at $r=2.5$: the 4-cycle exists only for $2.5265<r<2.6564$, so the genuine 4-point example is $r=2.6$ (Fig. EE3.4; `scripts/ee03_numbers.py`: periods 1, 2, 2, 4, chaos at $r=1.3,\,2.3,\,2.5,\,2.6,\,2.7$). The slide's own bifurcation diagram agrees (its second split is above 2.5). Probably a plotting-value slip. Use 2.6 in answers, and say which you use.

### 5.2 Period doubling and the bifurcation diagram
Slide 25 shows the **bifurcation diagram**: for each $r$, the values the system visits in the long run (after discarding a transient). "The periodicity for a given $r$ is equal to the number of points plotted for that value of $r$."

![[fig_ee03_bifurcation.png|820]]
*Figure EE3.5. The Ricker bifurcation diagram ($K=100$) with the Lyapunov exponent underneath. Marked: the first doubling at $r=2$, then 2.5265 (2→4), 2.6564 (4→8), and the onset of chaos at $r\approx2.6924$.*

> [!key] The route
> As $r$ increases: **stable point** ($r<2$) → **2-cycle** ($2<r<2.5265$) → **4-cycle** ($2.5265<r<2.6564$) → **8-cycle** (to 2.6846) → … a cascade of doublings accumulating at $r_\infty=2.6924$, beyond which the dynamics can be **chaotic**, with **periodic windows** (the white bands) inside the chaos ([[Period Doubling and Route to Chaos]]). Each cycle is born when the multiplier of the previous one passes through $-1$.

Compare the logistic map $X_{t+1}=aX_t(1-X_t)$ of May (1976), whose thresholds are $a=3,\ 3.4495,\ 3.5441,\ 3.5644,\ldots\to3.5700$. Writing the discrete logistic of §4.1 with $a=1+r$, they correspond to $r=2,\ 2.4495,\ 2.5441,\ 2.5644,\ldots\to2.5699$: almost the same, a little earlier than the Ricker's. May's Table 4 gives the Ricker numbers: the fixed point becomes unstable at $r=2.0000$ and its harmonics accumulate at $2.6924$.

> [!extra-book]+ 🟡 Extra (book): May (1976), the paper in brief
> May's review ([[May_Nature_1976.pdf#page=1|Nature 261: 459–467]]) starts from **first-order difference equations** $X_{t+1}=F(X_t)$, common for populations with non-overlapping generations, and uses $X_{t+1}=aX_t(1-X_t)$ ("arguably the simplest nonlinear difference equation") for most examples. Stability depends on the slope $\lambda=F'(X^*)$: for the logistic map $\lambda=2-a$, so $X^*=1-1/a$ is stable for $1<a<3$. At $a=3$ the **second iterate** $F(F(X))$ develops a loop and two period-2 points are born; the cycle process repeats with period $2^k$, the windows shrinking until the accumulation point $a_c=3.5700$, beyond which there are infinitely many periodic orbits and uncountably many aperiodic trajectories: "chaotic" in the sense of Li and Yorke. Odd periods first appear at $a=3.6786$ and the period-3 cycle at $a=3.8284$. He also gives the **Ricker** form, for which "local stability implies global stability" (positive for all $X>0$), and ends with a plea to teach these equations early because "simple nonlinear systems do not necessarily possess simple dynamical properties" ([[May_Nature_1976.pdf#page=9|Conclusion]]).

> [!extra-beyond]- 🔵 Extra (beyond): cobweb diagrams
> A **cobweb** iterates $n_{t+1}=g(n_t)$ graphically: go vertically to the curve, horizontally to the 45° line, repeat. At the fixed point the slope is $1-r$: for $r=1.3$ the web spirals in; for $r=2.3$ it closes on a square (2-cycle); for $r=3.0$ it never closes.
>
> ![[fig_ee03_cobweb.png|760]]
> *Figure EE3.6. Cobwebs for the Ricker map at $r=1.3,\ 2.3,\ 3.0$ ([[Cobweb Diagram]]).*

### 5.3 Chaos and sensitive dependence
Beyond $r_\infty$ the series never repeats (slide 25, $r=3.3$): the population visits values from about 0.75 to 280 in an irregular order. Yet nothing random enters: the rule is the same one-line equation. **Deterministic chaos** is bounded, aperiodic behaviour with **sensitive dependence on initial conditions (SDIC)** ([[Deterministic Chaos]]).

> [!key] The Lyapunov exponent
> Two starting values a tiny distance $\delta_0$ apart separate roughly as $\delta_t\approx\delta_0e^{\Lambda t}$; the average rate of separation is the **Lyapunov exponent** $\Lambda=\lim\frac1T\sum\ln|g'(n_t)|$. $\Lambda<0$: nearby orbits converge (stable point or cycle); $\Lambda>0$: they diverge exponentially (chaos). For the Ricker map: $r=1.3$: $-1.20$; $r=2.3$: $-0.90$; $r=2.6$: $-0.58$; **$r=3.0$: $+0.39$**; $r=3.3$: $+0.42$; and $r=3.6$: $-0.07$, one of the periodic windows (lower panel of Fig. EE3.5).

![[fig_ee03_sdic.png|760]]
*Figure EE3.7. Two Ricker runs ($r=3.0$, $K=100$) started at $N_0=50$ and $N_0=50.000001$. Left: they track each other for a while, then part. Right: the gap grows like $e^{\Lambda t}$ with $\Lambda=0.39$ until it is as large as the attractor.*

> [!example] Worked example 4: a forecast horizon
> A measurement error of $10^{-6}$ in $N_0$ becomes an error of order 100 (the size of the attractor) after $t=\ln(10^{2}/10^{-6})/0.39=47$ generations. Cutting the error by a factor of 1000 gains only $\ln(1000)/0.39=18$ more generations: the horizon grows only *logarithmically* with the accuracy of the data. This is why weather cannot be forecast beyond a couple of weeks however good the instruments: Lorenz's convection model in [[CL01 Earth as a System]] is the physical counterpart.

> [!pitfall] Chaos is not randomness, and not instability
> The chaotic series *looks* random but is generated by a rule with no noise: with exact initial values it is perfectly reproducible (only the *prediction from imprecise data* fails). The orbit is bounded: it never explodes. Inside the chaotic range there are periodic windows ($\Lambda<0$ at $r=3.6$), so $r$ above 2.69 does not guarantee chaos. And a short, noisy time series cannot by eye separate chaos from noise, which is the problem of §6–§7.

> [!extra-book]- 🟡 Extra (fun): Crichton's *Jurassic Park*
> The instructor includes extracts ([[Jurassic Park extract.pdf|pdf]]) with the warning that "the science portrayed here is accurate, the implications of that for real life: not necessarily so". They explain sensitive dependence with two cannon shells (linear: nearly the same start gives nearly the same landing) versus a weather system (nonlinear: tiny differences amplify, the "butterfly effect"), and fractals with Mandelbrot's observation that a mountain looks like its own peak at every scale. Not examinable.

### 5.4 Fractals
Slide 26 shows a zoom into the bifurcation diagram of the *logistic* map and says: "**fractals: self-similarity at multiple scales**; note that this bifurcation diagram comes from the logistic model (which looks a bit different from the Ricker), but the principle remains the same." ([[Fractals]])

![[fig_ee03_fractal.png|820]]
*Figure EE3.8. Left: the logistic-map bifurcation diagram, with the period-3 window shaded. Right: that window magnified; it contains three branches that split to 6, 12, …, a smaller copy of the whole tree.*

> [!extra-beyond]- 🔵 Extra (beyond): the same ratio everywhere
> Let $r_n$ be the parameter where the $2^n$-cycle is born. The gaps shrink geometrically, and the ratio $\delta_n=\dfrac{r_n-r_{n-1}}{r_{n+1}-r_n}$ tends to **Feigenbaum's constant $\delta=4.6692\ldots$**, the *same* number for the logistic map and the Ricker map (my computation, using superstable parameters: $4.669$ and $4.669$). Many different single-hump maps share it: the cascade is *universal*, which is why a simple population model can say anything general about chaos.
>
> ![[fig_ee03_feigenbaum.png|700]]
> *Figure EE3.9. Left: the ratio converges to 4.669 for both maps. Right: the gaps shrink geometrically (straight line on a log axis).*

## 6. What about the real world? The Hassell model and the puzzle
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=27|slides 27–30]]* · <span class="scope-extra-book">extra · book</span> *Hassell et al. 1976 (as presented)*

Slide 27: *what about the real world?* Slide 28 introduces the **Hassell model** (Hassell 1975, *J. Anim. Ecol.* 44: 283–295):

$$N_{t+1}=\lambda N_t\,(1+aN_t)^{-\beta}\qquad[[Hassell Model]]$$

$\lambda$ is the growth-rate parameter; $a$ and $\beta$ regulate the density-dependent feedback. Its own bifurcation diagram against $\lambda$ (slide 28, $\lambda$ from 5 to 35) goes through the same stable-cycle-chaos sequence as the Ricker's.

> [!derivation] Equilibrium and stability of the Hassell model
> Fixed point: $\lambda(1+aN^*)^{-\beta}=1\Rightarrow 1+aN^*=\lambda^{1/\beta}$, so $N^*=(\lambda^{1/\beta}-1)/a$. Slope: with $f(N)=\lambda N(1+aN)^{-\beta}$,
> $$f'(N^*)=1-\beta\,\frac{aN^*}{1+aN^*}=1-\beta\big(1-\lambda^{-1/\beta}\big).$$
> **Monotone damping** needs $0\le f'<1$, i.e. $\beta(1-\lambda^{-1/\beta})\le1$; **damped oscillation** needs $-1<f'<0$; the equilibrium is **unstable** for $f'\le-1$, i.e. $\beta(1-\lambda^{-1/\beta})\ge2$. Consequences: if $\beta\le1$ ($\beta=1$ is the Beverton-Holt form) the approach is *always* monotone, whatever $\lambda$; instability needs $\beta>2$ and large $\lambda$ (for $\beta=3$, $\lambda>27$; for $\beta=6$, $\lambda>11.4$; for $\beta=10$, $\lambda>9.3$).
>
> **What $\beta$ means.** At large $N$, $f(N)\approx\lambda a^{-\beta}N^{1-\beta}$.
> - For $\beta\le1$, the next generation never *falls* as this one grows. More parents always mean at least as many offspring: the crowded parents share out the resource (**contest** competition). With no hump in $f$ there is nothing to overshoot with, so the approach to $N^*$ is monotone.
> - For $\beta>1$, $f$ has a hump. Past it, more parents mean *fewer* offspring, because the resource is split so finely that most get too little (**scramble** competition). That is the overcompensation of §5.1.
> 
> So $\beta$ measures how abrupt the density dependence is, and $\lambda$ how hard the population pushes against it. Cycles and chaos need both to be large.

![[fig_ee03_hassell_map.png|640]]
*Figure EE3.10. Stability map of the Hassell model in the $(\lambda,\beta)$ plane (my computation). Green: monotone damping; yellow: oscillatory damping; red: unstable (cycles, chaos).*

Slide 29 shows Fig. 2 of **Hassell, Lawton and May (1976)**, the same plane with the regions *monotonic damping, damped oscillations, stable limit cycles, chaos* and **24 insect populations** placed by fitting $\lambda$ and $\beta$ to their life-table data. The slide's reading: "**22/24 exhibited monotonic damping. Conclusion: most natural populations exhibit relatively simple dynamics.**" (Turchin and Taylor summarise the same paper as 22 monotone damping, 1 damped oscillation, 1 limit cycle and no chaos.)

![[04_PopDyn_Chaos_18Aug_2026.pdf#page=29&height=340]]
*Slide 29: Hassell et al. (1976), Fig. 2.*

> [!key] The puzzle (slide 30)
> Simple models *can*, in principle, show everything from stability to chaos (May 1976), which launched many attempts to find chaos in nature. Yet "although many populations have very high growth rates, except 1–2 cases **no real population has been demonstrated to exhibit chaotic dynamics**"; and Hassell et al.'s finding of almost universal simple behaviour "even intuitively does not make sense". *So, what's going on?*
>
> Why it "does not make sense": insects lay tens to hundreds of eggs, so $\lambda$ is large, and §5 showed that large growth rates bring overshoot. By the derivation above, a population with large $\lambda$ falls in the monotone region only if its fitted $\beta$ is close to 1 or below. The fits imply that almost every insect has gentle, contest-like density dependence, and that is what is hard to believe.

The next section gives the two answers the lecture offers.

## 7. Making simple models more realistic: taming chaos
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=31|slides 31–35]]* · <span class="scope-extra-book">extra · book</span> *Turchin and Taylor 1992; Dey and Joshi*

### 7.1 Answer one: organisms are whole numbers (the lattice effect)
Slide 32 (Henson et al., *Science*, 19 Oct 2001): "although real organisms come in integer numbers, population-dynamics models do not incorporate this reality." The slide compares the bifurcation diagram of a model **unintegerised** and **integerised** (population size $N$ against the maximal per-capita growth rate $r$): "**chaos gives way to limit cycles or extinctions**."

> [!key] Why integerisation kills chaos (slide 33)
> "Chaos implies that the points in a time series never repeat themselves. But integerisation, coupled with the upper bound on population size imposed by the model structure, makes the set of possible values the system can take **finite**. In other words, sooner or later a particular value has to repeat, and that is the point where **periodicity** sets in." ([[Lattice Effect]])
> It is the **pigeonhole principle**: a deterministic map on a finite set of states is eventually periodic, because once a state recurs the whole sequence repeats. A series that never repeats needs infinitely many states.

![[fig_ee03_lattice.png|820]]
*Figure EE3.11. The lattice effect on the Ricker map ($K=100$, $r=3.0$, start 30). Left: the real-valued series is chaotic. Middle: the integer-valued series locks onto a 10-cycle after a 21-step transient. Right: longer cycles for bigger $K$ (cycle length reached, my computation).*

> [!example] Worked example 5: how long can the cycle be?
> In the integerised Ricker model with $K=100$ and $r=3.0$ the population never exceeds 245, so there are at most 246 states and the cycle length is at most 246. In practice it is much shorter: 10 for $K=100$, $r=3.0$; for $K=1000$ the cycle is 25–36; for $K=10{,}000$ it reaches 82 ($r=2.8$) to 155 ($r=3.0$). **The cycle length grows with $K$** (the number of allowed states grows), so for very large populations the periodic orbit becomes so long that it is indistinguishable from chaos in any real data set.

> [!pitfall] What the lattice effect does and does not show
> The slide itself adds: "the lattice effect can only explain why *deterministic chaos* cannot be observed in biological systems. It does **not** exclude the possibility of **limit cycles with long periodicities**." It is a statement about the *model*: the real-valued equation is a poor *encoding* ([[Modelling Relation]]) of the world at small $N$. Also, integerising sometimes sends the population to 0: when a chaotic orbit dips below 0.5 (Ricker with $K=100$, $r=3.3$ reaches 0.75) rounding to the integer lattice can be fatal, hence the slide's "or extinctions".

### 7.2 Answer two: the models were too simple (model complexity)
Slide 34 (Turchin and Taylor 1992): Hassell et al. "used a model that incorporated only **one time lag** and a **simple functional form**". Turchin and Taylor "**fit a large set of models with different number of time lags and varying complexity**". All kinds of behaviour were observed: exponential damping, oscillatory damping, limit cycles *and chaos*. Their conclusion (quoted on the slide): "***Use of overly simple models for reconstructing endogenous dynamics from data may be biased in favor of finding stability.***"

Why lags matter: a lag means this year's growth responds to the density of an *earlier* year, through a slow-growing food plant, a predator that builds up, or a cohort that matures only later. The population then keeps growing after it has passed its equilibrium, because the brake responds to the old, lower density. This is the delayed logistic of §4.2, where a lag alone produced cycles. A one-lag model fitted to such data can see only the *average* dependence of growth on current density, which slopes gently downward, and it reports stability (Fig. EE3.12).

> [!extra-book]+ 🟡 Extra (book): Turchin and Taylor (1992) in brief
> **Question:** how common are complex dynamics (limit cycles, quasiperiodicity, chaos) in real populations, if one does not force a single-lag model on the data? **Method:** the **response-surface methodology**: fit the yearly change $R_t=\ln(N_t/N_{t-1})$ as a flexible polynomial function of **two lagged densities** ($N_{t-1}$, $N_{t-2}$) instead of the one-lag Hassell form; lags stand for unseen *delayed density dependence*, from interacting species or age structure. They restricted themselves to long series (at least 18 years) and tested the reconstructed behaviour against the **autocorrelation function** of each series (if the method can recover limit cycles, there is some hope for chaos). **Data:** 14 insect and 22 vertebrate populations. **Result for the insects:** 1 unregulated, 3 exponentially stable, 6 damped oscillations, 1 limit cycle, 2 quasiperiodic and 1 chaotic; the vertebrates showed a similar spectrum without chaos. **Conclusion:** "the complete spectrum of dynamical behaviours, ranging from exponential stability to chaos, is likely to be found among natural populations" ([[TurchinTaylor_Ecology_1992.pdf#page=2|Ecology 73: 289–305]]). The paper is "a little advanced"; the instructor's advice for the extract is to ignore the technical detail and keep the conclusions.

![[fig_ee03_projection.png|820]]
*Figure EE3.12. A miniature of the argument (my construction). A two-lag Ricker-type model ($r=1.6$, $b=3$, $K=100$) cycles permanently (left). Regressing $\ln(N_{t+1}/N_t)$ on $N_t$ alone gives a poor fit ($R^2=0.30$, middle: the points trace a loop) and predicts smooth damping to $K$ (right).*

> [!intuition] The shadow of a cube
> Slide 35 shows a photograph of a wire-frame four-dimensional cube whose *shadow* is a simple shape: "complex high-dimensional objects can have simple low-dimensional projections. So be very careful when you are inferring the former based on the latter. Note 1: this is true of life in general. Note 2: this is just an analogy." One-lag models look at the shadow. If the real system has hidden dimensions (other species, age classes, time delays) the shadow may look like a stable point even when the object is a cycle. Fitting more lags is the way to see more of the object.

Both answers lead to the same moral for the course ([[Population Thinking]], [[Modelling Relation]]): *the model is not the world*; deciding which model fits should be done by comparison, e.g. with [[Akaike Information Criterion]], not by assuming the simplest form.

## 8. The reading tiers
<span class="scope-taught">taught</span> *[[04_PopDyn_Chaos_18Aug_2026.pdf#page=36|slides 36–37]]*

| item | tier |
|---|---|
| lecture slides; the practice sums | syllabus |
| Rockwood, *Introduction to Population Ecology* Ch. 1–2 ("some extra material here which was not covered in class and hence will have nothing to do with the exams") | detailed reading |
| Dey and Joshi, "Chaos in ecological systems: fact or artifact?" (a simple explanation of why integerisation kills chaos) | detailed reading |
| extract from Turchin and Taylor 1992 ("ignore the technical details") | detailed reading |
| May 1976 ("the paper that ushered in the era of non-linear dynamics"); Turchin and Taylor 1992 ("a highly cited paper… people who wish to get into applied maths… are well advised to grapple with it") | papers |
| Crichton, *Jurassic Park* extracts | fun |

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: From a stable point to chaos: the Ricker map
> n_{t+1} = n_t exp[r(1 − n_t/K)] with K = 100.
>
> ![[ee_ricker_chaos.png|720]]
>
> **Try:** r = 1.3 (damped), 2.3 (2-cycle 159.2/40.8), 2.6 (4-cycle), 3.0 (chaos, Λ = +0.39), 3.6 (periodic window, Λ < 0). With the second run on at r = 3.0 the two series part after ~35 steps.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_ricker_chaos.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_ricker_chaos.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How EE03 connects
> **Builds on:** [[EE02 Structured Population Models]] (structure; $\lambda$ as the growth multiplier; Phlox $\lambda=2.4177$).
> **Leads to:** [[EE04 Competition and Invasions]] (two species: logistic growth with a competitor's term) → [[EE05 Predation]] (Lotka-Volterra cycles; the same overcompensation and delays) → [[EE06 Eutrophication and Alternative Stable States]] → [[EE07 Conservation Biology]] (small populations, stochasticity, the extinction side of integerisation).
> **Concepts:** [[Modelling Relation]] · [[Exponential Growth]] · [[Density Dependence]] · [[Logistic Growth]] · [[Carrying Capacity]] · [[Ricker Model]] · [[Cobweb Diagram]] · [[Period Doubling and Route to Chaos]] · [[Deterministic Chaos]] · [[Fractals]] · [[Hassell Model]] · [[Lattice Effect]] · [[Time-Series Reconstruction]]
> **Other subjects:** [[Fixed Points and Linear Stability]] (the slope condition $|g'|<1$ for maps) · [[Relaxation Time]] · [[Bistability and Tipping Points]] · [[CL01 Earth as a System]] (Lorenz chaos) · [[Proofs, Analysis and Topology - Course Map]] (bifurcations, fractals)

> [!connection] Stability in climate and in ecology
> The logistic model's fixed points and relaxation time $1/r$ are the same mathematics as the energy-balance model of [[CL04 Feedback and Multiple Steady States]]: a restoring slope $f'(x^*)<0$. What is new here is the **discrete-time map**, where the stability criterion becomes $|g'|<1$ and the loss of stability at $g'=-1$ gives a period doubling instead of a tipping point.

## Summary
> [!summary] Cheat-sheet
> - **Model** = formal system linked to nature by encoding $\varepsilon$ and decoding $\delta$; good if the loop agrees with causation (Rosen).
> - **Exponential:** $N_{t+1}=\lambda N_t$, $N_t=\lambda^tN_0$ ($\lambda=1+b-d+i-e$); $\dot N=rN$, $N=N_0e^{rt}$; $\lambda=e^{r}$; doubling $t_d=\ln2/r$. A "law" because it describes the no-force case.
> - **Logistic:** $r'=r(1-N/K)$; $\dot N=rN(1-N/K)$; $N=K/[1+((K-N_0)/N_0)e^{-rt}]$; inflection at $K/2$, max rate $rK/4$, relaxation time $1/r$. Four forms of the realised rate (slide 20); only the continuous one is always smooth.
> - **Ricker:** $n_{t+1}=n_te^{r(1-n_t/K)}$; $g'(K)=1-r$; stable for $0<r<2$ (monotone for $r<1$); then 2-cycle ($r=2$), 4-cycle (2.5265), 8-cycle (2.6564), chaos from 2.6924; $K$ rescales only. **The slide's $r=2.5$ is a 2-cycle.**
> - **Chaos:** deterministic, bounded, aperiodic, sensitive to initial conditions ($\Lambda>0$; $\Lambda=0.39$ at $r=3$); forecast horizon $\sim\ln(\text{range}/\delta_0)/\Lambda$. The bifurcation diagram is a **fractal**; ratio of gaps $\to4.669$.
> - **Hassell:** $N_{t+1}=\lambda N_t(1+aN_t)^{-\beta}$; $f'(N^*)=1-\beta(1-\lambda^{-1/\beta})$; 22 of 24 insect populations monotone: "natural populations are simple".
> - **Resolutions:** *lattice effect* (integer $N$, finite states $\Rightarrow$ eventually periodic; chaos → cycles or extinction; long cycles remain possible) and *model complexity* (more lags and flexible forms find the whole spectrum, Turchin and Taylor: "overly simple models are biased toward stability").

## Practice
1. **(Sum 1–2)** The human population is expected to double in 50 years. Find $r$. If it was 5.4 billion in 1993, what is the projected size in 2000?
2. **(Sum 3)** A population of the annual *Nicotiana* increases by 12 % a year. Find $\lambda$, $r$ and the doubling time.
3. **(Sum 4)** A June-beetle population of 3,000 has 400 births and 150 deaths in a month. Estimate $r$ and the predicted size after 6 months. Redo it with the discrete model and compare.
4. **(Sum 5–6)** A culture of 100,000 algal cells grows to 500,000 in 10 days. Find $r$ and predict the size after another 10 days.
5. **Logistic.** $K=500$, $r=0.4$ per day, $N_0=10$. (a) When does the population reach $K/2$? (b) What is its largest growth rate and where? (c) Near $K$ a deviation decays like $e^{-rt}$: how long does it take to shrink to 1 % of its initial size?
6. **Ricker.** For $K=200$ and $r=1.8$: (a) the multiplier at $K$; (b) the kind of approach; (c) what changes if $r$ rises to 2.3 and what if $K$ is doubled? (d) Is the slide's "$r=2.5$: 4-point cycle" correct?
7. **Hassell.** $\lambda=10$, $\beta=3$: compute $f'(N^*)$ and classify. For $\beta=3$ at what $\lambda$ does the equilibrium become unstable?
8. **Chaos.** The Lyapunov exponent at $r=3.0$ is $0.39$ per generation. How many generations until an initial error of $10^{-4}$ (relative to a range of 100) has grown to the full range? What would you need to double that horizon?
9. **Lattice.** Explain in four sentences why integer-valued dynamics cannot be chaotic, and why the effect nevertheless does not make long cycles unlikely at large $K$.
10. **Exam-style.** "Simple population models predict chaos for high growth rates, but chaos is almost never observed." Give *two* explanations that appear in the lecture and the key evidence for each.

> [!example]- Solutions
> 1. $r=\ln2/50=0.0139\ \text{yr}^{-1}$; $N(2000)=5.4\times10^{9}e^{0.0139\times7}=5.95\times10^{9}$.
> 2. $\lambda=1.12$; $r=\ln1.12=0.1133\ \text{yr}^{-1}$; $t_d=\ln2/0.1133=6.1$ years.
> 3. $b=400/3000=0.1333$, $d=150/3000=0.0500$ per month, so $r=b-d=0.0833$ per month and $N=3000\,e^{0.0833\times6}=4{,}946$. With a discrete step, $\lambda=1.0833$ and $N=3000\times1.0833^{6}=4{,}849$. The difference (2 %) comes from using $R=0.0833$ as if it were the continuous $r=\ln1.0833=0.0800$ (see the pitfall in §3.1).
> 4. $r=\ln(500{,}000/100{,}000)/10=\ln5/10=0.161\ \text{d}^{-1}$. After another 10 days $N=500{,}000\times e^{0.161\times10}=500{,}000\times5=2.5\times10^{6}$ (the docx gets 2.47 million by rounding $r$ to 0.16).
> 5. (a) $t=\ln\big[(K-N_0)/N_0\big]/r=\ln49/0.4=9.7$ days. (b) $rK/4=0.4\times500/4=50$ cells per day at $N=250$. (c) Near $K$ the deviation decays like $e^{-rt}$; to fall to 1 % of itself takes $\ln100/0.4=11.5$ days.
> 6. (a) $1-r=-0.8$. (b) $|{-0.8}|<1$: **damped oscillation** (negative multiplier). (c) At $r=2.3$ the multiplier is $-1.3$: unstable, a 2-cycle (values $\approx1.59K$ and $0.41K$, i.e. 318 and 82 for $K=200$). Doubling $K$ to 400 changes only the scale: same qualitative behaviour. (d) No: at $r=2.5$ the map has period 2 (the 4-cycle exists for $2.5265<r<2.6564$); use $r=2.6$.
> 7. $f'=1-3(1-10^{-1/3})=1-3(0.5358)=-0.61$: between $-1$ and 0, so **oscillatory damping**. Instability needs $3(1-\lambda^{-1/3})=2$, i.e. $\lambda^{-1/3}=1/3$, $\lambda=27$.
> 8. $t=\ln(100/10^{-4})/0.39=\ln10^{6}/0.39=13.8/0.39=35$ generations. To double the horizon (70 generations) you need $\delta_0=100\,e^{-0.39\times70}=100\times1.4\times10^{-12}=1.4\times10^{-10}$, a **million-fold** better measurement ($10^{-4}\to10^{-10}$): horizons grow logarithmically with precision.
> 9. A deterministic map has only one next value for each state. If $N$ is an integer between 0 and an upper bound, there are finitely many states, so some state must eventually recur and the series repeats forever: periodic, not chaotic. But the number of states grows with $K$, so cycles can be very long (e.g. 82 to 155 generations for $K=10{,}000$), so a real finite-length time series cannot tell such a cycle from chaos.
> 10. (1) **Lattice effect:** integer numbers plus an upper bound ⇒ finitely many states ⇒ chaos is replaced by (possibly long) cycles or extinction (Henson et al. 2001; the integerised bifurcation diagram on slide 32). (2) **Model complexity:** Hassell et al. fitted a one-lag, simple-form model to 24 populations and found 22 monotone, but Turchin and Taylor fitted two-lag response surfaces to 14 insect and 22 vertebrate populations and found the whole spectrum, including one case of chaos in the insects.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | locusts; plan; domain | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=1\|sl. 1–4]] | taught |
> | modelling relation | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=5\|sl. 5–7]] (Simeonov 2010, Fig. 1) | taught |
> | exponential growth, first law | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=8\|sl. 8–16]] | taught |
> | density dependence, logistic, four forms | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=17\|sl. 17–23]] | taught |
> | Ricker, bifurcation, fractals | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=24\|sl. 24–26]] | taught |
> | Hassell model and puzzle | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=27\|sl. 27–30]] | taught |
> | lattice effect; model complexity | [[04_PopDyn_Chaos_18Aug_2026.pdf#page=31\|sl. 31–35]] | taught |
> | practice sums | [[Pop Dyn_Practise sums.docx]] (originally by Greg Anderson, Bates College) | taught |
> | the logistic map, cycles, Ricker Table 4 | May 1976 (paper) | extra/book |
> | response-surface reconstruction; 14 + 22 populations | Turchin and Taylor 1992 (paper) | extra/book |
> | Jurassic Park extracts | the "fun" tier | extra/book |
> | delayed logistic; logistic map equivalence; cobwebs; Lyapunov; Feigenbaum; Hassell map; integerised cycle lengths; projection example; Fibonacci matrix | computed here (`scripts/ee03_numbers.py`, `scripts/fig_ee03_*.py`) | extra/beyond |
>
> **Existing figures checked.** The twelve `fig_ee03_*` figures were made in an earlier session and are used here after checking their scripts and outputs: the Ricker series uses the genuine 4-cycle value $r=2.6$; the thresholds (2, 2.5265, 2.6564, 2.6846, 2.6924) and the Lyapunov exponents agree with May's Table 4 and with my independent computation; the integerised cycle lengths and the one-lag regression ($R^2=0.30$) agree with `ee03_numbers.py`.
>
> **Source discrepancy.** Slide 25 labels its $r=2.5$ time series a 4-point cycle (a 2-cycle at that $r$); flagged in §5.1.
>
> **Not read in detail.** Rockwood Ch. 1–2 (65-page scan, detailed reading) and the Turchin book chapter in the folder (not on the reading slide). Dey and Joshi is not in the folder; the argument of §7.1 is taken from slide 33. May (1976) and Turchin and Taylor (1992) are scans: OCR was used.

**References.** May, R. M. (1976) *Nature* 261, 459–467 · Turchin, P. & Taylor, A. D. (1992) *Ecology* 73, 289–305 · Hassell, M. P. (1975) *J. Anim. Ecol.* 44, 283–295 · Hassell, M. P., Lawton, J. H. & May, R. M. (1976) *J. Anim. Ecol.* 45, 471–486 · Henson, S. M. et al. (2001) *Science* 294 (19 Oct) · Tian, H. et al. (2011) *PNAS* · Pearl, R. & Reed, L. J. (1920) · Yoshinaga, T. et al. (2001) · Simeonov, P. L. (2010) *Prog. Biophys. Mol. Biol.* 102, 85–121 · Rosen, R. (1985) *Anticipatory Systems* · Ricker, W. E. (1954) *J. Fish. Res. Board Can.* 11, 559 · Verhulst, P.-F. (1838) · Hutchinson, G. E. (1948) · Li, T.-Y. & Yorke, J. A. (1975) *Am. Math. Monthly* 82, 985 · Feigenbaum, M. J. (1978) *J. Stat. Phys.* 19, 25 · Rockwood, L. L. *Introduction to Population Ecology* · Crichton, M. *Jurassic Park*.
