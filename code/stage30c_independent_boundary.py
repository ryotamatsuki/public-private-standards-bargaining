#!/usr/bin/env python3
"""Boundary/refinement regressions using only the new primitive evaluator."""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path
import sympy as s
from scipy.optimize import brentq
from stage30c_independent_symbols import objects
from stage30c_independent_numeric import (
    Parameters, common, exact_gains, exact_private, state, deviation, attack)

ROOT=Path(__file__).resolve().parents[1]


def exact_state(profile,p,A,r):
    gains=exact_gains(profile,p)
    yes=[i for i,d in enumerate(gains) if d>=0]
    mandate=len(yes)>=r and bool(set(A).intersection(yes))
    _,q,cs=exact_private(profile,p)
    m,phi,K=Q('.99'),Q('.14'),Q(str(p.K))
    sunk=[Q(0) if d is None else K+phi*(Q(str(d[0]))**2+Q(str(d[1]))**2)/2
          for d in profile]
    qi=Q('1.32')/Q('2.24')
    if mandate:
        extra=[K+phi/2 if d is None else phi*(1-Q(str(d[0]))**2)/2 for d in profile]
        profits=[3*m*qi**2-sunk[i]-extra[i] for i in range(3)]
    else:profits=[3*m*q[i]**2-sunk[i] for i in range(3)]
    return {'policy':'M' if mandate else 'L','delta':gains,'profit':profits}


def main():
    ob=objects();c,a,e=ob['vars'];f=ob['fields'];p=Parameters('.14','.55')
    out={'proof_status':'exact rational regressions plus boundary attacks; not a new theorem',
         'exact_checks':{},'boundary_searches':[]}
    # Formal boundary of the proposed overextension: all mandate gains exactly0.
    before=[('1','0')]*3;after=[None,('1','0'),('1','0')]
    old=exact_state(before,p,(0,1,2),3);new=exact_state(after,p,(0,1,2),3)
    assert old['delta']==[Q(0)]*3 and old['policy']=='M' and new['policy']=='L'
    gain=new['profit'][0]-old['profit'][0];assert gain>0
    out['exact_checks']['unanimity_scope_counterexample']={
        'eta':'7/50','K':'11/20','profile':before,'agenda':[0,1,2],'quorum':3,
        'old_delta':list(map(str,old['delta'])),'old_policy':old['policy'],
        'deviation':'firm0 -> N','new_delta':list(map(str,new['delta'])),
        'new_policy':new['policy'],'gain':str(gain),'gain_float':float(gain)}
    # Two false derivative simplifications were already rejected at construction.
    fac=s.cancel(f['F_ac'].subs({c:1,a:0,e:s.Rational('.1')}));assert fac<0
    yc=s.cancel(s.diff(f['y'],c).subs({c:1,a:1,e:s.Rational('.14')}));assert yc==0
    out['exact_checks']['rejected_blanket_F_ac_positive']=str(fac)
    out['exact_checks']['weak_y_c_boundary']=str(yc)
    # O(0,0) is development and switches the pair technology, unlike N.
    pp=[(1.,.5),(1.,.5),None];nn=list(pp);nn[2]=(0.,0.)
    qo=state(pp,p,(2,),2)['q'];qn=state(nn,p,(2,),2)['q']
    assert max(abs(qo-qn))>.01
    out['exact_checks']['N_vs_O00']={'profile_N':pp,'profile_O00':nn,
        'private_quantities_N':qo.tolist(),'private_quantities_O00':qn.tolist()}
    # The existing exact root bracket is independently solved here by matrix FOCs.
    cap=brentq(lambda t:common([(t,0.),(t,0.),None],p)[0],.9,.95,xtol=1e-14)
    roots=[(Parameters(E,.55),brentq(
        lambda t:common([(1.,t),(1.,t),None],Parameters(E,.55))[1],.30,.61,
        xtol=1e-14)) for E in [.10,.14]]
    cases=[]
    for A,r in [((2,),2),((0,1,2),3)]:
        cases.append(('weak F=P participation',[(cap,0.),(cap,0.),None],p,A,r))
        cases.append(('indifferent withdrawal action',[None,(cap,0.),None],p,A,r))
    for pp,aa in roots:
        cases.append(('canonical F_a=0 root',[(1.,aa),(1.,aa),None],pp,(0,1,2),3))
    for j,(kind,prof,pp,A,r) in enumerate(cases):
        ev=state(prof,pp,A,r)
        rows=[attack(prof,pp,A,r,i,350000+j*3+i) for i in range(3)]
        out['boundary_searches'].append({'kind':kind,'profile':prof,
            'eta':float(pp.eta),'K':float(pp.K),'agenda':A,'quorum':r,
            'policy':ev['policy'],'attacks':rows,
            'precision':'floating representative of the independently isolated algebraic root'})
    # Reusing the c=1 root at c<1 violates the actual derivative condition.
    aa=roots[-1][1];prof=[(.95,aa),(.95,aa),None]
    old=state(prof,p,(2,),2)
    actual=brentq(lambda t:common([(.95,t),(.95,t),None],p)[1],.30,.61)
    new=deviation(prof,p,(2,),2,0,(.95,actual));gain=float(new['profit'][0]-old['profit'][0])
    assert common(prof,p)[1]<0 and old['policy']=='L' and new['policy']=='L' and gain>1e-7
    out['exact_checks']['rejected_reuse_c1_optimum']={
        'c':.95,'eta':.14,'old_a':aa,'actual_c_root':actual,
        'old_F_a':common(prof,p)[1],'deviation':[.95,actual],'gain':gain,
        'policy_before':old['policy'],'policy_after':new['policy']}
    rows=[z for case in out['boundary_searches'] for z in case['attacks']]
    out['summary']={'boundary_profiles':len(cases),'boundary_deviation_searches':len(rows),
        'maximum_observed_gain':max(z['maximum_observed_gain'] for z in rows),
        'nonconvergence_count':sum(not z['DE_converged'] for z in rows),
        'nonconvergence_state':'UNRESOLVED searches; analytic boundary proof is separate'}
    out['source_sha256']={path.name:hashlib.sha256(path.read_bytes()).hexdigest() for path in
        [Path(__file__),Path(__file__).with_name('stage30c_independent_numeric.py'),
         Path(__file__).with_name('stage30c_independent_symbols.py')]}
    path=ROOT/'docs/audit/STAGE30C_BOUNDARY_RESULTS.json'
    path.write_text(json.dumps(out,indent=2)+'\n')
    if out['summary']['maximum_observed_gain']>1e-7:
        raise RuntimeError('POTENTIAL boundary COUNTEREXAMPLE saved; reconcile exactly')
    print(json.dumps(out['summary']),flush=True)


if __name__=='__main__':main()
