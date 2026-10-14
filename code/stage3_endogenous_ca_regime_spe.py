"""Stage3: FULL / PARTIAL / FRAGMENTED final SPE with endogenous c,a.

3 firms: F1 proposes NS, bilateral RS12(c,a), or IS123(c,a).
Invited firms individually accept/reject. After RS, G1,G2,G3
SEQUENTIALLY vote on regulatory IS(c,a) of the already-developed OPEN
interface. A unanimously approved mandate makes F3 decide implement
(paying cost) or exit; all 3 enter differentiated Cournot, with true
KKT active-set branches. The government is unable to conjure a yet
undeveloped technology or appropriate unlicensed proprietary IP.
Gov status-quo tie-breaking: certification requires STRICT gain for ALL.
F1 chooses global c,a on T={(c,a):0<a<=c<=1 or 0<=a<c<=1}.
ALL outcomes below are pure backward-induction SPE final types; no
strong-Nash stage-one refinement is used.
Original 6 primitives retained with off-diagonal quadratic cost extension;
nonzero installed technology may additionally require genuine setup K.
At K=0 fragmentation impossible if v>0 or rho>0. Explicit K=0.5
allows NS; this is a NEW SEVENTH primitive, not concealed.
"""
import sympy as S
from math import comb
Q=S.Rational
c,a,t=S.symbols("c a t", real=True)
v,g,k,rho,phi=Q(1,100),Q(7,50),Q(1,50),Q(8,25),Q(7,50)
m=1-v
z=1+rho*c
b=g+k*a-v*c
qI=z/(2*(m+b))
qN=1/(2*(m+g))
PN=S.cancel(3*m*qN*qN)
WN=S.cancel(PN+Q(3,2)*(m+2*g)*qN*qN)
CI=S.cancel(Q(3,2)*(m+2*b)*qI*qI)
cost=phi*(c*c+a*a)/2
PI=S.cancel(3*m*qI*qI-cost)
WI=S.cancel(PI+CI)

def regional(eta):
    d=g-eta*a
    A=2*m+b
    D=2*m*A-2*d*d
    Y=A-2*d*z
    x=(2*m*z-d)/D
    y=Y/D
    CR=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
    PR=S.cancel(3*m*x*x-cost)
    WR=S.cancel(PR+CR)
    WO=S.cancel(3*m*y*y+CR)
    return locals()

def sturm_positive(expr,x,low,high,tag):
    nu,de=S.fraction(S.cancel(expr))
    if de.subs(x,low)<0: nu,de=-nu,-de
    for part,poly in (("num",nu),("den",de)):
        p=S.Poly(poly,x)
        assert p.eval(low)>0 and p.eval(high)>0,(tag,part,"endpoint")
        assert p.count_roots(low,high)==0,(tag,part,"root")
    print("PASS Sturm:",tag,flush=True)

def tensor_positive(poly,tag):
    p=S.Poly(S.expand(poly),c,t)
    nx,ny=p.degree_list()
    coeff=[[S.Integer(0) for _ in range(ny+1)] for _ in range(nx+1)]
    for (i,j),value in p.terms():coeff[i][j]=value
    count=0
    for i in range(nx+1):
        for j in range(ny+1):
            bb=sum(coeff[h][ell]*
                  Q(comb(i,h),comb(nx,h))*Q(comb(j,ell),comb(ny,ell))
                  for h in range(i+1) for ell in range(j+1))
            assert bb>0,(tag,i,j,bb)
            count+=1
    print("PASS full triangle via tensor Bernstein:",tag,count,"positive",flush=True)

def general_spe_criterion():
    # Let D_K denote developed OPEN (c,a), and setup K be paid once
    # by each participating firm (both in RS and IS). Regulator chooses
    # the unanimous upgrade iff all 3 governments STRICTLY gain and
    # each regulated implementing firm makes >= its exit-profit zero.
    # Use TRUE KKT outcomes for outsider. Define:
    # T_S(K)={D_K : no public upgrade, PR(D_K)-K >= PN}
    # T_I(K)={D_K : PI(D_K)-K>=PN}
    # V_R=max_{T_S} PR(D_K)-K;
    # V_I=max_{T_I} PI(D_K)-K.
    # A private RS which will be regulator-upgraded has final payoff
    # PI(D_K)-K and can be implemented directly as IS at exactly D_K.
    # Hence it can never exceed V_I. Among attained, credible maxima,
    # final SPE STANDARD TYPES are exactly argmax of {PN,V_R,V_I}.
    # If an argmax is NOT attained due to a policy discontinuity,
    # pure SPE may fail. The concrete witnesses below attain maxima.
    print("THEOREM: type-SPE via argmax{PN, V_R(unupgraded), V_I}",flush=True)

