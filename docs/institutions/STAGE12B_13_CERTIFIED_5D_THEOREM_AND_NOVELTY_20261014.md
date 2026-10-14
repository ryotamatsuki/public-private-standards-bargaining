# Stage 12B–13: parameter-robust endogenous differentiation and theorem-level prior-art audit

**2026-10-14**. Stacked on draft PR #40. This is an exact independently rerun **five-dimensional local robustness certificate of a conditional WELFARE ranking**, not a purported seven-parameter global SPE partition. Every old research PR and paper manuscript remains unmerged/unchanged.

## Complete exact five-dimensional hyperrectangle welfare theorem (NEW)

Let the five primitives p=(v,gamma0,kappa,rho,phi) vary **SIMULTANEOUSLY and CONTINUOUSLY** in their independent +/-2% ranges around (.01,.14,.02,.32,.14). Let eta vary in [.10,.14], K in [.54,.56]. Maintain Stage11 market technology, sunk installation K, and its two specified possible final market allocations: proprietary two-member RS with active outsider, and publicly mandated all-firm IS.

RS Cournot:
m=1-v, z=1+rho*c, b=gamma0+kappa*a-v*c, d=gamma0-eta*a,
D=2m(2m+b)-2d², x=(2mz-d)/D, y=(2m+b-2dz)/D.
A member's gross-of-K private payoff f(a,eta,p)=3m*x(1,a)^2-phi(1+a²)/2.

**Proposition P12-R**: for every real five-dimensional p in the +/-2% box and every eta in [.10,.14], the private member has a **UNIQUE** strict interior product common-design optimum a_R*(eta,p) in (.25,.65). It is strictly increasing in eta. Compatibility remains optimal at c=1. Proof: exact Fraction interval evaluation of f_aa<0 and f_a,eta>0 over 32 rational 5D subboxes * four a-subintervals * two eta-subintervals (256 cells); uniform f_a(.25,.10)>0 and f_a(.65,.14)<0; uniform positive lower bound of f_c across full technology triangle.

Define RS consumer surplus CS_R=(m+b)x²+2dxy+(m/2)y² and nonmember operating private profit P_O=3my². Define public IS quantity q=(1+rho)/(2(m+gamma0-v)), full variable-cost-inclusive national welfare W_I^0=3m q²-phi/2+[3(m+2(gamma0-v))/2]q². The actual two final allocation **world national welfare** sum gap is
F(eta,K,p)=[2f(a_R*,eta,p)+P_O(a_R*,eta,p)+3CS_R(a_R*,eta,p)]-3W_I^0(p)+K.

**Proposition P12-W (a full 5D-perturbation guarantee)**: For EVERY five-dimensional p in the above entire real +/-2% box and EVERY real K in [.54,.56], F(eta,K,p) is continuous and **strictly increasing** on eta∈[.10,.14], with exactly ONE welfare-equality crossover eta_W(p,K)∈(.10,.14). At smaller eta the given public IS terminal allocation has higher sum W; above the crossover the given private RS terminal allocation has higher sum W. The crossing is a welfare boundary conditional on each allocation, **NOT a proved SPE coexistence region** at every perturbed p.

Exact rational certification:
- f_aa<0, f_a,eta>0 => a_R*,eta=-f_a,eta/f_aa>0.
- Exact Fraction interval arithmetic over the entire unpartitioned five-dimensional +/-2% box, with 8 design bins and 4 eta bins (32 checks), proves RS world welfare partial derivatives W_a>0 AND W_eta>0 on eta[.10,.14], a[.25,.65]. Therefore F_eta>0.
- Global interval root isolation over all perturbed p: a_R*(eta=.10)∈[.25,.35], a_R*(eta=.14)∈[.55,.65].
- Using the multi-dimensional MEAN VALUE THEOREM with exact rational interval gradients to bound the welfare expression at all real p, together with positive W_a to sandwich the private root: F(.10,K=.56,p)∈[-.04848235,-.00355880] STRICTLY NEGATIVE, and F(.14,K=.54,p)∈[+.03131021,+.07274133] STRICTLY POSITIVE. Display decimals are rounded, backing arithmetic Fraction is exact.

This is stronger than Stage12's 32-corner sensitivity tables and does NOT conflate a grid with a full box. The separate exact general marginal threshold eta0(p)=2m*kappa*N0/(D0-4gamma0*N0), with N0=2m(1+rho)-gamma0 and D0=2m(2m+gamma0-v)-2gamma0², has already been interval-verified in the FULL +/-2% 5D box: .03406768<eta0<.03715043.

