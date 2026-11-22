---
title: EE09 Hardy-Weinberg Equilibrium
aliases: [EE09, Hardy-Weinberg, Hardy–Weinberg equilibrium, HWE, HW law, population genetics, beanbag genetics, BI2113 lecture 9]
subject: eco-evo
type: chapter
chapter: 9
part: IV
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
prereq: ["[[EE08 Evolution - An Introduction]]"]
tags: [subject/eco-evo, type/chapter, taught, extra/book, extra/beyond, src/slides, src/book, src/own-notes, status/draft]
---
# EE09 · Hardy–Weinberg Equilibrium

◀ [[EE08 Evolution - An Introduction]] · [[Ecology and Evolution - Course Map|Course Map]] · next: [[EE10 Natural Selection]]

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] Syllabus map: what is in the syllabus and what is extra in this chapter
> 🟢 **In syllabus (taught)**: the lecture ([[09_Hardy-Weinberg.pdf|16 slides]]) **and** the *mandatory* readings, Templeton (2006) *Population Genetics and Microevolutionary Theory* Ch. 2, pp. 21–35 ([[Hardy-Weinberg_Templeton.pdf|reading]]) and Hartl & Clark *Principles of Population Genetics* Ch. 3, pp. 74–80 ([[Hartl_Clark_HWE_Short.pdf|reading]]), plus the **practice set** ([[PopgenPracticeProblem_Questions only.docx|five problems]]): "It is imperative that you learn how to solve H-W problems."
> - §1 Mendel's laws, what population genetics is, "beanbag genetics" (sl. 2–4)
> - §2 the one-locus, two-allele model; gene and genotype frequencies (sl. 5)
> - §3 the derivation, step by step with its assumptions (sl. 6; Hartl Table 3.1; Templeton Table 2.1)
> - §4 the law and Hardy's 1908 letter (sl. 7–8)
> - §5 five properties of the equilibrium (sl. 9–10)
> - §6 why it matters (sl. 11; Templeton pp. 32–35)
> - §7 using H-W: testing a population (sl. 12; χ², Hartl p. 80–81, Templeton Box 2.1)
> - §8 more than two alleles (sl. 13)
> - §9 carriers of recessive disease: PKU, PTC, albinism (sl. 14–15)
> - §10 every lecture example and the practice set, solved
>
> 🟡 **Extra · book**: Hardy's and Weinberg's two derivations (Templeton pp. 25–29); unequal allele frequencies in the sexes (Hartl Problem 3.3); why the model is fundamental (Hartl pp. 79–80); the limits of a χ² test (Hartl p. 80).
>
> 🔵 **Extra · beyond**: the de Finetti diagram, the "rare alleles hide in heterozygotes" ratios, exact χ² numbers for every problem, and the interactive tool (`scripts/ee08_10_numbers.py`).

> [!key] After this chapter you can
> - compute **allele** frequencies from **genotype** counts ($p=P+Q/2$) and the **Hardy–Weinberg** expectations $p^2:2pq:q^2$,
> - derive the law and **name every assumption** used at each step,
> - state the five properties (neutral stability, one generation to equilibrium, dependence on allele frequency only, $2pq\le\tfrac12$, rare alleles hide in heterozygotes),
> - **test** a sample for HWE with a χ² test (1 degree of freedom) and say what a non-significant result does and does not show,
> - extend to $k$ alleles, $(p_1+\dots+p_k)^2$,
> - estimate **carrier** frequencies for a recessive trait, and say when that estimate is untestable.

> [!intuition] The one-sentence story
> If you throw all gametes in a bag and pair them at random, the genotypes come out as $p^2:2pq:q^2$ in one draw, and the bag's contents never change: Mendelian inheritance by itself neither creates nor destroys variation, so every *change* in a population (selection, drift, mutation, migration, non-random mating) shows up as a departure from this baseline. "The law is boring, it is the deviations that are interesting" ([[Putting it all together_13-11-2026.pdf#page=12|wrap-up lecture, slide 12]]).

## 1. From Mendel to populations
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=2|slides 2–4]]*

