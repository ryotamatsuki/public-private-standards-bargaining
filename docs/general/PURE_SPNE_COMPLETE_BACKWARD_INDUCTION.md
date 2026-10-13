# First solve the two-stage game: PURE-STRATEGY SPNE baseline
Date: 2026-10-14 JST. Original one-endogenous-depth standards coalition model. This is logically PRIOR TO any Stage-1 strong-Nash selection analysis, and it does NOT replace/erase previous stronger-coalition results.

## 1. Game, subgames and assumptions
Players are G1,F1,G2,F2,G3,F3 (three national governments and their three globally active Cournot firms). At Stage 1 each simultaneously announces SQ, a *named* bilateral regional RS(C,s), or an all-country international IS(s), with s∈(0,1]. Contract RS(C,s) forms iff the government and firm for EACH of its two named member countries (four essential actors) announce that identical entire contract; IS(s) forms iff all SIX actors announce that identical entire contract. A nonmember under an actual RS can preannounce any other contract without changing the RS already formed. Failure of matching produces NS. No explicit random or political tie-break and no transfers. All Stage-1 messages are publicly observed before Stage 2; post-Stage-1 contracts are binding.

In Stage 2 each firm simultaneously selects quantities in each of the THREE nationally segmented markets, after observing the realized contract. Firms maximize global firm profit net the ONE-TIME member cost f*s²; governments do NOT directly choose quantities in Stage 2. Government payoff is own-country consumer surplus plus domestic firm's worldwide profit. The network strength v and demand/cost responsiveness are EXOGENOUS. Only contract type, its ONE commonality/standardization depth s and subsequent Cournot quantities are endogenous.

A well-defined stage-2 Cournot subgame exists for each complete stage-1 announcement profile, including nonmatching SQ histories. Work in the stated positive-definite differentiated quadratic utility/cournot regime with positive base demand and substitute goods, where the Cournot KKT system has a UNIQUE continuation at every possible s and contract. Do NOT blindly extrapolate an all-three-firms-interior formula: the RS outsider may rationally choose ZERO output and possibly reenter as s varies. Exactly as the verified previous mathematical work, this off-path boundary is part of the full SPNE continuation strategy.

## 2. Backward solve Stage 2 (five free composite parameters)
A=a-c0>0, m=1-v>0 and normalized primitives (G,Lambda,Delta,rho,F)=(gamma0/m,(kappa-v)/m,eta/m,h/A,m*f/A²). Quantities are scaled by A/m, every actor's net payoff by A²/m (positive scaling of ALL firm and government utilities). Define b(s)=G+Lambda*s, d(s)=G-Delta*s, D(s)=2(2+b(s))-2d(s)^2.

Under NS, EACH firm in each market produces n=1/[2(1+G)].
Under IS(s), EACH firm produces q_I(s)=[1+rho*s]/[2(1+b(s))].
Under RS({1,2},s), regional participants have common output x(s) and outside firm 3 has y(s). Let Y(s)=2+b(s)-2d(s)(1+rho*s).
- If Y(s)>0: x=[2(1+rho*s)-d]/D, y=Y/D.
- If Y(s)<=0: x=[1+rho*s]/[2+b], y=0.
At Y=0 both formulas agree; state the KKT zero-quantity limit explicitly. Uniqueness of the stage-2 Cournot strategy profile follows from SPD plus the strictly concave quadratic individual best replies and the strictly positive definite aggregate pseudo-gradient (M+I). Off-path continuation for EVERY proposed RS/IS contract depth is exactly this Cournot equilibrium, even if actual equilibrium play is SQ.

Let C_R(s)=(1+b)x^2+2dxy+y²/2, C_I(s)=3(1+2b)q_I²/2, C_N=3(1+2G)n²/2 be HOME-MARKET consumer surpluses. Member private payoffs are
 P_R(s)=3x(s)²−F*s²;
 P_I(s)=3q_I(s)²−F*s²;
 P_N=3n².
Member government payoffs are
 W_R(s)=P_R(s)+C_R(s);
 W_I(s)=P_I(s)+C_I(s);
 W_N=P_N+C_N.
The RS outsider has profit O_R(s)=3y(s)² and national welfare U_R(s)=O_R(s)+C_R(s). None of this outsider profit enters the RS member's participation condition.

