"""Exact 3-country / 3-firm one-shot standards-depth Cournot game.
Reproducible model construction (NOT an independent human proof or novelty result).
run: python code/verify_composite_depth.py ; dependency: sympy==1.14.0
"""
import sympy as S
from fractions import Fraction as F
s=S.symbols("s",real=True)
m=S.Rational(9,10);g=S.Rational(1,4); t=S.Rational(1,20)
a=S.S(1);c=S.Rational(1,5);h=S.Rational(1,5);f=S.Rational(1,5)
b=g+t*s
M=S.Matrix([[m,b,g],[b,m,g],[g,g,m]])
B=M+S.diag(m,m,m)
costs=S.Matrix([c-h*s,c-h*s,c])
quantities=B.inv()*(a*S.ones(3,1)-costs)
x=S.factor(quantities[0]);y=S.factor(quantities[2])
assert S.factor(quantities[1]-x)==0
assert S.factor(x-8*(9*s+31)/(713+18*s))==0
assert S.factor(y-4*(62-3*s)/(713+18*s))==0
for j in (1,2,3):
    assert M[:j,:j].det().subs(s,0)>0
    assert M[:j,:j].det().subs(s,1)>0
for qi in quantities:
    assert qi.subs(s,0)>0 and qi.subs(s,1)>0
prices=a*S.ones(3,1)-M*quantities
for i in range(3):
    assert S.factor(prices[i]-costs[i]-m*quantities[i])==0
CS=S.factor((quantities.T*M*quantities)[0]/2)
PF=S.factor(3*m*x*x-f*s*s)
PO=S.factor(3*m*y*y)
WG=S.factor(PF+CS)
WO=S.factor(PO+CS)
# Total welfare = 3 destination real net surplus minus two actual sunk setup costs.
assert S.factor(2*PF+PO+3*CS-(3*(a*sum(quantities)-CS-(costs.T*quantities)[0])-2*f*s*s))==0
P2=S.factor(S.diff(PF,s,2));W2=S.factor(S.diff(WG,s,2))
assert S.factor(P2+2*(104976*s**4+16632864*s**3+988269336*s**2+27737776008*s+234429139393)/(5*(18*s+713)**4))==0
assert S.factor(W2+2*(104976*s**4+16632864*s**3+988269336*s**2+26629159464*s+221319158173)/(5*(18*s+713)**4))==0
# Numerators of both negative second derivatives have strictly positive coefficients.
for fn in (PF,WG):
    der=S.diff(fn,s)
    assert der.subs(s,0)>0 and der.subs(s,1)<0
F0,F1=S.Rational(4753,10000),S.Rational(4754,10000)
G0,G1=S.Rational(7437,10000),S.Rational(7438,10000)
assert S.diff(PF,s).subs(s,F0)>0 and S.diff(PF,s).subs(s,F1)<0
assert S.diff(WG,s).subs(s,G0)>0 and S.diff(WG,s).subs(s,G1)<0
assert F1<G0
assert PF.subs(s,G1)>PF.subs(s,0)
assert WG.subs(s,F0)>WG.subs(s,0)
# Independent Fraction Gaussian elimination, not reusing SymPy's inverse.
def gaussian(mat,vec):
    z=[list(row)+[value] for row,value in zip(mat,vec)]
    for j in range(len(z)):
        pivot=next(i for i in range(j,len(z)) if z[i][j])
        z[j],z[pivot]=z[pivot],z[j]
        d=z[j][j];z[j]=[q/d for q in z[j]]
        for i in range(len(z)):
            if i==j:continue
            alpha=z[i][j]
            z[i]=[u-alpha*v for u,v in zip(z[i],z[j])]
    return [row[-1] for row in z]
def direct(ss):
    ss=F(ss); mm=F(9,10);gg=F(1,4);bb=gg+F(1,20)*ss
    mat=[[mm,bb,gg],[bb,mm,gg],[gg,gg,mm]]
    sys=[[mat[i][j]+(mm if i==j else 0) for j in range(3)] for i in range(3)]
    cc=[F(1,5)*(1-ss),F(1,5)*(1-ss),F(1,5)]
    q=gaussian(sys,[F(1)-z for z in cc])
    assert min(q)>0
    p=[F(1)-sum(mat[i][j]*q[j] for j in range(3)) for i in range(3)]
    cs=sum(q[i]*mat[i][j]*q[j] for i in range(3) for j in range(3))/2
    pf=3*(p[0]-cc[0])*q[0]-F(1,5)*ss*ss
    po=3*(p[2]-cc[2])*q[2]
    return (q[0],q[2],pf,cs,pf+cs,po,po+cs)
for ss in (F(0),F(2,5),F(1)):
    for expr,answer in zip((x,y,PF,CS,WG,PO,WO),direct(ss)):
        rational=S.Rational(answer.numerator,answer.denominator)
        assert S.factor(expr.subs(s,S.Rational(ss.numerator,ss.denominator))-rational)==0
def root(der,lo,hi):
    lo,hi=float(lo),float(hi)
    for _ in range(48):
        md=(lo+hi)/2
        if float(der.subs(s,md))>0:lo=md
        else:hi=md
    return (lo+hi)/2
sf=root(S.diff(PF,s),F0,F1);sg=root(S.diff(WG,s),G0,G1)
print("PASS: LQ demand, SPD, Cournot FOCs/SOCs, positive q, cost accounts, independent Fraction")
print("PASS: analytic strict concavity and exact rational unique-root bounds")
print("member firm optimum",sf,"member government optimum",sg)
print("joint coalition-strong matching interval [sF,sG]; firm-only sF; government-only sG")
print("all-SQ is Nash due to exact matching, but coalition-blocked")
for u in [0,sf,sg,1]:
    print("s",round(u,9),"q_member",float(x.subs(s,u)),"q_out",float(y.subs(s,u)),
          "member_profit",float(PF.subs(s,u)),"member_W",float(WG.subs(s,u)),
          "outside_profit",float(PO.subs(s,u)),"outside_W",float(WO.subs(s,u)))
