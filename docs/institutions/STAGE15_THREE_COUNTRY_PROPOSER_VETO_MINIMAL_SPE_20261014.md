# Stage 15 — Proposer wants mandatory standardization, outsider government vetoes: why THREE national governments matter

**2026-10-14 JST.** Stacked Draft PR after Stage14. This is the FIRST **direct continuous-private-strategy SPE** showing, in an explicitly SIMPLIFIED six-actor 3-firm/3-government model, that the agenda-setting RS member government strictly PREFERS a public international-standard intervention and the OTHER MEMBER country approves it, but the THIRD, NONMEMBER country vetoes it, so the existing privately established OPEN bilateral RS remains a SPE outcome. The candidate RS is OPEN (not a protected proprietary X), so hold-up by incumbent private patents is **not** required for this particular veto phenomenon. A two-of-three voting rule passes the same desired policy; the open-RS initial candidate loses SPE stability under that voting rule. This concretely illustrates the strategic necessity of a third country with separate local welfare, subject to the caveat that a literal two-country market model is different from merely changing the voting set.

## 1. Minimal six-player extensive form—DECLARED reduction

Original market primitives fixed `(v,gamma0,kappa,rho,phi)=(.01,.14,.02,.32,.14)`. The product-distinctiveness spillover `eta` varies over `[1/10,7/50]=[.10,.14]`, and real technology-family setup `K` over `[27/50,14/25]=[.54,.56]`.

At t=1, THREE independent profit-maximizing firms F1,F2,F3 choose **N** or OPEN legally usable O(c_i,a_i) with *arbitrarily real* `0<=a_i<=c_i<=1`, c_i>0 for installed technologies. Real resource fee `K+phi(c_i²+a_i²)/2` incurred up front and irretrievably sunk. If two or three firms use O, their pair compatibility and common design are min(c_i,c_j),min(a_i,a_j). If only two are members, the active outside product has distinctiveness substitution `d=gamma0-eta*min(a1,a2)`. Stage11 positive definite three-country demand Cournot and KKT remain intact. Each of the 3 physically identical segmented national markets has 3 domestic/foreign product suppliers, and G_i national objective `W_i=P_i+CS_{home}`.

At t=2, G1 is the agenda setter and representative of a potential RS member; it proposes public mandate M **of a SINGLE pre-existing lawfully implementable O(1,0)**, or nonintervention L. G2/G3 vote sequentially. Under **UNANIMITY**, M succeeds if both other governments approve; after M, F1/2/3 simultaneously decide conform to PUBLIC O(1,0) or permanently EXIT. At all relevant parameter/histories the unique policy-after-M adopter Nash is ALL THREE COMPLY: every conforming firm's gross operating profit under one compliant firm is >=25/33≈.75758, while each person's maximum incremental real installation fee <=K+phi/2<=.63. Under L every firm continues producing in the market and existing matching labels determine substitutions.

**Removed from the theoretical core by Stage14 causal ablation:** optional accreditation C of private O, both proprietary X/Y actions, and a governmental full continuum public cP,aP engineering stage. These are legitimate extension games, NOT secretly included in the minimal theorem. This reduction avoids the unresolved assumptions about proprietary IP ownership, publicly inventing an arbitrary technical family, and post-C Nash selection. Both legacy N and OPEN privately installed O are legally available to any firm, with real costs. The older more complex Stage10/11 claims remain separate historical drafts; do not transfer this complete proof to those enlargements without an independent deviation check.

At t=3 final differentiated 3-firm Cournot output/market share and W_i.

## 2. Direct three-country veto sign proposition (EXACT continuous-region)

At proposed private RS `h_R=(O(1,a_R^*(eta)),O(1,a_R^*(eta)),N)`, the privately chosen `a_R^*` is unique and lies (.25,.61) for EVERY eta in [.10,.14], with `c_R^*=1`. The private member pre-setup K net `f(eta,a)=3m x(eta,a)^2-phi(1+a²)/2`, outside firm gross `P_O=3m y²`, CS_R common home consumer surplus, and public per-country W_I^0 is computed with fee `phi/2` BUT prior to each firm's K.

