# Stage 5B — Reentry-mediated RS/IS strong-outcome bifurcation on an EXACT parameter interval

2026-10-14 JST. Stacked on Draft PR #25, which is stacked on PR #24, #23, #22. Keep all Draft and unmerged. This advances the old Stage5 "fee-only" negative identification to a **positive one-primitive differentiation experiment with a genuine feasible KKT comparator**. This is an application-specific exact theorem, **NOT YET an economically novel general theorem**. Stage6 NO-GO is retained.

## 1. Original source economy, one exogenous coordinate changed

Keep **five** of the original six independently normalized primitive parameters FIXED:
`(v,gamma0,kappa,rho,phi)=(2/5,2/5,3/20,13/2,65/4)`.
Vary ONLY original outsider differentiation `eta in [1/100,39/100]`, entirely within `0<eta<gamma0`. The ONE negotiated depth remains `s in (0,1]`. There are 3 countries with resident firms and independent government/private unanimous signatures; NS/RS/IS menu and real depth fee unchanged. A physically admissible underlying implementation is `a=17/2, c0=15/2, h=13/2, f=65/4`; marginal cost never negative. (The market normalization is `a-c0=1`.)

Set `m=1-v=3/5`, `b(s)=2/5-s/4` and `d(s)=2/5-eta*s`. Both member products have `z(s)=1+(13/2)s`. Uniform SPD across `0<=s<=1`, `1/100<=eta<=39/100` follows by the five endpoint conditions
`m-gamma0>0, m+2gamma0>0, m-b(1)>0, m+2b(1)>0, m(m+b(1))-2d(1,eta_min)^2>0`.
The final expression is strictly positive. All goods remain substitutes, including d(1)>=1/100.

RS Cournot active quantities come independently from
`[M_RS+diag(M_RS)](x,x,y)'=(z,z,1)'`.
If outsider zero, re-solve member 2x2 FOCs with `x=z/(2m+b), y=0`, outsider residual `1-2dx=Y/(2m+b)<=0`. Never use negative Cournot output as a fictitious benchmark.
The CORRECT outsider KKT support polynomial is
`Y(s;eta)=4/5+(-109/20+2eta)s+13eta*s^2`.
This has `Y(0)=4/5>0`, and `Y(1/2)<0` throughout the parameter interval.
At full depth `s=1`,
`Y(1;eta)=15eta-93/20`.

Hence **the second reentry transition crosses full depth at exactly**
`eta_KKT=31/100`.
For `eta<=31/100`, RS outsider at s=1 is zero; for `eta>31/100`, RS outsider at s=1 is strictly positive, so full-depth RS payoffs pick up outsider quantity. This is a comparison of actual valid Cournot equilibria under two genuine alternative primitive values, not an infeasible negative-output extension.

## 2. Uniform, independent algebraic depth audit

Reconstruct NS and IS 3x3 Cournot FOCs independently of RS. Firm worldwide `P=3m*x^2-phi*s^2`, participating government `W=P+(q'Mq)/2`; fixed fee charged once.

**EXACT bivariate Bernstein positive coefficient proof:** for the rational functions `P_RS_active(s,eta)` and `W_RS_active(s,eta)`, their derivative numerators (orientation corrected for the strictly negative denominator `10(-10D)^3`, D=positive Cournot determinant) have **all 56 tensor Bernstein coefficients strictly positive** on the entire rectangle `s in [0,1], eta in [1/100,39/100]`. Minimum Bernstein coefficients are respectively 366428.16 and 553902.08 (exact rational values internally). This proves both active-branch marginal payoffs are POSITIVE *for every eta and depth*, not merely a grid or endpoints.

For `P_RS_corner,W_RS_corner,P_IS,W_IS`, their derivatives are eta-independent and strictly positive on s in [0,1], verified by exact Sturm root counting and signs. The actual KKT piecewise payoffs join continuously at both support roots. Consequently, for EVERY eta in the admissible interval, participating firms and governments strictly prefer deeper standardization **within** each standard type. In the original reduced-stage1 strong Nash criterion, any RS(s<1) is jointly improved by RS(1) of the same coalition; IS(s<1) is improved by IS(1) for all six players. There are NO strong-depth equilibria other than s=1.

Both RS(1) and IS(1) satisfy strictly the four or six participant individual rationality conditions vs NS. IS(1) has exact `P_I(1)=115/4`, `W_I(1)=125/2`, and NS `P_N=9/20,W_N=39/40`.
For all eta in the interval, RS(1) resident-firm profit **strictly exceeds** IS(1) resident-firm profit; a global algebraic lower bound using `x_active>=430/81` proves this even near the KKT switch. For eta<=31/100, the RS outsider is absent and
`P_R(1)=1415/36`,
`W_R(1)=6745/108`,
hence
`W_R(1)-W_I(1)=-5/108<0`.
For eta=39/100 the outsider has reentered, giving
`W_R(1)=2344329205/37482172=62.545180279307...>W_I(1)=125/2`,
while `P_R(1)=10284020935/262375204=39.1958568424...>P_I(1)=115/4`.

## 3. EXACT critical parameter: status changes AFTER the KKT reentry switch

For eta>31/100, the true outsider-active RS national-welfare contrast at s=1 is the RATIONAL function
`W_R^A(1;eta)-W_I(1)=-3*F(eta)/[40*(2eta+1)^2*(10eta-13)^2]`, where
`F(eta)=420000eta^4-632000eta^3-55000eta^2+194840eta-40007`.
The denominator is strictly positive for eta in [31/100,39/100]. Rational Sturm root counting shows `F` has **EXACTLY ONE** zero on this entire interval, and strict opposite endpoint signs. Define it as
`eta_c≈0.385474362321989`.
Therefore:
`eta_KKT=0.31 < eta_c≈0.38547436 < 0.39`.

