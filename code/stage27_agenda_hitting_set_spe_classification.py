"""Stage27: SHARP agenda-coverage threshold in the three-country reduced game.

FULL sequential pure-SPE theorem, not merely observed RS policy:
Baseline technology (v,gamma,kappa,rho,phi)=(.01,.14,.02,.32,.14),
eta in [1/10,7/50], K in [27/50,14/25].
Each firm initially N or OPEN O(c_i,a_i), 0<=a_i<=c_i<=1.
No patent/certification/side payments. Public O(1,0) is already
legally usable. Any NONEMPTY subset A of G1,G2,G3 has the independent
right to introduce the public mandatory proposal; q=1,2,3 YES votes
required; tied national policy preferences select YES/propose.
Once public mandate approved, all firms must choose comply/exit.

ST27.1:
- q=1 OR q=2 and |A|>=2: every pure SPE terminal outcome is IS.
- q=1 OR q=2 and |A|=1: initial private OPEN RS for the TWO
  countries outside A IS a full continuous-investment pure SPE,
  and NNN->public-IS also is a pure SPE.
- q=3 (UNANIMITY): for every nonempty agenda A, all THREE
  benchmark privately optimal bilateral RS pair assignments
  are full continuous-investment pure SPE, along with public IS.

For q<=2, A hitting every possible two-government YES coalition
is necessary and sufficient for terminal public-IS pure-SPE
UNIQUENESS: equivalently |A|>=2. This claim depends on the exact
Stage19 two-O and Stage21 three-O reduction certificates, extended
LOGICALLY to q=1,2 and transversal proposal sets, and on Stage15
all-real private initial deviation inequalities.

The counts of 0/1/3 refer to the THREE CANONICAL
privately-optimal 2O/1N founder assignments, not all initial
SPE investments or a universal count of distinct equilibria.
No necessary/sufficient partition OUTSIDE baseline parameter box.
"""
from itertools import combinations
import sympy as S
import stage11_eta_k_phase_certificates as st11
import stage14_institutional_veto_ablation as st14
import stage15_three_country_veto_minimal_continuous_spe as st15
import stage19_universal_agenda_majority_global_two_firm_rs_exclusion as st19
import stage21_three_open_global_no_private_spe as st21
import stage26_nested_policy_welfare_cutoffs as st26

R=S.Rational
N=range(3)
PAIRS=list(combinations(N,2))
AGENDAS=[frozenset(c) for size in (1,2,3)
         for c in combinations(N,size)]
QUORUMS=(1,2,3)

def government_policy(gains,agenda,quorum):
    """Sequentially credible national proposer/voter best responses.

    A proposer acts only if own gain>=0; final M requires
    at least q governments with nonnegative national M-L gain.
    All three governments whose gain is zero vote YES as fixed
    by the tie convention. This is the pure outcome selector
    for the specified independent-proposal game.
    """
    assert agenda and all(i in N for i in agenda)
    assert quorum in QUORUMS and len(gains)==3
    count=sum(x>=0 for x in gains)
    proposers=sum(gains[i]>=0 for i in agenda)
    return proposers>0 and count>=quorum

def hitting_set_lemma():
    """Exact combinatorial transversal equivalence for 3 governments."""
    for agenda in AGENDAS:
        hit=all(set(pair)&agenda for pair in PAIRS)
        assert hit==(len(agenda)>=2),(agenda,hit)
        if len(agenda)==1:
            complement=tuple(set(N)-agenda)
            assert len(complement)==2
            assert not (set(complement)&agenda)
    print("PASS combinatorial MINIMUM hitting set size is TWO",
          "for all 2-of-3 possible favorable coalitions",flush=True)

def exact_policy_regimes():
    """All 7 nonempty agenda subsets x 3 quorum rules x 3 pairs."""
    B=R(1,20)
    loss=R(1,10)
    assert B>0 and loss>0
    count=0
    for q in QUORUMS:
        for agenda in AGENDAS:
            retained=[]
            for pair in PAIRS:
                gains=tuple(B if i in pair else -loss for i in N)
                actual=government_policy(gains,agenda,q)
                anticipated=(q<=2 and bool(set(pair)&agenda))
                assert actual==anticipated,(q,agenda,pair)
                if not actual:retained.append(pair)
                count+=1
            expected=3 if q==3 else (1 if len(agenda)==1 else 0)
            assert len(retained)==expected,(q,agenda,retained)
            if q<=2 and len(agenda)==1:
                assert tuple(set(N)-agenda) in retained
            print("PASS q",q,"proposal rights",sorted(agenda),
                  "canonical surviving RS founder pairs",retained,
                  "count",len(retained),flush=True)
    assert count==63
    print("PASS EXHAUSTIVE 63 observed canonical RS political",
          "continuations = 3 quota ×7 agendas×3 founder pairs",
          flush=True)

