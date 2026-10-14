"""Institutional authority in source 3-country six-primitive standards model.

Three FIXED regimes hold the original Cournot/technology payoffs IDENTICAL:
M = two/three private signers only (voluntary consortium, NOT de facto adoption)
R = two/three public signers only (enforceable open-interface mandate)
J = both governments and firms (original exact-consent benchmark).

Exact continuous-depth reduced-stage1 strong-Nash TYPE comparison (M=RS,
R=IS, J=RS+IS) and a conditional, endogenous subsequent unanimous
government IS override are proved by rational Sturm/Bernstein certificates.

Government mandate assumes free legal implementability of the named open
interface, cost borne by the firm and firm exit option 0; we only certify
examples with P_firm>0. This is a different authority protocol, NOT a
proof governments can compel patent licensing or force loss-making output.
"""
from math import comb
import sympy as S
Q=S.Rational
s,v=S.symbols("s v",real=True)
g,k,e,rho,fee=Q(2,5),Q(3,20),Q(1,100),Q(13,2),Q(65,4)

def market(v,fee=fee):
    m=1-v; b=g+(k-v)*s; d=g-e*s; z=1+rho*s
    A=2*m+b; D=2*m*A-2*d*d
    M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    qA=(M+S.diag(m,m,m)).inv()*S.Matrix([z,z,1])
    qC=S.Matrix([z/A,z/A,0])
    MI=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    qI=(MI+S.diag(m,m,m)).inv()*S.Matrix([z,z,z])
    MN=S.Matrix([[m,g,g],[g,m,g],[g,g,m]])
    qN=(MN+S.diag(m,m,m)).inv()*S.ones(3,1)
    def pay(q,matrix,adopt=True):
        P=S.cancel(3*m*q[0]**2-(fee*s*s if adopt else 0))
        CS=S.cancel((q.T*matrix*q)[0]/2)
        return P,S.cancel(P+CS),CS
    PA,WA,CSA=pay(qA,M)
    PC,WC,CSC=pay(qC,M)
    PI,WI,CSI=pay(qI,MI)
    PN,WN,CSN=pay(qN,MN,False)
    OFa=S.cancel(3*m*qA[2]**2) # NONPARTICIPANT no standard cost
    OGa=S.cancel(OFa+CSA)
    return locals()

def positive_interval(expr,low=Q(0),high=Q(1)):
    num,den=S.fraction(S.cancel(expr))
    if den.subs(s,low)<0: num,den=-num,-den
    for part in (num,den):
        p=S.Poly(part,s)
        assert p.eval(low)>0 and p.eval(high)>0
        assert p.count_roots(low,high)==0

def positive_bivar(expr,label):
    """Exact strict tensor Bernstein positivity: s∈[0,1],v∈[.39,.41]."""
    p=S.Poly(S.expand(expr),s,v)
    n,m=p.degree_list()
    a,b=Q(39,100),Q(41,100)
    c=[[S.Integer(0) for j in range(m+1)] for i in range(n+1)]
    for (i,j),value in p.terms():
        for h in range(j+1):
            c[i][h]+=value*comb(j,h)*a**(j-h)*(b-a)**h
    minimum=None
    for i in range(n+1):
        for j in range(m+1):
            x=sum(c[ii][jj]*Q(comb(i,ii),comb(n,ii))*
                  Q(comb(j,jj),comb(m,jj))
                  for ii in range(i+1) for jj in range(j+1))
            assert x>0,(label,i,j,x)
            minimum=x if minimum is None else min(minimum,x)
    print("PASS bivariate",label,"coefficients",(n+1)*(m+1),
          "min",S.N(minimum,7),flush=True)

