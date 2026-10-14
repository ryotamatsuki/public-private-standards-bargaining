"""Stage 1: a genuinely solved sequential firm-development/public-standard game.

The six physical primitives are unchanged. The NEW protocol is NOT equivalent
to the old all-six simultaneous message game. Here at s=1 only:
 F1 proposes no development, bilateral R12, or international I123;
 F2 accepts/rejects its invited technology contract; F3 additionally votes
 on I123; if rejected, NS occurs. R12 and I123 are real investments with
 a per-operating-firm cost phi*s^2, not a royalty.
 After a private R12 is developed, 3 GOVERNMENTS vote sequentially G1,G2,G3
 to certify and MANDATE the already-developed OPEN interface nationally.
 Unanimous YES offers firm3 a real post-mandate compliance/exit choice:
 compliance leads to exactly the IS network-compatible 3x3 Cournot game,
 real adoption cost paid ONCE by firm3; refusal leads to 2-firm R12
 activity and outsider exit=0. All other incumbents earn positive compliant
 profit, so continued production is optimal in the considered interval.
 No developed technology => government cannot certify it.
 CANNOT enforce patented technologies without an open implementability
 license; no independent de facto standard diffusion or continuous depth.

All subgames are solved by strict backward induction, not stage-one strong
Nash. At v=.39 on-path R12; at v=.41 on-path universal I123, even though
private firms would prefer unconstrained R12. No claim that the proposal or
off-path votes are unique, or that the government agenda is endogenous.
"""
import sympy as S
R=S.Rational
v=S.symbols("v",real=True)
lo,hi=R(39,100),R(41,100)
g,k,eta,rho,phi=R(2,5),R(3,20),R(1,100),R(13,2),R(65,4)

def original_market():
    m=1-v
    b=g+(k-v)           # s=1
    d=g-eta             # s=1
    z=1+rho             # s=1
    MR=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    MI=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    MN=S.Matrix([[m,g,g],[g,m,g],[g,g,m]])
    qr_all=(MR+S.diag(m,m,m)).inv()*S.Matrix([z,z,1])
    Y=S.factor(2*m+b-2*d*z)
    D=S.factor(2*m*(2*m+b)-2*d*d)
    assert S.factor(qr_all[2]-Y/D)==0
    assert S.factor(Y+R(33,10)+3*v)==0
    assert Y.subs(v,lo)<0 and Y.subs(v,hi)<0
    # Actual RS equilibrium must use outsider=0 KKT, not negative FOC.
    xR=z/(2*m+b)
    qr=S.Matrix([xR,xR,0])
    assert S.simplify(1-2*d*xR-Y/(2*m+b))==0
    qi=(MI+S.diag(m,m,m)).inv()*S.Matrix([z,z,z])
    qn=(MN+S.diag(m,m,m)).inv()*S.ones(3,1)
    def payoff(q,M,developers):
        cs=S.factor((q.T*M*q)[0]/2)
        ps=tuple(S.factor(3*m*q[i]**2-(phi if developers[i] else 0))
                 for i in range(3))
        ws=tuple(S.factor(p+cs) for p in ps)
        return dict(q=q,cs=cs,ps=ps,ws=ws)
    N=payoff(qn,MN,(0,0,0))
    RS=payoff(qr,MR,(1,1,0))
    IS=payoff(qi,MI,(1,1,1))
    return locals()

def exact_interval_positive(expr,name):
    n,d=S.fraction(S.cancel(expr))
    if d.subs(v,lo)<0:n,d=-n,-d
    for typ,piece in [("numerator",n),("denominator",d)]:
        p=S.Poly(piece,v)
        assert p.eval(lo)>0,(name,typ,"lower")
        assert p.eval(hi)>0,(name,typ,"upper")
        assert p.count_roots(lo,hi)==0,(name,typ,"root")
    print("PASS full v-interval",name,flush=True)

def audit_all_parameter_cases(model):
    N,RS,IS=model["N"],model["RS"],model["IS"]
    m,b,d=model["m"],model["b"],model["d"]
    # all 3 matrices SPD throughout the interval; substitute products:
    assert 1-hi>g>0
    assert b.subs(v,hi)>0
    assert (m-b).subs(v,hi)>0
    assert (m*(m+b)-2*d*d).subs(v,hi)>0
    assert d>0
    for name,expr in {
        "RS incumbent net profitability":RS["ps"][0],
        "IS all-firm net profitability":IS["ps"][0],
        "F2 accepts R even if later overridden":IS["ps"][1]-N["ps"][1],
        "F3 accepts I voluntarily":IS["ps"][2]-N["ps"][2],
        "private preference R over I":RS["ps"][0]-IS["ps"][0],
        "G outsider supports open IS mandate":IS["ws"][2]-RS["ws"][2],
        "G welfare IS beats NS":IS["ws"][0]-N["ws"][0],
        "G welfare R beats NS":RS["ws"][0]-N["ws"][0],
        "WORLD summed national W IS beats R":
            3*IS["ws"][0]-sum(RS["ws"]),
    }.items():
        exact_interval_positive(expr,name)
    # Network-effect threshold for INCUMBENT government support,
    # not assumed away. This is the true public-v-private wedge.
    u=S.factor(b/m)
    F=2*u**3+15*u*u+12*u-4
    assert S.factor(u-(R(11,20)-v)/(1-v))==0
    assert S.simplify(S.diff(u,v)+R(9,20)/(1-v)**2)==0
    assert F.subs(v,lo)>0 and F.subs(v,hi)<0
    n,_=S.fraction(S.factor(F))
    assert S.Poly(n,v).count_roots(lo,hi)==1
    assert S.factor(RS["ws"][0]-IS["ws"][0])/(S.factor(F)) !=0
    # More strongly, full symbolic identity govt wedge pref ratio:
    m,b,z=model["m"],model["b"],model["z"]
    wedge=z*z*(2*b**3+15*b*b*m+12*b*m*m-4*m**3)/(8*(m+b)**2*(2*m+b)**2)
    assert S.factor(RS["ws"][0]-IS["ws"][0]-wedge)==0
    print("PASS unique support-switch v* via u=(.55-v)/(1-v), root of 2u^3+15u^2+12u-4")

