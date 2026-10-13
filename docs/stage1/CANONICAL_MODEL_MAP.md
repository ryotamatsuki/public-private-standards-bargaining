# Stage 1 canonical model map (AUDITED continuation, PROVISIONAL bargaining)

Date: 2026-10-13. This document specifies an audit object, not a certified complete extensive-form bargaining game.

## Agents / objectives
Two sovereign states k=1,2; home-headquartered firms i=1,2, each selling in both destination markets; consumers in each market. Firm i maximizes worldwide net operating profit minus actual technology/adoption costs. Government k evaluates local consumer surplus plus its resident firm's worldwide net profit plus net public revenue minus real public spending. Transfers paid across national borders are accounted for by recipient ownership. No global planner or welfare-optimal standard is asserted.

## Bargaining and rights
Public authority R_k(s): enforceable legal approval/recognition of standard s for regulated sales in jurisdiction k. Private holder L_i(s): authorization to use privately controlled implementation IP/technology. Actual lawful implementation needs relevant approval AND technology authorization (when essential rights are protected) AND the firm's own adoption action. A government cannot grant IP licenses, nor can a private owner grant official approval. Other standards may exist; refusal does not prohibit every alternative product. The reality/scope of these rights is an assumption to justify by sector, not an institutional fact.

Protocol primitives to specify at the next research-design stage: who may propose, response/expiration, revisions, observable/verifiable approval and license rights, dispute settlement and discounting. Candidate endogenous objects: approval, license terms, technology/standard selection, participation, coalition. Current document does not assign a distribution over proposers or claim a stationary bargaining equilibrium.

An eventual joint-versus-separated-protocol comparison must HOLD FIXED legal rights, final enforceable feasible allocations, information, transfer budget, market payoff accounting and outside opportunities. Protocol/order/commitment can differ ONLY if explicitly recorded; simply allowing conditional contracts in one protocol and forbidding them in the other is not a pure bargaining result.

## Downstream differentiated quantity competition
Two products in destination k, quantities q=(q1,q2). Market consumers have quasi-linear gross utility:
U_k(q;z)=a(q1+q2) - 1/2 q' M_k(z) q, with a>0.
Inverse demand: p=a 1-M q. This is a consumer-valid integrable system, not simply the previous R9 reduced-form consumer-surplus expression.

Benchmark disconnected standards: M_0=[[1,gamma],[gamma,1]].
Two active firms with linked technical standard: M_L=[[1-v,gamma-v],[gamma-v,1-v]].
Use 0<=v<=gamma<1; then eigenvalues of M_L are 1-gamma and 1+gamma-2v, so demand is strictly concave and products remain substitutes. Gamma is exogenous horizontal substitutability, v is an independently identified compatibility effect. No endogenous product-location or quality investment.

Costs c1,c2 are REAL marginal resource costs, distinct from royalty r>=0, a pure payment by implementer 2 to resident IP owner 1 per unit in the audited sample contract. Effective private marginal costs are c1, c2+r. Fixed real investment/setup costs K_i may be subtracted when investment is feasible; whether already sunk depends on subgame timing. Government taxes/transfers zero in audited baseline. Future contracts may have a different rights structure, which requires a fresh calculation.

Given M, each firm chooses q_i>=0 noncooperatively. Best response is q_i=max{0,(a-c_i^{eff}-M_ij q_j)/(2 M_ii)} when own M_ii>0.

For linked M, let m=1-v, b=gamma-v, D=4m^2-b^2. If interior:
q1=(2m(a-c1)-b(a-c2-r))/D;
q2=(2m(a-c2-r)-b(a-c1))/D.
D>0 throughout stated domain; output positivity is a separate condition. If outputs violate feasibility, use complementarity/KKT and re-solve the active set. Conditional on an unchanged market matrix, the q2=0 corner has q1=(a-c1)/(2m) and entrant-2 gradient a-c2-r-b q1 <=0. If compatibility disappears when a licensee exits, this is a DIFFERENT off-path regime and must be separately specified/audited.

Consumer surplus CS_k=(q' M_k q)/2. Operating payoffs in any destination:
pi1^k=(p1-c1)q1 + r q2; pi2^k=(p2-c2-r)q2.
Both countries' worldwide firm profit sums these destination-specific payoffs (less actual fixed costs). With no taxes, sum_k W_k = sum_k(CS_k+pi1^k+pi2^k) = sum_k[a 1'q - 1/2 q'M_k q - (c1^k q1^k+c2^k q2^k)] minus real fixed costs; royalty cancels as a TRANSFER, but its endogenous quantity distortion does not.

## Exact audit diagnostics
For a=1,gamma=1/2,v=1/5,c1=0,c2=1/10,r=1/20, linked interior q=(269/494, 106/247), CS=80038/305045, pi1=157813/610090, pi2=44944/305045.
With c1=1/10,c2=0 in the second destination and same royalty, q=(231/494,125/247), CS=318347/1220180. Two-market national welfare with no public transfer/fixed costs: W1=880097/1220180, W2=748123/1220180.
For single-market costs (0,1/10), the entry cutoff is r=57/80. At r=4/5, q=(5/8,0) and entrant-2 KKT gradient=-7/80. These are EXACT conditional-market checks, not bargaining equilibria.

## Core methodological limitation
R9's common idiosyncratic valuation u across all producers does not by itself identify a unique differentiated brand demand allocation when consumers choose at most one. R9 posits product-level inverse demand and CS=Q^2/2; its network-benefit consumer interpretation is NOT the same as the present integrable LQ utility. Even the gamma->1 limit gives a singular M and the present CS=(1-v)Q^2/2 (for two linked products), not the old R9 CS=Q^2/2. Old national-welfare rankings/propositions CANNOT be inherited by relabeling gamma. Homogeneous endpoints require separate treatment.

## Not proved
No existence/uniqueness of public-private bargaining SPE, standards coalition structure, licensing Nash equilibrium, industry-wide adoption best responses, or standard optimality. This verified product-market continuation is only an input to Stage 2 literature audit and later mathematical construction.


IMPORTANT 2026-10-13 CHANGE CONTROL: original benchmark with singleton M_ii=1 and fixed gamma is superseded for the **CURRENT PROJECT MODEL** by docs/stage1/ONE_SHOT_PROTOCOL.md. Original formula identities remain an audit of their OLD assumptions only, not the revised economy. See STAGE1_PROTOCOL_REAUDIT.md.
