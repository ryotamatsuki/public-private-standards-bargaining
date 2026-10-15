#!/usr/bin/env python3
"""Exact boundary demonstration of paid O(0,0) binary family membership.

Verifies the existing demand model's discrete change and positive definiteness
at a representative legal history. Not a demand microfoundation, novelty audit,
general equilibrium proof, or robustness test for another technology.
"""
from fractions import Fraction as Q
import json
from pathlib import Path

m=Q("0.99")
gamma=Q("0.14")
kappa=Q("0.02")
v=Q("0.01")
eta=Q("0.14")
rho=Q("0.32")
K=Q("0.55")
c=Q(1)
a=Q("0.5")
def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]
def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
def matrix(discrete_open):
    h12=gamma+kappa*a-v*c
    h13=gamma if discrete_open else gamma-eta*a
    H=[[m,h12,h13],[h12,m,h13],[h13,h13,m]]
    z=[1+rho,1+rho,Q(1)]  # c3=0: intercept does NOT change
    return H,z
HN,zN=matrix(False)
HO,zO=matrix(True)
assert zN==zO
assert HN[0][1]==HO[0][1]
assert HO[0][2]-HN[0][2]==eta*a==Q("0.07")
assert HN[0][2]==Q("0.07")
assert HO[0][2]==Q("0.14")
assert all(HN[i][i]==HO[i][i] for i in range(3))
for H in (HN,HO):
    assert H[0][0]>0 and det2(H)>0 and det3(H)>0
# When private design a=0, the two demand branches agree for third O(0,0)
assert eta*Q(0)==0

data={
    "purpose":"Stage7.5 economic primitive mismatch, not an alternative-model proof",
    "founders":["O(1,0.5)","O(1,0.5)"],
    "outsider_before":"N",
    "outsider_after":"O(0,0), pays K=0.55",
    "z_unchanged":[str(x) for x in zN],
    "H_before":[[str(x)for x in row]for row in HN],
    "H_after":[[str(x)for x in row]for row in HO],
    "founder_outsider_cross_effect_jump":str(HO[0][2]-HN[0][2]),
    "general_formula":"eta * a",
    "leading_principal_det_before":[str(HN[0][0]),str(det2(HN)),str(det3(HN))],
    "leading_principal_det_after":[str(HO[0][0]),str(det2(HO)),str(det3(HO))],
    "status":"EXACT REDUCED-FORM DIFFERENCE ONLY; ECONOMIC EXPLANATION UNRESOLVED"
}
out=Path("docs/audit/STAGE30G_PRIMITIVE_BOUNDARY_RESULTS.json")
out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("PASS: paid O(0,0) entrant causes exact H13=H23 0.07 -> 0.14 jump.")
print("All market intercepts remain unchanged; both symmetric H matrices are positive definite.")
print("No economic microfoundation or generality theorem is certified by this calculation.")
