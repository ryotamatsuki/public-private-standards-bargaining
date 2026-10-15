#!/usr/bin/env python3
"""Stage30N — Exact fixed-quorum policy / national incidence counterfactual.

Only rational arithmetic on original two-founder Cournot primitives. The
status of histories as *entire-game* pure SPE comes from Stage30C C1/C3;
this finite checker neither reproves C1 nor validates unrestricted govt Nash.
"""
from fractions import Fraction as Q
from pathlib import Path
import json
m,g,kap,v,rho,phi,eta,K=map(Q,
    [".99",".14",".02",".01",".32",".14",".14",".55"])
def frac(x): return str(x)
def gov_selector(gains,agenda,r):
    assert 1<=r<=3 and agenda
    yes={i for i in range(3) if gains[i]>=0}
    return len(yes)>=r and bool(yes.intersection(agenda))

qI=(1+rho)/(2*(m+g-v))
piI=3*m*qI*qI
CSI=Q(3,2)*(m+2*(g-v))*qI*qI
P=piI-phi/2
WI=P+CSI
public_world=3*(WI-K)

def private(c,a):
    assert 0<=a<=c<=1
    b=g+kap*a-v*c
    d=g-eta*a
    z=1+rho*c
    D=2*m*(2*m+b)-2*d*d
    assert D>0
    numer=2*m*z-d
    x=numer/D
    y=(2*m+b-2*d*z)/D
    C=(m+b)*x*x+2*d*x*y+m*y*y/2
    F=3*m*x*x-phi*(c*c+a*a)/2
    B=piI+CSI-3*m*x*x-C-phi*(1-c*c)/2
    V=WI-3*m*y*y-C
    T=2*F+3*m*y*y+3*C
    # True partial F_a, not a finite-difference estimate.
    dD_da=2*m*kap+4*eta*d
    dx_da=(eta*D-numer*dD_da)/(D*D)
    F_a=6*m*x*dx_da-phi*a
    pi_founder_L=F-K
    pi_founder_M=P-K-phi*a*a/2
    W_founder_L=F-K+C
    W_founder_M=WI-K-phi*a*a/2
    pi_outsider_L=3*m*y*y
    pi_outsider_M=P-K
    W_outsider_L=pi_outsider_L+C
    W_outsider_M=WI-K
    pre_world=T-2*K
    post_world=public_world-phi*a*a
    assert pi_founder_M-pi_founder_L==P-F-phi*a*a/2
    assert W_founder_M-W_founder_L==B
    assert W_outsider_M-W_outsider_L==V-K
    assert 2*W_founder_L+W_outsider_L==pre_world
    assert 2*W_founder_M+W_outsider_M==post_world
    assert (post_world-pre_world)==2*B+V-K
    assert public_world-pre_world==3*WI-T-K
    assert public_world-post_world==phi*a*a
    assert F_a>=0 and F>=P and K>V and B>0,(c,a)
    assert pi_founder_M<=pi_founder_L
    assert W_founder_M>W_founder_L and W_outsider_M<W_outsider_L
    return locals()

def record(a):
    t=private(Q(1),a)
    gains=[t["B"],t["B"],t["V"]-K]
    old={2}; new={0,2}; all_one={2}
    assert gov_selector(gains,old,2)==False
    assert gov_selector(gains,new,2)==True
    assert gov_selector(gains,all_one,3)==False
    assert [x>0 for x in gains]==[True,True,False]
    # same history and same r, only preannounced proposer eligibility changes
    founder_real_cost_L=K+phi*(Q(1)+a*a)/2
    founder_real_cost_M_total=K+phi*(Q(1)+a*a)/2
    outsider_real_cost_L=Q(0)
    outsider_real_cost_M=K+phi/2
    # founder same-history M has sunk a unlike NEW EQUILIBRIUM with a_i=0
    assert founder_real_cost_L==founder_real_cost_M_total
    assert t["post_world"]==public_world-phi*a*a
    return {
        "history":{"firm1":["O","1",str(a)],"firm2":["O","1",str(a)],"firm3":"N"},
        "source_C1_membership_checks":{"F_a":frac(t["F_a"]),
            "F_minus_P":frac(t["F"]-P),"K_minus_V":frac(K-t["V"])},
        "gov_M_minus_L":{"founder1":frac(t["B"]),
            "founder2":frac(t["B"]),"outsider3":frac(t["V"]-K)},
        "firm_M_minus_L":{"founder1":frac(t["pi_founder_M"]-t["pi_founder_L"]),
            "founder2":frac(t["pi_founder_M"]-t["pi_founder_L"]),
            "outsider3":frac(t["pi_outsider_M"]-t["pi_outsider_L"])},
        "national_welfare":{"founder_L":frac(t["W_founder_L"]),
            "founder_same_history_M":frac(t["W_founder_M"]),
            "outsider_L":frac(t["W_outsider_L"]),
            "outsider_same_history_M":frac(t["W_outsider_M"])},
        "resources":{"founder_L_total":frac(founder_real_cost_L),
            "founder_same_history_M_total":frac(founder_real_cost_M_total),
            "outsider_L_total":frac(outsider_real_cost_L),
            "outsider_same_history_M_total":frac(outsider_real_cost_M)},
        "fixed_r2_old_agenda_outsider_only_passes":gov_selector(gains,old,2),
        "fixed_r2_new_agenda_outsider_plus_founder_passes":gov_selector(gains,new,2),
        "r3_outsider_agenda_passes":gov_selector(gains,all_one,3),
        "world_welfare":{"old_private_SPE":frac(t["pre_world"]),
            "new_public_pure_SPE":frac(public_world),
            "same_history_M_after_sunk_private_stocks":frac(t["post_world"]),
            "new_pure_minus_old_pure":frac(public_world-t["pre_world"]),
            "same_history_M_minus_old_L":frac(t["post_world"]-t["pre_world"]),
            "new_pure_minus_old_pure_decimal":float(public_world-t["pre_world"]),
            "old_pure_minus_new_pure_decimal":float(t["pre_world"]-public_world)},
        "status_in_new_institution":(
           "C3 new public pure SPE at same initial profile (a=0)" if a==0 else
           "NOT a new public pure SPE at same history (a>0): sunk a investment could be avoided"
        )
    }
