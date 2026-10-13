"""Endogenous interoperability s and endogenous product commonality z.
Full two-choice NS/RS/IS two-stage game: symbolic generic primitives and
global exact-rational proofs for a bounded symmetric parameter witness.

Do NOT confuse stage-1 strong Nash with ordinary/SPNE or certified novelty.
Do NOT interpret exogenous v as a strategically chosen parameter.
Run: python code/verify_two_choice_full_game.py  (sympy==1.14.0)
"""
import sympy as T
from fractions import Fraction as F
from math import comb

s,z=T.symbols("s z", real=True)
v,omega,kappa,eta,g,h,f,a,c0=T.symbols(
    "v omega kappa eta gamma0 h f a c0", real=True)
R=T.Rational
m=1-omega
A=a-c0
b=g+kappa*z-v*s
d=g-eta*z
D=2*m*(2*m+b)-2*d*d
x=T.factor((2*m*(A+h*z)-d*A)/D)
y=T.factor(((2*m+b)*A-2*d*(A+h*z))/D)
qi=T.factor((A+h*z)/(2*m+2*b))
qn=T.factor(A/(2*m+2*g))
fee=f*(s*s+z*z)/2
CSr=T.factor((m+b)*x*x+2*d*x*y+m*y*y/2)
CSi=T.factor(R(3,2)*(m+2*b)*qi*qi)
CSn=T.factor(R(3,2)*(m+2*g)*qn*qn)
PR=T.factor(3*m*x*x-fee);WR=T.factor(PR+CSr)
OR=T.factor(3*m*y*y);WO=T.factor(OR+CSr)
PI=T.factor(3*m*qi*qi-fee);WI=T.factor(PI+CSi)
PN=T.factor(3*m*qn*qn);WN=T.factor(PN+CSn)

# Exact nesting of previous stage-4 model on s=z AND omega=v:
u=T.symbols("u",real=True)
diag={s:u,z:u,omega:v}
mm=1-v
bb=g+(kappa-v)*u
dd=g-eta*u
Do=2*mm*(2*mm+bb)-2*dd**2
xo=(2*mm*(A+h*u)-dd*A)/Do
yo=((2*mm+bb)*A-2*dd*(A+h*u))/Do
assert T.factor(x.subs(diag)-xo)==0
assert T.factor(y.subs(diag)-yo)==0
assert T.factor(qi.subs(diag)-(A+h*u)/(2*mm+2*bb))==0
assert T.factor(fee.subs(diag)-f*u*u)==0

# Stage-2 Cournot consistency without parameter fixing:
MR=T.Matrix([[m,b,d],[b,m,d],[d,d,m]])
MI=T.Matrix([[m,b,b],[b,m,b],[b,b,m]])
MN=T.Matrix([[m,g,g],[g,m,g],[g,g,m]])
for mat,quant,cost in (
    (MR,T.Matrix([x,x,y]),T.Matrix([c0-h*z,c0-h*z,c0])),
    (MI,T.Matrix([qi]*3),T.Matrix([c0-h*z]*3)),
    (MN,T.Matrix([qn]*3),T.Matrix([c0]*3))
):
    rhs=a*T.ones(3,1)-cost
    assert all(T.factor(q)==0 for q in ((mat+m*T.eye(3))*quant-rhs))

# Each national market's consumer surplus + own firm global net profit.
assert T.factor(2*PR+OR+3*CSr-
   (3*(a*(2*x+y)-CSr-(c0-h*z)*2*x-c0*y)-2*fee))==0
assert T.factor(3*PI+3*CSi-
   (3*(a*3*qi-CSi-(c0-h*z)*3*qi)-3*fee))==0

PARAM={a:1,c0:R(1,5),h:R(1,5),f:R(1,5),g:R(1,4),
       kappa:R(3,20),eta:R(3,40),v:R(1,5),omega:R(1,5)}
