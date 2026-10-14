# Stage 22 — Exact capital-curvature robustness, boundary of theorem, and adversarial theorem-level prior-art audit

Date: 14 October 2026. Builds on the exact, full-real Stage21 3-O nonintervention exclusion and the conditional full reduced-game pure-SPE outcome classification. This is a **research audit**, not a manuscript amendment. No old Draft PR merged.

## New exact theorem: 3-OPEN exclusion over a nontrivial phi interval

Maintain ALL other structural and technology coefficients exactly as in Stage21:
\[
m=.99,\quad \gamma_0=.14,\quad\kappa=.02,\quad v=.01,\quad\rho=.32;
\]
three countries/firms; open designs O(c_i,a_i), 0<=a_i<=c_i<=1; O(1,0) mandate; universal independent governmental agenda authority; majority 2/3; votes on ties YES; same sunk-stock and positive-part O-family retrofit. K,eta remain in the old Stage15 adoption-validity region [.54,.56] and [.10,.14].

**ST22.1 (one-dimensional capital-curvature robustness):** The Stage21 theorem that **no initial profile with all three firms investing O can be a pure-strategy SPE with final L** remains true for EVERY EXACT REAL

\[
0<\phi\leq\Phi_*:=\frac{452295327}{649779200}=0.6960754160798006\ldots
\]

(provided public mandatory conformity continues to follow as specified). This is a genuine **continuum certificate**, not pointwise sensitivity experiments.

Reason: ST21.1's unique-largest-a redundancy provides a strictly profitable capital saving proportional to phi; ST21.2's unique-largest-c reduction provides another strictly positive saving under L. Both reductions preserve pairwise-min technology and the relevant government voting outcome for every phi>0. Any candidate L-SPE therefore must have tied a maxima and tied c maxima. For the two exhaustive remaining order types, the Stage21 policy-gain polynomial has an EXACT AFFINE representation in phi:

\[
N_j(\phi)=A_j-\phi B_j,\qquad N_j=2D^2\,\Delta_j
\]

with strictly positive D from Cournot diagonal dominance. Each tensor-Bernstein coefficient is therefore alpha-phi*beta. Compute its exact feasible interval analytically: beta>0 requires phi<=alpha/beta, beta<0 requires phi>=alpha/beta, beta=0 requires alpha>=0. No floating point enters the certificate. Intersect all 5,985 such inequalities.

| Exhaustive technology order case | Necessary majority government's welfare polynomial | Bernstein coefficients | Coefficient upper threshold | Structural zeros |
|---|---|---:|---|---:|
| smallest c also smallest a | G2 (G3 weakly higher) | 630 | 29340729/35123200 ~= 0.8353660543 | 1 |
| crossed maximal ties | G1 | 2835 | **452295327/649779200 ~= 0.6960754161** | 5 |
| crossed maximal ties | G2 | 2520 | 29340729/35123200 ~= 0.8353660543 | 5 |

Every coefficient is nonnegative for 0<=phi<=Phi*. There are 11 coefficients that are identically zero in phi in these polynomial expressions. The resulting bound is **the exact upper limit of the CURRENT tensor-Bernstein sufficient certificate**, **NOT** proof that the economic theorem fails above Phi*. At phi=0, the strict firm cost-deviation lemmas collapse; thus phi=0 is correctly **excluded** from ST22.1 even though the government welfare polynomials remain nonnegative.

The baseline phi=.14 lies strictly within the interval. In particular a nontrivial neighborhood [0.13,0.15] is rigorously covered for this *three-firm no-L-SPE* result. The interval changes ONLY phi; it does not establish robustness to m,gamma0,kappa,v,rho.

### Crucial scope separation

**DO NOT claim:** “All pure SPE end in public IS for every phi in (0,Phi*].” Stage21's terminal-outcome corollary additionally invokes (a) Stage19 elimination of two-open L profiles; (b) Stage20 policy at 0/1 O histories; (c) Stage15 unique all-firm conformity after M; (d) NNN→M initial SPE existence. Those claims were previously certified with phi=.14, not uniformly on (0,Phi*]. A large phi may cause a firm to exit rather than comply, or invalidate Stage19's private-profit/landscape bounds. ST22 proves **one independent major case** is robust; extending the entire corollary needs re-running and generalizing the other three proof families with variable phi and verifying all their strict inequalities.

