"""Six-dimensional normalized one-depth standards model, including Cournot corners.

Economic parameter domain:
  theta=(v,gamma0,kappa,eta,rho,phi), rho=h/(a-c0), phi=f/(a-c0)^2;
  0<=v<1, 0<=gamma0, kappa>=0, 0<=eta<=gamma0, rho>=0, phi>0,
  and SPD inverse-demand matrices at s=0 and s=1.

Provides exact Stage-2 Cournot payoffs for ALL depths, including
an outsider that exits and may re-enter. For rational theta and rational
candidate depth, globally certifies strong-Nash CONTRACT-OUTCOME membership
via Sturm-isolated polynomial sign intervals (not a grid).
It does NOT yet enumerate all six-dimensional parameter cells or solve
existential stable depths in generic symbolic theta.
"""
import sympy as S
s=S.symbols('s',real=True);R=S.Rational

def data(theta):
    v,g,k,e,r,phi=[R(x) for x in theta]
    m=1-v;b=g+(k-v)*s;d=g-e*s
    assert 0<=v<1 and g>=0 and k>=0 and 0<=e<=g and r>=0 and phi>0
    b1=b.subs(s,1);d1=d.subs(s,1)
    # Entire [0,1] SPD: the RS determinant is concave, other eigenvalues
    # are affine; checking endpoints is both necessary and sufficient.
    assert all(t>0 for t in (m-g,m+2*g,m-b1,m+2*b1,
                              m*(m+b1)-2*d1**2))
    D=2*m*(2*m+b)-2*d*d
    x=S.cancel((2*m*(1+r*s)-d)/D)
    y=S.cancel((2*m+b-2*d*(1+r*s))/D)
    xc=S.cancel((1+r*s)/(2*m+b))
    qi=S.cancel((1+r*s)/(2*(m+b)))
    qn=1/(2*(m+g))
    nout=S.factor(2*m+b-2*d*(1+r*s))
    cs=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
    csc=S.cancel((m+b)*xc*xc)
    csi=S.cancel(S.Rational(3,2)*(m+2*b)*qi*qi)
    csn=S.cancel(S.Rational(3,2)*(m+2*g)*qn*qn)
    pin=S.cancel(3*m*x*x-phi*s*s)
    pc=S.cancel(3*m*xc*xc-phi*s*s)
    pI=S.cancel(3*m*qi*qi-phi*s*s)
    pN=3*m*qn*qn
    inn={'P':pin,'W':S.cancel(pin+cs),
         'O':3*m*y*y,'U':S.cancel(3*m*y*y+cs)}
    cor={'P':pc,'W':S.cancel(pc+csc),'O':S.Integer(0),'U':csc}
    return dict(n=nout,inside=inn,corner=cor,
                I={'P':pI,'W':S.cancel(pI+csi)},
                N={'P':pN,'W':pN+csn},
                market=(m,b,d,x,y,xc,qi,qn),
                cs=(cs,csc,csi,csn),theta=theta)

def regional_at(z,t):
    regime=z['inside'] if z['n'].subs(s,t)>=0 else z['corner']
    return {key:S.cancel(expr.subs(s,t)) for key,expr in regime.items()}

def international_at(z,t):
    return {key:S.cancel(expr.subs(s,t)) for key,expr in z['I'].items()}

def numerator(expr):
    p,q=S.fraction(S.cancel(expr))
    if q.subs(s,0)<0:p=-p
    return p

def cell_samples(polynomials):
    polys=[S.Poly(p,s) for p in polynomials if S.expand(p)!=0]
    if not polys:return [R(1,2),R(1)]
    product=S.Poly(S.prod(polys),s);precision=12
    while True:
        intervals=product.intervals(eps=R(1,10**precision))
        boxes=[(a,b) for (a,b),multiplicity in intervals
               if b>=0 and a<=1]
        touching=any(a<=0<b or a<1<=b for a,b in boxes)
        touching |= any(boxes[i][1]>=boxes[i+1][0] and
                        boxes[i][1]!=boxes[i+1][0]
                        for i in range(len(boxes)-1))
        if not touching:break
        precision*=2
        assert precision<5000
    samples={R(1)};last=R(0)
    for a,b in boxes:
        left=max(R(0),a);right=min(R(1),b)
        if left>last:samples.add((left+last)/2)
        if 0<left<1:samples.add(left)
        if 0<right<1:samples.add(right)
        last=max(last,right)
    if last<1:samples.add((last+1)/2)
    return sorted(t for t in samples if 0<t<=1)

