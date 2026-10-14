# Stage 30 — Audit package

**Final verdict: NO-GO for the present full paper. Stage31 is blocked.**

The central baseline mathematics survives independent reconstruction under the
specified government policy selector. The full manuscript receives CONDITIONAL
PASS on mathematical assurance. Economic significance does not support the
current full-paper scale. A bounded diagnostic Research Note is the suggested
route; publication and final literature priority remain unconfirmed.

## Reports

- [Editor decision](STAGE30_EDITOR_DECISION.md)
- [Independent mathematical audit](STAGE30_INDEPENDENT_MATH_AUDIT.md)
- [Economic significance and seven scores](STAGE30_ECONOMIC_SIGNIFICANCE_AUDIT.md)
- [Theorem absorption and source-access limits](STAGE30_PRIOR_ART_THEOREM_ABSORPTION.md)
- [Anonymous-style hostile referee report](STAGE30_HOSTILE_REFEREE_REPORT.md)
- [Revision priorities and stop rule](STAGE30_REVISION_PRIORITY.md)
- [Eleven original/replacement paragraphs](STAGE30_EXPOSITION_REVISIONS.md)

## Evidence and reproduction

Baseline: Stage29 PR #57, commit
`2e96112280599cceaee43b89e265fcb5c073f1ca`.
Workflow: `research-paper-workflow` v2.9, commit
`81c37dd95fc93d918138ba9d0da86541d3cc1067`.

```bash
python -m pip install -r code/stage30_requirements.txt
python code/stage30_independent_exact_audit.py
python code/stage30_independent_game_audit.py
python code/stage30_audit_manifest_check.py
```

The independent implementations import no Stage11–27 research module. Their
first construction preceded production-code exposure; manuscript appendices
were visible. This is not a blind audit or an external human referee certificate.

- Exact evidence: 43 rational sign certificates, 10,023 Bernstein coefficients,
  matrix-derived policy numerators, root brackets and welfare identities.
- Search evidence: 27 regional candidates, all feasible-action grids and selected
  continuous optimizations, 6,000 asymmetric histories. Search is not a proof of
  global equilibrium absence.
- Diagnostics: public implementation cost and unrestricted simultaneous voting
  each defeat portability of the claimed baseline classification. They are
  changes of institution, not hidden counterexamples to the stated reduced game.
- Literature: final published Gandal–Shy and Klimenko theorem corpora remain
  UNRESOLVED. Earlier versions and abstracts are not novelty certificates.
- Seven-parameter certificate: author-code reproduction PASS, full independent
  reconstruction NOT INDEPENDENTLY VERIFIED.
- Formal proof: no Lean/Coq/Isabelle PASS is claimed.

The manifest checks that all pre-Stage30 files are unchanged. Proposed paragraph
edits are review material; none is applied to the original manuscript. No merge,
publication or submission was performed. A passing evidence CI does not change
the editorial NO-GO verdict.
