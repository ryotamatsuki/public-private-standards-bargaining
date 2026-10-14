# Applied-Theory Repositioning: Network Effects, Product Distinctiveness, and Public–Private Standards Negotiation
Date: 2026-10-14 JST. Parent Draft PR #27: independent novelty audit (NO-GO for freestanding IO novelty).
**Research decision:** Reposition as a theoretically disciplined APPLIED model / comparative-institutional application of established industrial organization, entry/exit, product differentiation and unanimous consent. **NOT a newly discovered foundational bargaining or Cournot theory.**

## Working title and contribution
**Network Effects and the Political Economy of Regional versus International Standards: An Applied Cournot Bargaining Model.**

**Applied research question:** When does stronger interoperability/network benefit exclude a nonmember producer, and how can governments nonetheless favor the INTERNATIONAL rather than the REGIONAL standard? How do product differentiation, technical costs and each government's/firm's independent implementation approval rights delimit feasible harmonization?

**Claimed contribution:** an integrated, auditable six-primitive comparative-statics policy map with EXACT endogenous continuous standardization depth, KKT-correct outsider quantity, 3 national markets, governments internalizing home CS and worldwide resident producer profit, and distinct government/firm signature constraints. Individual mathematical ingredients and basic strong-Nash payoff comparisons are NOT claimed novel. Stage6 literature threats acknowledged below.

## Unchanged original model and institutional discipline

Exogenous only `theta=(v,gamma0,kappa,eta,rho,phi)`. The only negotiated continuous standard-depth `s in (0,1]`. Three products/firms and national governments, three segmented destinations. For RS(pair,s), in a representative destination:
`m=1-v>0`, insider cross-coefficient `b(s)=gamma0+(kappa-v)s`,
insider/outsider cross-coefficient `d(s)=gamma0-eta*s`,
insider cost advantage `z(s)=1+rho*s`. Consumer demand `p=1-Mq` after normalized unit initial cost advantage. All demand matrices SPD; 0<=b,d<m where required. Both insider producer quantities `x` and outsider `y` are recomputed via Cournot complementarity. NS and IS are rebuilt from the SAME utility and cost primitives. Inside coalition, private gross operating receipts in the three markets: `P_X^0=3m q_X^2`; implementation fee `phi*s²` paid ONCE. Government `W_X=P_X+CS_X` with home `CS_X=(q'Mq)/2`. These are rights/consent effects and do NOT create a new unilateral regulator, transfer, royalty, bargaining agenda or extra standardization knob.

Stage 1 exact agreement: RS requires BOTH firms and BOTH governments of the nominated pair (4 signers); IS all six; missing any signature => NS. One round same-content announcements, followed by Cournot. **Pure SPNE always permits all-SQ (coordination failure)**; do not claim a unique realized regime. To sharpen implementable contract SETS we use only STRONG NASH OF THE REDUCED stage1 announcement game, never whole-game strong Nash or coalition proof. No unconstrained planner choice or unmodeled government monopoly rights.

## Proposition A1 — exact network-exclusion / differentiation-reentry frontier (entire admissible 6D domain)

Define `A=2m+b`, `D=2m(2m+b)-2d²>0`.
The UNCONSTRAINED outsider numerator, before imposing y>=0, is
`Y(s;theta)=2(1-v)+gamma0+(kappa-v)s -2(gamma0-eta*s)(1+rho*s)`.
The unique correct Cournot/KKT outcome has outsider y>0 iff `Y>0`, otherwise y=0. Derivatives at EVERY fixed depth `s>0`:
`Y_v=-(2+s)<0`, `Y_eta=2s(1+rho*s)>0`, `Y_rho=-2s(gamma0-eta*s)<=0` when d>=0, `Y_kappa=s>0`, `Y_gamma0=-1-2rho*s<0`.
The fixed-depth network-strength exclusion frontier is
`v_out(s)=[2-gamma0+(kappa-2gamma0*rho)*s+2eta*s*(1+rho*s)]/(2+s)`.
For a feasible primitive vector, outsider activity switches from positive when `v<v_out` to zero when `v>=v_out`. Valid only where SPD, positive substitutability and the source cost structure continue to hold.
`d v_out/d eta=2s(1+rho*s)/(2+s)>0`;
`d v_out/d rho=-2s d/(2+s)<=0`.
**Interpretation:** stronger network effect or productivity gain in participating platforms crowds out outsider production; stronger outsider differentiation (eta rises, d falls) protects or restores outsider production. This is an applied KKT-comparative-statics lemma, not a novel market-foreclosure theorem.

## Proposition A2 — market-rivalry ratio and the government/private standards wedge (entire admissible KKT corner)