There is a standard continuity argument for strict inequalities away from structural zero faces, but that alone does NOT supply a numeric joint open neighborhood in all five coefficients: Stage21's Bernstein proof has boundary zero coefficients, and other modules have fixed nominal parameters. Do not promote merely sampled perturbations or an unquantified continuity intuition to a proven full-dimensional open set.

## Prior-art audit: precisely what is and is not previously known

This is a **screening-level theorem comparison** based on published abstracts and accessible publisher pages (full derivations not all audited). No claim of comprehensive proof-level priority or full-text theorem correspondence is warranted yet.

1. **Katz & Shapiro (1985), American Economic Review, “Network Externalities, Competition, and Compatibility.”** General network compatibility, private adoption, and standardization incentives already established. Its standards discussion includes conditions under which parties' veto/no-side-payment blocks adoption. **NOT novel here:** strategic compatibility, adoption coordination, welfare divergences, the existence of vested private vetoes. **Candidate incremental difference:** separate *national* governments with universal agenda rights voting after independently sunk continuous 3-firm technology investment, and a complete no-private-L-SPE argument. https://ideas.repec.org/a/aea/aecrev/v75y1985i3p424-40.html

2. **Farrell & Saloner (1988), RAND Journal of Economics, “Coordination through Committees and Markets.”** Committees, preemptive irrevocable standard choice, and hybrid coordination already compared. **NOT novel:** institutional organization of standardization and the effect of ex ante commitments. **Candidate difference:** state-level majority veto with explicit 3-country national payoffs and a continuous min-pair Cournot production game. https://ideas.repec.org/a/rje/randje/v19y1988isummerp235-252.html

3. **Gandal & Shy (2001), Journal of International Economics, “Standardization policy and international trade.”** **CLOSEST international-standardization/three-country comparator.** Governments strategically recognize foreign standards, with network effects and conversion costs; two-country standardization unions may exclude a third country when conversion costs are large; full mutual recognition when network effects are important. **NOT novel:** three-country regional-vs-universal standardization, government incentives, conversion costs, public welfare coalition conflict. **Candidate difference:** legislation proposal rights and unanimity/majority interactions acting on privately and continuously pre-invested OPEN technical designs, a unique public mandatory terminal SPE outcome under majority-plus-universal agenda, contrasted to coexistence under unanimity. Critically compare timing/action spaces/coalition formation and full relevant propositions before claiming a substantive theoretical breakthrough. https://doi.org/10.1016/S0022-1996(00)00067-2

4. **Jensen & Thursby (1996), International Economic Review, “Patent Races, Product Standards, and International Competition.”** International product standards, endogenous R&D competition, government's anticipatory commitments and ex-post time inconsistency already exist. **NOT novel:** pre-standard technology investment as a policy-relevant strategic choice, dynamic standard time consistency. **Candidate difference:** 3-government agenda/vote structure, OPEN nonpatented technologies, pairwise-min two-dimensional technical investments and quantified pure-SPE elimination, without patent races/licensing. https://www.nber.org/papers/w3870

5. **Lerner & Tirole (2006), American Economic Review, “A Model of Forum Shopping.”** Sponsors choose standard certifiers/forum policies as a strategic response to user adoption and design. **NOT novel:** institutional selection and regulatory-friendly forums endogenous with sponsor design. **Candidate difference:** endogenous *country voting rights* over an already lawful public mandate, rather than sponsor choice of certification forum. Also *our minimal game EXCLUDES certification C*, limiting direct coverage of the earlier theory. https://www.nber.org/papers/w10664

6. **Klimenko (2009), Journal of International Economics, “Policies and international trade agreements on technical compatibility for industries with network externalities.”** **CLOSEST joint government-policy/competition comparator.** Competing governments strategically set compatibility policies in international oligopoly/trade networks; both excessive and insufficient standards and negotiated agreements arise. **NOT novel:** strategic government compatibility intervention, Cournot/market-welfare tradeoffs, interstate standard agreements. **Candidate difference:** discrete 3-government voting/agenda rule as an institutional variable, and global pure-SPE terminal outcome after 3 independent continuous OPEN capital stock decisions. https://doi.org/10.1016/j.jinteco.2008.08.005

