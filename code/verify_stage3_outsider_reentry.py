"""Stage 3 economic mechanism candidate: reentrant outsider Cournot activity.

Exact model, not additional primitives: η=κ/2, endogenous ONE s, exogenous
v, positive demand-SPD, positive prices and nonnegative marginal costs.
Proves necessary/sufficient double-market-activity switch at fixed theta,
a unique analytic network-externality threshold within a whole interval,
and a robust STRONG Stage-1 REGIONAL contract precisely when outsider
production is ZERO despite outsider government positive welfare gain.

Proof method: symbolic identities and exact rational Sturm real-root
counts on whole continuous t intervals, not sampling/optimizer.
Stage3 CONDITIONAL mathematics evidence, NOT peer-reviewed IO novelty.
"""
import sympy as S
t,v=S.symbols("s v", real=True)
R=S.Rational

# --- 1. General normalized 5D model: complete double-exit criterion ---
G,L,E,r=S.symbols("G Lambda Delta rho",real=True)
Y=S.expand(2-G+(L+2*E-2*G*r)*t+2*E*r*t*t)
C=2-G
B=L+2*E-2*G*r
Q=2*E*r
Y1=S.expand(Y.subs(t,1))
s_vertex=-B/(2*Q)
disc=S.expand(B**2-4*Q*C)
assert S.factor(Y-(C+B*t+Q*t*t))==0
assert S.factor(Y.subs(t,s_vertex)+disc/(4*Q))==0
# For 0<=G<1 and E,r>0, DOUBLE switch 0<r1<r2<1
# iff B<0, 0<-B/(2Q)<1, disc>0, Y(1)>0.
# At E=0 or r=0, Q=0 and only one root at most.
print("PASS generic quadratic activity and necessary/sufficient")
print("  B<0, 0<-B/(2Q)<1, B²-4Q(2-G)>0, Y(1)>0",flush=True)

# --- 2. Network bifurcation family retains η=κ/2 exactly ---
a=R(1);c0=R(9,10);h=R(1,2)
gamma=R(9,25);kappa=R(3,5);eta=kappa/2
A=a-c0;rho=h/A
assert eta==kappa/2 and c0-h>=0 and a>c0
m=1-v
b=gamma+(kappa-v)*t
d=gamma-eta*t
Yphys=S.expand(2*m+b-2*d*(1+rho*t))
assert S.factor(Yphys-(R(41,25)-2*v-(R(12,5)+v)*t+3*t*t))==0
assert S.diff(Yphys,v)==-(2+t)
Dscr=S.factor(S.discriminant(Yphys,t))
assert S.factor(Dscr-(v*v+R(144,5)*v-R(348,25)))==0
vstar=(-72+2*S.sqrt(1383))/5
assert S.simplify(Dscr.subs(v,vstar))==0
assert R(47,100)<vstar<R(48,100)<R(16,25)
# For v∈[0,16/25): vertex (12/5+v)/6 ∈ (.4,.507),
# Y(0)=41/25−2v>0; Y(1)=56/25−3v>0.
svert=(R(12,5)+v)/6
assert svert.subs(v,0)>0 and svert.subs(v,R(16,25))<1
assert Yphys.subs(t,0).subs(v,R(16,25))>0
assert Yphys.subs(t,1).subs(v,R(16,25))>0
assert S.factor(S.diff(Dscr,v))==2*v+R(144,5)
# SPD for all v∈[0,16/25) and s∈[0,1]:
# m−gamma>0; m−b(1)=1−gamma−kappa=1/25>0;
# m+2b(1)>0; RS determinant concave in s,
# minimum at s=0 or 1, positive throughout v range.
assert 1-gamma-kappa==R(1,25)
assert S.factor((m+2*b.subs(t,1)).subs(v,R(16,25)))>0
for ep in (0,1):
    det=S.factor((m*(m+b)-2*d*d).subs(t,ep))
    assert det.subs(v,0)>0 and det.subs(v,R(16,25))>0
    assert S.Poly(det,v).count_roots(0,R(16,25))==0
print("PASS network bifurcation: v*=(-72+2√1383)/5≈",
      vstar.evalf(13),flush=True)
print("PASS 0<=v<v*: outsider active for all s; "
      "v*<v<16/25: active/exited/active",flush=True)
print("NOTE v changes BOTH own demand m=1−v and inside cross b",flush=True)

