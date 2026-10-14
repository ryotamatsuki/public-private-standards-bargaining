"""Stage7b: alternative *continuous within-open-reference* retrofit technology.

The inherited Stage5 rule charges K+phi*(c_ref^2+a_ref^2)/2
AGAIN whenever two O references differ by any epsilon. As epsilon
tends to zero this induces a discrete K+phi/2 conversion jump and
makes govt policy and first-stage payoffs discontinuous.

This independent stress test REPLACES ONLY the retrofit fee for
O(old)->O(new) with phi*((c_old-c_new)^2+(a_old-a_new)^2)/2.
N->O and proprietary X/Y->O still incur FULL real setup K plus
the original reference deployment fee; same-specification conversion
costs zero. The original sunk fee is never refunded. Not claimed
as uniquely correct engineering technology, just a continuous alternative.

All adoption/proposal/firm actions are recomputed by monkey-patching
the local imported module in a NEW ephemeral Python process.
Do not edit Stage5 source results, which are a separate model.
"""
from fractions import Fraction as F
from collections import Counter,defaultdict
import stage5_integrated_independent_standards_and_government as s

original=s.continuation

def smooth_continuation(pre,policy,ref,flags,K,eta):
    p,w,q,cs,post=original(pre,policy,ref,flags,K,eta)
    p=list(p);w=list(w)
    if policy in ('C','M'):
        for i in range(3):
            if not flags[i] or pre[i]==ref:continue
            # If a firm already uses an O interface, its retrofit
            # cost is a continuous distance-in-design-space cost.
            if pre[i][0]=='O' and ref[0]=='O':
                original_refit=s.cost(ref,K)
                distance=(pre[i][1]-ref[1])**2+(pre[i][2]-ref[2])**2
                revised_refit=s.phi*distance/2
                correction=original_refit-revised_refit
                p[i]+=correction
                w[i]+=correction
    return tuple(p),tuple(w),q,cs,post

def patch():
    from functools import lru_cache
    s.continuation=lru_cache(None)(smooth_continuation)
    s.adoption_pure_nash.cache_clear()
    s.government_policy.cache_clear()

def compare_target():
    a1=('O',F(1),F(0))
    K,eta=F(1,2),F(3,100)
    variants=(F(0),F(1,10000),F(1,1000),F(1,100),F(3,5))
    print('ORIGINAL RETROFIT: same-label tiny mismatch pays all K again.')
    for a in variants:
        h=(s.N,a1,('O',F(1),a))
        pol=s.government_policy(h,K,eta)[0]
        print('old spec epsilon',a,'policy',pol[0],
              'firm3 payoff',float(pol[3][0][2]),flush=True)
    patch()
    print('SMOOTH RETROFIT: same-label change has continuous cost.')
    for a in variants:
        h=(s.N,a1,('O',F(1),a))
        pol=s.government_policy(h,K,eta)[0]
        print('new spec epsilon',a,'policy',pol[0],
              'firm3 payoff',float(pol[3][0][2]),flush=True)
    assert s.government_policy(
       (s.N,a1,('O',F(1),F(1,100))),K,eta)[0][0]=='M'
    assert s.government_policy(
       (s.N,a1,('O',F(1),F(1,1000))),K,eta)[0][0]=='M'
    assert s.government_policy(
       (s.N,a1,('O',F(1),F(1,10000))),K,eta)[0][0]=='M'
    print('PASS selected government discontinuity a->0+ removed locally',
          flush=True)

def collapse_passive_adopter_flags():
    K,eta=F(0),F(3,100)
    examples=((s.N,s.N,('O',F(1),F(0))),
              (s.N,('O',F(1),F(0)),('O',F(1),F(0))))
    for h in examples:
        ref=('O',F(1),F(0))
        eq=s.adoption_pure_nash(h,'C',ref,K,eta)
        outcomes=set((result[0],result[2],result[4])
                     for flags,result in eq)
        print('CERTIFY C pre',h,'strategy_profiles',len(eq),
              'distinct actual allocations/payoffs',len(outcomes),flush=True)
        assert len(outcomes)==1
    print('PASS on-path 2/4 adopter-matching Nash labels were')
    print('behaviorally equivalent redundant reference-holder flags',
          flush=True)

if __name__=="__main__":
    collapse_passive_adopter_flags()
    compare_target()
    print('NOT PROVED: full symmetric continuous refit game SPE;')
    print('new retrofit accounting is an alternate economic model.')
