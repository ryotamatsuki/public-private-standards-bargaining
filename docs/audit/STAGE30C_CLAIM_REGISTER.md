# Stage30C — Claim, dependency and theorem-certificate register

Date: 2026-10-15 JST. Frozen construction input: PR59,
`0735322e85dd876c5d361e6ddeaa6a4d79a9bbeb`.
Workflow input: `81c37dd95fc93d918138ba9d0da86541d3cc1067`.

**Mathematical state: all seven claims below PASS on the specified baseline.
Novelty, portability, author verification and formal verification are separate
unclosed states.** This register implements the theorem-certification checklist;
the common certificate fields below apply to every row, not just the first.

## Common scope, primitives and verification actors

Every quantifier below ranges over the unchanged manuscript model:
`(v,gamma,kappa,rho,phi)=(.01,.14,.02,.32,.14)`,
`eta∈[.10,.14]`, `K∈[.54,.56]`, three firms and three governments,
independent initial choices `N` or `O(c_i,a_i)`, `0<=a_i<=c_i<=1`.
Every nonempty agenda A and quorum r1/2/3 is covered where expressly indicated.
Cournot competition uses the given pair-minimum demand branches. Governments
use the **prescribed national-welfare motion/vote selector, including YES-on-tie**.
All firms comply following M; N is nondevelopment, not production exit.

The economic assumptions actually used are the preexisting costless public
interface, open technology without royalties/transfers, completion cost
`phi(1-c_i^2)/2` without a second K, national firm profit plus domestic CS,
equal national markets, and the two-/three-developer technology distinction.
The linear demand, quadratic expenditure, bounded triangle and numeric
rectangle supply the matrix, concavity and sign bounds. None is silently
upgraded to a general function class or endogenous voting game.

Verification actors: `AI` analytic derivation and `COMPUTATION` independent
symbolic/rational/numerical checks. `AUTHOR`, `EXTERNAL HUMAN` and `FORMAL`
verification have not occurred in this task. The assistant previously helped
construct Stage30B. Independence rests on a separate proof path and evaluator,
with a checkpoint before rereading production code; it is not blind review.
See [contract](STAGE30C_INDEPENDENT_AUDIT_CONTRACT.md) and
[audit](STAGE30C_INDEPENDENT_MATH_AUDIT.md).

Definitions: x,y are the primitive bilateral Cournot quantities, CS the
single-market consumer surplus; `P=pi_I^g-phi/2`, `W_I=pi_I^g+CS_I-phi/2`.
`F=3mx²-phi(c²+a²)/2`,
`B=pi_I^g+CS_I-3mx²-CS-phi(1-c²)/2`,
`V=W_I-3my²-CS`, `T=2F+3my²+3CS`.
`R(eta,K)={(c,a):0<=a<=c<=1, F_a>=0,F>=P,K>V}`.
Let a*(eta) be the unique root `F_a(1,a;eta)=0` in `(.30,.61)`.

## Adopted claim and dependency table

| ID | Exact result and quantifiers | Dependency | Proposed use | State |
|---|---|---|---|---|
| C1 | All private-terminal pure SPE, iff: up to relabeling `O(c,a),O(c,a),N`, `(c,a)∈R`; r3 with any A, or r1/2 with A consisting solely of the outsider | Primitive continuity/compliance; three-developer aggregate bound; complete finite deviations | Main equilibrium proposition | PROVED / PASS |
| C2 | Every public-terminal pure SPE under any constitution has all initial developers' `a_i=0`; all yield profits `P-K`, national welfare `W_I-K`, world welfare `3(W_I-K)` | Primitive costs; outsider lower bound | Main welfare bridge | PROVED / PASS |
| C3 | If r<=2 and |A|>=2, the complete initial pure-SPE correspondence is all profiles with entries `N` or `O(c_i,0)`, all ending in M | C1–C2; zero-effective-a top-country approval; on/off-path selector | Main institutional corollary | PROVED / PASS |
| C4 | For fixed eta and fixed private-admitting constitution, K1<K2 in the box implies `R(eta,K1)⊆R(eta,K2)`; strict inclusion exists, not necessarily for every pair K1,K2 | C1; uniform entry deterrence | Supporting comparative static | PROVED / PASS |
| C5 | For every private-admitting constitution and every eta,K in the box, the maximum private-SPE world welfare is `T(1,a*)-2K`, attained uniquely in (c,a) at `(1,a*)` | C1; T_c,T_a>0; restricted F_ac>0; root and feasibility | Main welfare proposition | PROVED / PASS |
| C6 | From any old private-admitting constitution to any new r<=2, |A|>=2 constitution: every new SPE weakly beats every old SPE iff `K<=K_W=3W_I-T(1,a*)`; above this cutoff reform improves the welfare infimum and lowers the supremum | C2–C5; feasible low-welfare private witness; public existence | Main institutional welfare result | PROVED / PASS |
| C7 | At every private SPE, founders weakly oppose M in firm profits while their governments strictly favor it; outsider government strictly opposes; founder-country ex-ante public-minus-private gap is `B+phi a²/2>0` | C1; B>0; primitive accounting | Mechanism corollary | PROVED / PASS |

