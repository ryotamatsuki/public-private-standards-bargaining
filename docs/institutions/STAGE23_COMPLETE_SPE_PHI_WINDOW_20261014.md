# Stage 23 — Exact complete pure-SPE terminal outcome robustness in the capital-cost coefficient

Date: 14 October 2026. Scope is the SAME 3 independently investing firms / 3 independently proposing and voting national governments reduced OPEN/N game inherited from Stage19–22. No previously Draft PRs merged; no paper draft changed.

## Main result ST23.1 (global over a nondegenerate three-parameter rectangle)

Fix the technological market coefficients at
\[
(v,\gamma_0,\kappa,\rho)=(.01,.14,.02,.32).
\]
Allow ALL THREE independent parameters to vary continuously and simultaneously:
\[
\eta\in[.10,.14],\qquad K\in[.54,.56],\qquad
\boxed{\phi\in[.12,.33].}
\]

**Theorem ST23.1.** With open public O(1,0) legally preexisting, all three governments independently entitled to propose mandatory M, national simple-majority 2/3, national ties YES, no government compensation and original incremental open-family physical-cost rules, **every pure-strategy subgame-perfect Nash equilibrium terminates in public mandatory universal IS**. At least one such SPE exists, namely all firms initially selecting N and all governments subsequently mandating O(1,0) with universal firm compliance. This is a classification of *terminal pure-SPE outcomes*, NOT uniqueness of initial O/N investments, NOT absence of mixed SPE, NOT a necessary-and-sufficient global phase partition. Full technical action sets are continuous triangles 0<=a_i<=c_i<=1 for every initial O founder; initial N is always available.

### 1. Exact global 2-O / 1-N nonintervention equilibrium exclusion over variable phi

One firm's unique maximum a is strictly wasted because changing it to its partner's a leaves all market outcomes, all national M-L differences and every governmental vote exactly unchanged, but saves phi(a_i²-a_j²)/2 in either eventual M or L. After a equalizes, if one c is larger, reducing that firm's c to the smaller preserves pairwise min technology and status quo market, decreases its own governmental YES propensity and increases its private L payoff. Since prior policy L cannot become M by removing a YES vote, no asymmetric 2-O L-SPE is possible whenever phi>0. Thus any hypothetical two-O L-SPE must have identical founder designs O(c,a) for all REAL 0<=a<=c<=1.

For identical pair designs define m=.99, b=gamma0+kappa*a-v*c, d=gamma0-eta*a, z=1+rho*c, D=2m(2m+b)-2d², X=2mz-d, Y=2m+b-2dz. Then private matched-firm output is x=X/D, outsider y=Y/D, consumer-surplus numerator C=(m+b)X²+2dXY+(m/2)Y², CS=C/D². The full public gross national profit+CS is G_I, defined in the code exactly by symmetric 3-firm Cournot O(1,0), independent of eta. Exact founder policy-gain B and the private design marginal sign have polynomial numerators:

\[
D^2 B=(G_I D^2-3m X^2-C)-\phi(1-c^2)D^2/2=A_B+\phi B_B.
\]

\[
D^3(-f_a)=
 -6mX(X_aD-XD_a)+\phi aD^3=A_H+\phi B_H.
\]

For a<=3/4, exact 3D rational Bernstein signs certify B>0 on the **larger** rectangular set (eta,a,c) in [.10,.14]×[0,.75]×[0,1], including even physically inadmissible a>c points. Both founder governments STRICTLY vote M, with independent initiative and majority, so L is impossible. All coefficient evaluations at BOTH phi endpoints 3/25 and 33/100 are STRICTLY positive (125/125 coefficients for each endpoint). Since each coefficient is AFFINE in phi, positivity holds for EVERY intermediate phi.

For a>3/4, if B>=0 the same political majority mandates M (national tie votes YES). If B<0, both founders strictly oppose intervention. Exact 3D Bernstein signs certify -f_a>0 on eta∈[.10,.14], a∈[.75,1], c∈[.75,1] for ALL phi∈[.12,.33], checking all 224 coefficients strictly at both endpoints. An arbitrarily small unilateral decrease in a of an identical founder therefore raises the firm's profit, and continuity preserves BOTH strict national B<0 vetoes. Hence no such private L profile is an initial Nash equilibrium. This proves no 2-O/1-N L pure SPE **over the entire eta,K,phi box**.

Optional outer coefficientwise certificate bounds (not the economic necessary/sufficient interval):
- low-a governmental Bernstein constraint: phi < 866739877263279/1109042981916800 ~= 0.7815205464;
- high-a corporate Bernstein constraint: phi > 1300995704448/10862756385725 ~= 0.1197666281.
These are threshold bounds of the stated polynomial-Bernstein method. In particular [.12,.33] lies strictly inside both conditions. They are not proven actual economic transition points.

### 2. All 0/1-O history governments STRICTLY mandate M

When there is no matched OPEN pair, all markets have the baseline N gross national welfare G_N, regardless of whether one firm has sunk setup. All uninvested countries gain

\[
\Delta_N=G_I-K-\phi/2-G_N,
\]
and the previously invested firm's government gains

\[\Delta_O=G_I-G_N-\frac{\phi}{2}(1-c^2)=\Delta_N+K+\frac{\phi c^2}{2}.\]

The initially paid setup K and design capital are sunk on both policy branches; this is why there is no second K in the invested country's retrofit comparison.

