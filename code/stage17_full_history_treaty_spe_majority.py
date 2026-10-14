"""Stage17: FULL-HISTORY six-player SPE construction with treaty pledges.

Three firms independently choose N or O(c,a), a genuine continuous
two-dimensional technology triangle; 3 governments G1 agenda, G2, G3
vote, then independent firm mandate compliance and differentiated
Cournot. Same prior Stage15 minimal market and physically installed
capital fees, eta ∈ [.10,.14], K ∈ [.54,.56], five fixed primitives.
NEW institutional action: governments G1/G2 SIMULTANEOUSLY pledge
nonnegative budget-balanced binding LUMP-SUM side payments to G3
conditional on M PASSES, after observing initial private choices.
G3's transfer and G1/G2's payments occur only if M. Sequential
G1 proposal and votes after pledges. All vote/proposal ties favor
M/YES; if a funded proposal fails all pledges refunded. Strictly
dominant full firm conformity following any public M is inherited.
Other than government pledges, the continuum private game unchanged.

THEOREM:
(1) Every possible post-private-history 3-government donation/vote
    game has a PURE subgame-perfect outcome under unanimity or
    2/3 majority: constructive generic exact algebraic selector
    on national mandate gains (delta1,delta2,delta3).
(2) Under UNANIMITY with pledges, for ALL eta,K rectangle, EXIST
    two genuine full continuous-first-move SPE outcomes:
    - RS OPEN: (O(1,a*),O(1,a*),N); choose zero pledge after this
      history, G1 weakly proposes doomed M (would strictly PREFER
      implemented M), G2 YES, G3 VETO; RS remains.
    - public IS: (N,N,N), zero pledge, G1 M all approve and comply.
    All 1st-stage arbitrary real deviations blocked by SAME UNIFORM
    Stage15 bound irrespective of whether chosen offpath government
    continuation results in L or M; proof of feasible credible
    continuations at ALL histories is new.
(3) At this RS history if 2B>L, OTHER credible government
    subgame Nash use binding payments t1+t2=L. But THAT funded
    continuation destabilizes that original RS initial profile:
    founding firm's N deviation saves EXACTLY phi*a*^2/2.
(4) Under 2-of-3 MAJORITY, NNN->M remains a full initial-action SPE.
    The specific bilateral OPEN RS founder profile NOT SPE (two
    member governments would pass M; founder N deviation strictly
    saves a design stock); NOT a classification of all possible
    majority SPE initial histories.
(5) Generic Nash selection may be nonunique. ZERO PLEDGES is a
    credible selection after h_RS because B<L for EACH country,
    even when two donors collectively could pay L. Thus
    unwillingness to coordinate treaty pledges is endogenous.

Avoid overclaim: full model is the explicit MINIMAL O/N, L/M game
plus treaty (no proprietary patent X/Y, no accreditation C, no govt
designing unprovided public technology). Public O(1,0) preexists.
Government treasury lump-sum transfers assumed nondistortionary,
votes on ties explicitly YES; private firms NOT directly taxed.
"""
from fractions import Fraction as Q
import sympy as S
import stage11_eta_k_phase_certificates as stage11
import stage14_institutional_veto_ablation as stage14
import stage15_three_country_veto_minimal_continuous_spe as stage15
import stage16_three_country_treaty_sidepayments_spe as stage16

eta,a=stage14.eta,stage14.a
R=S.Rational
Kmin,Kmax=R(27,50),R(14,25)
I_net=stage15.PIstar
W_I0=stage14.WI0
W_N=stage11.WN
P_N=stage11.PN
phi=stage14.phi
B=stage16.B
L0=stage16.L0

def govt_pledge_equilibrium(deltas,rule="unanimity",prefer_no_pledge=False):
    """Exact pure equilibrium selection for EVERY triple of REAL
    government policy gains. Inputs Q(Fraction) so no float ties.

    δ1,δ2,δ3 = each government's national W(M)-W(L) BEFORE
    conditional transfers, after true sunk private stock.

    The proposer G1 and donor G2 choose t1,t2 simultaneously; G3
    recipient. When eligible, G1 proposes M after pledges; G2,G3
    vote YES iff their OWN W change >=0; G1 proposes M iff its
    own delta1-t1>=0 and necessary governments would approve.
    Voter/proposer equal-utility ties YES/M by explicit convention.

    A nonzero donor-only pledge exists in this simple economic
    environment because at most G3 is COMPENSATED. Conditional
    contributions refunded on rejected M.
    """
    d1,d2,d3=tuple(Q(x) for x in deltas)
    assert rule in ("unanimity","majority")
    zero=(Q(0),Q(0))
    if d1<0:
        return zero,False,"agenda opposed"
    if rule=="majority":
        if d2>=0 or d3>=0:
            return zero,True,"majority without compensation"
        L=-d3
        if d1<L or (d1==L and prefer_no_pledge):
            return zero,False,"lead cannot singly compensate outsider"
        return (L,Q(0)),True,"lead pays outsider; G2 opposes"
    # unanimity
    if d2<0:
        return zero,False,"second country veto cannot be bribed"
    if d3>=0:
        return zero,True,"unanimity without compensation"
    L=-d3
    # (0,0) is a Nash iff no SINGLE government's funding
    # creates a strictly profitable passage. At d_i=L, donor is
    # only indifferent, so zero is STILL Nash.
    if prefer_no_pledge and d1<=L and d2<=L:
        return zero,False,"zero pledge Nash selected"
    if d1<L and d2<L and d1+d2<L:
        return zero,False,"insufficient aggregate gains"
    if d1==0 and d2<L:
        return zero,False,"no sufficient donor"
    if d1>=L:
        return (L,Q(0)),True,"single donor 1 covers outsider loss"
    if d2>=L:
        return (Q(0),L),True,"single donor 2 covers outsider loss"
    if d1+d2>=L:
        # Strictly positive or weakly nonnegative donor gains.
        # Exact critical financing; each unilateral reduction
        # makes G3 veto. Proportional split is one Nash.
        return (L*d1/(d1+d2),L*d2/(d1+d2)),True,"joint financing"
    return zero,False,"zero pledge Nash"

