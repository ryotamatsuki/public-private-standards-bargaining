#!/usr/bin/env python3
"""Textual stage30e inventory gate: NOT a journal-priority/originality certificate."""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
files=["STAGE30E_PUBLISHED_SOURCE_RECONCILIATION.md","STAGE30E_EDITOR_AND_ACCESS_DECISION.md","STAGE30E_README.md"]
texts={f:(root/"docs/audit"/f).read_text(encoding="utf-8") for f in files}
for f,s in texts.items():
    assert len(s)>1000,f
    assert "Takarada" in s and "Bordignon" in s and "Gandal" in s and "Klimenko" in s,f
    assert not any(c in s for c in "\x08\x0b\x0c"),f
decision=texts[files[1]]
assert "CONDITIONAL GO" in decision
assert "UNRESOLVED" in decision
assert "Stage31" in decision
assert "NO-GO" in decision
assert "NOT ROUTED" in decision
for doi in ["10.1016/S0022-1996(00)00067-2","10.1016/j.jinteco.2008.08.005","10.1016/j.jpubeco.2006.02.001"]:
    assert doi in decision,doi
src=texts[files[0]]
for c in range(1,8):
    assert re.search(rf"\bC{c}\b",src),c
for word in ["published", "Proposition 5", "Proposition 6", "core", "fixed cost", "UNRESOLVED"]:
    assert word.lower() in src.lower(),word
print("PASS: three source-access documents, published Takarada C1-C7 map, DOI acquisition plan.")
print("EDITORIAL VERDICT: CONDITIONAL GO; 3 publication-version sources UNRESOLVED.")
print("THIS CHECK IS NOT PRIORITY VERIFICATION OR AN AUTHORIZATION TO REWRITE/SUBMIT.")