Mendel's laws describe transmission **in a family**: **segregation** (each gamete receives one copy of a gene) and **independent assortment** (alleles of different genes assort independently) (sl. 2). **Population genetics** extends them to whole populations: individuals at time $t$ make gametes by reduction division, gametes fuse into zygotes, zygotes develop, and the population at $t+1$ may have different gene frequencies (sl. 3). The abstraction (sl. 4): treat individuals as **gene pairs**, gametes as **single genes**, mating as the **coming together of gametes**, and the next generation as a **sample from the pool of gametes** — "beanbag genetics".

Templeton (p. 21) frames every model of microevolution the same way: it must make assumptions about three mechanisms, **producing gametes** (genetic architecture), **uniting gametes** (population structure) and **developing phenotypes**; evolution is "a change over time in the frequency of alleles or allele combinations in the gene pool".

## 2. Gene and genotype frequencies
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=5|slide 5]]*

One autosomal locus, two alleles $A_1,A_2$ with frequencies $p,q$; genotypes $A_1A_1,A_1A_2,A_2A_2$ with frequencies $P,Q,R$:
$$P+Q+R=1,\qquad p+q=1,\qquad \boxed{p=P+\tfrac{Q}{2},\quad q=R+\tfrac Q2}.$$
Each homozygote carries two copies of its allele, each heterozygote one of each; dividing allele counts by $2N$ gives the formula. **This formula is always true** — it does not assume HWE (Templeton p. 34).

> [!example] Slide 5: the Pueblo MN sample
> 83 MM, 46 MN, 11 NN ($N=140$): $P=83/140=0.593$, $Q=0.329$, $R=0.079$; $p=0.593+0.329/2=0.757$, $q=0.243$. Counting genes: 280 copies, $166+46=212$ are M, $212/280=0.757$ (Templeton p. 30).

## 3. Deriving the law
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=6|slide 6]]* · <span class="scope-extra-book">extra · book</span> *Templeton pp. 24–29, Hartl pp. 74–77*

Slide 6 follows the frequency of $A_1$ through one life cycle and names the assumption needed at each arrow:

| stage | frequency of $A_1$ / genotypes | assumption that keeps it so |
|---|---|---|
| parents | $p$ | |
| all gametes | $p$ | normal (Mendelian) segregation; equal fertility (no fertility selection); no mutation, no migration |
| gametes forming zygotes | $p$ | large population; equal fertilising capacity of all gametes |
| zygotes | $p^2:2pq:q^2$ | **random mating**; equal frequency in males and females |
| progeny (adults) | $p^2:2pq:q^2$ | equal viability (no viability selection) |
| progeny allele frequency | $p^2+\tfrac12\cdot2pq=p(p+q)=p$ | |

The **random union of gametes** gives the genotypes directly: the chance that two $A_1$ gametes meet is $p\cdot p$, and a heterozygote can form two ways, $pq+qp=2pq$, i.e. $(pA_1+qA_2)^2$ (Hartl Fig. 3.2).

> [!example]- 🟡 Weinberg's route: random mating of *genotypes* (Hartl Table 3.1, Templeton Table 2.3)
> Pair genotypes at random: matings occur with frequencies $P^2$ (AA×AA), $2PQ$ (AA×Aa), $2PR$ (AA×aa), $Q^2$ (Aa×Aa), $2QR$ (Aa×aa), $R^2$ (aa×aa), and Mendel's law of segregation gives the offspring. Summing:
> $$P'=P^2+\tfrac12(2PQ)+\tfrac14Q^2=(P+\tfrac Q2)^2=p^2,\quad Q'=2(P+\tfrac Q2)(R+\tfrac Q2)=2pq,\quad R'=q^2.$$
> The parental $P,Q,R$ were arbitrary, so **one generation of random mating gives HW proportions from any start**. Random mating of genotypes and random union of gametes give the same answer (Hartl p. 76). Weinberg's version needs one more assumption than Hardy's monoecious model: genotype frequencies equal in both sexes (Templeton p. 29).

