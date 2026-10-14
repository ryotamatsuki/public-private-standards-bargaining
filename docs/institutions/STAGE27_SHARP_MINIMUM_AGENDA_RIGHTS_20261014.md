# Stage 27 — A sharp minimum agenda-rights threshold for pure-SPE regional-standard elimination

Date: 2026-10-14 JST. Stacked on Stage26 Draft PR #54, leaving previous PRs unmerged and the manuscript unchanged.

## The economic question

Previously Stage19 showed that three-government majority plus **ALL THREE** proposal entitlements precludes any private terminal RS in the minimum OPEN/N investment game. Stage18 showed that with a unique G1 agenda holder, the private RS whose pair *excludes G1* may still survive. Stage21–25 globally eliminated all other pure-SPE private outcomes when all three governments possess proposal rights. The exact MINIMUM number of proposer governments needed for the global elimination result was not stated as a necessary-and-sufficient institutional threshold.

This stage completes that **discrete constitutional problem** across ALL feasible nonempty proposal-right subsets and all three voting quorums, without a new technology equation. The principal new result is a sharp **agenda-transversal theorem** under the exact same continuously chosen individual private technologies. It does NOT yield necessary-and-sufficient economic capital/network-parameter phase boundaries outside the prior certified parameter rectangle.

## Model and parameter scope

Maintain the literal Stage15/19 model: three firms independently choose either N or any privately installed but legally OPEN O(c_i,a_i), 0<=a_i<=c_i<=1, with fixed and capitalized upfront fee K, physically increasing c and a stock, pairwise minimum technologically compatible designs, three differentiated Cournot markets, and full individual continuous investment deviations. After observing all corporate choices, each government with a legal proposal entitlement may introduce the ALREADY PUBLIC O(1,0) as a mandatory standard M. Vote ties and proposer-indifference select YES; government policy gain is own firm net profit plus national consumer surplus; no treasury side payments; public O-family retrofits charge missing capital once and never refund sunk a; under M all firms strictly conform. No proprietary X/Y standard, licensing, or private accreditation C.

Fixed technology v=.01,gamma0=.14,kappa=.02,rho=.32,phi=.14, and FULL eta∈[.10,.14], K∈[.54,.56] (certified Stage11/14/15/18/19/20/21). Let A be ANY nonempty subset of national governments {1,2,3} entitled to independently propose public M. Let q be an integer YES-quorum in {1,2,3}; q=3 is unanimity, q=2 is a simple majority, q=1 is a one-vote adoption rule. Private technologies and all other market primitives do not change as A and q vary.

## Theorem ST27.1 — sharp minimum proposal entitlements

**(A) Sufficiency / global outcome elimination.** For q=1 OR q=2, if **|A|>=2**, then at least one pure-strategy SPE exists and **EVERY pure-strategy SPE TERMINATES in public mandatory O(1,0) IS**. There is no private terminal RS (or other L private terminal outcome) in ANY pure SPE, including profiles with heterogeneous full-real open designs at two or three independently investing firms. The NNN→M initial strategy profile is a pure SPE. The proof for q=2 extends Stage19 and Stage21 from three to just TWO authorizing governments using the two-of-three *hitting-set* lemma. The same underlying firm deviations and vote signs prove the q=1 result separately (lower YES-quorum).

**(B) Necessity / constructive private counterexample.** For q=1 OR q=2, if **|A|=1**, there is at least one GENUINE private bilateral OON/L initial pure-SPE outcome, with precisely the two NON-AGENDA countries jointly choosing their privately optimal symmetric O(1,a_R*(eta)) while the sole proposal-holder remains N. That outsider government strictly opposes M, so it never proposes; the two founders cannot introduce M and their own 1st-stage design choices are optimal over all real deviations by the Stage15 uniform deviation lemmas. The public NNN→M pure SPE exists alongside it. Consequently public terminal pure-SPE uniqueness FAILS.

Therefore, for both q∈{1,2}, **|A|>=2 is NECESSARY AND SUFFICIENT for every pure SPE terminal outcome to be public IS** in the stated reduced game and baseline eta,K parameter rectangle. The **minimal delegating agenda set** has exactly 2 members. This is a SHARP constitutional threshold (a necessary/sufficient institutional cardinality condition), not a technology cutoff.

