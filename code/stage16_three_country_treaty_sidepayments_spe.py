"""Stage 16 — THREE governments, proposer CANNOT pay outsider alone;
jointly financed unanimous compensation may succeed (or fail to coordinate).

Scientific scope: conditional GOVERNMENT SUBGAME after the observed
genuine Stage15 privately created OPEN RS history O(1,aR*),O(1,aR*),N.
Unlike Stage15, allow binding, budget-balanced, lump-sum and costless
cross-government transfers, financed by G1+G2 and received by G3 ONLY IF
a unanimous public standard M passes. These are new explicit
institutional rights; standalone post-RS government equilibrium
comparisons, NOT a complete new initial-firm full-continuous SPE theorem.

Exact physical primitives original five (.01,.14,.02,.32,.14),
eta ∈[.10,.14], K∈[.54,.56], unique privately optimal
a*(eta) ∈(.3053,.61) strictly increasing (Stage11).

Symbols:
 B(eta) = domestic member government gain if M is implemented,
 L(eta,K)= positive outsider-government loss if M implemented.
The parent Stage14/15 certifies B>0, L>0.
This code now proves for ALL parameters in the compact rectangle:
  B < L: single government G1 CANNOT profitably buy G3 approval.
  2B-L strictly decreases with eta, and has one root eta_T(K).
  eta_T(K) in (.10,.14) for every K∈[.54,.56].
  eta_T(K) decreases with K.
  If eta<eta_T(K), binding G1/G2 transfers CAN induce
  unanimous passage; transfer profiles t1+t2=L and
  L-B<t1<B, t2=L-t1 have strict positive donor gains,
  G3 weakly approves using a tie-YES convention.
  At the SAME eta,K, ZERO pledged contributions is also a Nash
  equilibrium of simultaneous conditional-contribution game
  because B<L rules out any unilateral sufficient pledge.
  If eta>eta_T, no budget-balanced transfer makes all three
  strictly better off: aggregate ex-post surplus is negative.
  Equality at threshold gives knife-edge weak cases.

The donor/no-donation multiplicity is standard threshold-public-good
coordination, NOT standalone scientific novelty. Treaty enforceability,
non-distortionary transfers and approval-on-indifference are ASSUMED.
"""
import sympy as S
from fractions import Fraction as F
from itertools import product
from math import comb
import stage11_eta_k_phase_certificates as s11
import stage14_institutional_veto_ablation as s14

R=S.Rational
e,a=s14.eta,s14.a
m,phi=s14.m,s14.phi
f,po,cs,WI0=s14.f,s14.po,s14.cs,s14.WI0
ELO,EHI=R(1,10),R(7,50)
KLO,KHI=R(27,50),R(14,25)
ALO,AHI=R(3053,10000),R(61,100)
B=S.cancel(WI0-phi*a*a/2-f-cs)
L0=S.cancel(po+cs-WI0)
# L(eta,K)=L0+K, and 2*B-L=the ex-post world gain of M.
surplus_at_K0=S.cancel(2*B-L0)

def global_bernstein(expr, lo=ALO, hi=AHI, label=""):
    T,U=S.symbols("T U")
    trans={e:ELO+(EHI-ELO)*T,a:lo+(hi-lo)*U}
    n,d=S.fraction(S.cancel(expr.subs(trans,simultaneous=True)))
    assert d.subs({T:0,U:0})>0
    counts=[]
    for expr_poly in (n,d):
        p=S.Poly(expr_poly,T,U); deg=p.degree_list()
        terms=p.as_dict()
        values=[
            sum(val*S.prod(R(comb(i,j),comb(N,j))
                for i,j,N in zip(indices,term,deg))
                for term,val in terms.items()
                if all(j<=i for j,i in zip(term,indices)))
            for indices in product(*(range(q+1) for q in deg))
        ]
        assert len(values)>0
        assert min(values)>0,(label,expr_poly,deg,min(values))
        counts.append(len(values))
    print("PASS entire continuous eta-a rectangle rational Bernstein:",
          label,counts,flush=True)

def sturm_positive(expr, v, left,right,label):
    n,d=S.fraction(S.cancel(expr))
    if d.subs(v,left)<0:n,d=-n,-d
    for pol in (n,d):
        p=S.Poly(pol,v)
        assert p.eval(left)>0 and p.eval(right)>0,(label,'endpoint')
        assert p.count_roots(left,right)==0,(label,'interior root')
    print('PASS exact rational Sturm:',label,flush=True)

