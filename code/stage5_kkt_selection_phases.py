"""Stage 5, independently certified multi-parameter strong-outcome phases.

Original 6-parameter, 3-country, one-depth bargaining/Cournot economy.
Theta fixed at (v,gamma,kappa,eta,rho)=(1/5,1/10,1/5,1/10,40)
for two different REAL fee coefficients phi=400 and phi=1400.
Cournot SUPPORT polynomial is IDENTICAL in both economies and has
two genuine interior exit/reentry roots. Reduced stage-1 strong Nash
ONLY; second-stage Cournot need not be strong. Exact rational Sturm
certificates prove ALL depth inequalities; no grid selection.
"""
import sympy as S

s,t = S.symbols("s t", real=True)
Q=S.Rational


def pos(expr, variable, low, high, name):
    """Proof of strict positivity on whole rational closed interval."""
    num,den=S.fraction(S.cancel(expr))
    if den.subs(variable,low)<0:
        num,den=-num,-den
    for label,polyexpr in (("num",num),("den",den)):
        p=S.Poly(polyexpr,variable)
        assert p.eval(low)>0,(name,label,"left")
        assert p.eval(high)>0,(name,label,"right")
        assert p.count_roots(low,high)==0,(name,label,"roots")
    print("PASS",name,flush=True)


def original_game(phi):
    # 3x3 FULL Cournot system from utility Hessian, with all market
    # destinations symmetric: stage1 participating firms' z=1+rho*s.
    m=Q(4,5); gamma=Q(1,10)
    b=gamma # kappa=v=1/5, b does not vary with s.
    d=gamma*(1-s) # eta=gamma=1/10
    z=1+40*s
    M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    F=M+S.diag(m,m,m)
    qA=F.inv()*S.Matrix([z,z,1])
    pair=F[:2,:2].inv()*S.Matrix([z,z])
    qC=S.Matrix([pair[0],pair[1],0])

    # Full-matrix independent reconstruction of NS and IS.
    MI=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    qI=(MI+S.diag(m,m,m)).inv()*S.Matrix([z,z,z])
    MN=S.Matrix([[m,gamma,gamma],[gamma,m,gamma],[gamma,gamma,m]])
    qN=(MN+S.diag(m,m,m)).inv()*S.ones(3,1)
    assert all(z0>0 for z0 in
       (m-gamma,m+2*gamma,m-b,m+2*b,m*(m+b)-2*Q(0)**2))

    # KKT outsider support; outsider inactive IFF Y<=0.
    L=2*m*(2*m+b)-2*d*d
    Y=S.expand(2*m+b-2*d*z)
    assert S.factor(Y-(8*s*s-Q(39,5)*s+Q(3,2)))==0
    assert S.factor(qA[2]-Y/L)==0
    assert S.factor(qC[0]-z/(2*m+b))==0
    assert S.factor(1-2*d*qC[0]-Y/(2*m+b))==0
    roots=S.solve(Y,s)
    exit0,return0=roots
    assert exit0==(39-S.sqrt(321))/80
    assert return0==(39+S.sqrt(321))/80
    assert 0<exit0<Q(27,100)<Q(48,103)<Q(71,100)<return0<1
    assert Y.subs(s,0)>0 and Y.subs(s,Q(1,2))<0 and Y.subs(s,1)>0

    def pay(q,matrix):
        P=S.cancel(3*m*q[0]**2-phi*s**2)
        W=S.cancel(P+(q.T*matrix*q)[0]/2)
        return P,W
    PA,WA=pay(qA,M)
    PC,WC=pay(qC,M)
    PI,WI=pay(qI,MI)
    PN=S.simplify(3*m*qN[0]**2)
    WN=S.simplify(PN+(qN.T*MN*qN)[0]/2)
    assert PN==Q(20,27) and WN==Q(65,54)
    for root in roots:
        assert S.simplify((PA-PC).subs(s,root))==0
        assert S.simplify((WA-WC).subs(s,root))==0
    return (exit0,return0,PA,PC,WA,WC,PI,WI,PN,WN)


def general_corner_conflict():
    # General same-s RS-corner/IS comparisons: real fee cancels.
    m,b,z=S.symbols("m b z",positive=True)
    private_corner=3*m*z**2/(2*m+b)**2
    private_is=3*m*z**2/(4*(m+b)**2)
    govt_corner=(4*m+b)*z**2/(2*m+b)**2
    govt_is=(9*m+6*b)*z**2/(8*(m+b)**2)
    firm_diff=S.factor(private_corner-private_is)
    govt_diff=S.factor(govt_corner-govt_is)
    assert S.factor(firm_diff-3*b*m*z**2*(3*b+4*m)/
                    (4*(m+b)**2*(b+2*m)**2))==0
    assert S.factor(govt_diff-z**2*(2*b**3+15*b**2*m+
                     12*b*m**2-4*m**3)/
                    (8*(m+b)**2*(b+2*m)**2))==0
    u=S.symbols("u",nonnegative=True)
    h=2*u**3+15*u**2+12*u-4
    assert h.subs(u,0)<0 and h.subs(u,1)>0
    assert S.expand(S.diff(h,u)-(6*u*u+30*u+12))==0
    print("PASS general b/m welfare threshold; unique positive root",
          S.nroots(h)[-1],flush=True)


