#!/usr/bin/env python3
"""Clean-room matrix/rational audit. Imports no author research module.

Run from repo root: python code/stage30_independent_exact_audit.py
Output is exact certificates, not a proof-assistant certificate.
"""
import hashlib
import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
import sympy as s

R = s.Rational
m, gam, v, kap, rho, phi = map(R, ['.99','.14','.01','.02','.32','.14'])
a, c, eta = s.symbols('a c eta')
t, u, w, h = s.symbols('t u w h')
qi = (1+rho)/(2*(m+gam-v))
PI = 3*m*qi**2
CI = R(3,2)*(m+2*(gam-v))*qi**2
GI = PI+CI
WI = GI-phi/2
results = {'source':'independent matrix construction; no stage11-27 imports',
           'baseline':'2e96112280599cceaee43b89e265fcb5c073f1ca',
           'certificates':[], 'identities':{}}


def bernstein(expr, variables, name, weak=False):
    """Axiswise triangular basis conversion, exact Fraction arithmetic."""
    p = s.Poly(s.expand(expr), *variables, domain=s.QQ)
    degrees = tuple(int(n) for n in p.degree_list())
    shape = tuple(n+1 for n in degrees)
    arr = np.full(shape, Fraction(0), dtype=object)
    for powers, value in p.terms():
        arr[powers] = Fraction(int(value.p), int(value.q))
    for axis, n in enumerate(degrees):
        old = np.moveaxis(arr, axis, 0)
        new = np.empty_like(old)
        for j in range(n+1):
            acc = np.full(old.shape[1:], Fraction(0), dtype=object)
            for k in range(j+1):
                acc += old[k]*Fraction(math.comb(j,k), math.comb(n,k))
            new[j] = acc
        arr = np.moveaxis(new, 0, axis)
    vals = arr.ravel().tolist()
    minimum, maximum = min(vals), max(vals)
    ok = minimum >= 0 if weak else minimum > 0
    digest = hashlib.sha256('\n'.join(map(str,vals)).encode()).hexdigest()
    out = {'name':name, 'variables':list(map(str,variables)),
           'degrees':degrees, 'count':len(vals), 'min':str(minimum),
           'max':str(maximum),'zeros':int(sum(x==0 for x in vals)),
           'sha256':digest, 'weak':weak, 'pass':bool(ok)}
    results['certificates'].append(out)
    print(json.dumps(out), flush=True)
    if not ok:
        raise AssertionError(name+' independent certificate failed')
    return out


def numden(expr):
    n,d=s.fraction(s.cancel(expr))
    center={x:R(1,2) for x in d.free_symbols}
    center[eta]=R('.12')
    if d.subs(center)<0:n,d=-n,-d
    return n,d


def matrix_polynomial(H,z,stock,indices,variables,prefix):
    A = H + m*s.eye(3)
    D = s.expand(A.det())
    Q = A.adjugate()*z
    twiceCSnum = (Q.T*H*Q)[0]
    for i in indices:
        N = (2*GI-phi*(1-stock[i]**2))*D**2-6*m*Q[i]**2-twiceCSnum
        bernstein(N,variables,prefix+str(i+1),weak=True)


