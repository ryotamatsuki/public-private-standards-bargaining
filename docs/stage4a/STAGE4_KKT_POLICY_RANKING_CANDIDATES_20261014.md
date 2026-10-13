# Stage 4: KKT outsider exit changes standard-depth incentives and national policy ranking
Date: 2026-10-14 JST. Child of Draft PR #22. Stage 3 mathematics preserved, original **one endogenous s / exogenous network v**. This is a constructive Stage 4 theorem search, **NOT an independent Stage 4A clean-room audit or Stage 6 novelty GO**. No manuscript, no merge.

## Model and correct continuation
Normalize A=a-c0=1 and let theta=(v,gamma0,kappa,eta,rho,phi). Define
m=1-v, b(s)=gamma0+(kappa-v)s, d(s)=gamma0-eta*s,
z(s)=1+rho*s, a(s)=2m+b(s), Delta(s)=2m*a(s)-2d(s)^2.
RS outsider's KKT switching function, **with the corrected constant**, is
Y(s) = **2(1-v)-gamma0** + (kappa-v-2gamma0*rho+2eta)s + 2eta*rho*s^2.
For Y>0, the unique Cournot amounts are
y=Y/Delta, x=(2mz-d)/Delta;
for Y<=0, they are y=0, x0=z/a. The identity
x_active = x0 - (d/a)*y_active
holds everywhere algebraically. Under the source SPD/substitutes domain with b>=0, 0<d<m, m>b, Delta>0, the branch allocations coincide at Y=0.

For every participating firm, P_R=3m*x^2 - phi*s^2.
Government W_R=P_R+CS_R, where CS_R=(m+b)x^2+2dxy+(m/2)y^2.
For IS, qI=z/[2(m+b)], P_I=3m*qI^2-phi*s^2,
W_I=P_I+(3/2)(m+2b)qI^2.
NS uses qN=1/[2(m+gamma0)] and the previously certified P_N,W_N.

## Theorem 4.1: downward KKT kinks
At any simple Y-root r in (0,1), with d(r)>0, compare the derivative of the algebraic active extension with the zero-outsider extension. Direct differentiation at y=0 gives

