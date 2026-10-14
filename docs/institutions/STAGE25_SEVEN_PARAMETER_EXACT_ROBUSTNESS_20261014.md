# Stage 25 — Exact seven-parameter local robustness of the unique public-IS pure-SPE terminal outcome

2026-10-14. This is a STACKED research PR on Stage24 Draft PR #52; no prior branches merged, no manuscript edited.

## ST25.1 — nondegenerate SEVEN-dimensional parameter product box

Maintain the exact three-firm/three-national-government OPEN/N only minimal model: each firm initially invests in N or an independently chosen real O(c_i,a_i) with 0<=a_i<=c_i<=1. Existing legally public O(1,0) may be mandated by ANY government; national simple majority (two YES votes) enacts M, including national ties; no transfers, patents, private certification or exclusive agenda. Prior O capital and setup are sunk, post-M within-family public retrofit only adds the missing c stock. National welfare is firm net profit plus identical-market consumer surplus.

The Stage24 certified \((\eta,K,\phi,\rho,\kappa)\) rectangle remains fixed:
\[
\eta\in[.10,.14], \quad K\in[.54,.56],\quad \phi\in[.13,.30],
\quad \rho\in[.319,.321],\quad \kappa\in[.019,.021].
\]
Now additionally allow **independent simultaneous** variations
\[
\boxed{
v\in[.009999,.010001],\qquad
\gamma_0\in[.139999,.140001],
\qquad m=1-v.
}
\]

**Theorem ST25.1:** For EVERY point in this full continuous **seven-dimensional** box, at least one pure-strategy SPE exists (initial NNN, subsequent universal public O(1,0)), and EVERY pure-strategy SPE has **publicly mandated universal IS** as its terminal standard type. This is pure terminal outcome uniqueness, NOT unique initial investment vectors, NOT mixed-SPE classification, and NOT a global 7D necessary/sufficient phase partition.

## Rigorous proof strategy — avoid millions of unnecessary 7D Bernstein coefficients

The Stage24 result checked 251,436 Bernstein entries across **five normalized technical and parameter variables**, at BOTH endpoints of phi. Its three-O national welfare certificates had a few zero coefficients exactly on identical-public-standard technical faces. Thus naïve continuity of a strictly positive function would be invalid without an explicit analysis of those zeros.

Stage25 proceeds rigorously in four parts.

### 1. Lift to polynomial coefficients with no v,gamma denominator

Put \(m=1-v\), \(H=m+\gamma_0-v=1+\gamma_0-2v>0\). Let \(z_0=1+\rho\). Public **gross** national profit plus CS is
\[
G_I=\frac{[3m+\frac32(m+2(\gamma_0-v))]\,z_0^2}{4H^2}.
\]
Multiply the 2-O governmental-sign numerator and all 3-O national governmental-sign numerators by the strictly positive \(H^2\). The private high-a \(-f_a\) numerator needs no such multiplication. These lifted polynomials have polynomial—not rational—coefficients in v and gamma0, and remain affine in phi. At the nominal v=.01, gamma0=.14, the multiplication is by the positive constant \((28/25)^2\), so all sign certificates are preserved.

The Stage25 source **recomputes** the complete baseline Bernstein expansions for both phi endpoints with an auditable converter. It verifies that every NONZERO coefficient of the lifted polynomials is **strictly >1/50** (0.02), not merely nonnegative. It also enumerates all zero indices and checks there are no other zeros or negative coefficients. The five classes are:
- 2-O low-a YES government sign, 2-O high-a strictly negative private marginal;
- 3-O aligned min-c/min-a government G2;
- 3-O crossed-maximal-ties G1 and G2.

### 2. Every nominal zero is structurally zero for ALL v,gamma0

For the aligned 3-O polynomial, the **only zero technology Bernstein index** corresponds to \((t,s,w,h)=(1,1,0,0)\), with all rho and kappa indices: in that face the pairwise min design is EXACTLY the public standard O(1,0), and the private-to-public national policy difference is identically zero.

For the crossed 3-O polynomials the only zero technology indices are the 5 possible fourth-design-axis entries with \(t=s=1,u=0\), with all rho and kappa indices: all three private designs then implement O(1,0) in every pair. National public/private Cournot and remaining capital are identical, hence the policy difference vanishes exactly.

