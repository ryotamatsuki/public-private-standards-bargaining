# Stage 3 re-entry: network-dependent REENTRANT OUTSIDER ACTIVITY under an endogenous regional standard
Date: 2026-10-14 JST. Parent: Draft PR #20 Stage6 economic novelty NO-GO for generic gov/firm veto and high-cost partial-standard coexistence. This is a NEW, narrower demand-STRUCTURE question. It is NOT a reinstatement of the killed joint-veto novelty claim and NOT Stage6 novelty GO.

## 0. Selection, original game, and non-change-control
**Candidate A — CONDITIONAL GO to a narrowly bounded Stage4/independent4A attack.** Retain the ORIGINAL one endogenous standardization/technical commonality depth s∈(0,1], outside network coefficient v exogenous and simultaneous exact RS/IS country-government/firm signatures, with noncooperative Cournot stage 2. Do NOT add a second endogenously chosen compatibility variable, franchise/IP instrument, or timing stage. Demand M has own coefficient m=1−v, within regional members b(s)=gamma0+(kappa−v)s, outsider coefficient d(s)=gamma0−eta*s. Use the **original stronger calibration restriction eta=kappa/2**, so the effect cannot be attributed to loosening outsider substitutability into a new independent dimension. Nonnegative real post-standard marginal cost c0−h*s is enforced in the witness. All demands remain SPD, all own outputs feasible under exact zero-output KKT.

Distinguish carefully between OUTSIDER *resident producer* temporarily producing ZERO quantities in EVERY segmented national Cournot market and the OUTSIDER *country* being EXCLUDED from the RS coalition. Outsider is always a nonmember under any RS identity; the NEW reentry refers to actual product-market supply, not the country's coalition membership or an open-entry industry with sunk costs. This avoids incorrect interpretations.

## 1. The **necessary-and-sufficient** mechanism condition (GENERAL symbolic economic primitives)
Let A=a−c0>0, rho=h/A>=0, m=1−v>0, b(s)=gamma0+(kappa−v)s, d(s)=gamma0−eta*s>=0 on [0,1]. Under RS(C,s), the outsider's desired interior Cournot output is
  y_int(s)=A Y(s)/D(s),
  D(s)=2m(2m+b(s))−2d(s)^2>0,
  Y(s)=2m+b(s)−2d(s)(1+rho*s)
      = C+B*s+Q*s^2,
  C=2m−gamma0>0,
  B=kappa−v+2eta−2gamma0*rho,
  Q=2eta*rho.
The true outsider output is y=max{0,y_int(s)}, with INSIDER output recomputed at the corner x=(A+h*s)/(2m+b(s)) when Y<=0. At Y>0, x=[2m(A+h*s)−d*A]/D. These piecewise equations satisfy the differentiated-Cournot exact KKT system. All national consumer surpluses and worldwide payoffs use these genuine branch outputs.

When **Q>0 (eta>0 and rho>0)**, there exist TWO distinct Cournot activity transitions 0<s_-<s_+<1, with outsider
   active on [0,s_-),
   inactive on [s_-,s_+],
   active again on (s_+,1]
IF AND ONLY IF all following hold:
  (i) B<0,
  (ii) 0< -B/(2Q) <1 (vertex strictly interior),
  (iii) B^2−4Q*C>0 (vertex below zero),
  (iv) C+B+Q>0 (positive outsider desired output at s=1).
Because C>0 holds in the SPD substitutes domain, these are NECESSARY AND SUFFICIENT. The exact boundaries are
  s_±=[-B ± sqrt(B²−4Q*C)]/(2Q).
For Q=0, Y is affine in s and has at most ONE transition, proving a **joint necessity of BOTH inside-member cost reductions h>0 and outside-product distinctiveness response eta>0** in this linear LQ model for two-crossing outsider exit/reentry. Costs, quantities and the outside standard intensity s are ordinary model inputs; no desired U-shape is assumed directly in payoff.

