//META {"title":"The layer greenhouse model","desc":"Absorbed sunlight S(1 − α)/4 is balanced by outgoing longwave radiation. Put N atmospheric layers above the surface, each absorbing a fraction ε of the infrared passing through and re-emitting up and down. For black layers (ε = 1) the surface is (N+1)^{1/4} times the emission temperature (255 K): more layers or more absorption, a warmer surface and a colder top of the atmosphere.","vault":"CL","chapters":["CL08 Greenhouse Models","CL09 Radiative-Convective Equilibrium"],"tryit":"N = 1, ε = 1: surface 303 K (= 255·2^{1/4}). N = 0 gives 255 K, no greenhouse effect. Reduce ε to see the real, partly transparent atmosphere (the actual 288 K needs ε_eff ≈ 0.78 for one layer)."}
ui.gridOf(2);const P1=ui.canvas(360,{xmin:0,xmax:1,ymin:0,ymax:1,axes:false});const P2=ui.canvas(360,{xmin:200,xmax:400,ymin:-0.5,ymax:6.5,xlabel:'temperature (K)',ylabel:'layer (0 = surface)',title:'radiative-equilibrium temperature profile'});
const sN=ui.slider('number of layers N',0,6,1,1,draw),sE=ui.slider('layer IR absorptivity ε',0.05,1,0.01,1,draw),sa=ui.slider('planetary albedo α',0,0.7,0.01,0.3,draw);
const out=ui.readout();const sig=5.670374e-8,S0=1361;
function solve(N,e,al){const abs=S0*(1-al)/4;let Ts=300,T=new Array(N).fill(250);for(let it=0;it<4000;it++){// fixed-point on temperatures: each layer in equilibrium: absorbs fraction e of up- and down-welling IR, emits e σT⁴ from each side
  // compute up and down fluxes by sweeping
  const up=new Array(N+1),dn=new Array(N+2);dn[N]=0;
  // downward flux entering layer i from above: D_i ; layers indexed 0..N-1 from the bottom
  const D=new Array(N+1).fill(0);for(let i=N-1;i>=0;i--)D[i]=D[i+1]*(1-e)+e*sig*Math.pow(T[i],4);
  const U=new Array(N+1).fill(0);U[0]=sig*Math.pow(Ts,4);for(let i=0;i<N;i++)U[i+1]=U[i]*(1-e)+e*sig*Math.pow(T[i],4);
  // surface balance: abs + D[0] = σTs⁴ ; layer i: e(U[i] + D[i+1]) = 2 e σ T_i⁴
  const Tsn=Math.pow((abs+D[0])/sig,0.25);const Tn=T.map((t,i)=>Math.pow((U[i]+D[i+1])/(2*sig),0.25));
  const d=Math.abs(Tsn-Ts)+M.sum(Tn.map((t,i)=>Math.abs(t-T[i])));Ts=0.5*Ts+0.5*Tsn;T=T.map((t,i)=>0.5*t+0.5*Tn[i]);if(d<1e-9)break}
  const Ut=(()=>{let u=sig*Math.pow(Ts,4);for(let i=0;i<N;i++)u=u*(1-e)+e*sig*Math.pow(T[i],4);return u})();return{Ts,T,abs,OLR:Ut}}
function draw(){const N=sN.value,e=sE.value,al=sa.value,r=solve(N,e,al),Te=Math.pow(S0*(1-al)/4/sig,0.25);P1.clear();const g=P1.g,W=P1.w,H=P1.h;
 g.fillStyle=C.panel;g.fillRect(0,H*0.82,W,H*0.18);for(let i=0;i<N;i++){const y=H*(0.70-i*0.62/Math.max(N,1));g.fillStyle='rgba(42,120,214,0.20)';g.fillRect(W*0.25,y-12,W*0.5,24);P1.ptext('layer '+(i+1)+':  T = '+M.fmt(r.T[i],4)+' K',W*0.5,y,C.ink,'center','12px system-ui')}
 P1.ptext('surface  T_s = '+M.fmt(r.Ts,4)+' K',W/2,H*0.91,C.ink,'center','14px system-ui');
 P1.arrow(0.1,0.13,0.1,0.85,C.orange,3,10);P1.ptext('absorbed sunlight '+M.fmt(r.abs,4)+' W/m²',P1.X(0.1)+8,P1.Y(0.3),C.orange,'left');P1.arrow(0.9,0.2,0.9,0.95,C.red,3,10);P1.ptext('OLR '+M.fmt(r.OLR,4),P1.X(0.9)-8,P1.Y(0.3),C.red,'right');
 P2.clear();P2.set({ymax:Math.max(1.5,N+0.5)});P2.clear();const g2=P2.g;const pts=[[r.Ts,0],...r.T.map((t,i)=>[t,i+1])];P2.dots(pts.map(p=>p[0]),pts.map(p=>p[1]),C.blue,6);P2.line(pts.map(p=>p[0]),pts.map(p=>p[1]),C.blue,2);P2.vline(Te,C.red);P2.text('T_e = '+M.fmt(Te,4)+' K',Te+3,N+0.3,C.red);
 out.textContent=`N = ${N}, ε = ${M.fmt(e,3)}, α = ${M.fmt(al,3)}:  emission temperature T_e = (S(1−α)/4σ)^{1/4} = ${M.fmt(Te,4)} K   surface T_s = ${M.fmt(r.Ts,5)} K   greenhouse warming ΔT = ${M.fmt(r.Ts-Te,4)} K   OLR = ${M.fmt(r.OLR,5)} = absorbed ✓\nblack-layer formula T_s = T_e(1+N)^{1/4} = ${M.fmt(Te*Math.pow(1+N,0.25),5)} K (exact for ε = 1)`}
draw();ui.note('Each layer: absorbs a fraction ε of the IR from below and above and emits εσT⁴ upward and downward; the top layer\'s emission plus transmitted flux must equal the absorbed sunlight (OLR = S(1−α)/4). CL08.');
