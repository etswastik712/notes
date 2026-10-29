"""Graph-view colour groups for the vault: one reproducible spec -> .obsidian/graph.json.

    .venv/bin/python -W ignore scripts/graph_colors.py            # report coverage only (nothing written)
    .venv/bin/python -W ignore scripts/graph_colors.py --apply    # write colorGroups + filter + forces into graph.json
    .venv/bin/python -W ignore scripts/graph_colors.py --preview out.png   # simulated force layout coloured by the groups

Rules this encodes (Obsidian: the FIRST colour group that matches a node wins):
  1. One colour per SUBJECT, keyed on the folder (the vault's subject taxonomy) OR the `subject/<x>` tag.
     Note-type groups (type/moc, type/concept, extra...) are deliberately NOT groups: placed above the subjects
     they repainted every concept note by type and erased the subject clusters; placed below they never fire.
  2. The eight big subjects use the dataviz skill's validated categorical hues (dark-column steps, L 0.48-0.67, which
     keep >= 3:1 on both Obsidian surfaces #1e1e1e and #ffffff).  The hue -> subject assignment was OPTIMISED on the
     real link graph (heavily linked subject pairs get the most separable colours); see ASSIGNMENT below.
  3. Minor subjects use three extra hues found by greedy farthest-point search in OKLab (outside the validated eight,
     measured: min dE 14.9 / 11.0 / 11.4 against the others); Foundations (the shared toolkit that links everything)
     is a neutral grey; Earth-evolution (a one-note stub) shares Eco-Evo's colour until it is written.
  4. The other tool's notes (un-numbered folders, `zettel`) take their course's colour at reduced opacity, so a subject's
     sources sit with its vault notes; everything else of theirs is a dim neutral.
  5. 00-Home (Glossary alone links 640 notes), digests, master, dailies, Assets and scripts are filtered OUT of the
     graph: they link to everything and glue every subject into one hairball.  Use the local graph for them.
To add a subject: add a row to SUBJECTS (before the ones it must out-rank), pick the next colour from EXTRA, re-run --apply.
"""
import argparse
import collections
import glob
import json
import os
import re

import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
GRAPH = os.path.join(ROOT, ".obsidian", "graph.json")

# ---------------------------------------------------------------------------------------------------------------
# Validated categorical hues (dataviz reference palette, dark-column steps) and the extension hues.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#3987e5", "#d95926", "#199e70", "#c98500", "#d55181", "#008300", "#9085e9", "#e66767")
PURPLE, CYAN, BRICK = "#914cad", "#37a1b8", "#a0555c"     # extension hues (greedy OKLab search)
NEUTRAL = "#85857f"                                          # Foundations: shared toolkit, deliberately achromatic

# ASSIGNMENT (hue -> subject) came from an exhaustive search over the 8! permutations maximising the worst
# min(normal-vision dE/15, CVD dE/8) over subject pairs with >= 24 cross-links (links counted with each subject's
# sources and its minor children folded in).  Worst heavy pair: QM-Thermodynamics 13.0 normal / 6.7 CVD.

