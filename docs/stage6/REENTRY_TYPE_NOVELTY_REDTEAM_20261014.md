# Stage 6 — Independent Novelty Red-Team: KKT Reentry, Standards and Mixed Government/Private Veto

**Date** 2026-10-14 JST.
**Research object** ORIGINAL three-country, three-firm NS/RS/IS, a single continuous negotiated depth s, six normalized exogenous parameters theta, and separate government and resident-firm exact unanimous signatures. Parent: Draft PR #26 (Stage5B), parent of #25/#24/#23/#22. Do not merge any of these, and do not change a submission manuscript.

**Stage 6 independent decision: NO-GO for a standalone publication-level new mechanism** in the Stage5B RS/IS strong-type bifurcation. We separately **RETAIN** an exact model-class KKT welfare incidence lemma. This is not a proof that some prior author printed the identical fraction; it is a demonstration of a generic preference/consent reduction and extensive closest-paper threat mapping.

## 1. Independent mathematical result (clean-room 3x3 Cournot matrix)

Rebuild the product market from
`M=[[m,b,d],[b,m,d],[d,d,m]]`,
with `m=1-v>0, b=gamma0+(kappa-v)s, d=gamma0-eta*s>=0`, and `z=1+rho*s>0`. With positive definite M, the Cournot interior response is `[M+diag(M)]q=(z,z,1)'`.
Let `A=2m+b`, `D=2m A-2d^2>0`, and `Y=A-2dz`.
Then `x=(2mz-d)/D`, outsider `y=Y/D`; when `Y<=0`, x is re-solved as `xc=z/A` and outsider is zero. The accounting is: `P=3m*x^2-phi*s^2`, `CS=(q'Mq)/2`, `W=P+CS`, fee subtracted once. All agree in levels exactly at `Y=0`.

**Universal NEWLY DERIVED candidate lemma (not certified novel relative to literature).**
At ANY genuine outsider *entry/reentry* crossing reached by increasing eta while holding the original `s>0`, m,b,z and phi fixed, with `d>0`, positivity of D and the other quantities, and `Y=0`, the one-sided eta derivative on the zero-output side is zero. The one-sided right derivatives on the outsider-positive branch are EXACTLY:
`P_eta^+=-3m*s/(d*D)<0`;
`CS_eta^+=+m*s/(d*D)>0`;
`W_eta^+=-2m*s/(d*D)<0`.
The outsider reenters because `y_eta^+=s*A/(d*D)>0`.

Proof is entirely algebraic: differentiate the independent 3x3 matrix solution with respect to d with m,b,z fixed, substitute the boundary identity `z=A/(2d)`, obtain `P_d=3m/(dD)`, `CS_d=-m/(dD)`, `W_d=2m/(dD)`, and use `d_eta=-s`. The resulting first-order **gross participant-firm loss : consumer-surplus gain : net participating-state welfare loss** magnitudes are exactly `3:1:2`, in this symmetric 3-country LQ specification. If the outsider is inactive, x and consumer surplus do not depend on eta, so all eta derivatives vanish. This is not a general theorem for arbitrary market competition systems, asymmetries, or regulatory accounting.

**Scientific meaning:** In the source model, an entrant's positive output can improve domestic consumers and reduce national participant welfare at the first instant of market reentry. The nonmonotone rebound later and threshold eta_c of Stage5B remain parameter-specific and cannot be deduced from this lemma alone.

Independent proof code: `code/stage6_reentry_generic_absorption.py`; no prior Stage3/Stage4/Stage5B verifier imported.

## 2. Decisive theorem-absorption countermodel: no product-market content

Define an ABSTRACT one-shot, six-player exact-signature contract game with the IDENTICAL feasible outcomes NS, RS(pair,s), IS(s) and the same 4/6 signature sets. For each participating country, in payoff units unrelated to quantity competition:
`P_N=W_N=0`,
`P_R(s,eta)=3s`, `W_R(s,eta)=[3+G(eta)]s`,
`P_I(s)=2s`, `W_I(s)=3s`,
where `s in (0,1]`,
`u=max{eta-31/100,0}`,
`G(eta)=-1/20-u+(200/9)u^2=(200/9)(u-3/40)(u+3/100)`,
and `eta in [1/100,39/100]`. Non-participating outsider payoffs may be 0 and do not confer a veto. No consumer utility, network demand, entry, firms' production, or quantity choice appears in the construction.

For EVERY eta, all participating payoff functions are strictly increasing in s. Consequently every signed contract with s<1 is Pareto-blocked by the same coalition's full-depth contract, and NS is blocked by RS(pair,1). The private signers prefer RS(1) (3>2) at all eta. The government signers prefer IS(1) over RS(1) iff `G(eta)<0`. Strict strong-Nash blocking of IS occurs iff `G(eta)>0` because its four potential RS signers all strictly improve. At `G=0` neither can strictly block IS, which survives the weak boundary.

