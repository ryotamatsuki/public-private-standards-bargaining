# Stage 24 — Exact five-parameter robustness of the public-IS pure-SPE terminal outcome

Date: 2026-10-14 JST. Stacked on Stage23 Draft PR #51. All previous PRs remain Draft; manuscript not edited.

## ST24.1: 5D continuous global terminal-outcome theorem

**Model:** Three firms independently choose N or any real OPEN O(c_i,a_i) with 0<=a_i<=c_i<=1; three national governments each have proposal rights over legally existing public O(1,0); majority two of three YES votes mandates M, ties YES; no intergovernmental transfers, patented X/Y, licensing or private C-certification; sunk initial open development setup K, incremental missing c-only retrofit; 3-firm differentiated Cournot market with pairwise min technology and government objective national firm net profit plus local market CS.

Maintain v=.01, gamma0=.14 and m=1-v=.99. Let the five OTHER coefficients vary **independently and simultaneously** over their full closed boxes:

\[
\boxed{\begin{aligned}
\eta&\in[.10,.14],&K&\in[.54,.56],\\
\phi&\in[.13,.30],&
\rho&\in[.319,.321],&
\kappa&\in[.019,.021].
\end{aligned}}
\]

**Theorem ST24.1:** For EVERY such parameter combination and EVERY full-real set of individual firm technical actions, **every pure-strategy SPE ends in public mandatory O(1,0) universal IS**. At least one such SPE exists: the NNN initial history, followed by public M supported by every government and strictly dominant all-firm conformity. This is terminal *outcome* uniqueness, NOT initial SPE profile uniqueness, NOT mixed-SPE classification, NOT a full seven-parameter neighborhood, and NOT a necessary/sufficient phase boundary.

## Exact non-grid algebra: 251,436 multivariate Bernstein entries

The source reconstructs all separate cases with SymPy rational polynomials and a completely independent separable power-to-tensor-Bernstein change of basis. The technical-order cases are each certified over the FULL technology continuum, rho and kappa intervals. At both phi endpoints 13/100 and 3/10 the polynomial coefficients are verified nonnegative; since each policy/firm-deviation polynomial is **affine in phi**, the signs hold for every interior phi as well.

| Subcase per phi endpoint | Parameters inside polynomial | Checked coefficients | Zeros | Implication |
| --- | --- | ---: | ---: | --- |
| 2-O pair: low a<=3/4 | eta,a,c,rho,kappa | 1,125 | 0 | both founders strictly vote YES for public M |
| 2-O pair: high a>=3/4 | eta,a,c,rho,kappa | 2,688 | 0 | private f_a strictly NEGATIVE |
| 3-O aligned min-c/min-a | four design coordinates,rho,kappa | 9,450 | 15 | G2,G3 vote YES |
| 3-O crossed tied maxima, G1 | four design coordinates,rho,kappa | 59,535 | 105 | G1 votes YES |
| 3-O crossed tied maxima, G2 | four design coordinates,rho,kappa | 52,920 | 105 | G2 votes YES |

Per phi endpoint 125,718 coefficients; over both endpoints **251,436**. The three-O zeros are *structural* nonnegative coefficients, not failed tests. Full Cournot active solution is valid: pair effects 0<=b_ij<=gamma0+kappa_max=.161, FOC diagonal 2m=1.98>2*.161; maximal output each firm <=(1+rho_max)/(2m) and the other two cannot jointly eliminate a firm's positive best response because 1-2*.161*(1+rho_max)/(2m)>0.

## Economic and sequential-equilibrium proof

**Case nO=0,1:** When there is no matched OPEN pair, original N market gross G_N applies. Full public national gross G_I(rho) is increasing in rho. A previously N government's *minimum* M-L gain at rho=.319, phi=.30, K=.56 is the exact positive rational

\[
G_I(.319)-G_N-.56-.30/2 =
\frac{198040669721}{12813946880000}>0.
\]

Any sole existing O developer government's gain is higher than this by K+phi*c²/2, and therefore every one of the three governments strictly supports M after NNN or singleton O, regardless of individual c,a.

**Public implementation at ALL histories:** Even against any combination of rival exit/compliance actions, a public O(1,0) adopter earns at least the isolated gross Cournot profit 3/(4m)=25/33. A prior N firm spends at most K+phi/2; a prior O developer spends at most phi/2 additional (its original K is sunk). At the worst corner the strict conformity gain is bounded below by

\[
25/33-.56-.30/2=157/3300>0.
\]

Thus every firm has a STRICTLY dominant mandatory conformity action and the all-conforming public Cournot outcome is unique.

**Case nO=2:** Stage19's general cost-redundancy lemmas remain valid for any phi>0. If unequal a, the unique higher-a founder saves sunk capital by reducing a to partner a, without affecting the market or votes; if c unequal, the higher-c founder can reduce to partner c without provoking M and strictly raises its payoff under L. Therefore a hypothetical private L pure-SPE must have identical real O(c,a) founders. For a<=.75, both governments strictly favor M by the exact 5D low-a Bernstein certificate. If a>.75, either they support M or the government rejection B<0 and strict f_a<0 allow a profitable sufficiently small unilateral reduction in a with L persisting. All cases contradict a private L-SPE.

**Case nO=3:** Stage21's corporate cost-redundancy reductions extend to all phi>0. In a putative L-SPE the maximum a and maximum c must each be tied across at least two firms. Sort the three c choices; if the smallest c investor also has the smallest a, the aligned full-continuous G2/G3 YES certificate forces M. Otherwise the only possible tied-max crossing configuration has c1<=c2=c3 and a1=a2>=a3 (after permutation), and its two crossed-case certificates force G1 and G2 YES. Thus a three-O L-SPE cannot occur, even for six independent continuous technical investments.

**Existence:** At NNN all governments strictly mandate public M and all firms strictly conform. A single firm's unilateral deviation to any feasible O(c,a) yields singleton-O history, still unanimously mandatory M and unique compliance. Its final public Cournot gross payoff is unchanged, while its additional sunk investment relative to N equals phi*a²/2>=0; no profitable deviation. Every government finite binary proposal/vote subgame has a pure sequential best-response continuation. This establishes nonempty pure SPE (no vacuity).

The exhaustive nO=0,1,2,3 cases and mandatory conformity together prove **one final public IS pure-SPE OUTCOME TYPE** throughout the 5D box.

## Caveats and next gate

This is a sufficient box around the baseline rho=.32,kappa=.02; its edges do not denote an actual economic bifurcation. The other two primitive coefficients v,gamma0 remain fixed, so there is **NO** current evidence for full 7D robustness, and no exact worldwide necessary/sufficient phase diagram. Assumptions exclude private patented X/Y, recognition C, side payments and mixed equilibria; public O(1,0) is imposed as legally available, proposal rights are universal and vote ties select M. Literature novelty relative to Gandal–Shy, Klimenko and Farrell–Simcoe is not yet established at the full proposition/proof level.

Next Stage25: vary v,gamma0 as well using exact rational Bernstein in their feasible positive-matrix neighborhood; if possible prove a true 7D sufficient open set. Then extract economically interpretable threshold primitives and institutional interaction parameters rather than treating conservative Bernstein box boundaries as policy thresholds.

## Reproduce

Execute Python 3.12 / SymPy source code/stage24_five_parameter_full_spe_certificate.py. GitHub Actions workflow .github/workflows/stage24-five-parameter-certificates.yml runs all Stage11/19/20/21/22/23 exact proofs first and the 251,436-coefficient Stage24 certificate. No floating-point sampling is used as evidence of the theorem.
