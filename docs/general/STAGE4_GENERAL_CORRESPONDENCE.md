# General NS–RS–IS Equilibrium Correspondence and Comparative Statics
**2026-10-14 (JST) | Stage-4 REENTRY after narrow Stage-6 NO-GO; theorem candidate, not current-paper novelty or Stage4A PASS.**
**Critical NEW result:** For all v∈[19/100,23/100] keeping a=1, c0=h=f=1/5, γ0=1/4, κ=3/20, η=κ/2, the simultaneous 6-agent two-key game has **BOTH** strongly-stable matched outcomes RS(1) and IS(1). In the matching firm-only-rights benchmark the stable standard class is RS; in the matching government-only-rights benchmark it is IS. This nonempty continuum of v-values was missed by the earlier v=.10 and v=.30 witnesses. It was rigorously established by exact tensor-product Bernstein rational polynomial certificates, NOT discretely sampled points. This is not a new economic-theorem certification relative to existing multidimensional coalitional veto games.

## 1. Backward-induction economic construction
Players G1,F1,G2,F2,G3,F3. Stage 1 simultaneously announce one fully specified named contract z∈{SQ, RS(C,s), IS(s)} with C any 2-country pair, s∈(0,1]; each RS requires four exact matching government+firm messages, IS requires six; non-signing outsider messages may preannounce alternatives without affecting the current RS. Stage 2, in every national market, three firms choose nonnegative outputs in segmented differentiated Cournot. Formed standard changes two-sided within/outside product substitution, linked network compatibility, and real member costs, in EXACT source model of parent PRs. No transfers, no ex-post voluntary adoption or regulatory subsidy. Government W_i=own CS_i + its resident firm's worldwide operating profit net one-time real integration expense.

Let A=a−c0, m=1−v, b=γ0+(κ−v)s, d=γ0−ηs and D=2m(2m+b)−2d²:
RS member quantity x_R=[2m(A+hs)−d A]/D; outsider y_R=[(2m+b)A−2d(A+hs)]/D. IS q_I=(A+hs)/(2m+2b). NS q_N=A/(2m+2γ0).
Each destination CS_R=(m+b)x²+2dxy+m y²/2, CS_I=3(m+2b)q_I²/2; member profit P_R=3m x²−fs², outsider O_R=3m y²; universal profit P_I=3m q_I²−fs²; member national W_R=P_R+CS_R, outsider U_R=O_R+CS_R, W_I=P_I+CS_I. No contract: P0=3m q_N², W0=P0+3(m+2γ0)q_N²/2. These are analytic functions of full primitive vector θ, on the SPD and Cournot-interior domain. Beyond this domain solve complementarity/KKT active sets, never extrapolate the formulas.

## 2. Application-neutral global accepted-outcome test (uniform over all matching message profiles)
An RS(C,s) matched contract is **robustly strong Nash as an outcome at EVERY supporting message profile** if and only if:
 (IR) P_R(s)≥P0 and W_R(s)≥W0;
 (R→R) there exists NO alternative t∈(0,1] such that P_R(t)>P_R(s) AND W_R(t)>W_R(s);
 (R→I) there exists NO alternative t∈(0,1] such that P_I(t)>P_R(s) AND W_I(t)>W_R(s).
An IS(s) matched contract is robustly strongly Nash if and only if:
 (IR) P_I(s)≥P0 and W_I(s)≥W0;
 (I→I) there exists NO t∈(0,1] such that P_I(t)>P_I(s) AND W_I(t)>W_I(s);
 (I→R) there exists NO t∈(0,1] such that P_R(t)>P_I(s) AND W_R(t)>W_I(s).
These are EXACT, dimension-reduced, set-valued equilibrium-correspondence conditions for arbitrary θ **within symmetric source LQ SPD/interior regime and strict-improvement strong Nash**, for the stated stronger 'every supporting message profile' property. Outsiders may preannounce an IS alternative under an active RS, making a 4-deviator RS→IS switch possible even if outsider agents lose. Therefore this UNIFORM outcome correspondence differs from the existence of SOME strong matching message profile; do not mislabel as all strategic-form strong Nash equilibria. Unmatched-message outcomes and ordinary Nash multiplicity remain separate. The criteria follow from exhaustive logical cases of every alternative final contract and indispensable changed signers; no generic theorem novelty claimed.

## 3. ALL-V-INTERVAL analytic theorem (not grid)
Freeze (a,c0,h,f,g,κ,η)=(1,1/5,1/5,1/5,1/4,3/20,3/40). Take EVERY v∈[0.19,0.23], every RS or IS depth t∈[0,1]. Exact symbolic source:
- RS, IS and NS market utility M(v,t) strictly SPD and each market Cournot output strictly positive;
- RS member government W_R'(t)>0; IS government W_I'(t)>0;
- P_R(1;v)>P_I(t;v) for EVERY t;
- W_I(1;v)>W_R(t;v) AND W_I(1;v)>U_R(t;v) for EVERY t;
- RS and IS private profit functions both strictly concave in depth, P_R'(0)>0>P_R'(1), P_I'(0)>0>P_I'(1); each unique interior optimum sF,R(v), sF,I(v);
- P_R,sv(t;v)>0, P_I,sv(t;v)>0, so **dsF,R/dv=−P_R,sv/P_R,ss>0 and dsF,I/dv=−P_I,sv/P_I,ss>0** across interval;
- RS(1) and IS(1) signers privately/governmentally prefer contracts to default NS.
All above verified by code/verify_general_standard_coexistence.py: expand every rational numerator and denominator under affine map v=19/100+(4/100)z, z∈[0,1], t∈[0,1]; transform BOTH polynomials to tensor Bernstein basis with *exact rational coefficients*; every coefficient STRICTLY positive. This algebra proves signs for uncountably many (v,t) values on the FULL closed rectangle. FOC and national CS/resource accounting inherited from explicitly verified source; new script reconstructs FOCs and the expenditure identity too.

