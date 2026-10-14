#!/usr/bin/env python3
"""Verify preserved inputs, scope disclosures and negative diagnostic evidence.

Passing this check means audit evidence is internally consistent, not that the
manuscript has economic publication value or is submission ready.
"""
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
AUDIT=ROOT/'docs/audit'


def read(name):return json.loads((AUDIT/name).read_text())


def main():
    manifest=read('STAGE30_AUDIT_MANIFEST.json')
    expected=manifest['frozen_input_blobs']
    names=list(expected)
    proc=subprocess.run(['git','hash-object','--stdin-paths'],cwd=ROOT,
        input='\n'.join(names)+'\n',text=True,capture_output=True,check=True)
    actual=dict(zip(names,proc.stdout.splitlines(),strict=True))
    assert actual==expected,'A pre-Stage30 source file changed or disappeared'
    for name in manifest['required_reports']:
        text=(AUDIT/name).read_text()
        assert len(text)>600,name
        assert not any(c in text for c in ['\x08','\x0b','\x0c']),name
    assert 'NO-GO' in (AUDIT/'STAGE30_EDITOR_DECISION.md').read_text()
    assert 'CONDITIONAL PASS' in (AUDIT/'STAGE30_INDEPENDENT_MATH_AUDIT.md').read_text()
    assert 'NOT INDEPENDENTLY VERIFIED' in (AUDIT/'STAGE30_INDEPENDENT_MATH_AUDIT.md').read_text()
    assert 'UNRESOLVED' in (AUDIT/'STAGE30_PRIOR_ART_THEOREM_ABSORPTION.md').read_text()
    exact=read('STAGE30_INDEPENDENT_EXACT_RESULTS.json')
    assert len(exact['certificates'])==43
    assert sum(x['count'] for x in exact['certificates'])==10023
    assert all(x['pass'] for x in exact['certificates'])
    for key in ['Cournot_FOC','KW_minus_KE','KE_minus_KV','entrant_upper_less_three_fifths']:
        assert exact['identities'][key] is True,key
    numeric=read('STAGE30_INDEPENDENT_GAME_RESULTS.json')
    assert len(numeric['private_candidates'])==27
    for row in numeric['private_candidates']:
        assert row['continuation']['policy']=='L'
        assert max(d['gain'] for d in row['deviations'])<1e-7
    assert numeric['optimizer_nonconvergence_count']==0
    assert numeric['random_profiles']['count']==6000
    fee=next(c for c in numeric['alternatives']['public_cost'] if c['eta']==.14)
    assert fee['g']==.04 and fee['continuation']['policy']=='L'
    assert all(x<0 for x in fee['continuation']['gains'])
    assert max(d['gain'] for d in fee['deviations'])<1e-7
    voting=numeric['alternatives']['strategic_vote']['NNN_L']
    assert voting['continuation']['policy']=='L'
    assert all(x>0 for x in voting['continuation']['gains'])
    assert any(v['votes']==[0,0,0] and not v['pass'] for v in voting['vote_Nash'])
    edits=read('STAGE30_EXPOSITION_REVISIONS.json')
    assert len(edits)==11
    for edit in edits:
        original=(ROOT/edit['file']).read_text()
        assert edit['original'] in original,edit['file']
    print(f'PASS: {len(names)} frozen files unchanged; 6 reports, 43 exact certificates, '
          '27 numerical candidates, 2 negative diagnostics and 11 original passages checked.')
    print('EDITORIAL VERDICT REMAINS NO-GO; green CI does not authorize Stage31.')


if __name__=='__main__':main()