def certify():
    a=market(Q(41,100))
    assert Q(59,100)-Q(2,5)>0
    assert Q(59,100)*(Q(59,100)+Q(14,100))-2*Q(2,5)**2>0
    assert S.factor(a["qA"][2]-(a["A"]-2*a["d"]*a["z"])/a["D"])==0
    assert S.factor(1-2*a["d"]*a["qC"][0]-
                    (a["A"]-2*a["d"]*a["z"])/a["A"])==0
    assert (a["A"]-2*a["d"]*a["z"]).subs(s,0)>0
    assert (a["A"]-2*a["d"]*a["z"]).subs(s,1)==-Q(453,100)
    # Every member's payoff is strictly increasing in standard depth,
    # EVEN ACROSS both algebraic Cournot extensions; KKT branches join.
    for n in ("PA","WA","PC","WC","PI","WI"):
        positive_interval(S.diff(a[n],s))
        print("PASS increasing depth:",n,flush=True)
    at=lambda n:S.cancel(a[n].subs(s,1))
    pR,pI,wR,wI,pN,wN=[at(n) for n in
                           ("PC","PI","WC","WI","PN","WN")]
    outG=at("CSC");outF=Q(0)
    assert pR==Q(79165,1936)
    assert pI==Q(162310,5329)
    assert wR==Q(62395,968)
    assert wI==Q(2766605,42632)
    assert outG==Q(45625,1936)
    assert pR>pI>pN>0 and wI>wR>wN>0 and wI>outG
    assert pI>outF and pR>outF
    # Exact reduced-first-stage strong Nash OUTCOMES by signers:
    # M private RS survives, IS strictly blocked by RS pair;
    # R public IS survives, RS strictly blocked by IS ALL gov signers;
    # J government/firm cross-veto yields coexistence.
    # Any s<1 strictly Pareto dominated by its same-type s=1.
    print("PASS institutional comparative strong sets")
    print(" M: RS(any pair,1) | R: IS(1) | J: RS(any pair,1), IS(1)")
    # Separate participation example: same marketplace, higher real fee:
    # legal mandate still viable (P_IS>exit payoff 0), although firms
    # prefer NS and would not voluntarily sign IS.
    b=market(Q(2,5),Q(224,5))
    bt=lambda n:S.cancel(b[n].subs(s,1))
    assert (b["A"]-2*b["d"]*b["z"]).subs(s,1)<0
    assert bt("PI")==Q(1,5)
    assert bt("PN")==Q(9,20)
    assert bt("WI")==Q(679,20)
    assert bt("WN")==Q(39,40)
    assert 0<bt("PI")<bt("PN") and bt("WI")>bt("WN")
    print("PASS strict private veto but regulator implementation possible",
          "P_IS",bt("PI"),"P_NS",bt("PN"),flush=True)
    # Stage2 PRECONDITION for all first-stage voluntary RS(s) histories:
    # outsider govt W_RS_nonmember(s) < W_IS(1) UNIFORMLY.
    # Active and corner public outsider continuations independently.
    b=market(v)
    WI1=S.cancel(b["WI"].subs(s,1))
    for name,OG in (("active",b["OGa"]),("corner",b["CSC"])):
        t=S.cancel(WI1-OG)
        num,den=S.fraction(t)
        if den.subs({s:0,v:Q(2,5)})<0:num=-num
        positive_bivar(num,"G_outside_W_IS1_minus_RS_"+name)
    # Incumbent W_RS(s) <= W_RS(1) and strictly below W_IS(1)
    # at v=0.41; NS and every IS(s<1) also below W_IS(1).
    # Therefore in a subsequent unanimous 3-gov IS1 mandate vote,
    # all 3 govs strictly gain by overriding ANY M-market outcome,
    # except that overriding IS(1) is outcome equivalent.
    assert wI>wR and wI>outG and wI>wN
    print("PASS conditional postmarket government IS(1) override at v=.41")
    # Compare v=.39: incumbent govt strictly rejects IS(1) in favor
    # of a completed voluntary RS(1). A unanimous IS override fails.
    low=market(Q(39,100))
    assert low["WC"].subs(s,1)>low["WI"].subs(s,1)
    print("PASS completed voluntary RS blocks government IS(1) override at v=.39")
    print("CAVEAT: sequential govt stage evaluated with reduced-stage1 "
          "strong refinement; unanimous voting has coordination NE. "
          "Do not claim unique ordinary SPNE.")
if __name__=="__main__":
    certify()
