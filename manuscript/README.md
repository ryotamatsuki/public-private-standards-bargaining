# Stage29 English manuscript

The manuscript is an anonymous full DRAFT for the restricted three-country OPEN/N standards model. It is not a submission-frozen article.

Main.tex assembles eight sections, two technical appendices, and the verified-reference BibTeX file. Every major section is stored separately in sections/; proofs in appendix/.

## Build

In manuscript/ run:

    latexmk -pdf -file-line-error -halt-on-error -interaction=nonstopmode main.tex

For cleanup, run: latexmk -C main.tex

A GitHub Actions build runs the full PDF, checks citations and equation references, and uploads an artifact. The static manuscript gate also tests main-tex section inventory and conservative terminology.

## Scientific scope

The main two-agenda-government iff result is a pure-strategy SPE terminal-outcome theorem at fixed baseline technology for all eta∈[0.10,0.14], K∈[0.54,0.56], across ALL admissible real initial investments N or O(c_i,a_i), 0<=a_i<=c_i<=1. It is not initial investment uniqueness or mixed-strategy characterization. The seven-parameter box certifies SUFFICIENCY of the public terminal outcome for >=2 agenda governments with <=2 required YES votes, not a seven-dimensional necessary-and-sufficient region.

World welfare ex post after regional investment is sunk differs from world welfare ex ante comparing initial public and regional investment paths. The three veto/ex-post/ex-ante thresholds must never be confused.

## Stage30 blockers

- Independently examine the FULL propositions and proof appendices of Gandal–Shy (2001) and Klimenko (2009) and confirm Ruiz working-paper bibliographic details.
- Independently reconstruct the game-tree and asymmetric two/three-firm global no-L-SPE proofs from the manuscript-facing equations, not the same analysis code.
- Author sign-off for mathematics, citations, AI use and the final PDF.
- Final submission-journal requirements, anonymous metadata and copyright/license disclosure.
- Source-level LaTeX compilation is not a human peer-review or originality certification.

No older Draft PRs have been merged and no journal submission has been undertaken.
