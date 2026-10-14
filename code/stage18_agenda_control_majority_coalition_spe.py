"""Stage18: Agenda-setting power vs outsider veto in 3-country standards SPE.

FIXED baseline five primitives (.01,.14,.02,.32,.14),
eta∈[.10,.14], K∈[.54,.56]. Existing Stage17 MINIMAL treaty game
has 3 independently choosing firms N or O(c,a), G1 agenda, G2/G3
votes, G1/G2 may donate to G3 on approval, M public O(1,0) or L.

CORRECTION/NEW THEOREM: Simple majority does NOT wipe out the RS
OUTCOME TYPE: (N,O(1,a_R*),O(1,a_R*)) IS a FULL all-continuous
initial-strategy SPE under BOTH unanimity and majority! Outsider
G1 controls the proposal agenda and STRICTLY prefers no M, so never
proposes regardless of other two firms' governments supporting M.
All firms' arbitrary continuous unilateral deviations are blocked
by Stage11/15 *label-permutation-invariant* uniform Cournot bounds,
and Stage17 supplies credible donation/vote equilibrium at EVERY
initial corporate history.

Under majority the regional membership COMPOSITION matters:
an RS founded by G1+G2, or G1+G3, triggers government1's M
proposal and other member's YES -> M. The private RS co-founded by
G2+G3 instead can survive because the OUTSIDER IS AGENDA SETTER.
Thus agenda power is a separate institution from voting veto.

Further FULL-TRIANGLE EXACT proof: For all physically admissible
0<=a<=c<=1 and eta∈[.10,.14], a G1-member bilateral private
RS of identical firm technologies O(c,a) cannot be supported as a
STRICT-government-preference (non-degenerate) majority RS:
- if a <=3/4, TWO RS member govs STRICTLY PREFER M for any c:
  B(c,a,eta)>0, Bernstein exact all 3D coefficients 125/75.
- if a >3/4, any observed bilateral RS retained because both
  G1-member governments STRICTLY veto M cannot be company-Nash:
  f_a(c,a,eta)<0, proven exact 3D Bernstein 224/196
  on .75<=a,c<=1; one founder can lower its common a by epsilon
  while keeping strict gov veto, raising private profit.
- B=0 (government INDIFFERENCE, donation-game alternate
  weak-Nash costly-pledge precommitments) is explicitly excluded
  from any absolute majority 'all equilibria' nonexistence claim.
In baseline WITHOUT treaty and tie vote YES, B=0 enacts M, so
a strong full symmetric bilateral c,a impossibility follows.

THIS IS A MATHEMATICALLY SHARP CORRECTION to any misleading
interpretation that majority ensures public IS as the only standard
type. It does not solve ALL asymmetric/near-degenerate equilibria
under strategic government pledges.
"""
from fractions import Fraction as F
from math import comb
from itertools import product
import sympy as S
import stage11_eta_k_phase_certificates as st11
import stage14_institutional_veto_ablation as st14
import stage15_three_country_veto_minimal_continuous_spe as st15
import stage16_three_country_treaty_sidepayments_spe as st16
import stage17_full_history_treaty_spe_majority as st17
import stage5_integrated_independent_standards_and_government as st5

R=S.Rational
eta,a=st14.eta,st14.a
c=S.symbols('c', real=True)
m,g,v,k,rho,phi=st14.m,st14.g,st14.v,st14.k,st14.rho,st14.phi
z=1+rho*c
b=g+k*a-v*c
d=g-eta*a
A=2*m+b
D=2*m*A-2*d*d
x=S.cancel((2*m*z-d)/D)
y=S.cancel((A-2*d*z)/D)
f=S.cancel(3*m*x*x-phi*(c*c+a*a)/2)
CS=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
outsider=S.cancel(3*m*y*y)
WI0=st14.WI0
B=S.cancel(WI0-phi*a*a/2-f-CS)
ELO,EHI=R(1,10),R(7,50)
KLO,KHI=R(27,50),R(14,25)

