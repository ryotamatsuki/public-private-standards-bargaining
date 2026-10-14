# Stage 8 — Capital-stock Technology Upgrades and a GENUINE Full-continuous IS SPE

2026-10-14 JST | Draft stacked after PR #36. **Mathematical result:** a genuine, all-real-initial-design `c_i,a_i` subgame-perfect equilibrium supporting PUBLIC international interoperability IS over a nontrivial EXACT interval of real setup K, with all three firms' independent initial development options, all three government approval rights, endogenous adoption/exit, and Cournot quantities. Not an unconditional seven-dimensional phase partition; proprietary alternatives, postpolicy mixed equilibria and all off-path histories are included via the existence argument, but not explicitly solved for ALL equilibrium types.

## 1. Why technology-installation resource costs must be refrozen

Stage7 exposed two different economically problematic versions of the same firm's retrofit process:
- **Repeated full cost**: a change `O(1,epsilon)→O(1,0)` incurs full NEW `K+phi/2` even at arbitrarily small epsilon; discontinuity in the government's mandate vote and potential non-attainment of best responses.
- **Squared design-distance fee**: `phi/2[(delta c)^2+(delta a)^2]` is smooth, but produces a NEW path-inconsistency/free arbitrage: first install `O(1/2,0)` then upgrade to `O(1,0)` costs `K+phi/2[(1/2)^2+(1/2)^2]=K+phi/4`, versus `K+phi/2` for one-shot installation. This artifact makes private initial partial investment attractive EVEN when government will later impose the same final public interface.

A more defensible stylized **irreversible capital-stock** model retains the already chosen quadratic investment STOCK:
`C_init(ell,c,a)=K+(phi/2)(c²+a²)` for a new technology family (N costs 0).
For changes **within the same openly licensed O family**:
`C_up(O(c,a)→O(c',a'))=(phi/2)[(c'²-c²)_+ +(a'²-a²)_+]`;
`x_+=max{x,0}`. Existing sunk capital is CARRIED FORWARD; no refund on a downgrade; new additional physical requirements consume extra installation resources, but not a second setup K. This is a *separable capital-stock* simplification; real within-family compliance recertification might require an extra (nonnegative) recertification cost. Within-O edits are cost-continuous in design.
For N→O or proprietary X/Y→O, the new legal/engineering family requires a NEW real `K+(phi/2)(c'²+a'²)`, and all earlier private technology costs are sunk. The government cannot expropriate proprietary patent rights; mandatory O has a **pre-existing, legally implementable, publicly open interface** O(1,0), never invented by govt for free. No royalties or subsidies. This is a transparent redefinition of physical technology, NOT a theorem derived from the source six scalars.

**Crucial path-independent lower bound:** an old O(c,a) upgraded to public O(1,0), on 0<=a<=c<=1, incurs TOTAL initial-plus-upgrade resources
`K+phi(c²+a²)/2 + phi(1-c²)/2=K+phi(1+a²)/2 >=K+phi/2`.
Thus preliminary development is never cheaper than directly installing the final state; stepwise upgrades of precisely the same capital stock get no fictitious fee reduction.

The ORIGINAL six market technology primitives are unchanged. The one extra real setup resource K is the already OPENLY introduced seventh scalar primitive from Stage3, not concealed.

## 2. Existing six-player chronological game, with the new explicit cost

F1,F2,F3 independently choose `N` or proprietary X, proprietary Y, or legally open O and a full continuously valued pair `(c_i,a_i)`, `0<=a_i<=c_i<=1,c_i>0`. Cohort match uses pairwise minimum c/a and its partner–outsider differentiated Cournot matrix from Stage5; solo developer does not get fictitious consortium productivity.

After observing h, government G1 proposes L nonintervention, C(r) certification of an OBSERVED O reference (private voluntary migrations), or M mandatory **pre-existing** public O(1,0) (mandatory conformity or exit). Governments G2 and G3 sequentially approve/veto; all three must support proposed change; otherwise L. Under C all firms choose retain/migrate independently (simultaneous normal form); under M all choose comply/exit independently. Firms compete in 3 geographically segmented, symmetric Cournot markets (3x3 KKT including zero-output boundaries) with `P_i=3m q_i²-`real initial investment-`real additional change investment`; `W_i=P_i+CS_{m domestic}`.