def subgame_backward(vval,model):
    """Complete on-path backward induction; off-path continuation as defined.

    G1,G2,G3 cast OPEN sequential votes when market R is known.
    Distinct government winners imply a unique yes/no POLICY OUTCOME.
    Firms play F1 proposal -> F2 acceptance -> (if I) F3 acceptance,
    then G1,G2,G3 and firm's compliance choice. All continuation games
    are strict at the two witness v's except F1's R/I tie at .41.
    """
    x={}
    for typ in ("N","RS","IS"):
        y=model[typ]
        x[typ]={key:(tuple(S.simplify(val.subs(v,vval)) for val in arr)
                     if isinstance(arr,tuple) else
                     S.simplify(arr.subs(v,vval)))
                 for key,arr in y.items() if key in ("ps","ws","cs")}
    # Compliance decision of initially EXCLUDED F3 under policy mandate:
    # join payoff from the 3x3 IS Cournot equilibrium or legally permitted
    # outside option 0. F1/F2 have positive profit under both outcomes.
    f3_comply=x["IS"]["ps"][2]>0
    if f3_comply:
        override_candidate="IS"
    else:
        override_candidate="RS"  # under mandatory rule F3 exits, incumbent-only
    # Sequential unanimous public approval given full private RS history:
    govt_yes=all(x[override_candidate]["ws"][i]>x["RS"]["ws"][i]
                 for i in (0,1,2))
    govt_no=any(x[override_candidate]["ws"][i]<x["RS"]["ws"][i]
                for i in (0,1,2))
    assert govt_yes != govt_no # no govt tie at two witnesses
    resolved_R=override_candidate if govt_yes else "RS"
    # Backwards F3 accepts private I contract iff it beats NS:
    accepts3=x["IS"]["ps"][2]>x["N"]["ps"][2]
    assert accepts3
    # F2 accepts each credible invitation iff final P > NS.
    assert x[resolved_R]["ps"][1]>x["N"]["ps"][1]
    assert x["IS"]["ps"][1]>x["N"]["ps"][1]
    payoff_proposals={
        "N":x["N"]["ps"][0],
        "RS":x[resolved_R]["ps"][0],
        "IS":x["IS"]["ps"][0]}
    best=max(payoff_proposals.values())
    best_dev=[name for name,a in payoff_proposals.items() if a==best]
    outcomes=set("N" if k=="N" else resolved_R if k=="RS" else "IS"
                 for k in best_dev)
    print("at v=",vval,"G_yes=",govt_yes,"F3_complies=",f3_comply,
          "dev_proposals=",best_dev,"final SPE outcomes=",sorted(outcomes))
    return outcomes,govt_yes,x,resolved_R

if __name__=="__main__":
    model=original_market()
    audit_all_parameter_cases(model)
    r39,yes39,x39,cont39=subgame_backward(lo,model)
    r41,yes41,x41,cont41=subgame_backward(hi,model)
    assert r39=={"RS"} and not yes39
    assert r41=={"IS"} and yes41
    assert x39["RS"]["ps"][0]>x39["IS"]["ps"][0]>x39["N"]["ps"][0]
    assert x41["RS"]["ps"][0]>x41["IS"]["ps"][0]>x41["N"]["ps"][0]
    assert x39["IS"]["ws"][0]<x39["RS"]["ws"][0]
    assert x41["IS"]["ws"][0]>x41["RS"]["ws"][0]
    assert x41["RS"]["ps"][2]==0
    assert x41["IS"]["ps"][2]>0
    assert x41["IS"]["cs"]>x41["RS"]["cs"]
    assert x41["IS"]["ws"][0]>x41["RS"]["ws"][0]
    # Public/private INTERACTION via presence of developed technology:
    # absent technology -> certification cannot occur; developed bilateral
    # tech -> regulator's action changes downstream opportunity from
    # R to I; public-state payoff complement, private-profit substitution.
    assert x41["IS"]["ws"][0]-x41["RS"]["ws"][0]>0
    assert x41["IS"]["ps"][0]-x41["RS"]["ps"][0]<0
    # incumbent member's regulator approval can veto GLOBAL welfare gain
    # at v=.39 even though world welfare strictly rises under I.
    assert sum(x39["IS"]["ws"])>sum(x39["RS"]["ws"])
    assert not yes39
    print("PASS all original 6 source primitives; strict backwards SPE "
          "outcomes v=.39:RS, v=.41:IS, compliance/market-access effects.")
    print("CAVEAT fixed s=1; platform-proposal agenda and open-license "
          "eligibility are assumptions; full continuous-depth, proprietary "
          "IP, independent unilateral de facto adoption NOT solved.")
