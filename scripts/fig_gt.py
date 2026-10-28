"""Figures for GT01-GT04.   .venv/bin/python -W ignore scripts/fig_gt.py"""
import itertools, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *
from gt_numbers import *
from matplotlib.patches import Polygon, FancyArrowPatch, Rectangle, Circle

def cyc(p):
    seen, out = set(), []
    for i in range(len(p)):
        if i in seen: continue
        c, j = [], i
        while j not in seen: seen.add(j); c.append(j + 1); j = p[j]
        if len(c) > 1: out.append("(" + "".join(map(str, c)) + ")")
    return "".join(out) or "e"

# --- GT01a: Cayley table of S3 = D3 with the cosets of H = <(12)>
def fig_gt01_cayley():
    names = {(0,1,2): "e", (1,2,0): "r", (2,0,1): "r²", (0,2,1): "s", (2,1,0): "sr", (1,0,2): "sr²"}
    # s=(0,2,1) swaps 1,2 ; define elements as words; compute table by composition
    els = list(names)
    cols = {"e": "#dcdcd6", "r": BLUE, "r²": "#8fb6ea", "s": ORANGE, "sr": "#f4a07d", "sr²": AQUA}
    fig, ax = plt.subplots(1, 2, figsize=(9.6, 4.3), gridspec_kw={"width_ratios": [1.15, 1]})
    a = ax[0]; a.set_aspect("equal"); a.grid(False)
    for i, x in enumerate(els):
        for j, y in enumerate(els):
            z = names[compose(x, y)]
            a.add_patch(Rectangle((j, 5 - i), 1, 1, fc=cols[z], ec="white", lw=1.5))
            a.text(j + .5, 5 - i + .5, z, ha="center", va="center", fontsize=9.5, color=INK)
    for k, x in enumerate(els):
        a.text(k + .5, 6.25, names[x], ha="center", fontsize=9.5, color=MUTED)
        a.text(-.25, 5 - k + .5, names[x], ha="right", va="center", fontsize=9.5, color=MUTED)
    a.set_xlim(-1, 6.2); a.set_ylim(-.2, 6.8); a.axis("off")
    a.set_title("Cayley table of $S_3\\cong D_3$ ($x\\cdot y$: row × column)")
    b = ax[1]; b.axis("off"); b.set_xlim(0, 10); b.set_ylim(0, 8); b.grid(False)
    b.set_title("Left cosets of $H=\\{e,s\\}$ tile the group")
    H = [(0,1,2), (0,2,1)]
    seen = []; y = 6.2
    for g in els:
        c = frozenset(compose(g, h) for h in H)
        if c in seen: continue
        seen.append(c)
        lab = ",".join(names[x] for x in sorted(c, key=lambda t: list(names).index(t)))
        b.add_patch(Rectangle((1, y), 5.5, 1.2, fc=SURFACE, ec=[BLUE, ORANGE, AQUA][len(seen)-1], lw=2.2))
        b.text(3.75, y + .6, "g = %s :   {%s}" % (names[g], lab), ha="center", va="center", fontsize=10.5)
        y -= 2.1
    b.text(3.75, 0.3, "$|G|=|H|\\cdot|G:H|$:  $6=2\\cdot3$", ha="center", fontsize=10.5, color=MUTED)
    save(fig, "fig_gt01_cayley")

