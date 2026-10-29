"""Graph-view simulator: builds the vault's link graph exactly as Obsidian would draw it (strict link resolution, the filter and
colour groups of .obsidian/graph.json, unresolved links hidden) and runs a d3-force-style layout, so a structure can be judged
before Obsidian is opened.  Qualitative only: Obsidian's force constants are not published, so the parameters are CALIBRATED
against a real screenshot (see --calibrate) rather than known.

    .venv/bin/python -W ignore scripts/graph_sim.py --png scripts/_work/now.png                  # current vault, current graph.json
    .venv/bin/python -W ignore scripts/graph_sim.py --png out.png --charge -40 --dist 100 --center 0.1 --lstrength d3
    .venv/bin/python -W ignore scripts/graph_sim.py --metrics                                    # numbers only

Metrics (all on the simulated layout):
  home_rank     fraction of nodes closer to the centroid than Home            (0 = Home is the most central node)
  ring_cv       coefficient of variation of the 13 map-to-Home distances        (0 = all maps on one circle)
  angle_gap_cv  coefficient of variation of the angular gaps between the maps   (0 = evenly spaced around Home)
  purity        mean fraction of a node's 6 nearest neighbours in its own subject
  tentacle      95th-percentile distance of a node from its subject centroid / median such distance (1 = compact, big = stringy)
"""
import argparse
import collections
import json
import math
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import graph_colors as gc  # noqa: E402
import link_audit as la    # noqa: E402

ROOT = gc.ROOT
HOME = "00-Home/Home.md"
MAPS = {
    "climate": "01-Climate/Climate - Course Map.md", "eco-evo": "02-Eco-Evo/Ecology and Evolution - Course Map.md",
    "thermo": "03-Thermodynamics/Thermodynamics - Course Map.md", "earth-evo": "04-Evolution-of-Earth-and-Life/Evolution of Earth and Life - Course Map.md",
    "landscapes": "05-Landscapes-Geomorphology/Landscapes and Geomorphology - Course Map.md", "qm": "06-Quantum-Mechanics/Quantum Mechanics - Course Map.md",
    "waves": "07-Waves/Waves - Course Map.md", "probability": "08-Probability/Probability - Course Map.md", "foundations": "09-Foundations/09-Foundations.md",
    "group": "10-Group-Theory/Group Theory - Course Map.md", "analysis": "11-Proofs-Analysis-Topology/Proofs, Analysis and Topology - Course Map.md",
    "chem": "12-Inorganic-Chemistry/Inorganic Chemistry - Course Map.md", "neuro": "13-Neuroscience/Neuroscience - Course Map.md"}
SRC_TO_SUBJECT = {"src-qm": "qm", "src-chem": "chem", "src-group": "group", "src-analysis": "analysis", "src-probability": "probability",
                  "src-climate": "climate", "src-landscapes": "landscapes"}


def build_graph(search=None, groups=None):
    """Return (nodes, edges, subject_of, is_source) for the graph Obsidian would draw."""
    by_name, by_file, _, texts = la.index()
    notes = gc.load_notes()
    if search is not None:
        gc.SEARCH = search
    vis = [r for r in texts if gc.visible(r) or r == HOME]
    vis = [r for r in vis if r in notes or r == HOME]
    vis_set = set(vis)
    asg = gc.assign({r: notes[r] for r in vis})
    subj, is_src = {}, {}
    for r in vis:
        g = asg[r][0] if r in asg else None
        key = g[0] if g else None
        top = r.split("/")[0]
        own = bool(la.OWN.match(top))
        if r == HOME:
            subj[r] = "home"
        elif key in SRC_TO_SUBJECT:
            subj[r] = SRC_TO_SUBJECT[key]
        elif key in MAPS:
            subj[r] = key
        else:
            subj[r] = "misc"
        is_src[r] = not own
    idx = {r: i for i, r in enumerate(vis)}
    E = set()
    for r in vis:
        for m in la.LINK.finditer(la.strip_code(texts[r])):
            if m.group(1) == "!":
                continue
            raw = m.group(2).replace("\\|", "|")
            base = raw.split("|")[0].split("#")[0].strip()
            if not base:
                continue
            st, hits = la.resolve(base, by_name, by_file)
            if st == "missing":
                continue
            tgt = hits[0] if len(hits) == 1 else sorted(hits, key=lambda p: (len(p.split("/")), len(p)))[0]
            if tgt in idx and tgt != r:
                a, b = idx[r], idx[tgt]
                E.add((min(a, b), max(a, b)))
    return vis, sorted(E), subj, is_src


def layout(n, edges, dist=100.0, charge=-40.0, center=0.1, lstrength="d3", iters=300, seed=0):
    rng = np.random.default_rng(seed)
    pos = rng.normal(size=(n, 2)) * 80.0
    vel = np.zeros((n, 2))
    e = np.array(edges, dtype=int)
    deg = np.bincount(e.ravel(), minlength=n).astype(float)
    s, t = e[:, 0], e[:, 1]
    st = (1.0 / np.minimum(deg[s], deg[t])) if lstrength == "d3" else np.full(len(e), float(lstrength))
    bias = deg[s] / (deg[s] + deg[t])
    alpha, decay = 1.0, 1 - 0.001 ** (1 / 300)
    for _ in range(iters):
        alpha += (0 - alpha) * decay
        d = pos[t] + vel[t] - pos[s] - vel[s]
        l = np.sqrt((d ** 2).sum(1)) + 1e-6
        f = d * ((l - dist) / l * alpha * st)[:, None]
        np.add.at(vel, t, -f * bias[:, None])
        np.add.at(vel, s, f * (1 - bias)[:, None])
        diff = pos[:, None, :] - pos[None, :, :]
        d2 = np.maximum((diff ** 2).sum(2), 1.0)
        np.fill_diagonal(d2, np.inf)
        vel += (diff / d2[:, :, None] * (-charge) * alpha).sum(1)
        vel -= pos * center * alpha
        pos += vel
        vel *= 0.6
    return pos