## Per-claim certificates

### C1 — Complete private correspondence

Type: necessary-and-sufficient equilibrium characterization; global over the
entire stated continuous strategy triangle, not just the canonical design.
Multiplicity: a continuum, with either outsider label; no uniqueness assertion.
Proof: [alternative derivation §§1–4](STAGE30C_PRIMITIVES_FIRST_DERIVATION.md).

Candidate-deviation audit: arbitrary founder O deviations under both L and M,
withdrawal to N, all legal outsider entries including O(0,0), and every induced
government/compliance/Cournot continuation. `F_c>0`, `F_aa<0`, `F_a>=0` give a
finite comparison, not merely local FOCs. Alternative-equilibrium audit: sparse
L impossible; asymmetric pairs contain a redundancy-saving deviation; every
three-developer L candidate has a strictly profitable withdrawal, independently
of whether its continuation is M or L. The aggregate proof covers all order
and minimum ties, without importing Stage19/21 institutional conclusions.

Indifference audit: `F=P` is retained, `F_a=0` is retained, and `K=V` is excluded
because the outsider votes YES. Exact voting knife-edge and rational root
enclosures are stored; boundary representative attacks recompute continuation
after an indifferent withdrawal. Strict NO gains make the L region relatively
open and justify the local necessity argument even at other governments' ties.

Evidence: exact matrix/envelope bounds and founder sign certificate in
`STAGE30C_EXACT_RESULTS.json`; 48 private profiles, 144 finite-deviation searches
and all 21 constitution selectors in `STAGE30C_NUMERIC_RESULTS.json`; boundary
attacks in `STAGE30C_BOUNDARY_RESULTS.json`. Search nonconvergence remains
UNRESOLVED numerically; the exact analytic proof covers those cases.
Limitation: prescribed selector, pure SPE, baseline only.

### C2 — Public welfare invariance

Type: implication for **all** public-terminal pure SPE under every A,r; not a
complete initial correspondence under narrow agenda or unanimity.
Proof: alternative derivation §5. A developer with positive a can withdraw and
save its wasted expenditure if M persists, or obtain more as an outsider if L
results. This excludes every positive-a public candidate, including asymmetric
and three-developer profiles. No assumption of a retained public continuation
is used in the withdrawal proof. All remaining total expenses are K+phi/2.

Indifference/multiplicity audit: the continuum of zero-a c choices changes
initial expenditure/completion but not total public cost; downstream demand is
unchanged. This is payoff and welfare invariance, not action uniqueness.
An all-N public SPE exists for every constitution: every unilateral open
deviation leaves a sparse history, M follows, and cannot raise profit.
No off-path exit or zero-output branch is untested: §1 strictly excludes it.

Evidence: scalar outsider/public profit gap `.103872554...`, compliance margin
`421/3300`, exact cost/preference identities and direct market checks.
Limitation: initial public vectors under r3/narrow agenda are not enumerated,
which is unnecessary for this all-public welfare implication or C6.

### C3 — Broad-agenda initial correspondence

Type: iff on r<=2, |A|>=2; exact initial **set**, terminal outcome invariant.
Proof: §§4–5. At zero effective commonality the two highest-capacity countries
weakly support M, including all-O(1,0) ties. This statement is proved for all
asymmetric capacities by direct FOC differentiation. A unilateral positive-a
choice against zero-a rivals leaves every pair minimum at zero, so the same
approval proof covers every deviating history. Initial O(0,0) and N remain
distinct admissible actions and both are included.

Candidate and alternative audits: C1 removes all private possibilities, C2
removes positive-a public possibilities, and the direct policy proof supplies
sufficiency for every remaining initial profile, not only sampled profiles.
Evidence: exact positive derivative margins; 348 broad/sparse policy checks,
12 public profiles and 36 deviation searches in the main numerical file.

Scope falsification: all-O(1,0) is not an SPE under unanimity; withdrawal earns
`15291216325919/134283598086400>0`. The exact counterexample is retained in the
boundary JSON. It does not falsify the restricted iff. Do not extend C3 to all
constitutions or describe a unique initial equilibrium.

### C4 — Fixed-cost set expansion

Type: weak set inclusion for all K1<K2 in the box, with one strict witness.
Proof: §6 and C1. The only K-dependent condition is the outsider's strict
political inequality. Fixed cost cancels from founders' participation against
the mandated N fallback; entry deterrence is certified uniformly over the box.

Finite-deviation/globality follows from C1 rather than rechecking only the
old optimal design. Indifference audit: at `c=.929,a=0,eta=.14`, the exact
threshold is `52901114096583344443/97940845851620800000`≈`.540133318603`;
the threshold itself mandates under YES-on-tie. The design belongs at K=.55
and does not belong at K=.54. Evidence: rational witnesses and exact voter tie.
No prediction of monotone selected c/a, profits, or average welfare is certified.

### C5 — Maximum among all private equilibria

Type: attained global maximum over R, unique **design** up to firm relabeling;
not a planner's first best. The objective is `T(c,a)-2K`; the feasible set is
the complete privately stable set R, not all technologically possible states.

