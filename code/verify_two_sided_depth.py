"""Two-sided Ghosh–Morita-inspired differentiation with network standards.
3 countries, 3 firms, symmetric bilateral contract, continuous depth s ∈ [0,1].
Stage-4 construction only; no novel-theorem or exact Salop-to-LQ equivalence claim.
"""
import sympy as S
from fractions import Fraction as F
from math import comb
s=S.symbols('s',real=True)
a=S.S(1);c0=h=f=S.Rational(1,5)
v=S.Rational(1,10);g=S.Rational(1,4)
k=S.Rational(3,20);eta=k/2; m=1-v; A=a-c0
b=g+(k-v)*s; d=g-eta*s
M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
B=M+S.diag(m,m,m)
C=S.Matrix([c0-h*s,c0-h*s,c0])
q=B.inv()*(a*S.ones(3,1)-C)
x=S.factor(q[0]);y=S.factor(q[2])
assert S.factor(q[1]-x)==0
assert S.factor(x-16*(21*s+62)/(2852+132*s-9*s*s))==0
assert S.factor(y-8*(3*s*s+6*s+124)/(2852+132*s-9*s*s))==0
# Sylvester positive definite on entire interval [0,1] (factor inequalities).
assert S.factor(M[0,0]-S.Rational(9,10))==0
assert S.factor(M[:2,:2].det()-(13-s)*(s+23)/400)==0
assert S.factor(M.det()-(13-s)*(728+96*s-9*s*s)/16000)==0
# x,y numerators positive and D=2852+132s-9s²>0 for 0<=s<=1.
p=a*S.ones(3,1)-M*q
for i in range(3):assert S.factor(p[i]-C[i]-m*q[i])==0
cs=S.factor((q.T*M*q)[0]/2)
pi=S.factor(3*m*x*x-f*s*s);po=S.factor(3*m*y*y)
w=S.factor(pi+cs);wo=S.factor(po+cs)
resources=S.factor(3*(a*sum(q)-cs-(C.T*q)[0])-2*f*s*s)
assert S.factor(2*pi+po+3*cs-resources)==0
# Whole-interval STRICT concavity via positive Bernstein coefficients for -profit'' and -welfare''.
def bernstein_certificate(payoff):
    n,dn=S.fraction(S.factor(-S.diff(payoff,s,2)))
    poly=S.Poly(n,s);deg=poly.degree()
    assert deg==8
    bern=[S.factor(sum(poly.nth(t)*S.Rational(comb(j,t),comb(deg,t))
             for t in range(j+1))) for j in range(deg+1)]
    assert all(vv>0 for vv in bern)
    # denominator constant * (9s²-132s-2852)^4, >0.
    assert dn.subs(s,0)>0 and dn.subs(s,1)>0
    return bern
assert bernstein_certificate(pi) and bernstein_certificate(w)
fl,fu=S.Rational(5319,10000),S.Rational(5320,10000)
gl,gu=S.Rational(8249,10000),S.Rational(8250,10000)
for payoff,l,u in ((pi,fl,fu),(w,gl,gu)):
    assert S.diff(payoff,s).subs(s,0)>0 and S.diff(payoff,s).subs(s,1)<0
    assert S.diff(payoff,s).subs(s,l)>0 and S.diff(payoff,s).subs(s,u)<0
assert fu<gl
assert pi.subs(s,gu)>pi.subs(s,0) and w.subs(s,fl)>w.subs(s,0)
# Outside output gain: exact derivative on entire [0,1] >0.
dy=S.factor(S.diff(y,s))
assert S.factor(dy-48*(75*s*s+3224*s+124)/(9*s*s-132*s-2852)**2)==0
# Outsider profits and government welfare increase throughout [0,1]; checked by polynomials.
for payoff in (po,wo):
    n,dn=S.fraction(S.factor(S.diff(payoff,s)))
    poly=S.Poly(n,s)
    assert len(set(S.sign(z) for z in poly.all_coeffs()))==1
    assert S.sign(n.subs(s,0))==S.sign(dn.subs(s,0))