fixed={name:T.factor(value.subs(PARAM)) for name,value in
       [("x",x),("y",y),("qi",qi),("qn",qn),
        ("PR",PR),("WR",WR),("OR",OR),("WO",WO),
        ("PI",PI),("WI",WI),("PN",PN),("WN",WN)]}
MATS=[("RS",MR.subs(PARAM)),("IS",MI.subs(PARAM)),("NS",MN.subs(PARAM))]

def bern_coeff(poly):
    p=T.Poly(T.expand(poly),s,z)
    ns,nz=p.degree_list()
    return [sum(p.coeff_monomial(s**i*z**j)*
                R(comb(a1,i),comb(ns,i))*R(comb(b1,j),comb(nz,j))
                for i in range(a1+1) for j in range(b1+1))
            for a1 in range(ns+1) for b1 in range(nz+1)]

def cert_positive(expr, tag, pieces=1):
    """EXACT certificate over (s,z)∈[0,1]^2, including both boundaries.
    Both numerator AND denominator have strictly positive tensor-product
    Bernstein coefficients in each of pieces² rational subrectangles.
    """
    num,den=T.fraction(T.cancel(expr))
    if den.subs({s:0,z:0})<0:num,den=-num,-den
    tested=0
    for label,p0 in (("num",num),("den",den)):
        for i in range(pieces):
            for j in range(pieces):
                piece=T.expand(p0.subs({s:(s+i)/pieces,z:(z+j)/pieces},
                                      simultaneous=True))
                vals=bern_coeff(piece)
                assert all(w>0 for w in vals),(tag,label,i,j,min(vals))
                tested+=len(vals)
    print("EXACT",tag,"proven positive",pieces,"x",pieces,
          "subrectangles; Bernstein coefficients tested",tested)

def direct_fraction(kind,ss,zz):
    """Clean-room 3×3 Cramer's allocation/payoff evaluator (no SymPy inverse)."""
    ss,zz=F(ss),F(zz)
    own=F(4,5);gg=F(1,4);kk=F(3,20);ee=F(3,40);vv=F(1,5)
    shared=gg+kk*zz-vv*ss
    off=gg-ee*zz
    fee=F(1,10)*(ss*ss+zz*zz)
    if kind=="RS":
        mat=[[own,shared,off],[shared,own,off],[off,off,own]]
        costs=[F(1,5)*(1-zz),F(1,5)*(1-zz),F(1,5)]
        members=2
    elif kind=="IS":
        mat=[[own,shared,shared],[shared,own,shared],[shared,shared,own]]
        costs=[F(1,5)*(1-zz)]*3
        members=3
    else:
        assert kind=="NS"
        mat=[[own,gg,gg],[gg,own,gg],[gg,gg,own]]
        costs=[F(1,5)]*3
        members=0
    sys=[[mat[i][j]+(own if i==j else 0) for j in range(3)]
         for i in range(3)]
    rhs=[1-c for c in costs]
    def det(M):
        (a0,b0,c),(d0,e0,f0),(g0,h0,i0)=M
        return a0*(e0*i0-f0*h0)-b0*(d0*i0-f0*g0)+c*(d0*h0-e0*g0)
    assert mat[0][0]>0 and mat[0][0]*mat[1][1]-mat[0][1]**2>0
    assert det(mat)>0
    d0=det(sys);q=[]
    for j in range(3):
        matj=[r[:] for r in sys]
        for i in range(3):matj[i][j]=rhs[i]
        q.append(det(matj)/d0)
    assert min(q)>0
    assert all(sum(sys[i][j]*q[j] for j in range(3))==rhs[i]
               for i in range(3))
    CS=sum(q[i]*mat[i][j]*q[j] for i in range(3) for j in range(3))/2
    P=[3*own*q[i]**2-(fee if i<members else F(0)) for i in range(3)]
    return q,CS,P,[p+CS for p in P]