Proof: §6. Uniform `T_c>0,T_a>0` and the bound `a<=a*(eta)` establish the maximum.
The bound uses `F_ac>0` only on a∈[.30,.61], not at zero commonality. Root
existence/uniqueness follows from Sturm, a=.61 negative margin and strict
concavity. Canonical participation and outsider rejection are separately
verified, now with the latter on the full c1,a∈[0,.61] enclosure. Hence the
maximum is feasible throughout the K rectangle, not merely a formal upper bound.

Alternative and boundary audit: all other private designs covered by C1 are
dominated in world welfare; uniqueness of a design is not uniqueness of SPE.
An exact negative F_ac witness at c1,a0 is kept. At c=.95, using the c1 a-root
incorrectly produces a profitable finite reduction, retained in boundary JSON.
Evidence: four independent residual certificates, scalar T_c margin, root
enclosure, and explicit false-simplification regressions. Same population and
full initial cost accounts as C2; no selected equilibrium is fixed for the proof.

### C6 — Selection-free institutional welfare comparison

Type: necessary and sufficient universal weak welfare comparison, with exact
weak/strict boundaries; also infimum/supremum comparison on the full old set.
Proof: §6 with C2/C5. The new public value is unique, every old public value
equals it, and the old private maximum is attained. The c1,a0 private witness
exists throughout the box and lies below the public value. At K=K_W the best
private outcome ties; old public outcomes always tie. Above it, old private
outcomes exist on both sides of public welfare.

Benchmarks: ex-ante equilibrium world welfare for different constitutions,
all three firms and national markets, including full development expenses.
The old feasible set is all its pure SPE; selections may vary. No first-best,
expected welfare, national Pareto gain or mandatory-retrofit comparison is used.
From unanimity the change includes relaxing quorum; adding agenda rights while
retaining unanimity does not invoke C3 or remove private SPE.

Evidence: exact same-parameter designs c1,a0 versus c1,a.5 at eta .14,K .55
have private-minus-public gaps `-.106147364...` and `+.048787911...`.
These are actual SPE under sole-outsider agenda r2 and under unanimity.
No closed-form minimum design is claimed or needed for the strict infimum gap.

### C7 — Firm/home-government misalignment

Type: corollary holding at **every** private SPE; weak firm preference, strict
government preferences. Same-history firm mandate-minus-private profit is
`P-F-phi a²/2<=0`, founders' policy gain is B>0, outsider gain V-K<0.
Pre-investment founder-country public-minus-private welfare is B+phi a²/2>0.

Proof: C1 and independently checked accounting. Indifference is economically
admissible: at a0 and F=P a founder is indifferent although its government
strictly favors M; do not replace the weak firm inequality with “strictly
opposes everywhere.” The participation root and its strict outsider rejection
are certified exactly. Boundary withdrawal recomputes the new public history.
This is not a reversal of the same government's ex-ante/ex-post preference.
Evidence: exact preference identities and boundary files.
Novelty of profit/CS misalignment by itself remains unestablished.

## Checklist coverage and manuscript wording control

| Checklist field | Evidence-linked completion for all claims |
|---|---|
| Identity/quantifiers/assumptions | Common scope plus exact claim row and per-claim certificate |
| D1 global deviations | Derivation §§2–5; independent primitive evaluator; no FOC-only sufficiency |
| D2 alternatives/multiplicity | Exhaustive developer-count exclusion and pair correspondence; public welfare implication plus broad-agenda full initial set |
| D3 indifference/actions | Exact K=V voter tie; algebraic F=P withdrawal; F_a=0 roots; arbitrary public zero-a actions; unanimity scope regression |
| Selection rule | Original prescribed selector expressly retained; unrestricted voting excluded |
| Independent reconstruction | Contract, checkpoint db6f75d, no production imports/calls; post-checkpoint reconciliation |
| Counterexamples/solver failures | Attempt ledger and both numerical JSON files; absence of sampled attacks never treated as proof |
| Generality | Baseline / institution-specific; no new seven-parameter or nonquadratic claim |
| Benchmark/welfare selection | C5–C6 exact objective, feasible equilibrium set, accounts and universal quantifiers |
| Evidence maturity | PROVED analytically/computer-assisted; formal proof PLANNED; no author/external-human PASS |
| Manuscript use | Future equilibrium/mechanism/institution/welfare sections; Stage29 source unmodified |

Maximum defensible abstract/contribution wording is the baseline political
fallback discipline of the complete private investment set and the resulting
selection-free institutional welfare cutoff. Abstract, introduction, policy
and robustness wording must preserve the government rule, baseline domain,
pure strategies and ex-ante comparison. Prohibited strengthening includes
unrestricted six-player SPE, generic demand/investment technology, full
seven-parameter additional results, unique investment equilibrium, strict
founder opposition at every private SPE, or globally optimal standard/policy.

Every claim's formal applicability is `APPLICABLE`; implementation is
`PLANNED — NOT FORMALLY VERIFIED`. See the target map. This does not block
Stage4A routing to Stage6 under the workflow, but does block pre-freeze closure
at Stage7.5A. The old manuscript NO-GO and Stage31 stop remain in force.
