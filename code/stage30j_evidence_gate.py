#!/usr/bin/env python3
"""Stage30J documentary inventory ONLY, not literature-priority certification."""
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"docs/audit"
files=[
"STAGE30J_NEW_PARENT_THEOREM_COLLISIONS.md",
"STAGE30J_EDITOR_NOVELTY_DECISION.md",
"STAGE30J_SOURCE_VERSION_LEDGER.md",
"STAGE30J_README.md"]
d={f:(p/f).read_text(encoding="utf-8") for f in files}
for f,x in d.items():
 assert len(x)>1000,f
 assert "Stage30J" in x,f
 assert not any(ch in x for ch in "\x08\x0b\x0c"),f
combined="\n".join(d.values())
for word in ["Buccella","Nabin","Chou","Barrett","Takarada","Bordignon"]:
 assert word in combined,word
a=d[files[0]]
for i in range(1,8):
 assert f"C{i}" in a, i
for term in ["Proposition 1","Propositions 1–3","UNRESOLVED","DIRECT","POSSIBLE"]:
 assert term in a,term
e=d[files[1]]
for term in ["CONDITIONAL GO","NO-GO","Lean","C1","C5","C6","NOT","Barrett"]:
 assert term in e,term
v=d[files[2]]
for doi in ["10.1007/s00712-023-00834-x","10.1111/ijet.12374",
 "10.1016/S0022-1996(00)00082-9","10.1016/S0022-1996(00)00067-2",
 "10.1016/j.jinteco.2008.08.005","10.1016/j.jpubeco.2006.02.001"]:
 assert doi in v,doi
assert "four" in v.lower()
print("PASS: documentary novelty-collision ledger and source-version limitations present.")
print("NOT TESTED: actual originality, unavailable printed proofs, journal priority, C1–C7 mathematical proof or Lean.")
