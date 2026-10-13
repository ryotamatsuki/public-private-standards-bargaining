# Two-sided Ghosh–Morita differentiation × network effects × standards bargaining
**2026-10-13 | Explicit Stage 3→Stage 1/2 re-audit→Stage 4 model revision.** This is a child of the composite solved branch PR #5. Historical fixed-menu Stage4 NO-GO remains independently recorded and unchanged.

## 1. Why this is a substantive correction
The earlier composite model changed only the insider pair cross-substitution M12 and kept M13=M23=γ0. It did NOT implement Ghosh–Morita's crucial outsider-distinctiveness effect. This new version varies BOTH member-pair and member–outsider cross coefficients. The change directly affects the Cournot equilibrium and the bargaining payoffs and therefore invalidates earlier s_F≈0.47537 and s_G≈0.74377 (NOT carried over).

### Literature anchor and precise limitation
Ghosh & Morita (2012), *Competitor Collaboration and Product Distinctiveness*, IJIO 30:137–152, DOI 10.1016/j.ijindorg.2011.07.003, publisher abstract/intro https://www.sciencedirect.com/science/article/pii/S0167718711000671, analyze 3 Salop-circle firms, the collaborator pair moves closer by z/2 each, internal distance contracts z and their distances to outsider each grow by z/2. Original model features PRICE COMPETITION and cost sharing; it is **NOT** mathematically equivalent to linear-quadratic inverse demand and Cournot. We adopt the *qualitative geometry* and assume a LOCAL LINEAR mapping from pair distance into LQ substitutability. κ is the raw cross-substitution rise of the insider pair; η=κ/2 is a testable candidate consistent with relative circle arc changes, **NOT** a uniquely proven demand coefficient mapping from Salop. Bourreau & Doğan (2010), IJIO 28:176–190 DOI 10.1016/j.ijindorg.2009.07.010, already endogenize cooperative product-component commonality, real cost saving, and market competition. Hart & Kurz (1983) general coalition-announcement/stability logic remains prior art. Economides & Skrzypacz (2003) already do standards coalitions and oligopoly with network effects. Do NOT claim model-component novelty, direct Salop Cournot equivalence, or new bargaining theorem from a new parametric term alone.

## 2. Frozen governance, timing and rights
Three sovereign states G1,G2,G3 and their respective firms F1,F2,F3. National consumer markets k=1,2,3; each market has all three Cournot brands with identical segmented-market demand and production costs. Any single bilateral coalition C={i,j} may form via a one-shot simultaneous EXACT CONTRACT matching message from the FOUR required actors Gi,Fi,Gj,Fj, naming same C and continuous common-design/standard depth s∈(0,1]. Outsider actor cannot veto without essential rights. Three possible bilateral pairs always overlap, so at most one forms. If no pact, s=0 and default national standards compete; own installed-base network benefit remains. Contract signing commits implementation. No sequential bargaining, no royalty, no cash transfers; cost and payoff incidence identical across three markets. Initial symmetry creates coalition and interval multiplicity, NOT a unique standard selected.
The source-model assumptions about regulatory recognition and indispensable private IP consent are conditional and require industry-specific justification. Government G_k maximizes local CS_k plus total worldwide profits of resident firm F_k. Firm F_k maximizes its own worldwide profit. No governmental ownership or domestic/foreign cost asymmetry, and identical destination consumers: deliberately stylized benchmark, not a realistic geographic calibration.

## 3. Consumer-valid market demand, cost and payoff
For coalition C={1,2} without loss of generality, with q=(q1,q2,q3) in a given national market, quasilinear utility U=a1'q−q'M(s)q/2; inverse demand p=a1−M(s)q.
 M(s)=[[m,b,d],[b,m,d],[d,d,m]], with
 m=1−v, b=γ0+(κ−v)s, d=γ0−ηs.
Raw insider substitution γ12^raw=γ0+κs INCREASES, but linked network cross-benefit v*s offsets it in p. Raw outside substitution γ13=γ23=γ0−ηs DECREASES. Single-product own network effect v retained for all brands even if isolated.
Member firms' REAL per-unit production cost is c0−hs, with h≥0; outsider cost c0. Both joining firms pay a one-time real integration/R&D outlay f s² each, f>0. These SOURCE terms were already introduced in the immediately prior composite model and are now held unchanged; no arbitrary added welfare term to secure reversal.
SPD M(s) ensures integrated concave representative-consumer utility and positive diagonal m. Three Cournot firms choose q_i≥0 independently in each market. KKT system with B=M+mI is strictly monotone and has a unique solution when SPD holds. General corners need active sets; benchmark interior ∀s∈[0,1].

For A=a−c0, determinant D(s)=2m(2m+b)−2d², exactly:
 x(s)=[2m(A+hs)−dA]/D, y(s)=[(2m+b)A−2d(A+hs)]/D.
