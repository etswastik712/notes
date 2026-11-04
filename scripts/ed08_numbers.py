"""ED08 numbers. .venv/bin/python -W ignore scripts/ed08_numbers.py"""
import numpy as np
from scipy.integrate import solve_ivp
print("== Griffiths Ex 10.1: V=0, A=(mu0 k/4c)(ct-|x|)^2 zhat for |x|<ct ; units c=1, mu0 k=1 (mu0=eps0=1)")
c=1.0
def A(r,t):
    x=r[0]; return np.array([0,0,0.25*(t-abs(x))**2]) if abs(x)<t else np.zeros(3)
V=lambda r,t:0.0
def fields(r,t,h=1e-5):
    # E=-gradV - dA/dt ; B = curl A (finite differences)
    dAdt=(A(r,t+h)-A(r,t-h))/(2*h); E=-dAdt
    J=np.zeros((3,3))
    for j in range(3):
        d=np.zeros(3); d[j]=h; J[:,j]=(A(r+d,t)-A(r-d,t))/(2*h)
    B=np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]]); return E,B
r0=np.array([0.3,0.2,0.1]); t0=1.0; E,B=fields(r0,t0)
print("E=",E.round(6)," expected -1/2 (t-|x|) zhat = %.6f"%(-0.5*(t0-0.3)),"; B=",B.round(6)," expected +1/2 (t-x) yhat = %.6f"%(0.5*(t0-0.3)))
Ef=lambda r,t:fields(r,t)[0]; Bf=lambda r,t:fields(r,t)[1]
def curlf(F,r,t,h=1e-4):
    J=np.zeros((3,3))
    for j in range(3):
        d=np.zeros(3); d[j]=h; J[:,j]=(F(r+d,t)-F(r-d,t))/(2*h)
    return np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]])
dB=(Bf(r0,t0+1e-4)-Bf(r0,t0-1e-4))/2e-4; dE=(Ef(r0,t0+1e-4)-Ef(r0,t0-1e-4))/2e-4
print("Faraday residual |curl E + dB/dt|=%.2e ; Ampere residual |curl B - dE/dt|=%.2e (rho=J=0, both gauges: div A = 0 = dV/dt)"%(np.linalg.norm(curlf(Ef,r0,t0)+dB),np.linalg.norm(curlf(Bf,r0,t0)-dE)))
print("jump of B_y across x=0 at t=1 (analytic, B_y = 1/2 sign(x)(t-|x|)): %.6f ; equals mu0 K = mu0 k t = %.6f"%(0.5*1.0-(-0.5*1.0),1.0))
print("== gauge invariance of E,B under arbitrary lambda(r,t) (Griffiths 10.7): A'=A+grad lambda, V'=V-d lambda/dt")
lam=lambda r,t:np.sin(r[0]+2*r[1]-3*r[2]+0.7*t)*np.exp(-0.1*(r@r))*(1+t)
def gradlam(r,t,h=1e-5):
    g=np.zeros(3)
    for j in range(3):
        d=np.zeros(3); d[j]=h; g[j]=(lam(r+d,t)-lam(r-d,t))/(2*h)
    return g
Ap=lambda r,t:A(r,t)+gradlam(r,t); Vp=lambda r,t:V(r,t)-(lam(r,t+1e-5)-lam(r,t-1e-5))/2e-5
def fieldsp(r,t,h=1e-4):
    gV=np.zeros(3)
    for j in range(3):
        d=np.zeros(3); d[j]=h; gV[j]=(Vp(r+d,t)-Vp(r-d,t))/(2*h)
    E=-gV-(Ap(r,t+h)-Ap(r,t-h))/(2*h)
    J=np.zeros((3,3))
    for j in range(3):
        d=np.zeros(3); d[j]=h; J[:,j]=(Ap(r+d,t)-Ap(r-d,t))/(2*h)
    B=np.array([J[2,1]-J[1,2],J[0,2]-J[2,0],J[1,0]-J[0,1]]); return E,B
E2,B2=fieldsp(r0,t0); print("E diff=%.2e  B diff=%.2e  while |A'-A|=%.3f (potentials differ, fields do not)"%(np.linalg.norm(E2-E),np.linalg.norm(B2-B),np.linalg.norm(Ap(r0,t0)-A(r0,t0))))
print("== restricted gauge: lambda=sin(kx - w t), w=ck preserves Lorenz: laplace(lam) - d2 lam/dt2 = -(k^2 - w^2) sin = 0")
k=2.0;w=2.0; print("k^2-w^2 =",k**2-w**2)
print("== Landau vs symmetric gauge, uniform B=2 zhat, q=m=1: Hamilton's equations H=(p-A)^2/2 in each gauge, same initial x and v")
Bz=2.0
def H_run(gauge):
    if gauge==1:
        Af=lambda x,y:np.array([0,Bz*x]); dA=lambda x,y:np.array([[0,Bz],[0,0]])   # dA[i][j]=d_i A_j
    else:
        Af=lambda x,y:np.array([-Bz*y/2,Bz*x/2]); dA=lambda x,y:np.array([[0,Bz/2],[-Bz/2,0]])
    def f(t,u):
        x,y,px,py=u; A_=Af(x,y); v=np.array([px,py])-A_; dp=dA(x,y)@v
        return [v[0],v[1],dp[0],dp[1]]
    x0,y0,vx0,vy0=1.0,0.0,0.5,0.3; A0=Af(x0,y0); u0=[x0,y0,vx0+A0[0],vy0+A0[1]]
    return solve_ivp(f,[0,5],u0,rtol=1e-12,atol=1e-13,dense_output=True),u0
s1,u1=H_run(1); s2,u2=H_run(2)
print("final positions gauge1:",s1.y[:2,-1].round(8)," gauge2:",s2.y[:2,-1].round(8))
print("initial canonical momenta differ: p1=",np.round(u1[2:],3)," p2=",np.round(u2[2:],3))
x,y_=0.7,0.4
A1=np.array([0,Bz*x,0]); A2=np.array([-Bz*y_/2,Bz*x/2,0]); gl=np.array([Bz*y_/2,Bz*x/2,0]); print("A1-A2=",(A1-A2)," grad(Bxy/2)=",gl)
