"""Stage4A CLEAN-ROOM six-actor mechanism audit. Rational independent Cournot KKT.
No import of source payoff, strong() or SPNE verifier. An independent
finite-contract adversarial MODEL CHECKER, NOT full-continuum proof.
All off-path RS outsider messages from the finite menu are exhaustively tested.
"""
from fractions import Fraction as Q
from itertools import product
roles=("G1","F1","G2","F2","G3","F3")
pairs=("12","13","23")
SQ="SQ"

def det3(a):
    (a0,b0,c0),(d0,e0,f0),(g0,h0,i0)=a
    return a0*(e0*i0-f0*h0)-b0*(d0*i0-f0*g0)+c0*(d0*h0-e0*g0)

def solve(A,Y):
    n=len(A)
    if n==1:return (Y[0]/A[0][0],)
    if n==2:
        d=A[0][0]*A[1][1]-A[0][1]*A[1][0]
        return ((Y[0]*A[1][1]-A[0][1]*Y[1])/d,
                (A[0][0]*Y[1]-A[1][0]*Y[0])/d)
    assert n==3
    den=det3(A)
    return tuple(det3([[Y[i] if j==k else A[i][j]
                         for j in range(3)] for i in range(3)])/den
                 for k in range(3))

def participants(c):
    if c[0]=="I":return set(range(6))
    assert c[0]=="R"
    return {i for i,actor in enumerate(roles) if actor[1] in c[1]}

def resulting(profile):
    full={c for c in profile if c!=SQ and
          all(profile[i]==c for i in participants(c))}
    assert len(full)<=1,full
    return next(iter(full)) if full else SQ

def continuation(contract,mu):
    # Independent Cramer's 3x3 solver in NORMALIZED economy A=m=1.
    # mu=(G,Lambda,Delta,rho,F), all rational, stage-2 costs are
    # intercept-minus-marginal-cost A_i =1+rho*s for members.
    g,l,e,r,fee=mu
    if contract==SQ:
        mat=[[Q(1) if i==j else g for j in range(3)]
             for i in range(3)]
        rhs=[Q(1)]*3;member=set();s=Q(0)
    else:
        typ,pair,s=contract
        b=g+l*s;d=g-e*s
        member=set(range(3)) if typ=="I" else {int(ch)-1 for ch in pair}
        mat=[[Q(1) if i==j else b if typ=="I" or
                (i in member and j in member) else d
                for j in range(3)] for i in range(3)]
        rhs=[Q(1)+(r*s if i in member else Q(0)) for i in range(3)]
    foc=[[mat[i][j]+(1 if i==j else 0) for j in range(3)]
         for i in range(3)]
    candidates=[]
    for bitmap in range(1,8):
        active=[i for i in range(3) if bitmap>>i&1]
        coeff=[[foc[i][j] for j in active] for i in active]
        qpart=solve(coeff,[rhs[i] for i in active])
        q=[Q(0)]*3
        for i,qty in zip(active,qpart):q[i]=qty
        if all(q[i]>0 for i in active) and all(
            rhs[i]-sum(foc[i][j]*q[j] for j in range(3))<=0
            for i in range(3) if i not in active):
            candidates.append(tuple(q))
    assert len(candidates)==1,(contract,mu,candidates)
    q=candidates[0]
    cs=sum(q[i]*mat[i][j]*q[j] for i in range(3)
           for j in range(3))/2
    p=tuple(3*q[i]*q[i]-(fee*s*s if i in member else Q(0))
            for i in range(3))
    values=tuple((p[i]+cs if actor[0]=="G" else p[i])
            for actor in roles for i in (int(actor[1])-1,))
    return q,values

