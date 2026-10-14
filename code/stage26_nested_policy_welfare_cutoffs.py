"""STAGE26: three nested economic thresholds and sunk-capital welfare reversal.

The same minimal 3-country no-transfer OPEN/N model and baseline
technology parameters from Stage11/15/19 are maintained. This new
result does NOT imply a necessary/sufficient global phase partition
across all investments or all 7 technology and fee parameters.

For symmetric privately OPTIMAL bilateral O(1,a*(eta)),O(1,a*),N,
at eta in [1/10,7/50], K in [27/50,14/25], define:
 K_V = incumbent-outside national government's M-vs-L veto cutoff;
 B = each private RS member national governmental gain M-L;
 K_E = ex-POST total world gain zero after RS capital is SUNK;
 K_W = ex-ANTE world ranking between genuine IS NNN/M and RS OON/L.

THEOREM, exact (not approximated):
  K_V < K_E = K_V+2B < K_W=K_E+phi*a*(eta)^2.
  Every threshold decreases STRICTLY in eta.
  Each K in [.54,.56] admits unique eta_E(K)<eta_W(K) within
  [.10,.14], with eta_E the ex-post and eta_W the ex-ante
  world-welfare crossings. Under K=.55,
  eta_E in (.111,.112), eta_W in (.118,.119) EXACTLY.
  eta=.115,K=.55 witnesses ex-ante public best but
  ex-post M retrofit welfare worsening (sunk-cost wedge).

Political policy after any observed OON privately optimal regional
standard is (B,B,K_V-K): member countries support M; outsider
rejects M. Thus 2/3-all-agenda enacts M despite the outsider;
unanimity fails M irrespective of proposal rights; under 2/3 but
exclusive G1 agenda M passes only when G1 is a private founder.

Scope: observed RS voting ≠ claim it is onpath under universal
agenda + majority (Stage25 rules those SPEs out). Welfare
comparisons across constitutions must use EX-ANTE K_W, not K_E.
"""
import sympy as S
from fractions import Fraction
import stage11_eta_k_phase_certificates as st11
import stage14_institutional_veto_ablation as st14
import stage19_universal_agenda_majority_global_two_firm_rs_exclusion as st19

R=S.Rational
eta,a=st11.e,st11.a
phi=st11.phi
KLO,KHI=R(27,50),R(14,25)
EB=R(1,10);ET=R(7,50)
WI=st11.WIP
PR=st11.f
PO=S.cancel(st11.PO.subs(st11.c,1))
CSR=S.cancel(st11.CS.subs(st11.c,1))
WORLD_RS=st11.W

B=S.cancel(WI-phi*a*a/2-PR-CSR)
KV=S.cancel(WI-PO-CSR)
KE=S.cancel(KV+2*B)
KW=S.cancel(3*WI-WORLD_RS)

def algebraic_threshold_identities():
    # This identity holds at every (eta,a), not only a*(eta).
    assert S.factor(KW-KE-phi*a*a)==0
    assert S.factor(KE-KV-2*B)==0
    # RS members already sunk (K+phi*(1+a²)/2) and public M
    # requires no SECOND K. The ex-post world M-L gain after
    # RS installed is 2B + (KV-K) = KE-K.
    K=S.symbols("K")
    inc_RS=PR+CSR-K
    inc_retro=WI-K-phi*a*a/2
    out_RS=PO+CSR
    out_retro=WI-K
    post=S.factor(2*(inc_retro-inc_RS)+(out_retro-out_RS))
    assert S.factor(post-(KE-K))==0
    # In the ex-ante institutional choice, IS starts from NNN:
    # public world welfare 3(WI-K). RS costs 2K.
    pre=S.factor(3*(WI-K)-(WORLD_RS-2*K))
    assert S.factor(pre-(KW-K))==0
    assert S.factor(pre-post-phi*a*a)==0
    assert S.factor((out_retro-out_RS)-(KV-K))==0
    assert S.factor((inc_retro-inc_RS)-B)==0
    assert phi>0
    print("PASS exact national/world thresholds, sunk capital wedge",
          "KW-KE = phi * a^2",flush=True)

def global_continuum_monotonicities():
    # Existing Stage11 certified f_aa<0, f_a,eta>0,
    # guaranteeing unique interior a*(eta), a*'(eta)>0
    # on [.10,.14]. Re-run Stage11 theorem through parent CI.
    T,U=S.symbols("T U")
    subs={eta:R(1,10)+R(1,25)*T,
          a:R(1,4)+R(9,25)*U}
    # Exact full eta x a rectangle: K_V, K_E, K_W each
    # strictly fall if eta or the privately chosen a rises.
    # Positive integer-valued tensor Bernstein signs of
    # numerator and denominator, NOT a grid.
    for name,threshold in (("veto",KV),("ex-post",KE),("ex-ante",KW)):
        for param in (eta,a):
            st11.tensor_positive(-S.diff(threshold,param),
                                subs,(T,U),
                                f"ST26 {name} decreases in {param}")
    # Standalone Stage14 exact 2D Bernstein verification of
    # government member benefit >0, outsourced veto at Kmin.
    st14.bernstein_positive(B,"ST26 member B STRICT positive")
    st14.bernstein_positive(PO+CSR-WI+KLO,
                           "ST26 outsider strictly vetoes at K>=.54")
    print("PASS K_V<K_E<K_W strictly at a*(eta)>.25,",
          "all eta [.10,.14], K [.54,.56]",flush=True)

