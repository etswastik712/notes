//META {"title":"Noether in action: which symmetry conserves what?","desc":"A particle moves in the plane in one of three potentials. Watch the four candidate conserved quantities p_x, p_y, L_z = x p_y − y p_x and E over time: only those that match a symmetry of the potential stay flat. Isotropic well → L_z and E; well depending on x only (translation symmetry in y) → p_y and E; anisotropic well → only E.","vault":"CM","chapters":["CM03 Symmetries, Noether's Theorem and Conservation Laws"],"tryit":"Cycle through the three potentials with the same initial condition and see which curves become flat lines."}
ui.gridOf(2);const P1=ui.canvas(340,{xmin:-2.2,xmax:2.2,ymin:-2.2,ymax:2.2,axes:false,equal:true});
const P2=ui.canvas(340,{xmin:0,xmax:30,ymin:-2,ymax:2,xlabel:'t',ylabel:'value / initial value scale',title:'candidate conserved quantities'});
const sel=ui.select('potential',[['i','isotropic ½k r²  (rotation symmetry)'],['x','½k x²  (translation symmetry in y)'],['a','½k(x² + 4y²)  (no continuous symmetry)']],reset,'i');
const sv=ui.slider('initial vy',0.2,1.5,0.01,0.9,reset);
const out=ui.readout();let s,t,tr=[],H=[];
function acc(x,y){const k=sel.value;if(k==='i')return[-x,-y];if(k==='x')return[-x,0];return[-x,-4*y]}
function U(x,y){const k=sel.value;return k==='i'?0.5*(x*x+y*y):k==='x'?0.5*x*x:0.5*(x*x+4*y*y)}
function qs(){const[x,y,vx,vy]=s;return[vx,vy,x*vy-y*vx,0.5*(vx*vx+vy*vy)+U(x,y)]}
function reset(){s=[1,0.5,0.0,sv.value];t=0;tr=[];H=[];for(let i=0;i<1500;i++)step(0.02);draw()}
function step(h){s=M.rk4((tt,y)=>[y[2],y[3],...acc(y[0],y[1])],s,0,h);t+=h;tr.push([s[0],s[1]]);H.push([t,...qs()])}
function draw(){P1.clear();P1.line(tr.map(a=>a[0]),tr.map(a=>a[1]),C.blue,1.4);P1.circle(s[0],s[1],6,C.orange,C.ink);P1.circle(0,0,3,C.ink);
 const t0=Math.max(0,t-30);P2.set({xmin:t0,xmax:t0+30});const h=H.filter(a=>a[0]>=t0);P2.clear();P2.hline(0,C.grid);
 const names=['p_x','p_y','L_z','E'],cols=[C.blue,C.orange,C.aqua,C.violet];
 for(let k=0;k<4;k++)P2.line(h.map(a=>a[0]),h.map(a=>a[k+1]),cols[k],2.2);P2.legend(names.map((n,i)=>[n,cols[i]]),P2.o.ml+8,P2.o.mt+12);
 const ranges=[1,2,3,4].map(k=>{const v=H.map(a=>a[k]);return Math.max(...v)-Math.min(...v)});
 out.textContent=['p_x','p_y','L_z','E'].map((n,i)=>`${n}: variation over the run = ${M.fmt(ranges[i],3)}  ${ranges[i]<1e-5?'← conserved':''}`).join('\n')}
loop((dt)=>{const n=Math.max(1,Math.round(dt/0.01));for(let i=0;i<n;i++)step(dt/n);if(tr.length>4000){tr.splice(0,tr.length-4000)}if(H.length>6000)H.splice(0,H.length-6000);draw()});
reset();ui.note('Noether (CM03 §6): a one-parameter symmetry of L gives I = (∂L/∂q̇)·dh/ds. Rotation → L_z; translation along y → p_y; time translation → E.');
