"""Stage25: exact rational seven-parameter local robustness without 7D explosion.

The original 3-firm/3-government minimal OPEN/N game, all-government
proposal rights, 2/3 majority, YES on ties, no transfers, no X/Y/C,
full continuous c_i,a_i physical triangles, sunk K and positive missing
c capital under public O(1,0), is maintained without modification.

Uniform boxes:
 eta [0.10,0.14], K [0.54,0.56], phi [0.13,0.30],
 rho [0.319,0.321], kappa [0.019,0.021],
 NEW v [0.009999,0.010001], gamma [0.139999,0.140001],
 m = 1-v.

Proof uses Stage24's five-variable tensor Bernstein coefficients
at nominal v=.01, gamma=.14; clearing the positive common
public gross-welfare denominator H²=(m+gamma-v)², all nonzero
baseline Bernstein coefficients are >1/50. Zero coefficients
are precisely boundary public-identical designs; symbolic
parameter-free identities ensure they STAY zero under changes
in v,gamma. A deterministic coefficient-norm derivative bound
<13000 simultaneously bounds v and gamma sensitivity over the
larger [.009,.011] x [.139,.141] domain. By mean value theorem:
|new beta - old beta| <= (dv+dg)/1000000 < 13/1000 <1/50.
Thus all 5D Bernstein coefficients stay nonnegative in the
full v/gamma square, without grid interpolation or full 7D tensors.

Independent strict policy/compliance margin and Cournot KKT bounds
are checked at conservative corners. Entire Stage24 predecessor CI
also runs, but only Stage25 proves the simultaneous NEW variations.
"""
import sympy as S
from collections import defaultdict
from itertools import product
from math import comb
import stage24_five_parameter_full_spe_certificate as st24

R=S.Rational
EPS=R(1,1000000)
V0,G0=R(1,100),R(7,50)
VLOW,VHIGH=V0-EPS,V0+EPS
GLOW,GHIGH=G0-EPS,G0+EPS
H0=R(99,100)+G0-V0
assert H0==R(28,25)

def structural_indices(label,ds):
    if label.startswith("3O aligned"):
        assert ds[:4]==(6,5,4,2)
        return {(6,5,0,0,r,j) for r in range(ds[4]+1) for j in range(ds[5]+1)}
    if label.startswith("3O crossed"):
        assert ds[0:3]==(8,8,6) or ds[0:3]==(8,7,6)
        return {(ds[0],ds[1],0,w,r,j)
                for w in range(ds[3]+1)
                for r in range(ds[4]+1) for j in range(ds[5]+1)}
    return set()

def audited_baseline_bernstein(expr,variables,label):
    """Exact baseline signs, strict margin and ALL zero index identities.

    Stage24 calls this instead of its original tensor converter,
    so Stage24's case decomposition and all counts/asserts are used
    without editing the preceding proof script.
    """
    # Multiplication by H0² clears the public payoff denominator
    # after v,gamma become variables; at nominal values H0 is fixed.
    lift=H0**2 if label.startswith(("2O low","3O ")) else S.S.One
    poly=S.Poly(S.expand(expr*lift),*variables)
    ds=poly.degree_list()
    terms=poly.as_dict()
    for axis,N in enumerate(ds):
        groups=defaultdict(list)
        for power,value in terms.items():
            groups[power[:axis]+power[axis+1:]].append((power[axis],value))
        nxt={}
        d=[S.Integer(comb(N,k)) for k in range(N+1)]
        for key, entries in groups.items():
            a=[S.S.Zero]*(N+1)
            for ix,val in entries:a[ix]=val/d[ix]
            for ix in range(N+1):
                b=sum(a[k]*comb(ix,k) for k in range(ix+1))
                if b:
                    nxt[key[:axis]+(ix,)+key[axis:]]=b
        terms=nxt
    expected=structural_indices(label,ds)
    assert all(x>R(1,50) for x in terms.values()),(label,min(terms.values()))
    full=S.prod(z+1 for z in ds)
    assert full-len(terms)==len(expected)
    assert all(idx not in terms for idx in expected)
    print("PASS Stage25 baseline exact lifted coefficients",label,
          "N",full,"zeros",len(expected),
          "smallest positive >",R(1,50),flush=True)
    return int(full),len(expected)