The economics of the curvature is precise: increasing s gives incumbent members a cost-saving advantage that **initially harms outside output**; however the cross-member–outsider substitution coefficient d(s) simultaneously DECREASES, relieving competitive pressure by the incumbents at high s, while the term −2d(s)rho s creates +2eta*rho s². Either mechanism alone (h=0 or eta=0) kills the strictly convex quadratic and makes two-crossing impossible. This is a **restriction derived from demand and Cournot KKT**, not a free arbitrary two-type veto payoff.

For fixed ORIGINAL gamma0,kappa,eta,rho and s, v changes BOTH own m=1−v and within-club cross slope b(s), hence
   ∂Y(s;v)/∂v = −(2+s)<0.
A source-specific threshold for outsider active output at EACH s is
   v_exit(s)= [2−gamma0+(kappa+2eta−2gamma0*rho)*s+2eta*rho*s²]/(2+s),
with y(s)>0 iff v<v_exit(s) in SPD economic domain. Do NOT label this as a pure cross-compatibility effect holding standalone own-network value constant.

## 2. Original η=κ/2, positive-marginal-cost open ECONOMIC witness
Set:
 a=1, c0=9/10, h=1/2, f=15/38,
 gamma0=9/25=.36, kappa=3/5=.6, eta=kappa/2=3/10=.3,
 and consider EXOGENOUS v∈[0,16/25)= [0,.64).
Then rho=h/(a−c0)=5, post-standard marginal cost c0−h*s≥.4>0 for ALL s∈[0,1], nonnegative base c0, all goods remain differentiated demand substitutes (d(s)>=.06>0, b(s)>0 for the economically relevant tested v). NS, RS and IS inverse-demand matrices are strictly SPD across v∈[0,.64),s∈[0,1] (verified via eigenvalue and endpoint-minor inequalities). NS own-vs-cross eigen m−gamma0>0 until v=.64. Every necessary Cournot system unique in the KKT demand domain.

For this fixed collection of OTHERWISE ORIGINAL primitives,
   Y(s;v)=(41/25−2v)−(12/5+v)s+3s²,
   discriminant Δ(v)=v²+(144/5)v−348/25.
Define exact NETWORK threshold
   v_crit=(-72+2*sqrt(1383))/5 ≈0.47548318542964.
This is the UNIQUE root in (0,.64); vertex s_v=(12/5+v)/6 always lies strictly within (0,1), and Y(0;v),Y(1;v)>0 over the entire admissible network v interval.
**THEOREM (network-induced active-set bifurcation within valid original source primitives):**
 - If 0<=v<v_crit: outsider produces a strictly positive quantity for ALL RS depths 0<=s<=1.
 - At v=v_crit: its interior desired output touches zero at a UNIQUE intermediate depth; exact zero-production at that point, positive elsewhere.
 - If v_crit<v<.64: TWO distinct interior standardized depths s_-(v)<s_+(v) exist; outsider Cournot output becomes exactly ZERO on the entire closed interval [s_-,s_+], and reappears beyond s_+.
This is an EXACT sign/discriminant theorem on a WHOLE admissible exogenous network parameter interval, NOT two isolated simulation points. v influences both diagonal and compatibility coefficients, and interpretation must mention that non-identification.

At v=31/50=.62:
  Y(s)=3s²−(151/50)s+2/5,
  s_±=(151 ± sqrt(10801))/300 ≈0.15690713468 and 0.84975953198.
The outsider produces at s=.05, STOPS throughout s∈[.1569,.8498], and REENTERS at s=.95 and s=1. Importantly s=.5 is WELL INSIDE excluded production interval (Y(.5)=−9/25<0); SPD, positive domestic producer quantities and nonnegative marginal costs verified explicitly.

## 3. Not just an off-equilibrium curiosity: TRUE coalition-stable REGIONAL standard can STOP outsider production
Still at same real economy v=.62 and f=15/38, choose RS({1,2}, s=1/2). Normalize F=m*f/(a−c0)^2=15 (all other 5D variables implicit). The source-game government and firm participant payoffs under noncooperative Cournot with the outsider output KKT zero give, in normalized units P̂=(m/A²)*P and Ŵ=(m/A²)*W:
 RS member P̂_R(.5)=9151/16428≈.557037,
 RS member Ŵ_R(.5)=163379/49284≈3.315052,
 RS outsider firm P̂_O(.5)=0 (completely out of the product market),
 RS outsider GOVERNMENT Ŵ_O(.5)=67963/24642≈2.758015,
 NS resident profit P̂_N=1083/5476≈.197772,
 NS resident welfare Ŵ_N=5301/10952≈.484021.

