# Stage 4 — Exact network thresholds for the ORIGINAL one-depth standards game
Date: 2026-10-14 JST. Parent: Draft PR #12 general NS/RS/IS backward-induction outcome correspondence; this branch is a **fixed-other-primitives parametric theorem**. NOT optional two-choice PR #11. NOT a fully general 8-dimensional parameter-cell decomposition, an independent Stage 4A verdict, or an economic novelty PASS.

## 1. Theorem and its exact scope
Three symmetric nations/governments and resident firms, three segmented national differentiated Cournot markets, 6-player simultaneous exact-contract standard proposals. Four matched G/F actors activate a regional standard RS, all six activate universal IS, none gives NS; standard depth s∈(0,1] endogenous and network-intensity v exogenous. Match and joint-deviation logic as source PR #12, including outsiders' payoff-irrelevant off-path preannouncements and existence-vs-uniform-stability distinctions. Strict-gain strong-Nash concept; messages, exact identity and depth matter, but only **realized contract outcome types** are classified.

Freeze a=1, c0=h=f=1/5, gamma0=1/4, kappa=3/20, eta=3/40. Let network v vary freely on the ENTIRE closed interval [3/20,17/50]=[0.15,0.34]. Source own-network demand diagonal m=1−v and cross compatibility shift −vs BOTH vary with v; this is NOT a pure interoperability comparative static holding own-value fixed.

Set b(s)=gamma0+(kappa−v)s, d(s)=gamma0−eta*s, D=2m(2m+b)−2d², A=a−c0. Backward Cournot output: regional insiders x=[2m(A+hs)−d A]/D, regional outsider y=[(2m+b)A−2d(A+hs)]/D, IS q=(A+hs)/(2(m+b)); NS q0=A/(2(m+gamma0)).
Under Cournot FOC: participating private net profits PR(s)=3m x²−f s², PI(s)=3m q²−f s², outside private profit OR(s)=3m y²; each home government's W_X(s)=own market consumer surplus + worldwide resident firm's Π_X. Source accounting and SPD/internal outputs all checked over entire v×s rectangle.

### Two transition parameters are unique algebraic roots
Define α as the **unique root in [0.15,0.34]** of the quintic
  15372800000 v^5 −55257600000 v^4 +76251600000 v^3 −49645235200 v² +14713896205 v −1443202319 = 0.
It is characterized by W_I(1;α)=W_R(1;α) and lies in (184595/10^6,184596/10^6), numerically α≈0.184595370845337.

Define β as the **unique root in [0.15,0.34]** of
  3(v−1)(8000v²−8960v+1877)(56000v²−95360v+39787)=0.
It satisfies P_I(1;β)=P_R(1;β) and lies in (278975/10^6,278976/10^6), numerically β≈0.278975090072072.
Both uniqueness, ordering and signs near the roots are checked with exact polynomial real-root-count and rational inequalities; denominators of both payoffs have constant positive sign on the theorem domain.

### Headline FULL standard outcome-type partition
- For **0.15≤v<α**: at least one RS contract (in particular RS(s=1)) is a strong-Nash contract outcome, **no IS contract** is strong-Nash stable. NS is not strong-stable.
- For **α≤v≤β**: both RS(s=1) and IS(s=1) are strong-Nash contract outcomes. NS is not strong-stable.
- For **β<v≤0.34**: IS(s=1) is a strong-Nash contract outcome, **no RS contract** is strong-Nash stable. NS is not strong-stable.

"RS exists" always includes three symmetric bilateral identities. Within each type there may be OTHER stable depths; the theorem does not claim unique contract identity, unique message profile, or closed-form total depth correspondence. At α and β equality means strong Nash's STRICT-gain rule preserves both outcomes; do not silently use weak Pareto blocking. For v strictly in (α,β), the nested benchmark with only firms as necessary signers has RS as its stable standard class; only governments as signers yields IS. On endpoints tied nested outcomes can arise; do not claim strict nested uniqueness there.

