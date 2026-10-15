# Stage30N — A clean agenda-right experiment with quorum held fixed

Date: 2026-10-15 JST. Inputs: Stage30C C1–C7 original mathematical baseline PASS, Stage30M PR70 adversarial institutional objection B2, Stage30L outline. **The original model and government policy selector are UNCHANGED.** This is a fully specified *within-model* comparative institution and an economics exposition aid, NOT a new C8 theorem, empirical identification, endogenous politician Nash-equilibrium proof, or production manuscript release.

## 1. Fix the constitutions BEFORE corporate investments

Three countries and firms are permanently labeled 1,2,3. Choose both institutions **ex ante**:
\[
\mathcal I_{\rm old}=(r=2,\mathcal A_{\rm old}=\{3\}),\qquad
\mathcal I_{\rm new}=(r=2,\mathcal A_{\rm new}=\{1,3\}).
\]

- Both constitutions require two nationally sincere YES votes. **Quorum is identical**.
- Only the proposer eligibility changes: country 1 receives a previously absent right to propose M, while country 3 retains that right.
- This is NOT a treaty reform in which a committee can appoint "whichever state happens to be the outsider" after seeing firm investments. The *fixed* old \(\mathcal A=\{3\}\) makes country 3 eligible no matter which firms invest. We choose a representative **old pure equilibrium** in which firm 3 is N; we do not make agenda a function of investor identity.
- Rule M: \(\#\{i:\Delta_i\ge0\}\ge r\) **AND** \(\mathcal A\cap\{i:\Delta_i\ge0\}\ne\emptyset\), with YES on \(\Delta=0\) ties; the states' sincere choices are **stipulated deterministic protocol behavior**, not Nash voting.
- All 3 governments vote when M is validly proposed, regardless of eligibility to place the motion.

### Why this fixes the referee's problem

For a preannounced private pair \((O(c,a),O(c,a),N)\) with country 3 outside, **C7** yields \((\Delta_1,\Delta_2,\Delta_3)=(B,B,V-K)\) with \(B>0\) and \(V-K<0\). Thus states 1 and 2 support M, state 3 opposes it. Both systems have \(r=2\). The old government set contains only state 3, which will not propose: M fails on proposer eligibility **even though there are two YES voters**. The new A contains state 1, which is willing to propose: M passes. The constitution's policy difference is therefore **agenda eligibility alone**.

C1 certifies that under old fixed r=2,A={3} all private pure SPEs must have firm 3 as the unique N outsider, with founders 1 and 2 and \((c,a)\in R(\eta,K)\). C1 rejects private pure SPE with outsider 1 or 2 under this old singleton A because one of their founders is the sole eligible proposer. Under the new **fixed** A={1,3}, there are two eligible proposers and r=2: C3 says **every** pure SPE ends M, no private pure SPE survives for *any* founder/outsider permutation. This is a statement about two full **equilibrium correspondences**, not a claim only about the policy passage at one chosen historical state.

**Remember the OLD constitution also admits public pure SPE**, e.g. all N followed by M; C2 says their world welfare equals the NEW public pure equilibrium's world welfare. C6 includes these old public SPE in its \(\forall e_{\rm old}\) quantifier.

## 2. Two old *pure SPE* histories, same parameters, same constitutions

Take certified \(\eta=.14\), \(K=.55\), \(c=1\). Two distinct old private pure SPEs with firm 3 outside:
- **L-low:** \(h^0=(O(1,0),O(1,0),N)\);
- **L-high:** \(h^{.5}=(O(1,.5),O(1,.5),N)\).

Both pass the COMPLETE C1 characterization: \(F_a\ge0,\ F\ge P,\ K>V\). This is not inferred merely from a numerical sample: the C1 theorem supplies the global equilibrium claim; \`code/stage30n_fixed_quorum_counterfactual.py\` recomputes exact rational **membership conditions**, actor welfare, policy and accounting in both histories.

| At \(\eta=.14,\ K=.55\) | Old \(r2,A=\{3\}\) | Same original investment history with new \(r2,A=\{1,3\}\) | New institution's ACTUAL pure SPE |
|---|---|---|---|
| \(h^0\): 1,2 choose O(1,0), 3 chooses N | M blocked because only country3 may propose and it votes NO; outcome **L**, this is an old pure SPE | M adopted: founder governments vote YES, country1 can propose | **Yes, h0 itself is a new public pure SPE** under C3 because all a=0 |
| \(h^{.5}\): 1,2 choose O(1,.5), 3 chooses N | Same outsider proposer blocks M, ending **L**; old pure SPE | M adopted **after \(\phi a^2\) already sunk**, but **not a new SPE** | No: firms avoid sunk a>0 in new public pure SPE; some all-zero-a profile instead leads to M |

**Most consequential referee warning:** Ex post **mandating M on a previously installed \(h^{.5}\)** and ex ante **replacing the constitution before investment** are NOT the same experiment. A retrospective M at that old investment profile carries unused sunk commonality \(\phi a^2\); a new constitution's actual M pure SPE has \(a_i=0\) by C2, avoiding it. Do not use after-sunk world welfare in C6's across-constitution condition or claim \(h^{.5}\) itself remains a new pure SPE.

## 3. Exact national preferences and resource incidence

At any old C1 private history \((O(c,a),O(c,a),N)\) write \(F=3mx^2-\phi(c^2+a^2)/2\), \(P=\pi_I^g-\phi/2\), national home-market CS as \(C\), reference public per-country world-incidence as \(W_I=P+CS_I\), and \(B,V\) as already defined.

| Actor | L payoff at old private history | M payoff at that same installed history | M−L sign on C1 |
|---|---|---|---|
| Founder **firm** 1 or 2 | \(F-K\) | \(P-K-\phi a^2/2\) | \(P-F-\phi a^2/2\le0\) (**weakly** private) |
| Founder **government** 1 or 2 | \(F-K+C\) | \(W_I-K-\phi a^2/2\) | \(B>0\) (**strictly** public) |
| Outsider **government** 3 | \(3my^2+C\) | \(W_I-K\) | \(V-K<0\) (**strictly** private) |

The governments' current preferences are *not* a preference reversal of each single government over time. The founder firm's private-profit motive is distinct from its national government's joint firm-profit + **domestic** CS objective. The outsider's international firm's worldwide profit is included, and its country's one domestic market CS is included. No payments/royalties/transfers are silently invented.

### Real one-time costs: distinguish "incurred already" from "new under M"

| Real cost | Founders, under L | Founders, retrofitted M after existing private investment | Outsider under L | Outsider under M |
|---|---|---|---|---|
| Family qualification \(K\) | **Already sunk \(K\)** | **Reused \(K\)**; no second K | zero | **New real \(K\)** |
| c-intensive stock \(\phi c^2/2\) | Already sunk | Already sunk; complete to 1 at real \(\phi(1-c^2)/2\) if needed | zero | \(\phi/2\) new |
| a-intensive positioning \(\phi a^2/2\) | Sunk, commercially valuable under L | **Sunk but stranded** after M | zero | zero |
| Public government's separate administrative cost | zero by primitive | **zero** | zero | **zero** |

For a founder the total M real expense from pre-policy choice through implementation is \(K+\frac\phi2(1+a^2)\), irrespective of the earlier c (sunk c is completed, not repurchased). Under an actual **new public SPE**, a=0, so each of the three firms' total M real expenses are \(K+\phi/2\). For an installed old private pair the private world welfare is \(T(c,a)-2K\); at the **same history** forced M produces world welfare \(3(W_I-K)-\phi a^2\). In the *new constitution equilibrium* M world welfare is \(3(W_I-K)\).

At \(\eta=.14,K=.55,c=1\), with exact Fraction values retained in \`STAGE30N_FIXED_QUORUM_EXACT_RESULTS.json\`:

| Private design in old pure SPE | Founder govt gain B at same history | Outsider govt gain \(V-K\) | World L payoff (old) | World M in NEW pure SPE | NEW M minus OLD L |
|---|---:|---:|---:|---:|---:|
| O(1,0) bilateral | +0.063464 | −0.020781 | 3.081243 | 3.187390 | **+0.106147** |
| O(1,.5) bilateral | +0.024917 | −0.133622 | 3.236178 | 3.187390 | **−0.048788** |

The same reform, same \(\eta,K\), same country names, same r and A pair has **opposite welfare signs relative to two legitimate old equilibria**. This is exactly why the universal C6 condition \(K\le K_W(\eta)\), rather than "public implementation always raises welfare", is the meaningful policy result. At eta=.14, K=.55, \(K>K_W\) (computed in earlier Stage30 exact root work), so universal dominance fails; worst public-only welfare is higher than worst OLD welfare while top private L is eliminated. These dimensionless numbers are MODEL magnitudes, not empirical policy impacts.

### Ex ante / post-sunk treatment particularly transparent at \(a=.5\)

The old \(h^{.5}\) path reaches L at world welfare approximately **3.236178**. If its installed a=.5 investment is retrofitted to M, that SAME history produces \(\mathcal W_M^{post}\approx3.152390\), since wasted private a in two founders totals \(\phi a^2=.035\). A different NEW pure equilibrium with a=0 under the broad agenda reaches world welfare **3.187390**. Therefore:
\[
\underbrace{\mathcal W_M^{post}(h^{.5})-\mathcal W_L(h^{.5})}_{\approx-.083788}
\ne
\underbrace{\mathcal W_{\rm new}^{ante}-\mathcal W_{\rm old}^{ante}}_{\approx-.048788}.
\]
Difference \(=.035=\phi a^2\) is a cost-accounting identity, NOT the independent economic contribution. The important part is that C1/C3/C5 characterize which old/new histories are **equilibria** before applying the identity.

## 4. Hold-agenda alternative to separate voting-threshold change

To examine a different institutional effect, take **fixed A=\{3\}** but alter r=3 to r=2 at a candidate old private history with outsider3. Since outsider3 votes NO, the proposal never occurs in either institution; this specific private history survives both (C1). Thus changing r alone **does not** necessarily eliminate private L when the only potential proposer is the opposed outsider. More generally, broadening agenda alone at **r=3** does not eliminate L, since two YES governments cannot meet unanimous approval. For a full transformation to public-only C3 outcomes one needs BOTH a sufficient voting threshold \(r\le2\) and a set of eligible proposers of size at least 2—or the fixed-r2 agenda reform illustrated in §1.

This motivates accurate comparative prose:
- "Dispersing proposer eligibility **given an already nonunanimous quorum** can remove every private L SPE" is directly demonstrated here.
- "Changing proposal rights ALWAYS eliminates private coordination" is false.
- "Changing quorum alone ALWAYS eliminates private coordination" is false.
- "A voting and agenda reform can extinguish all private equilibria, conditional on the selector" is covered by C3.

## 5. Existing theorem reliance and limitations

No generalized political game has been added: nonpivotal all-NO remains a Nash outcome in unrestricted simultaneous voting; results are conditional on stipulated sincere proposal and YES-on-tie. There is no new implementation agency g and no general positive g robustness: Stage30 g=.04 negative counterexample still controls. The primitive two-/three-developer H branch remains categorical and may be challenged (third O(0,0) entry changes market substitution immediately; K means minimum paid family qualification).

The numeric fixed design example **demonstrates the mechanics** but does not prove the C1/C3 global claims on its own. Their existing Stage30C analytical proof and independent rational sign audits are the source. Four inaccessible published final source theorem corpora remain unresolved (Gandal–Shy 2001, Klimenko 2009, Bordignon–Brusco 2006, Barrett–Yang 2001); Buccella et al. 2026 only published abstract inspected. No claim of firstness made.

**Economic result:** This fixed-quorum example answers the most precise criticism in Stage30M Referee B2: it **separates agenda eligibility from voting-threshold change** and makes national cost incidence and equilibrium-welfare comparisons transparent. It is a manuscript-facing explanatory exhibit, **not** a new theorem, model expansion, evidence of journal priority, Stage7.5A formal proof, or final production paper edit.
