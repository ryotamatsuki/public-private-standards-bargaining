"""Independent exact Sturm certificate: full-depth RS and IS fee thresholds.

This certifies loss of the two PARTICULAR full-depth outcomes RS(1) and
IS(1), NOT disappearance of all RS/IS standards with endogenous lower s.
All depths in [0,1] checked, not finite sampled grids. Rational algebra.
"""
import sympy as S

s,F=S.symbols("s F",real=True)
Q=S.Rational
G=Q(5,16);Lam=-Q(1,16);Delta=Q(3,32);rho=Q(1,4)
b=G+Lam*s;d=G-Delta*s
dd=2*(2+b)-2*d*d
x=S.cancel((2*(1+rho*s)-d)/dd)
y=S.cancel((2+b-2*d*(1+rho*s))/dd)
q=S.cancel((1+rho*s)/(2*(1+b)))
n=1/(2*(1+G))
csr=S.cancel((1+b)*x*x+2*d*x*y+y*y/2)
csi=S.cancel(Q(3,2)*(1+2*b)*q*q)
csn=Q(3,2)*(1+2*G)*n*n
pR0=S.cancel(3*x*x);pI0=S.cancel(3*q*q)
wR0=S.cancel(pR0+csr);wI0=S.cancel(pI0+csi)
pn=3*n*n;wn=pn+csn
pr=pR0-F*s*s;pi=pI0-F*s*s
wr=wR0-F*s*s;wi=wI0-F*s*s

FR=S.factor(S.diff(wR0,s).subs(s,1)/2)
FI=S.factor(S.diff(wI0,s).subs(s,1)/2)
assert FR==Q(310713952,1042430125)
assert FI==Q(39,128)
assert 0<FR<FI

def exact_nonnegative_on_interval(expr,allow_endpoint_zero=False):
    num,den=S.fraction(S.cancel(expr))
    if den.subs(s,0)<0:num,den=-num,-den
    # Both numerator and denominator have fixed nonzero sign across entire
    # admissible interval. For the numerator, allow exact zero at s=1 only.
    for label,part in (("numer",num),("denom",den)):
        p=S.Poly(part,s)
        assert p.eval(0)>0,(label,"zero",p.eval(0))
        root_count=p.count_roots(0,1)
        if label=="numer" and allow_endpoint_zero and p.eval(1)==0:
            assert root_count==1,(label,root_count)
            quotient=S.cancel(part/(1-s))
            qpoly=S.Poly(quotient,s)
            assert qpoly.eval(0)>0 and qpoly.eval(1)>0
            assert qpoly.count_roots(0,1)==0
        else:
            assert p.eval(1)>0 and root_count==0,(label,root_count)
    return True

# For smaller F, all four full-depth inequalities are WEAKER and both
# IR differences increase, while derivative W'_X(s) also increases:
# prove each at its OWN maximal allowed normalized fee.
for label,expr in (
    ("RS1 blocks ALL IS(t)",pr.subs(s,1)-pi),
    ("RS govt vetoes other RS depths",S.diff(wr,s)),
    ("RS firm IR",pr.subs(s,1)-pn),
    ("RS govt IR",wr.subs(s,1)-wn)
):
    evaluated=S.factor(expr.subs(F,FR))
    if label.endswith("IR"):
        assert evaluated>0
    else:
        exact_nonnegative_on_interval(
           evaluated,allow_endpoint_zero=label.startswith("RS govt"))
    print("PASS RS exact max fee",label)
for label,expr in (
    ("IS1 govt vetoes ALL RS(t)",wi.subs(s,1)-wr),
    ("IS govt vetoes other IS depths",S.diff(wi,s)),
    ("IS firm IR",pi.subs(s,1)-pn),
    ("IS govt IR",wi.subs(s,1)-wn)
):
    evaluated=S.factor(expr.subs(F,FI))
    if label.endswith("IR"):
        assert evaluated>0
    else:
        exact_nonnegative_on_interval(
           evaluated,allow_endpoint_zero=label.startswith("IS govt"))
    print("PASS IS exact max fee",label)
assert S.diff(pR0,s).subs(s,1)/2 < FR
assert S.diff(pI0,s).subs(s,1)/2 < FI
assert S.factor((S.factor(S.diff(pr,s).subs(s,1)))-(2*(S.diff(pR0,s).subs(s,1)/2-F)))==0
assert S.factor((S.factor(S.diff(wr,s).subs(s,1)))-(2*(FR-F)))==0
assert S.factor((S.factor(S.diff(pi,s).subs(s,1)))-(2*(S.diff(pI0,s).subs(s,1)/2-F)))==0
assert S.factor((S.factor(S.diff(wi,s).subs(s,1)))-(2*(FI-F)))==0
print("THEOREM RS(1) robust strong iff 0<F<=FR =",FR, float(FR))
print("THEOREM IS(1) strong iff 0<F<=FI =",FI, float(FI))
print("THEOREM both full-depth contracts coexist iff 0<F<=FR")
print("THEOREM FR<F<=FI only IS(1) among TWO FULL-DEPTH candidates")
print("WARNING lower-depth RS and IS may remain at F>full-depth thresholds")
