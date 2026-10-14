# Stage 14 — Minimal mechanism / legal-IP / governmental veto adversarial audit

**2026-10-14.** Parent: Stage12–13 Draft PR #41. **Conclusion: significant causal attribution correction.** The existing RS/IS full-continuous SPE coexistence and conditional welfare frontier should NOT be attributed uniquely to proprietary patents, a recognition-C instrument, or governmental unrestricted technical-depth optimization. Distinct national government incentives and adoption costs must be separated.

## 1. Confirmed exact theorem on the whole 2D economic rectangle

Keep Stage11 original five physical coefficients fixed:
`(v,gamma0,kappa,rho,phi)=(.01,.14,.02,.32,.14)`.
Let outsider differentiation `eta in [.10,.14]`, capital setup `K in [.54,.56]`. From prior private global FOCs, `a_R*(eta) in (.25,.61)`; audit ALL possible real eta,a values in the LARGE rectangular enclosure, not just privately chosen roots.

At private RS(1,a) the Cournot outputs are
`x=(2m(1+rho)-d)/D`,
`y=(2m+b-2d(1+rho))/D`,
`m=1-v; b=gamma0+kappa*a-v; d=gamma0-eta*a`,
`D=2m(2m+b)-2d²`.
Per incumbent's K-unadjusted private payoff `f=3m*x²-phi*(1+a²)/2`; outsider `P_O=3m*y²`; each country's CS `(m+b)x²+2d*x*y+m*y²/2`.

Write `W_I^0` for full IS(1,0) per-government payoff after public variable installation `phi/2` BUT before initial public setup fee K.

**Proposition ST14-1 (TWO independent national barriers)**:
For ALL real `eta in [.10,.14], a in [.25,.61], K in [.54,.56]`, the following THREE strict inequalities hold simultaneously:
1. Outsider G3 refuses public IS even if private RS were OPEN:
`P_O+CS_R-[W_I^0-K]>0`.
2. If incumbent private design X is a technically/legally **incompatible proprietary family**, each incumbent G1/G2 refuses replacement by newly installed public O(1,0) because their old X investments are sunk and they must pay for a NEW O family:
`f+CS_R-W_I^0+K+phi*(1+a²)/2>0`.
3. If the same observed private RS design instead belongs to the same legally open family O(1,a), the incumbent G1/G2 EACH STRICTLY PREFERS a mandate of public O(1,0), because the capitalized O→O downgrade costs zero and prior overinvestment in a is sunk:
`W_I^0-phi*a²/2-f-CS_R>0`.

**Independent exact proof:** Map `eta=.10+.04t`, `a=.25+.36u`, t,u∈[0,1]. Convert each government welfare margin to one ratio of EXACT integer-coefficient bivariate polynomials. Numerator AND denominator both have degrees (4,4), with **25 of 25 Bernstein basis coefficients STRICTLY POSITIVE** for EACH inequality; no numerical sampling or interval sampling. At larger K, outsider/closed incumbent veto margins weakly increase; open incumbent approval margin is K-independent. Executable source `code/stage14_institutional_veto_ablation.py`.

At diagnostic eta=.14, K=.55, a=.595 (the rational isolating approximation of privately optimal a*≈.5949515085):
| National W | status quo RS | after IS mandate | choice |
|---|---:|---:|---|
| incumbent after proprietary X adoption | ≈1.021047 | ≈0.417686 | VETO |
| incumbent after open O adoption (counterfactual history) | ≈1.021047 | ≈1.037686 | APPROVE |
| outsider G3 | ≈1.218883 | ≈1.062463 | VETO |

The EX POST mandate policy L thus persists after the hypothetical change X→O because G3 alone vetoes it, **despite** incumbent support. This is a statement about the **government subgame after a specified private standard history**. We have **NOT** established that initial O12N is a true SPE of the full 3-firm game: all new private deviations must still be verified.

**Economic interpretation:** “sunk proprietary lock-in causes the government's failure to implement IS” is INCOMPLETE for the now-central Stage11 rectangle. `G3`'s endogenous policy demand is a separate sufficient explanation: the outsider country gains from its product's distinctiveness under RS. This is the concrete political-economy mechanism activated by Ghosh–Morita differentiation in the user-preferred theorem.

## 2. Institutional machinery ablation: what is actually causal?

**C (private firm recognition/certification):** Both existing candidate SPE equilibrium paths are RS(X,X,N)→G:L and IS(N,N,N)→G:M→all comply. C is not even feasible on those histories since no privately developed open O reference exists. The original all-continuous deviation arguments upper-bound the deviator's payoff under EACH possible L/C/M continuation, often without selecting a particular C adoption Nash. Thus, *conditional on those earlier complete global bounds*, deleting the policy C reduces government options and does NOT create new profitable deviations. Both constructed EXISTENCE examples also hold in the REDUCED L/M-only game. This does NOT mean C is universally irrelevant in all equilibria or industries.

**Endogenously chosen public cP,aP:** The Stage10 government globally selects its ideal public specification (1,0) along both established equilibria. If government may only mandate the legally pre-existing **SINGLE** public O(1,0), then onpath government choice is unchanged. Since the earlier firm unilateral-deviation profit bounds hold for ANY approved public specification, the bound remains valid when the set shrinks. Therefore endogenous public technical-depth selection is NOT NECESSARY to obtain THESE SPECIFIC RS/IS coexistence outcomes. It remains a possible separate thesis requiring another counterfactual in which government optimal public depth is interior or state-dependent.

