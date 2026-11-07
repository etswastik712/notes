//META {"title":"Holonomy of a plane field: why some plane fields have no integral surface","desc":"A plane field D = ker(dz − A) on R³ with A = A₁dx + A₂dy. Walk once round a closed loop in the (x, y)-plane and lift it to a curve tangent to D: z changes by ∮A = ∬ dA = (signed area) × (curl of A). If the plane field has integral surfaces (z = const + f(x, y)) the lifted loop must close up for <b>every</b> loop; otherwise the lift ends at a different height. Pick a plane field, a loop and its size: the height gap Δz is the obstruction to Frobenius integrability (the bracket [X, Y] leaves D).","vault":"DM","chapters":["DM16 Distributions, Involutivity and the Frobenius Theorem","DM15 Closed Subgroups and the Lie Correspondence"],"tryit":"Option 1 with c = 1: Δz = area exactly (for any position of the loop). Set c = 0 and Δz = 0: D = span{∂ₓ, ∂ᵧ} has the integral planes z = const. Option 3 (the Lee 19.14 distribution with leaves z − xy = const) gives Δz = 0 for every loop even though the planes are tilted. The figure-eight loop has signed area 0, so even the non-integrable fields close up for it: the obstruction is the signed area."}
ui.gridOf(2);const P1=ui.canvas(360,{xmin:-1.6,xmax:1.6,ymin:-1.6,ymax:1.6,equal:true,ml:48,mr:12,mt:26,mb:36,xlabel:'x',ylabel:'y',title:'the loop in the (x, y)-plane'});const P2=ui.canvas(360,{xmin:0,xmax:1,ymin:-1,ymax:1,xlabel:'fraction of the loop',ylabel:'z (height of the lift)',title:'height of the horizontal lift'});
const fld=ui.select('plane field D = ker(dz − A)',[['a','1:  A = c·x dy   (D = span{∂ₓ, ∂ᵧ + c x ∂_z})'],['b','2:  A = y dx   (Lee 19.1(d): span{∂ₓ + y∂_z, ∂ᵧ})'],['c','3:  A = y dx + x dy = d(xy)   (Lee 19.14: leaves z − xy = const)']],draw,'a');
const shp=ui.select('loop',[['sq','square (counter-clockwise)'],['ci','circle'],['re','rectangle 2:1'],['f8','figure eight (signed area 0)']],draw,'sq');
const sc=ui.slider('twist c (field 1 only)',-3,3,0.1,1,draw),se=ui.slider('loop size',0.05,0.8,0.01,0.5,draw),sx=ui.slider('loop centre x',-0.8,0.8,0.05,0,draw),sy=ui.slider('loop centre y',-0.8,0.8,0.05,0,draw);
const out=ui.readout();
function loopPts(kind,e,x0,y0,N){const P=[];for(let i=0;i<=N;i++){const s=i/N;let x,y;
 if(kind==='ci'){x=x0+e*Math.cos(2*Math.PI*s);y=y0+e*Math.sin(2*Math.PI*s)}
 else if(kind==='f8'){const t=2*Math.PI*s;x=x0+e*Math.sin(t);y=y0+e*Math.sin(t)*Math.cos(t)}
 else{const w=kind==='re'?2*e:e,h=e;const per=4*(w+h)/1; // piecewise: right, up, left, down starting at lower-left corner (x0-w/2? use centre)
  const L=[[w,0],[0,h],[-w,0],[0,-h]];let d=s*2*(w+h),px=x0-w/2,py=y0-h/2;for(const[dx,dy]of L){const len=Math.hypot(dx,dy);if(d<=len+1e-12){px+=dx*d/len;py+=dy*d/len;d=0;break}px+=dx;py+=dy;d-=len}x=px;y=py}
 P.push([x,y])}return P}
function area(P){let a=0;for(let i=0;i<P.length-1;i++)a+=P[i][0]*P[i+1][1]-P[i+1][0]*P[i][1];return a/2}
function draw(){const N=4000,kind=shp.value,P=loopPts(kind,se.value,sx.value,sy.value,N),c=sc.value;
 const Ax=(x,y)=>fld.value==='a'?0:(fld.value==='b'?y:y),Ay=(x,y)=>fld.value==='a'?c*x:(fld.value==='b'?0:x);
 let z=0;const zs=[0];for(let i=0;i<N;i++){const xm=(P[i][0]+P[i+1][0])/2,ym=(P[i][1]+P[i+1][1])/2;z+=Ax(xm,ym)*(P[i+1][0]-P[i][0])+Ay(xm,ym)*(P[i+1][1]-P[i][1]);zs.push(z)}
 const ar=area(P),curl=fld.value==='a'?c:(fld.value==='b'?-1:0);
 P1.clear();P1.poly(P.slice(0,-1),'rgba(42,120,214,0.13)',null);P1.line(P.map(p=>p[0]),P.map(p=>p[1]),C.blue,3);
 for(let k=0;k<6;k++){const i=Math.floor((k+0.5)/6*N);P1.arrow(P[i][0],P[i][1],P[i+8][0],P[i+8][1],C.blue,2.5,9)}
 P1.dot(P[0][0],P[0][1],C.ink,6);P1.text('start',P[0][0]+0.05,P[0][1]-0.08,C.ink);
 const zm=Math.max(0.25,...zs.map(Math.abs))*1.25;P2.set({ymin:-zm,ymax:zm});P2.clear();P2.line(M.linspace(0,1,N+1),zs,C.orange,3);P2.hline(0,C.muted);P2.dot(1,z,C.red,7);
 P2.arrow(1,0,1,z,C.red,2.5,8);P2.text('Δz = '+M.fmt(z,4),0.55,zm*0.85,C.red);
 const intg=fld.value==='c'?'integrable (leaves z − xy = const): every lifted loop closes':(fld.value==='a'&&Math.abs(c)<1e-9?'c = 0: D = span{∂ₓ, ∂ᵧ} is integrable (planes z = const)':'NOT integrable: ω∧dω ≠ 0, [X,Y] ∉ D');
 out.textContent=`signed area of the loop = ${M.fmt(ar,4)}     curl coefficient (dA = k dx∧dy) k = ${M.fmt(curl,3)}\nΔz (numerical lift) = ${M.fmt(z,5)}     k × area = ${M.fmt(curl*ar,5)}     [Stokes: ∮A = ∬dA]\n${intg}`}
draw();ui.note('DM16 §3 and DM15 §3. The lift solves dz = A₁dx + A₂dy along the loop (midpoint rule, 4000 steps). Field 1 with c = 1 reproduces the script check Δz = area (square of side 0.5: 0.25; circle of radius 0.5: 0.7854). The three fields are the examples of the chapter: Frobenius says D has integral surfaces iff dω ∧ ω = 0 (equivalently [X, Y] ∈ D), and the holonomy Δz measures exactly the failure.');
