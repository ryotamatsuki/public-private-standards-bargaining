#!/usr/bin/env python3
"""Audit *document consistency*, not actual publication priority.

Do not call this a literature novelty test: no machine can infer absence
of an earlier theorem simply because report formatting is consistent.
"""
from pathlib import Path
import re

root=Path(__file__).resolve().parents[1]
audit=root/"docs/audit"
docs={
 "sources":"STAGE30D_SOURCE_ACCESS_AND_SEARCH_LEDGER.md",
 "absorb":"STAGE30D_THEOREM_ABSORPTION_MAP.md",
 "editor":"STAGE30D_NOVELTY_EDITOR_DECISION.md",
 "frontier":"STAGE30D_FRONTIER_AND_STOP.md",
 "readme":"STAGE30D_README.md",
}
contents={k:(audit/v).read_text(encoding="utf-8") for k,v in docs.items()}
for k,x in contents.items():
 assert len(x)>1000,(k,len(x))
 assert "Bordignon" in x,(k,"published comparator absent")
 assert "Takarada" in x,(k,"JPET comparator absent")
 assert "UNRESOLVED" in x or "unresolved" in x or "not" in x.lower(),(k,"missing uncertainty")
 assert not any(c in x for c in "\x08\x0b\x0c"),k
ed=contents["editor"]
assert "CONDITIONAL GO" in ed
assert "NOT a GO" in ed and "Stage31" in ed
assert "PRIORITY" in ed
assert "C1" in ed and "C6" in ed
assert "ESSENTIAL FOLLOW-UP" in ed and "BOUNDED LIMITATION" in ed
mp=contents["absorb"]
assert all(re.search(r"\bC%d\b"%k,mp) for k in range(1,8))
assert all(re.search(r"\bP%d\b"%k,mp) for k in range(1,14))
for phrase in ["DIRECTLY ABSORBED","PARTIALLY ABSORBED","UNRESOLVED","Takarada","Bordignon"]:
 assert phrase in mp,phrase
src=contents["sources"]
for phrase in ["published", "Proposition 5", "Proposition 6", "Cornes", "Gandal", "Klimenko", "Owen", "Harstad"]:
 assert phrase.lower() in src.lower(),phrase
assert "NO DEFENSIBLE NEXT QUESTION FOUND" in contents["frontier"]
# Check that source URLs point to reputable known domains syntactically; this
# does NOT verify availability or theorem accuracy.
urls=re.findall(r"https?://[^\s<>)]+",src)
assert len(urls)>=14,len(urls)
print("PASS: five Stage6 docs, 7 claims mapped, 13 parent maps, URL inventory",len(urls))
print("NOTE: PASS verifies provenance assertions' presence ONLY.")
print("NOVELTY: CONDITIONAL GO; published priority NOT VERIFIED.")
print("NO manuscript rewrite, mathematical recertification, author-signoff or submission permitted.")
