# Stage 9 — First genuine all-continuous RS SPE and robust overlap with IS in the SIX-PLAYER governance model

**Date:** 2026-10-14 JST. Parent draft PR #37 (capital-stock retrofit). **Status:** exact full-continuous INITIAL technology-design SPE existence for a privately chosen proprietary regional standard, and coexistence with the separate public-IS SPE. Stage9 is not a universal seven-dimensional phase partition or every-equilibrium description, and it does not endogenize the public-domain O(1,0) design itself.

## The unchanged six-player extensive form and economic primitives

Maintain the FULL integrated Stage5/Stage8 game: three firms F1,F2,F3 simultaneously and independently choose legacy N, proprietary family X/Y, or open O, plus **genuinely continuous** firm-specific design `0<=a_i<=c_i<=1` (c_i>0 on a technology), paying real initial installation stock `K+phi(c_i^2+a_i^2)/2`. Three national governments then operate an agenda where G1 may propose laissez-faire L, certification C(r) of an OBSERVED open firm O(r), or a mandate M of a LEGALLY PREEXISTING public-domain O(1,0); G2 and G3 sequentially approve or veto, all three required for a change. After C the firms independently choose costly migration/stay; after M independently choose comply/exit. Product market is three identical 3-firm differentiated Cournot markets with exact KKT supports. Market network/technology parameters remain the original SIX `theta=(v,gamma0,kappa,eta,rho,phi)`. Setup K is separately identified SEVENTH resource-cost primitive.

**Installed-capital/refit technology FROM STAGE8 (no change):** a previously O firm increasing open design specifications pays only missing incremental capacity `phi/2[(c'^2-c^2)_++(a'^2-a^2)_+]`, not a second fixed K; an N or X/Y firm newly adopting O pays the full additional `K+phi(c'^2+a'^2)/2`. Patents on X/Y are not forcibly used without licensing; M uses independent accessible O(1,0). Firms' initial investment remains sunk at policy date.

At physical parameters EXACT
`(v,gamma0,kappa,eta,rho,phi)=(1/100,7/50,1/50,3/100,8/25,7/50)`,
all Cournot markets considered in the theorem have SPD LQ demand, nonnegative product substitutions, legal implementability, positive active third-country outsider output under proprietary RS.

## Proposition ST9-RS — an ACTUAL continuous-technology regional-standard SPE

Let `m=1-v`, `b(c,a)=gamma0+kappa a-vc`, `d(a)=gamma0-eta a`, `z(c)=1+rho c`. RS insider/outsider Cournot outputs on verified interior support:
`x_R=(2m z-d)/D`, `y_R=(2m+b-2d z)/D`, `D=2m(2m+b)-2d²`.
Let `U_R=max_{0<=a<=c<=1}(3m x_R(c,a)^2 -phi(c²+a²)/2)`; `U_I=max(3m q_I(c,a)^2-phi(c²+a²)/2)`; `P_{O,R}=3m y_R(1,0)^2`. Let `W_I^0` be a country's national W under universal installed public O(1,0) before new setup K; `W_N` be its national NS welfare.

Exact global constants:
- `U_R=8486784637/8564004980≈0.9909831506193263`, uniquely attained at `c=1,a=0`. Global *positive* c marginal for any fixed a by rational conservative bounds; strict negative a marginal along c=1 by exact Sturm roots.
- `U_I=301481/313600≈0.9613552295918367`, uniquely attained at c=1,a=0, certified by global exact Sturm and analytical a derivative.
- `P_{O,R}=5622566697/10705006225≈0.5252277839754362`; the outsider is **ACTIVE** in differentiated Cournot, not a zero-output firm, but it is a NONMEMBER OF THE STANDARD.
- `W_I^0=1011337/627200≈1.6124633290816326`;
`W_N=24375/25538≈0.954460020361814`;
`U_R+CS_R(1,0)=66328189879/42820024900≈1.54899932996069`.

Set the exact strict fixed setup resource thresholds:
`K_{RS,L}=U_R-P_{O,R}=19943656397/42820024900≈0.465755366643890`
`K_{RS,U}=W_I^0-W_N=5269762153/8008716800≈0.658003308719819`.

**Theorem:** For EVERY real `K∈(K_{RS,L},K_{RS,U})`, the integrated 3-firm/3-government game admits a pure-initial-strategy, pure-onpath-policy/adoption, mixed-continuation-offpath **SUBGAME PERFECT Nash equilibrium** with initial company technology choices
`(X(1,0), X(1,0), N)`;
onpath governments choose **L** (do not mandate pre-existing O(1,0)); all firms compete in product market as genuine RS12 `(x_R,x_R,y_R)`, with 3 firms producing and F3 NOT adopting consortium technology. Permutations and X/Y relabelings yield equivalent equilibria.

**NOT** a coalition-proof, strong or unique SPE claim. Arbitrary mixed adopters can be selected in unrelated offpath histories; the theorem blocks EVERY unilateral technology deviation for every selected credible continuation on a deviating history using global payoff bounds.

### Exhaustive ALL REAL first-stage unilateral deviation audit (analytic)

