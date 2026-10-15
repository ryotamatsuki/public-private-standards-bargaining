#!/usr/bin/env python3
"""Stage30L: document inventory and statement-scope checks ONLY.

Green CI does NOT certify originality, source full-text, equilibrium proofs,
external referee approval, theory freeze, Lean or paper submission readiness.
"""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
folder=root/"docs/audit"
files=[
"STAGE30L_PAPER_ARCHITECTURE.md",
"STAGE30L_WORKING_INTRO_CONTRIBUTIONS.md",
"STAGE30L_RELATED_LITERATURE_WORKING.md",
"STAGE30L_EDITORIAL_SCOPE_QA.md",
"STAGE30L_README.md",
]
d={f:(folder/f).read_text(encoding="utf-8") for f in files}
for f,s in d.items():
    assert len(s)>1800, (f,len(s))
    assert "Stage30L" in s,f
    assert not any(c in s for c in "\x08\x0b\x0c"),f
all_text="\n".join(d.values())
for token in ["C1","C2","C3","C4","C5","C6","C7","Stage7.5","UNRESOLVED",
              "O(0,0)","K_W","pure SPE","Takarada","Buccella","Barrett",
              "Gandal","Klimenko","Bordignon"]:
    assert token.lower() in all_text.lower(),token
intro=d["STAGE30L_WORKING_INTRO_CONTRIBUTIONS.md"]
for token in ["Working abstract","Working Introduction","Our analysis connects",
              "C1+C3+C7","C2+C5+C6","NOT manuscript","entire pure"]:
    assert token.lower() in intro.lower(),token
lit=d["STAGE30L_RELATED_LITERATURE_WORKING.md"]
for token in ["Katz","Buccella","Nabin","Takarada","Barrett","Gandal",
              "Bordignon","Farrell","Costinot","Harstad",
              "10.1007/s00712-023-00834-x","10.1111/jpet.12425"]:
    assert token in lit,token
arch=d["STAGE30L_PAPER_ARCHITECTURE.md"]
for token in ["Proposition 1","Proposition 2","Proposition 3","Main","Appendix",
              "r<=2","source","NOT Stage 8"]:
    assert token.lower() in arch.lower(),token
qa=d["STAGE30L_EDITORIAL_SCOPE_QA.md"]
for token in ["governments","outsider","strict","infimum","supremum","NO",
              "NOT EXECUTED"]:
    assert token.lower() in qa.lower(),token
assert "NOT FROZEN" in d["STAGE30L_README.md"] or "no official theory freeze" in d["STAGE30L_README.md"]
print("PASS: 5 Stage30L prewriting files, literature list, C1-C7 claim labels and explicit scope restrictions.")
print("No Lean, source-priority theorem signoff, theory freeze, full-paper rewrite or submission was tested.")
