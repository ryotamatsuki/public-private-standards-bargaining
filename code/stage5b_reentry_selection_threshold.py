"""Stage 5B: KKT-mediated outsider reentry changes the strong standard type.

For the ORIGINAL 3-country six-exogenous-parameter model, prove one entire
eta parameter interval, with all other primitives and bargaining rights fixed.
All s and eta quantifiers are certified by exact rational Bernstein/Sturm.
These are strong Nash OUTCOMES of the reduced stage-1 announcement game,
not strong Cournot quantities or a unique pure SPNE.
"""
from math import comb
import sympy as S
s,eta=S.symbols("s eta",real=True)
R=S.Rational
v,g,k,r,fee=R(2,5),R(2,5),R(3,20),R(13,2),R(65,4)
m=1-v
b=g+(k-v)*s
d=g-eta*s
z=1+r*s
M=S.Matrix([[m,b,d],[b,m,d],[d,d,m]])
qa=(M+S.diag(m,m,m)).inv()*S.Matrix([z,z,1])
qc=S.Matrix([z/(2*m+b),z/(2*m+b),0])
MI=S.Matrix([[m,b,b],[b,m,b],[b,b,m]])
qi=(MI+S.diag(m,m,m)).inv()*S.Matrix([z,z,z])
MN=S.Matrix([[m,g,g],[g,m,g],[g,g,m]])
qn=(MN+S.diag(m,m,m)).inv()*S.ones(3,1)

def pay(q,mat):
    p=S.cancel(3*m*q[0]**2-fee*s*s)
    return p,S.cancel(p+(q.T*mat*q)[0]/2)

pa,wa=pay(qa,M)
pc,wc=pay(qc,M)
pi,wi=pay(qi,MI)
pn=S.cancel(3*m*qn[0]**2)
wn=S.cancel(pn+(qn.T*MN*qn)[0]/2)
det=2*m*(2*m+b)-2*d*d
Y=S.expand(2*m+b-2*d*z)
assert S.expand(Y-(R(4,5)+(-R(109,20)+2*eta)*s+13*eta*s*s))==0
assert S.factor(qa[2]-Y/det)==0
assert S.factor(qa[0]-(2*m*z-d)/det)==0
assert S.factor(1-2*d*qc[0]-Y/(2*m+b))==0
assert pn==R(9,20) and wn==R(39,40)
# UNIFORM SPD: NS, IS, RS matrices on s in [0,1],
# eta in [1/100,39/100]. Positive substitute effects throughout.
assert all(q>0 for q in (
    m-g,m+2*g,m-(g+k-v),m+2*(g+k-v),
    m*(m+g+k-v)-2*(g-R(1,100))**2))
assert g-R(39,100)>0
assert Y.subs(s,0)>0
assert S.simplify(Y.subs(s,R(1,2)).subs(eta,R(39,100)))<0
assert S.simplify(Y.subs(s,1)-(15*eta-R(93,20)))==0
# Y(1) crosses 0 exactly at eta=31/100, and its middle-s
# value remains negative throughout the admitted eta interval.

def sturm_positive(formula,label):
    n,h=S.fraction(S.cancel(formula))
    if h.subs(s,0)<0: n,h=-n,-h
    for tag,piece in (("num",n),("den",h)):
        p=S.Poly(piece,s)
        assert p.eval(0)>0 and p.eval(1)>0,(label,tag,"endpoint")
        assert p.count_roots(0,1)==0,(label,tag,"roots")
    print("PASS Sturm",label,flush=True)

def bernstein_positive(poly,label):
    """Tensor Bernstein rational certificate on [0,1] x [0.01,0.39]."""
    p=S.Poly(poly,s,eta)
    ns,ne=p.degree(s),p.degree(eta)
    e0,e1=R(1,100),R(39,100)
    coeff=[[R(0) for _ in range(ne+1)] for _ in range(ns+1)]
    for (i,j),value in p.terms():
        for vj in range(j+1):
            coeff[i][vj]+=value*comb(j,vj)*e0**(j-vj)*(e1-e0)**vj
    minimum=None
    for i in range(ns+1):
        for j in range(ne+1):
            c=sum(coeff[ii][jj]*R(comb(i,ii),comb(ns,ii))*
                  R(comb(j,jj),comb(ne,jj))
                  for ii in range(i+1) for jj in range(j+1))
            assert c>0,(label,i,j)
            minimum=c if minimum is None else min(minimum,c)
    print("PASS exact bivariate Bernstein",label,
          "ncoeff",(ns+1)*(ne+1),"min",float(minimum),flush=True)

