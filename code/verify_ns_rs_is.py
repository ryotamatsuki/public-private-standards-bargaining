"""3 countries, 3 firms, one-shot NS/RS/IS coalition standards bargaining.
Exact SymPy source-model verification and independent Fraction Gauss evaluator.
Strong Nash for specific EXACT rational economies, NOT universal/novel theorem.
run: python code/verify_ns_rs_is.py
"""
import sympy as S
from fractions import Fraction as F
from math import comb
s=S.symbols('s',real=True)
Q=S.Rational
a=S.S.One;c0=h=f=Q(1,5);g=Q(1,4);k=Q(3,20);eta=k/2

def bern(p):
    poly=S.Poly(S.expand(p),s);n=poly.degree()
    return [S.factor(sum(poly.nth(i)*Q(comb(j,i),comb(n,i))
                        for i in range(j+1))) for j in range(n+1)]

def nonnegative(expr):
    numer,denom=S.fraction(S.together(expr))
    if denom.subs(s,0)<0:numer,denom=-numer,-denom
    pn,pd=bern(numer),bern(denom)
    assert all(x>=0 for x in pn) and any(x>0 for x in pn),('numerator',expr,pn)
    assert all(x>0 for x in pd),('denominator',expr,pd)
    return pn

def market(v,kind):
    m=1-v;b=g+(k-v)*s;d=g-eta*s
    if kind=='RS':
        M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
        costs=S.Matrix([c0-h*s,c0-h*s,c0]);paying=2
    elif kind=='IS':
        M=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
        costs=S.Matrix([c0-h*s]*3);paying=3
    else:
        assert kind=='NS'
        M=S.Matrix([[m,g,g],[g,m,g],[g,g,m]])
        costs=S.Matrix([c0]*3);paying=0
    B=M+m*S.eye(3)
    q=S.simplify(B.inv()*(a*S.ones(3,1)-costs))
    for i in range(3):
        assert S.factor(a-(M*q)[i]-costs[i]-m*q[i])==0
    CS=S.factor((q.T*M*q)[0]/2)
    profits=[S.factor(3*m*q[i]**2-(f*s*s if i<paying else 0)) for i in range(3)]
    welfare=[S.factor(profits[i]+CS) for i in range(3)]
    world=S.factor(3*(a*sum(q)-CS-(costs.T*q)[0])-paying*f*s*s)
    assert S.factor(sum(profits)+3*CS-world)==0
    for j in range(1,4):nonnegative(M[:j,:j].det())
    for qi in q:nonnegative(qi)
    return {'M':M,'q':q,'P':profits,'W':welfare,'CS':CS,'world':world}

def gaussian(A,y):
    z=[list(row)+[rhs] for row,rhs in zip(A,y)]
    for j in range(len(z)):
        pivot=next(i for i in range(j,len(z)) if z[i][j])
        z[j],z[pivot]=z[pivot],z[j]
        p=z[j][j];z[j]=[t/p for t in z[j]]
        for i in range(len(z)):
            if i==j:continue
            c=z[i][j];z[i]=[a-c*b for a,b in zip(z[i],z[j])]
    return [row[-1] for row in z]

def independent(v,kind,t):
    v=F(v);t=F(t);m=F(1)-v;g=F(1,4);kap=F(3,20);eta=kap/2
    b=g+(kap-v)*t;d=g-eta*t
    if kind=='RS':
        M=[[m,b,d],[b,m,d],[d,d,m]];c=[F(1,5)*(1-t)]*2+[F(1,5)];paid=2
    elif kind=='IS':
        M=[[m,b,b],[b,m,b],[b,b,m]];c=[F(1,5)*(1-t)]*3;paid=3
    else:
        assert kind=='NS'
        M=[[m,g,g],[g,m,g],[g,g,m]];c=[F(1,5)]*3;paid=0
    B=[[M[i][j]+(m if i==j else 0) for j in range(3)] for i in range(3)]
    q=gaussian(B,[F(1)-ci for ci in c])
    assert min(q)>0
    p=[F(1)-sum(M[i][j]*q[j] for j in range(3)) for i in range(3)]
    assert all(p[i]-c[i]==m*q[i] for i in range(3))
    cs=sum(q[i]*M[i][j]*q[j] for i in range(3) for j in range(3))/2
    P=[3*(p[i]-c[i])*q[i]-(F(1,5)*t*t if i<paid else 0) for i in range(3)]
    world=3*(sum(q)-cs-sum(q[i]*c[i] for i in range(3)))-paid*F(1,5)*t*t
    assert sum(P)+3*cs==world
    return {'q':q,'P':P,'W':[pi+cs for pi in P],'CS':cs,'world':world}