def symbolic_structural_zero_audit():
    """The ONLY zero coefficient faces are IDENTICAL public technology.

    At such faces the public and private Cournot matrices and c-stocks
    are identical regardless of v,gamma,rho,kappa. This verifies
    algebraic identities with INDEPENDENT symbolic V and Gamma.
    """
    V,G,RR,JJ,PP=S.symbols("V G RR JJ PP")
    m=1-V;H=m+G-V
    publichat=(3*m+R(3,2)*(m+2*(G-V)))*(1+RR)**2/4
    t,s,w,h=S.symbols("t s w h")
    c2=t;c1=t*s;a1=c1*w;d=a1+(c2-a1)*h
    b1=G+JJ*a1-V*c1;b2=G+JJ*d-V*c2
    z1=1+RR*c1;z2=1+RR*c2
    D=2*m*(2*m+b2)-2*b1*b1
    Q1=(2*m+b2)*z1-2*b1*z2;Q2=2*m*z2-b1*z1
    CS=m*Q1**2+2*m*Q2**2+4*b1*Q1*Q2+2*b2*Q2**2
    n=(2*publichat-PP*(1-c2*c2)*H**2)*D**2-(6*m*Q2**2+CS)*H**2
    assert S.factor(n.subs({t:1,s:1,w:0,h:0}))==0
    t,s,u,w=S.symbols("t s u w")
    c1=t*s;c2=t;ah=c1*u;al=ah*w
    p=G+JJ*ah-V*c1;r=G+JJ*al-V*c1;b=G+JJ*al-V*c2
    z1=1+RR*c1;z2=1+RR*c2
    D=8*m**3+2*p*r*b-2*m*(p*p+r*r+b*b)
    Q1=(4*m*m-b*b)*z1+(r*b-2*m*p)*z2+(p*b-2*m*r)*z2
    Q2=(r*b-2*m*p)*z1+(4*m*m-r*r)*z2+(p*r-2*m*b)*z2
    Q3=(p*b-2*m*r)*z1+(p*r-2*m*b)*z2+(4*m*m-p*p)*z2
    CS=m*(Q1*Q1+Q2*Q2+Q3*Q3)+2*(p*Q1*Q2+r*Q1*Q3+b*Q2*Q3)
    for Q,ci in ((Q1,c1),(Q2,c2)):
        n=(2*publichat-PP*(1-ci*ci)*H**2)*D**2-(6*m*Q**2+CS)*H**2
        assert S.factor(n.subs({t:1,s:1,u:0}))==0
    print("PASS symbolic identically-zero boundary coefficients for",
          "ALL v,gamma,rho,kappa,phi",flush=True)

class Bound:
    """Conservative coefficient l1 norm + 2 partial-derivative l1 norms.

    The coefficients are polynomials in FIVE normalized original
    unit-cube variables. All norms are exact nonnegative rationals.
    Partial derivatives are wrt unnormalized v and gamma.
    """
    def __init__(self,n,dv=0,dg=0):
        self.n,self.dv,self.dg=map(R,(n,dv,dg))
        assert min(self.n,self.dv,self.dg)>=0
    def __add__(self,x):
        if not isinstance(x,Bound):x=Bound(abs(x))
        return Bound(self.n+x.n,self.dv+x.dv,self.dg+x.dg)
    __radd__=__add__
    def __sub__(self,x):return self+x
    def __rsub__(self,x):return self+x
    def __neg__(self):return self
    def __mul__(self,x):
        if not isinstance(x,Bound):x=Bound(abs(x))
        return Bound(self.n*x.n,
                     self.dv*x.n+self.n*x.dv,
                     self.dg*x.n+self.n*x.dg)
    __rmul__=__mul__
    def __truediv__(self,x):
        assert isinstance(x,(int,S.Rational)) and x!=0
        return self*R(1,abs(x))
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        q=Bound(1)
        for _ in range(n):q=q*self
        return q

