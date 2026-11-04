"""ED06 figure. .venv/bin/python -W ignore scripts/fig_ed06.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
c=2.99792458e8; q=1.602176634e-19; me=9.1093837e-31; e0=8.8541878128e-12
def fres(th,n1,n2):
    ti=np.radians(th); st=n1/n2*np.sin(ti); ct=np.sqrt(1-st**2+0j)
    rp=(n1*np.cos(ti)-n2*ct)/(n1*np.cos(ti)+n2*ct)
    al=ct/np.cos(ti); be=n2/n1; rpar=(al-be)/(al+be)
    return abs(rp)**2,abs(rpar)**2
fig,ax=plt.subplots(2,2,figsize=(13.5,8.6))
th=np.linspace(0,89.9,600)
A=ax[0,0]; Rp,Rl=fres(th,1,1.5)
A.plot(th,Rp,color=BLUE,label="$E\\perp$ plane of incidence"); A.plot(th,Rl,color=ORANGE,label="$E\\parallel$ plane of incidence")
A.axvline(np.degrees(np.arctan(1.5)),color=RED,ls=":"); A.text(57,0.5,"Brewster\n$56.3^\\circ$",color=RED)
A.set_xlabel("angle of incidence (deg)"); A.set_ylabel("reflected fraction $R$"); A.legend(fontsize=8,loc="upper left"); A.set_title("A  Air $\\to$ glass ($n=1.5$)")
B=ax[0,1]; Rp,Rl=fres(th,1.5,1.0)
B.plot(th,Rp,color=BLUE,label="$E\\perp$"); B.plot(th,Rl,color=ORANGE,label="$E\\parallel$")
B.axvline(np.degrees(np.arcsin(1/1.5)),color=RED,ls=":"); B.text(30,0.55,"critical\n$41.8^\\circ$",color=RED)
B.set_xlabel("angle of incidence (deg)"); B.set_ylabel("$R$"); B.legend(fontsize=8,loc="center left"); B.set_title("B  Glass $\\to$ air: total internal reflection")
C=ax[1,0]
w0=1.5e16; gam=1e14; wp2=2.5e25*q**2/(me*e0)
w=np.linspace(0.97*w0,1.03*w0,2000)
n=1+0.5*wp2*(w0**2-w**2)/((w0**2-w**2)**2+gam**2*w**2); al=wp2*w**2*gam/(c*((w0**2-w**2)**2+gam**2*w**2))
C.plot(w/w0,(n-1)*1e4,color=BLUE,label="$(n-1)\\times10^4$"); C.set_xlabel("$\\omega/\\omega_0$"); C.set_ylabel("$(n-1)\\times10^4$",color=BLUE)
C2=C.twinx(); C2.plot(w/w0,al/1e6,color=ORANGE,label="$\\alpha$ (10$^6$ m$^{-1}$)"); C2.set_ylabel("absorption $\\alpha$ ($10^6\\,\\mathrm{m^{-1}}$)",color=ORANGE); C2.grid(False)
C.set_title("C  Lorentz oscillator: anomalous dispersion at resonance")
D=ax[1,1]
wpl=1.0; k=np.linspace(0,3,300); D.plot(k,np.sqrt(wpl**2+k**2),color=BLUE,label="$\\omega^2=\\omega_p^2+c^2k^2$"); D.plot(k,k,color=MUTED,ls="--",label="light line $\\omega=ck$")
D.axhline(wpl,color=RED,ls=":"); D.text(1.8,1.07,"cutoff $\\omega_p$",color=RED)
D.set_xlabel("$ck/\\omega_p$"); D.set_ylabel("$\\omega/\\omega_p$"); D.legend(fontsize=8,loc="lower right"); D.set_title("D  Plasma: no propagation below $\\omega_p$")
fig.tight_layout(); save(fig,"fig_ed06_matter")
