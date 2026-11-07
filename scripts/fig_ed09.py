"""ED09 figure. .venv/bin/python -W ignore scripts/fig_ed09.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig=plt.figure(figsize=(15.5,4.8));gs=fig.add_gridspec(1,3)
A=fig.add_subplot(gs[0]);t=np.linspace(1.002,12,600)
A.plot(t,t/np.sqrt(t*t-1),color=BLUE,label="$B(t)/B_{\\rm static}=ct/\\sqrt{(ct)^2-s^2}$");A.plot(t,1/np.sqrt(t*t-1),color=ORANGE,label="$|E|/(\\mu_0I_0c/2\\pi s)=s/\\sqrt{(ct)^2-s^2}$")
A.axhline(1,color=MUTED,ls=":");A.axvline(1,color=RED,ls="--",lw=1);A.text(1.08,5.4,"news arrives\n$t=s/c$",color=RED,fontsize=8);A.set_ylim(0,6);A.set_xlim(0,12)
A.set_xlabel("$ct/s$");A.legend(fontsize=8,loc="upper right");A.set_title("A  Current switched on in a long wire at $t=0$\n(Griffiths Example 10.2), fields at distance $s$",fontsize=10)
B=fig.add_subplot(gs[1],projection="polar");th=np.linspace(0,2*np.pi,721)
for b,col in ((0.0,MUTED),(0.5,BLUE),(0.9,ORANGE),(0.99,RED)):
    r=(1-b*b)/(1-b*b*np.sin(th)**2)**1.5;B.plot(th,np.minimum(r,6),color=col,label="$v/c=%.2f$"%b)
B.set_rlim(0,6);B.set_title("B  $E\\,R^2$ of a uniformly moving charge\n(in units of $q/4\\pi\\epsilon_0$), $\\theta$ from $\\vec v$",fontsize=10,pad=16);B.legend(fontsize=7.5,loc="lower left",bbox_to_anchor=(0.9,0.0))
C=fig.add_subplot(gs[2]);r=np.logspace(0,3,100);C.loglog(r,0.67353/r**2,color=BLUE,label="velocity field $\\propto r^{-2}$");C.loglog(r,0.08645/r,color=ORANGE,label="acceleration (radiation) field $\\propto r^{-1}$")
C.axvline(7.79,color=RED,ls="--",lw=1);C.text(8.5,3e-3,"$r^*\\approx7.8$",color=RED,fontsize=9);C.set_xlabel("retarded distance $r$ (orbit radius $=1$)");C.set_ylabel("$|\\vec E|$ in units $q/4\\pi\\epsilon_0$")
C.legend(fontsize=8,loc="lower left");C.set_title("C  Circular motion, $v=0.4c$: which field wins\n(fixed retarded time and direction)",fontsize=10)
fig.tight_layout();save(fig,"fig_ed09_retarded")
