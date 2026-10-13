# Stage 4 — Pure SPNE vs strong-Nash refinement of the FIRST-STAGE announcement game
2026-10-14 JST | Parent Draft PR #17 (SPNE-first). ORIGINAL model: one endogenous commonality/standardization rate s, and exogenous network strength v. NOT the optional two-choice extension.

## 1. Precise two-stage equilibrium concepts
Six players G1,F1,G2,F2,G3,F3. Stage 1: each simultaneously announces SQ, RS(named pair,s), or IS(s), s∈(0,1]; contract RS needs 4 exact member government/firm signatures, IS needs all 6, otherwise NS. Stage 2: three Cournot producers compete in each of three nationally segmented differentiated-good markets after the observed outcome, including zero-production KKT cases for the outsider under RS. Stage-2 Cournot equilibrium is unique in the symmetric SPD source-demand parameter domain.

**PURE SPNE** is the normal-form Nash profile of Stage-1 messages, together with unique Stage-2 Cournot continuation at EVERY realized and off-path contract history. Thus the pure contract OUTCOME set is exactly NS (always), RS(pair,s) iff P_R(s)>=P_N and W_R(s)>=W_N, and IS(s) iff P_I(s)>=P_N and W_I(s)>=W_N.

**REDUCED-STAGE-1 STRONG-NASH REFINEMENT**: after inserting each Cournot continuation payoff, impose strong Nash (all actual message-changing deviators must STRICTLY gain to block) in the Stage-1 exact-announcement game only. This is a refinement of pure SPNE realized outcomes because strong Nash implies Nash of the SAME reduced announcement game; it is NOT the strong Nash equilibrium concept for the entire two-stage extensive game or each Cournot subgame.

**CRITICAL second-stage collusion audit:** in any interior Cournot country market with product substitution M_ij=gamma>0, firms i,j can both lower output by epsilon>0 at the Nash point, leaving all other firms' outputs fixed. Each firm i gains exactly gamma*q_i*epsilon-(m+gamma)*epsilon², positive for 0<epsilon<gamma*q_i/(m+gamma); j likewise. Thus the Stage-2 Cournot Nash GENERICALLY is not a strong Nash quantity profile. One CANNOT identify reduced-stage-1 strong Nash with an overall strong subgame-perfect equilibrium. A sequential coalition-proof or renegotiation-consistent concept would require separately specified coalition permissions and deviation credibility; see Bernheim, Peleg, Whinston (1987), Coalition-Proof Nash Equilibria I. Concepts, JET; Bernheim & Whinston (1987), II. Applications (including Cournot). Economic justification of binding Stage-2 noncollusion and Stage-1 joint contract renegotiation MUST be stated openly in a paper.

## 2. FULL 5D parameter general theorem: SPNE vs first-stage strong outcome sets
Set m=1-v>0, A=a-c0>0 and five composite EXOGENOUS primitive coordinates mu=(G,Lambda,Delta,rho,F)=(gamma0/m,(kappa-v)/m,eta/m,h/A,m*f/A²). Endogenous s∈(0,1] and quantities only. The realized normal-form continuation payoff functions P_R(s),W_R(s),O_R(s),U_R(s),P_I(s),W_I(s),P_N,W_N are full Cournot/KKT rational functions, with the common actual member fee F s². All statements below apply to every parameter vector in the admissible SPD/substitutes region, with applicable outsider-corner branch rather than extrapolating interior outputs.

For X in {R,I}, define SPNE depth set
 S_X(mu,F)={s∈(0,1]:P_X(s)>=P_N, W_X(s)>=W_N}.
Equivalently, S_X={s:F<=T_X(s;mu)}, where
 T_X(s;mu)=min{[P_X^0(s)-P_N]/s²,[W_X^0(s)-W_N]/s²}.
Full SPNE realized outcomes are {NS} union the bilateral RS contracts for s∈S_R union IS(s) for s∈S_I.

Define strict-welfare Pareto blocker:
 B_X(p,w)=1 iff exists t∈(0,1] with P_X(t)>p AND W_X(t)>w.
This uses the TRUE Cournot payoff branch at every t. The reduced-stage-1 strong outcome sets are:
 E_R^strong = {s∈S_R: not B_R(P_R(s),W_R(s)), not B_I(max[P_R(s),O_R(s)],max[W_R(s),U_R(s)])}.
 E_I^strong = {s∈S_I: not B_I(P_I(s),W_I(s)), not B_R(P_I(s),W_I(s))}.
The REGIONAL predicate with max is about a strong equilibrium profile EXISTS: take both otherwise nonessential outsiders' original messages as SQ, so all six must change to activate IS. For stability against ALL original outsider preannouncements, replace max threshold with P_R(s),W_R(s); a preannounced IS contract requires no outsider message change, so outsiders need not personally improve. These are exhaustive possible standard changes in a three-country one-formed-contract game under simultaneous perfect exact signatures.

For NS: all SQ is always SPNE. It is a reduced-stage-1 strong-Nash outcome iff neither any RS(t) nor any IS(t) strictly improves the requisite signers over NS. Equivalently F>=Phi(mu) where
 Phi(mu)=max_X sup_{0<s<=1} min{(P_X^0(s)-P_N)/s²,(W_X^0(s)-W_N)/s²}.
When Phi=+infinity, NS survives as SPNE but NEVER survives reduced-stage-1 strong Nash for any finite F.

