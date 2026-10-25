"""EE02 - loggerhead sea turtle (Crowder et al. 1994), REPRODUCED from the slide-24 matrix and Table 1:
  fig_ee02_lifecycle  : life-cycle graph of the 5-stage matrix (P loops, G arrows, F arrows to stage 1)
  fig_ee02_loggerhead : A r after cutting annual mortality in one stage by 10/50/90 % (their Fig. 4),
                        B elasticity of lambda to stage survival (two conventions), C TED projections (their Fig. 5 idea)
The matrix elements are rebuilt from Table 1 with the Crouse/Caswell stage-duration formulas (max difference 0.003 from Table 2).
"""
from matplotlib.patches import Circle, FancyArrowPatch

from figlib import *

SIG = np.array([0.6747, 0.75, 0.6758, 0.7425, 0.8091])      # annual survival, Table 1
DUR = np.array([1, 7, 8, 6, 32.0])
FEC = np.array([0, 0, 0, 0, 76.5])
NAMES = ["egg/\nhatchling", "small\njuvenile", "large\njuvenile", "subadult", "adult"]


def build(sig, lam0, f=FEC):
    n = len(sig)
    gam = np.zeros(n)
    for i in range(n - 1):
        x = sig[i] / lam0
        gam[i] = x ** (DUR[i] - 1) * (1 - x) / (1 - x ** DUR[i])
    P = sig * (1 - gam); G = sig * gam
    P[-1], G[-1] = sig[-1], 0.0
    A = np.zeros((n, n))
    for i in range(n):
        A[i, i] = P[i]
        if i < n - 1:
            A[i + 1, i] = G[i]
        A[0, i] += f[i] * P[i] + (f[i + 1] * G[i] if i < n - 1 else 0)
    return A


def lam_of(sig, f=FEC):
    lam0 = 0.95
    for _ in range(300):
        ev = np.linalg.eigvals(build(sig, lam0, f))
        new = ev[np.argmax(ev.real)].real
        if abs(new - lam0) < 1e-11:
            break
        lam0 = new
    return lam0


base = lam_of(SIG)
A_slide = np.array([[0, 0, 0, 4.665, 61.896], [.675, .703, 0, 0, 0], [0, .047, .657, 0, 0], [0, 0, .019, .682, 0], [0, 0, 0, .061, .8091]])

# ---------------------------------------------------------------- life-cycle graph
fig, ax = plt.subplots(figsize=(10.2, 3.9))
ax.set_xlim(-1.0, 11.4); ax.set_ylim(-3.5, 1.9); ax.axis("off"); ax.set_aspect("equal")
xs = np.arange(5) * 2.6
for i, x in enumerate(xs):
    ax.add_patch(Circle((x, 0), 0.52, fc="#dbe8f9", ec=BLUE, lw=1.6, zorder=3))
    ax.text(x, 0, str(i + 1), ha="center", va="center", fontsize=13, fontweight="bold", zorder=4)
durs = ["1 yr", "7 yr", "8 yr", "6 yr", ">32 yr"]
for i, x in enumerate(xs):
    ax.text(x, -0.78, NAMES[i] + "\n" + durs[i], ha="center", va="top", fontsize=8.6, color=INK, linespacing=1.25)
# G arrows
for i in range(4):
    ax.add_patch(FancyArrowPatch((xs[i] + 0.55, 0), (xs[i + 1] - 0.55, 0), arrowstyle="-|>", mutation_scale=14, color=BLUE, lw=1.6, zorder=2))
    ax.text((xs[i] + xs[i + 1]) / 2, 0.14, f"$G_{i + 1}$={A_slide[i + 1, i]:.3f}".replace("0.", "."), ha="center", va="bottom", fontsize=8.8, color=BLUE)
# P loops
for i in range(1, 5):
    ax.add_patch(FancyArrowPatch((xs[i] - 0.3, 0.46), (xs[i] + 0.3, 0.46), connectionstyle="arc3,rad=-2.6", arrowstyle="-|>",
                                 mutation_scale=12, color=AQUA, lw=1.5, zorder=2))
    ax.text(xs[i], 1.32, f"$P_{i + 1}$={A_slide[i, i]:.3f}".replace("0.", "."), ha="center", fontsize=8.8, color=AQUA)
ax.text(xs[0], 0.8, "$P_1$=0\n(leaves in 1 yr)", ha="center", fontsize=8.2, color=MUTED, va="bottom")
# F arrows back to stage 1
for j, rad in ((3, 0.55), (4, 0.40)):
    ax.add_patch(FancyArrowPatch((xs[j] - 0.05, -0.54), (xs[0] + 0.42, -0.34), connectionstyle=f"arc3,rad={-rad}", arrowstyle="-|>",
                                 mutation_scale=13, color=ORANGE, lw=1.5, zorder=1))
ax.text(5.2, -3.25, "orange arrows: fecundity back to stage 1,  $F_4$ = 4.665 (subadults about to mature) and $F_5$ = 61.896 (adults)",
        color=ORANGE, fontsize=8.6, ha="center")
ax.set_title("Life-cycle graph of the five-stage loggerhead matrix (slide 24; Crowder et al. 1994, Table 2)", fontsize=10.5, pad=8)
save(fig, "fig_ee02_lifecycle")