At the worst K=14/25, Delta_N is strictly positive whenever

\[
\phi < 2(G_I-G_N-14/25)
=\frac{1345490921}{4004358400}
\simeq0.3360066174.
\]

The entire closed phi∈[.12,.33] lies strictly inside this government approval bound. Thus *all three* national governments strictly prefer mandatory public IS after any NNN or singleton-O initial history, for every c,a. For nO=0/1 this is global private-design policy classification, not a finite grid.

### 3. Public mandate implementation is STRICTLY dominant by every firm

The Stage15 all-active Cournot calculation implies that a firm complying with public O(1,0) earns gross market profit at least isolated gross P_1=3/(4m)=25/33 over every action pattern of the OTHER two firms. A previously N firm must pay at most K+phi/2 to comply. A previous OPEN firm uses the same O family and pays only missing c-capital no more than phi/2; prior fixed setup is sunk. Thus **strict conformity dominates exit for every firm after ANY initial N/O investment history** if

\[
K_{\max}+\phi/2 < 25/33,
\quad\phi<326/825\simeq0.3951515152.
\]

Again the entire interval [.12,.33] satisfies this uniformly in all eta,K and all prior c,a choices. Consequently the governmental policy comparison in cases nO=0,1,2,3 uses the same uniquely implemented public Cournot O(1,0) continuation as Stage19–21. This step is essential: Stage22's broad phi range by itself did not establish dominance for INITIAL N firms.

### 4. Three-O L pure-SPE exclusion from Stage22

Stage22 proves that for all real three-O designs the two redundancy lemmas and the exhaustive non-redundant technical rank-order cases force public M in any hypothetical L-SPE. Exact all-real polynomial-Bernstein certificates cover this for every 0<phi<=452295327/649779200≈.6960754161. Since [.12,.33] lies within that interval, its conclusion applies UNIFORMLY here. This is an exclusion of three-O PRIVATE L SPE, not an assertion that EVERY off-path three-O history mandates M.

### 5. Nonempty SPE: NNN→M and all firms comply

At NNN, the three governments mandate M strictly by part (2), and all firms comply strictly by part (3). If any firm unilaterally switches N to arbitrary O(c,a) at the initial investment stage, the resulting singleton history STILL elicits M and all comply. The deviator's eventual total setup/capital is exactly K+phi(1+a²)/2, while by staying N its total public installed cost is K+phi/2. The deviator's gross Cournot post-M profit is identical, so the difference in payoff is -phi a²/2<=0; no initial deviation strictly improves payoff. This holds over the full REAL triangle including a=0 indifferent alternatives. All government's off-path binary proposal/voting games possess pure best-response continuations; compliance after M is dominant. Thus NNN is an actual pure SPE initial investment profile, and public IS terminal-outcome set is nonempty.

### 6. Exhaustive investment count

| Number of initial OPEN founders | Terminal privately retained L can occur in a pure SPE? | Exact basis |
|---|---|---|
| 0 | No; all governments strictly approve M | ST23.1 part (2) |
| 1 | No; all governments strictly approve M | ST23.1 part (2) |
| 2 | No; firm redundancy plus all-real B or negative f_a dichotomy | ST23.1 part (1) |
| 3 | No; Stage22 exact three-OPEN proof | ST23.1 part (4) |

As all M continuations result in strict universal conformity, every possible pure SPE terminal outcome is IS. NNN→M establishes existence. **This is a full pure-SPE *outcome classification* on a genuine open-dimensional 3D (eta,K,phi) rectangle, holding 4 remaining market primitives fixed**. It remains a sufficient result; it does not prove the EXACT boundary where RS emerges under parameter perturbations.

## Model generality, novelty and next stage

Significant result: full institution-conditioned loss of equilibrium coexistence is robust to simultaneous variation of THREE continuous parameters (eta,K,phi), and the binding sufficient upper phi condition originates in government public-intervention demand, not the private three-O technology dominance. This directly addresses one calibration-specific weakness.

Not proven: a nondegenerate FIVE market-coefficient neighborhood in (v,gamma0,kappa,rho,phi), or a global parameter-region necessary-and-sufficient equilibrium classification, or inclusion of proprietary X/Y, licenses, private C, treasury side payments, negotiation over the public reference. Nor a complete full-text proposition-level novelty comparison to Gandal–Shy (2001), Klimenko (2009), Farrell–Simcoe (2012).

Recommended Stage24: jointly perturb at least v and kappa, using exact multivariate Bernstein over a small rational parameter box, taking special care of the Stage22 structural 11 coefficient zeros (some disappear under generic perturbations), and rerun EVERY component of ST23 including low/high-a private 2-O signs, public adoption, and all government votes. Only if a full open-box certificate passes should we claim greater than 3D robustness. Subsequently identify endogenously characterized phase thresholds and assess whether stronger dimension-free sufficient inequalities can be stated.

## Verification

Run python code/stage23_full_spe_phi_interval.py and full CI .github/workflows/stage23-full-pure-spe-phi-window.yml. The new script rederives 2×(125+224) exact 3D Bernstein checks, computes boundary rational thresholds, and checks uniform government votes, all-firm mandatory conformity and full REAL initial NNN deviation logic; it runs alongside Stage11, Stage19, Stage20, Stage21 and Stage22 exact certificate source in CI.
