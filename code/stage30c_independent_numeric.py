#!/usr/bin/env python3
"""Independent direct-market evaluator and hostile finite-deviation searches."""
import itertools
import json
from dataclasses import dataclass
from fractions import Fraction as Q
from pathlib import Path
import numpy as np
from scipy.optimize import brentq, differential_evolution

ROOT=Path(__file__).resolve().parents[1]
M,G,V,KAP,RHO,PHI=.99,.14,.01,.02,.32,.14
ALL_INST=[(tuple(i for i in range(3) if mask&(1<<i)),r)
          for mask in range(1,8) for r in (1,2,3)]


@dataclass(frozen=True)
class Parameters:
    eta: object
    K: object


def technology_market(profile,eta,exact=False):
    cast=(lambda v:Q(str(v))) if exact else float
    m,g,v,k,rho=map(cast,[M,G,V,KAP,RHO])
    eta=cast(eta)
    h=[[m if i==j else g for j in range(3)] for i in range(3)]
    z=[cast(1)]*3
    oo=[i for i,d in enumerate(profile) if d is not None]
    designs={i:tuple(map(cast,profile[i])) for i in oo}
    for c,a in designs.values():assert 0<=a<=c<=1
    if len(oo)==2:
        i,j=oo;o=next(x for x in range(3) if x not in oo)
        c=min(designs[i][0],designs[j][0]);a=min(designs[i][1],designs[j][1])
        z[i]=z[j]=1+rho*c
        h[i][j]=h[j][i]=g+k*a-v*c
        h[i][o]=h[o][i]=h[j][o]=h[o][j]=g-eta*a
    elif len(oo)==3:
        for i in range(3):
            z[i]=1+rho*max(min(designs[i][0],designs[j][0]) for j in range(3) if i!=j)
            for j in range(i):
                c=min(designs[i][0],designs[j][0]);a=min(designs[i][1],designs[j][1])
                h[i][j]=h[j][i]=g+k*a-v*c
    return h,z


def fraction_solve(A,b):
    """Small exact Gaussian elimination, separate from SymPy reconstruction."""
    aa=[list(row)+[bi] for row,bi in zip(A,b)];n=len(b)
    for j in range(n):
        pivot=next(i for i in range(j,n) if aa[i][j]!=0)
        aa[j],aa[pivot]=aa[pivot],aa[j]
        v=aa[j][j];aa[j]=[x/v for x in aa[j]]
        for i in range(n):
            if i!=j:
                v=aa[i][j];aa[i]=[x-v*y for x,y in zip(aa[i],aa[j])]
    return [row[-1] for row in aa]


def exact_private(profile,p):
    h,z=technology_market(profile,p.eta,True);m=Q('0.99')
    A=[[h[i][j]+(m if i==j else 0) for j in range(3)] for i in range(3)]
    q=fraction_solve(A,z)
    cs=sum(q[i]*h[i][j]*q[j] for i in range(3) for j in range(3))/2
    return h,q,cs


def exact_gains(profile,p):
    h,q,cs=exact_private(profile,p);m=Q('.99');phi=Q('.14');K=Q(str(p.K))
    qi=Q('1.32')/Q('2.24')
    public_gross=3*m*qi*qi+Q('1.875')*qi*qi
    return [public_gross-3*m*q[i]*q[i]-cs-
            (K+phi/2 if d is None else phi*(1-Q(str(d[0]))**2)/2)
            for i,d in enumerate(profile)]


def cournot(h,z):
    H=np.asarray(h,dtype=float);zz=np.asarray(z,dtype=float)
    A=H+np.eye(len(z))*M
    q=np.linalg.solve(A,zz)
    if not np.all(np.isfinite(q)):raise RuntimeError('UNRESOLVED nonfinite Cournot output')
    if np.any(q<=0):raise RuntimeError('UNRESOLVED/non-interior branch; do not filter')
    assert np.max(np.abs(A@q-zz))<1e-12
    assert np.linalg.eigvalsh(H).min()>0
    return q,3*M*q*q,float(q@H@q/2)


