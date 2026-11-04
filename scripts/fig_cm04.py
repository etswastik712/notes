"""CM04 figure. .venv/bin/python -W ignore scripts/fig_cm04.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
fig,ax=plt.subplots(1,3,figsize=(15.5,4.6))
A=ax[0]
r=np.linspace(0.25,8,600); M2=1.0; al=1.0
Ue=-al/r+M2/(2*r**2); A.plot(r,Ue,color=INK,lw=2.2,label="$U_{\\rm eff}=-\\alpha/r+M^2/2mr^2$")
A.plot(r,-al/r,color=MUTED,ls=":",label="$U=-\\alpha/r$"); A.plot(r,M2/(2*r**2),color=MUTED,ls="--",label="centrifugal")
for E,col,lab in ((-0.5,RED,"circular (minimum of $U_{\\rm eff}$)"),(-0.3,BLUE,"ellipse $E<0$"),(0.0,AQUA,"parabola $E=0$"),(0.3,ORANGE,"hyperbola $E>0$")):
    A.axhline(E,color=col,lw=1.2,label=lab)
A.set_ylim(-0.7,0.8); A.set_xlim(0,8); A.set_xlabel("$r$ ($m=\\alpha=M=1$)"); A.set_ylabel("energy"); A.legend(fontsize=7,loc="upper right"); A.set_title("A  Effective potential: orbit type set by $E$")
B=ax[1]
th=np.linspace(-np.pi,np.pi,1600); p=1.0
for e,col in ((0,BLUE),(0.5,ORANGE),(1.0,AQUA),(1.5,VIOLET)):
    rr=p/(1+e*np.cos(th)); ok=(rr>0)&(rr<12); B.plot((rr*np.cos(th))[ok],(rr*np.sin(th))[ok],color=col,label=f"$e={e}$")
B.plot([0],[0],"o",color=INK); B.set_xlim(-3.5,3.5); B.set_ylim(-3.5,3.5); B.set_aspect("equal"); B.legend(fontsize=8,loc="upper right"); B.set_xlabel("$x/p$"); B.set_ylabel("$y/p$"); B.set_title("B  Conics $p/r=1+e\\cos\\phi$ (focus at origin)")
C=ax[2]
n=-2.1
fr=lambda t,y:[y[2],y[3],-y[0]*np.hypot(y[0],y[1])**(n-1),-y[1]*np.hypot(y[0],y[1])**(n-1)]
s=solve_ivp(fr,[0,45],[1,0,0,1.1],rtol=1e-11,atol=1e-12,dense_output=True,max_step=0.01); t=np.linspace(0,45,40000); x,y=s.sol(t)[:2]
C.plot(x,y,color=BLUE,lw=1); C.plot([0],[0],"o",color=INK); C.set_aspect("equal"); C.set_xlabel("$x$"); C.set_ylabel("$y$"); C.set_title("C  $F\\propto r^{-2.1}$: perihelion advances $19.5^\\circ$/orbit")
fig.tight_layout(); save(fig,"fig_cm04_central")
