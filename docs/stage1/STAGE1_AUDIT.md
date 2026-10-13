# Stage 1 — Source & Mathematical Audit (2026-10-13)

**Verdict: GO TO NOVELTY GATE (on audited continuation and sharply limited hypotheses only).** Workflow stable v2.9 plus post-v2.9 main refinement, verified workflow main SHA 81c37dd95fc93d918138ba9d0da86541d3cc1067, source template templates/STAGE_01_AUDIT.md.

## 1. What was audited
Independent-stage-0 idea record (local package SHA256 48a1aa355b3fe578100b5d85a920d42f5f1f247f069aca927fc219cb5780dd9b), existing R9 paper/jict_short/short_02_model.tex and short_03_adoption.tex from branch revision/r9-jict-astra-final-polish (read 2026-10-13), and published accessible descriptions of Ray–Vohra (1999), Gallini (2014), Casella (2001), and Fiedler–Larrain–Prüfer (2023). Most parent full proofs NOT inspected; this remains Stage 2 work.

## 2. Canonical players/timing/objectives/contractability
See docs/stage1/CANONICAL_MODEL_MAP.md. Public legal recognition and private implementation-IP authorization are separate, and technology adoption is a third independent action. Governments count local consumers + globally earned profit of domestic firms + public net revenue. Firms count worldwide net operating profit and royalties according to rights ownership. Contractible/verifiable acts and the legal scope of public approval/private exclusion MUST be justified before using any bargaining theorem.

Provisional timing: offer/counteroffer/acceptance/approval and license -> implementation choice -> product-market Cournot. Proposer selection, amendment/deviation order, full bargaining commitment and transfer menu intentionally UNFROZEN. No pure-protocol comparison is certified unless feasible final contracts and welfare are matched.

## 3. Equation-by-equation audit
- Utility quadratic in q: U=a 1'q - q'Mq/2; inverse demand p=a 1-Mq: CORRECT for this independently stated utility.
- Disconnected matrix M0 [[1,gamma],[gamma,1]], linked ML [[1-v,gamma-v],[gamma-v,1-v]]: ASSUMED functional form, internally coherent; no claim of uniquely correct microfoundation.
- 0<=v<=gamma<1: makes ML symmetric positive definite with eigenvalues 1-gamma and 1+gamma-2v; ensures own profit strict concavity for both firms.
- Best-response equation and inverse-matrix Cournot interior solution: CORRECT, exact SymPy FOC/SOC and substitution checks in code/verify_stage1.py.
- Positive quantities: CONDITIONAL only, must test numerator inequalities. Example audited positive interior witness and exit/corner KKT witness.
- Consumer surplus CS=q'Mq/2: CORRECT from integrable quasi-linear utility.
- Firm 1 royalty income +r q2, licensee cost +r q2: CORRECT given actual licensor 1 owns transferable IP and no intermediary/cost.
- World welfare transfers cancellation: CORRECT as identity at fixed q; WRONG to claim royalty is welfare neutral after endogenous Cournot response.
- Two-destination national accounts: exact audited rationals; no public subsidies/fixed costs in diagnostic.
- Old R9 inverse demand as stipulated reduced-form: CORRECT AS STIPULATED; its common-u differentiated brand allocation and direct transplant of CS=Q^2/2 to LQ are AMBIGUOUS/INCORRECT respectively. This new LQ welfare system cannot be described as a continuous welfare nesting of R9.

## 4. Participation, active sets and feasibility
At any contemplated standardization contract, firms, IP holder and both governments have distinct veto/participation conditions. No minimum participation inequalities can be checked until proposer, conditional promises, renegotiation, fixed costs, disagreement payoffs and permitted contracts are specified. A contract that offers approval without private authorization is infeasible for essential-IP implementation. Conversely private consent alone does not guarantee governmental recognition.

