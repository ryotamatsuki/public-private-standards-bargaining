# Stage 5 — Multi-parameter equilibrium-type phases with IDENTICAL Cournot support switching
**2026-10-14 JST | Source six-exogenous-parameter/one-endogenous-depth NS–RS–IS game.**
Parent Stage4A Draft PR #24. **Scope:** exact six-dimensional *witnesses* and a general same-depth welfare sign lemma, NOT a full quantifier-free six-dimensional phase diagram.
**Scientific verdict:** SCOPED mathematical result, NO publication novelty clearance, Stage6 NO-GO unchanged.
**Critical causality caveat:** the type switch below is induced by a fee change at FIXED outsider support geometry. This proves outsider exit is NOT SUFFICIENT to determine which standards survive strong Nash. It does NOT prove outsider exit *causes* the type switch.

## 1. General corner-welfare incidence threshold (proof, entire parameter domain)

Let `m=1-v>0`, `b=b(s)=gamma0+(kappa-v)s>0` with substitutability `b<m`,
`d(s)=gamma0-eta*s>=0` and `z=1+rho*s>0`. Suppose demand is strictly positive definite and the regional-standard Cournot outsider satisfies its zero-output KKT inequality `Y(s)=2m+b-2dz<=0`. Under RS, each participant produces `x_R=z/(2m+b)`, and the outsider has `y_R=0`. Under IS all three firms produce `q_I=z/[2(m+b)]`.

In the original model private and national welfare per participating country, for the SAME `s` and SAME quadratic real adoption fee `phi*s^2`, are
`P_R=3m*x_R^2-phi*s^2`,
`W_R=(4m+b)*x_R^2-phi*s^2`,
`P_I=3m*q_I^2-phi*s^2`,
`W_I=[(9/2)m+3b]*q_I^2-phi*s^2`.
Thus FEE CANCELS between formats at a fixed depth. Exact identities:
`P_R-P_I=[3 b m z^2 (3b+4m)]/[4(m+b)^2(2m+b)^2]>0`.
`W_R-W_I=[z^2(2b^3+15b^2 m+12b m^2-4m^3)]/[8(m+b)^2(2m+b)^2]`.

Set `u=b/m`. The polynomial `F(u)=2u^3+15u^2+12u-4` has `F'(u)=6u^2+30u+12>0` for `u>=0`, `F(0)<0<F(1)`, so precisely one positive root
`u*=0.251570279593411...`.

**CORNER INCIDENCE THEOREM:** for any admissible RS zero-outsider regime at any fixed standard depth `s>0`, participant firms strictly prefer RS to IS whenever `b>0`; participating states strictly prefer IS for `0<b/m<u*`, are indifferent at `u*`, and prefer RS for `u*<b/m<1`. Strict cases persist over open parameter neighborhoods where the KKT corner remains binding. Both RS continuation payoffs on the zero-output branch are locally **independent of outsider differentiation eta** (holding b,m,z,phi fixed).

**IMPORTANT:** these are *same-depth preference* comparisons, not yet Pareto/strong-Nash selection over all alternative `t`. Government cannot impose IS unilaterally under the dual public/private signature rule. The condition is a familiar surplus-incidence calculation, not automatically new theory.

## 2. Two completely certified and dramatically different selection phases, SAME five other parameters

Hold
`(v,gamma0,kappa,eta,rho)=(1/5,1/10,1/5,1/10,40)`.
Physical normalization `a=41,c0=40,h=40` keeps `a-c0=1` and `c0-hs>=0` for all depths; actual `f=phi`.
For NS/RS/IS every demand matrix is SPD throughout `s in [0,1]`, all individual quantities satisfy correct KKT conditions.
`m=4/5`, `b(s)=1/10`, `d(s)=(1-s)/10`; in particular `b/m=1/8<u*`.
Outsider support polynomial is **independent of phi**:
`Y(s)=8s^2-(39/5)s+3/2`.
Two simple roots are
`s_-=(39-sqrt(321))/80=0.2635440891603885...` and
`s_+=(39+sqrt(321))/80=0.7114559108396115...`.
The outsider exits at `s_-` and reenters at `s_+` in **BOTH** economies below.

### 2A. phi=400: complete strong type and depth classification

Exact 3×3 Cournot red team, including the corner branch, proves all **six** curves `P_R^A,W_R^A,P_R^C,W_R^C,P_I,W_I` strictly increase over the WHOLE algebraic extension `s in [0,1]` (hence over their respective correct support segments). These are rational Sturm root-exclusion certificates, not numeric grid checks.

At `s=1` outsider reentered, and
`P_R(1)=287840/289≈995.986159`;
`W_R(1)=14053605/9248≈1519.637219`;
`P_I(1)=22820/27≈845.185185`;
`W_I(1)=87665/54≈1623.425926`.
NS `P_N=20/27≈0.740741`, `W_N=65/54≈1.203704`.

Private strictly prefers RS(1) over IS(1), but government strictly prefers IS(1). Every shallower RS depth is Pareto-dominated by RS(1) for incumbent signers; every shallower IS depth by IS(1) for all six signers. No RS(t) can dominate IS(1), because government `W_R(t)<=W_R(1)<W_I(1)`. No IS(t) can dominate RS(1) because private `P_I(t)<=P_I(1)<P_R(1)`. Thus exactly the following *realized strong-Nash OUTCOMES* survive:
`E_strong(phi=400)={RS(pair,1),IS(1): pair any of the 3 pairs}`.
NS always pure SPNE but is reduced-stage1 strong blocked by these improving contracts.
The claim is robust even if outsider preannounces IS when incumbents currently hold RS(1).

