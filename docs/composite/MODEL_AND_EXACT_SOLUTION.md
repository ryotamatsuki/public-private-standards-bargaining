# Composite continuous-standard model — audited construction, 2026-10-13
Working title: *Endogenous Public–Private Standards Bargaining under Differentiated Oligopoly*

## Governance and design decision
The author challenged the premature inference that Stage-4's **fixed finite menu** NO-GO invalidated the complete research idea. This is a SEPARATE branch from Stage 3 and preserves the previously failed Stage 4 result. The author specifically requests actually solving a compound model with network effects, standardization-dependent product differentiation, and one-shot bargaining. This branch introduces **one newly justified real economic channel:** shared technology reduces real unit costs and incurs convex real implementation/R&D expense. This is **new Stage-1 source-model content**, not smuggled into the failed model.

## Stage 3 revisit / Stage 1 source re-audit
Players: 3 countries k=1,2,3, with home firm F_k; states G_k control national recognition, essential technology owners/implementers F_k control technology consent. Every country has a distinct unit-mass consumer market; all three firms compete in quantities in each market (segmented Cournot). Each coalition is an UNORDERED BILATERAL PAIR C∈{{1,2},{1,3},{2,3}} with standard depth s∈(0,1]; no cross-border royalty or government cash transfers in this benchmark. Each of FOUR actors {Gi,Fi,Gj,Fj} submits the **exact same pair and depth** to activate a contract. Each of six actors submits one full contract or SQ simultaneously. Outsiders with no essential rights have no veto. Different bilateral coalitions overlap, so never both form. Contracting commits implementation; no later optional-adoption subgame is assumed. Each contract incurs real per-member common-design expense f s² with f>0.

Consumer utility in each country:
U_k(q;C,s)=a 1'q-(q'M(C,s)q)/2.
For all i: M_ii=1-v (so a singleton has own positive network benefits). For different i,j: M_ij=γ0 except M_ij=γ0+(κ-v)s when pair {i,j}=C. Thus s simultaneously raises product similarity by κs and creates mutual compatibility worth vs per cross quantity. γ0,κ,v remain conceptually distinct although net effect enters pair's off-diagonal through κ-v. Positive definiteness is imposed and explicitly checked. Inverse demand p=a1-Mq. No standard is s=0 with unchanged costs, no compatibility, no design similarity, but WITH each firm's own network benefit.

For C={1,2}, member firms have real marginal cost c(s)=c0-hs, outsider cost c0. Both member firms incur real common-design setup cost f s² each after signing, not per-market; outsider no cost. h≥0 is the resource saving to jointly develop/use the technical design, f>0 captures increasing technical integration/R&D difficulty. THESE ARE STYLIZED PRIMITIVES, not an asserted exact reproduction of Ghosh–Morita's circular-city model. Both components have direct precedent in cost-sharing work. The convex fixed real cost assumption can drive an interior standard and thus MUST be documented as a crucial, not novel, source of curvature.

