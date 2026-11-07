//META {"title":"Gauge freedom: change A, keep the fields","desc":"A gauge transformation A → A + ∇λ, V → V − ∂λ/∂t changes the potentials but not E or B. Left: a uniform magnetic field B ẑ drawn with the Landau potential A = (0, Bx) plus ∇λ for λ = c₁xy + c₂(x² − y²)/2: the arrow field of A changes wildly while the curl (colour) stays exactly B. Right: a uniform electric field E₀ represented either by V = −E₀x with A = 0, or by V = 0 with A = −E₀t x̂, and everything in between.","vault":"ED","chapters":["ED08 Potentials and Gauge Transformations"],"tryit":"Move c₁: the arrows rotate toward the symmetric gauge (c₁ = −B/2 gives A = (B/2)(−y, x)) yet the colour map of B does not change. On the right drag the mixing slider from the static V picture to the time-dependent A picture: E = −∇V − ∂A/∂t is identical."}
ui.gridOf(2);const P1=ui.canvas(360,{xmin:-1,xmax:1,ymin:-1,ymax:1,axes:false,equal:true});
const P2=ui.canvas(360,{xmin:-1,xmax:1,ymin:-1,ymax:1,axes:false,equal:true});
const B0=1;const s1=ui.slider('c₁ (λ ∋ c₁ x y)',-1.5,1.5,0.01,0,draw),s2=ui.slider('c₂ (λ ∋ c₂ (x²−y²)/2)',-1.5,1.5,0.01,0,draw),sm=ui.slider('E picture: static V ← mix → time-dependent A',0,1,0.01,0,draw),st=ui.slider('time t',0,2,0.01,1,draw);
const out=ui.readout();
function A(x,y){// Landau A=(0,B x) + grad λ ; grad λ = (c1 y + c2 x, c1 x - c2 y)
 const c1=s1.value,c2=s2.value;return[c1*y+c2*x,B0*x+c1*x-c2*y]}
function draw(){P1.clear();const g=P1.g;
 // curl of A (should be B0): colour constant; show as uniform tint with value text
 const curl=(()=>{const h=1e-4;return(A(h,0)[1]-A(-h,0)[1])/(2*h)-(A(0,h)[0]-A(0,-h)[0])/(2*h)})();
 g.fillStyle='rgba(42,120,214,0.18)';g.fillRect(P1.X(-1),P1.Y(1),P1.X(1)-P1.X(-1),P1.Y(-1)-P1.Y(1));
 for(let i=0;i<13;i++)for(let j=0;j<13;j++){const x=-0.92+i*0.153,y=-0.92+j*0.153,a=A(x,y),L=Math.hypot(a[0],a[1]);if(L<1e-9)continue;const s=0.11/Math.max(L,0.6);P1.arrow(x,y,x+a[0]*s*1.4,y+a[1]*s*1.4,C.orange,1.6,5)}
 P1.ptext('A field (arrows);  B = ∇×A = '+M.fmt(curl,6)+' ẑ  everywhere (blue tint)',P1.w/2,12,C.ink,'center','12px system-ui');
 // right: E picture
 P2.clear();const m=sm.value,t=st.value,E0=1;
 // potentials: V = -E0 x (1-m) ; A = -E0 t m x̂ ... gauge function lambda = E0 x t m : A' = A + grad lambda, V' = V - dlambda/dt
 g.fillStyle='rgba(235,104,52,0.07)';g.fillRect(P2.X(-1),P2.Y(1),P2.X(1)-P2.X(-1),P2.Y(-1)-P2.Y(1));
 // V(x) = -(1-m)E0 x shown as a horizontal shading gradient; A_x = -m E0 t shown as blue arrows; E = -dV/dx - dA/dt = E0 for any mix
 for(let i=0;i<40;i++){const x=-1+2*i/40;g.fillStyle=`rgba(42,120,214,${0.04+0.55*(1-m)*(i/40)})`;g.fillRect(P2.X(x),P2.Y(1),P2.X(x+0.05)-P2.X(x)+1,P2.Y(-1)-P2.Y(1))}
 for(let j=0;j<5;j++){const y=-0.8+j*0.4;P2.arrow(-0.45,y,0.45,y,C.red,3,10)}
 for(let j=0;j<4;j++){const y=-0.6+j*0.4+0.0;P2.arrow(0,y+0.1,-0.8*m*t/2,y+0.1,C.violet,2,8)}
 P2.ptext('blue shading ∝ V (darker toward +x for the static picture); violet arrows = A_x = −E₀t·mix; red = E (identical)',P2.w/2,P2.h-26,C.muted,'center','11px system-ui');
 P2.ptext('E = −∇V − ∂A/∂t = E₀ x̂ (red) for every mix',P2.w/2,12,C.ink,'center');
 P2.ptext(`V = ${M.fmt(-(1-m),3)}·E₀x      A_x = ${M.fmt(-m*t,3)}·E₀ t`,P2.w/2,P2.h-12,C.muted,'center','12px system-ui');
 const V_x=-(1-m);const Ax_t=-m;const Ex=-V_x-Ax_t;// -dV/dx - dA/dt
 out.textContent=`left:  A = (c₁y + c₂x, Bx + c₁x − c₂y), ∇×A = ${M.fmt(curl,6)} = B₀ for every c₁, c₂ (λ = c₁xy + c₂(x²−y²)/2 is harmonic and time-independent, so E = −∂A/∂t = 0 stays 0)\nright: E_x = −∂V/∂x − ∂A_x/∂t = ${M.fmt(-V_x,3)} + ${M.fmt(-Ax_t,3)} = ${M.fmt(Ex,3)} E₀ for every mix: V = −(1−mix)E₀x, A_x = −mix·E₀t (gauge function λ = mix·E₀ x t)`}
draw();ui.note('Uniform E from V: V = −E₀x. Same E from A: A = −E₀ t x̂ (ED08 Worked example 2 is the point-charge analogue: V = 0, A ∝ −qt r̂/r² versus A = 0, V = q/4πε₀r). The canonical momentum shifts by q∇λ but trajectories are identical (ED08 Worked example 6).');
