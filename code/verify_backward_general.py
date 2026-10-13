"""Exact 1-depth backward induction for rational primitives; no numerical grid."""
import sympy as S
s=S.symbols("s",real=True)
Q=S.Rational

def positive(expr):
    num,den=S.fraction(S.cancel(expr))
    if den.subs(s,0)<0:num,den=-num,-den
    for pol in (num,den):
        p=S.Poly(pol,s)
        if not(p.eval(0)>0 and p.eval(1)>0 and p.count_roots(0,1)==0):
            return False
    return True

def continuation(theta):
    a,c,h,f,g,k,e,v=[Q(p) for p in theta]
    A=a-c;m=1-v;b=g+(k-v)*s;d=g-e*s
    D=2*m*(2*m+b)-2*d*d
    x=S.cancel((2*m*(A+h*s)-d*A)/D)
    y=S.cancel(((2*m+b)*A-2*d*(A+h*s))/D)
    qi=S.cancel((A+h*s)/(2*(m+b)))
    qn=S.cancel(A/(2*(m+g)))
    cr=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
    ci=S.cancel(S.Rational(3,2)*(m+2*b)*qi*qi)
    cn=S.cancel(S.Rational(3,2)*(m+2*g)*qn*qn)
    pr=S.cancel(3*m*x*x-f*s*s);po=S.cancel(3*m*y*y)
    pi=S.cancel(3*m*qi*qi-f*s*s);pn=S.cancel(3*m*qn*qn)
    H=m+g+(k-v)*s;K=h*(m+g)-A*(k-v)
    assert S.cancel(2*H**3*S.diff(pi,s)
                    -(3*m*(A+h*s)*K-4*f*s*H**3))==0
    assert S.degree(S.expand(3*m*(A+h*s)*K-4*f*s*H**3),s)<=4
    assert m>0
    for p in (m-g,m+2*g,m-b,m*(m+b)-2*d*d,m+2*b,x,y,qi,qn):
        assert positive(p),("SPD/INTERIOR DOMAIN FAILED",p)
    MR=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    MI=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    for M,qq,rhs in ((MR,S.Matrix([x,x,y]),S.Matrix([A+h*s,A+h*s,A])),
                     (MI,S.Matrix([qi]*3),S.Matrix([A+h*s]*3))):
        assert all(S.cancel(r)==0 for r in ((M+m*S.eye(3))*qq-rhs))
    return {"R":(pr,S.cancel(pr+cr)),
            "O":(po,S.cancel(po+cr)),
            "I":(pi,S.cancel(pi+ci)),
            "N":(pn,S.cancel(pn+cn))}

def profitable(payoffs,limits):
    """Sturm isolate all roots of joint comparison; sample every open sign cell.
    Strict both-gain inequality over ALL t in (0,1], exact rational arithmetic.
    """
    pols=[]
    for expr,threshold in zip(payoffs,limits):
        n,d=S.fraction(S.cancel(expr-threshold))
        if d.subs(s,0)<0:n=-n
        if n==0:return False
        pols.append(S.Poly(n,s))
    roots=S.Poly(pols[0]*pols[1],s).intervals(eps=Q(1,10**12))
    points=[];last=Q(0)
    for (left,right),mult in roots:
        if right<0 or left>1:continue
        lo,hi=max(left,Q(0)),min(right,Q(1))
        if lo>last:points.append((lo+last)/2)
        last=max(last,hi)
    if last<1:points.append((last+1)/2)
    points.append(Q(1))
    return any(t>0 and pols[0].eval(t)>0 and pols[1].eval(t)>0
               for t in points)

def strong_contract(theta,kind,depth="0",uniform=False):
    """Strong-Nash CONTRACT OUTCOME existence; uniform=True tests all RS
    supporting outsiders' messages instead of best-protected SQ outsiders.
    """
    z=continuation(theta)
    at=lambda k:tuple(S.cancel(p.subs(s,Q(depth))) for p in z[k])
    n=at("N")
    if kind=="N":
        return not profitable(z["R"],n) and not profitable(z["I"],n)
    assert Q(0)<Q(depth)<=1
    if kind=="R":
        p,o=at("R"),at("O")
        if any(p[i]<n[i] for i in (0,1)):return False
        if profitable(z["R"],p):return False
        barrier=p if uniform else tuple(max(p[i],o[i]) for i in (0,1))
        return not profitable(z["I"],barrier)
    if kind=="I":
        p=at("I")
        if any(p[i]<n[i] for i in (0,1)):return False
        return not profitable(z["I"],p) and not profitable(z["R"],p)
    raise ValueError(kind)

def prove_is_margin():
    A,m,g,h,k,v,f=S.symbols("A m g h k v f",positive=True)
    H=m+g+(k-v)*s
    q=(A+h*s)/(2*H)
    K=h*(m+g)-A*(k-v)
    assert S.factor(S.diff(q,s)-K/(2*H**2))==0
    assert S.factor(2*H**3*S.diff(3*m*q*q-f*s*s,s)
                    -(3*m*(A+h*s)*K-4*f*s*H**3))==0
    print("PASS general IS private-profit quartic and K<=0 veto criterion")

if __name__=="__main__":
    prove_is_margin()
    base=["1","1/5","1/5","1/5","1/4","3/20","3/40"]
    cases=[("1/10","N","0",False),("1/10","R","3/5",True),
           ("1/10","I","1",False),("1/5","R","1",True),
           ("1/5","I","1",True),("3/10","R","1",False),
           ("3/10","I","1",True)]
    for v,kind,depth,expected in cases:
        theta=base+[v]
        actual=strong_contract(theta,kind,depth)
        robust=strong_contract(theta,kind,depth,uniform=True)
        assert actual==expected and robust==expected,(v,kind,actual,robust)
        print("EXACT",v,kind,depth,"strong",actual)
    print("PASS: all-depth profitable deviations via exact real-root cells")
