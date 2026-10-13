"""Stage 4: exact finite standards-contract game, coalition blocking, KKT corners.
This is construction-level mathematical evidence, not a novel theorem certificate.
"""
import sympy as S
from itertools import combinations,product
from verify_stage4_independent import payoff as independent_payoff

Q=S.Rational
PARAMS={'a':S.Integer(1),'gamma':Q(1,10),'v':Q(1,10),
        'kappa':Q(1,50),'export_cost':Q(3,20),'royalty':Q(1,25)}
PAIRS=tuple(combinations(range(3),2))
DEALS=tuple((pair,d) for pair in PAIRS for d in (0,1))
PLAYERS=tuple((t,i) for i in range(3) for t in ('G','F'))
SQ=None

def cournot(z,p=PARAMS):
    a,g,v,k,c,r=(p[k] for k in ('a','gamma','v','kappa','export_cost','royalty'))
    M=S.Matrix([[1-v if i==j else g for j in range(3)] for i in range(3)])
    if z is not None:
        (i,j),depth=z
        M[i,j]=M[j,i]=g+k*depth-v
    assert all(S.factor(M[:n,:n].det())>0 for n in (1,2,3)),('NOT_SPD',z)
    B=M+S.diag(*M.diagonal())
    pi=[S.S(0)]*3; CS=[]; quants=[]; active_sets=[]; global_real=S.S(0)
    for dest in range(3):
        C=S.Matrix([0 if i==dest else c for i in range(3)])
        eff=S.Matrix(C)
        if z is not None: eff[z[0][1]]+=r
        # All 2^3 possible Cournot/KKT active sets, including the zero-output state.
        valid=[]
        for n in range(4):
            for active in combinations(range(3),n):
                q=S.zeros(3,1)
                if active:
                    AA=B.extract(active,active)
                    qa=AA.inv()*S.Matrix([a-eff[i] for i in active])
                    for i,qi in zip(active,qa):q[i]=S.factor(qi)
                if any(q[i]<=0 for i in active):continue
                if any(S.factor(a-eff[i]-(B*q)[i])>0 for i in range(3) if i not in active):
                    continue
                valid.append((active,q))
        assert len(valid)==1,('UNRESOLVED_OR_MULTIPLE_COURNOT',z,dest,len(valid))
        active,q=valid[0]
        quants.append(tuple(q));active_sets.append(tuple(active))
        prices=a*S.ones(3,1)-M*q
        for i in active:assert S.factor(prices[i]-eff[i]-M[i,i]*q[i])==0
        CS.append(S.factor((q.T*M*q)[0]/2))
        for i in range(3):pi[i]+=S.factor((prices[i]-eff[i])*q[i])
        royalty_payment=S.S(0)
        if z is not None:
            royalty_payment=r*q[z[0][1]]
            pi[z[0][0]]+=royalty_payment
        real=S.factor(a*sum(q)-(q.T*M*q)[0]/2-(C.T*q)[0])
        assert S.factor(CS[-1]+sum((prices[i]-eff[i])*q[i] for i in range(3))
                        +royalty_payment-real)==0
        global_real+=real
    firms=tuple(S.factor(k) for k in pi)
    govt=tuple(S.factor(CS[i]+pi[i]) for i in range(3))
    assert S.factor(sum(CS)+sum(firms)-global_real)==0
    return {'payoff':{('G',i):govt[i] for i in range(3)}|
                      {('F',i):firms[i] for i in range(3)},
            'q':quants,'active':active_sets,'M':M,'world':global_real}

def signers(z,mode):
    groups=('G','F') if mode=='joint' else (mode,)
    return frozenset((t,i) for t in groups for i in z[0])

def match(msgs,mode):
    matched=[z for z in DEALS if all(msgs[h]==z for h in signers(z,mode))]
    assert len(matched)<=1,'Overlapping bilateral contracts cannot both activate'
    return matched[0] if matched else None

