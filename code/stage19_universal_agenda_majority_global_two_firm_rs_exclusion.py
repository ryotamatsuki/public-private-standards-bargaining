"""STAGE 19 — extend regulatory initiative from G1 to G1,G2,G3.

MAIN PROPOSITION (exhaustive relative to exactly TWO OPEN O inventors
and one N, full real 0<=a_i<=c_i<=1, final no-intervention L):
When ALL national governments can independently propose the same
lawfully pre-existing public standard O(1,0), and 2-of-3 majority
approves, NO bilateral private O/O/N regional-standard L outcome can
be a pure-strategy full six-player SPE. This includes DIFFERENT
initial c_i/a_i, not only symmetric pair private optimum.

The result is an exact logical consequence of:
  1. A high a_i relative to its partner's a_j is wasted: reducing
     a_i down to a_j leaves common pair min(a_i,a_j) unchanged,
     keeps all government POLICY DIFFERENCES δ_i identical, and
     saves phi/2*(a_i**2-a_j**2)>0 privately under L and M.
  2. Once a_i=a_j, c_i>c_j is wasted if final L: reducing
     c_i to c_j preserves shared market b,d,z, saves real upfront
     phi/2*(c_i**2-c_j**2), while weakly REDUCING the firm's own
     national desire for public M (all other δ remain unchanged).
     Passing coalition cannot emerge from this change if L
     previously held. Thus any L bilateral O/O/N SPE must have
     identical c,a between the two private participants.
  3. For symmetric O(c,a), independent exact 3D rational Bernstein
     on all eta∈[.10,.14],c∈[0,1],a∈[0,.75] proves both member
     governments strictly prefer public M over L; one member
     possesses an initiative right and the other votes YES, so M.
     This also covers ALL a=0 and c=0 equal design cases.
  4. For a>.75 and c>=a, if the member governments do not have
     a majority strictly/wkly preferring M, they have B(c,a)<0
     (since symmetric government payoffs). Independent Bernstein
     on whole eta∈[.10,.14],a,c∈[.75,1] proves f_a<0. One firm
     reduces own a_i slightly, raising private profits, preserving
     strictly negative member-government B and therefore L.
     At B(c,a)=0, government ties resolved M/YES, so M enacted;
     no degenerate knife-edge exception in this NO-TRANSFER game.
  5. Pure government sequential proposal/voting continuations
     exist at ALL uncountably many initial private histories by
     finite backward induction, and post-M firm conformity
     is strictly dominant (Stage15).

Important no-transfer simplification: NO conditional treasury pledges
in THIS institutional comparator, to avoid weak-Nash donation
selection; proprietary X/Y and private C accreditation also removed.
Earlier transfer-enhanced Stage17/18 results are VALID but separate.
Stage18's full 3D polynomial certificates re-executed by CI.

PARAMETER RECTANGLE exactly eta∈[.10,.14], K∈[.54,.56], with
(v,gamma0,kappa,rho,phi)=(.01,.14,.02,.32,.14).
No inference all initial-action SPE (including 3 O and strange
partial technologies) are public IS; only NO two-O/one-N L-RS.

Other 2x2 institutional regimes preserve public IS NNN->M SPE,
and genuine privately optimized RS O/O/N SPE when unanimous
(3 national-pair permutations) or exclusive G1 agenda+majority
(exactly G2/G3 pair from previous result).
This yields exact institutional interaction, not a proof all
asymmetric fully diversified standard-splitting equilibria absent.
"""
import sympy as S
from fractions import Fraction as F
from itertools import combinations
import stage11_eta_k_phase_certificates as st11
import stage14_institutional_veto_ablation as st14
import stage15_three_country_veto_minimal_continuous_spe as st15
import stage18_agenda_control_majority_coalition_spe as st18
import stage5_integrated_independent_standards_and_government as st5

R=S.Rational
eta,a,c=st18.eta,st18.a,st18.c
m,phi=st14.m,st14.phi
KLO,KHI=R(27,50),R(14,25)
ELO,EHI=R(1,10),R(7,50)

def public_vote_outcome(delta,proposal_rights,rule):
    """FULL normal-continuation decision rule in the no-transfer
    minimal game, after arbitrary initial corporate history. δ_i
    already includes all sunk tech and public retrofit real cost.
    EQUALITY convention: propose YES and vote YES at δ_i=0.
    No party can pay/receive a side transfer here.
    """
    assert rule in ('unanimity','majority')
    num=sum(x>=0 for x in delta)
    quorum=3 if rule=='unanimity' else 2
    can_propose=any(delta[i]>=0 for i in proposal_rights)
    return num>=quorum and can_propose