The exact equilibrium **OUTCOME** correspondence is
`E^strong_abstract(eta)={RS(pair,1) for each of three pairs} union {IS(1) iff eta<=77/200}`.
The payoff wedge is FLAT for eta<=31/100, then drops to a unique trough at `eta=31/100+9/400=133/400`, then rises and crosses zero at `77/200=0.385`. This replicates Stage5B's KKT-onset, welfare-trough, and RS-only/RS+IS pattern with no economic market structure. The numerical abstract threshold 0.385 is intentionally different from source model eta_c≈0.385474. Therefore **the qualitative bifurcation (including its nonmonotone underlying welfare gap), consent incentives, open phase sides, and indifference boundary are completely generic two-type unanimous contract logic**. It is illegitimate to sell the game-theoretic type switch alone as novel to Cournot, standards, networks or governmental/firm double veto.

Importantly, the countermodel does NOT eliminate the value of the source economy's exact quantitatively mapped `eta_KKT=0.31`, its actual endogenous quantity change or the 3:1:2 KKT derivative. These are true model-specific formulae; whether their economic mechanism warrants a journal paper is a separate literature and external-validity question.

Independent SymPy complete exact assertions: `code/stage6_reentry_generic_absorption.py`.

## 3. Closest prior studies: distinguish verified text from incomplete primary verification

| Source and verification | Proven/reported component actually examined | Stage5B collision | Not actually established by this source |
|---|---|---|---|
| **Fischer & Serra (2000)**, *Standards and protection*, JIE 52(2):377–400; DOI 10.1016/S0022-1996(99)00058-6. Elsevier article preview and University of Chile author/institution abstract, NOT full author proof. https://www.sciencedirect.com/science/article/abs/pii/S0022199699000586 | A domestic firm may lobby for the *lowest technical standard excluding a foreign competitor*. Local social planner includes consumer welfare and may prefer a different, less exclusionary cutoff without the externality. | **VERY HIGH DIRECT THREAT**: outsider exit threshold, firm-government divergence and standards as trade protection are already studied. | Exact 3-firm 3-country 6-signature RS/IS support KKT derivative and subsequent reentry not verified. |
| **Edwards & Poyago-Theotoky (2013)**, *Regulatory Protection When Firms Decide First on Technical Collaboration and R&D*, Review of International Economics 21(4):750–764; DOI 10.1111/roie.12068. Published publisher abstract and bibliography. https://onlinelibrary.wiley.com/doi/10.1111/roie.12068 | Cournot-style cross-border competition, technology collaboration first, potential government imposition of technical trade barrier, which can induce firms to **avoid collaboration** to invite government national monopolies. | **VERY HIGH DIRECT THREAT**: technology cooperation alters government exclusion incentives; public-private strategic feedback anticipated. | Exact simultaneous same-contract government+firm veto and Stage5B reentry threshold not determined from accessible abstract. |
| **Cai & Jørgensen (2017)**, *Mutual Recognition for Sale: International Bargaining over Product Standards*, SDU 1/2017; SSRN doi 10.2139/ssrn.2894786. SSRN abstract/metadata. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2894786 | Bargaining between two countries over horizontal differentiated standards, Cournot downstream, producer interests and mutual recognition versus harmonization tradeoff. | **VERY HIGH DIRECT THREAT**: international standards bargaining + cross-border competition under differentiated goods. | Exact 6-agent signature structure and outsider's reentry not established in abstract. |
| **Costinot (2008)**, *A Comparative Institutional Analysis of Agreements on Product Standards*, JIE 75:197–213; DOI 10.1016/j.jinteco.2007.11.004. Publisher introduction and institutional open-access working paper metadata. https://www.sciencedirect.com/science/article/pii/S0022199608000251 | Governments cannot write complete contracts for standards; national treatment and mutual recognition allocate authority differently and create systematic distortions relative to optimum. | **HIGH INSTITUTIONAL THREAT**: welfare/recognition-rights allocation and contractual incompleteness. | Not a source of the specific 3-player KKT rule or separate essential-technology licensee signers. |
| **Jørgensen & Schröder (2014)**, *Harmonization versus Mutual Recognition*, SDU WP23/2014; author-university abstract. https://pure.au.dk/portal/en/publications/harmonization-versus-mutual-recognition-some-pitfalls-for-the-coo | Two-country/three-firm entry vs home-profit loss and harmonization regime choice, lobbying and imperfect competition. | **VERY HIGH GOVERNMENT/COMPETITION THREAT**. | No exact product differentiation eta KKT witness established. |
| **Ghosh & Morita (2012)**, *Competitor collaboration and product distinctiveness*, IJIO 30:137–152, DOI 10.1016/j.ijindorg.2011.07.003. Publisher abstract and preview; full article restricted. https://www.sciencedirect.com/science/article/pii/S0167718711000671 | Two competing collaborators reduce own distinctiveness while increasing difference from a noncollaborator; profit and welfare effect. | **HIGH PRODUCT-MARKET THREAT**: eta-type channel is already a core research subject. | Precise zero-output reentry and national double-signature findings NOT full-text checked. |
| **Bourreau, Doğan & Manant (2016)**, *Size of RJVs with partial cooperation in product development*, IJIO 46:77–106, DOI 10.1016/j.ijindorg.2016.04.004. INSPECTED independently accessible **2014 IAS working-paper precursor** https://www.ias.edu/sites/default/files/sss/papers/econpaper104.pdf (26 pages), not verified identical to 2016 final text. | The precursor's Proposition 1 studies possible equilibrium RJV size, Proposition 2 states size can increase or decrease as degree of product-development cooperation changes, and Proposition 3 proves wedge between members' choice and consumer/industry perspective. Cournot and LQ consumer surplus are explicit. | **VERY HIGH COMPETITION + NONMONOTONE WELFARE THREAT**. | No verified government signers, and no proof viewed of the exact outsider-zero 3:1:2 derivative. |
| **Economides & Skrzypacz (2003)**, *Standards Coalitions Formation and Market Structure in Network Industries*, NYU working paper https://neconomides.com/uploads/Standards.pdf (31 pages FULL read). | Sequential standards-coalition selection and downstream market structure; Propositions 1–6 classify full, fragmented and uneven coalition structures as network effects vary, including no-delay equilibria. | **HIGH BASIC STANDARD-TYPE ENDOGENEITY THREAT**. | Their model uses firm coalition/profit reduced forms rather than THIS government/private signature/KKT Cournot construction. |
| **Farrell & Simcoe (2012)**, *Choosing the Rules for Consensus Standardization*, RAND J Econ 43:235–252; author 2012 PDF https://people.bu.edu/tsimcoe/documents/published/ConsensusRules.pdf (32 pages). | Formal standard bargaining without side payments, endogenous bargaining delays and screening versus consensus decision rules. | **HIGH INSTITUTIONAL THREAT**: unanimous signature is not a new bargaining model per se. | Specific KKT quantity and simultaneous public/private essential rights absent from examined sections. |

