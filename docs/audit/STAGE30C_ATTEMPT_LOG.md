# Stage30C — Failed attempts and scope counterexample ledger

Date: 2026-10-15 JST. These records are retained rather than converted to PASS.

## Certificate implementation attempt

The first exact run completed the four residual sign certificates. After adding
an exact participation-boundary check, the next run exited with
`RuntimeError: UNRESOLVED: denominator mapping`. The boundary function had already
substituted `a=0, eta=7/50`, while its proposed clearing denominator D still
contained these variables. No sign theorem was accepted from that failed run.

The correction substitutes the same values into D. The rerun verifies the
primitive identity before certifying the boundary margin, and completes with
`Saved STAGE30C_EXACT_RESULTS.json 17288 bytes`. This is a certificate-construction
bug, not a counterexample to the economic claim. The source and denominator
mapping are retained for reproduction.

## Numerical failures

Eight of the 180 final finite-deviation searches reached the maximum iteration
count. They remain `UNRESOLVED` searches, with their profiles, firm, institution
and solver message in `STAGE30C_NUMERIC_RESULTS.json`. Their observed returns
are not used as upper bounds or proof of equilibrium. The separate analytic
finite-deviation inequalities cover those histories.

An earlier exploratory three-developer top-government minimization with an
80-iteration budget also did not converge near the known equality corner
`C=t=1` (objective approximately 3.35e-10). It supplied no sign certificate.
The final proof instead differentiates the primitive FOCs and supplies exact
positive margins and the equality case. This preliminary probe is not included
in the final search-count statistic.

## Reproducible scope counterexample

At `eta=.14, K=.55`, all firms initially choose `O(1,0)`, all governments have
agenda rights, and quorum is3. The on-path mandate has all gains exactly zero
and passes under YES-on-tie. Firm0 can withdraw to N. The resulting two-developer
history is private under unanimity; its profit rises by approximately
`.11387255438359944`.

Thus the statement “every zero-commonality initial profile is an SPE” is false
if extended to unanimity. Stage30B restricts this sufficient-and-necessary
initial correspondence to quorum<=2 and at least two proposers. The example
does **not** refute that restricted claim, or public-terminal welfare invariance.
It must be kept as a regression guard against future scope inflation.

The final direct evaluator also records a three-developer private history
`[(1,0),(1,1),(1,1)]` and withdrawals under both a blocked proposer and unanimity.
Depending on the institution, withdrawal switches policy to M or leaves L;
both are explicitly evaluated. These are profitable-deviation demonstrations,
not alleged equilibrium counterexamples.

## Post-checkpoint boundary and reconciliation work

After construction-code comparison, the independent c1 outsider-rejection
certificate was expanded from a∈[.30,.61] to a∈[0,.61] to cover the full
canonical low-commonality family. The same primitive/Horner proof succeeds;
the final exact results file is17,266 bytes. This expansion is recorded rather
than misdated as part of the pre-comparison checkpoint.

Six additional boundary profiles generated18 deviation searches, with1
nonconvergence retained in `STAGE30C_BOUNDARY_RESULTS.json`. Thus the combined
final batches have198 searches and9 numerically UNRESOLVED cases. No boundary
candidate gain exceeded the attack threshold. The failed blanket F_ac sign,
weak y_c boundary, and c1-optimum reuse at c<1 are independently reproduced.
The scope counterexample's positive gain is now an exact rational number.