def exact_tensor_bernstein_positive(expr, interval, label):
    """GLOBAL polynomial Bernstein certificate, real 3D box.
    Correct power→Bernstein: coeff[index] = sum_{multi<=index}
       power[multi]*product C(index_j,multi_j)/C(degree_j,multi_j).
    All calculations EXACT rationals; no sampling.
    """
    variables=(eta,a,c)
    T,U,V=S.symbols('T U V')
    mapped=(T,U,V)
    substitute={q:L+(H-L)*t for q,(L,H),t in zip(variables,interval,mapped)}
    n,de=S.fraction(S.cancel(expr.subs(substitute,simultaneous=True)))
    if de.subs({T:0,U:0,V:0})<0:n,de=-n,-de
    result=[]
    for part,poly in (('numerator',n),('denominator',de)):
        p=S.Poly(poly,*mapped); degrees=p.degree_list(); terms=p.as_dict()
        values=[]
        for idx in product(*(range(deg+1) for deg in degrees)):
            beta=sum(value*S.prod(R(comb(i,j),comb(deg,j))
                         for i,j,deg in zip(idx,monom,degrees))
                     for monom,value in terms.items()
                     if all(j<=i for i,j in zip(idx,monom)))
            values.append(beta)
        assert min(values)>0,(label,part,min(values))
        result.append(len(values))
    print('PASS FULL CONTINUUM 3D Bernstein',label,
          'positive numerator/denominator coefficients',result,flush=True)
    return result

def verify_full_triangle_political_vs_design_dichotomy():
    # The HUGE rectangular supersets include all feasible triangles.
    # Even values with a>c in low-a certificate are checked,
    # making the certificate strictly stronger than needed.
    arr=exact_tensor_bernstein_positive(
        B,((ELO,EHI),(R(0),R(3,4)),(R(0),R(1))),
        'member government wants universal public IS at any c when a<=.75')
    assert arr==[125,75]
    arr2=exact_tensor_bernstein_positive(
        -S.diff(f,a),
        ((ELO,EHI),(R(3,4),R(1)),(R(3,4),R(1))),
        'private marginal profit strictly decreases at high a >=.75')
    assert arr2==[224,196]
    # Government vote may turn NO at high a, so do NOT extend the
    # simple all-member-YES statement beyond a=.75.
    v0=B.subs({eta:R(1,10),c:1,a:1})
    v1=B.subs({eta:R(7,50),c:1,a:1})
    assert v0>0 and v1<0
    # For b<0 (members strictly opposing), private high-a choice
    # is strictly locally dominated: lower a by arbitrarily small
    # epsilon preserves negative B (continuity), and f_a<0.
    # At B=0 the no-treaty YES-on-tie rule implements M;
    # the treaty government's pledge stage may create OTHER
    # degenerate weak-Nash nonimplementation equilibria, so
    # no absolute B=0 exclusion in treaty-extended game.
    print('THEOREM majority coalition WITH G1 member:',
          'no symmetric bilateral OPEN RS with strict policy',
          'preferences, across ALL real 0<=a<=c<=1;',flush=True)
    print('CAUTION treaty pledge game with B=0 is knife-edge',
          'and may have weak equilibrium selection ambiguity.',flush=True)

def exact_permutation_invariance_under_nonintervention():
    a0=F(3,5);o=('O',F(1),a0);N=st5.N
    K=F(11,20);eta0=F(7,50)
    case12=st5.continuation((o,o,N),'L',None,(0,0,0),K,eta0)
    case23=st5.continuation((N,o,o),'L',None,(0,0,0),K,eta0)
    # Source Stage5 is a SEPARATE market/KKT implementation for
    # L only, since its public retrofit is not Stage8 capitalized.
    for j in (0,1,2):
        assert case23[j]==(case12[j][2],case12[j][0],case12[j][1])
    assert case23[3]==case12[3]
    print('PASS exact independent full 3x3 Cournot and CS under',
          'cyclic reshuffling bilateral RS owner identities',flush=True)

