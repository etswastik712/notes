"""Numbers for the MT2113 question-paper archive notes (probability)."""
import math, random
from math import comb, exp, factorial
import numpy as np
from scipy import stats, integrate
rng=np.random.default_rng(1)
print("== 2022 midsem")
print("A1 P(X=3), Poisson(2):", round(exp(-2)*8/6,4))
print("A3 COFFEE:", factorial(6)//(2*2))
print("B2 P(G|A):", 0.3*0.6/(0.3*0.6+0.25*0.4))
# C1 check
a,b=0.3,0.55
for n in (2,3,6):
    s=sum(a*(1-a)**(k-1)*b*(1-b)**(n-k-1) for k in range(1,n))
    f=a*b/(b-a)*((1-a)**(n-1)-(1-b)**(n-1))
    print(f"C1 n={n}: direct {s:.6f} formula(beta-alpha) {f:.6f}")
print("== 2022 endsem")
print("1a:", (36-16)/100)
print("1d P(|Z|<=2):", round(stats.norm.cdf(2)-stats.norm.cdf(-2),4))
x=rng.random(10**6); y=rng.random(10**6)
print("2 P(X>1/2,2X+Y<1):", np.mean((x>.5)&(2*x+y<1)), " product:", np.mean(x>.5)*np.mean(2*x+y<1))
print("4b bound:", 1-160/100**2)
# simulate average of 1000 exp(400)
m=rng.exponential(400,(20000,1000)).mean(1); print("4b sim P(300<avg<500):", np.mean((m>300)&(m<500)))
# 6: given M near m, fraction with X==M and distribution of X
M=np.maximum(x,y); sel=np.abs(M-0.6)<0.002
print("6 P(X=M | M~0.6):", np.mean(x[sel]==M[sel]), " mean X|X<M:", x[sel][x[sel]<M[sel]].mean(), "(theory 0.3)")

print("== 2023 midsem")
n,r=10,3; print("Q1 line n=10,r=3:", 2*(n-r-1)/(n*(n-1)), " circle:", 1/(n-1))
# simulate line
cnt=0;T=200000
for _ in range(T):
    p=rng.permutation(n); a,b=np.where(p==0)[0][0],np.where(p==1)[0][0]
    cnt+= abs(a-b)-1==r
print("  sim line:", cnt/T)
al,p=0.3,0.6
for k in (1,2,3):
    s=sum(al*p**m*comb(m,k)*0.5**m for m in range(k,400)); f=al*2*p**k/(2-p)**(k+1)
    print(f"Q2 k={k}: sum {s:.6f} closed {f:.6f}")
print("Q3b:", ((2/3)**3+(1/3)**3)/((2/3)**2+(1/3)**2))
nn,pp=7,0.35; print("Q5 E[1/(X+1)]:", sum(comb(nn,k)*pp**k*(1-pp)**(nn-k)/(k+1) for k in range(nn+1)), (1-(1-pp)**(nn+1))/((nn+1)*pp))
print("== 2023 endsem")
print("1a c=", 2/math.pi, " 1b:", round(2*stats.norm.cdf(2)-1,4))
print("1c norm:", integrate.quad(lambda y:y*y/24,-2,4)[0])
th=2.5758; print("4b n >", (th/0.01)**2)
print("5f counterexample f_XY=2 > f_X=1")
print("== 2024 midsem")
print("Q1:", 312+470+525-42-147-86+25)
print("Q2:", math.factorial(8)/comb(64,8))
print("Q3:", 0.95*0.2/(0.95*0.2+0.85*0.5+0.7*0.3))
def maj(n,q): return sum(comb(n,k)*q**k*(1-q)**(n-k) for k in range(n//2+1,n+1))
print("Q4: 3 ex", maj(3,.8)/3+2*maj(3,.4)/3, " 5 ex", maj(5,.8)/3+2*maj(5,.4)/3)
print("Q5:", 1-exp(-3.5)*(1+3.5))
print("== 2024 endsem")
print("2a E|D1-D2|:", integrate.dblquad(lambda y,x: abs(x-y)*4*x*y,0,1,0,1)[0], 4/15)
X=stats.binom(200,0.15); print("5 CLT:", 1-stats.norm.cdf(5/math.sqrt(25.5)), " cc:", 1-stats.norm.cdf(4.5/math.sqrt(25.5)), " exact:", X.sf(34))
print("Quiz1:", comb(17,8), comb(7,3)*comb(10,5), comb(17,8)-comb(7,3)*comb(10,5))
print("Quiz2 (2):", 0.05/(0.05+0.0025), 0.1/(0.1+0.0025))
print("Quiz3 E[X]:", (40**2+33**2+25**2+50**2)/148, "E[Y]:", 148/4)
print("Quiz4 1a:", math.exp(-1)-math.exp(-1.5))
print("== 2025")
print("mid Q1:", 1-2/8, 1-(1/4)**3-(3/4)**3)
print("mid Q2:", (28+26+16-12-4-6+2), 1-comb(50,2)/comb(100,2))
B=stats.binom(50,0.01); print("mid Q5 poisson:", exp(-.5)*.125, 1-exp(-.5)*1.5, " exact:", B.pmf(2), B.sf(1))
def eg(p):
    q=1-p; return sum(m*comb(m-1,3)*(p**4*q**(m-4)+q**4*p**(m-4)) for m in range(4,8))
print("mid Q6 E[games] p=.5,.6,.7:", eg(.5), eg(.6), eg(.7))
c=1/(1-2*math.exp(-1)); py=c*(1-1.5*math.exp(-.5)); px=c*(1-math.exp(-.5)-.5*math.exp(-1))
print("end Q4 c=",c," P(Y<1/2|X<1/2)=",py/px)
print("end Q5b n>=", (1.96*4/2)**2)
print("== MCQ")
# E[N] two consecutive 1s
tot=0;T=40000
for _ in range(T):
    n=0;prev=False
    while True:
        n+=1; one=rng.random()<1/6
        if one and prev: break
        prev=one
    tot+=n
print("II.11 sim E[N]:", tot/T, " theory 42")
print("II.5 E[exp(Z^2/4)]:", integrate.quad(lambda z: math.exp(-z*z/4)/math.sqrt(2*math.pi),-50,50)[0], math.sqrt(2))
P=np.array([[.9,.1,0],[0,.2,.8],[.1,.1,.8]]); w,v=np.linalg.eig(P.T); s=np.real(v[:,np.argmin(abs(w-1))]); print("III.3 pi:", s/s.sum())
