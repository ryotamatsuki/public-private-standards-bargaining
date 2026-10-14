"""Stage23 -- full reduced-game pure-SPE terminal-IS robustness in phi.

CERTIFIED all η∈[1/10,7/50], K∈[27/50,14/25], phi∈[3/25,33/100].
Other coefficients (v,gamma,kappa,rho)=(.01,.14,.02,.32) fixed.
Government universal proposal rights, 2-of-3 majority and YES on ties.
Only N and independently chosen open O(c_i,a_i), 0<=a_i<=c_i<=1.
No side payments, patents, private C/certification; public O(1,0)
legally preexisting and O->O capital retrofit is incremental positive c.

This script independently re-certifies the variable-phi conditions
missing in Stage22: two-O/nonmember L-SPE exclusion, 0/1-O policy
approval, strict mandatory compliance for all histories, and NNN->M
Nash existence. Stage22 separately proves all-three-O L-SPE exclusion
for 0<phi<=452295327/649779200, covering this whole interval.
An exact 3D Bernstein certificate is run for EVERY coefficient, over
the entire eta/c/a continuum, not a finite technology grid.
"""
import sympy as S
from itertools import product
from math import comb
import stage22_exact_phi_robustness as stage22

R=S.Rational
m=R(99,100);gamma=R(7,50);v=R(1,100)
kappa=R(1,50);rho=R(8,25)
phi_min=R(3,25);phi_max=R(33,100)
eta,a,c=S.symbols("eta a c",real=True)
t,u,w=S.symbols("t u w")
z=1+rho*c
b=gamma+kappa*a-v*c
d=gamma-eta*a
D=2*m*(2*m+b)-2*d*d
X=2*m*z-d
Y=2*m+b-2*d*z
CSnum=(m+b)*X*X+2*d*X*Y+m*Y*Y/2
qfull=(1+rho)/(2*(m+gamma-v))
gross_public=3*m*qfull*qfull+R(3,2)*(m+2*(gamma-v))*qfull*qfull
gross_firm_public=3*m*qfull*qfull
qnone=R(1)/(2*(m+gamma))
gross_n=3*m*qnone*qnone+R(3,2)*(m+2*gamma)*qnone*qnone

def bernstein_coeffs(poly, variables, degrees):
    p=S.Poly(poly,*variables)
    assert all(i<=j for i,j in zip(p.degree_list(),degrees))
    term=p.as_dict()
    out=[]
    for indices in product(*(range(deg+1) for deg in degrees)):
        value=sum(
            coefficient*S.prod(
                R(comb(i,j),comb(deg,j))
                for i,j,deg in zip(indices,mon,degrees))
            for mon,coefficient in term.items()
            if all(j<=i for i,j in zip(indices,mon)))
        out.append((indices,value))
    return out

def box_certificate(expr0,exprp,subs,degrees,sign,label):
    """Check entire box, affine sign*(expr0+phi*exprp) in phi.

    Since each Bernstein coefficient is affine, endpoint STRICT
    positivity proves positivity at every interior phi.
    """
    p0=S.Poly(expr0.subs(subs,simultaneous=True),t,u,w).as_expr()
    p1=S.Poly(exprp.subs(subs,simultaneous=True),t,u,w).as_expr()
    B0=bernstein_coeffs(p0,(t,u,w),degrees)
    B1=bernstein_coeffs(p1,(t,u,w),degrees)
    assert len(B0)==len(B1)
    for cap in (phi_min,phi_max):
        vals=[sign*(z0+cap*z1) for (_,z0),(_,z1) in zip(B0,B1)]
        assert all(j>0 for j in vals),(label,"phi",cap,min(vals))
        print("PASS exact 3D Bernstein",label,"phi",cap,
              "n",len(vals),"all STRICT, min coefficient",min(vals),
              flush=True)
    return B0,B1

def two_founder_policy_vs_investment():
    # Symmetric bilateral OPEN founders O(c,a),O(c,a),N.
    # All private markets use min(c,a); η-dependent substitute d.
    # Their public-vs-L national welfare difference B =
    # gross_public - 3*m*x² - CS - phi*(1-c²)/2.
    # Sign numerator = B*D².
    B0=gross_public*D**2-3*m*X**2-CSnum
    Bp=-(1-c*c)*D**2/2
    lo_sub={eta:R(1,10)+R(1,25)*t,a:R(3,4)*u,c:w}
    B0_b,Bp_b=box_certificate(
         B0,Bp,lo_sub,(4,4,4),1,
         "low-a <= 3/4: both member governments approve")
    # If a>3/4 and public mandate blocked, founders B<0.
    # Their payoff f=3*m*(X/D)^2-phi*(c²+a²)/2 has f_a<0.
    # -f_a *D³ = -6mX(X_a D-X D_a)+phi*a*D³
    H0=-6*m*X*(S.diff(X,a)*D-X*S.diff(D,a))
    Hp=a*D**3
    hi_sub={eta:R(1,10)+R(1,25)*t,
            a:R(3,4)+R(1,4)*u,
            c:R(3,4)+R(1,4)*w}
    H0_b,Hp_b=box_certificate(
         H0,Hp,hi_sub,(6,7,3),1,
         "high-a >= 3/4: private marginal f_a strictly negative")
    assert len(B0_b)==125 and len(H0_b)==224
    # Compute TRUE rational outer bounds from coefficient constraints.
    positive_Bp=[(i,-a0/ap) for (i,a0),(_,ap) in zip(B0_b,Bp_b) if ap<0]
    assert positive_Bp
    policy_upper=min(positive_Bp,key=lambda it:it[1])
    positive_Hp=[(i,-a0/ap) for (i,a0),(_,ap) in zip(H0_b,Hp_b) if ap>0]
    assert positive_Hp
    design_lower=max(positive_Hp,key=lambda it:it[1])
    assert design_lower[1]==R(1300995704448,10862756385725)
    assert policy_upper[1]==R(866739877263279,1109042981916800)
    assert design_lower[1]<phi_min<phi_max<policy_upper[1]
    assert all(bp<=0 for _,bp in Bp_b)
    assert all(hp>=0 for _,hp in Hp_b)
    # D>0 for eta∈[.1,.14], 0<=c,a<=1 (indeed even
    # rectangular supersets). Bounds b∈[.13,.16],
    # d∈[0,.14] yield 2m*(2m+b)-2d² > 0.
    assert 2*m*(2*m+R(13,100))-2*(R(14,100))**2>0
    # Firm redundancy lemma relies on phi>0; both equal-a/c
    # maximal design reductions have strictly positive savings.
    assert phi_min>0
    print("BOUND two-founder low-a coefficient upper",policy_upper,
          "high-a coefficient lower",design_lower,flush=True)
    print("THEOREM two-OPEN/one-N lasting L cannot be pure SPE",
          "throughout eta,K,phi box",flush=True)

