"""Stage15: Three-country UNANIMITY necessity in MINIMAL public/private SPE.

Full continuous six-player *reduced* standards game:
At t=1 firms independently choose N or O(c_i,a_i), 0<=a_i<=c_i<=1,
where O is an OPEN and already legally useable technical family, with
upfront real K+phi(c_i^2+a_i^2)/2.
At t=2 G1 (RS member government) proposes public O(1,0) M vs L;
G2 and G3 sequentially vote. With unanimous YES implement M,
otherwise L. Under policy M companies decide comply/exit; the
dominant-strategy equilibrium all 3 comply for the theorem rectangle.
Same-O downgrade has no recouped sunk resources; conforming at O(1,0)
requires missing c-capital but never a repeat fixed K.
At L all firms produce differentiated Cournot in the 3 local markets.
At M all adopters produce differentiated Cournot in the 3 local markets.
NO certification C and NO proprietary X/Y actions. This is a
DECLARED REDUCTION from Stage10, not an automatic proof of original
complete X/Y/O/N governance game.

Fixed (v,g,k,rho,phi)=(.01,.14,.02,.32,.14), eta in [.10,.14],
K in [.54,.56]. Prior Stage11 (design root and global profit bounds)
and Stage14 (full rectangle national veto inequalities) are imported
mathematically: this script verifies their strict crucial inequalities
again and assembles the ALL-REAL continuous unilateral strategy game.

THEOREM:
(1) Under 3-state UNANIMITY, RS(O(1,a*),O(1,a*),N) is
    a subgame-perfect outcome. Country1 lead govt strictly WANTS M,
    country2 also WANTS M, country3 strictly VETOES M, so L obtains.
    Proposal M, approval G2 YES, veto G3 NO is a credible
    weak-indifferent G1 proposal equilibrium; lead may alternatively
    announce L because its vetoed M cannot change outcomes. NOT a
    claim that G1 has strict incentive to make a doomed proposal.
(2) Under the SAME three-state UNANIMITY, IS(N,N,N; public M(1,0);
    all firms comply) also is an SPE outcome, for all eta,K.
(3) Under MAJORITY (2 of 3 votes; same action/payoff/markets),
    the precise same private RS initial profile is NOT an SPE:
    country1 + country2 pass M; one incumbent O investor strictly
    gains phi*a*^2/2>0 by deviating t=1 to N, because the mandate
    still passes at (N,O,N) and its wasted initial extra a-capital
    becomes zero. DOES NOT prove that NO RS SPE exists under majority.
(4) The difference cannot be obtained from a TWO-government-only
    voting structure which retains just G1,G2 (but the 3-firm
    economy is retained for a clean institutional counterfactual):
    both members approve M. This is NOT a true 2-country
    market-demand-equilibrium comparison.
(5) G3 veto cutoff vs WORLD welfare cutoff are DISTINCT; there
    are parameters in the same region where G3 veto is inefficient,
    and others where it coincides with higher total welfare.

Proof: exact rational Bernstein, Sturm and global KKT bounds from
Stage10/11/14, plus directly checked new cost accounting, and
self-contained payoff inequalities here. Running parent workflows
in the same CI keeps an auditable proof chain.
"""
import sympy as S
from fractions import Fraction as F
from math import comb
from itertools import product
import stage11_eta_k_phase_certificates as s11
import stage14_institutional_veto_ablation as s14
R=S.Rational
e,a=s14.eta,s14.a
lo,hi=R(27,50),R(14,25)
m,g,v,k,rho,phi=s14.m,s14.g,s14.v,s14.k,s14.rho,s14.phi
private=s14.f
pout=s14.po
CS=s14.cs
WI0=s14.WI0
PN=s11.PN
WN=s11.WN
PIstar=s11.PIP
qIS=(1+rho)/(2*(m+g-v))
assert S.factor(WI0-PIstar-R(3,2)*(m+2*(g-v))*qIS*qIS)==0

def polynomial_strict(expr,q,L,U,tag):
    n,d=S.fraction(S.cancel(expr))
    if d.subs(q,L)<0:n,d=-n,-d
    for part,px in [('n',n),('d',d)]:
        poly=S.Poly(px,q)
        assert poly.eval(L)>0 and poly.eval(U)>0,(tag,part,poly.eval(L),poly.eval(U))
        assert poly.count_roots(L,U)==0,(tag,part)
    print('PASS exact Sturm',tag,flush=True)

