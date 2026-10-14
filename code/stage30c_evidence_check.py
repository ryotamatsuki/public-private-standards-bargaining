#!/usr/bin/env python3
"""Preservation, provenance and failure-semantics checks; not a formal kernel."""
import ast
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def read(name):return json.loads((ROOT/'docs/audit'/name).read_text())


def digest(path):return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def main():
    frozen=read('STAGE30C_FROZEN_INPUTS.json')
    assert frozen['construction_commit']=='0735322e85dd876c5d361e6ddeaa6a4d79a9bbeb'
    assert len(frozen['preserved_parent_files'])==239
    for name,h in frozen['preserved_parent_files'].items():
        assert digest(name)==h,'Modified frozen baseline: '+name
    for name,h in frozen['independent_source_sha256'].items():
        assert digest(name)==h,'Stale independent source: '+name
        if name.endswith('.py'):
            tree=ast.parse((ROOT/name).read_text())
            for node in ast.walk(tree):
                modules=([v.name for v in node.names] if isinstance(node,ast.Import) else
                         [node.module or ''] if isinstance(node,ast.ImportFrom) else [])
                assert not any(m.startswith(('stage30_','stage30b_')) for m in modules),name
    ex=read('STAGE30C_EXACT_RESULTS.json')
    bd=read('STAGE30C_BOUNDARY_RESULTS.json')
    nu=read('STAGE30C_NUMERIC_RESULTS.json')
    re=read('STAGE30C_RECONCILIATION.json')
    for obj in (ex,bd,re):
        for name,h in obj['source_sha256'].items():
            assert digest('code/'+name)==h,'Stale generated output: '+name
    assert set(ex['certificates'])=={'founder_policy_positive','world_T_a_positive',
        'F_ac_positive_above_030','canonical_veto_below_K_min'}
    for cert in ex['certificates'].values():
        assert cert['primitive_identity_checked'] and cert['rechecked']
        assert Q(cert['minimum_leaf_lower'])>0
        assert cert['leaf_count']==len(cert['leaves']) and cert['leaf_count']>0
    assert all(Q(v['rational'])>0 for v in ex['scalar_bounds'].values())
    assert ex['canonical_root_sturm']['root_count']==0
    assert ex['preference_identity_checked'] and ex['ante_government_identity_checked']
    boundary=bd['exact_checks']['unanimity_scope_counterexample']
    assert boundary['old_delta']==['0']*3
    assert boundary['old_policy']=='M' and boundary['new_policy']=='L'
    assert Q(boundary['gain'])==Q('15291216325919/134283598086400')>0
    assert Q(bd['exact_checks']['rejected_blanket_F_ac_positive'])<0
    assert bd['exact_checks']['weak_y_c_boundary']=='0'
    assert nu['summary']['finite_deviation_searches']==180
    assert bd['summary']['boundary_deviation_searches']==18
    assert nu['summary']['maximum_observed_candidate_gain']<=1e-7
    assert bd['summary']['maximum_observed_gain']<=1e-7
    nonconverged=sum(not z['DE_converged'] for row in nu['searches'] for z in row['attacks'])
    assert nonconverged==nu['summary']['nonconvergence_count']==len(nu['unresolved_searches'])
    assert all('UNRESOLVED' in row['resolution'] for row in nu['unresolved_searches'])
    nonconverged_boundary=sum(not z['DE_converged'] for row in bd['boundary_searches'] for z in row['attacks'])
    assert nonconverged_boundary==bd['summary']['nonconvergence_count']
    assert re['no_production_solver_called'] and len(re['symbolic_object_equivalence'])==7
    assert len(re['exact_witnesses_reconciled'])==4
    print(json.dumps({'preserved_parent_files':239,'independent_source_hashes':len(
        frozen['independent_source_sha256']),'finite_deviation_searches':198,
        'unresolved_numerical_searches':nonconverged+nonconverged_boundary,
        'formal_status':'NOT FORMALLY VERIFIED','author_status':'NOT VERIFIED',
        'evidence_checks':'PASS; does not independently replace analytic audit'}))


if __name__=='__main__':main()