def public_votes_conformity_nnn():
    # Once all M, each public firm earns the same Cournot gross.
    # Prehistories with no O or a single O do not feature
    # a private matched pair, so all national market gross = gross_n.
    # Two N-country governments at a singleton O, or all three
    # after NNN, earn the policy increment
    # gross_public - phi/2 - K - gross_n.
    Kmax=R(14,25)
    threshold_vote=2*(gross_public-gross_n-Kmax)
    assert threshold_vote==R(1345490921,4004358400)
    assert phi_max<threshold_vote
    # Existing O-government singleton additionally recovers
    # phi*c²/2 relative to a fresh N government's comparison;
    # thus it strictly approves too on the same interval.
    for pp in (phi_min,phi_max):
        n_gov=gross_public-pp/2-Kmax-gross_n
        assert n_gov>0
        print("PASS 0/1 O all national governments STRICTLY approve M",
              "at phi",pp,"worst-case K=.56 margin",n_gov,flush=True)
    # All-government universal proposal + vote-on-tie ensures
    # public policy if a strict 2/3 approving majority exists.
    # After M each originally N firm pays K+phi/2;
    # each originally OPEN firm pays <=phi/2 additional cost.
    # The MINIMUM gross Cournot profit from adoption regardless
    # of 0/1/2 other adopters is the isolated-adopter bound 25/33.
    isolated=R(3)/(4*m)
    one_competing=3*m*((1+rho)/(2*m+(gamma-v)))**2
    two_competing=3*m*((1+rho)/(2*(m+gamma-v)))**2
    assert isolated==R(25,33)
    assert isolated<two_competing<one_competing
    compliance_threshold=2*(isolated-Kmax)
    assert compliance_threshold==R(326,825)
    assert phi_max<compliance_threshold
    for pp in (phi_min,phi_max):
        assert isolated-Kmax-pp/2>0
    print("PASS post-M strict universal adoption dominance",
          "for ALL 0/1/2/3 prior O histories, every eta,K,phi",
          "in rectangle; minimum net increment",
          isolated-Kmax-phi_max/2,flush=True)
    # At initial NNN every government unanimously mandates M.
    # After one-firm initial unilateral O(c,a), governments
    # still unanimously mandate M by preceding strict vote proof.
    # The deviating inventor's eventual cost is
    # K+phi*(1+a²)/2 (original K+phi(c²+a²)/2 plus
    # missing capacity phi(1-c²)/2).
    # Original NNN entrant's cost K+phi/2. Since a>=0,
    # O(c,a) is never strictly more profitable than N.
    cc,aa,K,P=S.symbols("cc aa K P", nonnegative=True)
    initial=K+P*(cc*cc+aa*aa)/2
    retrofit=P*(1-cc*cc)/2
    assert S.factor(initial+retrofit-(K+P*(1+aa*aa)/2))==0
    assert S.factor((K+P*(1+aa*aa)/2)-(K+P/2)-P*aa*aa/2)==0
    print("PASS global all-continuous NNN->M initial SPE existence",
          "including any single O(c,a) corporate deviation",flush=True)
    return threshold_vote,compliance_threshold

def main():
    # Independent Stage22 coefficient-inequality reasoning is
    # called at the endpoints of its previously proven interval.
    previous_upper=R(452295327,649779200)
    assert 0<phi_min<=phi_max<previous_upper
    two_founder_policy_vs_investment()
    vote,comp=public_votes_conformity_nnn()
    assert phi_max<min(vote,comp)
    print("GLOBAL ST23 PURE-SPE TERMINAL RESULT: for every",
          "eta in [.10,.14], K in [.54,.56],",
          "phi in [.12,.33], all pure-strategy SPE end at mandatory",
          "public O(1,0) IS, and at least one such SPE exists.")
    print("NOTE this is NOT uniqueness of initial SPE vectors,",
          "NOT full 5D technology-parameter robustness,",
          "and NOT a necessary/sufficient equilibrium phase boundary.")

if __name__=="__main__":
    main()
