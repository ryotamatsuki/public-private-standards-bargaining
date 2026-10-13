# Stage 4 — Endogenous standard-depth, public–private conflict and fee thresholds
**2026-10-14 JST | Theorem-candidate track from Draft PR #14 | NEW 1D s problem, NOT 2-control PR #11**
This report delivers a general five-parameter theorem and one exact continuum of fixed-cost results; it does NOT assert a complete five-dimensional phase partition, Stage4A PASS, economic originality, or journal submission readiness.

## 1. What remains endogenous and what does not
Endogenous: standard type C∈{NS,RS,IS}, its **single** commonality/technical standardization depth s∈(0,1], and Stage-2 differentiated Cournot outputs q_i in each of three segmented national markets. Exogenous: own-network and interoperability coefficient v, baseline substitutability γ0, inside/outside differentiation response κ,η, marginal cost saving h, one-time quadratic fee f, demand intercept a and base marginal cost c0. Government G_i payoff = home-market consumer surplus + resident firm's total three-market worldwide profit net ONE fixed integration cost. Each named RS requires both G/F signatures of two members (4); named IS requires all 6. All proposals simultaneous and exact-depth matched. Outsiders may preannounce IS; robust RS result checks every such message-profile state. No transfers, government subsidy or sequential recognition.
Source demand M has own diagonal m=1−v, NS off diagonal γ0, RS member off diagonal b(s)=γ0+(κ−v)s, RS outsider cross d(s)=γ0−ηs, and IS all pair off-diagonal b(s). Fixed fee per signed firm f s² and marginal cost c0−h s.

## 2. Exact reduction from six to FIVE essential parameters
Let A=a−c0>0, m=1−v>0, and define:
  G=γ0/m, Lambda=(κ−v)/m, Delta=η/m, rho=h/A, F=m*f/A².
Rescale physical Cournot quantity by A/m and every private/government payoff by A²/m; positive uniform scaling leaves every strict/weak comparison and thus the complete strong-Nash contract game unchanged.

Normalized demand has diagonal 1, member cross b(s)=G+Lambda s, outsider cross d(s)=G−Delta s; real standard fee F s² per member. Normalized market q:
  q_N=1/[2(1+G)];
  x_R(s)=[2(1+rho*s)−d(s)]/[2(2+b(s))−2d(s)²];
  y_R(s)=[2+b(s)−2d(s)(1+rho*s)]/[2(2+b(s))−2d(s)²],
  q_I(s)=[1+rho*s]/[2(1+b(s))].
For RS outsider Cournot corners use the exact piecewise source in PR #14; present propositions restrict to a regular open domain where all three firms remain active at every depth and each demand M(s) is SPD. Conditions and real boundary KKT analysis of PR #14 remain part of full model.

Let \hat P_R(s)=3 x_R(s)², \hat P_I(s)=3 q_I(s)² denote private worldwide OPERATING profits without real fixed integration expense; \hat W_R(s)=\hat P_R(s)+CS_R(s) and \hat W_I(s)=\hat P_I(s)+CS_I(s) denote member national welfare without this expense. All true member outcomes P_X(s)=\hat P_X(s)−F s², W_X(s)=\hat W_X(s)−F s². NS payoffs P_N,W_N have no fee. Critically, RS and IS both charge the identical per-member fee at a matched depth.

## 3. Proposition A — same-depth conflict is entirely independent of setup fee
For every s and all five admissible parameters:
 P_R(s)−P_I(s) = \hat P_R(s)−\hat P_I(s),
 W_I(s)−W_R(s) = \hat W_I(s)−\hat W_R(s).
In particular, the **same-full-depth public–private conflict wedge** is defined by
  D_P(G,Lambda,Delta,rho) := \hat P_R(1)−\hat P_I(1) >0,
  D_W(G,Lambda,Delta,rho) := \hat W_I(1)−\hat W_R(1) >0.
