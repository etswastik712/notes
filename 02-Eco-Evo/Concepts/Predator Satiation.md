---
title: Predator Satiation
aliases: [predator swamping, swamping the predators, synchronous breeding]
subject: eco-evo
type: concept
scope: [taught, extra-book, extra-beyond]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, extra/beyond, src/slides, src/paper, src/own-notes, status/draft]
---
# Predator Satiation

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span> <span class="scope-extra-beyond">extra · beyond</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** "reproduction is highly synchronous, creating a glut for the predators" ([[01-IntroToBiology_-07-Aug-2026.pdf#page=7|slide 7]]) · 🟡 **extra · book:** the numbers and the caveats from Hopcraft et al. ([[Hopcraft+_Why are Wildebeest the most abundant herbivore.pdf#page=5|PDF p.5–10]]) · 🔵 **extra · beyond:** the toy upper bound.

> [!intuition] A buffet that is too big to finish
> One restaurant can serve only so many diners per hour. If a thousand people arrive in the same hour, most of them are never served; if they arrive evenly over a month, nobody leaves hungry. Synchronous births flood the predators' *capacity*, so any individual calf is less likely to be the one eaten.

> [!key] Definition
> **Predator satiation** (swamping): when prey are produced in a short, dense pulse, predators saturate (limited by their kill rate or by the time to handle each prey), so the **fraction** of prey lost is lower than if the same number appeared spread out in time.

- **Wildebeest numbers:** over 250,000 calves are born in about three weeks from mid-February, about 80 % of the year's calves: roughly 12,000 a day, 500 an hour. Topi spread 70 % of births over three months; hartebeest calve all year ([[Hopcraft+_Why are Wildebeest the most abundant herbivore.pdf#page=5|Hopcraft et al.]]).
- **Needs numbers:** with few animals the same synchrony *attracts* predators and raises losses; it works only above a critical herd size.
- **Rival explanation:** synchrony may instead be a by-product of migration: February might be the only time of year with enough food and time to calve, so selection favoured simultaneous births regardless of predators. The data do not yet exclude it.

> [!extra-beyond]- 🔵 Extra (beyond): a one-line upper bound
> Let $N$ calves be born over $w$ days and let the whole predator guild kill at most $K$ calves per day. Over the birth window at most $Kw$ can be taken, so the loss is bounded by
> $$f_{\max}=\min\!\left(1,\ \frac{Kw}{N}\right),$$
> which is $\propto w$: a shorter window means a lower cap. For $N=250{,}000$ and an assumed $K=1{,}000$ per day: 8.4 % at $w=21$ d, 36 % at 90 d, 100 % at $w\ge250$ d. (My construction; $K$ is an assumption. This is the saturating limit of a Holling type II functional response, met again in [[EE05 Predation]].)
> ![[fig_ee01_swamping.png|700]]

Used in: [[EE01 Introduction to Biology and Ecological Thinking]] · [[Serengeti Wildebeest Migration]].
Connections: [[Proximate and Ultimate Causation]] (the ultimate cause of the timing) · [[EE07 Conservation Biology]] (low numbers reverse the benefit, a form of Allee effect).

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