def state(profile,p,A,r):
    h,z=technology_market(profile,p.eta);q,gl,cs=cournot(h,z)
    K=float(p.K)
    sunk=np.array([0 if d is None else K+PHI*(d[0]**2+d[1]**2)/2 for d in profile])
    hp=np.full((3,3),G-V);np.fill_diagonal(hp,M)
    qp,gm,csm=cournot(hp,[1+RHO]*3)
    add=np.array([K+PHI/2 if d is None else PHI*(1-d[0]**2)/2 for d in profile])
    delta=gm+csm-gl-cs-add
    if np.any(np.abs(delta)<=5e-10):
        ex=exact_gains(profile,p)
        yes=[i for i,d in enumerate(ex) if d>=0]
        tie_method='exact Gaussian comparison'
    else:
        yes=[i for i,d in enumerate(delta) if d>=0]
        tie_method='float away from zero; not a sign proof'
    mandate=len(yes)>=r and bool(set(A).intersection(yes))
    pl,pm=gl-sunk,gm-sunk-add
    payoff=pm if mandate else pl
    if not np.all(np.isfinite(payoff)):raise RuntimeError('UNRESOLVED nonfinite payoff')
    return dict(q=q,profit=payoff,private_profit=pl,public_profit=pm,
                delta=delta,policy='M' if mandate else 'L',yes=yes,
                private_world=float(pl.sum()+3*cs),
                public_world=float(pm.sum()+3*csm),tie_method=tie_method)


def common(profile,p):
    """Derivatives from differentiated full FOCs, not a bilateral profit formula."""
    h,z=technology_market(profile,p.eta);H=np.array(h);A=H+np.eye(3)*M
    q=np.linalg.solve(A,np.array(z));qa=np.linalg.solve(A,-np.array(
        [[0,KAP,-float(p.eta)],[KAP,0,-float(p.eta)],[-float(p.eta),-float(p.eta),0]])@q)
    c,a=profile[0]
    F=3*M*q[0]**2-PHI*(c*c+a*a)/2
    Fa=6*M*q[0]*qa[0]-PHI*a
    qi=(1+RHO)/(2*(M+G-V));P=3*M*qi*qi-PHI/2
    return F-P,Fa


def exact_private_conditions(c,a,p):
    prof=[(c,a),(c,a),None];h,q,cs=exact_private(prof,p)
    m,phi,e=Q('.99'),Q('.14'),Q(str(p.eta))
    cc,aa=Q(str(c)),Q(str(a));qi=Q('1.32')/Q('2.24')
    P=3*m*qi*qi-phi/2
    A=[[h[i][j]+(m if i==j else 0) for j in range(3)] for i in range(3)]
    ha=[[Q(0),Q('.02'),-e],[Q('.02'),Q(0),-e],[-e,-e,Q(0)]]
    rhs=[-sum(ha[i][j]*q[j] for j in range(3)) for i in range(3)]
    qa=fraction_solve(A,rhs)
    return [3*m*q[0]*q[0]-phi*(cc*cc+aa*aa)/2-P,
            6*m*q[0]*qa[0]-phi*aa,-exact_gains(prof,p)[2]]


def deviation(prof,p,A,r,i,action):
    new=list(prof);new[i]=action
    return state(new,p,A,r)


def attack(prof,p,A,r,i,seed):
    initial=state(prof,p,A,r);base=initial['profit'][i]
    def objective(x):
        c,t=x
        return -(deviation(prof,p,A,r,i,(float(c),float(c*t)))['profit'][i]-base)
    if prof[i] is None:x0=(1.,0.)
    else:
        c,a=prof[i];x0=(c,a/c if c else 0.)
    ans=differential_evolution(objective,[(0.,1.),(0.,1.)],seed=seed,
        x0=x0,atol=2e-9,tol=1e-6,popsize=8,maxiter=100,polish=False)
    explicit=[None,(0.,0.),(1.,0.),(1.,1.)]
    explicit += [d for d in prof if d is not None]
    if prof[i] is not None: explicit.append(prof[i])
    records=[]
    for d in explicit:
        ev=deviation(prof,p,A,r,i,d)
        records.append((float(ev['profit'][i]-base),d,ev['policy']))
    best=max(records,key=lambda z:z[0])
    c,t=ans.x;ev=deviation(prof,p,A,r,i,(float(c),float(c*t)))
    search_gain=float(ev['profit'][i]-base)
    best=max(best,(search_gain,(float(c),float(c*t)),ev['policy']),key=lambda z:z[0])
    assert np.isfinite(search_gain) and abs(search_gain+ans.fun)<1e-11
    return {'firm':i,'maximum_observed_gain':best[0],'action':best[1],
            'policy_after':best[2],'DE_converged':bool(ans.success),
            'DE_message':str(ans.message),'evaluations':ans.nfev,
            'solver_failure_resolution':None if ans.success else
                'search UNRESOLVED; global theorem uses exact finite-deviation inequalities'}


