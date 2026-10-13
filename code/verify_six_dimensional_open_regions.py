"""Nonempty OPEN six-parameter sufficient cells for all four contract-type regimes.
Strict rational Bernstein coefficient positivity produces finite polynomial-sign
certificates on the ENTIRE continuum s in [0,1], not sampled grid points.
These regions do NOT exhaust the parameter space.
"""
import sympy as S
from math import comb
from verify_six_dimensional_corners import data,s,R

def bpositive(expr):
    n,d=S.fraction(S.cancel(expr))
    if d.subs(s,0)<0:n,d=-n,-d
    def check(poly):
        p=S.Poly(poly,s);degree=p.degree()
        coefs=[sum(p.nth(i)*R(comb(j,i),comb(degree,i))
                   for i in range(j+1))
               for j in range(degree+1)]
        return all(q>0 for q in coefs)
    return check(n) and check(d)

def certificates(theta):
    z=data(theta);reg=z['inside'];intl=z['I'];ns=z['N']
    v,g,k,e,r,phi=map(R,theta)
    m=1-v;delta=k-v
    D0=2*m*(2*m+g)-2*g*g
    D1=2*m*delta+4*g*e
    X0=2*m-g;X1=2*m*r+e
    K=r*(m+g)-delta
    B=X1*D0-X0*D1+2*e*e*X0
    outcomes={'NS_ONLY':K<0 and B<0}
    # Remaining certificates use the fully interior RS equations.
    # Their sufficient region explicitly requires no outsider exit.
    if not bpositive(z['n']):return outcomes
    a=R(3,4)
    outcomes['RS_ONLY']=bool(
        reg['P'].subs(s,a)>ns['P'] and
        reg['W'].subs(s,a)>ns['W'] and
        S.diff(reg['P'],s).subs(s,a)<0 and
        S.diff(reg['W'],s).subs(s,a)>0 and
        bpositive(-S.diff(reg['P'],s,2)) and
        bpositive(-S.diff(reg['W'],s,2)) and
        bpositive(reg['P'].subs(s,a)-intl['P']) and
        bpositive(reg['W'].subs(s,a)-intl['W']))
    outcomes['IS_ONLY']=bool(
        intl['P'].subs(s,1)>ns['P'] and
        intl['W'].subs(s,1)>ns['W'] and
        bpositive(S.diff(intl['W'],s)) and
        bpositive(intl['P'].subs(s,1)-reg['P']) and
        bpositive(intl['P'].subs(s,1)-reg['O']) and
        bpositive(intl['W'].subs(s,1)-reg['W']) and
        bpositive(intl['W'].subs(s,1)-reg['U']))
    outcomes['RS_IS_COEXIST']=bool(
        reg['P'].subs(s,1)>ns['P'] and
        reg['W'].subs(s,1)>ns['W'] and
        intl['P'].subs(s,1)>ns['P'] and
        intl['W'].subs(s,1)>ns['W'] and
        bpositive(S.diff(reg['W'],s)) and
        bpositive(S.diff(intl['W'],s)) and
        bpositive(reg['P'].subs(s,1)-intl['P']) and
        bpositive(intl['W'].subs(s,1)-reg['W']))
    return outcomes

if __name__=='__main__':
    cases=[
      ((R(1,50),R(1,4),R(2,5),R(1,100),R(1,200),R(1,10)),
       'NS_ONLY'),
      ((R(1,10),R(1,4),R(3,20),R(3,40),R(1,4),R(5,16)),
       'RS_ONLY'),
      ((R(3,10),R(1,4),R(3,20),R(3,40),R(1,4),R(5,16)),
       'IS_ONLY'),
      ((R(1,5),R(1,4),R(3,20),R(3,40),R(1,4),R(5,16)),
       'RS_IS_COEXIST')]
    for theta,label in cases:
        result=certificates(theta)
        assert result[label] and all(not v for k,v in result.items()
                                     if k!=label),(label,result)
        print("PROVED nonempty OPEN six-parameter",label,flush=True)
    print("PASS polynomial-certified sufficient open cells for all four classes")
