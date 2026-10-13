# Stage 4 — Endogenous outsourcing exit, kink-pinned RS depth and public/private veto
2026-10-14 JST. **Original six-exogenous-parameter model only.**
Parent: Draft PR #22, commit fb acd824... (actual SHA `fbacd824dd36d64d85a6de8b322c677c2a313471`).
**Scientific verdict: NEW structural candidate proven, novelty NO-GO unchanged.**
Nothing here is a manuscript/review clearance or whole-game strong Nash claim.

## 1. Correct Cournot support and general boundary proposition
Let `m=1-v>0`, `b(s)=gamma0+(kappa-v)s`, `d(s)=gamma0-eta*s>=0`, `A(s)=2m+b(s)>0`,
`z(s)=1+rho*s`, `D(s)=2m A(s)-2d(s)^2>0`.
All demand matrices are SPD throughout `s in [0,1]`, and the goods are substitutes. Correct *original* outsider support polynomial:
`Y(s)=A(s)-2d(s)z(s)=2(1-v)-gamma0+(kappa-v-2gamma0*rho+2eta)s+2eta*rho*s^2`.
This retains the **negative** gamma0 in the constant term (the Stage 3 corrected value).
Two simple interior roots `0<s_-<s_+<1` imply outsider positive for `s<s_-` and `s>s_+`, and zero in between.
The Cournot member quantity is `x_A=(2mz-d)/D` and outsider `y_A=Y/D` on positive branch.
On zero-outsider branch `x_C=z/A, y_C=0`.
At every root `x_A=x_C`, and exactly
`x_A=x_C-(d/A)y_A`.

Define per-member worldwide private `P_X(s)=3m x_X(s)^2-phi*s^2`;
per-participating-state `W_X=P_X+CS_X`, where
`CS_A=(m+b)x_A^2+2d x_A y_A+(m/2)y_A^2` and `CS_C=(m+b)x_C^2`.
At ANY simple outsider support crossing `s_0`, levels agree but
`P_A'(s_0)-P_C'(s_0)= -[6m x_C(s_0)d(s_0)/A(s_0)]Y'(s_0)/D(s_0)`;
`W_A'(s_0)-W_C'(s_0)= -[4m x_C(s_0)d(s_0)/A(s_0)]Y'(s_0)/D(s_0)`.
These identities follow by differentiating `x_A=x_C-(d/A)y_A` and domestic consumer surplus exactly at `y_A=0`.
When `d(s_-) > 0` and `Y'(s_-)<0`, both jumps are strictly **downward** moving from the active to the zero-outsider branch as standardization increases. A smooth interior-only FOC is INVALID there.