### 2B. phi=1400: strong RS EXISTS, every IS and NS STRONG BLOCKED

The KKT polynomial and its two roots are UNCHANGED. Nevertheless complete **strong STANDARD TYPE** set is `{RS}`.

The RS zero-outsider private payoff is exactly
`P_R^C(s)=240(1+40s)^2/289-1400s^2`,
strictly concave with **unique corner private maximum** at `s_F=48/103=0.4660194174757...`, strictly between `s_-` and `s_+`.
Sturm tests show the active branch private profit increases on `[0,s_-]` and decreases on `[s_+,1]`, so `s_F` is the UNIQUE global maximum across all physically feasible RS depths. Exactly
`P_R(s_F)=1680/103≈16.310680 > P_N=20/27`;
`W_R(s_F)=1447530/10609≈136.443586>W_N=65/54`.
All IS private profits are strictly below `P_R(s_F)`: their unique global peak is `P_I(4/29)=140/29≈4.827586`.
Therefore RS(pair,s_F) is a reduced-stage1 strong Nash equilibrium, immune to every other RS depth and every IS depth due incumbent private veto.

IS individual rationality:
`P_I(t)-P_N=-(200/27)t(29t-8)`,
`W_I(t)-W_N=(200/27)t(71t+13)`.
Therefore only `0<t<=8/29` is IS-SPNE eligible. For **EVERY** such t define the alternative RS contract at `s_R=(6/5)t`.
Independently recompute the RS Cournot KKT branch at `s_R`.
Exact rational Sturm certificates for
`[P_R((6/5)t)-P_I(t)]/t>0` and
`[W_R((6/5)t)-W_I(t)]/t>0`
cover `t in [0,0.22]` with the true active branch and `t in [0.219,0.276]` with the true corner branch, with overlapping rational envelopes around the exact algebraic switch `t=(5/6)s_-` and `8/29<0.276`.
Thus every individually-rational IS contract is strictly blocked by a coordinated RS contract signed by the two participant countries' FOUR agents. Any IS outside that interval is not even pure SPNE. NS is blocked by RS(s_F).

**DO NOT overclaim:** full RS strong-depth correspondence at phi=1400 was NOT classified. We proved presence of RS(s_F), complete elimination of IS and NS strong outcomes, and hence a complete standard-TYPE classification only.

## 3. Correct economic interpretation and limitations

- Both configurations have EXACTLY the same `Y(s)`, active sets and exit/reentry rates; a scalar real-standardization-fee parameter determines whether IS coexists or is eliminated.
- At phi400 the realized strong rates equal 1, where outsider has **reentered**.
- At phi1400 a strong RS rate equals 48/103, where outsider is **inactive**.
- This is a strict multi-dimensional equilibrium-type phase contrast; the qualitative phase examples are stable under sufficiently small primitive perturbations, with the usual preservation of simple KKT roots, sign margins, and smooth first-order conditions.
- The result is a NEGATIVE causal identification test for a too-strong Stage5 novelty claim: two-switch outsider support alone does not imply exclusion of IS or uniqueness of standards.
- It does NOT prove a KKT-induced reversal relative to an otherwise-identical no-exit economic structure: at fixed primitives Y(s) is invariant in phi, and the fee effect would exist without the KKT mechanism.
- Do not compare against negative outsider production extrapolated from an infeasible Cournot FOC and call that a causal counterfactual.
- The whole-game SPNE is not unique (all-SQ remains pure SPNE); stage2 Cournot is not overall strong Nash; only reduced stage1 contract-signature strong Nash is meant.

## 4. Closest literature and novelty gate

Ghosh–Morita (2012), *Competitor collaboration and product distinctiveness*, IJIO, DOI 10.1016/j.ijindorg.2011.07.003 (publisher text https://www.sciencedirect.com/science/article/pii/S0167718711000671) already analyzes two collaborative competitors, outsiders, differentiation and welfare. Bourreau–Doğan–Manant (2016), *Size of RJVs with partial cooperation in product development*, IJIO, DOI 10.1016/j.ijindorg.2016.04.004 (publisher https://www.sciencedirect.com/science/article/abs/pii/S0167718716300224) already analyzes endogenous RJV scope/size and nonmonotonicity. Main-text previews and abstracts were consulted; the full theorem-by-theorem novelty audit, especially their proofs/appendices and Cournot corners, remains INCOMPLETE.

Exact proof implementation: `code/stage5_kkt_selection_phases.py`. CI: `.github/workflows/stage5-kkt-selection-phases.yml`.
**Stage5 outcome: two valid phase witnesses and one sharp general corner-incidence threshold. NOT the entire six-dimensional semialgebraic partition. Stage6 novelty NO-GO maintained.**

## 5. Next gate

Determine whether zero-output KKT regime boundaries cause a **qualitative** equilibrium TYPE bifurcation when moving across them, holding fixed all but one meaningful original primitive, with an explicitly feasible no-exit counterfactual and a theorem-level control for the primitive's direct impact on competition. Prefer an analytically certified cutoff in e.g. eta or rho and a clean "before/after" pair with matched institutional rights and feasible positive Cournot quantities. If absent, abandon the strong originality claim and consider a restricted economic application or different mechanism instead of proliferating parameter examples.
