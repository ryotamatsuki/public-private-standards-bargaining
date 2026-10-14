#!/usr/bin/env python3
"""Numerical attacks and illustrations, explicitly not global proofs."""
import json
from pathlib import Path
import numpy as np
from scipy.optimize import brentq,minimize_scalar
from stage30_independent_game_audit import (
    cournot,evaluate,finite_best_response,serial,PI,WI,M,GAM,V,KAP,RHO,PHI)

SEED=300015
P=PI-PHI/2


def bilateral(c,a,eta):
    b=GAM+KAP*a-V*c;d=GAM-eta*a;D=2*M*(2*M+b)-2*d*d
    num=2*M*(1+RHO*c)-d;x=num/D;y=(2*M+b-2*d*(1+RHO*c))/D
    xa=(eta*D-num*(2*M*KAP+4*eta*d))/D**2
    cs=(M+b)*x*x+2*d*x*y+M*y*y/2
    F=3*M*x*x-PHI*(c*c+a*a)/2
    return {'F':F,'Fa':6*M*x*xa-PHI*a,'KV':WI-3*M*y*y-cs,
            'B':WI+PHI/2-3*M*x*x-cs-PHI*(1-c*c)/2,
            'world_noK':2*F+3*M*y*y+3*cs,'x':x,'y':y,'cs':cs}


def alpha(c,eta):
    if bilateral(c,c,eta)['Fa']>=0:return c
    return brentq(lambda a:bilateral(c,a,eta)['Fa'],0,c,xtol=1e-13)


def admissible(c,a,eta,K):
    b=bilateral(c,a,eta)
    return a<=c and b['Fa']>=-1e-10 and b['F']>=P-1e-10 and b['KV']<K-1e-11


def main():
    result={'method':'finite deviation search and numerical illustrations; not proof',
            'seed':SEED,'examples':[],'deviation_search':[],
            'frontiers':[],'public_zero_a_checks':[],'rejected_candidates':[]}
    for c,a,e,K in [(1,0,.14,.55),(1,.5,.14,.55),(.95,0,.14,.55),
                     (.929,0,.14,.54),(.929,0,.14,.55),(.9,0,.14,.55)]:
        pp=[(c,a),(c,a),None];ev=evaluate(pp,e,K,(2,),2)
        b=bilateral(c,a,e)
        result['examples'].append({'c':c,'a':a,'eta':e,'K':K,
          'qualifies_private_SPE':bool(admissible(c,a,e,K)),
          'continuation':serial(ev),'bilateral':b,
          'world_RS_minus_public':b['world_noK']-3*WI+K})
    # Baseline formulas are independently checked against the direct matrix.
    rng=np.random.default_rng(SEED);maxerr=0.
    for _ in range(1000):
        c=float(rng.random());a=float(c*rng.random());e=float(rng.uniform(.1,.14))
        b=bilateral(c,a,e);gross,cs,q,H=cournot([(c,a),(c,a),None],e)
        maxerr=max(maxerr,abs(b['x']-q[0]),abs(b['y']-q[2]),abs(b['cs']-cs),
          abs(b['F']-(gross[0]-PHI*(c*c+a*a)/2)))
    result['formula_matrix_maximum_error']=maxerr
    assert maxerr<1e-12
    for e in [.10,.115,.14]:
        cmin=brentq(lambda c:bilateral(c,alpha(c,e),e)['F']-P,.7,1,xtol=1e-12)
        result['frontiers'].append({'eta':e,'participation_c_floor':cmin,
          'a_at_floor':alpha(cmin,e),'a_at_c1':alpha(1,e)})
        for K in [.54,.55,.56]:
            for c in [cmin+1e-5,.95,1.]:
                hi=alpha(c,e)
                if bilateral(c,0,e)['F']>=P:lo=0.
                else:lo=brentq(lambda a:bilateral(c,a,e)['F']-P,0,hi,xtol=1e-13)
                aa=(lo+hi)/2
                if not admissible(c,aa,e,K):continue
                p=[(c,aa),(c,aa),None]
                for A,r in [((2,),2),((0,1,2),3)]:
                    checks=[finite_best_response(p,i,e,K,A,r,
                      extra=(e==.14 and K==.55 and c==1)) for i in range(3)]
                    result['deviation_search'].append({'eta':e,'K':K,'profile':p,
                      'A':A,'r':r,'checks':checks})
                    assert max(x['gain'] for x in checks)<1e-7
    # The active equality edge and zero-commonality witnesses are attacked too.
    for e in [.10,.14]:
        for c,a in [(1,0),(1,.5 if e==.14 else .25),(.929,0)]:
            K=.55;p=[(c,a),(c,a),None]
            for A,r in [((2,),1),((2,),2),((0,1,2),3)]:
                checks=[finite_best_response(p,i,e,K,A,r,extra=False) for i in range(3)]
                result['deviation_search'].append({'eta':e,'K':K,'profile':p,
                  'A':A,'r':r,'checks':checks})
                assert max(x['gain'] for x in checks)<1e-7
    for j in range(24):
        p=[(float(rng.random()),0.) if (j>>i)&1 else None for i in range(3)]
        e=float(rng.uniform(.1,.14));K=float(rng.uniform(.54,.56));r=j%2+1
        A=[(0,1),(0,2),(1,2),(0,1,2)][j%4]
        ev=evaluate(p,e,K,A,r)
        checks=[finite_best_response(p,i,e,K,A,r,extra=False) for i in range(3)]
        result['public_zero_a_checks'].append({'profile':p,'eta':e,'K':K,'A':A,
            'r':r,'policy':ev['policy'],'checks':checks})
        assert ev['policy']=='M' and max(x['gain'] for x in checks)<1e-7
    # A tempting but false simplification: substitute a*(1,eta) at every c.
    c=.95;e=.14;aa=alpha(1,e);p=[(c,aa),(c,aa),None]
    bad=finite_best_response(p,0,e,.55,(2,),2,extra=False)
    result['rejected_candidates'].append({'claim':'reuse c=1 optimal a at c<1',
        'profile':p,'eta':e,'K':.55,'deviation':bad})
    assert bad['gain']>1e-7
    result['optimizer_nonconvergence_count']=sum(
        x['optimizer']['success'] is False
        for row in result['deviation_search'] for x in row['checks'])
    # Numerical welfare envelope over the explicitly characterized pair region.
    envelope=[]
    for e in [.10,.115,.14]:
        cells=[]
        for c in np.linspace(.88,1,181):
            for a in np.linspace(0,.61,244):
                if admissible(c,a,e,.55):
                    b=bilateral(c,a,e)
                    cells.append((b['world_noK']-3*WI+.55,float(c),float(a)))
        envelope.append({'eta':e,'K':.55,'sampled_designs':len(cells),
          'sampled_min_RS_minus_public':min(cells),
          'sampled_max_RS_minus_public':max(cells),
          'scope':'grid illustration of characterized branch, no certified extrema'})
    result['sampled_welfare_envelope']=envelope
    out=Path('docs/audit/STAGE30B_NUMERIC_RESULTS.json')
    out.write_text(json.dumps(result,indent=2,default=lambda x:float(x))+'\n')
    print(json.dumps({'examples':result['examples'],'frontiers':result['frontiers'],
      'tested_profiles':len(result['deviation_search']),
      'nonconvergence':result['optimizer_nonconvergence_count'],
      'envelope':envelope},indent=2))


if __name__=='__main__':main()
