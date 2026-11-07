"""CM11 figure. .venv/bin/python -W ignore scripts/fig_cm11.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import quad, solve_ivp
from scipy.special import ellipk
fig,ax=plt.subplots(1,3,figsize=(15.5,4.7))
A=ax[0];qs=np.linspace(-np.pi,np.pi,800)
for th0,col in ((40,BLUE),(90,AQUA),(140,ORANGE)):
    E=-np.cos(np.radians(th0));pp=np.sqrt(np.maximum(2*(E+np.cos(qs)),0));msk=np.abs(qs)<=np.radians(th0)
    A.fill_between(qs[msk],-pp[msk],pp[msk],color=col,alpha=0.22);A.plot(qs[msk],pp[msk],color=col);A.plot(qs[msk],-pp[msk],color=col)
    I=2/(2*np.pi)*quad(lambda q:np.sqrt(2*(E+np.cos(q))),-np.radians(th0),np.radians(th0))[0];A.text(0,0.0+0.0,"",color=col)
    A.text(-np.radians(th0)+0.05,-0.15-0.0*th0,"$I=%.3f$"%I if th0==40 else "",fontsize=8,color=col)
A.plot(qs,np.sqrt(2*(1+np.cos(qs))),color=RED,lw=1.5,ls="--");A.plot(qs,-np.sqrt(2*(1+np.cos(qs))),color=RED,lw=1.5,ls="--")
A.set_xlabel("$q$");A.set_ylabel("$p$");A.set_title("A  Pendulum: the action $I=\\frac{1}{2\\pi}\\oint p\\,dq$ is the shaded area$/2\\pi$\n(amplitudes $40^\\circ,90^\\circ,140^\\circ$; dashed: separatrix)",fontsize=9.5)
B=ax[1];th=np.linspace(2,175,120);E=-np.cos(np.radians(th))
I=np.array([2/(2*np.pi)*quad(lambda q:np.sqrt(2*(e+np.cos(q))),-np.arccos(-e),np.arccos(-e))[0] for e in E]);om=np.pi/(2*ellipk(np.sin(np.radians(th)/2)**2))
B.plot(I,E+1,color=BLUE,label="energy above the bottom $E+1$");B.plot(I,I,color=MUTED,ls=":",label="small-amplitude: $E+1=I$ ($\\omega=1$)")
B2=B.twinx();B2.plot(I,om,color=ORANGE,label="$\\omega=dE/dI=\\pi/2K$");B2.set_ylabel("$\\omega$",color=ORANGE);B2.set_ylim(0,1.1)
B.set_xlabel("action $I$");B.set_ylabel("$E+1$");B.legend(fontsize=8,loc="upper left");B2.legend(fontsize=8,loc="lower right");B.set_title("B  $E(I)$ and $\\omega(I)=dE/dI$ for the pendulum",fontsize=10)
C=ax[2]
for tau,ls in ((3,"-"),(60,"-")):
    w_=lambda t:1+min(t,tau)/tau
    f=lambda t,y:[y[1],-w_(t)**2*y[0]]
    s=solve_ivp(f,[0,tau+12],[0.0,1.0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.01);t=np.linspace(0,tau+12,6000);q,p=s.sol(t);ww=np.array([w_(x) for x in t]);Et=0.5*p*p+0.5*ww**2*q*q
    C.plot(t/ (tau+12),Et/0.5,color=BLUE if tau==3 else AQUA,lw=1.0,label="$E/E_0$, ramp time %d"%tau);C.plot(t/(tau+12),(Et/ww)/0.5,color=ORANGE if tau==3 else RED,lw=1.2,label="$I/I_0=(E/\\omega)/(E_0/\\omega_0)$, ramp time %d"%tau)
C.set_xlabel("time (fraction of run)");C.set_ylabel("normalised");C.legend(fontsize=7.5,loc="upper left");C.set_title("C  Slow frequency ramp $\\omega:1\\to2$: $E$ doubles, $I=E/\\omega$ stays\n(slow ramp) or wobbles (fast ramp)",fontsize=9.5)
fig.tight_layout();save(fig,"fig_cm11_actionangle")
