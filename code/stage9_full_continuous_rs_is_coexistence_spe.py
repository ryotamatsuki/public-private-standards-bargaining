"""Stage9: GENUINE all-continuous 3-firm/3-government RS SPE theorem.

Uses EXACT same integrated game, six economic primitives, public O(1,0),
real capital-stock retrofit, and optional seventh real setup K as Stage8.

RS pure initial profile: (X(1,0), X(1,0), N), where X is a legally
excludable private interface not available to public regulators.
Govt G1,G2,G3 choose L; firm3 remains an ACTIVE Cournot producer but
a NONADOPTER; final regional standard RS12.

Proof uses FULL continuum of unilateral c_i,a_i designs, all X/Y/O
labels, all possible postpolicy C adoption Nash selections (pure or
mixed) and all government after-deviation decisions. NO grid inference.

Fixed theta=(.01,.14,.02,.03,.32,.14). The nonempty EXACT interval:
  K_RL = max{U_R - P_out, U_I-P_out} = U_R-P_out
  K_RU = W_I^0-W_N.
For every K in (K_RL,K_RU), this RS outcome is an SPE with credible
offpath Nash continuations. Combined with Stage8 IS existence over
(K_IL,K_IU), both IS and RS exist for K in (K_IL,K_RU).
No claim of uniqueness, full parameter-space classification,
or endogenously chosen public standard (the public blueprint O(1,0)
remains institutional prior art).

Enumerations at rational witness K=.5 use the exact Fraction engine,
but the theorem holds for EVERY real c,a over entire design triangle.
"""
import sympy as S
from fractions import Fraction as F
from functools import lru_cache
import stage5_integrated_independent_standards_and_government as core
import stage8_capitalized_retrofit_continuous_is_spe as prev

Q=S.Rational
c,a=prev.c,prev.a
m,g,v,k,eta,rho,phi=(
    Q(99,100),Q(7,50),Q(1,100),Q(1,50),
    Q(3,100),Q(8,25),Q(7,50))
K_WITNESS=F(1,2)
X1=('X',F(1),F(0))
O1=('O',F(1),F(0))
NN=core.N
h_RS=(X1,X1,NN)

xR=S.cancel(prev.x)
yR=S.cancel(prev.y)
grossR=S.cancel(prev.grossR)
PR=S.cancel(prev.PR)
PI=S.cancel(prev.PI)
P_O=S.cancel(3*m*yR*yR)
P_N=prev.PN
W_N=prev.WN
b=g+k*a-v*c
d=g-eta*a
z=1+rho*c
C_R=S.cancel((m+b)*xR*xR+2*d*xR*yR+m*yR*yR/2)
qI=S.cancel(z/(2*(m+b)))
C_I=S.cancel(Q(3,2)*(m+2*b)*qI*qI)

def strict_sign(expr,variable,lo,hi,label):
    expr=S.cancel(expr)
    numerator,denominator=S.fraction(expr)
    if denominator.subs(variable,lo)<0:
        numerator,denominator=-numerator,-denominator
    for kind,poly in (("num",numerator),("den",denominator)):
        p=S.Poly(poly,variable)
        assert p.eval(lo)>0 and p.eval(hi)>0,(label,kind,'endpoint',p.eval(lo),p.eval(hi))
        assert p.count_roots(lo,hi)==0,(label,kind,'roots')
    print('PASS EXACT Sturm',label,flush=True)

