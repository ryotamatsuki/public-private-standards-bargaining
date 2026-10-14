# Stage 30 — Hostile Referee Report

- **Manuscript:** Agenda Rights, Sunk Compatibility Investment, and Public Standardization
- **Version reviewed:** Stage29 PR #57, commit `2e96112280599cceaee43b89e265fcb5c073f1ca`
- **Recommendation:** Reject in its current full-paper form. A substantially shorter, explicitly conditional theoretical note may be worth reconsidering after the literature and institutional issues below are closed.
- **Mathematical assessment:** CONDITIONAL PASS for the manuscript as a whole; independent PASS for the central baseline result under the prescribed policy continuation. No fatal mathematical counterexample to that reduced game was found.

This is a simulated anonymous report based on an independent implementation and adversarial reconstruction, not an external human referee report. The baseline model and manuscript have not been edited.

## Summary and assessment of the contribution

The paper studies three firms that choose whether and how much to invest in open compatibility technologies before governments decide whether to mandate an existing common interface. Proposal eligibility and the voting quorum are exogenous constitutional variables. Under a specified policy continuation and an explicit parameter region, the author establishes that two independent proposal holders eliminate all non-public pure-SPE terminal outcomes when at most two affirmative votes are required. A sole outsider proposer and unanimity can sustain bilateral private regional standards. A separate analysis distinguishes national vetoes, the efficiency of a retrofit after investment, and the ex-ante comparison of two investment paths.

The full continuous investment-domain argument is a real strength. It is not equivalent to observing that two favorable governments can pass a motion. Heterogeneous investments, wasted stocks, high-commonality deviations, and three-investor cases require additional arguments. I independently reconstructed the baseline sign objects from the Cournot matrix and verified the relevant rational inequalities.

Nevertheless, the paper has not established a sufficiently consequential new economic insight for its present full-paper scale. Much of the constitutional conclusion is elementary once a two-government favorable coalition is established; the welfare wedge is a historical-cost identity. The substantive remaining contribution is a model-specific proof that firms cannot sustain regulatory avoidance through private investment. Its institutional meaning and its difference from the closest standards and collective-choice literature are insufficiently resolved.

## Major comments, in descending order

### R1. Economic contribution relative to the scale of the paper

**Severity: FATAL for the current full-paper editorial claim; not a finding of mathematical falsity.**

The paper should state what an economist learns beyond agenda control, national externalities and irreversible expenditure. “Institutions change the equilibrium set” is too broad and already well established. The meaningful candidate is narrower: certain private technology adjustments cannot sustain a coalition capable of blocking an existing public fallback.

The paper currently proves this using a particular demand specification and parameter box without identifying an important class of actual decisions for which this failure of private defensive investment changes our understanding. A large polynomial certificate does not establish the economic importance of the restriction being certified. The introductory framing should not treat the number of proposal holders as a general constitutional design result.

**Evidence:** main institutional proposition; Introduction paragraphs 5–7; the elementary intersection identity; the independent economic audit, Sections 1–2 and 7–10.

The proportionate remedy is to choose a theoretical note centered on the continuous-investment exclusion and its limits. I do not recommend adding a new standard-design, transfer or information model merely to increase the paper's scale.

### R2. The closest theorem-level comparisons are unfinished

**Severity: MAJOR BUT FIXABLE; submission blocker.**

The manuscript itself acknowledges that the full published propositions and proofs of Gandal–Shy (2001) and Klimenko (2009) remain unexamined. That is not a minor bibliographic omission. They are among the strongest threats to a contribution framed around international standardization and governmental incentives.

This audit obtained the 1996 Gandal–Shy working paper, but that paper must not be substituted for the 2001 publication. The earlier version's linear transport specification differs from the published specification identified in the author's other source ledger. Klimenko's numbered propositions remain unavailable. The correct status is UNRESOLVED, not novelty PASS.

The collective-choice comparison also needs Harstad. His 2004 working paper's Section 5 explicitly considers a losing initiator blocking a no-transfer proposal and a winning alternative proposer restoring a vote; Proposition 10 concerns investment under no transfers. This does not directly absorb the present Cournot externality and min-investment proof, but it makes any broad claim that proposal rights and investment are a newly connected idea untenable.

**Evidence:** `STAGE30_PRIOR_ART_THEOREM_ABSORPTION.md`, especially Sections 2.1–2.2 and 3. See that ledger for source versions, proposition numbers, pages and access failures.

### R3. The government continuation is prescribed, not a complete unrestricted voting equilibrium correspondence

**Severity: MAJOR BUT FIXABLE for the reduced theorem; FATAL if the theorem is asserted for unrestricted simultaneous voting.**

The main proposition is qualified as a result for a reduced game, and the model prescribes favorable voting and proposal behavior. Under that interpretation the policy selector is well-defined. However, the manuscript also says it solves the voting game and describes a full six-player SPE. A specialist could read this as a strategic voting result.

At quorum two, all NO is a Nash voting profile at any private history: no unilateral YES changes the result. This remains true when every country strictly prefers enactment. With no-passage voting after every history, NNN followed by no intervention is a pure SPE of the unrestricted simultaneous-vote game, even with all governments entitled to propose. A unilateral open developer still creates no compatible pair and only incurs costs. At the baseline example, each government's gain from public enactment is approximately .1080, yet all-NO voting is a nonpivotal Nash continuation.

YES-on-tie in national welfare does not resolve this issue: national welfare preferences are strict in the example. The additional multiplicity arises from nonpivotal ballots.

The Conclusion also refers to “a unique public equilibrium,” while the proven uniqueness concerns the terminal standard type. This is a manuscript quantifier regression, repairable without changing the central theorem.

