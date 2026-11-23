"""Figure for LS29: D8 routing, channel heads, effective discharge, bedrock profile."""
import numpy as np, math, matplotlib
matplotlib.use("Agg"); import matplotlib.pyplot as plt
z=np.array([[78,72,69,71,58,49],[74,67,56,49,46,50],[69,53,44,37,38,48],
            [64,58,55,22,31,24],[68,61,47,21,16,19],[74,53,34,12,11,12]],float)
nb={1:(0,1),2:(1,1),4:(1,0),8:(1,-1),16:(0,-1),32:(-1,-1),64:(-1,0),128:(-1,1)}
n,m=z.shape; d=np.zeros((n,m),int)
for i in range(n):
  for j in range(m):
    best,bc=0,0
    for c,(di,dj) in nb.items():
      a,b=i+di,j+dj
      if 0<=a<n and 0<=b<m:
        g=(z[i,j]-z[a,b])/(math.sqrt(2) if di and dj else 1)
        if g>best: best,bc=g,c
    d[i,j]=bc
d[5,4]=4  # outlet drains off the grid
acc=np.ones_like(z)
for _,i,j in sorted([(z[i,j],i,j) for i in range(n) for j in range(m)],reverse=True):
  if d[i,j] and (i,j)!=(5,4):
    a,b=i+nb[d[i,j]][0],j+nb[d[i,j]][1]; acc[a,b]+=acc[i,j]
fig,ax=plt.subplots(1,4,figsize=(19,4.6))
a=ax[0]; a.imshow(z,cmap="terrain",vmin=0,vmax=90)
for i in range(n):
  for j in range(m):
    a.text(j-0.32,i-0.22,int(z[i,j]),fontsize=7)
    di,dj=nb[d[i,j]]; a.arrow(j,i,0.38*dj,0.38*di,head_width=0.12,color="k",length_includes_head=True)
    a.text(j+0.05,i+0.38,int(acc[i,j]),fontsize=7,color="navy")
a.set_title("A  D8 on the slide grid\n(black: steepest descent; blue: cells draining through)",fontsize=9); a.set_xticks([]); a.set_yticks([])
R,I=50e-3/3600,10e-3/3600; nM=0.04; tc=5.0
S=np.linspace(0.03,0.6,200)
xc=(tc/(1000*9.81*S))**(1/0.6)*S**0.5/(nM*(R-I))
ax[1].loglog(S,xc,"k"); ax[1].xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%g")); ax[1].xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter()); ax[1].set_xlabel("hillslope gradient S"); ax[1].set_ylabel("distance to channel head x_c (m)")
ax[1].set_title("B  Steeper slopes start channels sooner\n(threshold shear 5 Pa; x_c ∝ S^-7/6)",fontsize=9)
Q=np.linspace(1,300,3000); f=Q**-2.5*np.exp(-5/Q); qs=np.clip(Q-20,0,None)**1.5
ax[2].plot(Q,f/f.max(),label="frequency of Q"); ax[2].plot(Q,qs/qs.max(),label="transport rate at Q")
ax[2].plot(Q,f*qs/(f*qs).max(),"r--",label="product = work done")
ax[2].set_xlabel("discharge Q"); ax[2].legend(fontsize=8); ax[2].set_title("C  Effective discharge: a peak in the product",fontsize=9)
x=np.linspace(0.05,25,400); U=1e-3; kc=2e-3  # x in km
for nexp,c in ((0.6,"k"),):
  C=kc*x**nexp
  zs=np.cumsum((U/C)[::-1]*(x[1]-x[0]))[::-1]
  ax[3].plot(x,zs/zs.max(),c,label="steady state, Q ∝ x^0.6")
zsn=zs/zs.max(); drop=0.12
for t,(xk,cl) in enumerate(((20,"tab:blue"),(13,"tab:orange"),(6,"tab:green"))):
  prof=np.where(x<xk,zsn,zsn-drop)
  ax[3].plot(x,prof,color=cl,lw=1,label=f"after base-level drop, t={t}")
ax[3].set_xlabel("distance downstream from divide"); ax[3].set_ylabel("elevation (scaled)")
ax[3].legend(fontsize=7); ax[3].set_title("D  Concave steady profile; a base-level\nstep travels upstream at C=kρgQ/W",fontsize=9)
plt.tight_layout(); plt.savefig("Assets/figures/fig_ls29_fluvial_slides.png",dpi=130); print("ok")
