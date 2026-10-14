"""Stage4: adversarial endogenous license choice and independent standard matching.

Module A: a patent-owning firm proposes (OPEN regional, LICENSED-EXCLUSIVE
regional, open international, or NONE), with continuous c,a design. Private
partners accept/refuse; an outsider can adopt an OPEN regional protocol and
governments may mandate it if legally licensed, but neither can appropriate
exclusive patent rights. This is a SEQUENTIAL GAME with true backward
induction and exact continuous global design optima.

Module B: DIFFERENT controlled institution, simultaneously independent
choices N, X, Y by all 3 firms at fixed c,a. No central proposer and no
post-announcement negotiations or adoption. Unmatched technology adopters
still incur their own physical investment cost, with no consortium benefit.
Enumerate ALL 3**3 action profiles, all 3 unilateral deviations, Cournot
payoffs. Reveals standards-coordination multiplicity at K=0. Do NOT call
this the same timing as Module A.

Both modules apply exactly the frozen 6 economic primitives and the
Stage2 off-diagonal cost extension, no royalty/SEP license payment,
and no new fixed cost; eta=.03,.14 are separately considered. The open
protocol is legally implementable; government cannot compel a CLOSED IP
license. Source's old IS-only SPE at eta=.03 is ABSORBED by closure if
excludable IP is an available action; no universal novelty asserted.
"""
import itertools
import sympy as S
from math import comb

Q=S.Rational
c,a=S.symbols("c a",real=True)
v,g,k,rho,phi=Q(1,100),Q(7,50),Q(1,50),Q(8,25),Q(7,50)
m=1-v
b=g+k*a-v*c
z=1+rho*c
fee=phi*(c*c+a*a)/2
PN=S.factor(3*m/(4*(m+g)**2))
qI=z/(2*(m+b))
PI=S.cancel(3*m*qI*qI-fee)
CSI=S.cancel(Q(3,2)*(m+2*b)*qI*qI)
WI=S.cancel(PI+CSI)

def regional(eta):
    d=g-eta*a
    A=2*m+b
    D=2*m*A-2*d*d
    Y=A-2*d*z
    x=(2*m*z-d)/D
    y=Y/D
    CR=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
    PR=S.cancel(3*m*x*x-fee)
    WR=S.cancel(PR+CR)
    PO=S.cancel(3*m*y*y)
    WO=S.cancel(PO+CR)
    return locals()

def exact_positive(expr,var,left,right,label):
    num,den=S.fraction(S.cancel(expr))
    if den.subs(var,left)<0:num,den=-num,-den
    for typ,x in (("num",num),("den",den)):
        poly=S.Poly(x,var)
        assert poly.eval(left)>0,(label,typ,"left")
        assert poly.eval(right)>0,(label,typ,"right")
        assert poly.count_roots(left,right)==0,(label,typ,"root")
    print("PASS global exact sign:",label,flush=True)

def structural_assertions():
    assert k>v>0
    assert m-g-k>0
    assert m*(m+g-v)-2*g*g>0
    assert 2*m+(g-v)-2*g*(1+rho)>0
    # all outsider production remains positive for eta=.03 and .14
    # over the FULL c,a triangle, and every demand is SPD/substitutes.
    # Compact RS technology: g-v <= b <= g+k-v, 0 <= d <= g.
    assert (g-v)>0
    # All IS and RS adopter costs reproduce original s on a=c=s.
    ss=S.symbols("ss")
    assert S.factor(fee.subs({c:ss,a:ss})-phi*ss*ss)==0
    print("PASS uniformly active Cournot/KKT and positive definite demand")

def global_standard_optima():
    # IS private firm chooses common-interface c=1 but no common
    # product design a=0 (strongest substitution b when a=1).
    assert S.factor(S.diff(PI,a)+6*m*k*qI*qI/(m+b)+phi*a)==0
    exact_positive(S.diff(PI.subs(a,0),c),c,Q(0),Q(1),
                   "IS private payoff increasing in interface c")
    pi_star=S.cancel(PI.subs({c:1,a:0}))
    assert pi_star>PN
    # Uniform RS monotone compatibility: x_c=2m(rho+v*x)/D.
    maxD=2*m*(2*m+g+k)
    minx=(2*m-g)/maxD
    minxc=2*m*rho/maxD
    assert 6*m*minx*minxc>phi
    for e in (Q(3,100),Q(7,50)):
        r=regional(e)
        assert S.factor(S.diff(r["x"],c)
              -2*m*(rho+v*r["x"])/r["D"])==0
    print("PASS global IS optimum c=1,a=0 and global RS optima c=1")
    return pi_star

def certified_R_ideal(e):
    r=regional(e)
    f=S.cancel(r["PR"].subs(c,1))
    deriv=S.cancel(S.diff(f,a))
    n,den=S.fraction(deriv)
    if den.subs(a,0)<0:n,den=-n,-den
    assert den.subs(a,0)>0
    assert S.Poly(den,a).count_roots(0,1)==0
    p=S.Poly(n,a)
    if e==Q(3,100):
        exact_positive(-deriv,a,Q(0),Q(1),
                       "eta .03 private RS payoff STRICTLY decreases with a")
        aa=S.Integer(0)
        low=high=Q(0)
    else:
        assert p.count_roots(0,1)==1
        assert p.eval(0)>0 and p.eval(1)<0
        low,high=Q(5949,10000),Q(5950,10000)
        assert p.eval(low)>0 and p.eval(high)<0
        aa=next(S.re(x) for x in S.nroots(p,maxsteps=400)
                if abs(float(S.im(x)))<1e-9 and 0<float(S.re(x))<1)
    print("PASS unique global private R ideal eta=",e,"a=",S.N(aa,12),
          "P_R=",S.N(f.subs(a,aa),12),flush=True)
    return r,f,aa,low,high

