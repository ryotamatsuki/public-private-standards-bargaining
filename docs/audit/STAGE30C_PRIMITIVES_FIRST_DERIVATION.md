# Stage30C — Alternative derivation fixed before construction-code comparison

Date: 2026-10-15 JST. Domain and exposure: see
[the audit contract](STAGE30C_INDEPENDENT_AUDIT_CONTRACT.md).
This document fixes the independent argument before rereading the Stage30B
construction source. It is an AI-side mathematical derivation, not a blind or
external-human certificate. Final reconciliation and numeric attacks are separate.

## 1. Primitive matrix bounds and boundary states

Let `A=H+mI`, `m=99/100`, and use the conservative off-diagonal bound
`0<=H_ij<=h=4/25`, with `1<=z_i<=1+rho=33/25` in every full private market.
The bound also holds on the auxiliary rectangular extensions used below.
`H` is symmetric and strictly diagonally dominant, so positive definite;
the same is true of `A`. The constrained Cournot game has a unique solution.

Write `A=2m(I+E)`. Then `||E||_infinity<=r=h/m=16/99<1`.
The Neumann bound first proves positivity of `A^{-1}z`:

\[
 q_i\ge {1-r(1+\rho)/(1-r)\over2m}>0.
\]

Thus no zero-quantity active set is the solution. Positive cross-effects in the
FOCs sharpen the bounds to

\[
 q_i\le\bar q={1+\rho\over2m}={2\over3},\qquad
 q_i\ge\underline q={1-2h\bar q\over2m}={118\over297}.
\]

For `w=A^{-1}q`, a second Neumann bound gives

\[
 w_i\ge\underline w
 ={\underline q-r\bar q/(1-r)\over2m}
 ={331300\over2440449}>0.
\]

For mandated markets enumerate all compliance/exit active sets. A lone adopter
has intercept1 and gross profit `3/(4m)`, not the full-public intercept. Two and
three adopters use the compatible public intercept `1+rho`. The smallest gross
return is `25/33`; the largest incremental cost is `K_max+phi/2=.63`.
Their strictly positive difference makes compliance strictly dominant after
every initial history, including histories with an initial N. Sunk expenditure
is excluded from the comply-versus-exit difference.

## 2. Three developers: a total-profit bound without a case polynomial

Define their aggregate return before fixed development costs by

\[
 S=3m\sum_iq_i^2-{\phi\over2}\sum_i(c_i^2+a_i^2).
\]

For fixed intercepts, changing one symmetric off-diagonal gives

\[
 {\partial(3m\sum q_i^2)\over\partial H_{ij}}
 =-6m(w_iq_j+w_jq_i)<0.
\]

In the three-developer branch every positive pair commonality increases a
cross-effect. Removing all commonality weakly increases gross profit and lowers
real cost, strictly if any `a_i>0`. This is an upper-bound comparison, not a
claim that simultaneous reductions constitute a unilateral deviation.

Order capacities `c_1>=c_2>=c_3`. The highest capacity does not enter a pairwise
minimum or any intercept, so reduce its redundant part to `c_2`. If its own
commonality exceeds `c_2`, it is uniquely highest and also redundant; reducing
it to `c_2` preserves every pair minimum and legality. Gross payoffs are
unchanged and investment cost weakly falls.

It suffices to bound profiles `(C,C,t)` with `0<=t<=C<=1` and zero commonality.
Increasing C changes the first two intercepts at rate rho and decreases H12
at rate v. Increasing t changes the third intercept at rate rho and decreases
H13/H23 at rate v. Therefore

\[
 S_C\ge12m\rho\underline w-2\phi
 ={48497\over205425}>0,
\quad
 S_t\ge6m\rho\underline w-\phi
 ={48497\over410850}>0.
\]

Increase C to1 and t to1. With `P=pi_I^g-phi/2`, obtain

\[
 S\le3P,
\]

with equality only when all three initial designs are `O(1,0)`.
If a private-terminal three-developer profile were an SPE, strict inequality
would give one firm a return before K below P. That firm can withdraw development.
Under M its return is `P-K`. Under L it becomes a nondeveloper outsider and earns
at least the lower bound in §3, which exceeds `P-K` uniformly. Withdrawal is
strictly profitable under either policy continuation, irrespective of agenda
or quorum. At equality all policy gains are exactly zero and YES-on-tie enacts
M, so it is not a private outcome. This excludes every three-developer private
SPE, including unanimity, without transporting a former institution's inequality.

## 3. Two developers, finite entry, and derivative bounds

For shared stocks c,a, solve the primitive two-equation FOC system:

\[
 A_0x+dy=z,\quad2dx+2my=1,
\quad A_0=2m+b,\quad b=\gamma+\kappa a-vc,
\quad d=\gamma-\eta a,\quad z=1+\rho c.
\]

Let `D=2m A_0-2d^2>0`, `C=q'Hq/2`, and

