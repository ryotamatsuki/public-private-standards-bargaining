# Stage 4A Independent Adversarial Audit — COMPLETE Reduced-Stage1 Strong Outcome Set
Date: 2026-10-14 JST | Original one-depth Cournot source | Stack: PR #22 => PR #23 => Stage4A.
**Verdict:** mathematical SCOPED PASS for an exact rational witness, **NO-GO novelty**. No main manuscript changes.

## 1. Red-team question and independent algebra

Does the stage4 privately optimal outsider exit point uniquely pin the negotiated RS depth? **NO.**
It is ONE reduced-stage1 strong Nash depth, at the LEFT END of a nondegenerate continuum of strong Nash depths.

No Stage3/Stage4 helper functions imported. Independently solve each of the 3 national product markets from the complete LQ consumer Hessian
`M_RS(s)=[[m,b(s),d(s)],[b(s),m,d(s)],[d(s),d(s),m]]`,
`m=1-v, b(s)=gamma0+(kappa-v)s, d(s)=gamma0-eta*s`.
The Cournot FOCs on the all-positive branch are
`[M+diag(M)] q=(1+rho s,1+rho s,1)'`.
For outsider-corner, solve the two-insider submatrix and verify
`1-2d(s)x_C(s) =Y(s)/[2m+b(s)]<=0`.
For NS and IS, rebuild their respective 3x3 Hessians and their FOCs afresh.
Consumer surplus is always `(q'M q)/2`, firm worldwide profit `3m x^2-phi s^2`, government payoff `P+CS`.
This independent implementation proves the correct branch equations and no discontinuity at the two switching roots. Positive-definite demand and positive insider quantity provide unique Nash Cournot continuation after every stage1 history.

## 2. Exactly specified model

The six independent exogenous parameters are
`(v,gamma0,kappa,eta,rho,phi)=(3/10,3/5,1/10,11/20,10,140)`,
with `a=13,c0=12,h=10,f=140` as a nonnegative-marginal-cost implementation.

The CORRECT outsider polynomial has **C=2(1-v)-gamma0=4/5**:
`Y(s)=(110s^2-111s+8)/10`.
Let
`s_-=(111-sqrt(8801))/220=0.07811979516834...`,
`s_+=(111+sqrt(8801))/220=0.93097111392257...`.
Outsider positive iff `Y>0`; zero otherwise. All five SPD inequalities hold strictly on [0,1].

The upper participation cutoff `s_IR` is defined as the UNIQUE root in `(0.14429,0.14430)` of
`P_C(s)=P_N=105/338`.
Equivalently it is the unique root on `[0.07,0.94]` of
`1352s^4-27040s^3+84503s^2-10200s-207=0`.
`s_IR=0.144296613782466...`.
Exact Sturm counts establish unique root on the outsider-zero segment; the other real roots of the quartic lie outside it.

## 3. Audited and stronger result: COMPLETE contract outcome correspondence

**Theorem (at theta*, including all continuous RS and IS rates).**
With 3 countries and 3 firms, the original one-round exact unanimous contract-signature protocol, unique KKT-Cournot continuation, and the *reduced FIRST-stage* strong Nash criterion, the complete strong Nash equilibrium **realized outcome set** is

`E_strong(theta*)={RS({i,j},s): {i,j} subset {1,2,3}, |{i,j}|=2, s_-<=s<=s_IR}`.