When RS outsider is INACTIVE at a chosen s>0, `x_R=z/(2m+b)`; IS all producers have `q_I=z/[2(m+b)]`. Compare BOTH format payoffs at the SAME depth and same fee.
**Private:** `P_R-P_I=3mb(3b+4m)z²/[4(m+b)²(2m+b)²]>0` when b>0.
**Government:** `W_R-W_I=z²[2b³+15b²m+12bm²-4m³]/[8(m+b)²(2m+b)²]`.
Set `u=b/m`, and `F(u)=2u³+15u²+12u-4`. F strictly increases for u>=0 and has ONE positive zero `u*=0.251570279593411...`. Thus the participating firm ALWAYS favors regional coordination in the true RS-corner market, but the government chooses IS at equal depth iff `u<u*`, and RS iff `u>u*`. No veto comparison of differing depths follows from this ALONE.

**Network mechanism (NOT just eta):**
`partial_v [b/m]=[gamma0+kappa*s-s]/(1-v)²`.
If `gamma0+kappa*s<s`, stronger networks LOWER u and can switch the participating government FROM RS to IS while `Y_v<0` simultaneously pushes the outsider DEEPER into nonproduction. This is the core conditional policy incidence result.

## Proposition A3 — consumer-surplus identity determines the binding public/private participation fee cap

Write `P_X=P_X^0-phi*s², W_X=W_X^0-phi*s²` for `X=RS,IS`, with `W_X^0=P_X^0+CS_X`, `W_N=P_N+CS_N`.
Firm/government willingness to pay per `s²` relative to NS:
`T_P^X(s)=[P_X^0(s)-P_N]/s²`;
`T_G^X(s)=[W_X^0(s)-W_N]/s²`.
**Exact identity**
`T_G^X(s)-T_P^X(s)=[CS_X(s)-CS_N]/s²`.
Thus if standardization RAISES domestic CS, the firm is the *stricter* signer for the common implementation fee; if it lowers CS, government is stricter; if equal, both identical. **Implementability iff phi<=min(T_P,T_G)** for the realized pure SPNE signed RS/IS contract (weak indifference permitted). This does NOT remove all-SQ Nash or check multi-coalition stability. It makes the PUBLIC-vs-PRIVATE veto division completely interpretable from consumer-surplus impacts, without new fee or regulator primitives.

## Proposition A4 — network-strength reversal of strong-standard coexistence on a genuine v-INTERVAL

Fix original FIVE exogenous coordinates
`(gamma0,kappa,eta,rho,phi)=(2/5,3/20,1/100,13/2,65/4)`
and vary **only network effect** `v in [39/100,41/100]`.
At full standard depth `s=1`:
`m=1-v`, `b=11/20-v`, `d=39/100`, `z=15/2`;
`Y(1)=-33/10-3v<0`. The outsider remains truly ZERO for BOTH sides and all v between. SPD for NS/RS/IS holds uniformly: m>=.59, b in [.14,.4] over [0,1], d in [.39,.4]; m-b>=.19, m(m+b)-2d²>=.1107.
All six algebraic payoff curves `P_R^active,W_R^active,P_R^corner,W_R^corner,P_I,W_I` are strictly INCREASING in depth `s in [0,1]` uniformly for v∈[.39,.41]. Proof is exact tensor Bernstein coefficient positivity for all six derivative numerator polynomials, 56 coefficients for each active branch and 20 each remaining branch, not a depth grid; each derivative denominator is a verified negative multiple of a positive power of D,A or m+b. Actual KKT piecewise branches join continuously at the outsider exit. Both members' RS and all IS signers strictly gain over NS at s=1 throughout the whole v interval (exact univariate Sturm sign/root proofs).

With outsider still zero at s=1,
`u(v)=(11/20-v)/(1-v)` strictly decreases,
`u(39/100)=16/61>u*`,
`u(41/100)=14/59<u*`.
Let
`v*=(11/20-u*)/(1-u*)≈0.3987411406437267`, strictly inside (.39,.41).
Governments prefer RS for `v<v*` and IS for `v>v*`; participating firms strictly prefer RS throughout. At `v=v*`, the government is indifferent and strict strong-Nash blocking fails, so IS survives.
**ENTIRE reduced-first-stage strong-Nash realized outcome correspondence:**
`E_strong(v)={RS(any country pair,1)}` if `.39<=v<v*`;
`E_strong(v)={RS(any country pair,1), IS(1)}` if `v*<=v<=.41`.
All RS/IS rates s<1 strongly blocked by same-type strictly deeper rate; NS blocked by matched full-depth RS; any alternative RS pair overlaps an incumbent participant, while full-depth opposite type cannot beat BOTH its firm and government. All-SQ is nonetheless a pure SPNE.
**Interpretation:** stronger network externalities ENHANCE outsider foreclosure (`Y_v<0`) yet RESURRECT the INTERNATIONAL standard as a stable public/private bargaining outcome, without outsider reentry or a changed real standardization fee. The direct route is the endogenous `b/m` ratio and the government's surplus incidence, not an invented KKT jump.

