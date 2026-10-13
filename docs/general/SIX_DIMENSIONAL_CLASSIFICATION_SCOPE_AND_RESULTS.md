# Six-dimensional parameter-space re-entry: exact domain, Cournot corners, certified regions
**Date:** 2026-10-14 JST | **Source:** ORIGINAL single endogenous s, exogenous network coefficient v; child of Draft PR #13, NOT the optional 2-choice PR #11.
**Scientific decision:** the old v-only classification does NOT constitute a full multi-parameter classification. This branch makes material mathematical progress but does NOT claim a completed quantifier-free six-dimensional equilibrium phase diagram. DO NOT promote this work to Stage 4A PASS, Stage 6 GO, or manuscript.

## 1. Exact reduction from eight to six essential parameters
Let A=a−c0>0, γ=gamma0, ρ=h/A and φ=f/A². Divide each firm's output by A and divide all real firm profits and governmental national welfare by A². A positive constant scaling of every actor's payoff preserves all preference comparisons and the entire Stage-1 simultaneous proposal game, even at boundary output solutions.

All economically relevant outcomes depend only on
   θ=(v,γ,κ,η,ρ,φ)
and s, where all six θ coordinates are independently varied as EXOGENOUS parameters and s remains the ONLY freely negotiated standardization/commonality depth. The associated prior dimension count (a,c0,h,f,γ,κ,η,v) was reducible due to demand/cost affine translation plus output scaling. Note that a restriction on price levels or c0 itself would require additional economic constraints; none is in the current source.

Natural economic parameter domain:
 0≤v<1; 0≤γ; κ≥0; 0≤η≤γ; ρ≥0; φ>0.
η≤γ guarantees member–outsider substitution d(s)≥0; products remain substitutes, not cross-complements. This is an intentionally explicit ECONOMIC domain; outside it different KKT branches including outsider-only demand may be relevant and are NOT covered. It is improper to claim this work classifies literally arbitrary real coefficients or non-SPD preferences.

## 2. Demand SPD: complete explicit inequalities, not a grid
Let m=1−v>0, b(s)=γ+(κ−v)s, d(s)=γ−ηs. The three demand matrices for NS, RS and IS are SPD for EVERY real s∈[0,1] **iff**:
  m−γ>0,
  m+2γ>0,
  m−(γ+κ−v)>0,
  m+2(γ+κ−v)>0,
  m[m+(γ+κ−v)]−2(γ−η)²>0.
Proof: NS SPD iff first two. IS has eigenvalues m−b (double) and m+2b; the two functions are affine in s and their minima are attained at s∈{0,1}. RS has eigenvalue m−b and remaining 2×2 block with determinant m(m+b)−2d². This last expression is a CONCAVE quadratic in s (coefficient −2η²) so its minimum occurs at s=0 or s=1; s=0 is already covered by NS inequalities. This yields the five displayed θ-polynomial conditions without universal s quantifiers. In particular m−b(1)=1−γ−κ, independent of v.

This source-domain validation does NOT by itself guarantee all Cournot outputs are interior; in fact, the RS outsider may rationally withdraw.

## 3. FULL Cournot continuation including boundary outputs (not previously modeled)
Normalize A=1. For NS all 3 firms produce qN=1/[2(m+γ)]; for IS all 3 produce qI=(1+ρs)/[2(m+b(s))]. These are strictly positive for the domain above.

For RS, two symmetric member firms always produce positive amounts under γ≥η≥0, A>0, ρ≥0 and SPD. The RS outsider can optimally choose zero. Define
 D(s)=2m[2m+b(s)]−2d(s)²>0,
 X(s)=2m(1+ρs)−d(s),
 Y(s)=2m+b(s)−2d(s)(1+ρs).

If Y(s)>0, the unique Cournot continuation is interior:
   x(s)=X(s)/D(s), y(s)=Y(s)/D(s).