This is an OPEN four-dimensional conflict set in the demand/technology parameter projection; the sign is independent of F. **It does NOT alone imply any jointly stable contract**, since every agent can compare all t≠s, and fee F then does not cancel. Neither old v-only switching root is the complete multidimensional outcome boundary.

## 4. Proposition B — rigorous generic endogenous-depth coexistence certificate
Fix any admissible (G,Lambda,Delta,rho) in the all-interior SPD domain. Define the cost-free payoff curves as above. Define up to six fee ceilings (extended real infima), all over the indicated CONTINUOUS depth interval, not mesh points:
  f_RI = inf_{0≤t<1} [\hat P_R(1)−\hat P_I(t)]/(1−t²)
  f_IR = inf_{0≤t<1} [\hat W_I(1)−\hat W_R(t)]/(1−t²)
  f_GR = inf_{0<t≤1} \hat W_R'(t)/(2t)
  f_GI = inf_{0<t≤1} \hat W_I'(t)/(2t)
  f_IR_R = \hat P_R(1)−P_N;
  f_IR_I = \hat P_I(1)−P_N;
  f_GOV_R = \hat W_R(1)−W_N;
  f_GOV_I = \hat W_I(1)−W_N.
Let f_coex be the MINIMUM of all eight ceilings. [All notation f refers to NORMALIZED fee F, not physical f].

**THEOREM:** If f_coex>0 and 0<F<f_coex, then full-depth RS(C,1) (for each bilateral identity C) AND full-depth IS(1) are jointly strong-Nash stable, with RS robust against ANY outsiders' irrelevant original contract messages. Proof:
- For all t<1, P_R(1)−P_I(t)=\hat P_R(1)−\hat P_I(t)−F(1−t²)>0 from f_RI; at t=1 use D_P>0, which is implied by f_RI>0.
- W_I(1)−W_R(t)>0 analogously from f_IR; at t=1 f_IR>0 implies D_W>0.
- W_R'(t),W_I'(t)>0 for t>0 from f_GR,f_GI. Hence no profitable renegotiation to another RS depth or another IS depth, because member governments would lose; the other-type switch is vetoed by incumbent firms (RS→IS) or governments (IS→RS).
- All four member IR inequalities hold from remaining ceilings.
The stronger **uniform** RS stability explicitly protects against preannounced IS messages by outsiders, so the lemma is valid independently of that predecessor audit concern.
This is an ANALYTIC sufficient theorem, not a necessary-and-sufficient entire coexistence classification. Lower-depth RS and IS contracts may remain strong even when a ceiling fails; empty sets and inf=−∞ should be interpreted as the theorem not applicable.

**Comparative statics of the sufficient region:** For fixed four real-technology primitives, membership of (0,f_coex) is **downward closed in F**. These ceilings are endogenously optimized over all depths and depend on G,Lambda,Delta,rho; they are NONCONSTANT threshold hypersurfaces, NOT exogenous numerical brackets. Where the minimizing t is uniquely interior and regular, the envelope theorem gives the parameter derivative of each ceiling, e.g. ∂f_RI/∂Delta = [∂Delta\hat P_R(1)−∂Delta\hat P_I(t*)]/(1−t*²). Nondifferentiable intersections require one-sided comparative statics or set-valued calculus.

## 5. Proposition C — a necessary local upper-cost threshold for full-depth RS
At any fixed four-dimensional market/technology vector, define
  f_R_end = max{ \hat P_R'(1), \hat W_R'(1) }/2.
If F>f_R_end, then BOTH member firm and government have P_R'(1)<0 and W_R'(1)<0, so a small change to s=1−epsilon STRICTLY improves each; the original 4 matched actors can jointly deviate to that lower-depth RS agreement. Thus RS(C,1) is NOT strong-Nash stable, irrespective of other RS/IS alternatives. (Similarly IS(1) is unstable if F>max{ \hat P_I'(1), \hat W_I'(1) }/2.)
This is a **necessary full-depth stability condition**, NOT a threshold at which all RS contracts disappear.