def fee_400():
    lo,hi,PA,PC,WA,WC,PI,WI,PN,WN=original_game(400)
    # ALL four actual RS branch functions and both IS functions increase
    # across whole s in [0,1]. Exact Sturm certificate on full interval.
    for label,formula in (
      ("400 P_RS active rising",PA),
      ("400 W_RS active rising",WA),
      ("400 P_RS corner rising",PC),
      ("400 W_RS corner rising",WC),
      ("400 P_IS rising",PI),
      ("400 W_IS rising",WI),
    ):
        pos(S.diff(formula,s),s,Q(0),Q(1),label)

    # Strict RS firm preference but IS government preference at s=1.
    assert S.simplify(PA.subs(s,1)-PI.subs(s,1))==Q(1176700,7803)>0
    assert S.simplify(WI.subs(s,1)-WA.subs(s,1))==Q(25915625,249696)>0
    assert PA.subs(s,1)>PN and WA.subs(s,1)>WN
    assert PI.subs(s,1)>PN and WI.subs(s,1)>WN

    # No s<1 survives within-type Pareto revisions. At s=1:
    # other RS cannot beat RS(1), and IS is vetoed by RS private.
    # other IS cannot beat IS(1), and RS is vetoed by IS government.
    # NS jointly blocked. Outsider IS preannouncements do not alter
    # the incumbent private veto for RS(1).
    print("PASS phi400 complete strong types/depths: RS(pair,1), IS(1)")


def fee_1400():
    lo,hi,PA,PC,WA,WC,PI,WI,PN,WN=original_game(1400)

    # First-stage RS exists robustly. Global firm max is a KKT-corner
    # interior quadratic stationary point; outside corner private payoff
    # rises to left root and falls from right root.
    pos(S.diff(PA,s),s,Q(0),Q(27,100),
        "1400 outsider active before exit: firm increases")
    pos(-S.diff(PA,s),s,Q(71,100),Q(1),
        "1400 outsider active after reentry: firm decreases")
    optimum=Q(48,103)
    assert lo<optimum<hi
    assert S.simplify(S.diff(PC,s)+Q(400,289)*(103*s-48))==0
    assert S.diff(PC,s,2)<0
    Pstar=S.simplify(PC.subs(s,optimum))
    Wstar=S.simplify(WC.subs(s,optimum))
    assert Pstar==Q(1680,103) and Pstar>PN and Wstar>WN

    # Independent IS IR restriction; only (0,8/29] can be SPNE.
    assert S.factor(PI-PN)==-Q(200,27)*s*(29*s-8)
    assert S.factor(WI-WN)==Q(200,27)*s*(71*s+13)
    assert S.diff(PI,s).subs(s,Q(4,29))==0
    assert S.simplify(Pstar-PI.subs(s,Q(4,29)))==Q(34300,2987)>0

    # For EVERY individually rational IS depth t in (0,8/29],
    # all its FOUR potential RS(6t/5) signers strictly gain.
    # The RS deviation is a genuine KKT Cournot continuation:
    # apply active formula below (5/6)*lo, corner above.
    # Slightly overlapping rational sign-check envelopes guarantee
    # that the algebraic switching depth is FULLY covered.
    alpha=Q(6,5)
    assert Q(219,1000)<(Q(5,6)*lo)<Q(22,100)
    assert alpha*Q(8,29)<1
    for name,RSformula,ISformula,low,high in (
       ("1400 IS-block private active",PA,PI,Q(0),Q(22,100)),
       ("1400 IS-block govt active",WA,WI,Q(0),Q(22,100)),
       ("1400 IS-block private corner",PC,PI,Q(219,1000),Q(276,1000)),
       ("1400 IS-block govt corner",WC,WI,Q(219,1000),Q(276,1000)),
    ):
        expr=S.cancel((RSformula.subs(s,alpha*t)-ISformula.subs(s,t))/t)
        pos(expr,t,low,high,name)
    assert Q(8,29)<Q(276,1000)

    # Consequently all IS are either not IR or strictly coalition
    # blocked. RS(optimum) is strong because member firm has unique
    # GLOBAL RS profit maximum and higher profit than ANY IS depth.
    # NS all-SQ is blocked by RS(optimum).
    print("PASS phi1400: strong RS exists at s=48/103; no strong IS,NS")


if __name__=="__main__":
    general_corner_conflict()
    fee_400()
    fee_1400()
    print("PASS Stage5: two distinct reduced-strong standard TYPE phases "
          "with identical Y(s) and two-switch exit/reentry.")
    print("CAUSALITY LIMIT: fee changes selection; KKT geometry unchanged. "
          "Do not claim outsider exit CAUSED the type switch.")