If Y(s)≤0, the true RS Cournot equilibrium is a BOUNDARY solution:
   x(s)=(1+ρs)/[2m+b(s)], y(s)=0.
At Y=0 the two formulas agree. Rationale: the insider FOCs are symmetric; if y=0 the outsider's marginal profit at zero is 1−2d(s)x(s)=Y(s)/[2m+b(s)]≤0, hence its zero-output KKT condition holds. By SPD and demand concavity the Cournot continuation is unique; an outsider-only equilibrium is excluded since the insider's margin at zero is strictly positive when d(s)<m and ρ≥0.

The switching polynomial is QUADRATIC:
  Y(s)=(2m−γ)
       +[(κ−v)−2γρ+2η]s
       +2ηρ s².
It can have TWO roots in (0,1): the outsider can EXIT at an intermediate standardization depth and REENTER later at high s. Exact regression θ=(3/10,3/5,0,3/5,10,1/5) gives Y(s)=(120s²−111s+8)/10, Y(0)>0,Y(1/2)<0,Y(1)>0, all demands SPD. Hence the older globally interior general-theta classifier was NOT a complete representation of the economically allowed six-dimensional source domain.

For RS with x,y chosen by the correct branch: national local
 CS_R=(m+b)x²+2dxy+(m/2)y²;
 participant P_R=3m x²−φs², W_R=P_R+CS_R;
 outsider O_R=3m y², U_R=O_R+CS_R.
IS P_I=3m qI²−φs², W_I=P_I+3(m+2b)qI²/2;
NS P_N=3m qN²,W_N=P_N+3(m+2γ)qN²/2.
World accounting is exact, including integration cost paid ONCE per joining firm and never multiplied by the number of destination markets. Independently checked in script.

## 4. Complete logical six-parameter classification targets
For any θ in the explicit domain, define a strict profitable-deviation oracle
  B_X(p,w;θ)=1 iff ∃t∈(0,1], P_X(t;θ)>p AND W_X(t;θ)>w,
where X∈{R,I} and R is evaluated using the correct Cournot interior/corner branch.

The strong-Nash CONTRACT OUTCOME TYPE triple is
   χ(θ)=(χ_N,χ_R,χ_I)∈{0,1}³.

N-type exists iff B_R(P_N,W_N)=B_I(P_N,W_N)=0.
R-type exists iff there is s∈(0,1] with:
   P_R(s)≥P_N, W_R(s)≥W_N;
   B_R(P_R(s),W_R(s))=0;
   B_I(max[P_R(s),O_R(s)],max[W_R(s),U_R(s)])=0.
I-type exists iff there is s∈(0,1] with:
   P_I(s)≥P_N, W_I(s)≥W_N;
   B_I(P_I(s),W_I(s))=0;
   B_R(P_I(s),W_I(s))=0.
The R MAX predicate tests EXISTENCE of a supporting strong-Nash exact-message profile (outsiders originally announce SQ). For robustness across EVERY supporting outsider message replace that last B_I threshold by (P_R(s),W_R(s)). This corrects a real error in pre-Stage4A drafts: already-preannounced losers do NOT have to gain if they do not deviate.

The eight Boolean possibilities for χ are logically disjoint sets of θ, **but their defining existential/universal s,t quantifiers have NOT all been eliminated**. This is an exact set-theoretic *specification* of the full phase partition, not a quantifier-free cell listing. Proving which sign cells are empty and producing explicit defining polynomials remains necessary to honestly call the six-dimensional classification complete.

