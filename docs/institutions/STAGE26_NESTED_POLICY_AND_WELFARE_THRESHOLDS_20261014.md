# Stage 26 — Nested veto, ex-post efficiency and ex-ante efficiency thresholds

Date: 2026-10-14 JST. Exact proof project stacked on Stage25 Draft PR #53, with all older PRs unmerged. No manuscript rewritten.

## Why this is the next economic result

Stage19–25 demonstrated that majority plus universal public agenda eliminates every privately retained RS **pure-SPE terminal outcome** of the reduced OPEN/N 3-country game in a certified technological neighborhood. That by itself does NOT prove majority is normatively superior. Stage11 already proved a **prospective ex-ante** private-RS-versus-public-IS social-welfare reversal; Stage15 separately introduced an **ex-post** mandate-after-RS-investment welfare cutoff. This Stage26 theorem unifies **both** cutoffs with the outsider's political veto, derives the EXACT nested threshold ordering, formally separates alternative policy dates, and gives rational isolations for the two distinct eta transition values at K=.55, plus a formal constitutional policy counterfactual.

Do NOT describe all component results as first discovered at Stage26. The contribution **relative to our own prior stages** is a single synthetic trichotomy/theorem + verified crossing-order/parameter witness, not initial discovery of either individual welfare crossover.

## Assumptions and notation

Only the Stage15/19 minimum three-firm independent choice N or OPEN O(c_i,a_i), full real 0<=a_i<=c_i<=1, legally accessible public O(1,0), no transfers, government voting/proposal configurations, and Stage11 baseline technology (v,gamma0,kappa,rho,phi)=(.01,.14,.02,.32,.14). eta∈[.10,.14], K∈[.54,.56]. All firms that conform to public O(1,0) incur proper sunk upfront and incremental missing-capital cost. Every country's welfare = its firm's net profit plus consumer surplus from the three-firm Cournot game in its local market. Nation-specific market shares are symmetric across markets.

At the observed privately optimal bilaterally regional cohort O(1,a_R*(eta)),O(1,a_R*(eta)),N, the strictly positive private optimizer a_R*(eta) is the unique global solution of f_a=0, certified by Stage11's all-real concavity and comparative-static proofs, and 1/4<a*<61/100.

Write G_I for national public gross welfare BEFORE new initial fixed-fee charges; pi_O for outsider's gross market profit under RS; C_R for each national consumer surplus at RS; f_R for matched private founder's Cournot market profit net of **existing physical phi(1+a²)/2 but before K**. Define the member government ex-post M-L gain
\[
B(\eta)=G_I-\frac{\phi}{2}(a_R^*)^2-f_R-C_R>0.
\]
Define three **K cutoff curves** (all evaluated at a_R*(eta)):
\[
\begin{aligned}
K_V(\eta)&=G_I-\pi_O-C_R
&&\text{outsider is weakly willing to approve M iff }K\le K_V;\\
K_E(\eta)&=K_V(\eta)+2B(\eta)
&&\text{after RS sunk, world M-L gain }=K_E-K;\\
K_W(\eta)&=3G_I-\bigl[2f_R+\pi_O+3C_R\bigr]
&&\text{before investment, world IS(NNN/M)-RS(OON/L) gain }=K_W-K.
\end{aligned}
\]

**ST26.1 (exact nested-threshold theorem).**
\[
\boxed{K_V(\eta)<K_E(\eta)<K_W(\eta),\qquad
K_W(\eta)-K_E(\eta)=\phi(a_R^*(\eta))^2>0.}
\]
This is an EXACT algebraic identity with the full installed fee accounting. The first strict inequality uses the certified member governmental B>0; the second uses phi>0 and the strictly positive private optimum. The outsider's M-L national gain is K_V-K (negative everywhere inside this coexistence rectangle), while each RS insider's gain is B>0. Accordingly majority+universal proposer M is adopted after the OON history despite the outsider's strictly negative national gain.