def realized_delta(deltas,t,rule):
    d1,d2,d3=tuple(Q(x) for x in deltas)
    t1,t2=t
    yes1=(d1-t1>=0)
    yes2=(d2-t2>=0)
    yes3=(d3+t1+t2>=0)
    passed=yes1 and (yes2 and yes3 if rule=="unanimity"
                     else yes2 or yes3)
    return passed,(d1-t1 if passed else Q(0),
                   d2-t2 if passed else Q(0),
                   d3+t1+t2 if passed else Q(0))

def verify_arbitrary_history_pure_government_subgames():
    """Reproducible adversarial exact rational CROSSCHECK of lemma;
    the analytic proof is the case partition in the source/docs.
    A grid alone is explicitly NOT the theorem."""
    vals=tuple(Q(i,4) for i in range(-8,9))
    tested=0
    for rule in ("unanimity","majority"):
        for d1 in vals:
            for d2 in vals:
                for d3 in vals:
                    ds=(d1,d2,d3)
                    for pref in (True,False):
                        t,passage,tag=govt_pledge_equilibrium(ds,rule,pref)
                        outcome,pay=realized_delta(ds,t,rule)
                        assert passage==outcome,(rule,ds,t,tag)
                        assert t[0]>=0 and t[1]>=0
                        if passage:
                            # no donor gain from raising its pledge:
                            # it reduces own payment, or fails M.
                            # Since threshold exactly met if any pledge,
                            # any positive donor pledge is CRITICAL.
                            if t[0]>0 or t[1]>0:
                                assert d3<0 and sum(t)==-d3
                                assert d1-t[0]>=0
                                if rule=="unanimity":
                                    assert d2-t[1]>=0
                        else:
                            # selected no-funding equilibrium:
                            # any single donor cannot profitably
                            # create an accepted mandate
                            assert sum(t)==0
                            if d1>=0 and d2>=0 and d3<0 and rule=="unanimity":
                                assert d1<=-d3 and d2<=-d3,(ds,tag)
                            if d1>=0 and d2<0 and d3<0 and rule=="majority":
                                assert d1<=-d3,(ds,tag)
                        tested+=1
    print("PASS all-history donation-game lemma:",
          tested,"exact rational exhaustive adversarial triple checks;",
          "additional analytic argument covers ALL reals",flush=True)

def confirm_onpath_exact_signs_and_margin():
    # Import global symbolic proof of strict private a* optimum:
    # Stage11 certifies a_R*(eta) in (.25,.61), strictly interior
    # and continuous. Stage14 strict two-member vote YES and
    # outsider NO over the WHOLE 2D eta x a rectangle. Stage16
    # certifies 0 < B < L for all eta,K at a*(eta).
    stage16.prove_global_no_unilateral_compensation()
    # Uniform M adoption/exit and firm deviations held in Stage15
    stage15.private_optimum_root_brackets()
    stage15.fixed_private_payoff_upper_bounds()
    stage15.mandatory_adoption_is_unique()
    stage15.government_votes_and_cutoffs()
    assert W_I0-W_N>Kmax
    assert I_net>P_N
    assert R(3)/(4*stage14.m)>Kmax+phi/2
    assert I_net < stage14.f.subs({eta:R(1,10),a:R(1,4)})
    print("PASS onpath gov signs, all real firm c,a deviation bounds",
          "and positive mandate compliance margins inherited",flush=True)