## 2. Local endogenous boundary pinning: general analytical fee band
Write `P_A^0,P_C^0,W_C^0` for payoffs before the real quadratic depth fee.
Set
`phi_P^-=(P_C^0)'(s_-)/(2s_-)`,
`phi_P^+=(P_A^0)'(s_-)/(2s_-)`,
`phi_G^+=(W_C^0)'(s_-)/(2s_-)`.
The positivity of the Cournot kink proves `phi_P^- < phi_P^+` (if `d(s_-)>0`).
For
`phi_P^- < phi < min(phi_P^+,phi_G^+)`,
the ACTUAL piecewise profit has `P_R'(s_-^-) > 0 > P_R'(s_-^+)` while
`W_R'(s_-^-)>0, W_R'(s_-^+)>0` (the latter because welfare's left derivative exceeds its right derivative).
Therefore exit is a strict LOCAL maximum of firms' profits despite a strictly positive GOVERNMENT incentive for deeper RS.
This is a parameter **band**, not a fixed-phi isolated derivative coincidence.
Global maximization, strong Nash, and RS/IS selection do NOT follow from these local inequalities alone.

## 3. Globally certified six-parameter witness (phi changed from Stage 3)
Exact primitives
`(v,gamma0,kappa,eta,rho,phi)=(3/10,3/5,1/10,11/20,10,140)`,
with `a=13,c0=12,h=10,f=140` as valid nonnegative physical cost implementation.
This changes ONLY the quadratic real integration fee versus Stage 3 (`phi=120`).
All five uniform SPD inequalities are strict. The corrected `Y=(110s^2-111s+8)/10`, with
`s_-=(111-sqrt(8801))/220=0.07811979516834...`,
`s_+=(111+sqrt(8801))/220=0.93097111392257...`.

At the first root:
`P_R(s_-)=0.837603589174423...`, `W_R(s_-)=1.87243265866417...`;
`P_N=105/338=0.31065088757...`, `W_N=495/676=0.73224852071...`.
Derivatives **at s_-** (LEFT uses outsider-active, RIGHT outsider-zero):
`P'_- = +2.06727075220...`, `P'_+ = -2.53423498487...`;
`W'_- = +12.20036266143...`, `W'_+ = +9.13269217005...`.
The local fee thresholds (for fixed remaining five market primitives):
`phi_P^-=123.7798154782...`; `phi_P^+=153.2314143153...`; `phi_G^+=198.4531241433...`.
Thus 140 is strictly within the pinning/conflict band.

**Exact global—not a sampled grid—certificates** in `code/stage4_exit_boundary_pinning.py`:
- `P_A'(s)>0` on the rational envelope `[0,2/25]`, covering `[0,s_-]`.
- `P_C'(s)<0` on `[7/100,94/100]`, covering `[s_-,s_+]`.
- `P_A'(s)<0` on `[93/100,1]`, covering `[s_+,1]`.
- Strict `P_I(t)<4/5<P_R(s_-)` for EVERY continuous `t in [0,1]`, with exact Sturm sign checks.
- NS IR strictly holds for both participant firms and participant governments; any other RS depth is no strictly profitable coordinated deviation because `P_R(s_-)` is the globally unique private maximum. Any IS depth is vetoed by an incumbent firm, even if the outsider had preannounced it.

So the contract `RS(12,s_-)` is a **pure SPNE and reduced-stage-1 strong Nash** of the actual exact-contract six-agent matching game, with genuine stage-2 KKT Cournot continuation. DO NOT call it strong Nash of the stage-2 Cournot game or coalition-proof equilibrium.

**Public/private policy wedge:** `W_R(1/10)=2.04862769105...>W_R(s_-)`, but
`P_R(1/10)=0.74263850627...<P_R(s_-)`.
Correct `Y(1/10)<0`, so using the INVALID interior Cournot extension there would instead give
`P_A(1/10)=0.85121294094...>P_R(s_-)`: it REVERSES the direction of the private comparison.
The government's unique **unconstrained** globally best RS depth is
`s_G in (0.1737,0.1738)` (approximately `0.1737083`),
inside the zero-outsider KKT segment. However `P_R(s_G)<P_N`; compulsory implementation at that government optimum would be vetoed by participant firms in the actual consent game.
The government optimum is *not* the equilibrium depth; the equilibrium is pinned at `s_-`.

## 4. Scope and predecessor theorem absorption
1. This establishes a **selection-of-depth effect**: the first outsider exit boundary itself, rather than a smooth stationary FOC, can be the strong-stable negotiated RS rate. It also establishes opposite preferences about deepening RS across that boundary.
2. It does **NOT** establish a reversal between RS and IS as contract TYPES under policy, nor a unique pure SPNE: all-SQ remains pure SPNE under exact unanimity. Nor is a new generic market exit phenomenon proven.
3. Ghosh & Morita (2012), *Competitor Collaboration and Product Distinctiveness*, IJIO 30:137-152, doi:10.1016/j.ijindorg.2011.07.003. Publisher abstract/introduction disclose two collaborators, outsider product-distinctiveness effects, and price/welfare changes; verified publisher page https://www.sciencedirect.com/science/article/pii/S0167718711000671 . FULL mathematical theorem inclusion of a boundary-pinned public/private RS depth **not verified**.
4. Bourreau, Dogan & Manant (2016), *Size of RJVs with partial cooperation in product development*, IJIO 46:77-106, https://ideas.repec.org/a/eee/indorg/v46y2016icp77-106.html . Explicit endogenous firm-collaboration scope and size with nonmonotonicity; public/private bilateral signature veto not established from abstract. FULL theorem absorption remains to do.
5. Standard complementarity/KKT corner optimization, Cournot exclusion, and ordinary public/private Pareto veto may together **already subsume** the local derivative/candidate theorem. The novel-research hurdle is to isolate a qualitative contract-type or welfare comparison **not** derivable from a generic KKT + unanimity template.

## 5. Control gate
**Stage4 algebraic boundary candidate: PASS conditional on workflow CI/independent adversarial reimplementation.**
**Stage4A clean-room: NOT YET PASS. Stage6 NOVELTY: NO-GO.**
Do not merge source Draft PR #22, do not alter production manuscript, and do not claim a publication-ready theoretical result. Next: independent clean-room audit of global sign certificates/contract-off-path deviations, then theorem-level predecessor comparison; only then test whether a policy intervention can causally move the RS-vs-IS selection boundary.