Baseline RS:
`W_1^L=W_2^L=f(eta,a_R^*)+CS_R(eta,a_R^*)-K`,
`W_3^L=P_O(eta,a_R^*)+CS_R(eta,a_R^*)`.

If G1's proposed M is approved, old OPEN design O(1,a_R^*) is DOWNGRADED to O(1,0) within the SAME legally open family, so old real extra a-investment is sunk with **NO refund**; incremental fee for prior O firms is zero because the new public c is unchanged (=1) and a=0. The newcomer F3 initially N must pay K+phi/2 for mandated O(1,0), and the baseline W_I^0 already includes phi/2:
`W_1^M=W_2^M=W_I^0-K-phi(a_R^*)²/2`,
`W_3^M=W_I^0-K`.

Therefore exact votes are:
`Delta W_1=Delta W_2=W_I^0-phi*(a_R^*)²/2-f-CS_R > 0`,
`Delta W_3=W_I^0-K-(P_O+CS_R) < 0`.

**THEOREM 15A:** ALL the two-member YES / outsider NO signs are strict for the *ENTIRE REAL 2D rectangle* eta∈[.10,.14], a∈[.25,.61], K∈[.54,.56]. The Stage14 exact independent rational **bivariate Bernstein** certificates prove each of the relevant sign numerator and denominator has ALL 25 basis coefficients strictly positive. This gives **nonempty policy conflict regions**, not a cherry-picked approximate calibration. It is especially interesting that proposer G1 and G2 agree on intervention despite the private O collaboration, while G3 independently preserves the asymmetric RS.

In the subgame after h_R, G1 STRICTLY WOULD PREFER the implemented public M terminal allocation to L (its policy objective). But under UNANIMITY G3 vetoes M, hence G1 cannot obtain it by proposing. Thus G1 is **INDIFFERENT between making the doomed proposal M and selecting L** in the *initial agenda action*. There exists a subgame-perfect continuation where G1 publicly PROPOSES M, G2 casts YES and G3 rejects NO, but when an institutional tie-break always favors a safe L proposal, G1 would instead propose L. These exact distinctions prevent the false claim that G1 has a strict strategic incentive to make a doomed proposal. The core political statement is strict in its preference for implementation, not strict in observable proposal behavior.

## 3. GENUINE full-continuous UNANIMOUS RS SPE construction, for the MINIMAL GAME

**THEOREM 15B:** For EVERY real eta∈[.10,.14] and K∈[.54,.56], the minimal O/N-only three-company/three-government sequential unanimous-vote game has (at least) TWO distinct SPE final outcomes:

- **Private OPEN RS**: initial `(O(1,a_R^*),O(1,a_R^*),N)`, onpath G1 wants M and (weakly optimally) MAY PROPOSE M, G2 votes YES, G3 strictly vetoes; final policy is L. All 3 companies continue producing, third nonmember market-active.
- **Public IS**: initial `(N,N,N)`, government G1 proposes M and G2/G3 strictly approve; all 3 conform. Public final specification O(1,0), cP=1,aP=0.

