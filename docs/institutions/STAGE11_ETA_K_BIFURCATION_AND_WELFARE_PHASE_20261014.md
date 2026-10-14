# Stage 11 — Exact two-dimensional eta–K bifurcation, RS/IS full-continuous SPE coexistence, and welfare boundary

**2026-10-14.** Draft stacked on Stage10 PR #39. Scope: the SAME integrated six-player private standard creation/three-government delegated open-regulation game, with independently and CONTINUOUSLY chosen private `c_i,a_i`, policy `L,C,M`, a regulator choosing `c_P,a_P`, true differentiated Cournot KKT and Stage8 physically capitalized open technology upgrades. Five of the six original economic parameters remain fixed:
`(v,gamma0,kappa,rho,phi)=(1/100,7/50,1/50,8/25,7/50)`.
`eta` varies on **the complete nonnegative-product-substitution admissible interval [0,7/50]=[0,.14]** and setup resource cost `K>=0` is the previously disclosed SEVENTH scalar parameter. The publicly implementable OPEN `O(c_P,a_P)` engineering specification family remains EXOGENOUSLY AVAILABLE; G1 has delegated authority to choose depth after government 2/3 approval of a mandate. **The governmental authorization/action timing is assumed, not solved as a constitutional game.**

## Result A — EXACT global threshold for strictly positive privately chosen design, all admissible eta

For a two-firm private proprietary standard `R12(c,a)` with an active Cournot outsider, let
`m=1-v`, `z=1+rho c`, `b=gamma0+kappa a-vc`, `d=gamma0-eta a`,
`D=2m(2m+b)-2d²`,
`x=(2m z-d)/D`, `y=(2m+b-2dz)/D`.
Real private profit per member before the extra fixed cost K is
`P_R(c,a;eta)=3m*x²-phi*(c²+a²)/2`.
All technology triangulations `0<=a<=c<=1` have positive definite demand and true all-firm positive Cournot production for eta∈[0,.14]. **Global marginal private profit in compatibility c is strictly positive** over the whole rectangle by the identity `x_c=2m(rho+v x)/D>0` plus a rational lower-bound on `6m x*x_c-phi*c`. Thus all optimal private designs have `c_R^*=1`.

Write `f(a,eta)=P_R(1,a;eta)`. Its EXACT marginal incentive to begin aligning product design at a=0 is
`f_a(0,eta)=14693184*(8604325*eta-306108)/221518693813925`.

**PROPOSITION 11A (fully admissible theta slice):**
`eta_0=306108/8604325 =0.035576062038567814...` is the EXACT PRIVATE PRODUCT-DESIGN bifurcation:
- for `0<=eta<=eta_0`, the UNIQUE global private optimal design has `a_R^*(eta)=0`;
- for `eta_0<eta<=.14`, it has a UNIQUE STRICTLY INTERIOR optimum `0<a_R^*(eta)<1`, determined by `f_a(a*,eta)=0`;
- `a_R^*(eta)` is strictly increasing in eta above the threshold.

**Proof, not sampled or presumed:** SymPy exact rational tensor Bernstein positive-coefficient decompositions over the ENTIRE two-dimensional square `a∈[0,1]`, `eta∈[0,.14]` establish `-f_aa>0` (81/81 positive numerator and 81/81 positive denominator coefficients) and `f_{a eta}>0` (36/36 numerator and 81/81 denominator). `f_a(0,eta)` is exactly linear in eta with the displayed single root; `f_a(1,.14)<0`, and `f_a(1,eta)` strictly increases in eta so is <0 for all lower eta. Strict concavity implies unique global max. Implicit differentiation gives `da_R^*/deta= -f_{a eta}/f_aa>0`. This is a **sharp nontrivial new threshold within the full admissible eta slice**, rather than a numerical assertion about eta=.03 versus .14.

This threshold is independent of K because K is a real fixed cost per developed family and its derivative in a is zero conditional on developing. It does NOT establish that a positive-design RS is an SPE for every eta in the parameter range; the private local/global optimum and institutional equilibrium are distinct propositions.

## Result B — REAL 2D area of simultaneous fully continuous private RS and public IS SPE

Let
`E=[1/10,7/50]=[.10,.14]`,
`Kbox=[27/50,14/25]=[.54,.56]`.
For every `eta∈E`, exact concavity, strict cross-partial and rational first-order-condition endpoint signs yield:
`1/4<a_R^*(eta)<61/100`,
and `a_R^*(eta)` increases strictly from approximately .305344 at eta=.10 to .5949515 at eta=.14.

