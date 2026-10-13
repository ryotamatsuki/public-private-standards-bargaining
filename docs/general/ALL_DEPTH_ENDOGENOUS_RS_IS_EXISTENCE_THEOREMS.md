# Stage 4: all-depth RS/IS equilibrium existence and partial-standard persistence
Date: 2026-10-14 JST. Original single endogenous s model, exogenous network strength v. Parent: PR #15. This is a theorem candidate, NOT all-five-dimensional quantifier-free CAD, Stage4A PASS, Stage6 novelty GO, or paper-submission authorization.

## 1. Game and exact Cournot continuation
Stage 1 six actors G1,F1,G2,F2,G3,F3 simultaneously announce SQ/RS(C,s)/IS(s), where s in (0,1], a bilateral RS requires its four government/firm matching signatures, IS requires all six. Stage 2 differentiated Cournot in each of three national markets. Actual deviators must all strictly improve for strong Nash; outsiders can preannounce irrelevant IS messages while RS remains in force. Government payoff is domestic consumer surplus plus its resident firm's worldwide net profit after one real quadratic setup fee.

Normalize five free EXOGENOUS market/technology/cost parameters:
 (G,Lambda,Delta,rho,F) = (gamma0/(1-v),(kappa-v)/(1-v),eta/(1-v),h/(a-c0),(1-v)f/(a-c0)^2).
Demand diagonal 1, RS within-club substitution b(s)=G+Lambda*s, outside d(s)=G-Delta*s. RS inside output x=[2(1+rho*s)-d]/[2(2+b)-2d²], outsider y=[2+b-2d(1+rho*s)]/[2(2+b)-2d²] when y>0; if outsider has nonpositive desired output, actual KKT output is y=0 and x=(1+rho*s)/(2+b). IS output qI=(1+rho*s)/[2(1+b)]. At s=0 all agree with NS. All matrices SPD in economic domain 0<=Delta<=G<1, rho>=0 and specified further SPD conditions; see parent PR #14 for complete domain. Firm and member-government payoff functions are P_X(s)=P_X^0(s)-F*s² and W_X(s)=W_X^0(s)-F*s². Outsider pays no fee.

## 2. NECESSARY AND SUFFICIENT all-s strong-Nash CONTRACT OUTCOME sets
For X=R,I let H_X(p) = sup { W_X(t) : 0<t<=1 AND P_X(t)>p }, sup(empty)=-infinity. Then another X-standard is strictly profitable for BOTH its requisite firm and government iff H_X(p)>w; if H_X(p)<=w no strictly joint-profitable X offer exists.

E_R(theta,F) is EXACTLY all s in (0,1] with:
  P_R(s)>=P_N AND W_R(s)>=W_N;
  H_R(P_R(s))<=W_R(s);
  H_I(max(P_R(s),O_R(s)))<=max(W_R(s),U_R(s)).
These criteria characterize SOME supporting six-player strong-Nash matching message profile (RS outsiders originally announce SQ). For EVERY possible outsider preannouncement, replace the last condition by the STRONGER H_I(P_R(s))<=W_R(s). No mistaken requirement that indifferent, NONDEVIATING outsiders strictly gain.

E_I(theta,F) is EXACTLY all s in (0,1] with:
  P_I(s)>=P_N AND W_I(s)>=W_N;
  H_I(P_I(s))<=W_I(s);
  H_R(P_I(s))<=W_I(s).
These are general for all endogenous depths, all five parameters in the SPD Cournot domain and piecewise KKT cases. The equalities at all depth boundaries correctly reflect strict-improvement strong Nash. The theorem follows the exhaustive original message-changing coalition deviation partition of parent PR #12, not from an assumed benevolent social planner.

The set is an EXACT functional/semialgebraic equilibrium correspondence; an explicit global 5D polynomial-cell enumeration remains unfinished. For any RATIONAL parameter vector and rational candidate s, previous exact rational Sturm global-deviation verifier decides each membership, taking all t continuum, including outsider-exit/reentry roots.