**SPE scope honestly restricted:** many conservative critical enterprise and government margin inequalities were also certified throughout the 5D real box; however, a complete all-history SPE construction for the perturbed institutional game still needs the public-domain feasible family O(cP,aP), endogenous legal IP rights to choose proprietary X/Y, precise C certification adoption timing, all offpath mixed adoption continuations and possible negative outsider cross-substitutability. For example gamma0=.1372 and eta=.14 give d(a=1)= -.0028, violating the originally maintained nonnegative substitution everywhere. Do not silently claim full +/-2% RS/IS SPE robustness.

## IMPORTANT correction of earlier purported Stage9 government fee problem

**The original Stage9 holdout government condition is correct**, not missing phi/2. The public W_I^0 defined above ALREADY deducts the public physical specification fee phi/2. After one proprietary partner switches to N, remaining X's national policy L payoff is W_N-K_old-phi*(1+a_old²)/2, whereas public mandate M payoff is W_I^0-K_old-phi*(1+a_old²)/2-K_new. Their difference is W_I^0-W_N-K_new. Thus the correct condition is K<W_I^0-W_N, not K<W_I^0-W_N-phi/2. An early audit step thought the fee missing; that allegation was retracted after detailed cost decomposition. As an additional strict stress test (NOT the economic condition), even W_I^0-W_N-.56-phi/2>0 was certified throughout the +/-2% 5D box: 4^5=1024 exact rational boxes and lower interval slack >.00185318.

## Direct theorem-level prior-art warning

- **Gil Molto, Georgantzis and Orts (2005), _Cooperative R&D with Endogenous Technology Differentiation_, JEMS 14:461-476**: publicly readable author text provides **Proposition 1** (noncooperative tech distance zero vs positive depending on potential spillover threshold), **Proposition 2** (RJV selects identical tech whereas patent pools' optimal differentiation may depend on parameters), **Proposition 3** (socially optimal tech distance). Therefore endogenous-design-threshold and private-vs-social design contrast are **already known in the field**. https://doi.org/10.1111/j.1530-9134.2005.00048.x and https://www.researchgate.net/publication/4765367_Cooperative_RD_with_Endogenous_Technology_Differentiation .
- **Ghosh and Morita (2012), _Competitor Collaboration and Product Distinctiveness_, IJIO 30:137-152**: publisher intro demonstrates collaborator rivalry increase vs noncollaborator differentiation (the Ghosh-Morita mechanism); formal Proposition statements unavailable in currently openly accessible text. No generic novelty for b_a>0,d_a<0. https://www.sciencedirect.com/science/article/pii/S0167718711000671 .
- **Lukach, Kort, Plasmans (2007), _Standard-Creating Coalitions in Oligopoly with Differentiated Products and Variable Network Density_**, Antwerp Working Paper / SSRN 996856: already combines product differentiation, joint R&D, network intensity and standard coalition stability; full formally numbered propositions still require a legitimate PDF. https://research.tilburguniversity.edu/en/publications/standard-creating-coalitions-in-oligopoly-with-differentiated-pro/ .
- **Lukach, Kort, Plasmans (2007), _Standard-Creating Coalitions: Open vs. Proprietary Standards_**, SSRN 1054021: abstract already distinguishes open vs proprietary standard structures and nonuniqueness. Full proposition text not yet accessible. https://ssrn.com/abstract=1054021 .
- **Takarada et al. (2020), _Standards Policy and International Trade: Multilateralism versus Regionalism_**, JPET 22:1420-1441: regional/multilateral comparisons, social ranking and fixed standard costs already known; their cooperative solution notion CORE is distinct from the current six independent public/private actors' SPE. https://doi.org/10.1111/jpet.12425 .

**Novelty decision HOLD**: The candidate is not any individually known mechanism but the **combination** endogenous private common-design choice plus irreversible proprietary first investment plus three national governments' sequential public mandate authority, yielding two possible SPE final standard types whose welfare ranking changes inside their coexistence region. For a credible top-journal novelty case, isolate exactly which removal of these institutions destroys that result, and inspect full numbered Propositions of Ghosh–Morita and both Lukach papers.

Reproducible **complete numerical/rational source files and tests** are attached in the originating ChatGPT conversation bundle (not yet committed into this PR). The present source checkpoint plus theorem statement are not a substitute for the source tests; mark proof replication outside GitHub as PASS, repository CI as NOT YET CONFIGURED.
