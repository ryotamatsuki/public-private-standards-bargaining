# Stage 2 Design Decision — Endogenous Product Differentiation Under Nested Regulatory Interoperability
2026-10-14 JST | Parent Stage1 Draft PR #30. **DESIGN PROTOCOL AND INDEPENDENT ALGEBRA AUDIT ONLY.** This file does not claim to solve a new SPE or to establish novel general equilibrium economics.

## 1. Author question and pivotal diagnosis

Current 3-country model endogenizes the common standards depth `s` only, with exogenous `eta` governing outsider-versus-insider product substitution:
`b(s)=gamma0+(kappa-v)s`, `d(s)=gamma0-eta*s`. The source model consequently does **NOT** let firms independently decide how differentiated their products become; stronger standardization mechanically moves the substitution coefficient, rather than firms designing their product features in response to regulator policy. The later government licensing/recognition game of PR #30 also fixed `s=1` for solvability. It would be incorrect to describe it as a complete strategic model of endogenous product design.

**Recommended institutional distinction:** The government sets the publicly required common INTERFACE and (if product-prescriptive regulation) permitted range of design variants; firms choose the *actual* compatible technology level, product attributes and compliance/exit. A government normally does not directly choose proprietary industrial product-design vectors unless it purchases or specifies a complete product; a private company cannot unilaterally bind other firms or countries to public regulatory terms.

## 2. Minimal coherent multi-dimensional characteristic map

Preserve the ORIGINAL six positive market primitives
`theta=(v,gamma0,kappa,eta,rho,phi)`. The extension introduces firm i's TWO strategy variables:
`t_i in [0,1]`: privately deployed optional common technical layer;
`delta_i in [0,1]`: ONE-DIMENSIONAL noninterface/product-attribute LOCATION.
Introduce only ONE additional physical parameter `chi>0` for real private differentiated design investment `chi*delta_i^2`, without which an arbitrary optimum or costless corner choice risks becoming vacuous. It is a new modeling assumption, not claimed to be part of frozen six-primitive benchmark.

Government chooses publicly mandated open core `r in [0,1]`, and regulatory scope `h in {0,1}`:
- h=0: **interface-only** regulation; product characteristics `delta_i` unrestricted except by general market feasibility, including at r=1.
- h=1: **product-prescriptive** regulation; among regulated/compliant products `|delta_i-delta_j| <= 1-r`, so a stronger mandate additionally constrains differentiation on the SPECIFIC REGULATED CHARACTERISTIC. This is not a general claim that standardized connectors prohibit diversity in all unrelated product attributes.

For a compliant pair of active firms `i,j`, bilateral interoperability depth is
`c_ij(r,t_i,t_j)=r+(1-r)*min(t_i,t_j)`.
The technical-efficiency index of a compliant producer i is
`h_i=r+(1-r)*t_i`, `z_i=1+rho*h_i`.
(For any noncompliant or legally excluded product, the public-r rule cannot be mechanically applied; its own market-access/exit action is modeled explicitly.)

The symmetric quadratic utility/cross-substitution matrix is then
`M_ii=1-v=m`,
`M_ij=gamma0+(kappa-v)*c_ij - eta*(delta_i-delta_j)^2` for i!=j.

The product characteristics are now actual firm decisions and may remain distinct even with full interface compatibility, except to the extent specifically forbidden by product-prescriptive h=1. **Market compatibility** `c_ij` and **product differentiation** `(delta_i-delta_j)^2` are structurally distinct. Demand matrix SPD and substitute conditions must be enforced or proved for the admissible action domain, not naively presumed from the old exogenous theta region.

