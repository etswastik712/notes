//META {"title":"Particle in a box: build a state from energy eigenstates","desc":"Infinite well of width 1 (ħ = m = 1), E_n = n²π²/2. Choose the amplitudes of the first four eigenstates: a single eigenstate has a frozen |ψ|²; a superposition has |ψ|² that sloshes back and forth at the Bohr frequencies E_m − E_n, and the energy expectation value stays constant. The probability of each energy is |c_n|².","vault":"QM","chapters":["QM04 The Particle in a Box","QM03 States Operators and Measurement"],"tryit":"Put equal weight on n = 1 and 2: the packet bounces with period 2π/(E₂−E₁) = 0.85. Add n = 3 and the motion is no longer a simple oscillation. Notice ⟨E⟩ never moves."}
ui.gridOf(2);const P1=ui.canvas(300,{xmin:0,xmax:1,ymin:-3,ymax:3,xlabel:'x',ylabel:'ψ, |ψ|²'});const P2=ui.canvas(300,{xmin:0,xmax:5,ymin:0,ymax:1,xlabel:'n',ylabel:'|c_n|²',title:'energy distribution'});
const c=[1,2,3,4].map(n=>ui.slider('amplitude c'+n,0,1,0.01,n<=2?0.7:0,()=>{}));ui.button('restart',()=>{tt=0});
const out=ui.readout();let tt=0;
const E=n=>n*n*Math.PI*Math.PI/2;
function draw(){let cs=c.map(s=>s.value);let nrm=Math.sqrt(cs.reduce((a,b)=>a+b*b,0))||1;cs=cs.map(x=>x/nrm);
 const xs=M.linspace(0,1,300);const psi=xs.map(x=>{let re=0,im=0;for(let n=1;n<=4;n++){const f=Math.sqrt(2)*Math.sin(n*Math.PI*x)*cs[n-1];re+=f*Math.cos(E(n)*tt);im-=f*Math.sin(E(n)*tt)}return[re,im]});
 P1.set({ymin:-3,ymax:4});P1.clear();P1.line(xs,psi.map(p=>p[0]),C.blue,1.6);P1.line(xs,psi.map(p=>p[0]**2+p[1]**2),C.orange,3);
 const xm=M.sum(xs.map((x,i)=>x*(psi[i][0]**2+psi[i][1]**2)))/(xs.length-1)*(xs.length-1)/ (M.sum(psi.map(p=>p[0]**2+p[1]**2))||1);P1.vline(xm,C.red);P1.legend([['Re ψ',C.blue],['|ψ|²',C.orange]],P1.o.ml+8,P1.o.mt+14);
 P2.clear();P2.set({ymax:1});cs.forEach((v,i)=>{const x0=i+1;const g=P2.g;g.fillStyle=C.violet;g.fillRect(P2.X(x0-.3),P2.Y(v*v),P2.X(x0+.3)-P2.X(x0-.3),P2.Y(0)-P2.Y(v*v))});
 const Em=M.sum(cs.map((v,i)=>v*v*E(i+1)));
 out.textContent=`t = ${M.fmt(tt,3)}   ⟨x⟩ = ${M.fmt(xm,4)}   ⟨E⟩ = Σ|c_n|²E_n = ${M.fmt(Em,4)} (constant)   E₁ = ${M.fmt(E(1),4)}, E₂ = ${M.fmt(E(2),4)}, E₃ = ${M.fmt(E(3),4)}, E₄ = ${M.fmt(E(4),4)}\nBohr period 2π/(E₂−E₁) = ${M.fmt(2*Math.PI/(E(2)-E(1)),4)}   revival time 4/π = ${M.fmt(4/Math.PI,4)}`}
loop((dt)=>{tt+=dt*0.5;draw()});draw();
ui.note('ψ_n(x) = √2 sin(nπx), E_n = n²π²ħ²/2mL² (QM04). The revival at T = 4mL²/πħ occurs because every E_n is an integer multiple of E₁.');
