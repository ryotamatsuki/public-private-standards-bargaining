# Stage 4 — Minimal Model Gate: Full construction and kill audit
Date: 2026-10-13 (JST). Workflow: v2.9 + main SHA 81c37dd95fc93d918138ba9d0da86541d3cc1067.
**Canonical Stage-4 verdict: NO-GO for S3-A's claim of a novel public/private + Ghosh–Morita differential substitution + network Cournot bargaining result.**
**Routing:** STOP this candidate branch. Return to Stage 3 ONLY for a genuinely distinct author-selected mechanism; substantive re-parameterization/revised costs or different signatory sets needs Stage-1/2 re-entry. No Stage 4A (cannot confer a GO by rechecking an economically unimportant result), no full paper freeze, no unsolicited edit of previous Stage-1/2/3 files.

## 1. Actual model and exhaustive choices
N=3 countries with one firm each; national markets k=1,2,3; segmented differentiated Cournot sold by all firms. Players H={G1,F1,G2,F2,G3,F3}. One-shot Γ-style exclusive exact-terms declarations, each chooses SQ or one z from six contracts:
I12,P12,I13,P13,I23,P23 (shallow interface / deeper shared platform for each bilateral pair). Each bilateral contract requires signature of exactly the four corresponding home governments and firms; all declarations simultaneous, full exact consensus needed; no sequential proposals, no institution-specific favoring rule, no contingent other deals. All three bilateral pairs overlap, so at most one activates. Each contract fixes a directed per-unit license payment r from the larger-index firm to the smaller-index firm in ALL three destination markets. Technology implementation by both signatory firms is binding as specified in Stage 1; no subsequent endogenous adoption stage. No contract signing costs or cost reductions in this frozen model; exports bear REAL marginal cost c, home sales have cost zero. A veto yields the SQ **Cournot** continuation, not zero production.

The menu is finite, prices not negotiated continuously. Rival deals share a given r and no extra monetary transfer is allowed. This is exactly the Stage-1/Stage-3 audited finite-menu subset. Instituting cost-saving, endogenous platform depth, country-vs-firm mismatched participation, extra transfers or new bargaining round would be a NEW research model, not a permitted Stage-4 repair.

## 2. Utilities, equations and equilibrium
For each destination k, quasi-linear utility
U_k=a 1' q^k - (q^k)'M(z)q^k/2. M_ii=1-v for ALL firms including singleton; M_ij=γ0 unless {i,j} forms the compatible contract, in which case M_ij=γ0+κ s-v (s=0 shallow, s=1 deep). Symmetric M required SPD (all principal leading minors >0) to ensure well-defined consumer utility. In each destination firms independently choose q_i^k≥0:
π_i,k=(p_i^k-c_i^k-r_i^k)q_i^k + receipts_i,k; p=a1-Mq; r is a PURE payment added to licensee private cost and licensor receipts.
Cournot complementarity: q_i≥0, 2M_ii q_i + Σ_{j≠i}M_ij q_j - a + c_i+r_i≥0, and product with q_i=0. Each positive-active-set quantity solves [M+diag(M)]_AA q_A = (a1-c-r)_A. Own-action second derivative -2M_ii<0. Since M is SPD, B=M+diag(M) is SPD, so the corresponding strictly convex quadratic complementarity problem has a unique solution. Verified all 2³ active sets per market, including off-path SQ and all six realized contracts. Every actual destination at the selected witness has the full active set {1,2,3}; no numerical failures or omitted KKT corners at these 7 contract-continuation regimes. Proof's *general* Cournot uniqueness follows from SPD B and linear complementarity / convex quadratic programming; formal theorem certification NOT claimed.
National welfare W_i=CS_i+Π_i (plus zero public transfer); worldwide firm profit Π_i includes ALL market operating profit and net royalty revenue; CS_i=q_i'Mq_i/2. For fixed quantities royalties cancel in global welfare; distorted quantities reflect their real economic consequences. Categorical comparison uses SAME national market populations, technologies, default and outside options.

## 3. Exact counterexample and controls
Take rational parameters:
a=1, γ0=1/10, v=1/10, κ=1/50, export c=3/20, royalty r=1/25, no real standard setup cost, and same M as above. All matrices SPD, all q_i^k>0 by exact active-set tests. Exact Fraction direct recomputation of every continuation matches SymPy and all CS/Π/W accounting.

For I12 relative to SQ:
ΔΠ1 = 1399449031/11985870400 (>0), ΔW1=23549357459/215745667200 (>0);
ΔΠ2 = 242265397/35957611200 (>0), ΔW2=−546708829/215745667200 (<0).
Thus F1,F2,G1 favor the contract but G2 vetoes. By country symmetry/order, for every two-country interface contract the royalty-paying participant government vetoes while its firm strictly benefits.
For P12, ΔΠ2=−1136902045509/189599277840500 (<0) and ΔW2=−2936387301577/189599277840500 (<0): fails even the private participation test.