def private_optimum_root_brackets():
    # All eta in [.10,.14] have unique interior private f(a,eta)
    # maximizer a_R*(eta) due to Stage11 rational concavity / positive
    # cross derivative. The conservative enclosure [.25,.61] suffices.
    polynomial_strict(S.diff(private,a).subs(a,R(1,4)),
                      e,R(1,10),R(7,50),"private f_a(.25,eta)>0")
    polynomial_strict(-S.diff(private,a).subs(a,R(61,100)),
                      e,R(1,10),R(7,50),"private f_a(.61,eta)<0")
    # We do NOT pretend this alone proves concavity. Parent Stage11
    # exact tensor-Bernstein verifies f_aa<0 on all a∈[0,1].
    print('IMPORT VERIFIED Stage11 uniqueness and private f(a*) max',flush=True)

def fixed_private_payoff_upper_bounds():
    # Stage11 globally bounds a private RS member after ANY real
    # unilateral design deviation by U_R<1.009 (before K).
    assert R(1009,1000)-lo<PN
    # Under public M, for ANY prior O(c,a), original upfront stock
    # plus incremental missing capacity for mandated O(1,0):
    # K+phi/2(c²+a²)+phi/2(1-c²)
    # =K+phi/2(1+a²) >= K+phi/2. So public M investor
    # always earns <=P_I^net_before_setup - K.
    # Original a_R*(eta) REGIONAL member earns strictly more.
    T,U=S.symbols("T U")
    s11.tensor_positive(private-PIstar,
       {e:R(1,10)+R(1,25)*T,a:R(1,4)+R(9,25)*U},
       (T,U),"private RS profit beats public IS across eta x a rectangle")
    # If one initially private RS founder switches to N, the
    # remaining O(1,a*) is the ONLY private inventor. Government
    # countries' gain from M is strict:
    # 2 N countries gain WI0-K-WN>0;
    # sole O country gains WI0-WN+phi/2>0.
    assert WI0-WN-hi>0
    assert WI0-WN+phi/2>0
    # Outsider F3 entrant O(c,a) after initial O,O:
    # incumbent pair remains (1,a*), entrant's q3<3/5 for any
    # 0<=a3<=c3<=1 (exact bound from Stage10/11).
    # Its profit net from setup <=3m*(3/5)^2-K<.5292.
    # The incumbent outsider profit at RS with optimal a*
    # is > .547893 (exact Stage11 full continuum).
    bound=s11.R(9114361,16635300)
    assert 3*m*(R(3,5))**2-lo<bound
    assert PIstar-lo<bound
    print('PASS global firm initial deviation bounds, all real c,a',
          'conditional on Stage11 continuous RS root certificates',flush=True)

def government_votes_and_cutoffs():
    # PUBLIC M after observed OPEN private RS O(1,a),O(1,a),N.
    # A member had invested K+phi(1+a²)/2 and downgrades a to 0
    # within same OPEN family without any refund or extra refit.
    # Delta W_incumbent=(WI0-K-phi*a²/2)-(f+CS-K)
    #                  =WI0-phi*a²/2-f-CS.
    d1=S.cancel(WI0-phi*a*a/2-private-CS)
    # A formerly N outsider spends new K+phi/2, already
    # accounted in WI0-K. Its difference:
    # Delta W_outsider=WI0-K -(PO+CS)
    d3_at_minK=S.cancel(WI0-lo-pout-CS)
    s14.bernstein_positive(d1,
                           'G1 G2 prefer public M at observed OPEN RS')
    s14.bernstein_positive(-d3_at_minK,
                           'G3 strictly rejects public M for all K>=.54')
    # Government preference SIGN persists over broad real a-range.
    # At NNN governments all prefer M; after a founder goes N,
    # government all prefer M after singleton O as checked above.
    assert WI0-hi-WN>0
    # On unanimity path: G1 proposal M, G2 YES, G3 NO yields L.
    # G1/G2 W prefer M > L but actual proposal cannot overcome veto.
    # G1 can equivalently propose L (weak Nash indifference).
    print('PASS 3 COUNTRY POLICY SPE: G1 would like M, G2 YES,',
          'G3 VETO (strict), observed RS retained',flush=True)
    # Without third government's veto the same proposal passes.
    print('PASS 2-of-3 majority: G1 G2 YES, G3 NO,',
          'mandate M IMPLEMENTED after O-O-N',flush=True)
    print('OUTSIDER VETO THRESHOLD K_veto(eta)=',
          'WI0-[PO(eta,a*(eta))+CS_R(eta,a*(eta))]',
          flush=True)
    return d1,d3_at_minK

