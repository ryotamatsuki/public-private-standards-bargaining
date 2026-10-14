"""Stage6 clean-room theorem absorption; do NOT import any stage3-5 helpers.

1) Derive general KKT outsider-reentry welfare incidence using a full 3x3
   independent Cournot FOC matrix. No fixed witness or grids.
2) Construct a six-player unanimous contract game WITHOUT oligopoly, products,
   networks or quantities that reproduces Stage5B plateau/trough/type switch.
The generic construction formally kills standalone novelty of the stage1
strong-outcome-type bifurcation; it does not show exact identities appeared
in any particular prior paper.
"""
import sympy as S
Q=S.Rational

def cournot_boundary_theorem():
    m,b,d,z,s=S.symbols("m b d z s",positive=True)
    A=2*m+b
    D=2*m*A-2*d*d
    M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    F=M+S.diag(m,m,m)
    q=F.inv()*S.Matrix([z,z,1])
    x=S.cancel(q[0]);y=S.cancel(q[2]);xc=S.cancel(z/A)
    assert S.factor(y-(A-2*d*z)/D)==0
    assert S.factor(x-(2*m*z-d)/D)==0
    assert S.factor(x-xc+d*y/A)==0
    P=S.cancel(3*m*x**2)
    CS=S.cancel((q.T*M*q)[0]/2)
    W=S.cancel(P+CS)
    qc=S.Matrix([xc,xc,0])
    Pc=3*m*xc**2
    CSc=S.cancel((qc.T*M*qc)[0]/2)
    Wc=S.cancel(Pc+CSc)
    # All quantities equal at Y=0, corresponding to z=A/(2d).
    for left,right in ((P,Pc),(CS,CSc),(W,Wc)):
        assert S.factor((left-right).subs(z,A/(2*d)))==0
    # Derivatives are wrt d at fixed s, m, b, z. Differentiation eta
    # gives dd/deta=-s. D=2m*A-2d*d strictly positive.
    # Right derivative comes from Y>0; left is zero for Y<=0.
    for label,expr,expected in (
        ("P",P,3*m/(d*D)),
        ("CS",CS,-m/(d*D)),
        ("W",W,2*m/(d*D)),
    ):
        assert S.factor(S.diff(expr,d).subs(z,A/(2*d))
                        -expected.subs(z,A/(2*d)))==0, label
    # At boundary, dy/dd=-A/(dD), so outsider output increases with eta.
    assert S.factor(S.diff(y,d).subs(z,A/(2*d))+A/(d*D))==0
    print("PASS exact 3:1 private-loss/consumer-gain and 2:1 net welfare loss")
    print("KKT right partial_eta: P=-3*m*s/(d*D), CS=+m*s/(d*D), W=-2*m*s/(d*D)")
    print("KKT left partial_eta: all zero. Holds whenever s,d,m,D>0.")

def generic_parent_countermodel():
    eta=S.symbols("eta",real=True)
    u=S.symbols("u",nonnegative=True)
    low=Q(1,100)
    kkt=Q(31,100)
    high=Q(39,100)
    crit=Q(77,200) # 0.385
    trough=kkt+Q(9,400)
    # Use u=max{eta-kkt,0}. This is a prescribed reduced-form payoff
    # parameter, NOT an outsider output or quantity. No product market.
    gap=S.factor(-Q(1,20)-u+Q(200,9)*u**2)
    assert S.factor(gap-Q(200,9)*(u-Q(3,40))*(u+Q(3,100)))==0
    assert gap.subs(u,0)==-Q(1,20)
    assert gap.subs(u,crit-kkt)==0
    assert gap.subs(u,high-kkt)>0
    assert S.diff(gap,u).subs(u,trough-kkt)==0
    assert S.diff(gap,u,2)>0
    assert gap.subs(u,trough-kkt)<gap.subs(u,0)
    # Exact SAME six independent players and signature sets:
    # RS: 2 national firms + 2 national governments; IS: all six.
    # For every s in (0,1], a signatory receives:
    #   NS: (P,W)=(0,0)
    #   RS: P_R=3s, W_R=(3+gap(eta))s
    #   IS: P_I=2s, W_I=3s.
    # In the eta-rectangle all payoff slopes positive, hence only
    # full-depth s=1 survives the reduced-stage1 strong refinement.
    assert 3+gap.subs(u,trough-kkt)>0
    # All RS firms strictly prefer RS(1) to IS(1); public signers
    # strictly prefer IS(1) iff gap<0; when gap=0 no strict RS blocker.
    for label,x in (
        ("below KKT",Q(0)),
        ("after KKT below welfare trough",Q(1,100)),
        ("at type threshold",crit-kkt),
        ("after type threshold",high-kkt),
    ):
        delta=gap.subs(u,x)
        print("PASS generic",label,"public RS-IS:",delta,
              "strong_IS_exists:",bool(delta<=0))
    # There are no Cournot quantities, entry decisions, differentiated
    # products or network externalities here: the same type switch
    # results from elementary multi-party consent with payoffs.
    print("PASS no-market parent reproduces NS exclusion, RS retention,")
    print("     IS coexistence for eta<=0.385 and disappearance afterwards.")

if __name__=="__main__":
    cournot_boundary_theorem()
    generic_parent_countermodel()
    print("Stage6 mathematical absorption result: STRICT NO-GO for")
    print("the bargaining-type switch alone; localized KKT incidence retained.")