cases=[record(Q(0)),record(Q("0.5"))]
assert cases[0]["world_welfare"]["new_pure_minus_old_pure_decimal"]>0
assert cases[1]["world_welfare"]["new_pure_minus_old_pure_decimal"]<0
assert cases[0]["world_welfare"]["same_history_M_minus_old_L"]==cases[0]["world_welfare"]["new_pure_minus_old_pure"]
assert cases[1]["world_welfare"]["same_history_M_minus_old_L"]!=cases[1]["world_welfare"]["new_pure_minus_old_pure"]

# Fixed A is assigned *before* investment; old private SPE is possible only
# when the actual outsider is the sole eligible proposer, per prior C1.
permutations=[]
for outsider in range(3):
    gains=[Q(1),Q(1),Q(1)]
    gains[outsider]=-Q(1)
    old_agenda={2}; new_agenda={0,2}
    permutations.append({
        "outsider_label_1_based":outsider+1,
        "fixed_old_r2_A3_mandate":gov_selector(gains,old_agenda,2),
        "fixed_new_r2_A13_mandate":gov_selector(gains,new_agenda,2),
        "old_private_SPE_eligible_by_C1":outsider==2,
        "new_private_SPE_eligible_by_C1":False
    })
    assert (not permutations[-1]["fixed_old_r2_A3_mandate"])==(outsider==2)
    assert permutations[-1]["fixed_new_r2_A13_mandate"]

# In old institution all-N yields M, therefore old set includes public SPE,
# not only private ones. Check the all-N approval signs from primitives.
qN=1/(2*(m+g))
csN=Q(3,2)*(m+2*g)*qN*qN
WN=3*m*qN*qN+csN
assert WI-K-WN>0
assert gov_selector([WI-K-WN]*3,{2},2)
assert gov_selector([WI-K-WN]*3,{0,2},2)

out={"scope":"fixed-r=2, A_old={3}, A_new={1,3} preannounced, eta=.14,K=.55",
     "evidence_class":"exact Fraction historical/selector accounting; C1/C3 entire-game SPE status inherited and NOT reproved",
     "source_claims":["C1","C2","C3","C5","C6","C7"],
     "cases":cases,"permutations":permutations,
     "all_N_history_both_institutions_M":True,
     "all_N_gov_delta":frac(WI-K-WN),
     "W_public_equilibrium":frac(public_world),
     "notes":["A does NOT change contingent on which firm is outsider; old A={3} and new A={1,3} fixed by policy design",
         "Old=private-admitting r2 sole outsider proposer; new=broad r2; no quorum reform in this counterfactual",
         "C1/C3 certification supports pure SPE classification; finite exact checker only establishes national gains and policy selector",
         "When a=.5, posthistory forced-M real a investment is sunk; new equilibrium avoids it",
         "No selected equilibrium probabilities, mixed SPE, strategic government-vote equilibria or empirical policy effect",
         "eta,K inside original rectangle, 5 other coefficients fixed"]}
dest=Path("docs/audit/STAGE30N_FIXED_QUORUM_EXACT_RESULTS.json")
dest.parent.mkdir(parents=True,exist_ok=True)
dest.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print("PASS: exact same-r institution-only agenda treatment, 3 outsider labels and two opposite-welfare pure histories")
for row in cases:
    w=row["world_welfare"]
    print("a=",row["history"]["firm1"][2],
        "old L W",float(Q(w["old_private_SPE"])),
        "new pure M W",float(Q(w["new_public_pure_SPE"])),
        "delta",w["new_pure_minus_old_pure_decimal"])
print("Both regimes use r=2; all-N public old equilibrium confirmed. No formal proof claims.")
