# Stage 6 — Full Continuous Strategy, Multiple Post-policy Equilibria: Exact Audit and Genuine High-K SPE

**2026-10-14 JST.** Stacked on Draft PR #34. The user asked for ALL-continuous technology designs and the COMPLETE SPE correspondence including multiple adoption equilibria. **Scientific disposition: only PARTIALLY completed, not an explicit global all-parameter classification.** We provide a new exact full-continuous-strategy SPE EXISTENCE theorem on a substantial fixed-cost subregion, a COMPLETE pure/mixed adopter equilibrium analysis at a difficult off-path public mandate subgame, and an exact necessary/sufficient behavioral SPE correspondence framework. No earlier manuscript was modified; no global 7D equilibrium diagram is claimed.

## 1. Unchanged combined extensive game and genuine mathematical distinction

Three firms independently choose `N` or `(ell_i,c_i,a_i)` with `ell_i∈{X,Y,O}`, `0<=a_i<=c_i<=1`, `c_i>0`. Original normalized production/network/differentiation coefficients `theta=(v,gamma0,kappa,eta,rho,phi)`; the optional real fixed firm development/setup resource cost K is explicitly a **seventh quantitative primitive**. Individual resource cost paid upfront `K+phi(c_i²+a_i²)/2`; conversion/retrofit after C or M costs the real implementation fee again only if a firm actually changes technology. No royalty, government subsidy or forced transfer of proprietary patents.

Government G1 proposes L (nonintervention), C(r) (certify an **actually observed** private OPEN O protocol r), or M (mandatory pre-existing PUBLIC open O(1,0)); governments G2 and G3 sequentially approve/reject, default L if either vetoes. After C, firms simultaneously choose retain/migrate; after M they simultaneously choose comply/exit. All firms select Cournot quantities with correct KKT support; three home governments maximize resident firm global profit + domestic CS. All technology pairing, min(c_i,c_j), min(a_i,a_j), outsider Ghosh–Morita distinctiveness, positive demand matrix are exactly the source Stage5 *new asymmetric institutional model*, not alleged consequences of old six-dimensional symmetric model.

**Different levels of completion:**
- All c_i,a_i in the feasible CONTINUUM are admitted as initial firm deviations in the theorem here.
- All possible **mixed** post-C and post-M equilibrium continuations are taken into account in the crucial high-K result.
- The prior **10/14/1 equilibrium counts** are still only the exact 10-action-per-firm **finite design-menu** game under ONE explicit adoption-equilibrium selection; they are NOT full-continuous robust counts.
- At arbitrary continuous initial profile h and arbitrary parameters, solving every C/M mixed adopter game, all public policy choice branches, and every continuous firm deviation remains genuinely unfinished.

## 2. ALL policy-after-h adoption equilibria, not a selected Nash

For each initial technology profile h, admissible public proposal p=C(r) or M, and each binary adoption vector `e∈{0,1}³`, first solve the actual firm Cournot/KKT quantities and obtain per-firm rational payoff `u_i(e|h,p)`, including initial sunk costs and any new real refit payment. Write the mixed adoption probability of firm i as `x_i∈[0,1]`. Define
`D_i(x_-i|h,p)=sum_{e_-i∈{0,1}²} [u_i(1,e_-i)-u_i(0,e_-i)] * product_{j!=i} x_j^{e_j}(1-x_j)^{1-e_j}`.

**COMPLETE mixed equilibrium predicate** for EVERY subgame h,p:
`x_i in [0,1]`,
`x_i * D_i >=0`,
`(1-x_i) * D_i <=0` for all i=1,2,3.

Proof: if x_i=0 then D_i<=0 (stay/exit is optimal); if x_i=1 then D_i>=0; if 0<x_i<1 both signs imply D_i=0 (indifference). It includes all pure, interior and boundary mixed Nash, including a CONTINUUM of Nash mixtures when payoff differences vanish. D_i is quadratic multilinear in rivals' probabilities, and rational/semialgebraic in h and admissible theta on each branch of the min/max and Cournot support constraints. Nash's finite game existence theorem guarantees at least one (possibly mixed) x in EACH postpolicy binary game and at every feasible continuous h.

