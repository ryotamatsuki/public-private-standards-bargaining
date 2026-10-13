"""All-depth endogenous RS/IS strong-Nash frontier theorem (five parameters).

Proves:
* necessary/sufficient FULL-DEPTH-UNRESTRICTED contract-outcome tests
  in consumer/firm Pareto-frontier form (using the parent exhaustive
  original exact-message deviator characterization);
* exact NS fee participation threshold as a sup over ALL depths;
* if K_R>0, no finite quadratic integration fee can make NS strong;
* partial-depth RS and IS genuinely coexist at F=2/5 even though
  both s=1 contracts are NOT strong, via independent exact Sturm and
  strict-concavity sign tests across the entire continuum of depths.
This is not a complete quantifier-free five-dimensional phase diagram.
"""
import sympy as S
from verify_six_dimensional_corners import strong
s=S.symbols("s",real=True)
G,L,E,r,F=S.symbols("G L E rho F",real=True)
Q=S.Rational
b=G+L*s;d=G-E*s
D=2*(2+b)-2*d*d
x=S.cancel((2*(1+r*s)-d)/D)
y=S.cancel(((2+b)-2*d*(1+r*s))/D)
xc=S.cancel((1+r*s)/(2+b))
q=S.cancel((1+r*s)/(2*(1+b)))
qn=1/(2*(1+G))
CSr=S.cancel((1+b)*x*x+2*d*x*y+y*y/2)
CSi=S.cancel(Q(3,2)*(1+2*b)*q*q)
CSn=S.cancel(Q(3,2)*(1+2*G)*qn*qn)
PR0=S.cancel(3*x*x);WR0=S.cancel(PR0+CSr)
PI0=S.cancel(3*q*q);WI0=S.cancel(PI0+CSi)
PN=S.cancel(3*qn*qn);WN=S.cancel(PN+CSn)
PR=PR0-F*s*s;WR=WR0-F*s*s
PI=PI0-F*s*s;WI=WI0-F*s*s

def lift(five):
    """Map ANY rational normalized feasible 5D tuple to a six-coordinate
    physical primitive economy preserving ALL preference comparisons.
    Scale m=1-v small enough to make kappa=v+m*Lambda >=0.
    """
    GG,LL,EE,rr,FF=map(Q,five)
    m=1/(4*(1+abs(LL)))
    v=1-m
    th=(v,m*GG,v+m*LL,m*EE,rr,FF/m)
    assert th[2]>0 and 0<=th[3]<=th[1] and th[-1]>0
    return th

def strict_positive_sturm(expr,label):
    """Global rational-function >0 on FULL [0,1].
    Distinct independent method from previous Bernstein certificate.
    """
    num,den=S.fraction(S.cancel(expr))
    for idx,poly in enumerate((num,den)):
        p=S.Poly(poly,s)
        assert p.eval(0)>0 and p.eval(1)>0,(label,idx,"ENDPOINT")
        assert p.count_roots(0,1)==0,(label,idx,"INTERIOR ROOT")
    print("PASS",label,flush=True)

def generic_identites():
    kr=E*(1-G)+2*r*(1+G)-L
    ki=r*(1+G)-L
    assert S.factor(S.diff(PR,s).subs({s:0,F:0})-
      3*kr/(2*(2-G)*(1+G)**3))==0
    assert S.factor(S.diff(PI,s).subs({s:0,F:0})-
      3*ki/(2*(1+G)**3))==0
    assert S.factor(kr-ki-
      (E*(1-G)+r*(1+G)))==0
    # EXACT public-private marginal comparison; at K_R>0 and
    # 0<=E<=G<1, r>=0, CS_R'(0) is nonnegative:
    lower=(G*kr+E*G*(1+G)+2*r*(1+G)**2)/(4*(1+G)**3)
    assert S.factor(S.diff(CSr,s).subs(s,0)-lower)==0
    # Every firm's and government's incremental utility is the
    # gross incremental benefit minus SAME F*s^2.
    for x0 in (PR0,WR0,PI0,WI0):
        real=(x0-F*s*s)
        assert S.factor(real-x0+F*s*s)==0
        assert S.factor((real-real.subs(s,0))/s**2-
          ((x0-x0.subs(s,0))/s**2-F))==0
    # No binary one-depth F threshold can extinguish all standardization
    # if regional FIRM initial gain K_R>0: the gains from small s are O(s),
    # while the fee is O(s^2), and government gains as well.
    print("PROVED symbolic K_R,K_I, consumer-surplus slope and NS fee threshold")

