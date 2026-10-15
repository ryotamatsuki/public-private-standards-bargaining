# Stage30I — Formal verification targets and statement-fidelity map (PRE-FLIGHT)

**2026-10-15 JST. Formalization APPLICABLE for all C1–C7, but NOT STARTED.**
Workflow authority: research-paper-workflow Stage7.5A and FORMAL_VERIFICATION_CHECKLIST.md. Stage30C mathematical PASS is AI/analytical/exact-rational, NOT a proof-assistant result. Stage7.5 remains CONDITIONAL GO / NOT FROZEN because Stage6 published-priority source access is user-deferred. This preliminary target map cannot count as Stage7.5A GO or permit Stage8.

## Highest-value certificate priorities

| Priority | Claimed theorem | Proof-critical target to formalize from original primitives | Explicit scope boundary |
|---|---|---|---|
| **P0/A** | C1 private-SPE iff | For arbitrary three legal O-investment vectors prove total net-of-variable-cost three-developer return S <= 3P, equality only all O(1,0), then a unilateral withdrawal is profitable under either policy continuation; ensure empty/one/two/triple developer partitions exhaustive | Do NOT *assume* "no three-developer SPE" as an axiom or bake it into SPE definition |
| **P0/B** | C1 private-SPE iff | For a pair O(c,a), O(c,a), N, prove global sufficiency over **all finite unilateral moves**, N withdrawal, asymmetric O deviations and policy-changing N→O entry including O(0,0), using the exact selector and full Cournot response | F_a>=0 is only a local necessary condition unless proved globally via F_c>0 and F_aa<0; all ties count |
| **P0/C** | C3 broad-agenda exact public profiles | For any initial vector of choices N or O(c,0), with r<=2 and at least two eligible proposers, derive >=2 government YES from national welfare and no profitable deviation; prove converse via C1/C2 | Under r=3 analogous sufficiency is FALSE; do not encode the theorem conclusion as the game type |
| **P0/D** | C5 maximum private-SPE welfare | From R, derive a<=a*(eta) using **restricted** F_ac>0 (a>=.30), prove T_c,T_a>0 on their actual enclosures, and prove (1,a*) in R, then unique maximizer **as a DESIGN PAIR** | Global F_ac>0 is false; maximum of private SPE is NOT global planner optimum |
| **P1/E** | C2 public welfare | Derive every *public pure SPE* initial investor a_i=0 by unilateral N withdrawal and correct off-path selector; only then deduce total K+phi/2 per firm and world 3(W_I-K) | Algebraic cost invariance assuming a=0 is not a complete proof of public SPE invariance |
| **P1/F** | C7 preference split | Derive founder firm public−private profit P-F-phi*a*a/2<=0; founding governments B>0; outsider V-K<0 using C1 membership and domain-restricted signs | Founders weakly prefer private, not always strictly; no same-government preference reversal |
| **P1/G** | C4 K comparative static | For all eta,K1<K2 in the box, the exact R conditions imply R(K1) subset R(K2); verify strict at c=.929,a=0,eta=.14,K1=.54,K2=.55 | Strictness is EXISTENTIAL for this witness, not proved for every K pair; C1 bridge still needed |
| **P1/H** | C6 welfare over all equilibria | Prove the logic of the ∀new e ∀old e weak-dominance iff K<=KW, and above KW the strictly improved infimum and reduced supremum, using proved C1,C2,C5 and genuine old public existence | An abstract set comparison with C2/C5 as hypotheses is NOT formalization of the entire economics |
| **P2/I** | Cournot/compliance foundation | Positive-definite symmetric H and A=H+mI for every developer pattern, positive interior q, CS=q'Hq/2; mandatory all-compliance via 25/33> Kmax+phi/2 | Singleton public adopter has intercept z=1, not automatic z=1+rho |
| **P2/J** | Crucial exact signs | Formalize rational cleared-denominator polynomials and verified inequalities B>0,T_a>0, restricted F_ac>0 and Kmin−V>0, including bounds on denominators and a-root brackets | Importing Boolean pass:true from a JSON file is not a proof; rational coefficients need a kernel-checkable checker or certificate |
| **P2/K** | Roots and knife edges | Exist/unique a*(eta) in (.30,.61); F=P weak participation boundary; K=V government YES on tie; y_c<=0 but not strictly everywhere | Don't replace rational witness, roots and partial curvature with unproved float approximations |

