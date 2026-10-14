#!/usr/bin/env python3
"""Independent direct matrix evaluator, finite deviations and diagnostics.

No production imports. Numerical searches are NOT continuous-domain proofs.
Errors and nonfinite payoffs abort. Optimizer nonconvergence is retained explicitly
and does not become evidence of an unprofitable deviation or of equilibrium.
"""
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar, differential_evolution, brentq

M=.99; GAM=.14; V=.01; KAP=.02; RHO=.32; PHI=.14
SEED=300014


def cournot(profile,eta,coherent=False):
    H=np.full((3,3),GAM);np.fill_diagonal(H,M)
    z=np.ones(3);dev=[i for i,p in enumerate(profile) if p is not None]
    if len(dev)==2:
        i,j=dev;k=next(n for n in range(3) if n not in dev)
        c=min(profile[i][0],profile[j][0]);a=min(profile[i][1],profile[j][1])
        H[i,j]=H[j,i]=GAM+KAP*a-V*c;z[[i,j]]=1+RHO*c
        H[i,k]=H[k,i]=H[j,k]=H[k,j]=GAM-eta*a
    if len(dev)==3:
        for i,j in itertools.combinations(dev,2):
            c=min(profile[i][0],profile[j][0]);a=min(profile[i][1],profile[j][1])
            H[i,j]=H[j,i]=GAM+KAP*a-V*c
        for i in dev:z[i]=1+RHO*max(min(profile[i][0],profile[j][0]) for j in dev if j!=i)
        if coherent:
            # Diagnostic only: a=0 entrant does not delete established differentiation.
            for i,j in itertools.combinations(dev,2):
                H[i,j]-=eta*abs(profile[i][1]-profile[j][1])
                H[j,i]=H[i,j]
    if not np.array_equal(H,H.T):raise ValueError('asymmetric demand matrix')
    q=np.linalg.solve(H+M*np.eye(3),z)
    if not np.all(np.isfinite(q)) or np.any(q<=0):raise ValueError('invalid Cournot branch')
    return 3*M*q*q,float(q@H@q/2),q,H


PI,CI,_,_=cournot([(1.,0.)]*3,.12)
PI=float(PI[0]);WI=PI+CI-PHI/2


def evaluate(profile,eta,K,A=(0,1,2),r=2,cost=0.,force_L=False,coherent=False):
    gross,cs,q,H=cournot(profile,eta,coherent=coherent)
    initial=np.array([0 if x is None else K+PHI*(x[0]**2+x[1]**2)/2 for x in profile])
    public=np.array([K+PHI/2 if x is None else K+PHI*(1+x[1]**2)/2 for x in profile])
    wl=gross+cs-initial;wm=PI+CI-public-cost
    gains=wm-wl;yes=gains>=-1e-12
    mandate=not force_L and int(yes.sum())>=r and any(yes[i] for i in A)
    pay=(np.full(3,PI)-public) if mandate else gross-initial
    if not np.all(np.isfinite(pay)):raise ValueError('nonfinite payoff')
    return {'policy':'M' if mandate else 'L','pay':pay,'gains':gains,'q':q,'cs':cs,'H':H}


def optimal_pair(eta):
    def fun(a):return cournot([(1,a),(1,a),None],eta)[0][0]-PHI*(1+a*a)/2
    r=minimize_scalar(lambda a:-fun(a),bounds=(0,1),method='bounded',options={'xatol':1e-14})
    if not r.success:raise ValueError(r.message)
    return float(r.x),float(-r.fun)


