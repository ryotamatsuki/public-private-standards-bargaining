"""Stage 2: endogenous interoperability and design convergence under nested regulation.

New CHOICE variables c (compatibility, 0<=c<=1) and a (common product
design, 0<=a<=c), NOT new exogenous technology coefficients. The original
six primitive coordinates are unchanged. At a=c=s the old market and
phi*s**2 fee are EXACTLY recovered. Off the old diagonal we ASSUME
real development cost phi*(c*c+a*a)/2 (a new, testable structural choice).

Ghosh-Morita two-sided effect:
 b=gamma0+kappa*a-v*c (collaborator substitution increases in a),
 d=gamma0-eta*a (outsider substitution decreases in a).
 IF kappa>v, all-design, all-firm unification at c=a=1 gives the
 maximum pairwise substitute effect b in the triangle. Every IS pair
 has b; RS has only insider-insider b while insider-outsider is d.

Solve EXACTLY a two-stage *delegated* public standard / firm consortium
game at a rational witness:
 regulator chooses minimum design commonality L in [0,1];
 two private consortium members jointly choose c,a subject L<=a<=c<=1;
 Cournot firms then independently compete. The jointly funded private
 consortium maximizes identical net P_R; the public regulator maximizes
 participant national W_R. Legal implementation of a minimum FLOOR
 and costless open licensing are maintained institutional assumptions.

For fixed c, exact outsider KKT and SPD conditions are checked. For the
witness outsider ALWAYS active, so no illicit negative Cournot output.
Global c=1 strictly dominant for firm for EACH fixed a. Unique private
a_F≈.508035 and national regulator ideal a_G≈.561025, both INTERIOR:
private response a(L)=max{a_F,L} at c=1. Regulator chooses L=a_G.
Independent IS fully unified technology a=1 maximizes direct product
substitutability but BOTH firm and regulator prefer less restrictive
a=0 with c=1 (interface-only unity). NS, RS, IS matrices rederived.
"""
import sympy as S

R=S.Rational
c,a=S.symbols("c a",real=True)
v=R(1,100)
g=R(7,50)
k=R(1,50)
eta=R(13,100)
rho=R(8,25)
phi=R(7,50)
m=1-v
z=1+rho*c
b=g+k*a-v*c
d=g-eta*a
A=2*m+b
D=2*m*A-2*d*d
Y=A-2*d*z
M_R=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
M_I=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
M_N=S.Matrix([[m,g,g],[g,m,g],[g,g,m]])
qa=(M_R+S.diag(m,m,m)).inv()*S.Matrix([z,z,1])
qi=(M_I+S.diag(m,m,m)).inv()*S.Matrix([z,z,z])
qn=(M_N+S.diag(m,m,m)).inv()*S.ones(3,1)
qR=S.cancel(qa[0])
qO=S.cancel(qa[2])
qI=S.cancel(qi[0])
real_fee=phi*(c*c+a*a)/2
PN=S.cancel(3*m*qn[0]**2)
WN=S.cancel(PN+(qn.T*M_N*qn)[0]/2)
PR=S.cancel(3*m*qR*qR-real_fee)
WR=S.cancel(PR+(qa.T*M_R*qa)[0]/2)
PI=S.cancel(3*m*qI*qI-real_fee)
WI=S.cancel(PI+(qi.T*M_I*qi)[0]/2)
CSR=S.cancel(WR-PR)
CSI=S.cancel(WI-PI)

def sign_on_unit(expr,sgn=1,name=""):
    num,den=S.fraction(S.cancel(expr*sgn))
    if den.subs(a,0)<0:num,den=-num,-den
    for tag,piece in (("num",num),("den",den)):
        pp=S.Poly(piece,a)
        assert pp.eval(0)>0,(name,tag,"0",pp.eval(0))
        assert pp.eval(1)>0,(name,tag,"1",pp.eval(1))
        assert pp.count_roots(0,1)==0,(name,tag,"roots")
    print("PASS exact Sturm unit sign:",name,flush=True)