**A. Post-M participation/market feasibility, for ANY one-firm deviation history.** Under the public O(1,0) standard, a conforming firm with respectively 1,2,3 conformers earns G1,G2,G3 operating profits before incremental cost; minimum is G1=25/33≈0.7575758, while MAXIMUM actual new implementation cost for any prior technology is `K+phi/2`. On our strict K interval, `K<K_{RS,U}<G1-phi/2`, so compliance is STRICTLY DOMINANT for all F_i after any hypothetical M following any unilateral deviation. Hence ANY post-M equilibrium uniquely ends in three compliers. A prior X/Y developer also loses sunk investment AND pays additional family conversion, while prior O developer incurs initial stock plus incremental gap, so any one-deviator's private post-M payoff is <=`U_I-K`.

**B. Government behavior after the proposed onpath proprietary RS (X1,X1,N).** No preexisting privately developed O => C unavailable. Under L incumbent national W `W_R^0-K`; after M each incumbent would incur old sunk X setup K+phi/2 plus additional public O setup K+phi/2, so its national W `W_I^0-2K-phi/2`. Difference
`(W_I^0-W_R^0)-K-phi/2` is STRICTLY NEGATIVE even at K=0 because
`W_I^0-W_R^0-phi/2≈-0.006536000879<0`.
Thus both incumbent G1/G2 veto M, government L is the unique final policy result at the proposed RS. Outside G3 has no power to overturn their veto alone.

**C. Deviating incumbent F1 or F2.** For any changed proprietary X(c,a) retaining pairing with the other original X(1,0), the effective paired design is (c,0), and only the deviator's sunk additional a fee changes. Its net L profit is <=U_R-K because private RS profit increases in c and decreases in (wasted) a; if M is proposed, three firms comply and its payoff is <=U_I-K<U_R-K. Any X→Y or X→O alternative loses the original match; under L it yields `P_N-K-phi(c²+a²)/2<U_R-K`; under C the deviator can obtain at most singleton, member RS payoff U_R-K or member IS payoff U_I-K; under M <=U_I-K. The incumbent may choose **N** and avoid its initial setup: this is the MOST important government strategic response. Then observed `(N,X1,N)` has G1/G2/G3 **UNANIMOUSLY SUPPORT M**, because the remaining old-X government compares `W_I^0-2K-phi/2` to its singleton-with-sunk-cost `W_N-K-phi/2` and gains `W_I^0-W_N-K>0`; both initial N governments also gain the same amount. All companies comply under M; the deviating incumbent's private payoff is exactly `U_I-K<U_R-K`. Therefore withdrawing from proprietary RS is NOT a profitable deviation; it changes public policy and erases any anticipated benefit from refusing initial investment.

**D. Deviating outside F3.** If it chooses N, indifferent. If it independently chooses the matching proprietary X(c,a), the resulting 3-company Cournot market is heterogeneously designed: two old incumbents retain pairwise b0=gamma0-v and intercept zA=1+rho, while newcomer F3 has bilateral cross t(c)=gamma0-vc and intercept z3(c)=1+rho c, because common design min(a,0)=0. The exact third-firm equilibrium quantity is
`q_3(c)=[(2m+b0)z3(c)-2t(c)zA]/[2m(2m+b0)-2t(c)^2]`.
The all-active Cournot support is certified for all c∈[0,1]. Exact rational Sturm proof gives
`d[3m q_3(c)²-phi c²/2]/dc>0` throughout [0,1]. Since its freely chosen a>=0 only adds sunk design expenses (pair min a=0), newcomer private profit after own setup is bounded above by `U_I-K`, which is < original outside proprietary-RS profit `P_{O,R}` whenever `K>K_{RS,L}`. If instead it selects Y or O, under L it remains a nonstandardized outsider and pays its setup; under C it may become a two-firm open RS member (profit <=U_R-K) or three-firm IS member (profit <=U_I-K), all strictly less than its original outsider profit as K>K_RS,L=U_R-P_out; under M its payoff <=U_I-K<P_out. Crucially, allowing **ANY** on/offpath adoption pure or mixed Nash after C cannot exceed these maximum component payoffs, so the theorem is not a disguised welfare-max adoption-equilibrium selection claim.

**E. Off-path strategy completion and true SPE.** For every OTHER possible h in the genuinely continuous strategy space, all private post-C/M adoption games have finite binary actions and thus some MIXED Nash. Following choice of one credible adoption Nash for each policy, G1/G2/G3 have finite publicly observed sequential actions and backward-induction best replies; choose one. Since the onpath and ALL unilateral deviations have been verified against these relevant policy outcomes and payoff bounds, completing arbitrary credible strategies on remaining offpath histories yields a subgame-perfect equilibrium. No need to discretize c/a nor assume a universal strong equilibrium refinement.

## Proposition ST9-COEXIST — pure SPE standard-type multiplicity in the SAME exact economy

The Stage8 public-IS continuous-SPE theorem is independently certified at
`K_{IS,L}=65543475780783/136692224487025≈0.479496738214283`
and `K_{IS,U}=W_I^0-W_N=K_{RS,U}≈0.658003308719819`.

