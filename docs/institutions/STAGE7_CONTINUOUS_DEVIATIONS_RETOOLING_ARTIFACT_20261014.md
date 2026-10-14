# Stage 7 — Continuous-strategy RED-TEAM: Exact Equilibrium Counterexamples and Retrofit-Cost Discontinuity

2026-10-14 JST. Parent Draft PR #35. **Scientific status:** finite-menu predecessor Stage5/Stage6 IS/RS existence claims are audited, not automatically promoted to continuous strategy SPE. We identify **six exact rational unilateral deviations** that invalidate six of the Stage5 fourteen K=.5 finite-design Nash/SPE candidates under the previously fixed selected adoption continuations; isolate a policy discontinuity caused by a mechanically repeated fixed K plus full implementation fee for arbitrarily tiny within-standard specification edits; recompute all 1,000 initial private profiles under a continuous retrofit-cost ALTERNATIVE; distinguish actual multiple economic adoption allocations from redundant choices by already-matched actors. **Not** a full all-parameter continuous first-stage/mixed-adoption SPE classification.

## 1. Original exactly reproduced Stage5 benchmark and adversarial feasible strategies

Original six economic parameters fixed `(v,gamma0,kappa,eta,rho,phi)=(.01,.14,.02,.03,.32,.14)`, independent initial private firms `N,X,Y,O`, `0<=a_i<=c_i<=1`, G1 proposes L/C/M, G2/G3 can veto, 3 firms then independently migrate/comply, differentiated Cournot-KKT production. New real setup cost K is already separately introduced in Stage3 and is NOT part of original six. Original postpolicy adoption equilibrium selection maximizes national W among adopter Nash equilibria, then private P, then compliance; this **remains a maintained selection rule in Section 1** and is not a claim about arbitrary mixed continuation choice.

Original **finite** actions per firm: `N` or labels X/Y/O paired with `(c_i,a_i)∈{(.5,0),(1,0),(1,.6)}`. The earlier exact ten/fourteen outcomes at K=0/.5 were checked for all nine finite unilateral deviations per firm. Here each original equilibrium is challenged by additional exact rational actions covering `c_i∈{.01,.25,.49,.51,.7,.9,.99,1}` and candidate common-design values `a_i∈{0,.01,.3,.5,.59,.61,.7}` where feasible, plus certain intermediate pairs, for each of X/Y/O and N. These are OFF-MENU CONTINUOUS STRATEGIES under the genuine c,a action space, not merely another initial grid equilibrium calculation. Cournot FOCs and stage2-policy logic use the source's exact `fractions.Fraction` engine in each re-solved offpath history.

**Audited under the SAME ORIGINAL retrofit fee model:**
- At `K=0`, 10 finite SPE candidates: no profitable deviation found among the 1,440 exact-rational off-menu probes. **ALL 10 remain UNPROVED** under arbitrary continuum and all mixed policy continuations; absence on a finite test is not proof.
- At `K=.5`, 14 finite SPE candidates: EXACTLY **six** distinct labeled/symmetric candidates defeated by an exact profitable unilateral deviation in the rational test; 8 candidates not refuted by this test; 1,674 exact-rational off-menu probes for this run. All six false candidates have exactly 2 firms on private OPEN O and one on N, but the OPEN adopters have mismatched common-design settings `(c,a)=(1,0)` and `(1,.6)`. The financial difference is real: the higher-design adopter incurs cost for product features that are not actually shared with its collaborator. Each of its government-policy stages remains L for an appropriate off-menu strategy.
- These six are NOT SPE under the original policy-after-adoption equilibrium SELECTION rule, because one single strictly profitable deviation suffices. Under an alternative offpath Nash selection the same prehistory might be supportable or not; do not claim all possible mixed SPE with those initial strategies have been excluded.

## 2. Explicit standalone exact counterexample, same gov policy and same market quantity

Take `K=1/2`, initial profile
`h^0=(N,O(1,0),O(1,3/5))`, government G1/G2/G3 all leave policy L. This was listed as a Stage5 finite-design Nash/SPE candidate. Since the effective shared interface/design uses `min(c_2,c_3),min(a_2,a_3)`, the two firms' market effective common design is **ZERO** despite firm3 paying `phi*(3/5)^2/2` to develop design that its partner cannot actually use.

