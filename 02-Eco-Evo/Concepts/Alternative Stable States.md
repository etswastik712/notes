---
title: Alternative Stable States
aliases: ["catastrophic shift", "regime shift", "critical transition", "hysteresis"]
subject: eco-evo
type: concept
scope: [taught, extra-book]
by: [slides, scheffer]
status: draft
tags: [subject/eco-evo, type/concept, taught, extra/book, src/slides, src/paper, status/draft]
---
# Alternative Stable States

<span class="scope-taught">taught · in syllabus</span> <span class="scope-extra-book">extra · book</span>

> [!syllabus] In the syllabus vs extra
> 🟢 **taught:** 'the solution is not so simple': the S-shaped response, catastrophic regime shift, tipping point; the slide's remark that this is catastrophe theory ([[06_04-Sep-2026_Biotic-Abiotic Interactions.pdf#page=17|slide 17]])  ·  🟡 **extra · book:** Scheffer, Carpenter, Foley, Folke and Walker (2001), *Nature* 413: 591 (see Box 1); Scheffer and van Nes (2007)

> [!intuition] In one picture
> Two stable states for the same external conditions, like a ball in either of two valleys. Cross the ridge between them and the system falls into the other valley; then returning to the old conditions may not bring it back.

> [!key] Definition
> For the same value of an external condition (e.g. nutrient load) an ecosystem can be in one of two stable states (clear or turbid). When the condition crosses a **tipping point** (fold bifurcation) the system shifts abruptly; the way back needs a lower value than the way forward: **hysteresis**. The same mathematics as the ice-albedo feedback in [[CL04 Feedback and Multiple Steady States]] and [[Bistability and Tipping Points]].

## Mathematics of the fold, in numbers
Equilibria of $\dot x=a-bx+rf(x)$ satisfy $a=bx-rf(x)$: an S-shaped curve when the recycling term is steep enough ($\max rf'>b$). On the stable branches $da/dx>0$ (restoring slope $r f'-b<0$); the middle branch is unstable and separates the two **basins of attraction**. With $b=1,\ r=1.4,\ h=1,\ p=8$ the folds are at $a=0.626$ (clear state vanishes) and $a=0.050$ (turbid state vanishes): bistable between, e.g. $a=0.4$ has $x=0.40$ (stable), $0.95$ (unstable), $1.79$ (stable).

> [!example] Hysteresis in one sentence
> Raising $a$ past 0.626 throws $x$ from about 0.72 up to 2.03 (×2.8); coming back, the system stays high until $a<0.050$, so recovery needs a cut of $1-0.050/0.626=92\,\%$ from the collapse value , not a return to $a=0.626$. **Resilience** is the size of the basin or the distance to the nearest fold; a slow loss of resilience is invisible in the state.

**Evidence and scope.** Shallow lakes (Lake Veluwe: vegetation collapsed in the late 1960s–70s but returned in the 1990s at far lower P), coral reefs, arid lands, oceans; catastrophe theory asks why the Sahara became desert, why reefs collapse. Early warning is difficult; near a fold the restoring slope tends to zero so the relaxation time diverges ([[Relaxation Time]]), the theoretical warning ([[Bistability and Tipping Points]]).

> [!pitfall] Smooth, folded, or just fast?
> Not every abrupt change is a fold: a response to a steep but single-valued curve (Scheffer et al.'s Fig. 1b) is reversible at the same condition. Proving alternative stable states needs hysteresis, an unstable threshold or a perturbation experiment. Related: [[Shallow Lake Regime Shift]], [[Causal Loop Diagram]].

Used in: [[EE06 Eutrophication and Alternative Stable States]]. Related: [[Shallow Lake Regime Shift]] · [[Bistability and Tipping Points]] · [[Ice-Albedo Feedback]].

## Linked from
```dataview
LIST FROM [[]] AND -#type/moc SORT file.name ASC
```
