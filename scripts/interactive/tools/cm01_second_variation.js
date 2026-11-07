//META {"title":"Is the action a minimum? The second variation","desc":"Oscillator with ω = 2 between fixed endpoints x(0)=0, x(T)=1. The true path makes the action stationary; adding a wiggle ε·sin(nπt/T) changes S by (mT/4)ε²[(nπ/T)² − ω²]. Slide the duration T past π/ω and watch the parabola flip from a minimum to a saddle.","vault":"CM","chapters":["CM01 Variational Calculus and Hamilton's Principle"],"tryit":"Move T through π/ω = 1.571: for n = 1 the curvature of S(ε) changes sign exactly there. Raise n and see that higher modes stay stabilising until ωT > nπ."}
const w=2,m=1;
const P1=ui.canvas(300,{xmin:0,xmax:2.4,ymin:-3,ymax:3,xlabel:'t',ylabel:'x(t)',title:'paths'});
const P2=ui.canvas(300,{xmin:-1,xmax:1,ymin:-1,ymax:1,xlabel:'ε',ylabel:'S[ε] − S[0]',title:'action vs amplitude of the wiggle'});
const sT=ui.slider('duration T',0.5,2.35,0.01,1.2,draw),sn=ui.slider('mode n',1,3,1,1,draw),se=ui.slider('wiggle ε',-1,1,0.01,0.4,draw);
const out=ui.readout();
function action(T,n,eps){const N=4000;let s=0,dt=T/N;for(let i=0;i<N;i++){const t=(i+.5)*dt,s0=Math.sin(w*T);const x0=Math.sin(w*t)/s0,v0=w*Math.cos(w*t)/s0;const x=x0+eps*Math.sin(n*Math.PI*t/T),v=v0+eps*(n*Math.PI/T)*Math.cos(n*Math.PI*t/T);s+=(0.5*m*v*v-0.5*m*w*w*x*x)*dt}return s}
function draw(){const T=sT.value,n=sn.value,e=se.value,s0=Math.sin(w*T);
 P1.set({xmax:T*1.05});P1.clear();
 if(Math.abs(s0)<0.03){P1.ptext('ωT ≈ π: conjugate point, true path not unique',P1.w/2,P1.h/2,C.red,'center','14px system-ui');}
 else{const ts=M.linspace(0,T,300);const x0=ts.map(t=>Math.sin(w*t)/s0);P1.set({ymin:Math.min(-1.2,...x0)-.2,ymax:Math.max(1.4,...x0)+.2});P1.clear();P1.line(ts,x0,C.ink,3);P1.line(ts,ts.map((t,i)=>x0[i]+e*Math.sin(n*Math.PI*t/T)),C.orange,2,[6,4]);P1.dot(0,0,C.red,5);P1.dot(T,1,C.red,5);P1.legend([['true path (stationary)',C.ink],['varied path',C.orange,[6,4]]],P1.o.ml+8,P1.o.mt+14)}
 const k=(m*T/4)*((n*Math.PI/T)**2-w*w);const es=M.linspace(-1,1,101);
 P2.set({ymin:-Math.max(1.5,Math.abs(k)*1.05),ymax:Math.max(1.5,Math.abs(k)*1.05)});P2.clear();P2.hline(0);P2.vline(0);
 P2.line(es,es.map(x=>k*x*x),C.blue,3);P2.dot(e,k*e*e,C.orange,6);
 if(Math.abs(s0)>=0.03){const num=(action(T,n,e)-action(T,n,0));out.textContent=`ωT = ${M.fmt(w*T,3)}  (π = 3.142)   mode n = ${n}\nS[ε]−S[0] = (mT/4)ε²[(nπ/T)²−ω²] = ${M.fmt(k*e*e,4)}    numerical quadrature: ${M.fmt(num,4)}\ncurvature coefficient = ${M.fmt(k,4)}  →  ${k>0?'MINIMUM along this mode':k<0?'SADDLE (action decreases along this mode)':'marginal (conjugate point)'}`}
 else out.textContent=`ωT = ${M.fmt(w*T,3)} ≈ π : the endpoint is conjugate to the start`}
draw();ui.note('Check: ω = 2, T = 1.0 → coefficient 1.4674; T = 1.4 → 0.3624; T = 2 (not reachable here) → −0.7663 (CM01 Worked example 6).');