Exact rational two-point witness (all actual KKT):
At `v=39/100`: `P_RS(1)=37.80245747, P_IS(1)=27.15424186, W_RS(1)=60.54584121>W_IS(1)=60.24108197`: RS only.
At `v=41/100`: `P_RS(1)=40.89101240, P_IS(1)=30.45787202, W_RS(1)=64.45764463<W_IS(1)=64.89503190`: RS and IS survive.
**This is a nontrivial comparative-statics application, NOT claimed an original welfare-incidence algebra or strong-Nash selection rule.**

## Proposition A5 (optional supporting lemma) — differentiation-dependent KKT reentry and welfare incidence

From audited Stage6 PR #27: at ANY admissible `Y=0, s,d,D,m>0` across increasing eta, outsider production increases on active side; right derivatives of resident firm P, home CS, and national W are `(-3ms/(dD), +ms/(dD), -2ms/(dD))`, zero on inactive side. Immediate national profit loss dominates consumer benefit in exactly 3:1 ratio. Stage5B PR #26 additionally proves one feasible eta continuum yielding IS disappearance FOLLOWING outsider reentry. Neither by itself establishes a new general bargaining game.

## Applied paper architecture (proposed 18–24 text pages, not a journal rule)

1. Motivation: cross-country compatibility standards (industry interfaces, digital platforms, equipment), positive network effects, strategic product similarity, and distinct public/private implementation authority. Do NOT make industry-specific factual claims without data.
2. Literature **positioned as synthesis/application**: (i) standards as strategic protection [Fischer & Serra 2000], (ii) technology collaboration and regulatory protection [Edwards & Poyago-Theotoky 2013], (iii) private coalition and standards network effects [Casella 2001; Economides & Skrzypacz 2003], (iv) collaboration and product differentiation [Ghosh & Morita 2012], (v) bargaining/harmonization [Costinot 2008; Jørgensen & Schröder 2014; Cai & Jørgensen 2017].
3. Frozen six-exogenous-primitives original symmetric 3-country demand, finance, rights & first-stage consent.
4. Cournot NS/RS/IS with exact KKT outsider.
5. FOUR ordered applied propositions: A1 support frontier, A2 private/government incidence, A3 fee-veto, A4 FULL network paradox phase interval; optionally A5 differentiation reentry.
6. A small original-model comparative-statics display with labeled axes for v, eta, fee and theoretical welfare; exact reproducible robustness appendix, not a new bargaining model.
7. Institutional interpretation, possible observable operationalization, and **assumptions**: symmetric home markets, no within-market collusion, no transfers/royalties, fees real not license rents, network strength treated exogenous, and unanimity/strong-stage1 as selection **assumption**.
8. Conclusions and falsifiable predictions: (i) stronger v reduces outsider participation at fixed depth conditional on parameters; (ii) government/firm preference reversal depends on b/m; (iii) domestic CS increase predicts the tighter private signer; (iv) standards selection in high-network markets need not be exclusively regional even when outsiders are excluded.

**Scope/identification guardrails:** This is a theoretical applied example, not an empirical estimate or proof the real world obeys the unique signed coalition prediction. Distinguish model comparative statics from exogenous real-world causal identification. At the symmetric model level, NS remains a pure SPNE; the refinement is strong Nash only of the reduced first-stage announcement game, not Cournot strong Nash. Earlier Stage6 publication NOVELTY NO-GO is **retained**; the study's defensible contribution is a transparent cross-mechanism application and policy-relevant conditional predictions, subject to journal fit/empirical grounding.

## Known antecedents (verified publisher summaries or university repository)
- Fischer & Serra (2000), *Standards and protection*, JIE 52:377–400, https://www.sciencedirect.com/science/article/abs/pii/S0022199699000586. Exclusionary standards and home-government/producer conflict.
- Edwards & Poyago-Theotoky (2013), *Regulatory Protection When Firms Decide First on Technical Collaboration and R&D*, Review of International Economics 21:750–764, https://onlinelibrary.wiley.com/doi/10.1111/roie.12068. Tech collaboration/HTBT/government.
- Casella (2001), *Product Standards and International Trade: Harmonization through Private Coalitions?*, Kyklos; 1996 NBER precursor https://www.nber.org/papers/w5853. Private cross-border coalitions.
- Ghosh & Morita (2012), *Competitor collaboration and product distinctiveness*, IJIO 30:137–152, https://www.sciencedirect.com/science/article/pii/S0167718711000671. Partner-vs-outsider differentiation and welfare.
- Bourreau, Doğan & Manant (2016), *Size of RJVs with partial cooperation in product development*, IJIO 46:77–106, DOI 10.1016/j.ijindorg.2016.04.004. Cooperation intensity/coalition membership trade-off; full final version still needs comparative proof check.

**Implementation:** `code/applied_standards_network_differentiation_propositions.py`, `.github/workflows/applied-standards-network-differentiation.yml`. All upstream PRs remain DRAFT and unmerged; no previous theoretical result or manuscript silently overwritten.