## 4. Normal-form and *strong* equilibrium
Pure message-profile Nash exists (all SQ) by exact-consent coordination, even with profitable contracts, and hence is NOT informative about standard choice. All six full-signature accepted proposals have their real Cournot continuation, and unilateral veto gives SQ. For any fully matched single contract z under this restricted 3-state two-country-only institution:
  a) it is a Nash outcome if each required signer h weakly prefers V_h(z)≥V_h(SQ);
  b) another z' strongly blocks it exactly when ALL necessary signers P(z') strictly prefer V_h(z') to V_h(z), because every bilateral pair overlaps and every matched alternative requires its signers to change; no disjoint simultaneous contract exists;
  c) no agreement is strongly stable iff for every feasible z at least one of P(z) fails to strictly gain from z vs SQ.
This is an *elementary consequence of the exact-matching protocol*, NOT a publishable new coalition theorem. This compact criterion was CROSS-CHECKED against direct brute force of all 7^6=117649 pure joint message profiles, evaluating every change-coalition from each of the seven fully matched/no-deal representatives. Firm-only G-removed benchmark independently checked 7^3=343 profiles per representative. Strong stability used here is *strong Nash* (every deviator strictly gains); it is NOT recursively self-enforcing coalition-proof Nash (BPW) nor the core. Do not report unique equilibrium, general strong-Nash existence or evolutionary selection.

Exact outcome sets under STRONG-NASH screening in the listed menu:
- Joint all-G+F signatures: **{SQ}**.
- Government-only signature benchmark: **{SQ}**.
- Firm-only signature benchmark: **{I13,I23}** (under fixed license orientation toward smaller firm indices).
This shows a genuine public-approval barrier relative to a firm-only *counterfactual*, with uniform payoff-matched contract menus. However **JOINT = GOVERNMENT-ONLY** in this economy: the result does NOT establish an interaction unattainable in each simpler benchmark.

## 5. Sensitivity and limits
Switch only κ→0: joint {SQ} and private-only nonempty stable standards STILL survive (with deep and shallow equivalent). Thus alleged necessity of Ghosh–Morita product-differentiation change is **FALSIFIED** in this test.
Switch only v→0: joint and private-only both {SQ} — network effect matters for this numerical family but no globally necessary theorem follows.
Switch only r→0: joint and private-only strong-outcome sets coincide (bilateral interface outcomes).
Switch only γ0→0: joint and private-only strong-outcome sets coincide, indicating the role of positive baseline substitutability in the selected witness.
A separate Stage-3 deep-platform-veto witness with γ0=3/20,v=9/50,κ=1/20,c=1/20,r=3/50 survives as a *participation* result on an open royalty interval. However at the SAME royalty the shallow compatible interface is better for ALL its required signers; that witness fails to establish a deep-standard selection problem.
A diagnostic float grid over 1152 parameter tuples (1152 SPD+strictly interior cases, six deals each) identified 32 tuples with different firm-only versus joint strong-outcome sets, **zero** where the joint set differed from BOTH the firm-only and government-only sets. Grid bounds γ0∈{0.1,0.15,0.25,0.35}, v∈{0.03,0.1,0.18,0.25}, κ∈{0.02,0.05,0.1,0.15}, export c∈{0.05,0.15}, r∈{0,0.02,0.04,0.06,0.08,0.1,0.15,0.2,0.25}. This is a search diagnostic with finite scope, NOT a proof that no such divergence can occur anywhere.

Positive strict inequalities and SPD/interiority at the rational example imply an open set within its symmetric-cost, common-contract-fee parameter family where govt veto blocks all contracts, but the exact *two-element firm-only strong set* partly uses symmetry/tie equality, so do NOT claim that exact pair set is open under unrestricted national asymmetry.

## 6. Canonical general parent class and absorbed statements
Strip application labels: a finite noncooperative common-proposal/unanimity matching game with six agents, 7 actions per agent, heterogeneous individual continuation payoffs induced by SPD linear-quadratic concave subgames. The strong-blocking / all-null Nash results are direct consequences of known consent/coalitional stability classes (Hart–Kurz 1983; Yi 1997; Bernheim–Peleg–Whinston 1987). Firm standards + network effects + differentiated rivalry is heavily covered by Economides–Skrzypacz (2003), Lukach–Kort–Plasmans (2007), and de Palma–Leruth (1996). Ghosh–Morita (2012) explains collaborating firms' common design savings, distinctiveness, outsider interaction; our stripped baseline DOES NOT have real cost savings or outsider-differentiation η.
At Stage 4, no theorem of new whole-game economic content survives the requested simultaneous κ×v×r plus separate G/F authority comparison against both benchmark games. Absence of a single paper with identical terminology is not evidence for a new theorem.