def prove_global_no_unilateral_compensation():
    # Parent global theorem s11 establishes a*(.10) ∈
    # (.3053,.3054), unique strict concavity, and a*'(eta)>0;
    # hence actual a*(eta) ∈(.3053,.61) for all eta in [.10,.14].
    assert S.diff(f,a).subs({e:ELO,a:ALO})>0
    assert S.diff(f,a).subs({e:ELO,a:R(3054,10000)})<0
    assert S.diff(f,a).subs({e:EHI,a:R(5949,10000)})>0
    assert S.diff(f,a).subs({e:EHI,a:R(5950,10000)})<0
    # For EVERY eta and every a∈[.3053,.61], minimum possible
    # outsider loss occurs at K=.54. Even then it exceeds the
    # proposed public standard's benefit to EACH member G1/G2.
    global_bernstein(L0+KLO-B,label="OUTSIDER loss > ONE member gain")
    s14.bernstein_positive(B,
        "each member government strictly PREFERS public M if enacted")
    s14.bernstein_positive(L0+KLO,
        "nonmember government strictly opposes public M at any K >=.54")
    print("THEOREM: For ALL real eta∈[.10,.14] and K∈[.54,.56],",
          "at a=a*(eta), each member's gain B is strictly",
          "POSITIVE but LESS than outsider's loss L.",flush=True)

def prove_ex_post_transfer_frontier():
    # Strictly decreasing social surplus in eta along a*(eta):
    # B_ETA is positive? not needed; show global 2B-L decreases
    # in eta and in a on the entire conservative [.25,.61].
    T,U=S.symbols('T U')
    trans={e:ELO+(EHI-ELO)*T,a:R(1,4)+R(9,25)*U}
    s11.tensor_positive(-S.diff(surplus_at_K0,e),
                        trans,(T,U),
                        'expost cooperation surplus DECREASES directly in eta')
    s11.tensor_positive(-S.diff(surplus_at_K0,a),
                        trans,(T,U),
                        'expost cooperation surplus DECREASES with a')
    # Strict private global concavity and positive eta-a cross-partial
    # from Stage11 => a* increases, so surplus(eta,a*) decreases.
    # Bound exact endpoints using rational design optimum brackets
    # and negative derivative in a on whole rectangle.
    # eta=.10: a* < .3054, so eval at .3054 is a LOWER bound.
    assert (surplus_at_K0.subs({e:ELO,a:R(3054,10000)})
            -KHI)>0
    # eta=.14: a* > .5949, so eval at .5949 is an UPPER bound.
    assert (surplus_at_K0.subs({e:EHI,a:R(5949,10000)})
            -KLO)<0
    print('THEOREM: For EVERY real K in [.54,.56],',
          'a UNIQUE eta_T(K)∈(.10,.14) exists with 2B=L;',
          'eta_T is strictly decreasing in K.',flush=True)

def contribution_game_proposition():
    # Given the observed OPEN RS private h_R and G1's M offer,
    # donor governments 1,2 simultaneously pledge nonnegative t1,t2
    # payable ONLY IF the mandate passes (enforceable budget balance);
    # G3 receives the sum. No transfer when rejected.
    # Once G3 is indifferent it votes YES (explicit acceptance tie).
    #
    # If B<L, unilateral g1/g2 donation cannot be profitable:
    # the other donor at 0 would need t_i>=L, but then t_i>B,
    # making its net gain B-t_i <0. Therefore (0,0) remains
    # an NASH equilibrium in the voluntary pledge game.
    #
    # If 2B>L and B<L, the whole interval
    #     L-B < t1 < B,  t2=L-t1
    # contains strictly payoff-positive fulfilled funding profiles.
    # Donor deviating DOWN from equality causes M rejection and
    # reverts its payoff to zero, less than B-t_i>0;
    # donor deviating UP decreases private gain; and G3 accepts
    # since recipient net =-L+t1+t2=0 under the tie-to-YES rule.
    # Hence each such offer is ALSO an exact pure NASH equilibrium.
    # If 2B<L, there is no binding balanced t1,t2>=0 with
    # t_i<=B and t1+t2>=L; impossible to make all three no worse.
    print('THEOREM: If eta<eta_T(K), conditional treaty subgame',
          'has BOTH (0,0) no-transfer/no-mandate Nash AND',
          'a CONTINUUM of financed-M Nash:',
          't1 in (L-B,B), t2=L-t1, with G3 approval on equality.',
          flush=True)
    print('THEOREM: If eta>eta_T(K), no Pareto-improving',
          'budget-balanced government-to-government compensation',
          'can attain unanimous public M (without new efficiency).',
          flush=True)
    print('CAUTION: Post-RS treaty SUBGAME equilibrium only;',
          'the initial 3-firm investments and any ex-ante treaty',
          'commitment are NOT re-solved.',flush=True)

