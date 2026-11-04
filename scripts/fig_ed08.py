"""ED08 figure. .venv/bin/python -W ignore scripts/fig_ed08.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig,ax=plt.subplots(1,3,figsize=(15.5,4.6))
A=ax[0]; t=1.0; x=np.linspace(-1.6,1.6,801)
Az=np.where(abs(x)<t,0.25*(t-abs(x))**2,0); Ez=np.where(abs(x)<t,-0.5*(t-abs(x)),0); By=np.where(abs(x)<t,0.5*np.sign(x)*(t-abs(x)),0)
A.plot(x,Az,color=BLUE,label="$A_z$ ($\\mu_0k/4c=1/4$)"); A.plot(x,Ez,color=ORANGE,label="$E_z=-\\partial_tA_z$"); A.plot(x,By,color=AQUA,label="$B_y=-\\partial_xA_z$")
A.axvline(1,color=MUTED,ls=":"); A.axvline(-1,color=MUTED,ls=":"); A.text(0.03,-0.52,"sheet at $x=0$:\n$B_y$ jumps by $kt$",fontsize=8)
A.set_xlabel("$x$ ($c=1$, $t=1$)"); A.legend(fontsize=8,loc="upper right"); A.set_title("A  Current sheet switched on at $t=0$ (Griffiths Ex. 10.1)")
B=ax[1]
g=np.linspace(-1,1,9); X,Y=np.meshgrid(g,g)
B.quiver(X-0.02,Y,0*X,2*X,color=BLUE,angles="xy",scale=30,width=0.004,label="Landau $A_1=(0,Bx,0)$")
B.quiver(X+0.02,Y,-Y,X,color=ORANGE,angles="xy",scale=30,width=0.004,label="symmetric $A_2=\\frac{B}{2}(-y,x,0)$")
B.set_aspect("equal"); B.set_ylim(-1.2,1.7); B.legend(fontsize=8,loc="upper right"); B.set_xlabel("$x$"); B.set_ylabel("$y$"); B.set_title("B  Same $B=2\\hat z$, different $A$ (differ by $\\nabla\\lambda$)")
C=ax[2]
r=np.linspace(0.3,3,300)
for tt,col in ((1,BLUE),(2,ORANGE),(3,AQUA)): C.plot(r,tt/r**2,color=col,label=f"gauge 1: $|A|\\propto t/r^2$, $t={tt}$")
C.plot(r,1/r,color=INK,lw=2.2,label="gauge 2: $V\\propto1/r$, $A=0$")
C.set_ylim(0,6); C.set_xlabel("$r$ (units $q/4\\pi\\epsilon_0=1$)"); C.legend(fontsize=7,loc="upper right"); C.set_title("C  Same Coulomb field from $V=0$ and from $A=0$")
fig.tight_layout(); save(fig,"fig_ed08_gauge")
