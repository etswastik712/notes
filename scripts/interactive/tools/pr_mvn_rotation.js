//META {"title": "Rotating a correlated Gaussian to independent coordinates (HW6 Q1)", "desc": "A bivariate normal with s.d. σ₁, σ₂ and correlation ρ (left: 1200 points, the 1σ and 2σ contours, the rotated axes y₁, y₂ at angle θ). Right: the same points in the coordinates Y = Oθ X, Y₁ = cosθ·X₁ + sinθ·X₂, Y₂ = −sinθ·X₁ + cosθ·X₂. Only one angle (up to 90°) makes Y₁ and Y₂ uncorrelated, hence independent for a normal: the direction of an eigenvector of Σ. At that angle the variances of Y are the eigenvalues of Σ (not σ₁² and σ₂²); only the trace is preserved. Press 'snap θ to the eigenvector' to jump there.", "vault": "PR", "chapters": ["PR09 Change of Variables the Multivariate Normal and Products of Uniforms"], "tryit": "σ₁ = σ₂ = 1.5, ρ = 0.8: the eigenvectors are at θ = 45° and the eigenvalues are σ²(1 ± ρ) = 4.05 and 0.45 (ratio of the axis lengths 3); at θ = 45° the Y-cloud is an upright ellipse with correlation 0. Then take σ₁ = 2, σ₂ = 1, ρ = 0.5: the snap angle is not 45° and Var Y₁ + Var Y₂ stays σ₁² + σ₂² = 5 for every θ."}
ui.gridOf(2);
const PX=ui.canvas(380,{xmin:-6,xmax:6,ymin:-6,ymax:6,xlabel:'x₁',ylabel:'x₂',title:'X ~ N(0, Σ): contours and the rotated axes y₁ (blue), y₂ (orange)',equal:true});
const PY=ui.canvas(380,{xmin:-6,xmax:6,ymin:-6,ymax:6,xlabel:'y₁',ylabel:'y₂',title:'Y = O_θ X: the same points in the rotated coordinates',equal:true});
const s1=ui.slider('σ₁ (s.d. of X₁)',0.5,3,0.05,1.5,()=>draw(false)),s2=ui.slider('σ₂ (s.d. of X₂)',0.5,3,0.05,1.5,()=>draw(false)),sr=ui.slider('correlation ρ',-0.95,0.95,0.01,0.8,()=>draw(false)),st=ui.slider('rotation angle θ (degrees)',-90,90,0.5,0,()=>draw(false));
ui.button('snap θ to the eigenvector',()=>{const a=sig(),th=0.5*Math.atan2(2*a.c,a.a-a.b)*180/Math.PI;st.value=Math.round(th*2)/2;if(st.el)st.el.value=st.value;draw(false)});
ui.button('resample',()=>draw(true));
const out=ui.readout();
let seedN=3,Z=null;
function sig(){const a=s1.value*s1.value,b=s2.value*s2.value,c=sr.value*s1.value*s2.value;return{a,b,c}}
function gen(){const r=M.rng(500+(seedN++)),n=1200;Z=[];for(let i=0;i<n;i++)Z.push([M.gauss(r),M.gauss(r)])}
function ellipse(S,k){const {a,b,c}=S,tr=a+b,dt=Math.sqrt(Math.max(0,(a-b)*(a-b)/4+c*c)),l1=tr/2+dt,l2=tr/2-dt,th=0.5*Math.atan2(2*c,a-b);const xs=[],ys=[];for(let i=0;i<=120;i++){const t=2*Math.PI*i/120;const u=k*Math.sqrt(l1)*Math.cos(t),v=k*Math.sqrt(Math.max(l2,0))*Math.sin(t);xs.push(u*Math.cos(th)-v*Math.sin(th));ys.push(u*Math.sin(th)+v*Math.cos(th))}return[xs,ys]}
function draw(resim){if(resim||!Z)gen();
 const S=sig(),rho=sr.value,sd1=s1.value,sd2=s2.value,th=st.value*Math.PI/180,c=Math.cos(th),s=Math.sin(th);
 const R=Math.max(3,2.7*Math.sqrt(Math.max(S.a,S.b)));PX.set({xmin:-R,xmax:R,ymin:-R,ymax:R});PY.set({xmin:-R,xmax:R,ymin:-R,ymax:R});PX.clear();PY.clear();
 const X=Z.map(z=>[sd1*z[0],sd2*(rho*z[0]+Math.sqrt(1-rho*rho)*z[1])]);
 const Y=X.map(p=>[c*p[0]+s*p[1],-s*p[0]+c*p[1]]);
 PX.dots(X.map(p=>p[0]),X.map(p=>p[1]),'rgba(42,120,214,0.35)',2.2);PY.dots(Y.map(p=>p[0]),Y.map(p=>p[1]),'rgba(42,120,214,0.35)',2.2);
 for(const k of[1,2]){const[ex,ey]=ellipse(S,k);PX.line(ex,ey,C.orange,1.8);
  const SY={a:c*c*S.a+2*c*s*S.c+s*s*S.b,b:s*s*S.a-2*c*s*S.c+c*c*S.b,c:c*s*(S.b-S.a)+(c*c-s*s)*S.c};const[fx,fy]=ellipse(SY,k);PY.line(fx,fy,C.orange,1.8)}
 PX.arrow(-R*0.95*c,-R*0.95*s,R*0.95*c,R*0.95*s,C.blue,2);PX.arrow(R*0.95*s,-R*0.95*c,-R*0.95*s,R*0.95*c,C.orange,2);
 PX.text('y₁',R*0.8*c+0.1,R*0.8*s+0.35,C.blue);PX.text('y₂',-R*0.8*s+0.1,R*0.8*c+0.35,C.orange);
 PY.hline(0,C.muted,[]);PY.vline(0,C.muted,[]);
 const n=Y.length;let m1=0,m2=0;Y.forEach(p=>{m1+=p[0];m2+=p[1]});m1/=n;m2/=n;let v1=0,v2=0,cv=0;Y.forEach(p=>{v1+=(p[0]-m1)**2;v2+=(p[1]-m2)**2;cv+=(p[0]-m1)*(p[1]-m2)});v1/=n;v2/=n;cv/=n;
 const tr=S.a+S.b,dt=Math.sqrt((S.a-S.b)*(S.a-S.b)/4+S.c*S.c),l1=tr/2+dt,l2=tr/2-dt,thStar=0.5*Math.atan2(2*S.c,S.a-S.b)*180/Math.PI;
 const V1=c*c*S.a+2*c*s*S.c+s*s*S.b,V2=s*s*S.a-2*c*s*S.c+c*c*S.b,CV=c*s*(S.b-S.a)+(c*c-s*s)*S.c,cr=CV/Math.sqrt(V1*V2);
 out.textContent=`Σ = [[${M.fmt(S.a,3)}, ${M.fmt(S.c,3)}], [${M.fmt(S.c,3)}, ${M.fmt(S.b,3)}]]   eigenvalues λ₁ = ${M.fmt(l1,3)}, λ₂ = ${M.fmt(l2,3)}   eigenvector angle θ* = ${M.fmt(thStar,3)}°   (tr Σ = ${M.fmt(tr,3)}, det Σ = ${M.fmt(S.a*S.b-S.c*S.c,3)} = λ₁λ₂)\n`+
  `at θ = ${M.fmt(st.value,3)}°:  Var Y₁ = ${M.fmt(V1,3)}, Var Y₂ = ${M.fmt(V2,3)}  (sum ${M.fmt(V1+V2,3)} = tr Σ),  Cov(Y₁,Y₂) = ${M.fmt(CV,3)},  corr = ${M.fmt(cr,3)}   |   sample: Var ${M.fmt(v1,3)}, ${M.fmt(v2,3)},  corr ${M.fmt(cv/Math.sqrt(v1*v2),3)}\n`+
  (Math.abs(cr)<0.02?'→ Y₁ and Y₂ are uncorrelated, so (being jointly normal) INDEPENDENT; their variances are the eigenvalues λ₁, λ₂ of Σ (not σ₁², σ₂²).':'→ still correlated: the cloud is tilted in the Y-plane; rotate to θ* to remove the tilt.')}
draw(true);
ui.note('HW6 Q1: f_Y(y) = f_X(Oᵀy)·|det O| with |det O| = 1; the exponent (x−μ)ᵀΣ⁻¹(x−μ) becomes Σ(y_i−μ′_i)²/λ_i when OΣOᵀ = diag(λ); det Σ = Πλ_i. The factorised density is independence. Cov(Y₁,Y₂) = ½ sin2θ·(σ₂²−σ₁²) + cos2θ·ρσ₁σ₂, zero at tan2θ = 2ρσ₁σ₂/(σ₁²−σ₂²).');
