# Institutional Stage 0/1 — Exogenous Authority Regimes, Proven Difference, and Conditional Endogenous Regulatory Override
2026-10-14 JST | Research direction explicitly authorized: compare FIXED institutional modes FIRST; endogenize regulatory/private interaction only AFTER a meaningful difference. This document contains precisely those two separated analyses and states remaining unsolved adoption dynamics.

**Baseline source economy unchanged:** `theta=(v,gamma0,kappa,eta,rho,phi)`, 3 national product markets, symmetric 3-firm Cournot continuation with correct outsider KKT, only one continuously selected depth `s in (0,1]`, standards NS, RS(pair,s), IS(s). All prior Stage0–6 pure SPNE vs REDUCED-stage-1 strong Nash caveats persist. **No silent manuscript edits; this is a new stacked Draft PR.**

## 1. Rights decomposition, NOT three payoff technologies

A named RS or IS contract has **identical product-market demand matrix, cost advantage z, real fee phi s^2, participant and outsider payoffs** in all three FIXED institutional regimes. Alter only signatory authority:

| Mode | Action authority | RS(pair,s) requires | IS(s) requires | What is NOT assumed |
|---|---|---|---|---|
| M — **private voluntary consortium** | Firms announce the same implementable OPEN compatibility agreement | 2 participating firms | all 3 firms | No governmental endorsement; **NOT market-share-driven de facto standard emergence**; unilateral patented platform adoption is unmodelled |
| R — **mandatory public interface** | Sovereign regulators coordinate a legally enforceable OPEN standard; firms choose Cournot quantity and may exit | 2 participating governments | all 3 governments | **No automatic patent rights**; no assumption states can force loss-making production; contract outcomes analyzed only if mandatory participant net payoff exceeds its exit payoff of 0 |
| J — **public–private consent** | Governments plus the implementing firms announce exactly the same contract | 2 govs + 2 firms | all 3 govs + 3 firms | Original dual-veto game; no first mover or within-coalition transfers |

Individual signers can unilaterally void a named agreement to default NS; non-signers do not veto the chosen type. Formal pure Nash implementation:
- M: `P_X(s)>=P_N`.
- R: `W_X(s)>=W_N`, PLUS physical/legal feasibility and firms' `P_X(s)>=0` (voluntary exit available, no patent impossibility).
- J: BOTH `P_X(s)>=P_N` AND `W_X(s)>=W_N`.

All-SQ is ALWAYS pure Nash in each protocol; none ensures unique SPNE. Stable sets are **REDUCED stage1 strong Nash** of signers' message game, never overall strong Nash of Cournot stage2. Under fixed payoff feasibility `IR_J=IR_M∩IR_R`; the R counterpart has an additional technology/firm-exit requirement. As a result, this rights-only J protocol **cannot create new IR-implementable technologies** or technological synergy. That is a crucial limit before building true public/private complementarity.

## 2. Proposition INST-1 — Different endogenous strong standard TYPES with identical original market primitives

Fix
`theta=(41/100,2/5,3/20,1/100,13/2,65/4)`.
At s=1 the outsider is strictly in Cournot zero-output KKT regime (`Y(1)=-453/100`), and all three market-demand matrices remain SPD on the entire s interval. Reconstruct 3x3 Cournot independent and prove by exact univariate Sturm root exclusion that **all SIX branch payoff functions** `P_R^active,W_R^active,P_R^corner,W_R^corner,P_I,W_I` are strictly increasing for `s∈[0,1]`. Thus any standard of depth s<1 is strongly blocked by the same signers' deeper s=1 contract in all modes. This is a true ALL DEPTHS proof, not grid sampling.

At s=1 EXACT:
- `P_R=79165/1936≈40.8910124`
- `P_I=162310/5329≈30.4578720`
- `W_R=62395/968≈64.4576446`
- `W_I=2766605/42632≈64.8950319`
- `W_outside_government(RS)=45625/1936≈23.5666322` (the nonmember home CS, its own firm y=0)
- NS `P_N=1475/3267≈0.45148454`, `W_N=6425/6534≈0.98331803`.

