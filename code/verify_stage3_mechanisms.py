"""Stage 3 bounded pre-theorem mechanism screen (exact rational SymPy).
This is NOT a new-game existence/uniqueness theorem or novel-result certificate.
Compatible with current frozen Stage-1 one-shot two-key standard contract economy.
"""
import sympy as s

Q=s.Rational
R=s.symbols("r",real=True)
PARAM={"a":Q(1),"gamma":Q(3,20),"v":Q(9,50),
       "kappa":Q(1,20),"c_foreign":Q(1,20)}

def solve_market(link=False,depth=0,royalty=Q(0),param=PARAM):
    a,g,v,kappa,c=(param[z] for z in ["a","gamma","v","kappa","c_foreign"])
    n=3
    M=s.Matrix([[1-v if i==j else g for j in range(n)] for i in range(n)])
    if link:
        M[0,1]=M[1,0]=g+kappa*depth-v
    assert M.is_positive_definite, "positive-definite utility required"
    B=M+s.diag(*M.diagonal())
    firm=[s.Integer(0)]*n
    cs=[]
    for destination in range(n):
        real_cost=s.Matrix([Q(0) if i==destination else c for i in range(n)])
        private_cost=s.Matrix(real_cost)
        if link:private_cost[1]+=royalty
        quantities=B.inv()*(a*s.ones(n,1)-private_cost)
        prices=a*s.ones(n,1)-M*quantities
        for i in range(n):
            assert s.cancel(prices[i]-private_cost[i]-M[i,i]*quantities[i])==0
            if royalty.is_number:
                assert quantities[i].is_positive
            firm[i]+=s.factor((prices[i]-private_cost[i])*quantities[i])
        if link:
            firm[0]+=royalty*quantities[1]
        surplus=s.factor((quantities.T*M*quantities)[0]/2)
        cs.append(surplus)
        real_welfare=s.factor(a*sum(quantities)-surplus-(real_cost.T*quantities)[0])
        transfer=royalty*quantities[1] if link else Q(0)
        assert s.cancel(surplus+sum((prices[i]-private_cost[i])*quantities[i] for i in range(n))+transfer-real_welfare)==0
    firm=tuple(s.factor(p) for p in firm)
    gov=tuple(s.factor(firm[i]+cs[i]) for i in range(n))
    return gov,firm,tuple(cs),M

def diff(contract,baseline):
    return tuple(tuple(s.factor(contract[k][i]-baseline[k][i]) for i in range(3)) for k in (0,1,2))

def checks():
    baseline=solve_market()
    deep=solve_market(True,1,R)
    shallow=solve_market(True,0,R)
    D=diff(deep,baseline)
    x=Q(3,50) # r=0.06
    assert D[1][0].subs(R,x)>0 and D[0][0].subs(R,x)>0 # firm1, state1 approve
    assert D[1][1].subs(R,x)>0 and D[0][1].subs(R,x)<0 # firm2 accepts, state2 vetoes
    assert D[1][2].subs(R,x)<0 and D[0][2].subs(R,x)<0 # external harms
    assert s.factor(D[0][1]-D[1][1]-D[2][1])==0
    # Certified NONTRIVIAL ROYALTY INTERVAL (0.057,0.064)
    # Both W2 and P2 are strictly decreasing on [0,0.1] (quadratic, derivative affine).
    for expr in (D[0][1],D[1][1]):
        derivative=s.diff(expr,R)
        assert s.degree(derivative,R)==1
        assert derivative.subs(R,0)<0 and derivative.subs(R,Q(1,10))<0
    assert D[0][1].subs(R,Q(57,1000))<0
    assert D[1][1].subs(R,Q(64,1000))>0
    for var in (Q(57,1000),Q(64,1000)):
        assert D[0][0].subs(R,var)>0 and D[1][0].subs(R,var)>0
        # Re-evaluate the product market at each royalty endpoint: strictly positive output.
        solve_market(True,1,var)
    # For both participating firm 1 and government 1, each gain is concave
    # quadratic in r; strictly positive endpoints imply positivity throughout.
    for expr in (D[0][0],D[1][0]):
        assert s.Poly(expr,R).degree()==2 and s.Poly(expr,R).LC()<0
    # The contractor's alternative shallower interface dominates this deep contract
    # for each required signer at this single witness. No selective-stable deep-standard result.
    for typeindex in (0,1):
        for signer in (0,1):
            assert (shallow[typeindex][signer]-deep[typeindex][signer]).subs(R,x)>0
    # Negative controls: turning off kappa or network effect at this ONE witness
    # removes the split-sign incentive (not a claim of global necessity).
    for change,expected in (("kappa",0),("v",0)):
        test=dict(PARAM);test[change]=Q(0)
        ch=diff(solve_market(True,1,x,test),solve_market(param=test))
        assert ch[0][1]*ch[1][1]>0
        assert (ch[0][1]>0)==(change=="kappa")

    m,g,k,v,A=s.symbols("m gamma kappa v A",positive=True)
    qN=A/(2*m+g)
    qP=A/(2*m+g+k-v)
    assert s.factor(qP-qN-(A*(v-k)/((2*m+g)*(2*m+g+k-v))))==0
    print("PASS: exact LQ Cournot/CS/royalty/world-accounting identities")
    print("PASS: G2 veto versus F2 consent, all exact inequalities at r=3/50")
    print("PASS: interval (57/1000, 64/1000) and κ=0/v=0 local negative controls")
    print("PASS: shallow interface dominates deep platform for the four signers in this witness")
    print("TESTED: one sample and bounded interval, NOT overall stable-coalition theorem")
    print("ΔW2:",D[0][1].subs(R,x),"ΔΠ2:",D[1][1].subs(R,x))
    print("ΔW1:",D[0][0].subs(R,x),"ΔΠ1:",D[1][0].subs(R,x))

if __name__=="__main__":checks()
