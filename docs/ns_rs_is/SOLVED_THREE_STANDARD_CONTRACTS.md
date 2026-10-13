# Stage 4 revised — NS, RS, IS complete one-shot negotiation benchmark
**Date:** 2026-10-13 | **Status:** MODEL-TESTED for two exact parameter economies; model-construction **GO to independent Stage 4A** on the extended game, NOT theorem-level novelty certification. This is a child of PR #6 and keeps the historical Stage-4 finite-contract NO-GO intact.

## 1. Stage-3/1/2 change-control
User requested international standard IS as an endogenous option, not merely an informal comparison. The existing RS parent (docs/two_sided/MODEL_AND_SOLVED_EQUILIBRIUM.md) had only bilateral coalitions. Newly add **IS** contract C={1,2,3}, depth t∈(0,1], signed jointly and exclusively by G1,F1,G2,F2,G3,F3. RS contracts still signed by their four required state/firm players and preserve outsider-distinctiveness parameter η=κ/2 (an assumed LQ stylization, NOT exact Salop microfoundation). An outsider does NOT have veto over RS. All exact-name messages are simultaneous; overlap prohibits a coexisting bilateral and global deal; contract binds subsequent technology implementation. Default NS Cournot firms still operate, with self-network value v retained.

Keep identical technical primitives for RS and IS: one participating firm saves h s real marginal production cost and pays f s² real setup/integration expense, irrespective of whether club size is 2 or 3. THIS holds per-firm cooperation benefit fixed and may understate additional true IS scale efficiency; it is a transparency condition, not empirical calibration. No royalties, government side payments, extra Ghosh–Morita outsider shift when there is no outsider, or newly invented negotiation priorities. Corporate and governmental objective functions remain separate.

## 2. Explicit demand, raw similarity and effective competition
Quasilinear national utility U_k(q)=a1'q−q'M(C,s)q/2; p=a1−Mq. Let m=1−v; g=γ0; κ>0 raw increase in SUBSTITUTABILITY from shared design; 0≤s≤1; v>0 interoperability-network benefit per linked other product (all products retain own installed-base benefit).
- NS: M0 diagonal m; all 3 off-diagonals g; all costs c0; no setup expense.
- RS for pair {1,2}: M_R(s)=[[m,b,d],[b,m,d],[d,d,m]], b=g+(κ−v)s and d=g−ηs, η=κ/2; participating unit costs c0−hs and outsiders c0; TWO real costs fs².
- IS: M_I(s)=[[m,b,b],[b,m,b],[b,b,m]], b=g+(κ−v)s for all THREE firm pairs; all costs c0−hs; THREE real costs fs².
Thus under IS, all three products become more substitutable due to raw κs, but network interoperability contributes −v s to effective cross-price-demand coefficient. If v>κ, the NET b decreases even while raw differentiation decreases. Do not confuse them or attribute RS outsider softening to IS with no outsider.
The LQ M is SPD, q>0 and Cournot unique throughout [0,1] for both rational regimes checked below; general domain must impose SPD and active-set KKT if a corner appears.

## 3. Completely solved Cournot, CS, firm and national welfare
For RS, member x_R and outsider y_R as fully rederived in PR #6:
 b=g+(κ−v)s, d=g−ηs, D=2m(2m+b)−2d², A=a−c0.
 x_R=[2m(A+hs)−dA]/D; y_R=[(2m+b)A−2d(A+hs)]/D.
Each destination CS_R=(m+b)x_R²+2d x_R y_R+(m/2)y_R²;
 participating firm Π_R=3m x_R²−f s²; outsider Π_O=3m y_R².
For IS, all three firms symmetric:
 q_I=(A+hs)/(2m+2b).
 CS_I=(3/2)(m+2b)q_I² per destination;
 each firm Π_I=3m q_I²−f s².
Each home government W_i=CS_(its market)+own firm's WORLDWIDE net profit; world social surplus = 3[ aΣq−q'Mq/2−Σ real c_i q_i]−number_of_signers(f s²). Royalties zero. No double counting of fixed costs. Firm's one-country operating margin = m q_i² at Cournot FOC. Exact independent Fraction Gaussian evaluator reproduces q, CS, Π, W and world accounting for NS, RS, IS at s=0,1/4,1/2,3/4,1 in both regimes.

## 4. One-shot equilibrium and *all* relevant coalition deviations
A complete contract message = (coalition C, standard depth s), or SQ. RS requires four matching consents, IS requires all six. A fully matched contract is individually rational iff every signer weakly prefers it to NS (veto -> NS). All SQ is ALWAYS ordinary Nash by unilateral inability to coordinate but strongly blocked when any coalition's required signers can all strictly improve from signing.