> [!example]- 🟡 What if the sexes differ? (Hartl Problem 3.3)
> With allele frequency $p_m$ in male and $p_f$ in female gametes, the first generation of zygotes is $p_mp_f : p_mq_f+q_mp_f : q_mq_f$ — **not** HW. But both sexes of that generation carry $\bar p=(p_m+p_f)/2$, so HW is reached in the **second** generation. Example: $p_m=0.9$, $p_f=0.3$: generation 1 is $0.27:0.66:0.07$ (HW at $\bar p=0.6$ would be $0.36:0.48:0.16$); generation 2 is $0.36:0.48:0.16$.

Templeton's Table 2.1 lists the assumptions by mechanism: **gamete production** — one autosomal locus, two alleles, no mutation, Mendel's first law; **gamete union** — random mating, infinite size, no genetic exchange (one isolated population), no age structure (discrete generations); **phenotype development** — all genotypes equally able to replicate their DNA. Hartl's list adds: diploid, sexual, alleles equally frequent in the sexes, no migration, no selection. Random mating is defined **for the locus in question only**: humans mate non-randomly for height or birthplace, but if the locus does not affect those traits, mating is random *for it* (Templeton p. 24).

## 4. The law
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=7|slides 7–8]]*

> [!key] The Hardy–Weinberg law (slide 7)
> In a **large random-mating population with no selection, mutation or migration**, the gene frequencies and the genotype frequencies are **constant from generation to generation**, and the genotype frequencies are related to the gene frequencies by
> $$A_1A_1:A_1A_2:A_2A_2 \;=\; p^2:2pq:q^2 .$$

Hardy's 1908 letter (sl. 8) opens: "I am reluctant to intrude in a discussion concerning matters of which I have no expert knowledge, and I should have expected the very simple point which I wish to make to have been familiar to biologists. However, some remarks of Mr. Udny Yule, to which Mr. R. C. Punnett has called my attention, suggest that it may still be worth making…" The story (Templeton p. 32; Hartl p. 79): **Yule** objected that if brachydactyly were a Mendelian dominant, one should see 3 affected : 1 unaffected in the population. Hardy showed the population ratio is $p^2+2pq:q^2$, which can take any value as $p$ varies: Yule had confused a **family** ratio (Aa × Aa) with a **population** frequency. Weinberg derived the same result independently the same year; Castle had noted it in 1903 (Hartl p. 79).

## 5. Five properties
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=9|slides 9–10]]*

1. **Gene and genotype frequencies do not change**: the equilibrium is **neutrally stable** — disturb $p$ and the population stays at the new $p$; nothing pulls it back (contrast the stable equilibria of [[EE03 Population Dynamics and Chaos]]). The reason is in the derivation of §3: $p'=p$ holds for *every* value of $p$. Every allele frequency is an equilibrium, so no particular value is favoured and there is nothing to return to. Pulling forces appear only when one of the assumptions fails. Selection, mutation and migration each make $p'$ a function of $p$ with particular fixed points ([[EE10 Natural Selection]]), while drift makes $p$ wander.
2. The relation between gene and genotype frequencies is reached in **a single generation**.
3. Progeny genotype frequencies depend only on the parents' **gene** frequencies, not their genotype frequencies. Slide 9's example: parents $0.3:0.6:0.1$ and $0.2:0.8:0$ both have $p=0.6$, and both give progeny $0.36:0.48:0.16$.
4. The **heterozygote frequency cannot exceed 0.5**, reached at $p=q=0.5$ ($2pq$ is a parabola with maximum $\tfrac12$).
5. When an allele is **rare, it occurs mostly in heterozygotes**: the share of copies of allele $a$ carried by heterozygotes is $pq/(pq+q^2)=p=1-q$. For $q=0.1$: 90 %; $q=0.01$: 99 %; $q=0.001$: 99.9 %. Carriers outnumber affected homozygotes by $2pq/q^2=2p/q$: 18, 198 and 1998 to one. *(Numbers mine.)*

