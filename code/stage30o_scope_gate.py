#!/usr/bin/env python3
"""Stage30O source-inventory QA, not published-priority or formal-theorem verification."""
from pathlib import Path
import json,subprocess
from fractions import Fraction as Q
root=Path(__file__).resolve().parents[1]
d=root/"docs/audit"
names=["STAGE30O_UNPROMOTED_RESULTS_INVENTORY.md","STAGE30O_EDITOR_NOVELTY_ABSORPTION.md","STAGE30O_PROMOTION_EDITOR_DECISION.md","STAGE30O_README.md"]
x={p:(d/p).read_text(encoding="utf8")for p in names}
for p,s in x.items():
 assert len(s)>1700,(p,len(s))
 assert "Stage30O" in s,p
 assert not any(y in s for y in "\x08\x0b\x0c"),p
whole="\n".join(x.values())
for term in ["Stage26","Stage25","Stage16","Stage17","Stage11",
             "C1","C3","C5","C6","C7","Harstad","Celik","Jensen",
             "NOT", "UNRESOLVED"]:
 assert term.lower() in whole.lower(),term
inventory=x[names[0]]
for term in ["A1 |","A2 |","A3 |","A4 |","A5 |","A6 |","A7 |","A8 |","A9 |","A10 |","A11 |"]:
 assert term in inventory,term
for term in ["PR54","PR53","PR44","PR41","PR60"]:
 assert term in inventory,term
novelty=x[names[1]]
for link in ["10.1016/j.jinteco.2020.103392","10.1257/aer.97.3.871",
             "10.1016/0176-2680(95)00017-8",
             "10.1111/j.1530-9134.2005.00048.x"]:
 assert link in novelty,link
subprocess.run(["python","code/stage30o_rational_timing_spotcheck.py"],cwd=root,check=True)
r=json.loads((d/"STAGE30O_TIMING_RATIONAL_SPOTCHECK.json").read_text())
assert Q(r["eta"])==Q("0.115") and Q(r["K"])==Q("0.55")
assert Q(r["at_lower"]["KE"])<Q(r["K"])<Q(r["at_lower"]["KW"])
assert Q(r["at_upper"]["KE"])<Q(r["K"])<Q(r["at_upper"]["KW"])
print("PASS: Stage30O eleven research clusters, source-scoped novelty ledger, exact rational timing witness.")
print("NOT VERIFIED: journal priority, transfers full-game SPE, seven-parameter main C1/C6, source complete proofs, Lean.")
