# Stage 3 — Three-country endogenous compatibility/design, government override and FULL/PARTIAL/FRAGMENTED SPE

**2026-10-14 JST.** Author mandate: merge continuous ENDOGENOUS compatibility `c` and product-design commonality `a` into the three-country/three-firm market-vs-regulation standards game and **solve conditions** under which fully interoperable IS, bilateral RS and fragmented NS are each subgame-perfect outcomes.

## 0. Scope and what IS actually solved

This is a new, clearly specified **finite-event extensive game with two CONTINUOUS endogenous private design actions**, one appointed agenda setter and 3 government sequential votes. It is mathematically stronger than just a finite menu or gridded best replies: continuous design optimizations are certified globally, with exact Sturm and tensor Bernstein coefficients in code.

Do **NOT** conflate FULL INTEROPERABILITY (all three firms implement one standard, IS) with FULL PRODUCT HOMOGENIZATION (all three converge to common design a=1). In these examples the FULL IS equilibrium keeps differentiated products at a=0. Complete-product homogenization increases pairwise substitution in the original Ghosh–Morita parameter channel but is not optimal for any firm in the IS market with positive kappa and the chosen real costs.

The game still ASSUMES a standardized OPEN, universally implementable interface (no compelled expropriation of patents), a privileged first private proposer and a pre-established public universal-IS regulatory agenda. It does not solve institution-choice agendas, 3 independent private incompatible technology races, endogenous exclusivity/essential IP licensing, spillovers across rival incompatible protocols or endogenous consumer adoption/installed base. Government power is deliberately LIMITED to making the privately available c,a interface universally mandatory; it cannot manufacture technology.

## 1. Original market and the two-endogenous-action extension

Original six quantitative primitives `theta=(v,gamma0,kappa,eta,rho,phi)`; regional consortium chooses `(c,a)` in compact triangle `T={0<=a<=c<=1}`. `c` denotes degree of technical interface compatibility; `a` degree of COMMON PRODUCT DESIGN / reduction in product distinction. An actual project requires `c>0`; (0,0) is NS default.

`m=1-v>0`;
`z=1+rho*c`;
`b=gamma0+kappa*a-v*c` (substitution among collaborators);
`d=gamma0-eta*a` (substitution between collaborators and outsider).

NS all three off-diagonal `gamma0`, `q_N=1/[2(m+gamma0)]`. RS (one named private pair 1,2) has demand matrix `[[m,b,d],[b,m,d],[d,d,m]]`, production `(x,x,y)`; outsider true KKT:
`Y=2m+b-2dz, D=2m(2m+b)-2d²`;
if Y>0, `x=(2mz-d)/D`, `y=Y/D`;
if Y<=0, `x=z/(2m+b)`, `y=0`.
IS all three have diagonal m/off-diagonal b, all 3 efficiency z, `q_I=z/[2(m+b)]`. Cournot uniqueness and positive definite demand on the specified admissible domain (including ALL c,a in both rational examples) are certified by rational bounds.

**Per-adopter real implementation cost** `C(c,a)=phi(c²+a²)/2 + K`, where K>=0 is incurred ONCE when c>0. For K=0 and a=c=s, exactly reproduces original technology fee `phi s²`; off-diagonal additive quadratic extension was a separate Stage2 modeling assumption. **K is a transparent, genuinely NEW SEVENTH exogenous primitive** (fixed development/setup resource cost, not a payment to IP owner) introduced ONLY after proving that fragmentation cannot occur under K=0. Do NOT say original six-primitive model endogenously yields all three standard types as final SPE in this protocol. Free-license assumption remains.

Firm payoff `P_i=3m q_i²-C(c,a)` if it develops/adopts and `3m q_i²` otherwise; home government `W_i=P_i + CS`, `CS=q'Mq/2` within its product destination. Under RS outsider's P3 is `3m y²` without adoption fee; under mandatory IS it pays the real implementation fee and may exercise its legal EXIT option 0.

## 2. Explicit 3-firm / 3-government sequential game

1. F1, the temporarily fixed private-convenor/proposer, chooses NS or offers exact OPEN project RS12(c,a) or IS123(c,a), c>0 and 0<=a<=c<=1. F1 may alternatively invite F3 for RS13, symmetrically. Contract title/design and licensing are part of observable offer.
2. Firm(s) invited choose to accept or reject sequentially, F2 then F3 if IS proposed. A rejection restores NS. Invited firms compare actual anticipated market payoff after possible regulation with NS P_N; agreements cannot force signers to accept lower profit.
3. Only following a privately developed RS offer, G1, G2 and G3 successively cast observable YES/NO votes to certify the **EXACT already-developed** open c,a interface as an obligatory all-three-country IS interface. All three must approve. Government votes are endogenous, **regulatory agenda, scope of competence, order and the tie-break (indifference keeps RS) are exogenous**.
4. F3 responds to a passed mandate by ACTUAL implementation/entry if its IS profit after real fee is >=0, else exits. F1/F2 have the same no-loss-making-production option. In our witnesses mandated firms have strictly positive profit. Regulatory implementation does not conjure nonexistent license rights.
5. Independently chosen Cournot product-market quantities in all 3 segmented destinations. The original demand matrices and correct real cost charges determine payoffs.

