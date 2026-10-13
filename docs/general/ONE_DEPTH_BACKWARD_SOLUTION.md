# Stage 4 — General backward-induction strong-Nash outcome solution
Date 2026-10-14 JST | SOURCE MODEL: ORIGINAL ONE DEPTH, not optional two-control PR #11.
NEW branch based on PR #10. This is an EXACT analytical **implicit equilibrium correspondence**, NOT a fully enumerated eight-dimensional parameter-region decomposition, novelty pass, or Stage4A independent certificate.

## 1. Entire two-stage game and regular domain
Parameters theta=(a,c0,h,f,gamma0,kappa,eta,v) EXOGENOUS. Set A=a−c0>0, m=1−v>0; s∈(0,1] is the unique NEGOTIATED standard-design/commonality intensity. When firms 1 and 2 join:
 b(s)=gamma0+(kappa−v)s, d(s)=gamma0−eta*s.
M_RS has diagonal m; member-member cross b, outsider cross d; M_IS diagonal m all cross b; M_NS diagonal m all cross gamma0. The coefficient v influences standalone own-network value and linked network benefit in this existing source game. Member marginal cost c0−h*s with h≥0; fixed resource outlay f*s² with f>0 once per member. No transfer, royalty, sequential signer stage or strategic network coefficient. Three firms supply every one of the three national segmented markets. All countries are symmetric. Six players (G_i,F_i) each announce SQ or an EXACT named RS(pair,s)/IS(s) simultaneously. The four necessary G/F member signatures activate RS; all six activate IS; otherwise NS. RS outsider's off-contract message can preannounce another standard without affecting current RS. Government W_i=consumer surplus in country i + total worldwide net firm profit of its resident firm. Stage 2 Cournot is chosen after the Stage 1 contract is determined.

Interior regular domain Theta_int explicitly requires for ALL s∈[0,1]:
 NS demand SPD m−gamma0>0 and m+2gamma0>0.
 RS SPD m−b>0 and m(m+b)−2d²>0.
 IS SPD m−b>0 and m+2b>0.
 All market quantities strictly positive.
 Outside this domain the interior formulas cannot be used: KKT active-set branches may change.

## 2. Backward Cournot solution (symbolically general in theta)
Define Delta(s)=2m(2m+b)−2d², A=a−c0.
 NS per-firm-per-country output q_N=A/[2(m+gamma0)].
 RS member output x=[2m(A+h*s)−d*A]/Delta; RS outsider output y=[(2m+b)*A−2d(A+h*s)]/Delta.
 IS output q_I=(A+h*s)/[2(m+b)].
These solve (M+m*I)*q = a*1−marginal_cost exactly; with SPD and interior outputs the Cournot equilibrium in every market is unique (individual quantity SOC −2m<0).

Every country's local consumer surplus:
 CS_R=(m+b)x²+2d*x*y+(m/2)*y²,
 CS_I=(3/2)(m+2b)q_I²,
 CS_N=(3/2)(m+2gamma0)q_N².
Worldwide member firm profits P_R(s)=3m*x²−f*s², P_I(s)=3m*q_I²−f*s², outsider O_R(s)=3m*y², NS P_N=3m*q_N².
National welfare of member W_R=P_R+CS_R; outsider U_R=O_R+CS_R; IS W_I=P_I+CS_I; NS W_N=P_N+CS_N. Resource/integration cost f*s² is subtracted ONCE, not once per destination. All are rational functions in s and theta with positive denominators in Theta_int.

## 3. MAIN THEOREM — Full Stage-1 STRONG-NASH CONTRACT-OUTCOME correspondence
For destination standard type Z∈{R,I}, and thresholds (p,w), let
  B_Z(p,w)=1  <=>  EXISTS t∈(0,1]: [P_Z(t)>p AND W_Z(t)>w].
B_Z=0 otherwise. This is a GLOBAL all-depth predicate (neither FOC nor local optimum).
Let E(theta) be the set of realized contracts which are supported by AT LEAST ONE strong-Nash **full message profile** in the six-agent simultaneous one-shot game.