Coalition-strong deviations (strict improvement for EVERY deviator):
1. RS(C,s)→other RS(C',t): pairs overlap in one country whose G and F signers both move. With symmetric countries their payoff pair is (Π_R(s),W_R(s)) before and (Π_R(t),W_R(t)) after; such deviation exists exactly if both payoff types can strictly improve. Same-pair renegotiation has the same condition.
2. RS(C,s)→IS(t): all 6 signers must match the new IS proposal. Requires Π_I(t)>max{Π_R(s),Π_O(s)} AND W_I(t)>max{W_R(s),W_O(s)}. (For a profitable deviation all six participants strictly prefer their respective IS continuation.)
3. IS(s)→RS(C,t): four prospective RS signers can match; requires Π_R(t)>Π_I(s) AND W_R(t)>W_I(s). Outsider formerly IS-signing agents cannot veto a valid RS.
4. IS(s)→IS(t): all six signers change; requires Π_I(t)>Π_I(s) AND W_I(t)>W_I(s).
5. An active contract can be killed unilaterally if a necessary signer prefers NS; conversely ANY nonmatched message profile is coalitionally blocked by a profitable fully matched RS/IS contract in the two parameter economies (because a subset of actors can coordinate agreement from NS).
These tests use the same admissible final standard contracts and lawful signing rights. Strong Nash is not Bernheim–Peleg–Whinston CPNE; does not imply unique strategic-form Nash profile or unique cooperative bargaining solution.

## 5. Regime A: weak network v=1/10 (other primitives fixed)
Set a=1, c0=h=f=1/5, g=1/4, κ=3/20, η=3/40.
IS q_I(s)=2(s+4)/(s+23).
IS firm Π_I(s)=−(s⁴+46s³+475s²−432s−864)/(5(s+23)²).
IS national W_I(s)=−(s⁴+43s³+409s²−816s−1536)/(5(s+23)²).
P_IS strictly concave; unique firm maximum at s≈0.3505920. W_IS strictly concave; unique govt maximum s≈0.7188960 (exact second-derivative sign using positive Bernstein polynomial coefficients).
RS participating P and W strictly concave with unique optima:
 s_F,R∈(5319/10000,5320/10000) (~0.531949);
 s_G,R∈(8249/10000,8250/10000) (~0.824927).
For **EVERY** IS(t) ∈(0,1] there exists a RS contract of fixed depth t_R=1/2 whose FOUR future signers strictly prefer it. This is established using IS's strictly concave tangent upper bounds at 7/20 for Π_I and 7/10 for W_I; both upper bounds lie strictly below the corresponding RS(1/2) payoffs. Hence **NO IS(t) is coalition-strong**.
At every s∈[s_F,R,s_G,R], RS member P(s) is above the global supremum of Π_I; therefore RS cannot be blocked by IS, and its member P/W pair is Pareto-efficient, precluding alternative RS blocking. All member P/W exceed NS and their required signers accept. Exactly the three symmetry-related RS club identities with s in this interval are coalition-strong outcomes. (The no-agreement SQ message profile survives ordinary Nash but not strong deviations.)

## 6. Regime B: stronger network v=3/10 (hold other primitives fixed)
All M are SPD and all q interior on s∈[0,1]; independent exact checks.
IS q_I(s)=2(s+4)/(19−3s).
At s=1, each participating firm's profits Π_I(1)=397/640≈0.6203125; each national government's W_I(1)=1469/1280≈1.14765625.
For every s∈[0,1], IS Π_I(s) and W_I(s) are strictly INCREASING (exact positive Bernstein coefficient check of derivatives). For every RS depth t∈[0,1], IS(1) exceeds the P and W values of BOTH prospective RS members AND the current RS outsider — checked by exact strictly positive rational-polynomial Bernstein coefficients in all four cases. IS(1) also individually dominates NS. Thus:
- IS(1) cannot be blocked by any other IS or bilateral RS agreement, and is individually rational.
- Every RS(t) and NS is blocked by the SIX necessary signers coordinating to IS(1).
- **IS(1) is the unique strongly-stable CONTRACT OUTCOME** in this symmetric continuous menu. As always, normal-form Nash includes all-SQ and invalid contract messages as coordination profiles, so this is NOT uniqueness of ordinary Nash.

This yields a strict RS→IS change of *coalition-strong stability* at two different v values with all other model parameters and permitted contracts held fixed. By continuous payoff dependence and strict inequalities, the two witnessed regimes support nearby parameters too, subject to SPD/interiority. A UNIQUE single threshold in v is NOT derived, and some intermediate parameter ranges may allow coexistence/multiplicity.

## 7. Rival theories, limits and success standard
Economides & Skrzypacz (2003) already identified network intensity determining incompatible/regional versus full standards coalitions, so the general proposition "stronger network effects favor IS" is **NOT A NOVEL ECONOMIC THEOREM**. Ghosh & Morita (2012) already identified competition changes inside versus outside joint platforms. Added here are the explicit integrated Cournot/consumer welfare payoffs, endogenous depth and separate public/private signing rights — these constitute a genuinely solved comparative game but need Stage4A/Stage6 whole-game theorem-absorption challenge.

Important identification caveat: changing v changes the self-network diagonal m=1−v for ALL brands and the cross-network interoperability benefit for compatible products. This is how source Stage 1 defined v; it is NOT a pure increase in cross-brand compatibility with self-benefits fixed. Also IS assumes the SAME per-firm h and f as RS. Different consortium scale efficiencies would be a material source change.

**Stage 4 construction verdict: GO TO Stage 4A independent hostile certification** of the newly included six-signer IS deviation set, mathematical all-depth proofs, normal-form strong-Nash outcome classification, and prior-art absorption. NOT a manuscript or journal-readiness verdict. Preserve the previous RS-only construction.