**Key economic identification:** Full-depth RS/IS PRIVATE/GOVT RANKINGS remain invariant to F at the same s, but above f_R_end a previously accepted full-depth RS contract is destabilized by endogenous redesign to s<1. This cannot appear in a model where s is fixed to 1 or where only full-depth payoffs are compared. This offers an actual mechanism-level contribution candidate, though generic concavity/veto theories threaten external novelty.

## 6. Exact certificate and cost comparative statics for a NONTRIVIAL baseline
Original baseline a=1,c0=h=f=1/5,γ0=1/4,κ=3/20,η=3/40,v=1/5 maps to:
  (G,Lambda,Delta,rho,F)=(5/16,−1/16,3/32,1/4,1/4).
The reproducible script \`code/verify_endogenous_depth_conflict_theorem.py\` proves symbolically that the entire normalized Cournot production/profit expressions match original source and that F cancels in same-depth comparisons. It checks the entire positive-depth interval [0,1] using EXACT RATIONAL Bernstein coefficient inequalities:
  P_R(1)>P_I(t) ∀t;
  W_I(1)>W_R(t) ∀t;
  W'_R(t)>0 and W'_I(t)>0 ∀t;
  private/government NS participation for both standards.
Hence both full-depth RS and IS are ROBUSTLY strong Nash at F=1/4. Since larger F always WEAKENS all eight inequalities monotonically, the result extends immediately to the entire POSITIVE normalized cost interval 0<F≤1/4, without arbitrary v-gridding or recomputation.

Moreover, at the SAME four-market coordinates,
  \hat W_R'(1)/2 = 310713952/1042430125 ≈0.29806693470221807,
  \hat P_R'(1)/2 = 226554624/1042430125 ≈0.21733315122680285,
  \hat W_I'(1)/2 = 39/128 =0.3046875.
Thus **EVERY** F>310713952/1042430125 makes the full-depth RS(1) unstable to lowering its own standard depth, even though D_P>0 and D_W>0 are UNCHANGED with F. Do not say *all RS* instability, do not presume full-depth IS remains stable for any F, and do not claim that the true coexistence-exit fee equals this local bound. The family F∈(0,1/4] is a certified positive-length slice, not an exact f_coex numeric evaluation. At F between 1/4 and 0.298... the theorem may hold but this exact witness proof does not certify every possible F.

Under the original cost variation with A=4/5 and m=4/5, F=5f/4; so physical real fixed-cost f threshold for full-depth RS local instability is (4/5)*(310713952/1042430125), keeping all original other primitives fixed.

## 7. Novelty re-kill and research next targets
The closest direct inherited results in Economides–Skrzypacz (2003) already compare network standard coalitions, Ghosh–Morita (2012) already distinguish insider/outsider product distinctiveness, and Bourreau–Doğan–Manant (2016) explicitly endogenize size and scope of RJV product development. These sources must be compared at THEOREM LEVEL. Hart–Kurz/Pareto multidimensional bargaining literature could immediately absorb parts of the veto/coexistence logic. The new candidate is NOT the generic statement 'v stronger → IS', nor a bare two-player veto: it is the fee-invariant SAME-DEPTH ranking vs fee-dependent ENDOGENOUS-DEPTH joint stability, the regular multidimensional parameter hypersurface f_coex, and the government/private threshold slope separation.

Before publication: (i) independent Stage4A verify every generic inequality, payoff, coalition-message edge case and cost normalization; (ii) tighten generic sufficient ceilings toward necessary-and-sufficient coexistence-exit conditions by solving Pareto frontiers at arbitrary depths, including RS outsider corner regimes; (iii) derive sign of derivative of the cost ceiling w.r.t. network and differentiation parameters under specific sufficient regularity assumptions, distinguish own-network effects from cross compatibility; (iv) Stage6 novelty absorption. Do not merge branch on mathematical success alone.
