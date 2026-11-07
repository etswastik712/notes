"""ED11 figure. .venv/bin/python -W ignore scripts/fig_ed11.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig=plt.figure(figsize=(15.5,4.9));gs=fig.add_gridspec(1,3)
A=fig.add_subplot(gs[0]);psi=np.linspace(0,2*np.pi,801)
for b,col in ((0.0,MUTED),(0.5,BLUE),(0.9,ORANGE),(0.99,RED)):
    r=(1-b*b)/(1-b*b*np.sin(psi)**2)**1.5;A.plot(r*np.cos(psi),r*np.sin(psi),color=col,lw=2,label="$\\beta=%g$"%b)
A.set_aspect("equal");A.set_xlim(-1.5,3.6);A.set_ylim(-3.6,3.6);A.axhline(0,color=GRID,lw=0.8);A.axvline(0,color=GRID,lw=0.8)
A.annotate("",xy=(3.3,0),xytext=(2.2,0),arrowprops=dict(arrowstyle="->",color=BLUE));A.text(2.2,0.25,"$v$",color=BLUE)
A.set_title("A  $|E|(\\psi)/E_{\\rm Coulomb}$ of a moving charge\n(radius = field strength, $\\psi$ from the velocity)",fontsize=10);A.legend(fontsize=8,loc="lower right")
B=fig.add_subplot(gs[1]);t=np.linspace(-3,3,4001);b=0.9;g=1/np.sqrt(1-b*b);den=(1+g*g*b*b*t**2)**1.5
B.plot(t,g/den,color=BLUE,lw=2,label="$E_2$ (transverse)");B.plot(t,-g*b*t/den,color=ORANGE,lw=2,label="$E_1$ (longitudinal)");B.plot(t,b*g/den,color=RED,lw=2,ls="--",label="$B_3=\\beta E_2$")
B.plot(t,1/(1+b*b*t**2)**1.5,color=MUTED,ls=":",label="$E_2$ at $\\beta\\to0$")
B.set_xlabel("$ct/b$");B.set_ylabel("field in units $q/b^2$ (Gaussian)");B.legend(fontsize=8);B.set_title("B  Fields at a fixed observer, $\\beta=0.9$ ($\\gamma=2.29$)\npeak $\\times\\gamma$, duration $\\div\\gamma$, $\\int E_2dt$ unchanged",fontsize=10)
C=fig.add_subplot(gs[2]);u=np.linspace(0,0.95,200)
for v,col in ((0.1,BLUE),(0.5,ORANGE),(0.9,RED)):
    C.plot(u,-2*u*v/np.sqrt(1-u*u),color=col,lw=2,label="$v/c=%g$"%v)
C.set_xlabel("$u/c$ (speed of the test charge)");C.set_ylabel("$\\lambda_{\\rm tot}/\\lambda$ seen from the test charge");C.legend(fontsize=8,title="current-carrying wire",title_fontsize=8)
C.set_title("C  A neutral wire is charged in the frame of the test charge:\n$\\lambda_{\\rm tot}=-2\\lambda uv/[c^2\\sqrt{1-u^2/c^2}]$",fontsize=10)
fig.tight_layout();save(fig,"fig_ed11_fields")