Member firm profit P(s)=3m x(s)²−f s²; outsider firm profit O(s)=3m y(s)².
Each market CS(s)=(m+b)x²+2dxy+(m/2)y²; a participating government W=P+CS, an outsider government W_o=O+CS. Across 3 markets Σ_k W_k=3Σ_i[a q_i−(q'Mq)/2−c_i q_i]−2 f s². All cost savings are REAL and all fixed integration outlays counted exactly once.

## 4. Completely solved exact-rational example
Parameters a=1, c0=h=f=1/5, v=1/10, γ0=1/4, κ=3/20, η=κ/2=3/40. Then:
 m=9/10, b=1/4+s/20 and d=1/4−3s/40;
 x(s)=16(21s+62)/(2852+132s−9s²);
 y(s)=8(3s²+6s+124)/(2852+132s−9s²).
SPD Sylvester minors: 9/10>0; (13−s)(s+23)/400>0; (13−s)(728+96s−9s²)/16000>0 on [0,1]. x,y>0 on that interval. Marginal own-profit SOC −2m<0, exact FOCs hold. Full 3-market national/world welfare identities independently reproduced by separate Python Fraction Gaussian elimination (no SymPy inversion reuse). Q at s=0 identical for all brands=8/23.

The member payoff functions P(s) and W(s) have strict negative second derivatives ALL s∈[0,1]. This is PROVED via exact degree-8 Bernstein coefficients of −P'' and −W'', each coefficient strictly positive; denominators are positive 5*(9s²−132s−2852)^4. Each derivative P',W' starts >0 at s=0 and ends <0 at s=1. Thus each has a UNIQUE interior argmax:
 0.5319<s_F<0.5320 (numerically 0.531949078345);
 0.8249<s_G<0.8250 (numerically 0.824926718026).
Each signer prefers any s∈[sF,sG] over SQ. Standardization deepens beyond firm-alone optimum if its country co-signs, without determining one exact bargained s.

### Three-country simultaneous coalition stability (restricted protocol only)
- Pure Nash all SQ exists from exact-match coordination, even if every participating right-holder could gain; all SQ is strong-coalitionally blocked because they can jointly sign a positive-depth beneficial agreement.
- For any of the three symmetry-related bilateral coalitions, FULLY MATCHED contracts s∈[sF,sG] survive ALL strong Nash deviations: incumbent firm member and home government have strictly concave preferences with peaks sF<sG, so any alternative s cannot strictly improve both. Any rival bilateral pair necessarily shares one incumbent country and its G and F signers. Since the member-payoff curve is the same for whichever pair participates, the same no-joint-improvement argument blocks such moves. Signing partial/invalid alternative cannot increase the payoff of an actual deviator. For s outside [sF,sG] the four signers can jointly change to a closer depth that makes both types strictly better, so not strong-stable.
- Private-only benchmark: signed depth sF; government-only: sG; full two-key: nonunique continuum [sF,sG]. The bargaining protocol has NO endogenous Nash product-location choice and no unique norm or coalition identity.
- Replacing strong Nash with BPW coalition-proof equilibrium needs separate recursive self-enforcement and existence audit; this code does NOT certify CPNE.

## 5. TWO-SIDED competitive effect and exact threshold
At η=0 and identical other parameters:
 y'_outside(s)=−13020/(18s+713)² < 0, so outsider sales/operating profit FALL.
With η=κ/2=3/40:
 y'_outside(s)=48(75s²+3224s+124)/(9s²−132s−2852)² >0 ∀s∈[0,1].
Po and Wo also strictly increase in this parameter case (exact positive-polynomial derivative check). Hence outsider business profit and outsider national welfare BOTH RISE rather than fall. This is a **verified sign reversal in a comparative model**, NOT a novel result certification relative to Ghosh–Morita.

For general (strictly interior) symmetric 3-firm Cournot with m,g,κ,v,h,A=a−c0:
 y'(0)=[2Amη + Ag(κ−v)−2gh(g+m)]/[2(2m−g)(g+m)²].
Under 2m>g, derivative positive iff
 η > ηcrit= g[2h(g+m)−A(κ−v)]/(2Am).
At given parameters ηcrit=7/96≈0.0729167. Our η=3/40=0.075 exceeds it, while η=0 does not. Exactly rational proof in code; sign switch holds on an OPEN neighborhood of benchmark primitives by continuity, not merely a single equality.
This is a marginal condition near s=0, NOT a claim of globally positive outside derivative for every arbitrary η. Global positive derivative is separately proven only for the selected exact-rational benchmark.

## 6. Source audit / mathematical limits / novelty routes
What changed from prior source model: ONLY d(s)=γ0→γ0−ηs; all other pre-existing LQ, h,f,v, one-shot rights remain. Historic sF=.47537,sG=.74377 and outsider decline cannot be inherited. No unlimited transfers, royalty, full international coalition, incumbent patent owner beyond signatories, or post-signature adoption.

Nested controls:
  η=0 recovers immediate predecessor exactly (outgoing direct competition does NOT soften);
  κ=0 erases insider raw homogenization but network effect remains;
  v=0 removes interoperability network gains while own utility diagonal becomes 1;
  h=0 removes real marginal production savings;
  f=0 removes convex real integration cost and can move optimum to boundary.
The general derivative expression identifies η/κ/v/h channels, but does NOT prove all three are indispensable for a paper-level theorem. An independent theorem-absorption audit must test Ghosh–Morita (2012), Bourreau–Doğan (2010), Economides–Skrzypacz (2003), Lukach–Kort–Plasmans (2007), Hart–Kurz (1983) and other adjacent models. Original Ghosh–Morita analyzed rival PRICE responses in Salop geometry; our outsider OUTPUT/profit sign reversal can be a known/expected Cournot translation.
The Stage4 construction proof is scope-limited to symmetric 3-country club, specified param benchmark and derived marginal threshold. This is NOT Stage4A independent mathematical certification and NOT a publication novelty PASS.