**(C) Unanimity impossibility.** At q=3, for EVERY nonempty A, ALL THREE different identity assignments of the same privately optimal bilateral OON/L private RS are genuine pure SPE, in addition to the public NNN→M SPE. The nonmember government strictly vetoes mandatory public O(1,0), irrespective of how widely proposal rights are distributed. Thus no nonempty delegation choice can globally eliminate private terminal RS while q=3.

### Complete 3x3 constitutional phase table

| Approval q | One proposer | Two proposers | Three proposers |
|---|---|---|---|
| 1 vote | RS + IS coexist | **IS is only pure-SPE terminal type** | **IS only** |
| 2 YES majority | RS + IS coexist | **IS only** | **IS only** |
| All 3 unanimous YES | RS + IS coexist | RS + IS coexist | RS + IS coexist |

“RS + IS coexist” means EXISTENCE of pure SPE of each outcome type, not the absence of other possible initial SPE outcomes or a count of all SPE strategy profiles. “IS only” means the final type of EVERY pure SPE is IS, not that all initial SPE technology choices are identical.

### Exact count of surviving CANONICAL privately optimal pair profiles

Let S denote the TWO founders in a candidate privately optimal bilateral standard O(1,a_R*)/O(1,a_R*), and let A be the agenda-authorized national set. At the relevant observed standard history all national policy gains are \((B,B,K_V-K)\) up to label permutation, with **B>0 and K_V-K<0** uniformly over the full Stage11/14 rectangle. Hence M is enacted if and only if

\[
q\le2\quad\text{AND}\quad A\cap S\neq\varnothing.
\]

Once M is enacted at this candidate history, its founders have a strict initial deviation to N, saving their sunk \(\phi(a_R^*)^2/2>0\), because any resulting singleton-history mandate still passes under every nonempty A and all q<=3. Thus the benchmark OON/L investment profile is an actual pure SPE if and only if

\[
q=3\quad\text{OR}\quad A\cap S=\varnothing.
\]

The second case is possible if and only if |A|=1, in which case the complement \(\{1,2,3\}\setminus A\) is the ONE surviving canonical founder pair. Therefore the NUMBER of **these THREE canonical private founder identities** that remain pure SPE is exactly

\[
N_{\rm canonicalRS}(q,A)=
\begin{cases}
3,&q=3,\\
1,&q\le 2,\ |A|=1,\\
0,&q\le 2,\ |A|\ge2.
\end{cases}
\]

This is NOT a count of all firm-stage equilibria or an assertion all possible RS action profiles under q=3 are known. It is sharp for the stated three natural privately optimal pair patterns.

The computational verifier enumerates ALL **63** constitutional-observed pair scenarios: q=1,2,3, seven nonempty proposal sets, three founder pairs. Every row is checked against the closed-form policy decision and the predicted number of supported canonical RS SPE profiles. It also rechecks exact Bernstein proofs of member positive vote and outsider negative vote, global firm initial deviation upper bounds, and the NNN corporate deviation identity.

## Why just two proposal rights suffice even for arbitrary heterogeneous THREE-OPEN investment

For ANY three-government gain vector, if at least two national governments weakly favor M, A of size>=2 MUST intersect this pair of supporters. Thus if q<=2 the public policy M is adopted.

- Stage20: with 0/1 privately OPEN investors all THREE governments strictly favor M, so A nonempty suffices, any q<=3.
- Stage19: with exactly two investors and a hypothetical pure-SPE terminal L, unequal pair maxima in a or c are strictly redundant corporate investments. With common design O(c,a) and a<=3/4, the TWO member governments strictly favor M and thus every |A|>=2 intersects them. With a>3/4, either member approval and q<=2 again mandates M, or both negative member gains make an arbitrarily small unilateral reduction in a strictly profitable while preserving L. For q=1 the same argument uses strict negativity of every ENABLED proposer's national gain at any observed nonintervention L history, which is preserved by continuity.
- Stage21: with exactly three investors, initial pure-SPE L also forces tied maxima of both private a and c, via strict private firm-capital redundancy. Every remaining aligned or crossed design topology has at least two governments with weakly positive M-L gains, certified by Stage21/24/25 4D-6D exact Bernstein analysis. These two supporters must intersect a size-2 agenda set, so M must pass if q<=2.
- After M all firms strictly comply for all histories (Stage15), and at NNN all governments strictly prefer M and firms cannot gain by initial choice of any O(c,a) because the public retrofit wastes only sunk private a physical stock. Thus the IS equilibrium EXISTS independent of the particular nonempty A and q.

