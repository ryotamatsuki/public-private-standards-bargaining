#!/usr/bin/env python3
"""Stage30K review-document inventory: NOT a novelty or peer-review certificate."""
from pathlib import Path

root=Path(__file__).resolve().parents[1]
audit=root/"docs/audit"
files=["STAGE30K_PUBLISHED_EXTENSION_POSITIONING.md","STAGE30K_CONTRIBUTION_REPOSITIONING.md","STAGE30K_JOURNAL_FIT_AND_GATE.md","STAGE30K_README.md"]
items={name:(audit/name).read_text(encoding="utf-8") for name in files}
for name,s in items.items():
    assert len(s)>1000,(name,len(s))
    assert "Stage30K" in s,name
    assert not any(ch in s for ch in "\x08\x0b\x0c"),name
whole="\n".join(items.values())
for name in ["Buccella","Nabin","Farrell","Harstad","Costinot","Takarada","Bordignon","Barrett","Gandal","Klimenko"]:
    assert name in whole,name
for name in ["C1","C2","C3","C4","C5","C6","C7","K_W"]:
    assert name in items["STAGE30K_CONTRIBUTION_REPOSITIONING.md"],name
for s in ["NOT CERTIFIED","4", "NO", "JPET", "Journal of Economics", "International Journal of Economic Theory"]:
    assert s.lower() in items["STAGE30K_JOURNAL_FIT_AND_GATE.md"].lower(),s
for literal in ["https://link.springer.com/article/10.1007/s00712-023-00834-x",
 "https://onlinelibrary.wiley.com/doi/10.1111/ijet.12374",
 "https://economics.mit.edu/sites/default/files/publications/standards_final.pdf",
 "https://onlinelibrary.wiley.com/doi/10.1111/jpet.12425"]:
    assert literal in items["STAGE30K_PUBLISHED_EXTENSION_POSITIONING.md"],literal
assert "PUBLISHABLE" in items["STAGE30K_CONTRIBUTION_REPOSITIONING.md"]
print("PASS: 4 economic-theory positioning reports; bibliography and scope markers present.")
print("NOT VERIFIED BY CI: actual novel priority, external referees, theorem, theory freeze or submission eligibility.")