7. **Farrell & Simcoe (2012), RAND Journal of Economics, “Choosing the rules for consensus standardization.”** **CLOSEST mechanism/contribution challenge.** Consensus rule choice, policy-dependent bargaining/delay, and ex ante incentives to improve proposals already examined. **NOT novel:** consensus governance can affect ex ante technology investments and standard-setting outcomes. **Candidate difference:** explicit multi-government voting/quorum and national right-to-propose combination can eliminate *all private terminal pure-SPE* under continuous sunk Cournot investment, conditional on a public alternative. Without sharp economic explanation beyond rule comparison, this may be viewed as a special calibrated example of established mechanism-design intuition. https://doi.org/10.1111/j.1756-2171.2012.00164.x

8. **Simcoe (2012), American Economic Review, “Standard Setting Committees: Consensus Governance for Shared Technology Platforms.”** Empirical-plus-theoretical link of bargaining/conflicts to standard-setting delay. **NOT novel:** conflicts inside standard governance. **Candidate difference:** cross-national public regulatory authority that overrides a private standard after sunk technology investments; no empirical test provided here. https://doi.org/10.1257/aer.102.1.305

### Conservative assessment of contribution after Stage22

**Credible demonstrated model-specific result:** Under a particular open/nondevelopment two-action-family game, exogenous immediately accessible full public compatibility, no treasury transfers, symmetric markets, selected Cournot/min-pair technology and sunk capital accounting, changing both the government approval quota and proposal-right allocation transforms feasible original private-RS/public-IS coexistence into unique public-IS pure-SPE terminal outcome. The 3-OPEN no-private-L case is robust to a wide ONE-PARAMETER change in phi.

**Most serious novelty risks:**
- Gandal–Shy (2001) already has three countries and nontrivial regional/universal coalition behavior. Calling the existence/abolition of RS novel without the governmental institutional game distinction is incorrect.
- Farrell–Simcoe (2012) already ties institutional standard-setting rules to ex ante investment and consensus equilibria.
- Klimenko (2009) already ties governments' compatibility policies to network effects and international competition.
- The exogenous public O(1,0), costless universal proposal, government tie-YES, exactly 3 governments, 2-of-3 vote and no private X/Y or licensing may mechanically drive the uniqueness result. The paper needs a general economically meaningful threshold or robust open-dimensional parameter region and a clean counterfactual.
- The Stage21 classification is **pure terminal outcomes** only; not necessarily unique initial SPE or mixed-strategy SPE. Calling it “full equilibrium uniqueness” would be inaccurate.
- A partial robustness result for phi cannot rescue a fixed-coefficient result from calibration-specific concerns; other coefficients and governmental rules must be audited.

**Next mathematically precise gates (Stage23):** derive Stage19 2-O theorem, Stage20 NNN/1-O vote and compliance, and Stage17 NNN→M firm-deviation inequalities as SYMBOLIC functions of phi, then certify a common phi interval centered on .14. Following that, perturb (v,gamma0,kappa,rho) with exact interval-Bernstein or parameter-space Bernstein to prove a nonempty **multidimensional** robustness rectangle (structural boundary zeros handled explicitly). Independently read and compare *theorems and proofs* from Gandal–Shy 2001, Klimenko 2009 and Farrell–Simcoe 2012, before journal-level quality or novelty claims.

## Reproducibility

File code/stage22_exact_phi_robustness.py independently reconstructs both four-dimensional technology order cases with SymPy rational arithmetic, computes 5,985 coefficientwise affine-in-phi inequalities, and ASSERTS the exact common threshold. Stage22 CI runs Stage11, Stage19, Stage20, Stage21 and this additional coefficient-bound script. Exact denominators are positive throughout the relevant market region by the previously verified strict Cournot diagonal dominance (m>.99? actual m=.99 and abs offdiag <=.16; the three-firm FOC has diagonal 2m and offdiagonals b_ij).

No source claims priority on uninspected full texts.