Government choices must be evaluated **after specifying one credible mixed Nash continuation for every possible C(r),M**; then G2 and G3 separately accept only strictly nationally beneficial policies (fixed indifference -> L), and G1 chooses the best among unanimously feasible proposals. Let `B(h)` denote the resulting correspondence of entire government/adoption subgame SPE outcomes over ALL feasible policy-by-policy Nash continuation selections. It is not generally a singleton. There are finitely many governmental proposals for a FIXED h (at most 3 observed O references plus M), so `B(h)` is nonempty once mixed adoption is allowed.

**Exactly complete behavioral SPE criterion for the whole continuous game**:
There must be a pure initial technology profile h* and ONE credible continuation policy `b(h)∈B(h)` at EVERY (including offpath) initial h, such that
`P_i(h*,b(h*)) >= P_i((h'_i,h*_-i),b(h'_i,h*_-i))`
for every firm i=1,2,3 and EVERY possible technology deviation h'_i (continuous c_i and a_i, any X/Y/O/N). After every policy proposal/approval history, adopters play their designated mixed Nash, and G1–G3 sequentially best respond. This predicate is NECESSARY AND SUFFICIENT for an SPE with pure first-stage firm choices, mixed adopter continuations and the specified tie convention.

Offpath continuation selection **matters**. To establish *existence* of a supported h*, one may choose different credible B(h) punishments at different offpath h. To establish stability independently of continuation selection, every offpath B(h) must be checked. Replacing B by 'maximum aggregate welfare equilibrium' is an extra restriction that changes the problem. These are exact characterization conditions, not computationally evaluated 7D inequalities; saying “we have completely classified all 7D phases” would be false.

With rational theta and a rational candidate h*, each fixed h,p mixed equilibrium set is a finite **semialgebraic** set. Real closed field quantifier elimination can IN PRINCIPLE check a proposed equilibrium inequality against all real continuous deviations, provided the finite policy continuation correspondence B(h) and Cournot active branches are encoded. Large nested quantifier blocks and high polynomial degrees make explicit full 7D CAD classification technically formidable. We have not executed CAD on the full space; no unsupported claim of its completion.

## 3. A FULL solved multiple-equilibrium subgame under government M

At prehistory `h=(N,N,N)`, consider mandating the legally existing public reference `O(1,0)` and letting each firm independently choose compliance or exit. Fix
`(v,gamma0,kappa,eta,rho,phi)=(.01,.14,.02,.03,.32,.14)`.
If n∈{1,2,3} firms comply, each receives `G_n-K` (noncompliant firm receives 0), with exact pre-fixed-cost profits
- `G_1=2269/3300≈.687575758` (no matching partner, thus no network improvement);
- `G_2=4863281/4452100≈1.092356641` (two interoperable firms, third exits);
- `G_3=301481/313600≈.961355230` (all three interoperable firms).

Thus `G_1<G_3<G_2`. A pure profile with n adopters is Nash iff each current adopter wants to remain, `G_n>=K`, and each exiting firm wants to stay out, `G_{n+1}<=K`. For strict open K intervals the **ENTIRE pure adoption Nash type partition** is:

| K interval | ALL pure adoption Nash profiles | Count |
|---|---|---:|
| `0<=K<G1` | 111 (all comply) | 1 |
| `G1<K<G3` | 000 and 111 | 2 |
| `G3<K<G2` | 000; 110,101,011 | 4 |
| `K>G2` | 000 (all exit) | 1 |

At the three exact thresholds add the profiles satisfying non-strict conditions; no false uniqueness claim. This is a **complete closed-form pure equilibrium classification** in K for the actual mixed public standard compliance stage.

