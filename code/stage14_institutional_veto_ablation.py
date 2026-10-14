"""Stage14 exact institutional veto ablation, with no hidden SPE overclaim.

Physical parameters: (v,gamma0,kappa,rho,phi)=(.01,.14,.02,.32,.14)
eta in [.10,.14], K in [.54,.56], and a in [.25,.61].
Stage11 proved a_R*(eta) lies in this entire rectangle.
X and O use SAME market Cournot design; switching costs differ.
Proof: each bivariate rational polynomial (numerator/denominator)
has ALL strictly positive Bernstein coefficients on the FULL
rectangle, not only sampled corners.

What is certified: national government's votes at an observed RS12
history, counterfactual X versus O family, and particular institutional
redundancies. An OPEN RS initial profile is NOT proved an SPE here.
"""
import sympy as S
from math import comb
from itertools import product
R=S.Rational
m,g,v,k,rho,phi=(R(99,100),R(7,50),R(1,100),
                  R(1,50),R(8,25),R(7,50))
eta,a=S.symbols('eta a',real=True)
b=g+k*a-v; d=g-eta*a; z=1+rho
D=2*m*(2*m+b)-2*d*d
x=S.cancel((2*m*z-d)/D)
y=S.cancel((2*m+b-2*d*z)/D)
f=S.cancel(3*m*x*x-phi*(1+a*a)/2)
po=S.cancel(3*m*y*y)
cs=S.cancel((m+b)*x*x+2*d*x*y+m*y*y/2)
q=z/(2*(m+g-v))
WI0=S.cancel(3*m*q*q-phi/2
             +R(3,2)*(m+2*(g-v))*q*q)
KMIN=R(27,50)
gov_outside_veto=S.cancel(po+cs-WI0+KMIN)
gov_X_veto=S.cancel(f+cs-WI0+KMIN+phi*(1+a*a)/2)
gov_O_approval=S.cancel(WI0-phi*a*a/2-f-cs)

def bernstein_positive(expr,name):
    T,U=S.symbols("T U")
    substitute={eta:R(1,10)+R(1,25)*T,
                a:R(1,4)+R(9,25)*U}
    n,d=S.fraction(S.cancel(expr.subs(substitute,
                                         simultaneous=True)))
    if d.subs({T:0,U:0})<0:n,d=-n,-d
    counts=[]
    for pol in (n,d):
        p=S.Poly(pol,T,U); degrees=p.degree_list()
        coef=p.as_dict(); mincoef=None; count=0
        for indices in product(*(range(deg+1) for deg in degrees)):
            value=sum(c*S.prod(R(comb(i,j),comb(N,j))
                           for i,j,N in zip(indices,mon, degrees))
                      for mon,c in coef.items()
                      if all(j<=i for i,j in zip(indices,mon)))
            assert value>0,(name,indices,value)
            mincoef=value if mincoef is None else min(mincoef,value)
            count+=1
        counts.append(count)
    assert counts==[25,25],(name,counts)
    print("PASS EXACT GLOBAL BERNSTEIN",name,
          "coefficients",counts,flush=True)

def theorem():
    bernstein_positive(gov_outside_veto,
       "outsider G3 VETO, independent of private X/O IP ownership")
    bernstein_positive(gov_X_veto,
       "proprietary X incumbent VETO after fresh open implementation")
    bernstein_positive(gov_O_approval,
       "open O incumbent APPROVE (within-O downgrade adds no fee)")
    bernstein_positive(S.diff(po+cs,eta),
       "outsider government W rises DIRECTLY with eta")
    bernstein_positive(S.diff(po+cs,a),
       "outsider government W rises with endogenous design a")
    # For optimally privately chosen a*(eta), a*'(eta)>0 by
    # previous exact concavity/cross-derivative certificate.
    # Consequently outsider's willingness to APPROVE public IS:
    # K < K_veto(eta):=WI0 - (PO+CS_R)(a*(eta),eta)
    # has a STRICTLY DECREASING K_veto curve across eta interval.
    # Thus outside govt always VETOES inside Stage11 coexistence box,
    # even though the separate social W ranking reverses within box.
    print("THEOREM outsider public-vote cutoff",
          "K_veto(eta)=WI0-(PO+CSR)(a*(eta),eta)",
          "strictly DECREASES with eta across [.10,.14]",flush=True)
    a0=R(119,200)   # inside proved Stage11 root isolating bracket
    E0=R(7,50); K=R(11,20)
    winc=S.N((f+cs).subs({a:a0,eta:E0})-K,15)
    wout=S.N((po+cs).subs({a:a0,eta:E0}),15)
    wIS=S.N(WI0-K,15)
    wincX=S.N(WI0-2*K-phi*(1+a0*a0)/2,15)
    wincO=S.N(WI0-K-phi*a0*a0/2,15)
    assert wincX<winc<wincO
    assert wIS<wout
    print("WITNESS eta=.14 K=.55 a=.595",
          "private incumbent",winc,
          "open->public incumbent",wincO,
          "closed->public incumbent",wincX,
          "outsider private",wout,
          "outsider public",wIS,flush=True)
    print("NOTE: removing policy C does NOT affect either onpath",
          "RS(X,X,N)->L or IS(N,N,N)->M outcome; global SPE",
          "conclusion here CONDITIONAL on prior full deviation bounds.")
    print("NOTE: replacing governmental full open design triangle",
          "with singleton O(1,0) also retains the actual onpath",
          "regulatory design; this makes government's endogenous",
          "design depth NON-ESSENTIAL for the existing coexistence.")
    print("IMPORTANT: X->O label ablation is an observed-government",
          "vote comparison; the full initial open RS SPE is UNPROVED.")
if __name__=="__main__":
    theorem()