# ---------------------------------------------------------------- results
fig, axes = plt.subplots(1, 3, figsize=(12.4, 4.1), gridspec_kw=dict(width_ratios=[1.35, 0.95, 1.05]))
a = axes[0]
labels = ["egg/\nhatchling", "small\njuvenile", "large\njuvenile", "subadult", "adult", "fecundity\n(+%)"]
reds = (0.1, 0.5, 0.9)
vals = np.zeros((6, 3))
for i in range(5):
    for k, red in enumerate(reds):
        s2 = SIG.copy(); s2[i] = 1 - (1 - s2[i]) * (1 - red)
        vals[i, k] = np.log(lam_of(s2))
for k, inc in enumerate(reds):
    f2 = FEC.copy(); f2[4] *= 1 + inc
    vals[5, k] = np.log(lam_of(SIG, f2))
shade = ["#a9c9f2", "#5a9be6", BLUE]
w = 0.26
for k in range(3):
    a.bar(np.arange(6) + (k - 1) * w, vals[:, k], w, color=shade[k], label=f"{int(reds[k] * 100)} %", edgecolor="white", lw=0.5)
a.axhline(np.log(base), color=MUTED, ls="--", lw=1.1)
a.axhline(0, color=INK, lw=1.0)
a.text(2.5, np.log(base) - 0.0045, "dashed: baseline r = -0.050 (λ = 0.952)", ha="center", va="top", fontsize=8.2, color=MUTED)
a.text(-0.45, 0.058, "r > 0: population grows", fontsize=8.2, color=MUTED, va="top")
a.set_xticks(range(6)); a.set_xticklabels(labels, fontsize=8.2)
a.set_ylabel("population growth rate  r = ln λ")
a.set_ylim(-0.062, 0.064)
a.legend(title="mortality cut by", fontsize=8.2, title_fontsize=8.2, loc="upper right", ncol=3, columnspacing=1.0, handlelength=1.1)
a.set_title("A  large juveniles respond most (egg care never reaches r > 0)", fontsize=10)
a.grid(axis="x", visible=False)

# B elasticities
b = axes[1]
el_c, el_p = [], []
for i in range(5):
    s2 = SIG.copy(); s2[i] *= 1.001
    el_c.append((lam_of(s2) - base) / base / 0.001)
ev, V = np.linalg.eig(A_slide); k = np.argmax(ev.real); wv = np.abs(V[:, k].real)
evl, Vl = np.linalg.eig(A_slide.T); kl = np.argmax(evl.real); vv = np.abs(Vl[:, kl].real)
S = np.outer(vv, wv) / (vv @ wv)
lam0 = base
for i in range(5):
    s2 = SIG.copy(); s2[i] += 1e-6
    dA = (build(s2, lam0) - build(SIG, lam0)) / 1e-6
    el_p.append(SIG[i] / lam0 * np.sum(S * dA))
x = np.arange(5)
b.bar(x, el_c, 0.55, color="#a9c9f2", label="λ also moves inside the stage formula\n(sums to 1.0)")
b.plot(x, el_p, "o", color=ORANGE, ms=7, label="Crowder et al. Fig. 2 convention\n(λ held fixed there; sums to 1.6)")
b.set_xticks(x); b.set_xticklabels(["egg", "small\njuv.", "large\njuv.", "sub-\nadult", "adult"], fontsize=8.2)
b.set_ylabel("elasticity of λ to annual survival σ")
b.set_ylim(0, 0.78)
b.legend(fontsize=7.6, loc="upper left")
b.set_title("B  where survival matters", fontsize=10)
b.grid(axis="x", visible=False)

# C TED projections
c = axes[2]
yrs = np.arange(0, 81)
aus = {2: 0.83, 3: 0.885, 4: 0.91}
scen = [("no TEDs", SIG, MUTED)]
for nm, fr, col in (("seasonal offshore TEDs (×0.67)", 0.67, BLUE), ("all waters, all year (×0.99)", 0.99, AQUA)):
    s2 = SIG.copy()
    for idx, v in aus.items():
        s2[idx] += fr * (v - s2[idx])
    scen.append((nm, s2, col))
for nm, s2, col in scen:
    lm = lam_of(s2)
    c.plot(yrs, np.log10(lm ** yrs), color=col, label=f"{nm}: λ={lm:.3f}")
    if lm > 1:
        ty = np.log(10) / np.log(lm)
        c.plot([ty], [1], "o", color=col, ms=5)
        c.text(ty - 0.5, 1.07, f"{ty:.0f} yr", color=col, fontsize=8.4, va="bottom", ha="center")
c.axhline(1, color=INK, lw=0.8, ls=":")
c.axhline(0, color=INK, lw=0.8)
c.set_xlabel("years after the change"); c.set_ylabel("population relative to today (log₁₀)")
c.set_xlim(0, 80); c.set_ylim(-2.1, 1.35)
c.legend(fontsize=7.8, loc="lower left")
c.set_title("C  how long a 10-fold recovery takes", fontsize=10)
fig.tight_layout()
fig.text(0.5, -0.045, "All three panels recomputed from the Table 1 survivals and stage durations (Crowder et al. 1994). C is deterministic and assumes the new stable stage "
         "distribution at once; TED effect = 0.67 or 0.99 of the gap to the Heron Island survivals (0.83, 0.885, 0.91). The paper reports ~70 yr for the seasonal case.",
         ha="center", fontsize=7.8, color=MUTED, wrap=True)
save(fig, "fig_ee02_loggerhead")
print("baseline r", np.log(base))