def metrics(vis, idx, pos, subj, is_src):
    n = len(vis)
    c = pos.mean(0)
    rad = np.linalg.norm(pos - c, axis=1)
    h = idx[HOME]
    out = {"home_rank": float((rad < rad[h]).mean())}
    mp = [idx[p] for k, p in MAPS.items() if p in idx and subj.get(p) == k and k not in ("waves", "neuro", "earth-evo", "foundations")]
    dm = np.array([np.linalg.norm(pos[i] - pos[h]) for i in mp])
    out["ring_cv"] = float(dm.std() / dm.mean())
    ang = np.sort(np.array([math.atan2(pos[i][1] - pos[h][1], pos[i][0] - pos[h][0]) for i in mp]))
    gaps = np.diff(np.concatenate([ang, [ang[0] + 2 * math.pi]]))
    out["angle_gap_cv"] = float(gaps.std() / gaps.mean())
    sub = np.array([subj[r] for r in vis])
    D = np.linalg.norm(pos[:, None] - pos[None], axis=2)
    np.fill_diagonal(D, 1e9)
    nn = np.argsort(D, axis=1)[:, :6]
    ok = sub != "misc"
    out["purity"] = float((sub[nn] == sub[:, None]).mean(1)[ok].mean())
    tent = []
    for k in set(sub) - {"home", "misc", "waves", "neuro", "earth-evo"}:
        ii = np.where(sub == k)[0]
        if len(ii) > 10:
            dd = np.linalg.norm(pos[ii] - np.median(pos[ii], axis=0), axis=1)
            tent.append(np.percentile(dd, 95) / np.median(dd))
    out["tentacle"] = float(np.mean(tent))
    return out


COL = {k: (c, a) for k, _, _, c, a in gc.all_groups()}
KEY = {"climate": "climate", "thermo": "thermo", "qm": "qm", "probability": "probability", "eco-evo": "eco-evo", "group": "group", "chem": "chem",
       "analysis": "analysis", "landscapes": "landscapes", "waves": "waves", "neuro": "neuro", "earth-evo": "earth-evo", "foundations": "foundations",
       "home": "home", "misc": "src-misc"}


def draw(vis, idx, edges, pos, subj, is_src, out, title=""):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    deg = np.zeros(len(vis))
    for a, b in edges:
        deg[a] += 1
        deg[b] += 1
    fig, ax = plt.subplots(figsize=(13, 10.5), dpi=100)
    fig.patch.set_facecolor("#1a1a1a")
    ax.set_facecolor("#1a1a1a")
    segs = np.array([[pos[a], pos[b]] for a, b in edges])
    from matplotlib.collections import LineCollection
    ax.add_collection(LineCollection(segs, colors="#777777", linewidths=0.12, alpha=0.35))
    for i, r in enumerate(vis):
        c, a = COL.get(KEY[subj[r]], ("#888888", 1.0))
        if r == HOME:
            c, a = "#ffffff", 1.0
        al = 0.45 if is_src[r] else 1.0
        ax.scatter([pos[i][0]], [pos[i][1]], s=5 + 2.2 * deg[i] ** 0.8, color=c, alpha=al, linewidths=0)
    for k, p in MAPS.items():
        if p in idx:
            ax.annotate(k, pos[idx[p]], color="white", fontsize=8, ha="center")
    ax.annotate("HOME", pos[idx[HOME]], color="#ffff88", fontsize=10, ha="center", weight="bold")
    ax.autoscale()
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_title(title, color="white", fontsize=10)
    fig.savefig(out, bbox_inches="tight", facecolor=fig.get_facecolor())
    plt.close(fig)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--png")
    ap.add_argument("--metrics", action="store_true")
    ap.add_argument("--dist", type=float, default=100)
    ap.add_argument("--charge", type=float, default=-40)
    ap.add_argument("--center", type=float, default=0.1)
    ap.add_argument("--lstrength", default="d3")
    ap.add_argument("--iters", type=int, default=300)
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    vis, edges, subj, is_src = build_graph()
    idx = {r: i for i, r in enumerate(vis)}
    print(f"nodes {len(vis)}  edges {len(edges)}")
    pos = layout(len(vis), edges, a.dist, a.charge, a.center, a.lstrength, a.iters, a.seed)
    m = metrics(vis, idx, pos, subj, is_src)
    print("  ".join(f"{k}={v:.2f}" for k, v in m.items()))
    if a.png:
        os.makedirs(os.path.dirname(os.path.abspath(a.png)), exist_ok=True)
        draw(vis, idx, edges, pos, subj, is_src, a.png, f"dist={a.dist} charge={a.charge} center={a.center} link={a.lstrength}   " + "  ".join(f"{k}={v:.2f}" for k, v in m.items()))
        print("wrote", a.png)


if __name__ == "__main__":
    main()
