#!/usr/bin/env python3
"""Stage30I preflight: scope data + finite Fraction witnesses, NOT formal proof."""
from pathlib import Path
import json
import subprocess

root=Path(__file__).resolve().parents[1]
audit=root/"docs/audit"
filenames=[
    "STAGE30I_CLAIM_SCOPE_AND_QUANTIFIERS.md",
    "STAGE30I_PRELIMINARY_FORMALIZATION_TARGETS.md",
    "STAGE30I_PREFLIGHT_DECISION.md",
    "STAGE30I_README.md",
]
data={f:(audit/f).read_text(encoding="utf-8") for f in filenames}
for name,txt in data.items():
    assert len(txt)>1000,name
    assert all(ch not in txt for ch in "\x08\x0b\x0c"),name
    assert "Stage" in txt,name
x=data[filenames[0]]
for c in range(1,8):
    assert f"### C{c} " in x,c
for required in ["K>V","F(c,a;\\eta)\\ge P","O(0,0)","unrestricted","infimum","supremum"]:
    assert required in x,required
y=data[filenames[1]]
for c in range(1,8):
    assert f"C{c}" in y,c
for term in ["P0/A","P0/B","P0/C","P0/D","NOT STARTED"]:
    assert term.lower() in y.lower(),term
contract=json.loads((audit/"STAGE30I_SCOPE_CONTRACT.json").read_text(encoding="utf-8"))
assert contract["schema"]=="stage30i-preflight-v1"
assert contract["stage75a"]=="NOT OPEN / NOT EXECUTED"
assert contract["formal_status"]=="APPLICABLE / NOT STARTED"
assert contract["economic_scope"]["eta"]==["1/10","7/50"]
assert contract["economic_scope"]["K"]==["27/50","14/25"]
assert len(contract["claims"])==7
assert [x["id"] for x in contract["claims"]]==[f"C{i}"for i in range(1,8)]
for claim in contract["claims"]:
    assert claim["formal_priority"] in ("P0","P1","P2")
    assert all(c in ("MODEL-SPECIFIC","INSTITUTION-SPECIFIC") for c in claim["classification"])
    assert claim["quantifier"] and claim["dependencies"] and claim["signs"] and claim["not_claimed"]
assert "K>V" in contract["claims"][0]["signs"]
assert "F>=P" in contract["claims"][0]["signs"]
assert "unique maximizing (c,a)" in contract["claims"][4]["signs"]
assert "published" in contract["novelty_certification"].lower()

result=subprocess.run(["python","code/stage30i_preformal_scope_witness.py"],
    cwd=root,capture_output=True,text=True,check=True)
print(result.stdout,end="")
w=json.loads((audit/"STAGE30I_PREFORMAL_RATIONAL_RESULTS.json").read_text())
assert w["scope"]["policy_sign_tie_cases"]==567
assert w["one_strict_inclusion_witness"]["only_existential_strictness"] is True
assert w["not_certified"] and len(w["not_certified"])>=7
assert w["witnesses"]["low_private"]["private_minus_public_decimal"]<0
assert w["witnesses"]["high_private"]["private_minus_public_decimal"]>0
print("PASS: 7-claim preformal contract and finite rational scope witnesses.")
print("No Lean source, no formal theorem, no generality, novelty, Stage7.5A or Stage8 PASS.")