Conditional on successful adoption/implementation and firm i still operating, private worldwide payoff is
`P_i=3m*q_i^2 - phi*h_i^2 - chi*delta_i^2`,
for 3 identical segmented Cournot markets, with `q` solved from full active-set complementarity:
`[M+diag(m)]q = (z_1,z_2,z_3)'` on active firms; inactive q_i=0 and its marginal residual <=0.
Government i obtains its resident producer's net profit plus domestic destination `CS=(q'Mq)/2`. Any firm may exit for an outside payoff (take 0 in initial benchmark) and does not pay future adoption cost when it does not implement; careful treatment of sunk design costs when exiting is crucial (sunk outlays do not return on exit).

**Historical benchmarks included as restricted strategy profiles** (NOT unrestricted new-game equilibrium):
- Original RS(s) TECHNICAL COEFFICIENTS: public core r=0, t1=t2=s,t3=0; delta1=delta2=sqrt(s),delta3=0. Then `c_12=s,c_13=c_23=0`, `M_12=gamma0+(kappa-v)s=b(s)`, `M_13=M_23=gamma0-eta*s=d(s)`; z1=z2=1+rho*s, z3=1. Historical profit accounting recovers exactly ONLY if new design cost chi=0 or the design cost is explicitly subtracted.
- Original IS(s): public core r=0, all t_i=s, all delta_i equal (e.g. 0), so c_ij=s and all offdiagonal coefficients equal old b(s), all z_i=1+rho*s. Thus private IS is feasible WITHOUT govt adoption.
- A fully universal public interface core r=1 with h=0 forces c_ij=1 but does NOT force delta_i=delta_j or product identity, avoiding a common conceptual error.
- Current PR #30 s=1/open-technology mandate is a restricted game under delta_i exogenously equal or under new assumptions guaranteeing that profile, not automatically an SPE of this extension.

## 3. Strict algebraic warning: introducing costly differentiation can kill old Stage5B mechanism

If one merely replaces `d(s)=gamma0-eta*s` by `d(delta)=gamma0-eta*delta` or `gamma0-eta*delta^2` and charges `chi*delta^2`, the outsider-zero KKT branch has
`q_1=q_2=z/(2m+b)`, `q_3=0`. Neither insider quantity nor domestic CS depends on its coefficient d to the inactive outsider. Holding insider characteristic profiles identical (so their mutual b is unaffected to first order) and holding the competitor outsider inactive with STRICT negative entry residual, an insider with positive delta can locally lower its characteristic investment with no first-order loss of quantity profits or CS, saving `2chi*delta` at the margin. Hence **a symmetric positive distinctiveness design is not individually optimal in that regime** under positive chi when it only affects inactive-outsider substitutability. Exact code asserts this sign.

This is a serious ECONOMIC identification issue, not merely a proof nuisance: the old theta variation in exogenous eta that produced outsider reentry does not imply a similar equilibrium response when firms strategically choose their characteristics. Firms may instead differentiate strongly FROM EACH OTHER (lower b_12), creating ASYMMETRIC endogenously differentiated products. The new game therefore must solve each firm's delta_i BR jointly, including asymmetric and corner solutions, rather than force delta1=delta2 and then report a fictitious equilibrium. This first result is a conditional LOCAL no-positive-design result, NOT a complete equilibrium classification.

## 4. Genuine nested-regulation implementation game

**Stage 0** (technology opportunity and legal rights): distinguish OPEN accessible common interface from proprietary/SEP-protected variants. Model an explicit offer/open-license choice; government cannot mandate access to an unavailable private patent. The engineering feasible set/quality must be specified. Keep licensing fees/transfers distinct from real investment costs.

**Stage 1** firms commit to develop innovations and choose technical capacities and preliminary product locations; private costs can be sunk or contingent, but choose one timing and maintain it consistently.

**Stage 2** public governments (with a specified agenda and cross-border approval rule) choose `(r,h)` from legal options `r<=available_open_technology_depth`. Public regulation sets a minimum standard, not firms' individual independent strategies.

**Stage 3** after policy, each firm independently chooses actual compliance, technical adoption `t_i`, allowed product characteristic `delta_i`, and exit. The feasible firm strategy set is *nested in regulatory decision*:
`A_i(r,h)={t_i,delta_i,comply/exit:0<=t_i,delta_i<=1; if compliant, c_ij>=r and if h=1, |delta_i-delta_j|<=1-r for other covered products}`.
An inter-firm pairwise harmonization constraint couples firms' feasible actions: formulate this as a GENERALIZED Nash game or an agreed compliance technology specification; it is NOT a standard unconstrained best-response game without additional allocation of compliance duties. For technical simplicity, a firm-specific distance to a fixed public reference characteristic is preferable as a first special case, `|delta_i-delta_public|<=1-r`, so each firm's feasible set is independent after policy. This should be the DEFAULT preliminary analytical implementation, with delta_public=0 as choice of coordinate; later broaden to pairwise requirements.

**Stage 4** full NS/RS/IS/coexistence active-set Cournot and national CS/profits; verify SPD, quantities, network utility and correct sunk-cost accounting at EVERY relevant history. An outside firm's q=0 is a true KKT inequality, not an extrapolated negative output.

Use backwards induction; first freeze r and h, compute firms' conditional design/adoption equilibrium; then endogenize regulator r,h; then firms' anticipatory R&D. A claim of a (unique) pure SPE requires strategies and continuation equilibria at every off-path history, and an equilibrium selector when the product-design game has multiple solutions.

## 5. Testable economic propositions (UNPROVED TARGETS unless labeled otherwise)

**ND-1 (verified restricted lemma):** on a strictly binding outsider-zero KKT region, equal positive insider product locations are locally dominated by less costly designs if location shifts only inactive-outsider substitution. This warns against simply turning eta into an endogenous scalar without re-solving.

**ND-2 (target):** nested regulatory scope h may constrain private product variety even with identical public interoperability r; compare marginal CS gains from network compatibility versus CS losses from variety reduction.

**ND-3 (target):** either sub- or supermodular government/firm technical investment may obtain depending on v, kappa, eta and chi: the net adoption value of one player's action depends on the other's. Avoid assuming unconditional complementarity.

**ND-4 (target):** government's optimal r need not equal firms' privately preferred common core; depending on induced characteristic design/entry, public minimum standard may crowd out proprietary market adoption, or unlock international network gains.

**ND-5 (target):** an endogenous market-based proprietary de facto standard may coexist with a mandated open interface, once firm-specific open/proprietary choice and multi-standard consumer demand are explicitly supported.

**ND-6 (target):** the old Stage5B outsider reentry vs public veto thresholds may shift/end/disappear altogether under endogenous delta_i; quantify only after finding global strategic design BR and suitable regularity/existence.

**NO theorem 2–6 is claimed proved by this design-only PR.**

## 6. Research value and prior literature

This is a more economically realistic bridge between GOVERNMENT interoperability requirements and PRIVATE product development than a simplistic government/firm equal veto to a single generic standard. It also makes clear that product differentiation and common-interface standardization are not synonymous.

Crucial antecedent **Spulber (2019), Economic Journal** *Standard Setting Organisations and Standard Essential Patents: Voting and Markets*, DOI 10.1111/ecoj.12606, already combines voting with inventor/adopter markets and describes complementary public/private standards as an institutional possibility; https://academic.oup.com/ej/article/129/619/1477/5364896 . The newly surfaced **Miyashita (2026), Characteristics Design: A Hedonic Approach to Optimal Product Differentiation**, https://arxiv.org/abs/2601.21573 , specifically treats ENDOGENOUS product characteristics and shows that oligopoly equilibria can vary qualitatively and yield different social optimum. The exact scope of its newest working paper must be full-text audited, not assumed from abstract. Add earlier standard-coordination literature: Belleflamme (2002), Ghosh–Morita (2012), Fischer–Serra (2000), Edwards–Poyago-Theotoky (2013), Takarada (2020). A novel fundamental IO theory is NOT certified by this formulation; this remains an applied nested-governance research track.

**Decision:** ACKNOWLEDGE user critique. Add product characteristic choice `delta_i` and design cost `chi` explicitly; do NOT permit government to control all product variety under an interface-only mandate. Preserve source-market benchmark as a restricted profile, and mark earlier RS/IS SPE as fixed-delta submodels only. Next conduct exact Stage2 endogenous private-design best-response and government constrained-optimum solves, using chosen simple private feasible set `|delta_i|<=1-r` only in product-prescriptive policy h=1. No manuscript edits/merges.