# (key, label, query, hex)   ORDER MATTERS: first match wins.  Probability precedes Eco-Evo so that Bayes' Theorem
# and AIC (folder 08, tagged probability AND eco-evo) take the probability colour.
SUBJECTS = [
    ("climate",     "Climate",                   "path:01-Climate OR tag:#subject/climate",                         BLUE),
    ("thermo",      "Thermodynamics",            "path:03-Thermodynamics OR tag:#subject/thermo",                   RED),
    ("qm",          "Quantum Mechanics",         "path:06-Quantum-Mechanics OR tag:#subject/qm",                    YELLOW),
    ("probability", "Probability",               "path:08-Probability OR tag:#subject/probability",                 AQUA),
    ("eco-evo",     "Eco-Evo",                   "path:02-Eco-Evo OR tag:#subject/eco-evo",                         ORANGE),
    ("group",       "Group Theory",              "path:10-Group-Theory OR tag:#subject/group-theory",               GREEN),
    ("chem",        "Inorganic Chemistry",       "path:12-Inorganic-Chemistry OR tag:#subject/chemistry",           MAGENTA),
    ("analysis",    "Proofs, Analysis, Topology", "path:11-Proofs-Analysis-Topology OR tag:#subject/analysis",      VIOLET),
    ("landscapes",  "Landscapes",                "path:05-Landscapes-Geomorphology OR tag:#subject/landscapes",     PURPLE),
    ("waves",       "Waves (stub)",              "path:07-Waves OR tag:#subject/waves",                             CYAN),
    ("neuro",       "Neuroscience (stub)",       "path:13-Neuroscience OR tag:#subject/neuroscience",               BRICK),
    ("earth-evo",   "Earth and Life (stub)",     "path:04-Evolution-of-Earth-and-Life OR tag:#subject/earth-evolution", ORANGE),
    ("foundations", "Foundations (toolkit)",     "path:09-Foundations OR tag:#subject/foundations",                 NEUTRAL),
]
COLOR_OF = {k: c for k, _, _, c in SUBJECTS}

SRC_ALPHA, MISC_ALPHA = 0.45, 0.35
# The other tool's layer: source folders, and `zettel` notes (which carry their course as a tag).
SOURCES = [
    ("src-qm",          "sources: PH2113",        "path:ph2113 OR tag:#ph2113",                                                        COLOR_OF["qm"]),
    ("src-chem",        "sources: CH2113",        "path:ch2113 OR tag:#ch2113-principles-of-inorganic-chemistry-august-20",           COLOR_OF["chem"]),
    ("src-group",       "sources: MT3184",        "path:mt3184 OR tag:#mt3184 OR tag:#mt3184-differential-geometry-and-lie-groups",   COLOR_OF["group"]),
    ("src-analysis",    "sources: intro to proofs", "path:intro-to-proofs OR tag:#intro-to-proofs",                                    COLOR_OF["analysis"]),
    ("src-probability", "sources: MT2113",        "path:introduction-to-probability OR tag:#introduction-to-probability OR tag:#mt2113", COLOR_OF["probability"]),
    ("src-climate",     "sources: climate",       "path:introduction-to-climate-science OR tag:#introduction-to-climate-science",     COLOR_OF["climate"]),
    ("src-landscapes",  "sources: landscapes",    "path:landscape-evolution OR tag:#landscape-evolution",                              COLOR_OF["landscapes"]),
]
MISC = ("src-misc", "other tool: maps, inbox, loose notes", "path:zettel OR path:maps OR path:inbox OR path:biology OR path:math", NEUTRAL)

# Notes hidden from the graph (they link to everything).  Obsidian search syntax.  Home.md alone stays visible: it is the
# centre of the graph (Home -> 13 subject maps -> every note, see scripts/graph_spine.py); the other 00-Home notes are hubs
# that glue every subject together (Glossary links 640 notes) and are used through the local graph instead.
SEARCH = ("-path:Assets -path:scripts -path:digests -path:master -path:dailies "
          "-path:00-Home/Conventions -path:00-Home/Dashboard -path:00-Home/Glossary -path:00-Home/PROGRESS "
          "-path:00-Home/Roadmap -path:00-Home/Sources -path:00-Home/Subject -path:00-Home/Tag -path:00-Home/Templates "
          "-path:00-Home/Toolkit")
HOME_GROUP = ("home", "Home (the centre)", 'path:"00-Home/Home.md"', "#f4f1de")

# Forces: shorter links + stronger repulsion + weaker centring = tight clusters with space between them.
FORCES = {"centerStrength": 0.2, "repelStrength": 20, "linkStrength": 1, "linkDistance": 100,
          "nodeSizeMultiplier": 1.1, "lineSizeMultiplier": 0.6, "textFadeMultiplier": -0.5,
          "showArrow": False, "showTags": False, "showAttachments": False, "hideUnresolved": True, "showOrphans": True}


def rgb_int(h):
    return int(h.lstrip("#"), 16)