Linked two-firm Cournot interior requires 2m(a-c1)>b(a-c2-r) and 2m(a-c2-r)>b(a-c1). Marginal-cost asymmetries and negotiated royalties may trigger q=0. The exact corner witness is retained; aggregate regime comparisons must re-solve entry/exit and possible loss of compatibility rather than extend an interior formula beyond it.

## 5. Inherited-claim classification
| Inherited/source claim | Stage-1 finding |
|---|---|
| R9 fixed public partition -> private adoption -> Cournot competition | CORRECT as declared timing; NOT the sought jointly negotiated six-agent game |
| R9 partial adaptation can shift government SU/IS incentive | NOT INHERITED: old consumer-surplus and public coalition environment differ |
| R9 product-specific p_i=1-Q+g_i from common u | AMBIGUOUS microfoundation of positive multibrand allocation; treat as reduced-form |
| LQ inverse demand, concavity, profits, CS | CORRECT under stated gamma/v domain and active-set tests |
| Uniform royalty shifts firm outputs as differentiated Cournot | CORRECT within interior; gamma=v yields zero rival quantity response |
| Royalties directly destroy real resources | INCORRECT for a pure transfer; indirect allocation loss may occur |
| Public-private bargaining must select different standard | UNVERIFIED HYPOTHESIS, NOT a Stage-1 mathematical finding |
| Adding both negotiations and Cournot guarantees novelty | INCORRECT; strong general predecessor classes |

## 6. Prior-art proximity (depth not overstated)
- Ray & Vohra 1999, 10.1006/game.1998.0648: partition-function extensive-form coalition bargaining and Cournot application; publisher abstract/result checked; full proof pending.
- Gallini 2014, 10.1016/j.ijindorg.2014.02.003: patent pooling + standard choice + substitutable products; publisher introduction/abstract read, full theorem proof pending.
- Casella 2001, 10.1111/1467-6435.00152 / NBER w5853: private standards coalitions; abstract/working-paper summary checked, full proof pending.
- Fiedler, Larrain, Prüfer 2023, 10.1016/j.respol.2023.104761: endogenous standard-setting association participation and governance; journal abstract read, accessible full-text available for Stage 2.

Stage 1 does NOT certify that any author stated an omitted joint-government-firm bargaining model; all proposed remaining gaps are AUDITOR-INFERRED.

## 7. Kill/repair alerts
1. Do not pretend that a new bargaining advantage from relaxing conditional-contract availability is the consequence of bargaining protocol alone.
2. Distinguish changing technology, consumption externalities, the direct demand-shift from compatibility and real cost savings; do not insert signs to force results.
3. Treat an implementation veto as economically/legal meaningful only with actual exclusion right; a seller cannot veto an unpatented substitute as a model tautology.
4. Homogeneous gamma=1 endpoint is singular for LQ utility; no silent continuity of consumer welfare or equilibrium uniqueness.
5. No equilibrium novelty statement on the basis of the two conditional Cournot witnesses.

## 8. Surviving precise research question
Can split public approval rights and private technology-consent rights change which enforceable international standard or mixed national/private coalition forms in a bargaining equilibrium, under identical contract feasible sets, downstream payoffs and admissible transfers?

## 9. Stage-2 novelty-kill contract
Freeze ONLY the Stage-1 audited market payoff mapping, ownership/accounting rules, source-model cautions, target null hypothesis and rights distinctions. Stage 2 must acquire closest full models/propositions (especially Ray–Vohra, Gallini, Maggi–Ossa, Casella, Fiedler et al.); map coalition-bargaining, vertical contracting/patent pooling, regulatory agreements, incomplete contracts; test generic parent theorem absorption; and distinguish real new equilibrium selection from trivial surplus sharing. It may not declare a new theorem or develop a full paper.

## 10. Provenance
All calculations by SymPy computation using code/verify_stage1.py; no independent person or formal prover verified the new theory. Literature notes rely on listed accessible abstracts, not a certified exhaustive survey. This Stage-1 report was materially AI-assisted and needs author review. No novel bargaining theorem has been proved.
