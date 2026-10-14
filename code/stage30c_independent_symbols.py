"""Stage30C primitives-first symbolic reconstruction; no Stage30/30B imports."""
from functools import lru_cache
import sympy as s


@lru_cache(maxsize=1)
def objects():
    c, a, eta = s.symbols('c a eta', real=True)
    m, g, v, k, rho, phi = map(s.Rational,
        ['.99', '.14', '.01', '.02', '.32', '.14'])
    b, d, z = g+k*a-v*c, g-eta*a, 1+rho*c
    # Obtain the common quantities by solving the primitive first-order system.
    sx, sy = s.symbols('x y')
    sol = s.solve([s.Eq((2*m+b)*sx+d*sy,z),
                   s.Eq(2*d*sx+2*m*sy,1)], [sx,sy])
    x, y = s.cancel(sol[sx]), s.cancel(sol[sy])
    H = s.Matrix([[m,b,d],[b,m,d],[d,d,m]])
    q = s.Matrix([x,x,y])
    C = s.cancel((q.T*H*q)[0]/2)
    pi = s.cancel(3*m*x*x)
    po = s.cancel(3*m*y*y)
    qi = (1+rho)/(2*(m+g-v))
    piI, csI = 3*m*qi*qi, s.Rational(3,2)*(m+2*(g-v))*qi*qi
    P, WI = piI-phi/2, piI+csI-phi/2
    F = s.cancel(pi-phi*(c*c+a*a)/2)
    B = s.cancel(piI+csI-pi-C-phi*(1-c*c)/2)
    V = s.cancel(WI-po-C)
    T = s.cancel(2*F+po+3*C)
    fields = dict(x=x,y=y,C=C,F=F,B=B,V=V,T=T)
    for name in ['F','T']:
        fields[name+'_a'] = s.cancel(s.diff(fields[name],a))
        fields[name+'_c'] = s.cancel(s.diff(fields[name],c))
    fields['F_aa'] = s.cancel(s.diff(fields['F_a'],a))
    fields['F_ac'] = s.cancel(s.diff(fields['F_a'],c))
    return dict(vars=(c,a,eta),m=m,g=g,v=v,k=k,rho=rho,phi=phi,
                b=b,d=d,z=z,qi=qi,piI=piI,csI=csI,P=P,WI=WI,
                fields=fields)


if __name__ == '__main__':
    from scipy.optimize import brentq, differential_evolution
    ob=objects(); c,a,e=ob['vars']
    fn={n:s.lambdify((c,a,e),v,'numpy') for n,v in ob['fields'].items()}
    for n in ['B','T_a','F_ac']:
        domain=[(0,1),(0,.61),(.10,.14)]
        if n=='F_ac': domain[1]=(.30,.61)
        r=differential_evolution(lambda t:fn[n](*t),domain,
            seed=3061,atol=1e-9,tol=1e-6,popsize=10,maxiter=160)
        print(n,'candidate minimum',r.fun,r.x,'converged',r.success)
        num,den=s.fraction(ob['fields'][n])
        poly=s.Poly(num,c,a,e)
        print('  numerator degrees',poly.degree_list(),'terms',len(poly.terms()))
    for E in [.10,.11,.115,.13,.14]:
        aa=brentq(lambda t:fn['F_a'](1,t,E),.30,.61)
        print('eta',E,'a_star',aa,'V',fn['V'](1,aa,E),
              'F-P',fn['F'](1,aa,E)-float(ob['P']))
    r=differential_evolution(lambda t:-fn['V'](1,t[0],t[1]),
        [(.30,.61),(.10,.14)],seed=3062,atol=1e-9,popsize=10,maxiter=160)
    print('canonical enclosure V max',-r.fun,r.x,'converged',r.success)