Country k welfare W_k = CS_k + Π_k (home firm's TOTAL net profit from all three markets), firm F_k wants Π_k. The cost f s² is deducted from Π_k and hence counts ONCE in W_k, not twice in world welfare. No foreign owners, taxes, unmodeled royalties, or change in market population. IP rights are assumed indispensable only for named signers, pending realistic sector justification.

## Exact Cournot / quantities
Write m=1-v, g=γ0, d=κ-v, b(s)=g+ds and A=a-c0.
With two identical members producing x per destination and outsider quantity y:
 (2m+b)x+g y = A+h s,
 2g x+2m y = A.
Let D(s)=2m(2m+b(s))-2g²>0. The unique interior equilibrium is:
 x(s) = [2m(A+h s)-g A]/D(s);
 y(s) = [(2m+b(s))A-2g(A+h s)]/D(s).
Consumer surplus in each destination: CS(s)=(m+b)x²+(m/2)y²+2gxy.
Worldwide **participant firm** profit P(s)=3m x(s)² - f s².
Participant government welfare W(s)=P(s)+CS(s).
Outsider profits Π_o(s)=3m y(s)²; outsider government W_o(s)=Π_o(s)+CS(s).
At s=0, all 3 firms have q(0)=A/(2m+2g), standard absent, real setup spending zero. For generic SPD M, B=M+diag(M) SPD gives unique Cournot via strictly convex quadratic complementarity; any corner requires KKT. In the verified parameter region, all q>0 over s∈[0,1], so these are genuine full continuation solutions. Market demand does not itself choose s: strategic agents do.

## Fully exact benchmark
Set a=1, c0=1/5, h=1/5, f=1/5, v=1/10, γ0=1/4, κ=3/20. Then m=9/10, b(s)=1/4+s/20 and:
 x(s)=8(9s+31)/(18s+713), y(s)=4(62-3s)/(18s+713).
Stage-4 verification gives positive q and strict positive definiteness over [0,1], and exact Cournot demand, cost/welfare identities and derivative factors. At this benchmark both P(s) and W(s) are strictly concave on [0,1], with unique interior peaks s_F and s_G:
 0.4753 < s_F < 0.4754, numerical s_F=0.47537259738...
 0.7437 < s_G < 0.7438, numerical s_G=0.74377312467...
All exact rational inequalities checked in code. P(s_G)>P(0) and W(s_F)>W(0), so the whole intermediate range satisfies BOTH firm and govt individual-rationality participation constraints. Outside members' quantity falls as s grows; the external profit and national-welfare incidence can have opposing signs, so compare them separately.

### Exact one-shot game outcome characterization in this benchmark
(1) All-SQ declaration profile is a pure Nash because no individual can activate an agreement; it is NOT coalition-strong because four signers can jointly change to a small positive s, which raises P and W.
(2) For any selected bilateral coalition C, any PERFECTLY MATCHED contract with s∈[s_F,s_G] is a STRONG NASH EQUILIBRIUM of this restricted exact-contract game: government signers and firm signers each strictly prefer it to SQ; and any new bilateral coalition shares one country's G and F, whose joint payoff pair is (W,P), hence a move to any new s cannot make BOTH strictly better on this Pareto-efficient interval. A same-pair change requires all signers and also cannot improve both types.
(3) No perfectly matched s outside this interval is strong: for s<s_F both P and W strictly increase by selecting larger s near s_F; for s>s_G both strictly increase by selecting smaller s near s_G. All non-activated messaging profiles can be coalition-blocked by a profitable fully matched contract.
(4) In the **firm-only rights** game the stable accepted-depth for each pair is uniquely s_F. In **government-only rights** it is s_G. In joint two-key rights, all depths between the two survive. The coalition identity (the pair chosen) is NOT unique due to country symmetry. The precise agreement s is NOT selected without an additional justified institution. These are **known Pareto agreement logic applied to a calculated Cournot payoff family**, not necessarily an independently novel theorem.
(5) The total global welfare is the sum of three market gross utility minus real production cost minus each actual integration expense; royalties zero. Symmetric entrant rights do not prove participation is essential in any real-world standard.

## Case-solution status and limits
- Exact mathematical solution of the 3-country composite benchmark: COMPLETE (symbolic formulas, strict-concavity root isolation, every coalition symmetry-related, IR and pure strong-Nash).
- Formal independent theorem certification Stage 4A: NOT RUN. Parent-theorem/novelty Stage 6: NOT RUN.
- Model-level source redesign is **explicit** and backed by Stage1 mini-audit; Stage2 mini-screen documented separately. No evidence that interdependence beyond generic consensus is novel.
- Multiplicity is unavoidable under exact-match one-shot rules. Continuous-depth signing does not force a unique standard.
- Symmetric firms and countries; no licensing royalty in this benchmark; adding r, asymmetric property ownership, country-vs-firm coalition mismatch, outsider-design η, IP FRAND restrictions or post-signature adoption requires explicit further source-math checks.
