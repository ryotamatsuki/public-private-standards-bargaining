# Stage30C — Reproduction and handoff

The Stage4A decision concerns the exact C1–C7 baseline claims in the claim
register. The alternative derivation fixes the proof before production-code
comparison. The contract and audit disclose prior exposure. No code from
Stage30/30B is imported by the independent modules; post-checkpoint reconciliation
only compares formulas and previously stored rational results.

From the repository root, Python3.12:

```bash
python -m pip install -r code/stage30c_requirements.txt
python code/stage30c_independent_exact.py
python code/stage30c_independent_numeric.py
python code/stage30c_independent_boundary.py
python code/stage30c_reconcile.py
python code/stage30c_evidence_check.py
```

Pins: SymPy1.14.0, NumPy2.3.5, SciPy1.17.0. Exact results contain source hashes;
the frozen-input manifest also preserves all239 parent files and independent
source hashes. The CI target regenerates the evidence. Numeric last bits or
optimizer convergence can differ across platforms; they are not mathematical
certificates. No nonconverged search is counted as an upper bound.

| Artifact | Purpose / assurance boundary |
|---|---|
| `STAGE30C_CLAIM_REGISTER.md` | Exact claims, dependencies, quantifiers, per-claim theorem certificates and prose limits |
| `STAGE30C_INDEPENDENT_MATH_AUDIT.md` | Mathematical verdict and continuation/global-deviation/selection audit |
| `STAGE30C_PRIMITIVES_FIRST_DERIVATION.md` | Matrix/envelope/continuity proof fixed before construction reconciliation |
| `STAGE30C_INDEPENDENT_AUDIT_CONTRACT.md` | Scope, exposure and independent path |
| `STAGE30C_ATTEMPT_LOG.md` | Failures and scope counterexample preserved |
| `STAGE30C_FORMALIZATION_TARGET_MAP.md` | APPLICABLE; implementation PLANNED; no formal PASS |
| `stage30c_independent_symbols.py` | Fresh bilateral quantities/CS/profits/derivatives from primitive FOCs |
| `stage30c_independent_exact.py` + exact JSON | Exact scalar bounds, rational polynomial minimum-face proofs, Sturm and root bracket |
| `stage30c_independent_numeric.py` + numeric JSON | Separate full-game direct-market evaluator and180 finite-deviation attacks |
| `stage30c_independent_boundary.py` + boundary JSON | Exact scope counterexample, rejected simplifications and18 boundary attacks |
| `stage30c_reconcile.py` + reconciliation JSON | Post-checkpoint identity/rational-value comparison; no production solver call |
| `stage30c_evidence_check.py` + frozen JSON | Preservation, provenance and solver-failure semantics; not a theorem prover |

The main numerical batch retained8 nonconverged searches, the boundary batch1.
The total198 searches found no gain above1e-7 at proposed equilibria; those
numbers do not prove the quantified claims. The separate analytic and exact
arguments do. The unanimity scope counterexample has strictly positive gain,
as expected, and is not included among proposed-equilibrium no-deviation tests.

The independently derived three-developer aggregate bound replaces, rather than
reruns, the production large Bernstein case proof. Residual exact signs use
four rational minimum-face certificates, each one leaf. A full proof-assistant
kernel acceptance is **NOT IMPLEMENTED**. The evidence must not be represented
as human/author certification.

Handoff is C1–C7 to Stage6, with their exact scope, prior negative diagnostic
models, and theorem-absorption uncertainties. No revised manuscript, new model,
submission, merge, new Stage6 PASS or Stage7.5A closure is part of this branch.
The preserved Stage30 NO-GO concerns the old manuscript's economic/editorial
value; the present mathematical PASS does not contradict that judgment.