Different from previous Stage0–2 STRONG-NASH-of-stage1 correspondence: these are actual **sequential subgame-perfect final OUTCOME** classifications (under the exact new agenda and continuation protocol), not claims about Cournot strong Nash or coalition-proof equilibrium. In general, away from strict comparisons some vote or proposal strategies are not unique.

## 3. General backward-induction theorem — characterization by global variational inequalities

For each physical technology `t=(c,a)`, define the actual Cournot/KKT participant payoffs `P_R(t;K),W_R(t;K),P_I(t;K),W_I(t;K)`, outsider govt `W_O(t)`, baseline `P_N,W_N`. At the government subgame, after an RS project, the mandatory IS upgrade is approved exactly when (with strict affirmative voting and firm voluntary compliance)
`H(t;K)=1 iff [P_I(t;K)>0 AND W_I(t;K)>W_R(t;K) AND W_I(t;K)>W_O(t)]`.
On `H=0`, the private pair remains under RS. For non-strict boundary preferences government retains RS as an explicit institutional tie-break. This is sequential-unanimous agenda, not all-six ex ante signatures.

Define `T_I(K)={t in T, c>0, P_I(t;K)>=P_N}`;
`T_R(K)={t in T, c>0, H(t;K)=0, P_R(t;K)>=P_N}` (credible accepted RS projects which are NOT overridden).
Let
`V_I(K)=max_{t in T_I(K)} P_I(t;K)`,
`V_R(K)=max_{t in T_R(K)} P_R(t;K)`,
with empty-domain maximum `-infinity`. **Condition: these maxima are attained** (if a veto/no-veto boundary induces unattained supremum, arbitrary-parameter pure SPE existence requires separate checking).

**THEOREM 3.1 (sharp necessary and sufficient SPE FINAL TYPE predicate within THIS agenda):**
- IS is an SPE final type iff `V_I>=max(P_N,V_R)`;
- RS is an SPE final type iff `V_R>=max(P_N,V_I)`;
- NS is an SPE final type iff `P_N>=max(V_R,V_I)`.
At a tie, several final SPE types may exist (under accepted weakly indifferent invitations); at strict inequalities the final standard type is unique. The theorem is EXACT for every admissible parameter vector with its actual KKT Cournot continuation, for which required maxima attained and the legal/adoption assumptions apply.

**Why an RS offer that gets upgraded never supplies a separate extra maximum:** its private proposer F1 ends with **exactly** the IS market payoff `P_I(t;K)`. If this upgraded RS proposal is credibly accepted, F1 and F2 receive at least P_N under IS, hence F3 also does by symmetry and direct private IS123 offer at the same (c,a) is feasible. Therefore its final payoff cannot beat `V_I`. This observation is ESSENTIAL; it allows all continuous proposals in the two-dimensional feasible triangle to be exhausted by just TWO global variational optimizations and no-development baseline.

**K=0 fragmentation NO-GO (general):** Consider a direct private IS proposal with a=0 and c tending to 0+. Its per-member payoff is
`P_I(c,0)=3m(1+rho*c)^2/[4(m+gamma0-v*c)^2]-phi*c²/2`.
At c=0 this equals P_N, but its right derivative is
`dP_I/dc|0+=3m[ rho(m+gamma0)+v ]/[2(m+gamma0)^3]>0`
whenever `rho>0` or `v>0`, `m>0`. Hence a small but strictly positive voluntary IS contract makes ALL three firms strictly better off than NS, independent of governments (which do not vote over already accepted private IS in this agenda). Consequently NS CANNOT be a SPE final outcome when K=0 and these conditions hold. This is a mathematical impossibility of fragmentation under zero marginal implementation cost, NOT a failure to find numerical examples. To allow fragmentation, the model must include K>0 or discrete threshold/legal/adoption friction.

## 4. Three EXACT nonempty equilibrium regions with continuous c,a globally optimized

Use original five parameters FIXED:
`(v,gamma0,kappa,rho,phi)=(1/100,7/50,1/50,8/25,7/50)=(.01,.14,.02,.32,.14)`.
Only outsider distinctiveness eta and the explicitly labeled NEW fixed development setup K vary. Here kappa=.02>v=.01; increasing a genuinely increases substitution among collaborating firms while reducing their substitution with the outsider. For all three witnesses and ALL c,a in T: `.13<=b<=.15`, `0<=d<=.14`, every NS/RS/IS demand matrix SPD, and the regional outsider stays strictly ACTIVE: `Y>=2m+.13-2*.14*(1+.32)>0`. All calculations therefore use legitimate interior Cournot. IS demand qI also stays positive; all invitation, government and technology-choice incentives are checked endogenously.

