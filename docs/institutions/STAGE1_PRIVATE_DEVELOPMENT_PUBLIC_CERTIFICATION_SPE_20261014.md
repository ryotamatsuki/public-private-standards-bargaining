# Stage 1 — Solved Sequential Development, Public Certification and Compliance Game
**2026-10-14 JST** | Stacked after Stage0 institutional regime comparison, Draft PR #29. This is a **subgame-perfect equilibrium (SPE) in an EXPLICIT sequential game**, not the prior reduced-stage-1 strong-Nash refinement. It is not a claim of unique strategies off path, continuous-depth optimization, or full endogenous formal/de facto standards competition.

## 1. Economic task and disciplined scope

**Question.** Can private firms freely develop and adopt a regional technology, anticipating that governments may certify/mandate expanded cross-border compatibility, and can a previously excluded third firm voluntarily comply and REENTER, with correct Cournot quantity responses? How does a change in original network strength alter the resulting perfect-information game?

Hold 5 of the 6 ORIGINAL scalar parameters fixed:
`(gamma0,kappa,eta,rho,phi)=(2/5,3/20,1/100,13/2,65/4)`;
vary only `v in [39/100,41/100]`. For this FIRST solved institution game, **standard depth is EXOGENOUSLY pinned at s=1** (development projects are discrete), in order to isolate institutional interactions. Firm proposal and licensing procedures are new DISCRETE protocol primitives, not a modification of Cournot utility or the six quantitative technology parameters. No invented subsidy, royalty or regulatory enforcement cost.

**Critical implementation assumptions (to avoid invented IP powers):**
- A previously developed compatibility interface is **open and lawfully implementable** in all 3 jurisdictions; the regulator cannot magically authorize patents, develop hardware, grant rights not actually available, or compel a loss-making firm to operate. The FIRST development/consortium action is necessary before certification: no R&D -> regulator has no interface to mandate.
- Bilateral private adoption makes F1 and F2 technically compatible and gives them the original productivity boost `z=1+rho s`; absent legal harmonization, F3 has not implemented mutual compatibility and cannot unilaterally cause both incumbent hardware protocols to become technically compatible. This is an explicitly restricted voluntary-consortium model, **NOT free individual adoption of open technology or de facto installed-base standard competition**.
- If all-country regulation is adopted, the previously available open interface is deployed to F3 upon F3's compliance; technical remapping of coefficients from RS `(b,d)` to IS `(b,b)` is the exact same previously frozen Cournot IS continuation. F3 pays the same real standardization fee `phi s²` as each already-implementing firm; F1 and F2 do not pay it TWICE. All operating firms may choose EXIT payoff 0 instead of negative net return. In the proven interval everyone complying with IS makes strictly positive net operating profit.
- Three regulators can only approve/mandate the available international upgrade of the developed interface. **Their available regulatory agenda, the one-firm proposer order and uniform-depth s=1 are exogenous rules.** The governments' eventual YES/NO is endogenous; the agenda/constitutional competence is not.
- Product-market competition is the unique Nash Cournot/KKT continuation with no collusion. Regulation is enforceable when enacted. Cost-free open licensing and complete commitment are *maintained assumptions*, not empirically established facts.

## 2. FULL explicit game tree and players' moves

