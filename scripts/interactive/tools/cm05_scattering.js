//META {"title":"Scattering: from impact parameter to cross-section","desc":"A uniform beam of unit-mass particles with equally spaced impact parameters hits a fixed repulsive Coulomb centre (or a hard sphere). Each trajectory is integrated; the lower panel shows the deflection angle χ(p) and the histogram of how many particles land in each angle against Rutherford's dσ/dΩ ∝ 1/sin⁴(χ/2).","vault":"CM","chapters":["CM05 Scattering"],"tryit":"Increase the strength α/mv²: the deflections grow and the curve p = (α/mv²)cot(χ/2) steepens. Switch to hard sphere and see the isotropic (flat) dσ/dΩ = a²/4."}
ui.gridOf(1);const P1=ui.canvas(340,{xmin:-8,xmax:8,ymin:-1.5,ymax:5.5,axes:false,equal:true});
const P2=ui.canvas(260,{xmin:0,xmax:180,ymin:0,ymax:3,xlabel:'scattering angle χ (deg)',ylabel:'impact parameter p',title:'deflection function and dσ/dΩ'});
const sa=ui.slider('strength α/(m v²)',0.1,2,0.01,0.6,run),sN=ui.slider('number of particles',10,80,1,31,run),kind=ui.select('scatterer',[['c','repulsive Coulomb 1/r'],['h','hard sphere (a = 1)']],run,'c');
const out=ui.readout();
function traj(p,k){ if(k==='h'){ if(p>=1) return{pts:[[-12,p],[12,p]],chi:0}; const x0=-Math.sqrt(1-p*p),vx=2*p*p-1,vy=2*p*Math.sqrt(1-p*p);return{pts:[[-12,p],[x0,p],[x0+12*vx,p+12*vy]],chi:Math.atan2(vy,vx)}}
 const a=sa.value;let s=[-12,p,1,0];const pts=[];let st=0;while(st<12000){const f=(t,y)=>{const r=Math.hypot(y[0],y[1]);return[y[2],y[3],a*y[0]/r**3,a*y[1]/r**3]};s=M.rk4(f,s,0,0.01);if(st%20==0)pts.push([s[0],s[1]]);st++;if(Math.hypot(s[0],s[1])>12&&s[0]>0)break}
 return{pts,chi:Math.atan2(s[3],s[2])}}
function run(){const k=kind.value,N=sN.value,pmax=3,ps=M.range(N).map(i=>(i+.5)/N*pmax);P1.clear();const chis=[];
 for(const p of ps){const T=traj(p,k);const pts=T.pts;
  P1.line(pts.map(q=>q[0]),pts.map(q=>q[1]),C.blue,1.2);chis.push(Math.abs(T.chi)*180/Math.PI)}
 P1.circle(0,0,k==='h'?P1.X(1)-P1.X(0):5,k==='h'?C.panel:C.ink,C.ink);
 P2.clear();P2.line(chis.map(x=>x),ps,C.blue,2);P2.dots(chis,ps,C.orange,3);
 const a=sa.value;P2.fn(x=>k==='c'?a/Math.tan(Math.max(x,0.5)*Math.PI/360):Math.cos(x*Math.PI/360),C.muted,1.5,[4,3],200);
 // histogram: counts per solid-angle (2π sinχ dχ), compared to Rutherford
 const nb=12,cnt=new Array(nb).fill(0);chis.forEach(c=>{const b=Math.min(nb-1,Math.floor(c/180*nb));cnt[b]++});
 out.textContent=`${N} particles, p from 0 to ${pmax}.   ${k==='c'?'Rutherford: p = (α/mv²) cot(χ/2); dσ/dΩ = (α/2mv²)²/sin⁴(χ/2)  → for α/mv² = '+M.fmt(a,3)+', at χ = 90°: dσ/dΩ = '+M.fmt((a/2)**2/Math.sin(Math.PI/4)**4,4):'hard sphere: p = a cos(χ/2), dσ/dΩ = a²/4 (isotropic), σ = πa² = 3.1416'}\ncounts in 12 equal χ-bins (0–180°): ${cnt.join(' ')}`}
run();ui.note('The dashed line is the exact deflection function. Counting uniformly spaced impact parameters is the same as weighting by 2πp dp, which is why dσ = 2πp|dp/dχ|dχ.');