### Constructive exact membership oracle (new)
\`code/verify_six_dimensional_corners.py\` accepts any RATIONAL six-parameter θ in the stated economic/SPD domain and any RATIONAL candidate s. It computes P_R,W_R,O_R,U_R with the correct KKT boundary switch, then decides ALL profitable RS/IS deviations at EVERY real t∈(0,1]. It isolates exact roots of the product of all payoff-comparison numerator polynomials AND the corner-switch polynomial Y, adaptively refines root boxes near s=0/1, and checks each constant-sign cell with rational samples. Thus the inner B oracle and a candidate's exact strong-Nash membership are NOT inferred from a finite numerical mesh.
**This is NOT yet an automatic complete χ(θ) classifier**, since deciding whether SOME s passes R or I requires one additional quantified-depth elimination. Also, arbitrary irrational θ requires exact real-algebraic coefficient representation or a general CAD backend, not approximate floats.

## 5. Two NEW general 6D sign conditions, including a nonempty NS-only region
Set δ=κ−v and m=1−v. Define
 D0=2m(2m+γ)−2γ²,
 D1=2mδ+4γη,
 X0=2m−γ,
 X1=2mρ+η.

**Public/private IS local incentive:** define
 K=ρ(m+γ)−δ.
 qI'(s)=K/[2(m+γ+δs)²], sign constant across admissible s.
 For φ>0, if K≤0 then P_I(s)<P_N for EVERY s>0, so joint signed IS can NEVER be strong stable (a complete six-parameter IS exclusion region). If K>0, local private entry is profitable near s=0 but global joint acceptance and no RS deviation need not hold.
 Define L=(3m+2γ)K+δ(m+γ).
 Government's marginal national welfare gain at zero satisfies
 W_I'(0)=3L/[4(m+γ)³]. Hence public/private incentives can be compared with two explicit six-parameter polynomials K and L, while this derivative alone cannot globally classify IS.

**Global NS-only sufficient region:** define
 B=(X1 D0−X0 D1)+2η²X0.
For the HYPOTHETICAL interior RS solution qR,int, there is the exact identity
  qR,int(s)−qN = s[(X1D0−X0D1)+2η²X0s]/[D(s)D0].
On the demand/SPD domain X0,D(s),D0>0. If B≤0, the bracket cannot be positive for any s∈[0,1], so qR,int≤qN. In a corner where the outside firm's hypothetical quantity would be negative, actual RS member output is even LOWER than qR,int because d≥0. Thus actual qR≤qN for every s, and the real φs² integration outlay makes P_R(s)<P_N for EVERY s>0.

Therefore, on the WHOLE admissible six-dimensional parameter domain:
    K≤0 AND B≤0  ==> NS is the UNIQUE strong-Nash CONTRACT TYPE.
The sufficiency region has nonempty OPEN INTERIOR: the exact rational witness
  (v,γ,κ,η,ρ,φ)=(1/50,1/4,2/5,1/100,1/200,1/10)
has STRICT K<0 and B<0 with SPD demand, so this is not a knife-edge example. Proof/verification: \`code/verify_six_dimensional_exclusion.py\`.
This theorem classifies an exact six-dimensional OPEN REGION, not just a chosen v value; it does not pretend to identify the entire NS boundary.

## 6. Tests, consequences, uncompleted global phase partition
The exact code reproduces the earlier fixed-other-parameter witness outcomes at v=1/10,1/5,3/10, a strict NS-only example, outsider-exit and outsider-REENTRY corner example, and a tiny (<10^-30 depth) strict-gain adversarial test. It rejects non-SPD parameters rather than passing them to false interior formulas. It does not perform a global result enumeration for all θ. No symbolic polynomial sign table for all χ cells, no full outer quantifier elimination, no asymmetric-country cases, no positive-volume empirical calibration, no independent human/math referee or stage4A certification of new corner/game claims.

**Required next gate to complete the user's demand, not optional polish:** perform an exact six-parameter CAD/real-quantifier-elimination of the R/I existence formulas above with piecewise Y(s)≥0/Y(s)≤0; give a finite quantifier-FREE polynomial sign representation of each NONEMPTY χ-region, identify all boundary, tangent, corner and multiple-equilibrium cells, and then analyze each continuous s-equilibrium branch's parameter derivatives. A merely sampled v-range, a collection of benchmark examples or this conditional theorem is NOT that completed task.