P_active'(r)-P_corner'(r) = - [6m*x0(r)*d(r)/a(r)] * [Y'(r)/Delta(r)];
W_active'(r)-W_corner'(r) = - [4m*x0(r)*d(r)/a(r)] * [Y'(r)/Delta(r)].

Thus at the lower root r=s_- (Y'<0), the ACTUAL left derivative is strictly ABOVE the actual right derivative. At the upper root s_+ (Y'>0), the ACTUAL right derivative is strictly BELOW the left derivative. Both transitions create a **downward** derivative jump for private profits and national government welfare. This is a generic *within-class* piecewise-Cournot result, not a claim of theoretical novelty.

Define P_active^0,P_corner^0,W_corner^0 without phi*s^2. A sufficient interval for a firm strict local optimum PINNED at lower exit, simultaneously with government strictly wanting more depth on both sides, is

max(0, P_corner^0'(s_-)/(2s_-))
     < phi
     < min(P_active^0'(s_-)/(2s_-), W_corner^0'(s_-)/(2s_-)).

This interval is nonempty whenever its left bound is below its right bound. This is an **analytic open inequality** in the underlying theta, provided the two roots remain simple and source-domain inequalities strict. A local kink alone does NOT prove global bargaining stability.

## Theorem 4.2: exit boundary itself is a reduced-stage1 strong-stable RS contract
Keep the exact Stage3 product-market parameters (v,gamma0,kappa,eta,rho)
=(3/10,3/5,1/10,11/20,10), but change only phi from 120 to **140**.
Y=(110s^2-111s+8)/10, with lower and upper roots
s_-=(111-sqrt(8801))/220 = 0.0781197951683... and
s_+=(111+sqrt(8801))/220 = 0.9309711139226....
All 3 demand matrices are SPD on the whole interval, products are substitutes.
Implementation a=13,c0=12,h=10,f=140 is physically nonnegative-cost.

At s=s_-, true P_R = 0.8376035891744...; true W_R=1.8724326586642...;
P_N=105/338=0.3106508875...; W_N=495/676=0.7322485207....
At lower exit:
P'_left=+2.0672707522..., P'_right=-2.5342349849...;
W'_left=+12.199..., W'_right=+9.1326921701....

**Global proof, not sampled-grid optimization.**
- Sturm root-count and rational endpoint signs prove P_R'(s)>0 on [0,2/25] when calculated from the ACTIVE continuation; all physically active depths below s_- are contained here.
- They prove P_R'(s)<0 on [7/100,94/100] on the CORNER extension; all outsider-zero depths are contained here.
- They prove P_R'(s)<0 on [93/100,1] on the ACTIVE continuation; all physically active depths above s_+ are contained here.
- Therefore s_- is the **unique global maximizer** of true RS participating firm profit over [0,1].
- A further exact closed-interval Sturm certificate proves P_I(t)<4/5 for EVERY t in [0,1], while P_R(s_-)>4/5, so either participating firm vetoes any IS alternative.
- P_R(s_-)>P_N and W_R(s_-)>W_N. No first-stage coalition can induce RS(s') with strict gains for all required signers because at least one incumbent firm cannot beat its global maximum. No IS alternative can obtain its incumbent firm's strict gain. Thus RS(12,s_-) is a realizable pure SPNE with reduced FIRST-STAGE strong Nash, even under arbitrary outsider IS preannouncements. This does **not** assert strong Nash of the stage-2 Cournot game or full extensive-form strong equilibrium.

At the feasible depth t=1/10, true P_R(t)<P_R(s_-) while W_R(t)>W_R(s_-). In contrast, algebraically extrapolating the **invalid negative-outsider** interior branch gives P_R^interior(t)>P_R(s_-). A smooth-all-interior analysis therefore reverses the local private depth ranking and entirely misses the binding first-stage firm veto. This is NOT a causal experiment that changes only the constraint while preserving the same downstream feasible set: the interior extension is not a valid economic equilibrium.

## Theorem 4.3: policy choice RS vs IS reverses when the outsider KKT constraint binds
At ANY same depth s with outsider zero, write z=1+rho*s and retain m,b.
After cancellation of the common fee phi*s^2, the TRUE national host-government RS-minus-IS welfare differential is

W_R^corner-W_I
 = z^2 * [2b^3+15m*b^2+12m^2*b-4m^3]
   / [8(m+b)^2(2m+b)^2].

For substitutes 0<=b<m, define t=b/m. The cubic
H(t)=2t^3+15t^2+12t-4
is strictly increasing for t>=0, H(0)<0, H(1)>0; it has one positive threshold
t_star approximately **0.251570279593411**.
Therefore, conditional on outsider zero output,
host government STRICTLY prefers IS over RS at the SAME s iff b(s)/m<t_star,
is indifferent iff equality, and strictly prefers RS if b(s)/m>t_star.
Importantly, this policy cutoff does **not depend on eta,d,rho,phi directly**
once b/m and active set are held fixed, though eta and rho govern WHETHER the corner is reached.

The invalid all-interior extrapolation changes host-government welfare by
W_R^interior-W_R^corner
 = -[4m*x0*d/a]*y + [m/2-b*d^2/a^2]*y^2 >0
whenever Y<0,d>0, 0<=b<m and the SPD domain holds (algebraic y=Y/Delta<0).
In this region an interior extrapolation **systematically overstates** both
incumbent profit and its government's welfare, and can misrank RS vs IS.

**Exact rational policy-rank reversal witness, no grid or generic continuity inference:**
theta=(v,gamma0,kappa,eta,rho,phi)
     =(2/5,1/5,59/200,19/100,15,200), at s=1/2.
The exact outsider-switch function is
Y(s)=(228s^2-229s+40)/40, giving 2 simple roots strictly inside (0,1),
with 1/2 between them; Y(1/2)=-7/16 and b(1/2)/m=59/240<t_star.
Global SPD checks at endpoints:
m-gamma0=2/5, m+2gamma0=1,
m-b(1)=101/200, m+2b(1)=79/100,
m[m+b(1)]-2d(1)^2=521/1250, all strictly positive.
b(s),d(s) are positive on [0,1], so all goods remain substitutes.
Choose a=17,c0=16,h=15,f=200 to keep marginal cost nonnegative.

At s=1/2 (all figures normalized):
P_RS(KKT)=6281950/290521 = 21.6230496...;
P_IS=731950/89401 = 8.1872686...;
W_RS(KKT)=14923050/290521 = **51.3665105...**;
W_IS=4611775/89401 = **51.5852731...**;
W_RS(invalid interior)=17539987975/339182067 = **51.7126042...**.
So the exact, strict ordering is
     W_RS(KKT) < W_IS < W_RS(invalid interior).
Both firms and governments accept the RS and IS same-depth contracts relative to NS; RS firms prefer RS, governments prefer IS. The invalid interior formula would instead conclude the government prefers RS, **reversing the sign of the national standard-type policy recommendation at the SAME standardization rate**.

This last result is a **same-depth policy preference reversal**, not yet a proof that the FULL continuum-depth game's RS/IS strong-equilibrium outcome SET changes. In the exact-announcement Stage1 protocol, both IR-matched standards can appear as pure SPNE and SQ always remains a pure SPNE. To claim an across-type strong-Nash selection reversal, the entire continuous set of deviations in both RS and IS must be certified under both continuation maps; this has NOT been done.

## Independent referee / novelty gate
These 3 mathematical candidates are specific comparative statics and existence statements, not a substantive novelty certificate. The market-exit kink is familiar complementarity/KKT theory. Ghosh–Morita (2012, IJIO 30, 137–152, DOI 10.1016/j.ijindorg.2011.07.003) already studies 2 collaborating firms and outsider product distinctiveness, prices and welfare; its displayed full introduction and abstract have been checked but a proposition-by-proposition full-text audit of KKT corners has NOT been completed.
Bourreau–Dogan–Manant (2016, IJIO 46, 77–106, DOI 10.1016/j.ijindorg.2016.01.001) already examines endogenous cooperation scope and coalition size; published institutional abstract verified, specific corner-case theorem coverage NOT verified. The model uses *exogenous* network v; the phenomenon already arises at v=0. Claims that these results uniquely depend on network externalities or that they are wholly absent from earlier work are NOT justified.

Next research gate: prove or disprove that the actual reduced first-stage strong-equilibrium *TYPE SET* differs from the all-interior extrapolation over continuous s, for an open 6D parameter set; then independent clean-room Stage4A and theorem-level Stage6 absorption. Remain **NO-GO**, Draft PR #22 UNMERGED.

Reproduction: python code/stage4_exit_boundary_policy_reversal.py (SymPy 1.14), and a standalone GitHub Actions workflow.
