"""Build node-and-arrow diagrams as BOTH an editable Excalidraw note (.excalidraw.md) and a plain SVG twin.

The SVG is what chapters embed (always renders); the Excalidraw file is the editable source for the plugin.
    .venv/bin/python scripts/diagrams.py
Add a diagram by appending a spec to SPECS (nodes with centre x,y and size, arrows between node ids).
"""
import html
import json
import math
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.join(HERE, "..", "Assets", "figures")
EXC = os.path.join(HERE, "..", "Assets", "excalidraw")
os.makedirs(FIG, exist_ok=True)
os.makedirs(EXC, exist_ok=True)

INK, MUTED, SURFACE = "#0b0b0b", "#52514e", "#fcfcfb"
BLUE, ORANGE, AQUA, RED = "#2a78d6", "#eb6834", "#1baf7a", "#e34948"
FILL = {"blue": "#dbe8f9", "orange": "#fbe0d4", "aqua": "#d3f1e6", "grey": "#eeeeea", "red": "#f8d9d9"}


def clip(cx, cy, w, h, tx, ty, gap=6):
    """Point where the ray from the box centre (cx,cy) toward (tx,ty) leaves the box, pushed out by `gap`."""
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    s = min((w / 2) / abs(dx) if dx else math.inf, (h / 2) / abs(dy) if dy else math.inf)
    ln = math.hypot(dx, dy)
    return cx + dx * s + dx / ln * gap, cy + dy * s + dy / ln * gap


SPECS = {
    "Ice-Albedo Feedback Loop": dict(
        size=(760, 470),
        nodes={
            "t":   dict(x=380, y=70,  w=230, h=64, text="Temperature falls\nT ↓", color="blue"),
            "ice": dict(x=620, y=225, w=230, h=64, text="More snow and ice\nice cover ↑", color="grey"),
            "alb": dict(x=380, y=370, w=230, h=64, text="Albedo rises\nα ↑", color="orange"),
            "sw":  dict(x=140, y=225, w=230, h=64, text="Less sunlight absorbed\nS(1−α)/4 ↓", color="orange"),
            "pl":  dict(x=380, y=225, w=250, h=104, text="Planck response\ncolder → σT⁴ falls\n→ restoring (negative)", color="aqua"),
        },
        arrows=[("t", "ice", "+"), ("ice", "alb", "+"), ("alb", "sw", "+"), ("sw", "t", "+")],
        title="Ice–albedo feedback: each link strengthens the cooling (f_α > 0)",
        footer="Net effect on the response:  Λ = Λ_P / (1 − f_α):  larger than the no-feedback Planck response Λ_P",
    ),
}


def svg(name, sp):
    W, H = sp["size"]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H+70}" width="{W}" height="{H+70}" font-family="DejaVu Sans, Helvetica, Arial, sans-serif">',
           f'<rect width="{W}" height="{H+70}" rx="10" fill="{SURFACE}"/>',
           f'<defs><marker id="ah" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="{ORANGE}"/></marker></defs>',
           f'<text x="{W/2}" y="30" text-anchor="middle" font-size="16" font-weight="600" fill="{INK}">{html.escape(sp["title"])}</text>']
    N = sp["nodes"]
    for a, b, lab in sp["arrows"]:
        A, B = N[a], N[b]
        x1, y1 = clip(A["x"], A["y"] + 40, A["w"], A["h"], B["x"], B["y"] + 40)
        x2, y2 = clip(B["x"], B["y"] + 40, B["w"], B["h"], A["x"], A["y"] + 40)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{ORANGE}" stroke-width="2.6" marker-end="url(#ah)"/>')
        if lab:
            out.append(f'<text x="{(x1+x2)/2+ (10 if x2>=x1 else -10):.1f}" y="{(y1+y2)/2-6:.1f}" font-size="20" font-weight="700" fill="{ORANGE}" text-anchor="middle">{html.escape(lab)}</text>')
    for k, n in N.items():
        x, y, w, h = n["x"] - n["w"] / 2, n["y"] + 40 - n["h"] / 2, n["w"], n["h"]
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w}" height="{h}" rx="12" fill="{FILL[n["color"]]}" stroke="{INK}" stroke-width="1.6"/>')
        lines = n["text"].split("\n")
        y0 = n["y"] + 40 - (len(lines) - 1) * 10 + 5
        for i, ln in enumerate(lines):
            out.append(f'<text x="{n["x"]}" y="{y0 + i*20:.1f}" text-anchor="middle" font-size="{15 if i==0 else 14}" fill="{INK}" font-weight="{600 if i==0 else 400}">{html.escape(ln)}</text>')
    out.append(f'<text x="{W/2}" y="{H+52}" text-anchor="middle" font-size="13" fill="{MUTED}">{html.escape(sp["footer"])}</text>')
    out.append("</svg>")
    path = os.path.join(FIG, name + ".svg")
    open(path, "w", encoding="utf-8").write("\n".join(out))
    print(os.path.normpath(path))


