"""SPNE -> reduced-stage-1 strong Nash: exact continuum-depth separation.

Original one-depth NS/RS/IS six-player game, Cournot stage-2 Nash
continuations, exact essential-signature rule. The coalitional
refinement is imposed on STAGE-1 contract announcements only.
Do not claim the entire Cournot subgame is strong Nash.

CI tests exact rational signs, all real roots by Sturm for participation
and ideal-depth frontiers, and independent full-message/coalitional
checks including off-path outsider preannouncements.
"""
import sympy as S
from verify_six_dimensional_corners import (
    s,R,data,regional_at,international_at,strong
)
from verify_pure_spne_complete import (
    SQ,support_profile,nash_message_profile,spne_contract
)

# Same original 4 market coordinates as prior F=.4 theorem:
# v=.2, gamma=.25, kappa=.15, eta=.075, rho=.25,
# phi=f/(a-c0)^2 = F/(1-v)= (.4)/(.8)=.5.
THETA=(R(1,5),R(1,4),R(3,20),R(3,40),R(1,4),R(1,2))

def clean_fraction(expr):
    n,d=S.fraction(S.cancel(expr))
    if d.subs(s,0)<0:n,d=-n,-d
    return S.Poly(n,s),S.Poly(d,s)

def sign_all_open_01(expr,positive=True,positive_at_one=True):
    n,d=clean_fraction(expr)
    assert d.eval(0)>0 and d.eval(1)>0 and d.count_roots(0,1)==0
    # Can vanish at 0: strip all leading powers of s to establish
    # signs on (0,1].
    while n.eval(0)==0:
        n=S.Poly(S.cancel(n.as_expr()/s),s)
    test=n if positive else -n
    assert test.eval(0)>0
    assert test.count_roots(0,1)==0
    if positive_at_one:assert test.eval(1)>0

def unique_irr_root(expr):
    n,d=clean_fraction(expr)
    while n.eval(0)==0:n=S.Poly(S.cancel(n.as_expr()/s),s)
    assert n.count_roots(0,1)==1
    options=[(iv,mul) for iv,mul in n.intervals(eps=R(1,10**12))
             if 0<iv[1] and iv[0]<1]
    assert len(options)==1
    (lo,hi),multiplicity=options[0]
    assert 0<lo<=hi<1 and multiplicity==1
    return lo,hi

def verify():
    Z=data(THETA)
    PR,WR=Z["inside"]["P"],Z["inside"]["W"]
    PI,WI=Z["I"]["P"],Z["I"]["W"]
    PN,WN=Z["N"]["P"],Z["N"]["W"]
    # First audit absence of outsider KKT corners for this complete
    # benchmark depth continuum (not assumed for general theta).
    sign_all_open_01(Z["n"])
    for name,v in (
        ("regional government IR",WR-WN),
        ("international government IR",WI-WN)):
        sign_all_open_01(v)
        print("PROVED",name,"strictly positive for all s>0",flush=True)
    for name,v in (
        ("regional firm SPNE IR cutoff sigma_R",PR-PN),
        ("international firm SPNE IR cutoff sigma_I",PI-PN)):
        lo,hi=unique_irr_root(v)
        assert (v.subs(s,R(1,100))>0 and v.subs(s,1)<0)
        print("EXACT",name,":",lo,"< root <",hi,
              "approx",float((lo+hi)/2),flush=True)
    # Strict concavity, checked by independent exact rational Sturm,
    # is a sufficient hypothesis for the Pareto compromise theorem.
    def strictly_negative(z):
        n,d=clean_fraction(z)
        assert d.eval(0)>0 and d.eval(1)>0 and d.count_roots(0,1)==0
        assert n.eval(0)<0 and n.eval(1)<0 and n.count_roots(0,1)==0
    for label,p in (("PR",PR),("WR",WR),("PI",PI),("WI",WI)):
        strictly_negative(S.diff(p,s,2))
        lo,hi=unique_irr_root(S.diff(p,s))
        assert S.diff(p,s).subs(s,0)>0 and S.diff(p,s).subs(s,1)<0
        print("EXACT",label,"unique best depth",float((lo+hi)/2),flush=True)
    # Positive fee F cannot reverse positive FIRST marginal benefit
    # at zero, thus positive-depth SPNE near zero ALWAYS fail same
    # standard Pareto efficiency / stage-1 strong Nash.
    for kind in ("R","I"):
        for depth,expected_strong in (
            ((R(1,10) if kind=="R" else R(1,10)),False),
            ((R(3,5) if kind=="R" else R(13,20)),True),
            ((R(17,20) if kind=="R" else R(18,25)),False)):
            contract=("R","12",depth) if kind=="R" else ("I","ALL",depth)
            assert spne_contract(Z,contract)
            assert nash_message_profile(Z,support_profile(contract))
            assert strong(THETA,kind,depth,uniform=True)==expected_strong
            print("EXACT",kind,str(depth),"pure SPNE=true",
                  "reduced stage-1 strong Nash="+str(expected_strong),flush=True)
    assert nash_message_profile(Z,support_profile(SQ))
    assert not strong(THETA,"N")
    # Regionally accepted firm and government at depth 0.1 BUT
    # strict two-party depths improve BOTH:
    assert PR.subs(s,R(1,5))>PR.subs(s,R(1,10))
    assert WR.subs(s,R(1,5))>WR.subs(s,R(1,10))
    assert PI.subs(s,R(1,5))>PI.subs(s,R(1,10))
    assert WI.subs(s,R(1,5))>WI.subs(s,R(1,10))
    # Separately confirm the Stage-2 Cournot Nash is NOT generally
    # coalitionally strong: two firms cut output together, all else
    # held fixed, and each increases its own worldwide market profit.
    g=R(5,16);m=S.Integer(1);n=R(1)/(2*(m+g));eps=R(1,100)
    gain=g*n*eps-(m+g)*eps*eps
    assert gain>0
    print("STAGE-2 COURNOT RED TEAM: pairwise firm collusion improves both",
          "delta profit per market",gain,
          "thus NOT a strong Nash equilibrium of full extensive game")
    print("PASS exact reduced stage-1 refinement + baseline IR/Pareto root cells")

if __name__=="__main__":verify()
