# Stage 5: One Integrated 3-Firm / 3-Government Public–Private Standards Game

2026-10-14 JST. Parent Draft PR #33. **User objective:** each firm independently chooses proprietary/open standard plus interoperability intensity `c_i` and product common-design intensity `a_i`, followed by three national governments' endogenous choice between nonintervention, private open-standard certification, and public open-standard mandate. All final firm technology adoption decisions and differentiated Cournot outputs are endogenous.

**Status: GAME FULLY SPECIFIED, exact-rational finite-design pilot fully solved; INFINITE-CONTINUOUS-GAME general SPE NOT SOLVED.** This is a research-stage institutional application, not a publication-ready or novel foundational IO theorem. Do not conflate private joint-contract outcomes from older stages with this independent-development model.

## 1. Six strategic actors, chronology, and legal implementation

There are six strategic players `F1,F2,F3,G1,G2,G3`, with each firm owned in country i and selling products in all three identical segmented product markets. Each firm simultaneously chooses:
`A_i = {N} UNION {(ell,c_i,a_i): ell in {X,Y,O}, 0<=a_i<=c_i<=1,c_i>0}`.
- `X,Y` are two legally proprietary, mutually incompatible private interface families; each developer has rights to its own implementation, while a government cannot take over essential technology absent permission.
- `O` is an openly licensed private family with legally accessible reference designs.
- `N` is separate legacy technology.
**The private design choices are simultaneously independent:** no appointed proposer, no unanimity agreement, and no firm can unilaterally dictate other firms' design.
- First-stage physical development/adoption `C(c_i,a_i)=phi(c_i²+a_i²)/2+K` is SUNK at the government decision date. K is a disclosed **seventh scalar primitive** (optional real setup cost); with K=0 the model has original six physical parameters. This two-dimensional off-diagonal fee split is a NEW structural assumption, reducing to `phi*s²` on `c=a=s`. Regulator policy does NOT refund sunk private development expenditures.

Governments observe all firm choices. One appointed governmental agenda setter G1 picks:
- `L` leave all firms' initially chosen standards and technologies in place.
- `C(r)` **certify an existing privately developed OPEN O design** `r=(c_r,a_r)` in the observed initial profile, opening a time-limited free-agency migration window for other firms. Firms independently decide migrate to this exact publicized O reference or stay in current platform. Migrating to a different reference incurs a NEW real `C(r)`, in addition to original sunk investment; previously identical O adopters do not repay cost. This is a deliberate technological refit-cost assumption. Without an observed O developer, certification cannot be proposed.
- `M` mandate a PRE-EXISTING, legally open/public-domain reference `O(c_P,a_P)`. The pilot fixes the already documented benchmark `(c_P,a_P)=(1,0)`; **government does NOT develop a new inaccessible invention**. All incumbent and legacy firms independently choose comply with the legally enforceable public reference or cease production. A converting firm incurs real refit cost unless it is already on the same O reference; preexisting sunk investment is not refunded. Government does not mandate private X/Y patents, royalty-free patent expropriation, or operation with negative ongoing net profitability.
- G2, then G3, publicly and sequentially approve/reject the specific G1 certification or mandate. A policy requires unanimous G1/G2/G3 support; a veto implements L. At individual welfare INDIFERENCE, a legislator votes NO to a change (tie convention); government proposer prefers the less interventionist of identical-welfare outcomes (L then C then M).

After C, 3 firms SIMULTANEOUSLY choose migrate/stay. After M, they SIMULTANEOUSLY choose comply/exit. In the C/M adoption games, all pure Nash profiles are enumerated, using their actual eventual profit as objective. Where multiple adopter Nash equilibria exist, the sample implementation chooses one maximizing aggregate governmental W, then firm P and conformity as explicit **continuation-equilibrium selection**. Such choice is *one valid Nash continuation*, not proof that all SPNE have the same result. An unrestricted SPE analysis must retain a correspondence of credible Nash continuations and consider the constitutional policy menu selection.

## 2. One common, symmetric, game-theoretically complete demand/payoff structure

Keep ORIGINAL normalized primitives `theta=(v,gamma0,kappa,eta,rho,phi)`. Define `m=1-v>0`.
Each pair of firms `i!=j` on the SAME nonlegacy standard family takes effective interoperability and common design
`c_ij=min(c_i,c_j)`, `a_ij=min(a_i,a_j)`.
Their substitution-demand matrix cross entry
`M_ij=gamma0 + kappa*a_ij - v*c_ij`.
Each firm i receives pre-marginal-cost advantage
`z_i=1+rho*max_{j: ell_i=ell_j !=N}c_ij`, with maximum over empty set 0: lone adopters do not obtain network/co-development productivity; they nevertheless pay their selected sunk investment.
When EXACTLY two firms use one common interface with third unmatched, define insider pair common-design intensity `a_in=min(a_i,a_j)` and outsider cross coefficient
`M_i,out=M_out,i=gamma0-eta*a_in` for two insiders. If no coordinated pair (all distinct) all off-diagonal substitutes use baseline `gamma0`. This is a new explicit asymmetric extension of the earlier symmetric RS and IS matrices, inspired by Ghosh–Morita: intra-coalition common design increases direct substitution by +kappa, outsider differentiation reduces cross-substitution by -eta. No outside-vs-inside effect is given to singleton firms without collaborators.

