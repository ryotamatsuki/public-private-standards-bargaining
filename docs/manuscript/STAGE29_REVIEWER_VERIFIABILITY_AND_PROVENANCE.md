# Stage29 reviewer verifiability map and AI provenance

## Proof-critical claim dependency map

| Manuscript claim | Primitive inputs | Intermediate object | Key equation visible to referee | Full proof and code | Scope / blocker |
|---|---|---|---|---|---|
| All firms comply after M | Mandatory existing O(1,0), N pays K+phi/2, O pays missing c only, Cournot with exit | gross profit by 1/2/3 adopters | equations adoption-profits and adoption-margin | Appendix A continuing public, Stage15/20/25 | strict in certified baseline box; outside domain unresolved |
| 0/1 O investment: M | No compatible private cohort until second O | W_N gross, W_I net stock | delta_N, delta_O | Stage20; Appendix A; Stage25 strict wide margin | all legal single-O c,a |
| 2 O initial L-SPE impossible with A≥2 | pairwise minimum c,a; individual quadratic sunk capital, all gov can vote, Q=2 | unique high a/c redundant; low a vote B>0; high a -f_a>0 | Appendix two-investor formulas and 3D sign cert | Stage18/19/23/24/25; Appendix B | r≤2 only; continuous legal c,a |
| 3 O initial L-SPE impossible with A≥2 | pairwise min interfirm links, Cournot 3x3, sunk stock | tied high a/c; aligned/crossed technical order | aligned 2D²Delta2 polynomial; crossed 2D²Delta_i polynomial | Stage21/22/24/25; Appendix A/B | relies on YES ties; other government histories may fail M |
| Necessary A≥2 | legal proposal rights A and quorum r≤2, G1 outsider; bilateral optimum | outsider negative delta, member B>0; full initial deviations bounded | B,B,K_V-K; uniform founder/outsider bounds | Stage11/14/15/18/27; Appendix A | fixed 5 technology coefficients with eta/K rectangle; not all 7D necessity |
| RS persists under unanimity | outsider veto regardless proposal powers | member positive, outsider negative | (B,B,K_V-K) | Stage15/18/27 | three canonical pairs; not all investments classified in veto regimes |
| Welfare K_V<K_E<K_W | sunk K, phi c/a stock and public retrofit, private optimum a*>0 | B, KV, KE, KW | world ex ante vs observed ex post; KW-KE=phi a*² | Stage11/15/26; Appendix welfare bridge | only two specified paths; not first best |
| eta crossings | global private concavity and a*'(eta)>0 | cutoff derivative signs, rational root brackets | eq eta-order, exact rational intervals | Stage11/26 | eta/K rectangle, phi fixed |
| Seven-parameter SUFFICIENCY | private sign polynomial, positive determinants, bounds | tensor Bernstein coeff + symbolic structural zero identities, derivative norm | eq robustness box and Appendix Bernstein-transform | Stage24/25 | narrow explicit 7D box; NOT necessity |
| Literature contribution | prior institutional/standards theorem | exact alternate timing and mandate rules | limited overlap statement in sec robustness | Stage28 novelty audit | Gandal–Shy and Klimenko final proposition texts incomplete |

## Reproducibility and disclosure ledger

Provenance classification:
- AUTHOR: Must decide whether the game, assumptions and economic interpretations are appropriate and claim intellectual responsibility; author verification is NOT yet recorded.
- AI: Assisted in finding literature, designing revisions, mathematical exploration, producing natural-language English and proofreading, and writing code/scripts. Details logged by stages 19–29; do NOT characterize text as solely human-written.
- COMPUTATION: SymPy rational Bernstein/Sturm and distinct Cournot implementations reproduce sign claims. GitHub Actions passing certifies only the tests exercised.
- FORMAL: Full main theorem has NOT been independently machine-formalized in Lean. DO NOT claim Lean proof.
- EXTERNAL HUMAN: No independent external referee audit yet; human reviewer gate is PENDING, not PASS.

Stage29 writing process:
1. Freeze the Stage27 model and Stage28 novelty claim scope.
2. Draft the body in dependency order Model→Policy→Equilibrium→Welfare→Robustness→Conclusion; refine the Introduction after those dependencies.
3. Separate each major section and Appendix into independent .tex input files and preserve a single main.tex notation register.
4. Execute static theorem/label/citation gate and latexmk full compile; inspect PDF and references.
5. Conduct the Stage30 independent hostile referee reconstruction; unresolved external novelty priority must block Stage31 submission.

Current known blocking issues:
- Final published Gandal–Shy 2001 proposition and proof corpus not independently read.
- Klimenko 2009 complete numbered proposition and proof corpus not independently read.
- No author IP/accountability sign-off of final statement set.
- No independent external human mathematical/game-tree referee review.
- No journal-specific anonymous/submission requirements verified.
- Writing fluency and CI test passing do not close these gates.

Draft disclosure sentence (venue-specific wording must be approved by author): "Generative AI tools were used during literature discovery, mathematical exploration and verification-script development, and English manuscript drafting/editing. The author reviewed and takes responsibility for the model, mathematical claims, source citations, and final manuscript. Exact reproducibility code and its limitations are supplied with the paper." The author responsibility sentence must NOT be used in a submitted package until the author has actually completed those checks.