def unique_max(expr,name,left,right):
    deriv=S.cancel(S.diff(expr.subs(c,1),a))
    num,den=S.fraction(deriv)
    if den.subs(a,0)<0:num,den=-num,-den
    pp=S.Poly(num,a)
    assert S.factor(den.subs(a,0))>0
    assert S.Poly(den,a).count_roots(0,1)==0
    assert pp.count_roots(0,1)==1,(name,"multiple stationary points")
    assert pp.eval(0)>0 and pp.eval(1)<0
    assert pp.eval(left)>0 and pp.eval(right)<0
    root=next(x for x in S.nroots(pp,maxsteps=500)
              if abs(S.im(x))<R(1,100000000) and 0<float(S.re(x))<1)
    print("PASS",name,"unique global interior ideal",root,flush=True)
    return root

def verify_original_and_market():
    s=S.symbols("s",real=True)
    assert S.factor(b.subs({c:s,a:s})-(g+(k-v)*s))==0
    assert S.factor(d.subs({c:s,a:s})-(g-eta*s))==0
    assert S.factor(z.subs(c,s)-(1+rho*s))==0
    assert S.factor(real_fee.subs({c:s,a:s})-phi*s*s)==0
    assert S.factor(qO-Y/D)==0
    assert S.factor(qR-(2*m*z-d)/D)==0
    assert S.factor(qI-z/(2*(m+b)))==0
    assert S.factor(S.diff(b,a)-k)==0
    assert S.factor(S.diff(d,a)+eta)==0
    assert k>v>0
    # For the full triangular feasible set 0<=a<=c<=1:
    #   13/100<=b<=15/100; 1/100<=d<=14/100.
    BMIN,BMAX,DHI=R(13,100),R(15,100),R(14,100)
    assert m-BMAX>0
    assert m*(m+BMIN)-2*DHI*DHI>0 # SPD RS 2x2 Schur complement
    assert m+2*BMIN>0 and m+2*g>0
    # True outsider output ALWAYS active even at the most adverse bound.
    assert (2*m+BMIN)-2*DHI*(1+rho)>0
    assert z.subs(c,0)>0
    assert 0<g-eta and b.subs({c:1,a:1})==BMAX
    # Max of b for all a<=c: b<=g+(k-v)*c<=g+k-v.
    assert k-v>0
    print("PASS original-diagonal nesting, strict SPD & ACTIVE KKT on entire triangle")

def verify_general_two_channel_theorem():
    # An INDEPENDENT symbolic general-parameter check, not restricted
    # to the rational witness and not relying on sampled grids.
    mm,gg,kk,ee,vv,rr,ff=S.symbols("mm gg kk ee vv rr ff",positive=True)
    B=gg+kk*a-vv*c
    Dout=gg-ee*a
    Z=1+rr*c
    AA=2*mm+B
    DD=2*mm*AA-2*Dout*Dout
    YY=AA-2*Dout*Z
    xx=(2*mm*Z-Dout)/DD
    yy=YY/DD
    assert S.simplify(S.diff(YY,c)+vv+2*rr*Dout)==0
    assert S.simplify(S.diff(YY,a)-kk-2*ee*Z)==0
    assert S.simplify(DD*S.diff(xx,a)-
          (2*mm*ee*yy-(2*mm*kk+2*Dout*ee)*xx))==0
    # In the Y<=0 outsider-zero KKT regime, common design a brings
    # NO productivity gain z (which depends ONLY on c), and only
    # raises insider rivalry and real design expense.
    Pc=3*mm*(Z/AA)**2-ff*(c*c+a*a)/2
    assert S.simplify(S.diff(Pc,a)+
             6*mm*kk*Z*Z/AA**3+ff*a)==0
    print("PASS GENERAL: Y_c=-v-2*rho*d<0 and Y_a=kappa+2*eta*z>0",flush=True)
    print("PASS GENERAL: active insider design-profit tradeoff and corner P_a<0",flush=True)


