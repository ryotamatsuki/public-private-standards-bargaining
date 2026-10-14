# Stage 30B — Results from the unchanged model

## Scope and evidence status

The model, prescribed government selector, and baseline rectangle are exactly
those of Stage29, equation `eq:baseline-box`:
`(v,gamma,kappa,rho,phi)=(.01,.14,.02,.32,.14)`,
`eta in [.10,.14]`, `K in [.54,.56]`. There are no new primitives.

These are **new construction results**, supported by rational certificates and
finite-deviation attacks. This development by the Stage30 auditor is not another
blind independent Stage4A review. No new Stage4A/6 PASS, formal-verification PASS,
seven-parameter extension, mixed-SPE classification, or submission GO is asserted.

Dependency baseline: Stage30 commit
`d1d267cd8eaa349a06df7ff4cd102343d22f7ff5`. Its independently checked Cournot
interiority, compliance dominance, sparse-history mandate, `F_c>0`, and the
low-commonality member-approval certificate are used explicitly below.

## 1. Definitions derived from demand

For a common bilateral profile `O(c,a),O(c,a),N`, set

\[
 b=\gamma_0+\kappa a-vc,\quad d=\gamma_0-\eta a,\quad
 z=1+\rho c,\quad D=2m(2m+b)-2d^2,
\]
\[
 x=\frac{2mz-d}{D},\qquad y=\frac{2m+b-2dz}{D},\qquad
 C=(m+b)x^2+2dxy+\frac m2y^2.
\]

Here `x` is each founder's quantity, `y` the outsider's quantity, and `C` one
national market's consumer surplus. The exact code reconstructs these from the
full symmetric 3-by-3 Cournot matrix, not a fitted numerical function.

Define

\[
 F(c,a;\eta)=3mx^2-\frac\phi2(c^2+a^2),\quad
 P=\pi_I^g-\frac\phi2,
\]
\[
 B(c,a;\eta)=\pi_I^g+CS_I-3mx^2-C-\frac\phi2(1-c^2),\quad
 V(c,a;\eta)=W_I-3my^2-C.
\]

Private founder payoff is `F-K`; their governments' policy gains are `B,B`.
The outsider's policy gain is `V-K`. `P-K` is a firm's payoff after an initial
`N` choice followed by the mandate. Notice that `F`, `P`, and `B` do not depend
on `K`, whereas the noninvestor government's policy gain does.

New exact certificates establish `F_aa<0` on the rectangular superset
`0<=c,a<=1`, `F_a(c,0)>0`, and `F_a(c,.61)<0`, uniformly in eta. Along with
Stage30's `F_c>0`, these statements suffice for global unilateral comparisons.

## 2. Uniform outsider bounds

The new certificates show `y_a>0` and `y_c<=0`. The latter is weak because
`d=0` at `eta=.14,a=1`. Consequently every two-developer history, including an
asymmetric pair reduced to its effective minima, has

\[
 y\ge\frac{8702}{20693},\qquad
 \pi_O^g\ge\frac{5622566697}{10705006225}=0.525227783975\ldots.
\]

Against a common incumbent pair `O(c,a)`, a new open entrant has intercept at
most `1+rho*c`, while both incumbents keep intercept `1+rho*c`. All quantities
are at most `q_U=(1+rho)/(2m)=2/3`; all three-developer cross-effects lie between
`.13` and `.16`. Each incumbent quantity is therefore at least

\[
 L(c)=\frac{1+\rho c-2(.16)q_U}{2m}.
\]

The entrant's quantity is at most

\[
 E(c)=\frac{1+\rho c-2(.13)L(c)}{2m}\le E(1)=\frac{17444}{29403}.
\]

`E'(c)=1376/9801>0`. Thus its private net return, even ignoring all variable
investment expenditure, is at most

\[
 3mE(1)^2-.54=\frac{73552349}{145544850}=0.505358650615\ldots,
\]

strictly below the outsider's status-quo profit. A mandate after entry pays at
most `P-.54=0.421355229592...`, also strictly below that profit. These bounds
cover **all legal entry designs and both policy continuations**, not just an
entry grid or a locally optimized candidate.

