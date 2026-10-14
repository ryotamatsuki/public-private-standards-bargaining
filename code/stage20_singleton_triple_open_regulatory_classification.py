"""Stage20: complete the 0/1-O and symmetric 3-O government policy cases.

Continuous MINIMAL 3 firms/3 national govs standards model; public
O(1,0), no treaty transfers, all govs MAY independently move M,
2/3 national majority approval. Firms choose N or ANY O(c_i,a_i)
with 0<=a_i<=c_i<=1. Existing capital remains sunk and within
open O-family retrofitting pays positive additional physical stock.

THEOREM A (all real 1-O technological designs):
  Whenever one F_i alone builds O(c_i,a_i), the other two N-country
  governments STRICTLY prefer mandatory public O(1,0).
  Because they jointly form a 2/3 majority and both can propose
  M, final government policy MUST be M, not L.
  The sole original firm's government also STRICTLY wants M.
  NNN likewise unanimously mandates.
THEOREM B (all real identical three-O designs):
  If all three firms choose the same O(c,a), all three govs
  WEAKLY prefer M; strictly prefer it unless (c,a)=(1,0).
  Given government M-on-indifference tie rule, L is impossible
  even at that exact equal-specification corner. Proof uses
  W_I(c,0) strictly increasing in c, and real consumer+profit
  gross welfare strictly decreasing in a for κ>0.
THEOREM C (real nonidentical 3-O counterexample):
  Exact Fraction Cournot with private O(1,0),O(1,1/2),O(1,1)
  yields G1 strictly opposing M while G2/G3 strictly approve.
  Therefore claims of government unanimity for ALL 3-O designs
  are FALSE. With simple majority M still passes here.
  This particular profile is not itself an initial SPE because
  unique max a3=1 can be reduced to 1/2, saving strictly
  positive cost without changing ANY bilateral common standard
  or government vote (under unanimity).
Proof stops there: all distinct three-O configurations do not
yet have a global majority-approval theorem, nor is complete
equilibrium uniqueness claimed for 3 independently developed O.

Previous Stage19 excluded EVERY (O,O,N) L-RS with asym c_i,a_i
under majority+all-government proposal rights. With A/B here,
all pure initial profiles except the asymmetric three-O class
have their public-policy outcome M, but other firm-stage
equilibrium paths within those classes require separate checks.
"""
import sympy as S
from fractions import Fraction as F
import stage11_eta_k_phase_certificates as st11
import stage14_institutional_veto_ablation as st14
import stage15_three_country_veto_minimal_continuous_spe as st15
import stage5_integrated_independent_standards_and_government as st5

R=S.Rational
m,g,v,k,rho,phi=st14.m,st14.g,st14.v,st14.k,st14.rho,st14.phi
c,a=st11.c,st11.a
KLO,KHI=R(27,50),R(14,25)
WI0=st14.WI0
WN=st11.WN
PI0=st15.PIstar
grossWI=S.cancel(st11.WI+phi*(c*c+a*a)/2)
grossWI0=S.cancel(grossWI.subs({c:1,a:0}))
# In homogeneous private 3-O history, EACH country's gain
# from upgrading open common technology O(c,a) to O(1,0).
# New variable capital = phi/2*(1-c^2). No fresh K.
delta_three_identical=S.cancel(
    grossWI0-grossWI-phi*(1-c*c)/2)

def singleton_government_theorem():
    # When only one O is installed, no pair-compatible O cohort
    # exists, so there is ZERO technology productivity or
    # substitution improvement in Cournot, as in Stage5 exact code.
    # All 3 markets have N-market CS and q before public M.
    # Any of the two N-country governments pay NEW K+phi/2
    # after M: G_N_M-G_N_L=WI0-K-WN.
    assert WI0-KHI-WN>0
    # The sole O-country already paid sunk K+phi/2(c^2+a^2).
    # At M it pays additional phi/2*(1-c^2) and obtains
    # national W_M=WI0-K-phi*a^2/2, while
    # W_L=WN-K-phi/2(c^2+a^2). Thus Δ_O=WI0-WN+phi*c^2/2.
    assert WI0-WN>0
    C=S.symbols('C',real=True)
    delta_sole=S.cancel(WI0-WN+phi*C*C/2)
    assert S.factor(delta_sole.subs(C,0)-(WI0-WN))==0
    assert S.factor(S.diff(delta_sole,C)-phi*C)==0
    # Check with a SEPARATE market+payoff Fraction solver
    # strictly for observed L baseline histories.
    K=F(11,20); E=F(7,50)
    a0=('O',F(4,5),F(3,5))
    L=st5.continuation((a0,st5.N,st5.N),'L',None,
                      (0,0,0),K,E)
    for j in (1,2):
        assert S.cancel(WI0-R(K)-R(L[1][j]))>0
    assert S.cancel(WI0-R(K)-phi*a0[2]*a0[2]/2
                    -R(L[1][0]))>0
    # NNN government compares WI0-K vs WN; unanimous.
    assert WI0-KHI-WN>0
    print('PASS exact ALL-REAL singleton O(c,a):',
          'each national government strictly wants public M',
          'throughout K∈[.54,.56] and eta∈[.10,.14]',
          flush=True)
    print('PASS NNN all-N => unanimous public mandate M',
          flush=True)