![[fig_ee09_de_finetti.png|560]]
*Figure EE9.1. The de Finetti diagram (slide 10 shows the curves $p^2$, $2pq$, $q^2$ against $p$; the triangle is an equivalent view, extra · beyond). Every population is a point in the triangle with corners AA, Aa, aa; Hardy–Weinberg populations lie on the parabola $Q^2=4PR$. One generation of random mating moves any point **vertically** to the parabola (the allele frequency, the horizontal position, does not change). Made with `scripts/fig_ee09.py`.*


## 6. Why the law matters
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=11|slide 11]]* · <span class="scope-extra-book">extra · book</span> *Templeton pp. 32–35, Hartl pp. 79–80*

1. One of the few **laws** in biology; the subject proceeds by studying **departures** from it.
2. All else equal, **allelic diversity is maintained**.
3. It gave **strong support to Darwin**: Jenkin's blending objection ([[EE08 Evolution - An Introduction]] §5.1) said heritable variation halves every generation; the HW law showed that under Mendelian inheritance it persists indefinitely, which "finally put to rest" the objection and made selection on random mutations plausible again (Templeton p. 34).
4. It extends easily to many alleles and many loci.
5. It gives the frequency of a **recessive allele** and of **carriers** (§9).

Hartl (p. 79) adds why such a restrictive model is fundamental: it is a **reference model**, like a frictionless plane in mechanics; and it splits the life cycle into **gametes → zygotes** (random union gives HW) and **zygotes → adults** (where selection, migration, etc. are added). Later models keep the first half and modify the second — exactly how [[EE10 Natural Selection]] builds its model.

## 7. Testing a population: the χ² test
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=12|slide 12]]* · <span class="scope-extra-book">extra · book</span> *Templeton Box 2.1, Hartl pp. 80–81*

Slide 12's recipe: compute allele frequencies → compute expected genotype frequencies → compare observed with expected numbers. The comparison is the **χ² statistic**
$$\chi^2=\sum_{\text{genotypes}}\frac{(\text{obs}-\text{exp})^2}{\text{exp}},\qquad \text{df}=3-1-1=1$$
(three classes, minus one because the counts sum to $N$, minus one because $p$ was estimated from the same data). Reject HWE at the 5 % level if $\chi^2>3.84$.

> [!example] Two worked tests
> **Pueblo MN** (slide 5; Templeton Box 2.1): expected $0.573\times140=80.2$ MM, $51.5$ MN, $8.26$ NN; $\chi^2=1.59$, $P=0.21$: **fail to reject** HWE.
> **British MN** (Hartl p. 81, Race & Sanger): 298 MM, 489 MN, 213 NN of 1000; $p=0.5425$; expected 294.3, 496.4, 209.3; $\chi^2=0.222$, $P=0.64$.

> [!pitfall] What a non-significant χ² does *not* show
> Statistical tests never prove a null hypothesis: a sample that fits HW proportions only fails to reject them (Templeton p. 33). χ² tests are **not very sensitive** to departures from HWE, so a fit "cannot be taken as evidence that all of the assumptions underlying the model are valid" (Hartl p. 80). Strong selection, for instance, can leave adult genotype frequencies close to HW.

## 8. More than two alleles
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=13|slide 13]]*

With alleles $A_1,\dots,A_k$ at frequencies $p_1,\dots,p_k$, random union gives $(p_1+\dots+p_k)^2$: homozygotes $p_i^2$, heterozygotes $2p_ip_j$. Allele frequency = homozygote frequency + half of every heterozygote containing it.

> [!example] Slide 13: red-cell acid phosphatase, 178 English people
> AA 9.6 %, AB 48.3 %, BB 34.3 %, AC 2.8 %, BC 5.0 %, CC 0.0 %.
> $p_A=9.6+\tfrac12(48.3+2.8)=35.15\%$, $p_B=34.3+\tfrac12(48.3+5.0)=60.95\%$, $p_C=\tfrac12(2.8+5.0)=3.9\%$ — the slide's $0.3515, 0.6095, 0.039$.
> **Why no CC?** Expected CC $=p_C^2\times178=0.0015\times178=0.27$ individuals: fewer than one expected; the chance of seeing none even under HWE is $(1-p_C^2)^{178}=0.76$. Absence is what HWE predicts for so rare an allele.