## 3. Proposition: complete characterization of private pure SPE

Up to relabeling, every pure SPE with `L` has exactly two developers with a
common design `O(c,a),O(c,a),N`. Such a profile is a private SPE **if and only if**

\[
 \boxed{0\le a\le c\le1,\quad F_a(c,a;\eta)\ge0,\quad
 F(c,a;\eta)\ge P,\quad K>V(c,a;\eta)}                    \tag{B1}
\]

and its constitution is either

* unanimity (`r=3`), with any nonempty agenda set; or
* `r=1` or `r=2`, with the outsider as the **sole** agenda holder.

The strict political inequality in (B1) is required by YES-on-tie. The private
participation inequality is weak: a founder may be indifferent to withdrawing
to `N` and thereby triggering public adoption. `F_a>=0` is automatically
satisfied at `a=0`, by the certified positive boundary derivative.

### Necessity: unequal and three-developer profiles

With two developers, a higher `a_i` is redundant above the other firm's stock.
Reducing it preserves every market outcome and policy gain and saves expense.
After equalizing `a`, a higher `c_i` can legally be reduced to the partner's
stock. This leaves markets unchanged and reduces only its own mandate gain.
The monotone government selector cannot change `L` to `M`. Thus an asymmetric
pair cannot be a private SPE.

With three developers, the same reasoning first rules out a unique maximum
`a_i`, and then a unique maximum `c_i`. The second reduction is feasible:
a tied maximum in `a` is held by another firm whose `c` is at most the
second-highest `c`. Relabel so `c_1<=c_2=c_3`. The remaining patterns are

* aligned: `a_1<=a_2=a_3`; or
* crossed: `a_1=a_2>=a_3`.

For these two classes the new matrix certificates prove

\[
 \sum_i\left[3mq_i^2-\frac\phi2(c_i^2+a_i^2)\right]\le3P,
                                                               \tag{B2}
\]

with equality **only** when all `c_i=1` and all `a_i=0`.
In the aligned parametrization `c_1=tu,c_2=c_3=t,a_1=c_1w,
a_2=a_3=a_1+(c_2-a_1)h`, all 5,103 Bernstein coefficients are nonnegative;
the only zero face is `t=u=1,w=h=0`. In the crossed parametrization
`a_1=a_2=c_1w,a_3=a_1h`, the only zero face is `t=u=1,w=0`.
All 81 faces, including corners, are checked exactly. A nonnegative Bernstein
polynomial can vanish in the relative interior of a face only if its restriction
to that face is identically zero; thus this is also a boundary equality proof.

At any other surviving profile at least one firm's pre-K payoff is strictly
below `P`. Its deviation to `N` pays `P-K` if the mandate follows and at least
`.525227...` if `L` follows. Both exceed its current payoff, since
`P-K<=.421355...`. At the equality profile all governments weakly approve
the mandate, so `L` is impossible under the specified selector. Hence three
developers cannot support a private SPE **even under unanimity**. Sparse
histories already always induce `M` by Stage30.

### Necessity: the design inequalities

At a common bilateral `L` history, a small decrease of positive `a` preserves
`L`. To see this despite vote ties: if `B<0`, the founders strictly oppose and
keep opposing locally; with quorum 1 any eligible outsider must strictly
oppose as well, or the original policy would already be `M`. If `B>=0`, both
founders vote YES, and nonintervention is possible only through the outsider's
strict opposition and unanimity or its exclusive agenda right. That strict
opposition persists locally. Thus `F_a<0` would yield a profitable decrease.

Strict concavity and `F_a(c,.61)<0` imply `a<.61` in any private SPE. Stage30's
low-commonality certificate then gives `B>0`. Enactment is blocked precisely
by the constitutional conditions above and `V-K<0`. A founder's switch to `N`
leaves a singleton and induces the mandate, so `F>=P` is necessary.

### Sufficiency: all finite deviations

For a founder's arbitrary new `O(c_i',a_i')`, let effective pair stocks be
`c'=min(c_i',c)`, `a'=min(a_i',a)`. Under `L`, its payoff is at most

