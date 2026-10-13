# Stage 4A — Independent adversarial audit of SPNE-first and contract-stage strong Nash
Date: 2026-10-14 JST. Source branches: #17 (SPNE first), #18 (contract-stage coalitional refinement). This is NOT an automated Stage 6 economic novelty approval, nor a claim that all previous mathematical results are independently certified.

## Verdict / scope
**GO (limited, exactly stated)** for (i) the general pure-SPNE **contract outcome** characterization in the defined exact-matching two-stage game; (ii) its reduced **contract-announcement stage-1** strong Nash equilibrium OUTCOME refinement's exhaustive coalition/action-logic; (iii) two independently re-derived **all-continuous-depth** RS/IS coexistence witnesses at F=2/5 and F=10.

**HOLD** for (a) a full quantifier-free 5-dimensional parameter region partition, (b) a clean-room formal proof of every previous general high-F and fee-envelope theorem, (c) any interpretation of the reported first-stage refinement as strong Nash of the WHOLE extensive-form game, (d) coalition-proofness or a sequentially credible renegotiation bargaining protocol, and (e) economic novelty / Stage6 publication GO. Do not merge into default branch on this report alone.

## 1. Audited source game
Stage 1: six actors G1,F1,G2,F2,G3,F3 simultaneously announce SQ or an EXACT COMPLETE regional contract RS(named pair,s) or IS(s), 0<s<=1. RS is formed only if all government+firm actors of BOTH named member countries match the exact same offer (4 required signatures); IS requires all six; otherwise NS. Outsiders under an already matched RS may preannounce any future IS or RS and do NOT veto the current RS. No transfers or explicit renegotiation substage.
Stage 2: three firms play noncooperative Cournot in each of three national markets; firms pay one real fixed quadratic fee if adopting a standard. Governments obtain local CS+resident firm's world profit. For SPD/substitute demand in stated source domain Cournot equilibrium is unique for all post-message histories, including RS outsider zero-output KKT solutions; s and coalition identity endogenous, network externality strength exogenous.

## 2. General pure-SPNE contract-outcome theorem: independent proof
Call the unique Cournot-continuation resident-firm and government payoff at NS (P_N,W_N), RS member (P_R(s),W_R(s)), IS member (P_I(s),W_I(s)). Every match-supported pure SPNE outcome equals:
  NS ALWAYS,
  RS(C,s) iff P_R(s)>=P_N and W_R(s)>=W_N,
  IS(s) iff P_I(s)>=P_N and W_I(s)>=W_N.
Necessity: every essential signer can single-handedly break an existing match to NS; a strictly losing signer refuses. Sufficiency: choose exactly the essential signers to announce the offer and all nonessential outsiders to announce SQ. One changer can only abort to NS, not create another full 4-/6-signature contract. All-SQ is NE regardless of parameters because no ONE agent can form a standard.
**Not every unmatched NS message profile is NE**: whenever all required actors but one are already announcing an individually profitable complete contract, the remaining actor can join it alone. A general NS profile is NE precisely if no single individual's message switch completes another contract that gives that individual a STRICT profit/welfare gain. The mathematical theorem classifies pure outcome possibilities and pure message profiles separately; no mixed SPNE existence/selection results are asserted.

## 3. General reduced-stage-1 strong Nash characterization
Let B_X(p,w) be true iff there exists ANY valid t∈(0,1] with P_X(t)>p and W_X(t)>w. This is a STRICT simultaneous gain test, with correct piecewise Cournot continuation.

For a matching RS(C,s) with both outsiders initially SQ, necessary AND sufficient strong stage-1 stability is:
  P_R(s)>=P_N, W_R(s)>=W_N,
  NOT B_R(P_R(s),W_R(s)),
  NOT B_I(max[P_R(s),O_R(s)],max[W_R(s),U_R(s)]).
RS(C,s) as an outcome is supported by SOME full strong-Nash message profile iff these hold. RS(C,s) is strong for EVERY possible initial irrelevant outsider announcement iff the last blocker is STRENGTHENED to
  NOT B_I(P_R(s),W_R(s)).
For IS(s) necessary and sufficient stability:
  P_I(s)>=P_N, W_I(s)>=W_N,
  NOT B_I(P_I(s),W_I(s)),
  NOT B_R(P_I(s),W_I(s)).
NS can be a strong-Nash contract OUTCOME iff neither RS nor IS strictly improves all of its ESSENTIAL G/F signers relative to NS (all-SQ supports it).