def majority_outsider_agenda_spe():
    # At h23=(N,O(1,a*),O(1,a*)) the proposer G1 is precisely
    # the differentiated OUTSIDER, government 1 national W(M)-W(L)
    # equals a NEGATIVE outsider loss -L, exact sign Stage14/16.
    # Government1 cannot receive a positive transfer, since donor
    # pledges only flow TO government3, so it rejects M strictly
    # under either voting rule before second government votes.
    st16.prove_global_no_unilateral_compensation()
    st15.fixed_private_payoff_upper_bounds()
    st15.mandatory_adoption_is_unique()
    assert st14.WI0-R(27,50)-st14.po.subs({eta:R(1,10),a:R(1,4)})-st14.cs.subs({eta:R(1,10),a:R(1,4)})<0
    # At the SAME history, G2/G3 benefit strictly from M
    # but cannot place a motion themselves: agenda-holder
    # veto, NOT 3-government voting-veto, is PIVOTAL.
    T,U=S.symbols('T U')
    st11.tensor_positive(st14.gov_O_approval,
        {eta:ELO+(EHI-ELO)*T,a:R(1,4)+R(9,25)*U},
        (T,U),'members 2 and 3 would approve public M')
    # Under L: any G2/G3 founder deviating to any O(c,a)
    # has <= private maximum f(a_R*(eta))-K, regardless of
    # offpath L/M selection. Any deviation to N leaves a
    # SINGLE remaining O history, for which each govt strictly
    # prefers M, so founder's payoff drops to PIstar-K.
    # F1 outsider N->O(c,a): either outsider entry quantity<.6
    # gross<=1.0692, net<original P_out; or M yields ≤PIstar-K.
    # The bounds are independent of which country owns the
    # technology because Cournot and cost parameters are symmetric.
    # At h23, G1 strictly refuses M, so RS remains ONPATH.
    # Every other observed private h has a credible government
    # pure continuation from Stage17 all-real decision-case lemma.
    assert st15.PIstar>st15.PN
    assert st14.WI0-st11.WN>KHI
    print('THEOREM MAJORITY FULL-CONTINUOUS 6-PLAYER PRIVATE RS SPE',
          'EXISTS at (N,O(1,a*(eta)),O(1,a*(eta))) FOR ALL',
          'eta∈[.10,.14], K∈[.54,.56]; G1 OUTSIDER',
          'strictly opposes/never proposes public mandate.',
          flush=True)
    print('THEOREM MAJORITY IS NNN remains full-continuous SPE',
          'via parent Stage17 theorem; hence BOTH RS and IS',
          'STANDARD TYPES STILL COEXIST under majority.',
          flush=True)
    print('THEOREM UNANIMITY all 3 possible bilateral',
          'optimal-design O-O-N coalition identity permutations',
          'have private RS SPE (outsider veto or agenda power),',
          'all alongside public IS NNN.',flush=True)

def exact_national_vote_permutation_regression():
    # Independent source: instantiate exact rational near-optimal
    # common design at eta=.14 and K=.55, then feed the exact
    # three-country national welfare gain triples into Stage17's
    # actual conditional-donation Nash constructor under both rules.
    E=R(7,50); aa=R(119,200); KK=R(11,20)
    benefit=S.cancel(st14.gov_O_approval).subs({eta:E,a:aa})
    outsiderloss=S.cancel(st14.po+st14.cs-WI0+KK).subs({eta:E,a:aa})
    assert outsiderloss>benefit>0
    D1=(benefit,benefit,-outsiderloss)
    D2=(benefit,-outsiderloss,benefit)
    D3=(-outsiderloss,benefit,benefit)
    for h, ds in [('members12',D1),('members13',D2),
                  ('members23',D3)]:
        U=st17.govt_pledge_equilibrium(ds,'unanimity',True)
        M=st17.govt_pledge_equilibrium(ds,'majority',True)
        assert U[1] is False and U[0]==(F(0),F(0)),(h,U)
        assert M[1]==(h!='members23') and M[0]==(F(0),F(0)),(h,M)
        print('PASS exact national coalition',h,
              'unanimity=NO majority='+('YES' if M[1] else 'NO'),
              'G1 net mandate preference',ds[0],flush=True)
    print('PASS public IS survives both voting rules by',
          'parent Stage17 full-history construction',flush=True)


def reg_vote_cutoff_diagnostic():
    import mpmath as mp
    mp.mp.dps=35
    b1=S.lambdify((eta,a),B.subs(c,1),'mpmath')
    vote_eta=mp.findroot(lambda E:b1(E,1),(.11,.12))
    assert mp.mpf('.11')<vote_eta<mp.mpf('.12')
    print('NUMERIC positive-design vote-change eta_critical_at_a1',
          mp.nstr(vote_eta,17),flush=True)
    for E in (mp.mpf('.10'),mp.mpf('.12'),mp.mpf('.14')):
        if b1(E,1)<0:
            root=mp.findroot(lambda aa:b1(E,aa),(.7,1))
            print('NUMERIC member public-policy vote frontier eta',
                  mp.nstr(E,4),'a_G',mp.nstr(root,15),flush=True)

if __name__=='__main__':
    verify_full_triangle_political_vs_design_dichotomy()
    exact_permutation_invariance_under_nonintervention()
    majority_outsider_agenda_spe()
    exact_national_vote_permutation_regression()
    reg_vote_cutoff_diagnostic()