def proof():
    for name,M in MATS:
        for i in (1,2,3):
            cert_positive(M[:i,:i].det(),name+" principal SPD "+str(i))
    for item in ("x","y","qi","qn"):
        cert_positive(fixed[item],item+" production positive")
    for label,expr in (
        ("RS govt W rising with commonality z",T.diff(fixed["WR"],z)),
        ("IS govt W rising with compatibility s",T.diff(fixed["WI"],s)),
        ("IS govt W rising with commonality z",T.diff(fixed["WI"],z)),
        ("IS1 govt W above all RS-member govts",
             fixed["WI"].subs({s:1,z:1})-fixed["WR"]),
        ("IS1 govt W above all RS-outsider govts",
             fixed["WI"].subs({s:1,z:1})-fixed["WO"]),
        ("RS(.714,1) firm P above all IS firm profits",
             fixed["PR"].subs({s:R(714,1000),z:1})-fixed["PI"]),
        ("RS(.6,1) firm P above all IS firm profits",
             fixed["PR"].subs({s:R(3,5),z:1})-fixed["PI"]),
    ):
        cert_positive(expr,label,4 if label.startswith("IS1 govt W above all RS-member") else 1)
    # Unique GLOBAL max of RS governmental W at (sG,1):
    cert_positive(-T.diff(fixed["WR"],s,2).subs(z,1),
                  "RS W(s,1) is strictly concave")
    lo,hi=R(713,1000),R(714,1000)
    assert T.diff(fixed["WR"],s).subs({s:lo,z:1})>0
    assert T.diff(fixed["WR"],s).subs({s:hi,z:1})<0
    # RS profit decreases in the narrow bracket; thus P(sG,1)>=P(.714,1).
    cert_positive(-T.diff(fixed["PR"],s).subs(
        {z:1,s:lo+(hi-lo)*s},simultaneous=True),
        "RS firm profit falling near govt maximum")
    assert fixed["PR"].subs({s:hi,z:1})>fixed["PN"]
    assert fixed["WR"].subs({s:lo,z:1})>fixed["WN"]
    assert fixed["PI"].subs({s:1,z:1})>fixed["PN"]
    assert fixed["WI"].subs({s:1,z:1})>fixed["WN"]
    assert fixed["WI"].subs({s:1,z:1})==R(17,20)
    # Direct payoff derivation independent of SymPy for many (s,z) combinations.
    for ss,zz in [(F(0),F(0)),(F(1,4),F(3,4)),
                  (F(3,5),F(1)),(F(3,4),F(1,2)),(F(1),F(1))]:
        at={s:R(ss.numerator,ss.denominator),
            z:R(zz.numerator,zz.denominator)}
        for kind in ("RS","IS","NS"):
            qs,cs,profits,gov=direct_fraction(kind,ss,zz)
            X=({ "RS":["x","x","y"],
                 "IS":["qi","qi","qi"],
                 "NS":["qn","qn","qn"] })[kind]
            PP=({ "RS":["PR","PR","OR"],
                  "IS":["PI","PI","PI"],
                  "NS":["PN","PN","PN"] })[kind]
            WW=({ "RS":["WR","WR","WO"],
                  "IS":["WI","WI","WI"],
                  "NS":["WN","WN","WN"] })[kind]
            for expected,arr in ((X,qs),(PP,profits),(WW,gov)):
                for label,value in zip(expected,arr):
                    assert fixed[label].subs(at)==R(value.numerator,value.denominator)
    print("C2: exact robust strong outcomes RS(sG,1) AND IS(1,1)")
    print("C3: matching firm-only stable type RS; matching government-only IS(1,1)")
    print("C4: RS government optimum depth sG strictly between .713 and .714")
    print("IS(1,1) govt W =",fixed["WI"].subs({s:1,z:1}))
    print("NOTE: firm-optimal pair (s,z) not symbolically isolated or globally unique.")
    print("NOTE: all admissible (v,omega,theta) regime partitions NOT solved.")
    print("NOTE: model is two-choice LQ stylization, not Salop microfoundation.")
if __name__=="__main__":proof()