def finite_best_response(profile,i,eta,K,A,r,cost=0.,force_L=False,extra=True):
    base=evaluate(profile,eta,K,A,r,cost,force_L)['pay'][i]
    options=[None]
    for c in np.linspace(0,1,31):
        for ratio in np.linspace(0,1,21):options.append((float(c),float(c*ratio)))
    for p in profile:
        if p is not None:
            options.extend([p,(p[0],0.),(p[0],p[0])])
            for eps in [1e-8,1e-5,.01,.1,.25]:
                options.extend([(p[0],max(0.,p[1]-eps)),(min(1.,p[0]+eps),p[1])])
    best=(base,profile[i],evaluate(profile,eta,K,A,r,cost,force_L)['policy'])
    def val(p):
        pp=list(profile);pp[i]=p
        out=evaluate(pp,eta,K,A,r,cost,force_L)
        return float(out['pay'][i]),out['policy']
    for p in options:
        value,policy=val(p)
        if value>best[0]:best=(value,p,policy)
    if extra:
        def objective(uv):return -val((float(uv[0]),float(uv[0]*uv[1])))[0]
        opt=differential_evolution(objective,[(0,1),(0,1)],seed=SEED+i,popsize=10,maxiter=100,tol=1e-8,polish=False)
        # Nonconvergence is explicitly recorded; sampled feasible value remains evidence only.
        p=(float(opt.x[0]),float(opt.x[0]*opt.x[1]));value,policy=val(p)
        if value>best[0]:best=(value,p,policy)
        status={'success':bool(opt.success),'message':str(opt.message)}
    else:status={'success':None,'message':'grid and targeted finite deviations only'}
    return {'firm':i,'base':float(base),'best':best[0],'gain':best[0]-float(base),
            'deviation':best[1],'policy':best[2],'optimizer':status}


def voting_equilibria(delta,r):
    equilibria=[]
    for votes in itertools.product([0,1],repeat=3):
        passed=sum(votes)>=r
        payoff=np.array(delta)*passed
        stable=True
        for i in range(3):
            alt=list(votes);alt[i]=1-alt[i]
            if delta[i]*(sum(alt)>=r)>payoff[i]+1e-12:stable=False
        if stable:equilibria.append({'votes':votes,'pass':bool(passed)})
    return equilibria


def serial(out):
    return {k:v.tolist() if isinstance(v,np.ndarray) else v for k,v in out.items()}