def homogeneous_three_open_government_theorem():
    assert S.factor(grossWI0-(
        st11.WI.subs({c:1,a:0})+phi/2))==0
    delta_a0=S.cancel(delta_three_identical.subs(a,0))
    assert S.factor(delta_a0-(
        st11.WI.subs({c:1,a:0})-st11.WI.subs(a,0)))==0
    # FULL c∈[0,1] exact rational Sturm proof of strict
    # positive ∂W_I(c,0)/∂c from Stage11.
    st11.sturm_positive(S.diff(st11.WI.subs(a,0),c),
                       c,R(0),R(1),
                       'homogeneous all-3-O improvement as c increases')
    # ∂grossWI/∂a STRICTLY NEGATIVE analytically for any
    # 0<=a<=c<=1, κ>0, m+b>0.
    z=1+rho*c
    b=g+k*a-v*c
    analytic=-3*k*(2*m+b)*z*z/(4*(m+b)**3)
    assert S.factor(S.diff(grossWI,a)-analytic)==0
    assert m+b.subs({c:1,a:0})>0
    assert k>0 and z.subs(c,0)>0
    # Fundamental theorem of calculus:
    # Δgov(c,a)=[W_I(1,0)-W_I(c,0)] +
    #            [grossWI(c,0)-grossWI(c,a)]>=0.
    algebra=S.cancel(
        delta_three_identical-(
           st11.WI.subs({c:1,a:0})-st11.WI.subs(a,0)
           +grossWI.subs(a,0)-grossWI))
    assert S.factor(algebra)==0
    assert S.factor(delta_three_identical.subs({c:1,a:0}))==0
    # Other feasible designs strictly gain due c<1 or a>0.
    assert delta_three_identical.subs({c:R(1,2),a:0})>0
    assert delta_three_identical.subs({c:1,a:R(1,2)})>0
    print('PASS exact GLOBAL homogeneous triple OPEN:',
          'all gov weakly prefer M throughout continuous c-a',
          'triangle and STRICTLY except (c,a)=(1,0);',
          'tie-M convention enacts M at the sole equality',
          flush=True)

def heterogeneous_three_open_counterexample():
    # Exact rational example: all c_i=1, products common design
    # differ so firm 1 is advantaged in output and loses public
    # standardization, while governments 2 and 3 gain.
    K=F(11,20); E=F(7,50)
    h=(('O',F(1),F(0)),('O',F(1),F(1,2)),
       ('O',F(1),F(1)))
    L=st5.continuation(h,'L',None,(0,0,0),K,E)
    delta=[]
    for i in range(3):
        ai=h[i][2]
        publicW=WI0-R(K)-phi*R(ai*ai)/2
        delta.append(S.cancel(publicW-R(L[1][i])))
    assert delta[0]<0 and delta[1]>0 and delta[2]>0,delta
    # No public M could pass under UNANIMITY, while 2/3
    # majority plus independent proposals from G2/G3 passes.
    # The original upper-a O(1,1) developer overinvests:
    # lowering a3=1 to .5 leaves every pair's min(a)
    # unchanged and makes a fixed genuine capital saving.
    reduced=(h[0],h[1],('O',F(1),F(1,2)))
    L2=st5.continuation(reduced,'L',None,(0,0,0),K,E)
    assert L[2]==L2[2] and L[3]==L2[3]
    savings=phi*(1-R(1,4))/2
    assert S.cancel(R(L2[0][2])-R(L[0][2])-savings)==0
    # For any government, both M and L private capital costs
    # change by exactly the same saving; its voting Δ is
    # unchanged and ALL majority/unanimity policy outcomes
    # are therefore unaffected by the reduction.
    delta2=tuple(S.cancel(
         WI0-R(K)-phi*R(reduced[i][2]*reduced[i][2])/2
         -R(L2[1][i])) for i in range(3))
    assert tuple(delta)==delta2
    print('PASS EXACT Fraction 3-O asymmetry COUNTEREXAMPLE:',
          'govt delta(M-L)=',tuple(str(d) for d in delta),
          'G1 veto under unanimity, G2/G3 approve under majority',
          flush=True)
    print('PASS observed asymmetric 3-O history itself NOT',
          'a private-stage SPE under unanimity: firm3 earns',
          'strict cost saving',savings,
          'by lowering wasted max common-design investment',
          flush=True)

if __name__=="__main__":
    singleton_government_theorem()
    homogeneous_three_open_government_theorem()
    heterogeneous_three_open_counterexample()
    print('SCOPE: full 3-O asymmetric game (including distinct',
          'pairwise c and a, offpath political responses and',
          'private Nash) remains OPEN; neither global uniqueness',
          'nor all-3-O government majority proved.',flush=True)