def beneficial(z,kind,threshold):
    """Existence of a jointly STRICT gain at ANY allowed continuous depth."""
    pay=z['I'] if kind=='I' else z['inside']
    polys=[numerator(pay['P']-threshold['P']),
           numerator(pay['W']-threshold['W'])]
    if kind=='R':
        cor=z['corner']
        polys.extend([z['n'],numerator(cor['P']-threshold['P']),
                     numerator(cor['W']-threshold['W'])])
    for t in cell_samples(polys):
        payoff=regional_at(z,t) if kind=='R' else international_at(z,t)
        if payoff['P']>threshold['P'] and payoff['W']>threshold['W']:
            return True
    return False

def strong(theta,kind,depth=None,uniform=False):
    """Exact existence of supporting STRONG-NASH message profile for a
    given normalized rational theta and rational candidate depth.
    For RS, uniform=True tests all outsiders' non-binding messages.
    """
    z=data(theta);n=z['N']
    if kind=='N':return not beneficial(z,'R',n) and not beneficial(z,'I',n)
    t=R(depth);assert 0<t<=1
    if kind=='R':
        p=regional_at(z,t)
        if p['P']<n['P'] or p['W']<n['W']:return False
        if beneficial(z,'R',p):return False
        lim={'P':p['P'] if uniform else max(p['P'],p['O']),
             'W':p['W'] if uniform else max(p['W'],p['U'])}
        return not beneficial(z,'I',lim)
    if kind=='I':
        p=international_at(z,t)
        if p['P']<n['P'] or p['W']<n['W']:return False
        return not beneficial(z,'I',p) and not beneficial(z,'R',p)
    raise ValueError(kind)

def audit(theta):
    z=data(theta)
    m,b,d,x,y,xc,qi,qn=z['market'];rho,phi=map(R,theta[-2:])
    mr=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    mi=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
    assert all(S.cancel(t)==0 for t in
      (mr+m*S.eye(3))*S.Matrix([x,x,y])-S.Matrix([1+rho*s,1+rho*s,1]))
    assert all(S.cancel(t)==0 for t in
      (mi+m*S.eye(3))*S.Matrix([qi]*3)-S.Matrix([1+rho*s]*3))
    assert S.cancel((2*m+b)*xc-(1+rho*s))==0
    assert S.cancel(z['n']-(2*m+b)*(1-2*d*xc))==0
    for which,xx,yy,C in (('inside',x,y,z['cs'][0]),
                           ('corner',xc,S.Integer(0),z['cs'][1])):
        P=z[which]
        assert S.cancel(2*P['P']+P['O']+3*C-
          (3*(2*xx+yy+2*rho*s*xx-C)-2*phi*s*s))==0
    P=z['I'];C=z['cs'][2]
    assert S.cancel(3*P['P']+3*C-
       (3*(3*qi+3*rho*s*qi-C)-3*phi*s*s))==0

if __name__=='__main__':
    for vv,expect in [(R(1,10),(False,True,False)),
                      (R(1,5),(False,True,True)),
                      (R(3,10),(False,False,True))]:
        th=(vv,R(1,4),R(3,20),R(3,40),R(1,4),R(5,16))
        audit(th)
        result=(strong(th,'N'),strong(th,'R',R(3,5) if vv==R(1,10) else 1),
                strong(th,'I',1))
        assert result==expect,(vv,result)
        print('PASS original calibrated network',vv,result,flush=True)
    th=(R(0),R(1,4),R(2,5),R(0),R(0),R(1))
    assert strong(th,'N') and not strong(th,'R',1) and not strong(th,'I',1)
    print('PASS NS-only example in full six-parameter domain',flush=True)
    th=(R(3,10),R(3,5),R(0),R(3,5),R(10),R(1,5))
    audit(th);z=data(th)
    assert z['n'].subs(s,0)>0 and z['n'].subs(s,R(1,2))<0
    assert z['n'].subs(s,1)>0
    assert regional_at(z,R(1,2))['O']==0
    assert regional_at(z,1)['O']>0
    print('PASS two outsider corners: exit then reentry at high standard depth',flush=True)
    fake={'I':{'P':R(2,10**60)-s*s,'W':S.Integer(1)}}
    assert beneficial(fake,'I',{'P':0,'W':0})
    print('PASS adversarial near-zero infinitesimal-standard deviation',flush=True)
