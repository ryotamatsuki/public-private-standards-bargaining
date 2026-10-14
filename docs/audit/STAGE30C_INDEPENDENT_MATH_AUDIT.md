# Stage30C — Independent mathematical adversarial certification of added results

Date: 2026-10-15 JST. Project Stage30C corresponds to workflow Stage4A,
not a replacement for the old Stage30 final referee report.

**Verdict: GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS for C1–C7 on the
baseline and prescribed government continuation. Route next to Stage6.**
No material counterexample or outstanding mathematical gap was found for those
exact claims. This is not novelty/editorial approval, a seven-parameter PASS,
a proof-assistant certificate, author verification or permission to submit.
The Stage29 manuscript remains unchanged and its Stage30 NO-GO remains recorded.

## 1. Inputs, reviewer exposure and distinct audit path

Construction input is PR59 head `0735322e85dd876c5d361e6ddeaa6a4d79a9bbeb`.
The unchanged manuscript contains the canonical primitives, with additional
claims in `STAGE30B_RESULTS_AND_PROOFS.md`. Workflow main was checked at
`81c37dd95fc93d918138ba9d0da86541d3cc1067`, including Stage4A,
`THEOREM_CERTIFICATION_CHECKLIST.md` and `FORMAL_VERIFICATION_CHECKLIST.md`.
The claim register implements the former; the formal target map implements
the required preliminary applicability part of the latter.

The same assistant previously constructed Stage30B, so this is **not blind
review or external-human verification**. First-pass exposure to claims and
earlier proof arguments is disclosed in the audit contract. During this pass,
the manuscript primitives were read first; new derivation and evaluator files
were fixed before rereading Stage30B production code. Checkpoint commit
`db6f75d66d7f66f37fa8d8c21611519781880da3` preserves that order.

The substantive differences are: a matrix-norm/aggregate-profit argument for
all three-developer profiles, rather than the production aligned/crossed
Bernstein case expansion; a general no-mandate openness lemma; a new entrant
envelope depending on the entrant's own capacity; rational interval-Horner and
derivative-minimum-face proofs rather than Bernstein conversion; and an
independent NumPy/Fraction full-market evaluator, with matrix differentiation
and explicit policy changes. No Stage30/30B solver or coefficients are imported.
Post-checkpoint reconciliation reads their statements and rational outputs but
does not call their solver. Later boundary regressions and the expanded c1
veto enclosure are explicitly post-checkpoint additions to the independent code.

`AI` supplies analytic reasoning; `COMPUTATION` checks exact and numerical
objects. Neither `AUTHOR`, `EXTERNAL HUMAN` nor `FORMAL` verification is claimed.

## 2. Reconstruction of continuations from primitives

The primitive demand system is `Aq=z`, `A=H+mI`. All legal private histories
satisfy `0<=H_ij<=.16`, `1<=z_i<=1.32`, `m=.99`. Strict diagonal dominance makes
H and A positive definite. A Neumann estimate first proves positive quantities;
positive off-diagonals then sharpen them to `118/297<=q_i<=2/3`.
The constrained Cournot potential is strictly convex and has this positive
solution, excluding another zero-output active set or production exit under L.

Under M, all compliance/exit subsets are evaluated separately. A lone adopter
uses intercept1; it does not receive the full common-interface intercept.
The minimum gross adoption return `25/33` exceeds the maximum incremental
cost `.56+.07` by `421/3300`. Compliance is strictly dominant at every history,
and the public quantities/CS therefore come from three adopters. Initial N
continues producing under L; initial O(0,0) is development and incurs K.
Entering as O(0,0) also changes the three-developer demand branch; this jump is
explicitly checked rather than treating it as N.

National gains compare **the same sunk history** and subtract only completion
expense when the mandate is contemplated. The original selector is

`M iff #{i:Delta_i>=0}>=r and A intersects {i:Delta_i>=0}`.

This is the prescribed sincere/weakly welfare-improving proposal/vote
continuation. It is not the unrestricted simultaneous voting game. The prior
Stage30 all-NO voting diagnosis remains relevant, not overridden by this PASS.
The selector is evaluated at all changed histories, including nonproposal
outcomes, government indifference and withdrawal-triggered mandates.

## 3. Exhaustive private-equilibrium attack

| History/case | Independent argument | Outcome |
|---|---|---|
| Zero/one developer | Exact smallest sparse national gain `.0980033087...>0` | Every constitution mandates; no private SPE |
| Two asymmetric developers | Trim redundant stocks to pair minima; preserve market outcomes and weakly reduce own mandate gain | Strict expenditure saving while retaining L; excluded |
| Two symmetric developers | L is relatively open under YES-on-tie; withdrawal implies F>=P; concavity implies F_a>=0 and a<.61 | Necessary design inequalities |
| Three developers, all orders/ties | Primitive matrix monotonicity proves aggregate pre-K return <=3P, equality only all O(1,0) | Below equality some firm profits strictly from withdrawal under either policy; equality mandates |
| Symmetric pair founder finite deviation | Effective stocks cannot exceed partner's; F_c>0 and concavity with F_a>=0 bound every L deviation; F>=P bounds every M/N deviation | Global sufficiency, including policy jumps |
| Outsider N→O | New private entrant net return <=.511484629; old outsider profit >=.525227784; public entry payoff smaller still | All legal finite entry excluded |
| Government ties | NO gains strictly negative at L; old NO remain NO locally, new YES set cannot expand | Local necessity valid at ties/kinks |