\[
 F(c',a')-K\le F(c,a')-K\le F(c,a)-K.
\]

The first inequality uses `F_c>0`; the second uses strict concavity and
`F_a(c,a)>=0` for **every** lower `a'`. Stocks above the partner's levels only
increase costs. Under `M`, any new open design pays at most `P-K`, bounded
by current profits using (B1). The `N` deviation also pays `P-K`. Entry is
ruled out by Section 2. This covers discontinuous policy switches without
assuming that a founder's deviation retains `L`.

At every off-path history use the unchanged prescribed policy selector,
strictly optimal compliance, and unique Cournot equilibrium certified in
Stage30. These continuations complete the SPE.

### Consequence: a continuum, including inefficient coordination

Every `c=1`, `0<=a<=a_R^*(eta)` satisfies (B1) throughout the baseline K box.
Here `a_R^*` maximizes `F(1,a)`, and is in `(.30,.61)` by exact signs and
strict concavity. Participation follows from `F(1,0)>P`; outsider opposition
is certified on the entire `c=1,a<=.61` rectangle.

There are also supported `c<1` designs. For example `(c,a)=(.95,0)` and
`(.929,0)` at `K=.55` meet all strict conditions apart from the intentionally
zero commonality stock. Any common design can be improved jointly toward
`(1,a_R^*)` in founder profits, but raising a stock unilaterally does not
raise the pair minimum. The optimum used by the manuscript is therefore a
distinguished upper design, **not the whole private equilibrium set**.

## 4. Proposition: public SPE have invariant welfare

In **every** pure SPE whose policy is `M`, each initial developer has `a_i=0`.
Every firm then pays total expense `K+phi/2`, whether it initially chose `N`
or `O(c_i,0)`. Consequently all public SPE have

\[
 u_i=P-K,\qquad \mathcal W_i=W_I-K,\qquad
 W^{\mathrm{ante}}=3(W_I-K).                              \tag{B3}
\]

**Proof.** With one or two developers, a developer with `a_i>0` can switch
to `N`, reach a sparse history and obtain `P-K`, strictly saving
`phi*a_i^2/2`. With three developers the same deviation either induces `M`
and yields that saving, or leaves `L` and pays at least the uniform outsider
profit in Section 2, which exceeds even the maximum public return.

For `r<=2,|A|>=2`, the initial SPE set is in fact exactly **all profiles
with entries `N` or `O(c_i,0)`**. Necessity follows from the Stage27 terminal
classification and the argument above. Sufficiency uses the low-a two-founder
and the tied-maxima three-developer approval certificates; c reductions make
mandate gains only smaller, so arbitrary zero-a profiles still have two YES
governments. A unilateral positive-a choice has no commonality effect because
the other stocks are zero, leaves the policy at `M`, and only wastes expense.

Under narrow agenda or unanimity the public initial-investment vectors are
not exhaustively enumerated here. Their payoffs and welfare nevertheless are
completely determined by (B3). Do not equate this with unique initial actions.

## 5. Proposition: a higher fixed cost expands the private SPE set

For fixed eta and an eligible private constitution, define `R(eta,K)` by (B1).
For `.54<=K_1<K_2<=.56`,

\[
 R(\eta,K_1)\subseteq R(\eta,K_2).                         \tag{B4}
\]

**Proof.** All design and founder-participation inequalities are independent
of K; uniform entry deterrence holds for the entire K interval. Only the
political constraint `K>V(c,a)` changes, and it becomes weaker when K rises.
This is a set comparison, not a prediction of the selected investment level.

Strict inclusion occurs within the original box. At `c=.929,a=0,eta=.14`,
`F-P=.000280815881...>0` and `F_a=.059572498937...>0`, while
`V=.540133318603...`. At `K=.54` the outsider votes YES and the mandate
passes. At `K=.55` it votes NO and the same design is a private SPE under
exclusive outsider agenda or unanimity.

Economically, the founders pay K under either their private path or the public
fallback induced by withdrawal. The noninvestor would newly pay K under public
adoption. A higher setup cost can therefore enlarge politically protected
private coordination outcomes while reducing their absolute returns.

## 6. Proposition: sharp welfare comparison without an equilibrium selector

Let `T(c,a;eta)=2F+3my^2+3C`. Private world welfare is `T-2K`.
The new certificates prove `T_c>0,T_a>0` on `c in [0,1],a in [0,.61]`.
Furthermore `a<=a_R^*(eta)` for every private SPE. This last assertion uses
`a_R^*>.30` and `F_ac>0` on `a in [.30,.61]`: at the c=1 root,
`F_a(c,a_R^*)<=F_a(1,a_R^*)=0`. Strict concavity gives the bound. It does
**not** require the false blanket claim `F_ac>0` on all a.

It follows that the manuscript's canonical design is the **world-welfare
maximum over all private pure SPE**, attained only at `c=1,a=a_R^*`:

\[
 \max_{(c,a)\in R(\eta,K)}W_R=T(1,a_R^*)-2K.               \tag{B5}
\]

Define the existing `K_W(eta)=3W_I-T(1,a_R^*)`. Suppose constitutional change
makes `r<=2,|A|>=2`, from a constitution admitting private SPE. Then

\[
 \boxed{\text{new world welfare is at least that of every old pure SPE}
 \quad\Longleftrightarrow\quad K\le K_W(\eta).}             \tag{B6}
\]

This is an ex-ante comparison of equilibria of different constitutions,
not the welfare of imposing a retrofit at an installed history.

If `K<=K_W`, (B3) and (B5) prove weak improvement from every old SPE.
Old public SPE give equality. If `K>K_W`, the best private SPE beats the
public outcome. But the supported design `c=1,a=0` always has

\[
 W_R-W_I^{\mathrm{ante}}=K-.656147364006722\ldots<0
\]

throughout the box. Thus above the cutoff the reform removes both
welfare-superior and welfare-inferior private equilibria. It strictly improves
the **infimum** of equilibrium world welfare, but strictly lowers its maximum.
Below the cutoff it improves the infimum without lowering the maximum, since
the public equilibrium already coexists under the old constitution.
No probability, average welfare, actual equilibrium selection, national
Pareto improvement, or unrestricted planner optimum is inferred.

### Exact same-parameter witnesses

With `eta=.14,K=.55,A={outsider},r=2`, all three rows are actual private SPE;
the broad-agenda public SPE always has world welfare `3(W_I-.55)`.

| Common design | Private minus public world welfare |
|---|---:|
| `c=.95,a=0` | `-.176148554383...` |
| `c=1,a=0` | `-.106147364007...` |
| `c=1,a=.5` | `+.048787911265...` |

Every sign and each equilibrium inequality is evaluated as an exact rational
number in `STAGE30B_EXACT_RESULTS.json`. This is stronger than selecting the
optimized design at three different parameters.

## 7. Failed candidates and remaining gates

* **False:** `F_ac>0` everywhere. At `c=1,a=0,eta=.10` it equals
  `-13843846307339136/4583886331091550025`. The restricted sufficient statement
  used for (B5) is certified separately.
* **False:** use `a_R^*(1,eta)` unchanged at every `c<1`. At `c=.95,eta=.14`
  a founder's finite reduction of a is profitable; recorded in the numerical
  evidence. The characterization uses `F_a(c,a)>=0` at the actual c.
* **False at a boundary:** strict `y_c<0` everywhere; `y_c=0` at `d=0`.
  The outsider lower bound needs only weak monotonicity.
* Not claimed: a closed-form minimum-welfare design, selected-investment
  monotonicity, public initial-vector enumeration under unanimity/narrow
  agenda, mixed SPE, or portability of these new results outside the box.

Construction evidence: 26 exact signs with 12,708 rational Bernstein
coefficients, exact boundary face tests and rational witnesses; 72 private
profiles attacked numerically under several constitutions, 24 broad-agenda
public profiles, and 1,000 direct-matrix identity checks. The numerical grid
illustrates welfare dispersion and does not prove the equilibrium classification
or compute certified extrema. Every applicable optimizer converged. The
propositions still require a new adversarial Stage4A review and novelty gate.
