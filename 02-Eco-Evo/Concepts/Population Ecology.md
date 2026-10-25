---
title: Population Ecology
aliases: ["population dynamics", "demography"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Population Ecology

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** what a population is, the three things population ecologists study, and why (conservation, management of useful and harmful species, the unit of evolution) ([[02_StageStructuredDynamics_11-Aug-2026.pdf#page=7|slide 7]])

> [!intuition] In one picture
> Individuals are born, die and move. A population is where these add up to a number that rises, falls or holds steady, so population ecology asks *where* the individuals are, *who* they are (age, stage) and *how their number changes*.

> [!key] Definition
> A **population** is a group of similar individuals inhabiting a defined space at a given time. Population ecology studies their **distribution** (spread over space), **demography** (age structure, survivorship, birth rate) and **dynamics** (how numbers change in time and space). Human demography is the same study applied to people.

## The three questions, and the one equation
Distribution, demography and dynamics are one question at three levels of detail. **Distribution** asks *where* the individuals are (clumped, regular or random over space); **demography** asks *who* they are (age, stage, sex, and the rates attached to each); **dynamics** asks how the total changes. They are linked by the ledger
$$N_{t+1}=N_t+B-D+I-E,$$
births $B$, deaths $D$, immigration $I$, emigration $E$ over one time step. Dividing by $N_t$ turns it into per-capita rates, $\lambda=N_{t+1}/N_t=1+b-d+i-e$, and $r=\ln\lambda$ for a continuous-time description.

> [!example] A population on paper
> $N_t=1000$ with $B=150$, $D=100$, $I=20$, $E=30$: $N_{t+1}=1040$, so $\lambda=1.04$ and $r=\ln1.04=0.039$ per time step. Close the population ($I=E=0$) and the same births and deaths give $\lambda=1.05$. The boundary you draw round a "population" (which areas count as inside) decides whether movement is an $I,E$ term or a birth or death.

> [!pitfall] Population is a convenience, not a fact of nature
> The slide's definition (similar individuals, defined space, given time) leaves the boundaries to you. A lake fish stock is a clear population; a wide-ranging bird may be several populations linked by dispersal ([[Metapopulation]]). Rates that are constant for every individual give geometric growth ([[Exponential Growth]]); the whole of [[EE02 Structured Population Models]] relaxes "every individual is the same".

> [!connection] Why the subject matters in this vault
> The practical reasons on the slide (conservation, pests, harvest, evolution) return as the loggerhead case ([[Loggerhead Turtle and Turtle Excluder Devices]]), invasions ([[Invasive Species]]) and tigers ([[Project Tiger]]).

Used in: [[EE02 Structured Population Models]]. Related: [[Levels of Biological Organisation]] · [[Cohort Life Table]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