1. **Private proposal:** F1 chooses `N` (do not develop), `R12` (develop bilateral interface with F2) or `I123` (develop shared interface with F2 and F3).
2. **Private voluntary adoption:** F2 chooses accept or reject the proposed R12/I123 project. If I123 is proposed and F2 accepts, F3 chooses accept or reject. A rejected proposal -> NS; accepted R12 -> provisional RS; accepted I123 -> provisional IS. No government signature is required to develop the provisional industry interface.
3. **Government standardization:** After observing R12, G1 then G2 then G3 each publicly votes YES or NO on compulsory *international* interface recognition and implementation in the 3 countries. The mandate is enacted iff ALL THREE vote YES. Otherwise original RS technology persists. After NS there is nothing technically available to certify; after IS the interface is already multilateral, so mandatory recognition is outcome equivalent and not needed.
4. **F3 independently chooses actual conformity/entry or exit after an enacted mandate:** If F3 complies, all 3 firms compete in IS; if F3 refuses, it exits, and the two incumbent firms compete under their same RS two-firm Cournot continuation. Incumbent firms may also exit instead of accepting a negative payoff; their payoff is always strictly positive in the audited domain, so all continue producing.
5. **Cournot production** is chosen independently in three identical segmented destinations. Consumers in each destination get LQ demand and welfare below. Firms have real adoption cost counted only once per producing adopter.

The vote is SEQUENTIAL (open ballot), not simultaneous. With strict preferences it eliminates the all-NO simultaneous-coordination trap at the government vote stage. Off-path voting histories still admit indifferent responses, so the result is an SPE **OUTCOME** classification, not a claim about every on/off-path individual strategy.

## 3. Identical original product-market primitives and unambiguous costs

Let `m=1-v,` `b=gamma0+(kappa-v)s,` `d=gamma0-eta s,` `z=1+rho s`.
The RS matrix (firms 1/2 developed together, F3 not mutually compatible) is
`M_R=[[m,b,d],[b,m,d],[d,d,m]]`, product-market Cournot FOC is `[M_R+diag(m,m,m)]q=(z,z,1)'`, with KKT `q3>=0`.
For `s=1`, `v in [.39,.41]`, RS outsider numerator `Y=2m+b-2dz=-3.3-3v<0`, so TRUE market RS output per destination
`q_R=(z/(2m+b),z/(2m+b),0)`.
The outsider does not participate, makes zero worldwide profit, and pays no standardization fee. Independent normalized product demand is `p=1-M_R q`.

For government-recognized international implementation, all firms use the *already developed and certifiable open* interoperability interface, `M_I=[[m,b,b],[b,m,b],[b,b,m]]`, all efficiencies `z`, and `q_I=(z/[2(m+b)])(1,1,1)'`. Each producing participant pays `phi s²` ONCE. Non-development NS has `M_N` with all off-diagonal `gamma0`, and `q_N=(1/[2(m+gamma0)])(1,1,1)'`. Each firm national total (3 segmented markets) `P_i=3m q_i²-phi s² I{implemented/complies}`. National home government welfare `W_i=P_i+(q'Mq)/2`. No licensing rents or transfer receipts exist.

Demand SPD and product substitution hold uniformly across `v in [.39,.41]`; exact rational Sturm root/sign tests certify all firm profitability, participation and welfare inequalities for the entire interval.

## 4. General within-benchmark SPE theorem: government intervention and private innovation

Set `u(v)=(11/20-v)/(1-v)`, and define the unique positive root `u*≈0.251570279593411` of `2u³+15u²+12u-4=0`.
Then `v*=(11/20-u*)/(1-u*)≈0.398741140643727`.

**THEOREM 1 (true backward-induction SPE outcome set; finite fixed-depth game):**
For every `v in [0.39,0.41]` strictly away from `v*`, the preceding sequential proposer–acceptor–unanimous-public-vote–compliance–Cournot game has the following **on-path subgame-perfect OUTCOMES**:

`0.39<=v<v*: private firms develop R12, all-country government IS mandate is blocked by incumbent government(s), and final standard is RS12 at s=1 (outsider zero).`

`v*<v<=0.41: firms develop R12 OR directly develop I123 (F1 is indifferent because any accepted R12 triggers regulatory upgrading); after R12 the governments each vote YES, excluded F3 voluntarily complies/enters, and final standard is IS at s=1 (three positive producers).`

At `v=v*`, some governments are indifferent about replacing private R12 with IS, allowing both final outcomes with appropriate credible continuation strategies. The final standard type is NOT unique right on the knife-edge.

