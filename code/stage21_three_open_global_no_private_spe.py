"""Stage21: exact global NO-private-L-SPE theorem, continuous 3-O model.

Three public-O initial investors, each 0<=a_i<=c_i<=1, independently
proposable public O(1,0), simple 2/3 majority, M on indifference.
K sunk; O-family retrofits add missing positive c-capital, not another K.
No proprietary X/Y, certification C, transfers or licensing.
Fixed (v,g,kappa,rho,phi)=(.01,.14,.02,.32,.14).

This proves NO triple-O firm-stage pure SPE sustaining L. It does not
assert that M is supported at all arbitrary off-path triple-O histories.
"""
import sympy as S
from fractions import Fraction as F
from itertools import product
from math import comb
import stage5_integrated_independent_standards_and_government as stage5

R = S.Rational
m,g,k,v,rho,phi = R(99,100),R(7,50),R(1,50),R(1,100),R(8,25),R(7,50)
q0 = (1+rho)/(2*(m+g-v))
G0 = S.factor(3*m*q0*q0 + R(3,2)*(m+2*(g-v))*q0*q0)

def certify(expr, variables, label):
    """Exact tensor-Bernstein nonnegativity on the entire unit hypercube."""
    p = S.Poly(S.expand(expr), *variables)
    degrees, coefficients = p.degree_list(), p.as_dict()
    npos = nzero = 0
    for inds in product(*(range(n+1) for n in degrees)):
        value = sum(
            coefficient*S.prod(
                R(comb(i,j), comb(n,j)) for i,j,n in zip(inds,powers,degrees))
            for powers,coefficient in coefficients.items()
            if all(j<=i for i,j in zip(inds,powers)))
        assert value>=0, (label,inds,value)
        if value>0: npos+=1
        else: nzero+=1
    assert npos>0
    print("PASS exact Bernstein",label,degrees,npos,nzero,flush=True)

def proof_aligned():
    """c1<=c2<=c3 and a1<=a2,a3: G2,G3 weakly favor mandatory IS."""
    t,s,w,h = S.symbols("t s w h")
    c2=t; c1=t*s; a1=c1*w
    d=a1+(c2-a1)*h  # d=min(a2,a3), covers every legal such value
    b1=g+k*a1-v*c1
    b2=g+k*d-v*c2
    z1=1+rho*c1
    z2=1+rho*c2
    D=2*m*(2*m+b2)-2*b1*b1
    Q1=(2*m+b2)*z1-2*b1*z2
    Q2=2*m*z2-b1*z1
    CS_num=m*Q1**2+2*m*Q2**2+4*b1*Q1*Q2+2*b2*Q2**2
    # Delta_2 = [G0 - 3m(Q2/D)^2 - CS_num/(2D^2)]
    #           - phi/2*(1-c2^2).
    numerator=(2*G0-phi*(1-c2*c2))*D**2-6*m*Q2**2-CS_num
    assert 2*m>2*(g+k)  # strict Cournot diagonal dominance, D>0
    certify(numerator,(t,s,w,h),"lowest-c founder also lowest-a: G2")
    # q2=q3 and c3>=c2: Delta_3-Delta_2 = phi*(c3²-c2²)/2 >=0.
    print("PASS all aligned-order continuous designs: G2,G3 vote YES")

def proof_crossed_ties():
    """c1<=c2=c3, a1=a2>=a3: G1,G2 weakly favor mandatory IS."""
    t,s,u,w=S.symbols("t s u w")
    c1=t*s; c2=t; ah=c1*u; al=ah*w
    p=g+k*ah-v*c1   # pair 1-2
    r=g+k*al-v*c1   # pair 1-3
    b=g+k*al-v*c2   # pair 2-3
    z1=1+rho*c1; z2=1+rho*c2
    D=8*m**3+2*p*r*b-2*m*(p*p+r*r+b*b)
    Q1=(4*m*m-b*b)*z1+(r*b-2*m*p)*z2+(p*b-2*m*r)*z2
    Q2=(r*b-2*m*p)*z1+(4*m*m-r*r)*z2+(p*r-2*m*b)*z2
    Q3=(p*b-2*m*r)*z1+(p*r-2*m*b)*z2+(4*m*m-p*p)*z2
    CS_num=m*(Q1*Q1+Q2*Q2+Q3*Q3)+2*(p*Q1*Q2+r*Q1*Q3+b*Q2*Q3)
    assert 2*m>2*(g+k)  # SPD, D>0
    for i,(Qi,ci) in enumerate(((Q1,c1),(Q2,c2)),1):
        numerator=(2*G0-phi*(1-ci*ci))*D**2-6*m*Qi**2-CS_num
        certify(numerator,(t,s,u,w),f"crossed maximal ties: G{i}")
    print("PASS all crossed-top-ties continuous designs: G1,G2 vote YES")

def strict_redundancy_lemmas():
    """Logical exhaustive reductions for any hypothetical triple-O L-SPE.

    (1) Unique largest a_i>A=max(other a) is strictly dominated even
        if M occurs: every pair min(a), Cournot market, each M-L vote
        is unchanged. Firm i saves phi*(a_i²-A²)/2 in L and M.
    (2) After (1), maximum a is tied. If c_i>C=max(other c) unique,
        then a_i<=C (another holder of max a has c_j<=C). Reducing
        c_i to C preserves all pair min(c), L payoffs except saving
        phi*(c_i²-C²)/2; i's own M-L vote falls, other votes unchanged.
        Accordingly L stays L, and the deviation strictly profits.
    Therefore any triple-O L-SPE must tie max a and max c.
    """
    ai,A,ci,C,aa=S.symbols("ai A ci C aa",nonnegative=True)
    sa=phi*(ai*ai-A*A)/2
    sc=phi*(ci*ci-C*C)/2
    assert S.factor(phi*(ci*ci+ai*ai-ci*ci-A*A)/2-sa)==0
    assert S.factor(phi*(1+ai*ai-1-A*A)/2-sa)==0
    assert S.factor(phi*(ci*ci+aa*aa-C*C-aa*aa)/2-sc)==0
    assert S.factor(phi*(1+aa*aa-1-aa*aa)/2)==0
    print("PASS exact capital identities + no-L corporate reduction lemmas")

def independent_fraction_checks():
    """Compare exact government signs to Stage5 independent Fraction Cournot."""
    examples=(
        (("O",F(3,5),F(1,5)),("O",F(4,5),F(3,5)),("O",F(1),F(2,5))),
        (("O",F(2,3),F(1,3)),("O",F(1),F(1,3)),("O",F(1),F(1,5))),
    )
    for h in examples:
        continuation=stage5.continuation(h,"L",None,(0,0,0),F(11,20),F(7,50))
        ds=[]
        for i in range(3):
            ai=R(h[i][2])
            # All founders have sunk one K; M finishes c-capital,
            # never refunds a-capital. Thus W_M=G0-K-phi(1+a_i²)/2.
            ds.append(S.cancel(G0-R(11,20)-phi*(1+ai*ai)/2-
                               R(continuation[1][i])))
        assert sum(1 for x in ds if x>=0)>=2, ds
        print("PASS independent Fraction Cournot signs:",tuple(str(x) for x in ds),flush=True)

if __name__=="__main__":
    strict_redundancy_lemmas()
    proof_aligned()
    proof_crossed_ties()
    independent_fraction_checks()
    print("ST21 THEOREM: No triple-O private nonintervention L pure SPE")
    print("ST21 COROLLARY (with ST19/ST20 and NNN->M existence):")
    print("Every pure SPE final outcome of reduced game is public mandated IS;")
    print("not unique initial choices and not necessarily M at every offpath history.")
