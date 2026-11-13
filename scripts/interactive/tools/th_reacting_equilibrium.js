//META {"title": "Reacting ideal gases: the minimum of G(ε), and how pressure and inert gas shift it", "desc": "Pick a gas reaction (A ⇌ B, N₂O₄ ⇌ 2NO₂, 2A ⇌ B, SO₂ + ½O₂ ⇌ SO₃, N₂ + 3H₂ ⇌ 2NH₃), the equilibrium constant K, the total pressure P and the amount of inert gas. Left: the Gibbs energy of the mixture G(ε)/RT as a function of the extent of reaction ε (stoichiometric start, ε = 1 means all reactant consumed); its minimum is the equilibrium, where Σνᵢμᵢ = 0 and Q = K. The mixing terms Σnᵢ ln xᵢ make the minimum interior, never at ε = 0 or 1. Right: ε_eq against P for the same K: if Σν = 0 pressure does nothing; if Σν < 0 higher pressure pushes toward products; if Σν > 0 toward reactants. Inert gas at constant total P acts like lowering P (a dilution).", "vault": "TH", "chapters": ["TH10 Open Systems Mixing and Reacting Gases", "TH08 Gibbs Energy Equilibrium Constants and Phase Boundaries"], "tryit": "Choose SO₂ + ½O₂ ⇌ SO₃ with K = 10 and P = 1 bar: ε_eq = 0.7645. Raise P to 10 bar: 0.8819 (Σν = −½, so K = [x-product](P/P°)^(−½)). Add 3 mol of inert gas at 1 bar: ε_eq falls to 0.6667. Switch to A ⇌ B (Σν = 0): the right-hand curve is flat, ε_eq = K/(1+K) whatever P and the inert gas. Switch to N₂O₄ ⇌ 2NO₂ (Σν = +1): ε_eq falls as P rises."}
ui.gridOf(2);
const P1=ui.canvas(360,{xmin:0,xmax:1,ymin:-3,ymax:1,xlabel:'extent of reaction ε',ylabel:'[G(ε) − G(0)]/RT',title:'Gibbs energy of the mixture: the minimum is the equilibrium'});
const P2=ui.canvas(360,{xmin:-1,xmax:3,ymin:0,ymax:1,xlabel:'log₁₀ (P / bar)',ylabel:'equilibrium extent ε_eq',title:'ε_eq against total pressure (same K, same inert)'});
const RX={a:{n:'A ⇌ B   (Σν = 0)',nu:[-1,1],names:['A','B']},d:{n:'N₂O₄ ⇌ 2NO₂   (Σν = +1)',nu:[-1,2],names:['N₂O₄','NO₂']},t:{n:'2A ⇌ B   (Σν = −1)',nu:[-2,1],names:['A','B']},s:{n:'SO₂ + ½O₂ ⇌ SO₃   (Σν = −½)',nu:[-1,-0.5,1],names:['SO₂','O₂','SO₃']},h:{n:'N₂ + 3H₂ ⇌ 2NH₃   (Σν = −2)',nu:[-1,-3,2],names:['N₂','H₂','NH₃']}};
const rx=ui.select('reaction',Object.keys(RX).map(k=>[k,RX[k].n]),()=>draw(),'s');
const sK=ui.slider('log₁₀ K (at the standard pressure 1 bar)',-3,4,0.05,1,()=>draw(),v=>'K = '+M.fmt(Math.pow(10,v),3));
const sP=ui.slider('total pressure log₁₀(P/bar)',-1,3,0.05,0,()=>draw(),v=>'P = '+M.fmt(Math.pow(10,v),3)+' bar');
const sI=ui.slider('moles of inert gas (at constant total P)',0,10,0.1,0,()=>draw());
const out=ui.readout();
function amounts(R0,e,nI){const nu=R0.nu,n=nu.map(v=>(v<0?-v:0)+v*e);return{n,N:n.reduce((a,b)=>a+b,0)+nI}}
function dG(R0,e,K,P,nI){const a=amounts(R0,e,nI);let s=0;R0.nu.forEach((v,i)=>{s+=v*Math.log(a.n[i]/a.N*P)});return s-Math.log(K)}
function G(R0,e,K,P,nI){const a=amounts(R0,e,nI);let s=-e*Math.log(K);a.n.forEach(x=>{if(x>0)s+=x*Math.log(x/a.N*P)});return s}
function eq(R0,K,P,nI){let lo=1e-9,hi=1-1e-9;if(dG(R0,lo,K,P,nI)>0)return lo;if(dG(R0,hi,K,P,nI)<0)return hi;for(let i=0;i<80;i++){const m=(lo+hi)/2;if(dG(R0,m,K,P,nI)<0)lo=m;else hi=m}return(lo+hi)/2}
function draw(){const R0=RX[rx.value],K=Math.pow(10,sK.value),P=Math.pow(10,sP.value),nI=sI.value,sn=R0.nu.reduce((a,b)=>a+b,0);
 const es=M.linspace(0.0005,0.9995,500),g0=G(R0,0.0005,K,P,nI),gs=es.map(e=>G(R0,e,K,P,nI)-g0);
 const gmin=Math.min(...gs),gmax=Math.max(...gs);P1.set({xmin:0,xmax:1,ymin:Math.floor(gmin-0.5),ymax:Math.ceil(gmax+0.5)});P1.clear();
 P1.hline(0,C.muted);P1.line(es,gs,C.blue,3);
 const ee=eq(R0,K,P,nI);P1.vline(ee,C.orange,[5,3]);P1.dot(ee,G(R0,ee,K,P,nI)-g0,C.orange,6);P1.text('ε_eq = '+M.fmt(ee,4),Math.min(0.62,ee+0.03),P1.o.ymax-0.4,C.orange);
 P1.text('slope dG/dε = Σνᵢμᵢ = RT ln(Q/K)',0.03,P1.o.ymax-0.4,C.muted);
 const lp=M.linspace(-1,3,200);P2.set({xmin:-1,xmax:3,ymin:0,ymax:1});P2.clear();
 P2.line(lp,lp.map(l=>eq(R0,K,Math.pow(10,l),nI)),C.blue,3);P2.line(lp,lp.map(l=>eq(R0,K,Math.pow(10,l),0)),C.muted,1.5,[5,4]);
 P2.vline(sP.value,C.orange,[5,3]);P2.dot(sP.value,ee,C.orange,6);
 P2.legend([['with the chosen inert gas',C.blue],['no inert gas',C.muted,[5,4]]],P2.o.ml+8,P2.o.mt+14);
 const a=amounts(R0,ee,nI),x=a.n.map(v=>v/a.N),xi=nI/a.N;
 let Q=1;R0.nu.forEach((v,i)=>{Q*=Math.pow(x[i]*P,v)});
 out.textContent=R0.n+'\nK = '+M.fmt(K,4)+'   P = '+M.fmt(P,4)+' bar   inert = '+M.fmt(nI,3)+' mol   →   ε_eq = '+M.fmt(ee,5)+'\nmole fractions at equilibrium: '+R0.names.map((s,i)=>s+' '+M.fmt(x[i],4)).join(',  ')+(nI>0?',  inert '+M.fmt(xi,4):'')+'\nQ = Π(xᵢP/P°)^νᵢ = '+M.fmt(Q,4)+'  (= K at equilibrium)   Σν = '+M.fmt(sn,3)+'  ⇒  K = Πxᵢ^νᵢ · (P/P°)^Σν\n'+(Math.abs(sn)<1e-9?'→ Σν = 0: the pressure cancels, ε_eq = K/(1+K) for A ⇌ B whatever P or inert gas.':sn<0?'→ Σν < 0: fewer moles of gas on the product side, so higher P (or less inert gas) pushes toward products (Le Chatelier).':'→ Σν > 0: more moles of gas on the product side, so higher P pushes toward reactants; inert gas at constant P acts like lower P and pushes toward products.')}
draw();
ui.note('TH10 / TH08: dG = Σμᵢdnᵢ = (Σνᵢμᵢ)dε at constant T, P; μᵢ = μᵢ° + RT ln(xᵢP/P°). The mixing terms nᵢ ln xᵢ (the entropy of mixing) are why G(ε) has an interior minimum. Stoichiometric start: reactant moles = |νᵢ|, products 0, so ε runs from 0 to 1.');