The strong three-developer bound uses `w=A^-1 q` and its positive lower bound
`331300/2440449`. With all commonality removed as a bounding operation, trim
the unused highest capacity and write `(C,C,t)`. Aggregate return increases
in C and t by lower margins `48497/205425` and `48497/410850` respectively.
This proves the full bound without assuming firms unilaterally coordinate
commonality reductions. The profitable withdrawal is a genuine unilateral
deviation. Its continuation is checked as either M or L.

Consequently the complete private-terminal pure correspondence is exactly C1:
`O(c,a),O(c,a),N` with `F_a>=0,F>=P,K>V`, under unanimity or sole-outsider agenda
with quorum1/2. Both founder governments have B>0 throughout its enclosure.
The strict `K>V` is indispensable; with an outsider YES all governments support
M and every nonempty agenda/quorum enacts it.

This derivation does not transport Stage19/21 no-deviation inequalities across
constitutions. It supplies a new continuation-independent three-developer
bound and checks the bilateral deviations for all current institutions.

## 4. Public multiplicity and indifference

A public candidate with any positive initial a is defeated by that developer's
withdrawal. It either saves waste under M or receives the strictly higher
outsider return under L. Thus all public SPE have zero a and total expenses
K+phi/2, with common world value `3(W_I-K)`. Initial stocks may be arbitrary;
this is welfare invariance, not uniqueness of initial actions.

For r<=2 and |A|>=2, every zero-effective-a history has two weakly favorable
governments. The full asymmetric three-developer case is proved by differentiating
the top countries' gross welfare in the lowest capacity t. Both derivative
terms are positive, with exact margins; the smallest mandate gain occurs at
t=C. Symmetric national return net of capacity expense increases strictly
toward the public interface. Increasing the highest capacity above C only
raises its own mandate gain. Hence two top countries approve, even at ties.
Every unilateral positive-a deviation against zero-a rivals has zero pair
minimum a and is covered by this proof. C3 is therefore a full initial
correspondence under its stated institution.

At the algebraic participation boundary F(c,0)=P (`c≈.92832`, K=.55), a founder
is indifferent to N withdrawal. Recomputing gives a public sparse history.
At that history, any entrant's effective pair capacity is capped by c and its
commonality by0; F_c>0 limits its private return to P-K. Other deviations mandate
or leave a sparse history. The changed public profile is also stable in the
checked eligible institutions. Boundary searches verify the approximate root
representatives, but the weak inequality is supported by this exact argument.

At K=V, the exact Fraction evaluator recomputes all 21 selectors and always
obtains M. Just above this threshold a sole-outsider agenda instead returns L.
Canonical F_a=0 roots and c/stock ties are retained, not excluded by tolerance.

## 5. Welfare, benchmarks and comparative statics

For private profiles, all initial expense is included in `W_R=T-2K`.
The primitive identity `T=3(q'z+m q'q)/2-phi(c²+a²)` and `w>0` prove T_c>0.
An independent exact certificate gives T_a>0 on the necessary low-a enclosure.
Sturm and strict concavity isolate a*(eta) in (.30,.61). F_ac is positive only
on the restricted a>=.30 enclosure needed to prove that every private-SPE a
is <=a*. Canonical F>P and outsider rejection are separately certified.
Therefore C5 is an **attained maximum over all private pure SPE**, not a
canonical-path substitution or unrestricted social optimum.

All new broad-agenda/quorum<=2 equilibria have the same public world value;
all old public equilibria have that value; the old private maximum is C5.
This proves C6's iff `K<=K_W`. At equality only weak comparison holds. Above
it the low-a private witness and the best private equilibrium lie on opposite
sides of public welfare. Reform improves the old infimum while lowering its
supremum; no equilibrium probabilities or selected/expected welfare are used.
The comparison is **ex ante between constitutions**. It is not retrofit welfare
after sunk investment, national Pareto improvement or first-best policy.

C4's fixed-cost inclusion follows from the full private correspondence, not
an old optimum being substituted into a new K game. All founder conditions
cancel K; the outsider political constraint alone weakens. Uniform entry
deterrence survives throughout the box. The exact c=.929 witness proves strict
inclusion for K=.54 versus .55, not for every two costs.

C7 uses `Delta_profit=P-F-phi a²/2<=0`, B>0 and V-K<0. Firms need only weakly
oppose the mandate; F=P,a0 is an admissible indifference boundary. The
founder-country ex-ante public advantage is `B+phi a²/2>0`. A firm/home-government
misalignment is not an ex-ante/ex-post reversal by the same government.

## 6. Exact computational certificate and direct evaluator