`M_ii=m`. In every destination, consumers have quasi-linear surplus:
`U(q)=z' q - (q'Mq)/2 - p'q` (with z reflecting adopted productivity/cost advantage equivalently represented as net-demand intercept), and Cournot best responses solve all **active-set KKT** conditions `[(M+diag(m))q]_i=z_i` for active firms; `q_i=0` and residual <=0 for inactive firms. Correct symmetric demand interpretation is `p=1-Mq`, with z_i representing an equivalent FOC shift from lower marginal cost; **DO NOT literally treat z_i as higher consumer utility intercept unless the model is refrozen**. The utility CS accounting is `CS=(q'Mq)/2` with the demand matrix and homogeneous quality intercept 1. Thus productivity gains enter the firm cost term, not the consumer demand intercept. This distinction is important for independent designs.

The total 3-country private firm payoff:
`P_i=3m*q_i² - initial_cost_i - new_refit_cost_i`. An exited firm produces zero but loses its already-sunk initial investment; real sunk costs are in home government national W. Consumers in each destination obtain identical `CS=q'Mq/2`; country i welfare `W_i=P_i+CS`. Only actual technology adopters pay costs. This recovers original 3x3 NS/RS/IS continuation for symmetric same-depth cohorts, and generalizes legally and economically to independent heterogeneous c_i,a_i.

**Pilot audit domain:** `v=.01,gamma0=.14,kappa=.02,eta=.03,rho=.32,phi=.14`, `K in {0,.50,.75}`, c/a candidate set below. All off-diagonal entries are nonnegative and <=.152; m=.99; strict row-diagonal dominance ensures M SPD for every possible profile, policy and post-adoption action. Product-market uniqueness and all KKT active-support masks are checked with exact fractions, not floating approximations.

## 3. General continuous-strategy SPE conditions (exact but NOT SOLVED)

For each observed initial vector `h=(ell_i,c_i,a_i)_{i=1..3}` and government policy `p`, let `E_A(h,p)` be ALL private postpolicy adoption Nash profiles (after mandate, exit is feasible). Each yields exact Cournot `P_i(h,p,e),W_i(h,p,e)` and welfare vector. Select ANY subgame-perfect credible equilibrium continuation `e(h,p)∈E_A(h,p)`; existence of pure Nash is not guaranteed for arbitrary continuous-profile induced binary migration game, so mixed continuation could be needed.

Given an equilibrium selection, government G2/G3 approve policy p only when `W_i(h,p,e(h,p)) >= W_i(h,L)` (strict version under our tie convention). G1 chooses among its feasible unanimously accepted policies by its own national W; label `p^*(h)`. At initial private simultaneous design selection, a pure-strategy SPE initial action h* requires FOR EACH firm i:

`P_i(h*,p*(h*)) >= sup_{ell_i', (c_i',a_i')∈T} P_i((h_i',h_-i*),p*(h_i',h_-i*))`.

All government and firm subgames must have credible continuation strategies at EVERY off-path action history. These are necessary and sufficient conditions under the fully specified selected continuation, but the supremum is over continuous technology choices; a simple all-parameter closed-form partition has NOT been proven, and best responses need not be attained if policy regimes jump at indifference surfaces. **DO NOT identify this implicit fixed-point condition with a completely solved continuum model.**

## 4. EXACT finite candidate subgame-perfect diagnostic (global enumeration, no grid-implied proof)

For a controlled finite policy/technology candidate menu:
`D={(1/2,0),(1,0),(1,3/5)}`; each firm has 10 initial choices N and three designs for each of X/Y/O. Total initial profiles `10^3=1000`. Exactly evaluated for **all** 3 unilateral firm deviations to each of 9 alternative initial actions, all government proposals, all 8 independent firm conversion/compliance profiles and their unilateral deviations (8 KKT active sets for every market continuation). Every arithmetic operation is `fractions.Fraction` / exact rational Gaussian elimination. Tie-breaking and postpolicy coordination selection documented above.

At fixed `(v,gamma0,kappa,eta,rho,phi)=(.01,.14,.02,.03,.32,.14)` and PUBLIC reference `O(1,0)`:

| K | private-stage pure NE plus credible government/adoption continuation (=finite-game SPE) | govt on-path actions | FINAL standard types |
|---|---:|---|---|
| 0 | 10 | L in 3, C in 6, M in 1 | IS 10 |
| 1/2 | 14 | L in 13, M in 1 | IS 2, RS 12 |
| 3/4 | 1 | L in 1 | NS 1 |

