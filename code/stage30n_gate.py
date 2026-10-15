#!/usr/bin/env python3
"""Stage30N scoped evidence integrity + real rational policy/cost evaluator.

DOES NOT audit complete C1-C7 SPE proofs, priority or real national voting law.
"""
from pathlib import Path
from fractions import Fraction as Q
import subprocess,json
root=Path(__file__).resolve().parents[1]
folder=root/"docs/audit"
names=[
    "STAGE30N_FIXED_QUORUM_AND_INCIDENCE.md",
    "STAGE30N_EDITOR_READY_PASSAGES.md",
    "STAGE30N_REFEREE_RESPONSE_DECISION.md",
    "STAGE30N_README.md",
]
docs={name:(folder/name).read_text(encoding="utf-8") for name in names}
for name,s in docs.items():
    assert len(s)>1200,(name,len(s))
    assert "Stage30N" in s,name
    assert all(ch not in s for ch in "\x08\x0b\x0c"),name
whole="\n".join(docs.values())
for x in ("C1","C2","C3","C5","C6","C7","O(1,.5)","O(0,0)","B>0",
          "g=.04","NOT","r=2","A={3}","UNRESOLVED"):
    assert x in whole,x
assert "2×2" in docs[names[1]]
assert "ex ante" in docs[names[0]].lower()
assert "not a new" in whole.lower()
result=subprocess.run(["python","code/stage30n_fixed_quorum_counterfactual.py"],
    cwd=root,text=True,capture_output=True,check=True)
print(result.stdout,end="")
out=json.loads((folder/"STAGE30N_FIXED_QUORUM_EXACT_RESULTS.json").read_text(encoding="utf-8"))
assert len(out["cases"])==2 and len(out["permutations"])==3
assert out["all_N_history_both_institutions_M"]
assert [p["old_private_SPE_eligible_by_C1"] for p in out["permutations"]]==[False,False,True]
assert all(p["fixed_new_r2_A13_mandate"] for p in out["permutations"])
for row in out["cases"]:
    assert row["fixed_r2_old_agenda_outsider_only_passes"] is False
    assert row["fixed_r2_new_agenda_outsider_plus_founder_passes"] is True
    signs=row["gov_M_minus_L"]
    assert Q(signs["founder1"])>0
    assert Q(signs["founder2"])>0
    assert Q(signs["outsider3"])<0
    assert Q(row["source_C1_membership_checks"]["F_a"])>=0
    assert Q(row["source_C1_membership_checks"]["F_minus_P"])>=0
    assert Q(row["source_C1_membership_checks"]["K_minus_V"])>0
    w=row["world_welfare"]
    a=Q(row["history"]["firm1"][2])
    assert Q(w["new_public_pure_SPE"])-Q(w["same_history_M_after_sunk_private_stocks"])==Q("0.14")*a*a
assert out["cases"][0]["world_welfare"]["new_pure_minus_old_pure_decimal"]>0
assert out["cases"][1]["world_welfare"]["new_pure_minus_old_pure_decimal"]<0
print("PASS: exact fixed-r=2 agendas, all country labels, two old private SPE histories, cost incidence and sunk wedge.")
print("NOT PASSED/NOT ATTEMPTED: theorem novelty, full pure-SPE proof, government Nash, empirical welfare, Lean, paper publication.")