All real continuous private unilateral deviations are blocked, NOT by discrete sampling:
- **RS member deviates O(c,a)**: if L continues, its market common effective design with other founder O(1,a_R*) is min(1,c),min(a_R*,a), and maximal private net profit is achieved uniquely at the original c=1,a=a_R* (Stage11 global `P_R,c>0`, strict concavity `P_R,aa<0`, and wasted a>a_R*). If after deviation gov chooses M, its total initial+retrofit OPEN stock is `K+phi(1+a²)/2>=K+phi/2`, so public net payoff <=`P_I^0-K<f(a_R*)-K`. Thus no gain even with different gov continuation.
- **RS member deviates to N**: then private prehistory is `(N,O(1,a_R*),N)`; all 3 national governments STRICTLY favor public M over L. For the two N representatives `W_I^0-K>W_N` since K<=.56; for the sole old-O representative `W_I^0-W_N+phi/2>0`. Hence public M is enacted, and deviant net profit `P_I^0-K<f(a_R*)-K`; choosing N to evade private setup is NOT a profitable deviation.
- **RS outsider deviates to O(c,a)**: after L, entrant bilateral interaction with fixed two O(1,a*) founders results in a genuinely asymmetric but SPD Cournot market; Stage10/11 exact universal KKT inequalities show entrant quantity <3/5 for EVERY feasible c,a. Its net payoff <=3m(3/5)²-K<.5292, whereas outsider's current gross P_O>9114361/16635300≈.547893. Under M it instead makes <=P_I^0-K<P_O. Thus no gain. N is status quo.
- **Public IS initial NNN**: all 3 governments strictly favor M, compliance unique. A deviating firm O(c,a) cannot induce voluntarily profitable alternative under L because solo O technology creates NO collaboration and returns `P_N-K-phi(c²+a²)/2<P_I^0-K`; if M still passes its old sunk stock plus incremental public O retrofit `K+phi(1+a²)/2` is >= the direct public fee, so its net profit <=`P_I^0-K`. Thus no profitable initial deviation.
- At every other observed private history, governments have finite M/L and sequential votes; M adoption uniquely all-compliance. Backward induction gives credible strategies after each history. G1's weak M/L onpath tie under veto is handled exactly. These define true SPE of the full continuous-initial-action *MINIMAL* extensive game.

No certification C or proprietary X/Y deviation occurs in this reduced game, so the theorem does not automatically establish original richer Stage10/11 game.

## 4. Counterfactual formal voting-institution test

**THEOREM 15C: Same market, technology and three country welfare functions; change ONLY the national voting rule from UNANIMITY to 2-of-3 SIMPLE MAJORITY.**

At observed open-RS `(O(1,a^*),O(1,a^*),N)`, governments G1,G2 STRICTLY support M, G3 rejects. Majority vote **enacts M**. The private RS path therefore can no longer be the same final RS outcome.

More strongly, even the INITIAL corporate profile itself cannot be an SPE under the majority rule: initially the two O founders would have sunk real positive common product alignment capital `phi (a^*)²/2` each, but a public mandate M(1,0) is ultimately implemented, rendering that design investment wasted. Founder F1 can instead choose N in the initial stage; its changed prehistory `(N,O(1,a^*),N)` induces unanimous public mandate, and it avoids precisely `phi(a^*)²/2>0` real capital expense while obtaining identical final Cournot market output. Hence the founder has a STRICT initial-stage profitable deviation under majority:
`Delta P_1^{majority}=phi (a_R^*(eta))²/2>0`.
All other underlying primitives and player groups are unchanged. This is an ACTUAL equilibrium stability difference from institutional votes, not just the political table.

**Limits**: This proves THIS private OPEN RS initial profile and its continuation collapse under majority; it does NOT prove all RS SPE are impossible under majority, nor compute every majority-rule possible outcome. Also it is not a literal 2-country MARKET model. A comparison retaining ONLY G1,G2 as decision-makers with the same 3-country demand makes the same point about which national VETO is necessary for the mechanism, but cannot on its own justify that literally only two countries can never have an interesting standards game.

## 5. Two thresholds with DISTINCT content: national veto vs social-optimal ex-post public switch

The OUTSIDER veto boundary after a privately optimal open RS is
`K_{G3}(eta)=W_I^0-[P_O(a_R^*,eta)+CS_R(a_R^*,eta)]`.
G3 approves M if K<K_G3; vetoes if K>=K_G3. By exact Bernstein `(P_O+CS_R)_eta>0, (P_O+CS_R)_a>0`, and Stage11 `a_R^{*\prime}(eta)>0`, the veto threshold **K_G3 is strictly decreasing** over eta∈[.10,.14]. Exact signs show K_G3(eta)<.54, so outsider veto operates throughout the proven RS/IS SPE coexistence rectangle.

The PRIOR Stage11 EX ANTE comparison between two terminal equilibrium paths has world aggregate welfare difference
`S_I^{ex ante}-S_R^{ex ante}=K_{world}(eta)-K`.
It counts from-scratch investment on the two different separate equilibrium paths, and its `K_world(eta)` strictly decreases with eta.

