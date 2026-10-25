---
title: Fractals
aliases: ["self-similarity", "fractal"]
subject: eco-evo
type: concept
scope: [taught]
by: [slides]
status: draft
tags: [subject/eco-evo, type/concept, taught, src/slides, status/draft]
---
# Fractals

<span class="scope-taught">taught · in syllabus</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** the slide: 'self-similarity at multiple scales' and the bifurcation diagram as an example ([[04_PopDyn_Chaos_18Aug_2026.pdf#page=26|slide 26]])

> [!intuition] In one picture
> Zoom into a small piece of the bifurcation diagram and you find a copy of the whole.

> [!key] Definition
> A **fractal** is a set that looks similar at many scales; it has non-integer (fractal) dimension. The bifurcation diagram of a one-humped map is self-similar: each periodic window contains a miniature of the full cascade (the slide shows the logistic map; 'the principle of fractals remains the same').

## Self-similarity and what it means here
A fractal has structure at all scales; its dimension need not be an integer. One-humped maps give fractal bifurcation diagrams: a magnified period-3 window of the logistic map (starting near $a=3.83$) contains three branches that split to 6, 12, ... and repeat the whole tree on a smaller scale. The geometry is tied to the **universality** of the period-doubling cascade: the ratio of successive gaps is $\delta=4.669$ and the ratio of branch widths is $\alpha=2.503$ (both properties of the *class* of single-hump maps).

> [!example] Box-counting in one line
> Cover a set with squares of side $\epsilon$; if $N(\epsilon)\propto\epsilon^{-D}$ then $D$ is its box-counting dimension: a line has $D=1$, a plane $D=2$, the middle-thirds Cantor set $D=\ln2/\ln3=0.63$. The attractor of a chaotic map is a Cantor-like set in the state space: infinitely many layers, zero length in the one-dimensional case.

The slide says "the principle remains the same" for the Ricker diagram: the self-similarity is the same although the pictures differ.

> [!pitfall] Self-similar is not identical
> Magnified copies are *similar*, not exact; and natural fractals (coastlines, cotton prices, Crichton's mountain) are self-similar only over a range of scales. Linked: [[Period Doubling and Route to Chaos]], [[Deterministic Chaos]].

Used in: [[EE03 Population Dynamics and Chaos]]. Related: [[Period Doubling and Route to Chaos]] · [[Deterministic Chaos]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