At `K=3/4`, payoff differences from compliance given 0/1/2 other adopters are
`A=G1-K=-103/1650<0`,
`B=G2-K=762103/2226050>0`,
`C=G3-K=66281/313600>0`.
The **COMPLETE adoption Nash set**, pure and mixed, contains **exactly three** points:
1. all exit `x=(0,0,0)`;
2. all comply `x=(1,1,1)`;
3. one completely mixed *symmetric* Nash `x=(t*,t*,t*)`, with `t*≈.08150520394` the unique root on (0,1) of
`A(1-t)²+2Bt(1-t)+Ct²=0`.

For proof of no hidden asymmetric mixtures: if some firm is pure 1, a counterpart has strictly positive incremental adoption profit under either action of remaining opponent because B,C>0; hence no other mixer. If one firm is pure 0 and both others mix, each mixing probability must equal `t0=-A/(B-A)`; but the pure 0 firm then strictly prefers adoption, contradiction. If all three are interior and two probabilities differ, subtracting two indifference polynomials forces the third to `-(B-A)/(A-2B+C)`, at which the relevant indifference polynomial is STRICTLY positive, contradiction. Hence only one symmetric mixed solution, with uniqueness and isolating interval (0.081,0.082) certified by exact Sturm root count.

This NONUNIQUENESS is not a numerical degeneracy; 000 and 111 are STRICT adoption Nash at K=.75. An earlier maximum-welfare selection would have silently deleted valid equilibrium outcomes.

## 4. New full-continuous, all-mixed-continuation SPE existence theorem

At prehistory h=(N,N,N), nonintervention L yields per-country
`P_N=7425/12769≈0.5814864124`,
`W_N=24375/25538≈0.9544600204`.

For n public-mandate adopters (n=0,1,2,3), let `CS_n` denote common domestic consumer surplus when exactly n firms remain and implement public O(1,0). With n=0 CS=0; for n=1, `CS_1=25/198`; n=2 `CS_2=487872/1113025`; n=3 `CS_3=16335/25088`. If n firms comply, the TOTAL national government welfare is
`S_n(K)=n*(G_n-K)+3*CS_n` for n≥1, with `S_0=0`.

Define the exact NATIONAL-UNANIMITY-FORBIDDING cutoff:
`K_G=max_{n=1,2,3} [(n G_n+3 CS_n-3 W_N)/n]`
`=5269762153/8008716800≈0.6580033087`.
For **every** `K>K_G`, **every** pure compliance vector has total government welfare `S_n(K)<3W_N`. Therefore ANY independent mixed, correlated or arbitrary convex mixture of compliance results has expected total government welfare STRICTLY BELOW 3W_N. It is then IMPOSSIBLE for all 3 governments to each enjoy a strict gain from an M mandate. Because C is unavailable when no firm initially develops OPEN technology, government L is therefore THE final policy outcome at NNN, **independent of postpolicy adoption equilibrium selection**. This is an aggregation-based proof, not a chosen adopter NE.

For ANY initial unilateral firm deviation with positive continuous `(c_i,a_i)`, the initial firm must incur setup cost K. Throughout admissible nonnegative-substitution domain, Cournot best-response FOC `2m q_i=z_i-sum_{j!=i} M_ij q_j<=z_i<=1+rho` holds when q_i>0; if q_i=0 its operating profit is zero. Thus, for ANY final public policy, open/proprietary family, legal conversion, other firms' strategies (pure/mixed), and any entire technology triangle design:
`P_i^deviation <=3(1+rho)²/(4m)-K`.
Consequently, if
`K>K_D=3(1+rho)²/[4(1-v)]-P_N`
`=235752/319225≈0.738514`,
a deviation cannot improve on PN, **for all continuous c_i,a_i, not merely the 3 pilot designs**. Exact symbolic arithmetic confirms `K_D>K_G`.

