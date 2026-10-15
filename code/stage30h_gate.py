#!/usr/bin/env python3
"""Stage30H: reporting inventory + exact original-branch arithmetic only.

Green CI does not turn a deliberately assumed category-demand discontinuity
into an empirically derived microfoundation, or certify literature novelty.
"""
from pathlib import Path
from fractions import Fraction as Q
import subprocess,json
root=Path(__file__).resolve().parents[1]
audit=root/"docs/audit"
files=["STAGE30H_CATEGORICAL_MEMBERSHIP_INTERPRETATION.md",
       "STAGE30H_EVIDENCE_AND_STOP.md",
       "STAGE30H_STAGE75_REASSESSMENT.md",
       "STAGE30H_README.md"]
contents={f:(audit/f).read_text(encoding="utf-8")for f in files}
for f,s in contents.items():
    assert len(s)>1000,f
    assert not any(ch in s for ch in "\x08\x0b\x0c"),f
    for key in ["Stage30","Stage7"]:
        assert key in s,f
it=contents[files[0]]
for phrase in ["PASS INTERPRETATION","FAIL","H_{13}","O(0,0)","K", "category", "USB","ISO"]:
    assert phrase.lower() in it.lower(),phrase
ed=contents[files[2]]
for phrase in ["CONDITIONAL GO","NOT FROZEN","Stage6","UNRESOLVED","Stage7.5A","BOUNDED"]:
    assert phrase in ed,phrase
ev=contents[files[1]]
for x in ["https://www.usb.org/compliance","https://www.usb.org/getting-vendor-id",
          "https://www.iso.org/conformity-assessment.html","10.1257/jep.8.2.117"]:
    assert x in ev,x
r=subprocess.run(["python","code/stage30h_branch_identity.py"],cwd=root,text=True,
                 capture_output=True,check=True)
print(r.stdout,end="")
v=json.loads((audit/"STAGE30H_BRANCH_IDENTITY_RESULTS.json").read_text(encoding="utf-8"))
assert v["founder_outsider_status_jump"]=="7/100"
assert len(v["cases"])==8
a=v["cases"]["bilateral_founders_with_N"]
b=v["cases"]["three_open_third_O00"]
assert a["z"]==b["z"]
assert Q(b["H"][0][2])-Q(a["H"][0][2])==Q("7/100")
assert "UNRESOLVED" in ed
print("PASS: exact source/interpretation gate + 8 original-demand cases.")
print("NOT verified: full microfoundation, source priority, all mixed equilibria, Stage7.5A formal or submission.")