def main():
    # Derive insider/outsider from full 3x3 system, not the author's reduced system.
    H = s.Matrix([[m,gam+kap*a-v*c,gam-eta*a],
                  [gam+kap*a-v*c,m,gam-eta*a],
                  [gam-eta*a,gam-eta*a,m]])
    z = s.Matrix([1+rho*c,1+rho*c,1])
    A = H+m*s.eye(3)
    q = A.inv()*z
    x,y = s.cancel(q[0]),s.cancel(q[2])
    cs = s.cancel((q.T*H*q)[0]/2)
    F = s.cancel(3*m*x*x-phi*(c*c+a*a)/2)
    B = s.cancel(GI-3*m*x*x-cs-phi*(1-c*c)/2)
    results['identities']['Cournot_FOC'] = all(s.cancel(x)==0 for x in A*q-z)
    # Polynomial signs on rectangular supersets of all legal domains.
    low={eta:R('.10')+R('.04')*t,a:R('.75')*u,c:w}
    high={eta:R('.10')+R('.04')*t,a:R('.75')+u/4,c:R('.75')+w/4}
    for name,expr,subs in [('two_low_policy',B,low),
                           ('two_high_negative_private_derivative',-s.diff(F,a),high),
                           ('bilateral_full_c_positive_derivative',s.diff(F,c),
                            {eta:R('.10')+R('.04')*t,a:u,c:w})]:
        n,d=numden(expr)
        bernstein(n.subs(subs),(t,u,w),name+'_numerator')
        bernstein(d.subs(subs),(t,u,w),name+'_denominator')
    f=F.subs(c,1)
    xv=x.subs(c,1);yv=y.subs(c,1);cv=cs.subs(c,1)
    bv=B.subs(c,1)
    kv=s.cancel(WI-3*m*yv**2-cv)
    ke=s.cancel(kv+2*bv)
    kw=s.cancel(3*WI-2*f-3*m*yv**2-3*cv)
    results['identities']['KW_minus_KE'] = s.cancel(kw-ke-phi*a*a)==0
    results['identities']['KE_minus_KV'] = s.cancel(ke-kv-2*bv)==0
    results['identities']['sparse_min_gain'] = str(s.cancel(WI-(3*m+R(3,2)*(m+2*gam))/(4*(m+gam)**2)-R('.56')))
    box={eta:R('.10')+R('.04')*t,a:R('.25')+R('.36')*u}
    broad={eta:R('.14')*t,a:u}
    tests=[('strict_concavity',-s.diff(f,a,2),broad),
           ('positive_a_eta',s.diff(f,a,eta),broad),
           ('member_approval_at_optimal_enclosure',bv,box),
           ('outsider_rejects_at_K_min',R('.54')-kv,box),
           ('founder_does_not_switch_to_M',f-PI+phi/2,box),
           ('outsider_private_profit_above_5478',3*m*yv**2-R('.5478'),box),
           ('outsider_no_public_deviation',3*m*yv**2-(PI-R('.54')-phi/2),box)]
    for label,fun in [('KV',kv),('KE',ke),('KW',kw)]:
        tests.extend([(label+'_decreases_eta',-s.diff(fun,eta),box),
                      (label+'_decreases_a',-s.diff(fun,a),box)])
    for name,expr,subs in tests:
        n,d=numden(expr)
        bernstein(n.subs(subs),(t,u),name+'_numerator')
        bernstein(d.subs(subs),(t,u),name+'_denominator')
    for av, sign in [(R('.25'),1),(R('.61'),-1)]:
        n,d=numden(sign*s.diff(f,a).subs(a,av))
        bernstein(n.subs(eta,R('.10')+R('.04')*t),(t,),f'FOC_at_{av}')
        bernstein(d.subs(eta,R('.10')+R('.04')*t),(t,),f'FOC_den_at_{av}')
    q_upper=(1+rho)/(2*m)
    founder_lower=(1+rho-2*(gam+kap)*q_upper)/(2*m)
    entrant_upper=(1+rho-2*(gam-v)*founder_lower)/(2*m)
    results['identities']['entrant_upper_less_three_fifths']=bool(entrant_upper<R(3,5))
    results['identities']['entrant_quantity_upper']=str(entrant_upper)
    results['identities']['entrant_net_profit_upper']=str(3*m*entrant_upper**2-R('.54'))
    # Three developers: independently form H, adjugate quantities and CS.
    c1=t*u;c2=t
    a1=c1*w;a2=a1+(c2-a1)*h
    H=s.Matrix([[m,gam+kap*a1-v*c1,gam+kap*a1-v*c1],
                [gam+kap*a1-v*c1,m,gam+kap*a2-v*c2],
                [gam+kap*a1-v*c1,gam+kap*a2-v*c2,m]])
    z=s.Matrix([1+rho*c1,1+rho*c2,1+rho*c2])
    matrix_polynomial(H,z,[c1,c2,c2],[1],(t,u,w,h),'three_aligned_gov_')
    a1=c1*w;a3=a1*h
    H=s.Matrix([[m,gam+kap*a1-v*c1,gam+kap*a3-v*c1],
                [gam+kap*a1-v*c1,m,gam+kap*a3-v*c2],
                [gam+kap*a3-v*c1,gam+kap*a3-v*c2,m]])
    matrix_polynomial(H,z,[c1,c2,c2],[0,1],(t,u,w,h),'three_crossed_gov_')
    # Exact rational root bracketing, separate from floating-point illustration.
    roots=[]
    for e in [R('.10'),R('.111'),R('.112'),R('.115'),R('.118'),R('.119'),R('.14')]:
        fn=s.Poly(numden(s.diff(f,a).subs(eta,e))[0],a)
        assert fn.count_roots(0,1)==1
        lo,hi=R(0),R(1)
        for _ in range(40):
            mid=(lo+hi)/2
            if fn.eval(mid)>0:lo=mid
            else:hi=mid
        entry={'eta':str(e),'a_interval':[str(lo),str(hi)]}
        for label,fun in [('KV',kv),('KE',ke),('KW',kw)]:
            # Certified partial derivative in a is negative.
            entry[label+'_interval']=[str(fun.subs({eta:e,a:hi})),str(fun.subs({eta:e,a:lo}))]
        roots.append(entry)
        if e==R('.14'):
            for name,fun in [('diagnostic_cost_g04_member_rejects',R('.04')-bv),
                              ('diagnostic_cost_g04_outsider_rejects',R('.55')+R('.04')-kv)]:
                n,d=numden(fun.subs(eta,e))
                bernstein(n.subs(a,lo+(hi-lo)*t),(t,),name+'_numerator')
                bernstein(d.subs(a,lo+(hi-lo)*t),(t,),name+'_denominator')
    results['rational_roots']=roots
    results['versions']={'sympy':s.__version__,'numpy':np.__version__}
    out=Path('docs/audit/STAGE30_INDEPENDENT_EXACT_RESULTS.json')
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(results,indent=2)+'\n')
    print('INDEPENDENT EXACT BASELINE CERTIFICATES COMPLETE',flush=True)


if __name__=='__main__':main()
