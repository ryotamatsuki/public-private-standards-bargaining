"""Applied-theory track: network effects, product differentiation and standards bargaining.

Original theta=(v,gamma0,kappa,eta,rho,phi), one endogenous RS/IS
standardization depth s. Exact symbolic calculations certify:
  P1. Network/outsider-differentiation Cournot support cutoff.
  P2. Firm vs government same-depth RS/IS preference in the KKT corner.
  P3. Common-fee participation-veto / consumer-surplus identity.
  P4. Full REDUCED-STAGE1 strong-standard correspondence on v in
      [39/100,41/100] holding (gamma0,kappa,eta,rho,phi) fixed.
No new primitive, no invented institution, no stage-2 strong Nash,
no publication novelty claim. The entire s x v rectangle is audited.
"""
import math
import sympy as S

s,v,e,r,g,k,m,b,z=S.symbols("s v e r g k m b z",real=True)
Q=S.Rational

def bernstein_positive(poly,label):
    """Exact strict positive tensor Bernstein coeffs on [0,1] x [0.39,0.41]."""
    p=S.Poly(S.expand(poly),s,v)
    nx,ny=p.degree_list()
    y0,y1=Q(39,100),Q(41,100)
    power=[[S.Integer(0) for _ in range(ny+1)] for _ in range(nx+1)]
    # Substitute (s,v)=(u, y0 + (y1-y0)w); ordinary power coeffs
    for (i,j),c in p.terms():
        for h in range(j+1):
            power[i][h]+=c*math.comb(j,h)*y0**(j-h)*(y1-y0)**h
    positive_count=0
    for i in range(nx+1):
        for j in range(ny+1):
            coef=sum(power[h][l]*Q(math.comb(i,h),math.comb(nx,h))*
                     Q(math.comb(j,l),math.comb(ny,l))
                     for h in range(i+1) for l in range(j+1))
            assert coef>0,(label,i,j,coef)
            positive_count+=1
    print("PASS exact continuum Bernstein",label,"positive coefficients",positive_count,flush=True)


def positive_on_v(expr,label):
    """Exact Sturm test on the CLOSED network interval."""
    n,h=S.fraction(S.cancel(expr))
    if h.subs(v,Q(39,100))<0: n,h=-n,-h
    for tag,p in (("numerator",n),("denominator",h)):
        poly=S.Poly(p,v)
        assert poly.eval(Q(39,100))>0,(label,tag,"low")
        assert poly.eval(Q(41,100))>0,(label,tag,"high")
        assert poly.count_roots(Q(39,100),Q(41,100))==0,(label,tag,"roots")
    print("PASS exact v-continuum",label,flush=True)


def proposition_one_outsider_support():
    Y=S.expand(2*(1-v)+g+(k-v)*s-2*(g-e*s)*(1+r*s))
    assert S.expand(S.diff(Y,v)+(2+s))==0
    assert S.expand(S.diff(Y,e)-2*s*(1+r*s))==0
    assert S.expand(S.diff(Y,r)+2*s*(g-e*s))==0
    vc=S.solve(Y,v)[0]
    assert S.factor(vc-(2-g+(k-2*g*r)*s+2*e*s*(1+r*s))/(s+2))==0
    assert S.simplify(S.diff(vc,e)-2*s*(1+r*s)/(2+s))==0
    assert S.simplify(S.diff(vc,r)+2*s*(g-e*s)/(2+s))==0
    # all thresholds are conditional on market admissibility, v<1,
    # substitution and positive definite demand at each evaluated theta
    print("PASS P1 exact network-exclusion and differentiation-reentry slopes")


def proposition_two_preference():
    m,b,z=S.symbols("m b z",positive=True)
    xC=z/(2*m+b)
    qI=z/(2*(m+b))
    pc=3*m*xC*xC
    pi=3*m*qI*qI
    wc=(4*m+b)*xC*xC
    wi=(Q(9,2)*m+3*b)*qI*qI
    assert S.simplify((pc-pi)-3*b*m*z*z*(3*b+4*m)/
                      (4*(m+b)**2*(2*m+b)**2))==0
    F=2*b**3+15*b*b*m+12*b*m*m-4*m**3
    assert S.simplify((wc-wi)-z*z*F/
                      (8*(m+b)**2*(2*m+b)**2))==0
    u=S.symbols("u",positive=True)
    f=2*u**3+15*u*u+12*u-4
    assert S.diff(f,u).subs(u,0)>0 and S.diff(f,u,2)>0
    assert f.subs(u,Q(251,1000))<0 and f.subs(u,Q(252,1000))>0
    assert S.factor((g+(k-v)*s)/(1-v)).subs(v,Q(39,100))!=0
    assert S.simplify(S.diff((g+(k-v)*s)/(1-v),v)
                      -(g+k*s-s)/(1-v)**2)==0
    print("PASS P2 exact public/private preference and unique critical b/m")


