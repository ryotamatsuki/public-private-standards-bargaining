#!/usr/bin/env python3
"""Check reproducible Stage7.5 decision inventory and exact branch demonstration.

Green CI is NOT Stage7.5 GO, source priority PASS, outside-model robustness, a
formal proof or an independent real-world microfoundation.
"""
from pathlib import Path
import subprocess
import json

root=Path(__file__).resolve().parents[1]
audit=root/"docs/audit"
files=[
"STAGE30G_THEORY_FREEZE_DECISION.md",
"STAGE30G_COMPLETENESS_CHECKLIST.md",
"STAGE30G_PRIMITIVE_AND_MICROFOUNDATION_CHALLENGE.md",
"STAGE30G_FRONTIER_INDEPENDENT.md",
"STAGE30G_README.md"
]
txt={f:(audit/f).read_text(encoding="utf-8") for f in files}
for f,s in txt.items():
    assert len(s)>1000,f
    assert not any(c in s for c in "\x08\x0b\x0c"),f
    assert "Stage30" in s or "Stage7" in s, f
ed=txt[files[0]]
assert "CONDITIONAL GO" in ed and "NOT FROZEN" in ed
assert "Stage7.5A" in ed and "UNRESOLVED" in ed
assert "Stage31" in ed or "submission" in ed
cl=txt[files[1]]
for x in ("## A.","## B.","## C.","## D.","## E.","## E2.","## F.","## G."):
    assert x in cl,x
for x in ("ESSENTIAL FOLLOW-UP","BOUNDED LIMITATION","FUTURE PAPER","CONDITIONAL GO"):
    assert x in cl,x
prim=txt[files[2]]
for x in ("O(0,0)",".07",".14","eta a","NOT VALIDATED","one"):
    assert x in prim,x
assert "NO DEFENSIBLE NEXT QUESTION FOUND" in txt[files[3]]
assert "Stage6" in txt[files[4]] and "UNRESOLVED" in txt[files[4]]
c=subprocess.run(["python","code/stage30g_boundary_inspect.py"],cwd=root,check=True,capture_output=True,text=True)
print(c.stdout,end="")
data=json.loads((audit/"STAGE30G_PRIMITIVE_BOUNDARY_RESULTS.json").read_text())
assert data["founder_outsider_cross_effect_jump"]=="7/100"
assert data["z_unchanged"]==["33/25","33/25","1"]
assert all(float(x)>0 for x in data["leading_principal_det_before"])
assert all(float(x)>0 for x in data["leading_principal_det_after"])
print("PASS: Stage7.5 A–G reports, exact primitive boundary and honest CONDITIONAL GO scope.")
print("NOT A FULL-PAPER FREEZE; THREE STAGE6 PUBLISHED PAPERS STILL DEFERRED.")