An intervention **AFTER** an OPEN private RS has already invested irrecoverable shared-product a^* capital must account for the sunk design wasted upon downgrade to public O(1,0). Hence the true AFTER-history world sum gain from implementing the public mandate vs maintaining RS is
`Delta W_{world}^{ex post}=K_{world}(eta)-K-phi(a_R^*)²`.
Define `K_{post}(eta)=K_{world}(eta)-phi(a_R^*)²`: the exact Stage11 strictly falling K_world and increasing a_R imply **K_post strictly falls** with eta.

**THEOREM 15D:** For EVERY real K∈[.54,.56], the THREE-country total welfare of a public mandate AFTER the installed private open RS crosses from strictly beneficial to strictly harmful exactly ONCE as eta increases across [.10,.14]. Rational root brackets at eta=.10 a*∈(.3053,.3054) and eta=.14 a*∈(.5949,.5950), together with exact tensor-Bernstein verification of both derivatives, establish strict positive gain at eta=.10 even when K=.56, and negative gain at eta=.14 even when K=.54. Therefore G3's private veto is **inefficient when eta small** but may be **efficient when eta large**, even though it remains an individually rational no vote. This is more precise than arguing only from ex-ante comparisons: the two social-welfare thresholds K_world and K_post should not be conflated.

**Independent exact CI proof chain:** stage11 global design optimum and welfare derivatives, stage14 strict national preference bivariate Bernstein, stage15 full continuous minimal game, governance regime comparison and *additional* ex-post welfare monotonicity Bernstein.

## 6. Illustrative normalized payoffs at K=.55

| eta | private optimal a* | G1/G2 implemented-public-M preference (∆W per country) | G3 implemented-public-M preference (∆W) | World welfare RS−IS across independent initial paths | Ex-post social gain from M after the installed private RS | Majority founder's profitable N deviation |
|---:|---:|---:|---:|---:|---:|---:|
| .10 | .30534434 | +.04952276 | −.06865937 | −.04343907 | +.03038614 | +.00652646 |
| .12 | .43260917 | +.03699642 | −.10337697 | +.00318302 | −.02938412 | +.01310055 |
| .14 | .59495151 | +.01663849 | −.15641964 | +.07358723 | −.12314266 | +.02477771 |

Numbers rounded, from true Cournot quantities and policy-dependent real sunk resources. The signs of all first-stage and government inequalities and the unique welfare reversal are certified for entire rectangles with EXACT rational arithmetic; approximations are illustrative only.

## 7. Prior-art/novelty warning and manuscript core

Takarada et al. (2020) already discuss nonmember countries' ability to block global multilateral standards, so **the existence of an outsider veto alone is NOT NOVEL**. Gil Moltó et al. (2005) endogenize differentiating technology, Ghosh–Morita (2012) distinguish internal-vs-outsider substitution, and Farrell–Saloner (1985/1986) analyze standard lock-in / installed-base costs. The **new candidate** is more precise and falsifiable: *endogenous private a_R^*(eta) induces G1's desire for mandatory public interoperability but a stable outsider G3 veto; changing the national voting rule both reverses the government's policy choice and creates a strictly profitable first-stage underinvestment deviation, eliminating the same private RS candidate; social efficiency of that persistent veto flips within the coexistence region*. This is a theoretical joint-mechanism result whose originality remains provisional until the closest source formal propositions are fully compared.

The manuscript's most economical baseline should be the **3-National-Government, 3-Firm, O/N-only L/M model**, with the two-company privately chosen design interior and a vetoing differentiated outsider. Proprietary X/Y labels, certification C and freely government-designed cP,aP are **nonessential** for this theorem, and may be relegated to optional extensions. The real meaning of 'two-country model is insufficient' is **an independent third government with domestic welfare/veto preferences is needed for this particular proposer-frustration mechanism**, not that all interesting standards research literally requires three country economies. Government national authority and prior existence of O(1,0) remain exogenous legal preconditions.

**Repository evidence:** `code/stage15_three_country_veto_minimal_continuous_spe.py`, `.github/workflows/stage15-three-government-veto-minimal-spe.yml`, antecedent exact symbolic code Stage11/14. Independent detailed source and rational proofs are in each stacked Draft PR. No paper manuscript edited, no merges.
