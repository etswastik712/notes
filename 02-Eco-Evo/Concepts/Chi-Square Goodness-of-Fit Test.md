---
title: Chi-Square Goodness-of-Fit Test
aliases: ["chi-square test", "χ² test", "goodness of fit", "HWE test"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, book]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/book, status/draft]
---
# Chi-Square Goodness-of-Fit Test

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** [[09_Hardy-Weinberg.pdf#page=12|EE09 slide 12]] (compare observed with expected)
> 🟡 **extra · book:** Templeton Box 2.1, Hartl p. 81

> [!intuition] In one picture
> Add up squared misfits relative to expectation; if the total is larger than chance usually gives, reject the model.

> [!key] Definition
> $\chi^2=\sum(\text{obs}-\text{exp})^2/\text{exp}$; degrees of freedom = classes − 1 − parameters estimated. For an HWE test with 3 genotypes and $p$ estimated, df = 1; 5 % critical value **3.84**. Pueblo MN $\chi^2=1.59$ ($P=0.21$), British MN 0.22, Shorthorn cattle 2.88 ($P=0.09$).

Failing to reject is not proof (Templeton p. 33); the test is insensitive to departures, so a fit does not validate the assumptions (Hartl p. 80).

Used in: [[EE09 Hardy-Weinberg Equilibrium]]. Related: [[Hardy-Weinberg Equilibrium]] · [[Probability - Course Map]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
