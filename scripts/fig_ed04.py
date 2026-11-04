"""ED04 figure. .venv/bin/python -W ignore scripts/fig_ed04.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
mu0=4e-7*np.pi; e0=8.8541878128e-12; k=1/(4*np.pi*e0)
fig,ax=plt.subplots(1,3,figsize=(15.5,4.4))
A=ax[0]
Rc=0.05;d=2e-3;I=2.0
t=np.linspace(0,5e-9,200)
E=I*t/(e0*np.pi*Rc**2); P=(E*I/(2*np.pi*Rc))*2*np.pi*Rc*d
dU=e0*E*(I/(e0*np.pi*Rc**2))*np.pi*Rc**2*d
A.plot(t*1e9,P,color=BLUE,lw=3,label="Poynting flux through the rim"); A.plot(t*1e9,dU,color=ORANGE,ls="--",label="$\\mathrm{d}U_E/\\mathrm{d}t$")
A.set_xlabel("$t$ (ns)"); A.set_ylabel("power (W)"); A.legend(fontsize=8); A.set_title("A  Charging capacitor: Poynting flux fills the gap")
B=ax[1]
Q=1e-9;R=1e-2
r=np.linspace(R,6*R,400)
Fin=k*Q**2/(16*R**2)
Fout=0.5*e0*(Q/(4*np.pi*e0))**2*2*np.pi*(1/(2*R**2)-1/(2*r**2))
B.plot(r/R,(Fin+Fout)*1e6,color=BLUE); B.axhline(3*k*Q**2/(16*R**2)*1e6,color=RED,ls=":"); B.text(3.0,3*k*Q**2/(16*R**2)*1e6*0.80,"$F=\\frac{3Q^2}{4\\pi\\epsilon_0\\,16R^2}$",color=RED)
B.set_xlabel("outer radius of the plane $z=0$ ($R$)"); B.set_ylabel("$F_z$ from $T_{zz}$ ($\\mu$N)"); B.set_title("B  Force on the northern half-ball via the stress tensor")
C=ax[2]
n=1000;Q=1e-6;Rs=0.02;a=0.01;I0=1.0
tt=np.linspace(0,1,200); I_t=I0*(1-tt)
Lem=-0.5*mu0*n*I_t*Q*(Rs**2-a**2); Lcyl=-0.5*mu0*n*I0*Q*(Rs**2-a**2)-Lem
K=0.5*mu0*n*Q*(Rs**2-a**2)
C.plot(tt,-K*I_t*1e13,color=BLUE,label="field $L_{em}$"); C.plot(tt,-K*(I0-I_t)*1e13,color=ORANGE,label="cylinders $L_a+L_b$"); C.plot(tt,-K*I0*1e13+0*tt,color=MUTED,ls=":",label="total (conserved)")
C.set_xlabel("fraction of the way the solenoid current is switched off"); C.set_ylabel("angular momentum ($10^{-13}$ J s)")
C.legend(fontsize=8); C.set_title("C  Angular momentum passes from field to cylinders")
fig.tight_layout(); save(fig,"fig_ed04_conservation")
