"""Stage4A clean-room red-team: exact Cramer's Fraction payoff and Sturm positivity.
No production verifier import, no SymPy Matrix.inv(), no Bernstein certificates.
Includes an explicit regression against erroneous 'six beneficiaries' RS->IS lemma.
"""
from fractions import Fraction as F
import sympy as S

t=S.symbols("t", real=True)
PARAM=dict(g=F(1,4),k=F(3,20),eta=F(3,40),a=F(1),
           c=F(1,5),h=F(1,5),f=F(1,5))
def det(z):
    (a,b,c),(d,e,f),(g,h,i)=z
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
def direct(v,kind,depth,p=PARAM):
    v=F(v);depth=F(depth);m=1-v
    b=p["g"]+(p["k"]-v)*depth;d=p["g"]-p["eta"]*depth
    if kind=="RS":
        M=[[m,b,d],[b,m,d],[d,d,m]]
        costs=[p["c"]-p["h"]*depth]*2+[p["c"]];members=2
    elif kind=="IS":
        M=[[m,b,b],[b,m,b],[b,b,m]]
        costs=[p["c"]-p["h"]*depth]*3;members=3
    else:
        assert kind=="NS"
        M=[[m,p["g"],p["g"]],[p["g"],m,p["g"]],[p["g"],p["g"],m]]
        costs=[p["c"]]*3;members=0
    assert M[0][0]>0 and M[0][0]*M[1][1]-M[0][1]*M[1][0]>0
    assert det(M)>0
    B=[[M[i][j]+(m if i==j else 0) for j in range(3)] for i in range(3)]
    D=det(B);rhs=[p["a"]-ci for ci in costs]
    q=[]
    for j in range(3):
        copy=[row[:] for row in B]
        for i in range(3):copy[i][j]=rhs[i]
        q.append(det(copy)/D)
    assert all(z>0 for z in q)
    prices=[p["a"]-sum(M[i][j]*q[j] for j in range(3)) for i in range(3)]
    assert all(prices[i]-costs[i]==m*q[i] for i in range(3))
    CS=sum(q[i]*M[i][j]*q[j] for i in range(3) for j in range(3))/2
    P=[3*(prices[i]-costs[i])*q[i]-
       (p["f"]*depth*depth if i<members else F(0)) for i in range(3)]
    W=[u+CS for u in P]
    resource=3*(p["a"]*sum(q)-CS-sum(q[i]*costs[i] for i in range(3)))
    resource-=members*p["f"]*depth*depth
    assert sum(P)+3*CS==resource
    return dict(P=P,W=W,CS=CS,q=q)

def formulas(v,kind):
    v=S.Rational(v.numerator,v.denominator)
    m=1-v;g=S.Rational(1,4);k=S.Rational(3,20);e=k/2
    a=S.Integer(1);A=S.Rational(4,5);h=f=S.Rational(1,5)
    b=g+(k-v)*t;d=g-e*t
    if kind=="RS":
        D=2*m*(2*m+b)-2*d*d
        x=S.factor((2*m*(A+h*t)-d*A)/D)
        y=S.factor(((2*m+b)*A-2*d*(A+h*t))/D);num=2
    elif kind=="IS":
        x=y=S.factor((A+h*t)/(2*m+2*b));d=b;num=3
    else:
        assert kind=="NS"
        x=y=A/(2*m+2*g);b=d=g;num=0
    CS=S.factor((m+b)*x*x+2*d*x*y+m*y*y/2)
    P=[S.factor(3*m*q*q-(f*t*t if i<num else 0))
       for i,q in enumerate((x,x,y))]
    return dict(P=P,W=[S.factor(q+CS) for q in P],CS=CS,Q=(x,x,y))

def positive_on_unit(expr):
    """Sturm interval root proof, intentionally not upstream Bernstein argument."""
    numerator,denominator=map(S.factor,S.together(expr).as_numer_denom())
    if denominator.subs(t,0)<0:numerator,denominator=-numerator,-denominator
    assert all(z.subs(t,endpoint)>0 for z in (numerator,denominator)
               for endpoint in (0,1))
    assert S.Poly(numerator,t).count_roots(0,1)==0
    assert S.Poly(denominator,t).count_roots(0,1)==0

def compare_independently(v,kind,expr):
    for x in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        val=direct(v,kind,x)
        for category in ("P","W"):
            for i in range(3):
                rhs=val[category][i]
                assert S.factor(expr[category][i].subs(
                    t,S.Rational(x.numerator,x.denominator))-
                    S.Rational(rhs.numerator,rhs.denominator))==0