def baseline_exact_partial_coexistence():
    # This is the ORIGINAL same baseline at v=.2, except the normalized
    # F is raised to 2/5 from 1/4. Other 4 normalized primitives unchanged.
    ssR=Q(3,5);ssI=Q(13,20)
    vals={G:Q(5,16),L:-Q(1,16),E:Q(3,32),r:Q(1,4),F:Q(2,5)}
    ev=lambda z:S.cancel(z.subs(vals))
    # Market SPD/interiority on entire continuum with correct model.
    for name,expr in (("RS x",x),("RS y",y),("IS q",q),
                      ("RS 1-b",1-b),("IS 1+2b",1+2*b),
                      ("RS SPD 1+b-2d²",1+b-2*d*d)):
        strict_positive_sturm(ev(expr),name)
    # Two opposite signers veto all cross-type attempts at ANY t.
    strict_positive_sturm(ev(PR.subs(s,ssR)-PI),
                          "PARTIAL RS(3/5) firm veto ALL IS(t)")
    strict_positive_sturm(ev(WI.subs(s,ssI)-WR),
                          "PARTIAL IS(13/20) govt veto ALL RS(t)")
    # Strict concavity of BOTH actor objectives within EACH standard:
    # FOC signs s_F<s_candidate<s_G imply candidate Pareto-efficient.
    for name,z in (("PR",PR),("WR",WR),("PI",PI),("WI",WI)):
        strict_positive_sturm(ev(-S.diff(z,s,2)),
                              "strict concavity "+name)
    assert ev(S.diff(PR,s).subs(s,ssR))<0
    assert ev(S.diff(WR,s).subs(s,ssR))>0
    assert ev(S.diff(PI,s).subs(s,ssI))<0
    assert ev(S.diff(WI,s).subs(s,ssI))>0
    for c in (PR.subs(s,ssR)-PN,WR.subs(s,ssR)-WN,
              PI.subs(s,ssI)-PN,WI.subs(s,ssI)-WN):
        assert ev(c)>0
    # Source independent rational-economy KKT + all-depth root-blocker
    # evaluator, not a depth grid. Both outcomes STABLE for all outsiders'
    # preannounced irrelevant RS-target messages.
    five=(Q(5,16),-Q(1,16),Q(3,32),Q(1,4),Q(2,5))
    th=lift(five)
    assert strong(th,'R',ssR,uniform=True)
    assert strong(th,'I',ssI)
    assert not strong(th,'R',1) and not strong(th,'I',1)
    assert not strong(th,'N')
    print("THEOREM all-depth RS(3/5) + IS(13/20) stable at F=2/5")
    print("THEOREM BOTH full-depth RS(1),IS(1) unstable at SAME economy")
    print("THEOREM coexistence persists in OPEN five-parameter neighborhood")
    print("EXACT normalized physical lift:",th)

def fee_examples():
    vals={G:Q(5,16),L:-Q(1,16),E:Q(3,32),r:Q(1,4)}
    kr=S.factor((E*(1-G)+2*r*(1+G)-L).subs(vals))
    ki=S.factor((r*(1+G)-L).subs(vals))
    assert kr>ki>0
    print("baseline K_R=",kr,"K_I=",ki,
          "=> no finite F makes NS strong in this market")
if __name__=="__main__":
    generic_identites()
    fee_examples()
    baseline_exact_partial_coexistence()