The extension to ANY q∈{1,2}, ANY |A|>=2 also carries over for the **public-IS-only SUFFICIENT direction** to the 7D local technological box already proved in Stage25, because each Stage25 governmental inequality delivers TWO weak national supporters and firm-redundancy deviations are institutionally monotone. **However**, constructive RS existence for |A|=1 and the necessity direction were revalidated ONLY for fixed technology and the eta,K benchmark rectangle; Stage15's no-profitable-deviation bound has not been fully re-certified under all Stage25 technology-parameter perturbations. Accordingly do not promote the full “iff” to the 7D box.

## Economic welfare interpretation with Stage26 cutoffs

The public terminal outcome set becomes pure-SPE UNIQUE once a second government obtains agenda rights, without any change to firms' underlying compatibility productivity or cost functions. The institution itself removes the outsider agenda bottleneck for ALL private standard-setting possibilities, not just the same optimal pair after policy.

But **unique IS is not necessarily world-efficient**. At K=.55 and eta=.10, Stage26's ex-ante cutoff K_W>.55 means public IS has higher world welfare than the private RS. At the SAME fixed K=.55 and eta=.14, K_W<.55 means retaining privately optimal RS would yield higher *ex-ante* world welfare in the one-agenda or unanimity regime. Increasing proposal coverage eliminates this potentially welfare-superior regional private SPE, while public NNN/M was already an SPE under either institution. This is an equilibrium-set comparison; it does NOT specify equilibrium selection when both RS and IS are available under the one-agenda regime.

Stage26's ex-post cutoff K_E concerns retrofit AFTER sunk private O capital, not the welfare difference between the newly possible constitutional pure-SPE outcomes. The latter is determined by ex-ante K_W.

## Related research and limits

The combinatorial hitting-set argument by itself is mathematically elementary. What makes ST27 a model-specific contribution is its application to **the entire endogenous continuously chosen technological pure-SPE space**, including otherwise hard three-firm heterogeneous profiles. Do NOT claim that “two agenda-holders intersect every two-member coalition” alone is a novel result. Nor is strategic standardization or government veto new (see Stage22 and 26 prior-art screens: Gandal–Shy 2001, Klimenko 2009, Farrell–Simcoe 2012). A full comparative theorem/proof examination is still required before selecting a journal.

Further limitations: deterministic nation-level YES-on-tie rule, legally existing exogenous public O(1,0), no intergovernmental monetary bargaining/transfer, 3 countries, no X/Y/C technology variants, and pure—not mixed—subgame-perfect equilibria. The **threshold 2 agenda governments** is an institutional exact result **at n=3**; extending to arbitrary n needs a new n-firm/country Cournot and governmental gain proof. We have NOT derived necessary-and-sufficient private SPNE existence cutoffs in the seven-dimensional fee/network-parameter space outside the certified eta,K region.

## Reproducibility and Stage28

Code: code/stage27_agenda_hitting_set_spe_classification.py. It verifies 63 exact discrete constitutional assignments, cost identities and the original Stage11/14/15 all-real continuous-game inequalities. Workflow: .github/workflows/stage27-agenda-transversal.yml, which re-runs Stage11, Stage15, Stage19, Stage21, Stage25, Stage26 and Stage27.

Recommended Stage28: BEFORE adding institutional complexity, derive the **nearest prior-art theorem-level match**, especially in Gandal–Shy (2001), Klimenko (2009) and Farrell–Simcoe (2012). Then find the sharpest simple economic sufficient inequality (in investment costs/network effects) for the canonical RS founder profile to survive under q=3 or one proposer, and distinguish global iff institutional results from *conditional on-parameters* iff results. Avoid claiming 7D necessary/sufficient economic phase partition solely from this new agenda theorem.
