# Stage30C — Preliminary formal-verification applicability and target map

Date: 2026-10-15 JST. **FORMALIZATION APPLICABLE. Implementation: PLANNED /
NOT FORMALLY VERIFIED. This is not a formal certificate or Stage7.5A closure.**

The current additional claims involve quantified inequalities, min/max cases,
discontinuous policy selection, indifference boundaries, global best responses
and universal welfare comparison. A small material core would improve assurance;
expense of formalizing the whole six-player model is not a N/A reason.

Workflow source: `FORMAL_VERIFICATION_CHECKLIST.md` and Stage4A/7.5A at
`81c37dd95fc93d918138ba9d0da86541d3cc1067`. Default proposed tool is Lean4/mathlib.
No version/library commit is selected or installed in this task; select and pin
them when implementing. No `sorry`, axiom report or build evidence is claimed
to have been audited in nonexistent formal source.

## Claim-critical target map

| Claim | Analytic component | Proposed formal statement | Initially excluded / supplied hypotheses | Reason and assurance gained |
|---|---|---|---|---|
| C1 / C3 | Mandate selector; relatively open L region; political iff | Finite YES-set/quorum intersection logic and strict-negative neighborhood lemma for continuous Delta | Continuity of primitive payoff maps must be supplied until derived | Certifies tie strictness and all A,r cases; does not certify endogenous voting |
| C1 | `S<=3P`, equality only all O(1,0) | Matrix bound/monotonicity implies aggregate inequality and withdrawal under either continuation | Either formalize A inverse norm bounds or list q,w bounds explicitly and certify their separate derivation | Targets the all-three-developer exclusion; avoids pretending the key bound is automatic |
| C1 | Necessary-and-sufficient private design conditions | Global founder-deviation inequalities, outsider entry envelope, and exhaustive developer-count implication | Cournot primitive correspondence and compliance dominance must be represented or explicitly remain analytic | Certifies full finite-deviation case logic; condition structures alone are not SPE equivalence |
| C1 / C5 | B, T_a, restricted F_ac, c1 veto signs | Rational polynomial nonnegativity/strict positivity on exact boxes, primitive denominator identities | SymPy output is not an axiom; polynomial identities and positivity witnesses must be accepted by kernel-checkable proofs | Certifies the residual signs and their mapping, not merely imported JSON |
| C2 / C3 | Zero wasted a, all public value; top-country approval | Withdrawal inequality plus expense identity; zero-effective-a approval for all capacities | Demand differentiation may be formalized later; supplied monotonicity hypotheses must be named | Targets invariance and broad-agenda sufficiency, including equality cases |
| C4 | K affects only K>V | Set inclusion theorem and exact rational strict witness | Equivalence to economic SPE depends on C1 formal coverage | Small core checks cancellation, strict boundary and existence, not selected investment monotonicity |
| C5 | a* unique; every stable a<=a*; attained maximum | Existence/uniqueness under strict concavity, restricted F_ac root comparison, monotone T maximum | Actual derivative signs supplied only if not separately formalized; do not silently assume the conclusion a<=a* | Checks canonical design as maximum of the complete stable set, not an arbitrary selected candidate |
| C6 | Every-new/every-old comparison iff K<=K_W | Welfare-set logic with public invariance, attained private maximum and inferior witness | Hypotheses identifying the economic equilibrium sets must be explicit and tied to C1–C5 | Certifies universal vs existential quantifiers, weak cutoff, infimum/supremum consequences |
| C7 | Weak firm preference; strict government gain | Exact accounting identities plus F>=P/B>0/V<K implications | Primitive costs/gross welfare maps explicit; preference uniqueness not assumed | Checks weak/strict consistency and same-history versus ex-ante accounts |
| Scope regressions | All-O1a0 under unanimity; negative F_ac | Exact rational encoded-profile counterexamples | Primitive payoff and policy mapping must be checked, not replaced by the desired counterexample assertion | Prevents future accidental extension of C3 or derivative sign |

## Minimum meaningful core and statement-fidelity rules

Start with the all-developer case/deviation implications and C6 universal
welfare-set logic, plus the proof-critical scalar/polynomial inequalities
they use. The analytic alternative derivation is the candidate statement source.
Do not prioritize decorative algebra while assuming away the three-developer
or policy-switch step. A staged core is acceptable if every supplied hypothesis
has an explicit independently checked analytic bridge.

Map each actual formal theorem to C1–C7 and state exact domains, quantifiers,
strict/weak boundaries and which hypotheses the kernel derives. If a formal
theorem takes `S<=3P` or the equilibrium correspondence as an assumption, it
does not certify that economic component. If it encodes R as a condition
structure, it does not prove R iff SPE unless that bridge is formalized.

The economic model's demand branches, national objective, proposal/vote rule,
compliance/exit subgame, and continuous initial strategy domain remain outside
formal verification until explicitly represented. No formal theorem should be
described as certifying unrestricted voting, mixed SPE, seven-parameter
robustness, novelty, realism or author accountability.

Before Stage7.5A closes, retain actual source, toolchain/mathlib lock, clean
build, theorem signatures, paper/domain correspondence, imported-hypothesis
list, `sorry`/`admit`/axiom audit and model-boundary certificate. Formal acceptance
and statement fidelity are separate checks. False mathematics or a missing
condition reopens Stage4/4A; a source/build issue alone returns to the formal
gate. Any material claim change invalidates the corresponding certificate.

Author intellectual-contribution records and economic portability attacks are
also still pending. AI reasoning and future Lean success are not author or
external-human verification. At Stage4A this preliminary map satisfies the
applicability obligation; it does not satisfy the pre-freeze Formal Verification
Gate. The next authorized step remains Stage6.