## 9. Carriers of recessive traits
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=14|slides 14–15]]* · <span class="scope-extra-book">extra · book</span> *Templeton pp. 33–34*

For a recessive trait only two phenotypes are visible (dominant: AA + Aa; recessive: aa). Assuming HWE, the recessive frequency is $q^2$, so $\hat q=\sqrt{\text{freq(aa)}}$ and carriers $=2\hat p\hat q$.

> [!example] Slides 14–15
> **PKU** (1972 study, 1 in 11 000): $q=\sqrt{1/11000}=0.0095$; carriers $2pq=0.019\approx1/53$ — the slide's ".0095 … carriers .019 ≈ 1/50".
> **PTC** (30 % non-tasters, recessive): $q=\sqrt{0.30}=0.548$.
> **Albinism** (1 in 10 000 in Europe): $q=0.01$; carriers $2(0.99)(0.01)=0.0198\approx$ **1 in 51**: about 200 carriers per affected person.

> [!warning] When the square-root estimate is valid
> $\hat q=\sqrt{\text{freq(aa)}}$ **assumes** HWE and cannot test it: two observable classes minus one for the total minus one estimated parameter leaves **0 degrees of freedom** (Templeton p. 34). When all three genotypes are distinguishable, always use $p=P+Q/2$ (true for any genotype frequencies). The square-root formula was the workhorse of 20th-century genetic counselling precisely because carriers could not be identified.

## 10. Every exercise, solved
<span class="scope-taught">taught</span> *practice set ([[PopgenPracticeProblem_Questions only.docx|PopgenPracticeProblem]]); all numbers from `scripts/ee08_10_numbers.py`*

> [!example]- P1. Gm(a+) dominant, Gm(a−) recessive: heterozygotes in three Swedish populations (Broman et al. 1963)
> Gm(a−) is the recessive phenotype, so $q=\sqrt{\text{freq}(a-)}$, heterozygotes $=2pq$:
>
> | region | $N$ | Gm(a−) | $q$ | $p$ | $2pq$ |
> |---|---|---|---|---|---|
> | Norrbotten County | 139 | 44.60 % | 0.6678 | 0.3322 | **0.4437** (≈ 62 people) |
> | Stockholm city and rural district | 509 | 42.24 % | 0.6499 | 0.3501 | **0.4550** (≈ 232) |
> | Malmöhus and Kristianstad counties | 293 | 45.05 % | 0.6712 | 0.3288 | **0.4414** (≈ 129) |
>
> All close to the 0.5 maximum, because $p$ and $q$ are not far from ½.

> [!example]- P2. Icelandic sheep, 1 in 256 yellow-fat (recessive): what proportion of *normal* sheep are carriers?
> $q^2=1/256\Rightarrow q=1/16=0.0625$, $p=15/16$. Carriers in the flock: $2pq=30/256=0.1172$. Among **normal** sheep (excluding the affected): $\dfrac{2pq}{1-q^2}=\dfrac{30/256}{255/256}=\dfrac{30}{255}=\mathbf{0.1176}$, about 120 of the 1020 normal sheep in a flock of 1024. *The conditioning on "normal" is the trap.*

> [!example]- P3. Shorthorn cattle: 260 white, 1430 red, 1130 roan (2820). One locus, random mating?
> Roan is the **heterozygote** (codominance: red RR, roan RW, white WW). $p_R=(2\cdot1430+1130)/5640=0.7074$, $q_W=0.2926$. Expected: red $0.5005\times2820=1411.4$, roan $1167.3$, white $241.4$. $\chi^2=0.25+1.19+1.43=2.88$, 1 df, $P=0.09$: **consistent** with one locus and random mating at the 5 % level (though not by much: slightly fewer heterozygotes than expected).