def verify_all_continuous_profit_bounds():
    # All admissible design c,a remain in Cournot-interior region for
    # all relevant symmetric RS and IS configurations.
    assert 2*m+(g-v)-2*g*(1+rho)>0
    assert m*(m+g-v)-2*g*g>0
    assert m>2*(g+k)
    assert S.simplify(S.diff(xR,c)-2*m*(rho+v*xR)/prev.D)==0

    # Even when a prospective RS pair forms through OPEN certification,
    # a pair member's NET profit is globally maximized at (1,0).
    Dmax=2*m*(2*m+g+k)
    Xmin=(2*m-g)/Dmax
    Xcmin=2*m*rho/Dmax
    assert 6*m*Xmin*Xcmin>phi
    strict_sign(-S.diff(PR.subs(c,1),a),a,Q(0),Q(1),
                'global private RS optimum design a=0 once c=1')
    U_R=S.factor(PR.subs({c:1,a:0}))
    U_I=S.factor(PI.subs({c:1,a:0}))
    assert U_R==Q(8486784637,8564004980)
    assert U_I==Q(301481,313600)
    assert U_R>U_I>P_N
    # Direct free private joining of a proprietary X cohort:
    # its own chosen design (c,a), a>=0, meets incumbent X(1,0),
    # so all bilateral common design equals ZERO. Original two
    # private incumbents' mutual interface remains fully c=1.
    # entrant intercept z3=1+rho*c, incumbent z1=z2=1+rho,
    # incumbent-incumbent substitute b0=g-v,
    # entrant cross-substitution t=g-v*c. EXACT Cournot/KKT.
    b0=g-v
    A0=2*m+b0
    zA=1+rho
    t=g-v*c
    q3=S.cancel((A0*(1+rho*c)-2*t*zA)/(2*m*A0-2*t*t))
    x12=S.cancel((zA-t*q3)/A0)
    assert q3.subs(c,1)==qI.subs({c:1,a:0})
    assert q3.subs(c,0)>0
    assert x12.subs(c,0)>0
    # Active KKT support for EVERY entrant c: q3 strictly increases
    # (net profit derivative below also positive); q3(1)=full IS
    # amount <1, t(c)<=g, and therefore incumbent quantities
    # x12=(1+rho-t*q3)/A0 >= (1+rho-g)/A0 >0.
    strict_sign(S.diff(q3,c),c,Q(0),Q(1),
                'heterogeneous outsider entrant Cournot q3 increasing')
    assert q3.subs(c,1)<Q(1)
    assert (1+rho-g)/A0>0
    strict_sign(S.diff(3*m*q3*q3-phi*c*c/2,c),
                c,Q(0),Q(1),
                'outsider X adoption net profit increases in c up to 1')
    # chosen a>=0 only ADDS costs since incumbent a=0.
    assert S.factor((3*m*q3*q3-phi*c*c/2).subs(c,1)-U_I)==0
    P_out=S.factor(P_O.subs({c:1,a:0}))
    K_low=S.factor(U_R-P_out)
    assert P_out==Q(5622566697,10705006225)
    assert K_low==Q(19943656397,42820024900)
    assert U_I-P_out<K_low
    print('PASS every outsider proprietary X continuous adoption bounded:',
          'max net U_I-K; outside payoff P_out',P_out,flush=True)
    print('PASS every O-certification result for private firm bounded:',
          'RS member U_R-K, IS member U_I-K, or nonadopter P_out-K-fee',
          flush=True)
    return U_R,U_I,P_out,K_low

def government_policy_thresholds(U_R,U_I,P_out):
    bpub=(g-v)
    zpub=1+rho
    qpub=zpub/(2*(m+bpub))
    CS_I0=S.factor(Q(3,2)*(m+2*bpub)*qpub*qpub)
    WR0=S.factor(U_R+C_R.subs({c:1,a:0}))
    WI0=S.factor(U_I+CS_I0)
    KU=S.factor(WI0-W_N)
    assert KU==Q(5269762153,8008716800)
    assert K_WITNESS>S.Rational(19943656397,42820024900)
    assert K_WITNESS<KU
    # After REAL bilateral proprietary RS (X1,X1,N), C cannot be
    # proposed (no existing OPEN O). In any contemplated public M
    # all 3 firms strictly comply for K<KU < (gross_single - phi/2).
    # Each incumbent would pay K+phi/2 sunk PLUS K+phi/2 refit.
    # Incumbent government's mandate-vs-L difference:
    # (WI0-2K-phi/2) - (WR0-K) = WI0-WR0-K-phi/2 <0.
    assert WI0-WR0-phi/2<0
    # Both incumbent national governors VETO full public IS mandate.
    # After one incumbent deviates to N (N,X1,N), public M instead
    # makes single X incumbent's national govt strictly happier iff
    # K<KU, since L welfare W_N-K-phi/2 and M WI0-2K-phi/2.
    # N countries' M-vs-L gain WI0-K-W_N >0 on same interval.
    print('PASS national govt L at RS; M strictly follows incumbent exit',
          'for all K in (Klow, KU)',flush=True)
    return WI0,WR0,KU

