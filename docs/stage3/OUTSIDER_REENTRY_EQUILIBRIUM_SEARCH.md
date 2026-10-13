# Stage 3: Outsider exit/reentry in one-depth Cournot standards bargaining
Date 2026-10-14 JST. No change to source model: endogenous standard depth s in (0,1], exogenous network strength v. Prior Stage6 NO-GO preserved. This report is a mathematical search result, NOT independent Stage4A or economic novelty GO.

## Proposition A: sharp two-switch domain
For a regional coalition of two firms let m=1-v, g=gamma0, rho=h/(a-c0), b(s)=g+(kappa-v)s, and d(s)=g-eta*s. Under strictly positive definite demand and substitute goods, outsider Cournot production is POSITIVE iff
Y(s)=2m+b(s)-2d(s)*(1+rho*s)>0;
otherwise outsider production is zero, while both RS members produce.
Write Y=C+B*s+H*s*s, with
C=2(1-v)-g >0,
B=kappa-v-2*g*rho+2*eta,
H=2*eta*rho >=0.
Exactly two distinct crossings 0<s_exit<s_reentry<1 (outsider active, then zero, then active) occur IFF
H>0; -2H<B<0; B*B>4*H*C; C+B+H>0.
Then s_exit=(-B-sqrt(B*B-4*H*C))/(2H);
s_reentry=(-B+sqrt(B*B-4*H*C))/(2H).
Proof: convex parabola has positive endpoints, negative interior vertex, and vertex inside (0,1). Hence both outsider differentiation eta>0 and member cost reduction rho>0 are NECESSARY to get two crossings within this model.

## Proposition B: root comparative statics
At s_exit Y_s=-sqrt(discriminant) and at s_reentry Y_s=+sqrt(discriminant). For any primitive z, ds_root/dz=-Y_z/Y_s. Here
Y_rho=-2*d(s)*s; Y_eta=2*s*(1+rho*s);
Y_kappa=s; Y_v=-2-s.
If d>0 at both simple roots and source SPD/economic constraints remain satisfied, increasing member cost savings rho or source network v expands the outsider-zero interval (earlier exit, later reentry). Increasing outsider differentiation eta or within-coalition substitution kappa contracts the interval (later exit, earlier reentry). A source-v perturbation also changes own-value coefficient m=1-v, so it is NOT a pure interoperability shock.

## Proposition C: outsider ZERO can occur ON a strong-stable RS contract
Exact original six-parameter rational witness:
(v,gamma0,kappa,eta,rho,phi)=(3/10,3/5,1/10,11/20,10,120).
All inequalities strict: 0<eta<gamma0<m=7/10; kappa>0; NS/RS/IS demand SPD for all s. Physical cost implementation a=13, c0=12, h=10, f=120 keeps all marginal costs >=2 at every s.
Y(s)=(110*s*s-111*s+8)/10;
s_exit=(111-sqrt(8801))/220 ≈0.07811979517;
s_reentry=(111+sqrt(8801))/220 ≈0.93097111392.
At the negotiated RS depth s=1/10, the OUTSIDER quantity is exactly zero, both insiders strictly produce. Resident firm and government member payoffs are P_R=15398/16335≈0.942639 and W_R=110194/49005≈2.248628, strictly above NS levels P_N=105/338 and W_N=495/676. Thus the contract is PURE SPNE realizable.

Stronger result: the contract RS(12,s=1/10) is STRONG NASH of the REDUCED CONTRACT-ANNOUNCEMENT game, robust to either outsider preannouncing any IS(t). Exact independent polynomial/Sturm checks over ALL alternative t in [0,1]:
(1) P_R(1/10)>P_I(t) always (RS firm vetoes any IS).
(2) On low-s outsider-active interval, W_R_active(t)<W_R(1/10) for t in [0,2/25].
(3) On high-s outsider-active interval, P_R_active(t)<P_R(1/10) for t in [93/100,1].
(4) On outsider-zero branch with t<1/10, W_R_corner strictly increases in depth.
(5) On outsider-zero branch with t>1/10, P_R_corner strictly decreases in depth.
By (2)-(5), no member firm AND govt can jointly gain from any new RS depth; other pair RS deviations are blocked by country symmetry. All exact rational sign checks passed in code/stage3_outsider_reentry_theorem.py, GitHub Actions 38451435782. Strict margins certify a nonempty open neighborhood around the witness.

Boundary significance: outsider quantity continuously reaches zero then later recovers; member quantities and profits generally have KINKED s-derivatives. Algebraic identity
x_active=x_zero-d*y_active/(2m+b)
makes the kink explicit when d>0 and Y_s≠0 at crossing. Simple smooth interior-FOC methods may therefore misidentify Stage1 optimal depths. Entry/reentry describes comparative statics across standardization rates, not the passage of time.

## Novelty gate
A second rational construction with v=0, gamma0=9/10, kappa=1/20, eta=17/20, rho=10 also satisfies SPD and the same two-crossing inequalities. Hence the phenomenon is NOT inherently a network externality effect. Nearby prior work: Ghosh–Morita (2012), competitor collaboration/product distinctiveness; Bourreau–Dogan–Manant (2016), endogenous scope+size in Cournot; IJIO 2011 R&D-induced industry polarization/shake-outs. The precise full-text theorem coverage in the cited literature is incomplete.

Stage3 verdict: a genuine market-specific structural and bargaining-equilibrium witness FOUND. Publication-level novelty NOT established; prior Stage6 NO-GO remains. Next required theorem must show a new equilibrium-selection or outsider welfare/policy comparison caused by the endogenous KKT regime boundary, beyond a familiar Cournot exit effect; then Stage4 independent red-team and Stage6 predecessor-theorem absorption. Do not merge, enter Stage7, or call paper submission ready.