Therefore RS incumbent 4 signers ALL have STRICT gains vs NS (SPNE IR). More surprisingly, the excluded outsider country's **government** GAINS welfare relative to NS even while its resident PRODUCER exits: home consumers benefit from imported member goods, which outweighs lost domestic producer profit. This is not an additional institution: national W=domestic CS+worldwide firm profit was already part of the original model. Outside country cannot veto RS.

To independently prove stage1 **strong Nash of the RS contract for EVERY possible outsider original message**, show:
 (a) MEMBER government W_R(t) strictly increases for EVERY t∈(0,.5), even across any KKT switch. This is certified using both analytic interior and corner derivative rational functions and exact Sturm no-root intervals; hence no profitable four-signer RS-depth reduction.
 (b) MEMBER firm P_R(t) strictly decreases for EVERY t∈(.5,1], again using both Cournot branches and exact Sturm no-root intervals; hence no profitable four-signer RS-depth increase.
 (c) P_R(.5)>P_I(t) for EVERY t∈[0,1], exact rational polynomial Sturm certificate, so REGIONAL firm incumbent blocks **any IS deviation regardless of the RS outsider's prior preannounced IS**.
 (d) There is no other profitable named RS pair deviation, by strict welfare/profit-veto symmetry of the incumbent members and the same-pair comparisons; outsider cannot alone break a matched RS.
 (e) RS outsider x=0 corner KKT and no-cost dummy output histories correctly treated; required four signers individually rational.
Hence RS(pair,s=.5) is a TRUE strong-Nash contract outcome of the **REDUCED Stage1 proposal game with Nash–Cournot Stage2 continuation**. NOT a coalition-strong equilibrium of the WHOLE two-stage game; Stage2 Cournot is susceptible to product-market multi-firm output reductions as recorded in PR#19.

Each key inequality is strict away from roots and has positive margins at s=.5 and all-depth comparisons, so a NONEMPTY OPEN neighborhood of ORIGINAL exogenous demand/cost parameters retains BOTH two-root exit/reentry and reduced-game strong stability of RS(.5), with its outsider government gaining despite its producer shutting down. Therefore the result is not an economic knife edge. A social-welfare comparison against alternate *IS* contracts, planner first best and public recognition policy are NOT yet proven, and no claims made about unique strong-Nash equilibrium or model-wide selection.