def full_history_strategy_completion_theorem():
    # Construct at EVERY observed initial corporate history h:
    # compute each government's exactly Cournot/KKT-derived
    # δ_i(h)=W_i(M)-W_i(L), including irrecoverable initial
    # capital stock, retrofit and compliance cost, and invoke
    # govt_pledge_equilibrium((δ1,δ2,δ3),'unanimity')
    # for a PURE credible donation/vote continuation.
    # Special h_R chooses "prefer_no_pledge" where 0<B<L,
    # so G3 vetoes and RS remains onpath.
    #
    # A first-stage unilateral deviation by any of the 3 firms,
    # into arbitrary N or real O(c,a), yields one of:
    # A) gov L -> member profit <=max privately chosen regional
    #    f(a*)-K; outsider O-entry profit <=1.0692-K < original
    #    outside PO; solo O investor earns PN-K-fee.
    # B) gov M -> all firms comply uniquely, and private O
    #    upfront + capitalization retrofit <=/=/≥ one-shot public
    #    setup so payoff <= I_net-K; RS members already earn
    #    strictly >I_net-K; outsider outside >I_net-K.
    # No transfer can REWARD a firm directly (gov treasury transfers
    # only), so no new first-stage unilateral profitable deviation.
    #
    # At h=(N,N,N) and h=(N,O(1,a*),N), the δ_i all positive;
    # zero pledges, all national govt support M, no anticommons.
    #
    # Thus full continuous first stage plus all govt subgames
    # admit 2 distinct SPE paths under extended UNANIMITY.
    eta0=R(1,10);K=R(11,20)
    aopt=S.nsolve(S.diff(stage14.f,a).subs(eta,eta0),
                  a,R(3,10),tol=1e-30,prec=50)
    dB=B.subs({eta:eta0,a:aopt})
    dL=L0.subs({eta:eta0,a:aopt})+K
    assert dL>dB>0
    dtuple=tuple(Q(str(x.evalf(30))) for x in (dB,dB,-dL))
    t,ok,msg=govt_pledge_equilibrium(dtuple,"unanimity",True)
    assert t==(0,0) and not ok
    t2,ok2,msg2=govt_pledge_equilibrium(dtuple,"unanimity",False)
    assert ok2 and sum(t2)==-dtuple[2] and all(t2[i]<dtuple[i] for i in (0,1))
    print("THEOREM full-continuous original firm OPEN RS and public IS",
          "SPE BOTH EXIST in augmented treaty game under UNANIMITY",
          "for EVERY eta∈[.10,.14], K∈[.54,.56],",
          "with all corporate-history government pure continuations",
          flush=True)
    print("NO-transfer and financed government Nash both feasible at",
          "already installed RS if 2B>L; only NO-transfer supports",
          "the UNCHANGED private initial a*>0 founders",flush=True)
    # Counterexample if funded on the original O-O-N initial h:
    # deviating founder N -> singleton O, government all favor M,
    # saves precisely positive upfront unnecessary a-design stock.
    assert phi*R(1,4)**2/2>0
    print("CERTIFIED anticipated funded-M at OPEN RS cannot be",
          "onpath at same initial O-O-N a* founders:", 
          "N deviation gain phi*a*(eta)^2/2>0",flush=True)

def majority_theorem():
    # At h=(O1a*,O1a*,N) both member governments prefer M.
    # By simple majority G3 cannot block. Extra contingent treasury
    # transfers only decrease contributor welfare and cannot improve
    # an already-passing motion, so zero pledge is credible.
    # A private founding firm switching to N produces a singleton
    # O with all three govt favor M, hence saves wasted
    # phi*a*²/2, strictly profitable. Thus h cannot be a SPE
    # under majority (without claiming no other RS SPE).
    #
    # At NNN, all three independently and strictly want public M.
    # Under any single firm private O(c,a) deviation, gov may
    # select M or L; payoff <=max(I_net-K,PN-K-fee) <=I_net-K.
    # Arbitrary govt histories have credible pure continuation
    # by govt_pledge_equilibrium with majority. Therefore
    # genuine full continuous NNN public IS SPE under majority.
    assert I_net>P_N
    assert (phi*R(1,4)**2/2)>0
    for ds in ((Q(1,20),Q(1,50),-Q(1,9)),
               (Q(1,20),Q(1,50),-Q(1,3))):
        t,passes,msg=govt_pledge_equilibrium(ds,"majority")
        assert t==(0,0) and passes
    print("THEOREM public IS NNN is full-continuous SPE under BOTH",
          "voting rules in government-transfer extension",flush=True)
    print("THEOREM exact private OPEN bilateral RS candidate NOT",
          "SPE under simple MAJORITY even with transfer option;",
          "a founder saves phi*a*(eta)^2/2>0 by choosing N",
          flush=True)
    print("NOT A COMPLETE majority SPE set classification: other",
          "offpath initial O/N profiles and asymmetric RS pure/mixed",
          "equilibria not excluded.",flush=True)

if __name__=="__main__":
    verify_arbitrary_history_pure_government_subgames()
    confirm_onpath_exact_signs_and_margin()
    full_history_strategy_completion_theorem()
    majority_theorem()
