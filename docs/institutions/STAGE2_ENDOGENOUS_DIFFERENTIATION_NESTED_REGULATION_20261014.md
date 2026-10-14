# Stage 2 — Endogenous Product Differentiation, Ghosh–Morita Competition, and Nested Public Standards
2026-10-14 JST | New *scoped applied model* stacked on Draft PR #30. User explicitly authorized revisiting product differentiation decisions, government/private authority over design and nested regulatory requirements. No manuscript rewrite, no claim of a new general IO theorem.

## 1. Key diagnostic: the prior reduced-form example did not deliver the requested intra-coalition competitive intensification

Original R/IS one-depth Cournot matrix had insiders' substitution `b(s)=gamma0+(kappa-v)s` and outsider substitute effect `d(s)=gamma0-eta*s`. This already has a Ghosh–Morita-inspired distinction between insider and outsider pairs, but it does NOT make product similarity `endogenous` independently of `s`. Critically the previous welfare-selection witnesses used `kappa=.15<v=.39 or .41`: hence `b'(s)=kappa-v<0`. In those particular examples deeper common standardization actually REDUCED the insider substitution coefficient. It is **wrong** to sell those earlier witnesses as proof that product uniformity intensified insider product competition. New witnesses must ensure `kappa>v` whenever the inside-competition-intensifying channel is invoked.

Ghosh & Morita (2012), *Competitor Collaboration and Product Distinctiveness*, IJIO 30(2):137–152, DOI 10.1016/j.ijindorg.2011.07.003, https://www.sciencedirect.com/science/article/pii/S0167718711000671, states explicitly that collaboration can reduce product distinction INSIDE the coalition and INCREASE distinction from a non-collaborating firm, and that equilibrium price, market rivalry and welfare respond to both effects. Their leading market model is a location model; the present three-market Cournot quadratic demand is an APPLICATION / REPRESENTATIVE-CONSUMER REDUCED FORM, not their original location derivation. Their paper's accessible article preview and introduction were read, not every paywalled lemma.

Additional direct predecessors: Besen & Farrell (1994), *Choosing How to Compete*, JEP 8(2):117–131, https://www.aeaweb.org/articles?id=10.1257/jep.8.2.117 (competition **for** a standard vs competition **within** it); Brander & Spencer (2015), *Endogenous Horizontal Product Differentiation under Bertrand and Cournot Competition*, NBER WP 20966 https://www.nber.org/papers/w20966; related published *Intra-industry trade with Bertrand and Cournot oligopoly: The role of endogenous horizontal product differentiation*, Research in Economics 69:157–165 (2015). Policy design effects and endogenous differentiation are NOT new theories.

## 2. New action variables, unchanged exogenous economic primitives

Remain within the original six EXOGENOUS normalized technological coordinates `theta=(v,gamma0,kappa,eta,rho,phi)`; introduce TWO genuine **ENDOGENOUS strategic choices**:
- `c in [0,1]`: depth of interoperability / shared interface. Private firm consortium can elect to develop this technology and governments can regulate a minimum compatible interface, subject to physical feasibility.
- `a in [0,c]`: depth of COMMON PRODUCT DESIGN. Firm consortium jointly chooses its horizontal differentiation / design convergence. Regulatory authority may impose a publicly enforceable MINIMUM common-design floor `L`, so feasible firm response `L<=a<=c<=1`. `a=c=1` means *all design attributes and interface* harmonized, different from merely `c=1,a=0` (compatible interface but distinct products).
Demand primitives:
`m=1-v`,
`z(c)=1+rho*c`,
`b(c,a)=gamma0+kappa*a-v*c`,
`d(a)=gamma0-eta*a`.
RS Cournot substitution matrix `M_R=[[m,b,d],[b,m,d],[d,d,m]]`; IS all three cross-pair substitutes `b`.
Crucial derivatives: `b_a=kappa>0,d_a=-eta<0,b_c=-v<0,z_c=rho>0`.
The positive `b_a` captures less distinct collaborator products/higher competition among them, the negative `d_a` captures lower insider-outsider cross-substitution/relaxed outsider competition. Within the feasible triangle, `b<=gamma0+(kappa-v)c`; if `kappa>v`, the maximum of `b` is at full unification `c=a=1`. IS then applies that maximum to **ALL THREE pairs**, maximizing direct product substitutability across the entire market among the feasible regimes. THIS is a substitution/marginal-rivalry statement, not a universal theorem that the resulting equilibrium prices are lowest or CS highest (demand changes with design).

**Recovery of frozen one-depth original model:** on the diagonal `a=c=s`, the coefficients are exactly `b(s)=gamma0+(kappa-v)s`, `d(s)=gamma0-eta*s`, and `z(s)=1+rho*s`, as before. Original fee was `phi s²`. For two-dimensional development, choose as an EXPLICIT new separable cost assumption `C(c,a)=phi(c²+a²)/2`, also exactly `phi s²` on the diagonal. No 7th scalar technological primitive is added. But this **off-diagonal extension is NOT IDENTIFIED by the old model**: changing the split of real cost between interoperability and product design changes the interior design equilibrium. Treat it as an institutional/engineering assumption, not a theorem mechanically implied by the six original numbers.

## 3. Structural tradeoff and correct entrant corner

Define `A=2m+b`, `D=2m A-2d²>0`, and outsider KKT support `Y=A-2dz`. With all three RS producers active, per national destination:
`x_R=(2mz-d)/D`, `y_R=Y/D`.
If `Y<=0`, the outsider makes zero (KKT) and `x_R=z/A`; do NOT extrapolate a negative outsider output.
With `c,a` freely chosen, the active outsider's response is endogenous through both `b(c,a)` and `d(a)`; it can itself affect which differentiation choices are profitable.

At fixed interoperability c on the active RS branch, implicit differentiation of firm FOCs gives
`D*x_{R,a}=2m*eta*y_R-(2m*kappa+2d*eta)*x_R`.
The first term is the competitive-relief benefit from making the nonparticipant more distinct; the second collects stronger head-to-head rivalry with collaborator and the other substitution effects. It is a PRECISE competition tradeoff, NOT an assumption that one term always wins. Firm designs by optimizing
`P_R(c,a)=3m*x_R(c,a)^2-C(c,a)`.
Thus any strictly interior optimum solves
`6m*x_R[2m*eta*y_R-(2m*kappa+2d*eta)*x_R]/D=phi*a`.
The government adds domestic CS to that private profit and can favor another a.
For IS, all 3 firms directly substitute through `b(c,a)`, so when c is fixed, rising a reduces each Cournot quantity and private profit; keeping interface compatibility while preserving product attributes is potentially attractive.

### General comparative-static theorem: two opposite outsider channels

For ANY admissible original-six-primitive economy with `v,rho,kappa,eta>0`, `d>=0`, positive demand SPD and c,a within their physically feasible triangle, the OUTSIDER SUPPORT numerator is `Y(c,a)=2m+b(c,a)-2d(a)z(c)`. Hence exact identities
`partial Y/partial c= -v-2rho*d<0`,
`partial Y/partial a= kappa+2eta*z>0`.
At a fixed common design, more technical interoperability pushes the outsider toward zero-output KKT exclusion; at fixed interoperability, increasing design convergence both intensifies *insider-insider* substitution b and reduces *insider-outsider* substitution d, thus pushes the outsider toward positive production. Positive Y does not mean full outsider quantity is monotone, since the Cournot D denominator also changes.

Moreover, in the genuine outsider-zero KKT region, insider x=z/(2m+b); if `kappa>0` and `C=phi(c²+a²)/2`, then `partial P_R^corner/partial a=-6m*kappa*z²/(2m+b)^3-phi*a<0`. Thus an unconstrained private designer cannot gain locally by **additional common-design convergence AFTER outsider exclusion**; this is a direct testable prediction of the separated-actions variant, not the old a=c restriction. Both general formulae are independently symbolically verified in source Python CI.

## 4. EXACT full-response nested-regulation theorem for rational admissible witness

Fix the ORIGINAL six economic primitives to
`(v,gamma0,kappa,eta,rho,phi)=(1/100,7/50,1/50,13/100,8/25,7/50)`.
Here kappa=.02>v=.01. The full feasible triangle `0<=a<=c<=1` has `.13<=b<=.15`, `.01<=d<=.14`, strict demand SPD in all regimes, and **outsider ACTIVE throughout**:
`Y>=2m+.13-2*.14*1.32>0`.
No negative-output continuation has been used. On c=a=s we recover the original model.

### The nested 2-stage game is EXPLICIT
(i) A competent common public regulator first chooses **a minimum harmonized design floor** `L∈[0,1]`. This regulator is modeled as maximizing a representative participating country's `W_R`; national-government vote and legal enforceability of the particular floor are maintained assumptions, NOT derived.
(ii) A consortium of the TWO symmetric participating private firms jointly chooses compatibility c and common design a subject to `0<=L<=a<=c<=1`, maximizing their identical worldwide `P_R` and paying the same real cost individually. The outsider doesn't sign or choose its product design here.
(iii) A Cournot differentiated-product market with all three firms plays the unique positive-output Nash continuation. This is a *constrained-joint-design/standards-approval* game, not independent unilateral specification choices or a full de facto standards race.

**Proposition N1 (global compatibility choice):** For all physically feasible (c,a) in this triangle, `P_{R,c}>0` at fixed a. Proven analytically by `x_{R,c}=2m(rho+v x_R)/D>0`, conservative exact rational lower bounds on x, its derivative and the fee derivative `phi c`. Thus the private optimal interoperability c=1 in EVERY regulated subgame for a given floor L. (For IS at a=0, a separate exact lower bound also shows c=1.)

**Proposition N2 (strict interior design):** With c=1, independent 3x3 rational Cournot expressions and exact Sturm root counts prove the firm profit function `P_R(1,a)` has exactly ONE stationary point in a∈(0,1), positive derivative below it and negative derivative above. Root
`a_F≈0.508035136761633`.
Government `W_R(1,a)` has exactly ONE stationary root and global max
`a_G≈0.561024802702390>a_F`.
Both private and govt outcomes beat their NS participation/outside baselines; the outsider is positive.

**Proposition N3 (unique regulator floor and SPE real design):** A minimum public harmonization L gives private best response
`a^{private}(L)=max{a_F,L}`, `c^{private}(L)=1`.
The regulator's W_R strictly rises along response a up to a_G and strictly falls above, so government chooses **L=a_G**. The resulting backward-induction SPE *outcome* is
`(c*,a*,L*)=(1,a_G,a_G)`.
The equilibrium is not imposed equal-design a=1, and the private and govt preferred differentiation levels genuinely diverge. Here a_G is the minimum of the government's instrument needed to induce its preferred design. Under general single-peaked private/government objectives, a MINIMUM-standard rule cannot enforce `a<a_F`; the model therefore generates a **directional asymmetry of regulatory power**. This insight is a nested-constraints result, not a generic novel theorem.

Exact indicative payoffs:
- private-only preferred design a_F: `P_R≈1.0046323714, W_R≈1.5663017466`.
- govt-floor induced a_G: `P_R≈1.0044850024, W_R≈1.5664568691`.
- baseline NS `P_N≈0.5814864, W_N≈0.95446` (baseline code prints exact symbolic).
The modest welfare improvement demonstrates a nonzero, but quantitatively SMALL, constraint effect in this normalized witness; don't inflate its policy magnitude.

## 5. Complete unification vs interoperability-only IS: relevant policy comparison

Under the same technology and `c=1`:
`IS(a=0)` achieves interface compatibility while retaining maximum permitted product distinctiveness: `P_I≈0.9613552296, W_I≈1.6124633291`.
`IS(a=1)` FULLY harmonizes **all firms' product designs**, yields the maximum substitutability `b=.15` across all 3 pairs, but `P_I≈0.8554847645, W_I≈1.5040581717`.
Exact Sturm certificates prove both `P_I(1,a)` and `W_I(1,a)` strictly DECREASE for a∈[0,1] in this admissible witness. Therefore a public/private global standard can be economically desirable in interface compatibility, without harmonizing products' entire attributes. This is the key distinction: **global compatibility does NOT logically require globally identical products**.

This separately compares a potential mandatory all-country interoperability outcome; it does NOT complete a single full multi-country sequential standard-type/endogenous-a/endogenous-c/SPE analysis. Any such claim must solve outsider F3's license and tech adoption, 3 governments' votes, asymmetric outside options, and all off-path c,a choices.

## 6. Novelty and future game protocol

- These are actual endogenous design choices with exact proof of a nested governmental MINIMUM requirement; the earlier stage's a=c=s forced design is superseded for this NEW application track, not retroactively altered.
- The joint derivative channel is precisely the Ghosh–Morita-type collaboration/differentiation channel that the user identified. It was **NOT** delivered by the previous kappa<v witnesses.
- Material unresolved: whether one government can impose the same design floor on both firms across states; whether open licensed standard can be taken up unilaterally by F3, and the fee/resource accounting for proprietary/hybrid technology; international government delegation vs unanimous votes; private firms' asymmetric/unilateral design decisions; whether intermediary standards SSO reveals a regulator-approved open interface; **full endogenized RS vs IS/NS and continuous c,a in one extensive form**.
- Before that expanded project, freeze a legal right matrix: (A) government regulation may specify open interoperability performance floors, but cannot transfer patent rights; (B) firms jointly own/choose implementable designs and retain product-specific unregulated features; (C) outsiders choose actual adoption and production; (D) public authorization and IP licensing can act as complements and conflicting mandates can create regulatory/mar​​ket-standard competition.
- Stage 6 novelty NO-GO remains. This is a coherent synthesis/extension for an applied research paper; the literature includes Brander–Spencer endogenous differentiation, Besen–Farrell standards rivalry, and Ghosh–Morita coalition differentiation.

Exact script: `code/stage2_endogenous_design_nested_regulation.py`, verified by GitHub Actions `.github/workflows/stage2-endogenous-design-nested-regulation.yml`.