def verify():
    assert k>v>0
    # All six original demand parameters as specified; across ENTIRE
    # feasible design triangle and eta=.03/.14 the outsider is active.
    assert 2*m+Q(13,100)-2*Q(14,100)*(1+rho)>0
    assert m-Q(15,100)>0
    assert m*(m+Q(13,100))-2*Q(14,100)**2>0
    # For any positive theta, PI(c,0) has strictly POSITIVE derivative
    # at zero (quadratic implementation cost has zero marginal cost).
    mm,gg,vv,rr,pp=S.symbols("mm gg vv rr pp",positive=True)
    cc=S.symbols("cc")
    psmall=3*mm*(1+rr*cc)**2/(4*(mm+gg-vv*cc)**2)-pp*cc**2/2
    assert S.factor(S.diff(psmall,cc).subs(cc,0)-
                   3*mm*(rr*(mm+gg)+vv)/(2*(mm+gg)**3))==0
    print("PASS no-fragmentation at setup K=0, positive v or rho",flush=True)
    # Global IS optimum: at FIXED c, design commonality always lowers
    # private output and raises implementation cost; choose a=0.
    assert S.factor(S.diff(PI,a)+6*m*k*qI*qI/(m+b)+phi*a)==0
    pi_c0=S.cancel(PI.subs(a,0))
    sturm_positive(S.diff(pi_c0,c),c,Q(0),Q(1),"IS P rises to c=1 at a=0")
    PImax=S.cancel(PI.subs({c:1,a:0}))
    assert PImax>PN
    print("PASS IS global optimum c=1,a=0",S.N(PImax,12),flush=True)
    # Uniform positivity of compliance profitability for K=0.
    assert 3*m/(4*(m+g+k)**2)-phi>0
    # For RS, P_c strictly positive at EVERY a, by exact lower bounds
    # and Cournot derivative identity. Thus global RS maximizer c=1.
    Dmax=2*m*(2*m+g+k)
    Xmin=(2*m-g)/Dmax
    Xcmin=2*m*rho/Dmax
    assert 6*m*Xmin*Xcmin>phi
    for eta in (Q(3,100),Q(7,50)):
        R=regional(eta)
        assert S.factor(S.diff(R["x"],c)-
                        2*m*(rho+v*R["x"])/R["D"])==0
        assert S.factor(R["y"]-R["Y"]/R["D"])==0
    print("PASS RS global c=1 for both theta",flush=True)
    # FULL IS: eta=.03; for every private RS proposal with
    # 0<c<=1 and 0<=a<=c all governments STRICTLY prefer IS.
    # Substitute a=c*t, 0<=t<=1 and prove *full continuum* signs.
    low=regional(Q(3,100))
    for tag,delta in (("incumbent gov IS-RS",WI-low["WR"]),
                      ("outsider gov IS-RS",WI-low["WO"])):
        nu,de=S.fraction(S.cancel(delta.subs(a,c*t)))
        assert de.subs({c:0,t:0})>0
        assert S.simplify(nu.subs(c,0))==0
        tensor_positive(S.cancel(nu/c),tag)
    # Since PI>0 uniformly and invited private direct IS contracts
    # at (c=1,a=0) strictly beat NS, all on-path SPE type IS.
    print("PASS FULL IS final SPE: eta=.03, K=0",flush=True)
    # PARTIAL RS: eta=.14; the GLOBAL private RS optimum is c=1
    # and the UNIQUE stationary aR in (.5949,.5950).
    high=regional(Q(7,50))
    PR1=S.cancel(high["PR"].subs(c,1))
    der=S.cancel(S.diff(PR1,a))
    n,de=S.fraction(der)
    if de.subs(a,0)<0:n,de=-n,-de
    n=S.Poly(n,a)
    assert de.subs(a,0)>0 and S.Poly(de,a).count_roots(0,1)==0
    assert n.eval(0)>0 and n.eval(1)<0 and n.count_roots(0,1)==1
    left,right=Q(5949,10000),Q(5950,10000)
    assert n.eval(left)>0 and n.eval(right)<0
    sturm_positive((high["WR"]-WI).subs(c,1),a,left,right,
                  "private RS* incumbent govt VETO (W_R>W_I)")
    sturm_positive(PR1-PImax,a,left,right,
                  "private RS* dominates GLOBAL IS private payoff")
    sturm_positive(PR1-PN,a,left,right,
                  "private RS* is voluntarily accepted")
    root=next(S.re(zz) for zz in S.nroots(n,maxsteps=400)
              if abs(float(S.im(zz)))<1e-9 and 0<float(S.re(zz))<1)
    print("PASS PARTIAL RS final SPE: eta=.14 K=0 c=1 a=",
          S.N(root,12),"P_R",S.N(PR1.subs(a,root),12),flush=True)
    # FRAGMENT NS: add upfront K=.5 for ANY nonzero developed standard.
    # Since P_R(c,a) <= P_R(1,a) for all 0<=a<=c<=1, a global
    # rational Sturm inequality excludes ALL bilateral developments.
    sturm_positive(PN+Q(1,2)-PR1,a,Q(0),Q(1),
                  "K=.5 makes EVERY RS inferior to NS")
    assert PImax-Q(1,2)<PN
    print("PASS FRAGMENT NS final SPE: eta=.14 K=.5",flush=True)
    print("CAUTION: full all-firm INTEROPERABILITY c=1 is NOT full")
    print("homogeneous PRODUCTS a=1; latter is suboptimal in IS.")
    print("CAUTION: existence across arbitrary parameter theta and")
    print("global SPE off policy indifference surfaces not proven.")

if __name__=="__main__":
    general_spe_criterion()
    verify()