(A) NS in E iff B_R(P_N,W_N)=0 and B_I(P_N,W_N)=0.

(B) RS(pair,s) in E iff
  (i) P_R(s)>=P_N AND W_R(s)>=W_N [4 participating signers' individual rationality];
  (ii) B_R(P_R(s),W_R(s))=0 [no same-pair profitable depth renegotiation];
  (iii) B_I(max[P_R(s),O_R(s)],max[W_R(s),U_R(s)])=0
       [no IS switch making ALL SIX original necessary deviators STRICTLY better].
This is NECESSARY AND SUFFICIENT for existence of a strong-Nash matching profile with both nonmember agents originally announcing SQ.

(C) IS(s) in E iff
  (i) P_I(s)>=P_N AND W_I(s)>=W_N;
  (ii) B_I(P_I(s),W_I(s))=0;
  (iii) B_R(P_I(s),W_I(s))=0.
IS has no nonmember message freedom, so this is also the complete condition for its unique fully matching message form.

**Proof of exhaustive deviation partition:**
A coalition changing messages can produce only NS, one of the 3 RS pair contracts, or IS; these exhaust possible continuation outcomes. Under NS all-SQ, any nontrivial formed RS/IS requires all necessary signers to change and strictly benefit. If any contract strictly benefits all its signers, it blocks every unmatched NS profile, since some signer must still change and all who must change gain. Under a matched RS, a current essential signer alone can break to NS; no such strict deviation exactly when IR holds. Any other RS contains one old-country pair of G/F essential players; if both improve by changing pair/depth, same-pair RS-depth renegotiation improves BOTH symmetric old member countries, so a profitable other-pair deviation implies (ii). Conversely a profitable same-pair amendment necessarily uses four improved old G/F signers. To switch from RS to IS when both outsiders originally say SQ, all six actors must change; strict improvement for BOTH the old member role and the outsider role is required, giving (iii). Preannounced alternatives can only omit a necessary member of the prospective deviating coalition, never manufacture a profitable deviation when outsiders are reset to SQ. Thus the SQ outsider profile is the most favorable original supporter of RS. Under IS, every player originally signs the same contract, so any IS amendment requires all six agents to change and any RS requires precisely its four new signers, both improving P_R,W_R over current P_I,W_I. Contract refusal to NS is captured by IR.

**CRITICAL EQUILIBRIUM CONCEPT DISTINCTION:**
- Existence of a strong-Nash RS outcome is described by B(iii) using the MAX of current insider/outsider payoffs.
- RS matched contracts robustly strong under EVERY POSSIBLE original outsider announcement require the STRICTLY STRONGER condition B_I(P_R(s),W_R(s))=0, together with IR and condition (ii). This is because outsiders might have preannounced a specific IS contract and need not themselves gain or deviate when four incumbents switch. Previous Stage4A identified exact rational counterexample. Do not claim uniform outcome stability from merely existential outcome stability.
- All-SQ ordinary Nash always exists, possibly strongly blocked. The strong-Nash contract outcome E(theta) may be empty or multiple. This theorem is not a unique normal-form Nash claim and not coalition-proof/SPE of an unmodeled sequential negotiation.

## 4. FINITE EXACT decision procedure for a given rational theta and candidate contract depth
The payoff functions are rational with strictly positive denominators on Theta_int. Delta_R is quadratic in t; common denominators can be taken as Delta_R². Member P_R,W_R numerators have degree at most SIX. IS's H=m+gamma0+(kappa−v)t is linear; P_I,W_I denominators H² and numerator degree at most FOUR. Thus B_Z(p,w) can be computed by finding all real roots of TWO polynomial numerators [P_Z(t)−p] and [W_Z(t)−w] on (0,1). Isolate the roots of their PRODUCT with a Sturm root-isolation method, partition the interval into cells where both signs are constant, and evaluate one rational midpoint per cell plus endpoint t=1. Both signs >0 on any cell iff a strict blocking standard exists; equality roots cannot count as simultaneous STRICT gains. No unexamined standard depth remains.
Executable code: code/verify_backward_general.py implements rational-primitive continuation, WHOLE INTERVAL SPD/interiority checking, symbolic generic IS FOC identity, rational global all-depth blocker, and the exact contract-classifier strong_contract(theta,kind,s,uniform=False/True). Tested v=1/10,1/5,3/10 for NS/RS/IS benchmark candidates. Unlike prior gridded numerical searches, this evaluator returns exact binary certification for any rational admissible theta and rational candidate s.
For real/algebraic variable theta the same formulas are semialgebraic quantified statements; cylindrical algebraic decomposition or real quantifier elimination can theoretically partition the valid theta domain. FULL explicit eight-parameter case classification and closed-form unique switch surfaces are NOT claimed or computed.

## 5. NEW GENERAL (not witness-only) IS private-entry impossibility theorem
Let H(s)=m+gamma0+(kappa−v)s >0, K=h(m+gamma0)−A(kappa−v). For IS:
 q_I(s)=(A+h*s)/(2H), dq_I/ds=K/(2H²) (same SIGN at every valid s).
 P_I'(s)=3m(A+h*s)K/(2H³)−2f*s.
 Private firm's interior first-order condition reduces exactly to quartic:
      4f*s*H(s)^3 = 3m(A+h*s)K.
 With A>0,m>0,h>=0,f>0,H>0 and K<=0, firm profit P_I(s) is STRICTLY BELOW P_N for EVERY s>0, since q_I is nonincreasing while a positive fixed integration cost is incurred. Hence **IS can never be a strong-Nash signed outcome in the FULL JOINT-RIGHTS GAME under K<=0**, irrespective of government preference and all other coalitions. This is a parameter-wide exclusion condition (not a new economics novelty claim). When K>0, P_I'(0)>0 and tiny standardization is privately feasible, but no global IS stability follows without the government/RS-deviation tests.
Example with A=4/5, h=1/20, gamma0=1/4 and kappa=1/5 gives K=(3/4)(v−13/100), so under otherwise admissible SPD/interior conditions any v≤13/100 categorically excludes privately signed IS. At v>13/100, it removes this particular private feasibility obstruction without implying IS equilibrium. This is an EXACT parameter-space threshold, not inferred from two sample points. The verification script additionally checks RS/IS/NS global real-cost and consumer-surplus world-accounting identities symbolically.

For each type X=RS,IS, if a UNIQUE INTERIOR strict private optimum s_F,X(theta) exists, then ds_F,X/dv=−P_X,sv/P_X,ss. Its sign is not universally positive absent curvature and cross-partial restrictions. At boundaries use KKT and regime transitions; strong Nash may be a set, with multiple branches and discontinuous jumps. The network parameter v is EXOGENOUS but affects own network m=1−v as well as compatible cross links, as in frozen source; changing only cross compatibility would need separate reentry.

## 6. Stage routing and limitations
Stage4 construction: exact stage-2 solution, exact ALL-parametric-depth first-stage strong-outcome correspondence, exact finite rational decision algorithm, and analytic necessary private IS condition; GO TO INDEPENDENT STAGE4A MATH ATTACK, **NOT** automatically novelty GO. Old Stage4A passed narrower witnesses; full current theorem has not been independently audited. User-requested original one-control model is retained, while PR #11 optional two-choice model remains separate. Stage6 NO-GO applied to then-known findings only; a NEW Stage6 direct parent theorem test is needed after Stage4A.
Known exclusions: corners/zero-output Cournot KKT beyond Theta_int; country asymmetries, more than 3 countries, collusive or dynamically renegotiated standards, private IP royalties, mixed equilibria, all-message-profile enumeration and a fully explicit theta cell decomposition. NO conclusion on publication readiness or independent human referee.
