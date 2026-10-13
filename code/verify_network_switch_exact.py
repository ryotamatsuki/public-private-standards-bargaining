"""Exact THREE REGIMES for the ORIGINAL one-depth NS/RS/IS bargaining game.

All three firms' Cournot competition is solved before one-shot standard
announcements; network valuation v is EXOGENOUS.  Theorem concerns STRONG-
NASH CONTRACT OUTCOME TYPES, not uniqueness of messages or novelty.

All rational-polynomial signs proved over ENTIRE v×depth rectangles via
exact tensor Bernstein coefficients plus dyadic de Casteljau subdivision.
The transition parameters are specified as UNIQUE ALGEBRAIC ROOTS.
Only fixed baseline other primitives and 0.15 <= v <= 0.34 certified.
"""
import sympy as S
from math import comb
v,t,u=S.symbols("v t u",real=True)
Q=S.Rational
L0=Q(15,100);U0=Q(34,100)
A=Q(4,5);g=Q(1,4);k=Q(3,20);eta=Q(3,40);h=f=Q(1,5)
m=1-v;b=g+(k-v)*t;d=g-eta*t
delta=2*m*(2*m+b)-2*d*d
x=S.cancel((2*m*(A+h*t)-d*A)/delta)
y=S.cancel(((2*m+b)*A-2*d*(A+h*t))/delta)
q=S.cancel((A+h*t)/(2*(m+b)))
qn=S.cancel(A/(2*(m+g)))
csr=(m+b)*x*x+2*d*x*y+m*y*y/2
csi=Q(3,2)*(m+2*b)*q*q
csn=Q(3,2)*(m+2*g)*qn*qn
PR=S.cancel(3*m*x*x-f*t*t);WR=S.cancel(PR+csr)
OR=S.cancel(3*m*y*y);UR=S.cancel(OR+csr)
PI=S.cancel(3*m*q*q-f*t*t);WI=S.cancel(PI+csi)
PN=S.cancel(3*m*qn*qn);WN=S.cancel(PN+csn)

def tensor(poly,lo,hi):
    zz=S.Poly(S.expand(poly.subs(v,lo+(hi-lo)*u)),u,t)
    nv,nt=zz.degree_list()
    raw=[[zz.coeff_monomial(u**i*t**j)
          for j in range(nt+1)] for i in range(nv+1)]
    return [[sum(raw[a][b]*Q(comb(i,a),comb(nv,a))*
                 Q(comb(j,b),comb(nt,b))
                 for a in range(i+1) for b in range(j+1))
             for j in range(nt+1)] for i in range(nv+1)]

def split(B,axis):
    nv,nt=len(B)-1,len(B[0])-1
    left=[[0]*(nt+1) for _ in range(nv+1)]
    right=[[0]*(nt+1) for _ in range(nv+1)]
    if axis==0:
        for j in range(nt+1):
            row=[B[i][j] for i in range(nv+1)]
            for level in range(nv+1):
                left[level][j]=row[0]
                right[nv-level][j]=row[-1]
                row=[(row[i]+row[i+1])/2 for i in range(len(row)-1)]
    else:
        for i in range(nv+1):
            row=B[i][:]
            for level in range(nt+1):
                left[i][level]=row[0]
                right[i][nt-level]=row[-1]
                row=[(row[j]+row[j+1])/2 for j in range(len(row)-1)]
    return left,right

def certify_bern(B,depth=0):
    coeff=[a for row in B for a in row]
    if min(coeff)>0:return (1,depth)
    if depth>=22:raise AssertionError(("UNPROVED",depth))
    first,second=split(B,depth%2)
    n1,d1=certify_bern(first,depth+1)
    n2,d2=certify_bern(second,depth+1)
    return n1+n2,max(d1,d2)

def certify(name,expr,lo,hi):
    num,den=S.fraction(S.cancel(expr))
    if den.subs({v:lo,t:0})<0:num,den=-num,-den
    for label,poly in (("numerator",num),("denominator",den)):
        bb=tensor(poly,lo,hi)
        boxes,depth=certify_bern(bb)
        print("PASS",name,label,"v=[%s,%s]"%(lo,hi),
              "degree",len(bb)-1,len(bb[0])-1,"boxes",boxes,
              "maxdepth",depth,flush=True)

def interval(lo,hi,items):
    for name,expr in items:certify(name,expr,lo,hi)