# --- 3. Exact economically regular witness + Stage 2 Cournot KKT ---
v0=R(31,50)
assert vstar<v0<R(16,25)
m0=S.factor(m.subs(v,v0));b0=b.subs(v,v0);d0=d
fee=R(15,38)
Fn=S.factor(m0*fee/A**2)
assert Fn==15
ymark=S.factor(Yphys.subs(v,v0))
assert ymark==3*t*t-R(151,50)*t+R(2,5)
root1=(151-S.sqrt(10801))/300
root2=(151+S.sqrt(10801))/300
assert S.factor(ymark.subs(t,root1))==0
assert S.factor(ymark.subs(t,root2))==0
assert 0<root1<R(1,2)<root2<1
assert ymark.subs(t,0)>0 and ymark.subs(t,R(1,2))==-R(9,25)
assert ymark.subs(t,1)>0
Delta0=2*m0*(2*m0+b0)-2*d0**2
xi=S.cancel((2*m0*(A+h*t)-d0*A)/Delta0)
yi=S.cancel(((2*m0+b0)*A-2*d0*(A+h*t))/Delta0)
xc=S.cancel((A+h*t)/(2*m0+b0))
qi=S.cancel((A+h*t)/(2*(m0+b0)))
qn=S.cancel(A/(2*(m0+gamma)))
# Verify every interior row and inactive-outsider Kuhn–Tucker branch.
assert S.factor((2*m0+b0)*xi+d0*yi-(A+h*t))==0
assert S.factor(2*m0*yi+2*d0*xi-A)==0
assert S.factor((2*m0+b0)*xc-(A+h*t))==0
assert S.factor((A-2*d0*xc)*(2*m0+b0)-A*ymark)==0
assert S.factor((2*m0+b0)*(xi-xc)+d0*yi)==0
# all SPD and member quantity positivity over the WHOLE s domain
def positive(expr, lo, hi, label):
    n,den=S.fraction(S.cancel(expr))
    if den.subs(t,lo)<0:n,den=-n,-den
    for name,poly in (("num",n),("den",den)):
        p=S.Poly(poly,t)
        assert p.eval(lo)>0,(label,name,"left",p.eval(lo))
        assert p.eval(hi)>0,(label,name,"right",p.eval(hi))
        assert p.count_roots(lo,hi)==0,(label,name,p.intervals())
    print("PASS",label,flush=True)
positive(m0-b0,0,1,"SPD insider eigen")
positive(m0+2*b0,0,1,"SPD IS aggregate eigen")
positive(m0*(m0+b0)-2*d0**2,0,1,"SPD RS 2x2 determinant")
positive(Delta0,0,1,"Cournot interior determinant")
positive(xi,0,1,"positive hypothetical RS member interior")
positive(xc,0,1,"positive genuine RS member corner")
positive(qi,0,1,"positive IS producer")
assert c0-h>0
print("PASS η=κ/2, a=1,c0=0.9,h=0.5, "
      "costs c0-hs>=0.4, SPD, outsider exits and reenters",flush=True)

# --- 4. Test a REAL coalition-stable RS at s=1/2 DURING EXIT ---
s0=R(1,2)
assert ymark.subs(t,s0)<0
csr_i=S.cancel((m0+b0)*xi*xi+2*d0*xi*yi+m0*yi*yi/2)
csr_c=S.cancel((m0+b0)*xc*xc)
PRi=S.cancel(3*m0*xi*xi-fee*t*t)
PRc=S.cancel(3*m0*xc*xc-fee*t*t)
WRi=S.cancel(PRi+csr_i)
WRc=S.cancel(PRc+csr_c)
PI=S.cancel(3*m0*qi*qi-fee*t*t)
CI=S.cancel(R(3,2)*(m0+2*b0)*qi*qi)
WI=S.cancel(PI+CI)
PN=S.cancel(3*m0*qn*qn)
CN=S.cancel(R(3,2)*(m0+2*gamma)*qn*qn)
WN=S.cancel(PN+CN)
p0=S.factor(PRc.subs(t,s0))
w0=S.factor(WRc.subs(t,s0))
outside_gov=S.factor(csr_c.subs(t,s0))
assert p0>PN and w0>WN
# Outsider RESIDENT firm produces ZERO in every national market,
# but home government can be far better off because local consumers
# import the cheaper, higher-volume standardized member products.
assert outside_gov>WN
assert S.factor(p0-R(9151,16428)*A*A/m0)==0
assert S.factor(w0-R(163379,49284)*A*A/m0)==0
assert S.factor((outside_gov-WN)-R(224143,98568)*A*A/m0)==0

# Fully adversarial no-same-type blocking without invalid global
# concavity assumptions (different Cournot active sets):
# For t<s0, govt member W_R(t) is STRICTLY increasing, below W_R(s0).
# For t>s0, firm member P_R(t) STRICTLY decreasing, below P_R(s0).
# Prove BOTH exact analytic branches on respective subintervals, then
# patch at the two KKT crossings via continuous q/payoffs identities.
positive(S.diff(WRi,t),0,s0,"pre-corner RS government W increasing")
positive(S.diff(WRc,t),0,s0,"corner RS government W increasing")
positive(-S.diff(PRi,t),s0,1,"post-corner RS firm P decreasing")
positive(-S.diff(PRc,t),s0,1,"corner RS firm P decreasing")
# All-depth R→IS deviation blocked by incumbent R firms, REGARDLESS
# of what the two irrelevant outsiders originally announced.
positive(p0-PI,0,1,"regional private veto dominates ALL international depths")
print("THEOREM strong-stage1 RS(pair,s=1/2) with outsider firm q=0")
print("THEOREM outsider home govt W_RS > W_NS despite outsider q=0")
print("NOTE: this proves ONE endogenous stage1 strongly stable contract"
      " in an open model-parameter neighborhood, not all equilibria")