def all_groups():
    g = [(*HOME_GROUP[:3], HOME_GROUP[3], 1.0)]
    g += [(k, lab, q, c, 1.0) for k, lab, q, c in SUBJECTS]
    g += [(k, lab, q, c, SRC_ALPHA) for k, lab, q, c in SOURCES]
    k, lab, q, c = MISC
    g.append((k, lab, q, c, MISC_ALPHA))
    return g


# ---------------------------------------------------------------------------------------------------------------
# A small evaluator of the search syntax used above (path:, tag:#, OR, leading -path:) so the groups can be tested
# against the real notes without opening Obsidian.
def load_notes():
    skip = {".git", ".obsidian", ".venv", "node_modules", "build", "__pycache__", "attachments"}
    notes = {}
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in skip]
        for f in fn:
            if not f.endswith(".md"):
                continue
            p = os.path.join(dp, f)
            rel = os.path.relpath(p, ROOT)
            t = open(p, encoding="utf-8", errors="ignore").read()
            m = re.match(r"---\n(.*?)\n---", t, re.S)
            fm = {}
            if m:
                try:
                    fm = yaml.safe_load(m.group(1)) or {}
                except Exception:
                    fm = {}
            tg = fm.get("tags") or []
            if isinstance(tg, str):
                tg = tg.replace(",", " ").split()
            tags = [str(x).lstrip("#") for x in tg]
            al = fm.get("aliases") or []
            if isinstance(al, str):
                al = [al]
            notes[rel] = dict(path=p, tags=tags, aliases=[str(a) for a in al], text=t, name=f[:-3])
    return notes


def term_match(term, rel, tags):
    term = term.strip()
    if term.startswith("path:"):
        return term[5:].strip('"').lower() in rel.lower()
    if term.startswith("tag:#"):
        w = term[5:].lower()
        return any(x.lower() == w or x.lower().startswith(w + "/") for x in tags)
    raise ValueError("unsupported term: " + term)


def query_match(query, rel, tags):
    return any(term_match(t, rel, tags) for t in re.split(r"\s+OR\s+", query))


def visible(rel):
    for t in SEARCH.split():
        assert t.startswith("-path:")
        if t[6:].lower() in rel.lower():
            return False
    return True


def assign(notes):
    out = {}
    for rel, n in notes.items():
        if not visible(rel):
            continue
        hit = [g for g in all_groups() if query_match(g[2], rel, n["tags"])]
        out[rel] = (hit[0] if hit else None, hit)
    return out


def report(notes):
    asg = assign(notes)
    cnt = collections.Counter(h[0][0] if h[0] else None for h in asg.values())
    print(f"visible notes: {len(asg)} (hidden by the filter: {len(notes) - len(asg)})")
    for k, lab, q, c, a in all_groups():
        print(f"  {k:16s} {c}  a={a:<4}  {cnt.get(k, 0):4d}  {lab}")
    print(f"  {'(no group)':16s}              {cnt.get(None, 0):4d}")
    for rel, (g, hit) in sorted(asg.items()):
        if g is None:
            print("   UNCOLOURED:", rel)
    multi = collections.Counter()
    for rel, (g, hit) in asg.items():
        if len(hit) > 1:
            multi[(hit[0][0], tuple(x[0] for x in hit[1:]))] += 1
    print("notes matching several groups (first wins):")
    for (a, rest), v in multi.most_common():
        print(f"   {v:4d}  {a} beats {', '.join(rest)}")
    return asg


# ---------------------------------------------------------------------------------------------------------------
def build_config(old):
    cfg = dict(old)
    cfg["search"] = SEARCH
    cfg["collapse-color-groups"] = False
    cfg["colorGroups"] = [{"query": q, "color": {"a": a, "rgb": rgb_int(c)}} for _, _, q, c, a in all_groups()]
    cfg.update(FORCES)
    return cfg


def apply():
    old = json.load(open(GRAPH, encoding="utf-8"))
    cfg = build_config(old)
    json.dump(cfg, open(GRAPH, "w", encoding="utf-8"), indent=2)
    print("wrote", GRAPH, "with", len(cfg["colorGroups"]), "colour groups")