def main():
    rng=np.random.default_rng(303031)
    output={'method':'direct NumPy matrix + separate Fraction Gaussian tie handling',
            'counterexample_threshold':1e-7,'searches':[],'scope_checks':[],
            'unresolved_searches':[],'proof_status':'numerics are attacks, not global proofs'}
    # Boundary participation and all open patterns, with independent linear solution.
    qmins=[];identity_errors=[]
    from stage30c_independent_symbols import objects
    import sympy as s
    ob=objects();sf={n:s.lambdify(ob['vars'],v,'numpy') for n,v in ob['fields'].items()}
    for j in range(1000):
        prof=[]
        for i in range(3):
            if not (j%8)&(1<<i):prof.append(None)
            else:
                c=float(rng.uniform());prof.append((c,float(c*rng.uniform())))
        p=Parameters(float(rng.uniform(.10,.14)),float(rng.uniform(.54,.56)))
        st=state(prof,p,(0,1),2);qmins.append(float(st['q'].min()))
        oo=[i for i,d in enumerate(prof) if d is not None]
        if len(oo)==2:
            c=min(prof[i][0] for i in oo);a=min(prof[i][1] for i in oo)
            outsider=next(i for i in range(3) if i not in oo)
            identity_errors.extend([abs(st['q'][oo[0]]-sf['x'](c,a,float(p.eta))),
                                    abs(st['q'][outsider]-sf['y'](c,a,float(p.eta)))])
    output['primitive_checks']={'profiles':1000,'minimum_quantity':min(qmins),
                               'maximum_bilateral_formula_error':max(identity_errors)}
    assert max(identity_errors)<1e-12
    # Verify all compliance/exit counts, including the different isolated intercept.
    margins=[]
    for prof in [[None]*3,[(0.,0.),(1.,1.),None],[(1.,0.)]*3]:
        for i in range(3):
            for other in range(4):
                count=1+other.bit_count();n=count
                hh=np.full((n,n),G-V);np.fill_diagonal(hh,M)
                z=[1.] if n==1 else [1+RHO]*n
                _,gp,_=cournot(hh,z)
                inc=.56+PHI/2 if prof[i] is None else PHI*(1-prof[i][0]**2)/2
                margins.append(float(gp[0]-inc))
    assert min(margins)>0
    output['compliance_checks']={'states':len(margins),'minimum_margin':min(margins)}
    # All constitutions at sparse histories and for arbitrary zero-a stocks.
    policies=0
    for mask in range(8):
        for caps in [(0.,.4,1.),(.12,.9,.63),(1.,1.,1.)]:
            prof=[(caps[i],0.) if mask&(1<<i) else None for i in range(3)]
            for A,r in ALL_INST:
                ev=state(prof,Parameters(.14,.55),A,r)
                if len(A)>=2 and r<=2 or mask.bit_count()<=1:
                    assert ev['policy']=='M';policies+=1
    output['broad_and_sparse_policy_checks']=policies
    # Explicit exact voting knife-edge and either side of it.
    c=.929;a=0.;e=.14
    prof=[(c,a),(c,a),None]
    kv=exact_gains(prof,Parameters(e,Q(0)))[2]
    assert Q('.54')<kv<Q('.56')
    for A,r in ALL_INST:assert state(prof,Parameters(e,kv),A,r)['policy']=='M'
    output['voting_boundary']={'K_exact':str(kv),'K_float':float(kv),
        'exact_delta':list(map(str,exact_gains(prof,Parameters(e,kv)))),
        'all_21_constitutions':'M under YES-on-tie',
        'K_minus_1e8_policy':state(prof,Parameters(e,kv-Q(1,10**8)),(2,),2)['policy'],
        'K_plus_1e8_policy':state(prof,Parameters(e,kv+Q(1,10**8)),(2,),2)['policy']}
    assert output['voting_boundary']['K_minus_1e8_policy']=='M'
    assert output['voting_boundary']['K_plus_1e8_policy']=='L'
    # Private SPE candidates have exact, strictly positive three-condition checks.
    candidates=[]
    for e,K,c in itertools.product([.10,.115,.14],[.54,.56],[.929,.95,1.]):
        p=Parameters(e,K)
        root=brentq(lambda a:common([(c,a),(c,a),None],p)[1],0,.61)
        for a in [0.,root/2,.97*root]:
            signs=exact_private_conditions(c,a,p)
            if all(x>0 for x in signs):candidates.append((c,a,p,list(map(str,signs))))
    rng.shuffle(candidates);candidates=candidates[:48]
    for j,(c,a,p,signs) in enumerate(candidates):
        outsider=j%3;founders=[i for i in range(3) if i!=outsider]
        prof=[None]*3
        for i in founders:prof[i]=(c,a)
        for A,r in ALL_INST:
            predicted_private=r==3 or A==(outsider,)
            assert (state(prof,p,A,r)['policy']=='L')==predicted_private
        r=1+j%3
        A=(outsider,) if r<=2 else ALL_INST[(j%7)*3][0]
        st=state(prof,p,A,r);assert st['policy']=='L'
        attacks=[attack(prof,p,A,r,i,330000+j*3+i) for i in range(3)]
        row={'kind':'private','profile':prof,'eta':float(p.eta),'K':float(p.K),
             'agenda':A,'quorum':r,'exact_condition_signs':signs,'attacks':attacks}
        output['searches'].append(row)
        print('private',j+1,'/',len(candidates),'max gain',max(z['maximum_observed_gain'] for z in attacks),flush=True)
    # Public candidate checks are scoped to broad agenda, not unanimity.
    for j in range(12):
        prof=[]
        for i in range(3):
            prof.append(None if not (j%8)&(1<<i) else (float(rng.uniform()),0.))
        p=Parameters([.10,.115,.14][j%3],[.54,.55,.56][j%3])
        A=(0,1) if j%2 else (0,1,2);r=1+j%2
        assert state(prof,p,A,r)['policy']=='M'
        attacks=[attack(prof,p,A,r,i,340000+j*3+i) for i in range(3)]
        output['searches'].append({'kind':'public-broad','profile':prof,
            'eta':float(p.eta),'K':float(p.K),'agenda':A,'quorum':r,'attacks':attacks})
    # Three-developer aggregate bound, plus L-to-M withdrawal witness.
    three=[];qi=(1+RHO)/(2*(M+G-V));P=3*M*qi*qi-PHI/2
    for j in range(300):
        caps=rng.uniform(size=3);aa=caps*rng.uniform(size=3)
        prof=list(zip(map(float,caps),map(float,aa)))
        h,z=technology_market(prof,.14);q,gross,cs=cournot(h,z)
        value=float(gross.sum()-PHI*(caps@caps+aa@aa)/2)
        three.append(value-3*P)
    assert max(three)<0
    output['three_developer_total_checks']={'profiles':len(three),'maximum_S_minus_3P':max(three)}
    triple=[(1.,0.),(1.,1.),(1.,1.)];p=Parameters(.14,.55)
    for A,r in [((0,),2),((0,1,2),3)]:
        old=state(triple,p,A,r);assert old['policy']=='L'
        rows=[]
        for i in range(3):
            ev=deviation(triple,p,A,r,i,None)
            rows.append({'firm':i,'gain':float(ev['profit'][i]-old['profit'][i]),
                         'policy_after':ev['policy']})
        assert max(x['gain'] for x in rows)>0
        output['scope_checks'].append({'kind':'three-developer L witness','agenda':A,
            'quorum':r,'profile':triple,'delta_before':old['delta'].tolist(),'withdrawals':rows})
    # Necessary zero-a condition is not sufficient under every constitution.
    prof=[(1.,0.)]*3;old=state(prof,p,(0,1,2),3)
    after=deviation(prof,p,(0,1,2),3,0,None)
    assert old['policy']=='M' and after['policy']=='L'
    output['scope_checks'].append({'kind':'overextended-public-initial-correspondence counterexample',
        'profile':prof,'agenda':[0,1,2],'quorum':3,'old_policy':old['policy'],
        'deviation':'firm0 -> N','new_policy':after['policy'],
        'gain':float(after['profit'][0]-old['profit'][0])})
    assert output['scope_checks'][-1]['gain']>0
    all_attacks=[z for row in output['searches'] for z in row['attacks']]
    for row in output['searches']:
        for z in row['attacks']:
            if not z['DE_converged']:
                output['unresolved_searches'].append({'profile':row['profile'],'agenda':row['agenda'],
                    'quorum':row['quorum'],'firm':z['firm'],'message':z['DE_message'],
                    'resolution':z['solver_failure_resolution']})
    output['summary']={'private_profiles':len(candidates),'public_profiles':12,
        'finite_deviation_searches':len(all_attacks),
        'maximum_observed_candidate_gain':max(z['maximum_observed_gain'] for z in all_attacks),
        'nonconvergence_count':len(output['unresolved_searches'])}
    path=ROOT/'docs/audit/STAGE30C_NUMERIC_RESULTS.json'
    path.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    if output['summary']['maximum_observed_candidate_gain']>1e-7:
        raise RuntimeError('POTENTIAL COUNTEREXAMPLE saved; exact reconciliation required')
    print(json.dumps(output['summary']),flush=True)


if __name__=='__main__':main()
