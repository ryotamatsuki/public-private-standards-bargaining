# Stage30P addendum — simultaneous governmental motion and vote with an admissibility refinement

**Important improvement over the sequential implementation:** One can recover the original policy selector without changing simultaneous-motion and simultaneous-ballot chronology, PROVIDED that political play is restricted to a **stagewise weakly undominated equilibrium selection**, and exact national-welfare ties continue to favor M. This does NOT hold for unrestricted Nash/SPE.

## Formal binary political game at any original firm history h

Given Delta_i(h)=W_i(M|h)-W_i(L|h), let each eligible proposer i simultaneously choose m_i in {0,1}, where 1 tables the single available public M. If sum m_i=0 => L. Otherwise all three governments simultaneously choose ballots b_i in {0,1}; enact M iff sum b_i>=r. The games are finite and complete information; no transfer, motion fee, or ballot fee. The underlying material payoffs and chronology of initial corporate investment then political rule match the originally described simultaneous reading of the protocol.

A **tie convention** adds a *lexicographic* preference M over L only when Delta_i=0, so every government has a strict ordinal preference between the two final policy outcomes even though a material national welfare tie produces no numerical difference. Define S={i:Delta_i>=0}. The lexicographic ordering is a normative tie selection assumption, not an implication of maximizing material welfare alone.

**Stagewise-admissible political equilibrium:** First retain a pure-strategy Nash equilibrium in each referendum subgame that uses no weakly dominated BALLOT action. Given these continuation policy outcomes, retain a Nash equilibrium of the simultaneous proposer game using no weakly dominated MOTION action in that reduced finite game. Do this separately at every private investment history. This is a precisely specified backward admissibility refinement; it is NOT asserted to be full extensive-form trembling-hand perfection of the entire continuous-firm game. Under finite generic binary policy payoffs, subgame-level trembling-hand perfection would also remove weakly dominated actions.

## Proposition P3 (outcome-unique under the simultaneous political admissibility refinement)

For each h, each real Delta, all quotas r=1,2,3 and every nonempty A, every stagewise-admissible government equilibrium produces exactly

    M iff |S| >= r AND A intersects S.

The political action strategies need not be unique when no referendum can possibly pass, but the terminal POLICY is.

### Proof

The ballot decision for an agent who strictly prefers M satisfies: casting YES can never replace M by L and when the other two ballots contribute exactly r-1 YES, casting YES changes L to M. Such a pivotal opponents' configuration is feasible for EACH r in {1,2,3}. Consequently YES **strictly weakly dominates** NO as a ballot action. For an agent preferring L the reverse domination holds. Lexical exact-tie preferrers count as M supporters. Eliminating weakly dominated ballots therefore leaves precisely the sincere action b_i=1{Delta_i>=0}. The only referendum outcome, if a motion is tabled, is M iff |S|>=r.

If |S|<r, any proposal profile yields L, so all surviving motion profiles have the same outcome.

If |S|>=r, a proposal leads to M and no proposals lead to L. For each eligible government in S, proposing weakly dominates abstaining and is **strictly better when no other eligible proposes**. For each eligible government outside S, abstaining weakly dominates proposing and is strictly better in that same pivotal proposal circumstance. Thus after stagewise deletion, precisely the members of A intersect S table M; all opposing eligible members abstain. M occurs iff A intersect S is nonempty. QED.

### Corporate game corollary

Since P3 reproduces the policy selector **for every feasible initial firm history**, all original first-stage corporate continuation payoffs are identical. Thus C1/C3/C4/C5/C6/C7 results from PR60 and the fixed-r=2 Stage30N old A={3} to new A={1,3} counterfactual apply to pure firm equilibria WITH THE SPECIFIED POLITICAL ADMISSIBILITY REFINEMENT on the original two-parameter rectangle.

**This is arguably the smaller institutional adjustment than sequential roll calls**: government motions and ballots remain simultaneous, but an explicit government *equilibrium refinement* is essential. Neither P3 nor P1 validates a claim about **all unrefined political SPEs**.

## Exhaustive policy-game test

The independent Python code code/stage30p_simultaneous_refinement.py computes pure undominated ballot actions by examining all 2^2 other ballots for each voter, and pure undominated motion actions by examining all 2^(|A|-1) other eligible proposer announcements. It verifies exact outcome equivalence over all 27 positive/tied/negative Delta types, 7 nonempty A and 3 quotas: **567 cases**. The code is a separate finite verification of P3, not a proof of the continuous investment equilibrium.

## Referee strategy: two transparent options, not a silent substitution

- **Option I: preserve simultaneous political chronology** and define an admissible/perfect-at-each-government-stage equilibrium concept, proving P3 and then transferring C1–C7. This is the preferred bounded modification for the current paper; refine claims explicitly.
- **Option II: choose a sequential proposer/roll-call constitution** and prove all governmental subgame SPE outcomes directly via P1. This is a more concrete timing microfoundation but changes the government institution.
- **Forbidden:** use either to claim that *unrestricted* simultaneous governmental Nash play implements the rule. The all-NO Nash r=2/NNN-L firm SPE counterexample remains.
- **Open:** tie selection still exogenous; eliminating O(0,0) category effects, government implementation fee robustness and full publication-priority audit are separate tasks. Stage7.5 and manuscript submission stay NO-GO.

## Novelty caution

Sincere voting as a weakly dominant action in a known binary binding referendum is familiar voting theory, not a new contribution. Here the payoff-equivalence transfer to the firm's previously derived full continuous-investment SPE is useful as a **validity repair** of the public-economics interpretation, not a third independent theoretical innovation. Government policy outcome equivalence depends on one fixed M, no participation/proposal costs, full information, and the explicit admissibility/tie rule.