def validate():
    cand = glob.glob("/tmp/claude-*/bundled-skills/*/*/dataviz/scripts/validate_palette.py") + \
        glob.glob("/tmp/claude-*/bundled-skills/*/dataviz/scripts/validate_palette.py")
    if not cand:
        print("(dataviz validator not found; skipped)")
        return
    import importlib.util
    spec = importlib.util.spec_from_file_location("vp", cand[0])
    vp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(vp)
    pal = [(k, c) for k, c in COLOR_OF.items() if c != NEUTRAL]
    uniq = []
    for k, c in pal:
        if c not in [u[1] for u in uniq]:
            uniq.append((k, c))
    worst = sorted(((min(vp.deltaE(a[1], b[1], None), vp.deltaE(a[1], b[1], "protan"), vp.deltaE(a[1], b[1], "deutan")), a[0], b[0])
                    for i, a in enumerate(uniq) for b in uniq[i + 1:]))[:8]
    print("weakest colour pairs (min of normal / protan / deutan, OKLab dE x100):")
    for d, a, b in worst:
        print(f"   {d:5.1f}  {a} - {b}")
    for k, c in uniq + [("foundations", NEUTRAL)]:
        print(f"   {k:12s} {c}  contrast white {vp.contrast(c, '#ffffff'):.2f}  dark {vp.contrast(c, '#1e1e1e'):.2f}")


def preview(notes, asg, out):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import networkx as nx
    names = {}
    for rel, n in notes.items():
        if rel in asg:
            names[n["name"].lower()] = rel
            for a in n["aliases"]:
                names.setdefault(a.lower(), rel)
    G = nx.Graph()
    G.add_nodes_from(asg)
    for rel in asg:
        t = re.sub(r"```.*?```", "", notes[rel]["text"], flags=re.S)
        for m in re.finditer(r"\[\[([^\]]+)\]\]", t):
            l = m.group(1).split("#")[0].split("|")[0].strip().lower()
            l = os.path.basename(l)
            if l.endswith(".md"):
                l = l[:-3]
            q = names.get(l)
            if q and q != rel:
                G.add_edge(rel, q)
    pos = nx.spring_layout(G, k=0.045, iterations=250, seed=3)
    fig, ax = plt.subplots(figsize=(15, 11), dpi=110)
    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#1e1e1e")
    nx.draw_networkx_edges(G, pos, ax=ax, width=0.25, edge_color="#888888", alpha=0.25)
    deg = dict(G.degree())
    for rel in G.nodes:
        g = asg[rel][0]
        col = g[3] if g else "#ff00ff"
        a = g[4] if g else 1.0
        ax.scatter([pos[rel][0]], [pos[rel][1]], s=8 + 3.2 * deg[rel] ** 0.8, color=col, alpha=a, linewidths=0)
    cent = collections.defaultdict(list)
    for rel in G.nodes:
        g = asg[rel][0]
        if g and g[4] == 1.0:
            cent[g[1]].append(pos[rel])
    for lab, pts in cent.items():
        if len(pts) > 5:
            x = sum(p[0] for p in pts) / len(pts)
            y = sum(p[1] for p in pts) / len(pts)
            ax.text(x, y, lab, color="white", fontsize=11, ha="center", va="center", weight="bold",
                    bbox=dict(boxstyle="round", fc="#1e1e1e", ec="none", alpha=0.6))
    ax.set_axis_off()
    fig.savefig(out, facecolor=fig.get_facecolor(), bbox_inches="tight")
    print("preview ->", out, f"({G.number_of_nodes()} nodes, {G.number_of_edges()} edges)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--preview")
    ap.add_argument("--validate", action="store_true")
    a = ap.parse_args()
    notes = load_notes()
    asg = report(notes)
    if a.validate:
        validate()
    if a.preview:
        preview(notes, asg, a.preview)
    if a.apply:
        apply()
