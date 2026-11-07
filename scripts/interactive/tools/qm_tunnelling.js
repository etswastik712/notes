//META {"title":"Tunnelling through a barrier: transmission and the standing-wave pattern","desc":"A plane wave of energy E hits a rectangular barrier of height V₀ and width 2a (units ħ²/2m = 1). The wavefunction |ψ|² is built from the exact matching solution: standing-wave ripples on the left (interference of incident and reflected waves), exponential decay inside the barrier for E < V₀, and a transmitted wave on the right. T(E) is plotted with your E marked, including the resonances (T = 1) above the barrier.","vault":"QM","chapters":["QM08 Quantum Tunnelling","QM10 The Finite Barrier and Tutorial V"],"tryit":"Make the barrier wider: T falls like e^{−4κa}. Raise E above V₀: T oscillates and reaches 1 when 2qa = nπ."}
ui.gridOf(1);const P1=ui.canvas(300,{xmin:-9,xmax:7,ymin:0,ymax:4,xlabel:'x',ylabel:'|ψ|² (incident amplitude 1)'});const P2=ui.canvas(230,{xmin:0,xmax:3,ymin:0,ymax:1,xlabel:'E / V₀',ylabel:'T',title:'transmission probability'});
const sE=ui.slider('energy E / V₀',0.05,2.6,0.01,0.5,draw),sa=ui.slider('half-width a (units 1/√V₀)',0.2,3,0.05,1,draw);
const out=ui.readout();
const cm=(a,b)=>[a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]],cd=(a,b)=>{const d=b[0]*b[0]+b[1]*b[1];return[(a[0]*b[0]+a[1]*b[1])/d,(a[1]*b[0]-a[0]*b[1])/d]},ce=(t)=>[Math.cos(t),Math.sin(t)];
function csqrt(x){return x>=0?[Math.sqrt(x),0]:[0,Math.sqrt(-x)]}
function solve(E,V0,a){ // units hbar^2/2m=1; unknown B,C,D,F ; psi_I=e^{ikx}+B e^{-ikx}; psi_II=C e^{iqx}+D e^{-iqx}; psi_III=F e^{ikx}
 const k=Math.sqrt(E),q=csqrt(E-V0); // q complex possibly
 const iq=[-q[1],q[0]];const mk=[0,-k];// matrix rows for continuity of psi and psi' at x=-a and a: unknown vector [B,C,D,F]
 const e=(z,x)=>{const m=Math.exp(-z[1]*x);return[m*Math.cos(z[0]*x),m*Math.sin(z[0]*x)]};
 const em=(z,x)=>{const m=Math.exp(z[1]*x);return[m*Math.cos(-z[0]*x),m*Math.sin(-z[0]*x)]};
 // e^{i z x} with z complex: use z=[re,im]: exp(i z x)=exp(-im x)*(cos(re x)+ i sin(re x)); e^{-i z x}=exp(+im x)(cos(re x) - i sin(re x))
 const ei=(z,x)=>{const m=Math.exp(-z[1]*x);return[m*Math.cos(z[0]*x),m*Math.sin(z[0]*x)]},emi=(z,x)=>{const m=Math.exp(z[1]*x);return[m*Math.cos(z[0]*x),-m*Math.sin(z[0]*x)]};
 const K=[k,0],ik=[0,k];
 const A=[[emi(K,-a),neg(ei(q,-a)),neg(emi(q,-a)),[0,0]],
  [cm([0,k],emi(K,-a)),neg(cm(iq,ei(q,-a))),cm(iq,emi(q,-a)),[0,0]],
  [[0,0],ei(q,a),emi(q,a),neg(ei(K,a))],
  [[0,0],cm(iq,ei(q,a)),neg(cm(iq,emi(q,a))),neg(cm(ik,ei(K,a)))]];
 // rhs: -e^{ik(-a)} and -ik e^{ik(-a)}  with sign for B: psi_I' = ik e^{ikx} - ik B e^{-ikx}
 const A2=[[emi(K,-a),neg(ei(q,-a)),neg(emi(q,-a)),[0,0]],[neg(cm(ik,emi(K,-a))),neg(cm(iq,ei(q,-a))),cm(iq,emi(q,-a)),[0,0]],A[2],A[3]];
 const rhs=[neg(ei(K,-a)),neg(cm(ik,ei(K,-a))),[0,0],[0,0]];
 const sol=gauss(A2,rhs);return{B:sol[0],C:sol[1],D:sol[2],F:sol[3],k,q}}