**PROPOSITION 11B (CERTIFIED TWO-DIMENSIONAL REAL RECTANGLE).** For EVERY real `(eta,K)∈E×Kbox`, the SAME integrated three-firm/three-government extensive-form game possesses BOTH of the following genuine full-continuous-first-stage **subgame-perfect Nash equilibrium outcomes**:
1. **Private proprietary RS12:** F1 and F2 independently invest `X(1,a_R^*(eta))`; F3 chooses legacy N, but continues producing in the differentiated Cournot market. G1/G2/G3 do not mandate (L), as existing X technology plus new open-family installation would reduce resident incumbent national welfare. Every firm can deviate to any X/Y/O/N and to any REAL c_i,a_i; no profitable unilateral deviation, permitting arbitrary credible mixed continuation Nash in other postcertification histories.
2. **Public international IS:** all F_i initially choose N. G1 proposes a public-domain standard mandate; G2/G3 unanimously approve delegating public technology depth to G1. Given unique all-firm compliance after ANY selected public depth, G1's unique national optimum over the FULL real triangle is `(c_P^*,a_P^*)=(1,0)`. All F_i implement it, so all 3 share a common interface while retaining differentiated products. All unilateral development deviations, private open-accreditation attempts and relevant government changes are globally blocked.

### Compact rational certificates of the uniform bilateral/individual incentives

- All private member RS gross-profit-maximizing design profit (before K) is nondecreasing in eta because `f_eta(eta,0)=0` and `f_{a eta}>0`; its largest value on E is attained at eta=.14, where exact Sturm signs give `max_a f(a,.14)<1.009`. Hence a lone O-developer cannot induce voluntary N migration under any `K>=.54`: `1.009-.54<PN≈.581486`. A second potential N adopter also strictly prefers retained nonmember Cournot profits to joining an IS coalition: `P_I^{max}-.54≈.421355` is smaller than a uniform outsider KKT lower bound.
- At the private RS optimum across E, `a_R^*(eta)>.25`, so `d=.14-eta*a_R<=.115` and `b>=.135`. Cournot outsider output `y>3019/7029`, and outsider profit is therefore `P_{O,R}>9114361/16635300≈.547893`. For any unilateral F3 attempted adoption of X with ANY real `c_3,a_3`, independently derived asymmetric KKT and exact rational bounding give newcomer `q_3<3/5`, gross profit `<1.0692`, and after paying K≥.54 net profit `<.5292<.547893<P_{O,R}`. F3's alternative Y/O actions under any L/C/M continuation yield at most `1.009-K` (regional), `P_I^{max}-K` (international), or baseline outsider minus development cost; they are strictly worse.
- An X member changing its c or a cannot outperform the TRUE globally optimized `f(a_R^*,eta)`. Switching to unrelated Y/O makes it a singleton unless other firms migrate, in which case its gross coalition member payoff remains bounded by the global regional optimum; switching to N induces the regulatory public standard M from all three national governments, yielding only `P_I^{max}-K<f(a_R^*,eta)-K` as the private member prefers its regional margin. The exact inequality holds since even baseline eta=0 private R net payoff `f(0,0)≈.990983>P_I^{max}≈.961355`.
- After established private X12, private incumbent national welfare is uniformly HIGHER than public M at any chosen legal specification, since the proprietary sunk real installation cost does NOT fund a newly required O technology-family installation. Uniform crude LOWER BOUND `f(0,0)+(m+g-v)((2m-g)/Dmax)^2` for old RS operating+CS, with K≥.54 and public national welfare upper bound W_I(1,0), proves member-government veto for every eta∈E and every optimal a_R. Conversely, after a member abandons X, only singleton X remains and all national governments strictly prefer public M because `W_I(1,0)-W_N>K` throughout Kbox.
- For ALL publicly available `0<=a_P<=c_P<=1`, all 3 firms find complying rather than exiting **STRICTLY DOMINANT** irrespective of past N/X/Y/O labels. For n=1 public adopter, `G_1-phi(c_P²+a_P²)/2>=25/33-phi>.56`; for n=2,3, private payoff net of variable design cost is decreasing in a_P at fixed c_P and increasing along the diagonal a_P=c_P, so minimum is at (0,0), with `G_2(0,0)>.56`, `G_3(0,0)=P_N>.56`. Since no incremental fee is larger than K + physical design cost, strict compliance follows for every K≤.56. Its uniqueness removes arbitrary policy-after-M adopter-equilibrium selection. Government national `W_I(c_P,a_P)` strictly decreases in a_P, and strictly increases in c_P at a_P=0 by rational Sturm. Thus its unique policy-optimal depth is (1,0) in relevant subgames. Other C games always admit a credible mixed Nash, which is allowed in offpath full SPE strategy completion.
- SAME-O capitalized stock upgrade costs avoid fictitious private stage-investment arbitrage; paying for preliminary O and then retrofitting for any final public O does NOT undercut one-shot public installation. Public patent rights and agenda delegation still assumed.

All statements are proven as strict inequalities with a nonzero margin on a CLOSED 2D eta–K rectangle. The older Stage10 single-eta K interval is a subset; this strengthens existence to nonzero 2D AREA, not just a lower-dimensional line.

## Result C — a UNIQUE welfare-ranking frontier INSIDE the actual SPE coexistence rectangle