## 7. Candidate-proposition ledger
| Candidate | Domain/result | Evidence | Disposition |
|---|---|---|---|
| P1 LQ national Cournot | SPD matrices and finite regimes, unique q with KKT | exact matrices, active sets, independent Fraction calculation | CORRECT WITH STATED DOMAIN; standard mathematical result |
| P2 Firm-approved but government-vetoed standards | rational 3-country example with strict sign inequalities | exact rationals, 7 complete continuations | CORRECT CASE EXAMPLE; directly known consent-complementarity mechanism |
| P3 Joint and firm-only strong outcomes differ | finite menu at rational witness: {SQ} versus {I13,I23} | exhaustive direct 7^6/7^3 deviations | CORRECT CASE EXAMPLE, no novel theorem |
| P4 Conflict requires κ>0 | κ=0 negative control | direct re-solved markets and strong deviations | FALSIFIED |
| P5 Joint group generates result unavailable in G-only group | rational witness: G-only={SQ}=joint | exact benchmark comparison | FALSIFIED IN WITNESS; not a global impossibility |
| P6 Deep platform uniquely selected / more depth necessary | shallow often strictly preferable, no real efficiency benefit | exact Stage3 witness; Stage4 finite menu | NOT SUPPORTED |
| P7 Unique standard bargaining equilibrium | all-null Nash, many mismatched profiles | finite consent rule proof | FALSIFIED |
| P8 General existence of strongly stable standards/CPNE | finite one-point check | no global proof | UNRESOLVED; NO CLAIM |
| P9 World welfare accounting | sum_i W_i = total CS + all profits | SymPy and independent Fraction | CORRECT identity with zero public/fixed setup costs |

## 8. Formal checklist disposition
KKT/corners: exhaustive 2³ per market for each feasible realized contract in witness. Boundary elsewhere: all finite regimes solved for witness; NOT an all-parameter solution. No sequential bargaining or interim adoption, so no off-path sequential bargaining continuation claim. Contract signing binds adoption by hypothesis. Normal-form unilateral and coalition deviations fully checked for the seven standard-outcome representatives; unmatched-message actions add only coordination Nash and do not create a new payoff object. Solver outcomes: 7/7 SPD market matrices, 21/21 strictly interior unique Cournot equilibria; 0 unresolved/solver errors at witness. Global statements about continuous transfer schedules and unrestricted standards menus NOT attempted.
Independent path: code/verify_stage4_independent.py uses Fraction Gaussian elimination and direct payoff reconstruction, without SymPy production solver; checked all quantity and government/firm accounts. AI-driven independent algorithm is NOT external human review and not Stage4A proof certification.

## 9. Consequence and diagnosed failure
The experimental institutional effect is **real**: split legal consent can veto a firm-profitable compatible standard. But the mechanism reduces to a standard veto/IR condition and is reproduced by government-only signing; κ-dependent product similarity is not necessary and deeper design sharing lacks a compensating real economic benefit. This does not meet the workflow Stage-4 requirement of a new economic generalization absent in each nested benchmark.

**NO-GO** for S3-A as formulated. Do not advance to Stage4A, Stage6 or a manuscript. No Stage5 fix is authorized because design/common-component real savings would alter the source model; the author must first select a genuinely different Stage-3 route and perform the requisite Stage1/2 source change/novelty recheck. Research findings and counterexamples are permanent records, not failures to be erased.

## 10. Next research choice (NOT AUTOMATICALLY AUTHORIZED)
S3-F: consider a separately scoped Ghosh–Morita **real** cost-saving mechanism as depth increases, or endogenous outside-versus-inside differentiation, and only adopt if a source-grounded marginal-resource/innovation mechanism plus contract choice generates a NEW and falsifiable governance/firm outcome. Must re-enter Stage 3 (mechanism authorization), Stage 1 (new demand/cost/payoff audit), Stage 2 (novelty search) before any Stage4 model. Alternative S3-E: mismatched public-private memberships, also requires rights re-audit. Author decides; no other GitHub branch or manuscript was created here.

## 11. Evidence / journal status
Sources: primary papers Economides & Skrzypacz https://papers.ssrn.com/sol3/papers.cfm?abstract_id=378340 and Ghosh & Morita https://www.sciencedirect.com/science/article/pii/S0167718711000671, with original Stage2 close-paper matrix. Reading-depth limits there still apply. No new theorem/novelty certification, no external review; all Stage4 scripts AI-generated, verified by GitHub CI and exact arithmetic only.