Hence private actors strictly rank **RS above IS**. Governments strictly rank **IS above RS** even for either current RS participant, and the excluded government also strictly gains by switching to IS.

**COMPLETE reduced-stage-1 STRONG outcome classification at this single ORIGINAL theta:**
`E_M^strong={RS(pair,1): all 3 pairs}`.
`E_R^strong={IS(1)}`.
`E_J^strong={RS(pair,1): all 3 pairs} union {IS(1)}`.
NS is a pure SPNE under all modes, but not strong. For M: the 2 private RS members strictly block each proposed IS, but they cannot improve by switching among overlapping RS pairs because an incumbent private signer would only get the same RS member payoff. For R: all 3 governments coordinate to change RS(1) to IS(1); conversely any RS proposal is vetoed by its 2 governors at IS(1). For J: existing RS members' firms veto IS, while IS government signers veto any RS proposal. The named pair symmetry means **coalition MEMBERSHIP is not uniquely determined**.

**Economic interpretation** (licensed OPEN technology only): the same fundamental network/differentiation/production environment can lead to regional-only private standards, international-only governmental mandates, or RS/IS coexistence under dual-consent governance. Distinguish selection/refinement from unique pure SPE. Institution is not yet strategically chosen; this is a comparison of exogenously fixed authority structures.

## 3. Proposition INST-2 — Regulation can implement a standard that an otherwise viable private consortium would reject

Same technology and economic specification, but set
`theta=(2/5,2/5,3/20,1/100,13/2,224/5)`,
and inspect international standard IS(1):
`P_I=1/5`, `P_N=9/20`; firm would strictly veto if asked to sign (0.2 < 0.45), **but** `P_I=0.2>0` means it will voluntarily remain in the product market even when noncompliant output or market exit is available as zero-profit alternative. On the public side `W_I=679/20=33.95>W_N=39/40=0.975`. Thus:
- IS(1) **cannot** be a pure signed-agreement Nash outcome under M or J.
- IS(1) **can** be a pure signed-agreement Nash outcome under R, given enforceable, freely implementable open technical requirements and firm exit at 0.
This example demonstrates **PRIVATE VETO ≠ legal ability to prevent public standard promulgation** and why regulatory and voluntary standardization cannot be collapsed into four/six universal signatures.
It is an implementability result for THIS depth; it does **not** classify all strong rate equilibria for the high fee theta.

## 4. First endogenous interaction, after exogenous modes have been shown to differ

**Minimal ordered policy/market interaction (provisional, conditional, not an unrestricted institution-choice equilibrium):**
1. Three firms can first voluntarily activate a fully named open RS/IS consortium standard or leave NS.
2. After observing their market standard, the three governments vote independently YES/NO on binding IS(1) recognition/mandate across all 3 countries. Only a UNANIMOUS YES activates the public IS(1) override; otherwise the private standard remains. Firms then choose Cournot quantities or exit as needed.
3. Apply the same strict strong-Nash coordination filter **to the government referendum stage**; record ordinary Nash's all-NO coordination trap and refrain from calling this unique SPNE. The regulatory **outcome decision** is endogenous to regulator preferences, while the override agenda (IS(1)), vote timing, and enforcement authority are institutional assumptions.

With theta of INST-1 (v=.41), exact bivariate Bernstein rational-coefficient certificates prove
`W_IS(1)>W_R_outside(s)` for EVERY `s in [0,1]` and even for every v in [.39,.41] on both algebraic active/corner Cournot branches, while monotone `W_R_members(s)<=W_R_members(1)<W_IS(1)` at v=.41. Hence ALL 3 governors strictly prefer IS(1) after **every** possible non-IS(1) initial voluntary firm outcome (including NS and IS(s<1)). All-YES is strong, and any non-IS(1) outcome is strongly blocked at the government vote; ex post the **regulatory override operates**. Anticipating this stagewise strong selection, private firms cannot produce a different final standard in the first stage (though the signed first-stage messages are not unique).

