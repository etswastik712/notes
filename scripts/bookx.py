"""Search / print pages of the Landscapes books (text cached in the job tmp dir).
   python3 scripts/bookx.py find <key> <regex> [maxhits]     -> PDF pages whose text matches
   python3 scripts/bookx.py page <key> <first> [last]        -> text of PDF pages (1-based)
   python3 scripts/bookx.py toc  <key> <first> <last>        -> pages (layout) for reading a table of contents
keys: aa (Anderson & Anderson), ts (Turcotte & Schubert, Bookos), ts2 (geokniga Geodynamics), hu (Huggett), gu (Gutierrez),
      mi (Migon), bi (Bierman & Montgomery), th (Thornbury), gv (Goudie & Viles)"""
import os, re, subprocess, sys, glob
B = "/home/swastik/Documents/notes/earth-and-climate/landscapes-geomorphology/books/"
CACHE = os.environ.get("BOOKCACHE", "/home/swastik/.claude/jobs/63159d7f/tmp/booktxt")
os.makedirs(CACHE, exist_ok=True)
PAT = {"aa": "geomorphology-the-mechanics-and-chemistry*", "ts": "[[]Turcotte*", "ts2": "geokniga*", "hu": "Fundamentals of Geomorphology*",
       "gu": "Geomorphology (Mateo*", "mi": "Geomorphological landscapes*", "bi": "Key concepts*", "th": "Principles of geomorphology*", "gv": "Landscapes and Geomorphology A Very*"}
def path(k):
    g = glob.glob(B + PAT[k]) or glob.glob(B + PAT[k].replace("[[]", "[[]"))
    if not g: g = [f for f in glob.glob(B + "*") if re.match(PAT[k].replace("[[]", r"\["), os.path.basename(f))]
    return g[0]
def text(k):
    c = f"{CACHE}/{k}.txt"
    if not os.path.exists(c):
        subprocess.run(["pdftotext", path(k), c], check=True)
    return open(c, errors="ignore").read().split("\f")
if __name__ == "__main__":
    cmd, k = sys.argv[1], sys.argv[2]
    if cmd == "find":
        rx = re.compile(sys.argv[3], re.I); mx = int(sys.argv[4]) if len(sys.argv) > 4 else 25; n = 0
        for i, p in enumerate(text(k), 1):
            m = rx.search(p)
            if m:
                s = max(0, m.start() - 60); print(f"p{i}: ..." + re.sub(r"\s+", " ", p[s:m.end() + 90])); n += 1
                if n >= mx: break
    elif cmd == "page":
        a = int(sys.argv[3]); b = int(sys.argv[4]) if len(sys.argv) > 4 else a; T = text(k)
        for i in range(a, b + 1): print(f"\n=== PDF p{i} ===\n" + T[i - 1])