def global_continuation(v,kind,obj):
    """Independent all-depth Sturm SPD/interiority and exact Cournot FOCs."""
    vv=S.Rational(v.numerator,v.denominator)
    m=1-vv;g=S.Rational(1,4);k=S.Rational(3,20);eta=k/2
    b=g+(k-vv)*t;d=g-eta*t
    if kind=="RS":
        mat=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
        cost=S.Matrix([S.Rational(1,5)*(1-t),
                       S.Rational(1,5)*(1-t),S.Rational(1,5)])
    elif kind=="IS":
        mat=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
        cost=S.Matrix([S.Rational(1,5)*(1-t)]*3)
    else:
        assert kind=="NS"
        mat=S.Matrix([[m,g,g],[g,m,g],[g,g,m]])
        cost=S.Matrix([S.Rational(1,5)]*3)
    for j in (1,2,3):positive_on_unit(mat[:j,:j].det())
    q=S.Matrix(obj["Q"])
    for i in range(3):
        positive_on_unit(q[i])
        assert S.factor(((mat+m*S.eye(3))*q)[i]-(1-cost[i]))==0
    assert m>0 # independent firm quantity SOC = -2m <0

def reject_nonspd_stress():
    """Fail closed rather than extrapolate witness interior branch."""
    try:
        direct(F(9,10),"NS",F(0))
    except AssertionError:
        print("OUTSIDE DOMAIN correctly rejected: v=0.9 violates SPD")
        return
    raise AssertionError("Unexpectedly admitted non-SPD quantity game")

def low():
    v=F(1,10);rs,iss,ns=(formulas(v,x) for x in ("RS","IS","NS"))
    for kind,obj in (("RS",rs),("IS",iss),("NS",ns)):
        global_continuation(v,kind,obj)
        compare_independently(v,kind,obj)
    P,W=rs["P"][0],rs["W"][0];IP,IW=iss["P"][0],iss["W"][0]
    for fn in (P,W,IP,IW):positive_on_unit(-S.diff(fn,t,2))
    sf0,sf1=S.Rational(5319,10000),S.Rational(5320,10000)
    sg0,sg1=S.Rational(8249,10000),S.Rational(8250,10000)
    assert S.diff(P,t).subs(t,sf0)>0>S.diff(P,t).subs(t,sf1)
    assert S.diff(W,t).subs(t,sg0)>0>S.diff(W,t).subs(t,sg1)
    # Stronger than tangent approximation: polynomial upper comparison at ALL IS depths.
    for left,right in ((P,IP),(W,IW)):
        positive_on_unit(left.subs(t,S.Rational(1,2))-right)
    for endpoint in (sf0,sg1):
        positive_on_unit(P.subs(t,endpoint)-IP)
    for left,base in ((P,ns["P"][0]),(W,ns["W"][0])):
        assert min(left.subs(t,sf0),left.subs(t,sg1))>base
    print("LOW: all IS depths blocked by RS(1/2), RS Pareto interval strongly stable")

def high():
    v=F(3,10);rs,iss,ns=(formulas(v,x) for x in ("RS","IS","NS"))
    for kind,obj in (("RS",rs),("IS",iss),("NS",ns)):
        compare_independently(v,kind,obj)
    for kind in ("P","W"):
        good=iss[kind][0]
        positive_on_unit(S.diff(good,t))
        for i in range(3):positive_on_unit(good.subs(t,1)-rs[kind][i])
        assert good.subs(t,1)>ns[kind][0]
    assert iss["P"][0].subs(t,1)==S.Rational(397,640)
    assert iss["W"][0].subs(t,1)==S.Rational(1469,1280)
    print("HIGH: IS(1) globally dominates all RS roles/depths and NS")

def indifference_regression():
    """Six match signatures are NOT always six strictly improving deviators."""
    p=dict(g=F(7,50),k=F(1,4),eta=F(1,8),a=F(1),c=F(3,10),
           h=F(3,20),f=F(7,20))
    v=F(3,10);RS=direct(v,"RS",F(33,40),p)
    IS=direct(v,"IS",F(17,40),p)
    NS=direct(v,"NS",F(0),p)
    for objective in ("P","W"):
        for i in (0,1):
            assert RS[objective][i]>NS[objective][i]
            assert IS[objective][i]>RS[objective][i]
        assert IS[objective][2]<RS[objective][2]
    # Preexisting RS12: G1,F1,G2,F2 sign RS12(.825).
    # Uninvolved G3,F3 PREANNOUNCE IS(.425), causing no original payoff effect.
    # Four old RS signers move to IS(.425); nondeviating G3,F3 lose.
    # This is a valid *profitable 4-person coalition deviation* in the exact-name game.
    print("GENERAL RULE COUNTEREXAMPLE: RS→IS does not require six gains")
    print("ΔF/member=",float(IS["P"][0]-RS["P"][0]),
          "ΔG/member=",float(IS["W"][0]-RS["W"][0]))
    print("ΔF/outsider=",float(IS["P"][2]-RS["P"][2]),
          "ΔG/outsider=",float(IS["W"][2]-RS["W"][2]))

if __name__=="__main__":
    low();high();indifference_regression();reject_nonspd_stress()
    print("PASS: two exact witness contract outcome results survive; generic six-gains lemma REJECTED.")