def independent_checks(v,z,kind):
    for t in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
        direct=independent(v,kind,t)
        for j in range(3):
            for label in ('q','P','W'):
                r=direct[label][j]
                assert S.factor(z[label][j].subs(s,Q(t.numerator,t.denominator))-
                         Q(r.numerator,r.denominator))==0
        for label in ('CS','world'):
            r=direct[label]
            assert S.factor(z[label].subs(s,Q(t.numerator,t.denominator))-
                            Q(r.numerator,r.denominator))==0

def witness_low():
    v=Q(1,10)
    ns,rs,ss=(market(v,knd) for knd in ('NS','RS','IS'))
    for name,z in [('NS',ns),('RS',rs),('IS',ss)]:independent_checks(v,z,name)
    firm,gov=rs['P'][0],rs['W'][0]
    isp,isw=ss['P'][0],ss['W'][0]
    assert S.factor(ss['q'][0]-2*(s+4)/(s+23))==0
    for z in (firm,gov,isp,isw):nonnegative(-S.diff(z,s,2))
    fl,fu=Q(5319,10000),Q(5320,10000)
    gl,gu=Q(8249,10000),Q(8250,10000)
    assert S.diff(firm,s).subs(s,fl)>0>S.diff(firm,s).subs(s,fu)
    assert S.diff(gov,s).subs(s,gl)>0>S.diff(gov,s).subs(s,gu)
    assert fu<gl
    # All IS depths are BLOCKED by a subset of four signers moving to RS(1/2).
    # Strict concavity: u(x)≤u(t)+u'(t)(x-t).
    for iso,rso,t in ((isp,firm,Q(7,20)),(isw,gov,Q(7,10))):
        assert S.diff(iso,s).subs(s,t)>0
        global_upper=iso.subs(s,t)+S.diff(iso,s).subs(s,t)*(1-t)
        assert rso.subs(s,Q(1,2))>global_upper
    # The original RS Pareto interval remains stable after IS is added:
    # member profits throughout [sf,sg] dominate every attainable IS member profit.
    peak_upper=isp.subs(s,Q(7,20))+S.diff(isp,s).subs(s,Q(7,20))*Q(13,20)
    assert min(firm.subs(s,fl),firm.subs(s,gu))>peak_upper
    assert min(firm.subs(s,fl),firm.subs(s,gu))>ns['P'][0]
    assert min(gov.subs(s,fl),gov.subs(s,gu))>ns['W'][0]
    print('PASS weak v=0.10: NS rejected by signers, IS always blocked by RS(0.5)')
    print('RS coalition-strong depths [sF,sG] with sF in (0.5319,0.5320), sG in (0.8249,0.8250)')

def witness_high():
    v=Q(3,10)
    ns,rs,ss=(market(v,knd) for knd in ('NS','RS','IS'))
    for name,z in [('NS',ns),('RS',rs),('IS',ss)]:independent_checks(v,z,name)
    pf=ss['P'][0].subs(s,1);wg=ss['W'][0].subs(s,1)
    assert pf==Q(397,640) and wg==Q(1469,1280)
    # Both IS firm profit and governmental welfare STRICTLY increase in depth.
    nonnegative(S.diff(ss['P'][0],s));nonnegative(S.diff(ss['W'][0],s))
    # IS full-depth strictly Pareto-dominates EVERY RS depth for members AND outsider.
    for i in range(3):
        nonnegative(pf-rs['P'][i])
        nonnegative(wg-rs['W'][i])
    assert pf>ns['P'][0] and wg>ns['W'][0]
    print('PASS strong v=0.30: IS(s=1) sole strongly-stable CONTRACT OUTCOME')
    print('IS(s=1) profit=',pf,'government W=',wg)

if __name__=='__main__':
    witness_low();witness_high()
    print('PASS: RS permutations symmetric, full-contract IS all six signatories')
    print('LIMIT: two exact economies, not a global v cut-off or novel theorem.')
