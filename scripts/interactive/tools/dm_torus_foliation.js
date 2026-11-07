//META {"title":"Leaves of a linear foliation of the torus: closed or dense?","desc":"The torus T² = ℝ²/ℤ² is foliated by the lines of slope θ: the leaf through a point is t ↦ (t, θt) mod 1. In a flat chart (a small square) each leaf appears as a <b>countable union of parallel slices</b>. For rational θ = p/q the leaf closes up after q turns and is an embedded circle; for irrational θ it never closes and is dense: an immersed, weakly embedded but not embedded submanifold (Lee Ex. 19.18(e)). Choose a slope and the number of turns: the right panel shows the successive crossings of the transversal circle x = ½ and how fast the gaps shrink.","vault":"DM","chapters":["DM17 Foliations, Weakly Embedded Submanifolds and Lie Subgroups","DM15 Closed Subgroups and the Lie Correspondence"],"tryit":"Slope 3/5: after 5 turns the leaf closes (exactly 5 distinct crossing points, spacing 0.2). Slope √2: after N turns there are N distinct crossings and the largest gap is about 1.2–1.5 / N (the gaps take only three sizes). Compare with slope 0.6 + 10⁻⁶: it looks closed for ~10⁵ turns and then changes: density is a limit statement."}
ui.gridOf(2);const P1=ui.canvas(380,{xmin:0,xmax:1,ymin:0,ymax:1,equal:true,ml:48,mr:12,mt:26,mb:36,xlabel:'angle 1',ylabel:'angle 2',title:'the leaf in the unrolled torus'});const P2=ui.canvas(380,{xmin:0,xmax:3,ymin:-5,ymax:0.2,xlabel:'log₁₀ N (number of turns)',ylabel:'log₁₀ (largest gap)',title:'largest gap on the transversal x = ½'});
const PRE={a:['slope 1/2',0.5],b:['slope 3/5',0.6],c:['slope √2',Math.SQRT2],d:['golden ratio 1/φ = 0.618…',(Math.sqrt(5)-1)/2],e:['slope π − 3',Math.PI-3],f:['slope 0.6 + 10⁻⁶ (nearly 3/5)',0.600001]};
const out=ui.readout();
function crossings(th,N){const a=[];for(let k=0;k<N;k++)a.push(((th*(0.5+k))%1+1)%1);return a}
function maxgap(pts){const s=pts.slice().sort((x,y)=>x-y);let m=0;for(let i=0;i<s.length;i++){const g=(i+1<s.length?s[i+1]:s[0]+1)-s[i];if(g>m)m=g}return m}
function draw(){const th=PRE[pre.value][1],N=sn.value;P1.clear();
 // leaf: t in [0,N], x = t mod 1, y = th t mod 1, drawn per unit step in x (each step is a straight segment of slope th, wrapping in y)
 P1.clip();const g=P1.g;g.lineWidth=1.6;g.strokeStyle=C.blue;g.beginPath();
 for(let k=0;k<N;k++){let y0=(th*k)%1;let y1=y0+th;let x0=0,x1=1;
  // segment from (0,y0) to (1,y1) in the cover; wrap in y
  let ya=y0,yb=y1;let xa=0;while(yb>1+1e-12){const frac=(1-ya)/(yb-ya);const xm=xa+(1-xa)*frac;g.moveTo(P1.X(xa),P1.Y(ya));g.lineTo(P1.X(xm),P1.Y(1));ya=0;yb-=1;xa=xm}
  g.moveTo(P1.X(xa),P1.Y(ya));g.lineTo(P1.X(1),P1.Y(yb))}
 g.stroke();P1.unclip();P1.vline(0.5,C.ink,[3,3]);
 const pts=crossings(th,N);for(const y of pts)P1.dot(0.5,y,C.orange,3.2);
 // right: max gap vs N
 P2.clear();const xs=[],ys=[];for(let n=1;n<=1000;n=Math.ceil(n*1.15+0.5)){xs.push(Math.log10(n));ys.push(Math.log10(maxgap(crossings(th,n))))}
 P2.line(xs,ys,C.blue,3);P2.line([0,3],[0,-3],C.muted,1.6,[5,3]);P2.dot(Math.log10(N),Math.log10(maxgap(pts)),C.orange,7);P2.legend([['largest gap after N turns',C.blue],['1/N',C.muted,[5,3]]],P2.o.ml+8,P2.o.mt+14);
 const s=pts.slice().sort((a,b)=>a-b);const uniq=new Set(pts.map(v=>Math.round(v*1e9)/1e9)).size;const mg=maxgap(pts);
 const gaps=new Set();for(let i=0;i<s.length;i++){const gg=(i+1<s.length?s[i+1]:s[0]+1)-s[i];gaps.add(Math.round(gg*1e8)/1e8)}
 const rat=pre.value==='a'||pre.value==='b';
 out.textContent=`θ = ${M.fmt(th,7)}, N = ${N} turns:  distinct crossings of x = ½: ${uniq},   largest gap = ${M.fmt(mg,4)},   N × largest gap = ${M.fmt(N*mg,3)},   distinct gap sizes = ${gaps.size}\n${rat?'rational: the leaf is an embedded circle (closes after q turns), a closed subset: the number of crossings stops growing at q':'irrational (or nearly): the leaf never closes, the crossings never stop accumulating: dense, immersed but not embedded'}`}
draw();ui.note('DM17 §2. The left panel is the leaf t ↦ (t, θt) mod 1 for 0 ≤ t ≤ N (the torus cut open to the unit square); each straight piece is one slice of the flat chart. The numbers for √2 agree with the script check in dm_numbers2.py (N = 10, 100, 1000: N × largest gap = 1.716, 1.219, 1.225; three distinct gap sizes).');
