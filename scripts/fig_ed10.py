"""ED10 figure. .venv/bin/python -W ignore scripts/fig_ed10.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig=plt.figure(figsize=(15.5,4.8));gs=fig.add_gridspec(1,3)
A=fig.add_subplot(gs[0],projection="polar");th=np.linspace(0,2*np.pi,721)
A.plot(th,np.sin(th)**2,color=BLUE,lw=2.2);A.fill(th,np.sin(th)**2,color=BLUE,alpha=0.15);A.set_theta_zero_location("N");A.set_theta_direction(-1);A.set_rticks([0.5,1]);A.set_title("A  Dipole radiation pattern $\\langle S\\rangle\\propto\\sin^2\\theta$\n(axis of the dipole vertical)".replace("\\\n","\n"),fontsize=10,pad=14)
B=fig.add_subplot(gs[1]);kr=np.logspace(-0.5,3.0,200)
B.loglog([2*np.pi*3,2*np.pi*10,2*np.pi*30,2*np.pi*100],[5.303e-2,1.591e-2,5.303e-3,1.591e-3],"o",color=ORANGE,ms=7,label="exact finite dipole vs (11.18)");B.loglog(kr,1/kr,color=MUTED,ls="--",label="$1/kr$")
B.set_xlabel("$kr=2\\pi r/\\lambda$");B.set_ylabel("relative error of the far-field formula");B.legend(fontsize=8);B.set_title("B  How far is the radiation zone?\nerror of Griffiths (11.18) falls as $1/kr$".replace("\\\n","\n"),fontsize=10)
C=fig.add_subplot(gs[2]);x=np.logspace(-1,1.6,300);th0=np.radians(45)
Er=2*np.cos(th0)*np.sqrt(1/x**6+1/x**4);Et=np.sin(th0)*np.sqrt((1/x**3-1/x)**2+1/x**4)
C.loglog(x,Er,color=BLUE,label="$|E_r|$ (longitudinal, near-field only)");C.loglog(x,Et,color=ORANGE,label="$|E_\\theta|$");C.loglog(x,np.sin(th0)/x,color=RED,ls=":",label="radiation part $\\propto1/kr$");C.loglog(x,2*np.cos(th0)/x**3,color=MUTED,ls=":",label="static part $\\propto1/(kr)^3$")
C.axvline(1,color=GRID);C.set_ylim(1e-3,1e3);C.set_xlabel("$kr$");C.set_ylabel("field in units $pk^3/4\\pi\\epsilon_0$");C.legend(fontsize=7.5,loc="upper right");C.set_title("C  Near zone to far zone (Jackson 9.18), $\\theta=45^\\circ$",fontsize=10)
fig.tight_layout();save(fig,"fig_ed10_dipole")