# --- GT01b: subgroup lattices of S3 and D4
def fig_gt01_lattice():
    fig, ax = plt.subplots(1, 2, figsize=(10, 4.4))
    def draw(a, nodes, edges, title):
        a.axis("off"); a.grid(False); a.set_title(title)
        for u, v in edges:
            a.plot([nodes[u][0], nodes[v][0]], [nodes[u][1], nodes[v][1]], color=MUTED, lw=1.4, zorder=1)
        for k, (x, y, t, c) in nodes.items():
            a.text(x, y, t, ha="center", va="center", fontsize=9.5, zorder=3,
                   bbox=dict(boxstyle="round,pad=0.3", fc=SURFACE, ec=c, lw=1.8))
        a.set_xlim(-.5, 7); a.set_ylim(-.6, 3.6)
    n1 = {"1": (3.2, 0, "1", MUTED), "a": (.5, 1.5, "$\\langle s\\rangle$", ORANGE), "b": (2.0, 1.5, "$\\langle sr\\rangle$", ORANGE),
          "c": (3.6, 1.5, "$\\langle sr^2\\rangle$", ORANGE), "r": (5.7, 1.5, "$A_3=\\langle r\\rangle$", BLUE), "G": (3.2, 3, "$S_3$", INK)}
    draw(ax[0], n1, [("1","a"),("1","b"),("1","c"),("1","r"),("a","G"),("b","G"),("c","G"),("r","G")], "$S_3$: 6 subgroups ($A_3$ normal)")
    n2 = {"1": (3, 0, "1", MUTED),
          "s1": (.5, 1.5, "$\\langle s\\rangle$", ORANGE), "s2": (1.75, 1.5, "$\\langle sr^2\\rangle$", ORANGE), "z": (3, 1.5, "$Z=\\langle r^2\\rangle$", RED),
          "s3": (4.25, 1.5, "$\\langle sr\\rangle$", ORANGE), "s4": (5.5, 1.5, "$\\langle sr^3\\rangle$", ORANGE),
          "v1": (.8, 2.9, "$V_4=\\{1,r^2,s,sr^2\\}$", AQUA), "c4": (3, 2.9, "$C_4=\\langle r\\rangle$", BLUE), "v2": (5.4, 2.9, "$V_4'=\\{1,r^2,sr,sr^3\\}$", AQUA), "G": (3, 4.0, "$D_4$", INK)}
    draw(ax[1], n2, [("1","s1"),("1","s2"),("1","z"),("1","s3"),("1","s4"),("z","v1"),("z","c4"),("z","v2"),("s1","v1"),("s2","v1"),("s3","v2"),("s4","v2"),("c4","G"),("v1","G"),("v2","G")],
         "$D_4$: 10 subgroups (centre $Z$ lies in all three of order 4)")
    ax[1].set_ylim(-.6, 4.5); ax[1].set_xlim(-.8, 7)
    save(fig, "fig_gt01_lattice")

# --- GT02: S4 -> S3 with kernel V4
def fig_gt02_quotient():
    S4 = list(itertools.permutations(range(4)))
    V = {p for p in S4 if cycle_type(p) in [(1,1,1,1), (2,2)]}
    cos = []; seen = set()
    for g in sorted(S4):
        if g in seen: continue
        c = sorted({compose(g, v) for v in V}); cos.append(c); seen |= set(c)
    fig, ax = plt.subplots(figsize=(9.8, 4.8)); ax.axis("off"); ax.grid(False)
    ax.set_xlim(0, 13); ax.set_ylim(-.5, 8.3)
    cs = [MUTED, BLUE, ORANGE, AQUA, VIOLET, RED]
    for k, c in enumerate(cos):
        y = 7 - k * 1.3
        ax.add_patch(Rectangle((.2, y - .45), 7.2, 1.0, fc=SURFACE, ec=cs[k], lw=2))
        ax.text(3.8, y + .05, "   ".join(cyc(x) for x in c), ha="center", va="center", fontsize=9.5)
        ax.add_patch(Circle((10.8, y + .05), .5, fc=SURFACE, ec=cs[k], lw=2))
        ax.text(10.8, y + .05, "$\\bar g_%d$" % (k + 1), ha="center", va="center", fontsize=10)
        ax.add_patch(FancyArrowPatch((7.5, y + .05), (10.2, y + .05), arrowstyle="-|>", mutation_scale=12, color=cs[k], lw=1.5))
    ax.text(3.8, 8.05, "$G=S_4$ cut into the 6 cosets of $N=V_4$ (first box = $N$ = kernel)", ha="center", fontsize=10.5)
    ax.text(10.8, 8.05, "$G/N\\cong S_3$", ha="center", fontsize=10.5)
    ax.text(9.0, 7.35, "$\\pi$", color=MUTED, fontsize=11)
    save(fig, "fig_gt02_quotient")