## 3. SHARP full-depth-unrestricted fee threshold for NS
At fixed four market coordinates mu=(G,Lambda,Delta,rho), let P_X^0,W_X^0 denote F=0 gross member profit and government welfare. Define
 Phi_X(mu) = sup_{0<s<=1} min((P_X^0(s)-P_N)/s²,(W_X^0(s)-W_N)/s²),
 evaluated with appropriate regional corner payoffs. Phi(mu)=max(Phi_R,Phi_I), allowing +infinity.
**EXACT GENERAL THEOREM:** NS is a strong-Nash CONTRACT OUTCOME iff F >= Phi(mu) (F>0). A collective profitable RS or IS offer exists exactly when F<Phi, because participating governments and firms must both strictly gain. At F=Phi equality is stable under strict-deviation strong Nash.

Define initial private normalized gross incentive polynomials
 K_R=Delta(1-G)+2*rho(1+G)-Lambda,
 K_I=rho(1+G)-Lambda.
Exact identities:
 P_R^0'(0)=3*K_R/[2(2-G)(1+G)^3],
 P_I^0'(0)=3*K_I/[2(1+G)^3],
 K_R-K_I=Delta(1-G)+rho(1+G)>=0,
 CS_R'(0)=[G*K_R+G*Delta(1+G)+2*rho(1+G)^2]/[4(1+G)^3].
If K_R>0, both regional private and government marginal gains at s=0 are strictly positive. Because benefits start at order s and costs are only F*s², there is for EVERY FINITE F a sufficiently small s>0 that makes both strictly better than NS. Thus Phi_R=+infinity and NS is NEVER strong Nash for finite F. Conversely K_R<=0 implies K_I<=0 and both Phi's finite, so at sufficiently large F NS is stable. This is a sharp qualitative five-parameter distinction. A high fee does not generically imply no standardization when s is endogenous.

## 4. The within-standard Pareto compromise interval
If BOTH P_X and W_X are strictly concave over s in [0,1], with unique maxima s_F^X and s_G^X, then H_X(P_X(s))<=W_X(s) iff s lies BETWEEN s_F^X and s_G^X inclusive, intersected with (0,1]. Outside this band moving toward the two individual maxima strictly improves both payoffs; inside no one-sided move improves both because the actor whose optimum has been passed vetoes it. This gives a transparent private/public compromise-depth band and collapses the same-standard universal deviation test to interval arithmetic. The required concavity is NOT universal in all parameters and must be verified or else the original H_X criterion used.

## 5. EXACT all-s partial-depth coexistence beyond BOTH full-depth extinction fees
At mu=(G,Lambda,Delta,rho)=(5/16,-1/16,3/32,1/4) and F=2/5=.4, previous exact full-depth cutoffs were FR*=310713952/1042430125 (~.29806693) and FI*=39/128 (=.3046875). Since F exceeds BOTH, RS(1) and IS(1) are each NOT strong Nash (the signer coalitions can lower own standard depth and all profit).

**Nevertheless** the following BOTH have strongly stable matched contracts:
   RS(s_R=3/5=.60); IS(s_I=13/20=.65).

Independent exact SymPy Sturm root-count certificates prove all t in [0,1]:
   P_R(3/5)>P_I(t) [private signer veto against any IS, even outsider preannouncements];
   W_I(13/20)>W_R(t) [public signer veto against any RS].
For each standard, P''(t)<0 and W''(t)<0 all t, and candidate s satisfies P'_X(s)<0<W'_X(s); therefore both lie in the Pareto-efficient private/public depth interval and all same-standard deviating coalitions are blocked. All four IR margins above NS strictly positive, market SPD and all outputs strictly positive for every depth. Parent independent exact KKT/Sturm global-game verifier confirms RS(.6) robust, IS(.65) strong, RS(1)/IS(1) not strong, NS not strong. Exact strict inequalities guarantee a nonempty OPEN FIVE-DIMENSIONAL neighborhood of this result.

**Conclusion:** neither earlier fee cutoff is a standard-TYPE disappearance threshold; lowering commonality can restore BOTH RS/IS types.