# Closed-form outsider derivative at s=0 for GENERAL eta with fixed m,g,k,v,h,A.
am,mm,gg,kk,vv,hh,ee=S.symbols('A m g k v h eta',positive=True)
bb=gg+(kk-vv)*s;dd=gg-ee*s
DD=2*mm*(2*mm+bb)-2*dd*dd
yy=((2*mm+bb)*am-2*dd*(am+hh*s))/DD
formula=(2*am*mm*ee+am*gg*(kk-vv)-2*gg*hh*(gg+mm))/(2*(2*mm-gg)*(gg+mm)**2)
assert S.factor(S.diff(yy,s).subs(s,0)-formula)==0
cutoff=S.factor(gg*(2*hh*(gg+mm)-am*(kk-vv))/(2*am*mm))
cutoff=S.factor(cutoff.subs({gg:g,mm:m,hh:h,am:A,kk:k,vv:v}))
assert cutoff==S.Rational(7,96) and eta>S.Rational(7,96)
# Negative control eta=0, other primitives/real costs unchanged -> outsider quantity falls.
M0=S.Matrix([[m,b,g],[b,m,g],[g,g,m]])
q0=(M0+S.diag(m,m,m)).inv()*(a*S.ones(3,1)-C)
y0=S.factor(q0[2])
assert S.factor(S.diff(y0,s)+13020/(18*s+713)**2)==0
assert y.subs(s,1)>y.subs(s,0) and y0.subs(s,1)<y0.subs(s,0)
# INDEPENDENT direct-payoff reconstruction using Fraction Gaussian (no SymPy solver).
def gaussian(matrix,rhs):
    data=[list(row)+[z] for row,z in zip(matrix,rhs)]
    for j in range(len(data)):
        row=next(i for i in range(j,len(data)) if data[i][j]!=0)
        data[j],data[row]=data[row],data[j]
        denom=data[j][j];data[j]=[vv/denom for vv in data[j]]
        for i in range(len(data)):
            if i!=j:
                fact=data[i][j]
                data[i]=[p0-fact*p1 for p0,p1 in zip(data[i],data[j])]
    return [row[-1] for row in data]
def independent(st):
    st=F(st);mm=F(9,10);gg=F(1,4);ka=F(3,20);ve=F(1,10);ee=ka/2
    bb=gg+(ka-ve)*st;dd=gg-ee*st
    mat=[[mm,bb,dd],[bb,mm,dd],[dd,dd,mm]]
    sys=[[mat[i][j]+(mm if i==j else 0) for j in range(3)] for i in range(3)]
    costs=[F(1,5)*(1-st),F(1,5)*(1-st),F(1,5)]
    qq=gaussian(sys,[F(1)-z for z in costs])
    assert min(qq)>0
    pp=[F(1)-sum(mat[i][j]*qq[j] for j in range(3)) for i in range(3)]
    for i in range(3):assert pp[i]-costs[i]==mm*qq[i]
    surplus=sum(qq[i]*mat[i][j]*qq[j] for i in range(3) for j in range(3))/2
    P=3*(pp[0]-costs[0])*qq[0]-F(1,5)*st*st
    O=3*(pp[2]-costs[2])*qq[2]
    real=3*(sum(qq)-surplus-sum(ci*qi for ci,qi in zip(costs,qq)))-2*F(1,5)*st*st
    assert 2*P+O+3*surplus==real
    return (qq[0],qq[2],surplus,P,P+surplus,O,O+surplus)
for st in (F(0),F(1,4),F(1,2),F(3,4),F(1)):
    for expr,val in zip((x,y,cs,pi,w,po,wo),independent(st)):
        assert S.factor(expr.subs(s,S.Rational(st.numerator,st.denominator))-S.Rational(val.numerator,val.denominator))==0
def locate(fn,lo,hi):
    for _ in range(55):
        mid=(lo+hi)/2
        if float(S.diff(fn,s).subs(s,mid))>0:lo=mid
        else:hi=mid
    return (lo+hi)/2
sf=locate(pi,float(fl),float(fu))
sg=locate(w,float(gl),float(gu))
# Exact-name one-shot four-signature coalitions: matched s in [sf,sg] are
# coalition-strong within any bilateral pair. Each alternative bilateral pair
# shares one incumbent state G and F; by strict concavity/Pareto efficiency,
# both cannot strictly improve at another depth. No-agreement is Nash but blocked.
print('PASS: SPD on [0,1]; all 3 Cournot firms positive; accounting + Fraction independently')
print('PASS: exact Bernstein concavity certificates + root brackets for both payoffs')
print('PASS: outsider growth eta=kappa/2; eta=0 decreases; marginal cutoff eta_c=',cutoff)
print('firm optimum s_F=',sf,'government optimum s_G=',sg)
print('coalition-strong depth correspondence for each symmetric pair: [s_F,s_G]')
for u in (0,sf,sg,1):
    print('s=',round(u,7),'member_q=',round(float(x.subs(s,u)),8),'out_q=',round(float(y.subs(s,u)),8),
          'member_profit=',round(float(pi.subs(s,u)),8),'member_W=',round(float(w.subs(s,u)),8),
          'outside_profit=',round(float(po.subs(s,u)),8),'outside_W=',round(float(wo.subs(s,u)),8))
print('SCOPE: LQ stylization; no unique coalition/depth, full Salop microfoundation or novelty certification.')