All THREE functions K_V, K_E, K_W strictly decrease in eta in the rectangle. Proof: Stage11 f_aa<0 and f_aη>0 imply a*'(η)>0; six separate exact two-dimensional Bernstein-sign certificates verify that each K function has strictly negative partial derivatives with respect to eta and a throughout eta∈[.10,.14], a∈[.25,.61]. Thus total derivatives are strictly negative without checking merely selected gridpoints.

### Three economic regions — not one welfare threshold

Conditional on the privately optimal bilateral RS observed in the SAME economic environment (and considering K over its real domain), the K threshold comparison has these strictly ordered phases:

| K region | Nonmember government's vote | Public IS relative to RS **before** investment | Mandatory public upgrade **after** RS costs sunk |
|---|---|---|---|
| K_V<K<K_E | NO | Better | Better |
| K_E<K<K_W | NO | Better | **Worse** |
| K>K_W | NO | **Worse** | **Worse** |

This table is a **conditional political/welfare map at the observed optimal RS design** and is not a global initial-investment equilibrium phase classification outside the proved eta,K rectangle. At equality endpoints welfare is tied, and tie YES applies to GOVERNMENT votes, not welfare sign. Within the certified eta,K coexistence rectangle K>K_V always holds by Stage14.

The central middle region is a **sunk-cost/time-consistency wedge**: public IS is efficient if chosen *before* private firms irreversibly develop an alternative O(1,a*), yet after that real capital has been invested, forcing all those firms to retrofit to public O(1,0) destroys strictly more resources than it recovers, lowering aggregate realized welfare. The full wedge is exactly phi a*². This is an actual economic distinction between two alternative policy timings, not mere relabeling of voter payoffs.

### Welfare-crossing ordering in the same eta,K rectangle

Stage11 and Stage15 already established that for EVERY K in [.54,.56] both welfare curves cross K exactly once as eta rises on [.10,.14]. The Stage26 exact monotonicity certificates and the strict K_E<K_W relationship strengthen this into

\[
\boxed{\eta_E(K)<\eta_W(K)\qquad\forall K\in[.54,.56].}
\]

When eta is BELOW eta_E(K), ex-post M is collectively desirable (though the outsider vetoes under unanimity). When eta is BETWEEN eta_E and eta_W, M is desirable before OON investment but harmful after private OON investment. When eta exceeds eta_W, retaining the RS has higher collective welfare under both investment timings (but majority+universal agenda cannot support it as a pure SPE terminal outcome).

**Exact root isolations at K=11/20=.55:**
\[
\boxed{.111<\eta_E(.55)<.112,\qquad
.118<\eta_W(.55)<.119.}
\]
These are rigorously certified by exact rational brackets for the unique a*(eta), exact f_a opposite signs on each bracket, exact negativity of K_E and K_W derivatives in a, and four exact rational inequalities at eta=.111,.112,.118,.119. Approximate numerical root values (NOT the proof): eta_E(.55)≈0.111240512597, eta_W(.55)≈0.118862471741.

**Exact time-consistency witness:** eta=.115=23/200 and K=.55. The uniquely optimal real design satisfies 39823/100000<a*<39825/100000. Exact rational inequalities give K_E(.115)<.55<K_W(.115). Thus public IS NNN/M is more efficient than OON/L when comparing initial feasible investments, but an ex-post M retrofit forced on installed OON/L reduces aggregate welfare. Both signed conclusions are STRICT.

## ST26.2 — constitutional quorum × agenda-selection rule, conditional on an observed OON history

Exact member/outsider vote-gain signs are (B,B,K_V-K), where K_V-K<0. Denote G1 the exclusive agenda holder in one counterfactual.

| Approval rule | G1 alone may propose | All three may propose |
|---|---|---|
| Unanimity | **L**, outsider vetoes | **L**, outsider vetoes |
| Two of three YES | **M** if G1 belongs to the original RS pair; **L** if G1 is outsider | **M** regardless of which two countries were in RS |