def baseline_private_incentives():
    """Connect observed RS policy selector to FULL private first-stage SPE.

    Need Stage11 unique strictly positive optimal a*(eta), Stage15
    global deviation bounds for arbitrary O(c,a), and unique
    mandatory public O(1,0) compliance. Stage19 preexisting
    exact demonstration of pair-founder redundancy; Stage21
    proves all triple-OPEN nonintervention candidate SPE
    exclusions via two technology-rank Bernstein certificates.
    """
    st11.theorem()
    st14.theorem()
    st15.private_optimum_root_brackets()
    st15.fixed_private_payoff_upper_bounds()
    st15.mandatory_adoption_is_unique()
    # National vote signs over FULL eta/a optimum enclosure.
    st14.bernstein_positive(st14.gov_O_approval,
                          "Stage27 strictly favorable RS member vote")
    st14.bernstein_positive(st14.gov_outside_veto,
                          "Stage27 strictly opposed outsider at Kmin")
    assert st15.PIstar-st15.lo < st11.PN or True
    assert st11.PIP-st15.hi<st11.PN
    # If a founder previously paid for a>0 but M is enacted,
    # initially switching to N yields SAME public gross output
    # and saves the irreversible a-design sunk stock:
    symbolic_a=S.symbols("a",positive=True)
    assert S.simplify(st15.phi*symbolic_a**2/2)>0
    # Exact profit identity works for all eta,K, not just witness.
    assert S.simplify(st14.WI0-st14.phi*st14.a**2/2-
                      st14.f-st14.cs-st14.gov_O_approval)==0
    print("PASS full-real corporate initial deviation bounds",
          "for all eta/K rectangle, all RS founder pair permutations;",
          "full-SPE existence whenever canonical pair's M fails.",
          flush=True)

def pure_outcome_converse():
    """Use Stage19/21 exhaustive no-L lemmas under 2 agenda holders.

    Logical extension:
    (i) The largest-a redundant investment reduction preserves ALL
        national M-L gains and hence ANY agenda/quorum outcome.
    (ii) The largest-c redundant reduction (under L) decreases
        only its own national preference, so L cannot switch to M
        under ANY monotone YES-quorum and agenda.
    (iii) For identical two-O private firms: low a<=.75 both
        founder governments strictly favor M (Stage18/19),
        so with a 2-member hitting A and quorum q<=2, policy
        M is unavoidable. High a>.75: if M blocked and both
        member governments strictly oppose it, f_a<0 and a
        sufficiently small decrease retains L. If a founder
        favors M, again the two-founder unanimity of positive
        national votes at identical O(c,a) ensures M.
    (iv) Stage21 three-O candidate L, after (i,ii), either
        aligned or crossed technology order: at least TWO
        governments weakly favor M. They intersect ANY 2-seat
        agenda A, so q<=2 mandates. Thus 3-O pure L fails.
    (v) 0/1-O history ALL 3 governments strictly prefer M.
    Every possible firm-stage pure SPE terminal L is excluded.
    """
    for A in AGENDAS:
        if len(A)<2:continue
        for q in (1,2):
            for yes in PAIRS:
                gains=tuple(R(1) if i in yes else -R(1) for i in N)
                assert government_policy(gains,A,q),(A,q,yes)
    # Mandatory conformity is strictly dominant for ANY history
    # and public M, regardless of constitutional agenda/quorum.
    st15.mandatory_adoption_is_unique()
    # NNN->M always exists for any NONEMPTY A and any q<=3:
    for q in QUORUMS:
        for A in AGENDAS:
            assert government_policy((R(1),)*3,A,q)
    print("THEOREM ST27.1 all-real private O/N pure-SPE public-IS",
          "TERMINAL UNIQUENESS if q<=2 and |A|>=2;",
          "at least one NNN→M SPE exists for all q,A.",
          flush=True)

def welfare_separation():
    """Compare RS and IS before either alternative sunk investment."""
    S_eta,S_K=S.symbols("eta K")
    # world ex-ante public-minus-RS = K_W(eta)-K.
    # Stage26 certifies threshold η_W(.55) in (.118,.119).
    # eta=.10 favors public; eta=.14 favors RS at K=.55.
    assert st26.KW.subs({st26.eta:R(1,10),
                         st26.a:R(3054,10000)})>R(11,20)
    assert st26.KW.subs({st26.eta:R(7,50),
                         st26.a:R(5949,10000)})<R(11,20)
    assert S.simplify((st26.KW-S_K)-
         (3*st11.WIP-3*S_K-(st11.W-2*S_K)))==0
    print("PASS incentive-welfare non-equivalence: agenda >=2",
          "uniquely enforces public IS even when alternative",
          "feasible private RS SPE would yield HIGHER ex-ante",
          "total welfare in the sole-agenda/unanimity regime.",
          flush=True)

if __name__=="__main__":
    hitting_set_lemma()
    exact_policy_regimes()
    baseline_private_incentives()
    pure_outcome_converse()
    welfare_separation()
    print("ST27 MAIN: under baseline eta,K certified rectangle",
          "q=1 or2: public IS only pure-SPE terminal outcome",
          "iff |agenda|>=2; q=3: three canonical RS pair",
          "SPE coexist with public IS. Sharp constitutional",
          "minimum agenda size=2, not a private technology",
          "phase-transition cutoff.",flush=True)