**BACKWARD-INDUCTION proof skeleton.**
1. F3 conformity after public IS mandate yields `P_I>0=P_exit` throughout v domain; F1/F2 also have `P_I>0`. In response to unanimous public recognition, all 3 implement interface, with fully feasible IS Cournot equilibrium (no forced loss-making operation).
2. Each invited private participant accepts private IS because `P_I>P_N` throughout; F2 accepts private RS because eventual payoff is either `P_R` or `P_I`, both above NS. Thus credible private projects exist.
3. After provisional R12, excluded government's public welfare STRICTLY increases with IS, `W_{3,I}>W_{3,R}` throughout interval. Incumbent govs evaluate `W_I-W_R` and this sign is positive iff `v>v*`; negative iff `v<v*`. Exact rational polynomial real-root counting certifies a unique crossing. By sequential unanimous open ballots, all 3 governments YES iff v>v*; if any incumbent prefers R, the IS mandate fails.
4. F1 strictly prefers unregulated private R12 over private IS (P_R>P_I). If governments will not mandate, F1 proposes R12, thereby obtaining P_R>P_I>P_N. If they will mandate, private R12 is upgraded to IS, giving F1 P_I; direct private I also yields P_I. Both lead to the same final IS, above NS. This completes SPE backward induction.

**Note the narrow nature of the result:** stage 1's bilateral/private proposer protocol selects *the named R12 pair* for expositional convenience, unlike the perfectly symmetric simultaneous-announcement coalition game where any pair can be selected. Relabeling gives the same technology-type theorem for any named pair. Formal support-switch inference does NOT automatically extend to s∈(0,1] or to independently designed proprietary technologies; those require extra analysis.

## 5. Quantitative exact-rational illustrative witnesses

| outcome and v | v=39/100 | v=41/100 |
|---|---:|---:|
| NS firm P | 4575/10201 ≈ 0.4485 | 1475/3267 ≈ 0.4515 |
| Provisional RS incumbent firm P | 39995/1058 ≈ 37.8025 | 79165/1936 ≈ 40.8910 |
| IS compliant firm P | 321995/11858 ≈ 27.1542 | 162310/5329 ≈ 30.4579 |
| RS incumbent govt W | 128115/2116 ≈ 60.5458 | 62395/968 ≈ 64.4576 |
| RS outsider govt W | 48125/2116 ≈ 22.7434 | 45625/1936 ≈ 23.5666 |
| IS any govt W | 2857355/47432 ≈ 60.2411 | 2766605/42632 ≈ 64.8950 |
| RS outsider output per destination | 0 | 0 |
| IS outsider/newly adopting firm output per destination | 375/77 ≈ 4.8701 | 375/73 ≈ 5.1370 |
| Total W gain if IS is imposed instead of private RS | 925580795/25091528 ≈ 36.8882 | 435407785/10316944 ≈ 42.2032 |
| Government unanimous upgrade after R | NO | YES |
| Final SPE market type | RS | IS |

**Result 1 (conditional market-access complementarity).** Without private development, there is no available certifiable interface and public certification cannot induce IS. After private R12 development, public recognition opens F3 conformity and reentry, moving outsider quantity from 0 to `375/73>0` at v=.41, with all firms satisfying their compliance/exit incentives. This implements a genuine technology-availability and institutional-activation link **under the explicitly assumed open-interface technology**.

**Result 2 (economic conflict):** At v=.41, RS firm1 would have earned `79165/1936` absent regulation, but after public IS certification earns `162310/5329`, strictly less though well above its no-development payoff. National incumbent government welfare rises from `62395/968` to `2766605/42632`. Thus `[W_I-W_R]>0` for incumbent government whereas `[P_I-P_R]<0` for incumbent firm. Government recognition and private development complement public welfare, but public regulation displaces the private incumbents' preferred regional market standard. At v=.39 incumbent governments block this move, even though aggregate SUM of W across 3 states would rise by `925580795/25091528`. International collective-welfare efficiency is not equivalent to unanimous national regulatory adoption.

