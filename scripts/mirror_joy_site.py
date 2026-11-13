"""Mirror Joy Monteiro's course site (https://joymonteiro.github.io/intro_climate_science/) into
earth-and-climate/climate/lecture-notes-slides/joy_intro_climate_science/ (HTML, SVG figures, PDFs, small JS/CSV/JSON assets).
Only URLs under the course prefix are fetched; files are stored unmodified and never executed.
    python3 -I scripts/mirror_joy_site.py
"""
import os, re, sys, urllib.request, urllib.parse
BASE = "https://joymonteiro.github.io/intro_climate_science/"
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "earth-and-climate", "climate", "lecture-notes-slides", "joy_intro_climate_science"))
SKIP_EXT = (".woff2", ".woff", ".ttf", ".otf", ".mp4", ".webm")
seen, queue, log = set(), [BASE], []
def local_path(url):
    rel = url[len(BASE):].split("#")[0].split("?")[0]
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    return os.path.join(ROOT, rel)
def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "course-notes-mirror"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), r.headers.get("Content-Type", "")
while queue:
    url = queue.pop(0).split("#")[0].split("?")[0]
    if url in seen or not url.startswith(BASE):
        continue
    seen.add(url)
    if url.lower().endswith(SKIP_EXT):
        continue
    try:
        data, ct = fetch(url)
    except Exception as e:
        log.append((url, "ERR %s" % e)); continue
    p = local_path(url)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "wb").write(data)
    log.append((url, len(data)))
    if "html" in ct or "javascript" in ct or url.endswith((".js", ".css", ".json")):
        txt = data.decode("utf-8", "ignore")
        refs = set(re.findall(r'(?:src|href)="([^"#]+)"', txt)) | set(re.findall(r'url\("?([^")]+)"?\)', txt)) | set(re.findall(r'"((?:assets|data|figures|img|images)/[^"\\]+\.[A-Za-z0-9]+)"', txt)) | set(re.findall(r"['\"]((?:\./|\.\./)?[A-Za-z0-9_./-]+\.(?:svg|png|jpg|jpeg|csv|json|js|pdf|nc|txt))['\"]", txt))
        for r in refs:
            if r.startswith(("http:", "https:", "data:", "mailto:", "javascript:")) and not r.startswith(BASE):
                continue
            q = urllib.parse.urljoin(url, r)
            if q.startswith(BASE) and q not in seen:
                queue.append(q)
for u, s in log:
    print(s, u[len(BASE):])
print("files:", len([1 for u, s in log if not str(s).startswith("ERR")]), " errors:", len([1 for u, s in log if str(s).startswith("ERR")]))