def excalidraw(name, sp):
    random.seed(7)
    els, texts = [], []
    N = sp["nodes"]
    ids = {k: f"box_{k}" for k in N}
    bound = {k: [{"id": f"txt_{k}", "type": "text"}] for k in N}

    def base(i, t, x, y, w, h):
        return dict(id=i, type=t, x=x, y=y, width=w, height=h, angle=0, strokeColor=INK, backgroundColor="transparent", fillStyle="solid",
                    strokeWidth=2, strokeStyle="solid", roughness=1, opacity=100, groupIds=[], frameId=None, roundness=None,
                    seed=random.randint(1, 2**31 - 1), version=3, versionNonce=random.randint(1, 2**31 - 1), isDeleted=False,
                    boundElements=[], updated=1761200000000, link=None, locked=False)

    arrow_els = []
    for j, (a, b, lab) in enumerate(sp["arrows"]):
        A, B = N[a], N[b]
        x1, y1 = clip(A["x"], A["y"], A["w"], A["h"], B["x"], B["y"])
        x2, y2 = clip(B["x"], B["y"], B["w"], B["h"], A["x"], A["y"])
        aid = f"arr_{j}"
        e = base(aid, "arrow", x1, y1, x2 - x1, y2 - y1)
        e.update(strokeColor=ORANGE, strokeWidth=3, roundness={"type": 2}, points=[[0, 0], [x2 - x1, y2 - y1]], lastCommittedPoint=None,
                 startBinding={"elementId": ids[a], "focus": 0, "gap": 6}, endBinding={"elementId": ids[b], "focus": 0, "gap": 6},
                 startArrowhead=None, endArrowhead="arrow", elbowed=False)
        arrow_els.append(e)
        bound[a].append({"id": aid, "type": "arrow"})
        bound[b].append({"id": aid, "type": "arrow"})
        if lab:
            tid = f"lab_{j}"
            t = base(tid, "text", (x1 + x2) / 2 - 10, (y1 + y2) / 2 - 28, 20, 28)
            t.update(strokeColor=ORANGE, text=lab, fontSize=24, fontFamily=1, textAlign="center", verticalAlign="top", containerId=None,
                     originalText=lab, autoResize=True, lineHeight=1.25)
            els.append(t)
            texts.append((lab, tid))
    for k, n in N.items():
        x, y, w, h = n["x"] - n["w"] / 2, n["y"] - n["h"] / 2, n["w"], n["h"]
        r = base(ids[k], "rectangle", x, y, w, h)
        r.update(backgroundColor=FILL[n["color"]], roundness={"type": 3}, boundElements=bound[k])
        els.append(r)
        t = base(f"txt_{k}", "text", x + 10, y + 10, w - 20, h - 20)
        t.update(text=n["text"], fontSize=18, fontFamily=1, textAlign="center", verticalAlign="middle", containerId=ids[k],
                 originalText=n["text"], autoResize=True, lineHeight=1.25)
        els.append(t)
        texts.append((n["text"], f"txt_{k}"))
    els.extend(arrow_els)
    title = base("title", "text", 20, -40, sp["size"][0] - 40, 28)
    title.update(text=sp["title"], fontSize=20, fontFamily=1, textAlign="center", verticalAlign="top", containerId=None,
                 originalText=sp["title"], autoResize=True, lineHeight=1.25)
    els.append(title)
    texts.append((sp["title"], "title"))
    scene = {"type": "excalidraw", "version": 2, "source": "https://excalidraw.com", "elements": els,
             "appState": {"gridSize": None, "viewBackgroundColor": "#ffffff"}, "files": {}}
    body = "\n".join(f"{t.replace(chr(10), ' ')} ^{i}" for t, i in texts)
    md = ("---\n\nexcalidraw-plugin: parsed\ntags: [excalidraw, type/diagram]\n\n---\n"
          "==⚠  Switch to EXCALIDRAW VIEW in the MORE OPTIONS menu of this document. ⚠== "
          "You can decompress Drawing data with the command palette: 'Decompress current Excalidraw file'. "
          "For more info check in plugin settings under 'Saving'\n\n\n"
          f"# Excalidraw Data\n\n## Text Elements\n{body}\n\n%%\n## Drawing\n```json\n{json.dumps(scene, ensure_ascii=False)}\n```\n%%\n")
    path = os.path.join(EXC, name + ".excalidraw.md")
    open(path, "w", encoding="utf-8").write(md)
    print(os.path.normpath(path))


if __name__ == "__main__":
    for nm, sp in SPECS.items():
        svg(nm, sp)
        excalidraw(nm, sp)