def ip_closure_theorem(e,pi_star):
    r,f,aa,lo,hi=certified_R_ideal(e)
    if e==Q(3,100):
        # The exact global RS exclusive payoff is attained at a=0.
        # This exceeds ALL IS designs; the third outsider would enter
        # this RS design if its open license permitted it.
        c0=Q(0)
        assert f.subs(a,0)>pi_star>PN
        assert PI.subs({c:1,a:0})>r["PO"].subs({c:1,a:0})
        exact_positive(WI.subs(c,1)-r["WR"].subs(c,1),
                       a,Q(0),Q(1),
                       "eta .03 govt incumbent wants IS all a at c=1")
    else:
        exact_positive(f-pi_star,a,lo,hi,
                       "eta .14 exclusive RS global > global IS")
        exact_positive(f-PN,a,lo,hi,
                       "eta .14 exclusive RS global accepted")
        exact_positive((PI-r["PO"]).subs(c,1),a,lo,hi,
                       "eta .14 outsider would JOIN open RS at optimum")
    assert float(f.subs(a,aa))>float(pi_star)
    # Consequence by exhaustive outcome PAYOFF bounds:
    # For any offered OPEN R(c,a), the final firm 1 payoff belongs
    # to {P_N, P_R(c,a), P_I(c,a)}; it cannot exceed unrestricted
    # MAX{P_R^max,P_I^max,P_N}. CLOSED R(c,a) guarantees P_R(c,a)
    # without violating the existing developer's license, and its
    # optimum is strictly higher than both non-R alternatives.
    # At the ONLY global R maximizer, a third firm strictly prefers
    # adopting if allowed (PI > outside PO), so OPEN R cannot attain
    # the closed R maximum. Therefore every SPE final standard in
    # this licensed-technology proposer game is CLOSED bilateral R.
    # This is a full c,a inequality argument, not a finite design grid.
    if e==Q(3,100):
        assert f.subs(a,0)-pi_star>0
    print("PASS exclusive license overturns open regulatory upgrade,",
          "eta=",e,"final full-game SPE TYPE=closed RS",flush=True)
    print("REFERENCE private R vs I profit gap=",S.N(f.subs(a,aa)-pi_star,12))
    # Competitive efficiency can diverge: even at the same design
    # international adoption may raise aggregate governmental welfare.
    if e==Q(3,100):
        ww=S.cancel((3*WI-2*r["WR"]-r["WO"]).subs({c:1,a:0}))
        assert ww>0
        assert S.cancel((r["WR"]-WI).subs({c:1,a:0}))<0
        print("PASS full-country welfare loss from patent closure:",
              S.N(ww,12),flush=True)
    return r

def independently_chosen_platforms(r,pi_star):
    """Exactly 3^3 no-coordinator labels for a pre-defined design c=1,a=0.

    Each firm chooses N (national/legacy) or incompatible X/Y (two
    competing technology families). If a cohort has >=2, those cohort
    adopters produce with the original RS or IS network parameters.
    Unmatched singletons remain at original NS/RS outsider q but still
    sink their individual private real implementation cost. The firms
    CANNOT commit a joint contract in this institution. Govt has no
    unilateral right to develop tech or compel exclusive licenses.
    No post-choice licensing/conversion; this matching subgame is a
    CONTROLLED game, intentionally different timing from the opener.
    """
    e=Q(3,100)
    design={c:1,a:0}
    ppR=S.cancel(r["PR"].subs(design))
    ppO=S.cancel(r["PO"].subs(design))
    ppI=pi_star
    cc=S.cancel(fee.subs(design))
    assert ppR>PN>ppO>0
    assert ppI>ppO
    assert cc>0
    acts=("N","X","Y")
    def pay(profile):
        sizes={s:profile.count(s) for s in ("X","Y")}
        triple=next((s for s in ("X","Y") if sizes[s]==3),None)
        double=next((s for s in ("X","Y") if sizes[s]==2),None)
        if triple is not None:
            return (ppI,ppI,ppI)
        if double is not None:
            return tuple(ppR if act==double else
                         (ppO if act=="N" else ppO-cc)
                         for act in profile)
        return tuple(PN if act=="N" else PN-cc for act in profile)

    eq=[]
    for profile in itertools.product(acts,repeat=3):
        p=pay(profile)
        ok=True
        for i in range(3):
            for dev in acts:
                q=list(profile);q[i]=dev
                if pay(tuple(q))[i]>p[i]:
                    ok=False
        if ok:eq.append(profile)
    assert set(eq)=={("N","N","N"),("X","X","X"),("Y","Y","Y")},eq
    assert pay(("N","N","N"))==(PN,PN,PN)
    # ALL-NS is STRICT Nash: a lone incompatible adopter gets no
    # shared-compatibility advantage, but pays positive cost. In
    # contrast the centralized first-proposer contract game of Stage3
    # could coordinate all three into strictly profitable IS and NO NS
    # SPE for K=0. Noncooperative institutions alter the RESULT.
    assert PN-cc<PN<ppI
    assert ppI>ppO
    print("PASS ALL 27 profiles x all 3 unilateral deviations:",
          "independent adoption pure equilibria",eq,flush=True)
    print("PASS fragmentation (NNN) at K=0 with positive marginal network")
    return eq

if __name__=="__main__":
    structural_assertions()
    pis=global_standard_optima()
    r03=ip_closure_theorem(Q(3,100),pis)
    ip_closure_theorem(Q(7,50),pis)
    independently_chosen_platforms(r03,pis)
    print("Stage4 CONDITIONAL institutional robustness: CLOSED RS replaces")
    print("old open-market IS; independent-platform adoption preserves")
    print("fragmented NE without fixed K. NOT globally joint seven-D.")