Firm3 unilaterally chooses `h_3' = O(1,1/100)`. This is admissible in the original CONTINUOUS triangle, but was unavailable in the old finite action menu. Under the original government protocol G1/G2/G3 again choose L. All actual Cournot quantities, substitution coefficients, outsider activity, CS and firm gross operating profits remain IDENTICAL because the paired minimum common design remains zero; only firm3's wasted design resource fee falls. Hence the payoff gain is the **EXACT RATIONAL**
`Delta P_3 = phi/2 * [(3/5)^2-(1/100)^2] = 25193/1000000 = +0.025193 >0`.
This is an elementary exact analytic SPE counterexample; it does NOT rest on approximate numerical optimization or proof-by-grid. The independent code prints both on/off government policies and exact payoffs.

As an alternative deviation, firm3 chooses `O(99/100,0)`, still G=L; the exact real-profit improvement is
`38625064570314185049190057 / 1833729979438911279049000000 ≈0.0210636598645`. Six symmetry-related finite proposals fail identically.

## 3. A PHYSICAL MODEL PROBLEM revealed by letting c_i,a_i be truly continuous

In the original Stage5 matching/certification protocol, a technology holder with OPEN reference `O(1,epsilon)` who changes to a legally identical family reference `O(1,0)` must pay `K+phi/2=0.57` **again**, however small positive epsilon is. When epsilon=0 exactly, no extra cost. The paid upfront initial development cost remains sunk and is never refunded. This creates an artificial discontinuity at epsilon=0 of 0.57 in real resource costs.

For prehistory `(N,O(1,0),O(1,epsilon))`:
- At exactly `epsilon=0`, selected government policy M, with incumbent firm3 final net profit `PI(1,0)-K≈0.4613552295918367`.
- At `epsilon=1/10000,1/1000,1/100,3/5` **EVERY tested case** selected G policy L because G3 would lose from the mandate due that full refit cost, so firm3's net payoff equals
`P3(epsilon)=PR(1,0)-K-(phi/2)*epsilon²`,
with `PR(1,0)-K≈0.4909831506193263`.
- The gross incumbent-government welfare gain before extra refit cost from changing RS(1,0) to IS(1,0) is EXACT
`Delta W0 = 681773932073 / 10742687846912 ≈0.0634639991`.
The discontinuous original refit cost 0.57 is far GREATER than `Delta W0`, whereas at epsilon=0 refit=0. Thus G3's yes/no changes sharply even though the real designs approach the SAME technical standard.
- IF L holds for all epsilon in a right neighborhood of 0, then `P3(epsilon)` is strictly decreasing in epsilon and its supremum as `epsilon↓0` is `PR(1,0)-K≈.49098315`, which strictly exceeds the at-equality M outcome `PI(1,0)-K≈.46135523` by EXACT
`3978543839391/134283598086400≈.0296279210`. This would leave NO attainable best reply on that restricted continuous choice slice. **We have verified the specified rational sequences and exact incentive formulas; we have NOT run full quantifier elimination to prove all sufficiently small epsilon preserve policy L**, nor disproved existence of a full six-player SPE in the entire action space. This is a serious model-existence concern, not a proven global no-SPE theorem.

### Explicit continuity repair: technology-family-specific retrofit costs

Alternative economic resource-cost mapping:
- The prior upfront development fee remains `K+phi(c_i²+a_i²)/2` and is sunk.
- A first-time converter from N, or from proprietary X/Y into the public O family, incurs full technology setup `K+phi(c_ref²+a_ref²)/2` (as before).
- A converter already in open family O who adjusts to another O reference incurs **continuous within-family refit cost**
  `C_retrofit(O(c,a)→O(c',a')) = (phi/2)[(c'-c)^2+(a'-a)^2]`;
  exactly identical designs entail zero additional fee, and an infinitesimal redesign incurs infinitesimal cost. This new function is a **substantive competing structural assumption**, and is compared to rather than silently substituted for Stage5.
- K is a true first-setup resource cost, not re-imposed on every negligible change.

All government votes and actual adopter payoffs are RECOMPUTED after this cost substitution, without touching the original Stage5 source. The previous prehistory now induces **M** for ALL epsilon tested `0,1/10000,1/1000,1/100,3/5`, rather than jumping M→L as epsilon becomes positive. The high-common-design firm loses its prospective windfall from a tiny mismatch. For epsilon=.01, its mandatory-IS profit ≈.461341 instead of the original L profit ≈.490976. This is a corrected-technology SENSITIVITY conclusion at explicit rational histories, **not a proof of uniform policy continuity over all reals**.