\[
 F=3mx^2-\phi(c^2+a^2)/2,
\quad B=\pi_I^g+CS_I-3mx^2-C-\phi(1-c^2)/2,
\quad V=W_I-3my^2-C.
\]

Capacity differentiation gives

\[
 x_c={2m(\rho+vx)\over D}>0,
\qquad y_c=-{2d(\rho+vx)\over D}\le0.
\]

Commonality differentiation gives

\[
 x_a={\eta-xD_a\over D},\quad
 D_a=2m\kappa+4\eta d,
\quad
 y_a={2[\eta(A_0x-dy)+d\kappa x]\over D}>0.
\]

The last strict inequality follows from `A_0x-dy=z-2dy>0` under the matrix bounds.
Thus outsider profit is minimized at c1,a0 and is
`5622566697/10705006225 = .525227783975...`.
The weak `y_c<=0` includes the `d=0` boundary; a strict global sign is false there.

For a new open entrant in a three-developer continuation, its own intercept is
at most `1+rho c_i`; both cross-effects are at least `gamma-v c_i` and rivals'
quantities at least the common lower bound. Hence its profit net of K is bounded
above by the convex quadratic

\[
 E(c_i)={3\over4m}
 [1-2\gamma\underline q+(\rho+2v\underline q)c_i]^2
 -\phi c_i^2/2-K_{\min}.
\]

Check both endpoints; the maximum is `.511484628277...`, strictly below outsider
profit by `.013743155697...`. Positive own commonality only lowers this upper
bound. If entry induces M, its return is at most `P-K_min`, also strictly lower.
Thus all finite entries are excluded, including policy-changing ones.

The same bounds imply `F_c>=1139/5350>0`. They imply `x_a>0`, since
`eta_min-q_upper D_a,max=8/375>0`. Differentiating again,

\[
 x_{aa}=(4\eta^2x-2D_ax_a)/D,
\qquad
 F_{aa}=6m(x_a^2+xx_{aa})-\phi.
\]

Dropping the negative term gives a strict upper bound
`F_aa<=-1781133151/21410012450=-.083191598...`
on the full auxiliary cube c,a∈[0,1]. Consequently `F_a(c,0)>0` and F is
strictly concave in a. A sharper fixed-a envelope at a=.61 gives
`F_a(c,.61)<=-.001203360586...` uniformly. Its ingredients and exact rational
margins are recorded in the independently generated exact results.

## 4. The policy discontinuity and private equilibrium equivalence

Within a fixed developer pattern all national policy gains are continuous in
physical stocks, including minimum ties. Under YES-on-tie, every NO gain is
strictly negative. At an L history, a sufficiently small perturbation keeps
all former NO governments negative. The new YES set is then a subset of the old
YES set, so the monotone mandate selector still returns L. **The L region is
relatively open.** This establishes necessary derivative conditions despite
the global discontinuity; it is not a global best-response proof by FOCs.

Unequal two-developer stocks cannot be private equilibria: a firm can cut
redundant capacity/commonality to the shared minima without changing demand,
saving cost. Its own mandate gain weakly decreases and others' gains remain
unchanged, so a previously blocked mandate remains blocked. Private pairs are
therefore symmetric `O(c,a),O(c,a),N`.

The L-openness lemma makes `F_a>=0` necessary; otherwise a small feasible
commonality reduction is profitable and stays L. Withdrawal leaves a sparse
history, which strictly induces M, so `F>=P` is necessary. The derivative
bounds force a<.61. The independently certified founder gain B is positive on
this entire enclosing region. Both founder governments support M. An outsider
YES would give all three YES and enact M for any nonempty agenda/quorum.
Thus `K>V` is necessary, with a strict inequality at the voting boundary.

With exactly the founders supporting, L is possible precisely if either r3,
or r<=2 and the sole proposer is the outsider. These conditions are also
sufficient. For any unilateral O deviation with private continuation, effective
shared stocks satisfy `c'<=c,a'<=a`, and own cost is at least the cost used in
`F(c',a')`. Since F_c>0, F_aa<0 and F_a(c,a)>=0,
`F(c',a')<=F(c,a')<=F(c,a)`. Every mandated O deviation yields at most `P-K`,
and withdrawal yields exactly `P-K`. Section3 excludes every outsider entry.
This is a finite-deviation proof over the full legal strategy set, not only
local derivative checking. The weak participation boundary F=P is retained.

Sparse histories' unanimous policy gain is separately positive by exact rational
evaluation. Combining §§2–4 proves the complete private-terminal correspondence.

## 5. Public equilibria and arbitrary zero-commonality capacity profiles

If a public-terminal initial profile has any `a_i>0`, withdrawal to N improves
that firm's return. If M still occurs, wasted commonality cost disappears. If L
occurs, the deviator is an outsider to at most two remaining developers and its
gross return exceeds the old public return; sparse L cannot occur under the
prescribed policy rule. Hence every public SPE has `a_i=0` and world welfare
`3(W_I-K)` regardless of how many firms initially developed.