**Result 3 (genuine complementarity vs a zero-opportunity baseline).** Denote `D=1` a successfully developed private R12 interface, `C=1` a legally effective global certification decision (when available). With `D=0`, both C=0 and a proposed C=1 leave NS because no technology exists; with D=1, C=0 yields RS and C=1 (when F3 complies) yields IS. Accordingly the regulatory-development cross-effect for incumbent government is exactly
`[W(1,1)-W(1,0)]-[W(0,1)-W(0,0)]=W_I-W_R`;
positive at v=.41, negative at v=.39. For an incumbent F1 it is `P_I-P_R<0` at both parameter witnesses. This is a CONDITIONAL organizational complementarity result, *not* evidence that the underlying engineering innovation is supermodular. The interaction is partly generated by the legal feasibility gate. A technologically deeper model must separate different investments and their engineering productivity effects.

## 6. Model limits and further endogenous competition

**Not yet solved:** (a) original ENDOGENOUS continuous s; (b) all three private firms simultaneously free to innovate/adopt incompatible technologies without coordinated development contracts (de facto tipping); (c) competing proprietary unlicensable interface versus government open interface, possibly TWO standards coexisting and multiple technologies on the market; (d) dynamic installed-base network demand, switching cost, alternative royalties/IP licensing, real public enforcement/compliance costs, late adopter's conversion option; (e) agenda-setting by national regulators, non-unanimous jurisdictions, public regulator coalition size; (f) general six-dimensional analytic case partition. Do NOT label the current s=1 solution as the fully endogenous technology/recognition institution or a unique selection in all possible designs.

**Next precise stage** after this finite-game solution: allow s∈(0,1] in the F1 proposal and let regulators choose a standard depth `t<=s` compatible with available technology; solve the resulting global incentive and policy threshold regions. Then add a *separate legal IP action* (open-license vs proprietary) so a government cannot mandate a protected private standard without access; and permit a genuine public open alternative that competes with private proprietary technology rather than just replacing its accreditation.

## 7. Literature novelty control

Standard-setting bodies already voting then affecting market competition: Spulber (2019), *Standard Setting Organisations and Standard Essential Patents: Voting and Markets*, Economic Journal 129(619) 1477–1509, DOI 10.1111/ecoj.12606, https://academic.oup.com/ej/article/129/619/1477/5364896 . Its voting, scarce capacity, SEP licensing and market equilibrium create a serious full-game precedent threat. Government vs private market standard coordination: Belleflamme (2002), *Coordination on formal vs. de facto standards: a dynamic approach*, EJPE 18(1) 153–176, https://www.sciencedirect.com/science/article/abs/pii/S0176268001000738 . Gandal & Shy (2001), *Standardization policy and international trade*, JIE 53(2) 363–383, https://www.sciencedirect.com/science/article/pii/S0022199600000672 . Sector case of hybrid government/private standards: *Market- and committee-based mechanisms in the creation and diffusion of global industry standards: the case of mobile communication*, Research Policy 30(4) 589–610, https://www.sciencedirect.com/science/article/pii/S0048733300000950 . Legal caution: Japan Fair Trade Commission, patent pools and standardization restrictive practices, https://www.jftc.go.jp/dk/guideline/unyoukijun/patent.html and JPO SEP licensing negotiations, https://www.jpo.go.jp/system/laws/rule/guideline/patent/seps-tebiki.html .

**Research verdict:** conditional sequential SPE and market reentry are mathematically verified; this is a **scoped applied-institutional example**, not a newly established generic theorem about government forcing private patents nor journal novelty GO. Keep branch Draft and unmerged; retain all older manuscripts untouched.

**Exact reproducibility:** `code/stage1_endogenous_private_development_public_certification_spe.py` and `.github/workflows/stage1-endogenous-development-certification-spe.yml`.