def exact_private_high_a_tech_dominance_lemma():
    # Exact symbolic Cournot market at pair common (c0,a0).
    # Demonstrate that founder own redundant a cannot change the
    # national POLICY GAIN of ANY country, and its owner gains
    # cost savings under BOTH L and M.
    c0,a0=S.symbols('c0 a0', nonnegative=True)
    ci,ai,low_ai=S.symbols('ci ai low_ai', nonnegative=True)
    K=S.symbols('K',nonnegative=True)
    gross=S.symbols('G',real=True)
    cs=S.symbols('CS',real=True)
    WI0=st14.WI0
    L_old=gross-K-phi*(ci*ci+ai*ai)/2
    L_new=gross-K-phi*(ci*ci+low_ai*low_ai)/2
    M_old=st15.PIstar-K-phi*ai*ai/2
    M_new=st15.PIstar-K-phi*low_ai*low_ai/2
    dL=S.factor(L_new-L_old)
    dM=S.factor(M_new-M_old)
    assert S.factor(dL-phi*(ai*ai-low_ai*low_ai)/2)==0
    assert S.factor(dM-dL)==0
    W_L_old=L_old+cs
    W_L_new=L_new+cs
    W_M_old=WI0-K-phi*ai*ai/2
    W_M_new=WI0-K-phi*low_ai*low_ai/2
    # Policy preference invariant, so govt action unchanged.
    assert S.factor((W_M_new-W_L_new)-(W_M_old-W_L_old))==0
    print('PASS exact asymmetric wasted a_i proof:',
          'replace larger a_i by min(a_i,a_j), market unchanged,',
          'policy preference unchanged, strict private saving',
          'phi*(ai^2-aj^2)/2',flush=True)

    # With a_i equalized, founder higher compatibility c_i can
    # lower c_i toward partner c_j while their shared pair min(c)
    # stays unchanged. M installation final capital phi/2*(1+a²)
    # is independent of original c_i; L initial capital goes down,
    # so owner's policy M-L difference DECREASES, and no new
    # regulatory majority may emerge from an observed L.
    cl=S.symbols('cl',nonnegative=True)
    aa=S.symbols('aa', nonnegative=True)
    L_old=gross-K-phi*(ci*ci+aa*aa)/2
    L_new=gross-K-phi*(cl*cl+aa*aa)/2
    M_old=M_new=st15.PIstar-K-phi*aa*aa/2
    delta_old=M_old-(L_old+cs)
    delta_new=M_new-(L_new+cs)
    assert S.factor(delta_old-delta_new
                    -phi*(ci*ci-cl*cl)/2)==0
    assert S.factor(L_new-L_old
                    -phi*(ci*ci-cl*cl)/2)==0
    print('PASS exact asymmetric wasted c_i proof:',
          'policy adoption delta_i weakly drops, status quo',
          'L payoff strictly rises',flush=True)

def verify_independent_asymmetric_cournot():
    # Independent exact Fraction Gauss+KKT implementation Stage5,
    # L branch ONLY (Stage5's C/M upgrade cost isn't Stage8 fee).
    # Two private firms O(1,.8), O(.8,.6), and outsider N.
    A=('O',F(1),F(4,5))
    B=('O',F(4,5),F(3,5))
    A_low_a=('O',F(1),F(3,5))
    A_low_c=('O',F(4,5),F(3,5))
    N=st5.N;K=F(11,20);E=F(7,50)
    p0=st5.continuation((A,B,N),'L',None,(0,0,0),K,E)
    pa=st5.continuation((A_low_a,B,N),'L',None,(0,0,0),K,E)
    pc=st5.continuation((A_low_c,B,N),'L',None,(0,0,0),K,E)
    assert p0[2]==pa[2]==pc[2]  # Cournot output EXACT same.
    assert p0[3]==pa[3]==pc[3]  # exact consumer surplus.
    assert pa[0][0]-p0[0][0]==F(7,50)/2*(F(4,5)**2-F(3,5)**2)
    assert pc[0][0]-pa[0][0]==F(7,50)/2*(F(1)**2-F(4,5)**2)
    print('PASS separate exact Fraction 3x3 asymmetric',
          'Cournot L profit and national CS after a and c',
          'redundancy removal',flush=True)

