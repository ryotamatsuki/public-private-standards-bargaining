"""Stage24 — exact five-parameter public-IS pure-SPE outcome certificate.

Full closed rectangular domain:
 eta in [1/10,7/50], K in [27/50,14/25],
 phi in [13/100,3/10], rho in [319/1000,321/1000],
 kappa in [19/1000,21/1000].
The other primitives are fixed: m=99/100, gamma0=7/50, v=1/100.

All private firms choose N or individual O(c_i,a_i), 0<=a_i<=c_i<=1.
Every government can propose mandatory public O(1,0), simple 2-of-3
majority, YES on policy ties, no transfers. All public O adaptation
pays strictly incremental missing physical c-stock, not duplicate K.
No X/Y patents, licensing or certification. Exact pure-SPE OUTCOMES,
not all possible initial SPE action vectors, are classified.

5D coefficient certificate: for every phi endpoint, directly check
Bernstein bases simultaneously over continuously variable eta/c/a/rho/
kappa. All rational; no coarse grid or floating-point extrapolation.
"""
import sympy as S
from math import comb
from collections import defaultdict
from itertools import product

R=S.Rational
m,g,v=R(99,100),R(7,50),R(1,100)
KLO,KHI=R(27,50),R(14,25)
PLO,PHI=R(13,100),R(3,10)
ELO,EHI=R(1,10),R(7,50)
RLO,RHI=R(319,1000),R(321,1000)
JLO,JHI=R(19,1000),R(21,1000)
r,j=S.symbols("r j")
rho=RLO+(RHI-RLO)*r
kappa=JLO+(JHI-JLO)*j
q0=(1+rho)/(2*(m+g-v))
G0=(3*m+R(3,2)*(m+2*(g-v)))*q0*q0

def tensor_bernstein(expr,vs,label):
    """Separable exact power-to-Bernstein conversion in N dimensions."""
    p=S.Poly(expr,*vs)
    degrees=p.degree_list()
    coefficients=p.as_dict()
    for ax,N in enumerate(degrees):
        groups=defaultdict(list)
        for multi,value in coefficients.items():
            groups[multi[:ax]+multi[ax+1:]].append((multi[ax],value))
        divisors=[R(comb(N,k)) for k in range(N+1)]
        transformed={}
        for key,entries in groups.items():
            base=[S.S.Zero]*(N+1)
            for idx,value in entries:
                base[idx]=value/divisors[idx]
            for idx in range(N+1):
                coef=sum(base[k]*comb(idx,k) for k in range(idx+1))
                if coef:
                    transformed[key[:ax]+(idx,)+key[ax:]]=coef
        coefficients=transformed
    negative=[(key,val) for key,val in coefficients.items() if val<0]
    assert not negative,(label,negative[:2])
    count=S.prod(x+1 for x in degrees)
    zeros=count-len(coefficients)
    print("PASS full rational tensor Bernstein",label,"degree",degrees,
          "coefficients",count,"strict-positive",len(coefficients),
          "zeros",zeros,flush=True)
    return count,zeros

def three_open_certificates(phi):
    """Exhaust feasible three-O no-L-SPE technical-rank topologies."""
    t,s,w,h=S.symbols("t s w h")
    c2=t;c1=t*s;a1=c1*w;d=a1+(c2-a1)*h
    b1=g+kappa*a1-v*c1;b2=g+kappa*d-v*c2
    z1=1+rho*c1;z2=1+rho*c2
    D=2*m*(2*m+b2)-2*b1*b1
    Q1=(2*m+b2)*z1-2*b1*z2
    Q2=2*m*z2-b1*z1
    CSnum=m*Q1**2+2*m*Q2**2+4*b1*Q1*Q2+2*b2*Q2**2
    n=(2*G0-phi*(1-c2*c2))*D**2-6*m*Q2**2-CSnum
    aligned=tensor_bernstein(n,(t,s,w,h,r,j),f"3O aligned G2 phi={phi}")
    assert aligned==(9450,15)
    # q2=q3, c3>=c2, so G3's vote gain >= G2's.
    t,s,u,w=S.symbols("t s u w")
    c1=t*s;c2=t;ah=c1*u;al=ah*w
    p=g+kappa*ah-v*c1
    rr=g+kappa*al-v*c1
    bb=g+kappa*al-v*c2
    z1=1+rho*c1;z2=1+rho*c2
    D=8*m**3+2*p*rr*bb-2*m*(p*p+rr*rr+bb*bb)
    Q1=(4*m*m-bb*bb)*z1+(rr*bb-2*m*p)*z2+(p*bb-2*m*rr)*z2
    Q2=(rr*bb-2*m*p)*z1+(4*m*m-rr*rr)*z2+(p*rr-2*m*bb)*z2
    Q3=(p*bb-2*m*rr)*z1+(p*rr-2*m*bb)*z2+(4*m*m-p*p)*z2
    CSnum=m*(Q1**2+Q2**2+Q3**2)+2*(p*Q1*Q2+rr*Q1*Q3+bb*Q2*Q3)
    result=[]
    for i,(Q,ci) in enumerate(((Q1,c1),(Q2,c2)),1):
        n=(2*G0-phi*(1-ci*ci))*D**2-6*m*Q*Q-CSnum
        result.append(tensor_bernstein(
            n,(t,s,u,w,r,j),f"3O crossed G{i} phi={phi}"))
    assert result==[(59535,105),(52920,105)]
    # Every 3-O private-L-SPE would need at least two firms tied
    # at maximal a (unique max-a wastes sunk cap), and at least
    # two tied at maximal c (unique max-c wasteful if L persists).
    # Sorted c: if smallest c also smallest a, the aligned G2/G3
    # case forces public M. Otherwise crossed G1/G2 forces M.
    # Cost-savings strict because PLO>0; no possibility of L-SPE.
    return aligned,result