# --- GT03: classes and orbit-stabiliser
def fig_gt03_classes():
    fig, ax = plt.subplots(1, 3, figsize=(11, 3.8))
    S4 = set(itertools.permutations(range(4)))
    cl = sorted(((cycle_type(next(iter(c))), len(c)) for c in conj_classes(S4)), key=lambda t: -t[0][0] if False else t[1])
    lab = ["$e$", "(12)(34)", "(12)", "(1234)", "(123)"]
    d = sorted(conj_classes(S4), key=lambda c: len(c))
    lab = {1: "$e$", 3: "(12)(34)", 8: "(123)"}
    names = []
    for c in d:
        t = cycle_type(next(iter(c)))
        names.append({(1,1,1,1): "$e$", (2,2): "(12)(34)", (3,1): "(123)", (2,1,1): "(12)", (4,): "(1234)"}[t])
    ax[0].bar(range(5), [len(c) for c in d], color=BLUE, width=.6)
    for i, c in enumerate(d): ax[0].text(i, len(c) + .2, str(len(c)), ha="center", fontsize=9)
    ax[0].set_xticks(range(5)); ax[0].set_xticklabels(names, fontsize=8); ax[0].set_ylabel("class size")
    ax[0].set_title("Classes of $S_4$: $24=1+3+6+6+8$")
    A5 = {p for p in itertools.permutations(range(5)) if sum(1 for i in range(5) for j in range(i+1, 5) if p[i] > p[j]) % 2 == 0}
    d5 = sorted(len(c) for c in conj_classes(A5))
    ax[1].bar(range(5), d5, color=ORANGE, width=.6)
    for i, v in enumerate(d5): ax[1].text(i, v + .3, str(v), ha="center", fontsize=9)
    ax[1].set_xticks(range(5)); ax[1].set_xticklabels(["$e$", "5-cycle", "5-cycle$'$", "(12)(34)", "(123)"], fontsize=8)
    ax[1].set_title("Classes of $A_5$: $60=1+12+12+15+20$"); ax[1].set_ylabel("class size")
    a = ax[2]; a.set_aspect("equal"); a.axis("off"); a.grid(False)
    sq = np.array([[1, 1], [-1, 1], [-1, -1], [1, -1]], float)
    a.add_patch(Polygon(sq, closed=True, fc="#eaf1fb", ec=BLUE, lw=2))
    for i, p in enumerate(sq):
        a.add_patch(Circle(p, .17, fc=BLUE, ec="white", zorder=3)); a.text(p[0]*1.32, p[1]*1.32, str(i + 1), ha="center", va="center", fontsize=10)
    a.plot([-1.6, 1.6], [-1.6, 1.6], ls="--", color=ORANGE, lw=1.4); a.text(1.55, 1.75, "stabiliser of 1:\n{e, reflection}", color=ORANGE, fontsize=8.5, ha="center")
    a.set_xlim(-2.2, 2.4); a.set_ylim(-2, 2.4)
    a.set_title("$D_4$ on vertices: $|G|=8=|\\mathrm{orbit}|\\cdot|\\mathrm{stab}|=4\\cdot2$")
    save(fig, "fig_gt03_classes")

# --- GT03b: Sylow counting table as figure
def fig_gt03_sylow():
    rows = [("$S_4$", 24, "$2^3\\cdot3$", "2: 3 subgroups of order 8", "3: 4 subgroups of order 3"),
            ("$A_5$", 60, "$2^2\\cdot3\\cdot5$", "2: 5 of order 4", "3: 10 of order 3; 5: 6 of order 5"),
            ("$S_3$", 6, "$2\\cdot3$", "2: 3 of order 2", "3: 1 of order 3 (normal)")]
    fig, ax = plt.subplots(figsize=(10, 2.8)); ax.axis("off"); ax.grid(False); ax.set_xlim(0, 10); ax.set_ylim(0, 4)
    heads = ["group", "order", "factorisation", "Sylow numbers $n_p$ (found by brute force)", ""]
    xs = [.3, 1.9, 3.0, 5.0, 8.4]
    for x, h in zip(xs[:4], heads[:4]): ax.text(x, 3.5, h, fontsize=9.5, fontweight="bold")
    for i, r in enumerate(rows):
        y = 2.6 - i * 1.0
        ax.text(xs[0], y, r[0], fontsize=10); ax.text(xs[1], y, str(r[1]), fontsize=10); ax.text(xs[2], y, r[2], fontsize=10)
        ax.text(xs[3], y, r[3] + ";  " + r[4], fontsize=9.5)
        ax.plot([0.2, 9.8], [y - .5, y - .5], color=GRID, lw=1)
    ax.set_title("Sylow: $n_p\\equiv1\\ (\\mathrm{mod}\\ p)$ and $n_p\\mid|G|/p^e$ (all rows satisfy it)")
    save(fig, "fig_gt03_sylow")