**Full re-solution of same 1,000 initial 10-action profiles, retaining the SAME welfare-max adopter-Nash selection, yields:**

| setup K | original repeated-full-fee equilibria | smooth within-O retrofit equilibria |
|---|---|---|
| 0 | 10 finite-first-stage SPE, all IS (policies L=3,C=6,M=1) | **3** finite-first-stage SPE, all IS (policies L=2,M=1) |
| .5 | 14 finite-first-stage SPE, IS=2/RS=12 | **1** finite-first-stage SPE, IS=1 (policy M=1) |

This sensitivity test is exact rational / full discrete-profile game resolution but **not** a certification of any of the 1 or 3 remaining outcomes against the COMPLETE real c_i,a_i triangles; do not call these full-continuous SPE.

## 4. Post-C 'multiple Nash equilibria': action-label degeneracy vs ECONOMIC outcome multiplicity

At K=0, the original Stage5 full-equilibrium profiles on-path with policy C were previously observed to have 2 or 4 independent-adopter pure Nash strategy profiles. Inspection shows these differences are in **inert flags of the firm that already owns the exact recognized O specification**. For example, with h=(N,N,O(1,0)) the certification subgame has 2 flag profiles, but all produce IDENTICAL final specifications, quantities, company profits and government W. With h=(N,O(1,0),O(1,0)), there are 4 such flags but only ONE distinct economic outcome. Thus, in these on-path cases, **the apparent 2 or 4 Nash multiplicity is a modeling artifact of retaining a redundant 'migrate to your own current spec' action**. Remove that flag or quotient outcomes before counting meaningful adoption multiplicity. Offpath M at NNN and K=.75 genuinely has DISTINCT economic 000,111 and interior mixed Nash; prior Stage6 proof remains.

This matters when claiming robustness to multiple policy-after-adoption equilibria: distinct strategy labels do NOT automatically imply distinct allocations or W, whereas multiple economic adopter outcomes must actually be tracked.

## 5. Research guidance and honest stopping point

1. **Reject 6 original selected finite equilibria** in the unrestricted-design source Stage5 cost model; the 14 cited earlier is not even a lower bound for real technology-space SPE. Other 8 at K=.5 and 10 at K=0 merely survived a *finite* enriched rational screen; no assertion they withstand arbitrary continuous deviations or mixed-continuation selection.
2. Adopt **continuous within-standard conversion cost** as the preferred benchmark only AFTER stating its economic implementation justification (retrofit/test/certification costs proportional to technical change, possibly an independently motivated discrete switch cost for physically changing incompatible technology families). No evidence the precise quadratic conversion distance is universal; prove sensitivity across plausible variants.
3. Remove inert adoption actions for firms already exactly using the reference, so multiple equilibria are counted by genuine behavior and payoff-distinct outcomes.
4. Keep proof of high-K continuous NS SPE from Stage6, but Stage7 does not establish IS/RS continuum SPE or a 7D parameter phase partition. Global semialgebraic CAD and certified interval methods may be needed for a rigorous complete classification.
5. Literature grounding: Farrell and Saloner (1985), *Standardization, Compatibility, and Innovation* https://ideas.repec.org/a/rje/randje/v16y1985ispringp70-83.html; Farrell and Saloner (1986), *Installed Base and Compatibility*, AER 76:940–955 https://www.gsb.stanford.edu/faculty-research/publications/installed-base-compatibility; Besen and Farrell (1994), *Choosing How to Compete* https://topcat.aeaweb.org/articles?id=10.1257%2Fjep.8.2.117. These study coordination, standards compatibility and adoption/inertia; the new model's particular infinitesimal-refit-cost jump is a diagnostic inconsistency, not established new general IO theory.

## 6. Reproducibility

- `code/stage7_continuous_deviation_redteam.py`: original protocol, all finite equilibrium candidates and individually profitable off-menu exact counterexamples, detailed rational policy branches, on-path raw adopter equilibrium multiplicity.
- `code/stage7_smooth_open_retrofit_sensitivity.py`: independent within-O conversion fee hypothesis, exact welfare-gap vs fixed switching-cost comparison, actual adopter-outcome quotient test, **full fresh 1000-profile finite-game equilibrium enumeration**.
- `.github/workflows/stage7-continuous-deviation-redteam.yml` and `.github/workflows/stage7-open-reference-smooth-retrofit.yml`; each separate CI SUCCESS.
- All previous Draft PRs preserved. No manuscript rewrite, no merge.