The four residual signs are B>0, T_a>0, restricted F_ac>0, and K_min-V>0 at
c1. Each primitive expression is independently reconstructed, cleared by a
positive power of `D>=20693/5000>0`, and checked identically against that
polynomial. Rational Horner ranges plus derivative-certified minimum faces
prove its sign on the closed box. Each final proof uses one leaf and no dyadic
subdivision; the stored face directions and bound are rechecked. Their exact
unscaled function signs, not a grid, support the proof. No scaled coefficient
lower bound is mislabeled a sharp economic margin.

Root signs use univariate Sturm, with denominator correspondence checked;
the weak F=P participation boundary is isolated by42 rational bisections and
its outsider rejection proved over the bracket. Scalar matrix, compliance,
entry, concavity and capacity margins use rational arithmetic.

The direct evaluator independently solves the 3×3 market and uses custom
Fraction Gaussian elimination for ambiguous policy signs. Main evidence:
1,000 random profiles across all developer patterns, 36 compliance comparisons,
348 broad/sparse selectors, 48 private and12 public profiles, 180 finite
deviation searches, 300 three-developer aggregate checks. Added boundary
evidence:6 profiles and18 more searches. Maximum observed candidate gains are
1.11e-16 (main) and2.22e-16 (boundary), below the 1e-7 attack trigger.

**Nine searches remain numerically UNRESOLVED**:8 main and1 boundary hit their
iteration limit. They are saved with solver messages and profiles and are not
accepted as global upper bounds. Analytic finite-deviation proofs resolve the
corresponding economic claims independently of their search status. A failed
denominator-mapping implementation attempt and a preliminary nonconverged
sign probe also remain in the attempt log.

## 7. Reconciliation and negative results

After checkpoint db6f75d, seven symbolic objects match the construction
definitions identically; four shared rational profiles match every participation,
policy, derivative and welfare quantity exactly. The construction entrant bound
is tighter (.505358651 versus the independent .511484629); both lie strictly
below outsider profit and are valid different sufficient bounds. No Stage30B
solver is rerun as independent evidence.

The following failed strengthenings are reproducibly preserved:

1. **C3 extended to unanimity:** all-O(1,0), eta=.14,K=.55, Aall,r3 mandates
   at exact ties; firm0→N leaves L and raises profit by
   `15291216325919/134283598086400=.11387255438...`.
2. **Blanket F_ac>0:** negative at c1,a0,eta .10. The C5 proof needs only the
   separately certified a>=.30 sign.
3. **Reuse c1 optimum at c<1:** at c=.95,eta=.14, the c1 root≈.594951509
   has F_a≈-.000603071. Reducing to≈.588887834 keeps L and gains≈1.82854e-6.
4. **Strict y_c<0 everywhere:** it is0 at eta .14,a1,d0; weak monotonicity suffices.

These do not refute the qualified construction claims. They are scope and
proof guards. The fresh analytic three-developer exclusion also reproduces
profitable withdrawals that either leave L or switch to M.

## 8. Severity, remaining verification and routing

| Finding | Severity / nature | Disposition |
|---|---|---|
| False or incomplete C1–C7 theorem on the baseline | FATAL search target | None found; no theorem rollback required |
| Unrestricted-government or cross-model claims inferred from this PASS | MAJOR BUT FIXABLE / claim scope | Maintain prescribed selector and baseline; re-audit if scope changes |
| Public zero-a sufficiency extended to unanimity; strict firm opposition at all private SPE | MAJOR BUT FIXABLE / economic/mathematical wording | Exact counterexample/weak boundary retained; stronger wording excluded |
| Purely numerical nonconvergence or failed denominator mapping promoted to proof | MAJOR BUT FIXABLE / evidence handling | Failure states retained; no such promotion made |
| Matrix/CS symbol ambiguity in audit draft | MINOR / exposition | Distinguished second-highest capacity C from consumer surplus CS |

**NOT INDEPENDENTLY VERIFIED here:** the full seven-parameter robustness
certificate; mixed SPE; unrestricted proposal/voting; positive public expense;
general function forms; author/external-human understanding; publication novelty.
The new claims are not claimed on those domains. Prior Stage30 negative
diagnostics are preserved without silently altering the canonical model.

Formalization applicability is **APPLICABLE** for the proof-critical core;
implementation remains **PLANNED / NOT FORMALLY VERIFIED**, permitted at Stage4A
but blocking Stage7.5A closure until properly resolved. The target map prioritizes
global deviation logic, case exhaustiveness, inequalities and welfare quantifiers.
No assistant build has occurred and no formal PASS is awarded.

Next is a bounded Stage6 theorem-level novelty re-kill using C1–C7. Do not begin
the full revised manuscript or add models to rescue publication value here.
If a central claim is absorbed without an independent economic implication,
follow the existing note/stop rule. If the claims survive, continue through
economic completeness and scope/formal closure before a new Stage8 freeze.
This PASS changes the additional-result mathematical state only; it does not
reverse the old manuscript editorial NO-GO or release Stage31.
