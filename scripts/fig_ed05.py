"""ED05 figure. .venv/bin/python -W ignore scripts/fig_ed05.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig,ax=plt.subplots(1,3,figsize=(15.5,4.4))
A=ax[0]
z=np.linspace(0,2*np.pi*2,400)
A.plot(z/(2*np.pi),np.cos(z),color=BLUE,label="$E_x/E_0$"); A.plot(z/(2*np.pi),np.cos(z),color=ORANGE,ls="--",label="$cB_y/E_0$ (in phase)")
A.plot(z/(2*np.pi),np.cos(z)**2,color=AQUA,label="$u/(\\epsilon_0E_0^2)=\\cos^2$"); A.axhline(0.5,color=MUTED,ls=":")
A.set_xlabel("$z/\\lambda$ at $t=0$"); A.legend(fontsize=8,loc="lower right"); A.set_title("A  Plane wave: $E\\parallel\\hat x$, $B\\parallel\\hat y$, in phase")
B=ax[1]
ph=np.linspace(0,2*np.pi,400)
for (a1,a2,d,col,lab) in ((3,3,0,BLUE,"linear $45^\\circ$"),(3,3,np.pi/2,ORANGE,"circular"),(3,4,np.pi/3,AQUA,"elliptical $\\delta=60^\\circ$"),(4,2,np.pi/2,VIOLET,"ellipse, axes aligned")):
    B.plot(a1*np.cos(ph),a2*np.cos(ph+d),color=col,label=lab)
B.set_aspect("equal"); B.set_xlabel("$E_x$"); B.set_ylabel("$E_y$"); B.legend(fontsize=7,loc="upper left",ncol=2); B.set_title("B  Polarization ellipses $(E_x,E_y)$ at fixed $z$")
C=ax[2]
t=np.linspace(0,3,600); w=2*np.pi
C.plot(t,np.cos(w*t)**2,color=BLUE,label="linear: $\\cos^2\\omega t$ (avg 1/2)")
C.plot(t,np.ones_like(t)*(1.0),color=ORANGE,label="circular, same $|E_0|$: constant"); C.axhline(0.5,color=MUTED,ls=":")
C.set_xlabel("$t/T$"); C.set_ylabel("$S/(c\\epsilon_0E_0^2)$"); C.set_ylim(0,1.15); C.legend(fontsize=8,loc="center right"); C.set_title("C  Energy flux: linear oscillates, circular is steady")
fig.tight_layout(); save(fig,"fig_ed05_plane_waves")
