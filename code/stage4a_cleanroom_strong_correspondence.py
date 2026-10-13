"""Stage 4A clean-room: entire reduced-stage1 strong-outcome SET at theta*.

Standalone Cournot from the FULL 3x3 first-order-condition matrix,
NOT from Stage3/Stage4 quantities or helper functions. Continuum claims are
rational Sturm certificates; algebraic endpoints bracketed exactly.

Claim is NOT overall strong Nash of stage2 quantities or novelty clearance.
"""
import sympy as S

t=S.symbols("t",real=True)
R=S.Rational


def certify_positive(expr, low, high, label):
    """Exact strict-sign certificate, including a possibly negative denominator."""
    n,d=S.fraction(S.cancel(expr))
    if S.simplify(d.subs(t,low))<0: n,d=-n,-d
    for name,poly in (("numerator",n),("denominator",d)):
        p=S.Poly(poly,t)
        assert p.eval(low)>0 and p.eval(high)>0,(label,name,"boundary")
        assert p.count_roots(low,high)==0,(label,name,"interior-root")
    print("PASS",label,flush=True)


def main():
    # Physical a=13, c0=12, h=10, f=140; normalized a-c0=1.
    m=R(7,10)
    gamma=R(3,5)
    b=gamma-R(1,5)*t
    d=gamma-R(11,20)*t
    z=1+10*t
    fee=140

    # Independently form the 3x3 representative-consumer utility Hessian
    # and Cournot best-response FOCs: (M+diag(M))q=z.
    M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    response=M+S.diag(m,m,m)
    outputs=response.inv()*S.Matrix([z,z,1])
    corner_two=(response[:2,:2]).inv()*S.Matrix([z,z])
    output_corner=S.Matrix([corner_two[0],corner_two[1],0])

    # Exact SPD for every s via 0 and 1 endpoints of the RS/IS restrictions.
    assert all(val>0 for val in
       (m-gamma,m+2*gamma,m-(gamma-R(1,5)),
        m+2*(gamma-R(1,5)),m*(m+gamma-R(1,5))-2*(gamma-R(11,20))**2))
    assert S.expand(outputs[0]-outputs[1])==0
    assert S.expand(output_corner[0]-output_corner[1])==0

    # Active set / KKT support recovered from the matrix, not assumed.
    # Numerator of outsider's product-market quantity is the CORRECTED Y.
    L=2*m*(2*m+b)-2*d*d
    Y=S.expand(2*m+b-2*d*z)
    assert S.factor(Y-(11*t*t-R(111,10)*t+R(4,5)))==0
    assert S.factor(outputs[2]-Y/L)==0
    assert S.factor(output_corner[0]-z/(2*m+b))==0
    assert S.factor(outputs[0]-(2*m*z-d)/L)==0
    lo,hi=S.solve(Y,t)
    assert lo==(111-S.sqrt(8801))/220
    assert hi==(111+S.sqrt(8801))/220
    assert 0<lo<R(2,25)<R(1,10)<R(93,100)<hi<1
    assert Y.subs(t,0)>0 and Y.subs(t,R(1,10))<0 and Y.subs(t,1)>0
    assert S.factor(1-2*d*output_corner[0]-Y/(2*m+b))==0
    assert m>d.subs(t,0)>0 and d.subs(t,1)>=0
    # Thus outsider is active on [0,lo) and (hi,1], corner on [lo,hi].
    # Insider margin z-d*y>0; demand SPD gives unique stage2 Cournot.

    # Firm total operating profit from its own Cournot FOC across 3 markets;
    # government = resident firm worldwide profit + domestic CS.
    def payoffs(q):
        P=S.cancel(3*m*q[0]**2-fee*t*t)
        CS=S.cancel((q.T*M*q)[0]/2)
        return P,S.cancel(P+CS)

    pA,wA=payoffs(outputs)
    pC,wC=payoffs(output_corner)

    # Separate 3x3 IS and NS Cournot systems, not inherited from RS.
    mIS=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    qIS=(mIS+S.diag(m,m,m)).inv()*S.Matrix([z,z,z])
    pI=S.cancel(3*m*qIS[0]**2-fee*t*t)
    wI=S.cancel(pI+(qIS.T*mIS*qIS)[0]/2)
    mNS=S.Matrix([[m,gamma,gamma],[gamma,m,gamma],[gamma,gamma,m]])
    qNS=(mNS+S.diag(m,m,m)).inv()*S.ones(3,1)
    pN=S.simplify(3*m*qNS[0]**2)
    wN=S.simplify(pN+(qNS.T*mNS*qNS)[0]/2)
    assert pN==R(105,338) and wN==R(495,676)

    # Agreement of payoffs at KKT switches (no spurious jump in levels).
    for root in (lo,hi):
        assert S.simplify((pA-pC).subs(t,root))==0
        assert S.simplify((wA-wC).subs(t,root))==0

    # Entire-depth monotonicity and global veto certificates.
    certify_positive(S.diff(pA,t), R(0),R(2,25),"RS firm rises up to exit")
    certify_positive(S.diff(wA,t), R(0),R(2,25),"RS government rises up to exit")
    certify_positive(-S.diff(pC,t),R(7,100),R(94,100),"RS firm falls on corner")
    certify_positive(-S.diff(pA,t),R(93,100),R(1),"RS firm falls after reentry")
    certify_positive(S.diff(wC,t),R(7,100),R(15,100),
                     "RS government rises through firm IR cutoff")
    certify_positive(R(1,2)-pI,R(0),R(1),"IS firm always below 1/2")
    certify_positive(R(7,4)-wI,R(0),R(1),"IS government always below 7/4")
    certify_positive(pN-pA,R(93,100),R(1),
                     "RS post-reentry firm below NS")

    pexit=S.simplify(pC.subs(t,lo))
    wexit=S.simplify(wC.subs(t,lo))
    assert pexit>R(1,2) and wexit>R(7,4)
    assert pexit>pN and wexit>wN

    # s_IR: the ONE positive crossing of private IR in the outsider-corner
    # interval; exact polynomial, rational isolating bracket (NO rounding test).
    eq=S.fraction(S.cancel(pC-pN))[0]
    assert S.Poly(eq,t).count_roots(R(7,100),R(94,100))==1
    lowcut,highcut=R(14429,100000),R(14430,100000)
    assert 0<lo<lowcut<highcut<hi
    assert S.simplify((pC-pN).subs(t,lowcut))>0
    assert S.simplify((pC-pN).subs(t,highcut))<0
    assert S.simplify((pC-pN).subs(t,hi))<0

    # Full strong-equilibrium OUTCOME correspondence at theta*:
    #   (a) NS: all SQ remains pure SPNE, but a joint deviation to RS(lo)
    #       makes all its FOUR signers strictly better;
    #   (b) IS(t): FOUR RS(lo) signers Pareto-improve, for EVERY t in (0,1];
    #   (c) RS(t<lo): FOUR resident signers Pareto-improve to RS(lo);
    #   (d) RS(t>s_IR): no pure SPNE due to P_R(t)<P_N;
    #   (e) for EACH RS(t) in [lo,s_IR], both govt+firm IR hold, and
    #       lower t' yields strictly lower incumbent W_R, whereas higher
    #       t' yields strictly lower incumbent P_R.
    #       RS contracts of OTHER pairs overlap in >=1 resident country.
    #       Every IS contract is blocked by incumbent govt W_R(t)>7/4>W_I.
    #       Thus ALL those RS outcomes are reduced-stage1 strong Nash.
    #       Remains valid if outsider preannounces any IS(t').
    assert S.simplify((pC-pN).subs(t,R(1,10)))>0
    assert S.simplify((wC-wN).subs(t,R(1,10)))>0
    assert S.simplify((wC-wexit).subs(t,R(1,10)))>0
    assert S.simplify((pexit-pC.subs(t,R(1,10))))>0

    print("PASS all stage4A cleanroom KKT, exact global signs and complete strong sets")
    print("Strong outcomes: RS(any pair,s),",lo,"<= s <= unique P_C(s)=P_NS root")
    print("s_exit =",S.N(lo,15),"s_IR in (",lowcut,",",highcut,")")
    print("Pexit =",S.N(pexit,12),"Wexit =",S.N(wexit,12))
    print("Not a unique negotiated depth; no reduced-stage1 strong NS or IS.")
    print("Stage6 novelty NO-GO preserved.")


if __name__=="__main__":
    main()