def derivative_norm_bounds():
    # N(v)<=.011,N(gamma)<=.141 over WIDER domain, giving
    # conservative algebraic rather than pointwise derivative bounds.
    one=Bound(1);z=Bound(1)
    v=Bound(R(11,1000),1,0)
    g=Bound(R(141,1000),0,1)
    m=one-v
    rho=Bound(R(321,1000))
    kappa=Bound(R(21,1000))
    eta=Bound(R(14,100))
    phi=Bound(R(3,10))
    H=m+g-v
    publichat=(3*m+R(3,2)*(m+2*(g-v)))*(one+rho)**2/4
    c=z;a=z;w=z
    b=g+kappa*a-v*c;d=g-eta*a;inter=one+rho*c
    D=2*m*(2*m+b)-2*d*d
    X=2*m*inter-d;Y=2*m+b-2*d*inter
    CS=(m+b)*X**2+2*d*X*Y+m*Y**2/2
    low=publichat*D**2-(3*m*X**2+CS)*H**2-phi*(one-c*c)*D**2*H**2/2
    Xa=eta;Da=2*m*kappa+4*eta*d
    high=-6*m*X*(Xa*D-X*Da)+phi*a*D**3
    c2=z;c1=z*z;a1=c1*z;d=a1+(c2-a1)*z
    b1=g+kappa*a1-v*c1;b2=g+kappa*d-v*c2
    z1=one+rho*c1;z2=one+rho*c2
    D=2*m*(2*m+b2)-2*b1*b1
    Q1=(2*m+b2)*z1-2*b1*z2;Q2=2*m*z2-b1*z1
    CS=m*Q1**2+2*m*Q2**2+4*b1*Q1*Q2+2*b2*Q2**2
    aligned=(2*publichat-phi*(one-c2*c2)*H**2)*D**2-(6*m*Q2**2+CS)*H**2
    c1=z*z;c2=z;ah=c1*z;al=ah*z
    p=g+kappa*ah-v*c1;rr=g+kappa*al-v*c1;b=g+kappa*al-v*c2
    z1=one+rho*c1;z2=one+rho*c2
    D=8*m**3+2*p*rr*b-2*m*(p*p+rr*rr+b*b)
    Q1=(4*m*m-b*b)*z1+(rr*b-2*m*p)*z2+(p*b-2*m*rr)*z2
    Q2=(rr*b-2*m*p)*z1+(4*m*m-rr*rr)*z2+(p*rr-2*m*b)*z2
    Q3=(p*b-2*m*rr)*z1+(p*rr-2*m*b)*z2+(4*m*m-p*p)*z2
    CS=m*(Q1**2+Q2**2+Q3**2)+2*(p*Q1*Q2+rr*Q1*Q3+b*Q2*Q3)
    cross1=(2*publichat-phi*(one-c1*c1)*H**2)*D**2-(6*m*Q1**2+CS)*H**2
    cross2=(2*publichat-phi*(one-c2*c2)*H**2)*D**2-(6*m*Q2**2+CS)*H**2
    items={"2O-low":low,"2O-high":high,"3O-aligned":aligned,
           "3O-cross1":cross1,"3O-cross2":cross2}
    for name,p in items.items():
        L=p.dv+p.dg
        assert L<13000,(name,L)
        assert EPS*L<R(1,50),(name,EPS*L)
        print("PASS exact 7D perturbation derivative norm",name,
              "dv",p.dv,"dg",p.dg,"coefficient change <",
              EPS*L,flush=True)
    # For ANY unit-cube Bernstein coefficient: |beta(partial P)|
    # <= ||partial P||_(power-coeff-l1) since monomial Bernstein
    # basis coefficients C(i,j)/C(N,j) lie in [0,1].
    # Integrating v and gamma along coordinate segments yields
    # |beta(v,g)-beta(v0,g0)|<=EPS*(dv+dg)<.013<.02.
    # The zero coefficients remain exactly zero by symbolic identity.

def policy_adoption_and_existence():
    # Use WIDER v/g ranges ±.0001 to get conservative exact rational
    # interval bounds that hold a fortiori for ±.000001.
    vl,vh=R(99,10000),R(101,10000)
    gl,gh=R(1399,10000),R(1401,10000)
    ml,mh=1-vh,1-vl
    rmin=R(319,1000);phimax=R(3,10);Kmax=R(14,25)
    # G_I = [4.5m+3(g-v)](1+rho)²/[4(m+g-v)²].
    # G_N = [4.5m+3g]/[4(m+g)²].
    GIlo=(R(9,2)*ml+3*(gl-vh))*(1+rmin)**2/(4*(mh+gh-vl)**2)
    GNhi=(R(9,2)*mh+3*gh)/(4*(ml+gl)**2)
    vote=GIlo-GNhi-Kmax-phimax/2
    assert vote==R(4879717257586623,356007624297600800)>0
    # Conformer's operating gross under 0/1/2 compliant peers
    # bounded below; isolated founder is always lowest here.
    isolated=3/(4*mh)
    two=3*ml*(1+rmin)**2/(4*(mh+gh-vl)**2)
    one=3*ml*(1+rmin)**2/(2*mh+gh-vl)**2
    assert isolated<min(one,two)
    compliance=isolated-Kmax-phimax/2
    assert compliance==R(47029,990100)>0
    # Cournot all-active KKT and strict diagonal dominance even
    # after varying v/g; offdiagonal at most gamma_max+kappa_max.
    crossmax=gh+R(21,1000)
    zmax=1+R(321,1000)
    assert 2*ml>2*crossmax
    assert 1-2*crossmax*zmax/(2*ml)>0
    # At NNN a unilateral private investor faces singleton M and
    # spends K+phi(1+a²)/2 instead of K+phi/2 (all other
    # Cournot outcomes coincide). Difference phi*a²/2 >=0.
    cc,aa,pp,KK=S.symbols("cc aa pp KK")
    assert S.factor(KK+pp*(cc*cc+aa*aa)/2+pp*(1-cc*cc)/2-
                    (KK+pp*(1+aa*aa)/2))==0
    print("PASS exact 7D uniform national policy margin >",vote,
          "and conformity margin >",compliance,flush=True)

def main():
    symbolic_structural_zero_audit()
    old=st24.tensor_bernstein
    try:
        st24.tensor_bernstein=audited_baseline_bernstein
        st24.main()
    finally:
        st24.tensor_bernstein=old
    derivative_norm_bounds()
    policy_adoption_and_existence()
    print("THEOREM ST25.1: unique final pure-SPE outcome public IS",
          "on 7D product rectangle [eta .10,.14; K .54,.56;",
          "phi .13,.30; rho .319,.321; kappa .019,.021;",
          "v .009999,.010001; gamma .139999,.140001].",
          "No claim these certificate limits are economic cutoffs.",
          flush=True)

if __name__=="__main__":
    main()
