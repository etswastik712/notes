"""CM03 figure. .venv/bin/python -W ignore scripts/fig_cm03.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
g=9.81
fig,ax=plt.subplots(1,3,figsize=(15.5,4.4))
A=ax[0]
v1=10.; th1=np.radians(np.linspace(0,89.9,400))
for dU,col in ((0,MUTED),(10,BLUE),(20,ORANGE),(40,AQUA)):
    v2=np.sqrt(v1**2-2*dU); s=v1*np.sin(th1)/v2; ok=s<=1
    A.plot(np.degrees(th1[ok]),np.degrees(np.arcsin(s[ok])),color=col,label=f"$\\Delta U={dU}$ ($\\theta_c={np.degrees(np.arcsin(v2/v1)):.1f}^\\circ$)" if dU else "$\\Delta U=0$")
A.set_xlabel("$\\theta_1$ (deg)"); A.set_ylabel("$\\theta_2$ (deg)"); A.legend(fontsize=8,loc="upper left"); A.set_title("A  Particle crossing a step: $p_\\parallel$ conserved")
B=ax[1]
l=1.0
def sp(t,y):
    th,ph,thd,phd=y; return [thd,phd,np.sin(th)*np.cos(th)*phd**2-g/l*np.sin(th),-2*np.cos(th)/np.sin(th)*thd*phd]
s=solve_ivp(sp,[0,30],[0.8,0,0.5,2.0],rtol=1e-12,atol=1e-13,dense_output=True); t=np.linspace(0,30,3001); th,ph,thd,phd=s.sol(t)
B.plot(t,th,color=BLUE,label="$\\theta(t)$ (varies)"); B.plot(t,l**2*np.sin(th)**2*phd,color=ORANGE,label="$p_\\phi$ (constant)")
E=0.5*l**2*(thd**2+np.sin(th)**2*phd**2)-g*l*np.cos(th); B.plot(t,E/10,color=AQUA,label="$E/10$ (constant)")
B.set_xlabel("$t$"); B.legend(fontsize=8); B.set_title("B  Spherical pendulum: $\\phi$ cyclic, $t$ absent")
C=ax[2]
R=0.5;W=6.0
f=lambda t,y:[y[1],np.sin(y[0])*(W**2*np.cos(y[0])-g/R)]
s=solve_ivp(f,[0,3],[1.0,0],rtol=1e-11,atol=1e-13,dense_output=True); t=np.linspace(0,3,600); th,thd=s.sol(t)
h=0.5*R**2*thd**2-0.5*R**2*W**2*np.sin(th)**2-g*R*np.cos(th); Et=0.5*R**2*thd**2+0.5*R**2*W**2*np.sin(th)**2-g*R*np.cos(th)
C.plot(t,h,color=BLUE,lw=3,label="$h$ (conserved)"); C.plot(t,Et,color=ORANGE,label="$T+U$ (not conserved)")
C.set_xlabel("$t$ (s)"); C.set_ylabel("per unit mass ($\\mathrm{m^2/s^2}$)"); C.legend(fontsize=8); C.set_title("C  Rotating hoop: $h\\neq T+U$")
fig.tight_layout(); save(fig,"fig_cm03_symmetry")