def outcome_stable(z,pay,mode):
    # Lemma 1: pure accepted deal requires every signer >= SQ.
    if z is not None and any(pay[z]['payoff'][h]<pay[None]['payoff'][h] for h in signers(z,mode)):
        return False
    # Lemma 2: another bilateral deal can form by moving just its necessary signers,
    # and this necessarily breaks any incumbent deal (three states only).
    for zz in DEALS:
        if zz==z:continue
        if all(pay[zz]['payoff'][h]>pay[z]['payoff'][h] for h in signers(zz,mode)):
            return False
    return True

def exhaustive_strong(z,pay,mode):
    """Independent direct exhaustive message enumeration (7^6 or 7^3)."""
    players=PLAYERS if mode=='joint' else tuple(h for h in PLAYERS if h[0]==mode)
    start={h:(z if z is not None and h in signers(z,mode) else None) for h in players}
    original=pay[z]['payoff']
    for offers in product((None,*DEALS),repeat=len(players)):
        new=dict(zip(players,offers))
        deviators=tuple(h for h in players if new[h]!=start[h])
        if not deviators:continue
        dest=match(new,mode)
        candidate=pay[dest]['payoff']
        if all(candidate[h]>original[h] for h in deviators):
            return False,(deviators,dest)
    return True,None

def stable_set(pay,mode):
    return tuple(z for z in (None,*DEALS) if outcome_stable(z,pay,mode))

def test():
    pay={z:cournot(z) for z in (None,*DEALS)}
    for z,out in pay.items():
        exact,q=independent_payoff(z)
        for h in PLAYERS:
            assert out['payoff'][h]==S.Rational(exact[h].numerator,exact[h].denominator)
        assert all(tuple(out['q'][k])==tuple(S.Rational(x.numerator,x.denominator)
                         for x in q[k]) for k in range(3))
        assert all(active==(0,1,2) for active in out['active'])
    for mode in ('joint','G','F'):
        for z in (None,*DEALS):
            direct,_=exhaustive_strong(z,pay,mode)
            assert outcome_stable(z,pay,mode)==direct,('STRONG_MISMATCH',mode,z)
    assert stable_set(pay,'joint')==(None,)
    assert stable_set(pay,'G')==(None,)
    assert stable_set(pay,'F')==(((0,2),0),((1,2),0))
    # Negative controls: only one primitive changed; NEVER assert global necessity.
    contrasts={}
    for target,val in (('kappa',Q(0)),('v',Q(0)),('royalty',Q(0)),('gamma',Q(0))):
        np=dict(PARAMS);np[target]=val
        other={z:cournot(z,np) for z in (None,*DEALS)}
        contrasts[target]=(stable_set(other,'joint'),stable_set(other,'F'))
    assert contrasts['kappa'][0]==(None,) and len(contrasts['kappa'][1])>0
    assert contrasts['v']==((None,),(None,))
    assert contrasts['royalty'][0]==contrasts['royalty'][1]
    assert contrasts['gamma'][0]==contrasts['gamma'][1]
    # 3-country 6 contracts, two authorities: firm-only and joint differ,
    # but removing standard-induced differentiation does NOT eliminate it.
    print('PASS EXACT: payoff/W identities, all 7 Cournot continuations, KKT active sets')
    print('PASS INDEPENDENT: Fraction Gaussian evaluator vs SymPy construction')
    print('PASS EXHAUSTIVE: 7^6 joint offer profiles and 7^3 firm-only profiles, every strong deviation')
    print('STRONG outcome joint:',stable_set(pay,'joint'))
    print('STRONG outcome private-only:',stable_set(pay,'F'))
    print('STRONG outcome government-only:',stable_set(pay,'G'))
    print('NEGATIVE CONTROLS:',contrasts)
    print('VERDICT: NO-GO on Stage-3-A as a novel joint differentiation/network bargaining theorem')
    print('LIMIT: finite fixed royalty, pure strongly-stable outcomes, exact selected parameter point.')
if __name__=='__main__':test()