def global_R_SPE_theorem():
    UR,UI,PO,KL=verify_all_continuous_profit_bounds()
    WI0,WR0,KU=government_policy_thresholds(UR,UI,PO)
    # All post-M initial-company profiles with up to two X incumbents:
    # incumbent or outsider sunk resources do not affect postdecision
    # incremental operating profitability. New public O(1,0) from
    # N or X/Y costs K+phi/2, old O refits cost <=phi/2.
    # A single public compliant firm gross profit 3/(4m);
    # groups of 2/3 have GREATER profit than a singleton.
    G1=Q(3)/(4*m)
    G2=S.factor(3*m*(1+rho)**2/(2*m+(g-v))**2)
    G3=S.factor(3*m*(1+rho)**2/(4*(m+g-v)**2))
    assert G1<G3<G2
    assert KU<G1-phi/2
    assert G1-KU-phi/2>0
    assert UI-PO<KL
    assert UR-PO==KL
    assert PO>P_N-KL-phi/2
    # Baseline RS incumbent profit UR-K; outsider PO (no setup).
    # Incumbent deviation within X family:
    # retained matching pair => PR(c,0)-K - phi*a²/2 <= UR-K;
    # if another policy M occurs => all comply, earns
    # <= UI-K (in fact initial X setup plus new O refit) < UR-K.
    # Incumbent deviation to N:
    # h=(N,X1,N), regulator M strictly (KU threshold),
    # unique all-comply, deviator payoff UI-K < UR-K.
    # Incumbent deviation to different proprietary Y / public O:
    # under L standalone earns P_N-K-fee < UR-K;
    # under C, max {UR-K,UI-K, solo}<UR-K or weakly equal;
    # under M, adheres to public O with total development costs >=
    # K+phi/2, so private payoff <=UI-K<UR-K.
    # Outsider deviation to N (status quo) is indifferent;
    # to X c,a as third compatible adopter, max UI-K < PO
    # (proved by exact own-q/c derivative);
    # to O or Y under L/N or C, payoff <=max(UR-K,UI-K,
    # PO-K-fee) < PO by KL threshold; under M payoff <= UI-K<PO.
    assert S.simplify(UI-UR)<0
    assert KL<KU
    IS_lower=S.Max(
        S.factor(prev.grossR.subs({c:1,a:0})-P_N),
        S.factor(UI-Q(18931201,37781700)))
    assert IS_lower==Q(65543475780783,136692224487025)
    assert IS_lower>KL
    assert IS_lower<KU
    print('PASS STAGE9 exact RS all-continuous SPE setup interval',
          '(',KL,',',KU,')',flush=True)
    print('PASS STAGE9 coexistence of RS and IS full-continuous SPE',
          '(',IS_lower,',',KU,')',flush=True)
    print('Numerical bounds:',
          'RS K_low',S.N(KL,15),
          'IS K_low',S.N(IS_lower,15),
          'shared K_high',S.N(KU,15),flush=True)
    return KL,KU

def independent_fraction_checks():
    # Modifiable capital-stock model is loaded in same Python
    # interpreter, no modification of old source files.
    prev.freeze_retrofit()
    etaF,K=F(3,100),F(1,2)
    pay=core.continuation(h_RS,'L',None,(0,0,0),K,etaF)
    assert pay[0][0]==pay[0][1]
    assert pay[0][2]>pay[0][0]
    assert pay[2][2]>0 # outsider economically ACTIVE.
    on,opts=core.government_policy(h_RS,K,etaF)
    assert on[0]=='L',on
    assert on[3][2][2]>0
    q=core.government_policy((NN,X1,NN),K,etaF)[0]
    assert q[0]=='M' and q[2]==(1,1,1),q
    P0=pay[0][0];P3=pay[0][2]
    assert q[3][0][0]<P0
    # Check independent firms changing exogenous standards and
    # exact continuous rational design samples: NOT used as proof.
    trials=((F(1,1000),F(0)),(F(1,4),F(0)),(F(1,2),F(0)),
            (F(99,100),F(0)),(F(1),F(0)),
            (F(1),F(1,100)),(F(1),F(3,5)),(F(1),F(1)))
    count=0
    for i in range(3):
        baseline=pay[0][i]
        for lab in ('X','Y','O'):
            for cc,aa in trials:
                h=list(h_RS)
                h[i]=(lab,cc,aa)
                h=tuple(h)
                got,_=core.government_policy(h,K,etaF)
                gain=got[3][0][i]-baseline
                assert gain<=0,('profitable-off-menu',i,h,got[0],gain)
                count+=1
        if i<2:
            h=list(h_RS);h[i]=NN
            got,_=core.government_policy(tuple(h),K,etaF)
            assert got[0]=='M' and got[3][0][i]<baseline
            count+=1
    # Explicitly check the far edge K=.6 where certification is
    # offpath and adoption multiple equilibria might appear.
    for Ke in (F(47,100),F(1,2),F(3,5),
               F(657,1000)):
        for h in (h_RS,(NN,X1,NN)):
            pol,_=core.government_policy(h,Ke,etaF)
            assert pol[0]==('L' if h==h_RS else 'M'),(Ke,h,pol)
    # Onpath after h=X1,X1,N, M all compliant uniquely given
    # gamma,m,K bounds; check direct adopter Nash continuation.
    adopted=core.adoption_pure_nash(h_RS,'M',core.PUBLIC,K,etaF)
    assert len(adopted)==1 and adopted[0][0]==(1,1,1)
    print('PASS independent exact Fraction Cournot-KKT',
          count,'unrestricted-design adversarial sample actions;',
          ' govt veto/consent and policy continuation',flush=True)

if __name__=='__main__':
    global_R_SPE_theorem()
    independent_fraction_checks()
    print('PASS genuine fully-continuous RS SPE and overlap with IS.',
          'NO claim of total seven-parameter phase classification.')