### Case F — FULL all-firm compatible IS: eta=3/100, K=0

- For ANY feasible positive private regional design `c>0,a∈[0,c]`, governments G1/2/3 STRICTLY prefer an IS regulatory upgrade, AND F3 optimally complies at positive IS profit.
- Exact proof: substitute `a=c*t`, `t∈[0,1]`; the sign of `W_I-W_{R,member}` and `W_I-W_{R,outsider}` is positive for all `c>0` because their polynomial numerators factor c and the remaining polynomials have **respectively 42 and 72 strictly POSITIVE rational tensor Bernstein coefficients** on [0,1]^2. Denominators are known positive Cournot factors.
- Firm IS profit is globally maximized over the WHOLE c,a triangle at `(c,a)=(1,0)`: for each fixed c it STRICTLY decreases in a; at a=0 it strictly increases in c. Strict exact Sturm sign/root certificates prove the latter.
- `P_I(1,0)≈0.9613552296>P_N≈0.5814864124`. Firms can directly coordinate voluntary IS, or an initial RS may be upgraded; all SPE final outcomes are IS, with **the full three-firm interface c=1 and differentiated product designs a=0**. No separately profitable unregulated RS can survive all three regulators.

### Case P — PARTIAL two-firm RS: eta=7/50=.14, K=0

- For every design in the whole triangle private RS profits are STRICTLY increasing with c at fixed a: `x_{R,c}=2m(rho+v x_R)/D` and a strict rational GLOBAL lower bound implies `P_{R,c}>0`. Thus any global private RS optimum has c=1.
- Restrict to c=1 and derive exact rational `P_R(1,a)`. Sturm's theorem proves exactly **ONE** stationary point in [0,1], positive derivative before and negative afterward. The root lies in rational interval `(0.5949,0.5950)`; numerical value
`a_R*=0.5949515085121895...`.
- At this **globally private-optimal** RS technology, Sturm certificates on the entire rational isolating interval independently prove `W_{R,member}(1,a_R*)>W_I(1,a_R*)`; incumbent regulators VETO the upgrade strictly, whatever G3 would prefer.
- Further exact inequalities `P_R(1,a_R*)≈1.0086209429>P_I(1,0)≈0.9613552296>P_N≈0.5814864124` certify all invitations accepted and REGULATORY SAFE maximal RS strictly dominates every IS proposal and every privately offered RS that subsequently gets upgraded.
- Hence EVERY pure SPE final type is RS (named pair), with private endogenous `(c*,a*)=(1,0.5949515...)`. One government (or both incumbents) denies international compulsory harmonization. All firms still separately participate in product market; the excluded firm is a **nonmember of the standard, not a nonproducing firm**. This distinction matters: in these rational examples it remains **active** in Cournot.

### Case N — FRAGMENTED national incompatible NS: eta=.14, K=1/2

K=1/2 is an ADDITIONAL upfront real setup cost PER participating firm, incurred for any strictly positive developed c and paid only ONCE on the final realized contract. It is NOT included in the earlier six parameter model.
- Exact univariate Sturm analysis proves `P_R(1,a)<P_N+1/2` for EVERY a∈[0,1]. The global private monotonic c argument gives `P_R(c,a)-K<P_N` for EVERY c,a in the triangle.
- Global IS optimum also fails acceptance: `P_I(1,0)-1/2≈0.4613552296<P_N≈0.5814864124`.
- Therefore EVERY offered private developed RS/IS standard would be rejected or not proposed. Government cannot mandate undeveloped technology; so no developing is the unique final SPE TYPE: NS, regardless of possible economically desirable open standards if an external organizer funded fixed costs.
- More sharply at eta=.14, define threshold `K_R*=P_R(1,a_R*;K=0)-P_N≈0.4271345305`. Because private global RS dominates IS and is strictly safe against regulatory override, final RS for `0<=K<K_R*`, and NS for `K>K_R*`. At equality, voluntary acceptance indifference and proposer choice can sustain both; for very high K, any firm may choose legal exit rather than implement a hypothetical forced standard, but it is off-path. This threshold claim holds with government's original all-country upgrade rule, as the member government RS/IS fee difference cancels K.

### Direct choice and regulation comparison