## 6. NEW GENERAL LARGE-F coexisting PARTIAL standards theorem
Fix any admissible 4D market mu. Let a_PR=P_R^0'(0), a_PI=P_I^0'(0), a_WR=W_R^0'(0), a_WI=W_I^0'(0), and suppose the following strict sign conditions hold:
 H1: a_PR>a_PI>0
 H2: a_WI>a_WR>0
 H3: 2*a_WR>a_PR
 H4: 2*a_PI>a_WI.

Then there is a finite F0(mu) such that for EVERY F>F0, both
  RS(s_R(F)) with s_R(F)=argmax_{s∈[0,1]} P_R(s;F)
  IS(s_I(F)) with s_I(F)=argmax_{s∈[0,1]} W_I(s;F)
are strongly stable matched contracts, RS robust across any nonbinding outsider message. Moreover s_R(F)=a_PR/(2F)+O(F^-2), s_I(F)=a_WI/(2F)+O(F^-2), so both depths approach ZERO as F increases, never abruptly disappearing.

Proof: source gross payoff functions are continuous, bounded on [0,1] and smooth near zero (initial symmetric three-firm market interior); quadratic F*s² makes each global optimum approach zero. Taylor expansion and FOC yield max P_R=P_N+a_PR²/(4F)+O(F^-2), max P_I=P_N+a_PI²/(4F)+O(F^-2), max W_R=W_N+a_WR²/(4F)+O(F^-2), max W_I=W_N+a_WI²/(4F)+O(F^-2). H1 implies regional firm's GLOBAL optimum dominates any IS firm's profit; H2 implies international government's GLOBAL optimum dominates any RS government's W. Thus RS is veto-protected against any IS regardless of outsider preannouncements and IS veto-protected against any RS. Their own within-type changes are impossible since R firm and I government respectively hold globally maximizing payoffs. H3 implies W_R(s_R)-W_N=a_PR(2*a_WR-a_PR)/(4F)+O(F^-2)>0; H4 implies P_I(s_I)-P_N=a_WI(2*a_PI-a_WI)/(4F)+O(F^-2)>0. Remaining IR conditions automatic. QED.

Baseline exact normalized initial slopes:
 a_PR=25664/83349=.3079101129
 a_PI=800/3087=.2591512796
 a_WR=36212/83349=.4344623211
 a_WI=1366/3087=.4425008098.
All H1-H4 are STRICTLY satisfied. Second independent exact all-depth proof at F=10 confirms RS(s=.017) and IS(s=.022) BOTH strong and NS not strong, using Sturm plus original KKT full-game evaluator. This is a NONEMPTY OPEN set of all five parameters, not a numerical grid finding. When integration cost becomes high, firms and governments reduce commonality to order 1/F; multi-standard equilibrium coexistence can persist for ARBITRARILY HIGH F.

## 7. Status and pending independent gates
Completed: general necessary-and-sufficient any-s strong-Nash outcome correspondence; sharp single-scalar NS fee threshold Phi(mu); general K_R criterion for NS NEVER strong at any finite F; strict concavity efficient depth-band theorem; exact partial s_R=.6, s_I=.65 coexistence at F=.4 despite both depth-1 failures; general sufficient high-F persistent coexistence theorem and exact F=10 all-depth witness, with Cournot corners covered in original game oracle. Verification via code/verify_all_depth_frontier_theorems.py and code/verify_high_fee_coexistence.py, original code/verify_six_dimensional_corners.py, full GitHub Actions.

Not completed: fully explicit necessary-sufficient five-dimensional quantifier-FREE phase classification for all standard type combinations; case taxonomy of all critical fees at finite F with arbitrary own/cross network coefficients; independent Stage4A source/contribution audit; Stage6 parent-theorem absorption testing against Bourreau–Doğan–Manant 2016 endogenous size+scope Cournot model, Economides–Skrzypacz 2003 standards coalitions, Ghosh–Morita 2012 and generic bargaining/veto results. This branch is not submission-ready and should remain a draft.