**Consequences for fixed v throughout band:**
- RS(C,1): IR, no RS alternative improves W_R because W_R strictly increasing, no IS alternative improves P_R because P_R(1)>sup_t P_I(t); hence robust strong Nash despite possible outsider preannouncements.
- IS(1): IR, no IS alternative improves W_I because W_I strictly increasing, no RS alternative improves govt W because W_I(1)>sup_t W_R(t); hence robust strong Nash.
- Firm-only-signing nested game: unique firm-optimal RS depth sF,R(v) and 3 symmetric possible bilateral identities. No IS contract survives because P_R(sF,R)>sup_t P_I(t). The other side of the firm's rights does not enter.
- Government-only nested game: IS(1) dominates all RS member and outsider W and NS and W_I increases in depth, so unique strong CONTRACT OUTCOME IS(1).
- Joint government+firm signing game: BOTH RS(1) and IS(1) stable (plus possibly other depths not exhaustively classified; do not claim these are the only ones).
Result: the joint-rights game has a strictly larger set of possible STANDARD TYPES than either nested benchmark in the band. This is a concrete **full-game-only equilibrium correspondence result**, not yet proof of original economics beyond general coalition/veto logic.

## 4. New exact witness at v=1/5
Defaults: P_NS=256/735≈.348299, W_NS=464/735≈.631293.
RS(1) member P_RS=11285663/25425125≈.443878; W_RS=21409919/25425125≈.842077.
IS(1) P_IS=2/5=.4; W_IS=17/20=.85.
So the firm prefers RS(1) but government prefers IS(1); BOTH pass IR. Firm-only RS optimal depth belongs to (.8203,.8205), while G-only chooses IS(1). This is an exact-rational constructive *counterexample* to earlier Stage6 conclusion 'both nested games always predict same RS/IS type'. Earlier Stage6 conclusion only described the two v points .10 and .30, which remains true for those points.

## 5. Analytic cross-ranking thresholds, NOT globally solved mode-switch thresholds
At depth s=1, the RS/IS government welfare ordering changes at an algebraic root v_G≈0.184595370845337, numerator:
  15372800000 v^5 −55257600000 v^4 +76251600000 v^3 −49645235200 v² +14713896205 v −1443202319.
At depth s=1, the RS/IS firm profit ordering changes at v_F≈0.278975090072072, numerator factors
  3(v−1)(8000v²−8960v+1877)(56000v²−95360v+39787).
Exact root-count bounds certified in code. These thresholds refer to the TWO DEPTH-ONE CONTRACTS, not global all-depth RS↔IS comparisons. Numeric scans show RS only for v=.10–.18, RS/IS coexist for v=.19–.27, IS only for v=.28–.30, but outside [0.19,0.23] scan data are exploratory, **not** complete theorem-level coverage. No monotonicity or single-switch v threshold claimed.

## 6. Why Stage 6 must be reopened rather than replacing it
The previous Stage6 assessment properly rejected the **then-certified** two extreme parameter cases, which did not show any novel joint-rights-only standard structure. The presently certified **continuum of intermediate parameter values** supplies a new full-game-only strong-outcome MULTIPLICITY finding. However an earlier general principal-veto/coalition agreement theorem might imply that mixing two different participation interests generates a Pareto-undominated union; direct Hart–Kurz/Maggi–Ossa/coalition-proof parent theorem absorption remains an active threat, as do Economides–Skrzypacz and Bourreau–Doğan–Manant. This is an author-requested extension of analysis *without new primitives*. ROUTE: Stage4 construction (this branch) → independent Stage4A red-team for the **new parametric theorem** → Stage6 **REOPENED** (not automatic Stage7). Prior stage6 NO-GO historical record is kept unchanged.

## 7. Scope, benchmark welfare and caveats
Same three national consumer markets, both network self-effect and cross-brand interoperability moved together by v (hold this in mind for policy/structural interpretation); no real calibration. RS changes outsider relative product differentiation through stylized η=κ/2; IS all firms become part of one standard. Same member savings h and real cost f across RS/IS. Global coalition structure not characterized outside source contracts or outside symmetric SPD/interior regime; near-singular, output-corner cases excluded. For arbitrary θ the logical uniform equilibrium conditions are exact but generally implicit, not a globally unique closed-form solution. The obtained analytic interval is a genuine partial symbolic comparative-statics theorem and makes no claimed journal novelty by itself.