def main():
    # Source market SPD / Cournot positive on the ENTIRE target v×s rectangle.
    interval(L0,U0,[
      ("NS m-g",m-g),("NS m+2g",m+2*g),
      ("RS and IS m-b",m-b),
      ("RS m(m+b)-2d^2",m*(m+b)-2*d*d),
      ("IS m+2b",m+2*b),
      ("RS member output",x),("RS outsider output",y),
      ("IS output",q),("NS output",qn)])
    MR=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    MI=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    assert all(S.cancel(z)==0 for z in
      ((MR+m*S.eye(3))*S.Matrix([x,x,y])-S.Matrix([A+h*t,A+h*t,A])))
    assert all(S.cancel(z)==0 for z in
      ((MI+m*S.eye(3))*S.Matrix([q]*3)-S.Matrix([A+h*t]*3)))
    assert S.cancel(2*PR+OR+3*csr-
        (3*(2*x+y-csr-2*(Q(1,5)-h*t)*x-Q(1,5)*y)-2*f*t*t))==0
    assert S.cancel(3*PI+3*csi-
        (3*(3*q-csi-3*(Q(1,5)-h*t)*q)-3*f*t*t))==0
    print("PASS general Cournot FOCs / resource accounting")

    # Two globally defined algebraic ordering thresholds at contract depth 1.
    wdiff=S.factor(WI.subs(t,1)-WR.subs(t,1))
    pdiff=S.factor(PI.subs(t,1)-PR.subs(t,1))
    alpha0=Q(184595,10**6);alpha1=Q(184596,10**6)
    beta0=Q(278975,10**6);beta1=Q(278976,10**6)
    for label,expr,lo,hi in (
        ("alpha: govt ranking",wdiff,alpha0,alpha1),
        ("beta: firm ranking",pdiff,beta0,beta1)):
        num,den=S.fraction(expr)
        poly=S.Poly(num,v)
        assert poly.count_roots(L0,U0)==1
        assert poly.count_roots(lo,hi)==1
        assert expr.subs(v,lo)<0<expr.subs(v,hi)
        print("PASS unique ranking root",label,
              "in (%s,%s)"%(lo,hi),flush=True)

    # Four exact RATIONAL strips, plus analytical root ordering to fill
    # the sub-micro gaps and include equality at each algebraic threshold.
    interval(L0,alpha0,[
        ("LOW PR(1) > PI(any depth)",PR.subs(t,1)-PI),
        ("LOW WR(1) > WI(any depth)",WR.subs(t,1)-WI)])
    interval(alpha1,beta0,[
        ("MIDDLE PR(1) > PI(any depth)",PR.subs(t,1)-PI),
        ("MIDDLE WI(1) > WR(any depth)",WI.subs(t,1)-WR)])
    interval(beta1,U0,[
        ("HIGH PI(1) > PR(any depth)",PI.subs(t,1)-PR),
        ("HIGH PI(1) > outsider profit",PI.subs(t,1)-OR),
        ("HIGH WI(1) > WR(any depth)",WI.subs(t,1)-WR),
        ("HIGH WI(1) > outsider welfare",WI.subs(t,1)-UR)])

    # Joining inequalities show how to cover EVERY real v, not just
    # three disjoint closed rational bands.
    interval(L0,beta0,[("JOIN PR(1)>PI(t)",PR.subs(t,1)-PI)])
    interval(alpha1,U0,[("JOIN WI(1)>WR(t)",WI.subs(t,1)-WR)])
    interval(L0,U0,[("JOIN dWR/dt>0",S.diff(WR,t))])
    interval(Q(18459,10**5),U0,[("JOIN dWI/dt>0",S.diff(WI,t))])
    interval(beta0,U0,[("JOIN dPR/dt>0",S.diff(PR,t)),
                       ("JOIN dPI/dt>0",S.diff(PI,t)),
                       ("JOIN PI(1)>OR(t)",PI.subs(t,1)-OR),
                       ("JOIN WI(1)>UR(t)",WI.subs(t,1)-UR)])
    interval(L0,U0,[("RS IR firm",PR.subs(t,1)-PN),
                    ("RS IR govt",WR.subs(t,1)-WN)])
    interval(Q(18459,10**5),U0,[
        ("IS IR firm",PI.subs(t,1)-PN),
        ("IS IR govt",WI.subs(t,1)-WN),
        ("IS(1) govt above any RS outsider govt",WI.subs(t,1)-UR)])
    # Analytic stitching:
    # unique wdiff root alpha and increasing WR and WI near alpha imply
    # for v<alpha RS(1) dominates each IS in (P,W); v>=alpha
    # WI(1)>=WR(1)>=WR(t), so IS(1) survives RS deviations.
    # unique pdiff root beta and P_R,P_I increasing for v>=beta0 imply
    # v<=beta PR(1)>=max_t PI(t), so RS(1) survives IS deviations;
    # v>beta PI(1)>PR(t), with all outsider inequalities, so
    # any RS is blocked by unanimous profitable IS(1).
    print("THEOREM [0.15,alpha): RS exists, all IS blocked")
    print("THEOREM [alpha,beta]: RS(1) and IS(1) both strongly stable")
    print("NESTED TYPES: firms-only RS; governments-only IS across [alpha,beta]")
    print("THEOREM (beta,0.34]: IS(1) exists, all RS blocked")
    print("THRESHOLDS alpha~0.184595370845337 beta~0.278975090072072")
    print("SCOPE: θ other than v fixed; strict strong-Nash outcomes only.")
    print("NOT: global θ partition, government policy optimum, new theory certification.")
if __name__=="__main__":main()
