#!/usr/bin/env python3
"""Stage30F evidence and document inventory; not journal/source/novelty proof."""
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parents[1]
audit=root/"docs/audit"
docs=[
"STAGE30F_WELFARE_ACCOUNTING.md",
"STAGE30F_INSTITUTIONAL_VALIDITY.md",
"STAGE30F_GENERALITY_AND_NEGATIVE_DIAGNOSTICS.md",
"STAGE30F_EDITOR_DECISION_AND_TRIAGE.md",
"STAGE30F_README.md",
]
text={s:(audit/s).read_text(encoding="utf-8")for s in docs}
for s,v in text.items():
    assert len(v)>1000,s
    assert not any(ch in v for ch in "\x08\x0b\x0c"),s
    assert "Stage30" in v or "Stage7" in v,s
v=text["STAGE30F_WELFARE_ACCOUNTING.md"]
for t in ["C1","C2","C5","C6","K_W","post","ante"]:
    assert t in v,t
v=text["STAGE30F_INSTITUTIONAL_VALIDITY.md"]
for t in ["ISO","ITU","EU","2022/2380","O(0,0)","2026-10-15","NON"]:
    assert t.lower() in v.lower(),t
v=text["STAGE30F_GENERALITY_AND_NEGATIVE_DIAGNOSTICS.md"]
for t in ["g=.04","all-NO","NOT CERTIFIED","MODEL/INSTITUTION","NOT"]:
    assert t.lower() in v.lower(),t
v=text["STAGE30F_EDITOR_DECISION_AND_TRIAGE.md"]
for t in ["CONDITIONAL PASS","ESSENTIAL EXPLANATORY","C1","C7","Stage7.5","Stage31"]:
    assert t in v,t
assert "UNRESOLVED" in text["STAGE30F_README.md"]
assert "CONDITIONAL" in text["STAGE30F_README.md"]
r=subprocess.run(["python","code/stage30f_welfare_reconciliation.py"],cwd=root,check=True,text=True,capture_output=True)
print(r.stdout, end="")
import json
j=json.loads((audit/"STAGE30F_WELFARE_RECONCILIATION.json").read_text())
assert len(j["samples"])==3
assert all(p["founder_support"] and p["outsider_veto"] for p in j["samples"])
assert j["samples"][0]["gap_private_minus_public_decimal"]<0
assert j["samples"][1]["gap_private_minus_public_decimal"]>0
print("PASS: Stage7 report inventory + exact rational accounting samples.")
print("No claim of formal certification, published priority, institutional match or original-draft readiness.")
