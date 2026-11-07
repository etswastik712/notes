"""ED01 figure. .venv/bin/python -W ignore scripts/fig_ed01.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from figlib import *  # noqa
import numpy as np
fig=plt.figure(figsize=(15.5,4.9));gs=fig.add_gridspec(1,3)
A=fig.add_subplot(gs[0]);x,z=np.meshgrid(np.linspace(-3,3,400),np.linspace(0.0,3.2,260))
def Efield(x,z,q,x0,z0):
    rx,rz=x-x0,z-z0;r3=(rx**2+rz**2)**1.5+1e-12;return q*rx/r3,q*rz/r3
Ex1,Ez1=Efield(x,z,1,0,1.0);Ex2,Ez2=Efield(x,z,-1,0,-1.0);Ex,Ez=Ex1+Ex2,Ez1+Ez2
A.streamplot(x,z,Ex,Ez,color=BLUE,density=1.6,linewidth=0.9,arrowsize=0.9,start_points=np.array([[0.35*np.cos(t),1.0+0.35*np.sin(t)] for t in np.linspace(0,2*np.pi,24,endpoint=False)]),integration_direction="both")
A.axhline(0,color="black",lw=2);A.plot([0],[1],"o",color=RED,ms=8);A.text(0.15,1.12,"$q$",color=RED);A.set_xlim(-3,3);A.set_ylim(-0.6,3.2)
rho=np.linspace(-3,3,400);sg=-1/(2*np.pi)*1.0/(rho**2+1)**1.5;A.fill_between(rho,0,sg*3.0,color=ORANGE,alpha=0.5);A.text(1.1,-0.5,"induced $\\sigma(\\rho)\\propto-(\\rho^2+d^2)^{-3/2}$",color=ORANGE,fontsize=8.5)
A.set_xlabel("$x/d$");A.set_ylabel("$z/d$");A.set_title("A  Charge above a grounded plane: field lines in $z>0$\n(same as $q$ and image $-q$; total induced charge $=-q$)",fontsize=10)
B=fig.add_subplot(gs[1]);rd=np.array([3,10,30,100]);err=np.array([2.476e-2,2.191e-3,2.431e-4,2.188e-5]);B.loglog(rd,err,"o",color=ORANGE,ms=8,label="physical dipole vs pure dipole\n($\\theta=60^\\circ$, exact sum)")
xs=np.logspace(0.3,2.2,100);B.loglog(xs,0.25/xs**2,color=MUTED,ls="--",label="$\\frac{1}{4}(d/r)^2$ (next term)")
N=np.array([0,1,2,4,8]);eN=np.array([2.60e-1,2.97e-2,4.53e-3,1.26e-3,7.71e-6]);B2=B.twiny();B2.semilogy(N,eN,"s-",color=BLUE,label="generating function, $s=0.3$");B2.semilogy(np.arange(0,9),0.3**(np.arange(0,9)+1),":",color=BLUE,label="$s^{N+1}$");B2.set_xlabel("order $N$ of the Legendre sum",color=BLUE);B2.tick_params(axis="x",colors=BLUE);B2.spines["top"].set_visible(True)
B.set_xlabel("$r/d$");B.set_ylabel("relative error");B.legend(fontsize=7.5,loc="lower left");B2.legend(fontsize=7.5,loc="upper right")
B.set_title("B  Convergence of the multipole expansion",fontsize=10,pad=32)
C=fig.add_subplot(gs[2]);Nn=41;rng=np.random.default_rng(2)
def run(init,iters=3000):
    V=init.copy();V[0,:]=0;V[:,0]=0;V[:,-1]=0;V[-1,:]=1.0;V[-1,0]=V[-1,-1]=0.5;h=[]
    for it in range(iters):
        W=V.copy();W[1:-1,1:-1]=0.25*(V[2:,1:-1]+V[:-2,1:-1]+V[1:-1,2:]+V[1:-1,:-2]);V=W;h.append(V[Nn//2,Nn//2])
    return np.array(h)
for init,lab,col in ((np.zeros((Nn,Nn)),"start from 0",BLUE),(rng.uniform(-5,5,(Nn,Nn)),"random start",ORANGE),(np.full((Nn,Nn),3.0),"start from 3",RED)):
    C.plot(np.arange(1,3001),run(init),color=col,lw=1.8,label=lab)
C.axhline(0.25,color="black",ls="--",lw=1);C.text(1500,0.37,"$V_0/4$",fontsize=9);C.set_xscale("log");C.set_ylim(-0.3,3.3);C.set_xlabel("relaxation sweeps");C.set_ylabel("$V$ at the centre of the square")
C.legend(fontsize=8);C.set_title("C  Uniqueness (Dirichlet on all sides):\ndifferent starting guesses, same solution",fontsize=10)
fig.tight_layout();save(fig,"fig_ed01_methods")
