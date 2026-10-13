# Stage 4 — Solved 3-country composite model: scoped GO to independent hostile audit
2026-10-13 | CANONICAL construction verdict for THIS SEPARATE NEW SOURCE-MODEL BRANCH: GO → Stage 4A (construction-level ONLY; not new-theory certification). The previous NO-GO for fixed-menu veto game stands unchanged.
Purpose: actually solve endogenous common-platform depth + own-network benefit + cross-network compatibility + differentiated Cournot + public/private one-shot approval.

## Mathematical outputs
See docs/composite/MODEL_AND_EXACT_SOLUTION.md for source primitives, formulas and proof. Exact SymPy and separately coded standard-library Fraction Gaussian payoff verification in code/verify_composite_depth.py:
- 3 firms in EACH of 3 destination markets; government welfare includes own CS and worldwide domestic profit, real R&D setup deducted once.
- All SPD/interiority/FOC/SOC and 3-country symmetric bilateral club continuation explicitly solved.
- Member x(s)=8(9s+31)/(18s+713), outsider y(s)=4(62-3s)/(18s+713).
- Participant P''(s) and W''(s) strictly negative throughout [0,1], shown with factored polynomials with positive coefficients.
- Unique firm optimum 0.4753<sF<0.4754; unique government optimum 0.7437<sG<0.7438. Verified exact-rational root bracketing, plus direct independent fraction payoffs.
- One-shot exact contract-unanimity results for three symmetry-related clubs: firm-only stable depth sF; government-only sG; joint government + firm stable agreement depth interval [sF,sG]. Null agreement is Nash but not strong Nash. Coalition identities remain symmetric/multiple.
- Outsider quantity and profits decrease with deeper member standard; outsider nation welfare separately evaluated (it may rise because of CS). No unique negotiated depth or country pair.
- Real marginal cost savings c(s)=c0-hs and convex real integration costs f s² are transparent newly justified STYLIZED assumptions, not disguised inherited Stage1 primitives.

## Exact proof notes
For bilateral member quantities x and outsider y:
M= [[m,b,g],[b,m,g],[g,g,m]], m=1-v, b=g+(κ-v)s. Cournot B=M+mI, RHS (a-c0+hs, a-c0+hs, a-c0). Solve symmetric x,y system. Global Cournot uniqueness due positive-definite B; KKT correct for all three strictly positive witness outputs over [0,1]. The member production first order payoffs are m x² per destination (FOC margin identity). Thus P=3mx²-fs², CS=1/2 q'Mq, W=P+CS.

For benchmark a=1,c0=h=f=1/5, v=1/10, γ0=1/4, κ=3/20, P'' and W'' have negative rational polynomial forms with all positive coefficients. Their derivatives have opposite signs at s=0 vs s=1. The bounded roots are ordered sf<sg and matched-contract signers have strict gains relative to SQ. Since P increases on [0,sF], decreases on [sF,1], and W increases on [0,sG], decreases on [sG,1], the Pareto-frontier interval is exactly [sF,sG]. Any competing bilateral coalition shares a government AND firm of one country; they cannot both strictly gain from an alternative depth because original depth is Pareto efficient. Therefore exactly all perfectly matched club-depth profiles in this interval are strongly Nash-stable. The generic exact-matching game additionally has many Nash equilibria including no agreement.

## Baseline comparisons / validity threats
- Firm only: sF; government only: sG; combined: interval (new set from two veto classes, but generic Pareto logic).
- Deleting κ=0 or v=0 separately: changes comparative statics and group optima, but no indispensable 3-channel nonseparability theorem was proved. Contrast source family Ghosh–Morita, Bourreau–Doğan, Economides–Skrzypacz.
- Cost-saving benefit h and real fixed cost f directly make interior s possible; simply declaring the interior stationary condition to be new would fail economic significance/novelty review.
- Novel political-economy theorem NOT proved; no general asymmetric equilibrium characterization, no group coalition membership mismatch, no royalty r.
- One-sided multiple contract match and strong Nash outside this paired bilateral exclusive exact-consent game remain UNRESOLVED. No external human referee; independent Fraction method is an AI-written clean-room calculator, not independent human certification.

## Preliminary candidate theorem-certificate ledger
C1 (known mathematical): if M SPD and B=M+diag(M)>0, Cournot complementarity has unique solution; PROVED conditional and benchmark.
C2 (standard-derived): exact member/outside quantities and welfare; PROVED FOR 3-market symmetric club.
C3 (bounded example): P and W have strict concave distinct interior maxima with exact rational brackets; EXACT SYMBOLIC PROOF.
C4 (bounded equilibrium correspondence): firm-only sF, govt-only sG, joint group stable [sF,sG] under stated one-shot protocol; ANALYTIC ARGUMENT + numeric inputs, READY FOR STAGE4A attack. New mathematical contribution NOT ESTABLISHED.
C5 (global novelty): original theorem beyond Hart–Kurz + Bourreau–Doğan + Economides? UNPROVED / DO NOT CLAIM.
Next: Stage4A independently try to falsify C4 and full coalition deviations, then Stage6 actual theorem absorption, no full manuscript until all gates.