The institution remains EXOGENOUS: G1 sets agenda and legal policy authority, government approval is endogenous; public O(1,0) already exists; no engineering or SEP legal magic. **No reason to say this result covers dynamic installed-base migration or voluntary rival X/Y competition in all initial histories.**

## 3. Exact FULL-CONTINUOUS IS SPE existence theorem

Fix the six OLD physical/network parameters
`(v,gamma0,kappa,eta,rho,phi)=(1/100,7/50,1/50,3/100,8/25,7/50)`.
Let `m=1-v=99/100`, `b(c,a)=gamma0+kappa a-v c`, `d(a)=gamma0-eta a`, `z(c)=1+rho c`. Every feasible technology triangle has strictly SPD demand matrix, nonnegative substitutes, positive outsider RS output `y>0`.

Original nonstandardized private payoff and national governmental payoff:
`P_N=7425/12769≈.581486412405`, `W_N=24375/25538≈.954460020`.

Define four globally certified constants:
- `R_gross_max=max_{0<=a<=c<=1} 3m x_R(c,a)² = 11357831232/10705006225≈1.06098315`, attained at `(c,a)=(1,0)`, `x_R=(2m z-d)/[2m(2m+b)-2d²]`.
- `I_net_max=max_{0<=a<=c<=1} [3m q_I(c,a)²-phi(c²+a²)/2] =301481/313600≈.961355229592`, attained at `(c,a)=(1,0)`.
- `O_gross_min_bound=3m(4351/10593)^2=18931201/37781700≈.501065`, a strict LOWER BOUND for outsider private RS payoff at ANY feasible c,a (not an exact infimum).
- `W_I^{public}(1,0;K=0)=1011337/627200≈1.612463329082`, before per-firm setup K, and public standard adopter operating gross returns `G_1=3/(4m)` (one compliant), `G_2=3m[(1+rho)/(2m+b(1,0))]^2` (two), `G_3=3m[(1+rho)/[2(m+b(1,0))]]^2` (three), with `min G_n=G_1=25/33≈.75757576`.

Set two EXACT setup thresholds:
`K_L=max{R_gross_max-P_N, I_net_max-O_gross_min_bound}=65543475780783/136692224487025≈0.4794967382142828`;
`K_U=min{ G_1-phi/2, W_I^{public}(1,0;K=0)-W_N}=5269762153/8008716800≈0.6580033087198189`.
Hence `K_L<K_U`, and in particular the FULL closed rational subinterval `[1/2,3/5]` lies within `(K_L,K_U)`.

### PROPOSITION ST8-IS (strict, nontrivial existence range)

For **EVERY K in the open real interval (K_L,K_U)**, the full six-player continuous-initial-design game has at least one SUBGAME PERFECT EQUILIBRIUM with all three firms initially choosing **N** (no new private technology), all three governments approving the freely implementable PRE-EXISTING public open standard O(1,0), and all three firms implementing it and supplying positive Cournot quantities; final market standard **IS with c=1, a=0**. Continuation adoption after the observed h=(N,N,N) is UNIQUE (all comply) and all three government votes strictly support M. This is an EXISTENCE claim, NOT that this is the unique SPE or all equilibrium strategies identified in every off-path continuum history.

### Complete proof in four steps, over ALL REAL feasible c,a, never a grid

1. **Global technology and Cournot bounds** (verified by exact Sturm):
   - Regional active outsider KKT: `Y=2m+b-2d z>=4351/2500>0`; denominator `D<=10593/2500`, thus `y>=4351/10593`; all RS market quantities positive.
   - `x_{R,c}=2m(rho+v x_R)/D>0`; `x_{R,a}(1,a)<0` for the entire a∈[0,1] (root-free exact polynomial with negative endpoint). Therefore maximum `x_R` across entire feasible c,a TRIANGLE occurs at c=1,a=0 and yields exact `R_gross_max`.
   - In IS each firm's net `P_I` strictly decreases with a at any fixed c (`P_{I,a}=-6mk q_I²/(m+b)-phi a<0`) and increases with c along a=0 (root-free exact rational derivative). Hence exact net IS maximum `I_net_max` is at c=1,a=0.