At and before eta_KKT, outsider-zero regime **shields** the full-depth RS government payoff completely from eta. After the outsider reenters, the active branch changes the payoff incidence; the sign change happens at eta_c, not exactly at eta_KKT.

**Additional nonmonotonicity theorem:** immediately after the outsider reenters, the RS participating government's national welfare initially FALLS as eta increases, despite the outsider gaining a foothold. It reaches its unique minimum on the genuine active branch at `eta_min≈0.3450299075` (strictly between 0.31 and eta_c), and then rises, eventually crossing the fixed IS national welfare at eta_c. An exact rational Sturm count gives exactly one zero of `d[W_RS^A(1;eta)-W_IS(1)]/deta` on `(0.31,0.39)`, with derivative negative at 0.31 and positive at 0.39. The sequence is therefore **KKT reentry at 0.31 -> RS government-welfare trough at approx. 0.34503 -> strong-type switch at approx. 0.38547**. The source-model channel combines outsider entry, within-market competitive displacement and a CS response, so do not label it a pure network externality effect. The market mechanism is genuine: the outsider is inactive in the baseline and active at the outcome where the standard ranking reverses. This is stronger than changing phi while leaving outsider support fixed, as in Stage5.

## 4. Complete first-stage reduced-strong outcome theorem on this entire eta segment

**Theorem.** For all eta in [1/100,39/100] under the foregoing fixed five primitives, the exact realized reduced-first-stage strong Nash standard/depth correspondence is

`E_strong(eta) = {RS(pair,1) for any 2 of 3 countries} ∪ {IS(1) if and only if eta<=eta_c}`.

Proof: strict depth monotonicity rules out every shallower s; NS is jointly blocked by RS(1) (all required resident govts and firms strictly gain); RS(1) cannot be jointly blocked by IS(1) because a member firm STRICTLY prefers RS(1), nor by another RS pair because in a 3-country market pairs necessarily overlap an incumbent country and that country's two required agents receive the SAME RS member payoff (no strict gain). IS(1) cannot be jointly blocked by another IS depth, but IS(1) can be blocked by any RS pair iff its private and government members both STRICTLY gain; private gain is always strict, so this holds EXACTLY when `W_R(1)>W_I(1)`, which is iff eta>eta_c. The crossing at eta_c itself is a weak government indifference; under the strict-improvement definition of strong Nash, IS still survives there. Outsider non-signers are not a veto to RS and no omitted late adoption/royalty actions are inserted.

The theorem holds on a **continuum of the original eta primitive, not just two endpoints**. The additional exact derivative check gives `F(0.385)>0>F(0.386)`, `F'<0` with NO critical root on `[0.385,0.386]`; hence the unique `eta_c` is a **simple root**. Since all depth derivatives are strictly positive on the compact rectangle, all relevant participation and preference inequalities are strict away from the phase boundary, and demand/KKT support at `eta_c,s=1` is strictly outsider-active, the implicit-function theorem yields a **locally smooth codimension-one six-dimensional selection frontier** `H(theta)=W_RS(1;theta)-W_IS(1;theta)=0` near the displayed critical parameter vector. The two open type-phase sides persist under sufficiently small perturbations of the other five primitives. This is a LOCAL conclusion; no global semialgebraic decomposition of all six dimensions has been proved. The same-depth comparison cancels the common fee `phi`, so the local welfare-indifference frontier is phi-invariant while depth-monotonicity continues to hold.

## 5. Major scientific caveats and nearest predecessor papers

- The theorem establishes a one-primitive **KKT-mediated** type switch: while RS's outsider remains inactive at the selected rate, eta cannot alter the RS government payoff; after outsider production reenters, eta has a nonzero effect and the government ranking ultimately reverses. It DOES NOT isolate a pure exogenous shock to quantity independently of changes in product differentiation. Thus causality is identified *within this structural primitive path*, not as a randomized experiment.
- Still NOT the whole six-dimensional phase diagram and NOT unique pure SPNE (all-SQ is pure SPNE under exact unanimous matching). Nor is the reduced-stage1 strong Nash an overall strong Cournot quantity equilibrium or coalition-proof Nash.
- Ghosh & Morita (2012), *Competitor collaboration and product distinctiveness*, IJIO 30(2) 137–152, DOI 10.1016/j.ijindorg.2011.07.003, https://www.sciencedirect.com/science/article/pii/S0167718711000671 . Publisher introduction establishes 3-firm two-collaborator model, outsiders, differentiation effects and welfare; their main characteristic-location model plus representative-consumer extension overlap our differentiation channel. Their exact no-output KKT and country-government double-consent theorem was NOT verified from the accessible excerpt.
- Bourreau, Doğan & Manant (2016), *Size of RJVs with partial cooperation in product development*, IJIO 46 77–106, DOI 10.1016/j.ijindorg.2016.04.004, https://www.sciencedirect.com/science/article/abs/pii/S0167718716300224 . Explicit endogenous scope/size with nonmonotonic differentiated oligopoly and Cournot; full theorem-by-theorem absorption NOT completed.
- Standard entry/exit KKT option value plus multiagent unanimity may entirely explain the result generically; **Stage6 NOVELTY GO requires proving a contribution irreducible to these predecessor classes**. Do not manufacture uniqueness claims from accessible abstracts.

## 6. Gate, artifacts and next priority

Exact reproduction: `code/stage5b_reentry_selection_threshold.py`. CI: `.github/workflows/stage5b-kkt-mediated-strong-type-switch.yml`. Stage5B theorem is exact and mathematically scoped PASS once Actions passes; independent hostile code audit and closest-theorem full proof comparison remain REQUIRED. Preserve upstream NO-GO / do not merge, and do not submit manuscript.