> [!example]- P4. PTC tasting (Snyder 1934): 3643 people, 70 % tasters (T dominant)
> (a) $q=\sqrt{0.30}=0.5477$, $p=0.4523$; $TT=p^2=0.2046$, $Tt=2pq=0.4954$, $tt=0.3000$.
> (b) A non-taster child needs both taster parents to be $Tt$ and the child $tt$. $P(Tt\mid\text{taster})=\dfrac{2pq}{p^2+2pq}=\dfrac{0.4954}{0.7}=0.7078$, so $P=0.7078^2\times\tfrac14=\mathbf{0.125}$ (algebraically $q^2/(1+q)^2$).

> [!example]- P5. MN blood groups: MM 28.38 %, MN 49.57 %, NN 22.05 %
> $p_M=0.2838+\tfrac12(0.4957)=0.5317$, $q_N=0.4684$. Expected: MM 28.27 %, MN 49.80 %, NN 21.94 % — within 0.25 percentage points of the observed: **in HW equilibrium**. (A χ² needs the sample size, which the problem does not give: for $N=1000$, $\chi^2=0.021$, $P=0.88$; even for $N=10\,000$, $\chi^2=0.21$, $P=0.65$.)

> [!example]- Lecture extras (slides 14–15), and Hartl's esterase example
> Albinism and PKU: §9. **Hartl's esterase-6** (*Drosophila*, $p_F=0.3579$): HW parents 0.1281 : 0.4596 : 0.4123; the six mating types occur at 0.0164, 0.1177, 0.1056, 0.2112, 0.3790, 0.1700, and summing their Mendelian offspring returns exactly 0.1281 : 0.4596 : 0.4123 (Hartl p. 78) — a numerical check of Table 3.1.