At K=0:
- all N private init => G1/G2/G3 find a public mandate M beneficial, all companies strictly optimally comply with previously available public-domain O(1,0); final IS.
- proprietary initial X-X-N => incumbent governments prefer nonintervention to public mandate because refit costs sunk and replacing X lowers their welfare; final RS on THAT history (but this profile fails initial private Nash, because outside F3 has a profitable unilateral deviation).
- open initial O-O-N => governments approve certification C; voluntary migration by third firm to existing O design makes final IS, with no patent appropriation.
- all firms independently chose compatible X-X-X or Y-Y-Y => governments optimally L because universal proprietary compatibility already exists; final IS without formal regulation.
Hence the SAME IS technical outcome occurs under ALL THREE policy institutions, depending on private initial history. The policy label is neither redundant nor unique.

At K=.5, among 14 equilibrium profiles, 12 retain bilateral consortium RS without government upgrading, while 2 end in IS. This shows a genuine coexistence correspondence in a SINGLE INTEGRATED independent firm + national policy game. At K=.75, alone equilibrium N-N-N persists without govt intervention and no firm implements private or public standard: NS. These K thresholds are finite-menu witness points, NOT globally exact continuous-action parameter frontier values.

**Robustness/institutional sensitivity:** independent market coordination and government open mandate can undo the Stage4 fragmentation trap for low enough setup costs; patent closure can block gov mandatory reuse of the PRIVATE technology but not independently available public-domain reference technology. When high costs make public adoption unappealing to domestic governments or private firms, both public and private standardization can fail.

## 5. Critical conceptual boundary and next proofs

1. The government is not an unrestricted social planner: national vetoes plus one appointed government agenda setter. Public open reference O(1,0) exists prior to government choice (no arbitrary authority to appropriate X/Y), and its implementability & zero licensing price are assumptions. Public reference real deployment/retrofitting cost is paid by the ADOPTING companies; no separate government standard creation cost is assumed.
2. Recognition C is economically distinct from laissez faire L because it opens a **new voluntary migration/adoption window** after public certification; this feature is an institutional modeling assumption to be justified by accreditation/conformance testing/recognized focal points. If unilateral private migration is always possible without approval, certification may be redundant; that variant is a crucial robustness test.
3. Public mandate M does not forcibly keep an unprofitable firm alive. Exit loses sunk initial cost but avoids new compliance investment; firms' postmandate best responses are enumerated rather than forced. Enforcement and national regulator competence are assumptions.
4. Initial member matching via min(c_i,c_j) and min(a_i,a_j), the no-benefit-for-singleton rule, and the one-cohort Ghosh–Morita outsider-distinctiveness rule are substantive NEW off-symmetric primitives/functions. They are NOT implied uniquely by the original 6-parameter homogeneous prototype. Sensitivity to mean/Leontief/minimum rules and deployment technology is indispensable.
5. At K=.5 the multi-equilibrium IS vs RS result depends in principle on the continuation equilibrium selection rule. The code explicitly computes ALL adoption-stage pure Nash equilibria, then selects welfare-maximal Nash in the illustrative branch. Full ALL-SPE correspondence under other valid post-policy adoption equilibria remains open.
6. Stage4 module B assumed NO public alternate standard. The integrated model adds a **legally pre-existing public-domain reference**; therefore its fragmentation prediction is not contradictory to the new case K=0.
7. Continuous original `c_i,a_i` remains a mathematical action domain in the formal game, but the enumerated results use three design candidates. A paper may NOT claim that the 10/14/1 equilibria survive arbitrary unilateral deviations in the full continuous triangle. The next research gate is certified global deviation screening and an all-history existence test (piecewise rational inequalities, interval arithmetic, semialgebraic methods), alongside native dual open/private-platform competition.
8. No new publication-level IO novelty GO: Ghosh & Morita (2012) industry partner-outsider design substitution; Belleflamme (2002) formal/de-facto standards choice; Spulber (2019) patents/standards voting and market competition are strong established antecedents.

## References independently checked (publisher and research records)
- Ghosh, Arghya, and Hodaka Morita (2012), *Competitor Collaboration and Product Distinctiveness*, International Journal of Industrial Organization 30:137–152, https://www.sciencedirect.com/science/article/pii/S0167718711000671.
- Belleflamme, Paul (2002), *Coordination on formal vs. de facto standards: a dynamic approach*, European Journal of Political Economy 18:153–176, https://www.sciencedirect.com/science/article/pii/S0176268001000738.
- Spulber, Daniel F. (2019), *Standard Setting Organisations and Standard Essential Patents: Voting and Markets*, The Economic Journal 129:1477–1509, https://academic.oup.com/ej/article/129/619/1477/5364896.

**Files:** `code/stage5_integrated_independent_standards_and_government.py` and `.github/workflows/stage5-integrated-six-player-standards-game.yml`. Existing Draft PRs #22–#33 unmerged; no manuscript overwritten.