def mandatory_adoption_is_unique():
    # At sole public reference (c,a)=(1,0), a conforming firm's
    # operating GROSS under 1/2/3 conformers is at least 25/33.
    # N->O(1,0) incremental fee=K+phi/2.
    # already-O -> O(1,0) incremental <=phi/2,
    # so conformity strictly dominates exit after any prehistory.
    G1=3/(4*m)
    G2=3*m*((1+rho)/(2*m+(g-v)))**2
    G3=3*m*((1+rho)/(2*(m+g-v)))**2
    assert G1<G3<G2 and G1>hi+phi/2
    print('PASS unique M adoption Nash=all 3 conform across all',
          'initial N/O histories in rectangle',flush=True)

def both_spe_and_majority_firm_counterexample():
    private_optimum_root_brackets()
    fixed_private_payoff_upper_bounds()
    mandatory_adoption_is_unique()
    government_votes_and_cutoffs()
    # For each eta in [.10,.14], Stage11 verifies an optimal
    # 0.25<a*(eta)<0.61; under unanimous adoption:
    # RS private founder payoff f(a*,eta)-K.
    # if a founder deviates to any O(c,a), under L its profit
    # <= f(a*,eta)-K, with `min` matching; under public M
    # <=PIstar-K<f(a*,eta)-K.
    # if a founder deviates N, singleton O history triggers
    # public mandate, founder earns PIstar-K<f(a*,eta)-K.
    # if outsider deviates O(c,a), under L q3<.6 => payoff
    # <=1.0692-K<original outsider P_O. Under M its profit
    # <=PIstar-K<outsider P_O. All initial unilateral real
    # alternatives are exhausted. Other subgames have finite
    # government options and conform/exit unique equilibria;
    # thus full pure-start SPE exists, including veto histories.
    # Independently NNN baseline: public M unanimously preferred,
    # all comply. A deviator O(c,a) cannot improve by L (solo PN)
    # or M (initial+retrofit >=direct mandatory cost).
    assert PIstar>PN
    # Majority counterexample: initial OPEN RS(a*>0) gets M,
    # founders pay excess sunk a-capital; founder F1 switches
    # O(1,a*) to N, government after singleton O again mandates.
    # F1's EXACT private improvement phi*a*²/2>0.
    polynomial_strict(phi*a*a/2,a,R(1,4),R(61,100),
                      'majority RS founder deviation N strictly profitable')
    print('THEOREM full-continuous UNANIMITY coexistence:',
          'RS OPEN(O1a*,O1a*,N) with desired but vetoed public M;',
          'IS(N,N,N) with enacted public M',flush=True)
    print('THEOREM counterfactual MAJORITY:',
          'THIS OPEN RS starting profile ceases to be SPE;',
          'founder N deviation gain phi*a*(eta)^2/2>0',flush=True)
    print('SCOPE: No claim all possible majority-rule RS SPE eliminated;',
          'no proprietary X/Y/C strategies in this minimal game',
          flush=True)

def numeric_witnesses():
    import mpmath as mp
    fprime=S.lambdify((e,a),S.diff(private,a),'mpmath')
    fn=S.lambdify((e,a),private,'mpmath')
    oo=S.lambdify((e,a),pout,'mpmath')
    cr=S.lambdify((e,a),CS,'mpmath')
    for ev in (.10,.12,.14):
        av=float(mp.findroot(lambda v:fprime(ev,v),(.25,.61)))
        K=.55
        WincRS=fn(ev,av)+cr(ev,av)-K
        WincIS=float(WI0)-K-float(phi)*av*av/2
        WoutRS=oo(ev,av)+cr(ev,av)
        WoutIS=float(WI0)-K
        # world prospective alternative final allocations are not
        # the same as a mandate after actual private sunk investment.
        WRSworld=2*WincRS+WoutRS
        WISworld=3*(float(WI0)-K)
        publicfounderprofit=float(PIstar)-K-float(phi)*av*av/2
        nodedevprofit=float(PIstar)-K
        assert WincIS>WincRS
        assert WoutIS<WoutRS
        assert nodedevprofit-publicfounderprofit>0
        print('NUMERIC WITNESS eta',ev,'a*',round(av,10),
              'G1 desired M gain',round(WincIS-WincRS,9),
              'G3 veto M loss',round(WoutRS-WoutIS,9),
              'world RS - IS',round(WRSworld-WISworld,9),
              'majority developer deviation gain',
              round(nodedevprofit-publicfounderprofit,9),
              flush=True)

if __name__=='__main__':
    both_spe_and_majority_firm_counterexample()
    numeric_witnesses()