# Rational enclosures for the unique optimum at selected eta values.
# Each enclosure is validated by strict opposing exact f_a signs,
# plus the Stage11 global strict concavity certificate.
ROOT_BRACKETS=(
    (R(1,10),R(30534,100000),R(30536,100000)),
    (R(111,1000),R(37208,100000),R(37210,100000)),
    (R(14,125),R(37851,100000),R(37853,100000)),
    (R(23,200),R(39823,100000),R(39825,100000)),
    (R(59,500),R(41862,100000),R(41864,100000)),
    (R(119,1000),R(42557,100000),R(42559,100000)),
    (R(7,50),R(59494,100000),R(59497,100000)),
)

def root_enclosure_audit():
    for E,L,H in ROOT_BRACKETS:
        assert R(1,4)<L<H<R(61,100)
        left=S.diff(PR,a).subs({eta:E,a:L})
        right=S.diff(PR,a).subs({eta:E,a:H})
        assert left>0 and right<0,(E,L,H)
        print("PASS exact rational a*(eta) root enclosure",
              "eta",E,"a in",L,H,flush=True)

def welfare_crossing_certs():
    # K_E and K_W strictly decrease in a and eta, so for every
    # root bracket a*(eta) in (L,H):
    # TH(E,H)<TH(E,a*(E))<TH(E,L).
    BOUNDS={E:(L,H) for E,L,H in ROOT_BRACKETS}
    def lower_at(thresh,E):return thresh.subs({eta:E,a:BOUNDS[E][1]})
    def upper_at(thresh,E):return thresh.subs({eta:E,a:BOUNDS[E][0]})
    half=R(11,20)
    # Both welfare crossing thresholds traverse every K in
    # [.54,.56] inside eta∈[.1,.14].
    for name,threshold in (("post",KE),("pre",KW)):
        assert lower_at(threshold,R(1,10))>KHI,name
        assert upper_at(threshold,R(7,50))<KLO,name
    # A unique eta_E(K) and eta_W(K) exist by continuity
    # and strict decrease; eta_E(K)<eta_W(K) follows
    # K_W(eta)>K_E(eta) pointwise, strictly on a*>0.
    assert lower_at(KE,R(111,1000))>half
    assert upper_at(KE,R(14,125))<half
    assert lower_at(KW,R(59,500))>half
    assert upper_at(KW,R(119,1000))<half
    # Exact witness interval at eta=.115 K=.55:
    E=R(23,200)
    assert upper_at(KE,E)<half
    assert lower_at(KW,E)>half
    assert upper_at(KV,E)<KLO
    # The SAME eta/K: ex-ante genuine public IS is socially
    # preferable to RS, while M retrofitted AFTER RS is
    # globally inferior (sunk overdesign loss).
    print("THEOREM nested welfare eta crossings for EVERY",
          "K in [.54,.56]: eta_E(K)<eta_W(K).",flush=True)
    print("EXACT ROOT ISOLATION K=.55: eta_E in (.111,.112)",
          "and eta_W in (.118,.119).",flush=True)
    print("EXACT WITNESS eta=.115, K=.55:",
          "K_E<.55<K_W, ex-ante M preferred, ex-post M detrimental",
          flush=True)

def institutional_policy_matrix():
    # Selected baseline equilibrium O(1,a*(eta)) private pair
    # has national policy-gain signs (B,B,-L), B>0 and L>0.
    # The outsider K_V-K<0 for the ENTIRE coexistence rectangle.
    for pair in ((0,1),(0,2),(1,2)):
        ds=tuple(R(1,100) if i in pair else -R(1,100)
                 for i in range(3))
        U0=st19.public_vote_outcome(ds,(0,),"unanimity")
        Uall=st19.public_vote_outcome(ds,(0,1,2),"unanimity")
        M0=st19.public_vote_outcome(ds,(0,),"majority")
        Mall=st19.public_vote_outcome(ds,(0,1,2),"majority")
        assert (U0,Uall,M0,Mall)==(False,False,(0 in pair),True)
        print("PASS OBSERVED RS policy (not on-path SPE assertion),",
              "founders",pair,
              "unanimity G1/all",U0,Uall,
              "majority G1/all",M0,Mall,flush=True)
    print("ECONOMIC CONSTITUTIONAL WARNING: compare actual",
          "unanimity-RS vs majority-all public IS using",
          "EX-ANTE K_W, never retrofit K_E; in the latter",
          "constitution RS cannot be an initial pure SPE.",
          flush=True)

if __name__=="__main__":
    algebraic_threshold_identities()
    global_continuum_monotonicities()
    root_enclosure_audit()
    welfare_crossing_certs()
    institutional_policy_matrix()
    print("ST26 SUCCESS: three nested cutoffs KV<KE<KW;",
          "distinct ex-post/ex-ante eta-crossings; exact",
          "sunk-cost preference reversal; agenda/quorum matrix.",
          "Conditional on previously certified reduced game.",
          flush=True)
