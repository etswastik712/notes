"""CM02 figure. .venv/bin/python -W ignore scripts/fig_cm02.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
g=9.81;R=0.5
fig,ax=plt.subplots(1,3,figsize=(15.5,4.4))
A=ax[0]
Om=np.linspace(0,9,400); Oc=np.sqrt(g/R)
A.plot(Om,np.zeros_like(Om),color=BLUE,ls="-" ,label="$\\theta=0$ (stable for $\\Omega<\\Omega_c$)")
mask=Om>Oc; th=np.degrees(np.arccos(g/(Om[mask]**2*R)))
A.plot(Om[mask],th,color=ORANGE,label="$\\cos\\theta_0=g/\\Omega^2R$ (stable)"); A.plot(Om[mask],-th,color=ORANGE)
A.axvline(Oc,color=RED,ls=":"); A.text(Oc+0.1,70,"$\\Omega_c=\\sqrt{g/R}=4.43$",color=RED)
A.set_xlabel("$\\Omega$ (rad/s)"); A.set_ylabel("equilibrium $\\theta$ (deg)"); A.legend(fontsize=8,loc="lower left"); A.set_title("A  Bead on a rotating hoop: pitchfork")
B=ax[1]
th=np.linspace(0,np.pi/2,300)
B.plot(np.degrees(th),3*np.cos(th)-2,color=BLUE,label="$N/Mg=-\\lambda/Mg=3\\cos\\theta-2$")
B.axhline(0,color=MUTED); B.axvline(np.degrees(np.arccos(2/3)),color=RED,ls=":"); B.text(50,0.4,"leaves at $48.19^\\circ$",color=RED)
B.set_xlabel("$\\theta$ (deg)"); B.set_ylabel("normal force $N/Mg$"); B.legend(fontsize=8); B.set_title("B  Mass on a hemisphere: multiplier gives the normal force")
C=ax[2]
s=solve_ivp(lambda t,y:[y[1],-4*y[0]-0.4*y[1]],[0,10],[1,0],rtol=1e-11,atol=1e-13,dense_output=True)
t=np.linspace(0,10,2000); x,v=s.sol(t); E=0.5*v**2+2*x**2
C.plot(t,E,color=BLUE,label="$E(t)$"); C.plot(t,E[0]-np.cumsum(0.4*v**2)*(t[1]-t[0]),color=ORANGE,ls="--",label="$E(0)-\\int 2\\mathcal{F}\\,dt$")
C.set_xlabel("$t$"); C.set_ylabel("energy"); C.legend(fontsize=8); C.set_title("C  Rayleigh function: $\\dot E=-2\\mathcal{F}$")
fig.tight_layout(); save(fig,"fig_cm02_constraints")