The table is an **ex-post, observed-history** continuation comparison. Separately certified *full initial pure-SPE* conclusions:
- Under unanimity, genuine privately optimized OON/L RS SPE exists, coexisting with NNN/M IS for all three assignments of the paired countries (Stage15/18/19, under the reduced no-transfer rules).
- Under exclusive G1 agenda + majority, the pair G2/G3 can still support its RS SPE because the outsider G1 never proposes M (Stage18/19).
- Under universal agenda + majority, every pure-SPE terminal outcome is mandated public IS (Stage21–25), for the baseline technology and a wider seven-parameter neighborhood.

**Crucial counterfactual discipline:** Comparing the actual RS equilibrium under unanimity/agenda-veto against the actual NNN public IS equilibrium under universal majority requires the **EX-ANTE** cutoff K_W, not K_E. The latter only measures the social effect of a mandatory retrofit imposed AFTER private firms had already spent the real nonrefundable OON capital. Claiming that K_E determines which political constitution's SPE welfare is higher would be WRONG.

At eta=.10, K=.55 we have K_W>.55, so the public equilibrium is ex-ante more efficient; at eta=.14, K=.55, K_W<.55, so the privately retained regional equilibrium is ex-ante more efficient. Hence neither constitutional rule is uniformly welfare-superior on the analyzed rectangle. This reinforces the point that eliminating RS equilibria is NOT a welfare theorem favoring majority as a constitutional reform.

## Existing theory priority audit (screening, not full text identity)

- Gandal and Shy (2001), JIE 53:363–383, DOI 10.1016/S0022-1996(00)00067-2: established government recognition, three-country standardization unions, nonmember exclusion, and potentially lower world welfare from coalition formation. Thus **three-country standardization conflicts or socially excessive regionalism are not original**. The difference to test is this project's sunk continuous private design investments interacting with both national proposal rights and approval quorum, and the two distinct ex-ante/ex-post welfare thresholds.
- Klimenko (2009), JIE 77:151–166, DOI 10.1016/j.jinteco.2008.08.005: compatibility policy strategic among governments, with non-cooperative excessive or insufficient compatibility already established. Thus **government policy divergence from world welfare is not new**.
- Farrell and Simcoe (2012), RAND J Econ 43:235–252, DOI 10.1111/j.1756-2171.2012.00164.x: standard-setting governance and ex-ante proposal-quality incentives already theorized. Thus **rules matter for investment is not new**; its model emphasizes bargaining/delay and screening, unlike sunk OPEN design stock and public national proposal/majority rules.
These publisher summaries support a LIMITED differentiated-mechanism claim, not proof-level global novelty. For a publishable theoretical contribution, compare the exact closest propositions and their assumptions and avoid trivial relabeling of older coalition/commitment results.

## Stage27 research priorities

The inequalities K_V<K_E<K_W are simple *conditional*, structurally interpretable cutoffs but **not** necessary/sufficient conditions for the existence of all initial pure SPE when the fixed-capital parameters K or eta leave the certified coexistence range. Stage27 should identify and prove when a full private OON SPE emerges, disappears or becomes supported under other agenda/approval rules, with the private first-stage Nash deviation inequalities and a constructive subgame continuation, not only ex-post voter thresholds. A more general voting-rule/quorum result with n countries is another possible expansion, but that would be a NEW model needing separate technology and coalition proofs.

## Reproduce

Code: code/stage26_nested_policy_welfare_cutoffs.py. It verifies exact symbolic identities for all eta,a,K, full-real eta/a Bernstein monotonicity, exact positive member vote and negative outsider vote signs, bracketed optimal-design roots, strict numerical intervals by rational inequalities, and all three founder-pair permutations under the two-by-two political constitutional rules. Workflow: .github/workflows/stage26-threshold-ordering.yml; reruns Stage11,14,15,19,23,25 and the Stage26 certificate.
