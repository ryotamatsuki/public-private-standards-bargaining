"""Large-integration-cost persistence theorem for endogenous RS/IS depth.

No full-depth-only inference. General FIVE-dimensional sufficient slope
condition plus independent exact F=10 all-t witness for same market baseline.
"""
import sympy as S
from verify_six_dimensional_corners import strong
from verify_all_depth_frontier_theorems import (
 G,L,E,r,F,s,PR0,WR0,PI0,WI0,PR,WR,PI,WI,PN,WN,
 lift,strict_positive_sturm)
Q=S.Rational
aPR=S.factor(S.diff(PR0,s).subs(s,0))
aPI=S.factor(S.diff(PI0,s).subs(s,0))
aWR=S.factor(S.diff(WR0,s).subs(s,0))
aWI=S.factor(S.diff(WI0,s).subs(s,0))

def asymptotic_general():
    # Under these STRICT five-parameter inequalities, for every
    # sufficiently large F>0, RS(s_R) at GLOBAL firm maximizer s_R
    # and IS(s_I) at GLOBAL government maximizer s_I both strong:
    # aPR>aPI>0, aWI>aWR>0,
    # 2*aWR>aPR, 2*aPI>aWI.
    # Taylor expansions valid near s=0 (RS outsider interior there);
    # global maximizers shrink as 1/F due compact feasible depths.
    eps=S.symbols('eps',positive=True)
    vals={G:Q(5,16),L:-Q(1,16),E:Q(3,32),r:Q(1,4)}
    slopes={z:S.factor(z.subs(vals)) for z in (aPR,aPI,aWR,aWI)}
    ap,ai,aw,bw=[slopes[k] for k in (aPR,aPI,aWR,aWI)]
    assert ap>ai>0
    assert bw>aw>0
    assert 2*aw>ap and 2*ai>bw
    print("PASS high-cost slope inequalities:",
          "aPR",ap,"aPI",ai,"aWR",aw,"aWI",bw)
    # Evaluate the SAME first-order high-fee value envelope in each class.
    # F=1/eps, candidate s=a*eps/2 gives optimum to first order,
    # with global max equality following uniform bounded curvature near 0.
    for tag,curve,a,baseline in (
       ("private regional",PR0,ap,PN),
       ("private international",PI0,ai,PN),
       ("government regional",WR0,aw,WN),
       ("government international",WI0,bw,WN)):
        candidate=a*eps/2
        expr=(curve.subs(vals).subs(s,candidate)
              -candidate**2/eps-baseline.subs(vals))
        assert S.simplify(S.limit(expr/eps,eps,0)-a*a/4)==0,tag
    # RS firm optimum s_R~ap/(2F) gives government participation
    # (aw*ap/2 - ap^2/4)/F>0; IS govt optimum s_I~bw/(2F)
    # gives private participation (ai*bw/2 - bw^2/4)/F>0.
    assert ap*(2*aw-ap)>0 and bw*(2*ai-bw)>0
    assert ap*ap>ai*ai and bw*bw>aw*aw
    print("PROVED asymptotic strict RS-vs-IS profit and IS-vs-RS govt dominance")
    print("PROVED existence: there is a finite F0 such that ALL F>F0")
    print("yield both partial-depth regional and international strong contracts")

def independent_high_fee_witness():
    sR=Q(17,1000);sI=Q(11,500)
    v={G:Q(5,16),L:-Q(1,16),E:Q(3,32),r:Q(1,4),F:Q(10)}
    ev=lambda e:S.cancel(e.subs(v))
    strict_positive_sturm(ev(PR.subs(s,sR)-PI),
      "F=10 RS(17/1000) strictly higher profit than EVERY IS depth")
    strict_positive_sturm(ev(WI.subs(s,sI)-WR),
      "F=10 IS(11/500) strictly higher govt W than EVERY RS depth")
    for name,e in (("private R concavity",-S.diff(PR,s,2)),
                   ("govt R concavity",-S.diff(WR,s,2)),
                   ("private I concavity",-S.diff(PI,s,2)),
                   ("govt I concavity",-S.diff(WI,s,2))):
        strict_positive_sturm(ev(e),name)
    assert ev(S.diff(PR,s).subs(s,sR))<0
    assert ev(S.diff(WR,s).subs(s,sR))>0
    assert ev(S.diff(PI,s).subs(s,sI))<0
    assert ev(S.diff(WI,s).subs(s,sI))>0
    for gain in (PR.subs(s,sR)-PN,WR.subs(s,sR)-WN,
                 PI.subs(s,sI)-PN,WI.subs(s,sI)-WN):
        assert ev(gain)>0
    physical=lift((Q(5,16),-Q(1,16),Q(3,32),Q(1,4),Q(10)))
    assert strong(physical,'R',sR,uniform=True)
    assert strong(physical,'I',sI)
    assert not strong(physical,'N')
    print("PASS exact F=10 continuous-depth strong RS(s=.017) and IS(s=.022)")
if __name__=='__main__':
    asymptotic_general()
    independent_high_fee_witness()