def main():
    result={'seed':SEED,'evidence_type':'numerical search and separately stated analytic diagnostics',
            'pair':[],'private_candidates':[],'alternatives':{},'random_profiles':{}}
    for eta in [.10,.111,.112,.115,.118,.119,.12,.14]:
        a,f=optimal_pair(eta);p=[(1,a),(1,a),None]
        e=evaluate(p,eta,.55)
        gross,cs,_,_=cournot(p,eta)
        B=e['gains'][0];kv=e['gains'][2]+.55;ke=kv+2*B;kw=ke+PHI*a*a
        result['pair'].append({'eta':eta,'a':a,'f':f,'B':float(B),'KV':float(kv),'KE':float(ke),'KW':float(kw),
                               'world_ex_ante_RS':float(2*(f-.55)+gross[2]+3*cs),
                               'world_ex_ante_NNN_M':float(3*(WI-.55))})
    def cutoff(e,label):
        ar,fr=optimal_pair(e);pr=[(1,ar),(1,ar),None]
        out=evaluate(pr,e,.55);bv=float(out['gains'][0]);kv=float(out['gains'][2]+.55)
        return kv+2*bv+(PHI*ar*ar if label=='KW' else 0.)
    eE=brentq(lambda e:cutoff(e,'KE')-.55,.10,.14,xtol=1e-12)
    eW=brentq(lambda e:cutoff(e,'KW')-.55,.10,.14,xtol=1e-12)
    result['welfare_numeric']={'eta_E':eE,'eta_W':eW,'reversal_width':eW-eE,
        'fraction_of_certified_eta_range':(eW-eE)/.04,
        'public_cost_share_gross_national_public_welfare':.04/(WI+PHI/2),
        'scope':'floating-point descriptive measures; rational intervals certify signs'}
    for eta in [.10,.115,.14]:
        a,f=optimal_pair(eta);p=[(1,a),(1,a),None]
        for K in [.54,.55,.56]:
            for A,r in [((2,),1),((2,),2),((0,1,2),3)]:
                e=evaluate(p,eta,K,A,r)
                checks=[finite_best_response(p,i,eta,K,A,r,extra=(eta==.115 and K==.55)) for i in range(3)]
                result['private_candidates'].append({'eta':eta,'K':K,'A':A,'r':r,
                    'profile':p,'continuation':serial(e),'deviations':checks})
    # All random profiles include arbitrary asymmetric stocks and open zero designs.
    rng=np.random.default_rng(SEED);n=6000;lowq=float('inf');loweig=float('inf');L=0
    max_waste_gain=0.;waste_switches=0
    for k in range(n):
        count=k%4;profile=[None]*3
        for i in rng.choice(3,count,replace=False):
            c=float(rng.random());profile[i]=(c,float(c*rng.random()))
        eta=float(rng.uniform(.10,.14));K=float(rng.uniform(.54,.56))
        A=tuple(i for i in range(3) if (k%7+1)&(1<<i));r=k%3+1
        e=evaluate(profile,eta,K,A,r)
        lowq=min(lowq,float(e['q'].min()));loweig=min(loweig,float(np.linalg.eigvalsh(e['H']).min()))
        if e['policy']=='L':
            L+=1
            dev=[i for i in range(3) if profile[i] is not None]
            if len(dev)>=2:
                j=max(dev,key=lambda i:profile[i][1]);a2=sorted(profile[i][1] for i in dev)[-2]
                pp=list(profile);pp[j]=(profile[j][0],a2)
                ep=evaluate(pp,eta,K,A,r)
                if ep['policy']!='L':waste_switches+=1
                max_waste_gain=max(max_waste_gain,float(ep['pay'][j]-e['pay'][j]))
    result['random_profiles']={'count':n,'minimum_q':lowq,'minimum_H_eigenvalue':loweig,
      'L_histories':L,'waste_reduction_policy_switches':waste_switches,'maximum_waste_reduction_gain':max_waste_gain,
      'scope':'search and algebra sanity check, not proof of equilibrium absence'}
    eta=.115;K=.55;a,f=optimal_pair(eta);p=[(1,a),(1,a),None]
    cost_cases=[]
    for ecost in [.10,.115,.14]:
        ac,_=optimal_pair(ecost);pc=[(1,ac),(1,ac),None]
        fee=evaluate(pc,ecost,K,cost=.04)
        cost_cases.append({'g':.04,'eta':ecost,'K':K,'profile':pc,'continuation':serial(fee),
            'deviations':[finite_best_response(pc,i,ecost,K,(0,1,2),2,cost=.04) for i in range(3)],
            'NNN':serial(evaluate([None]*3,ecost,K,cost=.04))})
    result['alternatives']['public_cost']=cost_cases
    strategic=evaluate(p,eta,K,force_L=True)
    result['alternatives']['strategic_vote']={'eta':eta,'K':K,'profile':p,'private_continuation':serial(strategic),
      'vote_Nash':voting_equilibria(strategic['gains'],2),
      'private_profile_deviations':[finite_best_response(p,i,eta,K,(0,1,2),2,force_L=True) for i in range(3)]}
    # A valid strategic-voting SPE with no mandate everywhere uses the private game.
    # NNN L: unilateral O still lacks a compatible partner and loses K+stock cost.
    result['alternatives']['strategic_vote']['NNN_L']={
        'profile':[None]*3,'continuation':serial(evaluate([None]*3,eta,K,force_L=True)),
        'vote_Nash':voting_equilibria(evaluate([None]*3,eta,K)['gains'],2),
        'all_history_continuation':'All NO is Nash at quorum 2 for every gain vector; proposal decisions are payoff indifferent.'}
    entrant=[]
    for eps in [0.,1e-12,1e-8,1e-4]:
        for coherent in [False,True]:
            pp=[(1,a),(1,a),(eps,0.)]
            entrant.append({'c3':eps,'coherent':coherent,'result':serial(evaluate(pp,eta,K,coherent=coherent))})
    result['alternatives']['entrant_discontinuity']={'before':serial(evaluate(p,eta,K,force_L=True)),
        'after':entrant,'scope':'diagnostic demand discontinuity; no global equilibrium claim'}
    for row in result['private_candidates']:
        if row['continuation']['policy']!='L':raise AssertionError('claimed regional continuation failed')
        if max(d['gain'] for d in row['deviations'])>1e-7:raise AssertionError('profitable baseline deviation found')
    assert waste_switches==0
    result['optimizer_nonconvergence_count']=sum(
        d['optimizer']['success'] is False
        for row in result['private_candidates'] for d in row['deviations'])
    out=Path('docs/audit/STAGE30_INDEPENDENT_GAME_RESULTS.json')
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'pairs':result['pair'],'alternatives':result['alternatives'],
                      'random':result['random_profiles']},indent=2))


if __name__=='__main__':main()