# Demand matrix SPD ensures det>0 throughout rectangle. Derivative
# rational denominator has factor 10*(-10*det)^3<0; verify exactly,
# then multiply numerator by -1 before Bernstein positivity test.
for label,payoff in (("P_RS_active",pa),("W_RS_active",wa)):
    n,h=S.fraction(S.cancel(S.diff(payoff,s)))
    assert S.simplify(h-10*(-10*det)**3)==0
    bernstein_positive(-n,label)
# Corner functions & IS functions do not depend on eta.
for label,payoff in (("P_RS_corner",pc),("W_RS_corner",wc),
                     ("P_IS",pi),("W_IS",wi)):
    sturm_positive(S.diff(payoff,s),label)

at1=lambda ex:S.cancel(ex.subs(s,1))
p_is,w_is=at1(pi),at1(wi)
assert p_is==R(115,4) and w_is==R(125,2)
assert at1(pc)==R(1415,36) and at1(wc)==R(6745,108)
assert at1(wc)-w_is==-R(5,108)
assert at1(pc)-p_is==R(95,9)>0
assert p_is>pn and w_is>wn
# All eta in interval have strictly P_RS(1)>P_IS(1):
# at s=1, 2mz-d>=43/5 and det<=81/50,
# x_active>=430/81, x_corner=50/9.
assert S.simplify(3*m*(R(430,81))**2-fee-p_is)>0
# Thus RS(1) IR holds (and W_RS>P_RS>WN) and RS is always strong.
assert S.simplify(3*m*(R(430,81))**2-fee-wn)>0
wg=S.factor(at1(wa)-w_is)
F=420000*eta**4-632000*eta**3-55000*eta**2+194840*eta-40007
assert S.simplify(wg+3*F/(40*(2*eta+1)**2*(10*eta-13)**2))==0
assert S.Poly(F,eta).count_roots(R(31,100),R(39,100))==1
assert F.subs(eta,R(31,100))>0 and F.subs(eta,R(39,100))<0
# Certified SIMPLE root: regular comparative-statics hypersurface follows
# from the implicit-function theorem near theta*, since all strong
# depth monotonicity, SPD and IR margins are strict on compact sets.
assert F.subs(eta,R(385,1000))>0 and F.subs(eta,R(386,1000))<0
assert S.Poly(S.diff(F,eta),eta).count_roots(R(385,1000),R(386,1000))==0
assert S.diff(F,eta).subs(eta,R(385,1000))<0
assert S.simplify(wg.subs(eta,R(39,100)))==R(1693455,37482172)>0
assert S.simplify(at1(wa).subs(eta,R(31,100))-at1(wc))==0
# Exactly ONE root eta_c in (0.31,0.39) makes government indifferent.
# For eta<=0.31, RS(1) corner payoff is eta-INDEPENDENT.
# For eta>0.31, outsider reenters at s=1, and actual WA(1)
# follows the active branch. Strict sign changes only at eta_c.
# Strict monotonic all depths => only s=1 may be strong for each type.
# At s=1, private strictly prefers RS and govt:
#     IS when eta<eta_c; RS when eta>eta_c.
# Other RS pairs overlap incumbent country; reduced stage1 strong logic.
print("PASS exact full reduced-stage1 strong outcome correspondence:")
print("eta in [0.01,eta_c] : RS(any pair,1) AND IS(1)")
print("eta in (eta_c,0.39] : RS(any pair,1) ONLY")
print("eta_KKT=31/100; eta_c=",S.nroots(F)[2],flush=True)
print("No new premises, no whole-game strong Nash, Stage6 NO-GO remains.")
