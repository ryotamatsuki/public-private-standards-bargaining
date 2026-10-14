# Stage 21 — Complete pure-SPE terminal-outcome classification: 3 countries with universal majority initiative

14 October 2026. Stacked directly on Stage20 (Draft PR #48); Stage19 (Draft PR #47) remains unmerged.

## Main theorem (ST21)

In the **minimal** three-country game with three independently investing OPEN firms, no full-real 3-O initial profile can be a pure-strategy SPE **and** sustain L (nonintervention). Together with Stage19's exclusion of 2-O/1-N lasting L pure SPE and Stage20's mandatory M after 0/1-O histories, **every pure-strategy SPE in the reduced model yields publicly mandated O(1,0), international IS, as its terminal outcome**. Public IS exists through the previously proved NNN→M SPE. This is an **outcome** uniqueness theorem, NOT uniqueness of initial investment choices or a theorem that all arbitrary off-path 3-O histories cause public M.

## Maintained game and model

Three simultaneous firms choose N or an independent O(c_i,a_i), 0<=a_i<=c_i<=1. The universal technical reference O(1,0) is exogenously legally public. After private technologies, **each** of the three governments may propose M; a proposal passes by **two YES votes**, and national indifference votes YES. Post-M adoption is uniquely all complying (Stage15). Cournot pair technology depends on pairwise minimum c and a, with a maximum-of-pair compatibility demand intercept. Fixed (v,gamma0,kappa,rho,phi)=(.01,.14,.02,.32,.14), eta in [.10,.14], setup K in [.54,.56]. Only O and N available; NO X/Y proprietary patent standards, private certification, licenses or side payments. Retrofitting an existing OPEN firm does not charge K a second time; only remaining missing positive c-capital is paid; sunk a stock receives no refund. National welfare = local firm profit plus common national consumer surplus.

After **three O** investments, K is sunk by all and eta does not enter any bilateral market matrix (there is no unmatched different-label outsider). With m=.99, private Cournot output q_i and consumer surplus CS, define G_i^L=3m q_i²+CS. For a full public O(1,0) all-firm Cournot outcome let G_I denote the same national gross-profit-plus-CS expression before capital and setup fees. The EXACT government policy-gain identity is

\[
\Delta_i=W_i(M)-W_i(L)=G_I-G_i^L-\frac{\phi}{2}(1-c_i^2).
\]

K and sunk a-capital cancel in the policy difference. The 3-O government subgame can therefore be studied for all K,eta in the rectangle with a six-real-variable problem in the c_i,a_i.

## ST21.1: maximum-a strict corporate redundancy

If a single firm i has a_i>A=max_{j≠i}a_j, reducing a_i to A preserves every pair minimum in a and c, so all private Cournot outputs, product interactions and consumer surplus are unchanged. In the L continuation, firm i saves exactly phi(a_i²-A²)/2. Under M, total sunk plus retrofit investment equals K+phi(1+a_i²)/2, so the same strict saving arises, with identical government M-L preferences. All governments' policy decisions therefore remain unchanged. Any initial pure SPE with three OPEN investors must have its highest a attained by **at least two firms**.

## ST21.2: maximum-c strict corporate redundancy conditional on L

Suppose a putative 3-O pure SPE yields L, and c_i>C=max_{j≠i}c_j. From ST21.1, maximum a is tied; hence a_i<=C (another firm with a_j>=a_i obeys a_j<=c_j<=C). The legal deviation c_i→C leaves all pairwise min(c) and min(a), private Cournot and CS unchanged. Its L real capital falls strictly by phi(c_i²-C²)/2. Under M its total capital K+phi(1+a_i²)/2 is **unchanged**. Hence the deviant government's preference Delta_i only decreases; other two governments' policy preferences are invariant. As before the policy was L, losing YES support cannot turn L into M under universal 2/3 initiative. So L persists and firm i strictly profits. Contradiction. Any putative three-O L-SPE therefore also requires maximum c to be attained by **at least two firms**. This lemma does NOT assert profitable unique-max-c deviation if the original outcome was M.

## ST21.3: smallest c also has smallest a

Relabel c1<=c2<=c3 and assume a1<=min(a2,a3). Set d=min(a2,a3), where a1<=d<=c2. Then pair (1,2) and (1,3) have exactly (c1,a1), pair (2,3) has (c2,d). Cournot makes q2=q3, regardless of c3,a3 above pairwise minima. Introduce

\[
b_1=\gamma_0+\kappa a_1-vc_1,\quad b_2=\gamma_0+\kappa d-vc_2,
\quad z_j=1+\rho c_j \ (j=1,2).
\]

Define D=2m(2m+b2)-2b1², Q1=(2m+b2)z1-2b1z2, Q2=2mz2-b1z1, with q1=Q1/D and q2=q3=Q2/D. The consumer-surplus numerator is C=mQ1²+2mQ2²+4b1Q1Q2+2b2Q2² (so CS=C/(2D²)). Then

\[
2D^2\Delta_2=(2G_I-\phi(1-c_2^2))D^2-6mQ_2^2-C.
\]

Parametrize the WHOLE feasible sector as c2=t, c1=ts, a1=tsw, d=a1+(c2-a1)h, with all (t,s,w,h) in [0,1]^4. The numerator polynomial's full tensor-Bernstein expansion has degrees (6,5,4,2): **629 positive coefficients and 1 zero**. D>0 by strict diagonal dominance. Thus Delta2>=0 throughout the closed continuum. Further Delta3-Delta2=phi(c3²-c2²)/2>=0 since the two private gross welfares coincide. **Governments 2 and 3 vote YES**, including every boundary and tie.

This covers both orderings of a2 versus a3; it is strictly more general than equal c_i or perfectly aligned c/a rankings.

## ST21.4: the ONLY other surviving technology-order type (crossed maximal ties)

After ST21.1/ST21.2 the two highest c values and the two highest a values are shared. If ST21.3 does not apply, a relabeling yields c1<=c2=c3, a1=a2>=a3. All feasible such designs are exactly parameterized by

\[
c_1=ts,\quad c_2=c_3=t,\quad a_1=a_2=tsu,\quad a_3=tsuw,
\qquad (t,s,u,w)\in[0,1]^4.
\]

Let p=gamma0+kappa*a1-v*c1, r=gamma0+kappa*a3-v*c1, b=gamma0+kappa*a3-v*c2. Solve the general **asymmetric** exact 3×3 Cournot linear system with diagonal 2m, off-diagonal p,r,b, and intercepts (1+rho*c1, 1+rho*c2, 1+rho*c2). D>0 is its determinant, and q_i=Q_i/D by the rational adjugate. Let C=mΣQ_i²+2(pQ1Q2+rQ1Q3+bQ2Q3). Then the exactly computed polynomial numerator satisfies

\[
2D^2\Delta_i=(2G_I-\phi(1-c_i^2))D^2-6mQ_i^2-C.
\]

Exact tensor-Bernstein certificates for all real parameters:

| Government | Numerator polynomial degrees | Positive coefficients | Zero coefficients | Result |
| --- | --- | --- | --- | --- |
| G1 | (8,8,6,4) | 2,830 | 5 | Delta1>=0 |
| G2 | (8,7,6,4) | 2,515 | 5 | Delta2>=0 |

All **5,345** coefficients in the crossed case are nonnegative (no grid/approximate signs). Thus G1 and G2 approve M for **every** crossed-ties profile. The conclusion includes full asymmetry of private Cournot output and costs.

## Proof by exhaustion, and limits

A hypothetical three-O L pure SPE must have nonunique maximum a (ST21.1) and nonunique maximum c (ST21.2). Sorting c, either the smallest-c investor also has smallest a, activating ST21.3 and passing M, or the unique remaining order is the crossed-ties case ST21.4, also passing M. Both contradict L. These alternatives partition the entire putative L-SPE set over the full continuous real technology triangle, including zero investments, equalities and corners. **No lasting triple-OPEN privately controlled pure-SPE exists under 2/3 majority and universal proposal rights.**

By Stage19, also no 2-OPEN/1-N L pure SPE survives; by Stage20, all 0/1-OPEN histories enact M. The existing NNN→M SPE establishes nonemptiness. Therefore **the unique terminal pure-SPE equilibrium outcome is mandated public IS** (but potentially multiple initial strategies and political voting histories).

The policy proposition is intentionally **weaker** than “M always passes at every 3-O history”; firm-investment deviations are part of the proof. Exact coefficient values are fixed and the theorem has not been generalized to arbitrary (v,gamma0,kappa,rho,phi), mixed equilibria, additional standards X/Y, patented platforms, compulsory license pricing, public C-certification or different constitutional rules. Prior unanimity/exclusive-agenda private-RS coexistence remains a separate comparator.

## Verification

Run python code/stage21_three_open_global_no_private_spe.py. SymPy uses exact multivariate rational coefficients and **5,985** Bernstein entries; the script also checks two independent rational-Fraction Cournot witnesses using Stage5 and the wasteful-capital identities. **Correct full tally: 630 + 2,835 + 2,520 = 5,985 coefficients, 5,974 strictly positive and 11 zero.** CI path .github/workflows/stage21-global-public-spe-closure.yml executes Stage11, Stage19, Stage20, Stage21 proof chains. Previous PRs remain DRAFT, without manuscript modifications or branch merges.

Next research step: adversarial independent verification of the cross-order exhaustive dichotomy, then journal-level novelty audit comparing the precise all-pure-outcome theorem to bargaining/standardization institutional theory; consider strengthening from one calibrated coefficient vector to a symbolically certified neighborhood rather than adding more institutions.