def parameter_model():
    gamma,kappa,eta,rho,phi=Q(2,5),Q(3,20),Q(1,100),Q(13,2),Q(65,4)
    m=1-v
    b=gamma+(kappa-v)*s
    d=gamma-eta*s
    z=1+rho*s
    A=2*m+b
    D=2*m*A-2*d*d
    Y=S.cancel(A-2*d*z)
    xA=S.cancel((2*m*z-d)/D)
    yA=S.cancel(Y/D)
    xC=S.cancel(z/A)
    qI=S.cancel(z/(2*(m+b)))
    # Exact accounting from worldwide resident firm + destination CS.
    def getp(q):
        return S.cancel(3*m*q*q-phi*s*s)
    PA=getp(xA)
    PC=getp(xC)
    PI=getp(qI)
    WA=S.cancel(PA+(m+b)*xA*xA+2*d*xA*yA+m*yA*yA/2)
    WC=S.cancel(PC+(m+b)*xC*xC)
    WI=S.cancel(PI+Q(3,2)*(m+2*b)*qI*qI)
    qN=S.cancel(1/(2*(m+gamma)))
    PN=S.cancel(3*m*qN*qN)
    WN=S.cancel(PN+Q(3,2)*(m+2*gamma)*qN*qN)
    # M_RS eigenvalue m-b, remaining Schur m(m+b)-2d^2.
    # Uniform rational LOWER BOUNDS on rectangle s∈[0,1],v∈[.39,.41].
    # m>=.59; .14<=b<=.4; .39<=d<=.4.
    assert Q(59,100)-Q(2,5)>0 # m-b>0
    assert Q(59,100)*(Q(59,100)+Q(14,100))-2*Q(2,5)**2>0
    assert S.factor(xA-(xC-d*yA/A))==0
    assert S.factor(1-2*d*xC-Y/A)==0 # outsider complementarity condition
    return locals()


def proposition_three_veto(data):
    # At fixed s, same real fee is paid by both government and firm.
    phi=Q(65,4)
    PN,WN=data["PN"],data["WN"]
    for name in ("A","C","I"):
        P,W=data["P"+name],data["W"+name]
        TP=S.cancel((P+phi*s*s-PN)/s**2)
        TG=S.cancel((W+phi*s*s-WN)/s**2)
        cs=S.cancel(W-P)
        csn=S.cancel(WN-PN)
        assert S.simplify((TG-TP)-(cs-csn)/s**2)==0
    print("PASS P3 consumer-surplus sign identifies binding IR/veto fee cap")


def proposition_four_network_paradox(data):
    # All actual KKT curves + IS are monotone in s, UNIFORMLY in v.
    # Endpoint-by-endpoint checks alone are NOT used.
    m,b,A,D=data["m"],data["b"],data["A"],data["D"]
    for name,refden in (("PA",D),("WA",D),("PC",A),("WC",A),
                        ("PI",m+b),("WI",m+b)):
        deriv=S.cancel(S.diff(data[name],s))
        numerator,denominator=S.fraction(deriv)
        factor=S.cancel(denominator/refden**3)
        assert not factor.free_symbols and factor<0,(name,"denominator sign",factor)
        bernstein_positive(-numerator,name+" depth marginal")
    # Entire v rectangle has outsider-zero at s=1; no ghost negative q.
    Y=data["Y"]
    assert S.factor(Y.subs(s,1) + 3*v +Q(33,10))==0
    assert Y.subs({s:1,v:Q(39,100)})<0
    assert Y.subs({s:1,v:Q(41,100)})<0
    # outsider positive before boundary; there is a true interior exit
    assert Y.subs({s:0,v:Q(41,100)})>0
    # Uniform IR of both formats at s=1, regardless of v.
    for name in ["PC","WC","PI","WI"]:
        baseline=data["PN"] if name.startswith("P") else data["WN"]
        positive_on_v(S.cancel(data[name].subs(s,1)-baseline.subs(s,1)),
                      name+" full-depth IR")
    # Firms always prefer RS to IS on outsider-zero branch, b>0;
    # government has a single crossing in v because u decreases.
    u=S.cancel(b/m).subs(s,1)
    f=lambda uu:2*uu**3+15*uu**2+12*uu-4
    assert S.simplify(u.subs(v,Q(39,100))-Q(16,61))==0
    assert S.simplify(u.subs(v,Q(41,100))-Q(14,59))==0
    assert f(Q(16,61))>0 and f(Q(14,59))<0
    assert S.simplify(S.diff(u,v)+Q(9,20)/(1-v)**2)==0
    assert S.simplify((data["PC"]-data["PI"]).subs(s,1).subs(v,Q(39,100)))>0
    assert S.simplify((data["PC"]-data["PI"]).subs(s,1).subs(v,Q(41,100)))>0
    assert S.simplify((data["WC"]-data["WI"]).subs(s,1).subs(v,Q(39,100)))>0
    assert S.simplify((data["WC"]-data["WI"]).subs(s,1).subs(v,Q(41,100)))<0
    # The monotone ratio u(v) gives a UNIQUE v* in (.39,.41).
    # Reduced-stage1 exact-signature strong-Nash OUTCOME correspondence:
    # v < v*: only RS(any pair,1); v>=v*: RS(any pair,1), IS(1).
    # At v*, govt indifference, so no strictly improving RS deviation
    # from IS. Firm always strictly favors RS. NS blocked by RS(1).
    for vv in (Q(39,100),Q(41,100)):
        print("exact witness",vv,"Y1",Y.subs({s:1,v:vv}),
              "P_RS",S.N(data["PC"].subs({s:1,v:vv}),10),
              "P_IS",S.N(data["PI"].subs({s:1,v:vv}),10),
              "W_RS",S.N(data["WC"].subs({s:1,v:vv}),10),
              "W_IS",S.N(data["WI"].subs({s:1,v:vv}),10),flush=True)
    print("PASS P4 entire v∈[.39,.41]: RS-only below v* and RS+IS above v*")


if __name__=="__main__":
    proposition_one_outsider_support()
    proposition_two_preference()
    data=parameter_model()
    proposition_three_veto(data)
    proposition_four_network_paradox(data)
    print("PASS applied-theory propositions P1–P4. Stage6 standalone-novelty NO-GO retained.")
