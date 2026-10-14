#!/usr/bin/env python3
"""Post-checkpoint reconciliation, not the primitives-first certificate."""
import hashlib
import json
from pathlib import Path
import sympy as s
from stage30c_independent_symbols import objects

ROOT=Path(__file__).resolve().parents[1]


def main():
    ob=objects();c,a,e=ob['vars'];f=ob['fields']
    m,g,v,k,rho,phi=(ob[x] for x in ('m','g','v','k','rho','phi'))
    # Transcription from Stage30B §1, only after the derivation checkpoint.
    b=g+k*a-v*c;d=g-e*a;D=2*m*(2*m+b)-2*d*d
    x=(2*m*(1+rho*c)-d)/D;y=(2*m+b-2*d*(1+rho*c))/D
    cs=(m+b)*x*x+2*d*x*y+m*y*y/2
    F=3*m*x*x-phi*(c*c+a*a)/2
    B=ob['piI']+ob['csI']-3*m*x*x-cs-phi*(1-c*c)/2
    V=ob['WI']-3*m*y*y-cs
    T=2*F+3*m*y*y+3*cs
    equivalents={'x':x,'y':y,'C':cs,'F':F,'B':B,'V':V,'T':T}
    assert all(s.cancel(f[name]-expr)==0 for name,expr in equivalents.items())
    construction=json.loads((ROOT/'docs/audit/STAGE30B_EXACT_RESULTS.json').read_text())
    fresh=json.loads((ROOT/'docs/audit/STAGE30C_EXACT_RESULTS.json').read_text())
    keymap={'F_minus_P':'F_minus_public_private','F_a':'F_a','B':'member_policy_gain',
            'K_minus_V':'outsider_policy_gain','private_minus_public_world':'world_RS_minus_public'}
    matches=[]
    for row in fresh['exact_witnesses']:
        old=next(r for r in construction['rational_examples'] if
            all(s.Rational(r[k])==s.Rational(row[k]) for k in ('c','a','eta','K')))
        for newkey,oldkey in keymap.items():
            lhs=s.Rational(row[newkey]['rational']);rhs=s.Rational(old[oldkey]['rational'])
            if newkey=='K_minus_V':rhs=-rhs
            assert lhs==rhs
        matches.append({k:row[k] for k in ('c','a','eta','K')})
    oldbound=s.Rational(construction['identities']['entrant_net_upper'])
    newbound=s.Rational(fresh['scalar_bounds']['entrant_net_upper']['rational'])
    outside=s.Rational(fresh['scalar_bounds']['outsider_profit_lower']['rational'])
    assert oldbound<outside and newbound<outside
    out={'phase':'post primitives-first checkpoint db6f75d66d7f66f37fa8d8c21611519781880da3',
         'no_production_solver_called':True,'symbolic_object_equivalence':list(equivalents),
         'exact_witnesses_reconciled':matches,'material_claim_discrepancy':'none on certified scope',
         'entrant_bounds':{'construction':str(oldbound),'independent':str(newbound),
             'outside':str(outside),'explanation':'different valid sufficient upper bounds'},
         'production_read_after_checkpoint':{
             path:hashlib.sha256((ROOT/path).read_bytes()).hexdigest() for path in (
                 'code/stage30b_within_model_exact.py','code/stage30b_within_model_numeric.py',
                 'docs/audit/STAGE30B_RESULTS_AND_PROOFS.md')},
         'source_sha256':{Path(__file__).name:hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
         'uncertified':'novelty, portability, seven-parameter extension, proof assistant, author verification'}
    path=ROOT/'docs/audit/STAGE30C_RECONCILIATION.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    print('Reconciled 7 symbolic objects and 4 rational witness profiles; no old solver invoked.')


if __name__=='__main__':main()
