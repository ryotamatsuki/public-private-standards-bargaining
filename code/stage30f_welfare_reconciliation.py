#!/usr/bin/env python3
"""Stage7 resource accounting: fresh rational 3x3 matrices, not a new SPE proof.

Verified objects: price, CS and profit from primitive linear demand;
national vs world profit/CS accounting; before-investment vs after-investment
mandate comparisons; same-parameter opposite-welfare equilibria already
certified by Stage30C C1. This is exact Fraction arithmetic only.

No author Stage30/30B production solver imported. It verifies welfare equations
on rational designs; it does not certify all pure-strategy SPE or a novel theory.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

m, gam, v, kap, rho, phi = (Q(x) for x in [".99",".14",".01",".02",".32",".14"])
K, eta = Q(".55"), Q(".14")

def solve(A,z):
    n=len(z); b=[list(row)+[z[i]] for i,row in enumerate(A)]
    for j in range(n):
        pivot=next(i for i in range(j,n) if b[i][j]!=0)
        b[j],b[pivot]=b[pivot],b[j]
        t=b[j][j];b[j]=[x/t for x in b[j]]
        for i in range(n):
            if i!=j:
                t=b[i][j]
                b[i]=[b[i][k]-t*b[j][k] for k in range(n+1)]
    return [b[i][-1] for i in range(n)]

def market(c,a,public=False):
    if public:
        z=[1+rho]*3
        off=gam-v
        H=[[m if i==j else off for j in range(3)]for i in range(3)]
    else:
        z=[1+rho*c,1+rho*c,Q(1)]
        b=gam+kap*a-v*c;d=gam-eta*a
        H=[[m,b,d],[b,m,d],[d,d,m]]
    A=[[H[i][j]+(m if i==j else 0) for j in range(3)]for i in range(3)]
    q=solve(A,z)
    cs=sum(q[i]*H[i][j]*q[j] for i in range(3) for j in range(3))/2
    return {"q":q,"cs":cs,"gross":[3*m*x*x for x in q],
            "price":[z[i]-sum(H[i][j]*q[j] for j in range(3)) for i in range(3)]}

pub=market(Q(1),Q(0),True)
piI=pub["gross"][0];CSI=pub["cs"]
P=piI-phi/2
WI=P+CSI

def audit(c,a):
    L=market(c,a)
    x,y=L["q"][0],L["q"][2]
    C=L["cs"]
    F=L["gross"][0]-phi*(c*c+a*a)/2
    T=2*F+L["gross"][2]+3*C
    wprivate=T-2*K
    wpublic=3*(WI-K)
    wmandated_post=wpublic-phi*a*a
    pchange=piI-L["gross"][0]-phi*(1-c*c)/2
    B=piI+CSI-L["gross"][0]-C-phi*(1-c*c)/2
    V=WI-L["gross"][2]-C
    national_L=[F-K+C,F-K+C,L["gross"][2]+C]
    national_M=[WI-K-phi*a*a/2,WI-K-phi*a*a/2,WI-K]
    assert sum(national_L)==wprivate
    assert sum(national_M)==wmandated_post
    assert national_M[0]-national_L[0]==B
    assert national_M[2]-national_L[2]==V-K
    assert pchange==P-F-phi*a*a/2
    assert B-pchange==CSI-C
    assert wpublic-wprivate==3*WI-T-K
    assert wmandated_post-wprivate==2*B+V-K
    assert (wpublic-wprivate)-(wmandated_post-wprivate)==phi*a*a
    assert all(pub["price"][i]==m*pub["q"][i] for i in range(3))
    assert all(L["price"][i]==m*L["q"][i] for i in range(3))
    return {"c":str(c),"a":str(a),"gap_private_minus_public":str(wprivate-wpublic),
            "gap_private_minus_public_decimal":float(wprivate-wpublic),
            "founder_firm_public_minus_private":str(pchange),
            "founder_government_policy_gain":str(B),
            "outsider_government_policy_gain":str(V-K),
            "post_welfare_gain":str(wmandated_post-wprivate),
            "pre_public_minus_private":str(wpublic-wprivate),
            "sunken_commonality_gap":str(phi*a*a),
            "founder_CS_gain":str(CSI-C),
            "founder_support":bool(B>0),"outsider_veto":bool(V-K<0)}

samples=[audit(Q(1),Q(0)),audit(Q(1),Q(".5")),audit(Q(".95"),Q(0))]
assert samples[0]["gap_private_minus_public_decimal"] < -.10
assert samples[1]["gap_private_minus_public_decimal"] > .04
assert samples[2]["gap_private_minus_public_decimal"] < -.17
for x in samples:
    assert x["founder_support"] and x["outsider_veto"]
    assert Q(x["founder_firm_public_minus_private"])<=0

output={"purpose":"Stage7 exact sample welfare reconciliation, not theorem novelty or full SPE proof",
        "parameters":{"eta":str(eta),"K":str(K)},
        "public":{"PI":str(piI),"CS":str(CSI),"WI":str(WI)},
        "samples":samples,
        "inference_limits":"Prior Stage30C proves sample eligibility; this script checks only matrix and accounting identities."}
out=Path("docs/audit/STAGE30F_WELFARE_RECONCILIATION.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(output,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("PASS: three exact rational private/public Cournot matrices; national/world accounts reconcile.")
for x in samples:print("O(",x["c"],",",x["a"],"): private-public world welfare",x["gap_private_minus_public_decimal"])
print("This is NOT a new SPE certificate or real-world welfare estimate.")
