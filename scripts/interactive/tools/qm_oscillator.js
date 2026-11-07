//META {"title":"The harmonic oscillator: eigenstates and a coherent state","desc":"ħ = m = ω = 1. Left: the eigenstate ψ_n(x) on the parabolic potential, drawn at height E_n with its probability density, with the classical turning points; note the tunnelling into the forbidden region and n nodes. Right: a coherent state |α⟩, a Gaussian that oscillates like a classical particle without changing shape; or an n/n+1 superposition.","vault":"QM","chapters":["QM05 The Harmonic Oscillator","QM06 The Oscillator Toolbox"],"tryit":"Increase n: the density approaches the classical 1/√(E−V) distribution. Switch to coherent state: ⟨x⟩ follows x_c cos t exactly, and the width stays 1/√2 forever."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-6,xmax:6,ymin:-0.5,ymax:12,xlabel:'x',ylabel:'energy / ψ'});const P2=ui.canvas(340,{xmin:-6,xmax:6,ymin:0,ymax:1,xlabel:'x',ylabel:'|ψ|²',title:'time-dependent state'});
const sn=ui.slider('quantum number n',0,12,1,3,draw),sa=ui.slider('coherent amplitude α',0,4,0.05,2,draw),mode=ui.select('right panel',[['c','coherent state'],['s','(|n⟩+|n+1⟩)/√2']],draw,'c');
const out=ui.readout();let t=0;
function H(n,x){let h0=1,h1=2*x;if(n===0)return h0;for(let k=1;k<n;k++){const h2=2*x*h1-2*k*h0;h0=h1;h1=h2}return h1}
function fact(n){let f=1;for(let i=2;i<=n;i++)f*=i;return f}
function psi(n,x){return H(n,x)*Math.exp(-x*x/2)/Math.sqrt(Math.pow(2,n)*fact(n)*Math.sqrt(Math.PI))}
function draw(){const n=sn.value,al=sa.value;P1.set({ymax:Math.max(6,n+3.5),xmin:-Math.max(5,Math.sqrt(2*n+1)+2.5),xmax:Math.max(5,Math.sqrt(2*n+1)+2.5)});P1.clear();const xs=M.linspace(P1.o.xmin,P1.o.xmax,500);P1.line(xs,xs.map(x=>x*x/2),C.ink,2);P1.hline(n+0.5,C.muted,[4,3]);
 const sc=1.2;P1.line(xs,xs.map(x=>n+0.5+sc*psi(n,x)**2*2),C.orange,3);P1.line(xs,xs.map(x=>n+0.5+sc*psi(n,x)),C.blue,1.5);const xt=Math.sqrt(2*n+1);P1.vline(xt);P1.vline(-xt);
 // classical density
 P1.line(xs.filter(x=>Math.abs(x)<xt-0.02),xs.filter(x=>Math.abs(x)<xt-0.02).map(x=>n+0.5+sc*2/(Math.PI*Math.sqrt(2*n+1-x*x))),C.red,1.2,[4,3]);
 P1.legend([['|ψ_n|² (shifted to E_n)',C.orange],['ψ_n',C.blue],['classical density',C.red,[4,3]]],P1.o.ml+8,P1.o.mt+14);
 P2.set({xmin:-8,xmax:8,ymax:1});P2.clear();const xs2=M.linspace(-8,8,500);let dens;
 if(mode.value==='c'){const xc=Math.SQRT2*al*Math.cos(t);dens=xs2.map(x=>Math.exp(-((x-xc)**2))/Math.sqrt(Math.PI));P2.set({ymax:0.7});P2.clear();P2.vline(xc,C.red);out.textContent=`coherent state: ⟨x⟩ = √2 α cos t = ${M.fmt(xc,4)} (classical path), width σ_x = 1/√2 = 0.7071 constant, ⟨E⟩ = α² + ½ = ${M.fmt(al*al+0.5,4)}   |   eigenstate n = ${n}: E = ${M.fmt(n+0.5,3)}, classical turning points ±${M.fmt(xt,4)}, ${n} nodes`}
 else{dens=xs2.map(x=>{const a=psi(n,x),b=psi(n+1,x);return 0.5*(a*a+b*b+2*a*b*Math.cos(t))});P2.set({ymax:Math.max(...dens)*1.3});P2.clear();out.textContent=`superposition of n=${n} and n=${n+1}: |ψ|² = ½(ψ_n² + ψ_{n+1}² + 2ψ_nψ_{n+1} cos t): sloshes with period 2π (Bohr frequency E_{n+1}−E_n = 1)`}
 P2.line(xs2,dens,C.orange,3);P2.line(xs2,xs2.map(x=>0),C.grid,1)}
loop((dt)=>{t+=dt*1.2;draw()});draw();
ui.note('ψ_n = (2ⁿ n! √π)^{-1/2} Hₙ(x) e^{-x²/2}; E_n = n + ½ (ħω). Coherent state |α⟩ = e^{-|α|²/2}Σ αⁿ/√n! |n⟩ has ⟨x⟩ = √2 α cos t, ⟨p⟩ = −√2 α sin t.');
