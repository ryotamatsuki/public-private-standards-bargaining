# Stage 3/Stage 1 re-entry: independently chosen compatibility and commonality
Date 2026-10-14 JST | This is a **NEW MODEL SOURCE VERSION** nested around the parent RS/IS model (PR #10). It is explicitly NOT the same frozen Stage-6 model. Previous Stage-4A and Stage-6 certificates remain historical; they do NOT certify these additional strategic choices.

## 1. Why the old result did not finish the problem
The prior source model chose ONLY s, with all competitor differentiation mechanically fixed by γ12=γ0+κs and γ13=γ23=γ0−ηs. Network intensity v was a primitive explored only in bounded regimes, and v also entered own diagonal 1−v. Thus the 1D optimum and a certified v rectangle are NOT a global solution with separately endogenous product positions/commonality and compatibility.

We deliberately split the two economic decisions: (a) technical standard **interoperability/network compatibility** s∈[0,1] and (b) **shared product-design/commonality/product-location convergence** z∈[0,1], BOTH named in the negotiated contract and BOTH freely chosen by signers. z is a collective endogenous product-characteristic choice, rather than the predetermined κs change. κ and η are demand sensitivity parameters, NOT themselves agent-chosen variables. This is not equivalent to Ghosh–Morita (2012) Salop location–price equilibrium; for that, an additional product-location best-response stage and full microfoundation would be needed.

To isolate exogenous network characteristics from interoperability, set two INDEPENDENT primitives ω (own-product network valuation) and v (cross-brand interoperability valuation). m=1−ω, held independent from v. They are freely varied across parameter space but firms/governments do NOT choose either coefficient strategically; realized network consumption/quantities remain endogenous in Cournot. Otherwise introducing a strategic choice of network valuation would change preferences and be economically inappropriate.

## 2. Exact nesting: old game recovered on diagonal
Let each signer's real R&D/integration outlay F(s,z)=f(s²+z²)/2, real marginal member cost c(z)=c0−h z. The old model with one depth u is EXACTLY recovered by imposing s=z=u, ω=v:
 M12=γ0+κ z−v s → γ0+(κ−v)u;
 M13=M23=γ0−η z → γ0−ηu;
 c(z)→c0−hu; F(u,u)=f u².
This preserves all prior benchmark results without giving the new model an unacknowledged extra cost-saving channel. Off-diagonal designs have costs deliberately split into two convex real investments; this is economically reasonable but NEW source content, subject to fresh novelty and robustness gate. Could vary weights fs,fz freely in future, but no ad hoc tuning here. s>0,z=0 represents compatibility without common components; s=0,z>0 represents common development without interoperability, economically possible under separate technological arrangements. Exclude s=z=0 from named RS/IS contracts to avoid duplicate NS labels.

## 3. Complete two-stage game and analytical Cournot continuation
Stage 1: Six players {Gi,Fi}_{i=1,2,3} simultaneously report SQ or exact named contract RS({i,j},s,z) for any country pair or IS(s,z). Four matched G/F actors for RS, all six for IS; others cannot veto RS. Stage 2: Each of three countries has a unit-mass market, and three internationally active differentiated Cournot competitors choose quantities. All agents anticipate unique Cournot continuation wherever the demand matrix is SPD and all equilibrium outputs are positive. All-one-round mismatched contracts lead to NS. No transfers, royalties, adoption stage, bargaining order or subsidy. Firm utility = worldwide net profit; government W = consumer surplus in own market + worldwide home firm profits.

Set A=a−c0, m=1−ω, b(s,z)=γ0+κ z−v s and d(z)=γ0−η z, Δ(s,z)=2m(2m+b)−2d². 
RS for pair {1,2}:
 M_R=[[m,b,d],[b,m,d],[d,d,m]]; unit costs (c0−hz,c0−hz,c0).
 x_R=[2m(A+hz)−dA]/Δ; y_R=[(2m+b)A−2d(A+hz)]/Δ.
 CS_R=(m+b)x_R²+2d x_R y_R+(m/2)y_R² per market;
 P_R=3m x_R²−F(s,z); outsider P_O=3m y_R²;
 W_R=P_R+CS_R; W_O=P_O+CS_R.
IS:
 M_I=[[m,b,b],[b,m,b],[b,b,m]], all costs c0−hz,
 q_I=(A+hz)/[2m+2b];
 CS_I=3(m+2b)q_I²/2, P_I=3m q_I²−F(s,z), W_I=P_I+CS_I.
NS has m own diagonal, γ0 all cross, cost c0; q_N=A/(2m+2γ0).
SPD/interiority and member F≥0 are assumptions to prove on each theorem domain. General corners, multi-standard simultaneous coalitions >3 countries and sequential/iterated proposals are not in this specified model.

## 4. General (parameter-continuous) game reduction
Write K=[0,1]² minus origin for feasible RS/IS contract depths. Every pair is symmetric; same-pair or cross-pair RS changes require one incumbent government's W_R and corresponding firm's P_R both STRICTLY improve when those two actually deviate. An arbitrary preannouncement by RS outsiders can make them NONDEVIATING IS signers and therefore does not require their payoffs to improve (Stage-4A correction).

A matched RS(C,s,z) contract is **strong-Nash stable uniformly over all supporting original outsider messages** iff:
 IR: P_R≥P_N, W_R≥W_N;
 no (s',z')∈K gives both P_R(s',z')>P_R(s,z) AND W_R(s',z')>W_R(s,z);
 no (s',z')∈K gives both P_I(s',z')>P_R(s,z) AND W_I(s',z')>W_R(s,z).
A matched IS(s,z) uniformly strong iff:
 IR: P_I≥P_N, W_I≥W_N;
 no (s',z')∈K gives P_I(s',z')>P_I(s,z) AND W_I(s',z')>W_I(s,z);
 no (s',z')∈K gives P_R(s',z')>P_I(s,z) AND W_R(s',z')>W_I(s,z).
These are EXACT implicit quantified inequalities for arbitrary primitive vector θ in a common global SPD/interior domain. They DO NOT give a closed-form full parameter-space partition; non-uniform message profiles and unmatched message Nash multiplicity are separate.

Under an interior optimum, the first-stage single-class benchmark first order conditions are ∂s P=∂z P=0 for F-only or ∂s W=∂z W=0 for G-only, with global KKT checks at 4 edges, corners, and stationary polynomial solutions. Differentiating these FOC systems with respect to v gives d(s*,z*)/dv = −H(P)^(-1)·(P_sv,P_zv)' where Hessian is nonsingular; the sign is NOT predetermined generally. For matching G/F strong-Nash, maximize vector (P,W) in Pareto rather than pretending one scalar FOC represents both.

## 5. EXACT GLOBAL TWO-CHOICE WITNESS, not a grid-only assertion
Freeze (a,c0,h,f,g,κ,η,ω,v)=(1,1/5,1/5,1/5,1/4,3/20,3/40,1/5,1/5).
All (s,z)∈[0,1]²: exact tensor Bernstein rational polynomial certificates + independent pure-Python Fraction Cramer payoffs establish RS/IS/NS SPD, strictly positive quantities, Cournot FOCs, real cost and national welfare accounts.
Certificate checks:
 (i) ∂z W_R(s,z)>0 uniformly => RS govt maximizes at z=1.
 (ii) ∂²_s W_R(s,1)<0 and ∂s W_R at .713>0, .714<0; unique global RS govt optimum (s_G∈(.713,.714), z=1).
 (iii) ∂s W_I>0 and ∂z W_I>0 => IS govt global optimum (1,1), W_I=17/20.
 (iv) For EVERY possible RS(s,z), W_I(1,1)>W_R(s,z), W_I(1,1)>W_O(s,z), with strict margin global tensor Bernstein certificates. Thus government-only strong-stable contract type is IS(1,1); joint IS(1,1) cannot be blocked by any RS (govt signers veto) or different IS (govt payoff already globally optimal).
 (v) For EVERY IS(s,z), P_R(.714,1)>P_I(s,z) by exact global 2D certificate; ∂s P_R(s,1)<0 throughout [.713,.714] => at s_G, P_R(s_G,1)≥P_R(.714,1)>sup P_I. Also W_R(s_G,1) globally maximal over RS, and both signers strictly prefer it to NS. Thus RS(s_G,1) jointly strongly stable, including preannounced outsider IS, and ALL firm-only stable contracts have RS type (a firm-only RS global profit optimum exists on compact domain and dominates IS).
 (vi) Strong-stable outcomes include **both** RS(s_G,1) and IS(1,1); different member interests produce coexistence. Firm-only selects RS (not necessarily unique optimum pair); government-only IS. This is a mathematically exact constructive result with independently chosen compatibility/commonality (not s=z).
No assertion that these are the ONLY joint strong outcomes, nor that all generic θ and v yield coexistence. Strong Nash in message game != CPNE, ordinary Nash remains multiple.

Illustrative exploratory differential_evolution (NOT used as proof): at ω=v=.2,
 firm RS argmax approx (s,z)=(.6420,.9542); government RS (.71309,1);
 firm IS (1,.35462); government IS (1,1).
These values are optimizer heuristics except government results mathematically proven; firm maxima existence is proved by continuity/compactness and type dominance, NOT unique global (s,z) values.

## 6. Stage status
This is **Stage 4 model construction in a NEW two-design source** with independently chosen s and z. Full-parameter semialgebraic Nash/strong-Nash correspondence is reduced to universal inequalities and Cournot exactly, but no unrestricted closed-form partition of θ exists yet. The shown global all-depth/all-commonality rational benchmark is rigorously proved, but demands a NEW independent Stage 4A and reopened Stage 6 theorem absorption; previous Stage4A and Stage6 judgements do not transfer. The strongest novelty threat is Bourreau–Doğan–Manant 2016 endogenous size/scope Cournot, Ghosh–Morita 2012 inside/outside products, Hart–Kurz 1983 generic Pareto coalition veto, plus Economides–Skrzypacz 2003 on network-standard coalitions.
Publication novelty/GE parameter threshold not certified. Network valuation ω and cross compatibility coefficient v stay EXOGENOUS and FREE as parameters, not choices. Fully microfounding location choice and network adoption could require extra stages not yet authorized.