### Theorem: OPEN continuum of SPNE depths eliminated by reduced-stage-1 strong Nash
Write K_R=Delta(1-G)+2rho(1+G)-Lambda. Exact symbolic source:
 P_R^0'(0)=3*K_R/[2(2-G)(1+G)^3].
 CS_R'(0)=[G*K_R+G*Delta*(1+G)+2rho*(1+G)^2]/[4*(1+G)^3].
For 0<=Delta<=G<1, rho>=0 and K_R>0, these imply P_R'(0)>0 and W_R'(0)>0 (fee derivative at zero is 0). Hence there exists epsilon>0 such that BOTH P_R,W_R are strictly increasing and exceed NS on (0,epsilon]. Every s∈(0,epsilon/2) is a PURE SPNE realized RS contract, but a coalitional agreement of its incumbent 4 signers to any slightly larger depth in (s,epsilon] improves BOTH resident firms and governments; hence **NO such s survives reduced-stage-1 strong Nash**. Likewise NS is SPNE but NOT strong since some positive shallow RS Pareto-improves upon NS.

Thus the substantive difference between SPNE and its reduced-stage-1 strong-Nash refinement holds GENERICALLY on an OPEN, nonempty multidimensional parameter domain; it is not an isolated numerical case. A unique standard-depth prediction is not attainable by ordinary SPNE from this exact-unanimity protocol alone.

### Pareto-compromise depth interval if within-type P_X,W_X strictly concave
If P_X and W_X strictly concave over [0,1] (for given mu,F) and attain unique best depths s_{FX},s_{GX}, then
  B_X(P_X(s),W_X(s))=0 if and ONLY IF
  s in [min(s_FX,s_GX), max(s_FX,s_GX)] intersect (0,1].
This is a transparent first-stage reduced-game Pareto-efficient compromise band; the CROSS-STANDARD blocker above may further remove its members. Without strict concavity, use the actual global B_X, never extend this statement.

## 3. EXACT benchmark comparison of ENTIRE SPNE and efficient-depth bands
Same original market primitives as prior partial-standard paper, normalized
 (G,Lambda,Delta,rho,F)=(5/16,-1/16,3/32,1/4,2/5).
RS outsiders stay positive at every s, all demand matrices SPD. Sturm exact rational real-root isolation proves:
 P_R(s)>=P_N iff 0<s<=sigma_R, where sigma_R is the UNIQUE positive root in (0,1) of rational numerator of P_R(s)-P_N and sigma_R≈0.908926438726.
 W_R(s)>W_N for EVERY s>0.
 P_I(s)>=P_N iff 0<s<=sigma_I, where sigma_I is the UNIQUE positive root in (0,1) of rational numerator of P_I(s)-P_N and sigma_I≈0.749575487831.
 W_I(s)>W_N for EVERY s>0.
So S_R^SPNE=(0,sigma_R], S_I^SPNE=(0,sigma_I]; plus NS ALWAYS. The existence of these entire intervals is exact, not a depth grid.

Global strict concavity P_X''<0,W_X''<0 (all four) and exact Sturm unique stationary roots:
 s_FR≈0.453383394613, s_GR≈0.676785014137;
 s_FI≈0.373823228346, s_GI≈0.693694987715.
Thus regionally Pareto-undominated within-standard depths are [s_FR,s_GR], internationally [s_FI,s_GI]. Cross-type coordination further restricts the reduced-stage-1 strong sets.

Examples verified via FULL strategy-message unilateral enumeration AND independent continuous-depth strong blocker code:
 * RS(0.10): PURE SPNE YES; reduced-stage-1 strong NO (jointly dominated by RS(0.20)).
 * RS(0.60): PURE SPNE YES; reduced-stage-1 strong YES, robust against outsider preannouncements.
 * RS(0.85): PURE SPNE YES; reduced-stage-1 strong NO (past both firms' and governments' ideal depths).
 * IS(0.10): PURE SPNE YES; reduced-stage-1 strong NO.
 * IS(0.65): PURE SPNE YES; reduced-stage-1 strong YES.
 * IS(0.72): PURE SPNE YES; reduced-stage-1 strong NO (past both actors' ideal depths).
 * NS: PURE SPNE ALWAYS; reduced-stage-1 strong NO in this benchmark.
This is a certified nontrivial strict nesting, not a relabeling of two equivalent solution concepts. Both RS and IS standard TYPES remain in the reduced-stage-1 strong set, but most pure SPNE depths do not necessarily survive.

## 4. Scientific implications, research routing
The first manuscript propositions MUST be (i) Cournot continuation including genuine KKT corner, (ii) pure SPNE outcome set and all-SQ coordination problem, (iii) exact reduced-stage-1 strong-Nash refinement and coalition deviation constraints, followed by (iv) public/private incentive divergence and endogenous-depth coexistence (from parent PR #16), (v) comparative static thresholds and welfare. Consider adopting an explicit alternative sequential/staged negotiation implementation or coalition-proof Nash if Stage-1 reduced strong Nash appears an arbitrary selection assumption; DO NOT conflate with overall strong SPNE.

Audit requirements: independent adversarial Stage4A for strong-outcome characterization and for the inability of Stage-2 Cournot to be strong Nash; interpretation of financial rights and ability to negotiate at Stage 1 but not collude quantities at Stage 2; exact source accounting; Stage6 theorem-by-theorem absorption vs Bernheim-Peleg-Whinston 1987, Hart-Kurz, Economides-Skrzypacz 2003, Bourreau-Doğan-Manant 2016 and Ghosh-Morita 2012. No novelty or manuscript completion claimed. Keep Draft PR unmerged.