| Theta and setup | Private unconstrained best technology | Government RS→IS response | Final SPE type |
|---|---|---|---|
| eta=.03,K=0 | IS at (c,a)=(1,0) | Every developed RS is upgraded | **All-firm IS** |
| eta=.14,K=0 | RS at (1,a_R*) | RS at optimum survives due member-gov veto | **Bilateral RS** |
| eta=.14,K=.5 | No development accepted | No interface to certify | **Fragmented NS** |

Full all-firm standard adoption is not the same as all-three-producer identical products: at IS optimal common design a=0. Partial standardization here refers to consortium MEMBERSHIP (two adopters), even though within those two firms interface depth is c=1. NS is three separate national standards, not an inactive product market.

## 5. Exactly how competition and technological complementarity are represented

- `b_a=kappa>0` means deeper common design makes INSIDER firms closer product substitutes and intensifies competition among them; `d_a=-eta<0` means deeper design commonality makes the OUTSIDER less substitutable with insiders, potentially protecting nonmembers (Ghosh–Morita opposing rivalry channels).
- `b_c=-v<0`, `z_c=rho>0`: enhanced compatibility directly lowers effective demand competition and boosts adopters' technology, while outsiders' support numerator `Y_c=-v-2rho*d<0`, `Y_a=kappa+2eta*z>0`. Network externalities, differentiation and bargaining decisions are all in the derived Cournot payoff.
- In IS ALL three firms share cross-product substitutability b, so full all-design homogenization (c=a=1, when kappa>v) makes b maximum across all feasible standardized markets. But this **does not make a=1 privately optimal**. In fact `PI_a<0` at fixed c whenever `kappa>0,phi>=0`. Govt national IS welfare also weakly declines with a in this Cournot setup. It is ECONOMICALLY CRITICAL not to assume full participation inevitably produces identical commodities or the most severe competition.
- Firm-created OPEN technology is a TECHNICAL NECESSARY condition for enforceable government recognition, but govt scope expansion after development can CROWD OUT incumbent firms' preferred bilateral exclusivity. The three regimes therefore appear endogenously as a result of network incentives, development overhead, technology comparisons and three public voting rights. Open licensing, proposal agenda and government authority remain maintained institutional assumptions.

## 6. Honest limits / next project

1. The general type criterion is global but variational (two continuous maxima), not a closed semialgebraic partition of all 7D exogenous parameters. The three robust exact witnesses show nonempty admissible regions. The law of large numbers, installed user base and device market share are NOT endogenously tracked.
2. F1 is an appointed proposer; the bilateral coalition contract has a COMMON c,a for both adopters and firms2/3 accept/reject; they do not each unilaterally create competing product standards. Genuine noncooperative three-firm technology choice requires new actions. No endogenous standard-setting institution / constitutional agenda.
3. Common private R/IS technology is open; a regulator cannot impose private patent rights without a license; all legal adoption and production feasibility must remain explicit. No real rulemaking/enforcement cost or political economy.
4. The fixed setup resource cost K is economically required to produce NS under the current quadratic-burden/linear-benefit environment. Claiming all 3 types in original 6D model with K=0 would be formally false under this protocol.
5. With K>0, a real-world government could subsidize setup (requiring a budget and new instrument), or permission thresholds, but neither is silently introduced here.
6. Pure SPE may fail to attain maxima on knife-edge policy boundaries if the first-mover payoff jumps at a regulator's strict-unanimity frontier. Our three cases have strict comparisons and attained maxima; do not extrapolate existence to all parameters without a separate proof.

## 7. Literature grounding

Ghosh & Morita (2012), *Competitor collaboration and product distinctiveness*, IJIO 30:137–152, https://www.sciencedirect.com/science/article/pii/S0167718711000671, already explain how collaboration makes members' products more similar but outsiders' products more distinct; the current linear-quadratic-demand setup is an inspired APPLICATION not their original circular-location model. Besen & Farrell (1994), *Choosing how to compete: Strategies and tactics in standardization*, JEP 8:117–131, https://www.aeaweb.org/articles?id=10.1257/jep.8.2.117, distinguish competition FOR and WITHIN standards. Spulber (2019), *Standard Setting Organisations and Standard Essential Patents: Voting and Markets*, Economic Journal 129:1477–1509, https://academic.oup.com/ej/article/129/619/1477/5364896, already analyzes standard-setting voting and market competition. Therefore NO new fundamental IO/standard-bargaining novelty is asserted. This is a reproducible 3-country policy/industry APPLICATION; provenance and precise conditional economics should lead introduction.

**Reproducibility and CI:** `code/stage3_endogenous_ca_regime_spe.py`, `.github/workflows/stage3-endogenous-ca-three-regimes-spe.yml`. Exact polynomial certificates use a,b,c Triangle transformed by a=c*t, all c/t in [0,1], Sturm root counts, rational inequalities, and genuine Cournot FOCs. Keep as Draft PR; do not merge earlier Draft PRs or modify submission manuscript.
