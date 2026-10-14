#!/usr/bin/env python3
"""Preserved-input and mathematical witness guards; not an editorial gate."""
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'docs/audit'


def main():
    freeze=json.loads((AUDIT/'STAGE30B_FROZEN_INPUTS.json').read_text())
    names=list(freeze['blobs'])
    result=subprocess.run(['git','hash-object','--stdin-paths'],cwd=ROOT,
        input='\n'.join(names)+'\n',capture_output=True,text=True,check=True)
    assert dict(zip(names,result.stdout.splitlines(),strict=True))==freeze['blobs']
    exact=json.loads((AUDIT/'STAGE30B_EXACT_RESULTS.json').read_text())
    assert len(exact['certificates'])==26
    assert sum(c['count'] for c in exact['certificates'])==12708
    assert all(c['pass'] for c in exact['certificates'])
    for row in exact['rational_examples']:
        assert row['F_minus_public_private']['float']>0
        assert row['F_a']['float']>0
        assert row['member_policy_gain']['float']>0
    low,high,under,political_m,political_l=exact['rational_examples']
    assert low['world_RS_minus_public']['float']<0<high['world_RS_minus_public']['float']
    assert under['world_RS_minus_public']['float']<low['world_RS_minus_public']['float']
    assert political_m['outsider_policy_gain']['float']>0
    assert political_l['outsider_policy_gain']['float']<0
    assert exact['rejected_blanket_F_ac_positive']['float']<0
    numeric=json.loads((AUDIT/'STAGE30B_NUMERIC_RESULTS.json').read_text())
    assert numeric['formula_matrix_maximum_error']<1e-12
    assert len(numeric['deviation_search'])==72
    assert numeric['optimizer_nonconvergence_count']==0
    for row in numeric['deviation_search']+numeric['public_zero_a_checks']:
        assert max(d['gain'] for d in row['checks'])<1e-7
    assert all(row['policy']=='M' for row in numeric['public_zero_a_checks'])
    assert numeric['rejected_candidates'][0]['deviation']['gain']>1e-7
    old=(AUDIT/'STAGE30_EDITOR_DECISION.md').read_text()
    assert 'NO-GO' in old
    print(f'PASS: {len(names)} inherited files unchanged; 26 exact signs, '
          'strict witness inequalities, 72 private and 24 public profile attacks.')
    print('Construction evidence only. Stage30 NO-GO preserved; new Stage4A/6 pending.')


if __name__=='__main__':main()