# --- GT04: ammonia C3v: symmetry elements + character table heatmap
def fig_gt04_c3v():
    fig, ax = plt.subplots(1, 2, figsize=(10.6, 4.4), gridspec_kw={"width_ratios": [1, 1.05]})
    a = ax[0]; a.set_aspect("equal"); a.axis("off"); a.grid(False)
    ang = np.radians([90, 210, 330]); H = np.c_[np.cos(ang), np.sin(ang)]
    a.add_patch(Polygon(H, closed=True, fc="#eaf1fb", ec=BLUE, lw=1.8))
    for i, p in enumerate(H):
        a.add_patch(Circle(p, .15, fc=ORANGE, ec="white", zorder=3)); a.text(p[0]*1.28, p[1]*1.28, "H%d" % (i + 1), ha="center", va="center", fontsize=9.5)
        a.plot([-p[0]*1.5, p[0]*1.5], [-p[1]*1.5, p[1]*1.5], ls="--", color=AQUA, lw=1.2)
    a.add_patch(Circle((0, 0), .17, fc=BLUE, ec="white", zorder=4)); a.text(.3, .02, "N (above)", fontsize=8.5, color=MUTED)
    a.text(0, -1.9, "view down the $C_3$ axis: 3 mirror planes $\\sigma_v$ (dashed) through N and one H", ha="center", fontsize=9, color=MUTED)
    a.set_xlim(-1.9, 1.9); a.set_ylim(-2.1, 1.8); a.set_title("NH$_3$: point group $C_{3v}$ (order 6)")
    b = ax[1]; b.grid(False)
    X = np.array([[1, 1, 1], [1, 1, -1], [2, -1, 0]]); im = b.imshow(X, cmap="RdBu", vmin=-2, vmax=2, aspect="auto")
    for (i, j), v in np.ndenumerate(X): b.text(j, i, str(v), ha="center", va="center", fontsize=12, color="white" if abs(v) == 2 else INK)
    b.set_xticks(range(3)); b.set_xticklabels(["$E$", "$2C_3$", "$3\\sigma_v$"]); b.set_yticks(range(3)); b.set_yticklabels(["$A_1$ ($z$)", "$A_2$ ($R_z$)", "$E$ $(x,y)$"])
    b.xaxis.tick_top(); b.set_title("character table (class sizes 1, 2, 3)", pad=26)
    b.text(1, 2.8, "rows orthogonal: $\\sum_C |C|\\chi_i\\chi_j=6\\,\\delta_{ij}$ (checked)", ha="center", fontsize=9, color=MUTED)
    for s in b.spines.values(): s.set_visible(False)
    save(fig, "fig_gt04_c3v")

# --- GT04b: reduction bar: Gamma_3N -> irreps; modes
def fig_gt04_reduce():
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    labs = ["$A_1$", "$A_2$", "$E$"]
    data = {"$\\Gamma(3\\,\\mathrm{H}\\ 1s)$": [1, 0, 1], "$\\Gamma_{3N}$": [3, 1, 4], "$\\Gamma_{trans}$": [1, 0, 1], "$\\Gamma_{rot}$": [0, 1, 1], "$\\Gamma_{vib}$": [2, 0, 2]}
    x = np.arange(5); w = .26
    for k, (c, col) in enumerate(zip(labs, [BLUE, ORANGE, AQUA])):
        ax[0].bar(x + (k - 1) * w, [v[k] for v in data.values()], w, color=col, label=c)
    ax[0].set_xticks(x); ax[0].set_xticklabels(list(data), fontsize=8, rotation=12); ax[0].set_ylim(0, 5); ax[0].legend(ncol=3, loc="upper right"); ax[0].set_ylabel("multiplicity $n_\\Gamma$")
    ax[0].set_title("Reduction by $n_\\Gamma=\\frac{1}{|G|}\\sum_C|C|\\chi\\chi_\\Gamma$")
    ax[1].axis("off"); ax[1].grid(False); ax[1].set_xlim(0, 10); ax[1].set_ylim(0, 8)
    txt = ["$\\Gamma_{3N}=3A_1+A_2+4E$  (dimension $3+1+8=12$)", "$-\\,\\Gamma_{trans}=A_1+E$", "$-\\,\\Gamma_{rot}=A_2+E$", "$\\Gamma_{vib}=2A_1+2E$  (6 modes, 4 frequencies)",
           "all $A_1$ and $E$ modes are IR active ($z$; $x,y$)", "NH$_3$: 3 H 1s SALCs $=A_1+E$  [[CH03 Molecular Orbital Theory Polyatomics]]"]
    for i, t in enumerate(txt): ax[1].text(.2, 7 - i * 1.2, t.replace("[[", "").replace("]]", ""), fontsize=10)
    save(fig, "fig_gt04_reduce")

if __name__ == "__main__":
    for f in (fig_gt01_cayley, fig_gt01_lattice, fig_gt02_quotient, fig_gt03_classes, fig_gt03_sylow, fig_gt04_c3v, fig_gt04_reduce): f()