2. **Private certification C after ANY first-stage unilateral open project** h=(N,N,O(c,a)), with arbitrary 0<a<=c or a=0. Every initially N firm strictly prefers to STAY at N regardless of the other N firm's migration:
   - if other N stays, joining creates bilateral RS but adopter profit at most `R_gross_max-K<P_N` since `K>K_L>=R_gross_max-P_N`;
   - if other N migrates, joining creates IS and its net payoff at most `I_net_max-K<O_gross_min_bound<=P_{O,RS}(c,a)` since `K>K_L>=I_net_max-O_gross_min_bound`.
   These two STRICT inequalities prove staying is DOMINANT for each initially N firm. Therefore the unique **economic allocation** after every C reference following any unilateral private O development is unchanged L, regardless of whether the initial O holder redundantly chooses its already-held specification. There is NO adopter-Nash-selection manipulation that can yield unilateral deviator a better payoff.

3. **Public mandate M after ANY unilateral initial development**: The real cost of conforming for a previously N firm or X/Y developer is at most `K+phi/2`, for O developer at most `phi/2`. All possible 1-,2-,3-complier public O(1,0) Cournot gross profits are at least `G_1=25/33>K+phi/2` since K<K_U<=G1-phi/2. Thus compliance is **STRICTLY DOMINANT** for every firm in this post-policy game, independent of opponents' actions, and the UNIQUE adopter Nash is all 3 comply. After M, a unilateral initial O(c,a) developer has resources `K+phi/2*(1+a²)>=K+phi/2` sunk+incremental, a proprietary X/Y developer incurs strictly more than K+phi/2 through refit. Therefore deviating firm's final profit is <=`I_net_max-K`, exactly the firm's payoff when initially N and then complying with M. Under L/C the solo developer gets only `P_N-K-phi(c²+a²)/2 < I_net_max-K`. Therefore no firm has ANY profitable initial deviation from h=(N,N,N), for **ALL real c,a in the original triangle and ALL X/Y/O/N families**, whatever equilibrium public policy G1/G2/G3 selects after the deviation. Some open advance investments may TIE when a=0, but cannot improve.

4. **Actual government optimum at h=(N,N,N)**: C is legally infeasible (nothing privately developed to recognize). Under M, each newcomer finds compliance strictly dominant, so national government payoff is `W_I^{public}(1,0;0)-K` and each compares to `W_N`. By K<K_U<=W_I^{public}(0)-WN, every government strictly prefers M over L; G1 proposes M and G2/G3 approve. Offpath after ANY other continuous h and any government p, adoption/exit games have finite binary strategy sets and therefore at least one MIXED Nash; G1/G2/G3 are sequential finite proposal/vote players and have optimal responses. Choosing any credible continuation at each offpath history constructs a SUBGAME-PERFECT strategy profile, and the onpath initial profile is globally immune to all real unilateral private technology changes by steps 2–3.

**Therefore an IS final outcome has been ACTUALLY PROVEN IN THE WHOLE CONTINUOUS CHOICE SPACE.** The cutoff surfaces are sufficient/existence thresholds, not necessary for all IS SPE and not uniqueness of IS.

## 4. Policy economics: government welfare can mandate what firms refuse to develop voluntarily

For K in (K_L,K_U), firms' *fully coordinated* direct private open IS net return `I_net_max-K` is LESS than the NS private payoff `P_N` whenever K>`I_net_max-P_N≈.37987` (already true on the entire theorem interval). Thus the absence of first-stage private coordinated development is consistent with firm incentives. However `W_I^{public}(0)-K>W_N` means domestic home CS gains more than offset the domestic profit reduction and implementation fee, so three governments all demand internationally compatible interfaces. An outside firm is NOT compelled to produce at a loss: after M its compliance payoff is `I_net_max-K>0` throughout this interval (since `K_U<.961355`), and conformity is its strictly dominant choice against any other adoption configuration.

This is a **deliberately specified public-versus-private rights equilibrium** that connects R&D stock and regulatory approval, not a universal theorem that public regulation always remedies underinvestment. Policy M supplies a LEGALLY existing blueprint, not unconsented patents, and mandatory exit is respected. Government can affect market implementation EVEN WHEN NO PRIVATE standard was initially developed because the public-domain blueprint was already available.