When **ONLY v** is reduced to 39/100 with all other original primitives FIXED, both incumbent RS(1) governors strictly prefer keeping voluntary RS(1) to the proposed IS(1) mandate: `W_R(1)>W_IS(1)`. Therefore the unanimous governmental override **fails** on that RS history and privately coordinated RS(1) can survive.

This is a genuine comparative-statics illustration of the government's **conditional ex post intervention decision** and private response. It is **NOT** yet a general full-game strong subgame-perfect equilibrium theorem, and the Stage1 private subgame/Stage2 government subgame each have coordination Nash profiles. A genuine full sequential game requires specifying acceptance of all histories, regulator constitutional competence, commitment to forbid/permit mandates, the firm cost/technology adoption option, and a non-arbitrary subgame selection protocol.

### Competitive and complementary channels: distinct claims

**Competition shown:** public IS(1) override can displace a voluntarily negotiated private RS(1), solely because governments internalize home CS and firms value their operating profit, despite common product-market network fundamentals.

**Complementarity NOT YET shown:** in the authority-only experiment, all regimes map the same standard contract to the same Cournot payoffs. Changing signers alone creates NO new technology or implementation surplus. At the PURE acceptance level J simply intersects M and R; at strong refinement J can sustain BOTH candidate standards due to different vetoes, but **this strategic coexistence is not technological complementarity**.

To genuinely MODEL joint complementarity, public recognition must change a downstream feasible interoperability/market-access opportunity or enforcement, while private technical development changes attainable technical efficiency/differentiation or licenses: `q^*(G=1,F=1)` must not equal the mechanically repeated fixed-contract equilibrium in both single modes. Preserve the 6 original quantitative primitives if possible by applying the already defined gamma,kappa,v,eta,rho through **two distinct discrete actions**, while verifying no mandate conjures unavailable IP rights, firms may exit, and regulatory recognition does not arbitrarily shift demand without its economic source. This is a future NEW freeze/rederivation, not a retroactive claim of the original model.

## 5. Primary literature that limits novelty and validates the institution taxonomy

- **David & Greenstein (1990)**, *The Economics of Compatibility Standards: An Introduction to Recent Research*, Economics of Innovation and New Technology 1:3–41. Their published survey distinguishes unsponsored market standards, sponsored private standards, voluntary formal committees, and direct government standard-making. https://www.tandfonline.com/doi/abs/10.1080/10438599000000002
- **Casella (2001)**, *Product Standards and International Trade: Harmonization through Private Coalitions?*, Kyklos 54:243–264; NBER precursor https://www.nber.org/papers/w5853. Private coalitions may cross national boundaries, countering a purely government standards view.
- **Belleflamme (2002)**, *Coordination on formal vs. de facto standards: a dynamic approach*, European Journal of Political Economy 18:153–176. https://www.sciencedirect.com/science/article/abs/pii/S0176268001000738. Formal vs de facto speed/quality and timing are already researched.
- **Takarada (2020)**, *Standards policy and international trade: Multilateralism versus regionalism*, Journal of Public Economic Theory, https://onlinelibrary.wiley.com/doi/10.1111/jpet.12425. Especially close **three-country and nationally segmented Cournot market** with public regulatory standard settings and regional/multilateral comparison; distinguish the externally affected technology/institutions, full proofs before claiming contribution.
- **Farrell & Simcoe (2012)**, *Choosing the rules for consensus standardization*, RAND Journal 43:235–252 https://onlinelibrary.wiley.com/doi/10.1111/j.1756-2171.2012.00164.x. Consensus voting and timing theory existing.

**Research decision:** Inst-1 and Inst-2 are mathematically accepted MODEL APPLICATION comparisons, **not publication novelty GO**. The first endogenous override subgame is conditional/partial, and proof that simultaneous market-vs-public standards can complement via technology is still required. Continue with Stage1 formal two-rights adoption/regulation game and exact all-history SPE verification ONLY after clean action timing and physical/IP feasibility are specified. No manuscript edit until that gate.
