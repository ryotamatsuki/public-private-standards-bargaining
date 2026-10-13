"""Economically interpretable 5D government-vs-firm standardization conflict theorem.

One endogenous s; network v is EXOGENOUS.  Source game and exact all-six
signatures are unchanged. This is NOT a 5D exhaustive phase diagram.
Formal proof: general algebraic identities and exact rational Bernstein
global-dominance certificates over all s in [0,1] at a FIVE-DIMENSIONAL
open-parameter witness; cost-axis monotonicity and sharp local destabilization.
Requires sympy.
"""
import sympy as S
from math import comb
s=S.symbols("s",real=True)
g,l,e,r,F=S.symbols("G lambda delta rho F",real=True)
Q=S.Rational
b=g+l*s;d=g-e*s
D=2*(2+b)-2*d*d
x=S.factor((2*(1+r*s)-d)/D)
y=S.factor(((2+b)-2*d*(1+r*s))/D)
qi=S.factor((1+r*s)/(2*(1+b)))
qn=1/(2*(1+g))
CSR=S.factor((1+b)*x*x+2*d*x*y+y*y/2)
CSI=S.factor(Q(3,2)*(1+2*b)*qi*qi)
CSN=S.factor(Q(3,2)*(1+2*g)*qn*qn)
PR0=S.factor(3*x*x)
PI0=S.factor(3*qi*qi)
WR0=S.factor(PR0+CSR)
WI0=S.factor(PI0+CSI)
PN=S.factor(3*qn*qn);WN=S.factor(PN+CSN)
PR=PR0-F*s*s;PI=PI0-F*s*s
WR=WR0-F*s*s;WI=WI0-F*s*s

def bernstein_positive(expr):
    """Sufficient exact rational positivity certificate for all s∈[0,1]."""
    numer,denom=S.fraction(S.cancel(expr))
    if denom.subs(s,0)<0:numer,denom=-numer,-denom
    for label,poly in (("num",numer),("den",denom)):
        p=S.Poly(poly,s);n=p.degree()
        bs=[sum((p.nth(j)*Q(comb(k,j),comb(n,j))
                 for j in range(k+1)),S.Integer(0))
            for k in range(n+1)]
        assert all(x>0 for x in bs),(label,poly,bs)

def prove_generic():
    v,gamma,kappa,eta,h,A,f=S.symbols(
        "v gamma kappa eta h A f",real=True)
    m=1-v
    mu={g:gamma/m,l:(kappa-v)/m,e:eta/m,
        r:h/A,F:m*f/A**2}
    # Original physical market outputs q= A/m * normalized qhat
    # and firm/government payoffs = A^2/m * normalized payoffs.
    physical_b=gamma+(kappa-v)*s
    physical_d=gamma-eta*s
    physical_D=2*m*(2*m+physical_b)-2*physical_d**2
    physical_x=(2*m*(A+h*s)-physical_d*A)/physical_D
    physical_q=(A+h*s)/(2*(m+physical_b))
    assert S.factor(x.subs(mu)*A/m-physical_x)==0
    assert S.factor(qi.subs(mu)*A/m-physical_q)==0
    assert S.factor((PR.subs(mu))*A*A/m-
                    (3*m*physical_x**2-f*s*s))==0
    assert S.factor((PI.subs(mu))*A*A/m-
                    (3*m*physical_q**2-f*s*s))==0
    # F cancels EXACTLY when both options specify the SAME depth.
    assert S.factor((PR-PI).diff(F))==0
    assert S.factor((WR-WI).diff(F))==0
    # At the same s=1, private-vs-government conflict is therefore
    # independent of the real fixed expenditure F (for a COMMON depth).
    # But considering deviations to ANY other depth reintroduces F.
    t=S.symbols("t",real=True)
    assert S.factor(((PR.subs(s,1)-PI.subs(s,t)).diff(F))-(t*t-1))==0
    assert S.factor(((WI.subs(s,1)-WR.subs(s,t)).diff(F))-(t*t-1))==0
    assert S.factor(S.diff(WR,s)-S.diff(WR0,s)+2*F*s)==0
    assert S.factor(S.diff(WI,s)-S.diff(WI0,s)+2*F*s)==0
    assert S.factor(S.diff(PR,s)-S.diff(PR0,s)+2*F*s)==0
    # Private initial incentive thresholds independent of setup fee F.
    assert S.factor(S.diff(PI,s).subs(s,0)-
                    3*((1+g)*r-l)/(2*(1+g)**3))==0
    assert S.factor(S.diff(PR,s).subs(s,0)-
                    3*(e*(1-g)+2*(1+g)*r-l)/(2*(2-g)*(1+g)**3))==0
    print("PASS all-dimension normalization, private entry, depth-1 mismatch identities")

def prove_witness():
    # Original baseline a=1,c0=h=f=1/5,gamma=1/4,kappa=3/20,
    # eta=3/40,v=1/5 => m=4/5,A=4/5,F=m*f/A^2=1/4.
    vals={g:Q(5,16),l:-Q(1,16),e:Q(3,32),
          r:Q(1,4),F:Q(1,4)}
    def ev(expr):return S.factor(expr.subs(vals))
    for kind,z in (
      ("RS member q",x),("RS outsider q",y),("IS q",qi),
      ("RS SPD m-b",1-b),("RS SPD det",1+b-2*d*d),
      ("IS SPD 1+2b",1+2*b)
    ):bernstein_positive(ev(z));print("PASS",kind)
    assert ev((PR-PI).subs(s,1))>0
    assert ev((WI-WR).subs(s,1))>0
    for label,expr in [
      ("private RS(1)>IS(t) ALL depths",PR.subs(s,1)-PI),
      ("government IS(1)>RS(t) ALL depths",WI.subs(s,1)-WR),
      ("govt R increasing depth",S.diff(WR,s)),
      ("govt I increasing depth",S.diff(WI,s)),
    ]:
        bernstein_positive(ev(expr));print("PASS",label)
    for expr in (PR.subs(s,1)-PN,WR.subs(s,1)-WN,
                 PI.subs(s,1)-PN,WI.subs(s,1)-WN):
        assert ev(expr)>0
    # All certificates at F=1/4 extend AUTOMATICALLY to any 0<F<=1/4:
    # for t<1, full-depth advantage falls as F rises and government
    # derivative falls as F rises. Joining margins also fall as F rises.
    print("PROVED full-depth RS AND IS robust strong across all 0<F<=1/4")
    wr_cap=S.factor(S.diff(WR0,s).subs(s,1).subs(vals)/2)
    pr_cap=S.factor(S.diff(PR0,s).subs(s,1).subs(vals)/2)
    wi_cap=S.factor(S.diff(WI0,s).subs(s,1).subs(vals)/2)
    assert wr_cap==Q(310713952,1042430125)
    assert pr_cap==Q(226554624,1042430125)
    assert wi_cap==Q(39,128)
    assert pr_cap<wr_cap<wi_cap
    # For F>max(PR0'(1),WR0'(1))/2, lowering RS depth benefits
    # BOTH old member firms and member governments (strict derivative).
    # Hence matched RS(1) cannot be strong Nash even when firm/government
    # rankings of RS(1) vs IS(1) are UNCHANGED.
    print("EXACT fee destabilization cutoff for full-depth RS:",
          wr_cap,"=",float(wr_cap))
    print("WARNING: RS with s<1 may remain strongly stable above cutoff")
    print("WARNING: results do NOT classify all depths across all parameters")
if __name__=="__main__":
    prove_generic()
    prove_witness()