**THEOREM 6.1 (genuine continuous-strategy SPE existence region).**
For fixed original 6 normalized coordinates `(.01,.14,.02,.03,.32,.14)`, and ANY `K>K_D=235752/319225`, the full integrated game admits at least one SUBGAME PERFECT equilibrium with all 3 firms selecting N initially and governments choosing L, and final Cournot NS, **for any selected mixed-Nash continuation of an unaccepted government M at this prehistory**. For each offpath continuous technology h, select some mixed Nash in each finite C/M adoption game (exists), then solve finite G1/G2/G3 sequential proposals/votes; such continuations exist. At NNN, no policy M can gain unanimous support since K>K_G; at Stage1 any positive continuous development deviation yields less than PN since K>K_D. Hence all-on-NS initial choice satisfies each firm's GLOBAL best response and every subgame has credible optimal continuation. This is a genuine SPE existence theorem with **continuous initial choices** and **mixed postpolicy adoption**, not a finite discretization or another strong-Nash refinement. We do NOT assert NS is the only SPE final type when K exceeds this bound; uniqueness would require excluding every other continuous-equilibrium profile.

**COROLLARY at K=.75** satisfies both conditions. The M adoption subgame has all three Nash distributions above, but the gov always chooses L at NNN, and no firm can profit by independent continuous development. Therefore fragmented NS is a TRUE full-continuous-game SPE final outcome with mixed-continuation robustness.

## 5. Honest uncompleted parts, required before claims of COMPLETE classification

1. **No exact global IS/RS SPE phase regions** under independent continuous firm designs have been derived. The previous finite 10/14/1 equilibrium counts DO NOT hold as proven continuous-game counts.
2. **No complete all-parameter mixed adoption equilibrium stratification** for EVERY initial real-valued h and every observed C(r),M: while the polynomial mixed Nash predicate is exact, the roots and solution-set dimension can vary discontinuously with h and theta.
3. **No full seven-dimensional explicit semialgebraic SPE partition** and no proof of pure first-stage existence on every institutional/parameter region. At boundary cases, discontinuities in government vetoes and standard-family participation can make best responses unachieved.
4. **Legal/institutional sensitivity** remains: government G1 alone sets agenda; G2/G3 have effective vetoes; formal certification opens a new firm migration window while unrecognized compatibility cannot be revisited (policy-dependent action set), public-domain open O(1,0) is assumed pre-existing; patent licenses X/Y remain unexpropriated. All are disclosed assumptions, not endogenous welfare optimal institutions.
5. **Conceptual correctness:** Stage5 benefits z_i are normalized marginal production COST reductions, not quality shifts in inverse consumer demand; `p=1-Mq`; CS is `q'Mq/2`. The bilateral Ghosh–Morita substitution/between-insider-outsider terms are a *new heterogeneous-pair extension*. Off-diagonal C(c_i,a_i), min technology matching and fixed setup K are not uniquely implied by the original six-parameter symmetric specification.
6. **Publication-level novelty remains NO-GO** from Stage6 theoretical audit; these are precise conditional applied industrial organization results.

## 6. Exact reproducibility

- Proof code: `code/stage6_full_continuous_mixed_spe_certification.py` (new; imports original Stage5 exact-rational 3-firm KKT module for independently cross-checking all 8 realized adopter outcomes).
- Full Stage5 integrated game (not silently modified): `code/stage5_integrated_independent_standards_and_government.py`.
- Continuous mixed SPE proof CI: `.github/workflows/stage6-full-continuous-mixed-spe.yml`.

Research gate for Stage7: conduct all-mixed-adopter subgame solution diagnostics on arbitrary continuous h, and compute certified global firm deviation maxima (piecewise rational branch optimization with CAD/interval certificates). If computational complexity prevents exhaustive regions, select properly stated identifiable lower-dimensional slices and formalize exact theorems. Do not label a grid search or arbitrary Nash-selection pilot a full SPE partition.