Proof with exact continuous sign certificates:
1. For active outsider `0<=s<=s_-`, both `P_A'(s)>0`, `W_A'(s)>0`. Each `RS(s<s_-)` is Pareto improved by `RS(s_-)` for all four incumbent signers. NS (even though always pure SPNE) is also jointly blocked by `RS(s_-)`.
2. On corner `[s_-,s_+]`, `P_C'<0`. For `[s_-,s_IR]`, `W_C'>0` and both resident-firm/government IR hold. Hence lower RS depth loses government welfare, higher RS depth loses firm profit. Other RS pair contracts necessarily overlap the current pair in one resident country and cannot improve both firm/government of this overlapping country.
3. Above `s_IR`, firm `P_R(s)<P_N`; these RS depths fail individual rationality and are not even pure SPNE. This remains true after reentry: `P_A'<0` and `P_A<P_N` on [s_+,1]. The Stage4 proof's unqualified "pinned negotiated rate" characterization is too strong: there is an *interval*, not a singleton.
4. Independent NS and IS calculation gives `P_I(t)<1/2` and `W_I(t)<7/4` for EVERY `t in [0,1]`. Meanwhile `P_R(s_-)>1/2`, `W_R(s_-)>7/4`. Thus EVERY IS contract is strictly Pareto blocked by the FOUR potential RS(s_-) signers: **NO IS strong outcome exists**.
5. For incumbent RS in [s_-,s_IR], `W_R(s)>=W_R(s_-)>7/4>sup_t W_I(t)`. No incumbent government will strictly prefer a proposed IS at ANY depth, even under preannounced outsider signatures; complete robustness is preserved. The incumbent's Pareto-frontier veto rules out all alternative RS depths.
6. For any candidate RS in the interval, the pure SPNE acceptance constraints hold; at `s_IR` firm is indifferent to NS, which suffices for weak unilateral Nash/strong Nash since profitable coalition deviations require *strict* improvements for all actual deviators.

All sign tests are exact rational numerator/denominator root-count certificates, not mesh searches:
- `P_A'>0,W_A'>0` over [0,0.08] covers full pre-exit branch.
- `P_C'<0` over [0.07,0.94] covers the full corner branch.
- `P_A'<0,P_A<P_N` over [0.93,1] covers all post-reentry output.
- `W_C'>0` over [0.07,0.15] covers [s_-,s_IR].
- `1/2-P_I>0`, `7/4-W_I>0` over [0,1].
- `P_C-P_N` has exactly one root on [0.07,0.94] and changes sign between 0.14429 and 0.14430.

**This is an equilibrium outcome classification, NOT unique pure SPNE or a unique signature profile**. Multiple first-stage announcement strategies can support each RS outcome.

## 4. Government/preference interpretation and novelty kill risks

At `s_-`, firm profit is approximately `0.837603589`, government welfare `1.872432659`, both strictly exceed NS. Government welfare continues to rise through `s_IR`, while firm profit decreases immediately upon outsider withdrawal. The unconstrained best RS welfare is approximately `s_G=0.173708278 > s_IR`, violating firm IR, so it cannot be implemented in this one-round bilateral public/private consent game without modifying the feasible payment menu or signature protocol.

However, NO demonstrated **RS-vs-IS type switch CAUSALLY driven by outsider exit** emerges at the witness; only RS survives for the selected parameters. A generic veto/payoff correspondence could reproduce the same market-type classification without a product-market KKT kink, so publication-level novelty remains **NO-GO**.

Nearest known parents (publisher abstracts/introduction verified October 2026, full appendices not certified):
- Ghosh & Morita (2012), *Competitor collaboration and product distinctiveness*, IJIO 30(2), 137-152, DOI 10.1016/j.ijindorg.2011.07.003, https://www.sciencedirect.com/science/article/pii/S0167718711000671 . Two incumbent collaborators become less distinct and more differentiated from outsider; welfare effects. Particular government/firm dual-signature kink theorem NOT established or excluded from publisher excerpt.
- Bourreau, Doğan & Manant (2016), *Size of RJVs with partial cooperation in product development*, IJIO 46, 77-106, DOI 10.1016/j.ijindorg.2016.04.004, https://www.sciencedirect.com/science/article/abs/pii/S0167718716300224 . Endogenous RJV size and scope, nonmonotone coalition scale. Full theorem coverage requires close reading.

## 5. Recommended next genuine research gate

Keep parent Draft PR #22 and Stage4 Draft PR #23 unmerged. Test a general or OPEN multi-parameter regime in which KKT support changes **strong outcome type** (RS only vs RS+IS, IS only) under a well-defined counterfactual that holds bargaining rights and other primitives fixed. Quantify the exact difference in type boundaries rather than comparing against an infeasible negative outsider Cournot continuation.
Stage4A scoped mathematical certificate is sufficient to proceed to such a search, NOT to manuscript or novelty GO.