def verify_endogenous_compatibility():
    # At every fixed design a, private consortium strictly raises c
    # whenever feasible a<=c<=1. Derive exactly x_c via FOC, then
    # lower bound c marginal net profit over full triangle.
    assert S.factor(S.diff(qR,c) - 2*m*(rho+v*qR)/D)==0
    Dmax=2*m*(2*m+g+k) # conservative strict upper bound
    Xmin=(2*m-g)/Dmax
    Xcmin=2*m*rho/Dmax
    assert 6*m*Xmin*Xcmin-phi>0
    # Verified numeric-free exact rational lower bound proves P_c>0.
    # For IS at a=0, q increases with c and marginal investment cost
    # cannot offset gain throughout c∈[0,1].
    Hmax=m+g+k
    qmin=1/(2*Hmax)
    qcmin=(rho*(m+g)+v)/(2*Hmax**2)
    assert 6*m*qmin*qcmin-phi>0
    print("PASS global private c*=1 for RS any a and IS at a=0")

def verify_nested_regulation():
    firm=unique_max(PR,"RS private a_F",R(508,1000),R(509,1000))
    govt=unique_max(WR,"RS government a_G",R(561,1000),R(562,1000))
    assert float(firm)<float(govt)
    # Firms strictly increase P until a_F and decrease afterwards:
    # firm best reply to public design floor L is a=max(a_F,L).
    # Government chooses L=a_G because W increases until a_G
    # and decreases afterwards and a_G>a_F.
    for tag,val in (("private",firm),("regulator",govt)):
        expr=PR if tag=="private" else WR
        print(tag,"optimized P",S.N(PR.subs({c:1,a:val}),12),
              "W",S.N(WR.subs({c:1,a:val}),12),flush=True)
    assert S.N(PR.subs({c:1,a:govt})-PN,15)>0
    assert S.N(WR.subs({c:1,a:govt})-WN,15)>0
    # Exact rational enclosure certifies participation independently of
    # numerical root printing: P,W increasing then decreasing only once,
    # and hG lies (.561,.562); both endpoint welfare/profit are > NS.
    for h in (R(561,1000),R(562,1000)):
        assert PR.subs({c:1,a:h})>PN
        assert WR.subs({c:1,a:h})>WN
    print("PASS nested SPNE: regulator floor L=a_G and firm chooses c=1,a=a_G")

def verify_full_unification_tradeoff():
    # In IS with c=1, all three pairs' b rises with common design a.
    # Private and public *both* prefer retaining product attributes
    # while standardizing interface: a=0 vs fully homogenizing a=1.
    sign_on_unit(S.diff(PI.subs(c,1),a),-1,"IS firm marginal cost of sameness")
    sign_on_unit(S.diff(WI.subs(c,1),a),-1,"IS govt marginal cost of sameness")
    assert PI.subs({c:1,a:0})>PI.subs({c:1,a:1})
    assert WI.subs({c:1,a:0})>WI.subs({c:1,a:1})
    assert WI.subs({c:1,a:0})>WR.subs({c:1,a:R(561,1000)})
    assert PI.subs({c:1,a:0})>PN
    assert S.factor(b.subs({c:1,a:1})-b.subs({c:1,a:0})-k)==0
    print("PASS full-design IS raises each of 3 substitution pairs and lowers")
    print("     both firm and national W relative to interface-only IS")
    for title,E in (("P_N",PN),("W_N",WN),
                    ("P_IS(c=1,a=0)",PI.subs({c:1,a:0})),
                    ("W_IS(c=1,a=0)",WI.subs({c:1,a:0})),
                    ("P_IS(c=1,a=1)",PI.subs({c:1,a:1})),
                    ("W_IS(c=1,a=1)",WI.subs({c:1,a:1}))):
        print(title,S.N(E,12),flush=True)

if __name__=="__main__":
    verify_original_and_market()
    verify_general_two_channel_theorem()
    verify_endogenous_compatibility()
    verify_nested_regulation()
    verify_full_unification_tradeoff()
    print("PASS Stage2 endogenous c,a plus nested govt minimum-design regulation.")
    print("NOT solved: all-national regulatory IS votes and private competing IP.")
