"""Stage 1 exact differentiated-Cournot continuation checks. NOT a bargaining model."""
import sympy as S

a,g,v,c1,c2,r=S.symbols('a gamma v c1 c2 r',real=True)
x,y=S.symbols('x y',real=True)
q=S.Matrix([x,y]); one=S.ones(2,1)
M0=S.Matrix([[1,g],[g,1]])
ML=S.Matrix([[1-v,g-v],[g-v,1-v]])
def eqzero(z,name):
    assert S.cancel(S.factor(z))==0, name

def market(M,eff):
    p=a*one-M*q
    profits=[S.expand((p[i]-eff[i])*q[i]) for i in range(2)]
    B=M+S.diag(M[0,0],M[1,1])
    res=S.simplify(B.inv()*(a*one-eff))
    for i in range(2):
        eqzero(S.diff(profits[i],q[i],2)+2*M[i,i],"SOC")
        eqzero(S.diff(profits[i],q[i]).subs({x:res[0],y:res[1]}),"FOC")
    return res,S.simplify(a*one-M*res),S.simplify((res.T*M*res)[0]/2)

q0,p0,cs0=market(M0,S.Matrix([c1,c2]))
ql,pl,csl=market(ML,S.Matrix([c1,c2+r]))
m,b=1-v,g-v
D=4*m*m-b*b
eqzero(ql[0]-(2*m*(a-c1)-b*(a-c2-r))/D,"q1")
eqzero(ql[1]-(2*m*(a-c2-r)-b*(a-c1))/D,"q2")
eqzero(S.diff(ql[0],r)-b/D,"dq1/dr")
eqzero(S.diff(ql[1],r)+2*m/D,"dq2/dr")
eqzero(ML.det()-(1-g)*(1+g-2*v),"matrix eigenvalues")
assert ML.det().subs({g:1})==0
for i in range(2):
    eqzero(ql[i].subs({v:0,r:0})-q0[i],"no-network recovery")
eqzero(csl.subs({v:0,r:0})-cs0,"CS no-network recovery")
eqzero(ql[0].subs({c1:0,c2:0,r:0})-a/(2+g-3*v),"symmetric quantity")
pi1=S.simplify((pl[0]-c1)*ql[0]+r*ql[1])
pi2=S.simplify((pl[1]-c2-r)*ql[1])
resources=S.simplify(a*(ql[0]+ql[1])-(ql.T*ML*ql)[0]/2-c1*ql[0]-c2*ql[1])
eqzero(csl+pi1+pi2-resources,"royalty transfer accounting")

z={a:S.Rational(1),g:S.Rational(1,2),v:S.Rational(1,5),
   c1:S.Rational(0),c2:S.Rational(1,10),r:S.Rational(1,20)}
val=lambda e,ps:S.factor(e.subs(ps))
assert [val(k,z) for k in ql]==[S.Rational(269,494),S.Rational(106,247)]
assert val(csl,z)==S.Rational(80038,305045)
assert val(pi1,z)==S.Rational(157813,610090)
assert val(pi2,z)==S.Rational(44944,305045)
zz=dict(z);zz[r]=S.Rational(4,5)
q1corner=val((a-c1)/(2*m),zz)
gradient=val(a-c2-r-b*q1corner,zz)
assert q1corner==S.Rational(5,8) and gradient==-S.Rational(7,80)
rmax=S.solve(2*m*(a-c2-r)-b*(a-c1),r)[0]
assert val(rmax,z)==S.Rational(57,80)

z2=dict(z);z2[c1]=S.Rational(1,10);z2[c2]=S.Rational(0)
def eval_market(ps):
    Q=[val(t,ps) for t in ql]
    assert all(k>0 for k in Q)
    return val(csl,ps),[val(pi1,ps),val(pi2,ps)],val(resources,ps),Q
csA,piA,worldA,qA=eval_market(z)
csB,piB,worldB,qB=eval_market(z2)
W1=csA+piA[0]+piB[0];W2=csB+piA[1]+piB[1]
assert W1==S.Rational(880097,1220180)
assert W2==S.Rational(748123,1220180)
assert W1+W2==worldA+worldB
print("STAGE1 SYMBOLIC + 2-MARKET WELFARE + CORNER KKT: PASS")
print("interior:",[str(k) for k in qA],"corner:",q1corner,0)
print("national welfare:",W1,W2)
print("SCOPE: only the conditional downstream Cournot game; no bargaining SPE.")