Using FULLY SYMBOLIC \(v,\gamma_0,\rho,\kappa,\phi\), the Stage25 script directly simplifies all corresponding lifted welfare numerators to **identically zero**. Thus all 11 technology zero positions (multiplied by parameter Bernstein axes, giving Stage24's 15+105+105) remain **zero throughout the new perturbation box**. No sign-continuity assertion is needed at these corners.

### 3. Coefficient-wise Lipschitz bound in both new primitives

Take the wider comparison box \(v\in[.009,.011]\), \(\gamma_0\in[.139,.141]\) (strictly contains the claimed new rectangle). For each of the five normalized-variable polynomial expressions \(P\), define the coefficient one-norm \(\|P\|_1\) as the sum of absolute power-basis coefficients over the original five unit-box variables.

The source constructs mathematically rigorous **upper bounds** for \(\|P\|_1\), \(\|\partial_v P\|_1\) and \(\|\partial_{\gamma_0}P\|_1\) using recursively verified rules:
\[
\|P+Q\|_1\le\|P\|_1+\|Q\|_1,
\quad
\|PQ\|_1\le\|P\|_1\|Q\|_1,
\quad
\|\partial_v(PQ)\|_1
 \le\|\partial_vP\|_1\|Q\|_1+
 \|P\|_1\|\partial_vQ\|_1.
\]
The same rule applies to the gamma0 derivative. All upper bounds use **exact rational arithmetic**; no sampled slopes. For every class (2-O low/high, 3-O aligned/crossed G1/G2), the conservative total bound satisfies
\[
\|\partial_vP\|_1+\|\partial_{\gamma_0}P\|_1 < 13,000.
\]

Every power monomial \(x^\alpha\) has Bernstein coefficients within [0,1] on a unit cube. Therefore each Bernstein coefficient of \(\partial P\) is bounded in absolute value by the corresponding derivative coefficient one-norm. Two sequential one-variable mean-value bounds (v and gamma0) imply, for any v,gamma0 within \(10^{-6}\) of their nominal levels:
\[
|\beta_\nu(v,\gamma_0)-\beta_\nu(.01,.14)|
 \le 10^{-6}
 (\|\partial_vP\|_1+\|\partial_{\gamma_0}P\|_1)
 <0.013<0.02.
\]
Thus every initially positive coefficient remains **strictly positive**, and every originally zero coefficient is **identically zero**. Consequently **all five Stage24 government and corporate sign certificates hold over all seven continuously varied parameters**. Because the expressions are affine in phi and checked at phi=.13,.30, the full interior phi interval follows.

This is an explicit seven-dimensional certificate, not an existence-by-continuity claim or numerical grid. The new v/gamma intervals are extremely conservative sufficient neighborhoods: their smallness reflects a cheap rigorous derivative-norm proof, not an economic transition at the endpoints.

### 4. Policy, conformity, existence, and active Cournot continuation

Independently of the sign certificates, strict policy and conformity bounds are checked for the much **wider** v∈[.0099,.0101], gamma0∈[.1399,.1401], covering the new intervals.

Let \(G_N=[\frac92 m+3\gamma_0]/[4(m+\gamma_0)^2]\), \(G_I=[\frac92 m+3(\gamma_0-v)](1+\rho)^2/[4(m+\gamma_0-v)^2]\). Lower-bound G_I by minimizing numerator and maximizing denominator independently, and upper-bound G_N by the reverse corner choices. With rho_min=.319, Kmax=.56 and phi_max=.30, every initially N government's minimum public policy gain is at least
\[
\frac{4879717257586623}{356007624297600800}>0.
\]
After a singleton-O initial history the sole developer government's policy gain exceeds the previous N government's by \(K+\phi c_i^2/2\); hence 0/1-O histories strictly enact M.

For ANY initial history, a mandatory public O(1,0) adopter's minimum operating gross across zero, one or two complying competitors is at least the isolated gross \(3/(4m_{\max})\). As originally N firms spend at most Kmax+phi_max/2, the strict compliance gain is uniformly bounded below by
\[
\frac{47029}{990100}>0.
\]
A previous O firm instead pays only missing incremental c capital and has an even larger gain. Cournot post-M active output and uniqueness follow from strict diagonal dominance and strictly positive best response lower bound on every private pairwise demand matrix throughout the box.

Finally, NNN→M is an SPE: any firm's unilateral initial switch to O(c,a) still causes unanimous M; its gross Cournot outcome is identical but its sunk total spending relative to N rises by \(\phi a^2/2\ge0\). The government finite voting/proposal games admit pure subgame continuations and compliance is strictly dominant.

Combining these policy and conformity inequalities with the now-seven-dimensional 2-O and 3-O no-L-SPE certificates proves ST25.1.

## Limits, interpretation, and Stage26

This seven-dimensional product box **does not** classify the genuine necessary/sufficient economic phase diagram. It is a strong stability-of-theorem result around baseline physical economics, and establishes that no claimed coefficient is held fixed among the seven parameters (though the functional form, demand normalization, public-standard identity, institutional voting rules and investment technology are maintained). The ±0.000001 intervals for v/gamma0 should NEVER be presented as a meaningful regulatory threshold or an economically large shock.

Next Stage26 should prioritize the **economic mechanism and threshold conditions**, not chase numerical robustness dimension. Independently derive the precise conditions under which the two voting institutions (unanimity versus universal-proposal majority) retain/lose a bilateral private OPEN RS initial equilibrium and compare them with world welfare ordering. The deepest priority audit is theorem-level correspondence to Gandal–Shy (2001), Klimenko (2009), and Farrell–Simcoe (2012). Testing models with privately patent-encumbered standards, alternate public reference, or licensing requires explicit NEW games.

## Reproduction

Source: code/stage25_seven_parameter_norm_robustness.py; full Stage24 proof is re-run with baseline coefficient instrumentation before derivative-norm certification. CI workflow .github/workflows/stage25-seven-parameter-norm-certificates.yml also runs Stage19, Stage21, Stage23 and Stage24 audits. No original PR is merged or manuscript changed.