## 3. PROPOSITION 1 — complete pure SPNE CONTRACT OUTCOME correspondence
Define C={12,13,23} and A_N, A_R(s), A_I(s) as the matched outcomes after Stage-1 messages. For every admissible original-theory parameter vector theta,

   E_SPNE^pure(theta)
   = {NS}
      ∪ {RS(C,s): C∈C, 0<s<=1, P_R(s)>=P_N and W_R(s)>=W_N}
      ∪ {IS(s): 0<s<=1, P_I(s)>=P_N and W_I(s)>=W_N}.

This is NECESSARY AND SUFFICIENT as the set of CONTRACT OUTCOMES induced by some PURE SPNE of the complete two-stage game. It is NOT claiming all mixed SPNE or a unique Stage-1 strategy profile.

Proof:
(i) By backward induction every Stage-2 proper subgame must use its unique Cournot equilibrium defined in §2, after ALL Stage-1 announcements including off path.
(ii) All six SQ at Stage 1 is a Nash message profile regardless of parameters: no ONE actor can unilaterally produce the four or six exact signatures needed to form any RS/IS. Thus NS is ALWAYS a pure SPNE outcome.
(iii) Suppose RS(C,s) is formed in a pure message profile. All four mandatory signers currently announce exactly RS(C,s). Any ONE required member firm or government can change its own announcement to SQ, destroying matching and yielding NS. Thus P_R(s)>=P_N and W_R(s)>=W_N are NECESSARY.
(iv) Those IR inequalities are also SUFFICIENT: assign those four mandatory signers exactly RS(C,s), all outsiders SQ. One incumbent signer unilaterally changes => NS; since IR, no one STRICTLY improves. A unilateral outsider message change cannot stop the four-way RS or generate any other completed RS/IS; one insider alone cannot form a different RS/IS because every alternative requires at least two of the four incumbents to change. Thus this matched RS profile is Nash. Irrelevant outsider messages may vary freely without affecting unilateral incentive to deviate, so every supported matched RS has the same NE condition.
(v) For IS(s), ALL six essential signers are matched. If any one changes, realized outcome is NS. No agent wants to do so iff P_I(s)>=P_N and W_I(s)>=W_N (six government/firm participation inequalities reduce by symmetry to two). This is NECESSARY and SUFFICIENT.
QED.

### Distinguish pure STRATEGY profile characterization from outcome existence
Let message profile M=(m_G1,m_F1,m_G2,m_F2,m_G3,m_F3), and denote realized outcome o(M). If o(M)=NS, M is first-stage NE iff, for every actor i and every completed contract X that i could trigger unilaterally by changing its message (meaning ALL other essential signers of X already announce the IDENTICAL X), the individual's continuation gain U_i(X)-U_i(NS) is nonpositive. Thus not EVERY unmatched message profile is an SPNE; 'five of six IS signers announcing IS' is NOT Nash when the sixth actor could profitably complete IS. All-SQ is ALWAYS Nash. If o(M) is a matched RS or IS, the IR tests above completely characterize Nash of M. These results and the unique Cournot continuation together characterize all PURE SPNE profiles, not just the possible outcomes.

### Crucial economic caveat
The exact-match simultaneous Stage-1 mechanism makes a unilateral deviation to a DIFFERENT depth t≠s automatically break the existing match. Therefore **ordinary SPNE does NOT choose the Pareto-efficient or profit-maximizing standard depth**. ANY s satisfying BOTH signer IR inequalities is supported, including depths that are strictly jointly dominated by some other depth or standard. Thus SPNE admits economically weak coordination/no-standard equilibria and extensive multiplicity. Strong-Nash Stage-1 refinement used in previous PRs removes many of these outcomes by permitting coalitions to simultaneously announce revised contracts. It is a FURTHER concept after reporting the complete SPNE set, not identical to SPNE or implied by it.

## 4. Exact fee-depth decomposition of all SPNE contract sets
Write each gross member payoff before one-time fee as P_X^0(s),W_X^0(s), with P_X=P_X^0-F*s² and W_X=W_X^0-F*s² for X∈{R,I}. Define the pointwise fee threshold
  T_X(s;mu)=min{[P_X^0(s)-P_N]/s²,[W_X^0(s)-W_N]/s²}, mu=(G,Lambda,Delta,rho).
Then the FULL endogenous-depth pure SPNE contract sets are exactly
  S_R^SPNE(mu,F)={s∈(0,1]:F<=T_R(s;mu)};
  S_I^SPNE(mu,F)={s∈(0,1]:F<=T_I(s;mu)}.
