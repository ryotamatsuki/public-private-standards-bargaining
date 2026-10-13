"""Stage 6: nested-architecture absorption test for frozen Stage-4A economies.
Question: Does adding BOTH government + firm signatories select RS/IS outcomes
unavailable in either firm-only or govt-only consent game?
Independent exact SymPy formulas + unit-interval Sturm checks; no source mutation.
"""
import sympy as S
s=S.symbols("s",real=True)
R=S.Rational
g=R(1,4);kap=R(3,20);eta=kap/2;h=f=R(1,5);A=R(4,5)

def signs_positive(expr):
    n,d=map(S.factor,S.together(expr).as_numer_denom())
    if d.subs(s,0)<0:n,d=-n,-d
    for poly in (n,d):
        assert poly.subs(s,0)>0 and poly.subs(s,1)>0,(expr,poly)
        assert S.Poly(poly,s).count_roots(0,1)==0,(expr,poly)
    return True

def pay(v,structure):
    m=1-v
    b=g+(kap-v)*s
    d=g-eta*s
    if structure=="RS":
        Delta=2*m*(2*m+b)-2*d*d
        x=S.factor((2*m*(A+h*s)-d*A)/Delta)
        y=S.factor(((2*m+b)*A-2*d*(A+h*s))/Delta)
        cs=S.factor((m+b)*x*x+2*d*x*y+m*y*y/2)
        p=[S.factor(3*m*x*x-f*s*s)]*2+[S.factor(3*m*y*y)]
    elif structure=="IS":
        x=S.factor((A+h*s)/(2*m+2*b))
        cs=S.factor(R(3,2)*(m+2*b)*x*x)
        p=[S.factor(3*m*x*x-f*s*s)]*3
    else:
        assert structure=="NS"
        x=S.factor(A/(2*m+2*g))
        cs=S.factor(R(3,2)*(m+2*g)*x*x)
        p=[S.factor(3*m*x*x)]*3
    w=[S.factor(x+cs) for x in p]
    return {"P":p,"W":w}

def test_low():
    v=R(1,10);rs=pay(v,"RS");isin=pay(v,"IS");ns=pay(v,"NS")
    P,W=rs["P"][0],rs["W"][0]
    FP,FW=isin["P"][0],isin["W"][0]
    f0,f1=R(5319,10000),R(5320,10000)
    g0,g1=R(8249,10000),R(8250,10000)
    signs_positive(-S.diff(P,s,2))
    signs_positive(-S.diff(W,s,2))
    assert S.diff(P,s).subs(s,f0)>0>S.diff(P,s).subs(s,f1)
    assert S.diff(W,s).subs(s,g0)>0>S.diff(W,s).subs(s,g1)
    # A single firm-only or govt-only platform decision already selects the RS class.
    signs_positive(P.subs(s,R(1,2))-FP)
    signs_positive(W.subs(s,R(1,2))-FW)
    for obj,lo,hi in (("P",f0,f1),("W",g0,g1)):
        y=rs[obj][0]
        for bound in (lo,hi):
            assert y.subs(s,bound)>ns[obj][0]
    assert f1<g0
    print("v=0.10: firm-only RS(sF), govt-only RS(sG), joint RS(s in [sF,sG])")
    print("No coalition-structure change uniquely attributable to two-key consent.")
    print("Only accepted-depth set expands by standard (Pareto) interval logic.")

def test_high():
    v=R(3,10);rs=pay(v,"RS");isin=pay(v,"IS");ns=pay(v,"NS")
    for obj in ("P","W"):
        q=isin[obj][0]
        signs_positive(S.diff(q,s))
        for i in range(3):
            signs_positive(q.subs(s,1)-rs[obj][i])
        assert q.subs(s,1)>ns[obj][0]
    print("v=0.30: firm-only IS(1), govt-only IS(1), joint IS(1).")
    print("No independent mixed-rights effect on standard structure or depth.")

if __name__=="__main__":
    test_low();test_high()
    print("PASS Stage6 NESTED ABSORPTION: certified benchmark outcomes already")
    print("occur in firm-only and govt-only architectures.")
    print("Economic contribution from BOTH public/private vetoes NOT demonstrated.")
    print("This does NOT show the entire game is literally identical to prior paper.")
