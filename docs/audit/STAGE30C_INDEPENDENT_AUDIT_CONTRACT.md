# Stage30C — Additional-results mathematical audit contract

Date: 2026-10-15 JST. Input: PR59 head
`0735322e85dd876c5d361e6ddeaa6a4d79a9bbeb`.
Workflow main: `81c37dd95fc93d918138ba9d0da86541d3cc1067`.
This task implements the claim-register and new Stage4A steps in the revision
execution plan. It does not write the revised manuscript or close Stage6/7.5A.

## Independence disclosure

The reviewing assistant participated in Stage30B construction and has already
seen the claims, their exposition, and prior proof arguments in the conversation.
This is **not a blind first-pass audit or external-human review**. No change of
reviewer/model name is offered as an independence certificate.

The present attack starts again from the frozen manuscript's primitive demand,
cost, compliance, and national-welfare rule. Before reading the Stage30B
construction source code in this pass, it builds a separate quantity/payoff
evaluator and a different proof path. In particular, matrix norm bounds and
monotonicity are used to replace the high-dimensional three-developer sign
argument; the openness of the no-mandate region under YES-on-tie is used to
establish local necessary conditions while a separate finite-deviation argument
establishes sufficiency. Exact rational interval/Sturm checks are permitted for
residual low-dimensional inequalities. Production coefficients and search
outputs are not imported as the independent certificate.

Later comparison with the existing proof/code is reconciliation, not the first
reconstruction. Keep the exposure limitation in the final verdict. Computational
checks, AI-side reasoning, formal proofs and author/external-human verification
must be distinguished.

## Frozen domain and claims

Five constants: `(v,gamma,kappa,rho,phi)=(.01,.14,.02,.32,.14)`;
`eta in [.10,.14]`, `K in [.54,.56]`.
Each initial action is `N` or `O(c_i,a_i)` with `0<=a_i<=c_i<=1`.
The nonempty agenda set and quorum `r=1,2,3` are all considered. Government
continuation is exactly the manuscript's prescribed national-welfare proposal
and YES-on-tie vote selector; unrestricted voting is not asserted.

Audit targets:

1. complete private-terminal pure-SPE characterization;
2. public-terminal pure-SPE zero wasted commonality and welfare invariance;
3. complete initial public equilibrium set under broad agenda and quorum<=2;
4. the private-set fixed-cost inclusion and a strict witness;
5. the welfare maximum over all private SPE and the selection-free institutional
   comparison, including weak/strict boundaries;
6. the firm/home-government preference corollary and its dependencies.

Seven-parameter extension, mixed SPE, unrestricted voting, positive public
implementation expense, patent royalties, transfers, and a global planner's
first best are outside this certificate. Preserve the negative diagnostics and
the earlier manuscript NO-GO.

## Attack plan and stopping rules

- Reconstruct physical Cournot states and compliance/exit active sets from the
  matrix, with development and production participation distinguished.
- Check 0/1/2/3 developers, asymmetric stocks, ties, corners, and entry/withdrawal.
- Attack finite deviations under both private and mandated continuations;
  do not infer a global equilibrium solely from FOCs.
- Compute exact scalar/matrix bounds, independently generated residual sign
  certificates, root enclosures, and rational boundary witnesses.
- Numerically search policy discontinuities and derivative near-boundaries;
  retain solver failures/ambiguous signs and reconcile them analytically rather
  than filtering them as unprofitable.
- Compare the independently reconstructed objects with the existing construction
  only after fixing the main alternative derivation.
- Save the final theorem register, proof audit, independent code/results, frozen
  input hashes, and preliminary formalization target map on this audit branch.

Budget is the adopted Stage30B result family on the unchanged model. A material
counterexample triggers a documented Stage4 rollback, not another model. A proof
gap blocks the affected claim. A complete baseline audit may issue Stage4A GO
while explicitly leaving Stage6, Stage7.5A/formal closeout and submission blocked.
This contract does not precommit to PASS.