**Proof exhaustive of coalition action changes in this 3-country source game:** Any changed realized outcome must be NS, RS(pair,t), IS(t). A coalition causing a new matched outcome need only include every ESSENTIAL required actor currently announcing something else; their messages are forced to change. If its members do not all strictly gain, no such deviation is profitable. To break the old RS for a different RS pair, at least one old pair government+firm must change because the two country pairs overlap. An alternative RS(pair',t) that is strictly profitable for the changed old overlapping member's firm/government is necessarily a strict Pareto improvement for BOTH original member countries if the ORIGINAL pair instead adopts the same t, by country symmetry; therefore same-pair B_R suffices to block ALL other-pair RS changes. An IS switch from an RS with outsiders SQ needs all six to change and strictly gain, but if BOTH outsiders originally PREANNOUNCE that specific IS(t), they are not actual deviators and may lose from the switch: hence the stronger all-supporting-profiles condition. Under IS all six must change to a different IS depth, and only the four RS members must change to an RS proposal.

In the whole game, the above is a **coalitional refinement of the STAGE-1 continuation-payoff normal-form game**, preserving sequentially rational noncooperative Cournot play. It is not a general coalitional equilibrium notion for the entire two-stage extensive-form game.

## 4. Independent source-code attack (not circular reuse)
File code/stage4a_independent_game_redteam.py imports NO previous Cournot/payoff/SPNE/strong verifier:
  - builds 3x3 normalized LQ inverse-demand matrices with exact Fraction coefficients;
  - independently solves every national Cournot market via CRAMER'S-rule/active-set enumeration of all 7 nonempty producer subsets, with rigorous zero-output KKT inequalities, and then calculates all six resident government/firm payoffs;
  - enumerates ALL 21 finite target contracts: SQ, 3 regional country pairs × 5 exact rational depths, and 5 international depths;
  - for matched RS profiles, exhaustively enumerates 21² distinct outsider original messages FOR EACH of 15 RS candidate contracts, namely **6,615 outsider-message settings per primitive economy**;
  - compares minimal necessary actual MESSAGE-CHANGING coalitions against the independently coded analytic B-style same-pair, cross-pair, IS and outsider-preannouncement conditions;
  - checks every essential signer can abort the matched offer, all-SQ unmatched NS, and near-complete unmatched NS profiles where a missing signer might profitably complete the agreement;
  - runs four distinct rational normalized economies, including F=1/4,2/5,10 at baseline market coordinates and a distinct RS-outside-producer EXIT/REENTRY corner parameter economy.

The finite-menu tests do NOT prove anything beyond those 21 named contracts and specific sampled market vectors; they are independent adversarial *counterexample search* supporting the separate generic combinatorial proof.

File code/stage4a_continuum_cleanroom.py also imports NO previous mathematical source payoffs: it directly INVERTS the 3×3 Cournot matrix symbolically for the baseline four market primitives (G,Lambda,Delta,rho)=(5/16,-1/16,3/32,1/4). It independently computes consumer surplus as 0.5*q'Mq, resident private profit after the one-time F*s² fee, and government W.

For two distinct fees and positive partial depths:
  F=2/5, stable RS(s=3/5) AND IS(s=13/20);
  F=10, stable RS(s=17/1000) AND IS(s=11/500).
At each, exact rational Sturm REAL-ROOT-COUNT proofs on the **ENTIRE interval [0,1]** certify: RS-member profit strictly exceeds EVERY IS firm payoff at any t, IS-government welfare strictly exceeds EVERY RS member govt W at any t, all four within-standard firm/government payoff curves strictly concave, each candidate depth lies strictly between its two individual maxima, all four individual-rationality margins strictly positive relative to NS, full SPD and RS-outsider output strictly positive at all depths. These are **full-depth-continuum mathematical certificates**, not gridded tests or external model/source code reuse. They independently corroborate the two positive-cost coexistence witnesses but not the generic five-parameter asymptotic theorem in PR #16.

## 5. Red-team conceptual finding: Cournot quantity stage is NOT strong Nash
For two Cournot firms i,j selling substitute goods (cross-price slope coefficient gamma>0) in an interior national market with own inverse-demand slope m>0, suppose both cut their Cournot-Nash quantities by identical small epsilon>0 while other firms' outputs stay fixed. Firm i's incremental operating profit is EXACTLY
    gamma*q_i*epsilon - (m+gamma)*epsilon²,
and likewise j (if symmetry q_i=q_j). For 0<epsilon<gamma*min(q_i,q_j)/(m+gamma) both strictly gain. Thus the Cournot continuation is GENERICALLY NOT a strong Nash equilibrium at its own second stage.
**Consequently**, one must NOT call the contract-stage strong refinement a 'strong subgame-perfect equilibrium of the full game' or assert that ALL profitable joint deviations of firms are blocked in all stages. To defend the hybrid solution concept economically, articulate binding/collectively renegotiable standard membership, but legally or institutionally separate NONCOOPERATIVE Cournot product-market quantity competition; alternatively build and solve an explicit sequential coalition-proof bargaining model. Bernheim, Peleg & Whinston (1987), JET 42:1-12 (doi 10.1016/0022-0531(87)90099-8) and Bernheim & Whinston (1987), JET 42:13-29 (doi 10.1016/0022-0531(87)90100-1) provide the equilibrium-concept comparators. Coalition-proof Nash, strong Nash, and subgame perfection are DISTINCT objects; no equivalence claimed.

## 6. NO new Stage6 originality decision
The mathematical findings show (a) exact-match noncooperative coordination causes many SPNE depths, and (b) stage-1 coalitional selection can eliminate jointly dominated contracts while leaving RS/IS coexistence. Both can be generic consequences of multilateral veto and unilateral coordination failure; nothing here proves they are novel beyond Hart–Kurz coalition structures or Bernheim–Peleg–Whinston. The high-F asymptotic theorem and baseline endogenous-depth data should now be subjected to theorem-level economic PRIOR-ART absorption against standards and endogenous-scope Cournot literature, not promoted automatically to a publishable mechanism.

## 7. Recommendations / explicit next gate
Keep research formulation with sequential game timing, **pure SPNE first**; then phrase the contract selection as 'strong Nash equilibrium of the first-stage proposal game given Nash–Cournot continuations'. If this ad hoc hybrid refinement is not institutionally defensible, reformulate one explicit multilateral negotiation protocol and rerun source equilibrium math. Before Stage6 novelty decision, do an independent FORMAL/general proof of high-F 5D comparative statics and the stage-1 full standard stability under all KKT corners if claimed at generic theta. PR must remain DRAFT and unmerged; old Stage6 NO-GO remains historical and cannot be automatically replaced by 'GO'.
