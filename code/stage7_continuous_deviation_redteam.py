"""Stage7: adversarial OFF-MENU continuous unilateral deviations from finite SPE.

Does NOT assume a 10-action Nash equilibrium remains SPE when agents
can select all real 0<=a_i<=c_i<=1. Checks a rational near-neighbor
test set and emits exact Fraction payoff gaps, including government's
policy and the firm adoption selection used in source Stage5.

Source Stage5 selects a W-max adoption Nash. A detected strictly
profitable deviation refutes ONLY THAT continuation selection, not
every possible full mixed-subgame SPE continuation.

Outputs counterexample data for later independent local symbolic proof.
"""
from fractions import Fraction as F
from collections import Counter
from stage5_integrated_independent_standards_and_government import (
    firm_nash,government_policy,adoption_pure_nash,ACTIONS,N,PUBLIC,
    final_type)

def variants(old):
    label,c,a=old
    designs=(
        (F(1,100),F(0)),(F(1,4),F(0)),(F(49,100),F(0)),
        (F(1,2),F(0)),(F(51,100),F(0)),
        (F(7,10),F(0)),(F(9,10),F(0)),(F(99,100),F(0)),
        (F(1),F(0)),
        (F(1),F(1,100)),(F(1),F(3,10)),
        (F(1),F(1,2)),(F(1),F(59,100)),
        (F(1),F(3,5)),(F(1),F(61,100)),
        (F(1),F(7,10)),(F(99,100),F(3,5)),
        (F(1,2),F(1,5)),
        (F(4,5),F(3,5)),
    )
    vals=[N]
    for lab in ('X','Y','O'):
        for cc,aa in designs:
            assert F(0)<=aa<=cc<=1
            vals.append((lab,cc,aa))
    return [d for d in vals if d not in ACTIONS and d!=old]

def screen(K,eta,limit=20):
    e=firm_nash(K,eta)
    print("Finite-menu SPE count",K,len(e),flush=True)
    n_checked=0
    cracks=[]
    survived=[]
    for h,pol in e:
        base=pol[3][0]
        got=None
        for i in range(3):
            for d in variants(h[i]):
                hh=tuple(d if j==i else h[j] for j in range(3))
                pp=government_policy(hh,K,eta)[0]
                n_checked+=1
                advantage=pp[3][0][i]-base[i]
                if advantage>0:
                    got=(i,h[i],d,advantage,pp[0],
                         final_type(hh,pp),len(
                             adoption_pure_nash(hh,pp[0],pp[1],K,eta))
                         if pp[0]!='L' else 1)
                    break
            if got:break
        if got:
            cracks.append((h,pol[0],final_type(h,pol),got))
            print("COUNTEREXAMPLE","K",K,"initial",h,
                  "initial_policy",pol[0],"final",final_type(h,pol),
                  "deviating_firm",got[0],
                  "old",got[1],"new",got[2],"GAIN",got[3],
                  "offpath_policy",got[4],"offpath_final",got[5],
                  "offpath_adoption_NE",got[6],flush=True)
        else:
            survived.append((h,pol[0],final_type(h,pol)))
    print("SCREEN SUMMARY K",K,"of",len(e),
          "profitable rational continuous deviants",len(cracks),
          "survive this restricted probe",len(survived),
          "checks",n_checked,flush=True)
    if survived:
        for item in survived:print("NOT YET REFUTED",item,flush=True)
    return cracks,survived

def targeted_policy_discontinuity():
    K,eta=F(1,2),F(3,100)
    a1=('O',F(1),F(0))
    a3=('O',F(1),F(3,5))
    initial=(N,a1,a3)
    initialpolicy,_=government_policy(initial,K,eta)
    print("WITNESS ORIGINAL POLICY",initialpolicy[0],
          "P3",initialpolicy[3][0][2],flush=True)
    candidate=(
        ('original',a3),
        ('finite_action_same_spec',('O',F(1),F(0))),
        ('offmenu_99pct',('O',F(99,100),F(0))),
        ('offmenu_999pct',('O',F(999,1000),F(0))),
        ('offmenu_9999pct',('O',F(9999,10000),F(0))),
        ('offmenu_unified_c_marginal_a',('O',F(1),F(1,100))),
    )
    for tag,d in candidate:
        h=(N,a1,d)
        pol,options=government_policy(h,K,eta)
        gain=pol[3][0][2]-initialpolicy[3][0][2]
        print("DIRECT EXACT WITNESS",tag,
              "firm3action",d,"policy",pol[0],
              "firm3_profit",pol[3][0][2],"DIFF",gain,
              "float",float(gain),
              "gov_feasible_options",tuple(
                  (z[0],z[1],sum(z[3][1]),z[3][1][0])
                  for z in options),
              flush=True)
    # STRONGEST simple analytical witness: c unchanged, only private
    # common-design excess reduced. Pair min(a2,a3) stays exactly ZERO,
    # so all Cournot payoffs and public L remain unchanged; the firm
    # saves exactly phi/2*(.6^2-.01^2)=25193/1000000.
    easy=government_policy((N,a1,('O',F(1),F(1,100))),K,eta)[0]
    assert easy[0]=='L'
    assert easy[3][0][2]-initialpolicy[3][0][2]==F(25193,1000000)
    print("PASS EXACT SIMPLE OFFMENU DEVIATION with no output change",
          F(25193,1000000),flush=True)
    assert government_policy(
        (N,a1,('O',F(99,100),F(0))),K,eta)[0][0]=='L'
    assert government_policy(
        (N,a1,('O',F(999,1000),F(0))),K,eta)[0][0]=='L'
    assert government_policy(
        (N,a1,('O',F(9999,10000),F(0))),K,eta)[0][0]=='L'
    assert government_policy(
        (N,a1,('O',F(1),F(0))),K,eta)[0][3][0][2]<=initialpolicy[3][0][2]
    assert government_policy(
        (N,a1,('O',F(9999,10000),F(0))),K,eta)[0][3][0][2]>initialpolicy[3][0][2]
    print("PASS exact knife-edge certifiable technology mismatch",flush=True)


def onpath_multiple_adopter_ne():
    from stage5_integrated_independent_standards_and_government import (
        continuation)
    for K in (F(0),F(1,2)):
        es=firm_nash(K,F(3,100))
        counts=Counter()
        examples=[]
        for h,pol in es:
            if pol[0]=='L':
                counts['L']+=1
                continue
            n=len(adoption_pure_nash(h,pol[0],pol[1],K,F(3,100)))
            counts[n]+=1
            if n>1:examples.append((h,pol[0],n))
        print("ONPATH ADOPTION MULTIPLICITY K",K,
              "eq counts",counts,"examples",examples[:5],flush=True)


if __name__=="__main__":
    targeted_policy_discontinuity()
    onpath_multiple_adopter_ne()
    k0=screen(F(0),F(3,100))
    kh=screen(F(1,2),F(3,100))
    print("CAUTION: a finite rational neighborhood SCREEN cannot PROVE",
          "survivors' unrestricted c,a optimality or all-mixed SPE.",flush=True)