## 11. Reading tiers
<span class="scope-taught">taught</span> *[[09_Hardy-Weinberg.pdf#page=16|slide 16]]*

| item | tier |
|---|---|
| lecture slides | syllabus |
| Templeton (2006), Ch. 2, pp. 21–35 | **mandatory** |
| Hartl & Clark, Ch. 3, pp. 74–80 | **mandatory** |
| practice set (five problems) | "imperative" |
| the instructor's warning | "several YouTube videos on this topic… many of them teach absolutely wrong concepts"; one recommended video for basic HW problems |

<!-- interactive:start (generated by scripts/embed_interactive.py; edit the tool in scripts/interactive/tools/, not this block) -->
> [!interactive]+ Interactive: Blending vs particulate inheritance: Jenkin's objection
> A quantitative trait in a randomly mating population of N individuals.
>
> ![[ee_blending.png|720]]
>
> **Try:** Press 'next generation' a few times: the blending histogram collapses to a spike (variance 1 → 0.5 → 0.25 …, theory 0.5^t; measured while building with N = 2000: 0.50, 0.25, 0.13), while the Mendelian one keeps its width. Lower N to 50 to see drift slowly erode the Mendelian variance too.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_blending.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_blending.html) · all tools and coverage: [[Interactive Tools]]

> [!interactive]+ Interactive: Hardy–Weinberg: the de Finetti triangle and drift
> Each population is a point (P, Q, R) of genotype frequencies in the de Finetti triangle; Hardy–Weinberg populations lie on the parabola Q² = 4PR.
>
> ![[ee_hardy_weinberg.png|720]]
>
> **Try:** Set P = 0.2, Q = 0.8, R = 0 and press 'random mating': the point drops to 0.36 : 0.48 : 0.16 (slide 9's example) in one step and stays. Then choose N = 20 and run drift: within about 4N = 80 generations most replicates hit a corner (fixation); with N = 500 they barely move.
>
> [▶ Open the tool in your browser](../Assets/interactive/ee_hardy_weinberg.html) · [absolute link](file:///home/swastik/Documents/notes/Assets/interactive/ee_hardy_weinberg.html) · all tools and coverage: [[Interactive Tools]]

<!-- interactive:end -->

## Map of this chapter
> [!connection] How EE09 connects
> **Builds on:** [[EE08 Evolution - An Introduction]] (Jenkin's objection; Mendel). **Next:** [[EE10 Natural Selection]] (add viability differences in the zygote → adult step). **Earlier in the course:** [[EE07 Conservation Biology]] (drift erodes heterozygosity, $H_t=H_0(1-1/2N_e)^t$: the "large population" assumption failing).
> **Concepts:** [[Hardy-Weinberg Equilibrium]] · [[Allele and Genotype Frequencies]] · [[Chi-Square Goodness-of-Fit Test]] · [[Genetic Drift and Inbreeding Depression]] · [[Wright-Fisher Drift as Diffusion]] · [[Blending Inheritance]]
> **Other subjects:** [[Probability - Course Map]] (independent trials, the multinomial distribution: $(p+q)^2$ is the binomial for two draws; [[PR08 Order Statistics and the Multinomial Distribution]]) · [[TH01 Temperature and the Zeroth Law|thermodynamics]] (an equilibrium reached in one step and neutrally stable is unlike a thermodynamic equilibrium, which is stable)

## Summary
> [!summary] Cheat-sheet
> - $p=P+Q/2$ (always true). HW: $p^2:2pq:q^2$; $p'=p$.
> - **Assumptions**: diploid, sexual, one autosomal locus, Mendelian segregation, no mutation, no migration, no selection (fertility or viability), infinite size, random mating, equal frequencies in the sexes, discrete generations.
> - **Properties**: neutrally stable; reached in one generation (two if the sexes differ); depends on allele frequencies only; $2pq\le\tfrac12$; rare alleles live in heterozygotes.
> - **Importance**: a baseline for every evolutionary force; preserves variation (answers Jenkin); carrier estimates.
> - **χ²** with 1 df (3.84 at 5 %); failing to reject ≠ proving HW.
> - **k alleles**: $(\sum p_i)^2$. **Recessive**: $\hat q=\sqrt{\text{aa}}$, carriers $2pq$ — untestable (0 df).
> - Worked: Pueblo $p=0.757$, $\chi^2=1.59$; PKU $q=0.0095$, carriers 1/53; albinism carriers 1/51; acid phosphatase 0.3515/0.6095/0.039; sheep carriers among normal 30/255; cattle $\chi^2=2.88$; PTC child 0.125.

## Practice
1. Genotype counts are 50 AA, 20 Aa, 30 aa. Find $P,Q,R,p,q$ and the HW expectations. Test with χ².
2. Show algebraically that one generation of random mating from $0.5:0:0.5$ gives HW proportions. What are they?
3. Why is the HW equilibrium called *neutrally* stable? Contrast with the logistic equilibrium $N^*=K$.
4. Prove that $2pq\le\tfrac12$ and find where equality holds.
5. A recessive disease affects 1 in 4900. Estimate the carrier frequency and the ratio of carriers to affected. Why can this population not be tested for HWE from these data?
6. Three alleles with $p_1=0.5$, $p_2=0.3$, $p_3=0.2$: list the six genotype frequencies and check they sum to 1. What is the total heterozygosity?
7. Males have $p=1$, females $p=0$ at an autosomal locus. Give the genotype frequencies in the next two generations.
8. "The sample fits HW, so there is no selection at this locus." Criticise.
9. A population of 10 individuals keeps $p=0.5$ on average but its $p$ wanders. Which HW assumption fails? What happens eventually? (Use the tool.)
10. **Exam-style.** Derive the HW law, stating at each step which assumption you use, and explain why the law was important for the acceptance of Darwin's theory.

> [!example]- Solutions
> 1. $N=100$: $P=0.5,Q=0.2,R=0.3$; $p=0.6$, $q=0.4$; expected 36 : 48 : 16. $\chi^2=(50-36)^2/36+(20-48)^2/48+(30-16)^2/16=5.44+16.33+12.25=34.0$, 1 df, $P\approx6\times10^{-9}$: **reject**; there is a large heterozygote deficit (inbreeding, population mixture, or selection against heterozygotes).
> 2. $p=0.5$; with Weinberg's table only AA×AA ($0.25$), AA×aa ($2\times0.25$) and aa×aa ($0.25$) occur, giving AA $0.25$, Aa $0.5$, aa $0.25$ = $p^2:2pq:q^2$.
> 3. A perturbed $p$ is not restored: the new $p$ is a new equilibrium (a line of equilibria). The logistic $N^*=K$ is asymptotically stable: perturbations decay ([[EE03 Population Dynamics and Chaos]]).
> 4. $2p(1-p)$ has derivative $2-4p=0$ at $p=\tfrac12$, value $\tfrac12$; or $\tfrac12-2pq=\tfrac12(p-q)^2\ge0$.
> 5. $q=1/70$, $2pq=2(69/70)(1/70)=0.0282\approx1/35$; ratio $2p/q=138$. Two phenotype classes, one estimated parameter: 0 df.
> 6. $0.25, 0.09, 0.04$ (homozygotes); $2(0.15)=0.30$, $2(0.10)=0.20$, $2(0.06)=0.12$; sum $=1$. Heterozygosity $1-\sum p_i^2=0.62$.
> 7. Generation 1: all Aa (male A × female a). Generation 2: Aa × Aa → $0.25:0.5:0.25$ (HW at $p=0.5$, reached in the second generation).
> 8. χ² tests are insensitive; selection acting after the census stage, or balanced selection, can leave near-HW proportions; one can only say departures are too small to detect (Hartl p. 80).
> 9. Infinite (large) size: **drift**. Eventually one allele is fixed and heterozygosity is lost ($H_t\approx H_0(1-1/2N)^t$; [[Genetic Drift and Inbreeding Depression]]).
> 10. §3 table, §6 point 3.

## Provenance
> [!provenance]- Source map for this chapter
> | Topic | Source | Scope |
> |---|---|---|
> | Mendel, population genetics, beanbag | [[09_Hardy-Weinberg.pdf#page=2\|sl. 2–4]] | taught |
> | frequencies, Pueblo example | [[09_Hardy-Weinberg.pdf#page=5\|sl. 5]]; Templeton pp. 30–31 | taught |
> | derivation and assumptions | [[09_Hardy-Weinberg.pdf#page=6\|sl. 6]]; Templeton pp. 21–29 (Tables 2.1, 2.3); Hartl pp. 74–77 (Fig. 3.2, Table 3.1) | taught (mandatory readings) |
> | the law, Hardy's letter, Yule–Punnett story | [[09_Hardy-Weinberg.pdf#page=7\|sl. 7–8]]; Templeton p. 32; Hartl p. 79 | taught |
> | five properties | [[09_Hardy-Weinberg.pdf#page=9\|sl. 9–10]] | taught |
> | importance; Jenkin | [[09_Hardy-Weinberg.pdf#page=11\|sl. 11]]; Templeton pp. 34–35; Hartl pp. 79–80 | taught |
> | χ² test, Pueblo and British MN | [[09_Hardy-Weinberg.pdf#page=12\|sl. 12]]; Templeton Box 2.1 (p. 33); Hartl pp. 80–81 | taught |
> | multi-allele, PKU, PTC, albinism | [[09_Hardy-Weinberg.pdf#page=13\|sl. 13–15]]; Templeton pp. 33–34 | taught |
> | readings and warning | [[09_Hardy-Weinberg.pdf#page=16\|sl. 16]] | taught |
> | practice set P1–P5 | `PopgenPracticeProblem_Questions only.docx` (questions only; solutions mine) | taught (practice) |
> | unequal sexes, esterase example | Hartl Problem 3.3, p. 78 | extra/book |
> | rare-allele ratios, χ² values, de Finetti figure, tool | `scripts/ee08_10_numbers.py`, `scripts/fig_ee09.py` | extra/beyond |
>
> **Read and not read.** Slides read in full (text layer). Templeton pp. 21–35 and Hartl pp. 74–81 were OCR'd from scans and read in the parts cited (Templeton's two-locus section, p. 35 onward, only its opening). The practice set has no answer key; all answers are mine and checked by script. The recommended YouTube video was not watched.
