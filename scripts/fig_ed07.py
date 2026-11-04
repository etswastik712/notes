"""ED07 figure. .venv/bin/python -W ignore scripts/fig_ed07.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
c=2.99792458e8
fig,ax=plt.subplots(1,3,figsize=(15.5,4.6))
A=ax[0]
x=np.linspace(1.0001,4,400); A.plot(x,1/np.sqrt(1-1/x**2),color=BLUE,label="$v_p/c$"); A.plot(x,np.sqrt(1-1/x**2),color=ORANGE,label="$v_g/c$"); A.plot(x,1/np.sqrt(1-1/x**2)*np.sqrt(1-1/x**2),color=MUTED,ls=":",label="$v_pv_g/c^2=1$")
A.set_ylim(0,3); A.set_xlabel("$\\omega/\\omega_c$"); A.set_ylabel("velocity / $c$"); A.legend(fontsize=8); A.set_title("A  Phase and group velocity in a guide")
B=ax[1]
a,b=2.28e-2,1.01e-2
modes=sorted([(np.hypot(m/a,n/b)*c/2/1e9,m,n) for m in range(0,4) for n in range(0,4) if (m,n)!=(0,0)])[:8]
for i,(f,m,n) in enumerate(modes):
    B.hlines(f,0.1,0.9,color=BLUE if i==0 else ORANGE if i<4 else MUTED,lw=2.5); B.text(0.95,f+(0.9 if (i>0 and abs(f-modes[i-1][0])<0.3) else 0),f"TE{m}{n}  {f:.2f} GHz",va="center",fontsize=8)
B.axhspan(modes[0][0],modes[1][0],color=AQUA,alpha=0.25); B.text(0.12,(modes[0][0]+modes[1][0])/2-0.3,"TE$_{10}$ only",fontsize=8,color=INK)
B.set_xlim(0,1.8); B.set_xticks([]); B.set_ylabel("cutoff frequency (GHz)"); B.grid(False); B.set_title("B  Cutoff ladder, $2.28\\times1.01$ cm guide")
C=ax[2]
a_=1.0; xs=np.linspace(0,a_,200); zs=np.linspace(0,2.0,400); X,Z=np.meshgrid(xs,zs)
kz=2*np.pi/1.0; Ey=np.sin(np.pi*X/a_)*np.cos(kz*Z)
im=C.pcolormesh(Z,X,Ey,cmap="RdBu_r",shading="auto"); C.set_xlabel("$z$ (guide wavelengths)"); C.set_ylabel("$x/a$"); C.set_title("C  TE$_{10}$: $E_y\\propto\\sin(\\pi x/a)\\cos(kz-\\omega t)$"); C.grid(False)
C.set_aspect("auto")
fig.tight_layout(); save(fig,"fig_ed07_guides")