def two_open_certificates(phi):
    """Two-O/one-N no-L-SPE: full-real low-a vote / high-a FOC."""
    eta,a,c=S.symbols("eta a c")
    t,u,w=S.symbols("t u w")
    z=1+rho*c
    b=g+kappa*a-v*c
    d=g-eta*a
    D=2*m*(2*m+b)-2*d*d
    X=2*m*z-d
    Y=2*m+b-2*d*z
    CSnum=(m+b)*X*X+2*d*X*Y+m*Y*Y/2
    low=G0*D**2-3*m*X**2-CSnum-phi*(1-c*c)*D**2/2
    subslo={eta:ELO+(EHI-ELO)*t,a:R(3,4)*u,c:w}
    lo=tensor_bernstein(low.subs(subslo,simultaneous=True),
                        (t,u,w,r,j),f"2O low-a member votes M phi={phi}")
    assert lo==(1125,0)
    high=-6*m*X*(S.diff(X,a)*D-X*S.diff(D,a))+phi*a*D**3
    subshi={eta:ELO+(EHI-ELO)*t,
            a:R(3,4)+R(1,4)*u,c:R(3,4)+R(1,4)*w}
    hi=tensor_bernstein(high.subs(subshi,simultaneous=True),
                        (t,u,w,r,j),f"2O high-a -f_a>0 phi={phi}")
    assert hi==(2688,0)
    # If a<=.75, BOTH same-design O governments strictly favor M.
    # For a>.75, either they support M, or f_a<0 and an infinitesimal
    # unilateral reduction in a keeps L and strictly raises profits.
    # Different a/c investors reduce uniquely excessive stock first.
    return lo,hi

def policy_and_implementation():
    """Exact *worst corner*, full parameter interval, strict inequalities."""
    # For nO<=1, baseline no-private-cohort N Cournot is independent of
    # rho,kappa,eta. Public gross national payoff increases in rho.
    qn=1/(2*(m+g))
    GN=(3*m+R(3,2)*(m+2*g))*qn**2
    GImin=G0.subs(r,0)
    gov_margin=S.factor(GImin-GN-KHI-PHI/2)
    assert gov_margin==R(198040669721,12813946880000)>0
    # Previously O singleton investor also gains extra K+phi*c²/2
    # over previously N national government; all 3 vote M.
    # Public O(1,0) has no common a stock: kappa and eta are absent.
    isolated=R(3)/(4*m)
    one=3*m*((1+RLO)/(2*m+(g-v)))**2
    two=3*m*((1+RLO)/(2*(m+g-v)))**2
    assert isolated==R(25,33) and isolated<two<one
    compliance_margin=isolated-KHI-PHI/2
    assert compliance_margin==R(157,3300)>0
    # With prior open investment, conformity has incremental
    # cost <=phi/2; with prior N, the bound K+phi/2 above applies.
    # All adopt public standard as a strictly dominant action.
    # A deviator from NNN to ANY legal O(c,a) still faces M and
    # receives identical Cournot gross, but spends phi*a²/2 extra.
    C,A,P,K=S.symbols("C A P K", nonnegative=True)
    assert S.factor(K+P*(C*C+A*A)/2+P*(1-C*C)/2-
                    (K+P*(1+A*A)/2))==0
    assert PLO>0
    # 3-firm Cournot diagonal dominance and interior activity:
    # any offdiagonal private b_ij lies in [0, .161].
    maximum=g+JHI
    assert maximum==R(161,1000)
    assert 2*m>2*maximum
    # If a candidate q_i were nonpositive, own FOC intercept
    # >=1 cannot be outweighed by two rivals; q_j<=z_max/(2m).
    zmax=1+RHI
    assert 1-2*maximum*zmax/(2*m)>0
    print("PASS government 0/1 O mandate (worst national gain)",
          gov_margin,flush=True)
    print("PASS all prior N/O firm conformity strict (min margin)",
          compliance_margin,flush=True)
    print("PASS initial NNN->M pure-SPE existence,",
          "full real O(c,a) unilateral deviations",flush=True)

def main():
    assert PLO>0
    tally=0
    for pp in (PLO,PHI):
        tally+=sum(x[0] for x in two_open_certificates(pp))
        a,cs=three_open_certificates(pp)
        tally+=a[0]+sum(x[0] for x in cs)
    assert tally==251436,tally
    policy_and_implementation()
    print("ST24.1 EXACT GLOBAL 5-PARAMETER CERTIFICATE SUCCESS:",
          "eta=[.10,.14], K=[.54,.56], phi=[.13,.30],",
          "rho=[.319,.321], kappa=[.019,.021].",
          "At least one pure SPE exists (NNN->M); every",
          "pure-SPE final outcome is mandatory public IS.",
          "This is only for the OPEN/N no-transfer 3-country game.",
          flush=True)

if __name__=="__main__":
    main()