The priority order is mathematical-assurance value: P0 targets make the main C1/C5 mechanism true rather than just checking decorative identities. P1/P2 may be necessary prerequisites for the P0 implementation even though the scheduling priority differs.

## Suggested statement forms (specification, NOT compiled Lean code)

~~~text
PARAM:  v=.01,gamma=.14,kappa=.02,rho=.32,phi=.14
DOMAIN: eta in [.10,.14], K in [.54,.56], a in [0,c], c in [0,1]
A: nonempty subset of {1,2,3}
r: one of {1,2,3}
Invest: N | O(c,a); O(0,0) != N, because O pays K

C1: ∀ eta K A r h legal, (PrivatePureSPE eta K A r h) iff
    ∃ permutation i,j,k, h_i=O(c,a),h_j=O(c,a),h_k=N,
    F_a(c,a;eta)>=0 ∧ F(c,a;eta)>=P ∧ K>V(c,a;eta),
    and (r=3 or (r<=2 and A={k})).

C2: ∀ eta K A r e,
    PublicPureSPE(e) ⇒
       (all initial O investors have a_i=0) ∧
       profit_i(e)=P-K ∧ nationalW_i(e)=WI-K ∧
       worldW(e)=3(WI-K).

C3: ∀ eta K A r with r<=2 and |A|>=2,
    InitialPureSPE(h) iff ∀i h_i=N or h_i=O(c_i,0),
    for ANY c_i in [0,1], and all such h end M.

C4: ∀ eta,K1,K2 in box with K1<K2,
    R(eta,K1) ⊆ R(eta,K2).
    ∃ particular (eta,K1,K2,c,a) witness strict inclusion.

C5: ∀ eta,K and old private-admitting constitution,
    max_{(c,a)∈R(eta,K)} [T(c,a)-2K] = T(1,a*(eta))-2K,
    unique maximizer as (c,a), NOT unique entire equilibrium.

C6: ∀ eta,K and old-private-admitting & new-broad constitutions,
    [∀ e_new ∈ PureSPE(new), ∀ e_old ∈ PureSPE(old),
     worldW(e_new)>=worldW(e_old)]
      iff K<=3WI-T(1,a*(eta)).
    If K>KW, inf(new)>inf(old) and sup(new)<sup(old).

C7: ∀ private pure SPE,
    founder firm mandate gain <=0,
    founder government mandate gain >0,
    outsider government mandate gain <0.
~~~

All displayed type signatures need a separate fidelity audit to ensure the construction of SPE uses *unilateral payoff deviations and the policy continuation*, not R by definition. All policy ties must use YES-on-tie. Constitutional and investor identities must not be conflated. No actual Lean source, toolchain or mathlib revision has been installed.

## Dependency graph and formal proof gap

1. Original demand branches + consumer quadratic utility → Cournot matrices → compliance and policy selector.
2. Global no-three-investor bound + exclusion of sparse/asymmetric histories + F_a/F_c/F_aa signs + uniform outsider entry bound + policy switch re-evaluation → C1.
3. C1 plus exact zero-a government support and deviations → C3; C1 plus national gains → C7; C1 plus K cancellation → C4.
4. Public deviations eliminate waste → C2.
5. C1 plus a-root and domain-limited polynomial sign certificates → C5.
6. C2+C3+C5 and old public/private existence/welfare witnesses → C6.

A formalized C6 abstract lemma with assumptions "C2 holds" and "C5 holds" proves neither C2 nor C5. A definition of "pure SPE" as "h∈R" followed by a theorem that all private SPE belong to R is also empty/circular. These are key conclusion-smuggling risks.

## Toolchain and certificate requirements upon actual authorization

Choose and pin Lean4+mathlib release and exact commit, preserve lean-toolchain, lakefile.toml, lake-manifest.json, and clean lake build command; log exact kernel-accepted theorem signatures and #print axioms. Reject unexplained sorry/admit, project-specific axioms encoding a target theorem, and any theorem whose quantified box differs from the manuscript. A Python rational regression or GitHub documentation-gate CI is NOT formal proof.

The correct present state is **FORMALIZATION APPLICABLE / IMPLEMENTATION NOT STARTED**, not FORMAL VERIFICATION PASS nor FORMALIZATION NOT APPLICABLE. The current source-priority blocker and Stage7.5 conditional freeze remain unchanged.
