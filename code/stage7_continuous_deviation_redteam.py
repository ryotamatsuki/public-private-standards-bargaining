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

if __name__=="__main__":
    k0=screen(F(0),F(3,100))
    kh=screen(F(1,2),F(3,100))
    print("CAUTION: a finite rational neighborhood SCREEN cannot PROVE",
          "survivors' unrestricted c,a optimality or all-mixed SPE.",flush=True)
