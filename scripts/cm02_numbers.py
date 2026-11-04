"""CM02 numbers. .venv/bin/python -W ignore scripts/cm02_numbers.py"""
import numpy as np
from scipy.integrate import solve_ivp, quad
g=9.81
print("== Atwood m1=3, m2=1: a=g(m1-m2)/(m1+m2), T=2 m1 m2 g/(m1+m2)")
m1,m2=3.,1.; print("a=%.4f  T=%.4f N"%(g*(m1-m2)/(m1+m2),2*m1*m2*g/(m1+m2)))
print("== bead on rotating hoop R=0.5, Omega=6: cos th0=g/(Omega^2 R); small osc w=Omega sin th0")
R=0.5;W=6.0; c0=g/(W**2*R); th0=np.arccos(c0); print("critical Omega=%.4f rad/s  th0=%.4f deg  w=%.4f rad/s"%(np.sqrt(g/R),np.degrees(th0),W*np.sin(th0)))
f=lambda t,y:[y[1],np.sin(y[0])*(W**2*np.cos(y[0])-g/R)]
s=solve_ivp(f,[0,20],[th0+0.01,0],rtol=1e-10,atol=1e-12,dense_output=True,max_step=0.005)
t=np.linspace(0,20,40001); th=s.sol(t)[0]-th0
# period from zero crossings
zc=t[1:][(th[:-1]>0)&(th[1:]<=0)]; print("measured period=%.5f  2pi/w=%.5f"%(np.mean(np.diff(zc)),2*np.pi/(W*np.sin(th0))))
print("== hemisphere: lambda=Mg(3cos th-2), leaves at cos th=2/3")
print("theta_c=%.4f deg   v^2/(g a)=%.4f (=2/3)"%(np.degrees(np.arccos(2/3)),2*(1-2/3)))
print("== damped oscillator m=1,k=4,b=0.4: w_d=%.5f, decay rate b/2m=0.2; check dE/dt=-b v^2 = -2F"%np.sqrt(4-0.01))
fo=lambda t,y:[y[1],-4*y[0]-0.4*y[1]]
s=solve_ivp(fo,[0,10],[1,0],rtol=1e-11,atol=1e-13,dense_output=True)
tt=np.linspace(0,10,20001); x,v=s.sol(tt); E=0.5*v**2+2*x**2
print("E(10)/E(0)=%.6f ; integral of b v^2 dt=%.6f  vs 1-E(10)/E(0)*E0 => E0-E(10)=%.6f"%(E[-1]/E[0],np.trapezoid(0.4*v**2,tt),E[0]-E[-1]))
print("== cyclotron from L=1/2 m v^2 + q A.v, A=B x r/2: period 2 pi m/(qB)")
q,m,B=1.,1.,2.
fc=lambda t,y:[y[2],y[3],q*B/m*y[3],-q*B/m*y[2]]
s=solve_ivp(fc,[0,5],[0,0,1,0],rtol=1e-11,atol=1e-13,dense_output=True)
x,y=s.sol(np.linspace(0,np.pi,5))[:2]; print("period 2pi m/qB=%.5f; radius v/w=%.4f ; return to start at pi/..." %(2*np.pi*m/(q*B),1/(q*B/m)))
print("== rolling disk: omega1=dx-a sin th dphi, omega2=dy+a cos th dphi; d omega1 = -a cos th dth^dphi (not in span) => nonintegrable")