## 5. Finite-institution sensitivity (not the central theorem)

For transparency the source Stage5 finite 10-action per firm, ALL 1000 initial private profiles, all government decisions and binary adopter deviations are independently recounted under the new capital-stock cost function using exact Fraction arithmetic. The finite pilot shows:
- K=0: 29 finite-menu SPE, all IS (M 8,C 18,L 3).
- K=0.5: 33 finite-menu SPE, IS 27 and RS 6 (M 20,C 6,L 7).
- K=0.6: 17 finite-menu SPE, IS 6 and RS 11 (M 5,C 3,L 9).
- K=0.75: 1 finite-menu SPE, NS 1 (L 1).
These C/M/L / RS type counts under the new model may change AGAIN when arbitrary real designs and alternative mixed adopters are allowed. **Only the h=(NNN) final IS equilibrium on the exact K interval is genuinely certified full-continuous.** Under the same capital-stock fee, Stage6's separate high-K NS SPE bound K>235752/319225≈.738514 still holds, since at h=NNN the public mandate cost from N is unchanged and the old global Cournot investment-profit bound applies to all technology designs under any government response.

Thus, for a SINGLE now-explicit capital-stock economy with `eta=.03`, we have:
- rigorous continuous-initial-design **IS SPE existence** for `K∈(0.4794967,0.6580033)`,
- rigorous continuous-initial-design **NS SPE existence** for `K>0.7385136`,
- **RS full-continuous SPE existence NOT yet proven**, even though finite design menus show many examples at intermediate K.

The interval between .658 and .739 is a genuinely open research area, not proven absence of SPE. Offpath mixed adopter Nash continuation multiplicity does not defeat onpath IS theorem because after every unilateral private deviation, C and M have a unique ECONOMIC adoption allocation in this K interval.

## 6. Novelty and institutional modeling caveats

- This is an **applied economics model**, not a general new IO theorem; the underlying standards coordination, transition investment and multiple technology standards are established research fields.
- `c_i,a_i` are meaningful CONTINUOUS endogenously available firm choices but the onpath IS equilibrium has all firms initially N and then mandatorily implement the public pre-specified O(1,0), so **onpath public standard depth is externally FIXED**. Accordingly the finding does NOT establish endogenously optimal policy choice of regulatory depth nor fully endogenous company-designed IS technology on path.
- G1 governmental agenda power and unanimity are maintained; the policy standard O(1,0) is a legal existing resource, with no new real public technological invention and no independent government expense; if this blueprint is unavailable or costly to procure, revisit the result.
- A monopoly of post-recognition migration options by a government certification is a maintained institutional assumption, not a universal legal requirement.
- Same-O stock-upgrade fee ignores recertification/engineering adjustment when technology is downgraded. This simplification needs sector-specific empirical support or sensitivity test. Patent interfaces X/Y remain legally excluded absent licence; no ability to confiscate SEP rights.
- The six old product-market coefficients and Ghosh–Morita differentiating technology extension remain phenomenological rather than engineering-microfounded.

**Relevant prior art:** Farrell & Saloner (1985), *Standardization, Compatibility, and Innovation*, RAND J Econ 16:70–83 https://ideas.repec.org/a/rje/randje/v16y1985ispringp70-83.html ; Farrell & Saloner (1986), *Installed Base and Compatibility*, AER 76:940–955 https://www.gsb.stanford.edu/faculty-research/publications/installed-base-compatibility ; Aoki & Arai (2013), *Evolution of Standards and Innovation*, RIETI DP 13-E-075 https://www.rieti.go.jp/en/publications/summary/13090005.html ; FTC 2000 *Standard Setting in a Network Economy* https://www.ftc.gov/news-events/news/speeches/standard-setting-network-economy . This literature motivates economic caution about sunk installed base, disruptive changes and anticompetitive private standard monopoly.

**Proof and CI:** `code/stage8_capitalized_retrofit_continuous_is_spe.py`; `.github/workflows/stage8-capitalized-retrofit-continuous-is-spe.yml` ; run independent SymPy exact full-triangle derivative and inequality certificates plus original 3x3 KKT/three-government Fraction engine. All earlier PRs Draft, no manuscript overwritten or merged.
