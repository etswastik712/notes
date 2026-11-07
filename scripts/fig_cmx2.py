"""CMX2 figure. .venv/bin/python -W ignore scripts/fig_cmx2.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
from scipy.integrate import solve_ivp
qe=1.602176634e-19;mp=1.67262192e-27;B0=1.0;E0=1e5;om=qe*B0/mp;Tc=2*np.pi/om
dA={'Landau-x':(lambda r:np.array([-B0*r[1],0.0]),np.array([[0,0],[-B0,0]])),'Landau-y':(lambda r:np.array([0.0,B0*r[0]]),np.array([[0,B0],[0,0]])),'symmetric':(lambda r:np.array([-B0*r[1]/2,B0*r[0]/2]),np.array([[0,B0/2],[-B0/2,0]]))}
def run(name,E=E0,v0=(3e4,1e4),N=6):
    Af,J=dA[name]
    def rhs(t,s):
        r=s[:2];P=s[2:];kin=P-qe*Af(r);return np.concatenate([kin/mp,(qe/mp)*(J@kin)-np.array([0.0,-qe*E])])
    P0=mp*np.array(v0)+qe*Af(np.zeros(2));return solve_ivp(rhs,[0,N*Tc],np.concatenate([[0,0],P0]),rtol=1e-11,atol=1e-14,dense_output=True)
tt=np.linspace(0,6*Tc,3000);fig=plt.figure(figsize=(15.5,4.9));gs=fig.add_gridspec(1,3)
A=fig.add_subplot(gs[0]);cols={'Landau-x':BLUE,'Landau-y':ORANGE,'symmetric':RED};lws={'Landau-x':5,'Landau-y':3,'symmetric':1.4}
for n in dA:
    S=run(n).sol(tt);A.plot(S[0]*1e3,S[1]*1e3,color=cols[n],lw=lws[n],label=n+" gauge",alpha=0.9)
A.set_ylim(-0.25,1.6);A.set_xlabel("$x$ (mm)");A.set_ylabel("$y$ (mm)");A.legend(fontsize=8,loc="upper left");A.set_title("A  One orbit, three gauges ($E\\times B$ drift, proton):\nthe curves lie on top of each other",fontsize=10)
B=fig.add_subplot(gs[1]);u=tt/Tc
for n,ls in (('Landau-x','-'),('Landau-y','--'),('symmetric',':')):
    S=run(n,E=0.0).sol(tt);B.plot(u,S[2]/1e-22,color=cols[n],ls=ls,lw=2,label="$P_x$ in %s"%n)
S=run('Landau-x',E=0.0).sol(tt);vx=np.gradient(S[0],tt);B.plot(u,mp*vx/1e-22,color="black",lw=1.2,label="kinetic $m\\dot x$ (physical)")
B.set_xlabel("time (cyclotron periods)");B.set_ylabel("momentum ($10^{-22}$ kg m/s)");B.legend(fontsize=7.5,loc="center right");B.set_title("B  The canonical momentum is gauge-dependent\n($P_x$ conserved only in Landau-$x$)",fontsize=10)
C=fig.add_subplot(gs[2]);y=np.linspace(-4e-3,6e-3,400);Px=0.0;V=((Px+qe*B0*y)**2/(2*mp)-qe*E0*y)/qe;C.plot(y*1e3,V,color=BLUE,lw=2,label="$V(y)=\\frac{(P_x+qBy)^2}{2m}-qEy$ (volts)")
y0=(mp*E0/B0-Px)/(qe*B0);C.axvline(y0*1e3,color=MUTED,ls="--",lw=1);C.axhline(0,color=ORANGE,lw=1.5)
C.plot([0,2*y0*1e3],[0,0],"o",color=ORANGE,ms=8);C.annotate("particle released at rest:\nturning points $y=0$ and $2y_0$",xy=(2*y0*1e3,0),xytext=(2.6,260),fontsize=8.5,color=ORANGE,arrowprops=dict(arrowstyle="->",color=ORANGE))
C.text(y0*1e3+0.15,150,"minimum at $y_0=\\frac{mE}{qB^2}$\n$\\dot x=E/B$ there",fontsize=9,color=MUTED);C.set_xlim(-2,5);C.set_ylim(-100,450)
C.set_xlabel("$y$ (mm)");C.set_ylabel("$V$ (V)");C.legend(fontsize=8,loc="upper center");C.set_title("C  Conserved $P_x$ reduces the 2D motion to a 1D oscillator\naround $y_0$, with $\\dot x=E/B$ (cycloid, $P_x=0$)",fontsize=10)
fig.tight_layout();save(fig,"fig_cmx2_gauge")