**Additional plausible threats requiring follow-up full proof comparisons:** Hart & Kurz (1983) coalition announcement game, Ray & Vohra (1999) sequential endogenous coalitions, Gandal & Shy (2001) international standardization/recognition. All are cited in the parent Stage2/6 audit.

## 4. What fails and what remains after rigorous absorption

### Absorbed as generic or already researched
1. Standards can exclude foreigners; firms and governments can prefer different exclusion cutoffs (Fischer–Serra).
2. Technical collaboration changes government regulatory incentives (Edwards–Poyago-Theotoky).
3. Standards regimes are bargained, including recognition/harmonization effects under imperfect competition (Cai–Jørgensen; Jørgensen–Schröder; Costinot).
4. Strong-Nash RS+IS coexistence/switch under dual signature follows mechanically from payoff order and commitment rights (exact NONMARKET COUNTERMODEL).
5. A codimension-1 smooth indifference frontier follows from a simple zero of payoff differences (ordinary implicit-function theorem).
6. Zero-output Cournot regimes and nonmonotone welfare/profit responses are not, by themselves, new mechanism classes.

### Retain with explicitly LIMITED status
- General Cournot-boundary formula above: stage6 mathematical **PASS**, model-class lemma with exact 3:1:2 marginal incidence (no external theorem equivalence yet checked).
- Exact 6D-local eta switching coefficient of Stage5B: verified product-market/application-specific fact, not independently a generic IO breakthrough.
- Separate government and firm legal approval / essential IP authorizations: not present *as the same proposed one-round contract signature set* in examined specific papers; nevertheless this is **assumed institutional feasibility**, not an endogenized mechanism. Need legally and economically credible real industry where all four signatures really matter; otherwise it is just arbitrary veto players.

## 5. Stage6 decision and research discipline

**Stage6 RED TEAM — NOVELTY NO-GO.** This is not a mathematical rejection of Stage5B, which remains a correct source-model property. It is a rejection of claiming its generic type bifurcation, public/private wedge or exiting outsider mechanism as standalone new research. Even the KKT ratio should be claimed only as a restricted lemma until its near-exact antecedents and economical significance are established.

**Next permitted research direction** (only if user requests):
- First complete FULL proof-level access for Fischer–Serra, Edwards–Poyago-Theotoky, Cai–Jørgensen, Jørgensen–Schröder, Costinot and Ghosh–Morita; compare whether exact Cournot outsider support, public-private signatures, and sharp 3:1:2 welfare kink are already present.
- Otherwise freeze this model as a narrow comparative-institutional APPLICATION, or pivot to an economically substantive change (separately enforceable regulator and IP rights with asymmetric bargaining/credible outside options, rather than an arbitrary exact-match consent rule). Such a change requires a fresh Stage0/1 protocol and new proofs. Do NOT silently add new primitives to the current frozen theta model.
- Keep Draft PRs #22–#26 unmerged; create this audit as a separate Draft PR. Do not rewrite the manuscript or label submission-ready.

Reproduction: `code/stage6_reentry_generic_absorption.py`, dedicated Actions workflow to follow.
