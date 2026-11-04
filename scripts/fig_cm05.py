"""CM05 figure. .venv/bin/python -W ignore scripts/fig_cm05.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
fig,ax=plt.subplots(1,3,figsize=(15.5,4.6))
A=ax[0]; chi=np.linspace(0,np.pi,500)
for (m1,m2,col) in ((1,4,BLUE),(1,1,ORANGE),(4,1,AQUA),(2,1,VIOLET)):
    th=np.degrees(np.arctan2(m2*np.sin(chi),m1+m2*np.cos(chi)))
    A.plot(np.degrees(chi),th,color=col,label=f"$m_1/m_2={m1/m2:g}$")
A.plot([0,180],[0,180],color=MUTED,ls=":")
A.set_xlabel("$\\chi$ (centre-of-mass angle, deg)"); A.set_ylabel("$\\theta_1$ (lab angle, deg)"); A.legend(fontsize=8); A.set_title("A  $\\tan\\theta_1=m_2\\sin\\chi/(m_1+m_2\\cos\\chi)$")
B=ax[1]
al=227.51; E=5.0; th=np.radians(np.linspace(8,180,400)); ds=(al/(4*E))**2/np.sin(th/2)**4/100
B.semilogy(np.degrees(th),ds,color=BLUE); B.set_xlabel("scattering angle (deg)"); B.set_ylabel("$d\\sigma/d\\Omega$ (barn/sr)")
B.text(60,3e3,"5 MeV $\\alpha$ on Au\n$\\propto\\sin^{-4}(\\theta/2)$",color=INK); B.set_title("B  Rutherford cross-section")
C=ax[2]
f=lambda t,y:[y[2],y[3],0.5*y[0]/np.hypot(y[0],y[1])**3,0.5*y[1]/np.hypot(y[0],y[1])**3]
cols=[BLUE,ORANGE,AQUA,VIOLET,RED]
for p,col in zip((0.25,0.5,1.0,1.5,2.5),cols):
    s=solve_ivp(f,[0,120],[-30,p,1,0],rtol=1e-10,atol=1e-12,max_step=0.05); C.plot(s.y[0],s.y[1],color=col,label=f"$p={p}$, $\\chi={np.degrees(2*np.arctan(0.5/p)):.0f}^\\circ$")
C.plot([0],[0],"o",color=INK); C.set_xlim(-12,12); C.set_ylim(-3,10); C.legend(fontsize=7,loc="upper left"); C.set_xlabel("$x$"); C.set_ylabel("$y$"); C.set_title("C  Repulsive Coulomb orbits ($\\alpha/mv^2=0.5$)")
fig.tight_layout(); save(fig,"fig_cm05_scattering")