Define national-welfare sum of the two ACTUAL equilibrium outcomes:
`S_R(eta,K)=2 f(a_R^*(eta),eta)+P_O(1,a_R^*(eta),eta)+3 CS_R(1,a_R^*(eta),eta)-2K`,
`S_I(K)=3(W_I(1,0)-K)`.
Hence exact sign is
`S_R-S_I=K-K_world(eta)`,
`K_world(eta)=3W_I(1,0)-[2 f(a_R^*(eta),eta)+P_O(1,a_R^*(eta),eta)+3CS_R(1,a_R^*(eta),eta)]`.

**THEOREM 11C:** On eta∈[.10,.14], `K_world(eta)` is CONTINUOUS and STRICTLY DECREASING. For each fixed real K∈[.54,.56], exactly ONE `eta_W(K)∈(.10,.14)` satisfies `K_world(eta_W)=K`. On the lower side `eta<eta_W(K)`, publicly mandated IS has strictly higher world-sum national W; on the higher side `eta>eta_W(K)`, private RS has higher world-sum national W. Crucially BOTH regimes remain economically/strategically possible SPE all along; this is a WELFARE BOUNDARY, not a standard-equilibrium existence/disappearance boundary.

**Exact monotonicity proof:** From 11A, a_R'(eta)>0. The global welfare function `W^{RS}(eta,a)=2P_R+P_O+3CS_R` has BOTH strict positive partial derivatives `W_eta>0` and `W_a>0` on the rational rectangle eta∈[.10,.14], a∈[.25,.61], demonstrated by strictly positive tensor Bernstein coefficients: respectively numerator+denominator 30/49 and 56/49 positive coefficients. All optimal private a_R live within this enclosing rectangle. Therefore
`d W^{RS}(eta,a_R(eta))/deta =W_eta+W_a a_R'(eta)>0`, and K_world'(eta)<0. The welfare difference is strictly increasing in K. Exact rational brackets for a_R(.10)∈(.3053,.3054) and a_R(.14)∈(.5949,.5950) prove `S_R(.10,K=.56)-S_I(.56)<0` and `S_R(.14,K=.54)-S_I(.54)>0`, hence a unique zero for EVERY K in [.54,.56]. Stronger rational brackets at eta=.118 and .119 prove `eta_W(.55)∈(.118,.119)` independently of any numerical root solver.

**Informative numerical approximations only (NOT proofs):**
| K | unique eta_W(K) | a_R(eta_W) |
|---:|---:|---:|
| .54 | .12235096 | .44948388 |
| .55 | .11886247 | .42461401 |
| .56 | .11510832 | .39896292 |

Private optimum sample grid for orientation (source exact thresholds take precedence):
| eta | a_R*(eta) | K_world(eta) |
|---:|---:|---:|
| .03 | 0 | .65614736 |
| .04 | .01845736 | .65487487 |
| .10 | .30534434 | .59343907 |
| .11 | .36571714 | .57245140 |
| .12 | .43260917 | .54681698 |
| .13 | .50803514 | .51537765 |
| .14 | .59495151 | .47641277 |

The eta=.03/.04 numeric welfare rows describe PRIVATE optimized RS and IS terminal allocations, NOT additional fully certified Stage11 SPE coexistence outside the [.10,.14] institutional rectangle; prior Stage9 separately certifies an eta=.03 RS+IS region for other K. No misleading 'complete global phase diagram' claim.

## Scientific synthesis and strict limits

**Research contribution actually established:** distinguishing technical interface compatibility c and product-design convergence a yields a calculable exact `eta_0` where endogenous PRIVATE RS design departs the zero boundary. The acquired product distinctiveness raises nonmember economic value; together with irreversible investment and multi-government sequential regulation, a nontrivial 2D rectangle has BOTH genuine full-continuous private RS and public IS SPE; within that same strategic coexistence region the socially preferred regime SWITCHES at unique, monotone eta_W(K). This is a sharper multi-mechanism result than merely comparing a few parameter witnesses, but needs focused novelty testing against existing product-distinctiveness/network compatibility literature before journal acceptance assertions.

**Not yet solved:** all 7 parameter dimensions necessary/sufficient SPE correspondence, national vote-on-each-public-depth constitutional choices vs G1 delegate authority, endogenous TECHNOLOGICAL public feasibility or public engineering/R&D procurement cost, proprietary license royalties, heterogeneous buyer network adoption. Fundamental standards lock-in, incumbent IP patent exclusion, and Ghosh–Morita competitor/outsider distinction have significant prior art. Do NOT describe these already studied ingredients as inherently novel.

**Reproduction:** `code/stage11_eta_k_phase_certificates.py` exact symbolic SymPy/Sturm/Bernstein; `.github/workflows/stage11-eta-k-phase-certification.yml` CI. Parent Stage10 `code/stage10_positive_design_endogenous_public_depth_spe.py` verifies complete six-player legal/adoption/government mechanism at eta=.14; Stage11 extends its margins uniformly. PR remains Draft, no manuscript edits or merge.
