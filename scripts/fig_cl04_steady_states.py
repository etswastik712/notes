"""CL04 - multiple steady states of the zero-d model with the ramp albedo of Argha L4 slide 45/47.

  alpha(T) = 0.7                          T < 253
             0.7 - 0.5 (T-253)/40         253 <= T <= 293
             0.2                          T > 293
  S = 1361 W m-2.   Absorbed: S/4 (1-alpha(T)).   Emitted: EPS * sigma T^4.

NOTE: the printed equation on slide 45 shows plain sigma T^4, but the slide's own Mathematica code plots
`.6 sigma T^4` (an effective emissivity 0.6, i.e. a crude greenhouse effect).  Only with EPS = 0.6 do three steady
states appear (~235 K, ~274 K, ~299 K, matching the circles drawn on slide 47).  With EPS = 1 the only
steady state is the snowball one (206 K); the script prints both cases.
"""
from scipy.optimize import brentq

from figlib import *

EPS = 0.6


def alpha(T):
    T = np.asarray(T, float)
    return np.where(T < 253, 0.7, np.where(T <= 293, 0.7 - 0.5 * (T - 253) / 40.0, 0.2))


def asr(T):
    return S0 / 4 * (1 - alpha(T))


def olr(T, eps=EPS):
    return eps * SIGMA * np.asarray(T, float) ** 4


def roots_of(eps, lo=180.0, hi=330.0):
    T = np.linspace(lo, hi, 3001)
    n = asr(T) - olr(T, eps)
    out = []
    for i in range(len(T) - 1):
        if n[i] * n[i + 1] < 0:
            out.append(brentq(lambda x: float(asr(x) - olr(x, eps)), T[i], T[i + 1]))
    return np.array(out)


for eps in (1.0, EPS):
    r = roots_of(eps)
    sl = [float((asr(x + 0.01) - olr(x + 0.01, eps)) - (asr(x - 0.01) - olr(x - 0.01, eps))) / 0.02 for x in r]
    print(f"eps={eps}: steady states (K) {np.round(r, 1)}   d(net)/dT {np.round(sl, 2)}  (negative = stable)")

roots = roots_of(EPS)
slopes = [float((asr(x + 0.01) - olr(x + 0.01)) - (asr(x - 0.01) - olr(x - 0.01))) / 0.02 for x in roots]
stable = [s < 0 for s in slopes]
T = np.linspace(200, 320, 1201)
net = asr(T) - olr(T)

fig, (a, b) = plt.subplots(2, 1, figsize=(7.2, 6.6), sharex=True, gridspec_kw={"height_ratios": [1.25, 1]})
a.plot(T, asr(T), color=ORANGE, label=r"absorbed solar  $\frac{S}{4}\,[1-\alpha(T)]$")
a.plot(T, olr(T), color=BLUE, label=r"emitted  $0.6\,\sigma T^4$")
a.plot(T, olr(T, 1.0), color=MUTED, lw=1.2, ls=":", label=r"$\sigma T^4$ (no greenhouse): only the snowball state")
for r, s in zip(roots, stable):
    a.plot([r], [float(olr(r))], "o", ms=8, mfc=(INK if s else SURFACE), mec=INK, mew=1.6, zorder=6)
a.set_ylabel("flux (W m$^{-2}$)")
a.set_ylim(30, 380)
a.legend(loc="upper left", fontsize=8.2)
a.set_title("Three steady states: two stable (●), one unstable (○)")
for r, nm, dx, dy in zip(roots, ["snowball", "unstable", "ice-free"], [34, 30, -6], [-24, -26, 26]):
    a.annotate(f"{nm}\n{r:.0f} K", (r, float(olr(r))), xytext=(dx, dy), textcoords="offset points", ha="center", fontsize=8.5)

b.axhline(0, color=MUTED, lw=0.8)
b.plot(T, net, color=INK)
b.set_ylabel(r"net heating  $\propto\ dT/dt$  (W m$^{-2}$)")
b.set_xlabel("global-mean temperature T (K)")
ys = -34
edges = [200] + list(roots) + [320]
for lo, hi in zip(edges[:-1], edges[1:]):
    mid = 0.5 * (lo + hi)
    d = np.sign(float(asr(mid) - olr(mid)))
    L = min(hi - lo, 30) * 0.8
    b.annotate("", xy=(mid + d * L / 2, ys), xytext=(mid - d * L / 2, ys), arrowprops=dict(arrowstyle="-|>", color=MUTED, lw=1.6))
for r, s in zip(roots, stable):
    b.plot([r], [0], "o", ms=8, mfc=(INK if s else SURFACE), mec=INK, mew=1.6, zorder=6)
b.set_ylim(-45, 40)
b.annotate("arrows: direction the temperature drifts", (205, ys), xytext=(0, -14), textcoords="offset points", fontsize=8, color=MUTED)
save(fig, "fig_cl04_steady_states")
