#!/usr/bin/env python3
"""Stage30O cross-stage regression for recovered ST26 timing witness only.

Independent rational substitution into unchanged bilateral Cournot primitives,
NOT independent derivation of global a* existence/uniqueness, original Stage26
full-domain Bernstein signs, or paper priority. Do not trust floating-point as
the certificate; all assertions use Fraction and source a* isolating bracket.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
v,g,kappa,rho,phi,eta,K=map(Q,[".01",".14",".02",".32",".14",".115",".55"])
m=1-v
qI=(1+rho)/(2*(m+g-v))
piI=3*m*qI*qI
CSI=Q(3,2)*(m+2*(g-v))*qI*qI
P=piI-phi/2
WI=P+CSI
def measure(a):
    c=Q(1)
    b=g+kappa*a-v*c
    d=g-eta*a
    z=1+rho*c
    D=2*m*(2*m+b)-2*d*d
    assert D>0
    nx=2*m*z-d
    x=nx/D
    y=(2*m+b-2*d*z)/D
    C=(m+b)*x*x+2*d*x*y+(m/2)*y*y
    F=3*m*x*x-phi*(c*c+a*a)/2
    Da=2*m*kappa+4*eta*d
    xa=(eta*D-nx*Da)/(D*D)
    Fa=6*m*x*xa-phi*a
    B=piI+CSI-3*m*x*x-C # no c completion cost c=1
    V=WI-3*m*y*y-C
    T=2*F+3*m*y*y+3*C
    KV=V
    KE=V+2*B
    KW=3*WI-T
    assert KW-KE==phi*a*a # exact after-history vs ex-ante
    assert V<KE<KW
    assert B>0 and F>P and K>V
    return {k:x for k,x in locals().items() if k in ["a","Fa","B","KV","KE","KW","F","V","P","T"]}
lo=Q(39823,100000)
hi=Q(39825,100000)
low=measure(lo)
high=measure(hi)
assert low["Fa"]>0 and high["Fa"]<0
for y in (low,high):
    assert y["KV"]<y["KE"]<K<y["KW"]
    assert y["KW"]-K>0 and y["KE"]-K<0
    assert K>y["V"] and y["F"]>=P
# The root is UNIQUE only by *inherited* strict concavity proof Stage11, NOT
# proved by endpoint signs in this single witness checker.
mid=(lo+hi)/2
approx=measure(mid)
out={
"verdict":"EXACT RATIONAL LOCAL WITNESS (source global uniqueness inherited Stage11/26), not full original proof",
"eta":str(eta),"K":str(K),
"root_bracket":[str(lo),str(hi)],
"at_lower":{"Fa":str(low["Fa"]),"KV":str(low["KV"]),"KE":str(low["KE"]),"KW":str(low["KW"])},
"at_upper":{"Fa":str(high["Fa"]),"KV":str(high["KV"]),"KE":str(high["KE"]),"KW":str(high["KW"])},
"midpoint_illustration":{x:float(approx[x]) for x in ["a","KV","KE","KW"]},
"hard_conditions":[
 "Fa(left)>0>Fa(right) exact; unique root by earlier global f_aa<0 stage11",
 "KV<KE<KW and KE<.55<KW at BOTH rational endpoints",
 "KW-KE=phi*a^2 exactly",
 "K>V and F>=P allow private policy history; full private SPE iff inherited C1",
 "not a certified sign/monotonic check over full eta,K rectangle",
 "not welfare empirical observation or equilibrium probability"
 ]}
path=Path("docs/audit/STAGE30O_TIMING_RATIONAL_SPOTCHECK.json")
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print("PASS: rational Stage26 eta=.115,K=.55 a* bracket, KV<KE<KW, KE<K<KW, F>=P and K>V.")
print("Approx illustrative KV,KE,KW:",out["midpoint_illustration"])
print("No new theorem or general global proof is certified by this spot-check.")
