"""Stage 22. Exact rational coefficient-robustness of Stage21's 3-O exclusion.

Only the 3-O no-L-SPE part (including strict public-M conformity by all 3 prior OPEN investors) is extended in phi; DO NOT infer that
Stage19's 2-O exclusions or public M conformity survive on this full
interval without additional independent certification.

For all phi>0 below the certified upper threshold, the corporate
unique-maximum a and (conditional on L) c cost-savings are strictly
profitable. The two remaining possible tied-max cases have 5,985
nonnegative tensor-Bernstein coefficients for EVERY phi in the bound.
All operations are rational. The 0 phi endpoint itself is EXCLUDED
from the L-SPE theorem (cost-savings are no longer strict).
"""
import sympy as S
from math import comb
from itertools import product

R = S.Rational
m,g,k,v,rho = R(99,100),R(7,50),R(1,50),R(1,100),R(8,25)
q0=(1+rho)/(2*(m+g-v))
G0=S.factor(3*m*q0**2+R(3,2)*(m+2*(g-v))*q0**2)

def bernstein_affine(base, factor, vs, label):
    """Exact N(phi)=base-phi*factor Bernstein coefficient bounds."""
    pb=S.Poly(S.expand(base),*vs)
    pf=S.Poly(S.expand(factor),*vs)
    degrees=tuple(max(a,b) for a,b in zip(pb.degree_list(),pf.degree_list()))
    bc,fc=pb.as_dict(),pf.as_dict()
    lo=R(0);hi=None;structural_zero=0;count=0
    for inds in product(*(range(n+1) for n in degrees)):
        def cv(coefficients):
            return sum(val*S.prod(R(comb(i,j),comb(n,j))
                        for i,j,n in zip(inds,powers,degrees))
                        for powers,val in coefficients.items()
                        if all(j<=i for i,j in zip(inds,powers)))
        b=cv(bc);f=cv(fc);count+=1
        if f>0:
            threshold=b/f
            if hi is None or threshold<hi: hi=threshold
        elif f<0:
            threshold=b/f
            if threshold>lo:lo=threshold
        elif b==0:structural_zero+=1
        else:assert b>0,(label,inds,b)
    assert lo<R(7,50)<hi,(label,lo,hi)
    assert count>0
    print("PASS exact coefficient range:",label,
          "degrees",degrees,"coefficients",count,
          "phi_lower",lo,"phi_upper",hi,
          "structural zeros",structural_zero,flush=True)
    return lo,hi,count,structural_zero

def aligned():
    t,s,w,h=S.symbols("t s w h")
    c2=t;c1=t*s;a1=c1*w;d=a1+(c2-a1)*h
    b1=g+k*a1-v*c1;b2=g+k*d-v*c2
    z1=1+rho*c1;z2=1+rho*c2
    D=2*m*(2*m+b2)-2*b1*b1
    Q1=(2*m+b2)*z1-2*b1*z2;Q2=2*m*z2-b1*z1
    CSnum=m*Q1**2+2*m*Q2**2+4*b1*Q1*Q2+2*b2*Q2**2
    return bernstein_affine(2*G0*D**2-6*m*Q2**2-CSnum,
                            (1-c2*c2)*D**2,(t,s,w,h),"aligned G2")

def crossed():
    t,s,u,w=S.symbols("t s u w")
    c1=t*s;c2=t;ah=c1*u;al=ah*w
    p=g+k*ah-v*c1;r=g+k*al-v*c1;b=g+k*al-v*c2
    z1=1+rho*c1;z2=1+rho*c2
    D=8*m**3+2*p*r*b-2*m*(p*p+r*r+b*b)
    Q1=(4*m*m-b*b)*z1+(r*b-2*m*p)*z2+(p*b-2*m*r)*z2
    Q2=(r*b-2*m*p)*z1+(4*m*m-r*r)*z2+(p*r-2*m*b)*z2
    Q3=(p*b-2*m*r)*z1+(p*r-2*m*b)*z2+(4*m*m-p*p)*z2
    CSnum=m*(Q1*Q1+Q2*Q2+Q3*Q3)+2*(p*Q1*Q2+r*Q1*Q3+b*Q2*Q3)
    return [bernstein_affine(2*G0*D**2-6*m*Q**2-CSnum,
                             (1-ci*ci)*D**2,(t,s,u,w),f"crossed G{i}")
            for i,(Q,ci) in enumerate(((Q1,c1),(Q2,c2)),1)]

if __name__=="__main__":
    results=[aligned()]+crossed()
    assert tuple(z[2] for z in results)==(630,2835,2520)
    assert tuple(z[3] for z in results)==(1,5,5)
    lo=max(x[0] for x in results);hi=min(x[1] for x in results)
    assert lo==0 and hi==R(452295327,649779200),(lo,hi)
    assert sum(x[2] for x in results)==5985
    # In an ALL-OPEN history, fixed family setup K is SUNK.
    # Post-M individual mandatory conformity incurs at most phi/2.
    # Against 0/1/2 other complying firms, minimum operating gross
    # profit is isolated one-firm G1=3/(4m)=25/33, not net of sunk K.
    # The other two gross profit cases are strictly higher.
    gross_one=3/(4*m)
    gross_two=3*m*((1+rho)/(2*m+(g-v)))**2
    gross_three=3*m*((1+rho)/(2*(m+g-v)))**2
    assert gross_one<gross_three<gross_two
    assert hi/2<gross_one
    print("PASS public M all three OLD-O investors strictly comply",
          "for EVERY phi <= certified upper bound; minimum net",
          "incremental profit margin",gross_one-hi/2,flush=True)
    print("THEOREM Stage21 3-O L pure-SPE exclusion certified",
          "for 0 < phi <=",hi,"=",float(hi),flush=True)
    print("LIMIT: no global-policy/all-investment-count extension",
          "has been certified over this phi interval.",flush=True)