def verify_3d_polynomial_necessity():
    # Re-execute Stage18 exact non-grid global results:
    # all a<=.75 -> BOTH founder member governments B>0
    # a>.75,c>=a -> f_a<0 (unless M already enacts).
    st18.verify_full_triangle_political_vs_design_dichotomy()
    # Verify B(c,a) and private marginal objects use the same
    # original reduced Stage15 Cournot payoff x(c,a),y(c,a).
    assert S.factor(st18.B - (st14.WI0-phi*a*a/2
                    -(st18.f+st18.CS)))==0
    assert S.factor(S.diff(st18.f,a).subs(c,1)
                    -S.diff(st11.PR.subs(st11.c,1),st11.a))==0
    print('PASS exact data provenance: Stage18 symmetric pair',
          'matches original Stage11 private payoff on c=1',flush=True)

def construct_four_full_policy_regimes():
    # At privately optimal c=1, 0.25<a*(eta)<0.61,
    # Stage14 strict 2D Bernstein: each RS insider wants M,
    # outsider strictly rejects it. Any identity permutation
    # produces policy gains (B,B,-L) with B>0,L>0.
    # At NNN: all gov gain WI0-K-WN>0 and approve M.
    b=R(1,20)    # symbolic representative B>0
    l=R(1,10)    # symbolic representative L>0
    gain={
        (0,1):(b,b,-l),
        (0,2):(b,-l,b),
        (1,2):(-l,b,b),
    }
    for rule in ('unanimity','majority'):
        for rights,label in (((0,), 'G1 exclusive'),
                             ((0,1,2),'all three entitled')):
            result={pair:public_vote_outcome(delta,rights,rule)
                    for pair,delta in gain.items()}
            count=sum(not x for x in result.values())
            if rule=='unanimity':assert count==3
            elif label=='G1 exclusive':assert count==1
            else:assert count==0
            print('PASS actual full 2x2 institutional',
                  'policy comparison',rule,label,
                  'RS retained pair count',count,'by pair',result,
                  flush=True)

    # Private RS over all permutations: under majority/open
    # agenda each 2member profile triggers M and is NOT an RS SPE.
    # For a_R*>0 its founder can instead N before eventual
    # public M, avoiding precisely positive wasted design fee.
    # Parent Stage15 already proves singleton O after one
    # founder switches to N leads UNANIMOUS M.
    assert st14.WI0-st11.WN>KHI
    assert st14.WI0-st11.WN+phi/2>0
    # NNN public IS survives any public agenda/voting reform,
    # with strict all-government desire to mandate.
    assert st15.PIstar>st15.PN
    assert st14.WI0-KHI-st11.WN>0
    print('PASS public IS NNN -> M genuine SPE survives',
          '4 constitutional variants; Cournot firm unilateral',
          'deviation bounds independent of proposal rights',flush=True)

def global_majority_complete_bilateral_rs_exclusion():
    exact_private_high_a_tech_dominance_lemma()
    verify_independent_asymmetric_cournot()
    verify_3d_polynomial_necessity()
    construct_four_full_policy_regimes()
    # Logical proof with ALL continuous asymmetric actions:
    # Suppose exactly TWO O investors, one N, with L as
    # after-political outcome in hypothetical majority+all-agenda
    # SPE. Any unequal a -> high a founder lowers it preserving
    # all market, δ and policy outcome, strictly improving pay.
    # Then equal a and unequal c -> high c founder can lower it,
    # preserving pair min and reducing own positive M-L delta.
    # As L previously obtained and majority approval is monotone
    # increasing in national δ, L still obtains, firm strictly
    # gains. Thus candidate must be symmetric common c,a.
    # If a<=.75, B>0 for both founders by 3D exact Bernstein:
    # a member proposes M, other votes YES, M passes majority,
    # contradiction to L. If a>.75 and B>=0, same contradiction.
    # If a>.75 and B<0, continuity gives small epsilon decrease
    # in founder's a, keeps member B<0 and L, yields strictly
    # increased private firm payoff by exact derivative f_a<0.
    # No pure SPE initial history with exactly 2 O+1 N and
    # final L is possible in this model. No boundary B=0
    # exception because all policy ties M/YES.
    print('MAIN THEOREM EXACT GLOBAL TWO-O ONE-N EXCLUSION:',
          '3-country SIMPLE MAJORITY + UNIVERSAL PROPOSAL',
          'RIGHTS yields NO private bilateral OPEN RS SPE',
          'for ANY real pair O(c1,a1), O(c2,a2)',
          '0<=ai<=ci<=1, full eta [.10,.14],K [.54,.56],',
          'under NO TREATY transfers.',flush=True)
    print('LIMIT: IS=N,N,N public-M SPE PROVED, not exclusive;',
          'all-3-O partial technologies, novel asymmetric standards',
          'or mixed initial equilibrium outcomes not classified.',
          flush=True)

if __name__=='__main__':
    global_majority_complete_bilateral_rs_exclusion()
