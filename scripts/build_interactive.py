"""Build the vault's interactive HTML tools.
   scripts/interactive/tools/<id>.js  (first line: //META {json})  +  lib.js + base.css  ->  Assets/interactive/<id>.html (self-contained)
   Then: node --check on every script; headless-Firefox preview PNGs -> Assets/interactive/previews/<id>.png; contact sheets for review.
   .venv/bin/python -W ignore scripts/build_interactive.py [--only id1,id2] [--no-shots] [--sheet N]
"""
import json, os, re, subprocess, sys, tempfile, html
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
SRC=os.path.join(HERE,"interactive"); OUT=os.path.join(ROOT,"Assets","interactive"); PRE=os.path.join(OUT,"previews")
JOB=os.environ.get("CLAUDE_JOB_DIR",tempfile.gettempdir())
def load_tools(only=None):
    tools=[]
    for fn in sorted(os.listdir(os.path.join(SRC,"tools"))):
        if not fn.endswith(".js"): continue
        tid=fn[:-3]
        if only and tid not in only: continue
        src=open(os.path.join(SRC,"tools",fn)).read()
        m=re.match(r"//META (\{.*\})\n",src)
        if not m: print("no META in",fn); continue
        meta=json.loads(m.group(1)); meta["id"]=tid
        tools.append((meta,src[m.end():]))
    return tools
def build(meta,code,lib,css):
    code=re.sub(r"-(\([^()]*\))\*\*2",r"-(\1**2)",code)  # JS forbids -(x)**2
    title=html.escape(meta["title"])
    body=f"<!doctype html><html lang=en><head><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'><title>{title}</title><style>{css}</style></head><body><div id=app></div><script>\n{lib}\n(function(){{\nconst META={json.dumps(meta)};ui.init(META.title,META.desc);\n{code}\n}})();\n</script></body></html>"
    return body
def check_js(path):
    html_=open(path).read(); js=re.search(r"<script>\n(.*)</script>",html_,re.S).group(1)
    tmp=os.path.join(JOB,"chk.js"); open(tmp,"w").write(js)
    r=subprocess.run(["node","--check",tmp],capture_output=True,text=True); return r.returncode==0,r.stderr.strip().split("\n")[0:3]
def shot(path,png,w=1060,h=820):
    prof=os.path.join(JOB,"ff"); os.makedirs(prof,exist_ok=True)
    env=dict(os.environ,MOZ_HEADLESS="1")
    subprocess.run(["timeout","60","firefox","--headless","--profile",prof,"--screenshot",png,f"--window-size={w},{h}","file://"+path],capture_output=True,env=env)
def sheet(ids,idx):
    from PIL import Image
    ims=[Image.open(os.path.join(PRE,i+".png")) for i in ids]
    W,H=ims[0].size; sc=0.5; tw,th=int(W*sc),int(H*sc); cols=3; rows=(len(ims)+cols-1)//cols
    S=Image.new("RGB",(tw*cols,th*rows),"white")
    for k,im in enumerate(ims): S.paste(im.resize((tw,th)),((k%cols)*tw,(k//cols)*th))
    p=os.path.join(JOB,f"sheet{idx}.png"); S.save(p); return p
if __name__=="__main__":
    a=sys.argv[1:]; only=None; shots=True; sh=None
    if "--only" in a: only=set(a[a.index("--only")+1].split(","))
    if "--no-shots" in a: shots=False
    lib=open(os.path.join(SRC,"lib.js")).read(); css=open(os.path.join(SRC,"base.css")).read()
    tools=load_tools(only); ok=[]
    os.makedirs(PRE,exist_ok=True)
    for meta,code in tools:
        p=os.path.join(OUT,meta["id"]+".html"); open(p,"w").write(build(meta,code,lib,css))
        good,err=check_js(p)
        if not good: print("SYNTAX ERROR",meta["id"],err); continue
        if shots: shot(p,os.path.join(PRE,meta["id"]+".png"))
        ok.append(meta["id"]); print("built",meta["id"])
    json.dump([m for m,_ in load_tools()],open(os.path.join(SRC,"catalog.json"),"w"),indent=1)
    if "--sheet" in a:
        n=int(a[a.index("--sheet")+1]); ids=ok
        for i in range(0,len(ids),n): print("sheet",sheet(ids[i:i+n],i//n))
