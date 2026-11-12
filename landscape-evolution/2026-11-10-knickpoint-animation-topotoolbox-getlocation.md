---
id: landscape-evolution/2026-11-10-knickpoint-animation-topotoolbox-getlocation
aliases: [Knickpoint animation and topotoolbox getlocation (2026-11-10)]
tags: [landscape-evolution, topotoolbox, knickpoints]
trust_tier: agent_written
---

# Knickpoint animation and topotoolbox getlocation (2026-11-10)

A short pointer from the teacher to a topotoolbox blog post (W. Schwanghart, 23 Nov 2020) and an animated GIF showing knickpoints marching upstream through a catchment under the stream power model.

## Covered
- *Knickpoint*: an abrupt change in channel gradient. The post's motivation for `getlocation` was to find where knickpoints are expected, given a model of knickpoint migration. (Web: topotoolbox blog, "Location, location, location!")
- Stream power model, linear form ($n = 1$): knickpoints travel upstream at a velocity set by upstream area. The distance a knickpoint covers in a given time is therefore proportional to $\chi$. Knickpoint celerity is proportional to upslope area to the exponent $m$; in the post's animation time is nondimensional, so only $m$ matters (natural landscapes: roughly 0.3 to 0.8). To get real celerity you also need the erosion efficiency $K$. (Web: blog post and the author's reply in the comments)
- `getlocation(S, ...)` returns locations along a `STREAMobj` where a quantity measured along the network takes given values. By default it queries distance from the outlet (`S.distance`, in map units, so metres for UTM data). Examples from the post: all points 30 km upstream of the outlet; where rivers cross a contour; the location of maximum $k_{sn}$ (steepness index). It also accepts a vector of values, custom GRIDobj or node-attribute data, anonymous functions such as `@max`, and can return a PPS object or cell arrays. (Web: blog post)
- Workflow used (Big Tujunga catchment, data shipped with topotoolbox): `GRIDobj` → `FLOWobj` → `STREAMobj(FD,'minarea',1000)` → `klargestconncomps`. Same chain as in [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]].
- Animation recipe: compute $\chi$ with `chitransform(S,A,'mn',0.4)` (A = `flowacc(FD)`), call `getlocation` for 500 values between min and max of $\chi$ with `'output','cell'`, then plot the points and update them with `set(h,'XData',...,'YData',...)` and `drawnow`. (Web: blog post)

## From the post
"to soumil, deep and their group: I think you'll find this very useful
https://topotoolbox.wordpress.com/2020/11/23/location-location-location/

it animates (using streampower model) the upstream march of a bunch of knickpoints in a catchment"

## Files
- [visualfun.gif](https://drive.google.com/file/d/1sdGQueH0sGfeRSHw1bdnRnFy9TU6zbpF/view?usp=drive_web): animated image; not viewed (image). The linked [blog post](https://topotoolbox.wordpress.com/2020/11/23/location-location-location/) was read in full.

## Related
- [[landscape-evolution/2026-08-11-qgis-and-topotoolbox-tutorials]]: the GRIDobj / FLOWobj / STREAMobj workflow this builds on
- [[05-landscapes-geomorphology/concepts/knickpoint]]: your concept note on knickpoints
- [[05-landscapes-geomorphology/concepts/stream-power-law]]: the model behind the migration
- [[05-landscapes-geomorphology/concepts/chi-transform]]: the $\chi$ coordinate used for the animation
