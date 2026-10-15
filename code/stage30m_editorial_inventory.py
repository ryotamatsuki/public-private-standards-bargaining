#!/usr/bin/env python3
"""Stage30M documentary editorial-review inventory; NOT true peer review."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]/"docs/audit"
names=[
    "STAGE30M_EDITOR_SCREEN_FULLPAPER.md",
    "STAGE30M_TWO_REFEREE_REPORTS.md",
    "STAGE30M_PARENT_AND_EDITOR_EVIDENCE.md",
    "STAGE30M_DESK_READINESS_ACTIONS.md",
    "STAGE30M_README.md",
]
texts={p:(root/p).read_text(encoding="utf-8") for p in names}
for name,s in texts.items():
    assert len(s)>1000, (name,len(s))
    assert "Stage30M" in s, name
    assert not any(x in s for x in "\x08\x0b\x0c"),name
combined="\n".join(texts.values())
for claim in ("C1","C2","C3","C4","C5","C6","C7",
              "Gandal","Shy","Klimenko","Bordignon","Barrett",
              "Buccella","2026","Takarada","Nabin","Farrell","Costinot"):
    assert claim in combined,claim
editor=texts[names[0]]
for claim in ("CONDITIONAL","NO","MAJOR REVISION","C1","C5","C6","K>V","K_W","UNRESOLVED"):
    assert claim.lower() in editor.lower(),claim
ref=texts[names[1]]
for claim in ("Referee A","Referee B","all-NO","O(0,0)","r=2","C5","CONDITIONAL"):
    assert claim.lower() in ref.lower(),claim
source=texts[names[2]]
for claim in ("10.1080/10438599.2025.2478583",
             "10.1007/s00712-023-00834-x",
             "10.1111/jpet.12425","10.1111/ijet.12374",
             "SOURCE","PRIORITY UNRESOLVED"):
    assert claim.lower() in source.lower(),claim
actions=texts[names[3]]
assert "| G8 " in actions and "G1 " in actions
assert "NO additional theorem" in actions
index=texts[names[4]]
for claim in ("NOT FROZEN","NOT RUN","NO-GO","CONDITIONAL YES"):
    assert claim in index,claim
print("PASS: Stage30M editor/referee/source/version/scope document inventory.")
print("NO NOVELTY CERTIFICATE; NO ACTUAL REFEREES; NO THEOREM TEST; NO MANUSCRIPT/FREEZE PASS.")