For the stronger broad-agenda initial correspondence, show that every profile
with zero effective pair commonality induces M when quorum<=2 and at least two
governments can propose. Sparse and bilateral histories were already covered.
In a three-developer profile order capacities. Demand only depends on the
second-highest C and lowest t; the highest country's own mandate gain is at
least the corresponding gain at capacity C.

For either top country write `G=3mx^2+CS`, where CS denotes one market's
consumer surplus (distinct from the second-highest capacity C).
At zero commonality, H13=H23=d=gamma-vt.
With `A_0=2m+gamma-vC`, differentiation in t yields

\[
 G_t={v y(4mx+2dy)\over A_0}
 +\left[m y-{4mdx+2d^2y\over A_0}\right]y_t.
\]

Here `y_t>0`; its FOC right-side lower margin is `2368/7425>0`.
The bracket is bounded below by `2417/14850>0`. Thus the top-country status
quo return increases with t and its mandate gain is minimized at t=C.
At t=C all quantities are symmetric. National return net of variable capacity
cost is strictly increasing in C (exact derivative lower margin `.470551115...`),
so the mandate gain is nonnegative, with equality at C1. Both top countries
therefore support M, including the ties. A broad agenda intersects them.

Starting from any `N`/`O(c_i,0)` profile, an arbitrary unilateral positive-a
investment leaves every pair minimum in a equal to0 because all other firms
have zero commonality. The preceding policy argument applies at the deviating
history as well. All such deviations induce M and return at most `P-K`.
Therefore the **complete initial SPE set under quorum<=2, |agenda|>=2** consists
of arbitrary N or `O(c_i,0)`, all yielding M. This does not claim a unique
initial investment vector. Public initial vectors under narrow agenda/unanimity
are not completely enumerated; their welfare nevertheless is.

## 6. Welfare maximum, cost inclusion, and preference boundaries

Set `T=2F+3my^2+3C`; private world welfare is `T-2K`. From
`Aq=z`, `q'Hq=q'z-m q'q`, obtain
`T=3(q'z+m q'q)/2-phi(c^2+a^2)`.
Let `u=A^{-1}(z+2mq)=q+2mw>0`. Differentiating capacity proves

\[
 T_c=3\rho(u_x+x)+3v u_xx-2\phi c>0
\]

using the scalar bound in the exact results. A separate low-dimensional exact
certificate gives T_a>0 for c∈[0,1], a∈[0,.61], eta∈[.10,.14].

A Sturm sign check gives `F_a(1,.30,eta)>0`; strict concavity and the .61 bound
give a unique canonical a*(eta)∈(.30,.61). The independently checked F_ac>0
on a∈[.30,.61] implies every private-SPE a is at most a*(eta): above .30,
`F_a(1,a)>=F_a(c,a)>=0`; below .30 the comparison is immediate.
Therefore T(c,a) is uniquely maximized over private SPE at c1,a*. That profile
is feasible uniformly: `F(1,a*)>=F(1,0)>P` and the exact V enclosure is below
K_min on c1,a∈[.30,.61].

For an old constitution admitting private SPE and a new broad-agenda
quorum<=2 constitution, every new SPE weakly improves world welfare relative
to every old SPE iff `K<=K_W(eta)=3W_I-T(1,a*)`. If K>K_W, the new welfare is
strictly below the best private equilibrium but above the old infimum, since
the exact c1,a0 witness is worse than public welfare everywhere in the box.
From unanimity this comparison also changes the quorum; expanding agenda while
keeping unanimity is not claimed to eliminate private equilibria.

For a fixed private-admitting constitution, K enters the private correspondence
only as `K>V`; the other conditions and all uniform no-entry bounds remain
valid. Raising K weakly expands this set. Exact c=.929,a0 witnesses give a
strict inclusion between K=.54 and .55.

At every private SPE the same-history founder profit change under M is
`P-F-phi a^2/2<=0`, while its government gain B is strictly positive and the
outsider gain V-K strictly negative. The pre-investment founder-country gap
is `B+phi a^2/2>0`. These are different comparisons. The firm-government
misalignment is not a temporal preference reversal by the same government.
An exactly defined algebraic root F(c,0)=P at K=.55 supplies the weak firm
indifference boundary and is enclosed in the exact results.

## 7. Remaining audit steps and evidence types

The matrix bounds and monotonicity are mathematical implications from primitive
FOCs and costs. The residual polynomial certificates use exact rational
Horner ranges, derivative-certified minimum faces, and a checked cover, with
positive D powers explicitly mapped to the primitive functions. Root signs use
Sturm and rational brackets. Numerical search is an attack/illustration, not
a substitute for these proofs. No seven-parameter or proof-assistant PASS is
implied. Finish independent direct-market/deviation attacks and compare the
construction proof/code before issuing a final Stage4A verdict.
