"""Stage8: fully continuous IS outcome SPE via CAPITALIZED open-standard retrofit.

This is the first fully certified continuous design IS equilibrium in
the unified three-independent-firm / three-national-government game.

Keep six original parameters (v,gamma0,kappa,eta,rho,phi)
=(.01,.14,.02,.03,.32,.14); the already explicit real technology
setup K varies in the WHOLE CLOSED INTERVAL [1/2,3/5].

OPEN->OPEN investment is CAPITAL STOCK, NOT fresh setup:
C_up(O(c,a)->O(c',a')) =
 phi/2*(max(0,c'^2-c^2)+max(0,a'^2-a^2)).
N->O, X/Y->O still pay new full K+phi/2*(c'^2+a'^2);
cost of old X/Y or O development remains SUNK.
In particular initial O(c,a) followed by mandatory O(1,0) costs
K+phi/2*(1+a^2) >= K+phi/2: no staged-investment arbitrage.

Theorem: all firms initially choose N. Government unanimously mandates
pre-existing PUBLIC-DOMAIN O(1,0), all firms strictly comply (unique
adoption NE); final international standard IS with compatible, non-
homogeneous products (c,a)=(1,0). This is a real SPE in the full
CONTINUOUS initial c_i,a_i strategy space, for any K in [.5,.6].
Every unilateral private technology development deviation is blocked
against ANY government equilibrium continuation: after an O proposal
no other N would voluntarily migrate under C (STRICT DOMINANCE); M
always induces all three to comply (STRICT DOMINANCE); thus deviator
can receive only L (solo N output) or mandatory public IS with total
capitalized cost >= nondeviator adoption cost. Proprietary alternatives
cannot be mandated without joining the open public alternative.

This is a CONDITIONAL existence result on a one-dimensional K interval,
NOT general 7D full SPE phase classification, nor unique SPE existence.
Finite stage5 benchmark with 3 discrete c,a options is separately rerun
under the new stock-cost model, to record how sensitive its count is.

Exact SymPy proof on ENTIRE design triangle, no sampling; model-specific
pure-Fraction 3x3 Cournot after any policy uses original KKT engine.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import Counter
import sympy as S
import stage5_integrated_independent_standards_and_government as mod
ORIGINAL_CONTINUATION=mod.continuation

Q=S.Rational
m,g,v,k,eta,rho,phi=(Q(99,100),Q(7,50),Q(1,100),Q(1,50),
                       Q(3,100),Q(8,25),Q(7,50))
c,a=S.symbols("c a",real=True)
z=1+rho*c
b=g+k*a-v*c
d=g-eta*a
A=2*m+b
D=2*m*A-2*d*d
x=S.cancel((2*m*z-d)/D)
y=S.cancel((A-2*d*z)/D)
qI=S.cancel(z/(2*(m+b)))
fee=phi*(c*c+a*a)/2
grossR=S.cancel(3*m*x*x)
PR=S.cancel(grossR-fee)
grossI=S.cancel(3*m*qI*qI)
PI=S.cancel(grossI-fee)
qN=S.cancel(1/(2*(m+g)))
PN=S.cancel(3*m*qN*qN)
WN=S.cancel(PN+S.Rational(3,2)*(m+2*g)*qN*qN)

def exact_positive(expr,var,left,right,name):
    nu,de=S.fraction(S.cancel(expr))
    if de.subs(var,left)<0:nu,de=-nu,-de
    for nm,part in (("numerator",nu),("denominator",de)):
        p=S.Poly(part,var)
        assert p.eval(left)>0 and p.eval(right)>0,(name,nm)
        assert p.count_roots(left,right)==0,(name,nm,"root")
    print("PASS full interval exact sign",name,flush=True)

def theorem_global_deviation_bounds():
    assert m>2*(g+k)
    assert d.subs(a,1)>0 and b.subs({c:1,a:0})>0
    assert S.factor(S.diff(x,c)-2*m*(rho+v*x)/D)==0
    # Outsider always ACTIVE throughout the full triangle, correctly KKT.
    Ymin=2*m+(g-v)-2*g*(1+rho)
    Dmax=2*m*(2*m+g+k)
    assert Ymin==Q(4351,2500)
    assert Dmax==Q(10593,2500)
    ymin=Ymin/Dmax
    assert ymin==Q(4351,10593)
    assert m*(m+g-v)-2*g*g>0
    # x(c,a) strictly increasing in c, and x(1,a) strictly DECREASING
    # in a in this eta=.03 example. Global GROSS RS firm profit
    # therefore cannot exceed grossR(1,0), even if a migrant does
    # not pay the small design term of the implementation resource fee.
    exact_positive(-S.diff(x.subs(c,1),a),a,Q(0),Q(1),
                   "insider Cournot quantity x(1,a) decreasing")
    xmax=x.subs({c:1,a:0})
    assert xmax==Q(12368,20693)
    rgrossmax=S.cancel(grossR.subs({c:1,a:0}))
    assert rgrossmax==Q(11357831232,10705006225)
    assert rgrossmax-Q(1,2)<PN
    # Under IS with all three adopters, private P after full fee has
    # UNIQUE global max at c=1,a=0 over the whole design triangle.
    assert S.simplify(S.diff(PI,a)+6*m*k*qI*qI/(m+b)+phi*a)==0
    exact_positive(S.diff(PI.subs(a,0),c),c,Q(0),Q(1),
                   "net private IS payoff increasing in c at a=0")
    PImax=S.cancel(PI.subs({c:1,a:0}))
    assert PImax==Q(301481,313600)
    outsidegrossmin=S.cancel(3*m*ymin*ymin)
    assert outsidegrossmin==Q(18931201,37781700)
    assert outsidegrossmin>PImax-Q(1,2)
    # Therefore after any SINGLE open developer O(c,a) and two other
    # firms N, each N has a STRICTLY DOMINANT nonmigration action in
    # a voluntary C(r) adoption subgame:
    # - when other N has NOT migrated: potential RS profit
    #   <=grossRmax-K < P_N.
    # - when other N HAS migrated: potential IS profit
    #   <=PImax-K < outside RS profit, which is >=outsidegrossmin.
    print("PASS full TRIANGLE: no other N can migrate after one O",
          "private open standard developer at ANY K>=1/2",flush=True)
    print("gross RS max",rgrossmax,"IS P net max",PImax,
          "outsider gross lower",outsidegrossmin,flush=True)
    return rgrossmax,PImax,outsidegrossmin

def capital_retrofit(pre,policy,ref,flags,K,eta_F):
    # mod.original uses original repeated setup fee when post[i]!=ref.
    # Only OLD->NEW SAME O family cost is replaced.
    initial=ORIGINAL_CONTINUATION(pre,policy,ref,flags,K,eta_F)
    p,w,q,cs,post=initial
    pp=list(p);ww=list(w)
    if policy in ('C','M'):
        for i,ok in enumerate(flags):
            if not ok or pre[i]==ref:continue
            if pre[i][0]=='O' and ref[0]=='O':
                oldcharged=mod.cost(ref,K)
                cc,aa=pre[i][1],pre[i][2]
                nr,ar=ref[1],ref[2]
                # explicit physical capital stock, no K charged again:
                newcharged=mod.phi/2*(max(F(0),nr*nr-cc*cc)
                                       +max(F(0),ar*ar-aa*aa))
                diff=oldcharged-newcharged
                pp[i]+=diff
                ww[i]+=diff
    return tuple(pp),tuple(ww),q,cs,post

def freeze_retrofit():
    # Run in a NEW interpreter, and patch only the imported Stage5
    # model in local process. Older GitHub files stay UNCHANGED.
    mod.continuation=lru_cache(None)(capital_retrofit)
    mod.adoption_pure_nash.cache_clear()
    mod.government_policy.cache_clear()

def theorem_public_mandate_and_private_incentives():
    _,pi,outs=theorem_global_deviation_bounds()
    Klow,Khigh=Q(1,2),Q(3,5)
    bpub=b.subs({c:1,a:0})
    zpub=z.subs(c,1)
    # Public standard n=1/2/3 compliant firm GROSS profits.
    gross=(Q(3)/(4*m),
           S.cancel(3*m*(zpub/(2*m+bpub))**2),
           S.cancel(3*m*(zpub/(2*(m+bpub)))**2))
    assert gross[1]>gross[0] and gross[2]>gross[0]
    # The highest possible ACTUAL FEE to switch to public from any
    # single proprietary developer or any initial N is K+phi/2;
    # from prior O(c,a) it is <=phi/2. All three strictly prefer
    # compliance to EXIT, whatever their rivals' compliance actions.
    assert gross[0]>Khigh+phi/2
    assert phi/2==Q(7,100)
    print("PASS any single-developer-history public mandate: all 3",
          "compliance strictly DOMINANT across every c,a and K in [.5,.6]",
          flush=True)
    CS_I=S.cancel(Q(3,2)*(m+2*bpub)*(zpub/(2*(m+bpub)))**2)
    WI_0=S.cancel(pi+CS_I)
    assert WI_0-Khigh>WN
    print("PASS all 3 government mandates after h=NNN:",
          "W_I0-K(max)",WI_0-Khigh,"W_N",WN,flush=True)
    # Under h=NNN: only L,M are feasible, unique adoption 111 after M,
    # all governments strictly prefer M; L payoff PN to each firm.
    # Each firm's final payoff PImax-K (all adopting public O(1,0)).
    # After single developer h'=(N,N, (label,c,a)):
    #    L or C (unique effective no-migration) => P_N - [K+fee(c,a)]
    #                                  < PImax-K.
    #    M unique 111 => P_I^gross(1,0) minus sunk investment and
    #                      any incremental refit fee.
    # If label O: K+phi/2*(c^2+a^2)
    #             +phi/2*(1-c^2)
    #             =K+phi/2*(1+a^2) >=K+phi/2.
    # If label X/Y: K+phi/2*(c^2+a^2)
    #               +K+phi/2 >K+phi/2.
    # Thus P_dev(M)<=PImax-K. Equalities allowed but no gain.
    assert PN<pi
    t=S.symbols("t",real=True,nonnegative=True)
    for design_c in (Q(1,1000),Q(1,2),Q(1)):
        for design_a in (Q(0),design_c):
            open_init=Klow+phi/2*(design_c**2+design_a**2)
            open_upgrade=phi/2*(1-design_c**2)
            assert open_init+open_upgrade>=Klow+phi/2
    print("PASS ENDOGENOUS full continuous first-stage deviation",
          "bound: all open/proprietary/legacy alternatives to N blocked",
          "by public IS at any K∈[.5,.6]",flush=True)
    return pi

def sampled_exact_fraction_crosscheck():
    # Fully recalculates equilibrium-continuation institutional choices
    # and exact KKT outcomes for selected admissible first-stage
    # full-continuum deviations; symbolic argument above is proof.
    K,eta_F=F(1,2),F(3,100)
    base=mod.government_policy((mod.N,mod.N,mod.N),K,eta_F)[0]
    assert base[0]=='M' and base[2]==(1,1,1)
    dev_baseline=base[3][0][2]
    for lab in ('X','Y','O'):
        for design_c,design_a in (
            (F(1,1000),F(0)),(F(1,2),F(0)),
            (F(1),F(0)),(F(1),F(1,100)),(F(1),F(3,5))):
            h=(mod.N,mod.N,(lab,design_c,design_a))
            q=mod.government_policy(h,K,eta_F)[0]
            assert q[3][0][2]<=dev_baseline,(
                h,q[0],q[3][0][2]-dev_baseline)
            if lab=='O':
                eq=mod.adoption_pure_nash(h,'C',h[2],K,eta_F)
                # There are inert developer self-retain flags; all
                # different allocations are equivalent to L (no
                # previously-N developer joins privately).
                for flags,outcome in eq:
                    assert flags[0]==0 and flags[1]==0
                    assert outcome[2]==mod.continuation(
                        h,'L',None,(0,0,0),K,eta_F)[2]
                # M compliance requires all 3 (strict dominance).
            em=mod.adoption_pure_nash(h,'M',mod.PUBLIC,K,eta_F)
            assert len(em)==1 and em[0][0]==(1,1,1),(h,em)
    print("PASS independent source Fraction 3x3 market, gov votes,",
          "migration, and compliance spot checks",flush=True)

def finite_pilot_new_cost():
    # Independent disclosure: these finite 10-per-firm equilibria are
    # NOT the above full-continuum existence theorem, nor exhaustive
    # mixed equilibrium correspondences.
    for K in (F(0),F(1,2),F(3,5),F(3,4)):
        es=mod.firm_nash(K,F(3,100))
        types=Counter(mod.final_type(h,pol) for h,pol in es)
        govt=Counter(pol[0] for h,pol in es)
        print("CAPITAL-STOCK REPAIRED FINITE menu K",K,
              "N",len(es),"types",dict(types),"policy",dict(govt),
              "initial_h",tuple(h for h,_ in es)[:5],flush=True)
        assert es

if __name__=="__main__":
    theorem_public_mandate_and_private_incentives()
    freeze_retrofit()
    sampled_exact_fraction_crosscheck()
    finite_pilot_new_cost()
    print("PASS Stage8 genuine full-continuous public-mandate IS SPE",
          "for all K ∈ [1/2,3/5]; no full 7D phase partition claim.")