Since `K_{RS,L}<K_{IS,L}<K_{RS,U}`, **for every real K satisfying**
`0.479496738214283<K<0.658003308719819`,
BOTH the newly verified proprietary bilateral RS SPE and the previously verified full public IS SPE exist in the **SAME six-player extensive game** with the same rules and the same six market parameters and setup cost K:
- Private equilibrium: F1,F2 invest X(1,0), F3 N; regulators do not override, final RS with active outsider.
- Public equilibrium: all F_i initially N, national governments mandate public O(1,0), all firms comply, final IS.

There is NO arbitrary postpolicy Nash equilibrium selection behind the coexistence because all relevant M subgames have **STRICT DOMINANT conformity**, C deviations are blocked by **GLOBAL unconditional profit upper bounds** (and Stage8 proved nonmigration dominant after a solitary O developer). This is **multiple equilibria from mutually consistent anticipation of PUBLIC ENFORCEMENT AND SUNK INCOMPATIBLE PRIVATE TECHNOLOGY STOCK**. Full continuous design choice a_i,c_i and independent platform choices are all admitted: this is not the old 10-action grid nor the original all-six simultaneous consent / first-stage strong Nash game.

**Third prior rigorous region:** the Stage6 high-setup fragmented NS continuous-SPE existence `K>K_{NS,L}=235752/319225≈0.73851359` remains valid under this EXACT Stage8/9 capital-stock model. Thus we have strictly proven FULL IS, FULL RS, and FRAGMENTED NS **EXISTENCE** on different subregions, and explicit nonempty IS/RS coexistence subregion, for a single economic-institutional specification. None is proven unique, no implicit all-seven-parameter sign-classification is claimed. The uncovered K gap `0.658003≤K≤0.738514` is UNCLASSIFIED, not a no-equilibrium assertion.

## Numeric economics at the overlap witness K=1/2

- Private RS first-stage technology: (X(1,0),X(1,0),N); government nonintervention L.
- Two private RS member net firm profits `U_R-K≈0.4909831506193`.
- RS nonmember firm net private payoff `P_{O,R}≈0.5252277839754`, with **strictly positive market quantity** `y_R≈0.420528681197`.
- After public M everyone would strictly comply but incumbent governmental W would strictly fall, so veto applies.
- If a member X deviated and no longer belonged to consortium, governments would mandate public standard and member deviator would earn `U_I-K≈0.4613552295918<0.49098315`.
- In separate public IS equilibrium: all F_i first choose N; public M unanimously enacted; all adopters earn `U_I-K≈0.46135523`; incumbents' lower private return is offset by CS improvement, so every home government strictly supports the international public open standard.

**Important interpretive caution:** the outside firm may earn MORE than an inside member in the private RS equilibrium, despite being a nonmember. It does not imply a free entrant can instantly use protected X IP; its product sells independently with own baseline, not X technology. The **nature of technology rights and the legacy-product outside option** is central to this result.

## Publication and future priorities

This is a REAL mathematical improvement over previous stages: full-continuous **two-type coexistence** in the same six-player sequential game. It remains an **application/synthesis** of established themes (standards competition, incompatibility, installed capital and joint public regulation), not yet demonstrably a novel fundamental theorem relative to Farrell–Saloner (1985/1986), Belleflamme (2002), Ghosh–Morita (2012), Spulber (2019), and Takarada on international standards. Stage6 prior originality NO-GO applies to earlier simpler mechanisms; don't silently transfer novelty approval or rejection to every new mechanism without focused literature search.

Major remaining gaps:
1. The public open reference O(1,0) is EXOGENOUS and legally preexisting; national governments may choose mandate/not, NOT design an optimal public `c_P,a_P`. Regulatory jurisdiction and G1 proposer power are exogenous.
2. Full 7D phase diagram (including K) is not explicitly computed; the theorem establishes nonempty exact regions on fixed six-parameter slice only.
3. Demand substitution and firm efficiency uses a declared asymmetric Leontief/min pair technology; not uniquely microfounded by previous symmetric original 6D model, and competitor choice of strategic locations under product differentiation would warrant sensitivity.
4. The QED applies to SETUP real cost K and nonrefundable capital-stock upgrade model. License royalties/SEP policy alternatives, government provision/public technology development cost, social planner optimum and endogenous government regulatory depth remain future additions.
5. Boundary equality (knife-edge) cases not classified: our existence theorems use strict open K intervals. Other mixed initial firm equilibria are not classified (Stage9 demonstrates two PURE initial types).
6. Future research should avoid breaking the symmetric all-firm common-design interpretation, and check economic novelty specifically for regulatory foreclosure/coordination multiplicity rather than counting independent equations.

**Exact verification:** `code/stage9_full_continuous_rs_is_coexistence_spe.py` is an independent globally quantified symbolic/economic proof and exact Fraction 3x3 KKT/government-adoption cross-check; CI `.github/workflows/stage9-full-continuous-rs-is-coexistence.yml`. Source Stage8 IP/capital costs preserved in its own parent draft PR. All PRs remain Draft, no manuscript modified or upstream merge.
