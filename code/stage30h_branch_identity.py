#!/usr/bin/env python3
"""Exact Stage30H demand-branch identity checks, NOT an economic microfoundation.

Original model unchanged. The interpretation K=paid baseline family qualification
is an economic reading of the already existing binary N/O action and cost K;
this program checks only its fit to the original H,z branches and expenses.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

g,kappa,v,rho,eta,m,phi,K=map(Q,[".14",".02",".01",".32",".14",".99",".14",".55"])

def mat(actions):
    """N=None, O=(c,a), zero-cost production exit NOT identified with N."""
    idx=[i for i,a in enumerate(actions) if a is not None]
    H=[[m if i==j else g for j in range(3)] for i in range(3)]
    z=[Q(1)]*3
    if len(idx)<2:
        return H,z
    if len(idx)==2:
        i,j=idx
        c=min(actions[i][0],actions[j][0])
        a=min(actions[i][1],actions[j][1])
        for u in (i,j):z[u]+=rho*c
        H[i][j]=H[j][i]=g+kappa*a-v*c
        o=({0,1,2}-{i,j}).pop()
        H[i][o]=H[o][i]=H[j][o]=H[o][j]=g-eta*a
        return H,z
    for i in range(3):
        z[i]+=rho*max(min(actions[i][0],actions[j][0]) for j in range(3) if j!=i)
        for j in range(i+1,3):
            c=min(actions[i][0],actions[j][0])
            a=min(actions[i][1],actions[j][1])
            H[i][j]=H[j][i]=g+kappa*a-v*c
    return H,z

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def det3(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])

def render(actions):
    h,z=mat(actions)
    return {"actions":[None if x is None else [str(t)for t in x] for x in actions],
        "z":[str(x) for x in z],
        "H":[[str(x)for x in line]for line in h],
        "leading_minors":[str(h[0][0]),str(det2(h)),str(det3(h))]}
C=Q(1);a=Q(".5");o0=(Q(0),Q(0));founder=(C,a)
before=mat([founder,founder,None])
after=mat([founder,founder,o0])
assert before[1]==after[1]==[Q("1.32"),Q("1.32"),Q(1)]
assert before[0][0][1]==after[0][0][1]==g+kappa*a-v*C
assert before[0][0][2]==before[0][1][2]==Q(".07")
assert after[0][0][2]==after[0][1][2]==Q(".14")
assert after[0][0][2]-before[0][0][2]==eta*a
# In the special a=0, there is NO status-driven cross-effect difference.
h0,_=mat([(C,Q(0)),(C,Q(0)),None])
h3,_=mat([(C,Q(0)),(C,Q(0)),o0])
assert h0[0][2]==h3[0][2]==g
# Membership with c=a=0 has no standalone demand benefit in singleton states.
hN,zN=mat([None,None,None])
h1,z1=mat([o0,None,None])
assert hN==h1 and zN==z1
# Two baseline-only open members also generate exactly the original N demand.
h2,z2=mat([o0,o0,None])
assert hN==h2 and zN==z2
# Positive entrant c/a changes technology component after categorical jump.
third=(Q(".1"),Q(".05"))
positive=mat([founder,founder,third])
assert positive[0][0][2]==g+kappa*third[1]-v*third[0]
assert positive[1][2]==1+rho*third[0]  # 3rd gets positive shared c
# Fixed K is real setup cost under O, no double payment after M; N pays K anew.
cost_N=K+phi/2
cost_O=lambda c,a:K+phi*(c*c+a*a)/2 +phi*(1-c*c)/2
assert cost_O(Q(0),Q(0))==cost_N
assert cost_O(C,a)==cost_N+phi*a*a/2
cases={
    "no_open":render([None,None,None]),
    "singleton_O00":render([o0,None,None]),
    "bilateral_O00":render([o0,o0,None]),
    "bilateral_founders_with_N":render([founder,founder,None]),
    "three_open_third_O00":render([founder,founder,o0]),
    "bilateral_founders_a_zero_with_N":render([(C,Q(0)),(C,Q(0)),None]),
    "three_open_third_O00_founder_a_zero":render([(C,Q(0)),(C,Q(0)),o0]),
    "three_open_positive_third_stocks":render([founder,founder,third])
}
for name,case in cases.items():
    for x in case["leading_minors"]:assert Q(x)>0,(name,x)
report={
    "scope":"Exact original demand branch and K resource accounting, NOT real demand validation",
    "eta":str(eta),"K":str(K),
    "founder_outsider_status_jump":str(eta*a),
    "cases":cases,
    "mandatory_cost_new_N":str(cost_N),
    "mandatory_cost_prior_O00":str(cost_O(Q(0),Q(0))),
    "mandatory_cost_prior_O1a":str(cost_O(C,a)),
    "interpretive_verdict":"PASS restricted category-membership interpretation; NOT a derived or empirical microfoundation",
    "source_status":"Three final published comparator articles still unresolved Stage6"
}
dest=Path("docs/audit/STAGE30H_BRANCH_IDENTITY_RESULTS.json")
dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print("PASS: 8 exact demand-branch histories, resource K reuse and SPD minors.")
print("Exact founder-outsider cross-effect jump, N -> O(0,0):",str(eta*a))
print("No physical-compatibility-only explanation or journal priority certified.")