This is a genuine necessary-and-sufficient FIVE-dimensional payoff/participation classification of WHICH STANDARD DEPTHS can be realized as SPNE contracts. There are no intra-type or cross-type Pareto blocker conditions under SPNE. Each function T_X(s;mu) is piecewise rational, including the RS outsider KKT root Y(s)=0. The set of all admissible stable depths may be intervals or unions and can have endpoint ties. For fixed rational parameters, its boundaries come from zeros of the two exact rational polynomial numerators P_X^0(s)-P_N-F*s² and W_X^0(s)-W_N-F*s² plus RS corner roots, and are thus exactly decidable with algebraic real-root isolation (independent of network grids). Even if F rises above a full-depth s=1 threshold, the contract's shallow s SPNE set may be NONEMPTY.

Let Phi_X(mu)=sup_{0<s<=1}T_X(s;mu). Then a positive-depth X-SPNE exists whenever F<Phi_X and does not exist if F>Phi_X. At F=Phi_X it exists iff the supremum is ATTAINED at some s>0; do not silently assume max attained because s=0 is excluded. This is distinct from but logically consistent with the previous strong-NS threshold: NS is always pure SPNE for ALL F, whereas NS is STRONG-NASH iff no participating coalition can strictly gain and may fail when F<Phi.

If P_X^{0'}(0)>0 and W_X^{0'}(0)>0, then T_X(s)~min{P_X^{0'}(0),W_X^{0'}(0)}/s →+infinity as s↓0; thus X-participation SPNE exists for EVERY finite quadratic fee F. This does not ensure a unique or socially desirable standard. In particular, the previous K_R>0 with substitution-domain positive consumer surplus slope makes RS(s) available as a pure SPNE for arbitrarily high F, while NS remains pure SPNE.

## 5. Exact independent strategy-profile test coverage
Script code/verify_pure_spne_complete.py reuses the source-approved piecewise Cournot KKT evaluator code/verify_six_dimensional_corners.py but constructs an INDEPENDENT full-message-profile unilateral-deviation enumerator. For any original rational economic parameters and a specified rational matched contract:
- Create all six original agent offers (G1,F1,G2,F2,G3,F3), with RS outsiders SQ or optionally preannouncing a target IS;
- Mechanically resolve exact 4-signature RS / exact 6-signature IS;
- Enumerate the SQ action and all distinct contracts already named by other players as alternative one-actor messages; any NEW contract never mentioned by other essential signers cannot be completed by a single message change, so this FINITE enumerator covers the uncountable contract-action set for unilateral deviation testing;
- Calculate exact continuation firm/government payoffs INCLUDING RS outsider roles; assert message-profile Nash iff signer IR for each named contract;
- Verify that all-SQ is Nash at v=.1,.2,.3; a PARTIALLY matched NS message profile with one remaining profitable necessary RS signer is NOT Nash; an NS profile with only one hopeful initial signer IS Nash; and there is an IR RS(s=.1) SPNE that FAILS strong Nash because incumbent coalition prefers another contract;
- Verify SPNE at regional/international partial-standard cost F=.4 and off-path outsider zero output.
The code checks sample profiles and algebraic identities; the complete generic proposition is proved analytically above, not inferred merely from these test samples.

## 6. Publication order and pending gate
Recommended logical paper layout:
  * Section 2. Timing, players, exogenous network parameters and endogenous depth s.
  * Section 3. Cournot subgame (Lemma 1: unique Cournot + boundary KKT).
  * Section 4. Pure SPNE (Proposition 1: exact matched-contract participation sets + all-SQ coordination equilibrium).
  * Section 5. Coalitional refinement (Definition strong-Nash Stage-1, full continuous-depth strong outcome correspondence from parent PR #16).
  * Section 6. Economic mechanism propositions, welfare and comparative statics; strict firm RS vs govt IS disagreement; cost-dependent endogenous-depth stability and coexisting partial standards.
  * Stage4A independent mathematical red-team BEFORE Stage6 novelty absorption and eventual manuscript.
SPNE alone is an excessively permissive solution concept under this particular simultaneous exact-match technology. Any selective theorem about endogenous realized depth or standard type MUST state an additional equilibrium refinement, bargaining protocol or selection criterion. It is inappropriate to relabel strong Nash as SPNE or claim backward induction alone picks a unique standard.