**Required correction:** label the rule as a sincere-voting or prescribed-continuation assumption, or specify an extensive form and refinement that delivers the selector. If a new political game is chosen, it requires rollback and re-certification, not a prose adjustment inside this audit.

**Evidence:** independent mathematical audit, Section 3 and diagnostic 2; `STAGE30_INDEPENDENT_GAME_RESULTS.json`, strategic-vote block. This is not a counterexample to the explicitly prescribed baseline rule.

### R4. The public fallback and the private demand transition drive the result

**Severity: MAJOR BUT FIXABLE in interpretation; a substantive model change would require additional research.**

An existing, open public reference, zero public implementation cost, and no second setup cost for developers are central conditions. The model is acceptable as a restricted diagnostic, but the paper should explain where these conditions jointly hold.

In a pre-specified diagnostic with a public implementation cost of .04 per country, the affected policy game was solved again. At eta=.14 and K=.55, the bilateral private optimum survives with all three proposal holders and quorum two. The national gains are approximately (−.02336,−.02336,−.19642). The corporate deviations are bounded analytically under either possible continuation, and the political signs are independently certified on the optimal-root interval. Thus the negative portability result is not merely a grid calculation. The diagnostic cost is about 2.38% of gross national welfare under the public interface.

A separate concern is the disappearance of the outsider differentiation term when the third firm chooses O(0,0). The incumbent pair's relationship with that firm changes although the entrant has built no positive stock. This is an explicit model primitive, not a coding error, but a technological explanation is missing.

**Evidence:** model demand equations; independent mathematical audit, diagnostic 1; economic audit assumption table; independent entrant-limit diagnostic. The manuscript should retain these limitations rather than claim cross-model robustness.

### R5. The welfare results need a modest interpretation

**Severity: MAJOR BUT FIXABLE.**

The welfare calculations are internally correct. They compare two initial paths and a separate retrofit of an installed regional design. Their separation should be retained.

But the difference between ex-ante and ex-post cutoffs follows from the specified historical resource costs. Endogenizing the commonality stock determines the magnitude and comparative statics; it is not necessary for the positive historical-cost wedge. A positive externally fixed stock would deliver the same identity.

The reversal is not just a numerical knife-edge within the chosen eta interval. At K=.55, the independently evaluated crossings are approximately .11124 and .11886. However, this is not evidence that the reversal is common across economically plausible models. Nor does eliminating a regional equilibrium identify the realized welfare effect of constitutional reform when the original constitution also supports a public equilibrium.

**Evidence:** welfare section; independent exact threshold identities and rational brackets; economic audit, Section 5. The strongest defensible statement is that wider agenda access can remove a feasible welfare-superior regional equilibrium in part of the certified region.

### R6. Certificate transparency and proof boundaries

**Severity: MAJOR BUT FIXABLE for unresolved assurance; otherwise MINOR exposition changes.**

The manuscript provides substantially more proof bridges than a typical solver-only paper: the national policy gain, the polynomial sign object and the Bernstein change of basis are visible. That is commendable as a substantive feature of the audit trail, not a substitute for correctness.

Two improvements are needed. First, the crossed three-investor adjugate numerators should be displayed explicitly. Second, the high-commonality argument should explicitly explain the outsider's strictly negative gain when quorum one and outsider agenda eligibility make it relevant.

I independently verified 43 sign certificates involving 10,023 rational Bernstein coefficients. I reproduced Stage25's seven-parameter certificate but did not independently regenerate every high-dimensional coefficient and derivative bound. The latter proposition should therefore be recorded as NOT INDEPENDENTLY VERIFIED in this audit. Its sufficiency-only scope is correctly stated in the manuscript and should not be strengthened.

The workflow's formal-verification gate also remains unclosed in the evidence inspected. SymPy's exact arithmetic is not a Lean proof of the complete economic game. This is an assurance/provenance issue, not evidence of a false theorem.

## Exposition and minor comments

The English is generally grammatical and readable. The main structural weakness is repetition of agenda rights, irreversible investment and the need to connect histories across the Introduction, policy, equilibrium and robustness sections. Several long paragraphs explain the certification process where the reader instead needs the economic restriction being certified.

The first introduction paragraph begins with a familiar observation about compatibility and should reach the private/government conflict more quickly. “Commonality” needs an interpretation in terms of an implementable technology. The phrase “opportunity cost of that abandoned design” is misleading in the welfare discussion: already sunk expenditure is not a new marginal cost at the retrofit date. Describe the difference between historical paths.

In Appendix A, “The second derivative expression alone” follows a first derivative of F with respect to c; revise the sentence. CS uses H consistently in the model, but an M matrix appears in the appendix while M already denotes the mandate. The constitution table should distinguish existence of displayed terminal types from a full list of initial equilibria.

Concrete original/replacement passages, a compressed structure and an explicit adjugate bridge are supplied in `STAGE30_EXPOSITION_REVISIONS.md`. These are proposed edits only; no original paragraph has been silently changed.

## Recommendation and bounded route

I would not recommend acceptance or an ordinary revise-and-resubmit of the current full paper. The mathematical core is substantially more credible than its economic positioning. A shorter diagnostic note could be reconsidered if it:

1. closes the closest published-theorem comparisons;
2. states the government rule and the contribution's limited scope exactly;
3. explains the demand and public-fallback primitives without claiming an unidentified real institutional match;
4. retains the negative diagnostics and correct welfare comparison; and
5. gives a clear publication rationale for the continuous-equilibrium exclusion.

If those changes do not leave a substantive novelty claim, preserve the working paper and stop. Further model expansion is not a condition of this report.

**Canonical Stage30 verdict: NO-GO. Stage31 submission preparation should not start.**