def anticipated_financing_destabilizes_original_rs():
    # The financed transfer equilibrium is a credible GOVERNMENT
    # continuation at the already developed h_RS, but its anticipation
    # makes EXACTLY THAT private initial profile NOT a full SPE.
    #
    # A founder initially O(1,a*) earns under financed public M:
    #   P_I^net (costs phi/2 for final c=1) - K - phi*a*²/2.
    # Deviating to N BEFORE development leaves h=(N,O(1,a*),N)
    # where ALL governments strictly authorize M WITHOUT transfers:
    # N governments: WI0-K>WN; sole old O govt:
    # WI0-WN+phi/2>0.
    # Then the deviator earns P_I^net-K, strictly MORE by
    # phi*a*²/2 >0. This is independent of donor transfer division
    # because private firm owner is not explicitly taxed as donor;
    # governmental transfer is borne nondistortionarily elsewhere.
    assert WI0-s11.WN-KHI>0
    assert WI0-s11.WN+phi/2>0
    assert (phi/2)*ALO**2>0
    print("THEOREM: financed-M conditional treaty equilibrium",
          "cannot be ONPATH at original initial open RS founders:",
          "a founder deviates to N and saves phi*a_R*(eta)^2/2 >0.",
          flush=True)
    print("SCOPE: does not exclude other PRIVATE starting profiles",
          "or other treaty-game SPE; unfinanced veto-continuation",
          "still supports original Stage15 RS outcome.",flush=True)


def diagnostics():
    import mpmath as mp
    mp.mp.dps=45
    fa=S.lambdify((e,a),S.diff(f,a),'mpmath')
    bb=S.lambdify((e,a),B,'mpmath')
    ll=S.lambdify((e,a),L0,'mpmath')
    def astar(eta):
        return mp.findroot(lambda A:fa(eta,A),(.31,.60))
    def total(eta,K):
        A=astar(eta)
        return 2*bb(eta,A)-ll(eta,A)-K
    for K in (mp.mpf('.54'),mp.mpf('.55'),mp.mpf('.56')):
        root=mp.findroot(lambda E:total(E,K),
                         (mp.mpf('.105'),mp.mpf('.12')))
        A=astar(root); Bi=bb(root,A);Li=ll(root,A)+K
        assert mp.fabs(2*Bi-Li)<mp.mpf('1e-30')
        print('NUMERIC root K=',mp.nstr(K,3),
              'eta_T=',mp.nstr(root,17),
              'a_R*=',mp.nstr(A,14),flush=True)
    K=mp.mpf('.55')
    for eta in (mp.mpf('.10'),mp.mpf('.12'),mp.mpf('.14')):
        A=astar(eta);bi=bb(eta,A);li=ll(eta,A)+K
        print('NUMERIC eta',mp.nstr(eta,3),
              'member_gain_B',mp.nstr(bi,12),
              'outsider_loss_L',mp.nstr(li,12),
              'joint_surplus_2B-L',mp.nstr(2*bi-li,12),
              'unilateral_gap_L-B',mp.nstr(li-bi,12),
              flush=True)
        assert li>bi>0
    eta=mp.mpf('.10');A=astar(eta)
    bi=bb(eta,A);li=ll(eta,A)+K
    assert 2*bi>li>bi
    t=li/2
    assert t<bi
    # 0 pledges => no single member wants to cover whole loss.
    assert bi-li<0
    print('NUMERIC concrete funder Nash at K=.55 eta=.10:',
          't1=t2=L/2=',mp.nstr(t,12),
          'each donor strict net gain',mp.nstr(bi-t,12),
          'outsider net zero accepting yes',flush=True)

if __name__ == '__main__':
    prove_global_no_unilateral_compensation()
    prove_ex_post_transfer_frontier()
    contribution_game_proposition()
    anticipated_financing_destabilizes_original_rs()
    diagnostics()