**X/Y intellectual property:** The original Stage5 source allows any firm to select X/Y labels independently, despite calling them proprietary; legal authority to use X/Y patents was never separately modeled. The entrant firm F3 is ALREADY unprofitable from joining incumbent private X even when entry/technology licence price is zero, because uniform Cournot bound `q3<.6` yields gross profit ≤1.0692 and setup K≥.54 gives ≤.5292 while remaining outsider's profit >.547893 in the Stage11 rectangle. Hence adding a nonnegative licence royalty `tau>=0` charged ONLY to a newcomer would not turn that particular deviation profitable. **DO NOT claim** that a fully endogenous excludable patent licensing game, founder/entrant title assignment or royalty redistribution have been proven SPE-stable: these are new actor actions, and governmental W and later licensing incentives must be recomputed.

**Government veto and outsider benefits:** Unlike C and freely chosen public depth, the national unanimity rule and outsider payoff enter government selection crucially. A clear follow-on counterfactual is to remove the outsider G3 veto (majority or incumbent-only approval), separately with X and O technologies, and then classify changed SPE outcomes. The model should distinguish the private firm's initial technology choice from the DIFFERENT GOVERNMENT whose national welfare prevents switching.

## 3. Research GO/NO-GO and model minimization

A serious adversarial novelty implication: two of the supposedly essential original policy options, government C and a continuum of publicly supplied designs, are NOT NECESSARY for the currently proved central coexistence and conditional welfare-ranking reversal. Therefore stating that all six player's complete policy richness is uniquely responsible for this result would be misleading. The most economical manuscript model should initially retain:

- 3 independently acting firms; private common product design a and interface c; regional compatibility cohort vs outsiders; Cournot competition
- Real setup capital K, differentiated adoption/retrofit costs
- 3 nationally self-interested governments, with sequential approval/veto of **a single feasible public O(1,0)** rather than an overcomplicated continuum of government-designed public technical standards
- Private bilateral RS versus public universal IS as two distinct subgame-perfect paths, with nonmember G3 policy veto and privately optimal positive a_R*(eta).

Put private C recognition and endogenous public cP,aP in extension/appendix **only if** they produce additional distinct testable predictions. This simplification is a concrete outcome of a causal ablation, not merely an editorial opinion.

This is **not** an academic originality GO: coalition differentiation (Ghosh–Morita 2012), endogenous R&D differentiation thresholds (Gil Moltó et al 2005), open vs proprietary coalition stability (Lukach et al 2007), region-wide/public standards and government welfare (Takarada et al 2020), and installed-base compatibility (Farrell–Saloner 1985/1986) all pose prior-art threats. Remaining contribution candidate = endogenous outsider-competition-induced *veto alignment* plus different privately chosen standard coalitions and identical public mandate availability causing coexistence and comparative institutional inefficiency. Requires theorem-level comparator and new full offpath legal-IP game if retained.

## 4. Reproducibility and boundaries

- `code/stage14_institutional_veto_ablation.py`: independent exact rational SymPy, 3x25+3x25 strict Bernstein coefficient proof. It does NOT import Stage5 and does not discretize eta/a.
- `.github/workflows/stage14-national-veto-institutional-ablation.yml`: continuous veto proof CI.
- The downloadable model audit report accompanying the source conversation contains additional distinctions and numeric corroboration.
- Prior Stage12/13 partial state retained; no research manuscript changed and no PR merged.
- Full five-market-parameter ±2% SPE coexistence theorem NOT completed; Stage12/13 proved the conditional WELFARE frontier but did not prove all offpath SPEs. New legal property-rights equilibrium, public technology procurement cost, historical R&D investment rights and arbitrary-majority-vote regime remain for later work.

## 5. Direct prior-art correction: outsider veto is NOT independently novel

The publisher's original text of **Takarada, Kawabata, Yanase & Kurata (2020), _Standards Policy and International Trade: Multilateralism versus Regionalism_, Journal of Public Economic Theory 22:1420–1441, DOI 10.1111/jpet.12425** explicitly states that when cross-border externalities are substantial, the single **nonmember** country can prevent multilateral harmonization from being in the core. Its model deals with mandatory product/process standards, consumption externalities, real implementation costs, three countries and coalition blocking. Its solution concept is the **core**, not the six independent actors' full SPE, and its outsider-harm channel is distinct in primitives from endogenous firm product common-design differentiation here; nonetheless the headline “an outsider country blocks multinational standards” is prior art, NOT novel. https://onlinelibrary.wiley.com/doi/10.1111/jpet.12425 .

**Further adversarial conclusion:** after this source check neither (i) generic private endogenous differentiation thresholds (Gil Moltó et al. 2005), nor (ii) collaborator-outsider differentiated competition (Ghosh–Morita 2012), nor (iii) outsider veto of multilateral harmonization (Takarada et al. 2020), nor (iv) public vs proprietary standard coalition multiplicity (Lukach et al. 2007) can stand independently as originality claims. The remaining candidate must demonstrate a mathematically NONREDUNDANT cross-interaction: endogenous `a_R*(eta)` *changes governmental VETO regions and welfare ranking while government/investment timing jointly supports separate IS/RS SPE outcomes*. The minimal version should be formally compared theorem-by-theorem with the above work BEFORE a novelty GO. The current Stage14 proves policy preference signs and demonstrates **C and full government public-depth action menus are nonessential** on the proven trajectories, which makes model simplification more pressing than extension.
