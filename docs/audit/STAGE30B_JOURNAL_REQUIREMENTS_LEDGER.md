# Stage30B — Initial journal requirements ledger: JPET

Date checked: 2026-10-14 UTC. Provisional target:
**Journal of Public Economic Theory, Original Article**.
This is a Stage12-style evidence baseline, not a compliant submission package.
The original manuscript has not been changed. No portal was initialized, no
editor contacted, and no submission made.

## Evidence and status meanings

Workflow authority:
[Journal Requirements Evidence Checklist](https://github.com/ryotamatsuki/research-paper-workflow/blob/81c37dd95fc93d918138ba9d0da86541d3cc1067/checklists/JOURNAL_REQUIREMENTS_CHECKLIST.md).

Sources read live:

- **J1, level3** — current journal-specific
  [Author Guidelines / forauthors.html](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/forauthors.html).
  Sections: Submission and Peer Review; Main Text File; LaTeX; Peer Review;
  Ethics; Article Types. Includes Research Exchange routing.
- **J2, level3** — coexisting journal-specific
  [Instructions to Authors / guide.htm](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/guide.htm).
  Includes ScholarOne routing and manuscript highlights. Treat as a legacy-looking
  source, not proof of current authenticated fields.
- **J3, level3** — journal
  [Overview / Aims and Scope](https://onlinelibrary.wiley.com/page/journal/14679779/homepage/productinformation.html).

Every item below has the same access date above. `PASS` means that the stated
public rule was found, **not** that the Stage29 manuscript satisfies it.
`UNVERIFIED` means an operative rule or actual file/portal reconciliation remains
unknown. `CONFLICT` preserves competing instructions; it is not silently resolved
by a portal accepting a file. No authenticated portal evidence (level2) or direct
editorial instruction (level1) has been obtained.

## Initial requirements ledger

| ID | Topic | Source / level | Operative baseline / uncertainty | Affected artifact or action | Status / verification |
|---|---|---|---|---|---|
| R01 | Journal / article identity | J1/J3, 3 | Wiley / JPET; Original Article for new research | Submission category, title page | PASS: public pages |
| R02 | Submission route | J1 vs J2, 3 | Research Exchange versus ScholarOne | Future submission record | CONFLICT: provisional J1 route; confirm live before submission |
| R03 | Review model / names | J1, 3 | Single anonymized; identified main text | Main PDF, metadata, acknowledgments | PASS: public rule; package untested |
| R04 | Title-page contents | J1, 3 | Author affiliations, emails and relevant declarations | Title page / main PDF | PASS: public rule |
| R05 | Separate title-page file | J1, 3 | Required file designation not established | Title-page upload | UNVERIFIED: portal preflight |
| R06 | Corresponding author / ORCID | J1, 3 | ORCID required; exact corresponding-author placement/fields untested | Title page, account/metadata | UNVERIFIED for full reconciliation |
| R07 | Initial main-file formats | J1, 3 | LaTeX, LyX, PDF or Word | Peer-review PDF or source submission | PASS: public rule; actual portal designation untested |
| R08 | Initial editable source | J1, 3 | PDF is an explicitly allowed initial format; portal required-source fields untested | Main file / future source bundle | PASS for public PDF permission; live field check remains |
| R09 | LaTeX upload dependencies | J1, 3 | Choosing .tex also requires review PDF and supporting files | .tex, PDF, bibliography, figures, packages | PASS: public rule |
| R10 | Source archive / folders | J1, 3 | Archive and folder restrictions not established | Clean source package | UNVERIFIED: do not assume ZIP layout |
| R11 | Abstract / keywords | J1, 3 | Abstract ≤250 words; ≤7 keywords; structured-abstract wording present | Abstract / metadata | PASS for public limits; exact structured-heading handling UNVERIFIED |
| R12 | Page / word limit | J1/J3, 3 | No operative full-article limit established | Main PDF | UNVERIFIED; absence of a limit on page is not proof of no limit |
| R13 | JEL / highlights / reviewers | J2, 3; J1 silent | Old page has JEL, 1–4 highlights, reviewer fields | Metadata / ancillary files | UNVERIFIED for current portal; do not import old fields as current obligations |
| R14 | Template / references | J1, 3 | Free Format; consistent references; NJD template recommended | .tex, references.bib | PASS: public rule; not a mandatory template claim |
| R15 | Figures / appendices separately | J1, 3 | Combined main-file permission coexists with separate-file wording | Review PDF + separate exhibits/appendix | CONFLICT: prepare separate files; reconcile initial upload rules live |
| R16 | Artwork specifics | J1 links, 3→4 | Source formats/resolution/font requirements not fully checked | SVG generator, export PDF/EPS/TIFF as appropriate | UNVERIFIED: current target-specific artwork QA at Stage14 |
| R17 | Supplement / code / certificates | J1, 3 | Supporting information separate; proof/code-specific obligations unestablished | Appendix, reproducibility archive, repository links | UNVERIFIED for exact required package |
| R18 | Data availability | J1, 3 | Statement required; data sharing expected | Statement covering code/generated evidence and absence of empirical data | PASS: rule; author statement not yet verified |
| R19 | Funding / conflict / ethics | J1, 3 | Appropriate declarations, funding acknowledgments, conflicts | Title page, acknowledgment, declarations | PASS: public rule; content pending author evidence; no invented funding/IRB claim |
| R20 | CRediT / contribution fields | J1, 3 | Exact current requirement not established | Author contributions, portal fields | UNVERIFIED |
| R21 | Material AI assistance | J1, 3 | Disclose manuscript-development use in Methods or Acknowledgments; human accountability | Research-method/provenance disclosure, manuscript-preparation statement if required | PASS: rule; final disclosure/content reconciliation pending |
| R22 | Preprints / other publication | J1, 3 | Preprints allowed; simultaneous journal consideration not allowed | Preprint links, prior-publication declarations | PASS: public rule; actual project attestations pending |
| R23 | Submission fee | J1, 3 | No submission fee | Future submission charge | PASS: public rule |
| R24 | OA / other author charges | J1, 3 | Subscription with optional OA after acceptance; APC amount/waivers and other charges not checked | Access/license choice | UNVERIFIED for financial terms; optional OA not called mandatory |
| R25 | Author sign-off / disclosures | J1, 3; workflow | Genuine author approval and truthful verification actors required | Author contribution record, exact final PDF | UNVERIFIED: AI/code success does not close this |
| R26 | Authenticated required fields | No level2 source | Exact account, file labels, required attestations unknown | Actual submission record and generated PDF | UNVERIFIED: not accessed in this planning task |

## Conflicts and conservative handling

R02 is a real coexistence of official instructions: J1 specifically directs new
submissions and revisions to Research Exchange; J2 still directs submissions to
ScholarOne. The initial planning choice follows J1's explicit new-submission
instruction, but the future actual portal/editorial evidence must resolve the
operative route. No account or manuscript record is created now.

For R15, supply independently usable figures and a separately identifiable
Appendix in the preparation plan while keeping a readable manuscript-facing
proof chain. This conservative package design does not prove which files the
actual initial submission requires. The journal page's permission to embed
figures does not settle every separate-file instruction.

The publisher-style structured-abstract wording is retained as observed. Recent
published examples using conventional abstracts are not a higher authority than
the journal's instructions. Confirm the operative presentation at Stage14 rather
than declaring the wording irrelevant.

An extensive AI contribution to derivation, audit, source assessment and proposed
exposition must not be described as spelling correction alone. The declaration
must match the existing records and distinguish AI, computation, formal proof,
author verification and external human review. No new authorship/verification
attestation is inferred here.

## Stage13/14 handoff

Theoretical certification and a new manuscript/referee gate come first. For a
later JPET integration, inherit R01–R26, preserve the unresolved items, and map
each resolved rule to the actual file or metadata field. Refresh all rules live
at Stage14, inspect the authenticated required fields and journal-generated PDF,
and resolve material conflicts by the appropriate current authority. Obtain
editorial clarification only if still needed at that point; this planning task
does not authorize unsolicited messages to editors.

**No SUBMISSION QA PASS:** material UNVERIFIED / CONFLICT entries remain, the
package has not been tested, and the earlier theory/novelty gates are open.
These operational unknowns do not by themselves reverse the provisional JPET
readership recommendation.