def strong_brutish(profile,menu,pay):
    """Enumerate all contract targets, using minimal changer subsets.
    To form new exact named contract, each of its necessary signers NOT
    already announcing it must change. For three countries every
    formed old RS intersects all new RS, so it is automatically broken.
    Additional changers are never required; any added actor would also
    need a strict gain and cannot create a new profitable deviation.
    """
    old=resulting(profile);base=pay[old]
    for target in menu:
        if target==old:continue
        if target==SQ:
            if old!=SQ and any(pay[SQ][i]>base[i]
                               for i in participants(old)):
                return False
            continue
        changers={i for i in participants(target) if profile[i]!=target}
        if not changers:continue
        update=list(profile)
        for i in changers:update[i]=target
        assert resulting(update)==target,(profile,target)
        if all(pay[target][i]>base[i] for i in changers):
            return False
    return True

def ordinary_brutish(profile,menu,pay):
    old=resulting(profile)
    for i in range(6):
        for target in menu:
            if target==profile[i]:continue
            changed=list(profile);changed[i]=target
            if pay[resulting(changed)][i]>pay[old][i]:
                return False
    return True

def theory_matched(c,menu,pay,uniform=False):
    if c==SQ:
        return all(not all(pay[target][i]>pay[SQ][i]
                           for i in participants(target))
                   for target in menu if target!=SQ)
    old=pay[c]
    if any(old[i]<pay[SQ][i] for i in participants(c)):return False
    if c[0]=="I":
        return all(not all(pay[t][i]>old[i]
                    for i in participants(t) if t[0]=="R" or t[0]=="I")
                    for t in menu if t!=SQ)
    # All same-pair Pareto improvements; if another RS pair were
    # profitable, symmetric incumbent pair could make same type.
    if any(all(pay[t][i]>old[i] for i in participants(c))
            for t in menu if t!=SQ and t[0]=="R" and t[1]==c[1]):
        return False
    I=[t for t in menu if t!=SQ and t[0]=="I"]
    test=participants(c) if uniform else set(range(6))
    return all(not all(pay[t][i]>old[i] for i in test) for t in I)

def sample(mu,menu):
    pay={c:continuation(c,mu)[1] for c in menu}
    assert ordinary_brutish([SQ]*6,menu,pay)
    assert strong_brutish([SQ]*6,menu,pay)==theory_matched(SQ,menu,pay)
    scans=0
    for c in menu:
        if c==SQ:continue
        essential=participants(c)
        prof=[c if i in essential else SQ for i in range(6)]
        assert resulting(prof)==c
        exp=all(pay[c][i]>=pay[SQ][i] for i in essential)
        assert ordinary_brutish(prof,menu,pay)==exp
        base=strong_brutish(prof,menu,pay)
        assert base==theory_matched(c,menu,pay),(c,base)
        if c[0]=="R":
            outside=[i for i in range(6) if i not in essential]
            every=True
            for messages in product(menu,repeat=2):
                profile=list(prof)
                for i,mess in zip(outside,messages):profile[i]=mess
                assert resulting(profile)==c
                result=strong_brutish(profile,menu,pay)
                if result:assert base,(c,messages)
                every=every and result
                scans+=1
            assert every==theory_matched(c,menu,pay,uniform=True)
    print("PASS clean-room finite-depth game: menu",len(menu),
          "outsider strategy-profile checks",scans,flush=True)

if __name__=="__main__":
    depths=(Q(1,10),Q(2,5),Q(3,5),Q(13,20),Q(1))
    contracts=(SQ,)+tuple(("R",p,s) for p in pairs for s in depths)+tuple(
        ("I","ALL",s) for s in depths)
    for fee in (Q(1,4),Q(2,5),Q(10)):
        mu=(Q(5,16),-Q(1,16),Q(3,32),Q(1,4),fee)
        sample(mu,contracts)
    # Re-run a distinct demand system with a regional outsider Cournot
    # exit at s=.5 and REENTRY at s=1 (all exact rational values).
    mm=Q(7,10)
    mu=(Q(6,7),-Q(3,7),Q(6,7),Q(10),Q(7,50))
    assert continuation(("R","12",Q(1,2)),mu)[0][2]==0
    assert continuation(("R","12",Q(1)),mu)[0][2]>0
    sample(mu,contracts)
    print("PASS: independent Fraction KKT, ordinary Nash, strong Nash,"
          " RS outsider preannouncements and corners")