Exact reproducibility: \`code/verify_stage3_outsider_reentry.py\` uses independent SymPy algebra with analytic 2-root discriminant, SPD endpoint/minor checks, full interior vs zero-output KKT, real cost lower bound, exact national profits/W values and polynomial Sturm signs over entire continuous contract-depth ranges; GitHub Actions CI to be checked before saying PASS. No numeric mesh, no extrapolated interior outputs.

## 4. Stage 3 prior-art kill: three credible routes (no inflated candidate bank)
**Candidate A — selected CONDITIONAL GO Stage 3 only:** Cost-reduction × product-differentiation produces a *reentrant outsider producer market participation* window under ONE increasing regional standard depth, with both zero-activity boundaries analytical, and can be a first-stage strong contract outcome. No added economic primitive. Nearest threat: Ghosh–Morita (IJIO 2012) demonstrates outsourcing distinctiveness + reduced costs and outsider-price/profit ambiguity, but available published abstract/introduction do not establish TWO distinct activity switches along a continuous collaboration depth. Lukach–Kort–Plasmans 2007 oligopoly standard coalition with variable network density remains ABSTRACT only and main access threat. Entry/exit under quality standards is known (e.g., Kuno/Toulouse and technical-regulation literatures; no claim of general novelty). Exact falsifier: prove such double root impossible under η=κ/2/SPD/nonnegative real costs, or show the allegedly stable middle-depth RS can be jointly improved by one alternate valid RS/IS depth. Direct symbolic/Sturm mathematical screen finds neither falsifier in source model. Authoritative new institutional comparison: Takarada & Kawabata (2025) *Multilateral Versus Regional Mutual Recognition*, NU city University DP701 PDF abstract+intro read. Three-country continuous government standards with regional-vs-multilateral recognition, regional benefits outsider govt possible, but no verified proposition on producer output reentry under original game's endogenous compatibility/differentiation.
**Candidate B — subsidiary of A, NOT independent novelty:** A nonmember government can BENEFIT while its resident firm is driven completely out; under this source model W_O=home CS. This is an equilibrium government-versus-resident producer incidence claim, with real import competition, but generic national welfare conflict and gains to outsiders already in Gandal–Shy (2001) and Takarada–Kawabata (2025). Do NOT double count as second research contribution.
**Candidate C — deferred, no new-model authorization:** Isolate pure cross-network interoperability from own-network value by treating v and m separately. Potential sharp comparative statics, but changes primitive independence, must return Stage3 change control and rerun full model, and product network compatibility already present in ES03/LKP07. Immediate risk: artificial independent coefficient introduced only to flip signs. Do NOT implement just to salvage novelty.

Main exact prior-art threats and reading levels:
- Ghosh & Morita (2012), IJIO 30(2): publisher full abstract and intro inspected; collaboraters become less distinct and noncollaborator more differentiated, ambiguous outsider profit; direct source of the mechanism, NOT a claim new to IO absent specified reentry/fixed condition.
- Bourreau, Doğan & Manant (2016) IJIO: 2014 original FULL working paper Sec4.1 (from Stage6), endogenous scope and coalition-size Cournot already; need scan their activity-regime assumptions to see if zero-output rivals permitted, not assume outside firm always interior.
- Lukach, Kort & Plasmans (2007/08): institution & ResearchGate abstract only, no theorem-level full text (strong unresolved).
- Gandal & Shy (2001) JIE 53: 3-country government standard unions can exclude outsider, different standards object; publisher abstract/introduction inspected.
- Economides & Skrzypacz (2003): network-based standards coalitions familiar; previous author PDF targeted propositions previously read.
- Takarada & Kawabata (Feb 2025) *Multilateral Versus Regional Mutual Recognition*, three-country oligopoly, CONTINUOUS region/multilateral government standard negotiations; institutional WP PDF introduction and abstract + first-page screenshot inspected. Its outsider-government benefit and region/multilateral results are a NEW strong direct threat; their content is asymmetric to source technology standard depth/outsider market reentry; all remaining theorem comparisons pending.
- Macedoni & Weinberger (2024) regulations and firm entry, CESifo abstract, general positive foreign spillovers (not same effect).
- Firm-exit under strong quality standards is known, e.g. established duopoly quality standards literature (don't misstate exit itself as new).

## 5. Stage 3 gate and NEXT strictly bounded proof
**CONDITIONAL GO** to Stage4 mathematical full theorem ONLY for the exact network bifurcation + equilibrium-implemented outsider activity window. The statement is much stronger than merely 'regional standards harm rivals' and is NOT mechanically predicted by arbitrary coalition veto payoffs. Yet mathematical distinction is NOT proof of publishable contribution; many Cournot entry/exit theorems may absorb result. Stage4 independent auditor must:
1. independently derive true KKT including zero outsider, explicit discriminant equivalence and the full admissible parameter domain η=κ/2;
2. replay third-party full stage-1 coalitional deviations with alternative pairs and outsider preannouncements, not only same-standard FOC;
3. test whether outsider government's welfare gain is robust in a nontrivial multi-parameter open region, without tuning negative costs;
4. compare predecessor Ghosh–Morita 2012, Takarada–Kawabata 2025, Lukach–Kort–Plasmans 2007 and Bourreau–Doğan–Manant 2016 at proposition/model level; stop if same reentry result and institutional consequence is already proved;
5. seek ONE substantive *further* equilibrium/welfare implication where observable market exit-and-reentry thresholds change equilibrium selection or welfare rankings; absent this, do NOT automatically claim economic novelty GO.
Preserve parent PR#20 NO-GO verdict for earlier pure veto claims. Do NOT merge or start paper submission on a Stage3 mechanism hypothesis.
