//META {"title":"The dihedral group D_n: symmetries, the Cayley table and cosets","desc":"Act on a labelled regular n-gon with the rotation r (by 2π/n) and the reflection s. Every state is r^a s^b, the group has 2n elements, and rs ≠ sr (the group is non-abelian for n ≥ 3, with srs = r⁻¹). The Cayley table is coloured by element, so every row and column is a permutation of the colours (cancellation). Pick any element g: the cyclic subgroup ⟨g⟩ is found and the left cosets aH are shown (they partition the group into equal blocks, Lagrange).","vault":"GT","chapters":["GT01 Groups Subgroups and Cosets","GT06 Permutation Groups"],"tryit":"n = 3 gives D₃ ≅ S₃: press r, then s, and compare with s then r (a different state). Choose g = s: the cosets are {1,s}, {r, rs}, {r², r²s} (3 cosets of size 2). Choose g = r in D₄: ⟨r⟩ has order 4, index 2: a normal subgroup."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-1.5,xmax:1.5,ymin:-1.5,ymax:1.5,axes:false,equal:true,title:'the labelled n-gon (current symmetry)'});const P2=ui.canvas(340,{xmin:0,xmax:1,ymin:0,ymax:1,axes:false,title:'Cayley table (row · column); row labels coloured by left coset'});
const sn=ui.slider('n (sides)',3,8,1,3,()=>{cur=[0,0];draw()}),sg=ui.select('choose g to generate a subgroup',[],()=>draw(),'');
ui.button('apply r (rotate)',()=>{cur=mul([1,0],cur);draw()});ui.button('apply s (reflect)',()=>{cur=mul([0,1],cur);draw()});ui.button('reset to identity',()=>{cur=[0,0];draw()});
const out=ui.readout();let cur=[0,0],lastN=0;
function mul(h,g){const n=sn.value;const a=h[0],b=h[1],c=g[0],d=g[1];return[(((a+(b?-c:c))%n)+n)%n,(b+d)%2]}
const eq=(x,y)=>x[0]===y[0]&&x[1]===y[1],name=e=>(e[0]===0&&e[1]===0)?'1':((e[0]?'r'+(e[0]>1?'^'+e[0]:''):'')+(e[1]?'s':''));
function elems(){const n=sn.value,L=[];for(let b=0;b<2;b++)for(let a=0;a<n;a++)L.push([a,b]);return L}
function powers(g){const L=[[0,0]];let x=g;while(!eq(x,[0,0])){L.push(x);x=mul(g,x)}return L}
function fillSelect(){const n=sn.value;if(lastN!==n){lastN=n;const s=sg.el||document.querySelector('select');}}
function draw(){const n=sn.value,L=elems();const sel=document.querySelectorAll('select')[document.querySelectorAll('select').length-1];if(sel&&sel.options.length!==2*n){sel.innerHTML='';L.forEach((e,i)=>{const o=document.createElement('option');o.value=i;o.textContent=name(e);sel.append(o)});sel.value=Math.min(1,2*n-1)}
 const gi=sel?parseInt(sel.value||'1'):1,g=L[gi]||[1,0],H=powers(g);
 // polygon
 P1.clear();const G=P1.g;const R=1.1;const pos=q=>[R*Math.cos(2*Math.PI*q/n+Math.PI/2),R*Math.sin(2*Math.PI*q/n+Math.PI/2)];const pts=M.range(n).map(pos);P1.poly(pts,'rgba(120,120,120,0.12)',C.ink,2.5);
 const a=cur[0],b=cur[1];const cols=[C.red,C.blue,C.aqua,C.orange,C.violet,C.gold,C.muted,C.ink];for(let q=0;q<n;q++){const p=(((b?-1:1)*(q-a))%n+n)%n;const [x,y]=pos(q);P1.circle(x,y,15,cols[p%8],C.ink);P1.text(String(p+1),x,y,'#fff','center','bold 13px system-ui')}
 P1.line([pos(0)[0]*0.0,0],[0,0],C.ink);P1.text('state = '+name(cur),0,0,C.ink,'center','bold 16px system-ui');
 // table
 const G2=P2.g;
 P2.clear();const N2=2*n,Wd=P2.w-30,Hd=P2.h-26,cs=Math.min(Wd,Hd)/(N2+1),x0=30,y0=26;const ecol=e=>{const i=e[0]+n*e[1];return `hsl(${Math.round(360*i/N2)},60%,62%)`};
 // coset index per element
 const cosetOf=new Map();const cosets=[];L.forEach(x=>{const k=name(x);if(cosetOf.has(k))return;const c=H.map(h=>mul(x,h));const id=cosets.length;cosets.push(c);c.forEach(y=>cosetOf.set(name(y),id))});
 const cc=id=>`hsl(${Math.round(360*id/cosets.length)},70%,55%)`;
 L.forEach((r,i)=>{G2.fillStyle=cc(cosetOf.get(name(r)));G2.fillRect(x0-cs*0.9,y0+(i+1)*cs,cs*0.85,cs-1);P2.ptext(name(r),x0-cs*0.45,y0+(i+1)*cs+cs/2,'#000','center',Math.max(8,Math.min(11,cs*0.5))+'px system-ui');P2.ptext(name(r),x0+(i+1)*cs+cs/2,y0+cs*0.45,C.ink,'center',Math.max(8,Math.min(11,cs*0.5))+'px system-ui')});
 L.forEach((r,i)=>L.forEach((c,j)=>{const p=mul(r,c);G2.fillStyle=ecol(p);G2.fillRect(x0+(j+1)*cs,y0+(i+1)*cs,cs-1,cs-1);if(eq(r,cur)||eq(c,cur)){G2.strokeStyle=C.ink;G2.lineWidth=0;}}));
 const rs=mul([1,0],[0,1]),sr=mul([0,1],[1,0]);
 out.textContent=`|D_${n}| = 2n = ${2*n}.  r·s = ${name(rs)} and s·r = ${name(sr)}: ${eq(rs,sr)?'equal':'DIFFERENT, so the group is non-abelian'}   (s r s = r⁻¹ = ${name(mul(mul([0,1],[1,0]),[0,1]))})\ng = ${name(g)}: order ${H.length}, H = ⟨g⟩ = {${H.map(name).join(', ')}}   index |G:H| = ${cosets.length} left cosets, each of size ${H.length}: ${cosets.map(c=>'{'+c.map(name).join(', ')+'}').join('  ')}   Lagrange: ${H.length} divides ${2*n} ✓   H normal? ${L.every(x=>cosets.find(c=>c.some(y=>eq(y,x)))&&H.every(h=>{const k=mul(mul(x,h),inv(x));return H.some(z=>eq(z,k))}))?'yes':'no'}`}
function inv(x){const n=sn.value;let y=x;for(let i=0;i<2*n;i++){const t=mul(x,y);if(eq(t,[0,0]))return y;y=t}return x}
draw();ui.note('GT01: D_n = ⟨r, s | rⁿ = s² = 1, srs = r⁻¹⟩ of order 2n; D₃ ≅ S₃ (Cayley table in the chapter). Table colour of the entry in row a, column b is the element ab (composition: apply b first, then a). Row labels are coloured by the left coset aH of the chosen subgroup.');
