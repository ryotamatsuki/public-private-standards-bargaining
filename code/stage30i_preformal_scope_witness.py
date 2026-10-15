#!/usr/bin/env python3
"""Stage30I: preformal boundary and theorem-scope witnesses only.

Stdlib Fraction; derives examples from the original 2-founder primitive demand.
This is NOT a Lean formal proof, complete SPE theorem, priority novelty check,
source manuscript validation, new model, or generic portability certificate.
"""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json

m, g, kap, v, rho, phi = [Q(s) for s in (".99",".14",".02",".01",".32",".14")]
eta=Q(".14")
K=Q(".55")
def pair(c,a,eta=eta):
    assert Q(0)<=a<=c<=1
    b=g+kap*a-v*c
    d=g-eta*a
    z=1+rho*c
    D=2*m*(2*m+b)-2*d*d
    assert D>0
    x=(2*m*z-d)/D
    y=(2*m+b-2*d*z)/D
    C=(m+b)*x*x+2*d*x*y+m*y*y/2
    F=3*m*x*x-phi*(c*c+a*a)/2
    return x,y,C,F
qI=(1+rho)/(2*(m+g-v))
PI=3*m*qI*qI
CSI=Q(3,2)*(m+2*(g-v))*qI*qI
P=PI-phi/2
WI=P+CSI
def vals(c,a):
    x,y,C,F=pair(c,a)
    B=PI+CSI-3*m*x*x-C-phi*(1-c*c)/2
    V=WI-3*m*y*y-C
    T=2*F+3*m*y*y+3*C
    firm_delta=P-F-phi*a*a/2
    pub=3*(WI-K)
    priv=T-2*K
    # Same-history policy change versus ex-ante cross-constitution comparison
    post=pub-phi*a*a
    assert post-priv==2*B+V-K
    assert pub-priv==3*WI-T-K
    assert (pub-priv)-(post-priv)==phi*a*a
    assert B-firm_delta==CSI-C
    return {"c":str(c),"a":str(a),"F_minus_P":str(F-P),"B":str(B),
        "V":str(V),"firm_policy_gain":str(firm_delta),
        "private_minus_public":str(priv-pub),
        "private_minus_public_decimal":float(priv-pub)}
points={}
for label,c,a in [
    ("low_private",Q(1),Q(0)),
    ("high_private",Q(1),Q(".5")),
    ("other_low_private",Q(".95"),Q(0)),
    ("inclusion_witness",Q(".929"),Q(0)),
    ("participation_lower_bracket",Q(".928"),Q(0))
]:
    points[label]=vals(c,a)

assert Q(points["low_private"]["private_minus_public"])<0
assert Q(points["high_private"]["private_minus_public"])>0
for label in ["low_private","high_private","other_low_private","inclusion_witness"]:
    p=points[label]
    assert Q(p["F_minus_P"])>=0
    assert Q(p["firm_policy_gain"])<=0
    assert Q(p["B"])>0
    assert Q(".55")>Q(p["V"])
assert Q(points["participation_lower_bracket"]["F_minus_P"])<0
assert Q(points["inclusion_witness"]["F_minus_P"])>0
# C4: one existential strict inclusion witness, not ∀K strict inclusion
V=Q(points["inclusion_witness"]["V"])
assert Q(".54")<V<Q(".55")
# Certification at the knife edge is a SET/TIE rule, not a new game.
def mandate(yes,agenda,r):
    assert 1<=r<=3 and len(agenda)>0
    return sum(yes)>=r and any(yes[i] for i in agenda)

# Exhaustive 3^3 policy-gain sign/tie states, every possible agenda and quorum.
# Nonnegative delta means YES even on exact equality.
cases=0
for gains in product([-1,0,1],repeat=3):
    yes=[z>=0 for z in gains]
    for mask in range(1,8):
        agenda=[i for i in range(3) if mask & (1<<i)]
        for r in (1,2,3):
            result=mandate(yes,agenda,r)
            assert result == (sum(z>=0 for z in gains)>=r and any(gains[i]>=0 for i in agenda))
            cases+=1
assert cases==567
# Even unanimous positive *preferences* don't guarantee passage in an
# unrestricted simultaneous voting game with r>=2. All NO is Nash:
# no single unilateral switch from NO to YES can reach r=2.
all_no=[False]*3
for i in range(3):
    new=all_no.copy();new[i]=True
    assert sum(new)<2
# Boundary: under stipulated selector outsider's K=V is YES, not NO.
founders_gain=[Q(1),Q(1)]
assert mandate([True,True,True],[2],2)
assert not mandate([True,True,False],[2],2)
assert mandate([True,True,False],[0,2],2)

# Cost identity for N vs O(0,0) under public mandate; the action labels differ.
cost_N=K+phi/2
def total_cost_prior_O(c,a):
    return K+phi*(c*c+a*a)/2+phi*(1-c*c)/2
assert total_cost_prior_O(Q(0),Q(0))==cost_N
assert total_cost_prior_O(Q(1),Q(".5"))==cost_N+phi*Q(".5")**2/2

out={
    "status":"PREFORMAL RATIONAL SCOPE WITNESSES ONLY — NOT FORMAL PROOF",
    "claim_context":"C1-C7 Stage30C baseline under prescribed sincere selector",
    "scope":{"five_fixed_constants":[str(x) for x in [v,g,kap,rho,phi]],
             "eta_interval":["1/10","7/50"],"K_interval":["27/50","14/25"],
             "one_private_history_parameter_eta":str(eta),
             "one_private_history_parameter_K":str(K),
             "policy_sign_tie_cases":cases},
    "witnesses":points,
    "one_strict_inclusion_witness":{"K1":"27/50","K2":"11/20","V":str(V),
      "only_existential_strictness":True},
    "other_negative_scope":{"r2_unrestricted_all_NO_is_nonpivotal_Nash":True,
        "prescribed_selector_uses_yes_on_tie":True,
        "all_initial_public_profiles_not_unique":True,
        "no_claim_of_mixed_or_seven_parameter_spe":True},
    "not_certified":[
        "C1 entire global finite-deviation pure SPE iff",
        "C2 public a=0 from all possible strategic deviations",
        "C3 exact full broad-agenda initial equilibrium correspondence",
        "C5 welfare envelope and root signs on the full parameter rectangle",
        "C6 universal all-equilibrium iff from the model",
        "formal Lean/mathlib kernel acceptance",
        "complete Stage7.5A portability audit",
        "Stage6 published theorem priority"]
}
path=Path("docs/audit/STAGE30I_PREFORMAL_RATIONAL_RESULTS.json")
path.parent.mkdir(exist_ok=True,parents=True)
path.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print("PASS: 567 prescribed policy selector sign/tie cases and three-course rational welfare identities.")
print("PASS: strict K inclusion witness, weak firm preference and same-parameter opposite-welfare private histories.")
print("IMPORTANT: These are finite rational checks, not universal theorem or formal-verification PASS.")