function neg(z){return[-z[0],-z[1]]}
function gauss(A,b){const n=4;const M_=A.map((r,i)=>[...r,b[i]]);for(let i=0;i<n;i++){let p=i;for(let r=i+1;r<n;r++)if(Math.hypot(...M_[r][i])>Math.hypot(...M_[p][i]))p=r;[M_[i],M_[p]]=[M_[p],M_[i]];for(let r=i+1;r<n;r++){const f=cd(M_[r][i],M_[i][i]);for(let c=i;c<=n;c++){const t=cm(f,M_[i][c]);M_[r][c]=[M_[r][c][0]-t[0],M_[r][c][1]-t[1]]}}}
 const x=new Array(n);for(let i=n-1;i>=0;i--){let s=M_[i][n];for(let j=i+1;j<n;j++){const t=cm(M_[i][j],x[j]);s=[s[0]-t[0],s[1]-t[1]]}x[i]=cd(s,M_[i][i])}return x}
function Tof(E,a){const V0=1;if(Math.abs(E-V0)<1e-4)E=V0+1e-4;if(E<V0){const kap=Math.sqrt(V0-E);return 1/(1+V0*V0*Math.sinh(2*kap*a)**2/(4*E*(V0-E)))}const q=Math.sqrt(E-V0);return 1/(1+V0*V0*Math.sin(2*q*a)**2/(4*E*(E-V0)))}
function draw(){const E=sE.value,a=sa.value,V0=1;const S=solve(E<=V0&&Math.abs(E-V0)<1e-6?V0+1e-6:E,V0,a);const k=S.k;const xs=M.linspace(-9,7,1000);
 const ps=xs.map(x=>{if(x<-a){const i=[Math.cos(k*x),Math.sin(k*x)],r=cm(S.B,[Math.cos(-k*x),Math.sin(-k*x)]);return(i[0]+r[0])**2+(i[1]+r[1])**2}
  if(x<=a){const ei=(z,x)=>{const m=Math.exp(-z[1]*x);return[m*Math.cos(z[0]*x),m*Math.sin(z[0]*x)]},emi=(z,x)=>{const m=Math.exp(z[1]*x);return[m*Math.cos(z[0]*x),-m*Math.sin(z[0]*x)]};const u=cm(S.C,ei(S.q,x)),v=cm(S.D,emi(S.q,x));return(u[0]+v[0])**2+(u[1]+v[1])**2}
  return S.F[0]**2+S.F[1]**2});
 P1.set({ymax:Math.max(2.2,Math.max(...ps)*1.15)});P1.clear();P1.area([-a,a],[0,0],[P1.o.ymax,P1.o.ymax],'rgba(235,104,52,0.15)');P1.vline(-a,C.orange);P1.vline(a,C.orange);P1.line(xs,ps,C.blue,2.5);P1.text('barrier',0,P1.o.ymax*0.95,C.orange,'center');
 P2.clear();const Es=M.linspace(0.01,3,400);P2.line(Es,Es.map(e=>Tof(e,a)),C.aqua,3);P2.vline(1,C.muted);P2.dot(E,Tof(E,a),C.orange,6);
 const Tn=S.F[0]**2+S.F[1]**2,Rn=S.B[0]**2+S.B[1]**2;
 out.textContent=`E/V₀ = ${M.fmt(E,3)}   2a = ${M.fmt(2*a,3)}   T from matching = |F|² = ${M.fmt(Tn,5)}   R = |B|² = ${M.fmt(Rn,5)}   R+T = ${M.fmt(Tn+Rn,6)}   closed form T = ${M.fmt(Tof(E,a),5)}\n${E<1?`κ = √(V₀−E) = ${M.fmt(Math.sqrt(1-E),4)}, decay length 1/κ = ${M.fmt(1/Math.sqrt(1-E),3)}, thin-barrier estimate 16(E/V₀)(1−E/V₀)e^{−4κa} = ${M.fmt(16*E*(1-E)*Math.exp(-4*Math.sqrt(1-E)*a),4)}`:`above the barrier: q = √(E−V₀) = ${M.fmt(Math.sqrt(E-1),4)}, T = 1 when 2qa = nπ (resonance)`}`}
draw();ui.note('T = [1 + V₀² sinh²(2κa)/(4E(V₀−E))]⁻¹ for E < V₀ (QM10). R + T = 1 to machine precision confirms the matching solution.');