## 2. Proof architecture — all depths, not a network grid
The code \`code/verify_network_switch_exact.py\` constructs exact rational Cournot and welfare functions in (v,s), verifies the SPD principal minor inequalities for NS/RS/IS, interior Cournot positive x,y,q and FOCs/resource accounts.

For every positivity claim numerator AND denominator separately: map each claimed rational v range linearly to u∈[0,1] and s∈[0,1], express the polynomial in 2D Bernstein basis with *exact rational coefficients*, and check that every coefficient is positive. When coefficients have mixed sign, bisect u or s recursively with exact-rational de Casteljau operations until every child patch has strictly positive Bernstein coefficients. A positive Bernstein coefficient collection is a constructive sufficient proof of strict positivity for all real points in the box, not a sample or optimizer report.

Core globally certified inequalities and joins:
(A) **dW_R(s;v)/ds>0 for all v∈[0.15,0.34], s∈[0,1].**
(B) **dW_I(s;v)/ds>0 for v∈[0.18459,0.34], all s** (it need NOT hold for the very lowest v; avoid overclaim).
(C) P_R(1;v)>P_I(s;v) for v∈[0.15,0.278975] and all s; for v∈(0.278975,β) use P_I'(s)>0 and the exact sign P_R(1)>P_I(1).
(D) W_I(1;v)>W_R(s;v) for v∈[0.184596,0.34] and all s; for v∈[α,0.184596) use W_R'(s)>0 and exact W_I(1)≥W_R(1).
(E) For v∈[0.15,0.184595], P_R(1)>P_I(s) and W_R(1)>W_I(s) for all s. For v∈(0.184595,α), W_I'(s)>0 and W_R(1)>W_I(1) by root ordering, hence W_R(1)>W_I(s).
(F) For v∈[0.278976,0.34], P_I(1)>P_R(s), P_I(1)>O_R(s), W_I(1)>W_R(s), W_I(1)>U_R(s), all s; for v∈(β,0.278976), the exact P_I(1)>P_R(1) and dP_R/ds>0 imply P_I(1)>P_R(s), with other comparisons directly certified on [0.278975,0.34].
(G) On [0.278975,0.34], dP_R/ds>0 and dP_I/ds>0 for all s. Thus at β P_I(1)=P_R(1) are tied, while no lower-depth IS can strictly gain over RS(1), nor a lower-depth RS strictly gain over IS(1).
(H) Signing IR P_R(1)>P_N, W_R(1)>W_N and P_I(1)>P_N,W_I(1)>W_N certified on their relevant v intervals. For governments-only nested type, W_I(1)>outside RS govt U_R(s) is certified at v≥0.18459. All comparison/corner requirements are checked by exact positive Bernstein certificates.

Therefore for v<α, ANY IS(s) is blocked by four profitable G/F members switching to RS(1). For α≤v≤β, RS(1) is protected against alternate RS by increasing W_R and IS switching by P_R(1)≥all P_I(s); IS(1) is protected against IS depth changes by increasing W_I and RS switching by W_I(1)≥all W_R(s). For v>β, all RS(s) are blocked by six signers agreeing to IS(1), including the original RS outsider government/firm actors, each strictly gaining. A deviating signer can refuse an existing contract to NS only if personally strictly better there; IR rules out such deviations.

## 3. Parameter sensitivity and scientific limitations
This resolves actual STANDARD TYPE switches for every real v in one closed interval with OTHER economics primitives held at rational benchmark values. It does NOT solve the entire eight-dimensional θ partition, general country asymmetry, active-set Cournot with zero quantities, monetary transfers, different mechanism of government recognition, or mixed Nash equilibria.

The formerly certified interval [0.19,0.23] is a **strict subset** of the true coexistence region here, not a separate finding. The two root thresholds are the actual type-switching thresholds WITHIN THE FIXED-OTHER-PRIMITIVES theorem domain because all alternative depths are globally certified; previous PR #10 had them only as *depth-one payoff ranking candidates* before this proof.

The two-key public/private conflict is substantive as an allocation of RIGHTS, but prior multi-agent veto/Pareto and standards coalition games may absorb the mechanism. Prior Stage6 NO-GO on smaller two-point results remains an accurate historical verdict. A **NEW Stage4A clean-room proof audit and Stage6 exact parent-theorem comparison** are mandatory. Do not claim publication-level contribution or auto-merge stacked Draft PR.
