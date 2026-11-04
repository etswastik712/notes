"""CM06 figure. .venv/bin/python -W ignore scripts/fig_cm06.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
fig,ax=plt.subplots(1,3,figsize=(15.5,4.6))
A=ax[0]; w0=1.;a=0.1
f=lambda t,y:[y[2],y[3],-w0**2*y[0]+a*y[1],-w0**2*y[1]+a*y[0]]
s=solve_ivp(f,[0,80],[1,0,0,0],rtol=1e-11,atol=1e-12,dense_output=True); t=np.linspace(0,80,4000); x,y=s.sol(t)[:2]
A.plot(t,x,color=BLUE,label="$x(t)$",lw=1.2); A.plot(t,y,color=ORANGE,label="$y(t)$",lw=1.2)
env=np.cos((np.sqrt(1.1)-np.sqrt(0.9))*t/2); A.plot(t,env,color=MUTED,ls=":"); A.plot(t,-env,color=MUTED,ls=":")
A.set_xlabel("$t$"); A.legend(fontsize=8,loc="lower left"); A.set_title("A  Coupled oscillators: beats")
B=ax[1]; g=np.linspace(0.3,1.7,4000)
w1s,w2s=0.9,1.1
xa=0.5*(1/(w2s-g**2)+1/(w1s-g**2)); ya=0.5*(1/(w2s-g**2)-1/(w1s-g**2))
B.semilogy(g,np.abs(xa)+1e-4,color=BLUE,label="$|x|$ (force acts on $x$)"); B.semilogy(g,np.abs(ya)+1e-4,color=ORANGE,label="$|y|$")
B.axvline(1.0,color=RED,ls=":"); B.text(1.02,3e-4,"$x=0$ at $\\gamma=\\omega_0$",color=RED,fontsize=8)
B.set_ylim(1e-4,1e3); B.set_xlabel("driving frequency $\\gamma/\\omega_0$"); B.set_ylabel("amplitude per unit force"); B.legend(fontsize=8,loc="upper left"); B.set_title("B  Forced response: two resonances, one anti-resonance")
C=ax[2]
for k,(A2,col,lab) in enumerate(((1.4142,BLUE,"slow mode $\\omega_1=0.765\\sqrt{g/l}$: $(1,\\ 1.414)$"),(-1.4142,ORANGE,"fast mode $\\omega_2=1.848\\sqrt{g/l}$: $(1,\\ -1.414)$"))):
    x0=k*3.0
    C.plot([x0,x0+0.25*1],[0,-1],color=col,lw=2); C.plot([x0+0.25*1,x0+0.25*1+0.25*A2],[-1,-2],color=col,lw=2); C.plot(x0,0,"s",color=INK)
    C.plot([x0+0.25,x0+0.25+0.25*A2],[-1,-2],"o",color=col); C.text(x0-0.7,-2.6-0.45*k,lab,fontsize=8,color=col)
C.set_xlim(-1,5); C.set_ylim(-3.6,0.4); C.set_aspect("equal"); C.axis("off"); C.set_title("C  Double pendulum ($m_1=m_2$, $l_1=l_2$): normal modes")
fig.tight_layout(); save(fig,"fig_cm06_oscillations")
